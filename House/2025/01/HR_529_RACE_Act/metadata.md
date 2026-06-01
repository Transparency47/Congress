# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/529?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/529
- Title: RACE Act
- Congress: 119
- Bill type: HR
- Bill number: 529
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-03-20T18:07:36Z
- Update date including text: 2025-03-20T18:07:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/529",
    "number": "529",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "RACE Act",
    "type": "HR",
    "updateDate": "2025-03-20T18:07:36Z",
    "updateDateIncludingText": "2025-03-20T18:07:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:09:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "B001291",
      "district": "36",
      "firstName": "Brian",
      "fullName": "Rep. Babin, Brian [R-TX-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Babin",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr529ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 529\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Pfluger (for himself, Mr. Babin , and Ms. Tenney ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to establish deadlines for States to count the ballots cast in elections for Federal office and to certify the results of such elections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring American Confidence in Elections Act or the RACE Act .\n#### 2. Deadline for counting ballots and certifying results in Federal elections\n##### (a) Deadlines\nTitle III of the Help America Vote Act of 2002 ( 52 U.S.C. 20181 et seq. ), as amended by section 2(a) of the COCOA Act of 2024, is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Deadline for counting ballots and certifying results (a) Deadlines (1) Counting ballots A State shall finish counting the ballots cast in an election for Federal office held in the State not later than 10 o\u2019clock p.m. on the date of the election. (2) Certifying results A State shall certify the results of an election for Federal office held in the State not later than 48 hours after the date of the election. (b) Exceptions Subsection (a) does not apply if the failure of a State to meet a deadline under such subsection is attributable to\u2014 (1) a bona fide emergency, including a major disaster (as defined in section 102 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5122 )); or (2) technical difficulties, including malfunctioning election equipment or software. .\n##### (b) Conforming amendment relating to existing enforcement provisions\nSection 401 of such Act ( 52 U.S.C. 21111 ), as amended by section 2(b) of the COCOA Act of 2024, is amended by striking and 304 and inserting 304, and 305 .\n##### (c) Clerical amendment\nThe table of contents of such Act, as amended by section 2(c) of the COCOA Act of 2024, is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to section 306 and 307; and\n**(2)**\nby inserting after the item relating to section 304 the following:\nSec. 305. Deadline for counting ballots and certifying results. .\n##### (d) Effective date\nThis Act and the amendments made by this Act shall apply with respect to elections held after the date of the enactment of this Act.",
      "versionDate": "2025-01-16",
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
        "item": [
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-02-19T21:23:47Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-19T21:23:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-18T20:59:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr529",
          "measure-number": "529",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr529v00",
            "update-date": "2025-03-20"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Restoring American Confidence in Elections Act or the RACE Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to finish counting the ballots cast in a federal election held in the state not later than 10:00 p.m. on the date of the election. Further, the state must certify the election results not later than 48 hours after the election.\u00a0</p><p>The bill provides exceptions to these deadlines for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p>"
        },
        "title": "RACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr529.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring American Confidence in Elections Act or the RACE Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to finish counting the ballots cast in a federal election held in the state not later than 10:00 p.m. on the date of the election. Further, the state must certify the election results not later than 48 hours after the election.\u00a0</p><p>The bill provides exceptions to these deadlines for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr529"
    },
    "title": "RACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring American Confidence in Elections Act or the RACE Act</strong></p><p>This bill establishes deadlines for states to count ballots and certify results in federal elections.\u00a0</p><p>Specifically, the bill requires a state to finish counting the ballots cast in a federal election held in the state not later than 10:00 p.m. on the date of the election. Further, the state must certify the election results not later than 48 hours after the election.\u00a0</p><p>The bill provides exceptions to these deadlines for bona fide emergencies (e.g., major disasters) or technical difficulties (e.g., malfunctioning election equipment or software).</p>",
      "updateDate": "2025-03-20",
      "versionCode": "id119hr529"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr529ih.xml"
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
      "title": "RACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring American Confidence in Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T09:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to establish deadlines for States to count the ballots cast in elections for Federal office and to certify the results of such elections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:18:24Z"
    }
  ]
}
```
