# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6996?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6996
- Title: Full AI Stack Export Promotion Act
- Congress: 119
- Bill type: HR
- Bill number: 6996
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-05-21T12:20:27Z
- Update date including text: 2026-05-21T12:20:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 37 - 7.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 37 - 7.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6996",
    "number": "6996",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "F000484",
        "district": "6",
        "firstName": "Randy",
        "fullName": "Rep. Fine, Randy [R-FL-6]",
        "lastName": "Fine",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Full AI Stack Export Promotion Act",
    "type": "HR",
    "updateDate": "2026-05-21T12:20:27Z",
    "updateDateIncludingText": "2026-05-21T12:20:27Z"
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 37 - 7.",
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
      "actionDate": "2026-01-09",
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
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
            "date": "2026-04-22T20:22:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-09T14:00:50Z",
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
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6996ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 6996\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Fine introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo facilitate the export of United States artificial intelligence systems, computing hardware, and standards globally.\n#### 1. Short title\nThis Act may be cited as the Full AI Stack Export Promotion Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe United States is in a race to achieve global dominance in artificial intelligence, the winner of which will reap broad economic and military benefits.\n**(2)**\nWinning the AI race will usher in a new golden age of human flourishing, economic competitiveness, and national security for the American people.\n**(3)**\nEstablishing United States AI as the gold standard for AI worldwide and ensuring our allies build AI on United States technology will help the United States win the AI race.\n**(4)**\nAdvanced AI compute is essential to the AI era, enabling both economic dynamism and novel military capabilities. Denying our foreign adversaries access to this resource, then, is a matter of both geostrategic competition and national security.\n#### 3. Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\nmaintain United States dominance in the global deployment of artificial intelligence;\n**(2)**\ndrive adoption of the U.S. full AI stack by allies and partners;\n**(3)**\nensure global deployment of artificial intelligence is based on United States-developed AI models, run by United States cloud operators, run by data centers owned or operated by United States firms, and functioning on United States-designed artificial intelligence semiconductors;\n**(4)**\nreduce the barriers faced by United States firms to export the U.S. full AI stack;\n**(5)**\ncounter Chinese influence in international governance bodies and ensure the global deployment of the full AI stack strengthens United States values abroad;\n**(6)**\nprevent illicit foreign adversary access to the U.S. full AI stack deployed abroad;\n**(7)**\nensure the global deployment of AI strengthens the qualitative military superiority of the United States and its allies over foreign adversaries; and\n**(8)**\nmaintain a majority of globally deployed artificial intelligence computing capacity and memory bandwidth in the United States.\n#### 4. Industry consortia for exporting the full AI stack\n##### (a) In general\nThe Secretary of Commerce shall establish and carry out a program to identify and receive proposals that meet United States-approved security requirements and standards from industry consortia to facilitate the export of the U.S. full AI stack to allies and partners. An industry consortia shall be eligible to submit proposals under this subsection if the consortia is established only for the purposes of participating in the program under this subsection.\n##### (b) Report\nNot later than 180 days after the date on which the program required by subsection (a) is established, the Secretary of Commerce shall submit to the appropriate congressional committees a report on the status and results of the program.\n#### 5. Eliminating foreign barriers to the U.S. full AI stack\n##### (a) In general\nThe Secretary of State, in consultation with the Secretary of Commerce, shall work to increase efforts to eliminate foreign barriers to the export of the U.S. full AI stack, including\u2014\n**(1)**\ncarrying out activities such as holding regular industry listening sessions;\n**(2)**\nestablishing a hotline for industry to communications barriers to exporting the U.S. full AI stack;\n**(3)**\nelevating appropriate diplomatic channels; and\n**(4)**\ncarrying out other relevant actions.\n##### (b) Diplomatic strategy\nNot later than 180 days after the enactment of this Act, the Secretary of State shall establish a diplomatic strategy outlining how the United States will address the following:\n**(1)**\nEasing United States AI companies\u2019 access to foreign markets.\n**(2)**\nCommunicating to foreign countries the importance and benefits of using the U.S. full AI stack to deploy artificial intelligence.\n**(3)**\nLeveraging the United States position in international diplomatic and standard-setting bodies to advocate for international AI governance approaches that promote innovation, reflect American values, and counter authoritarian influence.\n##### (c) Report\nNot later than 180 days after the date on which the strategy required by subsection (c) is completed, the Secretary of Commerce shall submit to the appropriate congressional committees the strategy and an update on efforts to implement the strategy.\n#### 6. Study on global AI deployment\n##### (a) In general\nThe Secretary of State, in coordination with the Director of National Intelligence and the Secretary of Commerce, shall conduct a study on the benefits and impact of the global deployment of artificial intelligence.\n##### (b) Matters To be addressed\nThe study required by subsection (a) shall address the following:\n**(1)**\nThe economic, diplomatic, and technological impact for the United States and its allies from the global deployment of the U.S. full AI stack.\n**(2)**\nThe impact on U.S. economic, diplomatic, and technological leadership from the global deployment of the U.S. full AI stack.\n**(3)**\nHow the global deployment of the U.S. full AI stack assists countries worldwide in achieving economic prosperity, improving quality of life, expanding healthcare and educational access for their citizens, and growing access to AI.\n**(4)**\nThe competitive position of the U.S. full AI stack globally, compared to similar technology developed by foreign countries.\n**(5)**\nHow the global deployment of the U.S. full AI stack enhances or affects United States and allied security, including the qualitative military superiority of the United States and its allies over foreign adversaries.\n**(6)**\nPriority regions and countries for exporting the U.S. full AI stack abroad.\n##### (c) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State submit to appropriate congressional committees a report on the results of the study required by subsection (a).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex.\n#### 7. Security of U.S. artificial intelligence semiconductor products\n##### (a) In general\nThe Secretary of Commerce, in coordination with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, shall work with foreign purchasers of the U.S. full AI stack to institute security measures to prevent illicit or unauthorized foreign adversary access to the U.S. full AI stack.\n##### (b) Report\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Commerce shall submit to the appropriate congressional committees a report on the development and implementation of the security measures described in subsection (a).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex.\n##### (c) Matters To be addressed\nThe report required by subsection (b) shall address the following:\n**(1)**\nPlans of the Secretary of Commerce, in coordination with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, to increase the speed and security of the deployment of the U.S. full AI stack, such as creating standardized security requirements for the U.S. full AI stack deployed in third countries.\n**(2)**\nAgreements reached with countries designed to promote adoption of the U.S. full stack, including efforts to prevent illicit or unauthorized foreign adversary access to the U.S. full AI stack.\n**(3)**\nThe security measures that foreign purchasers of the U.S. full AI stack must undertake to prevent transfer of the U.S. full AI stack to foreign adversaries, including by remote access.\n**(4)**\nThe presence of foreign adversary hardware and software within the artificial intelligence supply chains of foreign purchasers of the U.S. full AI stack, and supply-chain security measures that foreign purchasers of the U.S. full AI stack take to eliminate that presence.\n**(5)**\nAny other relevant information regarding the security of the U.S. full AI stack.\n#### 8. AI full stack confidence initiative\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Commerce, in coordination with the Secretary of State, the Secretary of Defense, the Secretary of Energy, and the public, including the industry consortia identified in section 4, shall develop generally applicable practices, product offerings, or related standards to help demonstrate confidence and reassurance to major national purchasers of the U.S. full AI stack of the privacy, confidentiality, security, and effectiveness of the U.S. full AI stack for achieving the economic and security goals of major foreign purchasers.\n#### 9. AI full stack export success tracker\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and biannually thereafter for five years, the Secretary of Commerce, in coordination with the Director of National Intelligence and the Secretary of State, shall complete an estimate of the success of the export of the U.S. full AI stack (in this section referred to as the AI export success tracker ).\n##### (b) Contents\nThe AI export success tracker shall contain the following elements:\n**(1)**\nAn estimate of each country\u2019s installed artificial intelligence, measured by total national computing capacity and total national memory bandwidth.\n**(2)**\nAn estimate of what proportion of globally installed artificial intelligence integrated circuits are designed by United States firms.\n**(3)**\nAn estimate of what proportion of globally installed artificial intelligence is installed in data centers owned or operated by United States firms, with appropriate descriptive breakdowns for each region or country.\n**(4)**\nAn estimate of the proportion of global artificial intelligence model usage, measured by tokens processed, that occurs for models owned or operated by United States firms, with appropriate descriptive breakdowns for each region or country.\n**(5)**\nAn estimate of the proportion of global cloud computing services revenue and data-processing capacity is attributable to cloud operators owned or operated by United States firms.\n##### (c) Report\n**(1) In general**\nThe Secretary of Commerce shall submit to the appropriate congressional committees and make available to the public a report that contains the findings of each estimate described under subsection (b).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex.\n#### 10. Definitions\nIn this Act\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(2)**\nthe term artificial intelligence integrated circuits means any semiconductor device or integrated circuit architecture that is marketed to perform artificial intelligence model training, inference, or acceleration, including but not limited to graphics processing units;\n**(3)**\nthe term foreign adversaries has the meaning given the term covered nation in section 4872(f) of title 10, United States Code;\n**(4)**\nthe term full AI stack means the compute and data infrastructure that enable artificial intelligence research and development, including high-performance computing resources, data centers, the trained algorithms deployed on such infrastructure, cloud services and infrastructure, and the technical standards with which these facets operate;\n**(5)**\nthe term national computing capacity means the aggregate maximum number of floating-point operations per second (FLOP/s) or equivalent operations available within a country from computing devices, processors, or systems configured for large-scale artificial intelligence training or inference. Computing capacity shall be calculated as the maximum number of floating-point operations per second (FLOP/s), normalized at a precision level determined by the Secretary of Commerce;\n**(6)**\nthe term national memory bandwidth means the aggregate maximum rate, expressed in bytes per second, at which data can be transferred between processing elements and directly attached memory resources in all computing devices, processors, or systems that are configured for large-scale artificial intelligence training or inference within a country. National memory bandwidth shall be measured as the sum of the sustained aggregate data transfer rates of such systems under standard benchmark conditions;\n**(7)**\nthe term U.S. artificial intelligence semiconductor products means any semiconductor device or integrated circuit architecture for which design activities were conducted in the United States and that is marketed to perform artificial intelligence model training, inference, or acceleration, including but not limited to graphics processing units;\n**(8)**\nthe term U.S. full AI stack means those parts of the full AI stack with respect to which entities whose ultimate parent company is organized or headquartered in the United States are key developers, manufacturers, or providers across the relevant parts of the supply chain; and\n**(9)**\nthe term token means a basic unit of text, code, or other data processed by an artificial intelligence model, typically corresponding to a word, part of a word, or symbol, used for the purpose of measuring the volume of model input or output.",
      "versionDate": "2026-01-09",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2026-05-18T15:27:01Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2026-05-18T15:27:27Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-05-18T15:27:06Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-18T15:27:15Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-18T15:27:22Z"
          },
          {
            "name": "Technology transfer and commercialization",
            "updateDate": "2026-05-18T15:27:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-03-19T19:41:05Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6996ih.xml"
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
      "title": "Full AI Stack Export Promotion Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T03:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Full AI Stack Export Promotion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-18T03:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To facilitate the export of United States artificial intelligence systems, computing hardware, and standards globally.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T03:18:23Z"
    }
  ]
}
```
