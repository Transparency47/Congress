# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/467
- Title: Foreign Medical Program Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 467
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-09-17T08:06:45Z
- Update date including text: 2025-09-17T08:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/467",
    "number": "467",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Foreign Medical Program Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-17T08:06:45Z",
    "updateDateIncludingText": "2025-09-17T08:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:38:17Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr467ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 467\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Van Drew introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to eliminate the requirement of a service-connected disability to furnish veterans with medical care outside of a State, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Medical Program Modernization Act of 2025 .\n#### 2. Expansion of Foreign Medical Program of Department of Veterans Affairs\n##### (a) Elimination of service-Connected disability requirement\nSection 1724 of title 38, United States Code, is amended\u2014\n**(1)**\nby striking subsection (a);\n**(2)**\nby redesignating subsections (b) through (e) as subsections (a) through (d), respectively;\n**(3)**\nin subsection (a), as so redesignated\u2014\n**(A)**\nin paragraph (1), by striking if the Secretary determines that such care and services are needed for the treatment of a service-connected disability of the veteran or as part of a rehabilitation program under chapter 31 of this title ; and\n**(B)**\nin paragraph (2), by striking a service-connected disability of ; and\n**(4)**\nin subsection (d), as so redesignated, by striking who has a service-connected disability .\n##### (b) Electronic fund transfer reimbursement\nThe Secretary of Veterans Affairs shall update the payment system of the Department of Veterans Affairs to allow for reimbursements through electronic fund transfer for hospital care or medical services furnished pursuant to section 1724 of title 38, United States Code.\n##### (c) Assessment of contract for provision of care\nThe Secretary shall assess the feasibility and implications of entering into a contract with an appropriate non-Department entity to build a network of non-Department entities to provide hospital care and medical services pursuant to section 1724 of title 38, United States Code, including implications for the administrative burden on veterans eligible to receive such care and services.",
      "versionDate": "2025-01-15",
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
            "name": "Computers and information technology",
            "updateDate": "2025-03-07T15:22:59Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-03-07T15:22:47Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-03-07T15:22:53Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-03-07T15:23:04Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-07T15:22:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T15:30:55Z"
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
          "measure-id": "id119hr467",
          "measure-number": "467",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr467v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Foreign Medical Program Modernization Act of 2025</strong></p><p>This bill expands eligibility for care under the Foreign Medical Program of the Department of Veterans Affairs (VA) by removing certain eligibility requirements. The program authorizes the VA to furnish care and services to veterans abroad (i.e., outside any state) for the treatment of service-connected disabilities or as part of a Veteran Readiness and Employment rehabilitation program. The bill expands eligibility for care by removing the requirement that a veteran have a service-connected disability or be participating in a rehabilitation program.</p><p>The bill also requires the VA to update its payment system to allow for reimbursements through electronic fund transfer.</p><p>Under the bill, the VA must assess the feasibility and implications of contracting with an appropriate non-VA entity to build a network of non-VA entities to provide hospital care and medical services abroad under the Foreign Medical Program.</p>"
        },
        "title": "Foreign Medical Program Modernization Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr467.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Foreign Medical Program Modernization Act of 2025</strong></p><p>This bill expands eligibility for care under the Foreign Medical Program of the Department of Veterans Affairs (VA) by removing certain eligibility requirements. The program authorizes the VA to furnish care and services to veterans abroad (i.e., outside any state) for the treatment of service-connected disabilities or as part of a Veteran Readiness and Employment rehabilitation program. The bill expands eligibility for care by removing the requirement that a veteran have a service-connected disability or be participating in a rehabilitation program.</p><p>The bill also requires the VA to update its payment system to allow for reimbursements through electronic fund transfer.</p><p>Under the bill, the VA must assess the feasibility and implications of contracting with an appropriate non-VA entity to build a network of non-VA entities to provide hospital care and medical services abroad under the Foreign Medical Program.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr467"
    },
    "title": "Foreign Medical Program Modernization Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Foreign Medical Program Modernization Act of 2025</strong></p><p>This bill expands eligibility for care under the Foreign Medical Program of the Department of Veterans Affairs (VA) by removing certain eligibility requirements. The program authorizes the VA to furnish care and services to veterans abroad (i.e., outside any state) for the treatment of service-connected disabilities or as part of a Veteran Readiness and Employment rehabilitation program. The bill expands eligibility for care by removing the requirement that a veteran have a service-connected disability or be participating in a rehabilitation program.</p><p>The bill also requires the VA to update its payment system to allow for reimbursements through electronic fund transfer.</p><p>Under the bill, the VA must assess the feasibility and implications of contracting with an appropriate non-VA entity to build a network of non-VA entities to provide hospital care and medical services abroad under the Foreign Medical Program.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr467"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr467ih.xml"
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
      "title": "Foreign Medical Program Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T13:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Medical Program Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T13:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to eliminate the requirement of a service-connected disability to furnish veterans with medical care outside of a State, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:23Z"
    }
  ]
}
```
