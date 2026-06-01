# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2561?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2561
- Title: One Vote One Choice Act
- Congress: 119
- Bill type: HR
- Bill number: 2561
- Origin chamber: House
- Introduced date: 2025-04-01
- Update date: 2025-07-01T20:53:04Z
- Update date including text: 2025-07-01T20:53:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-04-01: Introduced in House

## Actions

- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Introduced in House
- 2025-04-01 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2561",
    "number": "2561",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "One Vote One Choice Act",
    "type": "HR",
    "updateDate": "2025-07-01T20:53:04Z",
    "updateDateIncludingText": "2025-07-01T20:53:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-01",
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
      "actionDate": "2025-04-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T14:00:25Z",
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
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "NY"
    },
    {
      "bioguideId": "M001211",
      "district": "15",
      "firstName": "Mary",
      "fullName": "Rep. Miller, Mary E. [R-IL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2561ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2561\nIN THE HOUSE OF REPRESENTATIVES\nApril 1, 2025 Mr. Lawler (for himself, Ms. Tenney , and Mrs. Miller of Illinois ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to prohibit States from using ranked choice voting to carry out an election for Federal office, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Vote One Choice Act .\n#### 2. Prohibiting States from using ranked choice voting in Federal elections\n##### (a) Requirement\nSubtitle A of title III of the Help America Vote Act of 2002 ( 52 U.S.C. 21081 et seq. ) is amended\u2014\n**(1)**\nby redesignating sections 305 and 306 as sections 306 and 307, respectively; and\n**(2)**\nby inserting after section 304 the following new section:\n305. Prohibiting States from the use of ranked choice voting with respect to an election for Federal office A State may not carry out an election for Federal office in the State using a system of ranked choice voting under which each voter shall rank the candidates for the office in the order of the voter\u2019s preference. .\n##### (b) Conforming amendment relating to enforcement\nSection 401 of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 ) is amended by striking 303, and 304 and inserting 303, 304, and 305 .\n##### (c) Clerical amendment\nThe table of contents of such Act is amended\u2014\n**(1)**\nby redesignating the items relating to sections 305 and 306 as relating to sections 306 and 307, respectively; and\n**(2)**\nby inserting after the item relating to section 304 the following new item:\nSec. 305. Prohibiting States from the use of ranked choice voting with respect to an election for Federal office. .\n##### (d) Effective date\nThe amendments made by this section shall apply with respect to elections held on or after the date of the enactment of this Act.",
      "versionDate": "2025-04-01",
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
        "updateDate": "2025-05-23T14:16:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119hr2561",
          "measure-number": "2561",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-01",
          "originChamber": "HOUSE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2561v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>One Vote One Choice Act</strong></p><p>This bill prohibits states from using ranked-choice voting in federal elections. Ranked-choice voting is a system that allows voters to rank multiple candidates on a ballot in order of preference.</p>"
        },
        "title": "One Vote One Choice Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2561.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Vote One Choice Act</strong></p><p>This bill prohibits states from using ranked-choice voting in federal elections. Ranked-choice voting is a system that allows voters to rank multiple candidates on a ballot in order of preference.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr2561"
    },
    "title": "One Vote One Choice Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>One Vote One Choice Act</strong></p><p>This bill prohibits states from using ranked-choice voting in federal elections. Ranked-choice voting is a system that allows voters to rank multiple candidates on a ballot in order of preference.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr2561"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2561ih.xml"
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
      "title": "One Vote One Choice Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Vote One Choice Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to prohibit States from using ranked choice voting to carry out an election for Federal office, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:36Z"
    }
  ]
}
```
