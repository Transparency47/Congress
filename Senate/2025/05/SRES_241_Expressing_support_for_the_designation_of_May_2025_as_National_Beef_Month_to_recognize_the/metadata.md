# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/241?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/241
- Title: A resolution expressing support for the designation of May 2025 as "National Beef Month" to recognize the important role cattle play in the United States, and to consumers.
- Congress: 119
- Bill type: SRES
- Bill number: 241
- Origin chamber: Senate
- Introduced date: 2025-05-21
- Update date: 2026-04-03T12:27:12Z
- Update date including text: 2026-04-03T12:27:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in Senate
- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S3064)
- Latest action: 2025-05-21: Introduced in Senate

## Actions

- 2025-05-21 - IntroReferral: Introduced in Senate
- 2025-05-21 - IntroReferral: Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S3064)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/241",
    "number": "241",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "A resolution expressing support for the designation of May 2025 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
    "type": "SRES",
    "updateDate": "2026-04-03T12:27:12Z",
    "updateDateIncludingText": "2026-04-03T12:27:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S3064)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T17:28:51Z",
          "name": "Referred To"
        }
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "KS"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
      "state": "NE"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres241is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 241\nIN THE SENATE OF THE UNITED STATES\nMay 21, 2025 Mr. Ricketts (for himself, Mr. Marshall , Mrs. Fischer , and Mr. Cornyn ) submitted the following resolution; which was referred to the Committee on Agriculture, Nutrition, and Forestry\nRESOLUTION\nExpressing support for the designation of May 2025 as National Beef Month to recognize the important role cattle play in the United States, and to consumers.\nThat the Senate\u2014\n**(1)**\nsupports the designation of May 2025 as National Beef Month ; and\n**(2)**\nrecognizes that\u2014\n**(A)**\nhistorically, cattle production has contributed about 17 percent of the $520,000,000,000 in total cash receipts for agricultural commodities;\n**(B)**\nthe United States is also the largest consumer of beef in the world, primarily high-value, grain-fed beef; and\n**(C)**\nbeef is an excellent source of nutritious protein.",
      "versionDate": "2025-05-21",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-10T23:24:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119sres241",
          "measure-number": "241",
          "measure-type": "sres",
          "orig-publish-date": "2025-05-21",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres241v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution supports the designation of May 2025 as National Beef Month.</p>"
        },
        "title": "A resolution expressing support for the designation of May 2025 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres241.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of May 2025 as National Beef Month.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres241"
    },
    "title": "A resolution expressing support for the designation of May 2025 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers."
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution supports the designation of May 2025 as National Beef Month.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119sres241"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres241is.xml"
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
      "title": "A resolution expressing support for the designation of May 2025 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T03:33:30Z"
    },
    {
      "title": "A resolution expressing support for the designation of May 2025 as \"National Beef Month\" to recognize the important role cattle play in the United States, and to consumers.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-22T12:15:51Z"
    }
  ]
}
```
