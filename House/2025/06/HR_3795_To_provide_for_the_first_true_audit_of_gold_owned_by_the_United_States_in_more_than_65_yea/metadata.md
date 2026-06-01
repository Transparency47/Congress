# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3795?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3795
- Title: Gold Reserve Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3795
- Origin chamber: House
- Introduced date: 2025-06-06
- Update date: 2026-01-05T20:36:27Z
- Update date including text: 2026-01-05T20:36:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-06: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-06-06: Introduced in House

## Actions

- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Introduced in House
- 2025-06-06 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-06",
    "latestAction": {
      "actionDate": "2025-06-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3795",
    "number": "3795",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Gold Reserve Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-05T20:36:27Z",
    "updateDateIncludingText": "2026-01-05T20:36:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-06",
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
          "date": "2025-06-06T13:03:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "OH"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "NC"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "TX"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3795ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3795\nIN THE HOUSE OF REPRESENTATIVES\nJune 6, 2025 Mr. Massie (for himself, Mr. Davidson , Mr. McDowell , and Mr. Nehls ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo provide for the first true audit of gold owned by the United States in more than 65 years and to conduct subsequent audits every 5 years.\n#### 1. Short title\nThis Act may be cited as the Gold Reserve Transparency Act of 2025 .\n#### 2. Assay, inventory, and audit of gold reserves\n##### (a) In general\nThe Comptroller General of the United States shall contract with a qualified, independent, third-party, external auditor to conduct and complete, not later than nine months after the date of enactment of this Act, and every 5 years thereafter\u2014\n**(1)**\na full assay, inventory, and audit of all gold reserves, including any gold in deep storage , of the United States at the place or places where such reserves are kept;\n**(2)**\nan analysis of the sufficiency of the measures taken to ensure the physical security of such reserves;\n**(3)**\na full accounting of any and all encumbrances, including those due to lease, swap, or similar transactions presently in existence or entered into at any time during the past 50 years with respect to the gold reserves;\n**(4)**\na full accounting of any and all sales, purchases, disbursements, or receipts at any time during the past 50 years\u2014whether directly or indirectly undertaken\u2014with respect to the gold reserves, including the specific terms and parties involved in such transactions; and\n**(5)**\na full accounting of all gold in which the U.S. Government (including the Board of Governors of the Federal Reserve System or any other Federal agency) presently has a direct or indirect interest, including gold that may be held by third parties, including, for example, the Bank for International Settlements, the International Monetary Fund, the Exchange Stabilization Fund, any foreign central bank, or any other party, public or private.\n##### (b) Report\nNot later than 3 months after the completion of each assay, inventory, audit, analysis, and accounting required under subsection (a), the Comptroller General shall issue a report to the Congress and the Secretary of the Treasury containing all results, findings, and determinations made in carrying out the assay, inventory, audit, analysis, and accounting, and promptly make such report (together with copies of all source materials relied upon) available to the public on the internet. No redactions shall be permitted except with respect to underlying details contained in the analysis completed under subsection (a)(2) dealing only with physical security.\n##### (c) GAO access\nFor purposes of carrying out this Act, the Comptroller General, and any external auditor contracting with the Comptroller General under subsection (a), shall have full access (enforceable by the Comptroller General by subpoena authority) to any depository or other public or private facility where such reserves are kept or where any records are kept that are necessary to carry out this Act.\n##### (d) Information made available by Treasury\nThe Secretary of the Treasury (and all other Federal agencies, including the Board of Governors of the Federal Reserve System) shall make available, without any redactions, to the Comptroller General, for purposes of carrying out this Act, all books, accounts, records, reports, files, correspondence, memoranda, papers, or any other document, tape, or written, audio, or digital record pertaining to the assay, inventory, audit, analysis, and accounting required under subsection (a), as determined by the Comptroller General.",
      "versionDate": "2025-06-06",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3218",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Gold Reserve Transparency Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-07-18T13:12:42Z"
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
      "date": "2025-06-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3795ih.xml"
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
      "title": "Gold Reserve Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-12T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gold Reserve Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T06:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the first true audit of gold owned by the United States in more than 65 years and to conduct subsequent audits every 5 years.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T06:18:26Z"
    }
  ]
}
```
