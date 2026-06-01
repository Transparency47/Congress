# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1191?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1191
- Title: Supporting Access to Rural Community Hospitals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1191
- Origin chamber: House
- Introduced date: 2025-02-11
- Update date: 2025-12-05T22:03:46Z
- Update date including text: 2025-12-05T22:03:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-11: Introduced in House

## Actions

- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Introduced in House
- 2025-02-11 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1191",
    "number": "1191",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Supporting Access to Rural Community Hospitals Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:03:46Z",
    "updateDateIncludingText": "2025-12-05T22:03:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T15:04:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1191ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1191\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2025 Mr. Flood (for himself and Mr. Smith of Nebraska ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title XVIII of the Social Security Act to waive certain distance requirements for certain hospitals electing to be designated as critical access hospitals.\n#### 1. Short title\nThis Act may be cited as the Supporting Access to Rural Community Hospitals Act of 2025 .\n#### 2. Waiving certain distance requirements for certain hospitals electing to be designated as critical access hospitals\n##### (a) In general\nSection 1820(c)(2)(B)(i) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by striking or at the end;\n**(2)**\nin subclause (II), by adding or at the end; and\n**(3)**\nby adding at the end the following new subclause:\n(III) with respect to designations occurring during the 1-year period beginning on the date that is 6 months after the date of the enactment of this subclause, is a rural community hospital (as defined in subsection (f) of section 410A of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003) that was participating in the demonstration program established under such section as of such date of enactment. .\n##### (b) Conforming amendments\nSection 410A(f)(1)(A)(iv) of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 42 U.S.C. 1395ww note) is amended by striking is not and all that follows through the period and inserting is not a critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act). .",
      "versionDate": "2025-02-11",
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
        "actionDate": "2025-02-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "521",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting Access to Rural Community Hospitals Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-05-02T14:49:30Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-05-02T14:49:19Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-05-02T14:49:25Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-05-02T14:49:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-17T14:26:27Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-11",
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
          "measure-id": "id119hr1191",
          "measure-number": "1191",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-11",
          "originChamber": "HOUSE",
          "update-date": "2025-06-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1191v00",
            "update-date": "2025-06-11"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>"
        },
        "title": "Supporting Access to Rural Community Hospitals Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1191.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1191"
    },
    "title": "Supporting Access to Rural Community Hospitals Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>",
      "updateDate": "2025-06-11",
      "versionCode": "id119hr1191"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1191ih.xml"
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
      "title": "Supporting Access to Rural Community Hospitals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T05:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Access to Rural Community Hospitals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to waive certain distance requirements for certain hospitals electing to be designated as critical access hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T05:18:36Z"
    }
  ]
}
```
