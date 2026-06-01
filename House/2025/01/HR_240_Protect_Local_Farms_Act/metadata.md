# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/240?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/240
- Title: Protect Local Farms Act
- Congress: 119
- Bill type: HR
- Bill number: 240
- Origin chamber: House
- Introduced date: 2025-01-07
- Update date: 2025-07-21T19:44:15Z
- Update date including text: 2025-07-21T19:44:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-07: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-07: Introduced in House

## Actions

- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Introduced in House
- 2025-01-07 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-07",
    "latestAction": {
      "actionDate": "2025-01-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/240",
    "number": "240",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Protect Local Farms Act",
    "type": "HR",
    "updateDate": "2025-07-21T19:44:15Z",
    "updateDateIncludingText": "2025-07-21T19:44:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-07",
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
          "date": "2025-01-07T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "NY"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr240ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 240\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 7, 2025 Ms. Tenney (for herself, Mr. Langworthy , and Mr. LaMalfa ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Fair Labor Standards Act of 1938 to provide for the preemption of certain State overtime laws for agricultural employees.\n#### 1. Short title\nThis Act may be cited as the Protect Local Farms Act .\n#### 2. Preemption of certain state overtime laws for agricultural employees\nSection 18 of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 218 ) is amended\u2014\n**(1)**\nin subsection (a), by striking No provision of this Act or of any order thereunder and inserting Except as provided in subsection (c), no provision of this Act or of any order thereunder ; and\n**(2)**\nby adding at the end the following:\n(c) The provisions of this Act shall preempt any State law that provides for a maximum workweek for employees employed in agriculture of less than 60 hours. .",
      "versionDate": "2025-01-07",
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
            "name": "Labor standards",
            "updateDate": "2025-02-27T15:23:44Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-27T15:23:50Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-02-27T15:23:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-02-06T21:34:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-07",
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
          "measure-id": "id119hr240",
          "measure-number": "240",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-07",
          "originChamber": "HOUSE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr240v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect Local Farms Act</strong></p><p>This bill provides that the Fair Labor Standards Act (FLSA) preempts any state law that establishes a maximum workweek (i.e., the maximum number of hours an employee is permitted to work without receiving overtime pay) of less than 60 hours for agricultural employees. </p><p>Under the FLSA, agricultural employees are generally exempt from\u00a0federal overtime requirements.\u00a0However, federal overtime requirements currently do not preempt state\u00a0laws that provide greater protections to employees.</p>"
        },
        "title": "Protect Local Farms Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr240.xml",
    "summary": {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Local Farms Act</strong></p><p>This bill provides that the Fair Labor Standards Act (FLSA) preempts any state law that establishes a maximum workweek (i.e., the maximum number of hours an employee is permitted to work without receiving overtime pay) of less than 60 hours for agricultural employees. </p><p>Under the FLSA, agricultural employees are generally exempt from\u00a0federal overtime requirements.\u00a0However, federal overtime requirements currently do not preempt state\u00a0laws that provide greater protections to employees.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr240"
    },
    "title": "Protect Local Farms Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-07",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Local Farms Act</strong></p><p>This bill provides that the Fair Labor Standards Act (FLSA) preempts any state law that establishes a maximum workweek (i.e., the maximum number of hours an employee is permitted to work without receiving overtime pay) of less than 60 hours for agricultural employees. </p><p>Under the FLSA, agricultural employees are generally exempt from\u00a0federal overtime requirements.\u00a0However, federal overtime requirements currently do not preempt state\u00a0laws that provide greater protections to employees.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr240"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr240ih.xml"
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
      "title": "Protect Local Farms Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T01:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Local Farms Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T01:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Labor Standards Act of 1938 to provide for the preemption of certain State overtime laws for agricultural employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T01:03:28Z"
    }
  ]
}
```
