// Jordan's November 3 briefs, adapted for the approved Astro site.
// Bryan approved these reviewed pages for publication on November 4, 2026.
export type LandingKind = 'general' | 'delta';
export const reviews = [
  { name: 'Matt', quote: "A+ all around. I needed a new dentist, but I kept putting it off. Tooth began hurting, so I couldn't put it off any longer. I called and they got me in the next day. The staff was super friendly, knowledgeable, and I felt like I was in great hands." },
  { name: 'Trevor T.', quote: 'Great staff, enjoyable experience! Called about an issue I was having and they were able to fit me in their schedule the following day! Calm atmosphere, friendly staff. Would recommend MidTown Dental to anyone!' },
  { name: 'Peter M.', quote: 'For a person who has always since childhood had a negative relationship to the dentist … I was floored by the warmth, professionalism, and care I received from the whole staff … They have given me a renewed point of view on the dentist office and I look forward to continuing my care there.' },
  { name: 'Bonnie H.', quote: 'Warm and welcoming from check in to check out, everyone was friendly! Great experience all around!! Highly recommend MidTown Dental Care for all your dental needs 😊' },
  { name: 'Mark W.', quote: 'I love my Mid Town Dental! They have all the up to date technology and a very friendly and professional staff.' },
];
export const dentists = [
  { name: 'Dr. Laura Russell, DDS', image: 'laura-russell.jpg', subtitle: 'Owner · Patients come first', bio: 'A University of Michigan School of Dentistry graduate, Dr. Russell has practiced for over 20 years. She brings a “patients come first” philosophy and modern dentistry to MidTown.' },
  { name: 'Dr. AnnMarie Hoyme', image: 'annmarie-hoyme.jpg', subtitle: 'Family & children’s dentistry', bio: 'A Marquette graduate with a general practice residency at Loyola University Chicago. Dr. Hoyme enjoys helping children build a positive relationship with the dentist.' },
  { name: 'Dr. Karla Schmidt, DDS', image: 'karla-schmidt.jpg', subtitle: 'Gentle, personal care', bio: 'A 2004 Marquette graduate, Dr. Schmidt focuses on comfortable, personal care, helping patients with dental anxiety and caring for older adults.' },
  { name: 'Dr. Mark Crego, DDS', image: 'mark-crego.jpg', subtitle: 'More than 40 years in practice', bio: 'A proud Marquette graduate, Dr. Crego enjoys implant, crown and bridge work and keeps current with new dental technology.' },
];
export const generalFaq = [
  { q: 'Are you accepting new patients?', a: 'Yes. We welcome new patients of all ages. Call our new patient line to schedule a dentist appointment.' },
  { q: 'Do you take walk-ins?', a: 'Please call before coming in. We work by appointment so we can give each patient our attention. Our team can discuss the next available visit with you.' },
  { q: 'Is MidTown Dental Care a dentist near me?', a: 'Our dentist office is at 8726 W. North Ave in Wauwatosa, serving Tosa and the greater Milwaukee community.' },
  { q: 'How often should I get a dental cleaning?', a: 'Most people do best with a cleaning and checkup every six months. Your dentist may recommend a different schedule based on your gum health.' },
  { q: 'Do you see kids?', a: 'Yes. We’re a family dentist office, and Dr. AnnMarie Hoyme especially enjoys helping children build a positive relationship with the dentist.' },
  { q: 'Do you take my insurance? What if I don’t have insurance?', a: 'Call us to discuss your plan before scheduling. If you don’t have insurance, ask about our in-house membership plan and financing through Cherry, CareCredit and Sunbit.' },
  { q: 'I get nervous at the dentist. Can you help?', a: 'Our team takes time to explain your care, and nitrous oxide is available to help you relax. Tell us about your concerns when you call.' },
];
export const deltaFaq = [
  { q: 'Do you accept Delta Dental?', a: 'Delta Dental’s directory lists Dr. Mark Crego at our North Avenue office in the PPO and Premier networks. Participation depends on your dentist and specific plan. Call before booking to confirm the right dentist for your coverage.' },
  { q: 'I have a Delta Dental PPO plan. Can I see a Delta Dental PPO dentist here?', a: 'Dr. Mark Crego is listed in the Delta Dental PPO directory at this address. Confirm current participation for your specific plan and the dentist you will see before scheduling.' },
  { q: 'What’s the difference between Delta Dental PPO and Premier?', a: 'PPO and Premier are different Delta Dental networks. Your plan determines which network and benefits apply. Check your member card and plan documents, then call us to discuss your appointment.' },
  { q: 'Is there a Delta Dental provider near me in Wauwatosa or Milwaukee?', a: 'Our office is at 8726 W. North Ave in Wauwatosa. Dr. Mark Crego’s Delta Dental directory listing is for this location.' },
  { q: 'Are you accepting new Delta Dental patients?', a: 'New patients are welcome. Call our new patient line and tell us your plan so we can discuss dentist availability and next steps.' },
  { q: 'Does Delta Dental cover cleanings?', a: 'Many Delta Dental plans include preventive care such as cleanings and exams. Your exact benefits, limitations and costs depend on your plan. Review your plan documents before treatment.' },
  { q: 'Will you file my claims?', a: 'Please ask our front desk how claims are handled for your specific plan before your visit.' },
  { q: 'What if I need treatment my plan doesn’t fully cover?', a: 'We’ll walk you through your treatment options and costs. Financing options include Cherry, CareCredit and Sunbit.' },
];
export const landing = {
  general: {
    slug: 'ppc-general', title: 'Dentist in Wauwatosa, WI | Book an Appointment | MidTown Dental Care',
    description: 'Looking for a dentist in Wauwatosa? Family and general dentistry, dental cleanings and same-day crowns in Tosa. Call (414) 261-3376 for an appointment.',
    h1: 'Your trusted dentist in Wauwatosa.',
    intro: 'General dentistry, dental cleanings and checkups for the whole family — right here in Tosa. Call today to book your dentist appointment.',
    heroCall: 'Call for your first visit', faq: generalFaq,
  },
  delta: {
    slug: 'ppc-delta-dental', title: 'Delta Dental Dentist in Wauwatosa, WI | MidTown Dental Care',
    description: 'Looking for a Delta Dental dentist in Wauwatosa near Milwaukee? Ask about Dr. Crego’s PPO and Premier directory listing and confirm your plan. Call (414) 261-3376.',
    h1: 'Your Delta Dental dentist in Wauwatosa.',
    intro: 'Have Delta Dental PPO or Premier? Dr. Mark Crego is listed in both networks at our Wauwatosa office. Call to confirm your plan and dentist before booking.',
    heroCall: 'Call about your Delta Dental plan', faq: deltaFaq,
  },
};
