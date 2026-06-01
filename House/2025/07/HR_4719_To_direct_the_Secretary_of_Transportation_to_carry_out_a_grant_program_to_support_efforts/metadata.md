# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4719?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4719
- Title: Freedom to Move Act
- Congress: 119
- Bill type: HR
- Bill number: 4719
- Origin chamber: House
- Introduced date: 2025-07-23
- Update date: 2026-04-21T08:05:51Z
- Update date including text: 2026-04-21T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-23: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-23: Introduced in House

## Actions

- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Introduced in House
- 2025-07-23 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-24 - Committee: Referred to the Subcommittee on Highways and Transit.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4719",
    "number": "4719",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "P000617",
        "district": "7",
        "firstName": "Ayanna",
        "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
        "lastName": "Pressley",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Freedom to Move Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:05:51Z",
    "updateDateIncludingText": "2026-04-21T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-23",
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
          "date": "2025-07-23T14:15:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-24T21:30:50Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NC"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OH"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MO"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "SC"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "LA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "PA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NJ"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "WI"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "DC"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MN"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MI"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "GA"
    },
    {
      "bioguideId": "O000172",
      "district": "14",
      "firstName": "Alexandria",
      "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Ocasio-Cortez",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CT"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "RI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4719ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4719\nIN THE HOUSE OF REPRESENTATIVES\nJuly 23, 2025 Ms. Pressley (for herself, Ms. Adams , Mrs. Beatty , Mr. Bishop , Ms. Brown , Mr. Carson , Mr. Cleaver , Mr. Clyburn , Ms. Crockett , Mr. Davis of Illinois , Mr. Fields , Mr. Jackson of Illinois , Mr. Johnson of Georgia , Ms. Lee of Pennsylvania , Mrs. McIver , Ms. Moore of Wisconsin , Ms. Norton , Ms. Omar , Mrs. Ramirez , Ms. Simon , Ms. Tlaib , and Ms. Williams of Georgia ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to carry out a grant program to support efforts to provide fare-free transit service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Freedom to Move Act .\n#### 2. Purpose\nThe purposes of this Act are\u2014\n**(1)**\nto invest in State, county, and local municipalities efforts to provide fare-free public transportation; and\n**(2)**\nto support State, county, and local municipalities in improving and expanding access to safe, accessible, and reliable mass transit systems in order to improve the livability of communities.\n#### 3. Grants to support fare-free transit\n##### (a) In general\nNot later than 360 days after the date of enactment of this Act, the Secretary shall award grants (which shall be known as Freedom to Move Grants ) to eligible entities, on a competitive basis, to cover the lost fare revenue for fare-free public transportation and improve public transportation.\n##### (b) Application\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, including, at a minimum, the following:\n**(1)**\nA description of how the eligible entity plans to implement fare free transit access.\n**(2)**\nA description of how the entity will work to expand and improve bus service, which may include\u2014\n**(A)**\na bus network redesign;\n**(B)**\nhow such redesign will prioritize consistent and reliable service for low-income and historically underserved communities;\n**(C)**\nhow such redesign will prioritize connectivity to critical services and improve community livability; and\n**(D)**\nhow the eligible entity will meaningfully consult with community, community leaders, local stakeholders and advocates, including transit advocates and disability advocates, local education agencies and institutions of higher education, community developers, labor unions, public housing agencies and workforce development boards, while facilitating such redesign.\n**(3)**\nA description of how the eligible entity will meaningfully partner and collaborate with community, community leaders, local stakeholders and advocates, including transit advocates and disability advocates, local education agencies and institutions of higher education, community developers, labor unions, public housing agencies and workforce development boards to support outreach efforts to increase awareness of fare-free bus and transit programs.\n**(4)**\nA description of the eligible entity\u2019s equity evaluation examining any transit and mobility gaps within the current transit system and how the eligible entity plans to significantly improve these gaps, including\u2014\n**(A)**\nthe average commute times for driver commuters and non-driver commuters;\n**(B)**\npublic transit ridership rates disaggregated by mode of transportation and demographic group (youth (including youth involved in the foster care system), seniors, individuals with disabilities, and low-income status); and\n**(C)**\naverage length of bus routes and average delay times.\n**(5)**\nA description of the eligible entity\u2019s current fare evasion enforcement policies, including\u2014\n**(A)**\nthe cost of the fine and whether the infraction is considered a civil offense or a criminal offense punishable by imprisonment;\n**(B)**\nthe number of individuals charged with violating a fare evasion policy, disaggregated by age, race, gender, and disability status; and\n**(C)**\nhow the eligible entity plans to eliminate fare evasion policies and end the criminalization of individuals evading fares.\n**(6)**\nAn estimate of additional costs as a result of increased ridership, including\u2014\n**(A)**\nfuel;\n**(B)**\npersonnel;\n**(C)**\nmaintenance; and\n**(D)**\nother operational costs.\n**(7)**\nInformation and statistics on assaults on transit employees and a description of trainings and policies to protect employees, which may include de-escalation training.\n##### (c) Duration\nGrants awarded under this section shall be for a 5-year period.\n##### (d) Selection of eligible entities\nIn carrying out the program under this section, the Secretary shall award grants to eligible entities located in both rural and urbanized areas.\n##### (e) Uses of funds\nAn eligible entity that receives a grant under this section shall use such grant to support\u2014\n**(1)**\nimplementing a fare-free transit program; and\n**(2)**\nefforts to improve public transportation, particularly in underserved communities, including costs associated with efforts to provide more safe, frequent, and reliable bus service, including\u2014\n**(A)**\nbus stop safety and accessibility improvements;\n**(B)**\npedestrian and bike shelters;\n**(C)**\nsignage;\n**(D)**\npainted bus lanes;\n**(E)**\nsignal priority systems;\n**(F)**\nstreet redesign;\n**(G)**\noperational costs to meet demands of increased ridership, including hiring and training of personnel; and\n**(H)**\nconducting a bus network redesign.\n##### (f) Definitions\nIn this section:\n**(1) Eligible entities**\nIn this section, the term eligible entity means\u2014\n**(A)**\na State, county, local municipality;\n**(B)**\na transit agency;\n**(C)**\na private nonprofit organization engaged in public transportation in rural areas; or\n**(D)**\na partnership between entities described in subparagraphs (A) through (C).\n**(2) Underserved community**\nThe term underserved community means\u2014\n**(A)**\na community not served by existing bus routes or infrequent service; and\n**(B)**\na community located in an area within a census tract that is identified as\u2014\n**(i)**\na low-income community; and\n**(ii)**\na community of color.\n**(3) Low-income individuals**\nThe term low-income individuals means an individual whose family income is at or below 150 percent of the poverty line (as that term is defined in section 673(2) of the Community Service Block Grant Act ( 42 U.S.C. 9902(2) ), including any revision required by that section) for a family of the size involved.\n**(4) Foster care youth**\nThe term foster care youth \u2014\n**(A)**\nmeans children and youth whose care and placement are the responsibility of the State or Tribal agency that administers a State or Tribal plan under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. and 670 et seq.), without regard to whether foster care maintenance payments are made under section 472 of such Act ( 42 U.S.C. 672 ) on behalf of such children and youth; and\n**(B)**\nincludes individuals who were age 13 or older when their care and placement were the responsibility of a State or Tribal agency that administered a State or Tribal plan under part B or E of title IV of the Social Security Act ( 42 U.S.C. 621 et seq. and 670 et seq.) and who are no longer under the care and responsibility of such a State or Tribal agency, without regard to any such individual\u2019s subsequent adoption, guardianship arrangement, or other form of permanency outcome.\n**(5) Public transportation**\nThe term public transportation \u2014\n**(A)**\nmeans regular, continuing shared-ride surface transportation services that are open to the general public or open to a segment of the general public defined by age, disability, or low income; and\n**(B)**\ndoes not include\u2014\n**(i)**\nintercity passenger rail transportation provided by the entity described in chapter 243 of title 49, United States Code (or a successor to such entity);\n**(ii)**\nintercity bus service;\n**(iii)**\ncharter bus service;\n**(iv)**\nschool bus service;\n**(v)**\nsightseeing service;\n**(vi)**\ncourtesy shuttle service for patrons of one or more specific establishments; or\n**(vii)**\nintra-terminal or intra-facility shuttle services.\n##### (g) Report\n**(1) In general**\nNot later than 3 years after the date on which funds are made available to carry out this section, the Secretary shall collect data from eligible entities receiving a grant under this section on the progress of meeting the targets described in the application of such entity.\n**(2) Requirements**\nThe report required under paragraph (1) shall\u2014\n**(A)**\ncollect data on demographics of communities served under this Act, disaggregated and cross-tabulated by\u2014\n**(i)**\nrace;\n**(ii)**\nethnicity;\n**(iii)**\nsex; and\n**(iv)**\nhousehold median income; and\n**(B)**\nprogress towards significantly closing transit equity gaps as described in subsection (b)(4).\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $5,000,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-07-23",
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
        "actionDate": "2025-07-28",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2478",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Freedom to Move Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-16T17:45:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-23",
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
          "measure-id": "id119hr4719",
          "measure-number": "4719",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-23",
          "originChamber": "HOUSE",
          "update-date": "2025-09-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4719v00",
            "update-date": "2025-09-19"
          },
          "action-date": "2025-07-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>"
        },
        "title": "Freedom to Move Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4719.xml",
    "summary": {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119hr4719"
    },
    "title": "Freedom to Move Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-23",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Freedom to Move Act</b></p> <p>This bill directs the Department of Transportation to award competitive five-year grants (i.e., Freedom to Move Grants) to states, local governments, transit agencies, and nonprofit organizations in both rural and urban areas to cover the lost fare revenue for fare-free public transportation and improve public transportation.</p> <p>Grants must be used to support (1) implementing a fare-free transit program; and (2) efforts to improve public transportation, particularly in underserved communities, such as costs associated with efforts to provide more safe, frequent, and reliable bus service, including bus stop safety and accessibility improvements, and pedestrian and bike shelters.</p>",
      "updateDate": "2025-09-19",
      "versionCode": "id119hr4719"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4719ih.xml"
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
      "title": "Freedom to Move Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Freedom to Move Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to carry out a grant program to support efforts to provide fare-free transit service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:49:01Z"
    }
  ]
}
```
