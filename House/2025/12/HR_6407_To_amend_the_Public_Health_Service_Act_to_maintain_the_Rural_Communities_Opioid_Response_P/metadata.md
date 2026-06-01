# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6407?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6407
- Title: RCORP Authorization Act
- Congress: 119
- Bill type: HR
- Bill number: 6407
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-04-17T08:07:15Z
- Update date including text: 2026-04-17T08:07:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6407",
    "number": "6407",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001205",
        "district": "1",
        "firstName": "Carol",
        "fullName": "Rep. Miller, Carol D. [R-WV-1]",
        "lastName": "Miller",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "RCORP Authorization Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:15Z",
    "updateDateIncludingText": "2026-04-17T08:07:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
        "item": {
          "date": "2025-12-03T15:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "GA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "VA"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "GU"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6407ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6407\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mrs. Miller of West Virginia (for herself, Mr. Tonko , Mr. Carter of Georgia , and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to maintain the Rural Communities Opioid Response Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the RCORP Authorization Act .\n#### 2. Rural Communities Opioid Response Program\nSubpart I of part D of title III of the Public Health Service Act is amended by inserting after section 330A\u20132 ( 42 U.S.C. 254c\u20131b ) the following:\n330A\u20133. Rural Communities Opioid Response Program (a) Establishment The Secretary, acting through the Administrator of the Health Resources and Services Administration (in this section referred to as the Administrator ), shall maintain a program to be known as the Rural Communities Opioid Response Program to establish and expand prevention, treatment, and recovery services in rural areas (as defined by the Secretary) for substance use disorders (including opioid use disorder), related behavioral health conditions, and other related public health issues. (b) Grants and cooperative agreements (1) In general In carrying out the program under this section, the Administrator may award grants or cooperative agreements to eligible entities. (2) Use of funds An eligible entity that receives a grant or cooperative agreement under this section may use funds received through such grant or cooperative agreement to\u2014 (A) conduct planning activities to strengthen the capacity of cross-sector networks and improve coordination of resources and care involving substance use disorder; (B) identify and implement evidence-based and sustainable delivery models to provide direct prevention, treatment, and recovery services; (C) respond to new and emerging public health issues involving substance use disorder; (D) provide targeted technical assistance or evaluation activities with respect to grants or cooperative agreements awarded under this section; or (E) engage in such other activities as the Secretary may determine appropriate to carry out the program under this section. (3) Prohibited use of funds An eligible entity that is awarded a grant or cooperative agreement under this section may not use funds provided through such grant or cooperative agreement for the acquisition or improvement of real property. (4) Eligibility To be eligible to receive a grant or cooperative agreement under this section, an entity shall be\u2014 (A) a State; (B) an Indian Tribe or Tribal organization (as such terms are defined in section 4 of the Indian Self-Determination and Education Assistance Act); (C) a State office of rural health; or (D) any other domestic entity. (5) Application To seek a grant or cooperative agreement under this section, an eligible entity shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require, including a description of how the rural population in the local community or region to be served will be involved in the development and ongoing operations of such activities, as applicable. (6) Grant period The Administrator may not award a grant or cooperative agreement under this section for a period of more than 5 years. (7) Funding The Administrator may fully fund a grant or cooperative agreement made under this section at the time of the award. (c) Authorization of appropriations There are authorized to be appropriated to carry out this section $165,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-12-03",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-01-05T16:17:49Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6407ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "RCORP Authorization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-23T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RCORP Authorization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-23T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to maintain the Rural Communities Opioid Response Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-23T05:33:19Z"
    }
  ]
}
```
