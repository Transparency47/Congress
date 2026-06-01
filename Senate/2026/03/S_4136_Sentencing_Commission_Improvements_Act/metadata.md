# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4136?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4136
- Title: Sentencing Commission Improvements Act
- Congress: 119
- Bill type: S
- Bill number: 4136
- Origin chamber: Senate
- Introduced date: 2026-03-18
- Update date: 2026-04-03T15:49:53Z
- Update date including text: 2026-04-03T15:49:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-18: Introduced in Senate
- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-03-18: Introduced in Senate

## Actions

- 2026-03-18 - IntroReferral: Introduced in Senate
- 2026-03-18 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4136",
    "number": "4136",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Sentencing Commission Improvements Act",
    "type": "S",
    "updateDate": "2026-04-03T15:49:53Z",
    "updateDateIncludingText": "2026-04-03T15:49:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T20:28:36Z",
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
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4136is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4136\nIN THE SENATE OF THE UNITED STATES\nMarch 18, 2026 Mr. Booker (for himself and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo include a Federal defender as a nonvoting member of the United States Sentencing Commission.\n#### 1. Short title\nThis Act may be cited as the Sentencing Commission Improvements Act .\n#### 2. Federal defender as a nonvoting member of the United States Sentencing Commission\n##### (a) In general\nSection 991(a) of title 28, United States Code, is amended\u2014\n**(1)**\nin the first sentence, by striking one nonvoting member and inserting 2 nonvoting members ; and\n**(2)**\nin the fifth sentence, by striking shall be an ex officio, nonvoting member and inserting and a Federal public defender, or a community defender, designated by the Defender Services Office of the Administrative Office of the United States Courts, shall be ex officio, nonvoting members .\n##### (b) Conforming amendment\nSection 235(b)(5) of the Sentencing Reform Act of 1984 ( 18 U.S.C. 3551 note) is amended, in the third sentence, by striking nine members, including two and inserting 10 members, including 3 .",
      "versionDate": "2026-03-18",
      "versionType": "Introduced in Senate"
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-04-01T17:54:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-18",
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
          "measure-id": "id119s4136",
          "measure-number": "4136",
          "measure-type": "s",
          "orig-publish-date": "2026-03-18",
          "originChamber": "SENATE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s4136v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2026-03-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Sentencing Commission Improvements Act</strong></p> <p>This bill adds one nonvoting member to the U.S. Sentencing Commission and requires the new member to be a public defender.<br/> </p>"
        },
        "title": "Sentencing Commission Improvements Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s4136.xml",
    "summary": {
      "actionDate": "2026-03-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sentencing Commission Improvements Act</strong></p> <p>This bill adds one nonvoting member to the U.S. Sentencing Commission and requires the new member to be a public defender.<br/> </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4136"
    },
    "title": "Sentencing Commission Improvements Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Sentencing Commission Improvements Act</strong></p> <p>This bill adds one nonvoting member to the U.S. Sentencing Commission and requires the new member to be a public defender.<br/> </p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119s4136"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4136is.xml"
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
      "title": "Sentencing Commission Improvements Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T04:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Sentencing Commission Improvements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to include a Federal defender as a nonvoting member of the United States Sentencing Commission.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T04:18:41Z"
    }
  ]
}
```
