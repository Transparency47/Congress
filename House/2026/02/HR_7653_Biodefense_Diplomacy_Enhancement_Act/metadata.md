# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7653
- Title: Biodefense Diplomacy Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 7653
- Origin chamber: House
- Introduced date: 2026-02-23
- Update date: 2026-05-29T16:39:10Z
- Update date including text: 2026-05-29T16:39:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-23: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 46 - 0.
- Latest action: 2026-02-23: Introduced in House

## Actions

- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Introduced in House
- 2026-02-23 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported by the Yeas and Nays: 46 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-23",
    "latestAction": {
      "actionDate": "2026-02-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7653",
    "number": "7653",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Biodefense Diplomacy Enhancement Act",
    "type": "HR",
    "updateDate": "2026-05-29T16:39:10Z",
    "updateDateIncludingText": "2026-05-29T16:39:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 46 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-02-23",
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
      "actionDate": "2026-02-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-23",
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
            "date": "2026-03-26T16:18:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-23T17:01:25Z",
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "MA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
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
      "sponsorshipDate": "2026-03-03",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NY"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7653ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7653\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 23, 2026 Mr. Self (for himself and Mr. Keating ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo enhance diplomatic engagement on international biotechnology and biosecurity matters.\n#### 1. Short title\nThis Act may be cited as the \u201c Biodefense Diplomacy Enhancement Act \u201d.\n#### 2. Enhancement of diplomatic engagement on international biodefense, biosecurity, and biotechnology matters\n##### (a) In general\nThe Secretary of State shall advance United States foreign policy goals to improve cooperation in the field of international biodefense, biosecurity, and biotechnology matters with United States allies and partners, including by carrying out the activities described in this section.\n##### (b) Policy development\nThe Secretary of State, acting through the Under Secretary for Arms Control and International Security if the Secretary so delegates, in coordination with the Under Secretary for Political Affairs and the Permanent Representative of the United States to the North Atlantic Treaty Organization (NATO), shall pursue enhanced biodefense cooperation within NATO, including by\u2014\n**(1)**\nadvocating for the prioritization of policy development within NATO relating to biodefense, including in the areas of biotechnology, biosurveillance, and countermeasures in the field of biological threats;\n**(2)**\nidentifying and evaluating opportunities to strengthen NATO planning, policies, and activities relating to biodefense and biotechnology;\n**(3)**\npursuing potential revisions or amendments to the NATO Chemical, Biological, Radiological, and Nuclear Defence Policy to further enhance biodefense efforts in NATO;\n**(4)**\ncoordinating with NATO member states to prioritize and implement measures described in the NATO Chemical, Biological, Radiological, and Nuclear Defence Policy;\n**(5)**\nstrengthening NATO interoperability and allied forces capabilities in resilience, detection, attribution, emergency response, and recovery in the event of a weaponized biological attack;\n**(6)**\nevaluating opportunities for expanded NATO capabilities to research, develop, and deploy biotechnology for international security purposes; and\n**(7)**\npromoting adherence by NATO member states to the highest standards of safety and security in biological research.\n##### (c) Cooperation with United States allies and partners\nThe Secretary of State, acting through the Under Secretary for Arms Control and International Security if the Secretary so delegates, in coordination with the Under Secretary for Political Affairs, shall pursue international biotechnology, biosecurity, and biodefense cooperation with United States allies and partners, including\u2014\n**(1)**\nexploring potential areas of cooperation with countries that are major non-NATO allies in biotechnology, biosecurity, and biodefense matters;\n**(2)**\ncoordinating with allied and partner countries, including NATO countries, on formulation of export control policies in the field of biotechnology, including items that may be identified as dual-use items that would pose a substantial risk to national security if used for military end-uses, such as items that could enable the development of bioweapons;\n**(3)**\npromoting adherence by United States allies and partners to the highest standards of safety and security in biological research; and\n**(4)**\ncollaborating on efforts to enforce the Biological Weapons Convention.\n##### (d) Strategies\n**(1) NATO biodefense strategy**\nThe Secretary of State, acting through the Under Secretary for Arms Control and International Security if the Secretary so delegates, in coordination with the Under Secretary for Political Affairs, shall develop a strategy, to be known as the NATO Biodefense Strategy , which shall include\u2014\n**(A)**\nan assessment of current cooperation between the United States and NATO member states in biotechnology, biosurveillance, biological threat countermeasures, and other biodefense capabilities;\n**(B)**\nan identification of strategic planning and deployment gaps in NATO relating to biotechnology and biodefense;\n**(C)**\nrecommendations to address gaps identified under subparagraph (B), including through coordination with NATO member states, capability development, and coordination mechanisms; and\n**(D)**\nan assessment of current Department of State cooperation with other United States Government agencies in biodefense, biotechnology, biosecurity, biosurveillance, and biological threat countermeasures.\n**(2) International biotechnology, biosecurity, and biodefense cooperation strategy**\nThe Secretary of State, acting through the Under Secretary for Arms Control and International Security if the Secretary so delegates, in coordination with the Under Secretary for Political Affairs, shall develop a strategy, to be known as the International Biotechnology, Biosecurity, and Biodefense Cooperation Strategy , which shall include\u2014\n**(A)**\nproposals for commitments or agreements under which the United States and United States allies and partners, including countries that are major non-NATO allies, may expand cooperation on international security matters relating to biotechnology, biosecurity, and biodefense;\n**(B)**\nan assessment of the feasibility and effectiveness of coordinating export control efforts, in addition to existing export control regimes such as the Wassenaar Arrangement and the Australia Group, related to biotechnology items that may pose national security risks if used for military end uses; and\n**(C)**\nan overview of nonproliferation, anti-terrorism, demining, and related (NADR) programs and funds for the purposes of enhancing capabilities and capacities to address international biosecurity threats and recommendations for the use of Department of State programs and funds, including NADR programs and funds, to expand cooperation outlined in subparagraph (A) and increase the effectiveness of export control efforts identified in subparagraph (B).\n**(3) Limitation**\nThe strategies developed under paragraphs (1) and (2) shall be limited to addressing threats posed by biological agents and toxins as such terms are defined in section 178 of title 18, United States Code.\n##### (e) Report\n**(1) In general**\nNot later than 270 days after the date of the enactment of this Act, the Secretary of State, acting through the Under Secretary for Arms Control and International Security if the Secretary so delegates, shall submit to the appropriate congressional committees a report that contains the strategies required by subsection (d).\n**(2) Form**\nThe report required by this subsection shall be submitted in unclassified form but may include a classified annex if submitted separately from the unclassified portion.\n##### (f) Congressional briefing\nNot later than 90 days after the date of the enactment of this Act, the Under Secretary for Arms Control and International Security shall provide a briefing to the appropriate congressional committees in response to significant developments relating to\u2014\n**(1)**\nthe contents of the report required by subsection (e); and\n**(2)**\nother material developments in biotechnology and biosecurity globally that may affect United States national security interests.\n##### (g) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of the Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate;\n**(2)**\nthe term biodefense means actions to counter biological threats, reduce risks, and prepare for, respond to, and recover from biological incidents;\n**(3)**\nthe term biological threat means entities involved with, or a situation involving, a biological hazard that can potentially cause a biological incident;\n**(4)**\nthe term \u2018\u2018biosecurity\u2019\u2019 means policies, practices, and controls that reduce the risk of loss, theft, misuse, diversion of, or intentional unauthorized release of biological materials;\n**(5)**\nthe term \u2018\u2018biosurveillance\u2019\u2019 means the process of gathering, integrating, interpreting, and communicating essential information and indications related to all-hazard threats or disease activity affecting human, animal, plant, and environmental health to achieve early detection and provide early warning and contribute to overall situational awareness of the health aspects of a biological incident to support and enhance decision-making at all levels;\n**(6)**\nthe term biotechnology means the use of biological processes, organisms, or systems for manufacturing, research, or medical purposes, including genetic engineering, synthetic biology, and bioinformatics; and\n**(7)**\nthe term countries that are major non-NATO allies means countries designated pursuant to section 517 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321k ).",
      "versionDate": "2026-02-23",
      "versionType": "Introduced in House"
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
        "actionDate": "2026-05-12",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "4491",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Biodefense Diplomacy Enhancement Act",
      "type": "S"
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
            "name": "Alliances",
            "updateDate": "2026-04-23T19:12:16Z"
          },
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2026-04-23T19:12:41Z"
          },
          {
            "name": "Biological and life sciences",
            "updateDate": "2026-04-23T19:07:26Z"
          },
          {
            "name": "Chemical and biological weapons",
            "updateDate": "2026-04-23T19:07:42Z"
          },
          {
            "name": "Collective security",
            "updateDate": "2026-04-23T19:12:34Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-04-23T19:07:35Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-04-23T19:12:27Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2026-04-23T19:07:51Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2026-04-23T19:07:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-02-27T16:50:14Z"
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
      "date": "2026-02-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7653ih.xml"
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
      "title": "Biodefense Diplomacy Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T09:08:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Biodefense Diplomacy Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T09:08:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance diplomatic engagement on international biotechnology and biosecurity matters.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T09:03:38Z"
    }
  ]
}
```
