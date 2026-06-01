# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1892?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1892
- Title: Wireless Electric Vehicle Charging Grant Program Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1892
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-02-25T09:06:37Z
- Update date including text: 2026-02-25T09:06:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-05 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1892",
    "number": "1892",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "S001215",
        "district": "11",
        "firstName": "Haley",
        "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
        "lastName": "Stevens",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Wireless Electric Vehicle Charging Grant Program Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:37Z",
    "updateDateIncludingText": "2026-02-25T09:06:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-05T23:04:47Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-03-05T15:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
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
      "sponsorshipDate": "2025-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1892ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1892\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Ms. Stevens (for herself, Ms. Barrag\u00e1n , Mrs. Dingell , and Ms. Titus ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Transportation to establish a Wireless Electric Vehicle Charging Grant Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wireless Electric Vehicle Charging Grant Program Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nElectric vehicles are crucial to cutting greenhouse gas emissions, reducing reliance on fossil fuels, strengthening United States economic and national security, and combating the climate crisis. As of 2019, the transportation sector accounts for 29 percent of all greenhouse gas emissions, which is the most of any sector.\n**(2)**\nIncreasing the adoption of electric vehicles will reduce pollution and increase air quality for communities located near roads with high traffic density or high-volume routes.\n**(3)**\nAs the automotive industry shifts towards electric vehicles, investing in new electric vehicle technologies will be crucial to enhancing America\u2019s competitiveness, creating jobs, and ensuring continued economic growth.\n**(4)**\nRange anxiety is one of the chief barriers to electric vehicle adoption. If deployed strategically, wireless electric vehicle charging could help by providing drivers convenient opportunities to charge and extend the range of electric vehicles.\n**(5)**\nWireless charging technologies could be invaluable for electric transit buses, trucking, fleet vehicles, and autonomous electric vehicles, allowing for convenient and hands-free charging, while also lowering costs, as effective wireless charging would reduce the need for larger and heavier batteries.\n**(6)**\nWireless and dynamic charging can also reduce pressure on the grid, allowing vehicles to charge through space and time, shaving peak demand and reducing the need to build massive charging capacity at any given location to meet growing electric vehicle charging demand.\n**(7)**\nWireless can enhance electrification of fleets, including medium and heavy-duty vehicles, helping them meet operational needs that cannot be met solely by traditional charging systems.\n**(8)**\nWireless electric vehicle charging has the potential to make electric vehicles more accessible and allow all people of the United States, regardless of physical ability, to enjoy the benefits of electric vehicles.\n**(9)**\nIt is critical to establish a resilient and robust domestic supply chain for all electric vehicle charging infrastructure. With strong Buy America requirements, federally funded programs can incentivize companies to build facilities in the United States, creating good paying jobs and economic growth for communities.\n#### 3. Establishment of Wireless Electric Vehicle Charging Grant Program\nThe Secretary of Transportation shall establish a program, in coordination with the Department of Energy, to award grants on a competitive basis to eligible entities for projects to construct, install, or improve existing wireless charging infrastructure and technology for electric vehicles, including performance, safety, electromagnetic compatibility, interoperability, development, and testing of wireless charging. The program shall be known as the Wireless Electric Vehicle Charging Grant Program (in this Act referred to as the Program ).\n#### 4. Duties of Secretary\nIn carrying out the Program, the Secretary\u2014\n**(1)**\nmay award grants for projects described in section 3, including for wireless charging located along roads, in parking lots, airports, and at coastal and inland ports;\n**(2)**\nshall ensure that recipients of the grants focus on the wireless charging of 1 or more of\u2014\n**(A)**\nlight-, medium-, and heavy-duty vehicles;\n**(B)**\nfleet vehicles, including the Federal vehicle fleets; and\n**(C)**\npublic transit;\n**(3)**\nshall publish an annual progress report to the relevant committees of the House of Representatives and the Senate that includes\u2014\n**(A)**\na description of recipients of grants, amount disbursed, and reasons for the selection of projects;\n**(B)**\nthe progress of each pilot project funded under the Program;\n**(C)**\nsuccesses, failures, and safety of the technologies funded under the Program;\n**(D)**\nrecommendations for future funding, best practices, and policies relating to wireless electric vehicle charging;\n**(E)**\nworkforce impacts of each project;\n**(F)**\nthe environmental impact of each project, such as the amount of fuel saved from the project, predicted emissions savings, changes in air quality, and any other environmental information deemed necessary by the Secretary; and\n**(G)**\nany other information the Secretary considers necessary; and\n**(4)**\nmay provide technical assistance, as determined appropriate by the Secretary to eligible entities with respect to activities described in paragraph (1).\n#### 5. Grant recipients\n##### (a) Eligible entities\nTo be eligible for a grant or technical assistance under the Program, an entity shall be, or be partnered with, any of the following:\n**(1)**\nA State, local, Tribal, or territorial government.\n**(2)**\nA Metropolitan Planning Organization.\n**(3)**\nA special purpose district or public authority with a transportation function.\n**(4)**\nA transit agency.\n##### (b) Geographic diversity\nIn selecting eligible entities to receive grants under the Program, the Secretary shall prioritize geographical diversity.\n##### (c) Additional grant amounts\nAn eligible entity may receive a grant from a State, local, Tribal, or territorial government to carry out similar activities as the activities funded under the Program.\n##### (d) Workforce development and training\nEligible entities may use a portion of their grant to cover costs associated with training workers to construct, install, maintain, or operate the projects.\n##### (e) Community engagement\nEligible entities may use a portion of their grant to cover costs associated with engaging the communities and affected workers, such as drivers, on the planning and design of the project and educating the public on the project.\n#### 6. Cost share\n##### (a) Federal share\nThe Federal share of a grant awarded under the Program may not exceed 80 percent of total cost of the project.\n##### (b) Maximum grant amount\nThe amount of a grant awarded to an eligible entity under the Program may not exceed $25,000,000.\n#### 7. Program requirements\n##### (a) Priority\nIn awarding the grants under the Program, the Secretary shall prioritize projects that\u2014\n**(1)**\nfocus on non-disruptive designs that are compatible with existing infrastructure and beneficial to the public, including for low income, underserved, or disadvantaged communities;\n**(2)**\nfocus on cost-effective, energy-efficient, and environmentally sustainable technologies for public use;\n**(3)**\nfocus on compatibility with the entire range of electric vehicles and with, if determined appropriate by the Secretary, developing and evolving universal wireless charging standards;\n**(4)**\nfocus on safe designs that are compatible with frequent use in a variety of weather conditions and road maintenance activities;\n**(5)**\nare carried out by entities that emphasize diversity, equity, and inclusion in the eligible entity\u2019s workforce and business practices;\n**(6)**\nare likely to leverage Federal investment by encouraging non-Federal contributions to the project, including projects from public-private partnerships;\n**(7)**\nhave State, local, Tribal, or territorial government support;\n**(8)**\nhave an outreach strategy to inform and educate the public on project benefits and uses before, during, and after the construction of the projects;\n**(9)**\nhave an inclusive plan to engage and ensure that the surrounding communities and impacted workers, such as the drivers of the vehicles, are included in the planning and design process;\n**(10)**\nfocus on interoperability development and testing;\n**(11)**\nfocus on fleets, including medium and heavy-duty vehicles, which through transitioning to electric can have a significant impact on reducing fuel consumption and CO2 emissions; and\n**(12)**\nhelp improve the life of the vehicle\u2019s battery.\n##### (b) Wage rate requirement\nThe Secretary shall require that each recipient of a grant under the Program provides reasonable assurances that all laborers and mechanics employed to carry out the projects for which the assistance is provided, including laborers and mechanics employed by contractors or subcontractors, will be paid wages at rates not less than those for similar work in the locality as determined by the Secretary of Labor in accordance with subchapter IV of chapter 31 of title 40, United States Code (commonly referred to as the Davis-Bacon Act ).\n##### (c) Neutrality toward organized labor\nThe recipient of grants under the Program shall have, and ensure that all employed by contractors and subcontractors of the covered entity with respect to the covered activities have\u2014\n**(1)**\nan explicit policy of neutrality with regard to\u2014\n**(A)**\nlabor organizing for the employees engaged in the covered activities; and\n**(B)**\nsuch employees\u2019 choice to form and join labor organizations; and\n**(2)**\npolicies that require\u2014\n**(A)**\nthe posting and maintenance of notices in the workplace to such employees of their rights under the National Labor Relations Act ( 29 U.S.C. 151 et seq. ); and\n**(B)**\nthat such employees are, at the beginning of their employment, provided notice and information regarding the employees\u2019 rights under such Act.\n##### (d) Buy America\n**(1) In general**\nExcept as provided in paragraph (2), recipients of grants under the Program shall comply with the requirements described in section 5323(j) of title 49, United States Code.\n**(2) Waiver**\nThe Secretary may provide any waiver to the requirements described in paragraph (1) in the same manner and to the same extent as the Secretary of Transportation may provide a waiver under section 5323(j)(2) of title 49, United States Code.\n#### 8. Definitions\nIn this Act:\n**(1) Electric vehicle**\nThe term electric vehicle means a zero-emission vehicle powered by an electric battery and train.\n**(2) State**\nThe term State has the meaning given the term in section 101 of title 23, United States Code.\n**(3) Wireless charging**\nThe term wireless charging means the charging of a battery by inductive charging or by any means in which a battery is charged without a wire, or plug-in wire, connecting the power source and battery.\n#### 9. Authorization of appropriations\nThere is authorized to be appropriated $250,000,000 to carry out this Act, to remain available until expended.",
      "versionDate": "2025-03-05",
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
        "name": "Energy",
        "updateDate": "2025-03-21T13:46:22Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1892ih.xml"
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
      "title": "Wireless Electric Vehicle Charging Grant Program Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wireless Electric Vehicle Charging Grant Program Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a Wireless Electric Vehicle Charging Grant Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:17Z"
    }
  ]
}
```
