# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1978
- Title: Defense Technology Hubs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1978
- Origin chamber: Senate
- Introduced date: 2025-06-05
- Update date: 2025-10-28T11:03:15Z
- Update date including text: 2025-10-28T11:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-05: Introduced in Senate
- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-06-05: Introduced in Senate

## Actions

- 2025-06-05 - IntroReferral: Introduced in Senate
- 2025-06-05 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-05",
    "latestAction": {
      "actionDate": "2025-06-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1978",
    "number": "1978",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Defense Technology Hubs Act of 2025",
    "type": "S",
    "updateDate": "2025-10-28T11:03:15Z",
    "updateDateIncludingText": "2025-10-28T11:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-05",
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
          "date": "2025-06-05T18:02:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-06-05",
      "state": "CO"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1978is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1978\nIN THE SENATE OF THE UNITED STATES\nJune 5, 2025 Mr. Schmitt (for himself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the Secretary of Defense to establish a network of regional hubs to foster innovation, collaboration, and rapid development of defense-related technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defense Technology Hubs Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to enhance national security and technological superiority by requiring the Secretary of Defense to establish a network of regional defense technology hubs to foster innovation, collaboration, and rapid development of defense-related technologies to attract talent from across the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Anchor Federal defense institution**\nThe term anchor Federal defense institution means a defense manufacturing facility, an institution of higher education that engages the Department on research, development, testing, and evaluation, or a military installation.\n**(2) Defense technology hub**\nThe term defense technology hub means a regional hub designated and supported under the Program.\n**(3) Eligible consortium**\nThe term eligible consortium means a consortium composed of universities, defense contractors, small businesses, nonprofit organizations, and State or local governments.\n**(4) Emerging technologies**\nThe term emerging technologies means scientific and engineering advancements with potential military applications as identified by the Secretary of Defense.\n**(5) Program**\nThe term Program means the Defense Technology Hubs Program established under section 4(a).\n#### 4. Establishment of Defense Technology Hubs Program\n##### (a) Program required\n**(1) In general**\nThe Secretary of Defense shall establish a program to designate and support regional hubs focused on advancing defense technologies critical to national security.\n**(2) Designation**\nThe program established pursuant to paragraph (1) shall be known as the Defense Technology Hubs Program .\n##### (b) Designation of defense technology hubs\n**(1) Solicitation of applications**\nUnder the Program, the Secretary shall solicit applications from eligible consortia to be designated as defense technology hubs under the Program.\n**(2) Submittal of applications**\nA consortium seeking designation and support as a regional hub under subsection (a)(1) shall submit to the Secretary an application therefor at such time, in such manner, and containing such information as the Secretary may require.\n**(3) Criteria**\nThe Secretary shall select eligible consortia for designation and support under subsection (a)(1) from among those submitting applications pursuant to paragraph (2) of this subsection using the following criteria:\n**(A)**\nDemonstrated capability in defense-relevant technology areas.\n**(B)**\nEvidence of regional collaboration and stakeholder commitment.\n**(C)**\nPresence of anchor Federal defense institutions or mission-critical installations of the Department that support or utilize emerging defense technologies, particularly in areas such as geospatial intelligence, data fusion, and artificial intelligence.\n**(D)**\nExistence of regional innovation ecosystems with demonstrated success in leveraging Federal, State, and private sector collaboration, such as technology innovation consortia, academic research clusters, and specialized defense accelerators.\n**(E)**\nPotential to address Department-identified strategic priorities.\n**(F)**\nEconomic and workforce development impact.\n**(4) Geographic distribution**\nIn selecting eligible consortia for designation and support under the Program, the Secretary shall ensure that defense technology hubs are distributed across diverse geographic regions of the United States, with a goal of designating at least 10 defense technology hubs before the date that is 3 years after the date of the enactment of this Act. In considering geographic distribution, the Secretary may give preference to regions with demonstrated strategic relevance to national security missions, including those with newly constructed or expanded Department facilities and intelligence community investments.\n##### (c) Objectives of defense technology hubs\nThe objectives of a defense technology hub under the Program are as follows:\n**(1)**\nTo accelerate the research, development, prototyping, and transition to operational use of emerging technologies with military applications, including artificial intelligence, quantum technologies, hypersonics, biotechnology, and advanced manufacturing.\n**(2)**\nTo foster partnerships among components of the Department of Defense, private industry, academic institutions, and State and local governments.\n**(3)**\nTo address regional defense technology needs while leveraging local expertise, infrastructure, and economic strengths, including proximity to Federal mission partners such as combat support agencies and participation in existing innovation consortia or university-industry alliances.\n**(4)**\nTo promote workforce development and training programs to build a skilled pipeline for defense innovation including partnerships with research universities, community colleges, and vocational programs.\n**(5)**\nTo enhance the resilience and security of the defense industrial base.\n##### (d) Grants\n**(1) Grants authorized**\nUnder the Program, the Secretary may award grants to defense technology hubs.\n**(2) Use of funds**\nA defense technology hub receiving a grant under paragraph (1) shall use the amounts of the grant for the following purposes:\n**(A)**\nAs seed funding for establishment of the defense technology hub.\n**(B)**\nFor research, prototyping, and technology transition projects consistent with the objectives set forth in subsection (c).\n**(C)**\nAdministrative and evaluation expenses of the defense technology hub relating activities under the Program.\n##### (e) Security and compliance requirements\n**(1) In general**\nUnder the Program, each defense technology hub shall do the following:\n**(A)**\nImplement cybersecurity measures consistent with Department cybersecurity standards.\n**(B)**\nEnsure all research and technology transfers comply with the International Traffic in Arms Regulations (ITAR) and the Export Administration Regulations (EAR).\n**(C)**\nPrevent participation by foreign entities of concern, as identified by the Secretary in coordination with the heads of the elements of the intelligence community (as defined in section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )) or identified in the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, and consistent with existing Federal designations.\n**(D)**\nEstablish mechanisms to prevent unauthorized access to sensitive defense-related research and technology.\n**(2) Monitoring and enforcement**\nThe Secretary shall, in coordination with the Director of the Defense Counterintelligence and Security Agency, establish procedures to monitor and enforce compliance with the requirements set forth in paragraph (1).\n##### (f) Intellectual property management\n**(1) Guidelines required**\nThe Secretary shall develop guidelines under the Program for intellectual property ownership and licensing within the defense technology hubs, balancing national security needs with commercial incentives for private sector participation.\n**(2) Retention of rights**\nThe guidelines developed pursuant to paragraph (1) shall include provisions for the Department to retain necessary rights for defense applications while allowing members of consortia that are defense technology hubs to pursue commercial opportunities as may be appropriate.\n##### (g) Funding\n**(1) Authorization of appropriations**\nThere is authorized to be appropriated to the Department of Defense to carry out the Program $375,000,000 for the period of fiscal years 2026 through 2030.\n**(2) Availability**\nOf the amounts appropriated pursuant to the authorization in paragraph (1), $75,000,000 shall be available to the Secretary to award grants under subsection (d).\n**(3) Federal share**\nThe Federal share of support provided to a defense technology hub under the Program in a fiscal year may not exceed 50 percent of the total cost of the operations and activities of the defense technology hub under the Program in that fiscal year.\n##### (h) Administration\n**(1) In general**\nThe Secretary shall administer the Program through the Under Secretary of Defense for Research and Engineering, in coordination with the Director of the Defense Innovation Unit and the heads of such other elements of the Department as the Secretary considers appropriate.\n**(2) Waiver of acquisition regulations**\nFor any project of a defense technology hub under the Program that the Secretary determines has a total cost of less than $10,000,000, the Secretary may waive applicable acquisition regulations to expedite development and prototyping, consistent with similar authorities of the Secretary that were in effect on the day before the date of the enactment of this Act.\n**(3) Annual progress reports**\nEach defense technology hub shall, not less frequently than once each year, submit to the Secretary an annual progress report detailing technological advancements, partnerships, and economic outcomes.\n#### 5. Coordination with existing program\nThe Secretary of Defense shall ensure the Program complements, and does not duplicate, existing efforts such as efforts of the Defense Advanced Research Projects Agency (DARPA), the Manufacturing USA Institutes, the Regional Technology and Innovation Hubs of the Economic Development Administration (EDA), the Defense Innovation Unit (DIU), and the Regional Innovation Engines of the National Science Foundation. The Secretary shall, as the Secretary determines appropriate, align defense technology hub activities with existing defense and intelligence infrastructure to maximize the use of established mission platforms and reduce redundant investments, particularly in areas where new Federal campuses are designed to serve as long-term anchors for defense innovation ecosystems.\n#### 6. Evaluation and reporting\n##### (a) Independent evaluations\nThe Secretary of Defense shall seek to enter into a contract with an independent entity to evaluate the effectiveness of the Program annually for the first 5 years of the Program, and biennially thereafter, assessing technology outputs, national security impacts, and return on investment.\n##### (b) Annual reports\nNot less frequently than once each year, the Secretary shall submit to the Committee on Armed Services of the Senate and the Committee on Armed Services of the House of Representatives an annual report detailing Program activities, defense technology hub performance, and recommendations for improvement to the Program.\n#### 7. Effective date\nThe provisions of this Act shall take effect on the date that is 180 days after the date of the enactment of this Act.",
      "versionDate": "2025-06-05",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-16T15:13:32Z"
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
      "date": "2025-06-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1978is.xml"
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
      "title": "Defense Technology Hubs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defense Technology Hubs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Defense to establish a network of regional hubs to foster innovation, collaboration, and rapid development of defense-related technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T05:18:24Z"
    }
  ]
}
```
