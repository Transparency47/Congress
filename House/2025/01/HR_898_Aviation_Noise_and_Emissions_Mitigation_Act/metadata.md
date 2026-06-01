# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/898?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/898
- Title: Aviation Noise and Emissions Mitigation Act
- Congress: 119
- Bill type: HR
- Bill number: 898
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-04-29T08:05:58Z
- Update date including text: 2025-04-29T08:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-01 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-01 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/898",
    "number": "898",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S000510",
        "district": "9",
        "firstName": "Adam",
        "fullName": "Rep. Smith, Adam [D-WA-9]",
        "lastName": "Smith",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Aviation Noise and Emissions Mitigation Act",
    "type": "HR",
    "updateDate": "2025-04-29T08:05:58Z",
    "updateDateIncludingText": "2025-04-29T08:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-01",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:07:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-01T15:45:56Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-31T15:07:15Z",
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
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "OR"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "WA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "IL"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "NY"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "MD"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr898ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 898\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Smith of Washington (for himself, Mr. Moulton , Ms. Bonamici , Mr. Panetta , Ms. Norton , Mr. Quigley , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo develop pilot grant programs through the Environmental Protection Agency to research and collect data on aircraft and airport noise and emissions and to use such information and data to develop a mitigation strategy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Aviation Noise and Emissions Mitigation Act .\n#### 2. Noise and air quality monitoring and research grant program\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Administrator of the Environmental Protection Agency in consultation with Secretary of Transportation and other relevant Federal agencies determined by the Administrator, shall establish a 3-year pilot grant program with eligible entities to measure noise and emissions, including greenhouse gases, particulate matter, ultrafine particles, and air toxics, in communities near airports or air flight pathways using sophisticated methods and technology that allow tracing of noise and emissions to specific sources such as aircraft and airport related noise and emissions near such communities, including identifying specific neighborhoods, structures, or areas impacted by such noise and emissions.\n##### (b) Grant activities\nRecipients of grants under subsection (a) shall\u2014\n**(1)**\nuse technology capable of producing data that can be used for wedge analysis to decipher the sources of noise and emissions so communities may better understand the primary contributors of noise and emissions;\n**(2)**\nmake every reasonable effort to establish a program that can be easily replicated across the country with the goal of ongoing data collection and monitoring in areas near airports or air flight pathways;\n**(3)**\nproduce neighborhood and ZIP Code-level data for a designated area to be used to determine or predict the level and impact of noise and emissions on certain neighborhoods and ZIP Codes of such area, and to identify frontline and disproportionately impacted communities;\n**(4)**\ncoordinate and regularly communicate with the local clean air agency (or agencies, if applicable), local public health departments, local metropolitan planning organizations, Indian Tribal governments, community based organizations, and other local government, State government, or non-profit entities as the grantee determines useful to the project;\n**(5)**\nwork with community-based organizations, some of which may be selected for a grant under section 2, to assist in developing a mitigation abatement strategy for communities, neighborhoods, or areas impacted by aircraft or airport noise and emissions;\n**(6)**\nestablish a clear plan for disseminating the data and results of the program on an regular basis; and\n**(7)**\nconsult initially and throughout the process with the public and relevant community-based organizations or local governments on the design and execution of the noise and emissions monitoring program.\n##### (c) Eligible entities\nAn institution of higher education or other non-profit research entity, health institution, or local government with demonstrated experience in conducting either or both aviation noise or emissions research is eligible to receive a grant under this section. The Administrator may award not more than 6 awards under this section.\n##### (d) Grant award amount\nThe Administrator may award a grant under this section to an eligible entity of not less than $2,500,000 and not more than $5,000,000 for the 3-year grant period.\n##### (e) Annual report\nA grantee under the section shall submit an annual report to the Administrator regarding the research conducted and any findings. The Administrator shall make such reports publicly available.\n#### 3. Mitigation and support services grant program\n##### (a) In general\nNot later than 6 months after the submission of the final annual report submitted under section 1(e), the Administrator of the Environmental Protection Agency, in consultation with the Department of Health and Human Services, Department of Transportation, or other relevant Federal agencies as determined by the Administrator, shall establish a pilot grant program to mitigate aircraft or airport noise and emissions, and their impacts, in communities near airports and air flight pathways.\n##### (b) Grant requirements\n**(1) Priority**\nThe Administrator shall prioritize and provide guidance and technical assistance to applicants applications that\u2014\n**(A)**\nfocus on communities found to be disproportionately impacted by aviation noise or emissions identified in the research produced under the section 1 grant;\n**(B)**\nprimarily benefit disadvantaged communities and communities with a higher prevalence of diseases associated with environmental exposures; and\n**(C)**\ndemonstrate community support and involvement from affected communities in their proposed program.\n**(2) Eligibility**\nTo be eligible to receive a grant under this section, an applicant shall be a local community-based non-profit organization, a consortium of community-based non-profit organizations from a community that participated in the noise and emissions monitoring program under section 1, a local public health department, or a local or Indian Tribal government. If the recipient is a public health department or local or Indian Tribal government, the recipient shall demonstrate community support for the program and how it plans to partner with at least 1 non-profit community-based organization.\n**(3) Mitigation strategy**\nAn applicant shall demonstrate in its application how the\u2014\n**(A)**\nresearch conducted under section 1 informs its proposed project design;\n**(B)**\nproposed project addresses environmental or health disparities and the needs and concerns of affected communities, disadvantaged communities, or other communities facing environmental justice concerns, including how the applicant used the Climate and Economic Justice Screening Tool or other similar environmental justice mapping tool to effectively target mitigation strategies;\n**(C)**\napplicant incorporated input from affected communities in its proposed program, demonstrated community support for the proposed program, and has established a written plan detailing how the applicant will maintain ongoing engagement with the affected communities; and\n**(D)**\napplicant intends to partner or coordinate with relevant local organizations, government entities, and service providers such as local public health departments, Indian Tribal governments, community health centers, and local education authorities, depending on the mitigation plan.\n**(4) Use of funds**\nFunds under the grant program shall be used to mitigate the impacts of aircraft or airport noise and emissions on communities near airports or air flight pathways, including establishing 1 or more of the following:\n**(A)**\nNoise mitigation packages that may include weatherization, retrofitting, or energy efficiency upgrades that have noise reduction, environmental, or health benefits for households, schools, or other facilities, prioritizing low-income households and low-resourced communities and facilities, and structures that are less likely to be eligible for other similar Federal resources.\n**(B)**\nPrograms to promote environmental and public health services in impacted communities, including programs that address the disproportionate effects of climate change on environmental justice communities.\n**(C)**\nHealth care services and environmental and public health interventions that address underlying impacts from airport noise and pollution on health and quality of life, especially in children, vulnerable populations, disadvantaged communities, and communities of color.\n**(5) Duration**\nA grant under this section shall be not less than 3 years and not more than 5 years as determined appropriate by the Administrator.\n##### (c) Reporting requirements\n**(1) After 1st year**\nOne year after the awarding of grants under this section, and annually thereafter, the Administrator shall submit a report to the Committees on Energy and Commerce and Transportation and Infrastructure of the House of Representatives and the Committees on Environment and Public Works and Commerce, Science, and Transportation of the Senate on the activities of the grant programs to include\u2014\n**(A)**\nthe services provided and their targeted beneficiaries (including households, schools, other facilities, children, adults, seniors);\n**(B)**\nthe steps taken by the grantee to engage the public and impacted communities during execution of the grant;\n**(C)**\na breakdown of the areas served under the grant and if and how such areas align with locations identified under section 1; and\n**(D)**\naggregate information about the communities, households, and individuals benefitting from the services provided under the grant, including a breakdown of the demographic information and socioeconomic status of individuals and households.\n**(2) After 3d year**\nThree years after awarding of the first grant under this section, the agency shall submit a report to the congressional committees referred to in paragraph (1) to include\u2014\n**(A)**\nan assessment of the grant program\u2019s ability to meet its goal of mitigating airport and aviation noise and emissions;\n**(B)**\npotential lessons learned to inform future efforts to address the impacts of noise and emissions in communities near airports and air flight pathways; and\n**(C)**\na review of how levels and impact of noise and pollution from airports and air flight pathways can be incorporated into the Climate and Economic Justice Screening Tool or other similar environmental justice mapping tool used by the Government.\n**(3) Input in report**\nThe report under this subsection shall be completed with input from grantees and affected communities.",
      "versionDate": "2025-01-31",
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
        "name": "Environmental Protection",
        "updateDate": "2025-03-04T16:50:49Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr898ih.xml"
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
      "title": "Aviation Noise and Emissions Mitigation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-01T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Aviation Noise and Emissions Mitigation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-01T04:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To develop pilot grant programs through the Environmental Protection Agency to research and collect data on aircraft and airport noise and emissions and to use such information and data to develop a mitigation strategy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:33:16Z"
    }
  ]
}
```
