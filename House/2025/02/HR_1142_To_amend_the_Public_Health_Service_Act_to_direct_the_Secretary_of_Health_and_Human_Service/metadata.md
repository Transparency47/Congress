# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1142?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1142
- Title: To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 1142
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-06-04T19:11:16Z
- Update date including text: 2025-06-04T19:11:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1142",
    "number": "1142",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-06-04T19:11:16Z",
    "updateDateIncludingText": "2025-06-04T19:11:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1142ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1142\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mr. Schweikert introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes.\n#### 1. Establishment of drug adherence guidelines\nTitle XVII of the Public Health Service Act ( 42 U.S.C. 300u et seq. ) is amended by inserting after section 1711 ( 42 U.S.C. 300u\u201316 ) the following:\n1712. Establishment of drug adherence guidelines (a) In general The Secretary shall establish drug adherence guidelines with the goal of achieving 90 percent adherence for all Medicare part B and D drugs. (b) Contents In establishing the guidelines under subsection (a), the Secretary shall\u2014 (1) incorporate artificial intelligence and machine learning technologies; and (2) to the maximum extent practicable, promote the use of generic and biosimilar drugs. (c) Definitions In this section: (1) Medicare part b drug The term Medicare part B drug means a drug or biological product for which payment may be made under part B of title XVIII of the Social Security Act ( 42 U.S.C. 1395j et seq. ). (2) Medicare part d drug The term Medicare part D drug means a covered part D drug (as defined in section 1860D\u20132(e) of the Social Security Act ( 42 U.S.C. 1395w\u2013102(e) )). .",
      "versionDate": "2025-02-07",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-04-24T16:16:59Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-04-24T16:16:51Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-04-24T16:16:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-11T18:01:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-07",
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
          "measure-id": "id119hr1142",
          "measure-number": "1142",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-07",
          "originChamber": "HOUSE",
          "update-date": "2025-06-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1142v00",
            "update-date": "2025-06-04"
          },
          "action-date": "2025-02-07",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish drug adherence guidelines for covered drugs under Medicare so as to achieve an adherence rate of 90%. The CMS must incorporate artificial\u00a0intelligence and machine-learning technologies and promote generics and biosimilars when developing the guidance.</p>"
        },
        "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1142.xml",
    "summary": {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish drug adherence guidelines for covered drugs under Medicare so as to achieve an adherence rate of 90%. The CMS must incorporate artificial\u00a0intelligence and machine-learning technologies and promote generics and biosimilars when developing the guidance.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr1142"
    },
    "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-02-07",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Centers for Medicare & Medicaid Services (CMS) to establish drug adherence guidelines for covered drugs under Medicare so as to achieve an adherence rate of 90%. The CMS must incorporate artificial\u00a0intelligence and machine-learning technologies and promote generics and biosimilars when developing the guidance.</p>",
      "updateDate": "2025-06-04",
      "versionCode": "id119hr1142"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1142ih.xml"
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
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-10T12:18:31Z"
    },
    {
      "title": "To amend the Public Health Service Act to direct the Secretary of Health and Human Services to establish drug adherence guidelines, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T09:01:52Z"
    }
  ]
}
```
