# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3170?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3170
- Title: Stuck On Hold Act
- Congress: 119
- Bill type: S
- Bill number: 3170
- Origin chamber: Senate
- Introduced date: 2025-11-10
- Update date: 2026-04-30T11:03:20Z
- Update date including text: 2026-04-30T11:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-10: Introduced in Senate
- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.
- Latest action: 2025-11-10: Introduced in Senate

## Actions

- 2025-11-10 - IntroReferral: Introduced in Senate
- 2025-11-10 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-04-29 - Committee: Committee on Veterans' Affairs. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3170",
    "number": "3170",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Stuck On Hold Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:20Z",
    "updateDateIncludingText": "2026-04-30T11:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-10",
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
            "date": "2026-04-29T21:37:12Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-11-10T18:53:52Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3170is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3170\nIN THE SENATE OF THE UNITED STATES\nNovember 10, 2025 Mr. Kennedy (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to implement an automated system with callback functionality for each customer service telephone line of the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stuck On Hold Act .\n#### 2. Improvements regarding wait times for callers to certain service telephone lines of the Department of Veterans Affairs\n##### (a) Automated system\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs shall implement, for each covered line, an automated system that\u2014\n**(1)**\ninforms any caller to a covered line about the anticipated wait time, if any; and\n**(2)**\nautomatically offers a callback to any such caller with an anticipated wait time of more than 10 minutes.\n##### (b) Guidance regarding caller wait times\nThe Secretary shall issue such guidance as the Secretary determines necessary to reduce the average wait time of a caller to a covered line to not more than 10 minutes.\n##### (c) Covered line defined\nIn this section, the term covered line \u2014\n**(1)**\nmeans a customer service telephone line of the Department of Veterans Affairs; and\n**(2)**\ndoes not include\u2014\n**(A)**\nthe toll-free hotline for veterans provided by the Secretary under section 1720F(h) of title 38, United States Code; or\n**(B)**\na phone line for the emergency department of a health care facility of the Department.",
      "versionDate": "2025-11-10",
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
        "actionDate": "2025-11-17",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "5992",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stuck On Hold Act",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:59:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-10",
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
          "measure-id": "id119s3170",
          "measure-number": "3170",
          "measure-type": "s",
          "orig-publish-date": "2025-11-10",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3170v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stuck On Hold Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement automated systems for their customer phone lines that inform callers of the expected wait time and that offer callbacks for wait times of more than 10 minutes. The\u00a0VA must also issue guidance to reduce the average wait time to no more than 10 minutes.</p>"
        },
        "title": "Stuck On Hold Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3170.xml",
    "summary": {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stuck On Hold Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement automated systems for their customer phone lines that inform callers of the expected wait time and that offer callbacks for wait times of more than 10 minutes. The\u00a0VA must also issue guidance to reduce the average wait time to no more than 10 minutes.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3170"
    },
    "title": "Stuck On Hold Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stuck On Hold Act</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to implement automated systems for their customer phone lines that inform callers of the expected wait time and that offer callbacks for wait times of more than 10 minutes. The\u00a0VA must also issue guidance to reduce the average wait time to no more than 10 minutes.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3170"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3170is.xml"
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
      "title": "Stuck On Hold Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stuck On Hold Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Veterans Affairs to implement an automated system with callback functionality for each customer service telephone line of the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:15Z"
    }
  ]
}
```
