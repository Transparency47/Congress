# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3110?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3110
- Title: PFAS–Free Procurement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3110
- Origin chamber: House
- Introduced date: 2025-04-30
- Update date: 2026-05-08T08:06:52Z
- Update date including text: 2026-05-08T08:06:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-04-30: Introduced in House

## Actions

- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Introduced in House
- 2025-04-30 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3110",
    "number": "3110",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "PFAS\u2013Free Procurement Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:52Z",
    "updateDateIncludingText": "2026-05-08T08:06:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-30",
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
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T14:01:05Z",
          "name": "Referred To"
        }
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NH"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "ME"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "ME"
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
      "sponsorshipDate": "2025-07-21",
      "state": "VA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-13",
      "state": "NV"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CO"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3110ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3110\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2025 Mr. Lawler (for himself, Mr. Fitzpatrick , Mr. Ryan , Ms. Stevens , Mr. Pappas , Ms. Tlaib , and Ms. Pingree ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the procurement of certain items containing perfluorooctane sulfonate or perfluorooctanoic acid and prioritize the procurement of products not containing PFAS.\n#### 1. Short title\nThis Act may be cited as the PFAS\u2013Free Procurement Act of 2025 .\n#### 2. Prohibition on procurement of certain items containing PFOS or PFOA\n##### (a) Prohibition\nThe head of an executive agency may not renew or enter into a contract for the procurement of a covered item that contains PFOS or PFOA.\n##### (b) Priority procurement of products not containing pfas\nThe head of an executive agency shall prioritize the procurement of covered items, where available and practicable, that do not contain PFAS.\n##### (c) Definitions\nIn this section:\n**(1) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(2) Covered item**\nThe term covered item means\u2014\n**(A)**\nnonstick cookware and a cooking utensil; and\n**(B)**\nfurniture, carpet, and any rug treated with stain-resistant coating.\n**(3) PFAS**\nThe term PFAS means harmful perfluoroalkyl or polyfluoroalkyl substances.\n**(4) PFOA**\nThe term PFOA means perfluorooctanoic acid.\n**(5) PFOS**\nThe term PFOS means perfluorooctane sulfonate.\n##### (d) Applicability\nThis section shall take effect 6 months after the date of the enactment of this Act and shall apply with respect to any contract entered into on and after such effective date.",
      "versionDate": "2025-04-30",
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
        "name": "Environmental Protection",
        "updateDate": "2025-05-29T18:04:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119hr3110",
          "measure-number": "3110",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-30",
          "originChamber": "HOUSE",
          "update-date": "2025-08-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3110v00",
            "update-date": "2025-08-04"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>PFAS\u2013Free Procurement Act of 2025</strong></p><p>This bill prohibits an executive agency from renewing or entering into a contract for the procurement of covered items that contain\u00a0perfluorooctane sulfonate (PFOS) or perfluorooctanoic acid (PFOA). Under the bill, <em>covered items </em>means (1) nonstick cookware and cooking utensils; and (2) furniture, carpet, and any rug treated with stain-resistant coating.\u00a0Both PFOS and PFOA are types of\u00a0per- and\u00a0polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>The bill also specifies that agencies must prioritize the procurement of covered items that do not contain\u00a0PFAS.</p>"
        },
        "title": "PFAS\u2013Free Procurement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3110.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PFAS\u2013Free Procurement Act of 2025</strong></p><p>This bill prohibits an executive agency from renewing or entering into a contract for the procurement of covered items that contain\u00a0perfluorooctane sulfonate (PFOS) or perfluorooctanoic acid (PFOA). Under the bill, <em>covered items </em>means (1) nonstick cookware and cooking utensils; and (2) furniture, carpet, and any rug treated with stain-resistant coating.\u00a0Both PFOS and PFOA are types of\u00a0per- and\u00a0polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>The bill also specifies that agencies must prioritize the procurement of covered items that do not contain\u00a0PFAS.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hr3110"
    },
    "title": "PFAS\u2013Free Procurement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>PFAS\u2013Free Procurement Act of 2025</strong></p><p>This bill prohibits an executive agency from renewing or entering into a contract for the procurement of covered items that contain\u00a0perfluorooctane sulfonate (PFOS) or perfluorooctanoic acid (PFOA). Under the bill, <em>covered items </em>means (1) nonstick cookware and cooking utensils; and (2) furniture, carpet, and any rug treated with stain-resistant coating.\u00a0Both PFOS and PFOA are types of\u00a0per- and\u00a0polyfluoroalkyl substances, commonly known as PFAS. PFAS are man-made and may have adverse human health effects.</p><p>The bill also specifies that agencies must prioritize the procurement of covered items that do not contain\u00a0PFAS.</p>",
      "updateDate": "2025-08-04",
      "versionCode": "id119hr3110"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3110ih.xml"
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
      "title": "PFAS\u2013Free Procurement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:41Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PFAS\u2013Free Procurement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the procurement of certain items containing perfluorooctane sulfonate or perfluorooctanoic acid and prioritize the procurement of products not containing PFAS.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:33:24Z"
    }
  ]
}
```
