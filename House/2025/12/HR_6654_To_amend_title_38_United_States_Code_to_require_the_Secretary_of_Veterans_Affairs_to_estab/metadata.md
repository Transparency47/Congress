# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6654?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6654
- Title: VAMOSA Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6654
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-11T16:40:16Z
- Update date including text: 2026-05-11T16:40:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-01-21 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6654",
    "number": "6654",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "VAMOSA Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-11T16:40:16Z",
    "updateDateIncludingText": "2026-05-11T16:40:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-25",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-21",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:04:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-15T13:31:03Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-15T12:51:27Z",
                "name": "Markup by"
              },
              {
                "date": "2026-03-25T14:36:36Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-21T15:19:38Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6654ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6654\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Ms. Mace introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish and implement a comprehensive policy for managing software assets throughout the Department, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Management and Oversight of Software Assets Act of 2025 or the VAMOSA Act of 2025 .\n#### 2. Department-wide software asset management policy for the Department of Veterans Affairs\n##### (a) In general\nSubchapter II of chapter 5 of title 38, United States Code, is amended by adding at the end the following new section:\n534. Department-wide software asset management policy (a) Establishment The Secretary shall ensure coordination between the Chief Information Officer and such other officers as the Secretary considers appropriate to establish and implement a comprehensive policy for managing software assets. (b) Minimum elements The policy required by subsection (a) shall, at a minimum, provide for the following: (1) Maintaining a comprehensive inventory of software assets. (2) Assessing interoperability and license restrictions with respect to those assets. (3) Identifying and eliminating waste, fraud, and abuse, including by regularly comparing the inventory maintained under paragraph (1) against purchase records, subscription records, vendor billing records, and contract files to identify discrepancies, over-procurement, redundant purchases, unauthorized use, and under-utilized licenses. (4) Requiring that the Chief Information officer coordinate with the relevant officials in the Department regarding any significant acquisition of a software asset. (5) Adopting cost-effective licensing strategies, including enterprise-wide agreements where practicable. (6) Measuring and enforcing compliance with license terms. (c) Reviews and updates Not less than once every three years, the Chief Information Officer, in consultation with the Chief Financial Officer and any other appropriate officials of the Department, or their designees, shall review and update the policy. (d) Training The Secretary shall ensure that each employee responsible for acquiring, managing, or implementing software assets receives training no less often than annually on matters relevant to their duties, including such matters as\u2014 (1) negotiating contract terms to minimize vendor-imposed restrictions on deployment, data access, and transferability; (2) the differences between acquiring commercial software and custom software development; and (3) evaluating cost models for seat-based, consumption-based, enterprise, or scalable license structures. (e) Use of existing resources This section shall be implemented using existing personnel, systems, and funds. This section does not authorize additional appropriations or the establishment of a new program, office, or organizational entity. (f) Annual report The Secretary shall include, in the annual report submitted to Congress under section 529 of this title\u2014 (1) a description of any substantive updates to the policy made during the preceding year; and (2) an estimate of cost savings realized from implementation of the policy during the preceding year. (g) Definitions In this section: (1) The term comprehensive inventory of software assets \u2014 (A) includes\u2014 (i) the comprehensive inventory of software licenses required by section 2(b)(2)(A) of the Making Electronic Government Accountable By Yielding Tangible Efficiencies Act of 2016 ( Public Law 114\u2013210 ; 40 U.S.C. 11302 note) and any directive issued by the Director of the Office of Management and Budget under that Act; and (ii) a comprehensive inventory of all other software assets (as defined in this section); and (B) reflects all accounts, subscriptions, tenants, deployments, and associated license or usage entitlements. (2) The term software asset means any software, software-as-a-service (SaaS) product, cloud-based service, platform service, or application programming interface (API) service for which the Department incurs a cost to acquire, license, subscribe, operate, or maintain, whether hosted on Government-managed or vendor-managed infrastructure. The term includes any associated software license, subscription, usage right, seat entitlement, capacity allocation, or consumption-based entitlement that governs access to or use of such software functionality. (h) Sunset The requirements and authorities of this section shall terminate on the date that is five years after the date of the enactment of the VAMOSA Act. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by inserting after the item relating to section 533 the following new item:\n534. Department-wide software asset management policy. .\n##### (c) GAO report\nNot later than three years after the date of the enactment of this Act, the Comptroller General shall submit to the Committees on Veterans\u2019 Affairs of the Senate and the House of Representatives a report evaluating\u2014\n**(1)**\nthe Department\u2019s implementation of section 534 of title 38, United States Code, as added by this section;\n**(2)**\nthe cost savings achieved and duplication reduced; and\n**(3)**\nthe degree of operational independence and conflict avoidance in any contractor support used to perform inventory management or entitlement reconciliation.",
      "versionDate": "2025-12-11",
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
            "updateDate": "2026-05-11T15:50:48Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-05-11T16:40:06Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-11T16:27:42Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-11T16:40:16Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-11T15:53:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-14T16:29:38Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6654ih.xml"
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
      "title": "VAMOSA Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VAMOSA Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Affairs Management and Oversight of Software Assets Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to require the Secretary of Veterans Affairs to establish and implement a comprehensive policy for managing software assets throughout the Department, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T03:18:25Z"
    }
  ]
}
```
