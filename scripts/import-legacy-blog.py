"""Rebuild public blog data from the ignored, saved WordPress snapshots.
Run only when outputs/launch-2026-11-02/source and blog-migration/asset-map.json exist.
Does not execute WordPress code, copy private backup data, or invent attribution.
"""
from html.parser import HTMLParser
from html import escape, unescape
from pathlib import Path
from urllib.parse import urlparse
import json, re, xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'outputs/launch-2026-11-02/source'
EVIDENCE = ROOT / 'outputs/launch-2026-11-02/blog-migration'
ASSETS = json.loads((EVIDENCE / 'asset-map.json').read_text())
ADJUSTMENTS = json.loads((ROOT / 'src/data/blog-migration-adjustments.json').read_text())
class Node:
    def __init__(self, tag='', attrs=(), parent=None):
        self.tag, self.attrs, self.parent, self.children = tag, dict(attrs), parent, []
    def walk(self):
        yield self
        for child in self.children:
            if isinstance(child, Node): yield from child.walk()
    def text(self):
        return ''.join(child.text() if isinstance(child, Node) else child for child in self.children)
class Parser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True); self.root=Node(); self.current=self.root
    def handle_starttag(self, tag, attrs):
        node=Node(tag, attrs, self.current); self.current.children.append(node)
        if tag not in {'area','base','br','col','embed','hr','img','input','link','meta','param','source','track','wbr'}: self.current=node
    def handle_endtag(self, tag):
        node=self.current
        while node.parent:
            if node.tag==tag: self.current=node.parent; break
            node=node.parent
    def handle_startendtag(self,tag,attrs): self.handle_starttag(tag,attrs);self.handle_endtag(tag)
    def handle_data(self, data): self.current.children.append(data)
def parse(text):
    parser=Parser(); parser.feed(text); return parser.root

BUILDER_SHORTCODE = re.compile(r'\[/?fusion_(?:builder_container|builder_row|builder_column|text)\b[^\]]*\]')
def without_builder_markup(text): return BUILDER_SHORTCODE.sub('', text)
def normalized(text): return ' '.join(text.split())
def meta(root,name):
    return next((n.attrs.get('content','') for n in root.walk() if n.tag=='meta' and n.attrs.get('name')==name),'')
def sitemap(name):
    return [n.find('{*}loc').text for n in ET.parse(SOURCE/name).getroot() if n.tag.endswith('url')]
def load_path(path): return parse((SOURCE/'pages'/((path.strip('/').replace('/','--') or 'home')+'.html')).read_text())
ALIASES={
    '/services/preventive-dentistry/':'/services/preventative-dentistry/',
    '/services/childhood/':'/services/pediatric-dentist-milwaukee/',
    '/services/clear-aligner-therapy/':'/services/clear-aligner-therapy-milwaukee/',
    '/services/implants/':'/services/dental-implants-milwaukee/',
}
changes=[]; missing_images=[]; heading_changes=[]
def href_value(href):
    parsed=urlparse(href)
    if parsed.hostname in {'www.midtowndentalcare.org','midtowndentalcare.org'}:
        href=parsed.path or '/'
        if parsed.query: href+='?'+parsed.query
        if parsed.fragment: href+='#'+parsed.fragment
    replacement=ALIASES.get(href,href)
    if replacement!=href: changes.append({'from':href,'to':replacement})
    return replacement

def serialize(node,slug):
    if isinstance(node,str):return escape(without_builder_markup(node))
    tag=node.tag
    if tag in {'script','style','form','input','button','svg','noscript'}:return ''
    if tag=='img':
        url=node.attrs.get('src',''); image=ASSETS.get(url)
        if not image:missing_images.append({'post':slug,'url':url});return ''
        alt=node.attrs.get('alt','')
        return f'<img src="{image["src"]}" width="{image["width"]}" height="{image["height"]}" alt="{escape(alt,quote=True)}" loading="lazy" decoding="async" />'
    if tag=='iframe':
        url=node.attrs.get('src','')
        return f'<p><a href="{escape(url,quote=True)}" target="_blank" rel="noopener noreferrer">Watch the original video</a></p>' if url.startswith('https://') else ''
    inner=''.join(serialize(c,slug) for c in node.children)
    if tag=='h1':heading_changes.append(slug);tag='h2'
    if tag not in {'p','h2','h3','h4','h5','h6','ul','ol','li','strong','em','b','i','a','br','hr','table','thead','tbody','tr','th','td','blockquote','figure','figcaption','sup','sub'}:return inner
    attrs=''
    if node.attrs.get('id'):attrs+=' id="'+escape(node.attrs['id'],quote=True)+'"'
    if tag=='a':
        href=href_value(node.attrs.get('href',''))
        if not href or not href.startswith(('/','#','http:','https:','tel:','mailto:')):return inner
        attrs+=' href="'+escape(href,quote=True)+'"'
        if href.startswith(('https://','http://')):attrs+=' target="_blank" rel="noopener noreferrer"'
    if tag in {'th','td'}:
        for key in ['colspan','rowspan']:
            value=node.attrs.get(key,'')
            if value.isdigit():attrs+=f' {key}="{value}"'
    if tag=='ol' and node.attrs.get('start','').isdigit():attrs+=f' start="{node.attrs["start"]}"'
    return f'<{tag}{attrs}>'+inner+(f'</{tag}>' if tag not in {'br','hr'} else '')

