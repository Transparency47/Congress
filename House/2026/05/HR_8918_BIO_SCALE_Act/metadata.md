# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8918
- Title: BIO-SCALE Act
- Congress: 119
- Bill type: HR
- Bill number: 8918
- Origin chamber: House
- Introduced date: 2026-05-20
- Update date: 2026-05-29T15:55:53Z
- Update date including text: 2026-05-29T15:55:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-20: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-05-20: Introduced in House

## Actions

- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Introduced in House
- 2026-05-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - IntroReferral: Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8918",
    "number": "8918",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001307",
        "district": "4",
        "firstName": "James",
        "fullName": "Rep. Baird, James R. [R-IN-4]",
        "lastName": "Baird",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "BIO-SCALE Act",
    "type": "HR",
    "updateDate": "2026-05-29T15:55:53Z",
    "updateDateIncludingText": "2026-05-29T15:55:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-20",
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
      "text": "Referred to the Committee on Transportation and Infrastructure, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-20T15:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2026-05-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8918ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8918\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2026 Mr. Baird (for himself and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide for the establishment of technology maturation facilities for the bioindustrial sector, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bioindustrial Infrastructure for Open Scale-up, Commercialization, and Accelerated Launch Ecosystems Act or the BIO-SCALE Act .\n#### 2. Technology maturation facility program\n##### (a) Definitions\nIn this section:\n**(1) Bioindustrial sector**\nThe term bioindustrial sector means industries involved in producing bio-based chemicals, fuels, materials, and other products through biological and biochemical processes.\n**(2) Eligible entity**\nThe term eligible entity means public and private foundations and nonprofit organizations, including institutions of higher education, that\u2014\n**(A)**\nare incorporated in the United States; and\n**(B)**\noperate primarily in the United States.\n**(3) Facility**\nThe term facility means a facility established under subsection (c).\n**(4) Feedstock**\nThe term feedstock means raw material used as input for industrial processes to produce biofuels, chemicals, or materials, such as agricultural byproducts, microbial or algal biomass, synthetic biological products or components, and waste oils.\n**(5) Open access**\nThe term open access means the use of infrastructure, data, or research resources that are\u2014\n**(A)**\navailable without licensing or intellectual property barriers; and\n**(B)**\naccessible to public and private entities on an equitable basis.\n**(6) Product-agnostic**\nThe term product-agnostic , with respect to a facility, technology, or process means that the facility, technology, or process can accommodate a variety of end products without being limited to a specific output.\n**(7) Secretary**\nThe term Secretary means the Secretary of Commerce, acting through the Assistant Secretary for Economic Development.\n**(8) Technology maturation**\nThe term technology maturation means the development, testing, and scaling of technologies to a level of readiness suitable for commercialization or integration into industrial processes, including activities such as prototyping, pilot-scale testing and demonstration, and early-stage manufacturing and market entry.\n##### (b) Purpose\nThe purpose of this section is to establish technology maturation facilities to provide world-class capabilities, positioning the United States as a leader in bioindustrial innovation and enabling participation in groundbreaking projects through state-of-the-art infrastructure.\n##### (c) Establishment\n**(1) In general**\nThe Secretary shall establish not less than 3 regional, nonprofit, open access, product-agnostic technology maturation facilities for the bioindustrial sector to ensure the integration of advanced and emerging capabilities such as solid-state, gas, and continuous fermentation methods, biomass processing equipment, and scalable commercial-grade fermentation tanks of capacity ranging from 1,500 to over 75,000 liters.\n**(2) Operation**\nIn carrying out this section, the Secretary shall\u2014\n**(A)**\nuse a competitive process to carry out paragraph (1) through the award of\u2014\n**(i)**\nplanning grants or cooperative agreements to eligible entities for the design, construction, and operation of the facilities; and\n**(ii)**\nimplementation grants or cooperative agreements to eligible entities that were awarded and completed a planning grant or cooperative agreement under clause (i); and\n**(B)**\nfacilitate commercialization activities and technology transfer in coordination with any applicable programs of the Department of Energy and the Department of Defense.\n##### (d) Implementation plan\nNot later than 180 days after the date of enactment of this Act, the Secretary shall submit to Congress a report on plans to implement this section, including, at a minimum\u2014\n**(1)**\nfinalized site selection criteria and a description of the decisionmaking process that will be used, including a timeline for selecting facilities;\n**(2)**\nfunding allocation methodologies and a description of the decisionmaking process that was used in developing those methodologies;\n**(3)**\ndesign specifications for facilities, including a plan for consulting with entities outside of the Department of Commerce, as appropriate;\n**(4)**\nan outreach strategy for soliciting proposals and engaging key stakeholders across industry, academia, and government, including specific goals to advance the leadership of the United States in the biotechnological and bioindustrial sectors;\n**(5)**\nconsiderations for how facilities may\u2014\n**(A)**\ncomplement existing infrastructure of the Department of Energy, the Department of Defense, and other facilities;\n**(B)**\nensure increased production levels by functioning as a connected network, including by providing fermentation capacity that covers the full range needed for precommercial scale-up; and\n**(C)**\nbuild on existing initiatives to increase local or regional job opportunities and economic growth and competitiveness; and\n**(6)**\nhow the Secretary intends to coordinate with other Federal agencies, such as the Department of Energy and the Department of Defense, to ensure the effective usage of funds, development of capabilities, and prioritization of biotechnologies.\n##### (e) Proposals and selection\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall\u2014\n**(A)**\nsolicit proposals from eligible entities for the design, construction, and establishment of the facilities; and\n**(B)**\nselect not less than 3 facilities.\n**(2) Considerations**\nIn selecting facilities under paragraph (1)(B), the Secretary shall\u2014\n**(A)**\nensure that the facilities are geographically distributed throughout the United States, with preference given to proposals for\u2014\n**(i)**\nfacilities located near major feedstock sources; and\n**(ii)**\nfacilities located in areas with established bioindustrial capabilities;\n**(B)**\ngive preference to proposals for\u2014\n**(i)**\nfacilities in regions with a demonstrated need for enhanced infrastructure, especially in rural areas; and\n**(ii)**\nfacilities from eligible entities already engaged in biotechnological and bioindustrial activities.\n##### (f) Use of funds\n**(1) In general**\nFunds provided for a facility under this section shall be used for construction, equipment procurement, and initial operating expenses of the facility.\n**(2) Deadline**\nFunds provided for a facility under this section shall be expended by\u2014\n**(A)**\nnot later than 2 years after the date on which the amounts were provided to the facility, in the case of a facility that has existing infrastructure and resources, as determined by the Secretary; and\n**(B)**\nnot later than 3 years after the date on which the amounts were provided to the facility, in the case of a facility that is to be constructed.\n##### (g) Facility goals and activities\nA facility shall seek\u2014\n**(1)**\nto advance and promote technological innovation in bioindustrial processes, including fermentation, biomass processing, and downstream processing;\n**(2)**\nto strengthen national security by de-risking and accelerating the scaling up of emerging biotechnology processes and technologies;\n**(3)**\nto enhance the leadership of the United States in biotechnology through the promotion of innovation, economic growth, workforce development, and job creation;\n**(4)**\nto establish a secure digital infrastructure for data sharing and process analysis; and\n**(5)**\nto provide unique technical capabilities to sustain the cutting-edge position of the United States in biotechnology in order to enhance economic growth and international competitiveness.\n##### (h) Oversight and interagency coordination and collaboration\nIn carrying out this section, the Secretary shall\u2014\n**(1)**\nif applicable, oversee the design, construction, and establishment of the facilities to ensure the integration of advanced and emerging capabilities;\n**(2)**\nestablish partnerships with industry, institutions of higher education, and other Federal agencies to maximize the impact and utilization of the facilities;\n**(3)**\ndevelop and implement policies to ensure equitable and open access to the facilities for public and private sector entities, with a focus on inclusion of rural communities;\n**(4)**\npursue cost-sharing and co-funding arrangements or opportunities with private sector stakeholders to supplement Federal funding and promote financial sustainability; and\n**(5)**\ncoordinate and consult with relevant stakeholders to identify suitable locations and capabilities objectives for the facilities, which stakeholders may include\u2014\n**(A)**\nother Federal agencies, such as the Department of Energy, including the National Laboratories;\n**(B)**\nthe defense community, including the Department of Defense and BioMADE;\n**(C)**\nindustry partners, including nonprofit organizations;\n**(D)**\nthe agricultural community and relevant Federal agencies, including the Department of Agriculture;\n**(E)**\nthe transportation sector and relevant Federal agencies, including the Department of Transportation;\n**(F)**\nFederal education and workforce development programs, including the National Science Foundation;\n**(G)**\ninstitutions of higher education;\n**(H)**\nrural community stakeholders;\n**(I)**\nState and local governments; and\n**(J)**\ninternational bodies with relevant scientific expertise.\n##### (i) Intellectual property protections\n**(1) Federal employee contributions**\nAny intellectual property created by a Federal employee at a facility in the performance of the duties of that employee shall be considered to be part of the public domain.\n**(2) Other entities**\nAny intellectual property created by an individual at a facility who is not described in paragraph (1) shall be protected under applicable intellectual property laws, subject to the terms of the agreement that the individual has entered into with the Secretary.\n**(3) Data sharing**\nTo the maximum extent practicable, the facilities shall establish secure, interoperable digital systems to facilitate data exchange across government, academia, and industry.\n##### (j) Reports\nNot less frequently than annually, the Secretary shall submit to Congress a report that includes\u2014\n**(1)**\na description of the progress on the construction and operation of the facilities;\n**(2)**\nmetrics on facility activities, including\u2014\n**(A)**\ndata on usage and participation by public and private sector entities;\n**(B)**\na description of ongoing and completed projects of the facilities related to scale-up and commercialization of biotechnologies; and\n**(C)**\nany additional relevant metrics, such as\u2014\n**(i)**\nworkforce training and development, including engagement with local or regional academic institutions; and\n**(ii)**\ndomestic and local job creation;\n**(3)**\nfinancial reports that detail expenditures and cost-sharing contributions of the facilities, including access to private capital; and\n**(4)**\na description of any obstacles encountered by the facilities in carrying out facility activities and achieving the goals described in subsection (g).\n##### (k) Authorization of appropriations\n**(1) In general**\nThere are authorized to be appropriated to the Secretary to carry out this section\u2014\n**(A)**\n$345,000,000 for the period of fiscal years 2026 through 2028; and\n**(B)**\n$117,000,000 for the period of fiscal years 2029 through 2030.\n**(2) Administrative costs**\nOf the amounts made available for each fiscal year under paragraph (1), the Secretary may use not more than 7.5 percent for the administrative and oversight costs of implementing this section.\n##### (l) Sunset\n**(1) In general**\nSubject to paragraph (2), the authority to establish and operate a facility under this section shall terminate on the date that is 10 years after the date of enactment of this Act.\n**(2) Continued operation**\nThe Secretary may allow a facility that demonstrates successful performance to continue to operate after the date described in paragraph (1), subject to ongoing oversight by the Secretary.",
      "versionDate": "2026-05-20",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-29T15:55:53Z"
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
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8918ih.xml"
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
      "title": "BIO-SCALE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-22T02:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIO-SCALE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bioindustrial Infrastructure for Open Scale-up, Commercialization, and Accelerated Launch Ecosystems Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-22T02:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the establishment of technology maturation facilities for the bioindustrial sector, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-22T02:18:34Z"
    }
  ]
}
```
