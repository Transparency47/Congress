# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/215?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/215
- Title: Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act
- Congress: 119
- Bill type: S
- Bill number: 215
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2025-12-06T07:04:59Z
- Update date including text: 2025-12-06T07:04:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/215",
    "number": "215",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act",
    "type": "S",
    "updateDate": "2025-12-06T07:04:59Z",
    "updateDateIncludingText": "2025-12-06T07:04:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T18:24:18Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TN"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "AL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s215is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 215\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Cruz (for himself, Mrs. Blackburn , Mrs. Britt , Mr. Scott of Florida , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country\u201d.\n#### 1. Short title\nThis Act may be cited as the Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that the principles of Duty, Honor, Country should be\u2014\n**(1)**\ndeeply embedded in the ethos of the United States Military Academy; and\n**(2)**\ninstilled in each cadet.\n#### 3. Modification of united states military academy mission statement\nNot later than 30 days after the date of the enactment of this Act, the Secretary of the Army shall amend the mission statement of the United States Military Academy to include the phrase Duty, Honor, Country .",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-01-23",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "700",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "MACARTHUR Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Higher education",
            "updateDate": "2025-03-20T13:41:45Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-03-20T13:41:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T19:24:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119s215",
          "measure-number": "215",
          "measure-type": "s",
          "orig-publish-date": "2025-01-23",
          "originChamber": "SENATE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s215v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>"
        },
        "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s215.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s215"
    },
    "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119s215"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s215is.xml"
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
      "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:56Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the mission statement of the United States Military Academy to include the phrase \"Duty, Honor, Country\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:05Z"
    }
  ]
}
```
