export function officeState(date = new Date()) {
  const parts = Object.fromEntries(new Intl.DateTimeFormat('en-US', { timeZone: 'America/Chicago', weekday: 'short', hour: 'numeric', minute: 'numeric', hourCycle: 'h23', month: 'numeric', year: 'numeric' }).formatToParts(date).map(p => [p.type, p.value]));
  const weekday = parts.weekday;
  const hour = Number(parts.hour) + Number(parts.minute) / 60;
  const close = weekday === 'Fri' ? 15 : ['Mon','Tue','Wed','Thu'].includes(weekday) ? 17 : 0;
  const status = close && hour >= 8 && hour < close ? (hour >= close - 1 ? 'closing' : 'open') : 'closed';
  const copy = { open: 'Within our regular office hours — call to book.', closing: 'Our regular office hours end soon — call to book.', closed: 'Call to book. Office hours: Mon–Thu 8–5 · Fri 8–3.' }[status];
  return { weekday, status, copy, season: Number(parts.month) >= 10 ? 'year-end' : 'evergreen', year: Number(parts.year) };
}
export function phoneClickPayload(landingPage, location) {
  return { event: 'phone_click', landing_page: landingPage, cta_location: location };
}
