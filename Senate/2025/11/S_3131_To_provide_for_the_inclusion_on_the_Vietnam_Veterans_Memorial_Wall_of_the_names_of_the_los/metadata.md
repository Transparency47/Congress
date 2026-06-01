# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3131
- Title: USS Frank E. Evans Act
- Congress: 119
- Bill type: S
- Bill number: 3131
- Origin chamber: Senate
- Introduced date: 2025-11-06
- Update date: 2026-04-08T17:53:33Z
- Update date including text: 2026-04-08T17:53:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-11-06: Introduced in Senate
- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-11-06: Introduced in Senate

## Actions

- 2025-11-06 - IntroReferral: Introduced in Senate
- 2025-11-06 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-06",
    "latestAction": {
      "actionDate": "2025-11-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3131",
    "number": "3131",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "USS Frank E. Evans Act",
    "type": "S",
    "updateDate": "2026-04-08T17:53:33Z",
    "updateDateIncludingText": "2026-04-08T17:53:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-06",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-06",
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
            "date": "2025-11-06T18:46:42Z",
            "name": "Referred To"
          },
          {
            "date": "2025-11-06T18:46:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-11-06",
      "state": "ND"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-06",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3131is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3131\nIN THE SENATE OF THE UNITED STATES\nNovember 6, 2025 Mr. Schiff (for himself, Mr. Cramer , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo provide for the inclusion on the Vietnam Veterans Memorial Wall of the names of the lost crew members of the USS Frank E. Evans killed on June 3, 1969.\n#### 1. Short title\nThis Act may be cited as the USS Frank E. Evans Act .\n#### 2. Inclusion on the Vietnam Veterans Memorial Wall of the names of the lost crew members of the USS Frank E. Evans killed on June 3, 1969\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Defense shall authorize the inclusion on the Vietnam Veterans Memorial Wall in the District of Columbia of the names of the 74 crew members of the USS Frank E. Evans killed on June 3, 1969.\n##### (b) Required consultation\nThe Secretary of Defense shall consult with the Secretary of the Interior, the Vietnam Veterans Memorial Fund, and other applicable authorities with respect to any adjustments to the nomenclature and placement of names pursuant to subsection (a) to address any space limitations on the placement of additional names on the Vietnam Veterans Memorial Wall.\n##### (c) Nonapplicability of commemorative works act\nChapter 89 of title 40, United States Code (commonly known as the Commemorative Works Act ), shall not apply to any activities carried out under subsection (a) or (b).",
      "versionDate": "2025-11-06",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5945",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "USS Frank E. Evans Act",
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
        "updateDate": "2025-12-02T21:59:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-06",
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
          "measure-id": "id119s3131",
          "measure-number": "3131",
          "measure-type": "s",
          "orig-publish-date": "2025-11-06",
          "originChamber": "SENATE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3131v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-11-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>USS Frank E. Evans Act</b></p> <p>This bill requires the Department of Defense to authorize inclusion on the Vietnam Veterans Memorial Wall in the District of Columbia of the names of the 74 crew members of the USS <i>Frank E. Evans</i> killed on June 3, 1969.</p>"
        },
        "title": "USS Frank E. Evans Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3131.xml",
    "summary": {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>USS Frank E. Evans Act</b></p> <p>This bill requires the Department of Defense to authorize inclusion on the Vietnam Veterans Memorial Wall in the District of Columbia of the names of the 74 crew members of the USS <i>Frank E. Evans</i> killed on June 3, 1969.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3131"
    },
    "title": "USS Frank E. Evans Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>USS Frank E. Evans Act</b></p> <p>This bill requires the Department of Defense to authorize inclusion on the Vietnam Veterans Memorial Wall in the District of Columbia of the names of the 74 crew members of the USS <i>Frank E. Evans</i> killed on June 3, 1969.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119s3131"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3131is.xml"
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
      "title": "USS Frank E. Evans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "USS Frank E. Evans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-11T06:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the inclusion on the Vietnam Veterans Memorial Wall of the names of the lost crew members of the USS Frank E. Evans killed on June 3, 1969.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T06:48:16Z"
    }
  ]
}
```
