# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/899?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/899
- Title: Producer and Agricultural Credit Enhancement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 899
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2025-12-05T21:59:45Z
- Update date including text: 2025-12-05T21:59:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/899",
    "number": "899",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001061",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hoeven, John [R-ND]",
        "lastName": "Hoeven",
        "party": "R",
        "state": "ND"
      }
    ],
    "title": "Producer and Agricultural Credit Enhancement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:59:45Z",
    "updateDateIncludingText": "2025-12-05T21:59:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T20:28:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "MN"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s899is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 899\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Hoeven (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to modify limitations on amounts of farm ownership loans and operating loans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Producer and Agricultural Credit Enhancement Act of 2025 .\n#### 2. Limitations on loan amounts\n##### (a) Limitations on amount of farm ownership loans\nSection 305(a)(2) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925(a)(2) ) is amended by striking $600,000, or, in the case of a loan guaranteed by the Secretary, $1,750,000 (increased, beginning with fiscal year 2019 and inserting $850,000, or, in the case of a loan guaranteed by the Secretary, $3,000,000 (increased, beginning with fiscal year 2025 .\n##### (b) Limitations on amount of operating loans\nSection 313(a)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1943(a)(1) ) is amended by striking $400,000, or, in the case of a loan guaranteed by the Secretary, $1,750,000 (increased, beginning with fiscal year 2019 and inserting $750,000, or, in the case of a loan guaranteed by the Secretary, $2,600,000 (increased, beginning with fiscal year 2025 .\n#### 3. Inflation percentage\nSection 305(c) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925(c) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking of the Prices Paid By Farmers Index (as compiled by the National Agricultural Statistics Service of the Department of Agriculture) for the 12-month period ending on July 31 of the immediately preceding fiscal year and inserting of the per acre average United States farm real estate value, the per acre average United States cropland value, and the per acre average United States pasture value for the preceding year (as published in the applicable Agricultural Land Values report of the National Agricultural Statistics Service of the Department of Agriculture), weighted equally ; and\n**(2)**\nin paragraph (2), by striking of such index (as so defined) for the 12-month period that immediately precedes the 12-month period described in paragraph (1) and inserting of the per acre average United States farm real estate value, the per acre average United States cropland value, and the per acre average United States pasture value for the year immediately preceding the year described in paragraph (1) (as so published), weighted equally .\n#### 4. Down payment loan program\nSection 310E(b)(1) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1935(b)(1) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking exceed 45 percent of the least and inserting exceed, subject to section 305(a), 45 percent of the lesser ;\n**(2)**\nin subparagraph (A), by adding or after the semicolon;\n**(3)**\nin subparagraph (B), by striking ; or and inserting a period; and\n**(4)**\nby striking subparagraph (C).\n#### 5. Limitation on microloan amounts\nSection 313(c)(2) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1943(c)(2) ) is amended by striking $50,000 and inserting $100,000 .\n#### 6. Refinancing of guaranteed loans into direct loans\n##### (a) In general\nNot later than 1 year after the date of enactment of this Act, the Secretary of Agriculture, acting through the Administrator of the Farm Service Agency (referred to in this section as the Secretary ), shall promulgate regulations allowing certain loans guaranteed by the Farm Service Agency to be refinanced into direct loans issued by the Farm Service Agency, in accordance with this section.\n##### (b) Requirements\n**(1) In general**\nThe regulations promulgated under subsection (a) shall provide that a guaranteed loan described in that subsection may be refinanced into a direct loan described in that subsection only if the Secretary determines that\u2014\n**(A)**\nthe guaranteed loan is distressed;\n**(B)**\nthe borrower on that guaranteed loan has attempted to work with the lender and has been unsuccessful;\n**(C)**\na reasonable chance for the success of the operation financed by the guaranteed loan exists; and\n**(D)**\nall other criteria established by the Secretary for purposes of this section to protect taxpayer funds and the loan programs of the Farm Service Agency have been satisfied.\n**(2) Reasonable chance of success**\nFor purposes of paragraph (1)(C), the Secretary may determine that a reasonable chance for the success of an operation exists if the Secretary determines that\u2014\n**(A)**\nall relevant problems with the operation financed by the guaranteed loan\u2014\n**(i)**\nhave been identified; and\n**(ii)**\ncan be corrected; and\n**(B)**\non correction of those problems, the operation can achieve, or be returned to, a sound financial basis.\n##### (c) No effect on subsidies\nIn carrying out this section, the Secretary shall ensure that the refinancing of guaranteed loans into direct loans has no impact on the subsidy rate of\u2014\n**(1)**\nloans guaranteed by the Farm Service Agency; or\n**(2)**\ndirect loans issued by the Farm Service Agency.\n##### (d) Loan programs\nIn making direct loans pursuant to the regulations promulgated under subsection (a), the Secretary may refinance a loan guaranteed under 1 program of the Farm Service Agency into a direct loan issued under another program of the Farm Service Agency, as the Secretary determines to be appropriate and in accordance with the laws applicable to the program under which the new direct loan is issued.\n##### (e) Maximum amount of direct refinancing loans\nA direct loan issued by the Farm Service Agency pursuant to the regulations promulgated under subsection (a) shall be subject to any otherwise applicable limitation on the maximum amount of a direct loan issued by the Farm Service Agency, including, if applicable, the limitations described in\u2014\n**(1)**\nsection 305 of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1925 ); and\n**(2)**\nsection 313 of that Act ( 7 U.S.C. 1943 ).\n#### 7. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\naccess to credit is essential to the success of farmers and ranchers; and\n**(2)**\nmicroloans, direct loans, and guaranteed loans provided by the Farm Service Agency should be fully funded to meet producer demand, help beginning farmers and ranchers, and support family farms.",
      "versionDate": "2025-03-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-04",
        "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit."
      },
      "number": "1991",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-05-05T20:54:26Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s899is.xml"
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
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consolidated Farm and Rural Development Act to modify limitations on amounts of farm ownership loans and operating loans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Producer and Agricultural Credit Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
