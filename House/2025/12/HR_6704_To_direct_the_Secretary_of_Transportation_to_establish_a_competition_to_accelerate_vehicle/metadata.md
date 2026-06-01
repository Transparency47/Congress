# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6704
- Title: Drunk Driving Prevention and Enforcement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6704
- Origin chamber: House
- Introduced date: 2025-12-15
- Update date: 2026-02-03T09:05:39Z
- Update date including text: 2026-02-03T09:05:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-15: Introduced in House

## Actions

- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Introduced in House
- 2025-12-15 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6704",
    "number": "6704",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000602",
        "district": "4",
        "firstName": "Laura",
        "fullName": "Rep. Gillen, Laura [D-NY-4]",
        "lastName": "Gillen",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Drunk Driving Prevention and Enforcement Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:39Z",
    "updateDateIncludingText": "2026-02-03T09:05:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
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
      "actionDate": "2025-12-15",
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
      "actionDate": "2025-12-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T17:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:40:57Z",
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
      "sponsorshipDate": "2025-12-15",
      "state": "NY"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6704\nIN THE HOUSE OF REPRESENTATIVES\nDecember 15, 2025 Ms. Gillen (for herself, Mr. Lawler , and Mrs. Dingell ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to establish a competition to accelerate vehicle integration of passive, anti-drunk driving technology, with a cash prize awarded to an entity that demonstrates technology that is ready for integration into passenger motor vehicles, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Drunk Driving Prevention and Enforcement Act of 2025 .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress finds the following:\n**(1)**\nAlcohol-impaired driving is a leading cause of death and injury on our nation's roadways, with more than 12,000 people killed every year and hundreds of thousands seriously injured in drunk driving crashes annually. These deaths and injuries are 100 percent preventable.\n**(2)**\nCongress has directed the integration of passive, advanced anti-drunk driving in-vehicle technology into all new passenger motor vehicles under Section 24220 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ).\n**(3)**\nAccelerated deployment are needed to bring forward passive, consumer-ready vehicle-integrated technologies designed to prevent drunk driving.\n**(4)**\nPublic-private innovation prize competitions have proven effective in spurring rapid advancements and breakthroughs in science, engineering, safety and technology.\n##### (b) Purpose\nThe purpose of this Act is to establish a competitive prize award program to incentivize deployment of effective, passive, anti-drunk driving technology that is consumer-ready for integration into passenger motor vehicles.\n#### 3. Establishment of prize competition\n##### (a) Authority\nThe Secretary of Transportation, acting through the Administrator of the National Highway Traffic Safety Administration shall carry out a program on a competitive basis to award a cash prize that the Secretary determines is appropriate to recognize outstanding achievement in the development of passive, advanced anti-drunk driving technology to\u2014\n**(1)**\nimplement the adoption of breath-based, touch-based, or other sensor technology to prevent drivers with a blood alcohol concentration at or above the legal limit from operating a vehicle; or\n**(2)**\ninstall consumer-ready, passive, advanced anti-drunk driving technologies in vehicles to eliminate drunk driving.\n##### (b) Competition requirements\nThe program established under subsection (a) shall\u2014\n**(1)**\nuse a competitive process for the selection of a recipient of a cash prize;\n**(2)**\ninclude the widely advertised solicitation of submissions;\n**(3)**\nmake available a prize purse of not less than $45,000,000 to be awarded to the winner of the competition who is able to demonstrate consumer-ready, passive, advanced anti-drunk driving technology for vehicle integration; and\n**(4)**\nbe open to individuals, private sector entities, nonprofit organizations, academic institutions, and consortia thereof.\n##### (c) Relationship to other authority\nThe program established under subsection (a) may be carried out in conjunction with, or in addition to, the exercise of any other authority of the Department of Transportation.\n##### (d) Authorization of appropriations\nFor the purposes of carrying out this Act, including the prize purse, administration, evaluation, and outreach, there is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $50,000,000 to remain available until expended, except that such amount may not be expended after the last day of fiscal year 2028.\n##### (e) Congressional notice\n**(1) In general**\nNot later than 15 days after a cash prize has been awarded under this section, the Secretary shall submit to the Committee on Appropriations and the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Appropriations and the Committee of Commerce, Science, and Transportation of the Senate written notice of such award.\n**(2) Contents**\nEach notice submitted under paragraph (1) shall include\u2014\n**(A)**\na description of the technology development for which the cash prize was awarded;\n**(B)**\nthe outcomes and benefits that the competition winner anticipates generating; and\n**(C)**\nrecommendations for further accelerating deployment of anti-drunk driving technology.\n##### (f) Reporting requirement\nNot later than 3 years after the date of enactment of this Act, the Secretary shall submit to the Committee on Appropriations and the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Appropriations and the Committee of Commerce, Science, and Transportation of the Senate a report that contains\u2014\n**(1)**\ndetails on the results of the program; and\n**(2)**\nadditional steps the Department can take to ensure vehicle integration continues at a rapid pace, including through implementation of section 24220 of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ).\n#### 4. NHTSA Traffic Safety Enforcement Center of Excellence\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Transportation shall establish a Traffic Safety Enforcement Center of Excellence within the Department of Transportation, to provide leadership and technical assistance to States and law enforcement agencies to maximize efficient and effective ways to conduct traffic safety enforcement of hazardous driving behaviors with the goal to reduce fatalities and injuries on the roads of the United States.\n##### (b) Duties\nThe Traffic Safety Enforcement Center of Excellence established under subsection (a) shall\u2014\n**(1)**\nserve as a central location within the Department of Transportation for expertise in traffic safety enforcement;\n**(2)**\nprovide State highway safety offices and law enforcement agencies across the country with centralized expertise, tools, and support;\n**(3)**\npromote evidence-based strategies on what works in hazardous driving behavior enforcement, including targeted, cost-effective drunk-driving patrols, speed enforcement best practices, and coordinated traffic safety campaigns proven to reduce roadway fatalities and injuries;\n**(4)**\nestablish best-practice protocols for enforcement operations, with the goal of improving outcomes based on data and research;\n**(5)**\ndevelop and deliver standardized training on the use of data for hot spot detection, drug-impaired driving enforcement strategies, speed management, and other risk mitigation of death and injury on public roads;\n**(6)**\nassist States and agencies in using real-time data systems to identify high-crash corridors and target enforcement resources in the most efficient ways;\n**(7)**\nhelp agencies assess current enforcement practices and identify gaps;\n**(8)**\nprovide recommendations for hazardous driving behavior enforcement plans based on crash data and local context;\n**(9)**\nassist agencies in using limited resources more efficiently through data-driven deployment and risk-based enforcement;\n**(10)**\nhelp States fully leverage programs under sections 402 and 405 of title 23, United States Code, by providing technical assistance on program development and design and outcome measurement tools;\n**(11)**\nlaunch model demonstration projects in States or cities to test new roadside technologies, data-driven deployment models, new enforcement strategies (such as those targeting drug-impaired driving), and share results nationally to help with the adoption of effective tools;\n**(12)**\nserve as a national convener for State highway safety offices, law enforcement agencies, traffic safety researchers, victims and survivors, and public health and traffic safety leaders;\n**(13)**\ncollaborate with, and provide support on, traffic safety enforcement to all operating administrations of the Department of Transportation; and\n**(14)**\nhave a workforce composed of Department of Transportation employees, including direct hires or detailees from operating administrations of the Department of Transportation, Department of Justice, and other Federal agencies.\n##### (c) Rule of construction\nThe Traffic Safety Enforcement Center of Excellence shall not supersede laws or regulations granting certification authorities to Operating Administrations of the Department of Transportation.\n##### (d) Report on staffing needs\nNot later than 90 days after the date of enactment of this Act, the Secretary shall report to the Committee on Appropriations and the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Appropriations and the Committee of Commerce, Science, and Transportation of the Senate on staffing needs and the staffing plan for the Traffic Safety Enforcement Center of Excellence.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $5,000,000 for fiscal year 2026 and each fiscal year thereafter to carry out this section.\n#### 5. National drug involved crash data collection system\n##### (a) Purpose\nThe purpose of this section is to track and analyze the role of drugs in serious injury and fatal traffic crashes, supporting enforcement, prevention, and research.\n##### (b) Definitions\nIn this section:\n**(1) Drug involved crash**\nThe term drug involved crash means a crash causing serious injury or death in which 1 or more drivers test positive for impairing substances other than alcohol.\n**(2) Impairing substance**\nThe term impairing substance means prescription, over-the-counter, controlled, or illicit psychoactive drugs affecting driving.\n**(3) State**\nThe term State means the 50 States, the District of Columbia, Puerto Rico, Guam, the U.S. Virgin Islands, American Samoa, and the Northern Mariana Islands.\n##### (c) Establishment\nThe Administrator of the National Highway Traffic Safety Administration shall establish a national drug involved crash data collection system to\u2014\n**(1)**\ncollect standardized toxicology data from States for fatal and serious injury crashes;\n**(2)**\nlink crash data with medical, coroner, hospital, and emergency medical services records;\n**(3)**\nprovide model protocols for specimen collection, testing, and reporting;\n**(4)**\noperate sentinel sites in multiple States to pilot enhanced data collection; and\n**(5)**\nreport annually to Congress and the public on trends, substance types, and geographic patterns.\n##### (d) State grants\n**(1) In general**\nThe Administrator may award grants to States for toxicology labs, specimen collection, training, data systems, and data linkage.\n**(2) Prioritization**\nIn awarding grants under paragraph (1), the Administrator shall prioritize States that contain high-fatality, rural, or underserved areas.\n**(3) Non-Federal funds**\nThe Administrator may require a non-Federal match from a State to be eligible for a grant under this subsection unless the State demonstrates hardship.\n##### (e) Implementation timeline\n**(1) Model protocols**\nNot later than 1 year after the date of enactment of this Act, the Administrator shall publish the model protocols required under subsection (c)(3).\n**(2) Sentinel sites**\nThe Administrator shall ensure that the sentinel sites required under subsection (c)(3) are operational not later than 2 years after the date of enactment of this Act.\n**(3) Submission of data**\nThe Administrator shall ensure that the system established under this section has begun collecting standardized toxicology data from States for fatal and serious injury crashes beginning not later than 3 years after the date of enactment of this Act.\n##### (f) Privacy protections\nAny data made available to the public pursuant to this section shall be deidentified before and used in compliance with Federal and State privacy laws, including the Health Insurance Portability and Accountability Act of 1996 ( Public Law 104\u2013191 ), as applicable.\n##### (g) Authorization\nThere is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $30,000,000 for each of fiscal years 2026 through 2031 to carry out this section.",
      "versionDate": "2025-12-15",
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
        "updateDate": "2026-01-08T19:31:59Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6704ih.xml"
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
      "title": "Drunk Driving Prevention and Enforcement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:24:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Drunk Driving Prevention and Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:24:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to establish a competition to accelerate vehicle integration of passive, anti-drunk driving technology, with a cash prize awarded to an entity that demonstrates technology that is ready for integration into passenger motor vehicles, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:18:33Z"
    }
  ]
}
```
