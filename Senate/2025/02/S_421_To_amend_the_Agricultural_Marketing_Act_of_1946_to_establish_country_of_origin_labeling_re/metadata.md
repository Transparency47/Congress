# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/421?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/421
- Title: American Beef Labeling Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 421
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2026-01-13T12:03:23Z
- Update date including text: 2026-01-13T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S668)
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S668)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/421",
    "number": "421",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000250",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Thune, John [R-SD]",
        "lastName": "Thune",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "American Beef Labeling Act of 2025",
    "type": "S",
    "updateDate": "2026-01-13T12:03:23Z",
    "updateDateIncludingText": "2026-01-13T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S668)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
            "date": "2025-02-05T20:25:09Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-05T20:25:09Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NJ"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "SD"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "WY"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "PA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "ND"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NM"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "UT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-05",
      "state": "MS"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s421is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 421\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Thune (for himself, Mr. Booker , Mr. Rounds , Mr. Heinrich , Ms. Lummis , Mr. Fetterman , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Marketing Act of 1946 to establish country of origin labeling requirements for beef, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Beef Labeling Act of 2025 .\n#### 2. Country of origin labeling for beef\n##### (a) Definitions\nSection 281 of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1) through (7) as paragraphs (2) through (8), respectively;\n**(2)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Beef The term beef means meat produced from cattle (including veal). ; and\n**(3)**\nin subparagraph (A) of paragraph (2) (as so redesignated)\u2014\n**(A)**\nin clause (i), by inserting , beef, after lamb ; and\n**(B)**\nin clause (ii), by inserting , ground beef, after lamb .\n##### (b) Notice of country of origin\nSection 282(a)(2) of the Agricultural Marketing Act of 1946 ( 7 U.S.C. 1638a(a)(2) ) is amended\u2014\n**(1)**\nin the paragraph heading, by inserting beef, after for ;\n**(2)**\nin each of subparagraphs (A) through (D), by inserting beef, before lamb each place it appears; and\n**(3)**\nin subparagraph (E)\u2014\n**(A)**\nin the subparagraph heading, by inserting beef, after Ground ; and\n**(B)**\nby inserting ground beef, before ground lamb each place it appears.\n##### (c) Means of reinstating MCOOL for beef\n**(1) Determination of means**\nNot later than 180 days after the date of enactment of this Act, the United States Trade Representative, in consultation with the Secretary of Agriculture, shall determine a means of reinstating mandatory country of origin labeling for beef in accordance with the amendments made by subsections (a) and (b) that is in compliance with all applicable rules of the World Trade Organization.\n**(2) Implementation of means**\nNot later than 1 year after the date of enactment of this Act, the United States Trade Representative and the Secretary of Agriculture shall implement the means determined under paragraph (1).\n##### (d) Effective date\nThe amendments made by subsections (a) and (b) take effect on the earlier of\u2014\n**(1)**\nthe date on which the Secretary of Agriculture publishes a determination in the Federal Register that the means determined under paragraph (1) of subsection (c) have been implemented under paragraph (2) of that subsection; and\n**(2)**\nthe date that is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-02-05",
      "versionType": "Introduced in Senate"
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-01T20:16:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-05",
    "originChamber": "Senate",
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
          "measure-id": "id119s421",
          "measure-number": "421",
          "measure-type": "s",
          "orig-publish-date": "2025-02-05",
          "originChamber": "SENATE",
          "update-date": "2025-05-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s421v00",
            "update-date": "2025-05-27"
          },
          "action-date": "2025-02-05",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>American Beef Labeling Act of 2025</strong></p><p>This bill reinstates mandatory country-of-origin labeling (COOL) requirements for beef.\u00a0COOL\u00a0is a labeling law that requires retailers, such as full-line grocery stores, supermarkets, and club warehouse stores, to provide information to\u00a0customers regarding the source of certain foods.</p><p>Specifically, the bill requires the Office of the U.S. Trade Representative (USTR),\u00a0in consultation with the Department of Agriculture (USDA), to determine a means of reinstating mandatory\u00a0COOL for beef that is compliant with World Trade Organization rules.\u00a0The USTR and USDA must implement the means of reinstating mandatory COOL for beef within one year\u00a0of the bill's enactment.</p>"
        },
        "title": "American Beef Labeling Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s421.xml",
    "summary": {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Beef Labeling Act of 2025</strong></p><p>This bill reinstates mandatory country-of-origin labeling (COOL) requirements for beef.\u00a0COOL\u00a0is a labeling law that requires retailers, such as full-line grocery stores, supermarkets, and club warehouse stores, to provide information to\u00a0customers regarding the source of certain foods.</p><p>Specifically, the bill requires the Office of the U.S. Trade Representative (USTR),\u00a0in consultation with the Department of Agriculture (USDA), to determine a means of reinstating mandatory\u00a0COOL for beef that is compliant with World Trade Organization rules.\u00a0The USTR and USDA must implement the means of reinstating mandatory COOL for beef within one year\u00a0of the bill's enactment.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s421"
    },
    "title": "American Beef Labeling Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-05",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>American Beef Labeling Act of 2025</strong></p><p>This bill reinstates mandatory country-of-origin labeling (COOL) requirements for beef.\u00a0COOL\u00a0is a labeling law that requires retailers, such as full-line grocery stores, supermarkets, and club warehouse stores, to provide information to\u00a0customers regarding the source of certain foods.</p><p>Specifically, the bill requires the Office of the U.S. Trade Representative (USTR),\u00a0in consultation with the Department of Agriculture (USDA), to determine a means of reinstating mandatory\u00a0COOL for beef that is compliant with World Trade Organization rules.\u00a0The USTR and USDA must implement the means of reinstating mandatory COOL for beef within one year\u00a0of the bill's enactment.</p>",
      "updateDate": "2025-05-27",
      "versionCode": "id119s421"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s421is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "American Beef Labeling Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-13T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "American Beef Labeling Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Marketing Act of 1946 to establish country of origin labeling requirements for beef, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:53Z"
    }
  ]
}
```
