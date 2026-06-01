# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6217?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6217
- Title: Revitalize Our Neighborhoods Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6217
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-02-03T09:05:40Z
- Update date including text: 2026-02-03T09:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6217",
    "number": "6217",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "M001214",
        "district": "1",
        "firstName": "Frank",
        "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
        "lastName": "Mrvan",
        "party": "D",
        "state": "IN"
      }
    ],
    "title": "Revitalize Our Neighborhoods Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:40Z",
    "updateDateIncludingText": "2026-02-03T09:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:04:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
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
      "sponsorshipDate": "2025-11-20",
      "state": "DC"
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
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "WA"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "KY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OH"
    },
    {
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PR"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6217ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6217\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Mrvan (for himself, Mr. Sorensen , Ms. Norton , Mr. Kennedy of New York , Mr. Thanedar , Ms. Tlaib , Ms. Budzinski , Ms. Randall , Mr. McGarvey , and Mr. Landsman ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo authorize the Secretary of Housing and Urban Development to make grants to eligible entities for use to eliminate blight and assist in neighborhood revitalization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Revitalize Our Neighborhoods Act of 2025 .\n#### 2. Blight elimination and neighborhood revitalization grants\n##### (a) Authority\nThe Secretary of Housing and Urban Development may make grants under this section, on a competitive basis, to eligible entities for use for eligible activities designed to eliminate blight and promote neighborhood revitalization.\n##### (b) Use in low-Income areas\nAmounts from a grant awarded under this section may be used only to carry out eligible activities within low-income communities.\n##### (c) Eligible entities\nTo be eligible for a grant under this section, and entity shall be\u2014\n**(1)**\na State;\n**(2)**\na unit of general local government, including a city, county, town, parish, village, or other general-purpose political subdivision of a State; or\n**(3)**\na multi-jurisdictional entity.\n##### (d) Eligible activities\n**(1) In general**\nAmounts from a grant awarded under this section may be used only for the following activities:\n**(A)**\nDemolition, clearance, and removal of blighted structures.\n**(B)**\nBoarding of vacant properties and blighted structures.\n**(C)**\nDeconstruction of structures.\n**(D)**\nRemoval of waste and site clearance and vacant land management.\n**(E)**\nRenovation of existing structures that are blighted or abandoned.\n**(F)**\nConstruction or preservation of affordable rental or owner-occupied housing as an outcome of blight elimination.\n**(G)**\nAdministrative costs, including for staffing and compliance with grant requirements, in an amount that is not more than 10 percent of the total grant for the recipient.\n**(2) Use of amounts by land banks, Community Housing Development Organizations, and local governments**\n**(A) In general**\nA recipient of grant under this section that may provide such grant amounts to land banks or Community Housing Development Organizations (as such term is defined in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704(1) )) to carry out eligible activities within low-income communities.\n**(B) State grantees**\nA recipient of a grant under this section that is a State may provide such grant amounts to units of general local government whose jurisdictions include low-income communities to carry out eligible activities within such low-income communities.\n**(3) Prohibition**\nAmounts from a grant awarded under this section may not be used to acquire any occupied residential dwelling unit.\n##### (e) Matching requirement\n**(1) In general**\nThe Secretary shall require each eligible entity that receives a grant under this section to contribute an amount of matching funds that is equal to or greater than 15 percent of the amount of the grant, to be used for eligible activities under this section.\n**(2) Source of funds**\nAmounts from the following sources may be counted towards compliance with the requirement under paragraph (1):\n**(A)**\nAny amounts received pursuant to any Federal program.\n**(B)**\nAny amounts provided by the applicants.\n**(C)**\nAny proceeds from sales of properties renovated using grant amounts under this section.\n##### (f) Application and plan\n**(1) Application**\nA grant awarded under this section may only be provided to an eligible entity that submits to the Secretary an application for such a grant that contains a plan for use of grant funds in accordance with paragraph (2) and such other information, certifications, and assurances as the Secretary considers necessary.\n**(2) Plan**\nA plan under this paragraph shall be a detailed 5-year plan for the use of grant amounts awarded under this section and matching amounts contributed that includes\u2014\n**(A)**\nidentification of the low-income communities in which eligible activities under subsection (d)(1) will be carried out using grant and matching amounts;\n**(B)**\na description of the eligible activities under subsection (d)(1) to be carried out using grant and matching amounts;\n**(C)**\na timetable for carrying out such eligible activities, which shall provide for the expenditure of grant and matching amounts within 5 years after receipt; and\n**(D)**\nidentification of the sources of matching amounts to be provided and assurances of the availability of such matching amounts.\n##### (g) Selection; criteria\nThe Secretary shall select applications to receive grants under this section pursuant to a competition and based on criteria as established by the Secretary for such selection.\n##### (h) Coordination with other Federal programs\nAn eligible entity that receives grant amounts under this section may use such grant amounts in coordination with the eligible activities of other Federal programs, including with\u2014\n**(1)**\nthe Community Development Block Grant program;\n**(2)**\nthe HOME Investment Partnership program;\n**(3)**\nthe Housing Trust Fund;\n**(4)**\nthe Low-Income Housing Tax Credit program;\n**(5)**\nthe Environmental Protection Agency Brownfields Program; and\n**(6)**\nthe New Market Tax Credit program.\n##### (i) Technical assistance\n**(1) In general**\nThe Secretary shall provide technical assistance to eligible entities that receive a grant under this section for the life cycle of the grant.\n**(2) Limitation**\nThe Secretary may not use more than 5 percent of amounts appropriated under this section for technical assistance.\n##### (j) Reports\n**(1) Grantee reports**\n**(A) In general**\nNot later than 15 months after receiving an initial grant under this section, and annually thereafter, a recipient of such grant shall submit to the Secretary a report on the activities funded with amounts under this section, through a report template developed by the Secretary.\n**(B) Requirements**\nThe report required under subparagraph (A) shall include a description of\u2014\n**(i)**\namounts used for the matching requirement;\n**(ii)**\namounts used for eligible activities funded under this section, apart from the amounts provided under this section;\n**(iii)**\nresources made available by amounts provided under this section;\n**(iv)**\nhow the recipient invested amounts under this section;\n**(v)**\nthe geographic distribution of such investments;\n**(vi)**\nthe families and persons assisted under this section; and\n**(vii)**\nthe progress meeting planned objectives using amounts provided under this section.\n**(C) Availability**\nThe Secretary shall make the reports submitted under this paragraph publicly available on a website of the Department of Housing and Urban Development.\n**(2) GAO reports**\n**(A) Initial report**\nNot later than 3 years after initial grant awards are provided under this section, the Comptroller General of the United States shall submit to the Congress a report that describes, with respect to the grant program under this section\u2014\n**(i)**\nplanned projects;\n**(ii)**\npopulations impacted;\n**(iii)**\nchallenges and recommendations; and\n**(iv)**\nexpected outcomes.\n**(B) Final report**\nNot later than 6 years after initial grant awards are provided under this section, the Comptroller General of the United States shall submit to the Congress a report that describes, with respect to the grant program under this section\u2014\n**(i)**\nfinal outcomes;\n**(ii)**\nthe implementation and projects completed;\n**(iii)**\npopulations impacted; and\n**(iv)**\nchallenges and recommendations for future recipients of grants under this section.\n##### (k) Definitions\nFor purposes of this section, the following definitions shall apply:\n**(1) Abandoned**\nThe term abandoned means, with respect to an unoccupied structure\u2014\n**(A)**\nthe mortgage, tribal leasehold, or tax payments are at least 90 days delinquent;\n**(B)**\na code enforcement inspection has determined that the property is not habitable and the owner has taken no corrective actions within 90 days of notification of the deficiencies; or\n**(C)**\nthe structure is subject to a court-ordered receivership or nuisance abatement related to abandonment pursuant to State or local law or otherwise meets a State definition of an abandoned structure.\n**(2) Affordable rental or owner-occupied housing**\nThe term affordable rental or owner-occupied housing means housing that qualifies as affordable under section 215 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12745 ).\n**(3) Blighted**\nThe term blighted means a structure that exhibits determinable signs of deterioration sufficient to constitute a threat to human health, safety, and public welfare, as determined by the Secretary.\n**(4) Land bank**\nThe term land bank means a government entity, agency, or program, or a special purpose nonprofit entity formed by 1 or more units of government in accordance with a State or local law with respect to land banks, that has been designated by 1 or more State or local governments to acquire, steward, and dispose of vacant, abandoned, or other problem properties in accordance with locally determined priorities.\n**(5) Low-income community**\nThe term low-income community has the meaning given such term in section 45D of the Internal Revenue Code of 1986 ( 26 U.S.C. 45D ) and includes any census tract or other area that is treated as a low-income community for purposes of such section.\n**(6) Multi-jurisdictional entity**\nThe term multi-jurisdictional entity means an association of local governments or public agencies which are bound by a collective agreement, as determined appropriate by the Secretary for the purpose of carrying out the eligible activities under this section.\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(8) State**\nThe term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Virgin Islands, Guam, American Samoa, the Northern Mariana Islands, the Trust Territory of the Pacific Islands, and any other territory or possession of the United States.\n**(9) Structure**\nThe term structure includes residential structures and commercial structures.\n**(10) Unoccupied**\nThe term unoccupied means a structure that\u2014\n**(A)**\nhas no occupants;\n**(B)**\nis not being maintained for seasonal use;\n**(C)**\nis not actively marketed for sale or rent; or\n**(D)**\nis not being held vacant pending re-occupancy by a buyer or tenant.\n##### (l) Regulations\nThe Secretary may issue any regulations necessary to carry out this section.\n##### (m) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this section for each of fiscal years 2026 through 2031.",
      "versionDate": "2025-11-20",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-12-10T16:39:15Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6217ih.xml"
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
      "title": "Revitalize Our Neighborhoods Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Revitalize Our Neighborhoods Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Secretary of Housing and Urban Development to make grants to eligible entities for use to eliminate blight and assist in neighborhood revitalization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:21Z"
    }
  ]
}
```
