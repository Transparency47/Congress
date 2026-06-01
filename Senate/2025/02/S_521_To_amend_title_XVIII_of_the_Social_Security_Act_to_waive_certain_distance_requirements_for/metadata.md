# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/521?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/521
- Title: Supporting Access to Rural Community Hospitals Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 521
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2025-12-05T22:49:09Z
- Update date including text: 2025-12-05T22:49:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/521",
    "number": "521",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "F000463",
        "district": "",
        "firstName": "Deb",
        "fullName": "Sen. Fischer, Deb [R-NE]",
        "lastName": "Fischer",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Supporting Access to Rural Community Hospitals Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:49:09Z",
    "updateDateIncludingText": "2025-12-05T22:49:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-11T20:40:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s521is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 521\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mrs. Fischer introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to waive certain distance requirements for certain hospitals electing to be designated as critical access hospitals.\n#### 1. Short title\nThis Act may be cited as the Supporting Access to Rural Community Hospitals Act of 2025 .\n#### 2. Waiving certain distance requirements for certain hospitals electing to be designated as critical access hospitals\n##### (a) In general\nSection 1820(c)(2)(B)(i) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by striking or at the end;\n**(2)**\nin subclause (II), by adding or at the end; and\n**(3)**\nby adding at the end the following new subclause:\n(III) with respect to designations occurring during the 1-year period beginning on the date that is 6 months after the date of the enactment of this subclause, is a rural community hospital (as defined in subsection (f) of section 410A of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003) that was participating in the demonstration program established under such section as of such date of enactment. .\n##### (b) Conforming amendments\nSection 410A(f)(1)(A)(iv) of the Medicare Prescription Drug, Improvement, and Modernization Act of 2003 ( 42 U.S.C. 1395ww note) is amended by striking is not and all that follows through the period and inserting is not a critical access hospital (as defined in section 1861(mm)(1) of the Social Security Act). .",
      "versionDate": "2025-02-11",
      "versionType": "Introduced in Senate"
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
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1191",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Supporting Access to Rural Community Hospitals Act of 2025",
      "type": "HR"
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
            "updateDate": "2025-05-02T14:49:45Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-05-02T14:49:45Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-05-02T14:49:45Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2025-05-02T14:49:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T14:14:23Z"
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
    "originChamber": "Senate",
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
          "measure-id": "id119s521",
          "measure-number": "521",
          "measure-type": "s",
          "orig-publish-date": "2025-02-11",
          "originChamber": "SENATE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s521v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-02-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>"
        },
        "title": "Supporting Access to Rural Community Hospitals Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s521.xml",
    "summary": {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s521"
    },
    "title": "Supporting Access to Rural Community Hospitals Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Supporting Access to Rural Community Hospitals Act of 2025</strong></p><p>This bill temporarily allows additional hospitals to qualify as critical access hospitals (CAHs) that receive special payment under Medicare.</p><p>Currently, in order to qualify as a CAH under Medicare, a hospital must either (1) be located more than 35 miles (or 15 miles in mountainous regions or areas with only secondary roads) from another hospital, or (2) have been certified prior to January 1, 2006, by the state as a necessary provider of services in the area. Hospitals also must meet certain size and service requirements, including having no more than 25 acute care inpatient beds.</p><p>The bill allows, for one year, hospitals that are participating in the Rural Community Hospital Demonstration Program to also qualify as CAHs. (The program tests the feasibility\u00a0of cost-based reimbursement for small rural hospitals that are too large to qualify as CAHs.)</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s521"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s521is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Access to Rural Community Hospitals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to waive certain distance requirements for certain hospitals electing to be designated as critical access hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:37Z"
    }
  ]
}
```
