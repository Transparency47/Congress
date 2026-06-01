# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/965?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/965
- Title: A bill to strengthen the United States Interagency Council on Homelessness.
- Congress: 119
- Bill type: S
- Bill number: 965
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-04-01T20:49:25Z
- Update date including text: 2026-04-01T20:49:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666)
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/965",
    "number": "965",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A bill to strengthen the United States Interagency Council on Homelessness.",
    "type": "S",
    "updateDate": "2026-04-01T20:49:25Z",
    "updateDateIncludingText": "2026-04-01T20:49:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1666)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
        "item": {
          "date": "2025-03-11T22:20:03Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ME"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NV"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s965is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 965\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Reed (for himself, Ms. Collins , Mr. Van Hollen , Ms. Cortez Masto , Ms. Smith , and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo strengthen the United States Interagency Council on Homelessness.\n#### 1. Authorization of appropriations for Interagency Council on Homelessness\n##### (a) In general\nTitle II of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11311 et seq. ) is amended\u2014\n**(1)**\nin section 208 ( 42 U.S.C. 11318 ), by striking to carry out this title $3,000,000 for fiscal year 2010 and such sums as may be necessary for fiscal years 2011 and inserting such sums as may be necessary to carry out this title ;\n**(2)**\nby striking section 209 ( 42 U.S.C. 11319 ); and\n**(3)**\nby redesignating section 210 ( 42 U.S.C. 11320 ) as section 209.\n##### (b) Technical and conforming amendments\nThe table of contents in section 101(b) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11301 note) is amended by striking the items relating to sections 209 and 210 and inserting the following:\nSec. 209. Encouragement of State involvement. .",
      "versionDate": "2025-03-11",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-02-27T20:43:16Z"
          },
          {
            "name": "Homelessness and emergency shelter",
            "updateDate": "2026-02-27T20:43:16Z"
          },
          {
            "name": "Interagency Council on Homelessness",
            "updateDate": "2026-02-27T20:43:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-03-31T13:03:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s965",
          "measure-number": "965",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s965v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill permanently reauthorizes the United States Interagency Council on Homelessness, an independent federal agency within the executive branch that coordinates the federal response to prevent and end homelessness.</p>"
        },
        "title": "A bill to strengthen the United States Interagency Council on Homelessness."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s965.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill permanently reauthorizes the United States Interagency Council on Homelessness, an independent federal agency within the executive branch that coordinates the federal response to prevent and end homelessness.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s965"
    },
    "title": "A bill to strengthen the United States Interagency Council on Homelessness."
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill permanently reauthorizes the United States Interagency Council on Homelessness, an independent federal agency within the executive branch that coordinates the federal response to prevent and end homelessness.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119s965"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s965is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to strengthen the United States Interagency Council on Homelessness.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T10:48:20Z"
    },
    {
      "title": "A bill to strengthen the United States Interagency Council on Homelessness.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T10:56:19Z"
    }
  ]
}
```
