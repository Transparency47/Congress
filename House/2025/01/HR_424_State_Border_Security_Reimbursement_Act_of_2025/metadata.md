# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/424?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/424
- Title: State Border Security Reimbursement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 424
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-03-17T19:29:45Z
- Update date including text: 2025-03-17T19:29:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/424",
    "number": "424",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "State Border Security Reimbursement Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-17T19:29:45Z",
    "updateDateIncludingText": "2025-03-17T19:29:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001051",
      "district": "31",
      "firstName": "John",
      "fullName": "Rep. Carter, John R. [R-TX-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr424ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 424\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Crenshaw (for himself and Mr. Roy ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo reimburse the States for border security expenses, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the State Border Security Reimbursement Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nBorder security is primarily a Federal responsibility.\n**(2)**\nDue to failures of the Federal Government, the State of Texas has been forced to provide resources for border security.\n**(3)**\nSince the 2008\u20132009 biennium budget, Texas has allocated more than $3,208,000,000 for border security in Texas\u2019 biennium budget disaggregated, as follows:\n**(A)**\nIn 2008\u20132009, Texas allocated more than $110,000,000 for border security.\n**(B)**\nIn 2010\u20132011, Texas allocated more than $120,000,000 for border security.\n**(C)**\nIn 2012\u20132013, Texas allocated more than $222,100,000 for border security.\n**(D)**\nIn 2014\u20132015, Texas allocated more than $510,000,000 for border security.\n**(E)**\nIn 2016\u20132017, Texas allocated more than $800,000,000 for border security.\n**(F)**\nIn 2018\u20132019, Texas allocated more than $663,100,000 for border security.\n**(G)**\nIn 2020\u20132021, Texas allocated more than $782,800,000 for border security.\n**(H)**\nFor 2022\u20132023, the State of Texas Legislative Budget Board is currently recommending an additional $797,100,000 for border security.\n**(4)**\nCitizens of border States are being taxed twice for the same purpose.\n**(5)**\nStates using their taxpayer dollars and allocating State budgets to meet public safety obligations, which fall under Federal responsibilities, imposes an undue burden on the State.\n#### 3. Reimbursement\n##### (a) Qualification\nNotwithstanding any other provision of law, States that have expended more than $2,500,000,000 on border security and enforcement in support of Federal efforts in the ten years prior to the date of the enactment of this Act shall have all associated expenses reimbursed.\n##### (b) Application\nNot later than 180 days after the date of the enactment of this Act, the Governors of eligible States shall submit\u2014\n**(1)**\nan accounting of all non-federally funded border security expenses incurred by the State and its municipalities; and\n**(2)**\nthe total sum of such expenses.\n##### (c) Reimbursement\nNot later than 1 year after the date on which the State submits the application pursuant to subsection (b), the Federal Government shall reimburse such expenses pursuant to subsection (a).",
      "versionDate": "2025-01-15",
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
        "name": "Immigration",
        "updateDate": "2025-02-14T13:02:29Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr424",
          "measure-number": "424",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr424v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>State Border Security Reimbursement Act of 2025 </strong></p><p>This bill requires the federal government to reimburse eligible states for their border security expenses.</p><p>To be eligible, a state must have expended more than $2.5 billion on border security and enforcement in the 10 years before this bill's enactment. If such a state provides by a certain deadline an accounting of all of its nonfederally funded border security expenses, the federal government must reimburse the full amount.</p>"
        },
        "title": "State Border Security Reimbursement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr424.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>State Border Security Reimbursement Act of 2025 </strong></p><p>This bill requires the federal government to reimburse eligible states for their border security expenses.</p><p>To be eligible, a state must have expended more than $2.5 billion on border security and enforcement in the 10 years before this bill's enactment. If such a state provides by a certain deadline an accounting of all of its nonfederally funded border security expenses, the federal government must reimburse the full amount.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr424"
    },
    "title": "State Border Security Reimbursement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>State Border Security Reimbursement Act of 2025 </strong></p><p>This bill requires the federal government to reimburse eligible states for their border security expenses.</p><p>To be eligible, a state must have expended more than $2.5 billion on border security and enforcement in the 10 years before this bill's enactment. If such a state provides by a certain deadline an accounting of all of its nonfederally funded border security expenses, the federal government must reimburse the full amount.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr424"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr424ih.xml"
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
      "title": "State Border Security Reimbursement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Border Security Reimbursement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reimburse the States for border security expenses, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T03:03:23Z"
    }
  ]
}
```
