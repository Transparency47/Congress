# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5793
- Title: Eastern Flank Strategic Partnership Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5793
- Origin chamber: House
- Introduced date: 2025-10-17
- Update date: 2026-04-06T20:04:28Z
- Update date including text: 2026-04-06T20:04:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-17: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-17: Introduced in House

## Actions

- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Introduced in House
- 2025-10-17 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-17 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-17",
    "latestAction": {
      "actionDate": "2025-10-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5793",
    "number": "5793",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "W000795",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Wilson, Joe [R-SC-2]",
        "lastName": "Wilson",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Eastern Flank Strategic Partnership Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-06T20:04:28Z",
    "updateDateIncludingText": "2026-04-06T20:04:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-17",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Armed Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-17",
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
          "date": "2025-10-17T18:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-17T18:04:05Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "TN"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "OH"
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
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5793ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5793\nIN THE HOUSE OF REPRESENTATIVES\nOctober 17, 2025 Mr. Wilson of South Carolina (for himself and Mr. Cohen ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Armed Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo strengthen strategic defense cooperation between the United States and NATO allies on the Eastern Flank, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Eastern Flank Strategic Partnership Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe frontline North Atlantic Treaty Organization (NATO) allies of Bulgaria, Estonia, Finland, Hungary, Latvia, Lithuania, Poland, Romania, and Slovakia play a critical role in regional and transatlantic security.\n**(2)**\nThose NATO allies have demonstrated consistent commitments to NATO defense spending targets, support for Ukraine, and forward deployments to deter Russian aggression.\n**(3)**\nThose NATO allies are on the front line of deterring and defending against threats from Russia and Belarus, and require continued United States coordination, defense cooperation, and security assistance.\n**(4)**\nUkraine is on the front line of United States and NATO security, fighting to defend itself against Russian aggression that could also be turned upon those same NATO allies.\n**(5)**\nThe United States possesses existing authorities and tools, including assistance under the Foreign Military Financing program under section 23 of the Arms Export Control Act ( 22 U.S.C. 2763 ), assistance under section 333 of title 10, United States Code, transfer of excess defense articles under section 516 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321j ), and the War Reserve Stocks for Allies program administered under section 514 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321h ), that can be used to enhance resilience, logistics, and interoperability with those NATO allies.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(2) Eastern Flank strategic defense partner**\nThe term Eastern Flank strategic defense partner \u2014\n**(A)**\nmeans a NATO member state that\u2014\n**(i)**\nshares a border with, or is in direct geographic proximity to, the Russian Federation, the Republic of Belarus, or Ukraine, and plays a role in the defense of NATO\u2019s Eastern Flank due to its geographic proximity to those countries;\n**(ii)**\nhas committed to allocating 5 percent of its gross domestic product annually to defense by 2035, including at least 3.5 percent for meeting core defense requirements and NATO capability targets and 1.5 percent for other defense- and security-related investments;\n**(iii)**\nhosts or supports the forward deployment of NATO military forces, including rotational deployments; and\n**(iv)**\nfaces persistent threats from hostile state actors; and\n**(B)**\nincludes Bulgaria, Estonia, Finland, Hungary, Latvia, Lithuania, Poland, Romania, and Slovakia.\n#### 4. Policy and priority for strategic defense cooperation\n##### (a) Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto recognize the critical role of Eastern Flank strategic defense partners in defending NATO\u2019s Eastern Flank, deterring aggression from hostile state actors, and advancing transatlantic security;\n**(2)**\nto prioritize cooperation with Eastern Flank strategic defense partners in the implementation of defense cooperation authorities;\n**(3)**\nto treat Eastern Flank strategic defense partners as priority recipients of security assistance under security assistance authorities; and\n**(4)**\nto support Ukraine, including with the security assistance necessary to deter Russian aggression against allies along NATO\u2019s Eastern Flank.\n##### (b) Priority\nThe Secretary of State and the Secretary of Defense shall, as appropriate and consistent with law, give priority to Eastern Flank strategic defense partners for the following:\n**(1)**\nAssistance under the Foreign Military Financing program under section 23 of the Arms Export Control Act ( 22 U.S.C. 2763 ).\n**(2)**\nAssistance under section 333 of title 10, United States Code (relating to authority to build the capacity of foreign security forces).\n**(3)**\nTransfer of excess defense articles under section 516 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321j ).\n**(4)**\nParticipation in bilateral and multilateral military exercises, interoperability training, logistics, and forward mobility planning.\n##### (c) Implementation\nThe policy established by subsection (a) and the priority established by subsection (b) shall be implemented to reinforce bilateral defense cooperation arrangements, including defense cooperation agreements, status of forces agreements, and other bilateral or multilateral agreements.\n#### 5. Stockpiling and pre-positioning of defense articles\nConsistent with operational requirements and in consultation with NATO allies, and with the goal of increasing regional deterrence and reducing strategic response time, the Secretary of Defense shall\u2014\n**(1)**\nprioritize Eastern Flank strategic defense partners under the War Reserve Stocks for Allies program administered under section 514 of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2321h ); and\n**(2)**\nconsider expanding stockpiles under such program in additional Eastern Flank strategic defense partner countries, as appropriate.\n#### 6. Congressional briefing\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense, in coordination with the Secretary of State, shall brief the appropriate congressional committees on the implementation of sections 3 and 4, including timelines, goals, and cooperative mechanisms.",
      "versionDate": "2025-10-17",
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
        "actionDate": "2025-09-19",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "2914",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Eastern Flank Strategic Partnership Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T19:48:22Z"
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
      "date": "2025-10-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5793ih.xml"
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
      "title": "Eastern Flank Strategic Partnership Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-22T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Eastern Flank Strategic Partnership Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-22T03:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To strengthen strategic defense cooperation between the United States and NATO allies on the Eastern Flank, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T03:48:16Z"
    }
  ]
}
```
