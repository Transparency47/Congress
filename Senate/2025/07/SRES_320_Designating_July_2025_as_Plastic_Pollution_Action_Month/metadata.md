# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/320?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/320
- Title: A resolution designating July 2025 as "Plastic Pollution Action Month".
- Congress: 119
- Bill type: SRES
- Bill number: 320
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-04-06T19:26:51Z
- Update date including text: 2026-04-06T19:26:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4338)
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S4338)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/320",
    "number": "320",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "A resolution designating July 2025 as \"Plastic Pollution Action Month\".",
    "type": "SRES",
    "updateDate": "2026-04-06T19:26:51Z",
    "updateDateIncludingText": "2026-04-06T19:26:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S4338)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-14",
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
          "date": "2025-07-14T21:01:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-07-14",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "IL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "MD"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres320is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 320\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Mr. Merkley (for himself, Mr. Booker , Ms. Duckworth , Mr. Van Hollen , Mr. Welch , and Mr. Whitehouse ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating July 2025 as Plastic Pollution Action Month .\nThat the Senate\u2014\n**(1)**\ndesignates July 2025 as Plastic Pollution Action Month ;\n**(2)**\nrecognizes the dangers to human health and the environment posed by plastic pollution; and\n**(3)**\nencourages all individuals in the United States to protect, conserve, maintain, and rebuild public health and the environment by responsibly participating in activities to reduce plastic pollution in July 2025 and year-round.",
      "versionDate": "2025-07-14",
      "versionType": "IS"
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
        "updateDate": "2025-07-25T12:11:22Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-14",
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
          "measure-id": "id119sres320",
          "measure-number": "320",
          "measure-type": "sres",
          "orig-publish-date": "2025-07-14",
          "originChamber": "SENATE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres320v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates July 2025 as Plastic Pollution Action Month.</p>"
        },
        "title": "A resolution designating July 2025 as \"Plastic Pollution Action Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres320.xml",
    "summary": {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates July 2025 as Plastic Pollution Action Month.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres320"
    },
    "title": "A resolution designating July 2025 as \"Plastic Pollution Action Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates July 2025 as Plastic Pollution Action Month.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119sres320"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres320is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution designating July 2025 as \"Plastic Pollution Action Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:23Z"
    },
    {
      "title": "A resolution designating July 2025 as \"Plastic Pollution Action Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-15T10:56:19Z"
    }
  ]
}
```
