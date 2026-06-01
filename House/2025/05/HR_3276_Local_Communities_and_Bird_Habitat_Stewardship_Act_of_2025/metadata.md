# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3276
- Title: Local Communities & Bird Habitat Stewardship Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3276
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-05-13T08:06:21Z
- Update date including text: 2026-05-13T08:06:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-01-28 - Committee: Referred to the Subcommittee on Water, Wildlife and Fisheries.
- 2026-02-04 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3276",
    "number": "3276",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Local Communities & Bird Habitat Stewardship Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:21Z",
    "updateDateIncludingText": "2026-05-13T08:06:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "actionDate": "2026-01-28",
      "committees": {
        "item": {
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water, Wildlife and Fisheries.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T13:01:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-04T15:00:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-01-28T18:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Water, Wildlife and Fisheries Subcommittee",
          "systemCode": "hsii13"
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "VA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "CA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MD"
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
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "MI"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CT"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PR"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NV"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-11",
      "state": "VA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MO"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
      "state": "CT"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-04-15",
      "state": "DC"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MO"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3276ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3276\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Mrs. Dingell (for herself and Mr. Cline ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo direct the Secretary of the Interior to establish the Urban Bird Treaty Program.\n#### 1. Short title\nThis Act may be cited as the Local Communities & Bird Habitat Stewardship Act of 2025 .\n#### 2. Urban Bird Treaty Program\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAccording to the 2025 State of Birds Report, bird populations continue to decline and have resulted in a 50 percent loss of tipping point bird population species in the last 50 years. The report found that policies to reverse bird declines carry benefits such as healthier working lands, cleaner water, and more resilient landscapes that can withstand fires, floods, and drought.\n**(2)**\nNearly 96 million Americans\u2014more than a third of United States adults\u2014engage in birdwatching every year, generating $279,000,000,000 in annual economic output from these birder expenditures\u2014including spending $108,000,000,000 annually on birding-related trips and equipment, directly supporting local businesses and 1.4 million American jobs.\n**(3)**\nMaintaining an abundance of healthy, well-distributed green spaces and bird habitats in and near communities reduces the risk of cross-transmission between wild birds and domestic poultry by dispersing bird populations, minimizing overlap at concentrated feeding or resting areas, and enabling earlier disease detection and response through coordinated monitoring.\n**(4)**\nEnhancing bird habitat and stewardship in populated areas serves not only to conserve bird populations and connect people to nature, but also to strengthen the ecological infrastructure necessary to mitigate the spread of wildlife-borne diseases such as Highly Pathogenic Avian Influenza.\n##### (b) Urban Bird Treaty Program\n**(1) In general**\nThe Director shall establish a program for the voluntary conservation of birds and the habitats of such birds in urban areas, to be known as the Urban Bird Treaty Program .\n**(2) Program duties**\nIn carrying out the Program, the Director shall\u2014\n**(A)**\nwork with and support covered entities to\u2014\n**(i)**\nprotect, restore, or enhance urban habitats for birds, including through the control of invasive species and restoration of native plant species;\n**(ii)**\nreduce urban hazards to birds;\n**(iii)**\nengage communities in scientific activities involving the monitoring of birds and the habitats of such birds in urban areas; and\n**(iv)**\neducate and engage communities in caring about and conserving birds and the habitats of such birds in urban areas;\n**(B)**\nprovide technical and financial assistance through partnerships with covered entities to build capacity for, plan, and carry out projects related to activities described in subparagraph (A); and\n**(C)**\nfacilitate collaboration and information sharing among covered entities and the public with respect to best management practices for the conservation, restoration, and enhancement of urban bird habitats.\n**(3) Grant program**\n**(A) In general**\nThe Director shall establish a competitive grant program to award amounts to eligible entities for the purposes of conducting research, planning, assessments, management, building capacity, monitoring, collaboration and information sharing, workforce training, and accomplishing related activities as described in paragraph (2) with respect to the conservation, restoration, enhancement or management of urban birds and the habitats of urban birds.\n**(B) Applications**\nTo be eligible for a grant under this paragraph, an eligible entity shall submit to the Director an application in such form, at such time, and containing such information as the Director determines appropriate.\n**(C) Administration**\n**(i) Agreement**\nThe Director shall enter into an agreement with the Foundation for the Foundation to administer the grant program established under subparagraph (A) pursuant to the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701 et seq. ).\n**(ii) Application of National Fish and Wildlife Foundation Establishment Act**\nSection 10(a) of the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3709(a) ) shall not apply with respect to\u2014\n**(I)**\nan agreement entered into under clause (i); or\n**(II)**\namounts made available to carry out this section.\n##### (c) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na Federal, Tribal, State, or municipal agency;\n**(B)**\na nongovernmental organization;\n**(C)**\na community group; and\n**(D)**\nan academic institution.\n**(2) Director**\nThe term Director means the Secretary of the Interior, acting through the Director of the United States Fish and Wildlife Service.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na Tribal, State, or municipal agency;\n**(B)**\na nongovernmental organization;\n**(C)**\na community group; and\n**(D)**\nan academic institution.\n**(4) Foundation**\nThe term Foundation means the National Fish and Wildlife Foundation established by section 2(a) of the National Fish and Wildlife Foundation Establishment Act ( 16 U.S.C. 3701(a) ).\n**(5) Program**\nThe term Program means the Urban Bird Treaty Program established under subsection (b)(1).\n**(6) Urban**\nThe term urban has the meaning given the term urban area in section 101(a) of title 23, United States Code.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Director to carry out this section $1,000,000 for each of fiscal years 2026 through 2032.",
      "versionDate": "2025-05-08",
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
            "name": "Birds",
            "updateDate": "2026-03-09T19:19:53Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2026-03-09T19:21:41Z"
          },
          {
            "name": "Environmental assessment, monitoring, research",
            "updateDate": "2026-03-09T19:21:59Z"
          },
          {
            "name": "Urban and suburban affairs and development",
            "updateDate": "2026-03-09T19:22:16Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-03-09T19:22:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Environmental Protection",
        "updateDate": "2025-05-22T17:38:45Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3276ih.xml"
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
      "title": "Local Communities & Bird Habitat Stewardship Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Communities & Bird Habitat Stewardship Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of the Interior to establish the Urban Bird Treaty Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:32Z"
    }
  ]
}
```
