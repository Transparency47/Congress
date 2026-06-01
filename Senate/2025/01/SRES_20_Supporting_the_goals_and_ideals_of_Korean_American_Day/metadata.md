# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/20?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/20
- Title: A resolution supporting the goals and ideals of Korean American Day.
- Congress: 119
- Bill type: SRES
- Bill number: 20
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Referred to the Committee on the Judiciary.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/20",
    "number": "20",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "A resolution supporting the goals and ideals of Korean American Day.",
    "type": "SRES",
    "updateDate": "2025-07-21T19:32:26Z",
    "updateDateIncludingText": "2025-07-21T19:32:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T22:16:30Z",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "HI"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-01-13",
      "state": "AK"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "NJ"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "NY"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres20is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 20\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Kim (for himself, Ms. Hirono , Mr. Sullivan , Mr. Booker , Mr. Schumer , and Mr. Schatz ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nSupporting the goals and ideals of Korean American Day.\nThat the Senate\u2014\n**(1)**\nsupports the goals and ideals of Korean American Day;\n**(2)**\nurges all individuals in the United States to observe Korean American Day so as to have a greater appreciation of the invaluable contributions Korean Americans have made to the United States; and\n**(3)**\nhonors and recognizes the 122nd anniversary of the arrival of the first Korean immigrants to the United States.",
      "versionDate": "2025-01-13",
      "versionType": "IS"
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
        "actionDate": "2025-01-13",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "33",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Supporting the goals and ideals of Korean American Day.",
      "type": "HRES"
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
            "name": "Asia",
            "updateDate": "2025-01-23T15:59:28Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-01-23T15:59:28Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-01-23T15:59:28Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-01-23T15:59:28Z"
          },
          {
            "name": "South Korea",
            "updateDate": "2025-01-23T15:59:28Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-01-23T15:59:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-01-16T16:51:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119sres20",
          "measure-number": "20",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres20v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution\u00a0honors the 122nd anniversary of\u00a0the arrival of\u00a0Korean immigrants to the United States and urges all individuals in the United States to observe Korean American Day.</p>"
        },
        "title": "A resolution supporting the goals and ideals of Korean American Day."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres20.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution\u00a0honors the 122nd anniversary of\u00a0the arrival of\u00a0Korean immigrants to the United States and urges all individuals in the United States to observe Korean American Day.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119sres20"
    },
    "title": "A resolution supporting the goals and ideals of Korean American Day."
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution\u00a0honors the 122nd anniversary of\u00a0the arrival of\u00a0Korean immigrants to the United States and urges all individuals in the United States to observe Korean American Day.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119sres20"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres20is.xml"
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
      "title": "A resolution supporting the goals and ideals of Korean American Day.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-15T00:18:22Z"
    },
    {
      "title": "A resolution supporting the goals and ideals of Korean American Day.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-14T11:56:19Z"
    }
  ]
}
```
