# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/700?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/700
- Title: MACARTHUR Act
- Congress: 119
- Bill type: HR
- Bill number: 700
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-12-06T07:04:21Z
- Update date including text: 2025-12-06T07:04:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/700",
    "number": "700",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "MACARTHUR Act",
    "type": "HR",
    "updateDate": "2025-12-06T07:04:21Z",
    "updateDateIncludingText": "2025-12-06T07:04:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-23T15:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-02-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr700ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 700\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend the mission statement of the United States Military Academy to include the phrase Duty, Honor, Country .\n#### 1. Short title\nThis Act may be cited as the Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act or the MACARTHUR Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that the principles of Duty, Honor, Country should be\u2014\n**(1)**\ndeeply embedded in the ethos of the United States Military Academy; and\n**(2)**\ninstilled in each cadet.\n#### 3. Modification of united states military academy mission statement\nNot later than 30 days after the date of the enactment of this Act, the Secretary of the Army shall amend the mission statement of the United States Military Academy to include the phrase Duty, Honor, Country .",
      "versionDate": "2025-01-23",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "215",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act (MACARTHUR) Act",
      "type": "S"
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
            "updateDate": "2025-03-20T13:40:42Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-03-20T13:40:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-05T19:48:58Z"
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
    "originChamber": "House",
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
          "measure-id": "id119hr700",
          "measure-number": "700",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr700v00",
            "update-date": "2025-03-18"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act or the\u00a0MACARTHUR\u00a0Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>"
        },
        "title": "MACARTHUR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr700.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act or the\u00a0MACARTHUR\u00a0Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr700"
    },
    "title": "MACARTHUR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act or the\u00a0MACARTHUR\u00a0Act</strong></p><p>This bill requires the Department of the Army to amend the mission statement of the United States Military Academy to include the phrase \u201cDuty, Honor, Country.\u201d</p>",
      "updateDate": "2025-03-18",
      "versionCode": "id119hr700"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr700ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "MACARTHUR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "MACARTHUR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Maintaining Academy Culture and Assuring Retention of Tradition, Honor, and Unity of the Republic Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the mission statement of the United States Military Academy to include the phrase \"Duty, Honor, Country\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:30Z"
    }
  ]
}
```
