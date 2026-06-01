# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1501
- Title: Protecting Domestic Mining Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1501
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-05-21T17:54:22Z
- Update date including text: 2026-05-21T17:54:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 21 - 16.
- 2026-04-21 - Committee: Subcommittee on Energy and Mineral Resources Discharged
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held
- 2026-04-21 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 21 - 16.
- 2026-04-21 - Committee: Subcommittee on Energy and Mineral Resources Discharged

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1501",
    "number": "1501",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Protecting Domestic Mining Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T17:54:22Z",
    "updateDateIncludingText": "2026-05-21T17:54:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 21 - 16.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-21",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Energy and Mineral Resources Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
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
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
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
        "item": [
          {
            "date": "2026-04-21T17:30:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-21T20:31:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-04-21T17:00:00Z",
                "name": "Discharged from"
              },
              {
                "date": "2026-02-24T15:30:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-17T16:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "UT"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1501ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1501\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Shreve (for himself and Mr. Moore of Utah ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the FAST Act to include certain mineral production activities as a covered project, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Domestic Mining Act of 2025 .\n#### 2. Definition of covered project\nSection 41001(6)(A) of the FAST Act ( 42 U.S.C. 4370m(6)(A) ) is amended by inserting mining, before or any other sector .\n#### 3. Prohibition against finalizing, implementing, or enforcing proposed rule related to scope of mining under FAST Act\nThe Federal Permitting Improvement Steering Council may not finalize, implement, administer, or enforce the proposed rule titled Revising Scope of the Mining Sector of Projects That Are Eligible for Coverage Under Title 41 of the Fixing America\u2019s Surface Transportation Act (88 Fed. Reg. 65350; September 22, 2023).",
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
            "name": "Infrastructure development",
            "updateDate": "2026-02-25T17:31:20Z"
          },
          {
            "name": "Metals",
            "updateDate": "2026-02-25T17:31:20Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-02-25T17:31:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-03-18T16:32:23Z"
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
          "measure-id": "id119hr1501",
          "measure-number": "1501",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1501v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Domestic Mining Act of 2025</strong></p><p>This bill provides statutory authority for federal agencies to expedite the environmental review of certain mining infrastructure projects.</p><p>Specifically, the bill permanently makes certain mining infrastructure projects eligible for expedited environmental review under the Fixing America's Surface Transportation Act (FAST Act).\u00a0This provides statutory authority for similar authorities that were included in\u00a0the rule titled <em>Adding Mining as a Sector of Projects Eligible for Coverage Under Title 41 of the Fixing America's Surface Transportation Act\u00a0</em>and issued by the Federal Permitting Improvement Steering Council (Permitting Council) on January 8, 2021. </p><p>The bill also prohibits the Permitting Council from finalizing its proposed rule titled\u00a0<em>Revising Scope of the Mining Sector of Projects That Are Eligible for Coverage Under Title 41 of the Fixing America\u2019s Surface Transportation Act </em>and issued on September 22, 2023. Among other modifications, the rule proposes to limit the types of mining projects that are eligible for the expedited environmental review process. Specifically, the proposed rule limits the expedited process to critical minerals mining projects.</p>"
        },
        "title": "Protecting Domestic Mining Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1501.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Domestic Mining Act of 2025</strong></p><p>This bill provides statutory authority for federal agencies to expedite the environmental review of certain mining infrastructure projects.</p><p>Specifically, the bill permanently makes certain mining infrastructure projects eligible for expedited environmental review under the Fixing America's Surface Transportation Act (FAST Act).\u00a0This provides statutory authority for similar authorities that were included in\u00a0the rule titled <em>Adding Mining as a Sector of Projects Eligible for Coverage Under Title 41 of the Fixing America's Surface Transportation Act\u00a0</em>and issued by the Federal Permitting Improvement Steering Council (Permitting Council) on January 8, 2021. </p><p>The bill also prohibits the Permitting Council from finalizing its proposed rule titled\u00a0<em>Revising Scope of the Mining Sector of Projects That Are Eligible for Coverage Under Title 41 of the Fixing America\u2019s Surface Transportation Act </em>and issued on September 22, 2023. Among other modifications, the rule proposes to limit the types of mining projects that are eligible for the expedited environmental review process. Specifically, the proposed rule limits the expedited process to critical minerals mining projects.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr1501"
    },
    "title": "Protecting Domestic Mining Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Domestic Mining Act of 2025</strong></p><p>This bill provides statutory authority for federal agencies to expedite the environmental review of certain mining infrastructure projects.</p><p>Specifically, the bill permanently makes certain mining infrastructure projects eligible for expedited environmental review under the Fixing America's Surface Transportation Act (FAST Act).\u00a0This provides statutory authority for similar authorities that were included in\u00a0the rule titled <em>Adding Mining as a Sector of Projects Eligible for Coverage Under Title 41 of the Fixing America's Surface Transportation Act\u00a0</em>and issued by the Federal Permitting Improvement Steering Council (Permitting Council) on January 8, 2021. </p><p>The bill also prohibits the Permitting Council from finalizing its proposed rule titled\u00a0<em>Revising Scope of the Mining Sector of Projects That Are Eligible for Coverage Under Title 41 of the Fixing America\u2019s Surface Transportation Act </em>and issued on September 22, 2023. Among other modifications, the rule proposes to limit the types of mining projects that are eligible for the expedited environmental review process. Specifically, the proposed rule limits the expedited process to critical minerals mining projects.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr1501"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1501ih.xml"
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
      "title": "Protecting Domestic Mining Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-18T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Domestic Mining Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-18T05:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the FAST Act to include certain mineral production activities as a covered project, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-18T05:18:31Z"
    }
  ]
}
```
