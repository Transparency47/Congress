# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1733?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1733
- Title: Rural Veterans Transportation to Care Act
- Congress: 119
- Bill type: HR
- Bill number: 1733
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2025-12-19T09:07:03Z
- Update date including text: 2025-12-19T09:07:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1733",
    "number": "1733",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Rural Veterans Transportation to Care Act",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:03Z",
    "updateDateIncludingText": "2025-12-19T09:07:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:15:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:02:16Z",
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
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AZ"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NM"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NC"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SD"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "OH"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "IA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "WA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-07-25",
      "state": "WA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "KY"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "NV"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1733ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1733\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Ms. Perez (for herself, Mr. Ciscomani , Mr. Vasquez , Mr. Davis of North Carolina , Mr. Johnson of South Dakota , Mr. Joyce of Ohio , Mr. Golden of Maine , and Ms. Pettersen ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo expand and modify the grant program of the Department of Veterans Affairs to provide innovative transportation options to veterans in highly rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Veterans Transportation to Care Act .\n#### 2. Expansion and modification of transportation grant program of Department of Veterans Affairs\nSection 307 of the Caregivers and Veterans Omnibus Health Services Act of 2010 ( Public Law 111\u2013163 ; 38 U.S.C. 1710 note) is amended\u2014\n**(1)**\nin the section heading, by inserting rural or before highly ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby inserting rural or before highly each place it appears;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(ii)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) County veterans service organizations. ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(D) Tribal organizations. ;\n**(C)**\nin paragraph (3), by striking A State veterans service agency or veterans service organization awarded and inserting A recipient of ; and\n**(D)**\nby striking paragraph (4) and inserting the following new paragraph (4):\n(4) Maximum amount (A) In general Except as provided in subparagraph (B), the amount of a grant under this section may not exceed $60,000. (B) Additional amount to purchase a vehicle The amount of a grant under this section to a recipient may be increased to an amount not to exceed $80,000 if the recipient is required to purchase a vehicle to comply with the requirements of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) in carrying out this section. ;\n**(3)**\nin subsection (c), by striking paragraph (1) and inserting the following:\n(1) Rural; highly rural The terms rural and highly rural have the meanings given those terms under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. ; and\n**(4)**\nin subsection (d), by striking $3,000,000 for each of fiscal years 2010 through 2022 and inserting such sums as may be necessary .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-05-21",
        "text": "Committee on Veterans' Affairs. Hearings held."
      },
      "number": "784",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rural Veterans Transportation to Care Act",
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
            "name": "Rural conditions and development",
            "updateDate": "2025-06-03T16:00:07Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-06-03T16:00:07Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-03T16:00:07Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-06-03T16:00:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T19:55:38Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1733",
          "measure-number": "1733",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1733v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>"
        },
        "title": "Rural Veterans Transportation to Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1733.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1733"
    },
    "title": "Rural Veterans Transportation to Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119hr1733"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1733ih.xml"
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
      "title": "Rural Veterans Transportation to Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Veterans Transportation to Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T10:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand and modify the grant program of the Department of Veterans Affairs to provide innovative transportation options to veterans in highly rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T10:18:34Z"
    }
  ]
}
```
