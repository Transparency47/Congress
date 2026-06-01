# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/137?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/137
- Title: A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.
- Congress: 119
- Bill type: SRES
- Bill number: 137
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-06T07:09:09Z
- Update date including text: 2025-12-06T07:09:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1838)
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S1838)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/137",
    "number": "137",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.",
    "type": "SRES",
    "updateDate": "2025-12-06T07:09:09Z",
    "updateDateIncludingText": "2025-12-06T07:09:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S1838)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T22:59:54Z",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres137is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 137\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Tuberville (for himself and Mrs. Britt ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCommending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.\nThat the Senate\u2014\n**(1)**\ncommends Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States;\n**(2)**\nrecognizes Volkert, Inc. for its significant contributions to engineering, infrastructure, and economic development; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe Chief Executive Officer and Chairman of the Board of Volkert, Inc., Mr. Thomas Hand; and\n**(B)**\nthe President and Chief Operating Officer of Volkert, Inc., Mr. Leon Barkan.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "330",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.",
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
        "updateDate": "2025-03-31T13:18:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119sres137",
          "measure-number": "137",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres137v00",
            "update-date": "2025-04-02"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution recognizes Volkert, Inc., headquartered in Alabama, for its 100th anniversary and its contributions to engineering, infrastructure, and economic development.</p>"
        },
        "title": "A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres137.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes Volkert, Inc., headquartered in Alabama, for its 100th anniversary and its contributions to engineering, infrastructure, and economic development.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119sres137"
    },
    "title": "A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution recognizes Volkert, Inc., headquartered in Alabama, for its 100th anniversary and its contributions to engineering, infrastructure, and economic development.</p>",
      "updateDate": "2025-04-02",
      "versionCode": "id119sres137"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres137is.xml"
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
      "title": "A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T10:48:21Z"
    },
    {
      "title": "A resolution commending Volkert, Inc. on the occasion of its 100th anniversary and its century of service to the State of Alabama and the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T10:56:17Z"
    }
  ]
}
```
