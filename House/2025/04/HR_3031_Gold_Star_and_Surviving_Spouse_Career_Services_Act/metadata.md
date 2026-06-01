# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3031?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3031
- Title: Gold Star and Surviving Spouse Career Services Act
- Congress: 119
- Bill type: HR
- Bill number: 3031
- Origin chamber: House
- Introduced date: 2025-04-28
- Update date: 2026-04-24T22:14:28Z
- Update date including text: 2026-04-24T22:14:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-28: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-04-28: Introduced in House

## Actions

- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Introduced in House
- 2025-04-28 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-12 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-28",
    "latestAction": {
      "actionDate": "2025-04-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3031",
    "number": "3031",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Gold Star and Surviving Spouse Career Services Act",
    "type": "HR",
    "updateDate": "2026-04-24T22:14:28Z",
    "updateDateIncludingText": "2026-04-24T22:14:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-28",
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
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-28",
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
          "date": "2025-04-28T16:00:35Z",
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
                "date": "2025-06-11T13:55:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-12T13:54:45Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3031ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3031\nIN THE HOUSE OF REPRESENTATIVES\nApril 28, 2025 Mr. Bacon introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to make certain spouses eligible for services under the disabled veterans\u2019 outreach program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gold Star and Surviving Spouse Career Services Act .\n#### 2. Eligibility of spouses for services under the disabled veterans\u2019 outreach program\nSection 4103A of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by inserting and eligible persons after eligible veterans ; and\n**(ii)**\nin subparagraph (C), by inserting , and eligible persons, after Other eligible veterans ;\n**(B)**\nin paragraph (2), by inserting and eligible persons after veterans each place it appears; and\n**(C)**\nin paragraph (3)\u2014\n**(i)**\nby inserting or eligible person after veteran each place it appears; and\n**(ii)**\nby inserting or eligible person\u2019s after veteran\u2019s ;\n**(2)**\nin subsection (d)(1)\u2014\n**(A)**\nby inserting and eligible persons after eligible veterans each place it appears; and\n**(B)**\nby striking non-veteran-related ; and\n**(3)**\nby adding at the end the following new subsection:\n(e) Eligible person defined In this section, the term eligible person means\u2014 (1) any spouse described in section 4101(5) of this title; or (2) the spouse of any person who died while a member of the Armed Forces. .",
      "versionDate": "2025-04-28",
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
        "actionDate": "2025-12-19",
        "actionTime": "14:40:31",
        "text": "Held at the desk."
      },
      "number": "1204",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Gold Star and Surviving Spouse Career Services Act",
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
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-26T16:45:25Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-26T16:45:25Z"
          },
          {
            "name": "Veterans' pensions and compensation",
            "updateDate": "2025-06-26T16:45:25Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-28T20:53:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-28",
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
          "measure-id": "id119hr3031",
          "measure-number": "3031",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-28",
          "originChamber": "HOUSE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3031v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2025-04-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>"
        },
        "title": "Gold Star and Surviving Spouse Career Services Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3031.xml",
    "summary": {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr3031"
    },
    "title": "Gold Star and Surviving Spouse Career Services Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gold Star and Surviving Spouse Career Services Act</strong></p><p>This bill expands eligibility for the Disabled Veterans\u2019 Outreach Program to the spouses of certain veterans and members of the Armed Forces. Such program is administered by the Department of Labor and generally provides career and employment services to disabled veterans.</p><p>The bill expands eligibility for the program to spouses of</p><ul><li>persons who died while members of the Armed Forces;</li><li>persons who died of a service-connected disability;</li><li>members of the Armed Forces serving on active duty who, for more than 90 days, are listed as missing in action, captured by a hostile force, or forcibly detained or interned in the line of duty by a foreign government power;</li><li>persons who have a total permanent disability resulting from a service-connected disability; and</li><li>persons who died while an evaluated total disability was in existence.</li></ul>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hr3031"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3031ih.xml"
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
      "title": "Gold Star and Surviving Spouse Career Services Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-08T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gold Star and Surviving Spouse Career Services Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-08T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to make certain spouses eligible for services under the disabled veterans' outreach program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-08T04:33:18Z"
    }
  ]
}
```
