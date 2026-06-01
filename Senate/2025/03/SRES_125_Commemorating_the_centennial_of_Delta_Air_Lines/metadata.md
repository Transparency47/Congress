# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/125?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/125
- Title: A resolution commemorating the centennial of Delta Air Lines.
- Congress: 119
- Bill type: SRES
- Bill number: 125
- Origin chamber: Senate
- Introduced date: 2025-03-12
- Update date: 2025-07-21T19:32:26Z
- Update date including text: 2025-07-21T19:32:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-12: Introduced in Senate
- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1716)
- Latest action: 2025-03-12: Introduced in Senate

## Actions

- 2025-03-12 - IntroReferral: Introduced in Senate
- 2025-03-12 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1716)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-12",
    "latestAction": {
      "actionDate": "2025-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/125",
    "number": "125",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "A resolution commemorating the centennial of Delta Air Lines.",
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
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1716)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-12",
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
          "date": "2025-03-12T17:14:37Z",
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
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "UT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-12",
      "state": "GA"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-12",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres125is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 125\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2025 Mr. Ossoff (for himself, Mr. Curtis , Mr. Warnock , and Mr. Lee ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommemorating the centennial of Delta Air Lines.\nThat the Senate\u2014\n**(1)**\nrecognizes Delta Air Lines for 100 years of connecting people to the world and to each other; and\n**(2)**\ncommemorates the centennial of Delta Air Lines.",
      "versionDate": "2025-03-12",
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
        "actionDate": "2025-03-14",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "226",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Commemorating the centennial of Delta Air Lines.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-03-17T17:44:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-12",
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
          "measure-id": "id119sres125",
          "measure-number": "125",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-12",
          "originChamber": "SENATE",
          "update-date": "2025-04-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres125v00",
            "update-date": "2025-04-21"
          },
          "action-date": "2025-03-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution commemorates the centennial of Delta Air Lines.</p>"
        },
        "title": "A resolution commemorating the centennial of Delta Air Lines."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres125.xml",
    "summary": {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution commemorates the centennial of Delta Air Lines.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119sres125"
    },
    "title": "A resolution commemorating the centennial of Delta Air Lines."
  },
  "summaries": [
    {
      "actionDate": "2025-03-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution commemorates the centennial of Delta Air Lines.</p>",
      "updateDate": "2025-04-21",
      "versionCode": "id119sres125"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres125is.xml"
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
      "title": "A resolution commemorating the centennial of Delta Air Lines.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T03:18:23Z"
    },
    {
      "title": "A resolution commemorating the centennial of Delta Air Lines.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T10:56:33Z"
    }
  ]
}
```
