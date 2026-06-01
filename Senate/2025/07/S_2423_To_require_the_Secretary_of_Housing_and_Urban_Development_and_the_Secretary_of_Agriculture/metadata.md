# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2423?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2423
- Title: Streamlining Rural Housing Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2423
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2026-01-15T12:03:40Z
- Update date including text: 2026-01-15T12:03:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2423",
    "number": "2423",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Streamlining Rural Housing Act of 2025",
    "type": "S",
    "updateDate": "2026-01-15T12:03:40Z",
    "updateDateIncludingText": "2026-01-15T12:03:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
            "date": "2025-07-23T22:17:19Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-23T22:17:19Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NH"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "NE"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "AZ"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "VA"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "NE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NV"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "ID"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NH"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2423is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2423\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Moran (for himself, Mrs. Shaheen , Mr. Ricketts , and Mr. Gallego ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of Housing and Urban Development and the Secretary of Agriculture to enter into a memorandum of understanding relating to housing projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Rural Housing Act of 2025 .\n#### 2. Memorandum of understanding\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall enter into a memorandum of understanding to\u2014\n**(1)**\nevaluate categorical exclusions (as defined in section 111 of the National Environmental Policy Act of 1969 ( 42 U.S.C. 4336e )) for housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture;\n**(2)**\ndevelop a process to designate a lead agency among the Department of Housing and Urban Development and the Department of Agriculture and streamline the adoption of environmental impact statements and environmental assessments approved by the other agency to construct housing projects funded by amounts from both agencies;\n**(3)**\nmaintain compliance with environmental regulations under part 58 of title 24, Code of Federal Regulations, as in effect on January 1, 2025; and\n**(4)**\nevaluate the feasibility of a joint physical inspection process for housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture.\n##### (b) Advisory working group\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall establish an advisory working group for the purpose of consulting on the implementation of the memorandum of understanding entered into under subsection (a).\n**(2) Members**\nThe advisory working group established under paragraph (1) shall consist of rural and non-rural stakeholders, including\u2014\n**(A)**\naffordable housing nonprofit organizations;\n**(B)**\nState housing and housing finance agencies;\n**(C)**\nnonprofit and for-profit home builders and housing developers;\n**(D)**\nproperty management companies;\n**(E)**\nowners of multifamily properties, including nonprofit and for-profit owners and operators;\n**(F)**\npublic housing agencies;\n**(G)**\nresidents in housing assisted by the Department of Housing and Urban Development or the Department of Agriculture and representatives of those residents; and\n**(H)**\nhousing contract administrators.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary of Housing and Urban Development and the Secretary of Agriculture shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report that includes recommendations for legislative, regulatory, or administrative actions\u2014\n**(1)**\nto improve the efficiency and effectiveness of housing projects funded by amounts from the Department of the Housing and Urban Development and the Department of Agriculture; and\n**(2)**\nthat do not materially, with respect to residents of housing projects described in paragraph (1)\u2014\n**(A)**\nreduce the safety of those residents;\n**(B)**\nshift long-term costs onto those residents; or\n**(C)**\nundermine the environmental standards of those residents.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-08-15",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "4989",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Streamlining Rural Housing Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-09-12T15:14:20Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2423is.xml"
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
      "title": "Streamlining Rural Housing Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-15T12:03:40Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Streamlining Rural Housing Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Housing and Urban Development and the Secretary of Agriculture to enter into a memorandum of understanding relating to housing projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:29Z"
    }
  ]
}
```
