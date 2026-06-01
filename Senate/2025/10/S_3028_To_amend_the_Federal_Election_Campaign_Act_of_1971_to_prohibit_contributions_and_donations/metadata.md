# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3028?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3028
- Title: Protecting Ballot Measures From Foreign Influence Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3028
- Origin chamber: Senate
- Introduced date: 2025-10-22
- Update date: 2026-04-08T16:14:02Z
- Update date including text: 2026-04-08T16:14:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-22: Introduced in Senate
- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-10-22: Introduced in Senate

## Actions

- 2025-10-22 - IntroReferral: Introduced in Senate
- 2025-10-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-22",
    "latestAction": {
      "actionDate": "2025-10-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3028",
    "number": "3028",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T16:14:02Z",
    "updateDateIncludingText": "2026-04-08T16:14:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-22",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-22",
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
          "date": "2025-10-22T19:50:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-10-22",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3028is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3028\nIN THE SENATE OF THE UNITED STATES\nOctober 22 (legislative day, October 21), 2025 Mr. Banks (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit contributions and donations by foreign nationals in connection with ballot initiatives and referenda.\n#### 1. Short title\nThis Act may be cited as the Protecting Ballot Measures From Foreign Influence Act of 2025 .\n#### 2. Prohibition on contributions and donations by foreign nationals in connection with ballot initiatives and referenda\n##### (a) Prohibition\nSection 319(a)(1)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(a)(1)(A) ) is amended by inserting , or a State or local ballot initiative or ballot referendum after election .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to contributions and donations made on or after the date of enactment of this Act.",
      "versionDate": "2025-10-22",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-12-16",
        "text": "Referred to the House Committee on House Administration."
      },
      "number": "6738",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
      "type": "HR"
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-05T22:06:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-22",
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
          "measure-id": "id119s3028",
          "measure-number": "3028",
          "measure-type": "s",
          "orig-publish-date": "2025-10-22",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3028v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-10-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>"
        },
        "title": "Protecting Ballot Measures From Foreign Influence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3028.xml",
    "summary": {
      "actionDate": "2025-10-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3028"
    },
    "title": "Protecting Ballot Measures From Foreign Influence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3028"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3028is.xml"
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
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-24T02:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Election Campaign Act of 1971 to prohibit contributions and donations by foreign nationals in connection with ballot initiatives and referenda.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-24T02:18:19Z"
    }
  ]
}
```
