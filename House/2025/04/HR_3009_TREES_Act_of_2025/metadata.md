# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3009
- Title: TREES Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3009
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2026-05-21T08:08:00Z
- Update date including text: 2026-05-21T08:08:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3009",
    "number": "3009",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "M001163",
        "district": "7",
        "firstName": "Doris",
        "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
        "lastName": "Matsui",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "TREES Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:00Z",
    "updateDateIncludingText": "2026-05-21T08:08:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
          "date": "2025-04-24T15:04:35Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "PA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MO"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "KS"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "DE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3009ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3009\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Ms. Matsui (for herself, Mr. Fitzpatrick , and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Secretary of Energy to establish a grant program to facilitate tree planting that reduces residential energy consumption, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Trees for Residential Energy and Economic Savings Act of 2025 or the TREES Act of 2025 .\n#### 2. Tree planting grant program\n##### (a) Establishment\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish a program under which the Secretary may award grants to eligible entities to facilitate covered projects in accordance with this section.\n##### (b) Consultation\nIn carrying out the Program, the Secretary shall consult with the Secretary of Agriculture, acting through the Chief of the Forest Service.\n##### (c) Applications\nTo receive a grant under the Program, an eligible entity shall submit to the Secretary an application at such time, in such form, and containing such information as the Secretary may require, including the following:\n**(1)**\nA description of how the proposed covered project will reduce residential energy consumption.\n**(2)**\nAn estimate of the expected reduction in residential energy consumption to be achieved by the covered project.\n**(3)**\nA description of the total eligible costs of the project and other sources of funding for the covered project.\n**(4)**\nA description of anticipated community engagement in the covered project.\n**(5)**\nA description of the tree species to be planted under the covered project and the suitability of such species to the local environment.\n##### (d) Priority\nIn awarding grants under the Program, the Secretary shall give priority to covered projects that\u2014\n**(1)**\nprovide the largest potential reduction in residential energy consumption for households with a high energy burden;\n**(2)**\nprovide maximum amounts of\u2014\n**(A)**\nshade during periods when residences are exposed to the most sun intensity; and\n**(B)**\nwind protection during periods when residences are exposed to the most wind intensity;\n**(3)**\nare located in a neighborhood with a low percentage of tree canopy cover;\n**(4)**\nare located in a neighborhood with a high percentage of senior citizens or children;\n**(5)**\nare located in an area where the average annual income is below the regional median;\n**(6)**\nwill collaboratively engage community members to be affected by the tree planting; and\n**(7)**\nwill employ local residents as a substantial percentage of the workforce of the covered project, with a focus on local residents who are unemployed or underemployed.\n##### (e) Tree planting goals\nSubject to the availability of appropriations, the Secretary shall, to the maximum extent practicable, award grants under the Program in a manner that facilitates the planting of at least 300,000 trees each year.\n##### (f) Federal share\nThe Federal share of the cost of a covered project assisted by a grant awarded under the Program shall be 90 percent.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out the Program, $50,000,000 for each of fiscal years 2026 through 2030.\n##### (h) Definitions\nIn this section:\n**(1) Covered project**\nThe term covered project means a tree planting project carried out to reduce residential energy consumption.\n**(2) Eligible cost**\nThe term eligible cost means, with respect to a covered project\u2014\n**(A)**\nthe cost of carrying out the project, including\u2014\n**(i)**\nplanning and design activities;\n**(ii)**\nestablishing nurseries to supply trees;\n**(iii)**\npurchasing trees; and\n**(iv)**\npreparing sites and planting trees;\n**(B)**\nthe cost of maintaining and monitoring planted trees for a period of not more than 3 years;\n**(C)**\nthe cost of training activities; and\n**(D)**\nany other cost determined appropriate by the Secretary.\n**(3) Eligible entity**\nThe term eligible entity means each of the following:\n**(A)**\nA State government entity.\n**(B)**\nA local government entity.\n**(C)**\nAn Indian Tribe.\n**(D)**\nA nonprofit organization.\n**(E)**\nA retail power provider.\n**(4) Energy burden**\nThe term energy burden means the percentage of household income spent on residential energy bills.\n**(5) Indian Tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(6) Local government entity**\nThe term local government entity means any municipal government or county government entity with jurisdiction over local land use decisions.\n**(7) Nonprofit organization**\nThe term nonprofit organization means an organization described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such Code.\n**(8) Program**\nThe term Program means the program established under subsection (a).\n**(9) Retail power provider**\nThe term retail power provider means any entity authorized under State or Federal law to generate, distribute, or provide retail electricity, natural gas, or fuel oil service.\n**(10) Secretary**\nThe term Secretary means the Secretary of Energy.",
      "versionDate": "2025-04-24",
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
        "updateDate": "2025-05-29T17:50:42Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3009ih.xml"
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
      "title": "TREES Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TREES Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Trees for Residential Energy and Economic Savings Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Energy to establish a grant program to facilitate tree planting that reduces residential energy consumption, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:30Z"
    }
  ]
}
```
