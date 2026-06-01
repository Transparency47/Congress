# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/646?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/646
- Title: Build Housing with Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 646
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-05-30T08:05:26Z
- Update date including text: 2025-05-30T08:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-23 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/646",
    "number": "646",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Build Housing with Care Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-30T08:05:26Z",
    "updateDateIncludingText": "2025-05-30T08:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:09:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-23T15:09:00Z",
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NV"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "DC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "MI"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NJ"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "HI"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "VA"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NC"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OH"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "FL"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr646ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 646\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Bonamici (for herself, Ms. Titus , Ms. Barrag\u00e1n , Ms. Scanlon , Mr. Panetta , Mrs. McIver , Ms. Norton , Ms. Dean of Pennsylvania , Mrs. Hayes , Mr. McGovern , Mrs. Ramirez , Ms. Salinas , Ms. Bynum , Mrs. Dingell , Mr. Keating , Ms. Garcia of Texas , Mr. Evans of Pennsylvania , Ms. Jacobs , Ms. Tlaib , Mr. Nadler , Mrs. Watson Coleman , Ms. Tokuda , Ms. McClellan , Ms. Ross , Ms. Clarke of New York , Mr. Landsman , Ms. Castor of Florida , Ms. Escobar , Ms. Hoyle of Oregon , and Ms. Dexter ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a grant program to address the crises in accessing affordable housing and child care through the co-location of housing and child care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Build Housing with Care Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to expand access to affordable housing and child care through the establishment of a grant program to promote the co-location of housing and child care providers.\n#### 3. Housing and child care provider co-location grant program\n##### (a) Establishment\nThe Secretary of Housing and Urban Development shall establish a program (hereafter in this section referred to as the Program ) to award grants, on a competitive basis, to eligible entities to facilitate the design, planning, construction, conversion, retrofitting, preservation, or renovation of a co-location facility.\n##### (b) Consultation\nIn developing the Program, the Secretary shall consult with\u2014\n**(1)**\nthe Secretary of Health and Human Services, acting through the Assistant Secretary of the Administration for Children and Families;\n**(2)**\nthe Secretary of the Treasury, acting through the Director of the Community Development Financial Institutions Fund; and\n**(3)**\nthe Secretary of Agriculture, acting through the Under Secretary for Rural Development.\n##### (c) Application\nTo be eligible to receive a grant under the Program, an eligible entity shall submit to the Secretary an application at such time, in such manner, and containing such information as the Secretary determines appropriate, including the following:\n**(1)**\nA certification that the eligible child care provider associated with such application is eligible to receive vouchers or assistance under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ), or in the case of an application to construct a new facility, or an application when the eligible entity intends to subgrant or capitalize amounts provided, a commitment to\u2014\n**(A)**\nestablish a partnership with an eligible child care provider not later than 1 year after the date on which funding is received;\n**(B)**\nsubmit to the Secretary a certification of such eligibility of said provider to receive vouchers or assistance under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ); and\n**(C)**\nclearly establish a project pipeline, and submission of a certification to the Secretary that a child care provider associated with a co-location facility project receives vouchers or assistance under the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9857 et seq. ) or the Head Start Act ( 42 U.S.C. 9831 et seq. ).\n**(2)**\nA certification that activities funded by grant amounts will not result in the eviction of residents of the housing facility associated with such application.\n**(3)**\nA description of a plan to inform and engage residents of the housing facility associated with such application about the proposed use of grant amounts.\n**(4)**\nA certification of compliance with required Federal, State, and local environmental laws and State and local land use policies, unless the eligible entity\u2014\n**(A)**\nintends to use grant amounts to facilitate the planning or design required for permit approval; or\n**(B)**\ndemonstrates that the construction, preservation, conversion, retrofitting, or renovation of an existing facility does not require environmental review.\n**(5)**\nA business plan for the eligible child care provider associated with such application, submitted at the time of application or not later than 1 year after the date on which the application is submitted, including\u2014\n**(A)**\na budget or, in the case of a new eligible child care provider, a proposed budget;\n**(B)**\nappropriate State and local licensing or, in the case of a new eligible child care provider, a copy of the application of such provider for appropriate State and local licensing; and\n**(C)**\ncopies of contracts between such provider and a local, county, regional, State, or Federal governmental entity, to facilitate\u2014\n**(i)**\nthe business operations of such provider; or\n**(ii)**\nthe enrollment of children from low-income families with such provider.\n##### (d) Awarding of grants\n**(1) Priority**\nIn awarding grants under the Program, the Secretary shall give priority to each eligible entity that demonstrates that the eligible child care provider associated with the application of such entity will\u2014\n**(A)**\noperate in a child care desert, in a low-income community, or a rural area as determined by the Secretary;\n**(B)**\ncertify designation as a Head Start provider, Early Head Start Provider, Migrant and Seasonal Head Start Provider, American Indian and Alaska Native Head Start Provider, or enroll at least 10 percent of children from very-low income families; or\n**(C)**\ndemonstrate a partnership with a community development financial institution, including through the provision of financial or technical assistance.\n**(2) Grant amounts**\nAn eligible entity may be awarded not more than $10,000,000 under this Act.\n##### (e) Use of amounts\n**(1)**\nAn eligible entity may only use grant amounts provided under the Program to facilitate the design, planning, construction, acquisition, preservation, conversion, retrofitting, long-term leasing, or renovation of a new or existing co-location facility.\n**(2)**\nAn eligible entity receiving a grant under this section may distribute grant amounts to a government entity, a nonprofit organization that develops housing, a public housing agency, a Tribally designated housing entity, or other appropriate entity as determined by the Secretary, to carry out activities in accordance with this section.\n**(3)**\nA community development financial institution receiving a grant under this section may capitalize amount received to create financial products, including loans, to carry out activities in accordance with this section.\n**(4)**\nAn eligible entity may use\u2014\n**(A)**\nnot more than 10 percent of amounts awarded to facilitate the pre-development phase of a new facility, including planning and design; and\n**(B)**\nnot more than 10 percent of amounts awarded to partner with a community development financial institution that provides technical assistance and capacity building to help the eligible entity to submit applications to the Program, support an eligible child care provider that is home-based with meeting relevant State and local licensing and quality standards, and conduct pre-development activities.\n##### (f) Assistance\nThe Secretary shall provide technical assistance and publish best practices online to facilitate the operation of co-location facilities.\n##### (g) Report to Congress\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for the duration of the Program, the Secretary shall submit a report to the Committees on Financial Services and Education and Workforce of the House of Representatives and the Committees on Banking, Housing, and Urban Affairs and Health, Education, Labor, and Pensions of the Senate regarding the implementation of the Program, including\u2014\n**(1)**\nthe number of grants awarded;\n**(2)**\na description of the activities funded;\n**(3)**\nthe number of child care slots created, including the number of child care slots serving children from low-income families or children who are dual language learners;\n**(4)**\nthe number of child care slots preserved that were at risk of elimination due to a child care center closing or proposed price increases;\n**(5)**\nthe number and percentage of residents in a co-location facility that use or are employed by the associated child care program;\n**(6)**\nthe number of staff employed by the child care provider;\n**(7)**\ndemographic data of residents of housing facilities associated with the Program;\n**(8)**\nthe number and type of projects facilitated through eligible uses of amounts described in subsections (e)(2) and (e)(3);\n**(9)**\nthe number of early childhood providers supported with funds from the program; and\n**(10)**\nthe number of eligible entities of each type that receive grant funding under the Program.\n##### (h) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $100,000,000 for each of fiscal years 2025 through 2030.\n##### (i) Definitions\nIn this section:\n**(1) Caregiver**\nThe term caregiver has the meaning given such term in section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ).\n**(2) Eligible child care provider**\nThe term eligible child care provider has the meaning given that term under section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ).\n**(3) Child care desert**\nThe term child care desert means a census tract that contains not less than 3 times more children than the licensed child care providers in such census tract have the capacity to care for, or a census tract where there are no licensed child care providers.\n**(4) Co-location facility**\nThe term co-location facility means a housing facility that contains an eligible child care provider within, on the premises of such facility or nearby such facility, where such provider serves the residents of such housing facility.\n**(5) Community development financial institution**\nThe term community development financial institution has the meaning given such term in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 ).\n**(6) Community Development Corporation**\nThe term community development corporation has the same meaning as when used in the Cranston-Gonzalex National Affordable Housing Act.\n**(7) Community housing development organization**\nThe term community housing development organization has the meaning given in the Cranston-Gonzalez National Affordable Housing Act of 1990.\n**(8) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na community development financial institution;\n**(B)**\nan eligible child care provider;\n**(C)**\na public housing authority;\n**(D)**\na government entity including a public housing agency;\n**(E)**\nan Indian Tribe or a Tribal organization;\n**(F)**\na community development corporation;\n**(G)**\na housing developer using\u2014\n**(i)**\nlow income housing tax credits; or\n**(ii)**\nnew market tax credits;\n**(H)**\na nonprofit organization that develops housing;\n**(I)**\ncommunity housing development organization;\n**(J)**\na consortia of 2 or more entities under this paragraph; or\n**(K)**\nanother entity identified as appropriate by the Secretary.\n**(9) Indian Tribe; Tribal organization**\nThe terms Indian Tribe and Tribal organization have the meanings given such terms in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ) and shall include tribally designated housing entities (as such term is defined in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 )) and entities that serve Native Hawaiians (as such term is defined in section 338K(c) of the Public Health Service Act ( 42 U.S.C. 254s(c) )).\n**(10) Low-income family**\nThe term low-income family has the meaning given such term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n**(11) Public housing agency**\nThe term public housing agency has the meaning given such term in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) ).\n**(12) Very low-income family**\nThe term very low-income family has the meaning given such term in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n#### 4. GAO study and report regarding child care access for residents of public housing\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study regarding the availability and affordability of child care for residents of public housing dwelling units, that shall include\u2014\n**(1)**\na description of how amounts from the following programs have been used by eligible child care providers to establish, renovate, or improve facilities\u2014\n**(A)**\nCommunity Development Block Grant funds;\n**(B)**\nNew Market Tax Credits;\n**(C)**\nCommunity Development Financial Institution Program funds;\n**(D)**\nLow Income Housing Tax Credits;\n**(E)**\nCapital Management Fund funds; or\n**(F)**\nHOME Investment Partnerships Program funds;\n**(2)**\nan evaluation of the effects of housing and child care costs on the economic outlook of residents of public housing dwelling units;\n**(3)**\nan evaluation of what percentage of residents of public housing dwelling units are both\u2014\n**(A)**\ncost-burdened, as defined by the Secretary of Housing and Urban Development; and\n**(B)**\npart of a household where not less than 7 percent of the income of such household is spent on child care;\n**(4)**\nidentification and analysis of State or local laws that are barriers to building or maintaining a facility for use by eligible child care providers within or near a public housing dwelling unit;\n**(5)**\nan assessment of how housing assistance provided under the program for rental assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ) affects the ability of residents of public housing dwelling units to afford child care and other essential expenses, including\u2014\n**(A)**\nfood;\n**(B)**\ntelecommunications services and equipment such as broadband internet connectivity and cellular phones; and\n**(C)**\nmeans of transportation such as automobiles, bicycles, or public transportation;\n**(6)**\nan evaluation of the efficacy of the Child and Dependent Care Tax Credit, Earned Income Tax Credit, Child Tax Credit, and Dependent Care Flexible Spending Account for residents of public housing dwelling units, including\u2014\n**(A)**\nthe degree of public knowledge about such programs;\n**(B)**\nthe degree of success of outreach or public education programs regarding such programs; and\n**(C)**\nan assessment of the sufficiency of each program to cover the costs of child care;\n**(7)**\nan evaluation of the extent that residents of public housing dwelling units receive information regarding child care resources from Federal agencies or public housing agencies; and\n**(8)**\nrecommendations to improve access to child care within and near public housing dwelling units and to improve awareness of the availability of Federal programs to assist with the costs of housing and child care.\n##### (b) Report\nNot later than 12 months after the date of the enactment of this Act, the Comptroller General shall submit a report to the Committees on Financial Services and Education and Workforce of the House of Representatives and the Committees on Banking, Housing, and Urban Affairs and Health, Education, Labor, and Pensions of the Senate, describing the results and conclusions of the study required in subsection (a).\n##### (c) Definitions\nIn this section:\n**(1) Eligible child care provider**\nThe term eligible child care provider has the meaning given such term in section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ).\n**(2) Public housing dwelling unit**\nThe term public housing dwelling unit means a dwelling unit assisted under the public housing program under the United States Housing Act of 1937 ( 42 U.S.C. 1437 et seq. ).\n**(3) Public housing agency**\nThe term public housing agency has the meaning given such term in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) ).",
      "versionDate": "2025-01-23",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Child care and development",
            "updateDate": "2025-03-19T17:37:36Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-19T17:37:36Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-19T17:37:36Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-03-19T17:37:36Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-03-19T17:37:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-02-24T21:05:56Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr646ih.xml"
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
      "title": "Build Housing with Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:51Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Build Housing with Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a grant program to address the crises in accessing affordable housing and child care through the co-location of housing and child care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:47Z"
    }
  ]
}
```
