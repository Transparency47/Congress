# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7632?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7632
- Title: SHADOW Act
- Congress: 119
- Bill type: HR
- Bill number: 7632
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-04-16T16:20:22Z
- Update date including text: 2026-04-16T16:20:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 46 - 0.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-03-26 - Committee: Committee Consideration and Mark-up Session Held
- 2026-03-26 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 46 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7632",
    "number": "7632",
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
    "title": "SHADOW Act",
    "type": "HR",
    "updateDate": "2026-04-16T16:20:22Z",
    "updateDateIncludingText": "2026-04-16T16:20:22Z"
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 46 - 0.",
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
      "actionDate": "2026-02-20",
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
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
            "date": "2026-03-26T16:22:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-02-20T16:32:30Z",
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
      "sponsorshipDate": "2026-02-20",
      "state": "MA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
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
      "sponsorshipDate": "2026-02-23",
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
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7632ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7632\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Self (for himself, Mr. Keating , and Mr. Sherman ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo designate a Coordinator for hybrid warfare accountability, require the Secretary of State to submit a report identifying Chinese entities materially supporting Russia\u2019s defense industrial base and recommending appropriate sanctions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Hybrid Activities Defense and Operations for the West Act or the SHADOW Act .\n#### 2. Assessment and engagement relating to hybrid warfare activities against United States interests\nThe Secretary of State shall\u2014\n**(1)**\nin consultation with other relevant officials of the Department of State, assess the persistent and growing threat of hybrid warfare activities, including in Europe against United States interests as a matter of importance to the foreign policy of the United States;\n**(2)**\nengage diplomatically with foreign governments including in Europe to promote transatlantic cooperation in countering and addressing hybrid warfare activities that may threaten transatlantic stability, the security of United States citizens and institutions abroad, and the stability of the North Atlantic Treaty Organization (NATO); and\n**(3)**\nencourage closer United States information sharing with NATO allies on hybrid warfare activities, including on Chinese and Russian cyber campaigns including in Europe, through measures such as the adoption of common attribution language, shared red lines for disruptive activities, coordinated non-kinetic response options, and common definitions for gray zone activities, to strengthen shared understanding, preparedness, and mitigation efforts.\n#### 3. Coordinator for hybrid warfare accountability\n##### (a) Designation\nNot later than 30 days after the date of the enactment of this Act, the Secretary of State shall designate a senior official from among existing officers or employees of the Department of State, who shall report to the Under Secretary for Political Affairs, to serve as the principal official responsible for coordinating all United States interagency and allied engagement on hybrid warfare (in this section referred to as the Coordinator ).\n##### (b) Duties\nThe Coordinator shall oversee the efforts of the Department of State relating to the following:\n**(1)**\nAssessing, integrating, and disseminating information on hybrid warfare activities, including Chinese and Russian-linked efforts as well as those of non-state actors, for use in diplomatic engagement, interagency strategy, and allied coordination.\n**(2)**\nIdentifying analytic and operational gaps in the United States understanding of hybrid threats and developing recommendations to address those gaps.\n**(3)**\nCoordinating within NATO and among NATO allies, as well as with other key partners, such as South Korea, Japan, Australia, and New Zealand, to facilitate timely information sharing, including the exchange of assessments, and to support the development of aligned response strategies among allied and partner countries.\n**(4)**\nSupporting resilience and de-risking efforts with allies and partners in sectors vulnerable to foreign coercion, including critical infrastructure, telecommunications, energy, and strategic materials.\n##### (c) Plan\nNot later than 60 days after the designation of a Coordinator pursuant to subsection (a), the Secretary of State shall submit to the appropriate congressional committees\u2014\n**(1)**\nthe name of the official designated as the Coordinator; and\n**(2)**\na strategy describing the manner in which the Coordinator will support the Department of State and interagency efforts to address hybrid threats.\n##### (d) Report\nNot later than 1 year after the designation of a Coordinator pursuant to subsection (a), and annually thereafter for 3 years, the Coordinator shall submit to the appropriate congressional committees a report detailing the following:\n**(1)**\nKey assessments and findings on hybrid warfare activities.\n**(2)**\nProgress on interagency and allied coordination.\n**(3)**\nMeasures taken to support resilience and de-risking efforts with allies and partners.\n##### (e) Form\nEach report required by this section may be submitted in classified form as necessary to protect sensitive sources and methods.\n##### (f) Hybrid warfare activities defined\nFor purposes of this section, the term hybrid warfare activities refers to the use of a combination of military and non-military, as well as covert and overt, means to influence, destabilize, or undermine United States interests abroad. Such activities may include the following among others:\n**(1)**\nInformation campaigns targeting United States interests.\n**(2)**\nCyber-attacks.\n**(3)**\nEconomic pressure, coercion, or manipulation.\n**(4)**\nDeployment of operatives, irregular armed groups, and uses of regular forces in ways that threaten United States or allied interests.\n**(5)**\nThe deliberate weaponization or exploitation of migration flows to exert political, economic, or security pressure on the United States or its allies.\n**(6)**\nSabotage, damage, or disruption of critical onshore or offshore infrastructure, including energy, telecommunications, or undersea infrastructure.\n**(7)**\nTargeted assassinations or attempted assassinations undertaken as part of a broader effort to intimidate, destabilize, or coerce.\n#### 4. Report on the nexus of Chinese entities that materially support Russia\u2019s defense industrial base\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the Coordinator designated pursuant to section 3(a), in consultation with the relevant heads of other Federal departments and offices, shall submit to the appropriate congressional committees a report that\u2014\n**(1)**\nidentifies each Chinese entity the Coordinator determines materially supports Russia\u2019s defense industrial base; and\n**(2)**\nrecommends sanctions, export controls, or other measures the Coordinator determines are necessary or appropriate to address such support.\n##### (b) Form\nThe report required by subsection (a) shall be submitted in unclassified form, but may include a classified annex only for the protection of intelligence sources and methods relating to the matters contained in such report.\n##### (c) Publication\nThe Secretary of State shall publish on a publicly available website of the Department of State the unclassified portion of the report required by subsection (a).\n#### 5. Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-02-27T16:49:54Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7632ih.xml"
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
      "title": "SHADOW Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SHADOW Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strategic Hybrid Activities Defense and Operations for the West Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate a Coordinator for hybrid warfare accountability, require the Secretary of State to submit a report identifying Chinese entities materially supporting Russia's defense industrial base and recommending appropriate sanctions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T06:33:37Z"
    }
  ]
}
```
