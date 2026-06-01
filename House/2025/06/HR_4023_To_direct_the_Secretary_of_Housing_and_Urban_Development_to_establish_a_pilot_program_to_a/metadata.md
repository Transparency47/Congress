# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4023?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4023
- Title: American Dream for All Act
- Congress: 119
- Bill type: HR
- Bill number: 4023
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-04-21T08:06:16Z
- Update date including text: 2026-04-21T08:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4023",
    "number": "4023",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "American Dream for All Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:16Z",
    "updateDateIncludingText": "2026-04-21T08:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:30Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "DC"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4023ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4023\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Carbajal introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Secretary of Housing and Urban Development to establish a pilot program to award grants to States, territories, and Indian tribes to provide down payment assistance loans to certain borrowers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the American Dream for All Act .\n#### 2. Appreciation sharing down payment loan pilot program\n##### (a) In general\nNot later than 1 year after the date of the enactment of this section, the Secretary of Housing and Urban Development (hereafter referred to as the Secretary ) shall establish a pilot program to award capitalization grants to eligible entities.\n##### (b) Eligible entity\nTo be eligible to receive a grant under this section, an entity shall\u2014\n**(1)**\nbe an agency of a State or Indian tribe, or instrumentality thereof, including a State or Indian tribe housing finance agency; and\n**(2)**\nhave or establish a revolving loan fund (hereafter referred to a State loan fund ) for the purpose of providing down payment assistance loans.\n##### (c) Determination of amount\nThe Secretary shall award grants under this section in amounts that are proportional to the population of the State or Indian tribe in which the grant amounts are directed, as determined by the Secretary.\n##### (d) Use of funds\n**(1) In general**\nAn eligible entity that is awarded a grant under this section\u2014\n**(A)**\nshall deposit such grant amounts into the State loan fund of such eligible entity;\n**(B)**\nshall provide down payment assistance loans with such grant amounts from the State loan fund to eligible borrowers in an amount that is\u2014\n**(i)**\nnot more than 20 percent of the purchase price of the home; and\n**(ii)**\nnot less than 3 percent of the purchase price of the home;\n**(C)**\nshall distribute such assistance loans to eligible borrowers\u2014\n**(i)**\non a first-come, first-serve basis; or\n**(ii)**\nby lottery option;\n**(D)**\nmay not use more than 15 percent of such grant amounts for administrative costs; and\n**(E)**\nmay determine any additional requirements for eligible borrowers with respect to the first mortgage of the home.\n**(2) Distribution of loans**\nAn eligible entity that distributes down payment assistance loans with amounts provided under this section may\u2014\n**(A)**\ndistribute such assistance loan to an eligible borrower prior to the purchase of a home; and\n**(B)**\nprovide the eligible borrower with\u2014\n**(i)**\na certain time period to locate a home and enter a purchase sale contract, as determined by the eligible entity based on market conditions; and\n**(ii)**\nthe option to renew the loan offer, one time, as determined by the eligible entity.\n##### (e) Terms and limitations\n**(1) Repayment**\n**(A) Repayment from borrower**\nAn eligible borrower that receives a down payment assistance loan with amounts provided under this section shall, upon the sale of the home purchased with the assistance of such loan, repay such assistance loan to the eligible entity that distributed such assistance loan in an amount that is equal to\u2014\n**(i)**\nwith respect to a home that appreciates in value\u2014\n**(I)**\nthe amount of such loan; and\n**(II)**\nthe amount that is equal to the percentage of such loan of the purchase price of the home multiplied by the amount of appreciation of the home; or\n**(ii)**\nwith respect to a home that depreciates in value, the amount of such loan.\n**(B Return to State loan fund**\nAn eligible entity that receives repayment under subparagraph (A) shall return the amounts from the repayment back into the State loan fund, to be redistributed as a down payment assistance loan as described in this section.\n**(2) Maximum loan amount**\n**(A) In general**\nThe maximum loan amount provided to an eligible borrower shall be\u2014\n**(i)**\n$150,000 in a high-cost State or Indian tribe;\n**(ii)**\n$100,000 in a medium-cost State or Indian tribe; and\n**(iii)**\n$50,000 in a low-cost State or Indian tribe.\n**(B) Classification**\nAnnually, the Secretary, in consultation with the eligible entity in each State or Indian tribe that is awarded a grant under this section\u2014\n**(i)**\nshall determine the cost-category described in subparagraph (A) of such State or Indian tribe; and\n**(ii)**\nshall increase or decrease the maximum loan amounts described in subparagraph (A) based on the consumer price index.\n##### (f) Reports\n**(1) Reports to the Secretary**\nAn eligible entity that is awarded a grant under this section shall submit to the Secretary a report, on an annual basis or as determined appropriate by the Secretary, that includes\u2014\n**(A)**\nthe number of down payment assistance loans distributed using such grant amounts;\n**(B)**\nthe number of home sales processed using down payment assistance loans;\n**(C)**\nthe amount of each down payment assistance loan distributed; and\n**(D)**\nany other data as determined appropriate by the Secretary.\n**(2) Report to the Congress**\nNot later than 1 year after the pilot program has been established, the Secretary shall submit to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate a report with respect to the implementation of the pilot program.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary such sums as may be necessary for each of fiscal years 2026 through 2030 to carry out this section.\n##### (h) Definitions\nIn this section:\n**(1) Eligible borrower**\nThe term eligible borrower means an individual that\u2014\n**(A)**\nis a citizen or permanent resident of the United States;\n**(B)**\nis a first-time homebuyer or a first-generation homebuyer;\n**(C)**\nhas completed a homebuyer education course, as determined appropriate by the Secretary, including individual counseling;\n**(D)**\nhas a certificate of completion from a Housing Counseling Agency approved by the Secretary;\n**(E)**\nhas an income that is not more than 150 percent of the area median income; and\n**(F)**\nby self-attestation, does not have the ability to pay more than 5 percent of the total value of the home for which a loan under this section is used.\n**(2) First-time homebuyer**\nThe term first-time homebuyer has the meaning given the term in section 104 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12704 ), except that for the purposes of this section the reference in such section 104 to title II shall be considered to refer to this section, and except that ownership of heir property shall not be treated as owning a home for purposes of determining whether a borrower qualifies as a first-time homebuyer.\n**(3) First-generation homebuyer**\nThe term first-generation homebuyer means a homebuyer who is, as self-attested by the homebuyer\u2014\n**(A)**\nan individual\u2014\n**(i)**\nwhose parents or legal guardians do not, or did not at the time of their death, to the best of the individual\u2019s knowledge, have any present ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel; and\n**(ii)**\nwhose spouse or domestic partner has not, during the 3-year period ending upon acquisition of the eligible home to be acquired using such assistance, had any present ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel, whether the individual is a co-borrower on the loan or not; or\n**(B)**\nan individual who has at any time been placed in foster care or institutional care whose spouse or domestic partner has not, during the 3-year period ending upon acquisition of the eligible home to be acquired using such assistance, had any ownership interest in a residence in any State, excluding ownership of heir property or ownership of chattel, whether such individual is a co-borrower on the loan or not.\n**(4) Indian tribe**\nThe term Indian tribe has the meaning given the term in section 248(i) of the National Housing Act ( 12 U.S.C. 1715z\u201313(i) ).\n**(5) State**\nThe term State has the meaning given the term in section 201(d) of the National Housing Act ( 12 U.S.C. 1707 ).",
      "versionDate": "2025-06-17",
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
        "updateDate": "2025-07-11T12:06:35Z"
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
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4023ih.xml"
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
      "title": "American Dream for All Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Dream for All Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-27T11:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Housing and Urban Development to establish a pilot program to award grants to States, territories, and Indian tribes to provide down payment assistance loans to certain borrowers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-27T11:18:24Z"
    }
  ]
}
```
