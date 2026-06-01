# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4458
- Title: COUNTER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4458
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2025-12-05T22:06:44Z
- Update date including text: 2025-12-05T22:06:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4458",
    "number": "4458",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "COUNTER Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:06:44Z",
    "updateDateIncludingText": "2025-12-05T22:06:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-16T14:03:25Z",
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
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
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
      "sponsorshipDate": "2025-11-04",
      "state": "VA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-11-04",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4458ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4458\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Mr. Krishnamoorthi (for himself and Mr. LaHood ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Permanent Select Committee on Intelligence , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of State and the Secretary of Defense to develop a strategy in response to the global basing intentions of the People\u2019s Republic of China.\n#### 1. Short titles\nThis Act may be cited as the Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025 or the COUNTER Act of 2025 .\n#### 2. Findings\nAccording to multiple sources, including the 2024 annual report to Congress, titled Military and Security Developments Involving the People\u2019s Republic of China and known informally as the China Military Power Report \u2014\n**(1)**\nthe PRC is seeking to expand its overseas logistics and basing infrastructure to allow the PLA to project and sustain military power at greater distances;\n**(2)**\na global PLA logistics network could give the PRC increased capabilities to surveil or disrupt United States military operations;\n**(3)**\nin August 2017, the PRC officially opened the first overseas PLA military base near the commercial port of Doraleh in Djibouti;\n**(4)**\nin 2019, the PRC also attempted to acquire strategically important port infrastructure at Subic Bay in the Philippines, but was stopped by the Government of the United States, the Philippines, and Japan, and by private investors;\n**(5)**\nin April 2025, officials from the PRC and Cambodia officially inaugurated the China-Cambodia Ream Naval Base Joint Support and Training Center and celebrated the expansion of port facilities at Ream Naval Base, some of which appear to have been reserved for the use of PRC ships that have been continuously stationed at Ream Naval Base since December 2023; and\n**(6)**\nin addition to the base in Djibouti and the PRC's access to the port at the Ream Naval Base in Cambodia, the PRC is likely pursuing access to additional military facilities to support naval, air, and ground forces projection in many countries.\n#### 3. Sense of Congress\nWhile the executive branch has undertaken case-by-case efforts to forestall the establishment of new PRC permanent military presence in several countries, it is the sense of Congress that future efforts to counter the PRC's global basing intentions must\u2014\n**(1)**\nproceed with the urgency required to address the strategic implications of the PRC\u2019s actions;\n**(2)**\nreflect sufficient interagency coordination with respect to a problem that necessitates a whole-of-government approach;\n**(3)**\nensure that the United States Government maintains a proactive posture rather than a reactive posture in order to maximize strategic decision space;\n**(4)**\nidentify a comprehensive menu of actions that would be influential in shaping a partner\u2019s decision making regarding giving the PRC military access to its sovereign territory;\n**(5)**\nappropriately prioritize the subject of the PRC's global basing intentions within the context of the overall United States strategic competition with the PRC;\n**(6)**\nconsider how the PRC uses commercial and scientific cooperation as a guise for establishing access for the PLA and other PRC security forces in foreign countries;\n**(7)**\nfactor in the potential contributions of key allies and partners to help respond to the PRC's pursuit of global basing, many of which\u2014\n**(A)**\nhave historic ties and influence in many of the geographic areas the PRC is targeting for potential future bases; and\n**(B)**\nrely on the same basic intelligence picture to form our baseline understanding of the PRC\u2019s global intentions;\n**(8)**\nestablish and ensure sufficient resourcing for enduring organizational structures and security and foreign assistance and cooperation efforts to effectively address the issue of PRC global basing intentions; and\n**(9)**\nensure that future force posture, freedom of movement, and other interests of the United States and our allies are not jeopardized by the continued expansion of PRC bases.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Armed Services of the Senate ;\n**(C)**\nthe Select Committee on Intelligence of the Senate ;\n**(D)**\nthe Committee on Appropriations of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on Armed Services of the House of Representatives ;\n**(G)**\nthe Permanent Select Committee on Intelligence of the House of Representatives ; and\n**(H)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) PLA**\nThe term PLA means the People's Liberation Army of the PRC.\n**(3) PRC**\nThe term PRC means the People's Republic of China.\n**(4) PRC global basing**\nThe term PRC global basing means the establishment of physical locations outside the geographic boundaries of the PRC where the PRC maintains some element of the People\u2019s Liberation Army, PRC intelligence or security forces, or infrastructure designed to support the presence of PRC military, intelligence, or security forces, for the purposes of potential power projection.\n#### 5. Assessment of executive branch's C\u2013PRC global basing strategy\n##### (a) Assessment\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit an intelligence assessment, in classified form, if needed, to the appropriate congressional committees. The assessment shall analyze the risk posed by PRC global basing to the United States or to any United States allies with respect to their ability to project power, maintain freedom of movement, and protect other interests as a function of the PRC's current or potential locations identified pursuant to subsection (b)(2)(A).\n##### (b) Strategy\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall submit a strategy to the appropriate congressional committees that contains the information described in paragraph (2).\n**(2) Contents**\nThe strategy required under paragraph (1) shall\u2014\n**(A)**\nidentify not fewer than 5 locations that pose the greatest potential risks, as identified in the assessment required under subsection (a), where the PRC maintains a physical presence, or is suspected to be seeking a physical presence, which could ultimately transition into a PRC global base;\n**(B)**\ninclude a comprehensive listing of executive branch entities currently involved in addressing aspects of PRC global basing, including estimated programmatic and personal resource requirements on an agency-by-agency basis to effectively address the issue of PRC global basing intentions, and any relevant resource constraints;\n**(C)**\ndescribe in detail all executive branch efforts to mitigate the impacts to the national interests of the United States and partner countries of the locations referred to in subparagraph (A) and prevent the PRC from establishing new global bases, including with resources described in subparagraph (B); and\n**(D)**\nfor each of the locations referred to in subparagraph (A), identify the actions by the United States or its allies that would be most effective in ensuring the respective foreign governments terminate plans for hosting a PRC base.\n##### (c) Task force\nNot later than 90 days after submitting the strategy described in subsection (b), the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall establish an interagency task force\u2014\n**(1)**\nto implement the strategy described in section (b) to counter the PRC\u2019s efforts at the locations of chief concern; and\n**(2)**\nto identify mitigation measures that would prevent the PRC from establishing new bases in locations beyond the locations of chief concern identified pursuant to subsection (b)(2)(A).\n##### (d) Quadrennial reviews and reports\nNot later than 4 years after the submission of the strategy required under subsection (b), and not less frequently than once every 4 years thereafter, the Secretary of State, in coordination with the Secretary of Defense, the Director of National Intelligence, and other appropriate senior Federal officials, shall\u2014\n**(1)**\nconduct a review of the Executive Branch\u2019s strategy and overall approach in response to the PRC global basing intentions; and\n**(2)**\nsubmit the results of such review, including the information described in subsection (b)(2), to the appropriate congressional committees.",
      "versionDate": "2025-07-16",
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
        "actionDate": "2025-06-18",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 96."
      },
      "number": "1731",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COUNTER Act of 2025",
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
        "updateDate": "2025-07-29T22:18:03Z"
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
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4458ih.xml"
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
      "title": "COUNTER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:53:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COUNTER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of State and the Secretary of Defense to develop a strategy in response to the global basing intentions of the People's Republic of China.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:48:27Z"
    }
  ]
}
```
