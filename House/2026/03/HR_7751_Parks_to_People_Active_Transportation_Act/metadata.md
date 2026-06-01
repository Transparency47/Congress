# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7751?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7751
- Title: Parks to People Active Transportation Act
- Congress: 119
- Bill type: HR
- Bill number: 7751
- Origin chamber: House
- Introduced date: 2026-03-02
- Update date: 2026-05-06T14:34:20Z
- Update date including text: 2026-05-06T14:34:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-02: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- Latest action: 2026-03-02: Introduced in House

## Actions

- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Introduced in House
- 2026-03-02 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-02",
    "latestAction": {
      "actionDate": "2026-03-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7751",
    "number": "7751",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Parks to People Active Transportation Act",
    "type": "HR",
    "updateDate": "2026-05-06T14:34:20Z",
    "updateDateIncludingText": "2026-05-06T14:34:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-02",
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
      "actionDate": "2026-03-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-02",
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
          "date": "2026-03-02T14:00:45Z",
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
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "GA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "MI"
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
      "sponsorshipDate": "2026-03-03",
      "state": "DC"
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
      "sponsorshipDate": "2026-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "NV"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7751ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7751\nIN THE HOUSE OF REPRESENTATIVES\nMarch 2, 2026 Mrs. McIver (for herself and Mrs. McBath ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo direct the Secretary of Transportation to carry out a program to make grants for the improvement or construction of greenway paths, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Parks to People Active Transportation Act .\n#### 2. National and regional greenways program\n##### (a) In general\nThe Secretary shall carry out a program to make grants, on a competitive basis, to eligible organizations to improve or construct safe and connected greenway paths between communities that are designated as regionally or nationally significant by the Secretary under subsection (b).\n##### (b) Regionally or nationally significant greenway paths\nIn carrying out the program under this section, the Secretary shall establish a national greenway paths network. The national greenway paths network shall contain regionally or nationally significant greenway paths designated by the Secretary that\u2014\n**(1)**\ncross multiple local jurisdictions or State lines;\n**(2)**\nreduce congestion and single-occupant vehicle trips, improve safety and access to jobs, and lower emissions for criteria pollutants (NOx, VOC, PM) and greenhouse gases;\n**(3)**\nsupport community goals and objectives in areas covered by metropolitan planning organizations; or\n**(4)**\nmeet any other criteria the Secretary determines appropriate.\n##### (c) Application\n**(1) In general**\nTo receive a grant under this section, an eligible organization shall submit to the Secretary an application in such manner and containing such information as the Secretary may require.\n**(2) Eligible projects partially on Federal land**\nWith respect to an application for eligible greenway projects that are located in part on Federal lands, an eligible organization shall enter into a cooperative agreement with the appropriate Federal agency with jurisdiction over such land to be eligible for a grant under this section.\n##### (d) Application considerations\nIn making a grant for construction of a greenway path under this section, the Secretary shall consider the following:\n**(1)**\nWhether the proposed eligible greenway project is likely to provide substantial additional opportunities for walking, bicycling, and recreation, including by\u2014\n**(A)**\ncreating greenway paths connecting multiple communities, counties, metropolitan regions, or States;\n**(B)**\nintegrating greenway paths with transit services, where available, to improve access to public transportation; and\n**(C)**\nintegrating greenway paths with existing parks, recreation or scenic areas, adjacent waterways, or transportation corridors.\n**(2)**\nWhether the eligible organization proposing a project demonstrates broad community support through\u2014\n**(A)**\nprior public input in the development of a plan for the proposed project; and\n**(B)**\nthe commitment of any project sponsors and community leaders, including elected officials in the jurisdiction in which such project is located, partner organization leaders, and private or nongovernmental organizations in the area in which such project is located, to the success and timely implementation of an eligible greenway project.\n**(3)**\nThe extent to which the eligible organization provides evidence of commitment to traffic safety, regulations, financial incentives, or community design policies that facilitate significant increases in walking and bicycling.\n**(4)**\nThe extent to which the eligible organization demonstrates commitment of State, local, or eligible Federal matching funds, and land or in-kind contributions, in addition to the local match required under subsection (g)(1), unless the applicant qualifies for an exception under subsection (g)(2).\n**(5)**\nThe extent to which the eligible organization demonstrates that the grant will address existing disparities in bicyclist and pedestrian fatality rates based on race or income level or provide access to schools, jobs, services, transit, or recreational opportunities for low-income communities and communities of color.\n**(6)**\nWhether the eligible organization demonstrates how investment in active transportation will advance safety for pedestrians and cyclists, accessibility to schools, jobs, and transit, accessibility to national, State, or local parks, economic competitiveness, environmental protection, and quality of life.\n##### (e) Use of funds\nA grant awarded under this section may be used\u2014\n**(1)**\nto improve or construct a greenway path; and\n**(2)**\nto acquire real property necessary for the improvement or construction of a greenway path.\n##### (f) Set aside\n**(1) Planning and design grants**\nEach fiscal year, the Secretary shall set aside not less than $5,000,000 from the funds made available to carry out this section to provide planning grants for eligible organizations to develop a local or regional greenways and paths plan.\n**(2) Administrative costs**\nEach fiscal year, the Secretary shall set aside not more than $3,500,000 of the funds made available to carry out this section to cover the costs of administration, research, technical assistance, communications, and training activities under the program.\n##### (g) Grant timing\n**(1) Request for application**\nNot later than 60 days after funds are made available to carry out this section, the Secretary shall publish in the Federal Register a request for applications for grants under this section.\n**(2) Selection of grant recipients**\nNot later than 180 days after funds are made available to carry out this section, the Secretary shall select grant recipients for grants under this section.\n##### (h) Federal share\n**(1) In general**\nExcept as provided in paragraph (2), the Federal share of the cost of a project under this section shall not exceed 80 percent of the total project cost.\n**(2) Exceptions**\n**(A) Disadvantaged communities**\nFor projects serving communities with a poverty rate of over 40 percent based on the majority of census tracts served by such project, the Secretary may increase the Federal share of the cost of a project under this section to 100 percent of the total project cost.\n**(B) Rural areas**\nFor projects serving rural areas, as such term is defined in section 101 of title 23, United States Code, the Federal share of the cost of a project under this section shall be 90 percent of the total project cost.\n##### (i) Reports\n**(1) Interim report**\nNot later than September 30, 2028, the Secretary shall submit to Congress a report containing the information described in paragraph (3).\n**(2) Final report**\nNot later than September 30, 2030, the Secretary shall submit to Congress a report containing the information described in paragraph (3).\n**(3) Report information**\nA report submitted under this subsection shall contain the following:\n**(A)**\nA list of grants made under this section.\n**(B)**\nBest practices of recipients in implementing projects funded under this section.\n**(C)**\nImpediments experienced by recipients of grants under this section in planning for and delivering projects under this section.\n##### (j) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $300,000,000 for each of fiscal years 2027 through 2031.\n##### (k) Definitions\nIn this Act:\n**(1) Active transportation**\nThe term active transportation means alternative methods of transportation to motor vehicles, including walking, bicyling, or utilizing assistive mobility or micro mobility devices.\n**(2) Greenway path**\nThe term greenway path means a hard-surfaced or wheelchair-accessible facility built for active transportation, including a walkway, bikeway, or shared-use path that connects communities, cities, counties, metropolitan regions, or States.\n**(3) Community**\nThe term community means a geographic area that is socioeconomically interdependent and may include rural, suburban, and urban jurisdictions.\n**(4) Eligible organization**\nThe term eligible organization means\u2014\n**(A)**\na local or regional governmental organization, including a metropolitan planning organization or regional planning organization or council;\n**(B)**\na multi-county special district;\n**(C)**\na State (including the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, and any other territory of the United States);\n**(D)**\na multi-State group of governments; and\n**(E)**\nan Indian Tribe.\n**(5) Eligible greenway project**\nThe term eligible greenway project means an active transportation project, or group of projects\u2014\n**(A)**\nthat is designated as a regionally or nationally significant greenway path under subsection (b);\n**(B)**\nwithin or between a community or group of communities, at least one of which falls within the jurisdiction of an eligible organization, which has submitted an application under this section;\n**(C)**\nthat has\u2014\n**(i)**\na total cost of not less than $15,000,000; or\n**(ii)**\nwith respect to planning and design grants, planning and design costs of not less than $100,000;\n**(D)**\nthat construct path segments that close local or regional network gaps or are located within underserved areas;\n**(E)**\nthat support an accessible public realm, connect to public transportation, support opportunities for economic development, or promote health and safety; and\n**(F)**\nthat connect communities to public spaces and parks, enhance ecological connectivity, support land conservation and access, or support sites for remediation and restoration.\n**(6) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4(e) of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304(e) ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Transportation.\n**(8) Total project cost**\nThe term total project cost means the sum total of all costs incurred in the development of a project that are approved by the Secretary as reasonable and necessary, including\u2014\n**(A)**\nthe cost of acquiring real property;\n**(B)**\nthe cost of site preparation, demolition, and development;\n**(C)**\nexpenses related to the issuance of bonds or notes;\n**(D)**\nfees in connection with the planning, execution, and financing of the project;\n**(E)**\nthe cost of studies, surveys, plans, permits, insurance, interest, financing, tax, and assessment costs;\n**(F)**\nthe cost of construction, rehabilitation, reconstruction, and equipping the project;\n**(G)**\nthe cost of land improvements;\n**(H)**\ncontractor fees;\n**(I)**\nthe cost of training and education related to the safety of users of any greenway path constructed as part of an eligible greenway project; and\n**(J)**\nany other cost that the Secretary determines is necessary and reasonable.",
      "versionDate": "2026-03-02",
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
        "updateDate": "2026-03-20T18:51:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-02",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr7751",
          "measure-number": "7751",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-02",
          "originChamber": "HOUSE",
          "update-date": "2026-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7751v00",
            "update-date": "2026-05-06"
          },
          "action-date": "2026-03-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Parks to People Active Transportation Act</strong></p><p>This bill requires the Department of Transportation (DOT) to establish a grant program for states, localities, and Indian tribes to support community greenway paths for walking, bicycling, and other motor vehicle alternatives.</p><p>DOT must designate eligible greenway paths that are considered regionally or nationally significant through a national greenway paths network; paths must cross multiple localities or states, reduce congestion, improve safety, benefit the environment, support communities, or meet other specified criteria. Eligible projects must support access to public parks, transportation, and other community needs.</p>"
        },
        "title": "Parks to People Active Transportation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7751.xml",
    "summary": {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parks to People Active Transportation Act</strong></p><p>This bill requires the Department of Transportation (DOT) to establish a grant program for states, localities, and Indian tribes to support community greenway paths for walking, bicycling, and other motor vehicle alternatives.</p><p>DOT must designate eligible greenway paths that are considered regionally or nationally significant through a national greenway paths network; paths must cross multiple localities or states, reduce congestion, improve safety, benefit the environment, support communities, or meet other specified criteria. Eligible projects must support access to public parks, transportation, and other community needs.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr7751"
    },
    "title": "Parks to People Active Transportation Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Parks to People Active Transportation Act</strong></p><p>This bill requires the Department of Transportation (DOT) to establish a grant program for states, localities, and Indian tribes to support community greenway paths for walking, bicycling, and other motor vehicle alternatives.</p><p>DOT must designate eligible greenway paths that are considered regionally or nationally significant through a national greenway paths network; paths must cross multiple localities or states, reduce congestion, improve safety, benefit the environment, support communities, or meet other specified criteria. Eligible projects must support access to public parks, transportation, and other community needs.</p>",
      "updateDate": "2026-05-06",
      "versionCode": "id119hr7751"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7751ih.xml"
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
      "title": "Parks to People Active Transportation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Parks to People Active Transportation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to carry out a program to make grants for the improvement or construction of greenway paths, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:21Z"
    }
  ]
}
```
