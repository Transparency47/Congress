# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/35?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/35
- Title: A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 35
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S372)
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S372)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/35",
    "number": "35",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States.",
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
      "actionDate": "2025-01-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S372)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T19:19:32Z",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres35is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 35\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Ms. Lummis (for herself and Mr. Barrasso ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nHonoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States.\nThat the Senate\u2014\n**(1)**\nrecognizes and commemorates the legacy of Governor Nellie Tayloe Ross (referred to in this resolution as Governor Ross ) and her groundbreaking role as the first female elected as the Governor of a State in the United States;\n**(2)**\ncelebrates the lasting contributions of Governor Ross to the advancement of women in leadership positions; and\n**(3)**\ncalls on the citizens of the United States to join in the observance of January, 2025, as the 100th anniversary of the pioneering spirit of Governor Ross, whose work continues to inspire and empower women in the political arena and beyond.",
      "versionDate": "2025-01-24",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-03-27T14:51:04Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-03-27T14:51:33Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-27T14:51:15Z"
          },
          {
            "name": "Women's rights",
            "updateDate": "2025-03-27T14:51:28Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2025-03-27T14:51:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-19T19:23:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119sres35",
          "measure-number": "35",
          "measure-type": "sres",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres35v00",
            "update-date": "2025-03-04"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution commemorates the legacy of Governor Nellie Tayloe Ross, the first female elected as a state governor in the United States. (Governor Ross was the 14th state governor of Wyoming, inaugurated on January 5, 1925.) The resolution celebrates the contributions of Governor Ross to the advancement of women in leadership positions and calls on U.S. citizens to observe January 2025 as the 100th anniversary of Governor Ross' pioneering spirit.</p>"
        },
        "title": "A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres35.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution commemorates the legacy of Governor Nellie Tayloe Ross, the first female elected as a state governor in the United States. (Governor Ross was the 14th state governor of Wyoming, inaugurated on January 5, 1925.) The resolution celebrates the contributions of Governor Ross to the advancement of women in leadership positions and calls on U.S. citizens to observe January 2025 as the 100th anniversary of Governor Ross' pioneering spirit.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119sres35"
    },
    "title": "A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution commemorates the legacy of Governor Nellie Tayloe Ross, the first female elected as a state governor in the United States. (Governor Ross was the 14th state governor of Wyoming, inaugurated on January 5, 1925.) The resolution celebrates the contributions of Governor Ross to the advancement of women in leadership positions and calls on U.S. citizens to observe January 2025 as the 100th anniversary of Governor Ross' pioneering spirit.</p>",
      "updateDate": "2025-03-04",
      "versionCode": "id119sres35"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres35is.xml"
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
      "title": "A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-28T01:48:23Z"
    },
    {
      "title": "A resolution honoring the 100th anniversary of Nellie Tayloe Ross becoming the first female elected as the Governor of a State in the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-25T11:56:21Z"
    }
  ]
}
```
