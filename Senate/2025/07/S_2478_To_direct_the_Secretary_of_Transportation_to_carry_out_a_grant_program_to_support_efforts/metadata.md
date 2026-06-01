# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2478
- Title: Freedom to Move Act
- Congress: 119
- Bill type: S
- Bill number: 2478
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-12-05T21:52:09Z
- Update date including text: 2025-12-05T21:52:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2478",
    "number": "2478",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Freedom to Move Act",
    "type": "S",
    "updateDate": "2025-12-05T21:52:09Z",
    "updateDateIncludingText": "2025-12-05T21:52:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
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
      "actionDate": "2025-07-28",
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
          "date": "2025-07-28T21:50:22Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-07-28",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2478is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2478\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Mr. Markey (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo direct the Secretary of Transportation to carry out a grant program to support efforts to provide fare-free transit service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom to Move Act .\n#### 2. Purpose\nThe purposes of this Act are\u2014\n**(1)**\nto invest in State, county, and local municipalities efforts to provide fare-free public transportation; and\n**(2)**\nto support State, county, and local municipalities in improving and expanding access to safe, accessible, and reliable mass transit systems in order to improve the livability of communities.\n#### 3. Definitions\nIn this Act:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State, county, or local municipality;\n**(B)**\na transit agency;\n**(C)**\na private nonprofit organization engaged in public transportation in rural areas; or\n**(D)**\na partnership between entities described in subparagraphs (A) through (C).\n**(2) Foster care youth**\nThe term foster care youth \u2014\n**(A)**\nmeans children and youth whose care and placement are the responsibility of the State or Tribal agency that administers a State or Tribal plan under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 670 et seq.), without regard to whether foster care maintenance payments are made under section 472 of such Act ( 42 U.S.C. 672 ) on behalf of such children and youth; and\n**(B)**\nincludes individuals who were age 13 or older when their care and placement were the responsibility of a State or Tribal agency that administered a State or Tribal plan under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. , 670 et seq.) and who are no longer under the care and responsibility of such a State or Tribal agency, without regard to any such individual\u2019s subsequent adoption, guardianship arrangement, or other form of permanency outcome.\n**(3) Low-income individuals**\nThe term low-income individuals means an individual whose family income is at or below 150 percent of the poverty line (as that term is defined in section 673(2) of the Community Service Block Grant Act ( 42 U.S.C. 9902(2) ), including any revision required by that section) for a family of the size involved.\n**(4) Public transportation**\nThe term public transportation \u2014\n**(A)**\nmeans regular, continuing shared-ride surface transportation services that are open to the general public or open to a segment of the general public defined by age, disability, or low income; and\n**(B)**\ndoes not include\u2014\n**(i)**\nintercity passenger rail transportation provided by the entity described in chapter 243 of title 49, United States Code (or a successor to such entity);\n**(ii)**\nintercity bus service;\n**(iii)**\ncharter bus service;\n**(iv)**\nschool bus service;\n**(v)**\nsightseeing service;\n**(vi)**\ncourtesy shuttle service for patrons of one or more specific establishments; or\n**(vii)**\nintra-terminal or intra-facility shuttle services.\n**(5) Underserved community**\nThe term underserved community means\u2014\n**(A)**\na community not served by existing bus routes or infrequent service; and\n**(B)**\na community located in an area within a census tract that is identified as\u2014\n**(i)**\na low-income community; and\n**(ii)**\na community of color.\n#### 4. Grants to support fare-free transit\n##### (a) In general\nNot later than 360 days after the date of enactment of this Act, the Secretary shall award grants, which shall be known as Freedom to Move Grants , to eligible entities, on a competitive basis, to cover the lost fare revenue for fare-free public transportation and improve public transportation.\n##### (b) Application\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum, the following:\n**(1)**\nA description of how the eligible entity plans to implement fare-free transit access.\n**(2)**\nA description of how the entity will work to expand and improve bus service, which may include\u2014\n**(A)**\na bus network redesign;\n**(B)**\nhow such redesign will prioritize consistent and reliable service for low-income and historically underserved communities;\n**(C)**\nhow such redesign will prioritize connectivity to critical services and improve community livability; and\n**(D)**\nhow the eligible entity will meaningfully consult with community, community leaders, local stakeholders and advocates, including transit advocates and disability advocates, local education agencies and institutions of higher education, community developers, labor unions, public housing agencies and workforce development boards, while facilitating such redesign.\n**(3)**\nA description of how the eligible entity will meaningfully partner and collaborate with community, community leaders, local stakeholders and advocates, including transit advocates and disability advocates, local education agencies and institutions of higher education, community developers, labor unions, public housing agencies, and workforce development boards to support outreach efforts to increase awareness of fare-free bus and transit programs.\n**(4)**\nA description of the eligible entity\u2019s equity evaluation examining any transit and mobility gaps within the current transit system and how the eligible entity plans to significantly improve these gaps, including\u2014\n**(A)**\nthe average commute times for driver commuters and non-driver commuters;\n**(B)**\npublic transit ridership rates disaggregated by mode of transportation and demographic group, including youth (including youth involved in the foster care system), seniors, individuals with disabilities, and low-income status; and\n**(C)**\naverage length of bus routes and average delay times.\n**(5)**\nA description of the eligible entity\u2019s current fare evasion enforcement policies, including\u2014\n**(A)**\nthe cost of the fine and whether the infraction is considered a civil offense or a criminal offense punishable by imprisonment;\n**(B)**\nthe number of individuals charged with violating a fare evasion policy, disaggregated by age, race, gender, and disability status; and\n**(C)**\nhow the eligible entity plans to eliminate fare evasion policies and end the criminalization of individuals evading fares.\n**(6)**\nAn estimate of additional costs as a result of increased ridership, including\u2014\n**(A)**\nfuel;\n**(B)**\npersonnel;\n**(C)**\nmaintenance; and\n**(D)**\nother operational costs.\n**(7)**\nInformation and statistics on assaults on transit employees and a description of trainings and policies to protect employees, which may include de-escalation training.\n##### (c) Duration\nGrants awarded under this section shall be for a 5-year period.\n##### (d) Selection of eligible entities\nIn carrying out the program under this section, the Secretary shall award grants to eligible entities located in both rural and urbanized areas.\n##### (e) Uses of funds\nAn eligible entity that receives a grant under this section shall use such grant to support\u2014\n**(1)**\nimplementing a fare-free transit program; and\n**(2)**\nefforts to improve public transportation, particularly in underserved communities, including costs associated with efforts to provide more safe, frequent, and reliable bus service, including\u2014\n**(A)**\nbus stop safety and accessibility improvements;\n**(B)**\npedestrian and bike shelters;\n**(C)**\nsignage;\n**(D)**\npainted bus lanes;\n**(E)**\nsignal priority systems;\n**(F)**\nstreet redesign;\n**(G)**\noperational costs to meet demands of increased ridership, including hiring and training of personnel; and\n**(H)**\nconducting a bus network redesign.\n##### (f) Report\n**(1) In general**\nNot later than 3 years after the date on which funds are made available to carry out this section, the Secretary shall collect data from eligible entities receiving a grant under this section on the progress of meeting the targets described in the application of such entity.\n**(2) Requirements**\nThe report required under paragraph (1) shall\u2014\n**(A)**\ncollect data on demographics of communities served under this Act, disaggregated and cross-tabulated by\u2014\n**(i)**\nrace;\n**(ii)**\nethnicity;\n**(iii)**\nsex; and\n**(iv)**\nhousehold median income; and\n**(B)**\nprogress towards significantly closing transit equity gaps as described in subsection (b)(4).\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-07-28",
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
        "actionDate": "2025-07-24",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "4719",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Freedom to Move Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-16T17:46:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-28",
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
          "measure-id": "id119s2478",
          "measure-number": "2478",
          "measure-type": "s",
          "orig-publish-date": "2025-07-28",
          "originChamber": "SENATE",
          "update-date": "2025-09-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2478v00",
            "update-date": "2025-09-19"
          },
          "action-date": "2025-07-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>"
        },
        "title": "Freedom to Move Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2478.xml",
    "summary": {
      "actionDate": "2025-07-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119s2478"
    },
    "title": "Freedom to Move Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119s2478"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2478is.xml"
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
      "title": "Freedom to Move Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom to Move Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Secretary of Transportation to carry out a grant program to support efforts to provide fare-free transit service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:31Z"
    }
  ]
}
```
