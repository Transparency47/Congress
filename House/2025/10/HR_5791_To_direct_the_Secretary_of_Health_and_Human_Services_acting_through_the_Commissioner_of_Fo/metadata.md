# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5791?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5791
- Title: BLOOD Centers Act
- Congress: 119
- Bill type: HR
- Bill number: 5791
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-03-25T08:05:30Z
- Update date including text: 2026-03-25T08:05:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5791",
    "number": "5791",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000829",
        "district": "8",
        "firstName": "Tony",
        "fullName": "Rep. Wied, Tony [R-WI-8]",
        "lastName": "Wied",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "BLOOD Centers Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:05:30Z",
    "updateDateIncludingText": "2026-03-25T08:05:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:01:10Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "WA"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "WI"
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
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "WA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "AL"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5791ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5791\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Wied (for himself, Ms. Schrier , and Mr. Tiffany ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to establish an expedited process for the approval of certain biologics license application supplements for blood centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Boosting Lifesaving Operations, Opening Donation Centers Act or the BLOOD Centers Act .\n#### 2. Expedited process for approval of certain BLA supplements for blood centers\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Secretary, acting pursuant to section 351(a)(2) of the Public Health Service Act ( 42 U.S.C. 262(a)(2) ), shall establish an expedited process for the approval of a supplemental application submitted by the owner or operator of a blood center seeking to add an apheresis collection device to an existing BLA license at a location not previously licensed for such a device.\n##### (b) Deadline\nUnder the expedited procedure, the Secretary shall approve a supplemental application described in subsection (a) not later than 30 days after the date of submission of the application unless the Secretary makes a showing that there is\u2014\n**(1)**\na specific concern for the safety, purity, or potency of products produced at the specific location subject to the supplemental application; or\n**(2)**\na systemic failure by the owner or operator to meet standards designed to ensure the continued safety, purity, and potency of products produced at other locations under a biologics license.\n##### (c) Applicability\nThe expedited procedure shall apply with respect to a supplemental application described in subsection (a) if the owner or operator that submits the application\u2014\n**(1)**\nholds a biologics license for at least one blood center site; and\n**(2)**\n**(A)**\nhas been approved for a biologics license at 3 or more Food and Drug Administration registered locations under the biologics license referred to in paragraph (1); or\n**(B)**\nis accredited and in good standing for blood collection by an accreditation organization with standards that meet or exceed, as determined by the Secretary, all applicable regulatory requirements for blood collections.\n##### (d) Definitions\nIn this section:\n**(1) BLA**\nThe term BLA means a biologics license application.\n**(2) Blood center**\nThe term blood center means a human blood donation center.\n**(3) Expedited procedure**\nThe term expedited procedure means the expedited procedure to be established under subsection (a).\n**(4) Secretary**\nThe term Secretary means the Secretary of Health and Human Services acting through the Commissioner of Food and Drugs.",
      "versionDate": "2025-10-17",
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
        "updateDate": "2025-12-09T13:49:05Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5791ih.xml"
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
      "title": "BLOOD Centers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BLOOD Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Boosting Lifesaving Operations, Opening Donation Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T08:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Health and Human Services, acting through the Commissioner of Food and Drugs, to establish an expedited process for the approval of certain biologics license application supplements for blood centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T08:18:25Z"
    }
  ]
}
```
