# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1991
- Title: Producer and Agricultural Credit Enhancement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1991
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-01-31T09:05:28Z
- Update date including text: 2026-01-31T09:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1991",
    "number": "1991",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "Producer and Agricultural Credit Enhancement Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:28Z",
    "updateDateIncludingText": "2026-01-31T09:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:12:15Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "MN"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-09-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
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
      "sponsorshipDate": "2025-09-16",
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
      "sponsorshipDate": "2025-10-10",
      "state": "MD"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "OH"
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
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "LA"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "HI"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "IN"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "IN"
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
      "sponsorshipDate": "2025-11-20",
      "state": "PR"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "KS"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-11-25",
      "state": "NC"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "VA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1991ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1991\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Finstad (for himself and Ms. Craig ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to modify limitations on amounts of farm ownership loans and operating loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producer and Agricultural Credit Enhancement Act of 2025 .\n#### 2. Limitations on loan amounts\n##### (a) Limitations on amount of farm ownership loans\nSection 305(a)(2) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925(a)(2) ) is amended by striking $600,000, or, in the case of a loan guaranteed by the Secretary, $1,750,000 (increased, beginning with fiscal year 2019 and inserting $850,000, or, in the case of a loan guaranteed by the Secretary, $3,500,000 (increased, beginning with fiscal year 2025 .\n##### (b) Limitations on amount of operating loans\nSection 313(a)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1943(a)(1) ) is amended by striking $400,000, or, in the case of a loan guaranteed by the Secretary, $1,750,000 (increased, beginning with fiscal year 2019 and inserting $750,000, or, in the case of a loan guaranteed by the Secretary, $3,000,000 (increased, beginning with fiscal year 2025 .\n#### 3. Inflation percentage\nSection 305(c) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925(c) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking of the Prices Paid By Farmers Index (as compiled by the National Agricultural Statistics Service of the Department of Agriculture) for the 12-month period ending on July 31 of the immediately preceding fiscal year and inserting of the per acre average United States farm real estate value, the per acre average United States cropland value, and the per acre average United States pasture value for the preceding year (as published in the applicable Agricultural Land Values report of the National Agricultural Statistics Service of the Department of Agriculture), weighted equally ; and\n**(2)**\nin paragraph (2), by striking of such index (as so defined) for the 12-month period that immediately precedes the 12-month period described in paragraph (1) and inserting of the per acre average United States farm real estate value, the per acre average United States cropland value, and the per acre average United States pasture value for the year immediately preceding the year described in paragraph (1) (as so published), weighted equally .\n#### 4. Down payment loan program\nSection 310E(b)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1935(b)(1) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking exceed 45 percent of the least and inserting exceed, subject to section 305(a), 45 percent of the lesser ;\n**(2)**\nin subparagraph (A), by adding or after the semicolon;\n**(3)**\nin subparagraph (B), by striking ; or and inserting a period; and\n**(4)**\nby striking subparagraph (C).\n#### 5. Limitation on microloan amounts\nSection 313(c)(2) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1943(c)(2) ) is amended by striking $50,000 and inserting $100,000 .\n#### 6. Refinancing of guaranteed loans into direct loans\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture, acting through the Administrator of the Farm Service Agency (referred to in this section as the Secretary ), shall promulgate regulations allowing certain loans guaranteed by the Farm Service Agency to be refinanced into direct loans issued by the Farm Service Agency, in accordance with this section.\n##### (b) Requirements\n**(1) In general**\nThe regulations promulgated under subsection (a) shall provide that a guaranteed loan described in that subsection may be refinanced into a direct loan described in that subsection only if the Secretary determines that\u2014\n**(A)**\nthe guaranteed loan is distressed;\n**(B)**\nthe borrower on that guaranteed loan has attempted to work with the lender and has been unsuccessful;\n**(C)**\na reasonable chance for the success of the operation financed by the guaranteed loan exists; and\n**(D)**\nall other criteria established by the Secretary for purposes of this section to protect taxpayer funds and the loan programs of the Farm Service Agency have been satisfied.\n**(2) Reasonable chance of success**\nFor purposes of paragraph (1)(C), the Secretary may determine that a reasonable chance for the success of an operation exists if the Secretary determines that\u2014\n**(A)**\nall relevant problems with the operation financed by the guaranteed loan\u2014\n**(i)**\nhave been identified; and\n**(ii)**\ncan be corrected; and\n**(B)**\non correction of those problems, the operation can achieve, or be returned to, a sound financial basis.\n##### (c) No effect on subsidies\nIn carrying out this section, the Secretary shall ensure that the refinancing of guaranteed loans into direct loans has no impact on the subsidy rate of\u2014\n**(1)**\nloans guaranteed by the Farm Service Agency; or\n**(2)**\ndirect loans issued by the Farm Service Agency.\n##### (d) Loan programs\nIn making direct loans pursuant to the regulations promulgated under subsection (a), the Secretary may refinance a loan guaranteed under 1 program of the Farm Service Agency into a direct loan issued under another program of the Farm Service Agency, as the Secretary determines to be appropriate and in accordance with the laws applicable to the program under which the new direct loan is issued.\n##### (e) Maximum amount of direct refinancing loans\nA direct loan issued by the Farm Service Agency pursuant to the regulations promulgated under subsection (a) shall be subject to any otherwise applicable limitation on the maximum amount of a direct loan issued by the Farm Service Agency, including, if applicable, the limitations described in\u2014\n**(1)**\nsection 305 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925 ); and\n**(2)**\nsection 313 of that Act ( 7 U.S.C. 1943 ).\n#### 7. Sense of the Congress\nIt is the sense of the Congress that\u2014\n**(1)**\naccess to credit is essential to the success of farmers and ranchers; and\n**(2)**\nmicroloans, direct loans, and guaranteed loans provided by the Farm Service Agency should be fully funded to meet producer demand, help beginning farmers and ranchers, and support family farms.",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "899",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "type": "S"
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
        "updateDate": "2025-05-05T20:56:32Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1991ih.xml"
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
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to modify limitations on amounts of farm ownership loans and operating loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:44Z"
    }
  ]
}
```
