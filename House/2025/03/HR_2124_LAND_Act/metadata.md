# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2124?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2124
- Title: LAND Act
- Congress: 119
- Bill type: HR
- Bill number: 2124
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-04-16T08:06:51Z
- Update date including text: 2026-04-16T08:06:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2124",
    "number": "2124",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000603",
        "district": "26",
        "firstName": "Brandon",
        "fullName": "Rep. Gill, Brandon [R-TX-26]",
        "lastName": "Gill",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LAND Act",
    "type": "HR",
    "updateDate": "2026-04-16T08:06:51Z",
    "updateDateIncludingText": "2026-04-16T08:06:51Z"
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
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:06:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:13:35Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "bioguideId": "B001317",
      "district": "2",
      "firstName": "Josh",
      "fullName": "Rep. Brecheen, Josh [R-OK-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Brecheen",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OK"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "LA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "IN"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WV"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "AZ"
    },
    {
      "bioguideId": "H001102",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Harris, Mark [R-NC-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "NC"
    },
    {
      "bioguideId": "F000485",
      "district": "14",
      "firstName": "Clay",
      "fullName": "Rep. Fuller, Clay [R-GA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Fuller",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2124ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2124\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Gill of Texas (for himself, Mr. Brecheen , Mr. Higgins of Louisiana , Ms. Greene of Georgia , and Mr. Stutzman ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require that a foreign purchaser of agricultural land be subject to the same restrictions as are applicable to United States citizens and nationals in the home country of such foreign purchaser.\n#### 1. Short title\nThis Act may be cited as the Land And National Defense Act or the LAND Act .\n#### 2. Restrictions on foreign purchasers\n##### (a) In general\nIn the case of a sale of agricultural land, a foreign purchaser of such land shall be subject to\u2014\n**(1)**\nthe same restrictions and limitations as a United States citizen or national would be subject to with respect to the purchase of agricultural land in the home country of such purchaser; and\n**(2)**\nany restrictions and limitations under State law that apply with respect to the purchase of agricultural land in the State involved.\n##### (b) Determination of home countries of foreign purchasers\n**(1) United States citizens**\n**(A) Dual citizen**\nFor purposes of applying subsection (a), in the case of a foreign purchaser who is a citizen of the United States and 1 other country, the other country shall be treated as the home country of such purchaser.\n**(B) Multiple citizenship**\nFor purposes of applying subsection (a), in the case of a foreign purchaser who is a citizen of the United States and more than 1 other country, the other country (other than the United States) with the most restrictive laws with respect to the purchasing of agricultural land, as determined by the Task Force, shall be treated as the home country of such purchaser.\n**(2) Non-United States citizens**\n**(A) In general**\nFor purposes of applying subsection (a), in the case of a foreign purchaser who is a not a United States citizen and is a citizen of 1 country, the country in which such purchaser is a citizen shall be treated as the home country of such purchaser.\n**(B) Multiple citizenship**\nFor purposes of applying subsection (a), in the case of a foreign purchaser who is a not a United States citizen and is a citizen of more than 1 country, the country with the most restrictive laws with respect to the purchasing of agricultural land, as determined by the Task Force, shall be treated as the home country of such purchaser.\n**(3) Companies**\nFor purposes of applying subsection (a), in the case of a foreign purchaser that is a company, the country with the most restrictive laws with respect to the purchasing of agricultural land, as determined by the Task Force, and of which the citizens of such country hold at least 5 percent of such company shall be treated as the home country of such purchaser.\n**(4) Foreign governments**\nFor purposes of applying subsection (a), in the case of a foreign purchaser that is a foreign government, the country such government represents shall be treated as the home country of such purchaser.\n##### (c) Notification\n**(1) In general**\nIn the case of a sale of agricultural land to a foreign purchaser, the seller of such agricultural land shall report such sale to the Secretary of Agriculture.\n**(2) Congressional notification**\nWith respect to each notification of a sale of agricultural land to a foreign purchaser under paragraph (1), the Secretary of Agriculture shall notify\u2014\n**(A)**\nthe members of the Senate from the State in which the agricultural land is located; and\n**(B)**\nthe member from the Congressional District in which such agricultural land is located.\n##### (d) Task Force\n**(1) In general**\nThere is established a Task Force (to be known as U.S. Land Protection Task Force ) to identify violations of subsection (a).\n**(2) Membership**\nThe Task Force shall be composed of the following:\n**(A)**\nThe Secretary of Agriculture, who shall serve as Chair of the Task Force.\n**(B)**\nThe Committee on Foreign Investment in the United States.\n**(C)**\nThe National Security Division of the Department of Justice.\n**(D)**\nThe Secretary of State.\n**(3) Reports**\nNot later than 1 year after the date of the enactment of this Act and every 6 months thereafter, the Task Force shall submit to Congress a report that includes with respect to the 6-month period preceding the report\u2014\n**(A)**\nthe percentage of agricultural land (disaggregated by land type) that was sold to foreign purchasers;\n**(B)**\nthe States in which such land was sold;\n**(C)**\nthe average purchase cost of such land;\n**(D)**\nwith respect to each such purchase of agricultural land, the title history with respect to the agricultural land purchased; and\n**(E)**\nwhether any of the purchased agricultural land is located within 100 miles of a military installation.\n##### (e) Severability\nIf any provision of this Act (or the application of that provision to particular persons or circumstances) is held invalid or found to be unconstitutional, the remainder of this Act (or the application of that provision to other persons or circumstances) shall not be affected.\n##### (f) Definitions\nIn this section:\n**(1) Agricultural land**\nThe term agricultural land has the meaning given the term in section 9 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508 ).\n**(2) Foreign purchaser**\nThe term foreign purchaser means\u2014\n**(A)**\na foreign person (as defined in section 9 of the Agricultural Foreign Investment Disclosure Act of 1978 ( 7 U.S.C. 3508 )); and\n**(B)**\na United States citizen who is a citizen of another country.",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-05-14T13:02:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2124",
          "measure-number": "2124",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-08-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2124v00",
            "update-date": "2025-08-12"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Land And National Defense Act or the LAND Act</strong></p><p>This bill requires that a foreign purchaser of agricultural land be subject to (1) the same restrictions and limitations as a U.S. citizen or national would be subject to when purchasing agricultural land in the foreign purchaser's home country, and (2) any restrictions and limitations that apply under state law with respect to the purchase.</p><p>The bill applies to all foreign purchasers, including U.S. citizens who are also a citizen of one or more other countries (e.g., a dual citizen).</p><p>For a foreign company purchasing agricultural land, a country is treated as the company's home country if (1) it has the most restrictive laws with respect to the purchasing of agricultural land, and (2) the citizens of the country hold at least 5% of the company.</p><p>The seller of the agricultural land to a foreign purchaser must report the sale to the Department of Agriculture (USDA). Further, USDA must\u00a0notify certain\u00a0Members of Congress of the sale, including\u00a0(1) the Senators from the state in which the agricultural land is located, and (2) the Representative from the congressional district where the land is located.</p><p>In addition, the bill establishes the U.S. Land Protection Task Force, chaired by the Secretary of Agriculture, to identify violations of these restrictions on foreign agricultural land purchasers.</p><p>The task force must submit a report to Congress every six months, which must include specific information on the sale of agricultural land to foreign purchasers.</p>"
        },
        "title": "LAND Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2124.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Land And National Defense Act or the LAND Act</strong></p><p>This bill requires that a foreign purchaser of agricultural land be subject to (1) the same restrictions and limitations as a U.S. citizen or national would be subject to when purchasing agricultural land in the foreign purchaser's home country, and (2) any restrictions and limitations that apply under state law with respect to the purchase.</p><p>The bill applies to all foreign purchasers, including U.S. citizens who are also a citizen of one or more other countries (e.g., a dual citizen).</p><p>For a foreign company purchasing agricultural land, a country is treated as the company's home country if (1) it has the most restrictive laws with respect to the purchasing of agricultural land, and (2) the citizens of the country hold at least 5% of the company.</p><p>The seller of the agricultural land to a foreign purchaser must report the sale to the Department of Agriculture (USDA). Further, USDA must\u00a0notify certain\u00a0Members of Congress of the sale, including\u00a0(1) the Senators from the state in which the agricultural land is located, and (2) the Representative from the congressional district where the land is located.</p><p>In addition, the bill establishes the U.S. Land Protection Task Force, chaired by the Secretary of Agriculture, to identify violations of these restrictions on foreign agricultural land purchasers.</p><p>The task force must submit a report to Congress every six months, which must include specific information on the sale of agricultural land to foreign purchasers.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr2124"
    },
    "title": "LAND Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Land And National Defense Act or the LAND Act</strong></p><p>This bill requires that a foreign purchaser of agricultural land be subject to (1) the same restrictions and limitations as a U.S. citizen or national would be subject to when purchasing agricultural land in the foreign purchaser's home country, and (2) any restrictions and limitations that apply under state law with respect to the purchase.</p><p>The bill applies to all foreign purchasers, including U.S. citizens who are also a citizen of one or more other countries (e.g., a dual citizen).</p><p>For a foreign company purchasing agricultural land, a country is treated as the company's home country if (1) it has the most restrictive laws with respect to the purchasing of agricultural land, and (2) the citizens of the country hold at least 5% of the company.</p><p>The seller of the agricultural land to a foreign purchaser must report the sale to the Department of Agriculture (USDA). Further, USDA must\u00a0notify certain\u00a0Members of Congress of the sale, including\u00a0(1) the Senators from the state in which the agricultural land is located, and (2) the Representative from the congressional district where the land is located.</p><p>In addition, the bill establishes the U.S. Land Protection Task Force, chaired by the Secretary of Agriculture, to identify violations of these restrictions on foreign agricultural land purchasers.</p><p>The task force must submit a report to Congress every six months, which must include specific information on the sale of agricultural land to foreign purchasers.</p>",
      "updateDate": "2025-08-12",
      "versionCode": "id119hr2124"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2124ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that a foreign purchaser of agricultural land be subject to the same restrictions as are applicable to United States citizens and nationals in the home country of such foreign purchaser.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-03T13:33:30Z"
    },
    {
      "title": "LAND Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LAND Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Land And National Defense Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-03T13:23:20Z"
    }
  ]
}
```
