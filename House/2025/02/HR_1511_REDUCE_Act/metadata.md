# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1511?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1511
- Title: REDUCE Act
- Congress: 119
- Bill type: HR
- Bill number: 1511
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-03-04T18:56:32Z
- Update date including text: 2026-03-04T18:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1511",
    "number": "1511",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "REDUCE Act",
    "type": "HR",
    "updateDate": "2026-03-04T18:56:32Z",
    "updateDateIncludingText": "2026-03-04T18:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:34:05Z",
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
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1511ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1511\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo direct executive branch agencies to conduct a review of redundant positions, to limit civil service hiring, to require agency plans for reductions in force or reorganization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reducing Expensive Departments & Unnecessary Civil Employees Act or the REDUCE Act .\n#### 2. Review of redundant agency activities and positions; limitation on hiring; agency plans for RIF or reorganization\n##### (a) In general\nNot later than 30 days after the date of the enactment of this Act, the head of each agency of the executive branch of the Federal Government shall review each position within such agency and submit a report to Congress on which such positions are redundant and unnecessary.\n##### (b) Hiring limitation\n**(1) In general**\nNotwithstanding any other provision of law, the head of each such agency may appoint no more than 1 employee for every 4 employees of the agency retiring, transferring, or otherwise separating from the agency after the date of the enactment of this Act.\n**(2) Application**\nThe limitation in paragraph (1) shall apply until the date that the total number of employees at an executive branch agency is equal to or less than 80 percent of the total number of such employees at such agency on the date of the enactment of this Act.\n##### (c) RIF or reorganization plan\nThe head of each such agency shall determine which agency components should be eliminated or combined with another component, and establish a plan to so eliminate or combine (as the case may be) such components under a reduction in force or through a reorganization.\n##### (d) Exception\nThis section shall not apply to any position or agency component that is critical to national security, public safety, law enforcement, or immigration enforcement, as determined by the head of each executive branch agency.",
      "versionDate": "2025-02-21",
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
            "name": "Congressional oversight",
            "updateDate": "2025-07-17T18:42:56Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-07-17T18:42:44Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-07-17T18:42:50Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-07-17T18:42:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-21T13:58:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1511",
          "measure-number": "1511",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1511v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reducing Expensive Departments & Unnecessary Civil Employees Act or the REDUCE Act</strong></p><p>This bill limits federal hiring and requires each federal agency to establish plans to eliminate or combine components of the agency.\u00a0The bill does not apply to positions or agency components that are critical to national security, public safety, law enforcement, or immigration enforcement.</p><p>Specifically, a federal agency may not appoint more than one employee for every four employees that retire, transfer, or separate from such agency. This limitation does not apply after the agency has reduced the number of its employees by 20%.</p><p>The bill also requires each agency to determine which agency components should be eliminated or combined and develop a plan to bring this into effect through reorganization or reduction in force.\u00a0</p><p>Each agency must conduct a review of each position within the agency to identify\u00a0positions that are redundant or unnecessary and report the results of this review to Congress.</p>"
        },
        "title": "REDUCE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1511.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reducing Expensive Departments & Unnecessary Civil Employees Act or the REDUCE Act</strong></p><p>This bill limits federal hiring and requires each federal agency to establish plans to eliminate or combine components of the agency.\u00a0The bill does not apply to positions or agency components that are critical to national security, public safety, law enforcement, or immigration enforcement.</p><p>Specifically, a federal agency may not appoint more than one employee for every four employees that retire, transfer, or separate from such agency. This limitation does not apply after the agency has reduced the number of its employees by 20%.</p><p>The bill also requires each agency to determine which agency components should be eliminated or combined and develop a plan to bring this into effect through reorganization or reduction in force.\u00a0</p><p>Each agency must conduct a review of each position within the agency to identify\u00a0positions that are redundant or unnecessary and report the results of this review to Congress.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1511"
    },
    "title": "REDUCE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reducing Expensive Departments & Unnecessary Civil Employees Act or the REDUCE Act</strong></p><p>This bill limits federal hiring and requires each federal agency to establish plans to eliminate or combine components of the agency.\u00a0The bill does not apply to positions or agency components that are critical to national security, public safety, law enforcement, or immigration enforcement.</p><p>Specifically, a federal agency may not appoint more than one employee for every four employees that retire, transfer, or separate from such agency. This limitation does not apply after the agency has reduced the number of its employees by 20%.</p><p>The bill also requires each agency to determine which agency components should be eliminated or combined and develop a plan to bring this into effect through reorganization or reduction in force.\u00a0</p><p>Each agency must conduct a review of each position within the agency to identify\u00a0positions that are redundant or unnecessary and report the results of this review to Congress.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1511"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1511ih.xml"
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
      "title": "REDUCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REDUCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reducing Expensive Departments & Unnecessary Civil Employees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct executive branch agencies to conduct a review of redundant positions, to limit civil service hiring, to require agency plans for reductions in force or reorganization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:50Z"
    }
  ]
}
```
