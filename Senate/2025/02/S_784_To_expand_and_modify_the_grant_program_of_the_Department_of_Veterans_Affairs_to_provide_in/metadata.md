# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/784
- Title: Rural Veterans Transportation to Care Act
- Congress: 119
- Bill type: S
- Bill number: 784
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2026-03-19T11:03:25Z
- Update date including text: 2026-03-19T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-05-21 - Committee: Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/784",
    "number": "784",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "O000174",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Ossoff, Jon [D-GA]",
        "lastName": "Ossoff",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Rural Veterans Transportation to Care Act",
    "type": "S",
    "updateDate": "2026-03-19T11:03:25Z",
    "updateDateIncludingText": "2026-03-19T11:03:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held. Hearings printed: S.Hrg. 119-86.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-27",
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
        "item": [
          {
            "date": "2025-05-21T20:00:18Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-05-21T20:00:18Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-02-27T18:08:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "ME"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "CA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s784is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 784\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Ossoff (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo expand and modify the grant program of the Department of Veterans Affairs to provide innovative transportation options to veterans in highly rural areas, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Rural Veterans Transportation to Care Act .\n#### 2. Expansion and modification of transportation grant program of Department of Veterans Affairs\nSection 307 of the Caregivers and Veterans Omnibus Health Services Act of 2010 ( Public Law 111\u2013163 ; 38 U.S.C. 1710 note) is amended\u2014\n**(1)**\nin the section heading, by inserting rural or before highly ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby inserting rural or before highly each place it appears;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby redesignating subparagraph (B) as subparagraph (C);\n**(ii)**\nby inserting after subparagraph (A) the following new subparagraph (B):\n(B) County veterans service organizations. ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(D) Tribal organizations. ;\n**(C)**\nin paragraph (3), by striking A State veterans service agency or veterans service organization awarded and inserting A recipient of ; and\n**(D)**\nby striking paragraph (4) and inserting the following new paragraph (4):\n(4) Maximum amount (A) In general Except as provided in subparagraph (B), the amount of a grant under this section may not exceed $60,000. (B) Additional amount to purchase a vehicle The amount of a grant under this section to a recipient may be increased to an amount not to exceed $80,000 if the recipient is required to purchase a vehicle to comply with the requirements of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12101 et seq. ) in carrying out this section. ;\n**(3)**\nin subsection (c), by striking paragraph (1) and inserting the following:\n(1) Rural; highly rural The terms rural and highly rural have the meanings given those terms under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. ; and\n**(4)**\nin subsection (d), by striking $3,000,000 for each of fiscal years 2010 through 2022 and inserting such sums as may be necessary .",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-03-27",
        "text": "Referred to the Subcommittee on Health."
      },
      "number": "1733",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rural Veterans Transportation to Care Act",
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
            "name": "Rural conditions and development",
            "updateDate": "2025-06-03T15:59:55Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-06-03T15:59:50Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-03T15:59:50Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-06-03T15:59:50Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-04T20:06:47Z"
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
          "measure-id": "id119s784",
          "measure-number": "784",
          "measure-type": "s",
          "orig-publish-date": "2025-02-27",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s784v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>"
        },
        "title": "Rural Veterans Transportation to Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s784.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s784"
    },
    "title": "Rural Veterans Transportation to Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Rural Veterans Transportation to Care Act</strong></p><p>This bill expands and makes permanent the Department of Veterans Affairs (VA) grant program that provides transportation options to veterans for medical purposes.</p><p>First, the bill expands the program to cover transportation for veterans in rural areas, in addition to veterans in highly rural areas (who are already eligible under the program).</p><p>The bill also authorizes the VA to award such grants to county veterans service organizations and tribal organizations to assist veterans with transportation for medical care.</p><p>Further, the bill increases the maximum grant amount to $60,000. However, if a grant recipient is required to purchase a vehicle to comply with the Americans with Disabilities Act of 1990, such grant amount may be increased to not more than $80,000.</p><p>Finally, the bill defines<em> rural</em> and <em>highly rural </em>in the same manner as the terms are given under the Rural-Urban Commuting Areas (RUCA) coding system of the Department of Agriculture. RUCA uses population density and commuting patterns to assign designations.\u00a0</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s784"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s784is.xml"
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
      "title": "Rural Veterans Transportation to Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Rural Veterans Transportation to Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand and modify the grant program of the Department of Veterans Affairs to provide innovative transportation options to veterans in highly rural areas, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:04:17Z"
    }
  ]
}
```
