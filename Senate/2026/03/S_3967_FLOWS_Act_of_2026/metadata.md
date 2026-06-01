# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3967?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3967
- Title: FLOWS Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3967
- Origin chamber: Senate
- Introduced date: 2026-03-03
- Update date: 2026-04-11T02:27:32Z
- Update date including text: 2026-04-11T02:27:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-03: Introduced in Senate
- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-03-03: Introduced in Senate

## Actions

- 2026-03-03 - IntroReferral: Introduced in Senate
- 2026-03-03 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-03",
    "latestAction": {
      "actionDate": "2026-03-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3967",
    "number": "3967",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Water Resources Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "FLOWS Act of 2026",
    "type": "S",
    "updateDate": "2026-04-11T02:27:32Z",
    "updateDateIncludingText": "2026-04-11T02:27:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-03",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-03",
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
          "date": "2026-03-03T16:02:47Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3967is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3967\nIN THE SENATE OF THE UNITED STATES\nMarch 3, 2026 Mr. Boozman (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo establish a rural area digital infrastructure technology grant program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Futureproofing Local Operations for Water Systems Act of 2026 or the FLOWS Act of 2026 .\n#### 2. Rural area digital infrastructure technology grant program\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Digital infrastructure technology**\nThe term digital infrastructure technology means information technology or operational technology that utilizes\u2014\n**(A)**\nremote sensing, flow or pressure monitoring, real-time monitoring, management, analytics, data, or acoustic data collection tools and technologies that may detect or reduce water loss, identify damaged or nonfunctioning infrastructure, or improve the efficiency of the operations and asset condition assessment of a public water system or treatment works;\n**(B)**\nindustrial control systems, including supervisory control and data acquisition technology;\n**(C)**\nartificial or embedded intelligence, or other intelligent optimization tools; and\n**(D)**\nhydraulic analysis, digital design software, and advanced digital design and construction management tools or software that may aid in the development of digital models and engineering plans.\n**(3) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\nthe owner or operator of a publicly owned public water system or treatment works that serves a rural area;\n**(B)**\na rural area; and\n**(C)**\na State or Tribe, on behalf of an entity described in subparagraph (A) or (B).\n**(4) Program**\nThe term program means the grant program established under subsection (b)(1).\n**(5) Public water system**\nThe term public water system has the meaning given the term in section 1401 of the Safe Drinking Water Act ( 42 U.S.C. 300f ).\n**(6) Rural area**\nThe term rural area has the meaning given the term in section 609(a) of the Public Utility Regulatory Policies Act of 1978 ( 7 U.S.C. 918c(a) ).\n**(7) Treatment works**\nThe term treatment works has the meaning given the term in section 212 of the Federal Water Pollution Control Act ( 33 U.S.C. 1292 ).\n##### (b) Grant program\n**(1) Establishment**\nThe Administrator shall establish a grant program to provide infrastructure assistance to eligible entities in accordance with this subsection.\n**(2) Form of grants**\n**(A) In general**\nSubject to subparagraph (B), the Administrator may award a grant under the program to assist an eligible entity in\u2014\n**(i)**\ndesigning, constructing, operating, and maintaining digital infrastructure technology for water infrastructure, source water protection, and water development projects in rural areas, including for\u2014\n**(I)**\nfacilities that supply, collect, and treat water, including drinking water, wastewater, and stormwater, including through desalination and water reuse;\n**(II)**\nwater distribution or wastewater conveyance systems; and\n**(III)**\nthe protection or development of surface water or groundwater resources, including through banking or recharging of aquifers;\n**(ii)**\nproviding training and workforce development activities to help project and construction managers and owners and operators of drinking water, wastewater, and stormwater utilities manage water infrastructure projects using digital infrastructure technology; and\n**(iii)**\nmitigating risks and employing countermeasures to reduce the vulnerabilities of digital infrastructure technology for water infrastructure from cyber-attacks through on-site cybersecurity training and technical assistance.\n**(B) Acquisition and maintenance of software**\nWith respect to digital infrastructure technology that is software and notwithstanding any other provision of law, including the Safe Drinking Water Act ( 42 U.S.C. 300f ), the recipient of a grant under the program may use grant funds for the initial acquisition and ongoing maintenance costs of that software.\n**(3) Prioritization**\nIn selecting recipients of grants under the program, the Administrator shall give priority to eligible entities that\u2014\n**(A)**\nown or operate public water systems or treatment works that serve fewer than 3,300 people; and\n**(B)**\nserve people or comprise people that, as determined by the Administrator, are most in need, such as\u2014\n**(i)**\npre-fabricated home community organizations or associations that are controlled by a local public body; and\n**(ii)**\nother organizations that\u2014\n**(I)**\nown or operate a public water system or treatment works; and\n**(II)**\nare owned or controlled by members of the community served by the public water system or treatment works, as opposed to investor-owned.\n**(4) Authorization of appropriations**\nThere is authorized to be appropriated to the Administrator to carry out the program $50,000,000 for each of fiscal years 2027 through 2031, to remain available until expended.\n##### (c) Applicability of other Federal and State laws\nNothing in this Act waives, limits, or otherwise affects the applicability of any provision of Federal or State law that would apply to a project to be carried out with grants provided under the program.\n##### (d) Digital transformation study\nNot later than 5 years after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study to determine the impact of adopting digital infrastructure technology in water infrastructure projects in rural areas, including\u2014\n**(1)**\nidentification of\u2014\n**(A)**\nwater loss and inadequate fire flow capacity in public water systems that serve rural areas;\n**(B)**\npotential bottlenecks in combined sewer systems that serve rural areas that could prevent an overflow in a wastewater infrastructure system caused by extreme precipitation or excess runoff; and\n**(C)**\nmodels and simulations that are effective in assessing the challenges of water resource management in rural areas; and\n**(2)**\nrecommendations for\u2014\n**(A)**\ndeveloping water resource management plans to accommodate population growth in rural areas;\n**(B)**\nprioritizing areas for improvement of the infrastructure and operations of public water systems and treatment works in rural areas;\n**(C)**\nmaximizing interoperability of digital infrastructure technology with other systems, products, tools, and applications;\n**(D)**\nreducing project delays and cost overruns in projects that serve rural areas;\n**(E)**\nreducing the total cost of drinking water and wastewater infrastructure projects in rural areas;\n**(F)**\nunderstanding the impact of digital infrastructure technology in rural areas on sustainability and resiliency of a public water system or treatment works; and\n**(G)**\nusing digital infrastructure technology to increase the affordability of drinking water, wastewater, and stormwater services in rural areas.\n##### (e) Report\nNot later than December 31, 2030, the Comptroller General of the United States shall submit to the Committee on Environment and Public Works of the Senate and the Committee on Transportation and Infrastructure of the House of Representatives a report describing\u2014\n**(1)**\nthe results of the study under subsection (d); and\n**(2)**\nthe results of the program.",
      "versionDate": "2026-03-03",
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
        "name": "Water Resources Development",
        "updateDate": "2026-04-11T02:27:31Z"
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
      "date": "2026-03-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3967is.xml"
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
      "title": "FLOWS Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FLOWS Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Futureproofing Local Operations for Water Systems Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a rural area digital infrastructure technology grant program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:18:24Z"
    }
  ]
}
```
