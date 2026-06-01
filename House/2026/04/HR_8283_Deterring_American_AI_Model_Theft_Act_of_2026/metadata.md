# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8283?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8283
- Title: Deterring American AI Model Theft Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8283
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-28T19:35:24Z
- Update date including text: 2026-05-28T19:35:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8283",
    "number": "8283",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001058",
        "district": "4",
        "firstName": "Bill",
        "fullName": "Rep. Huizenga, Bill [R-MI-4]",
        "lastName": "Huizenga",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Deterring American AI Model Theft Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-28T19:35:24Z",
    "updateDateIncludingText": "2026-05-28T19:35:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-15",
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
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
            "date": "2026-04-22T20:32:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:00:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "MI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "C001087",
      "district": "1",
      "firstName": "Eric",
      "fullName": "Rep. Crawford, Eric A. \"Rick\" [R-AR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Crawford",
      "middleName": "A. \"Rick\"",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "AR"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "IL"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "NC"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "AL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8283ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8283\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Huizenga (for himself and Mr. Moolenaar ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prevent foreign adversaries from threatening the national security of the United States by extracting key technical features of closed-source, American-owned artificial intelligence models, and for other purposes.\n#### 1. Short title\nThis Act may be cited as Deterring American AI Model Theft Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nartificial intelligence (AI) models owned by United States private sector companies are essential for advancing United States economic and national security interests;\n**(2)**\nmany of the most advanced AI models owned by United States companies are closed-source models whose unique technical characteristics are not openly shared or published;\n**(3)**\nthe unauthorized acquisition of model capabilities, such as model weights, model architectures, and other technical characteristics of closed-source AI models by entities of concern through model extraction attacks represents a threat to the national security and foreign policy interests of the United States, as well as the intellectual property rights and economic competitiveness of United States companies;\n**(4)**\nthe United States Government, in cooperation with private owners of closed-source AI models, should take steps to identify, punish, and deter model extraction attacks on the protected capabilities of closed-source models by entities of concern;\n**(5)**\nmodel extraction attacks against American closed-source AI models allow foreign adversaries a short cut to acquiring advanced AI capabilities; and\n**(6)**\nauthorized model training practices that adhere to the terms of service or are otherwise consistent with contractual terms set by the owners of closed-source AI models are a legitimate research method that play an important role in AI research and are fundamentally distinct from model extraction attacks defined in this Act.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs in the Senate.\n**(2) Closed-source AI model**\nThe term closed-source AI model means any artificial intelligence model with the following characteristics:\n**(A)**\nProprietary key technical information such as underlying model weights that are necessary to reproduce and independently recreate the model that are not willingly shared with third parties or otherwise made publicly available by the owner of the model.\n**(B)**\nAccess and use governed by terms of service or contractual agreements that are established by the owner of the model.\n**(C)**\nAccess that is provided via an Application Program Interface (API) or other consumer-facing, owner-controlled interfaces without enabling third parties to obtain, modify, or host the closed-source AI model on their own data servers or other technology unless specifically authorized by the owner of the closed-source AI model.\n**(3) Country of concern**\nThe term country of concern means\u2014\n**(A)**\nthe People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions;\n**(B)**\nthe Russian Federation; and\n**(C)**\nany other foreign country\u2014\n**(i)**\nlisted in Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations, as published on January 1, 2026, that is designated by the Secretary of State as a country of concern for purposes of this section and for which notice of such designation has been published in the Federal Register; and\n**(ii)**\ndesignated by the Secretary of State pursuant to the assessment described in subsection (b) or (e) of section 4 of this Act.\n**(4) Entity of concern**\nThe term entity of concern means any foreign person or entity that\u2014\n**(A)**\nis located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern;\n**(B)**\nis operating under the direction or control of any entity located or headquartered in, or the ultimate parent company of which is headquartered in, a country of concern; or\n**(C)**\nis conducting or attempting to conduct a model extraction attack against closed-source AI models owned by United States persons and outside of authorized model training practices.\n**(5) Export**\nThe term export has the meaning given that term in section 1742(3) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(3) ).\n**(6) Foreign person**\nThe term foreign person means a person that is not a United States person.\n**(7) Fraudulent account network provider**\n**(A) In general**\nThe term fraudulent account network provider means any foreign entity that knowingly and intentionally creates, obtains, maintains, sells, brokers, or otherwise provides access to accounts that allow entities of concern to access closed-source AI models that they would otherwise be prohibited from accessing due to location restrictions in the terms of service or contractual agreements created by the owner of the closed-source AI model.\n**(B) Exception**\nAn entity that creates or transmits location information to enable persons within countries of concern to access the internet for purposes of freedom of expression is not considered, on the basis of this activity alone, a fraudulent account network provider.\n**(8) Good**\nThe term good has the meaning given that term in section 16 of the Export Administration Act of 1979 ( 50 U.S.C. App. 2415 )(as continued in effect pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. )).\n**(9) In-country transfer**\nThe term in-country transfer has the meaning given that term in section 1742(6) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(6) ).\n**(10) Item**\nThe term item has the meaning given that term in section 1742(7) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(7) ).\n**(11) Model extraction attack**\n**(A) In general**\nThe term model extraction attack means the unauthorized extracting of a closed-source AI model\u2019s capabilities to replicate, develop, train, or improve another AI model, where such querying\u2014\n**(i)**\ncircumvents technical, contractual, or other access controls, identity verification requirements, or geographic access restrictions implemented by the model\u2019s owner;\n**(ii)**\nis conducted through fraudulent, misrepresented, or unauthorized credentials; or\n**(iii)**\nviolates the terms, conditions, or restrictions governing access to or use of the model, as established by the owner or authorized provider, that specifically prohibit the use of model outputs or interactions to replicate, develop, train, or improve another AI model.\n**(B) Inference of purpose**\nFor purposes of subparagraph (A), the purpose of querying may be inferred from the totality of circumstances, including\u2014\n**(i)**\nthe volume, structure, pattern, coordination, or timing of the querying activity;\n**(ii)**\nthe concentration of queries on specific model capabilities;\n**(iii)**\nthe use of multiple accounts in a coordinated matter; or\n**(iv)**\nthe correlation of querying activity within the development timeline of another AI model.\n**(C) Exclusion**\nModel training activities conducted in compliance with the terms, conditions, and restrictions governing access to and use of the closed-source AI model, or otherwise conducted within a permitted exception or the express authorization of the owner of the closed-source AI model, are not model extraction attacks.\n**(12) Operating Committee for Export Policy**\nThe term Operating Committee for Export Policy means the Operating Committee for Export Policy referred to in section 1763(c) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4822(c) ).\n**(13) Owner**\nThe term owner means, with respect to a closed-source AI model, the person or entity that\u2014\n**(A)**\nholds intellectual property rights (including trade secret, copyright, patent, or other proprietary rights), contractual rights, or a combination thereof, sufficient to authorize or restrict third-party access to, use of, extraction from, or reproduction of such closed-source AI model, or any version, instance, or deployment thereof, whether such rights were obtained through development, acquisition, assignment, license, or otherwise; and\n**(B)**\nis a United States person.\n**(14) Reexport**\nThe term reexport has the meaning given that term in section 1742(9) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4801(9) ).\n#### 4. Assessment of model extraction attacks and fraudulent account network providers\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall complete an assessment to determine\u2014\n**(1)**\nwhich, if any, entities of concern have conducted or are currently conducting model extraction attacks against closed-source AI models owned by United States entities; and\n**(2)**\nwhich, if any, entities of concern are fraudulent account network providers.\n##### (b) Matters To be included\nThe assessment required by subsection (a) shall include the following:\n**(1)**\nA determination of which entities of concern\u2014\n**(A)**\nhave either previously or are currently engaging in model extraction attacks; or\n**(B)**\nare fraudulent account network providers.\n**(2)**\nA determination of which, if any, countries model extraction attacks have originated from and where fraudulent account network providers exist.\n**(3)**\nAn identification of which, if any, agencies or instrumentalities of governments of countries of concern have provided or are providing material assistance to entities identified pursuant to paragraph (1).\n**(4)**\nAn analysis of the methods employed by entities of concern identified pursuant to paragraph (1), including\u2014\n**(A)**\nthe role of fraudulent account network providers in model extraction attacks, including, to the extent possible, the physical location of fraudulent account network provider offices and data centers; and\n**(B)**\na determination, to the extent possible, of the number of attempted model extraction attacks that occurred in the previous two calendar years from the date on which the Secretary of State begins the assessment pursuant to subsection (a)(1).\n**(5)**\nAn examination of the strengths and weaknesses of various detection approaches that can be used to determine whether a model extraction attack has occurred or is occurring.\n**(6)**\nAn assessment of the economic and national security consequences of successful model extraction attacks by entities of concern that occurred in the previous two calendar years from the date on which the Secretary of State begins the assessment pursuant to subsection (a)(1).\n**(7)**\nSteps detailing how the United States Government is assisting owners of closed-source AI models that have been the target or victim of model extraction attacks in detecting model extraction attacks, deterring future model extraction attacks, and punishing entities of concern that engage in model extraction attacks or are fraudulent account network providers.\n**(8)**\nA diplomatic strategy to leverage United States allies and partners in detecting and preventing model extraction attacks by entities of concern.\n##### (c) Public consultation\nIn conducting the assessment required by subsection (a), the Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall consult with owners of closed-source AI models that have been the targets or victims of model extraction attacks, whose participation in this consultation shall be voluntary, other companies, academic experts, industry fora, and other appropriate entities to\u2014\n**(1)**\nidentify patterns of attacker behavior and methods to better inform United States Government and private sector efforts to detect model extraction attacks;\n**(2)**\ndevelop best practices for defending against model extraction attacks; and\n**(3)**\ndevelop best practices for identifying fraudulent account network provider activities that facilitate model extraction attacks.\n##### (d) Report\n**(1) In general**\nNot later than 210 days after the date of the enactment of this Act, the Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall submit to the appropriate congressional committees a report that contains the findings of the assessment. The Secretary of Commerce shall, annually for 3 years, submit to the appropriate congressional committees an updated report with any additional entities of concern identified pursuant to subsection (b)(1).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form, but may contain a classified annex.\n##### (e) Routine assessment\nThe Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall routinely assess for\u2014\n**(1)**\nmodel extraction attacks directed against owners of closed-source AI models that occur after the date of completion of the assessment required by this section;\n**(2)**\nfraudulent account network providers that facilitate model extraction attacks after the date of completion of the assessment required by this section; and\n**(3)**\nany material changes related to other matters specified in subsection (b).\n##### (f) Industry coordination\nThe Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall establish an information sharing mechanism that allows owners of closed-source AI models to voluntarily, quickly, and confidentially share information about model extraction attacks and fraudulent account network providers with the Department of Commerce.\n##### (g) AI model extraction attackers list\n**(1) In general**\nThe Secretary of State, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall\u2014\n**(A)**\nmaintain a list, to be known as the AI Model Extraction Attackers List , that displays information about specific individuals and entities of concern, that the assessment required by subsection (a) and routine assessment described in subsection (e) identify as having conducted or directed model extraction attacks in the past year; and\n**(B)**\npublish such list on a publicly available website of the Department of State for up to 5 years.\n**(2) Protection of confidential information**\nThe Secretary of State may not, in publishing the list required by paragraph (1) on a publicly available website of the Department of State, disclose confidential information provided by owners of closed-source AI models without the express permission of said owner.\n##### (h) Public guidance\nNot later than 210 days after the date of the enactment of this Act, the Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall publish a report comprising of best practices to detect, prevent, and respond to model extraction attacks.\n**(1) Public access**\nThe report required by this subsection shall be publicly available.\n**(2) Protection of confidential information**\nIn making the report required by this subsection publicly available, the Secretary of Commerce, in coordination with each agency that is a member of the Operating Committee for Export Policy, shall not disclose confidential information provided by owners of closed-source AI models without the express permission of said owner.\n#### 5. Deterring model extraction attacks and fraudulent account network providers\n##### (a) Addition consideration for Entity List\nNot later than 210 days after the date of the enactment of this Act, the Under Secretary of Commerce for Industry and Security, in coordination with each agency that is a member of the End-User Review Committee, shall make a determination by majority vote of the Committee on whether entities identified as having conducted model extraction attacks or having facilitated them via fraudulent account networks after the date of the completion of the assessment required under section 4 of this Act (identified pursuant to subsection (e) of such section), or any affiliate of such entity (to be determined by ownership of 50 percent or more in the aggregate, directly or indirectly), should be added to the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce under Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, or any successor regulations.\n##### (b) Sanctions described\n**(1) In general**\nThe President, acting through the Secretary of State, may, pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ), block and prohibit all transactions in all property and interests in property of entities of concern identified pursuant to subsections (b)(1) and (e) of section 4 if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Exceptions**\n**(A) Exception to comply with international obligations**\nSanctions under this subsection shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(B) Exception relating to the provision of humanitarian assistance**\nSanctions under this subsection may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(i)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(ii)**\nthe provision of humanitarian assistance;\n**(iii)**\nfinancial transactions relating to humanitarian assistance; or\n**(iv)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(C) Exception for intelligence, law enforcement, and national security activities**\nSanctions under this subsection shall not apply to any authorized intelligence, law enforcement, or national security activities of the United States.\n**(3) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this subsection or any regulation, license, or order issued to carry out that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.",
      "versionDate": "2026-04-15",
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
        "name": "International Affairs",
        "updateDate": "2026-04-20T22:30:16Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8283ih.xml"
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
      "title": "Deterring American AI Model Theft Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T08:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Deterring American AI Model Theft Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prevent foreign adversaries from threatening the national security of the United States by extracting key technical features of closed-source, American-owned artificial intelligence models, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T08:18:29Z"
    }
  ]
}
```
