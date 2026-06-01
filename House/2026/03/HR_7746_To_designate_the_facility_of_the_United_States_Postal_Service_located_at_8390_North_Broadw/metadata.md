# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7746?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7746
- Title: To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the "Chuck Stone Post Office".
- Congress: 119
- Bill type: HR
- Bill number: 7746
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-05-30T08:06:04Z
- Update date including text: 2026-05-30T08:06:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7746",
    "number": "7746",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\".",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:04Z",
    "updateDateIncludingText": "2026-05-30T08:06:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:00:40Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "MO"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MO"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "MO"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "MO"
    },
    {
      "bioguideId": "S001195",
      "district": "8",
      "firstName": "Jason",
      "fullName": "Rep. Smith, Jason [R-MO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "MO"
    },
    {
      "bioguideId": "B001316",
      "district": "7",
      "firstName": "Eric",
      "fullName": "Rep. Burlison, Eric [R-MO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Burlison",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MO"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert F. [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-05-29",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7746ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7746\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mr. Bell introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the Chuck Stone Post Office .\n#### 1. Chuck Stone Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, shall be known and designated as the Chuck Stone Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Chuck Stone Post Office .",
      "versionDate": "2026-03-02",
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
        "updateDate": "2026-03-18T14:58:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-02",
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
          "measure-id": "id119hr7746",
          "measure-number": "7746",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-02",
          "originChamber": "HOUSE",
          "update-date": "2026-03-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7746v00",
            "update-date": "2026-03-18"
          },
          "action-date": "2026-03-02",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7746.xml",
    "summary": {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\".",
      "updateDate": "2026-03-18",
      "versionCode": "id119hr7746"
    },
    "title": "To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\".",
      "updateDate": "2026-03-18",
      "versionCode": "id119hr7746"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7746ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T04:48:30Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 8390 North Broadway in St. Louis, Missouri, as the \"Chuck Stone Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T09:05:25Z"
    }
  ]
}
```
