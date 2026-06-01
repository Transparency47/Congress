# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1371?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1371
- Title: Presidential Legacy Act
- Congress: 119
- Bill type: HR
- Bill number: 1371
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-07-13T23:06:43Z
- Update date including text: 2025-07-13T23:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1371",
    "number": "1371",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Presidential Legacy Act",
    "type": "HR",
    "updateDate": "2025-07-13T23:06:43Z",
    "updateDateIncludingText": "2025-07-13T23:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
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
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:31:20Z",
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
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1371ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1371\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Ms. Budzinski (for herself and Mr. Joyce of Ohio ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo redesignate the third Monday in February as Presidents\u2019 Day, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Presidential Legacy Act .\n#### 2. Redesignate the third Monday in February as Presidents\u2019 Day\nSection 6103(a) of title 5, United States Code, is amended by striking Washington\u2019s Birthday and inserting Presidents\u2019 Day .\n#### 3. Term Washington\u2019s Birthday replaced\n##### (a) In general\nExcept as provided in subsection (b), any reference to Washington\u2019s Birthday in any law, rule, regulation, or other official paper in effect as of the date of the enactment of this Act shall be deemed to be a reference to Presidents\u2019 Day .\n##### (b) Conforming amendments\n**(1) Title 4**\nSection 6(d) of title 4, United States Code, is amended by striking Washington\u2019s Birthday and inserting Presidents\u2019 Day .\n**(2) Federal Contested Election Act**\nSection 15(a) of the Federal Contested Election Act ( 2 U.S.C. 394(a) ) is amended by striking Washington\u2019s Birthday and inserting Presidents\u2019 Day .",
      "versionDate": "2025-02-14",
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
      "legislativeSubjects": {
        "item": {
          "name": "Commemorative events and holidays",
          "updateDate": "2025-07-08T12:59:18Z"
        }
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-02T15:06:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1371",
          "measure-number": "1371",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-07-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1371v00",
            "update-date": "2025-07-13"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Presidential Legacy Act</strong></p><p>This bill redesignates the federal holiday of Washington's Birthday as Presidents' Day.</p>"
        },
        "title": "Presidential Legacy Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1371.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Presidential Legacy Act</strong></p><p>This bill redesignates the federal holiday of Washington's Birthday as Presidents' Day.</p>",
      "updateDate": "2025-07-13",
      "versionCode": "id119hr1371"
    },
    "title": "Presidential Legacy Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Presidential Legacy Act</strong></p><p>This bill redesignates the federal holiday of Washington's Birthday as Presidents' Day.</p>",
      "updateDate": "2025-07-13",
      "versionCode": "id119hr1371"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1371ih.xml"
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
      "title": "Presidential Legacy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Presidential Legacy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To redesignate the third Monday in February as Presidents' Day, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:19:21Z"
    }
  ]
}
```
