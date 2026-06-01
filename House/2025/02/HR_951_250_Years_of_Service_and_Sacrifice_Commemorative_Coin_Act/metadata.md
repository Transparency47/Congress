# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/951?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/951
- Title: 250 Years of Service and Sacrifice Commemorative Coin Act
- Congress: 119
- Bill type: HR
- Bill number: 951
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-09-09T08:05:24Z
- Update date including text: 2025-09-09T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/951",
    "number": "951",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "250 Years of Service and Sacrifice Commemorative Coin Act",
    "type": "HR",
    "updateDate": "2025-09-09T08:05:24Z",
    "updateDateIncludingText": "2025-09-09T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:00:40Z",
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
      "bioguideId": "H001072",
      "district": "2",
      "firstName": "J.",
      "fullName": "Rep. Hill, J. French [R-AR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hill",
      "middleName": "French",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "AR"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NJ"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "OH"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "FL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "NJ"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "ID"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "OH"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr951ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 951\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Ms. Malliotakis (for herself, Mr. Hill of Arkansas , and Mrs. Watson Coleman ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of the Treasury to mint coins in commemoration of the continual recognition of the Nation\u2019s semiquincentennial by honoring over 250 years of Americans\u2019 service and sacrifice.\n#### 1. Short title\nThis Act may be cited as the 250 Years of Service and Sacrifice Commemorative Coin Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nJuly 4, 1776, marks the historic date when the unanimous Declaration of Independence was adopted, establishing the thirteen United States of America as a free and independent nation.\n**(2)**\nJuly 4, 2026, will commemorate the 250th anniversary of the Nation\u2019s declaration of independence.\n**(3)**\nIt is a long-standing tradition to honor significant milestones in American history through the minting of commemorative coins.\n**(4)**\nThe Stephen Siller Tunnel to Towers Foundation exemplifies the principles of service and sacrifice that have defined the Nation for more than 250 years by providing financial support, housing assistance, and educational opportunities to Gold Star families, first responders, veterans, and their families, honoring the bravery and dedication of those who serve.\n**(5)**\nFirst responders have played a vital role in safeguarding American lives and communities since the Nation\u2019s founding, dating back to the first publicly funded, paid fire department established in Boston in 1678.\n**(6)**\nDuring the Civil War (1861\u20131865), first responders, including battlefield medics and firefighters, played critical roles in saving lives and mitigating destruction, reinforcing their importance in times of national crisis.\n**(7)**\nGold Star families, who have made the ultimate sacrifice in service to the Nation, have endured profound loss while upholding the principles of freedom and democracy. Their resilience and dedication to honoring their fallen loved ones continue to inspire and strengthen communities across America.\n**(8)**\nFirst responders embody the ideals of life, liberty, and the pursuit of happiness by safeguarding lives and communities, representing a modern continuation of the sacrifices made during the fight for independence.\n**(9)**\nThe Stephen Siller Tunnel to Towers Foundation\u2019s mission ensures that the legacy of service and sacrifice is preserved and that those who dedicate their lives to protecting others are never forgotten.\n**(10)**\nThe issuance of this commemorative coin will raise awareness of the sacrifices made by Gold Star families, first responders, veterans, and their families, fostering a deeper understanding of their role in upholding the freedoms envisioned in the Declaration of Independence.\n**(11)**\nCongress has a long-standing tradition of authorizing commemorative coins to celebrate the Nation\u2019s history and the contributions of its citizens and organizations to preserving liberty and justice for all.\n**(12)**\nProceeds from the surcharges on the sale of these commemorative coins will directly benefit the Stephen Siller Tunnel to Towers Foundation, enabling the continuation of its impactful programs that support Gold Star families, first responders, veterans, and their families.\n#### 3. Coin specifications\n##### (a) Denominations\nThe Secretary of the Treasury (hereafter in this Act referred to as the Secretary ) shall mint and issue the following coins in continual recognition of the Nation\u2019s semiquincentennial by honoring over 250 years of Americans\u2019 service and sacrifice:\n**(1) $5.00 Gold Coins**\nNot more than 100,000 $5.00 coins, which shall\u2014\n**(A)**\nweigh 8.359 grams;\n**(B)**\nhave a diameter of 0.850 inches; and\n**(C)**\ncontain at least 90 percent gold.\n**(2) $1 Silver Coins**\nNot more than 500,000 $1 coins, which shall\u2014\n**(A)**\nweigh 26.73 grams;\n**(B)**\nhave a diameter of 1.500 inches; and\n**(C)**\ncontain not less than 90 percent silver.\n**(3) Half-dollar clad coins**\nNot more than 750,000 half dollar coins, which shall\u2014\n**(A)**\nweigh 11.34 grams;\n**(B)**\nhave a diameter of 1.205 inches; and\n**(C)**\nbe minted to the specifications for half-dollar coins, contained in section 5112(b) of title 31, United States Code.\n##### (b) Legal tender\nThe coins minted under this Act shall be legal tender, as provided in section 5103 of title 31, United States Code.\n##### (c) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all coins minted under this Act shall be considered to be numismatic items.\n##### (d) Mintage limit exception\nIf the Secretary determines, based on independent, market based research conducted by the designated recipient organization identified in section 7(b) that the mintage levels described under this subsection are not adequate to meet public demand, the Secretary may increase the mintage levels as the Secretary determines is necessary to meet public demand.\n#### 4. Designs of coins\n##### (a) Design requirements\n**(1) In general**\nThe designs of the coins minted under this Act shall be emblematic of over 250 years of American\u2019s service and sacrifice.\n**(2) Designation and inscriptions**\nOn each coin minted under this Act, there shall be\u2014\n**(A)**\na designation of the value of the coin;\n**(B)**\nan inscription of the year 2028 ; and\n**(C)**\ninscriptions of the words Liberty , In God We Trust , United States of America , and E Pluribus Unum .\n##### (b) Selection\nThe designs for the coins minted under this Act shall be\u2014\n**(1)**\nselected by the Secretary, after consultation with the Stephen Siller-Tunnel to Towers Foundation and the Commission of Fine Arts; and\n**(2)**\nreviewed by the Citizens Coinage Advisory Committee.\n#### 5. Issuance of coins\n##### (a) Quality of coins\nCoins minted under this Act shall be issued in uncirculated and proof qualities.\n##### (b) Period for issuance\nThe Secretary may issue coins under this Act only during the period beginning on January 1, 2028, and ending on December 31, 2028.\n#### 6. Sale of coins\n##### (a) Sale price\nThe coins issued under this Act shall be sold by the Secretary at a price equal to the sum of\u2014\n**(1)**\nthe face value of the coins;\n**(2)**\nthe surcharge provided in section 7(a) with respect to such coins; and\n**(3)**\nthe cost of designing and issuing the coins (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping).\n##### (b) Bulk sales\nThe Secretary shall make bulk sales of the coins issued under this Act at a reasonable discount.\n##### (c) Prepaid orders\n**(1) In general**\nThe Secretary shall accept prepaid orders for the coins minted under this Act before the issuance of such coins.\n**(2) Discount**\nSale prices with respect to prepaid orders under paragraph (1) shall be at a reasonable discount.\n#### 7. Surcharges\n##### (a) In general\nAll sales of coins issued under this Act shall include a surcharge as follows:\n**(1)**\nA surcharge of $35 per coin for the gold coins.\n**(2)**\nA surcharge of $10 per coin for the silver coins.\n**(3)**\nA surcharge of $5 per coin for the half-dollar coins.\n##### (b) Distribution\nAll surcharges received by the Secretary from the sale of coins issued under this Act shall be allocated to the Stephen Siller Tunnel to Towers Foundation to support programs that provide mortgage-free homes to Gold Star families, the families of first responders killed in the line of duty, scholarships for their children, resources for disaster response teams, and memorial projects honoring their service and sacrifice. These efforts serve as a living tribute to the enduring legacy of those who have safeguarded and advanced the ideals of the Declaration of Independence from its signing to the present day.\n##### (c) Audits\nThe Stephen Siller Tunnel to Towers Foundation shall be subject to the audit requirements of section 5134(f)(2) of title 31, United States Code, with regard to the amounts received under subsection (b).\n##### (d) Limitation\nNotwithstanding subsection (a), no surcharge may be included with respect to the issuance under this Act of any coin during a calendar year if, as of the time of such issuance, the issuance of such coin would result in the number of commemorative coin programs issued during such year to exceed the annual 2 commemorative coin program issuance limitation under section 5112(m)(1) of title 31, United States Code. The Secretary of the Treasury may issue guidance to carry out this subsection.\n#### 8. Financial assurances\nThe Secretary shall take such actions as may be necessary to ensure that\u2014\n**(1)**\nminting and issuing coins under this Act will not result in any net cost to the United States Government; and\n**(2)**\nno funds, including applicable surcharges, shall be disbursed to any recipient designated in section 7(b) until the total cost of designing and issuing all of the coins authorized by this Act (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping) is recovered by the United States Treasury, consistent with sections 5112(m) and 5134(f) of title 31, United States Code.",
      "versionDate": "2025-02-04",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-07T12:57:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr951",
          "measure-number": "951",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr951v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>250 Years of Service and Sacrifice Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition of the United States\u2019\u00a0semiquincentennial.</p><p>All surcharges received by Treasury from the sale of such coins must be paid to the Stephen\u00a0Siller Tunnel to Towers Foundation.</p>"
        },
        "title": "250 Years of Service and Sacrifice Commemorative Coin Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr951.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>250 Years of Service and Sacrifice Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition of the United States\u2019\u00a0semiquincentennial.</p><p>All surcharges received by Treasury from the sale of such coins must be paid to the Stephen\u00a0Siller Tunnel to Towers Foundation.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr951"
    },
    "title": "250 Years of Service and Sacrifice Commemorative Coin Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>250 Years of Service and Sacrifice Commemorative Coin Act</strong></p><p>This bill directs the Department of the Treasury to mint and issue coins in recognition of the United States\u2019\u00a0semiquincentennial.</p><p>All surcharges received by Treasury from the sale of such coins must be paid to the Stephen\u00a0Siller Tunnel to Towers Foundation.</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119hr951"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr951ih.xml"
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
      "title": "250 Years of Service and Sacrifice Commemorative Coin Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:09Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "250 Years of Service and Sacrifice Commemorative Coin Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of the Treasury to mint coins in commemoration of the continual recognition of the Nation's semiquincentennial by honoring over 250 years of Americans' service and sacrifice.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:17Z"
    }
  ]
}
```
