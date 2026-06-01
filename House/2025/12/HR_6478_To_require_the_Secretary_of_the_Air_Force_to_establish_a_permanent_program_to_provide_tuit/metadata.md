# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6478
- Title: Air Guard STATUS Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6478
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-04-08T15:28:31Z
- Update date including text: 2026-04-08T15:28:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6478",
    "number": "6478",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001225",
        "district": "17",
        "firstName": "Eric",
        "fullName": "Rep. Sorensen, Eric [D-IL-17]",
        "lastName": "Sorensen",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Air Guard STATUS Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-08T15:28:31Z",
    "updateDateIncludingText": "2026-04-08T15:28:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
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
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:03:30Z",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MN"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "MO"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6478ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6478\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Sorensen (for himself, Mr. Finstad , and Mr. Graves ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of the Air Force to establish a permanent program to provide tuition assistance to members of the Air National Guard.\n#### 1. Short title\nThis Act may be cited as the Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025 .\n#### 2. Provision of tuition assistance to members of Air National Guard\nThe Secretary of the Air Force shall establish a permanent program to pay, under section 2007 of title 10, United States Code, all or a portion of the charges of an educational institution for the tuition or expenses of a member of the Air National Guard who is in compliance with the training requirements under regulations prescribed under section 502(a) of title 32, United States Code.",
      "versionDate": "2025-12-04",
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "489",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Air Guard STATUS Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-05T16:14:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-04",
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
          "measure-id": "id119hr6478",
          "measure-number": "6478",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6478v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-12-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>"
        },
        "title": "Air Guard STATUS Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6478.xml",
    "summary": {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6478"
    },
    "title": "Air Guard STATUS Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025 or the Air Guard STATUS Act of 2025</strong></p><p>This bill requires the Department of the Air Force to establish a permanent program to pay all or a portion of tuition or expenses at an educational institution for members of the Air National Guard who are in compliance with training requirements (i.e., required field exercises and drills).</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hr6478"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6478ih.xml"
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
      "title": "Air Guard STATUS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T09:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Air Guard STATUS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T09:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Air Guard Standardizing Tuition Assistance To Unify the Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-05T09:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Air Force to establish a permanent program to provide tuition assistance to members of the Air National Guard.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T09:18:20Z"
    }
  ]
}
```
