# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/743?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/743
- Title: Ag Disputes Act
- Congress: 119
- Bill type: S
- Bill number: 743
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2026-04-30T11:03:19Z
- Update date including text: 2026-04-30T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/743",
    "number": "743",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Ag Disputes Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:19Z",
    "updateDateIncludingText": "2026-04-30T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
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
        "item": [
          {
            "date": "2025-02-26T16:50:01Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-26T16:50:01Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "MS"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AR"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "IA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "AL"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s743is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 743\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Cassidy (for himself, Mrs. Hyde-Smith , Mr. Boozman , Ms. Ernst , and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the establishment of a joint task force to identify and eliminate barriers to agriculture exports of the United States.\n#### 1. Short title\nThis Act may be cited as the Prioritizing Offensive Agricultural Disputes and Enforcement Act or the Ag Disputes Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAgricultural competitiveness through access to international markets is a vital part of the economy of the United States.\n**(2)**\nA healthy, well-functioning, rules-based trading system is the basis for the success of agriculture exports of the United States.\n**(3)**\nWhen foreign governments erect trade barriers, that makes it difficult for agricultural exporters in the United States to compete in the global marketplace and undermines the rules-based trading system.\n**(4)**\nThose trade barriers can harm farmers, ranchers, workers, and businesses in the United States and can also lead to higher prices for consumers and a less resilient international trading system.\n**(5)**\nDispute settlement is available to the President through trade agreements with 163 countries, and there are protectionist trade barriers to agriculture exports of the United States in many of those countries.\n**(6)**\nMany of those barriers are systemically important. For example, the use by the Government of India of unrestrained price support programs violates the commitments by that government under the World Trade Organization.\n**(7)**\nThe Government of India recognizes that its price support programs violate its commitments under the World Trade Organization, so instead of reforming its programs, it has repeatedly demanded an exemption from disputes for those programs. Moreover, the Government of India has tried to prevent discussions at the World Trade Organization of any other significant agricultural trade issue unless it gets a permanent exemption from disputes for those programs.\n**(8)**\nThe Government of India has repeatedly raised its minimum price supports, which has had negative effects on several commodity markets and most notably has led to its dominance of the global rice trade, with a 40-percent share of the global market since marketing year 2020 through 2021. India is also the world's largest producer of pulses and second largest producer of wheat, peanuts, and cotton.\n**(9)**\nThe United States Trade Representative submitted a counter notification at the World Trade Organization in 2023 showing that price supports by the Government of India for rice increased from 78.6 percent of the value of production in marketing year 2014 through 2015 to 93.9 percent of the value of production in marketing year 2020 through 2021, compared to the limit at the World Trade Organization on increased price supports of 10 percent of the value of production. That counter notification also showed price supports by the Government of India for wheat increasing from 77.7 percent to 81.3 percent during the same period. Previous counter notifications have shown similar violations by the Government of India for other commodities. For example, in the marketing year 2016 through 2017, price supports by the Government of Indian were 67.9 percent for cotton, 31.7 percent for chickpeas, 41 percent for lentils, and 47.4 percent for pulses overall.\n**(10)**\nMinor attempts to reform the agriculture subsidy system in India in marketing year 2020 through 2021 failed to produce results. Reforms enacted as a result of those attempts would not have changed the policies that violate commitments under the World Trade Organization, but would have merely provided farmers in India with opportunities to sell their products outside of the government-run mandi system, but those reforms were ultimately repealed.\n**(11)**\nDispute settlement is an effective way to provide a neutral assessment of compliance with terms of trade agreements and empower internal reformers who recognize a problem but have not been able to overcome entrenched resistance.\n**(12)**\nGlobal agriculture is uniquely susceptible to trade barriers and requires special attention to resolve myriad systemic and economically significant trade violations that impede the development of a resilient, sustainable, and rules-based agricultural trading system.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe President should accelerate efforts to address foreign trade barriers that harm agriculture exports of the United States;\n**(2)**\nthe United States Trade Representative and the Secretary of Agriculture both have a critical role in developing agricultural trade disputes;\n**(3)**\nCongress and the private sector have key roles to play in the development of disputes and agricultural trade enforcement strategy;\n**(4)**\nin the case of price supports by the Government of India, the President has exhausted other options available through the World Trade Organization short of requesting consultations under the Dispute Settlement Understanding of the World Trade Organization;\n**(5)**\nthere should be a plan and definitive deadlines in place for a request for consultations and establishment of a panel under the Dispute Settlement Understanding;\n**(6)**\nthe United States Trade Representative and the Secretary of Agriculture, in consultation with Congress and the private sector, should jointly develop a proactive enforcement strategy for addressing systemic and economically significant trade barriers in the agriculture sector; and\n**(7)**\nthe Office of the United States Trade Representative is the lead agency for trade policy of the United States.\n#### 4. Agricultural Trade Enforcement Task Force\n##### (a) Establishment\nNot later than 30 days after the date of the enactment of this Act, the President shall establish a joint task force to be known as the Agricultural Trade Enforcement Task Force (in this section referred to as the Task Force ).\n##### (b) Membership\nThe Task Force shall be comprised of the following members:\n**(1)**\nEmployees of the Foreign Agricultural Service of the Department of Agriculture, who shall be appointed by the Under Secretary of Agriculture for Trade and Foreign Agricultural Affairs.\n**(2)**\nEmployees of the Office of the United States Trade Representative, who shall\u2014\n**(A)**\nbe appointed by the General Counsel and the Chief Agricultural Negotiator; and\n**(B)**\nhave appropriate expertise in agricultural trade policy and trade enforcement.\n**(3)**\nEmployees from other Federal agencies as determined by the United States Trade Representative or the Secretary of Agriculture.\n##### (c) Duties\n**(1) In general**\nThe Task Force shall\u2014\n**(A)**\nidentify trade barriers to agriculture exports of the United States that are vulnerable to dispute settlement under the World Trade Organization or other trade agreements to which the United States is a party;\n**(B)**\ndevelop and implement a strategy for enforcing violations of trade agreements related to those trade barriers;\n**(C)**\nidentify like-minded trading partners that could act as co-complainants or primary complainants on disputes relating to specific trade barriers that are systemically or economically important to the United States; and\n**(D)**\nreport to Congress pursuant to subsection (d).\n**(2) Consultation**\nIn carrying out the duties under paragraph (1), the Task Force shall regularly consult, to the extent necessary and appropriate, with the following:\n**(A)**\nRelevant stakeholders in the private sector, including the agricultural trade advisory committees.\n**(B)**\nFederal agencies that are not represented on the Task Force.\n**(C)**\nLike-minded trading partners that are similarly concerned with trade barriers and are potential participants in a dispute settlement process.\n##### (d) Reports\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, and not less frequently than quarterly thereafter, the Task Force shall submit to Congress a report on the progress of the Task Force in identifying and addressing trade barriers to agriculture exports of the United States.\n**(2) Elements**\nEach report submitted under paragraph (1) shall include the following:\n**(A)**\nThe systemic and economically significant trade barriers that have been identified by the Task Force.\n**(B)**\nA justification for including those trade barriers in the report.\n**(C)**\nThe progress that has been made in developing dispute settlement cases and an assessment of whether further information is required.\n**(D)**\nThe current status of ongoing disputes and the implementation of panel decisions, arbitration decisions, or decisions by the Appellate Body of the World Trade Organization.\n**(3) Confidential information**\n**(A) In general**\nThe Task Force shall remove from each report submitted under paragraph (1) any information determined by the Task Force to be confidential.\n**(B) Briefing**\nFor each report required to be submitted under paragraph (1), the United States Trade Representative and the Secretary of Agriculture shall provide to members of Congress, congressional staff, and cleared advisors a briefing on the information determined by the Task Force to be confidential and removed from the report pursuant to subparagraph (A).\n##### (e) Consultations with India\n**(1) In general**\nThe Task Force shall include as part of the first report required under subsection (d)(1) a plan for filing a request for consultations under the World Trade Organization with respect to the price supports implemented by the Government of India with respect to agricultural products, which shall include other members of the World Trade Organization that have been identified and approached as potential co-complainants.\n**(2) Elements**\nThe plan required under paragraph (1) shall include\u2014\n**(A)**\nspecific claims that the United States Trade Representative intends to make during the consultations requested pursuant to the plan; and\n**(B)**\na timeline for\u2014\n**(i)**\nrequesting those consultations; and\n**(ii)**\nrequesting the establishment of a panel under the World Trade Organization in the event that the Government of India fails to provide a satisfactory path to compliance by the date that is 60 days after the date of receipt of the request for consultations.",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in Senate"
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
            "name": "Advisory bodies",
            "updateDate": "2025-07-24T17:59:56Z"
          },
          {
            "name": "Agricultural trade",
            "updateDate": "2025-07-24T17:59:53Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-07-24T18:00:07Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-07-24T18:00:14Z"
          },
          {
            "name": "Free trade and trade barriers",
            "updateDate": "2025-07-24T17:59:47Z"
          },
          {
            "name": "India",
            "updateDate": "2025-07-24T18:00:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-07-03T23:00:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s743",
          "measure-number": "743",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-07-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s743v00",
            "update-date": "2025-07-08"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Prioritizing Offensive Agricultural Disputes and Enforcement Act or the Ag Disputes Act</strong></p><p>This bill establishes a joint task force to identify and address trade barriers to U.S.\u00a0agricultural exports.</p><p>Specifically, the bill directs the President to establish the Agricultural Trade Enforcement Task Force. Members of this task force include employees of the Department of Agriculture's Foreign Agricultural Service and the Office of the U.S. Trade Representative.</p><p>The bill requires the task force to (1) identify trade barriers to U.S. agricultural exports that are vulnerable to dispute settlement under the World Trade Organization (WTO) or other trade agreements to which the United States is a party, (2) develop and implement a strategy for enforcing violations of trade agreements related to those trade barriers, (3) identify like-minded trading partners that could act as complainants on disputes relating to specific trade barriers that are systemically or economically important to the United States, and (4) submit periodic reports to Congress.</p><p>In its first report, the task force must include a plan for filing a request for consultations under the WTO with respect to agricultural price supports implemented by the Indian government.</p>"
        },
        "title": "Ag Disputes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s743.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prioritizing Offensive Agricultural Disputes and Enforcement Act or the Ag Disputes Act</strong></p><p>This bill establishes a joint task force to identify and address trade barriers to U.S.\u00a0agricultural exports.</p><p>Specifically, the bill directs the President to establish the Agricultural Trade Enforcement Task Force. Members of this task force include employees of the Department of Agriculture's Foreign Agricultural Service and the Office of the U.S. Trade Representative.</p><p>The bill requires the task force to (1) identify trade barriers to U.S. agricultural exports that are vulnerable to dispute settlement under the World Trade Organization (WTO) or other trade agreements to which the United States is a party, (2) develop and implement a strategy for enforcing violations of trade agreements related to those trade barriers, (3) identify like-minded trading partners that could act as complainants on disputes relating to specific trade barriers that are systemically or economically important to the United States, and (4) submit periodic reports to Congress.</p><p>In its first report, the task force must include a plan for filing a request for consultations under the WTO with respect to agricultural price supports implemented by the Indian government.</p>",
      "updateDate": "2025-07-08",
      "versionCode": "id119s743"
    },
    "title": "Ag Disputes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Prioritizing Offensive Agricultural Disputes and Enforcement Act or the Ag Disputes Act</strong></p><p>This bill establishes a joint task force to identify and address trade barriers to U.S.\u00a0agricultural exports.</p><p>Specifically, the bill directs the President to establish the Agricultural Trade Enforcement Task Force. Members of this task force include employees of the Department of Agriculture's Foreign Agricultural Service and the Office of the U.S. Trade Representative.</p><p>The bill requires the task force to (1) identify trade barriers to U.S. agricultural exports that are vulnerable to dispute settlement under the World Trade Organization (WTO) or other trade agreements to which the United States is a party, (2) develop and implement a strategy for enforcing violations of trade agreements related to those trade barriers, (3) identify like-minded trading partners that could act as complainants on disputes relating to specific trade barriers that are systemically or economically important to the United States, and (4) submit periodic reports to Congress.</p><p>In its first report, the task force must include a plan for filing a request for consultations under the WTO with respect to agricultural price supports implemented by the Indian government.</p>",
      "updateDate": "2025-07-08",
      "versionCode": "id119s743"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s743is.xml"
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
      "title": "Ag Disputes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ag Disputes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Prioritizing Offensive Agricultural Disputes and Enforcement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the establishment of a joint task force to identify and eliminate barriers to agriculture exports of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:24Z"
    }
  ]
}
```
