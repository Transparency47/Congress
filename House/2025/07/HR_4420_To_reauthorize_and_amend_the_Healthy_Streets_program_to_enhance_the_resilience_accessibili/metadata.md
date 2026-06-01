# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4420?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4420
- Title: Cool Corridors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4420
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-10-25T08:05:48Z
- Update date including text: 2025-10-25T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-07-16 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4420",
    "number": "4420",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001159",
        "district": "10",
        "firstName": "Marilyn",
        "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
        "lastName": "Strickland",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Cool Corridors Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-25T08:05:48Z",
    "updateDateIncludingText": "2025-10-25T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-07-16T19:35:42Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
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
      "sponsorshipDate": "2025-07-15",
      "state": "DC"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NC"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NV"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MO"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TN"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "AZ"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "AZ"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "PA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "OR"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "PA"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "WA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "TX"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "LA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "IN"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-09",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sponsorshipDate": "2025-10-24",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4420ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4420\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Ms. Strickland (for herself, Mr. Lawler , Ms. Norton , Ms. Adams , Mr. Thanedar , Ms. Titus , Ms. Matsui , Mr. Cleaver , Mr. Cohen , Mr. Stanton , Ms. Ansari , Ms. Garcia of Texas , Ms. Scanlon , Mr. Ruiz , Mr. Kennedy of New York , and Mr. Harder of California ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo reauthorize and amend the Healthy Streets program to enhance the resilience, accessibility, and safety of the Nation\u2019s transportation corridors by supporting strategic investments in tree canopy, shade infrastructure, and other nature-based cooling strategies along pedestrian, bicycle, and transit routes.\n#### 1. Short title\nThis Act may be cited as the Cool Corridors Act of 2025 .\n#### 2. Findings; purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nExtreme heat is a growing public health and infrastructure challenge.\n**(2)**\nTree canopy and green infrastructure reduce surface and air temperatures, improve safety and usability along transportation corridors, and protect infrastructure from heat-related degradation.\n**(3)**\nCommunities with limited infrastructure investment often lack sufficient tree cover and face increased exposure to extreme heat and limited transportation access.\n**(4)**\nFederal programs such as the Healthy Streets program and the Urban and Community Forestry Program have demonstrated both high demand and the effectiveness of locally driven, community-scale interventions.\n**(5)**\nLocally driven efforts to plant and maintain trees along key walking, biking, and transit corridors are under-resourced, despite proven benefits to heat mitigation, public safety, and community health.\n##### (b) Purpose\nThe purpose of this Act is to\u2014\n**(1)**\npromote the deployment of cooling infrastructure along transportation corridors;\n**(2)**\nenhance resilience and safety of transportation systems in the face of extreme heat and improve air quality;\n**(3)**\nimprove safety, accessibility, and usability for pedestrians, cyclists, and transit users;\n**(4)**\nextend the useful life of infrastructure; and\n**(5)**\nprioritize investment in communities facing disproportionate heat and access challenges.\n#### 3. Reauthorization of Healthy Streets program\nSection 11101(b)(2)(C) of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note(b)(2)(C)) is amended by striking through 2026 and inserting through 2030 .\n#### 4. Healthy Streets program\n##### (a) In general\nSection 11406 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (D) by striking and at the end;\n**(ii)**\nin subparagraph (E) by striking the period and inserting a semicolon; and\n**(iii)**\nby adding at the end the following:\n(F) State and local transit agencies; (G) State departments of transportation; (H) local educational agencies; and (I) tree and greenspace stewardship organizations, environmental asset management groups, or infrastructure resilience partners with experience in protecting and sustaining green infrastructure and shade assets. ; and\n**(B)**\nby adding at the end the following:\n(8) Cool corridor The term cool corridor means\u2014 (A) a designated transportation route enhanced through linear greening strategies, including tree canopy, shade infrastructure, and other nature-based solutions designed to reduce surface and ambient temperatures; and (B) incorporates planning and stewardship measures to ensure the long-term functionality, protection, and climate resilience of the activities described in subparagraph (A). (9) Heat mitigation strategies The term heat mitigation strategies means activities that result in the mitigation of heat in public spaces, including tree planting, vegetative infrastructure, cool or reflective surfaces, shade structures, and other evidence-based practices, including the maintenance and preservation of already existing green infrastructure, roadside vegetations and trees. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby inserting for demonstration projects in geographically and climatically diverse regions, including both urban and rural communities with historically low tree canopy or high heat vulnerability before to eligible entities ;\n**(B)**\nin paragraph (1) by striking and at the end;\n**(C)**\nin paragraph (2) by striking the period and inserting , including the integration of shade structures, bus stop shelters, and climate-resilient streetscape elements, which may include the strategic planting of trees for shade; ; and\n**(D)**\nby adding at the end the following:\n(3) to plan, design, construction, and maintain tree canopy and green infrastructure along public transportation corridors, including alongside transportation right of ways, at bus stops, near transit hubs, and within designated public-school zones and properties; (4) to deploy smart sensors and data tools to monitor heat exposure and performance; (5) for community engagement, planning, and workforce development activities relating to heat mitigation, tree planting and maintenance; and (6) to integrate cooling infrastructure into existing or planned multimodal corridors or new and existing transportation projects; particularly school zones, and neighborhood-scale corridors where pedestrian mobility is high to create cool corridors ;\n**(3)**\nin subsection (d)(2)\u2014\n**(A)**\nin subparagraph (A) by striking and at the end;\n**(B)**\nin subparagraph (B) by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(C) plans to undergo review and seek approval from the State or local agency of jurisdiction prior to project implementation to ensure projects do not interfere or hinder any ongoing or future developments. ;\n**(4)**\nin subsection (f)\u2014\n**(A)**\nin paragraph (1) by inserting that is impacted by high heat or low tree canopy coverage after disadvantaged community ;\n**(B)**\nin paragraph (2) by striking or at the end;\n**(C)**\nin paragraph (3) by striking the period at the end and inserting a semicolon; and\n**(D)**\nby adding at the end the following:\n(4) that improves access to transit, schools, jobs, or essential services; (5) that incorporates maintenance and long-term sustainability plans; (6) that leverages additional funding through public private or interagency coordination; (7) that aims to preserve and maintain existing green infrastructure and vegetation alongside transportation corridors and transit routes; (8) that incorporates the use of vegetation or tree species that require minimal maintenance; or (9) that integrates workforce training and urban forestry job creation strategies. ; and\n**(5)**\nby adding at the end the following:\n(i) Interagency coordination In carrying out the program under this section, the Secretary shall coordinate with the following, as appropriate: (1) The Administrator of the Environmental Protection Agency. (2) The Secretary of Energy. (3) The Secretary of Housing and Urban Development. (4) The Secretary of Agriculture, particularly the Chief of the Forest Service. (5) The Director of the United States Climate Resilience Toolkit and United States Global Change Research Program. (j) Technical assistance and guidance The Secretary, in coordination with relevant Federal agencies, shall provide\u2014 (1) technical assistance, model project templates, and guidance to grantees to promote cost-effective and evidence-based project delivery under this section; and (2) guidance on tree species selection, short and long term stewardship plans, and integration with local forestry plans. (k) Specifications for tree planting If the recipient of a grant under this section uses grant funding for tree planting\u2014 (1) such planting shall be done in a manner that does not obstruct traffic views or hinder public safety, as determined by the Secretary; and (2) the recipient shall be responsible for tree maintenance, including watering and upkeep, as needed. (l) Reporting A recipient of a grant under this section shall submit to the Secretary an annual report on\u2014 (1) temperature reduction and environmental performance metrics; (2) infrastructure resilience improvements; (3) public health and equity outcomes; (4) cost-benefit analyses; and (5) community engagement practices. .\n##### (b) Report\nNot later than 5 years after the date of enactment of this Act, the Secretary of Transportation shall submit to Congress a report evaluating the outcomes of the program under section 11406 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note) and making recommendations for permanent authorization and integration of the program into the surface transportation block grant program under section 133 of title 23, United States Code.",
      "versionDate": "2025-07-15",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-31T12:09:17Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4420ih.xml"
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
      "title": "Cool Corridors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:51:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cool Corridors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-23T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and amend the Healthy Streets program to enhance the resilience, accessibility, and safety of the Nation's transportation corridors by supporting strategic investments in tree canopy, shade infrastructure, and other nature-based cooling strategies along pedestrian, bicycle, and transit routes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-23T02:03:29Z"
    }
  ]
}
```
