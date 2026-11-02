// Existing client website and public Google Maps listing, checked November 2,
// 2026. Maps confirms the main number, address, and hours. Number ownership,
// especially the separate new-patient number, remains a launch gate.
export const practice = {
  name: 'MidTown Dental Care',
  site: 'https://www.midtowndentalcare.org',
  phone: '(414) 258-5351',
  telephone: '+14142585351',
  newPatientPhone: '(414) 261-3376',
  newPatientTelephone: '+14142613376',
  // Published accessibility contact; Bryan confirmed this form recipient Nov 2.
  email: 'frontdesk@midtowndentalcare.net',
  maps: 'https://maps.app.goo.gl/zaHUajak3e7CWQKe8',
  forms: 'https://app.operadds.com/Forms/SetFormsGroupGen?cFgId=492ea1da-d86b-4b86-bd01-0552a75dae51#main',
  payment: 'https://midtowndentalcaresc.secure.lq-pay.net/',
};

export const practiceSchema = {
  '@context': 'https://schema.org',
  '@type': 'Dentist',
  '@id': `${practice.site}/#practice`,
  name: practice.name,
  url: practice.site,
  telephone: practice.telephone,
  logo: `${practice.site}/images/midtown-logo.webp`,
  sameAs: [practice.maps],
  geo: { '@type': 'GeoCoordinates', latitude: 43.0606698, longitude: -88.0219602 },
  address: {
    '@type': 'PostalAddress', streetAddress: '8726 W. North Ave',
    addressLocality: 'Wauwatosa', addressRegion: 'WI', postalCode: '53226', addressCountry: 'US',
  },
  openingHoursSpecification: [
    { '@type': 'OpeningHoursSpecification', dayOfWeek: ['Monday', 'Tuesday', 'Wednesday', 'Thursday'], opens: '08:00', closes: '17:00' },
    { '@type': 'OpeningHoursSpecification', dayOfWeek: ['Friday'], opens: '08:00', closes: '15:00' },
  ],
};
