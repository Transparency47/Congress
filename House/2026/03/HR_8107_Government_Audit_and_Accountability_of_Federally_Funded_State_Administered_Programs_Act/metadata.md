# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8107
- Title: Government Audit and Accountability of Federally Funded State-Administered Programs Act
- Congress: 119
- Bill type: HR
- Bill number: 8107
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-05-29T15:54:39Z
- Update date including text: 2026-05-29T15:54:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 0.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8107",
    "number": "8107",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000389",
        "district": "17",
        "firstName": "Ro",
        "fullName": "Rep. Khanna, Ro [D-CA-17]",
        "lastName": "Khanna",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Government Audit and Accountability of Federally Funded State-Administered Programs Act",
    "type": "HR",
    "updateDate": "2026-05-29T15:54:39Z",
    "updateDateIncludingText": "2026-05-29T15:54:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 41 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
        "item": [
          {
            "date": "2026-04-29T13:08:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-03-26T14:03:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8107ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8107\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Khanna (for himself and Mr. Burchett ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the establishment of a list identifying program areas and administrative practices presenting the greatest risk to the integrity of Federal funds administered by States and local governments.\n#### 1. Short title\nThis Act may be cited as the Government Audit and Accountability of Federally Funded State-Administered Programs Act .\n#### 2. High Risk List for federally-funded State-administered programs\n##### (a) In general\nNot later than 2 years after the date of the enactment of this Act, and periodically thereafter, the Comptroller General of the United States shall submit to Congress a High Risk List identifying program areas and administrative practices presenting the greatest risk to the integrity of Federal funds administered by States and local governments, including Federal pass through programs subject to audit under chapter 75 of title 31, United States Code.\n##### (b) Contents\nThe High Risk List required under subsection (a) shall\u2014\n**(1)**\nidentify high-risk program areas and administrative practices presenting systematic vulnerability the administration of Federal funds by State and local governments;\n**(2)**\nassess best practices that have strengthened the integrity of Federal funds administered by State and local governments and reduced waste, fraud, and abuse in federally funded programs;\n**(3)**\nidentify Federal tools, resources, and technical assistance available to address the vulnerability patterns under paragraph (1); and\n**(4)**\ninclude recommendations to Congress for addressing the high risk program areas and administrative practices identified under paragraph (1).\n##### (c) Sources\n**(1)**\nIn carrying out the preparation of the High Risk List under subsection (a), the Comptroller General shall primarily rely on existing publicly available oversight, audit and investigative materials, to conduct an analysis of federally funded State-administered programs, which may include\u2014\n**(A)**\nfindings of Federal and State auditors, inspectors general, and attorneys general with respect to the administration of Federal funds by State and local governments;\n**(B)**\nsingle audit reports required under section 7502 of title 31, United States Code; and\n**(C)**\nand other publicly available Federal oversight and program integrity data.\n**(2)**\nIn preparing the High Risk List, the Comptroller General shall apply professional auditing and evaluation standards in analyzing such materials. The Comptroller General may supplement such materials with independent analysis of publicly available Federal program data where existing oversight materials are insufficient to identify high-risk program areas or administrative practices, provided that nothing in this section shall be construed to authorize the Comptroller General to compel the production of information from States or local governments or to conduct independent audits of State or local programs.\n##### (d) Form and methodology\nThe Comptroller General shall determine the appropriate form and methodology for preparing and presenting the High Risk List required under this section, consistent with Government Auditing Standards and the requirements of subsection (c).",
      "versionDate": "2026-03-26",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-29T15:54:39Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8107ih.xml"
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
      "title": "Government Audit and Accountability of Federally Funded State-Administered Programs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T03:53:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Government Audit and Accountability of Federally Funded State-Administered Programs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-15T03:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the establishment of a list identifying program areas and administrative practices presenting the greatest risk to the integrity of Federal funds administered by States and local governments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T03:48:36Z"
    }
  ]
}
```
