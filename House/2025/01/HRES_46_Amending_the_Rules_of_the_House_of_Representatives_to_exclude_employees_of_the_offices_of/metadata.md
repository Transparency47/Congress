# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/46?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/46
- Title: Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes.
- Congress: 119
- Bill type: HRES
- Bill number: 46
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-07-03T20:03:50Z
- Update date including text: 2025-07-03T20:03:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-15 - Committee: Submitted in House
- 2025-01-15 - IntroReferral: Submitted in House
- Latest action: 2025-01-15: Submitted in House

## Actions

- 2025-01-15 - IntroReferral: Referred to the House Committee on Rules.
- 2025-01-15 - Committee: Submitted in House
- 2025-01-15 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/46",
    "number": "46",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes.",
    "type": "HRES",
    "updateDate": "2025-07-03T20:03:50Z",
    "updateDateIncludingText": "2025-07-03T20:03:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-01-15T15:07:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres46ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 46\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Mills submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nAmending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes.\n#### 1. Exemption of certain House employees who are members of Armed Forces from allotment of number of employees of Member office who may hold security clearances processed by the Office of House Security\nRule XXIX of the Rules of the House of Representatives is amended by adding at the end the following new clause:\n5. (a) If an employee of the office of a Member, Delegate, or Resident Commissioner described in paragraph (c) is a member of the armed forces who holds a security clearance issued by the Department of Defense, the employee shall not be included in determining the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security. (b) The level of the security clearance of an employee of an office who is described in paragraph (a) may not exceed the lower of\u2014 (1) the level of the clearance held by the employee which was issued by the Department of Defense; or (2) the highest clearance level which may be sponsored by the office for its employees. (c) A Member, Delegate, or Resident Commissioner described in this paragraph is a Member, Delegate, or Resident Commissioner who serves on any of the following Subcommittees or Committees of the House of Representatives: (1) The Subcommittee on Defense of the Committee on Appropriations. (2) The Subcommittee on Homeland Security of the Committee on Appropriations. (3) The Subcommittee on State, Foreign Operations, and Related Programs of the Committee on Appropriations. (4) The Committee on Armed Services. (5) The Committee on Foreign Affairs. (6) The Committee on Homeland Security. (7) The Permanent Select Committee on Intelligence. .",
      "versionDate": "2025-01-15",
      "versionType": "IH"
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
            "name": "Congressional committees",
            "updateDate": "2025-01-22T15:32:18Z"
          },
          {
            "name": "Congressional officers and employees",
            "updateDate": "2025-01-22T15:31:55Z"
          },
          {
            "name": "House Committee on Appropriations",
            "updateDate": "2025-01-22T15:32:51Z"
          },
          {
            "name": "House Committee on Armed Services",
            "updateDate": "2025-01-22T15:32:58Z"
          },
          {
            "name": "House Committee on Foreign Affairs",
            "updateDate": "2025-01-22T15:33:04Z"
          },
          {
            "name": "House Committee on Homeland Security",
            "updateDate": "2025-01-22T15:33:10Z"
          },
          {
            "name": "House Permanent Select Committee on Intelligence",
            "updateDate": "2025-01-22T15:33:17Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-01-22T15:31:36Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-01-22T15:33:25Z"
          },
          {
            "name": "Legislative rules and procedure",
            "updateDate": "2025-01-22T15:31:42Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-01-22T15:32:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-01-21T12:48:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hres46",
          "measure-number": "46",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres46v00",
            "update-date": "2025-02-07"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution creates an exception to the House limit on\u00a0the number of employees who may hold security clearances within certain Member offices. Specifically, any member of the Armed Forces who holds a security clearance issued by the Department of Defense does not count toward the\u00a0number of employees of a Member who may hold security clearances issued by the Office of House Security. The exception applies to employees of Members on the Committees on Armed Services, Foreign Affairs, or Homeland Security; the Permanent Select Committee on Intelligence; or specified subcommittees of the Committee on Appropriations.</p>"
        },
        "title": "Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres46.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution creates an exception to the House limit on\u00a0the number of employees who may hold security clearances within certain Member offices. Specifically, any member of the Armed Forces who holds a security clearance issued by the Department of Defense does not count toward the\u00a0number of employees of a Member who may hold security clearances issued by the Office of House Security. The exception applies to employees of Members on the Committees on Armed Services, Foreign Affairs, or Homeland Security; the Permanent Select Committee on Intelligence; or specified subcommittees of the Committee on Appropriations.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres46"
    },
    "title": "Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution creates an exception to the House limit on\u00a0the number of employees who may hold security clearances within certain Member offices. Specifically, any member of the Armed Forces who holds a security clearance issued by the Department of Defense does not count toward the\u00a0number of employees of a Member who may hold security clearances issued by the Office of House Security. The exception applies to employees of Members on the Committees on Armed Services, Foreign Affairs, or Homeland Security; the Permanent Select Committee on Intelligence; or specified subcommittees of the Committee on Appropriations.</p>",
      "updateDate": "2025-02-07",
      "versionCode": "id119hres46"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres46ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-17T09:33:23Z"
    },
    {
      "title": "Amending the Rules of the House of Representatives to exclude employees of the offices of Members who serve on certain committees of the House from the allotment of the number of employees of the office who may hold security clearances processed by the Office of House Security if such employees are members of the armed forces who hold a security clearance issued by the Department of Defense, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-16T09:05:41Z"
    }
  ]
}
```
