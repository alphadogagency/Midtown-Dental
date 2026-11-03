"""Verify restored article text, routes, links, images and attribution in the build."""
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urlparse,unquote
import json
ROOT=Path(__file__).resolve().parents[1]
posts=json.loads((ROOT/'src/data/blog-posts.json').read_text());archives=json.loads((ROOT/'src/data/blog-archives.json').read_text())
class Document(HTMLParser):
 def __init__(self):super().__init__();self.h1=0;self.links=[];self.images=[];self.scripts=[];self.script=False;self.buf='';self.copy_depth=0;self.copy=[];self.ids=set();self.robots=[]
 def handle_starttag(self,t,attrs):
  a=dict(attrs)
  if t=='h1':self.h1+=1
  if t=='a':self.links.append(a.get('href',''))
  if t=='img':self.images.append(a.get('src',''))
  if a.get('id'):self.ids.add(a['id'])
  if t=='div' and ('blog-copy' in a.get('class','') or self.copy_depth):self.copy_depth+=1
  if t=='script' and a.get('type')=='application/ld+json':self.script=True;self.buf=''
  if t=='meta' and a.get('name')=='robots':self.robots.append(a.get('content'))
 def handle_endtag(self,t):
  if t=='div' and self.copy_depth:self.copy_depth-=1
  if t=='script' and self.script:self.script=False;self.scripts.append(json.loads(self.buf))
 def handle_data(self,s):
  if self.script:self.buf+=s
  if self.copy_depth:self.copy.append(s)
def plain(s):
 class Text(HTMLParser):
  def __init__(self):super().__init__();self.parts=[]
  def handle_data(self,s):self.parts.append(s)
 p=Text();p.feed(s);return ' '.join(''.join(p.parts).split())
paths=[p['path'] for p in posts]+[f'{a["path"]}'+(f'/page/{i+1}' if i else '') for a in archives for i in range((len(a['posts'])+9)//10)]
errors=[];documents={}
for path in paths:
 f=ROOT/'dist'/path/'index.html'
 if not f.exists():errors.append((path,'missing route'));continue
 d=Document();d.feed(f.read_text());documents[path]=d
 if d.h1!=1:errors.append((path,'H1 count',d.h1))
 if any('noindex' in (r or '').lower() or 'none' in (r or '').lower().split(',') for r in d.robots):errors.append((path,'production article/archive blocked from indexing'))
 for img in d.images:
  if img.startswith('/') and not (ROOT/'dist'/img.lstrip('/')).is_file():errors.append((path,'missing image',img))
 for href in d.links:
  u=urlparse(href)
  if u.scheme in ['tel','mailto'] or u.netloc and u.netloc not in ['www.midtowndentalcare.org','midtowndentalcare.org']:continue
  p=unquote(u.path)
  if p=='/privacy-policy/':continue # existing, separately recorded legal-content blocker
  if not p:continue
  target=ROOT/'dist'/p.lstrip('/')
  if not target.is_file() and not (target/'index.html').is_file():errors.append((path,'broken internal link',href))
for post in posts:
 d=documents.get(post['path'])
 if not d:continue
 if ' '.join(''.join(d.copy).split())!=plain(post['html']):errors.append((post['path'],'rendered body text differs'))
 article=next((s for s in d.scripts if s.get('@type')=='BlogPosting'),{})
 if article.get('creditText')!=f'Original publishing credit: {post["publishingCredit"]}':errors.append((post['path'],'publishing credit mismatch'))
 if article.get('author') or article.get('reviewedBy'):errors.append((post['path'],'unapproved author/reviewer claim'))
 if '[fusion_' in post['html'] or '[/fusion_' in post['html']:errors.append((post['path'],'unrendered builder shortcode'))
 if article.get('datePublished')!=post['published']:errors.append((post['path'],'publication date mismatch'))
# Every article must be reachable from an archive and another article.
for post in posts:
 url='/'+post['path']+'/'
 from_archives=sum(url in d.links for p,d in documents.items() if p not in {x['path'] for x in posts})
 from_articles=sum(url in documents[p['path']].links for p in posts if p['path']!=post['path'])
 if not from_archives:errors.append((post['path'],'not linked from archive'))
 # Adjacent navigation ensures even old posts have an inbound article link.
 if not from_articles:errors.append((post['path'],'not linked from another article'))
result={'posts':len(posts),'archive_routes_including_pagination':len(paths)-len(posts),'errors':errors}
print(json.dumps(result,indent=2));(ROOT/'outputs/launch-2026-11-02/blog-migration/build-verification.json').write_text(json.dumps(result,indent=2))
raise SystemExit(bool(errors))
