# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4723?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4723
- Title: Mental Health for Latinos Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4723
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2025-12-05T21:31:48Z
- Update date including text: 2025-12-05T21:31:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4723",
    "number": "4723",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001226",
        "district": "6",
        "firstName": "Andrea",
        "fullName": "Rep. Salinas, Andrea [D-OR-6]",
        "lastName": "Salinas",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Mental Health for Latinos Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:31:48Z",
    "updateDateIncludingText": "2025-12-05T21:31:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
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
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:14:00Z",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "True",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4723ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4723\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Salinas (for herself, Ms. Barrag\u00e1n , Mr. Garc\u00eda of Illinois , Ms. Randall , Mr. Cisneros , and Mr. Ruiz ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to provide for a behavioral and mental health outreach and education strategy to reduce stigma associated with mental health among the Hispanic and Latino population, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mental Health for Latinos Act of 2025 .\n#### 2. Hispanic and Latino behavioral and mental health outreach and education strategy\nPart D of title V of the Public Health Service Act ( 42 U.S.C. 290dd et seq. ) is amended by adding at the end the following new section:\n554. Behavioral and mental health outreach and education strategy (a) In general The Secretary, acting through the Assistant Secretary, shall, in coordination with advocacy and behavioral and mental health organizations serving populations of Hispanic and Latino individuals or communities, develop and implement an outreach and education strategy to promote behavioral and mental health and reduce stigma associated with mental health conditions and substance abuse among the Hispanic and Latino populations. Such strategy shall\u2014 (1) be designed to\u2014 (A) meet the diverse cultural and language needs of the various Hispanic and Latino populations; and (B) be developmentally and age appropriate; (2) increase awareness of symptoms of mental illnesses common among such populations, taking into account differences within subgroups, such as gender, gender identity, age, sexual orientation, or ethnicity, of such populations; (3) provide information on evidence-based, culturally and linguistically appropriate and adapted interventions and treatments; (4) ensure full participation of, and engage, both consumers and community members in the development and implementation of materials; and (5) seek to broaden the perspective among both individuals in these communities and stakeholders serving these communities to use a comprehensive public health approach to promoting behavioral health that addresses a holistic view of health by focusing on the intersection between behavioral and physical health. (b) Reports Beginning not later than 1 year after the date of the enactment of this section and annually thereafter, the Secretary, acting through the Assistant Secretary, shall submit to Congress, and make publicly available, a report on the extent to which the strategy developed and implemented under subsection (a) improved behavioral and mental health outcomes associated with mental health conditions and substance abuse among Hispanic and Latino populations. (c) Authorization of appropriations There is authorized to be appropriated to carry out this section $1,000,000 for fiscal year 2026. .",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-24",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2446",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Mental Health for Latinos Act of 2025",
      "type": "S"
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
        "updateDate": "2025-09-16T14:28:05Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4723ih.xml"
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
      "title": "Mental Health for Latinos Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-05T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Mental Health for Latinos Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T12:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to provide for a behavioral and mental health outreach and education strategy to reduce stigma associated with mental health among the Hispanic and Latino population, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T12:18:18Z"
    }
  ]
}
```
