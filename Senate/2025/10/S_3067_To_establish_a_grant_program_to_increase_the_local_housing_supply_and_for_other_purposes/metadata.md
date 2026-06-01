# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3067
- Title: Innovation Fund Act
- Congress: 119
- Bill type: S
- Bill number: 3067
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2025-12-05T22:49:30Z
- Update date including text: 2025-12-05T22:49:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3067",
    "number": "3067",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Innovation Fund Act",
    "type": "S",
    "updateDate": "2025-12-05T22:49:30Z",
    "updateDateIncludingText": "2025-12-05T22:49:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T21:57:33Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3067is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3067\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Ms. Warren (for herself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a grant program to increase the local housing supply, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Innovation Fund Act .\n#### 2. Innovation Fund\n##### (a) Definitions\nIn this section:\n**(1) Attainable housing**\nThe term attainable housing means housing that\u2014\n**(A)**\nserves\u2014\n**(i)**\na majority of households with income not greater than 80 percent of area median income; and\n**(ii)**\nhouseholds with income not greater than 100 percent of area median income; or\n**(B)**\nserves\u2014\n**(i)**\na majority of households with income not greater than 60 percent of area median income; and\n**(ii)**\nhouseholds with income not greater than 120 percent of area median income.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na metropolitan city or urban county, as those terms are defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ), that has demonstrated an objective improvement in housing supply growth, as determined by the Secretary, whose methodology for determining such growth is published in the Federal Register to allow for public comment not less than 90 days before date on which the notice of funding opportunity is made available; or\n**(B)**\na unit of general local government or Indian tribe, as those terms are defined in section 102 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5302 ), that has demonstrated an objective improvement in housing supply growth, as determined by the Secretary, whose methodology for determining such improvement is published in the Federal Register to allow for public comment not less than 90 days before the date on which the notice of funding opportunity is made available.\n**(3) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n##### (b) Establishment of a grant program\n**(1) Establishment**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish a program to award grants on a competitive basis to eligible entities that have increased their local housing supply.\n**(2) List of eligible entities**\nThe Secretary shall make a list of eligible entities publicly available on the website of the Department of Housing and Urban Development.\n**(3) Eligible purposes**\nAn eligible entity receiving a grant under this section may use funds to\u2014\n**(A)**\ncarry out any of the activities described in section 105 of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5305 );\n**(B)**\ncarry out any of the activities permitted under the Local and Regional Project Assistance Program established under section 6702 of title 49, United States Code;\n**(C)**\nserve as matching funds under a State revolving fund program related to a clean water or drinking water program administered by the Environmental Protection Agency in which the eligible entity is the grantee under that program, unless otherwise determined by the Secretary; and\n**(D)**\ncarry out initiatives of the eligible entity that facilitate the expansion of the supply of attainable housing and that supplement initiatives the eligible entity has carried out, or is in the process of carrying out, as specified in the application submitted under paragraph (4).\n**(4) Application**\n**(A) In general**\nAn eligible entity seeking a grant under this section shall submit to the Secretary an application that provides\u2014\n**(i)**\na description of each purpose for which the eligible entity will use the grant, and an attestation that the grant will be used only for 1 or more eligible purposes described in paragraph (3);\n**(ii)**\ndata on characteristics of increased housing supply during the 3-year period ending on the date on which the application is submitted, which may include whether such housing\u2014\n**(I)**\nserves households at a range of income levels; and\n**(II)**\nhas improved the quality and affordability of housing in the jurisdiction of the eligible entity;\n**(iii)**\na description of how each eligible purpose described in clause (i) may address a community need or advance an objective, or an aspect of an objective, included in the comprehensive housing affordability strategy and community development plan of the eligible entity under part 91 of title 24, Code of Federal Regulations, or any successor regulation (commonly referred to as a consolidated plan ); and\n**(iv)**\na description of how the eligible entity has carried out, or is in the process of carrying out, initiatives that facilitate the expansion of the supply of housing.\n**(B) Initiatives**\nInitiatives that meet the criteria described in paragraph (3)(D) include\u2014\n**(i)**\nincreasing by-right uses, including duplex, triplex, quadplex, and multifamily buildings, in areas of opportunity;\n**(ii)**\nrevising or eliminating off-street parking requirements to reduce the cost of housing production;\n**(iii)**\nrevising minimum lot size requirements, floor area ratio requirements, set-back requirements, building heights, and bans or limits on construction to allow for denser and more affordable development;\n**(iv)**\ninstituting incentives to promote dense development;\n**(v)**\npassing zoning overlays or other ordinances that enable the development of mixed-income housing;\n**(vi)**\nstreamlining regulatory requirements and shortening processes, increasing code enforcement and permitting capacity, reforming zoning codes, or other initiatives that reduce barriers to increasing housing supply and affordability;\n**(vii)**\neliminating restrictions against accessory dwelling units and expanding their by-right use;\n**(viii)**\nusing local tax incentives or public financing to promote development of attainable housing;\n**(ix)**\nstreamlining environmental regulations;\n**(x)**\neliminating unnecessary manufactured-housing regulations and restrictions;\n**(xi)**\nminimizing the impact of overburdensome energy and water efficiency standards on housing costs; and\n**(xii)**\nother activities that reduce cost of construction, as determined by the Secretary.\n**(5) Grants**\n**(A) In general**\nThe Secretary shall make not fewer than 25 grants on an annual basis (unless amounts appropriated to provide grant amounts consistent with subsection (b) are insufficient, in which case fewer grants may be awarded), with strong consideration of different geographical areas and a relatively even spread of rural, suburban, and urban communities.\n**(B) Limitations on awards**\nNo grant awarded under this paragraph may be\u2014\n**(i)**\nmore than $10,000,000; or\n**(ii)**\nless than $250,000.\n**(C) Priority**\nWhen awarding grants under this paragraph, the Secretary shall give priority to an eligible entity that has\u2014\n**(i)**\ndemonstrated the use of innovative policies, interventions, or programs for increasing housing supply, including adoption of any of the frameworks developed under section 203; and\n**(ii)**\ndemonstrated a marked improvement in housing supply growth.\n**(D) Grant administration and terms**\nProjects assisted under this section for activities described in sector 23 of the North American Industry Classification System shall be treated as projects assisted under the Community Development Block Grant program under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. ).\n##### (c) Rules of construction\nNothing in this section shall be construed\u2014\n**(1)**\nto authorize the Secretary to mandate, supersede, or preempt any local zoning or land use policy; or\n**(2)**\nto affect the requirements of section 105(c)(1) of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12705(c)(1) ).\n##### (d) Authorization of appropriations\n**(1) In general**\nThere is authorized to be appropriated to carry out this section $200,000,000 for each of fiscal years 2027 through 2031.\n**(2) Adjustment**\nThe amount authorized to be appropriated under paragraph (1) shall be adjusted for inflation based on the Consumer Price Index.",
      "versionDate": "2025-10-28",
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
        "actionDate": "2025-11-07",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committees on Transportation and Infrastructure, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5938",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Innovation Fund Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 143."
      },
      "number": "2651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROAD to Housing Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-11-19T14:20:04Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3067is.xml"
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
      "title": "Innovation Fund Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Innovation Fund Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a grant program to increase the local housing supply, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T03:48:20Z"
    }
  ]
}
```
