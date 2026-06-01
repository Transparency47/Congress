# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6058?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6058
- Title: STRIDE Act
- Congress: 119
- Bill type: HR
- Bill number: 6058
- Origin chamber: House
- Introduced date: 2025-11-17
- Update date: 2026-05-13T12:05:23Z
- Update date including text: 2026-05-13T12:05:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-17: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.
- Latest action: 2025-11-17: Introduced in House

## Actions

- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Introduced in House
- 2025-11-17 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-17",
    "latestAction": {
      "actionDate": "2025-11-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6058",
    "number": "6058",
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
    "title": "STRIDE Act",
    "type": "HR",
    "updateDate": "2026-05-13T12:05:23Z",
    "updateDateIncludingText": "2026-05-13T12:05:23Z"
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.",
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
      "actionDate": "2025-11-17",
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
      "actionDate": "2025-11-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-17",
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
            "date": "2026-04-22T20:26:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-17T17:02:10Z",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "GU"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-11-21",
      "state": "NY"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6058ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6058\nIN THE HOUSE OF REPRESENTATIVES\nNovember 17, 2025 Mr. Huizenga (for himself, Mr. Moylan , and Mr. Crenshaw ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide for multilateral semiconductor technology supply chain coordination, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Semiconductor Technology Resilience, Integrity, and Defense Enhancement Act or the STRIDE Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe global semiconductor technology supply chain is critical to United States and allied national security, economic competitiveness, and technological leadership;\n**(2)**\nthe Chinese Communist Party is pursuing strategies to dominate the semiconductor technology industry to assist in its military modernization efforts and human rights abuses through non-market practices, export control violation and avoidance, economic espionage, military-civil fusion, and predatory investment;\n**(3)**\nthe integrity of the global semiconductor technology supply chain requires coordinated action with allied and partner nations to prevent technological capture by the Chinese Communist Party and other foreign adversaries;\n**(4)**\nunilateral export controls for protecting critical semiconductor technologies can be amplified with multilateral coordination; and\n**(5)**\nfully utilizing certain unilateral United States export control authorities, including the Foreign Direct Product Rule, has proven effective at preventing circumvention or avoidance of United States export controls through third-country production.\n#### 3. Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\nmaintain United States and allied partner technological leadership in semiconductor technology research, design, manufacturing, and advanced materials;\n**(2)**\nprevent adversarial capture of key chokepoints in the global semiconductor technology supply chain;\n**(3)**\ncoordinate with allied and partner nations to expand and enhance semiconductor technology protection;\n**(4)**\nensure that United States-origin technology and intellectual property, including the direct products of United States-origin technology, do not contribute to the Chinese Communist Party\u2019s military modernization, human rights abuses, and pursuit of technological dominance over the United States and its allies and partners; and\n**(5)**\npromote resilient, secure, and trusted semiconductor supply chains among United States allies and partners.\n#### 4. Multilateral semiconductor technology supply chain coordination\n##### (a) In general\nThe Secretary of State shall coordinate with governments of countries that maintain significant capabilities in semiconductor technology research, design, manufacturing, materials, equipment, or equipment subsystems and components to establish coordinated and expanded approaches for protecting critical semiconductor technologies from acquisition by the Chinese Communist Party and other foreign adversaries of the United States and its allies and partners.\n##### (b) Coordination objectives\nIn carrying out subsection (a), the Secretary of State shall seek to achieve\u2014\n**(1)**\nalignment of export control policies regarding semiconductor technology manufacturing equipment, including lithography systems, deposition equipment, etching tools, thermocompression bonding equipment, resist processing tools, chemical mechanical planarization tools, cleaning tools, handling tools, assembly, packaging, and test tools, and inspection systems and the critical subcomponents needed to produce such equipment;\n**(2)**\nexpanded restrictions on semiconductor technology design tools, intellectual property transfers, equipment servicing, and technical assistance that could enable indigenous semiconductor technology development capabilities in countries of concern;\n**(3)**\nharmonized approaches to controlling dual-use semiconductor technology materials, including photoresists, specialty gases, and advanced substrates;\n**(4)**\njoint monitoring, enforcement, and administration mechanisms to prevent circumvention of semiconductor technology controls through third-country entities as well as prevent foreign backfilling of restricted items;\n**(5)**\ninformation sharing regarding semiconductor technology transfer risks, end-user verification, and supply chain security threats; and\n**(6)**\nestablishment of trusted supplier networks for critical semiconductor technology components and manufacturing services.\n##### (c) Consequences for non-Cooperation\n**(1) Assessment of cooperation**\nThe Secretary of State, in consultation with the Secretary of Commerce, shall regularly assess the extent to which countries engaged pursuant to subsection (a) are implementing measures consistent with United States policy described in section 3.\n**(2) Determination of insufficient security measures**\nIf the Secretary of State determines that a country engaged with pursuant to subsection (a) is not implementing security measures sufficient to fully prevent semiconductor technology transfer to countries of concern, the Secretary shall\u2014\n**(A)**\nprovide a detailed explanation of the specific deficiencies in the country\u2019s semiconductor technology protection measures;\n**(B)**\nrequest the Secretary of Commerce to convene a meeting of the Export Advisory Review Board to identify and execute a plan of action to address the insufficient security measures within 21 days of the Secretary of State\u2019s determination of inadequate cooperation; and\n**(C)**\nnotify the appropriate congressional committees of such determination not later than 30 days after making such determination and provide routine updates on the Export Advisory Review Board meeting request and plan of action described in subparagraph (B).\n**(3) Enhanced foreign direct product rule application**\nIn carrying out the process described in paragraph (2)(B), the Secretary of State shall provide to Export Advisory Review Board\u2014\n**(A)**\nrecommendations for the application of Foreign Direct Product Rule restrictions to semiconductor technology produced in the non-cooperating country that incorporate United States-origin technology, software, or equipment;\n**(B)**\nrecommended entities for the expansion of Entity List designations for semiconductor technology supply chain companies or research institutions in the non-cooperating country that pose technology transfer risks; and\n**(C)**\nguidance on what additional steps may be needed to prevent foreign backfilling of U.S. technology in restricted sectors or entities in countries of concern.\n##### (d) Reports\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, and every 90 days thereafter, the Secretary of State shall submit to the appropriate congressional committees a report on\u2014\n**(A)**\nthe status of diplomatic engagement with key semiconductor technology-producing countries;\n**(B)**\nprogress toward achieving the coordination objectives specified in subsection (b);\n**(C)**\nany determinations of inadequate cooperation made under subsection (c); and\n**(D)**\nthe effectiveness of multilateral coordination in preventing semiconductor technology transfer to countries of concern.\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Countries of concern**\nThe term countries of concern has the meaning given the term covered nation in section 4872(f) of title 10, United States Code.\n**(3) Entity list**\nThe term Entity List means the list maintained by the Bureau of Industry and Security of the Department of Commerce and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations, or successor regulations.\n**(4) Foreign direct product rule**\nThe term Foreign Direct Product Rule means the rule exercising United States export controls on an item produced in a foreign country for shipment or transmission to another foreign country or foreign person, if the item\u2014\n**(A)**\nis produced using technology or software that is otherwise subject to the jurisdiction of the United States;\n**(B)**\nis produced with the use of a plant or major component of a plant that\u2014\n**(i)**\nis located outside the United States; and\n**(ii)**\nhas been created using the technology or software described in subparagraph (A); or\n**(C)**\ncontains, is commingled with, is bundled with, is drawn from, or is produced by an item described in subparagraph (A) or (B).\n**(5) Semiconductor technology**\nThe term semiconductor technology includes\u2014\n**(A)**\nintegrated circuits, microprocessors, and memory devices;\n**(B)**\nsemiconductor manufacturing equipment and tools, including subsystems and components;\n**(C)**\nsemiconductor design software and intellectual property;\n**(D)**\nsemiconductor materials and specialty chemicals;\n**(E)**\ntesting, assembly, and packaging equipment; and\n**(F)**\nany technology, component, or service that is essential to semiconductor design, manufacturing, or testing processes.",
      "versionDate": "2025-11-17",
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
        "updateDate": "2025-11-25T19:44:13Z"
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
      "date": "2025-11-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6058ih.xml"
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
      "title": "STRIDE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STRIDE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semiconductor Technology Resilience, Integrity, and Defense Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-20T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for multilateral semiconductor technology supply chain coordination, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-20T08:18:27Z"
    }
  ]
}
```
