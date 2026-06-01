# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4575?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4575
- Title: Jobs in the Woods Act
- Congress: 119
- Bill type: HR
- Bill number: 4575
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-04-09T16:49:56Z
- Update date including text: 2026-04-09T16:49:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4575",
    "number": "4575",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000600",
        "district": "3",
        "firstName": "Marie",
        "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
        "lastName": "Perez",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Jobs in the Woods Act",
    "type": "HR",
    "updateDate": "2026-04-09T16:49:56Z",
    "updateDateIncludingText": "2026-04-09T16:49:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NC"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "MN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "ME"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "PA"
    },
    {
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-22",
      "state": "NY"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "AL"
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
      "sponsorshipDate": "2025-09-04",
      "state": "ME"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OR"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NH"
    },
    {
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "WA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "PA"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4575ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4575\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Ms. Perez (for herself, Mr. Rouzer , Mr. Stauber , Ms. Pingree , Mr. Fitzpatrick , and Mr. Thompson of Pennsylvania ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo require the Secretary of Agriculture to establish a grant program to address forestry workforce development needs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Jobs in the Woods Act .\n#### 2. Forestry workforce development grants\n##### (a) Establishment\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall establish a competitive grant program to make grants to eligible entities to carry out career pathway training programs in eligible areas in accordance with subsection (c).\n**(2) Term; amount**\nA grant made under this section shall be\u2014\n**(A)**\nfor a period of not greater than 4 years; and\n**(B)**\nmade in an amount\u2014\n**(i)**\ngreater than or equal to $500,000; and\n**(ii)**\nless than or equal to $2,000,000.\n##### (b) Applications\n**(1) In general**\nTo be eligible to receive a grant under this section, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary may require, which shall include\u2014\n**(A)**\na demonstrated capacity to carry out a career pathway training program in accordance with subsection (c);\n**(B)**\na demonstration of need for such program within a region;\n**(C)**\na projection of the extent of reach intended for such program;\n**(D)**\na plan to ensure that such program is sustainable; and\n**(E)**\na plan for the implementation of such program.\n**(2) Priority**\nIn awarding grants under this section, the Secretary shall give priority to eligible entities that\u2014\n**(A)**\npropose to carry out activities to address the issues of an aging workforce and youth migration;\n**(B)**\nto engage students, intends to partner with\u2014\n**(i)**\na secondary school;\n**(ii)**\na vocational or technical school; or\n**(iii)**\na junior or community college; and\n**(C)**\ndemonstrate the ability to assist with forestry workforce placement and hiring.\n##### (c) Use of funds\nAn eligible entity that receives a grant under this section shall use the grant funds to carry out career pathway training programs with respect to forestry operations and forestry products industries.\n##### (d) Definitions\nIn this section:\n**(1) Career pathway**\nThe term career pathway has the meaning given the term in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ).\n**(2) Eligible area**\nThe term eligible area means\u2014\n**(A)**\na nonmetropolitan area that qualifies as a low-income community (as defined in section 45D(e) of the Internal Revenue Code of 1986);\n**(B)**\nan area that has access to or has a plan to achieve broadband service (as defined in section 601 of the Rural Electrification Act of 1936 ( 7 U.S.C. 950bb )); and\n**(C)**\nan area that has a population of 50,000 or fewer inhabitants.\n**(3) Eligible entity**\nThe term eligible entity means a nonprofit organization, a State, an Indian Tribe, a local government, or an institution of higher education.\n**(4) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(5) Junior or community college**\nThe term junior or community college has the meaning given such term in section 312(f) of the Higher Education Act of 1965 ( 20 U.S.C. 1058(f) ).\n**(6) Secondary school**\nThe term secondary school has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $10,000,000 for each of fiscal years 2026 through 2030.",
      "versionDate": "2025-07-21",
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
        "updateDate": "2026-04-09T16:49:56Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4575ih.xml"
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
      "title": "Jobs in the Woods Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T09:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Jobs in the Woods Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T09:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to establish a grant program to address forestry workforce development needs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T09:33:19Z"
    }
  ]
}
```
