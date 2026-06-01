# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1417?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1417
- Title: Rural Health Care Facility Technical Assistance Program Act
- Congress: 119
- Bill type: HR
- Bill number: 1417
- Origin chamber: House
- Introduced date: 2025-02-18
- Update date: 2026-04-28T08:06:01Z
- Update date including text: 2026-04-28T08:06:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-18: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-02-18: Introduced in House

## Actions

- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Introduced in House
- 2025-02-18 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1417",
    "number": "1417",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Rural Health Care Facility Technical Assistance Program Act",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:01Z",
    "updateDateIncludingText": "2026-04-28T08:06:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T18:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:43:08Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "HI"
    },
    {
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "MT"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "ME"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "IA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MN"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "WV"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "KS"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "AR"
    },
    {
      "bioguideId": "G000546",
      "district": "6",
      "firstName": "Sam",
      "fullName": "Rep. Graves, Sam [R-MO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Graves",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "MO"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "GA"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "WA"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "CO"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "VA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "MD"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "KS"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "GA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "WA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "GU"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CO"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1417ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1417\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 18, 2025 Mr. Jackson of Texas (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo expand and codify the Rural Hospital Technical Assistance Program of the Department of Agriculture and rename it as the Rural Health Care Facility Technical Assistance Program.\n#### 1. Short title\nThis Act may be cited as the Rural Health Care Facility Technical Assistance Program Act .\n#### 2. Expansion and codification of the rural health care facility technical assistance program of the Department of Agriculture\n##### (a) In general\nIn lieu of any other authority under which the Secretary of Agriculture (in this section referred to as the Secretary ) may provide technical assistance to any eligible health care facility, the Secretary shall establish, and maintain, directly or by grant, contract, or cooperative agreement, a Rural Health Care Facility Technical Assistance Program (in this section referred to as the Program ) to provide technical assistance and training, tailored to the capacity and needs of each eligible health care facility, to help eligible health care facilities in rural areas\u2014\n**(1)**\nidentify development needs for maintaining essential health care services, and support action plans for operational and quality improvement projects to meet the development needs;\n**(2)**\nbetter manage their financial and business strategies, including providing financial planning assistance and preparing long-term financial plans; and\n**(3)**\nidentify, and apply for assistance from, loan and grant programs of the Department of Agriculture for which the facilities are eligible.\n##### (b) Goals\nThe goals of the Program shall be to\u2014\n**(1)**\nimprove the long-term financial position and operational efficiency of the eligible health care facilities;\n**(2)**\nprevent the closure of eligible health care facilities;\n**(3)**\nstrengthen the delivery of health care in rural areas;\n**(4)**\nhelp eligible rural health care facilities better access and compete for loans and grants from programs administered by the Department of Agriculture; and\n**(5)**\ncontinue the activities of the Rural Hospital Technical Assistance Program in effect as of the date of the enactment of this subsection.\n##### (c) Program participation\n**(1) In general**\nThe Secretary shall engage in outreach and engagement strategies to encourage eligible health care facilities to participate in the Program.\n**(2) Eligible health care facility selection**\nIn selecting eligible health care facilities to participate in the Program, the Secretary shall give priority to borrowers and grantees of the Rural Housing Service, Rural Business-Cooperative Service, and Rural Utilities Service. The Secretary may also consider\u2014\n**(A)**\nthe age and physical state of the health care facility involved;\n**(B)**\nthe financial vulnerability of the eligible health care facility, and the ability of the eligible health care facility to meet debt obligations;\n**(C)**\nthe electronic health record implementation needs of the health care facility;\n**(D)**\nwhether the eligible health care facility is located in a health professional shortage area or a medically underserved area;\n**(E)**\nwhether the eligible health care facility serves a medically underserved population; and\n**(F)**\nsuch other criteria and priorities as are determined by the Secretary.\n##### (d) Reporting requirements\nNot later than 1 year after the date of the enactment of this section, and annually thereafter, the Secretary shall submit to the Committee on Agriculture of the House of Representatives and the Committee on Agriculture, Nutrition, and Forestry of the Senate a written report describing the progress and results of the program conducted under this section, which should include\u2014\n**(1)**\na brief description of each project to provide technical assistance to an eligible health care facility under this section, including\u2014\n**(A)**\nthe name and location of the facility;\n**(B)**\na description of the assistance provided;\n**(C)**\na description of the outcomes for completed projects;\n**(D)**\nthe cost of the technical assistance; and\n**(E)**\nany other information the Secretary deems appropriate;\n**(2)**\na summary of the technical assistance projects completed;\n**(3)**\na summary of the outcomes of the technical assistance projects;\n**(4)**\nan assessment of the effectiveness of the Program; and\n**(5)**\nrecommendations for improving the Program.\n##### (e) Limitations on authorization of appropriations\nTo carry out this section, there are authorized to be appropriated to the Secretary not more than $2,000,000 for each of fiscal years 2026 through 2030.\n##### (f) Definitions\nIn this section:\n**(1) Rural area**\nThe term rural area has the meaning given the term in section 343(a)(13)(A) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1991(a)(13)(A) ).\n**(2) Development needs**\nThe term development needs includes\u2014\n**(A)**\nconstructing, expanding, renovating, or otherwise modernizing health care facilities;\n**(B)**\nincreasing telehealth capabilities;\n**(C)**\nacquiring or upgrading health care information systems such as electronic health records;\n**(D)**\nproviding financial planning assistance and preparing long-term financial plan; and\n**(E)**\nsuch other needs as the Secretary deems critical to maintaining health care services in the community in which an eligible health care facility is located.\n**(3) Eligible health care facility**\nThe term eligible health care facility means a facility that is located in a rural area and is\u2014\n**(A)**\na hospital (as defined in section 1861(e) of the Social Security Act);\n**(B)**\na psychiatric hospital (as defined in section 1861(f) of such Act);\n**(C)**\na long-term care hospital (as defined in section 1861(ccc) of such Act);\n**(D)**\na critical access hospital (as defined in section 1861(mm)(1) of such Act);\n**(E)**\na rural health clinic (as defined in section 1861(aa)(2) of such Act);\n**(F)**\na religious nonmedical health care institution (as defined in section 1861(ss)(1) of such Act);\n**(G)**\na sole community hospital (as defined in section 1886(d)(5)(C)(iii) of such Act);\n**(H)**\na rural emergency hospital (as defined in section 1861(kkk)(2) of such Act);\n**(I)**\na home health agency (as defined in section 1861(o) of such Act); or\n**(J)**\na community health center (as defined in section 330 of the Public Health Service Act).\n**(4) Health professional shortage area**\nThe term health professional shortage area has the meaning given the term in section 332(a)(1)(A) of the Public Health Service Act.\n**(5) Medically underserved area**\nThe term medically underserved area has the meaning given the term in section 330I(a)(5) of the Public Health Service Act.\n**(6) Medically underserved population**\nThe term medically underserved population has the meaning given the term in section 330(b)(3) of the Public Health Service Act.",
      "versionDate": "2025-02-18",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-03-21T15:21:42Z"
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
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1417ih.xml"
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
      "title": "Rural Health Care Facility Technical Assistance Program Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:32:55Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Health Care Facility Technical Assistance Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To expand and codify the Rural Hospital Technical Assistance Program of the Department of Agriculture and rename it as the Rural Health Care Facility Technical Assistance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:29Z"
    }
  ]
}
```
