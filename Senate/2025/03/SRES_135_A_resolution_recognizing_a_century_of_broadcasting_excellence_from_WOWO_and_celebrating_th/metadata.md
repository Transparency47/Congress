# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/135?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sres/135
- Title: A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.
- Congress: 119
- Bill type: SRES
- Bill number: 135
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-07-16T15:16:03Z
- Update date including text: 2025-07-16T15:16:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S1837)
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S1837)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sres/135",
    "number": "135",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
    "type": "SRES",
    "updateDate": "2025-07-16T15:16:03Z",
    "updateDateIncludingText": "2025-07-16T15:16:03Z"
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
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S1837)",
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
          "date": "2025-03-25T19:40:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres135is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 135\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Banks (for himself and Mr. Young ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nA resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station\u2019s 100th anniversary.\nThat the Senate\u2014\n**(1)**\ncelebrates March 31, 2025, as WOWO\u2019s 100th anniversary on air;\n**(2)**\nrecognizes WOWO\u2019s record of exemplary broadcasting, which has strengthened communities and educated countless families on the most important issues; and\n**(3)**\nsupports WOWO\u2019s efforts to continue informing and inspiring generations to come.",
      "versionDate": "2025-03-25",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-03-28T13:23:04Z"
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
          "measure-id": "id119sres135",
          "measure-number": "135",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-07-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres135v00",
            "update-date": "2025-07-16"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution celebrates March 31, 2025, as the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>"
        },
        "title": "A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres135.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution celebrates March 31, 2025, as the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119sres135"
    },
    "title": "A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary."
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution celebrates March 31, 2025, as the 100th anniversary of the Fort Wayne, Indiana radio station WOWO.\u00a0</p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119sres135"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres135is.xml"
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
      "title": "A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T04:18:20Z"
    },
    {
      "title": "A resolution recognizing a century of broadcasting excellence from WOWO and celebrating the radio station's 100th anniversary.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T10:56:22Z"
    }
  ]
}
```
