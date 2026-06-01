# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4780?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4780
- Title: USTRx Act
- Congress: 119
- Bill type: HR
- Bill number: 4780
- Origin chamber: House
- Introduced date: 2025-07-29
- Update date: 2026-04-21T08:06:25Z
- Update date including text: 2026-04-21T08:06:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-29: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-29: Introduced in House

## Actions

- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Introduced in House
- 2025-07-29 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-29",
    "latestAction": {
      "actionDate": "2025-07-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4780",
    "number": "4780",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "A000375",
        "district": "19",
        "firstName": "Jodey",
        "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
        "lastName": "Arrington",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "USTRx Act",
    "type": "HR",
    "updateDate": "2026-04-21T08:06:25Z",
    "updateDateIncludingText": "2026-04-21T08:06:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-29",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-29",
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
          "date": "2025-07-29T21:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "FL"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "TN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NY"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "NC"
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
      "sponsorshipDate": "2025-08-05",
      "state": "WV"
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
      "sponsorshipDate": "2026-03-27",
      "state": "IN"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4780ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4780\nIN THE HOUSE OF REPRESENTATIVES\nJuly 29, 2025 Mr. Arrington (for himself, Mr. Buchanan , Mr. Fleischmann , Ms. Tenney , and Mr. Murphy ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo identify and take action against international trade practices of high income countries that unfairly exploit innovation by deviating from market-based policies and unfairly exploit United States innovation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Use Sovereignty To reduce Rx Act or the USTRx Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nPharmaceutical price controls in foreign markets distort global trade flows and competition by depressing the prices of innovative drugs and exploiting pharmaceutical innovations researched and developed in the United States.\n**(2)**\nBy setting prices at levels that are not market-based, such price controls undervalue the discovery of new, innovative treatments, diminish opportunities and incentives for global innovation in new medicines, and threaten to restrict access to new treatments and cures for United States patients and consumers.\n**(3)**\nRecognizing these dynamics, it is critical that the United States use all available trade tools to address such free-riding to ensure that foreign government regulatory reimbursement regimes are transparent, provide procedural fairness, are non-discriminatory, and provide full market access to United States products.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nensuring the security of innovative and affordable healthcare is a top priority for Americans and for Congress;\n**(2)**\nforeign government policies that mandate artificially low drug prices in foreign markets undermine this priority by reducing global incentives to invest in the development of new medicines;\n**(3)**\nsuch exploitative behavior unfairly shifts the cost of developing new treatments to the United States and unduly relies on America\u2019s patients and taxpayers to finance global pharmaceutical innovation; and\n**(4)**\nsafeguarding access to life-saving treatments for American patients requires combating such behavior so that foreign countries pay their fair share of the costs associated with the development of new drugs.\n#### 3. Chief Pharmaceutical Trade Negotiator\n##### (a) Establishment\nSection 141(b) of the Trade Act of 1974 ( 19 U.S.C. 2171(b) ), is amended as follows:\n**(1)**\nIn paragraph (2)\u2014\n**(A)**\nin the first sentence, by inserting one Chief Pharmaceutical Trade Negotiator, after one Chief Agricultural Negotiator, ; and\n**(B)**\nby inserting the Chief Pharmaceutical Trade Negotiator, after the Chief Agricultural Negotiator, each place it appears.\n**(2)**\nBy adding at the end the following new paragraph:\n(7) The principal functions of the Chief Pharmaceutical Trade Negotiator shall be to conduct trade negotiations, enforce trade agreements relating to United States pharmaceutical products, and take appropriate action to address acts, policies, or practices of high-income countries that have a significant adverse impact on the ability of United States pharmaceutical manufacturers to enjoy full market access. The Chief Pharmaceutical Trade Negotiator shall be a vigorous advocate on behalf of United States manufacturers and consumers of pharmaceutical products and shall perform such other functions as the United States Trade Representative may direct. In carrying out such duties, the Chief Pharmaceutical Negotiator shall, as appropriate, consult or coordinate with the Chief Intellectual Property Negotiator. .\n##### (b) Annual report\n**(1) List of high-income countries**\nThe United States Trade Representative shall compile and annually update a list of each foreign country that is defined as high-income by the official statistics of the International Bank for Reconstruction and Development of the World Bank.\n**(2) Report required**\nWith respect to each country included on the most recent list required under paragraph (1), the United States Trade Representative, acting through the Chief Pharmaceutical Trade Negotiator, (as established pursuant to the amendments made by subsection (a)) shall annually submit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate and concurrently publish on a publicly available website of the United States Trade Representative a report that\u2014\n**(A)**\ndescribes in detail the results of a review of the acts, policies, and practices of such country relating to the trade in pharmaceutical products in the previous fiscal year;\n**(B)**\ndetermines whether such acts, policies, or practices\u2014\n**(i)**\nare not developed and implemented in a fair, nondiscriminatory, and transparent manner;\n**(ii)**\nare not market-based or do not appropriately recognize the value of innovative medicines;\n**(iii)**\ndeny reciprocal market access for United States products;\n**(iv)**\ndiminish incentives for innovation in a manner that delays, prevents, or otherwise adversely impacts the introduction of new medicines in the United States;\n**(v)**\nviolate or are inconsistent with the provisions of, or otherwise deny benefits to the United States under, any bilateral or multilateral trade agreement with such country; and\n**(vi)**\nare unjustifiable or impose a significant burden or unreasonable or discriminatory restriction on United States commerce with such country; and\n**(C)**\ndescribes the current status of any responsive actions taken by the United States with respect to acts, policies, or practices for which the United States Trade Representative has determined and included in any prior report, pursuant to subparagraph (B), that the interests of the United States are harmed, including responsive actions pursuant to title III of the Trade Act of 1974 ( 19 U.S.C. 2411 et seq. ).\n##### (c) Response to adverse actions\nNot later than 30 days after the United States Trade Representative determines that an act, policy, or practice of a country included in the applicable list required under subsection (b)(1) meets any of the criteria described in subsection (b)(2)(B), the United States Trade Representative shall submit to Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a plan to respond to such adverse action, which may include initiating an investigation under chapter 1 title III of the Trade Act of 1974 ( 19 U.S.C. 2411 et seq. ), in accordance with section 302(b)(1) of such chapter.",
      "versionDate": "2025-07-29",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T17:16:12Z"
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
      "date": "2025-07-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4780ih.xml"
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
      "title": "USTRx Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USTRx Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Use Sovereignty To reduce Rx Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To identify and take action against international trade practices of high income countries that unfairly exploit innovation by deviating from market-based policies and unfairly exploit United States innovation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:33Z"
    }
  ]
}
```
