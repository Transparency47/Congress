# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2422?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2422
- Title: ICBM Act
- Congress: 119
- Bill type: S
- Bill number: 2422
- Origin chamber: Senate
- Introduced date: 2025-07-23
- Update date: 2025-12-05T22:48:57Z
- Update date including text: 2025-12-05T22:48:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-23: Introduced in Senate
- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-23: Introduced in Senate

## Actions

- 2025-07-23 - IntroReferral: Introduced in Senate
- 2025-07-23 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-23",
    "latestAction": {
      "actionDate": "2025-07-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2422",
    "number": "2422",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "ICBM Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:57Z",
    "updateDateIncludingText": "2025-12-05T22:48:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-23",
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
        "item": {
          "date": "2025-07-23T22:15:49Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-07-23",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2422is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2422\nIN THE SENATE OF THE UNITED STATES\nJuly 23, 2025 Mr. Markey (for himself, Mr. Sanders , Mr. Merkley , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo pause development of the new Sentinel program, extend the life of the Minuteman III, and redirect savings from Sentinel toward the Department of Education, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Investing in Children Before Missiles Act of 2025 or the ICBM Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nAccording to the Congressional Budget Office, the projected cost to sustain and modernize the United States nuclear arsenal, as of 2025, is $946 billion over the 2025\u20132034 period, or an average of about $95 billion a year , and nuclear forces account for 8.4 percent of the total 10-year cost of the plans for national defense outlined in the President\u2019s 2025 budget submission.\n**(2)**\nIn September 2020, the Air Force awarded a sole-source contract to Northrop Grumman for the ground-based strategic deterrent program (now called Sentinel intercontinental ballistic missile program), raising concerns that the absence of competition for the award would result in higher than projected costs to United States taxpayers. The program is intended to replace 400 deployed Minuteman III missiles with more than 600 new missiles, to allow for test flights and spares.\n**(3)**\nThe Sentinel program has encountered significant cost growth and schedule delays in recent years, and the full extent of both remains uncertain as the Department of Defense is currently restructuring the program.\n**(4)**\nIn January 2024, increases in the total costs of the Sentinel program triggered a review under chapter 325 of title 10, United States Code (commonly known as the Nunn-McCurdy Act ), which is intended to determine whether a program that has experienced large cost overruns should continue, and what, if any, changes should be made to control costs.\n**(5)**\nIn July 2024, the Department of Defense completed that review and released a new estimate of total costs for the program of $141,000,000,000 in constant 2020 dollars, which is 81 percent (or $63,000,000,000) larger than the program\u2019s baseline 2020 estimate of $78,000,000,000. The total estimated life cycle cost of the Sentinel program (not including warheads) was estimated by the Department of Defense to be $260,000,000,000 in 2020 and is undoubtedly higher today.\n**(6)**\nIn May 2025, the Air Force announced the Sentinel program will likely predominantly require digging fresh missile silos, a significant change from previous plans to reuse existing silos and a move that would likely cause further significant cost increases and schedule delays.\n**(7)**\nAccording to public reports, officials of the Department of Defense expect the restructuring effort to delay the Sentinel program by several years. The Department of Defense\u2019s 2025 budget plans called for initial operating capability to be achieved in May 2029, a date that, as of the date of the enactment of this Act, looks unachievable. The Air Force is considering contingency plans that would extend the life of Minuteman III intercontinental ballistic missiles by 11 more years to 2050 if delays continue to plague the Sentinel missiles intended to replace them.\n**(8)**\nThe National Nuclear Security Administration is developing a replacement intercontinental ballistic missile warhead, the W87\u20131, for the Sentinel and expanding plutonium pit production to build new warhead cores, costing at least $14,000,000,000 and $18,000,000,000, respectively.\n**(9)**\nEven in the absence of an intercontinental ballistic missile leg of the triad, the United States would have an assured retaliatory capability in the form of multiple ballistic missile submarines, which are virtually undetectable, and there are no known, near-term credible threats to the survivability of the ballistic missile submarine force. The survivability of the submarine force will be enhanced as the Department of Defense moves to replace the Ohio class ballistic submarine fleet with the new Columbia class ballistic missile fleet.\n**(10)**\nWhile intercontinental ballistic missiles have historically been the most responsive leg of the United States nuclear triad, advances in ballistic missile submarine communications to allow for the dissemination of emergency action messages in wartime have negated that advantage.\n**(11)**\nIntercontinental ballistic missiles based in silos are vulnerable and, once launched, cannot be recalled, leaving decisionmakers with mere minutes to decide whether to launch the missiles before they are destroyed, known as a posture of launch on warning or launch under attack in the face of a perceived nuclear attack, greatly increasing the risk of a national leader initiating a nuclear war by mistake.\n**(12)**\nUnder current policy, the President has the authority\u2014\n**(A)**\nto launch United States nuclear weapons first and is not limited to retaliation;\n**(B)**\nto launch nuclear weapons under warning of attack, rather than waiting for evidence of attack; and\n**(C)**\nto launch nuclear weapons on the President's sole order.\n**(13)**\nFalse alarms have happened multiple times and can happen again. For example, in 1980, a false alarm was reported to the Assistant to the President for National Security Affairs and was almost reported up to President Jimmy Carter as a real attack but was luckily identified in time. Recent Pentagon reports have found that, as a result of cyberattacks, the President could be faced with false warnings of attack or lose the ability to control nuclear weapons.\n**(14)**\nIn 1983, Stanislav Petrov, a former lieutenant colonel of the Soviet Air Defense Forces correctly identified a false warning in an early warning system that showed several United States incoming nuclear missiles, preventing Soviet leaders from launching a retaliatory response, earning Colonel Petrov the nickname the man who saved the world .\n**(15)**\nFormer Secretary of Defense William J. Perry wrote that the ground-based leg of the nuclear triad is destabilizing because it invites an attack and intercontinental ballistic missiles are some of the most dangerous weapons in the world and could even trigger an accidental nuclear war .\n**(16)**\nGeneral James Cartwright, former vice chair of the Joint Chiefs of Staff and former Commander of the United States Strategic Command, wrote, with Secretary Perry, [T]he greatest danger is not a Russian bolt but a US blunder\u2014that we might accidentally stumble into nuclear war. As we make decisions about which weapons to buy, we should use this simple rule: If a nuclear weapon increases the risk of accidental war and is not needed to deter an intentional attack, we should not build it. \u2026 Certain nuclear weapons, such as \u2026 the [intercontinental ballistic missile], carry higher risks of accidental war that, fortunately, we no longer need to bear. We are safer without these expensive weapons, and it would be foolish to replace them. .\n**(17)**\nGeneral George Lee Butler, the former Commander-in-Chief of the Strategic Air Command and subsequently Commander-in-Chief of the United States Strategic Command, said, I would have removed land-based missiles from our arsenal a long time ago. I\u2019d be happy to put that mission on the submarines. So, with a significant fraction of bombers having a nuclear weapons capability that can be restored to alert very quickly, and with even a small component of Trident submarines\u2014with all those missiles and all those warheads on patrol\u2014it\u2019s hard to imagine we couldn\u2019t get by. .\n**(18)**\nWhile a sudden bolt from the blue first strike from a near-peer nuclear adversary is a highly unlikely scenario, extending the Minuteman III would maintain the purported role of the intercontinental ballistic missile leg of the triad to absorb such an attack.\n#### 3. Statement of policy on Minuteman III, Sentinel, and education funding\nIt is the policy of the United States that\u2014\n**(1)**\nas of the date of the enactment of this Act, the Sentinel program is significantly over budget and behind schedule and should be paused and reevaluated for need and technical merit;\n**(2)**\nthe operational life of the Minuteman III missile should be safely extended until at least 2050; and\n**(3)**\ninvestments in the Department of Education are a better use of United States taxpayer resources than continuing with the current Sentinel program.\n#### 4. Availability of funds for education instead of Sentinel\n##### (a) Transfer from Department of Defense\nThe Secretary of Defense shall transfer all amounts appropriated to the Department of Defense for the research, development, test, and evaluation of the Sentinel program, and available for obligation as of the date of the enactment of this Act, to the Department of Education to carry out part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ).\n##### (b) Transfer from National Nuclear Security Administration\nThe Secretary of Energy shall transfer all amounts appropriated to the National Nuclear Security Administration for the W87\u20131 warhead modification program, and available for obligation as of the date of the enactment of this Act, to the Department of Education to carry out part A of title I of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311 et seq. ).\n#### 5. Prohibition on use of funds for ground-based strategic deterrent program and W87\u20131 warhead modification program\nNone of the funds authorized to be appropriated or otherwise made available for fiscal year 2026 may be obligated or expended for the Sentinel program or the W87\u20131 warhead modification program.\n#### 6. Independent study on extension of Minuteman III intercontinental ballistic missiles\n##### (a) Independent study\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Defense shall seek to enter into a contract with the National Academy of Sciences to conduct a study on extending the life of Minuteman III intercontinental ballistic missiles to 2050 or beyond.\n##### (b) Staffing\n**(1) Experts**\nThe conduct of the study required by subsection (a) shall include input from a wide variety of technical and subject matter experts.\n**(2) Prohibition on certain Air Force employees**\nNo member or former member of the Air Force or employee or former employee of the Department of the Air Force who is or was paid for work relating to the Sentinel program may participate in the conduct of the study required by subsection (a).\n##### (c) Elements\nThe study required by subsection (a) shall address the following:\n**(1)**\nA comparison of the costs through 2050 of\u2014\n**(A)**\nextending the life of Minuteman III intercontinental ballistic missiles; and\n**(B)**\ndeploying the Sentinel program.\n**(2)**\nAn analysis of opportunities to incorporate technologies into the Minuteman III intercontinental ballistic missile program as part of a service life extension program that could also be incorporated in a possible future Sentinel program, including, at a minimum, opportunities to increase resilience against adversary missile defenses.\n**(3)**\nAn analysis of the benefits and risks of incorporating sensors and nondestructive testing methods and technologies to reduce destructive testing requirements and increase the service life and number of Minuteman III missiles through 2050.\n**(4)**\nAn analysis and validation of the methods used to estimate the operational service life of Minuteman II and Minuteman III motors, taking into account the test and launch experience of motors retired after the operational service life of such motors in the rocket systems launch program.\n**(5)**\nAn analysis of the risks and benefits of alternative methods of estimating the operational service life of Minuteman III motors, such as those methods based on fundamental physical and chemical processes and nondestructive measurements of individual motor properties.\n**(6)**\nAn analysis of risks, benefits, and costs of configuring a Trident II D5 submarine-launched ballistic missile for deployment in a Minuteman III silo.\n**(7)**\nAn analysis of the impacts of the estimated service life of the Minuteman III force associated with decreasing the deployed intercontinental ballistic missiles delivery vehicle force from 400 to 300 or less.\n**(8)**\nAn assessment of the extent to which the Columbia class ballistic missile submarines will possess features that will enhance the current invulnerability of ballistic missile submarines of the United States to future antisubmarine warfare threats.\n**(9)**\nAn analysis of the extent to which an extension of the life of the Minuteman III missiles would impact the decision of the Russian Federation to target intercontinental ballistic missiles of the United States in a crisis, compared to proceeding with the Sentinel.\n**(10)**\nA best case estimate of what percentage of the strategic forces of the United States would survive a counterforce strike from the Russian Federation, broken down by intercontinental ballistic missiles, ballistic missile submarines, and heavy bomber aircraft.\n**(11)**\nThe benefits, risks, and costs of relying on the W\u201378 warhead for either the Minuteman III or a new Sentinel missile as compared to proceeding with the W\u201387 life extension.\n**(12)**\nThe benefits, risks, and costs of adding additional launchers on submarines or uploading submarine-launched ballistic missiles with additional warheads to compensate for a reduced deployment of intercontinental ballistic missiles of the United States.\n##### (d) Report required\n**(1) Submission to Department of Defense**\nNot later than 180 days after the date of the enactment of this Act, the National Academy of Sciences shall submit to the Secretary of Defense a report containing the results of the study conducted under subsection (a).\n**(2) Submission to Congress**\nNot later than 210 days after the date of the enactment of this Act, the Secretary shall transmit to the appropriate congressional committees the report required by paragraph (1), without change.\n**(3) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.\n**(4) Appropriate congressional committees defined**\nIn this subsection, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services, the Committee on Foreign Relations, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Armed Services, the Committee on Foreign Affairs, and the Committee on Appropriations of the House of Representatives.",
      "versionDate": "2025-07-23",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-23",
        "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4685",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ICBM Act",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-12T15:09:31Z"
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
      "date": "2025-07-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2422is.xml"
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
      "title": "ICBM Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ICBM Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investing in Children Before Missiles Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-02T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to pause development of the new Sentinel program, extend the life of the Minuteman III, and redirect savings from Sentinel toward the Department of Education, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T03:18:37Z"
    }
  ]
}
```
