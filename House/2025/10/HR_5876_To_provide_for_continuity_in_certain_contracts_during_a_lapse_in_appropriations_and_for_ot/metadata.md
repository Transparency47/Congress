# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5876
- Title: Keep America Building Act
- Congress: 119
- Bill type: HR
- Bill number: 5876
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2025-11-08T09:06:06Z
- Update date including text: 2025-11-08T09:06:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5876",
    "number": "5876",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000481",
        "district": "2",
        "firstName": "Shomari",
        "fullName": "Rep. Figures, Shomari [D-AL-2]",
        "lastName": "Figures",
        "party": "D",
        "state": "AL"
      }
    ],
    "title": "Keep America Building Act",
    "type": "HR",
    "updateDate": "2025-11-08T09:06:06Z",
    "updateDateIncludingText": "2025-11-08T09:06:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "GA"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "IN"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5876ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5876\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Figures (for himself, Mr. Johnson of Georgia , Ms. Pou , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo provide for continuity in certain contracts during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keep America Building Act .\n#### 2. Continuity of contracts\nNo Federal funds may be used to suspend, delay, or interrupt all or part of the work of a project under a contract during any lapse in appropriations or stop all or any part of the work agreed to in such contract.",
      "versionDate": "2025-10-31",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-11-06T14:56:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-31",
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
          "measure-id": "id119hr5876",
          "measure-number": "5876",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-31",
          "originChamber": "HOUSE",
          "update-date": "2025-11-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5876v00",
            "update-date": "2025-11-06"
          },
          "action-date": "2025-10-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Keep America Building Act</strong></p><p>This bill prohibits federal funds from being used to (1) to suspend, delay, or interrupt all or part of the work of a project under a contract during any lapse in appropriations (i.e., government shutdown); or (2) stop all or any part of the work agreed to in the contract.\u00a0</p>"
        },
        "title": "Keep America Building Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5876.xml",
    "summary": {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep America Building Act</strong></p><p>This bill prohibits federal funds from being used to (1) to suspend, delay, or interrupt all or part of the work of a project under a contract during any lapse in appropriations (i.e., government shutdown); or (2) stop all or any part of the work agreed to in the contract.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119hr5876"
    },
    "title": "Keep America Building Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Keep America Building Act</strong></p><p>This bill prohibits federal funds from being used to (1) to suspend, delay, or interrupt all or part of the work of a project under a contract during any lapse in appropriations (i.e., government shutdown); or (2) stop all or any part of the work agreed to in the contract.\u00a0</p>",
      "updateDate": "2025-11-06",
      "versionCode": "id119hr5876"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5876ih.xml"
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
      "title": "Keep America Building Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep America Building Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T10:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for continuity in certain contracts during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T10:48:17Z"
    }
  ]
}
```
