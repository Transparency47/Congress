# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2126?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2126
- Title: Integrated Ocean Observation System Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2126
- Origin chamber: Senate
- Introduced date: 2025-06-18
- Update date: 2026-05-15T17:55:49Z
- Update date including text: 2026-05-15T17:55:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-18: Introduced in Senate
- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 405.
- Latest action: 2025-06-18: Introduced in Senate

## Actions

- 2025-06-18 - IntroReferral: Introduced in Senate
- 2025-06-18 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.
- 2026-05-11 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.
- 2026-05-11 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 405.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-18",
    "latestAction": {
      "actionDate": "2025-06-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2126",
    "number": "2126",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "W000437",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Wicker, Roger F. [R-MS]",
        "lastName": "Wicker",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Integrated Ocean Observation System Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T17:55:49Z",
    "updateDateIncludingText": "2026-05-15T17:55:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 405.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-05-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-120.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-10-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
      "type": "IntroReferral"
    }
  ]
}
```

## API Data: committees

```json
{
  "committees": [
    {
      "activities": {
        "item": [
          {
            "date": "2026-05-11T20:17:00Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-21T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-18T18:00:44Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
      "state": "WA"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "MS"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AK"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-09-09",
      "state": "AK"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "DE"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "WI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MA"
    }
  ]
}
```

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2126is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2126\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Wicker (for himself and Ms. Cantwell ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo reauthorize the Integrated Coastal and Ocean Observation System Act of 2009, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Integrated Ocean Observation System Reauthorization Act of 2025 .\n#### 2. Purposes\nSection 12302 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3601 ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking Council and inserting Committee ;\n**(B)**\nby striking and ocean observation and inserting , ocean, and meteorological observations ; and\n**(C)**\nby striking and coastal information and inserting , coastal, and meteorological information ; and\n**(2)**\nin paragraph (4)(A), by inserting data management systems and cyber infrastructure, after data gaps, .\n#### 3. Definitions\nSection 12303 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3602 ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by striking Council and inserting Committee ; and\n**(B)**\nby striking term and all that follows through established and inserting term Committee means the Ocean Policy Committee established ;\n**(2)**\nin paragraph (3), by striking Council and inserting Committee ;\n**(3)**\nin paragraph (6), by inserting conduct operational oceanography measurements and after systems in order to ;\n**(4)**\nby redesignating paragraphs (8) and (9) as paragraphs (9) and (10), respectively;\n**(5)**\nby inserting after paragraph (7) the following:\n(8) State The term State has the meaning given that term in section 3501 of title 40, United States Code. ; and\n**(6)**\nin paragraph (10), as redesignated by paragraph (4), by striking Council and inserting Committee .\n#### 4. Integrated Coastal and Ocean Observing System\nSection 12304 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3603 ) is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (A), by striking national and inserting regional, national, ;\n**(B)**\nin subparagraph (C), by inserting and ocean after weather ; and\n**(C)**\nin subparagraph (E)\u2014\n**(i)**\nin clause (iv), by inserting and ocean after weather each place it appears; and\n**(ii)**\nin clause (v), by inserting and ocean after weather ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking Council and inserting Committee ; and\n**(ii)**\nin the matter preceding subparagraph (A), by striking Council each place it appears and inserting Committee ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking The Council and inserting The Committee ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby redesignating clauses (vi) through (x) as clauses (vii) through (xi), respectively; and\n**(II)**\nby inserting after clause (v) the following:\n(vi) develop requirements and processes for regional associations and federally funded projects of the agencies participating in the Interagency Ocean Observation Committee to collaborate with the regional coastal observing systems for data sharing at regional levels; ; and\n**(C)**\nin paragraph (3)(C)\u2014\n**(i)**\nin clause (iii)(I), by inserting as operational entities after associations ;\n**(ii)**\nin clause (x), by inserting , cyber infrastructure, after data management ; and\n**(iii)**\nin clause (xiii)\u2014\n**(I)**\nby inserting and ocean after weather ; and\n**(II)**\nby striking and harmful algal bloom forecasting and inserting harmful algal bloom forecasting, and resource and coastal management ;\n**(3)**\nin subsection (d)(1), by adding a period at the end; and\n**(4)**\nby striking the Council each place it appears and inserting the Committee .\n#### 5. Report to Congress\nSection 12307 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3606 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (8) and (9) as paragraphs (9) and (10), respectively; and\n**(B)**\nby inserting after paragraph (7) the following:\n(8) a post-storm evaluation for all major storms in the United States that occurred during the year preceding submission of the report, to assess the impact of observations of the System and other products of the System with respect to storm forecast accuracy; ; and\n**(2)**\nby striking the Council each place it appears and inserting the Committee .\n#### 6. Authorization of appropriations\nSection 12311 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3610 ) is amended\u2014\n**(1)**\nby striking There are and inserting the following:\n(a) In general There are ;\n**(2)**\nby striking this subtitle and all that follows and inserting $56,000,000 for each of fiscal years 2026 through 2030. ; and\n**(3)**\nby adding at the end the following:\n(b) Allocation of funds (1) In general Except as provided by paragraph (2), the Secretary shall allocate not less than 7.5 percent of amounts appropriated pursuant to the authorization of appropriations under subsection (a) to each regional coastal observing system that was in existence on January 1, 2025. (2) Exclusion of disaster relief appropriations Paragraph (1) does not apply with respect to any amounts appropriated by an Act making supplemental appropriations for disaster relief. .\n#### 7. Conforming amendments\n##### (a) Interagency financing and agreements\nSection 12305(b) of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3604(b) ) is amended by striking the Council and inserting the Committee .\n##### (b) Public-Private use policy\nSection 12308 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3607 ) is amended by striking the Council each place it appears and inserting the Committee .\n##### (c) Intent of Congress\nSection 12310 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3609 ) is amended by striking the Council each place it appears and inserting the Committee .",
      "versionDate": "2025-06-18",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2126rs.xml",
      "text": "II\nCalendar No. 405\n119th CONGRESS\n2d Session\nS. 2126\n[Report No. 119\u2013120]\nIN THE SENATE OF THE UNITED STATES\nJune 18, 2025 Mr. Wicker (for himself, Ms. Cantwell , Mrs. Hyde-Smith , Ms. Murkowski , Mr. Sullivan , Ms. Blunt Rochester , Ms. Baldwin , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nMay 11, 2026 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo reauthorize the Integrated Coastal and Ocean Observation System Act of 2009, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Integrated Ocean Observation System Reauthorization Act of 2025 .\n#### 2. Purposes\nSection 12302 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3601 ) is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking Council and inserting Committee ;\n**(B)**\nby striking and ocean observation and inserting , ocean, and meteorological observations ; and\n**(C)**\nby striking and coastal information and inserting , coastal, and meteorological information ; and\n**(2)**\nin paragraph (4)(A), by inserting data management systems and cyber infrastructure, after data gaps, .\n#### 3. Definitions\nSection 12303 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3602 ) is amended\u2014\n**(1)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by striking Council and inserting Committee ; and\n**(B)**\nby striking term and all that follows through established and inserting term Committee means the Ocean Policy Committee established ;\n**(2)**\nin paragraph (3), by striking Council and inserting Committee ;\n**(3)**\nin paragraph (6), by inserting conduct operational oceanography measurements and after systems in order to ;\n**(4)**\nby redesignating paragraphs (8) and (9) as paragraphs (9) and (10), respectively;\n**(5)**\nby inserting after paragraph (7) the following:\n(8) State The term State has the meaning given that term in section 3501 of title 40, United States Code. ; and\n**(6)**\nin paragraph (10), as redesignated by paragraph (4), by striking Council and inserting Committee .\n#### 4. Integrated Coastal and Ocean Observing System\nSection 12304 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3603 ) is amended\u2014\n**(1)**\nin subsection (b)(1)\u2014\n**(A)**\nin subparagraph (A), by striking national and inserting regional, national, ;\n**(B)**\nin subparagraph (C), by inserting and ocean after weather ; and\n**(C)**\nin subparagraph (E)\u2014\n**(i)**\nin clause (iv), by inserting and ocean after weather each place it appears; and\n**(ii)**\nin clause (v), by inserting and ocean after weather ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking Council and inserting Committee ; and\n**(ii)**\nin the matter preceding subparagraph (A), by striking Council each place it appears and inserting Committee ;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking The Council and inserting The Committee ; and\n**(ii)**\nin subparagraph (B)\u2014\n**(I)**\nby redesignating clauses (vi) through (x) as clauses (vii) through (xi), respectively; and\n**(II)**\nby inserting after clause (v) the following:\n(vi) develop requirements and processes for regional associations and federally funded projects of the agencies participating in the Interagency Ocean Observation Committee to collaborate with the regional coastal observing systems for data sharing at regional levels; ; and\n**(C)**\nin paragraph (3)(C)\u2014\n**(i)**\nin clause (iii)(I), by inserting as operational entities after associations ;\n**(ii)**\nin clause (x), by inserting , cyber infrastructure, after data management ; and\n**(iii)**\nin clause (xiii)\u2014\n**(I)**\nby inserting and ocean after weather ; and\n**(II)**\nby striking and harmful algal bloom forecasting and inserting harmful algal bloom forecasting, and resource and coastal management ;\n**(3)**\nin subsection (d)(1), by adding a period at the end; and\n**(4)**\nby striking the Council each place it appears and inserting the Committee .\n#### 5. Report to Congress\nSection 12307 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3606 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (8) and (9) as paragraphs (9) and (10), respectively; and\n**(B)**\nby inserting after paragraph (7) the following:\n(8) a post-storm evaluation for all major storms in the United States that occurred during the year preceding submission of the report, to assess the impact of observations of the System and other products of the System with respect to storm forecast accuracy; ; and\n**(2)**\nby striking the Council each place it appears and inserting the Committee .\n#### 6. Authorization of appropriations\nSection 12311 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3610 ) is amended\u2014\n**(1)**\nby striking There are and inserting the following:\n(a) In general There are ;\n**(2)**\nby striking this subtitle and all that follows and inserting $56,000,000 for each of fiscal years 2026 through 2030. ; and\n**(3)**\nby adding at the end the following:\n(b) Allocation of funds (1) In general Except as provided by paragraph (2), the Secretary shall allocate not less than 7.5 percent of amounts appropriated pursuant to the authorization of appropriations under subsection (a) to each regional coastal observing system that was in existence on January 1, 2025. (2) Exclusion of disaster relief appropriations Paragraph (1) does not apply with respect to any amounts appropriated by an Act making supplemental appropriations for disaster relief. .\n#### 7. Conforming amendments\n##### (a) Interagency financing and agreements\nSection 12305(b) of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3604(b) ) is amended by striking the Council and inserting the Committee .\n##### (b) Public-Private use policy\nSection 12308 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3607 ) is amended by striking the Council each place it appears and inserting the Committee .\n##### (c) Intent of Congress\nSection 12310 of the Integrated Coastal and Ocean Observation System Act of 2009 ( 33 U.S.C. 3609 ) is amended by striking the Council each place it appears and inserting the Committee .",
      "versionDate": "2025-06-18",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-01-07T16:51:26Z"
          },
          {
            "name": "Atmospheric science and weather",
            "updateDate": "2026-01-07T16:51:16Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-07T16:51:06Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-08T13:31:43Z"
          },
          {
            "name": "Earth sciences",
            "updateDate": "2026-01-07T16:51:20Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-01-07T16:50:54Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-01-07T16:50:58Z"
          },
          {
            "name": "Navigation, waterways, harbors",
            "updateDate": "2026-01-07T16:51:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-05-15T17:55:49Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2126is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2126rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Integrated Ocean Observation System Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-05-13T04:53:27Z"
    },
    {
      "title": "Integrated Ocean Observation System Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Integrated Ocean Observation System Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-02T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Integrated Coastal and Ocean Observation System Act of 2009, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-02T01:19:03Z"
    }
  ]
}
```
