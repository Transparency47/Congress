# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5299?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5299
- Title: DFC Modernization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5299
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-12-15T21:58:33Z
- Update date including text: 2025-12-15T21:58:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5299",
    "number": "5299",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "DFC Modernization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-15T21:58:33Z",
    "updateDateIncludingText": "2025-12-15T21:58:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 23.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
        "item": [
          {
            "date": "2025-09-18T18:20:20Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-17T18:20:09Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-11T13:04:35Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5299ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5299\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Mast introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo modify and reauthorize the Better Utilization of Investments Leading to Development Act of 2018, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the DFC Modernization Act of 2025 .\n#### 2. Sense of Congress; statement of policy\n##### (a) In general\nIt is the sense of Congress that the United States International Development Finance Corporation should seek to responsibly increase its risk tolerance in investments to ensure that the Corporation is maximizing the mobilization of private capital and properly pursuing its statutory objectives of advancing United States foreign policy, economic development, and national security goals to make America safer, stronger, and more prosperous, including\u2014\n**(1)**\nby more frequent use of one or more of a variety of tools to mitigate risk to the private sector, including the use of equity, hybrid securities, mezzanine debt, accepting creditor status that is subordinate to that of other creditors, using partial guarantees, employing first loss coverage, insurance, and using blended finance;\n**(2)**\nby lending, investing, or offering insurance in high-risk countries, regions, or sectors as a means to achieve its mission as a United States foreign policy and development agency of economic statecraft to mobilize capital, secure strategic needs, and build private markets;\n**(3)**\nby preventing strategic competitor inroads and dominance of key sectors such as infrastructure, critical and rare earth minerals, and critical supply chains and industries, which is in the economic and national security interests of the United States; and\n**(4)**\nby assisting allied and partner countries in achieving energy security through diversification of their energy sources and supply routes which is in the economic and national security interests of the United States.\n##### (b) Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto advance United States foreign policy, national security, and economic development goals by facilitating market-based private sector development in countries to make America safer, stronger, and more prosperous;\n**(2)**\nto counter or limit strategic competitor inroads and dominance of key sectors such as infrastructure, critical and rare earth minerals, and critical supply chains and industries through support of diversified private sector options and by providing a robust alternative to and reducing reliance on state-directed, unsustainable financing by strategic competitors of the United States;\n**(3)**\nto advance United States foreign policy, national security, and economic development goals by assisting countries to reduce their dependence on resources from countries that use dependence for undue malign influence and that have used natural gas, nuclear energy, oil, rare earths, critical and strategic materials, and other resources to coerce, intimidate, and influence other countries;\n**(4)**\nto promote the energy security of allied and partner countries by encouraging the development of accessible, transparent, and competitive energy markets that provide diversified sources, energy types, and diversified energy transport and distribution methods and routes, which are in the economic and national security interests of the United States;\n**(5)**\nto encourage United States public and private sector investment in energy, telecommunications, and other infrastructure projects in allied and partner countries to bridge the gap between security requirements and commercial demand consistent with the country\u2019s absorptive capacity;\n**(6)**\nto facilitate the export of United States energy, telecommunications, technology, expertise, and other resources to global markets in a way that benefits the economic and national security interests of the United States;\n**(7)**\nto support private sector development in countries that promote economic prosperity in a manner that can help to curb illegal migration and secure the borders of the United States;\n**(8)**\nto facilitate procurement of necessary resources and supply chains for the benefit of the United States and its citizens; and\n**(9)**\nto facilitate market-based private sector development and economic growth through the provision of credit, capital, and other financial support by taking on substantial financial risk, and when necessary financial losses, to unlock new, significant private capital investments or achieve or advance major United States foreign policy objectives. Losses may be expected, in certain instances, at the individual investment level and financial performance may be measured at the overall portfolio level.\nI\nDEFINITIONS AND LESS DEVELOPED COUNTRY FOCUS\n#### 101. Definitions\nSection 1402 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9601 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (3), (4), and (5), respectively;\n**(2)**\nby inserting after paragraph (1) the following:\n(2) High-income country The term high-income country means a country with a high-income economy, as defined by International Bank for Reconstruction and Development and the International Development Association (collectively referred to as the World Bank ). ;\n**(3)**\nin paragraph (5), as so redesignated\u2014\n**(A)**\nin subparagraph (A), by striking or at the end;\n**(B)**\nin subparagraph (B), by striking the period at the end and inserting ; or ; and\n**(C)**\nby adding at the end, the following:\n(C) any other similar institution that has a purpose that is similar to the purposes of the Corporation as described in section 1412(b) of this title. ; and\n**(4)**\nby adding at the end the following:\n(6) Country of concern The term country of concern means any of the following countries: (A) The Bolivarian Republic of Venezuela. (B) The Republic of Cuba. (C) The Democratic People\u2019s Republican of Korea. (D) The Islamic Republic of Iran. (E) The People\u2019s Republic of China. (F) The Russian Federation. (G) Belarus. .\n#### 102. Less developed country focus\nSection 1412 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9612 ) is amended\u2014\n**(1)**\nby inserting and high income countries and areas, as appropriate, after less developed countries ; and\n**(2)**\nby adding at the end the following:\n(3) Support in high-income countries and areas The Corporation shall restrict the provision of support under title II in high-income countries and areas unless the President certifies to the appropriate congressional committees that such support furthers the national economic or foreign policy interests of the United States. .\nII\nMANAGEMENT OF CORPORATION\n#### 201. Board of Directors\nSection 1413(b) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9613(b) ) is amended\u2014\n**(1)**\nin subparagraph (2)(A)(iii), by striking 5 individuals each place it appears and inserting 3 individuals ;\n**(2)**\nin subparagraph (2)(B)(i), by striking subclause III and inserting the following:\n(III) One other principal officer from an executive Department designated by the President. ; and\n**(3)**\nby striking subparagraph (4) and inserting the following:\n(4) Vice chairperson The President shall appoint a member of the Board to serve as the Vice Chairperson of the Board. .\n#### 202. Chief Risk Officer\nSection 1413(f) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9613(f) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking , who\u2014 and inserting a period;\n**(2)**\nin paragraph (1), by striking subparagraphs (A) and (B); and\n**(3)**\nin paragraph (2), by striking audit and inserting risk .\n#### 203. Chief Development Officer\n##### (a) In general\nSection 1413 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9613 ) is amended\u2014\n**(1)**\nin subsection (a), by striking a Chief Development Officer, ;\n**(2)**\nby striking subsection (g) and redesignating subsections (h) and (i) as subsections (g) and (h), respectively;\n**(3)**\nin subsection (g) as so redesignated, by striking paragraph (1) and inserting the following:\n(1) In general Except as otherwise provided in this section, officers, employees, and agents shall be selected and appointed by or under the authority of the Chief Executive Officer, and shall be vested with such powers and duties as the Chief Executive Officer or the designee of the Chief Executive Officer may determine. ; and\n**(4)**\nin subsection (h), as so redesignated, by striking and the Chief Development Officer, .\n##### (b) Chief Executive Officer\nSection 1445 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9655 ) is amended\u2014\n**(1)**\nby striking subsection (a) and inserting the following:\n(a) In general The Chief Executive Officer shall\u2014 (1) develop a strategic relationship with private sector entities focused at the nexus of business opportunities and development priorities; (2) engage such entities and reduce business risks primarily through direct transaction support and facilitating investment partnerships; (3) develop and support tools, approaches, and intermediaries that can mobilize private finance at scale in the developing world; and (4) pursue highly developmental projects of all sizes, especially those that are small but designed for work in the most underdeveloped areas, including countries with chronic suffering as a result of extreme poverty, fragile institutions, or a history of violence. ; and\n**(2)**\nin subsection (c), by striking the United States Agency for International Development and .\n#### 204. Administratively determined positions\nSection 1413(g)(2) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9613(g)(2) ), as so redesignated, is amended in subparagraph (A) by striking 50 and inserting 100 .\nIII\nAUTHORITIES RELATING TO PROVISION OF SUPPORT\n#### 301. Equity limitation\nSection 1421(c)(4)(A) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9621(c)(4)(A) ) is amended by striking 30 and inserting 49 .\n#### 302. Revolving equity investment account\n##### (a) Equity Investments Account\nSection 1421(c) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9621(c) ) is amended by adding at the end the following:\n(7) Equity Investments Account (A) Establishment There is established in the Treasury of the United States an Equity Investments Account of the United States International Development Finance Corporation (referred to in this subsection as the Equity Investments Account ). (B) Retention of collections Collections derived from the earnings, fees, credits, and other collections from the equity investments made using amounts in the Equity Investments Account shall be deposited into the Equity Investments Account, and shall be available to the Corporation without further appropriation or fiscal year limitation for carrying out the purposes of this section. .\n##### (b) Collections\nSection 1434(h) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9634(h) ) is amended by adding except earnings, fees, credits, and other collections related to equity investments from the Equity Investments Account, after earnings collected related to equity investments, .\n#### 303. Enterprise funds\nSection 1421(g) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9621(g) ) is amended\u2014\n**(1)**\nin paragraph (1), by striking the Administrator of the United States Agency for International Development, ; and\n**(2)**\nin paragraph (3)(E), by striking Agency for International Development .\n#### 304. Termination\nSection 1424(a) of the Better Utilization of investments Leading to Development Act of 2018 ( 22 U.S.C. 9624(a) ) is amended by striking the date that is 7 years after the date of the enactment of this Act and inserting December 31, 2031 .\nIV\nOTHER MATTERS\n#### 401. Corporate powers\nSection 1432(a) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9632(a) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking division C of subtitle I of ; and\n**(2)**\nin paragraph (10), by striking until the expiration of the current lease under predecessor authority, as of the day before the date of the enactment of this Act .\n#### 402. Maximum contingent liability\nSection 1433 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9633 ) is amended by striking $60,000,000,000 and inserting $250,000,000,000 .\n#### 403. Authority to use portion of corporation fees to update information technology systems; transfer of funds\nSection 1434 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9634 ) is amended\u2014\n**(1)**\nin subsection (d)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (B), by adding and at the end;\n**(ii)**\nin subparagraph (C), by striking the semicolon at the end and inserting a period; and\n**(iii)**\nby striking subparagraph (D); and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (B), by striking and at the end;\n**(ii)**\nin subparagraph (C), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following:\n(D) project-specific transaction costs; and (E) transfers and additions to such other accounts, funds, or reserves as the Corporation may establish, at such time and in such amounts as the Board may determine. ;\n**(2)**\nin subsection (j), by inserting (i) title 10, United States Code, (ii) the Strategic and Critical Materials Stock Piling Act ( 50 U.S.C. 98 et seq. ), or (iii) after funds authorized to be appropriated to carry out ; and\n**(3)**\nin subsection (k)\u2014\n**(A)**\nin paragraph (1), by inserting other direct costs associated with origination or monitoring services, including seminars, conferences, and other pre-investment services, after legal expenses, ; and\n**(B)**\nin paragraph (2), by striking does not include and inserting includes .\n#### 404. Notifications to be provided by the corporation\nSection 1446(a) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9656(a) ) is amended by striking $10,000,000 and inserting $100,000,000 .\n#### 405. Millennium challenge corporation\n##### (a) Coordination with other development agencies\nSection 1435 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9635 ) is amended by striking the United States Agency for International Development .\n##### (b) Sources of information\nSection 1451(g)(2) of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9671(g)(2) ) is amended by striking the Department of Commerce\u2019s Country Commercial Guides, or the Millennium Challenge Corporation\u2019s Constraints Analysis, and inserting or the Department of Commerce\u2019s Country Commercial Guides, .\n#### 406. State-owned enterprises\nSection 1451 of the Better Utilization of Investments Leading to Development Act of 2018 ( 22 U.S.C. 9671 ) is amended by adding at the end the following:\n(j) Policies with respect to state-Owned enterprises, anticompetitive practices, and countries of concern (1) Policy The Corporation shall develop appropriate policies and guidelines for support provided under title II for a project involving a state-owned enterprise, sovereign wealth fund, or a parastatal entity to ensure such support is provided consistent with appropriate principles and practices of competitive neutrality. (2) Prohibitions (A) Anticompetitive practices The Corporation may not provide support under title II for a project that involves a private sector entity engaged in anticompetitive practices. (B) Countries of concern The Corporation may not provide support under title II for projects\u2014 (i) that involve partnerships with the government of a country of concern or a state-owned enterprise that belongs to or is under the control of a foreign country of concern; or (ii) that would be operated, managed, or controlled by the government of a country of concern or a state-owned enterprise that belongs to or is under the control of a foreign country of concern. (3) Definitions In this subsection: (A) State-owned enterprise The term state-owned enterprise means any enterprise established for a commercial or business purpose that is directly owned or controlled by one or more governments, including any agency, instrumentality, subdivision, or other unit of government at any level of jurisdiction. (B) Control The term control , with respect to an enterprise, means the power by any means to control the enterprise regardless of\u2014 (i) the level of ownership; and (ii) whether or not the power is exercised. (C) Owned The term owned , with respect to an enterprise, means a majority or controlling interest, whether by value or voting interest, of the shares of that enterprise, including through fiduciaries, agents, or other means. (4) Qualifying sovereign entity State-owned enterprises, sovereign wealth funds, or parastatal entities that the Corporation supports, pursuant to the policy and prohibitions in section 407 (1) and (2), shall be considered as a qualifying sovereign entity as defined in section 1402. .\n#### 407. Repeal of redundant provisions of the European Energy Security and Diversification Act of 2019\nThe European Energy Security and Diversification Act of 2019 (title XX of division P of Public Law 116\u201394 ; 22 U.S.C. 9501 note) is hereby repealed.",
      "versionDate": "2025-09-11",
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
            "name": "Business investment and capital",
            "updateDate": "2025-12-15T21:55:38Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-12-15T21:57:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-15T21:55:44Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2025-12-15T21:55:53Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-12-15T21:58:25Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-15T21:55:59Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-12-15T21:56:07Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-12-15T21:56:16Z"
          },
          {
            "name": "Government corporations and government-sponsored enterprises",
            "updateDate": "2025-12-15T21:56:28Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-12-15T21:56:37Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-12-15T21:56:45Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-12-15T21:56:55Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-12-15T21:57:06Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-12-15T21:58:19Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-12-15T21:57:13Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2025-12-15T21:58:33Z"
          },
          {
            "name": "Trade agreements and negotiations",
            "updateDate": "2025-12-15T21:57:22Z"
          },
          {
            "name": "U.S. International Development Finance Corporation",
            "updateDate": "2025-12-15T21:58:11Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-12-15T21:57:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-19T16:30:18Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5299ih.xml"
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
      "title": "DFC Modernization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "DFC Modernization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify and reauthorize the Better Utilization of Investments Leading to Development Act of 2018, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T04:33:22Z"
    }
  ]
}
```
