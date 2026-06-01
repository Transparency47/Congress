# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1825?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1825
- Title: GRACE Act
- Congress: 119
- Bill type: HR
- Bill number: 1825
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-02-17T20:09:19Z
- Update date including text: 2026-02-17T20:09:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-03-04: Introduced in House

## Actions

- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1825",
    "number": "1825",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "GRACE Act",
    "type": "HR",
    "updateDate": "2026-02-17T20:09:19Z",
    "updateDateIncludingText": "2026-02-17T20:09:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:02:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1825ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1825\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo direct the Secretary of Education to eliminate the Office of Enforcement within the Office of Federal Student Aid, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding Religious And Career Education Act or the GRACE Act .\n#### 2. Elimination of Office of Enforcement\nThe Secretary of Education, acting through the chief operating officer for the Office of Federal Student Aid, shall eliminate the Office of Enforcement (as established pursuant to the electronic announcement entitled (GENERAL\u201321\u201364) Federal Student Aid to Establish Enforcement Office and Enhance Federal and State Oversight Partnerships and published on October 8, 2021).",
      "versionDate": "2025-03-04",
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
            "name": "Department of Education",
            "updateDate": "2026-02-17T20:09:19Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2026-02-17T20:09:13Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2026-02-17T20:09:07Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2026-02-17T20:08:57Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-02-17T20:09:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Education",
        "updateDate": "2025-03-21T16:39:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119hr1825",
          "measure-number": "1825",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1825v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Guarding Religious And Career Education Act or the GRACE Act</strong></p><p>This bill directs the Department of Education's Office of Federal Student Aid (FSA) to eliminate its Office of Enforcement. On October 8, 2021, the FSA announced it was reestablishing the Office of Enforcement to strengthen oversight of and enforcement actions against\u00a0postsecondary schools that participate in federal student loan, grant, and work-study programs.</p>"
        },
        "title": "GRACE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1825.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guarding Religious And Career Education Act or the GRACE Act</strong></p><p>This bill directs the Department of Education's Office of Federal Student Aid (FSA) to eliminate its Office of Enforcement. On October 8, 2021, the FSA announced it was reestablishing the Office of Enforcement to strengthen oversight of and enforcement actions against\u00a0postsecondary schools that participate in federal student loan, grant, and work-study programs.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1825"
    },
    "title": "GRACE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Guarding Religious And Career Education Act or the GRACE Act</strong></p><p>This bill directs the Department of Education's Office of Federal Student Aid (FSA) to eliminate its Office of Enforcement. On October 8, 2021, the FSA announced it was reestablishing the Office of Enforcement to strengthen oversight of and enforcement actions against\u00a0postsecondary schools that participate in federal student loan, grant, and work-study programs.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1825"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1825ih.xml"
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
      "title": "GRACE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRACE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarding Religious And Career Education Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Education to eliminate the Office of Enforcement within the Office of Federal Student Aid, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:34Z"
    }
  ]
}
```
