# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4025?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4025
- Title: Energy Transitions Initiative Authorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4025
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2025-07-17T11:31:51Z
- Update date including text: 2025-07-17T11:31:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-17 - IntroReferral: Sponsor introductory remarks on measure. (CR E582-583)
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-06-17 - IntroReferral: Sponsor introductory remarks on measure. (CR E582-583)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4025",
    "number": "4025",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001055",
        "district": "1",
        "firstName": "Ed",
        "fullName": "Rep. Case, Ed [D-HI-1]",
        "lastName": "Case",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Energy Transitions Initiative Authorization Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-17T11:31:51Z",
    "updateDateIncludingText": "2025-07-17T11:31:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR E582-583)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:02:00Z",
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
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4025ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4025\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Case introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Energy to establish an initiative to provide grants to fund the development of resilient energy systems in remote communities, island communities, and Tribal communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Energy Transitions Initiative Authorization Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nRemote communities, island communities, and Tribal communities are commonly characterized by the unique challenges arising from isolation and the resultant difficulties in achieving economies of scale in the delivery of critical goods and services.\n**(2)**\nWith respect to energy, such challenges include high energy costs, limited and non-resilient energy infrastructure, and increased vulnerability to natural disasters.\n**(3)**\nSelf-sufficient renewable energy solutions are required to ensure energy security for these communities.\n**(4)**\nThese communities require specialized assistance, which they have difficulty procuring on their own, in acquiring and building necessary infrastructure, such as energy storage, solar energy facilities, hydropower plants, distributed energy resources, microgrids, and necessary transportation.\n**(5)**\nSuch specialized assistance should be provided in partnership with remote communities, island communities, and Tribal communities because their unique expertise and deep knowledge of local challenges and needs are necessary for the success of resulting solutions.\n#### 3. Energy Transitions Initiative grant\n##### (a) Establishment\nThe Secretary of Energy shall establish an initiative to provide grants to eligible entities to fund eligible projects for the development of resilient energy systems in remote communities, island communities, and Tribal communities.\n##### (b) Terms\n**(1) Grants**\nIn carrying out the initiative, the Secretary may make a grant of not more than $5,000,000 to an eligible entity for an eligible project.\n**(2) Cost-share**\nThe Secretary may not make a grant under this section in an amount that is more than 90 percent of the cost of an eligible project.\n##### (c) Technical assistance\nUpon the request of a grantee, the Secretary shall provide technical assistance to such grantee for a period of not less than 1 year and not more than 2 years through the Energy Transitions Initiative Partnership Program.\n##### (d) GAO audit\nNot later than 1 year after the establishment of the initiative described in this section, and annually thereafter, the Comptroller General of the United States shall\u2014\n**(1)**\nconduct an audit of the initiative established under this section to ensure proper use of funds and compliance with applicable regulations; and\n**(2)**\nsubmit a report that includes the results of such audit and recommendations for improving the efficiency and effectiveness of the initiative to\u2014\n**(A)**\nthe Committee on Energy and Commerce of the House of Representatives;\n**(B)**\nthe Committee on Appropriations of the House of Representatives;\n**(C)**\nthe Committee on Energy and Public Works of the Senate; and\n**(D)**\nthe Committee on Appropriations of the Senate.\n##### (e) Authorization of Appropriations\nThere is authorized to be appropriated to the Secretary $31,000,000 for each of fiscal years 2026 through 2030 to carry out this section.\n##### (f) Definitions\nFor purposes of this section:\n**(1) Alaska Native Corporation**\nThe term Alaska Native Corporation has the meaning given the term Native Corporation in section 3 of the Alaska Native Claims Settlement Act ( 42 U.S.C. 1602 ).\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State that includes a remote community, an island community, or a Tribal community;\n**(B)**\na unit of local government serving or that includes a remote community or an island community;\n**(C)**\na Tribal community; or\n**(D)**\na community organization that serves a remote community, an island community, or a Tribal community.\n**(3) Eligible project**\nThe term eligible project means any of the following projects:\n**(A)**\nA project to implement energy efficiency measures in buildings.\n**(B)**\nA project for a resilient energy system that is a project to develop\u2014\n**(i)**\na hydropower, solar power, wind energy, geothermal energy, tidal power, or wave energy system;\n**(ii)**\na microgrid; or\n**(iii)**\ninfrastructure necessary for the transmission and distribution of electricity.\n**(4) Federally recognized Tribe**\nThe term federally recognized tribe has the meaning given the term in section 102(2) of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5130(2) ).\n**(5) Island community**\nThe term island community means a group of individuals living on an area of land isolated from the mainland by oceans or lakes, that is not connected to a larger regional grid network, and experiences resilience challenges, including energy disruptions or threats to infrastructure from natural disasters.\n**(6) Native Hawaiian Organization**\nThe term Native Hawaiian Organization means an organization listed by the Department of the Interior in the Native Hawaiian Organization Notification List maintained by the Office of Native Hawaiian Relations.\n**(7) Remote community**\nThe term remote community means a group of individuals living in an area isolated from a larger regional grid network, with limited access to centralized energy sources due to environmental or geographical impediments.\n**(8) Resilient energy system**\nThe term resilient energy system means a facility or equipment that\u2014\n**(A)**\ncan generate and deliver energy; and\n**(B)**\ncan withstand or quickly recover from an energy disruption.\n**(9) State**\nThe term State means each of the 50 States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Northern Mariana Islands.\n**(10) Tribal community**\nThe term Tribal community means a federally recognized Tribe, an Alaska Native Corporation, or a Native Hawaiian Organization.",
      "versionDate": "2025-06-17",
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
        "updateDate": "2025-07-09T13:06:25Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4025ih.xml"
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
      "title": "Energy Transitions Initiative Authorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:51Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Energy Transitions Initiative Authorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T12:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Energy to establish an initiative to provide grants to fund the development of resilient energy systems in remote communities, island communities, and Tribal communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T12:18:20Z"
    }
  ]
}
```