posts=[];text_checks=[]
for url in sitemap('post-sitemap.xml'):
    path=urlparse(url).path.strip('/')
    if path=='blog':continue
    root=load_path(path)
    container=next(n for n in root.walk() if n.attrs.get('data-elementor-type')=='single-post')
    body=next(n for n in container.walk() if n.attrs.get('data-widget_type')=='theme-post-content.default')
    title_node=next(n for n in container.walk() if n.attrs.get('data-widget_type')=='theme-post-title.default')
    feature=next((n for n in container.walk() if n.attrs.get('data-widget_type')=='theme-post-featured-image.default'),None)
    image_node=next((n for n in feature.walk() if n.tag=='img'),None) if feature else None
    image=ASSETS.get(image_node.attrs.get('src','')) if image_node else None
    graph=[]
    for n in root.walk():
        if n.tag=='script' and n.attrs.get('type')=='application/ld+json':
            graph.extend(json.loads(n.text()).get('@graph',[]))
    article=next(n for n in graph if n.get('@type') in ['Article','BlogPosting'])
    title=normalized(title_node.text());html=serialize(body,path)
    before=normalized(without_builder_markup(body.text()));after=normalized(parse(html).text())
    # The only added body words are the link replacing a legacy video embed.
    text_checks.append({'path':path,'text_preserved':normalized(after.replace('Watch the original video',''))==before,'source_characters':len(before)})
    assert text_checks[-1]['text_preserved'], path
    description=unescape(meta(root,'description')) or before[:180].rsplit(' ',1)[0]+'…'
    classes=container.attrs.get('class','').split()
    posts.append({'path':path,'title':normalized(next(n for n in root.walk() if n.tag=='title').text()),'heading':title,'description':description,'excerpt':before[:185].rsplit(' ',1)[0]+('…' if len(before)>185 else ''),'published':article['datePublished'],'modified':article.get('dateModified',article['datePublished']),'publishingCredit':meta(root,'author'),'html':html,'image':({**image,'alt':image_node.attrs.get('alt','')} if image else None),'categories':[c.removeprefix('category-') for c in classes if c.startswith('category-')],'tags':[c.removeprefix('tag-') for c in classes if c.startswith('tag-')],'source':url})
posts.sort(key=lambda p:p['published'],reverse=True)
source_posts = posts[:]
source_post_count = len(posts)
redirected_posts = ADJUSTMENTS['redirectedPosts']
posts = [post for post in posts if post['path'] not in redirected_posts]
for post in posts:
    if post['path'] in ADJUSTMENTS['coverImages']:
        post['image'] = ADJUSTMENTS['coverImages'][post['path']]
archives=[{'path':'blog','title':'Patient Education','type':'all','posts':[p['path'] for p in posts]}]
redirected_archives = []
for kind, filename, field in [('category','category-sitemap.xml','categories'),('tag','post_tag-sitemap.xml','tags')]:
    for url in sitemap(filename):
        path=urlparse(url).path.strip('/');slug=path.split('/')[-1];r=load_path(path)
        title=normalized(next(n for n in r.walk() if n.tag=='title').text())
        label=re.split(r'\s+(?:Archives|\||—|–| - )',title,maxsplit=1)[0]
        matches=[p['path'] for p in posts if slug in p[field]]
        if not matches:
            # The duplicate cosmetic post was the sole entry in six archives.
            original_matches = {p['path'] for p in source_posts if slug in p[field]}
            assert original_matches and original_matches <= set(redirected_posts), path
            redirected_archives.append(path)
            continue
        archives.append({'path':path,'title':label,'type':kind,'posts':matches})
(ROOT/'src/data/blog-posts.json').write_text(json.dumps(posts,ensure_ascii=False,indent=2)+'\n')
(ROOT/'src/data/blog-archives.json').write_text(json.dumps(archives,ensure_ascii=False,indent=2)+'\n')
(EVIDENCE/'import-verification.json').write_text(json.dumps({'source_posts':source_post_count,'posts':len(posts),'archives':len(archives),'redirected_posts':redirected_posts,'redirected_archives':redirected_archives,'cover_replacements':ADJUSTMENTS['coverImages'],'text_checks':text_checks,'internal_link_repairs':changes,'body_heading_demotions':heading_changes,'missing_body_images':missing_images,'posts_without_feature_image':[p['path'] for p in posts if not p['image']]},indent=2))
print(json.dumps({'source_posts':source_post_count,'posts':len(posts),'archives':len(archives),'redirected_posts':redirected_posts,'redirected_archives':redirected_archives,'body_text_preserved':all(c['text_preserved'] for c in text_checks),'missing_body_images':missing_images},indent=2))
