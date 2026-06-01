# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5721?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5721
- Title: Protect Our Judiciary Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5721
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2026-04-03T20:01:20Z
- Update date including text: 2026-04-03T20:01:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5721",
    "number": "5721",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "R000603",
        "district": "7",
        "firstName": "David",
        "fullName": "Rep. Rouzer, David [R-NC-7]",
        "lastName": "Rouzer",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Protect Our Judiciary Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-03T20:01:20Z",
    "updateDateIncludingText": "2026-04-03T20:01:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T19:03:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5721ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5721\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mr. Rouzer (for himself and Mr. Fallon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit picketing or parading certain buildings or residences.\n#### 1. Short title\nThis Act may be cited as the Protect Our Judiciary Act of 2025 .\n#### 2. Picketing or parading\nSection 1507 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking , or in or near a building or residence occupied or used by such judge, juror, witness, or court officer ; and\n**(2)**\nby inserting after the first sentence the following: Whoever knowingly pickets or parades in or near a building or residence being used by any judge, juror, witness, or court officer, or uses any sound-truck or similar device or resorts to any other demonstration in or near any such building or residence, shall be fined under this title or imprisoned not more than one year, or both. .",
      "versionDate": "2025-10-08",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-12-09T15:32:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-08",
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
          "measure-id": "id119hr5721",
          "measure-number": "5721",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-08",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5721v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-10-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect Our Judiciary Act of 2025</strong></p><p>This bill removes the intent requirement for the criminal offense related to picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer.</p>"
        },
        "title": "Protect Our Judiciary Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5721.xml",
    "summary": {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Our Judiciary Act of 2025</strong></p><p>This bill removes the intent requirement for the criminal offense related to picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr5721"
    },
    "title": "Protect Our Judiciary Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Our Judiciary Act of 2025</strong></p><p>This bill removes the intent requirement for the criminal offense related to picketing or parading in or near a building or residence used by a judge, juror, witness, or court officer.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr5721"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5721ih.xml"
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
      "title": "Protect Our Judiciary Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Our Judiciary Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit picketing or parading certain buildings or residences.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T05:48:20Z"
    }
  ]
}
```
