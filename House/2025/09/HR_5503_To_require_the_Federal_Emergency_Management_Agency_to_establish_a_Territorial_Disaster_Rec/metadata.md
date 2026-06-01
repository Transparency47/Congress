# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5503?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5503
- Title: Strengthening Capacity for Disaster Resilient Territories Act
- Congress: 119
- Bill type: HR
- Bill number: 5503
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-05T21:43:35Z
- Update date including text: 2025-12-05T21:43:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-19 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-09-19 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5503",
    "number": "5503",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "V000081",
        "district": "7",
        "firstName": "Nydia",
        "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
        "lastName": "Vel\u00e1zquez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Strengthening Capacity for Disaster Resilient Territories Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:43:35Z",
    "updateDateIncludingText": "2025-12-05T21:43:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-09-19T21:47:24Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5503ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5503\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Ms. Vel\u00e1zquez introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Federal Emergency Management Agency to establish a Territorial Disaster Recovery Program to continuously identify, monitor, and address factors and capability gaps that hinder the execution and completion of recovery activities relating to major disasters by eligible entities located in the territories of the United States.\n#### 1. Short title\nThis Act may be cited as the Strengthening Capacity for Disaster Resilient Territories Act .\n#### 2. Findings and purpose\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe United States territories are particularly vulnerable to extreme weather events, which have become more frequent and stronger in recent years.\n**(2)**\nCategory\u20135 Hurricane Mar\u00eda, which made its landfall in Puerto Rico on September 20, 2017, is considered to be the second deadliest storm recorded in United States history.\n**(3)**\nCategory\u20135 Hurricane Irma, which struck the U.S. Virgin Islands and Puerto Rico on September 6, 2017, is considered to be the second-most intense tropical cyclone worldwide in 2017.\n**(4)**\nTyphoon Mawar, which struck Guam on May 19, 2023, and the south of Rota, Northern Mariana Islands on May 24, 2023, is considered to be the strongest to hit Guam since 2002.\n**(5)**\nSuper Typhoon Yutu, which struck the Northern Mariana Islands on October 24, 2018, is considered to be the strongest typhoon recorded to impact the Mariana Islands.\n**(6)**\nHurricane Fiona made its landfall as a Category\u20131 Hurricane in Puerto Rico on September 18, 2022, causing severe flooding and compounding the damage left by Hurricanes Irma and Mar\u00eda.\n**(7)**\nA major disaster declaration was issued for the territory of American Samoa on September 15, 2022, due to high surf, high winds, and flooding.\n**(8)**\nRising sea levels, caused by ocean warming, contribute to the increased frequency and intensity of hurricanes, and the fragile condition of coastal environments in the United States territories. This translates to disrupted economic activity, such as tourism, agriculture and fishing, damaged dwellings, and limited drinking water supplies.\n**(9)**\nThe Federal Emergency Management Agency (hereinafter referred to as FEMA ) has obligated significant amounts of funding to address multiple natural disasters in the United States territories.\n**(10)**\nAs of September 2025, FEMA had obligated $10,382,528,245 under the Public Assistance and Hazard Mitigation programs to address damages caused by Hurricane Mar\u00eda in Puerto Rico. In addition, as of September 2025, FEMA had obligated $2,497,729,050 under the Public Assistance and Hazard Mitigation programs to address damages caused by Hurricane Fiona in Puerto Rico.\n**(11)**\nAs of August 2022, FEMA had obligated $4,200,000,000 under the Public Assistance program and $138,200,000 under the Hazard Mitigation program to address damages caused by Hurricanes Irma and Mar\u00eda in the Virgin Islands.\n**(12)**\nAfter the passage of Typhoon Mangkhut and Super Typhoon Yutu in Guam and the Northern Mariana Islands, FEMA obligated a total of $677,200,000 between 2018 and 2020 to aid response and recovery efforts related to both disasters.\n**(13)**\nThe United States territories have similar vulnerabilities that result in long and difficult recovery processes.\n**(14)**\nThe economies of the United States territories depend heavily on tourism to create revenue. Such dependency undermines disaster resiliency, given the industry\u2019s susceptibility to external shocks, such as atmospheric conditions, financial crises, and global pandemics. Any of this phenomenon can reduce the number of visitors and trigger the closure of businesses and lay-offs.\n**(15)**\nThe United States territories struggle with high levels of public debt, which impact their ability to provide cash advances to initiate disaster recovery projects. Notably\u2014\n**(A)**\nPuerto Rico is in the midst of debt restructuring proceedings that, as of 2025, have reduced Puerto Rico\u2019s public debt from over $70,000,000,000 to $31,000,000,000 and pension liabilities from $55,000,000,000 to $7,000,000,000;\n**(B)**\nas of September 2021, Virgin Islands\u2019 public debt stood at $2,200,000,000, representing 50 percent of its gross domestic product; and\n**(C)**\nas of September 2023, Guam\u2019s public debt stood at $2,500,000, representing 38 percent of its gross domestic product.\n**(16)**\nThe physical infrastructure of the United States territories, including electricity grids and water plants, is outdated, and has lacked appropriate maintenance and hardening.\n**(17)**\nThe United States territories face housing affordability and availability challenges that impact their ability to absorb the influx of the recovery workforce after a disaster occurs.\n**(18)**\nThe United States territories are situated in remote locations, which results in higher import costs, significant delays in the shipping and transportation of construction materials necessary to carry out recovery projects, and barriers for staff seeking to travel to the continental United States to receive recovery training.\n**(19)**\nThe United States territories have limited specialized staff to adequately navigate and manage recovery programs, including developing projects for obligation, using Public Assistance to cover administrative and managerial costs, and procuring goods and services according to Federal standards.\n**(20)**\nThe United States territories hurdle to find and procure specialized personnel to advance recovery efforts, such as engineers and construction contractors, given the high demand for these professionals by public agencies and large corporations in the aftermath of disasters.\n**(21)**\nThe United States territories struggle with dangerous demographic patterns that exacerbate social, financial, and economic fragilities. From 2010 to 2020, the populations of the territories shrunk, and at a faster pace than any other continental state. In such period, Puerto Rico\u2019s population was reduced by 11.8 percent, U.S. Virgin Islands\u2019 population by 18.1 percent, Northern Mariana Islands\u2019 population by 12.2 percent, American Samoa\u2019s population by 10.5 percent, and Guam\u2019s population by 3.5 percent. Additionally, the islands are experiencing lower birthrates and higher death rates.\n**(22)**\nThe postal addresses used in the United States territories have not been recognized and registered by the United States Postal Service, which can result in additional obstacles for recovery, primarily for individuals and households seeking to obtain FEMA assistance.\n**(23)**\nThe United States territories have endured consecutive major disasters, which has made it more difficult for FEMA to correctly assess recent and older damages, and therefore obligate funding for Public Assistance projects.\n**(24)**\nThe United States territories encompass a variety of languages, political sensitivities, and cultural differences that Federal authorities like FEMA have not traditionally considered, thereby impacting the territories\u2019 full and equal participation in Federal disaster recovery programs.\n##### (b) Statement of purpose\nIt is the purpose of this Act to establish a program within FEMA to continuously identify, monitor, and address factors and capability gaps that hinder the execution and completion of recovery activities by eligible entities located in the territories of the United States under sections 403, 404, 406, 407, and 502 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n#### 3. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Federal Emergency Management Agency.\n**(2) Community**\nThe term community means a network of individuals and families, businesses, governmental and nongovernmental organizations, and other civic organizations that reside or operate within a shared geographical boundary and may be represented by a common political leadership at a regional, county, municipal, or neighborhood level.\n**(3) Eligible entity**\nThe term eligible entity means an entity eligible for a grant under section 403, 404, 406, 407, or 502 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act (5121 U.S.C. et seq.).\n**(4) Recovery**\nThe term recovery means the capabilities and actions necessary to recover effectively from a major disaster declared under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ), including\u2014\n**(A)**\nrebuilding infrastructure systems;\n**(B)**\nproviding adequate interim and long-term housing for individuals impacted by such incident;\n**(C)**\nrestoring health, social, and community services;\n**(D)**\npromoting economic development; and\n**(E)**\nrestoring natural and cultural resources.\n**(5) Territory of the United States**\nThe term territory of the United States means American Samoa, the Commonwealth of the Northern Mariana Islands, the Commonwealth of Puerto Rico, Guam, the United States Virgin Islands, and any other territory or possession of the United States.\n#### 4. Territorial Disaster Recovery Program\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Administrator shall establish a Territorial Disaster Recovery Program (in this section referred to as the Program ) to continuously identify, monitor, and address factors and capability gaps of local emergency managers, or other applicable emergency response coordinators, and eligible entities located in the territories of the United States in carrying out recovery activities relating to major disasters declared under the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5121 et seq. ).\n##### (b) Duties\nIn carrying out the Program, the Administrator shall\u2014\n**(1)**\nnot later than 1 year after the date of enactment of this Act, and every 2 years thereafter, identify and analyze gaps in identifying, applying and receiving assistance, and carrying out recovery activities described in subsection (a) that are specific to eligible entities located in the territories of the United States;\n**(2)**\nprovide technical assistance to the entities described in paragraph (1) in applying for grants under sections 403, 404, 406, 407, and 502 of such Act that\u2014\n**(A)**\nis tailored to meet the needs of applicants at each stage of the administration of projects for which grants are made under such sections; and\n**(B)**\ntakes into account the challenges of\u2014\n**(i)**\napplicants who are located in remote or difficult-to-access areas;\n**(ii)**\napplicants who are part of a minority cultural group;\n**(iii)**\napplicants with limited English language proficiency; and\n**(iv)**\napplicants with slow internet speeds or limited broadband access;\n**(3)**\ndesign online and in-person training courses that are specific to the entities described in paragraph (1) and that address the capability gaps identified under this section;\n**(4)**\ndevelop best practices regarding the administration of projects in the territories of the United States for which grants are made under sections 403, 404, 406, 407, and 502 of such Act;\n**(5)**\ndevelop feedback mechanisms for entities receiving technical assistance or training under this section; and\n**(6)**\nfoster meaningful collaboration with local experts, community leaders, and other members of the community, that leads to the performance of activities under this section that are locally informed and relevant to local needs.\n##### (c) Report to Congress\n**(1) In general**\nNot later than 2 years after the date of enactment of this Act, and every 2 years thereafter for the duration of the Program, the Administrator shall submit to the Committee on Transportation and Infrastructure and the Committee on Homeland Security of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate a report on\u2014\n**(A)**\nany capability gaps identified under subsection (b)(1);\n**(B)**\nthe nature of any technical assistance provided under the Program;\n**(C)**\nany online or in-person training courses developed, or planned to be developed under the Program;\n**(D)**\nany best practices identified under subsection (b)(4); and\n**(E)**\nan analysis of, responses to, and any activities carried out as a result of feedback received by applicants for assistance under the Program and entities receiving such assistance.\n**(2) Final report**\nIn the report required to be submitted in the final year for which the Program is authorized, the Administrator shall include recommendations on\u2014\n**(A)**\nwhether to continue the Program;\n**(B)**\nif a continuation of the program is recommended, the suggested duration of such continuation; and\n**(C)**\nthe necessary funding to carry out the Program.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-09-18",
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
        "name": "Emergency Management",
        "updateDate": "2025-12-05T21:43:35Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5503ih.xml"
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
      "title": "Strengthening Capacity for Disaster Resilient Territories Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T04:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strengthening Capacity for Disaster Resilient Territories Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T04:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Emergency Management Agency to establish a Territorial Disaster Recovery Program to continuously identify, monitor, and address factors and capability gaps that hinder the execution and completion of recovery activities relating to major disasters by eligible entities located in the territories of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-08T04:03:12Z"
    }
  ]
}
```
