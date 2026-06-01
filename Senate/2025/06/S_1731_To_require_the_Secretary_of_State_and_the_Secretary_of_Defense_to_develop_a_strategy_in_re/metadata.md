# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1731?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1731
- Title: COUNTER Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1731
- Origin chamber: Senate
- Introduced date: 2025-05-13
- Update date: 2025-12-05T22:05:32Z
- Update date including text: 2025-12-05T22:05:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in Senate
- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 96.
- Latest action: 2025-05-13: Introduced in Senate

## Actions

- 2025-05-13 - IntroReferral: Introduced in Senate
- 2025-05-13 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 96.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1731",
    "number": "1731",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "COUNTER Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:05:32Z",
    "updateDateIncludingText": "2025-12-05T22:05:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 96.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-13",
      "committees": {
        "item": [
          {
            "name": "Intelligence (Select) Committee",
            "systemCode": "slin00"
          },
          {
            "name": "Foreign Relations Committee",
            "systemCode": "ssfr00"
          }
        ]
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-13",
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
            "date": "2025-06-18T18:16:37Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-13T18:48:48Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "NE"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "VA"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1731is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1731\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Coons (for himself, Mr. Ricketts , Mr. Kaine , Mr. Cornyn , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the Secretary of State and the Secretary of Defense to develop a strategy in response to the global basing intentions of the People\u2019s Republic of China.\n#### 1. Short titles\nThis Act may be cited as the Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025 or the COUNTER Act of 2025 .\n#### 2. Findings\nAccording to multiple sources, including the 2024 annual report to Congress, titled Military and Security Developments Involving the People\u2019s Republic of China and known informally as the China Military Power Report \u2014\n**(1)**\nthe PRC is seeking to expand its overseas logistics and basing infrastructure to allow the PLA to project and sustain military power at greater distances;\n**(2)**\na global PLA logistics network could disrupt United States military operations as the PRC\u2019s global military objectives evolve;\n**(3)**\nin August 2017, the PRC officially opened the first overseas PLA military base near the commercial port of Doraleh in Djibouti;\n**(4)**\nin June 2022, the PRC and Cambodia hosted a ceremony to mark the groundbreaking on PRC-built upgrades to Ream Naval Base, including a joint logistics and training center and a pier to accommodate larger ships;\n**(5)**\nofficials from Cambodia and the PRC officially inaugurated expanded port features at the Ream Naval Base in April 2025; and\n**(6)**\nin addition to the base in Djibouti and the PRC's access to the port at the Ream Naval Base in Cambodia, the PRC is likely pursuing access to additional military facilities to support naval, air, and ground forces projection in many countries, including Angola, Bangladesh, Burma, Cuba, Equatorial Guinea, Gabon, Indonesia, Kenya, Mozambique, Namibia, Nigeria, Pakistan, Papua New Guinea, Seychelles, Solomon Islands, Sri Lanka, Tajikistan, Tanzania, Thailand, and the United Arab Emirates.\n#### 3. Sense of Congress\nWhile the executive branch has undertaken case-by-case efforts to forestall the establishment of new PRC bases in several countries, it is the sense of Congress that future efforts to counter the PRC's global basing intentions must\u2014\n**(1)**\nproceed with the urgency required to address the strategic implications of the PRC\u2019s actions;\n**(2)**\nreflect sufficient interagency coordination with respect to a problem that necessitates a whole-of-government approach;\n**(3)**\nensure that the United States Government maintains a proactive posture rather than a reactive posture in order to maximize strategic decision space;\n**(4)**\nidentify a comprehensive menu of actions that would be influential in shaping a partner\u2019s decision making regarding giving the PRC military access to its sovereign territory;\n**(5)**\nappropriately prioritize the subject of the PRC's global basing intentions within the context of the overall United States strategic competition with the PRC;\n**(6)**\nfactor in the potential contributions of key allies and partners to help respond to the PRC's pursuit of global basing, many of which\u2014\n**(A)**\nhave historic ties and influence in many of the geographic areas the PRC is targeting for potential future bases; and\n**(B)**\nrely on the same basic intelligence picture to form our baseline understanding of the PRC\u2019s global intentions;\n**(7)**\nestablish and ensure sufficient resourcing for enduring organizational structures to effectively address the issue of PRC global basing intentions; and\n**(8)**\nensure that future force posture, freedom of movement, and other interests of the United States and our allies are not jeopardized by the continued expansion of PRC bases.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Armed Services of the Senate ;\n**(C)**\nthe Select Committee on Intelligence of the Senate ;\n**(D)**\nthe Committee on Appropriations of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on Armed Services of the House of Representatives ;\n**(G)**\nthe Permanent Select Committee on Intelligence of the House of Representatives ; and\n**(H)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) PLA**\nThe term PLA means the People's Liberation Army of the PRC.\n**(3) PRC**\nThe term PRC means the People's Republic of China.\n**(4) PRC global basing**\nThe term PRC global basing means the establishment of physical locations outside the geographic boundaries of the PRC where the PRC maintains some element of the People\u2019s Liberation Army, PRC intelligence or security forces, or infrastructure designed to support the presence of PRC military, intelligence, or security forces, for the purposes of potential power projection.\n#### 5. Assessment of executive branch's C\u2013PRC global basing strategy\n##### (a) Assessment\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit an intelligence assessment, in classified form, if needed, to the appropriate congressional committees. The assessment shall analyze the risk posed by PRC global basing to the United States or to any United States allies with respect to their ability to project power, maintain freedom of movement, and protect other interests as a function of the PRC's current or potential locations identified pursuant to subsection (b)(2)(A).\n##### (b) Strategy\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall submit a strategy to the appropriate congressional committees that contains the information described in paragraph (2).\n**(2) Contents**\nThe strategy required under paragraph (1) shall\u2014\n**(A)**\nidentify not fewer than 5 locations of chief concern where the PRC maintains a physical presence, or is suspected to be seeking a physical presence, which could ultimately transition into a PRC global base;\n**(B)**\ninclude a comprehensive listing of executive branch entities currently involved in addressing aspects of PRC global basing, including any resource or personnel constraints limiting the ability to effectively address the issue of PRC global basing intentions;\n**(C)**\ndescribe in detail all executive branch efforts\u2014\n**(i)**\nto mitigate the impacts of the locations referred to in subparagraph (A); or\n**(ii)**\nto prevent the PRC from establishing new global bases; and\n**(D)**\nfor each of the locations referred to in subparagraph (A), identify the actions by the United States or its allies that would be most effective to enable the respective foreign governments to terminate plans for hosting a PRC base.\n##### (c) Task force\nNot later than 90 days after submitting the strategy described in subsection (b), the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall establish an interagency task force\u2014\n**(1)**\nto implement the strategy described in section (b) to counter the PRC\u2019s efforts at the locations of chief concern; and\n**(2)**\nto identify mitigation measures that would prevent the PRC from establishing new bases in locations beyond the locations of chief concern identified pursuant to subsection (b)(2)(A).\n##### (d) Quadrennial reviews and reports\nNot later than 4 years after the submission of the strategy required under subsection (b), and not less frequently than once every 4 years thereafter, the Secretary of State, in coordination with the Secretary of Defense, the Director of National Intelligence, and other appropriate senior Federal officials, shall\u2014\n**(1)**\nconduct a review of the Executive Branch\u2019s strategy and overall approach in response to the PRC global basing intentions; and\n**(2)**\nsubmit the results of such review, including the information described in subsection (b)(2), to the appropriate congressional committees.",
      "versionDate": "2025-05-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1731rs.xml",
      "text": "II\nCalendar No. 96\n119th CONGRESS\n1st Session\nS. 1731\nIN THE SENATE OF THE UNITED STATES\nMay 13, 2025 Mr. Coons (for himself, Mr. Ricketts , Mr. Kaine , Mr. Cornyn , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of State and the Secretary of Defense to develop a strategy in response to the global basing intentions of the People\u2019s Republic of China.\n#### 1. Short titles\nThis Act may be cited as the Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025 or the COUNTER Act of 2025 .\n#### 2. Findings\nAccording to multiple sources, including the 2024 annual report to Congress, titled Military and Security Developments Involving the People\u2019s Republic of China and known informally as the China Military Power Report \u2014\n**(1)**\nthe PRC is seeking to expand its overseas logistics and basing infrastructure to allow the PLA to project and sustain military power at greater distances;\n**(2)**\na global PLA logistics network could disrupt United States military operations as the PRC\u2019s global military objectives evolve;\n**(3)**\nin August 2017, the PRC officially opened the first overseas PLA military base near the commercial port of Doraleh in Djibouti;\n**(4)**\nin June 2022, the PRC and Cambodia hosted a ceremony to mark the groundbreaking on PRC-built upgrades to Ream Naval Base, including a joint logistics and training center and a pier to accommodate larger ships;\n**(5)**\nofficials from Cambodia and the PRC officially inaugurated expanded port features at the Ream Naval Base in April 2025; and\n**(6)**\nin addition to the base in Djibouti and the PRC's access to the port at the Ream Naval Base in Cambodia, the PRC is likely pursuing access to additional military facilities to support naval, air, and ground forces projection in many countries, including Angola, Bangladesh, Burma, Cuba, Equatorial Guinea, Gabon, Indonesia, Kenya, Mozambique, Namibia, Nigeria, Pakistan, Papua New Guinea, Seychelles, Solomon Islands, Sri Lanka, Tajikistan, Tanzania, Thailand, and the United Arab Emirates.\n#### 3. Sense of Congress\nWhile the executive branch has undertaken case-by-case efforts to forestall the establishment of new PRC bases in several countries, it is the sense of Congress that future efforts to counter the PRC's global basing intentions must\u2014\n**(1)**\nproceed with the urgency required to address the strategic implications of the PRC\u2019s actions;\n**(2)**\nreflect sufficient interagency coordination with respect to a problem that necessitates a whole-of-government approach;\n**(3)**\nensure that the United States Government maintains a proactive posture rather than a reactive posture in order to maximize strategic decision space;\n**(4)**\nidentify a comprehensive menu of actions that would be influential in shaping a partner\u2019s decision making regarding giving the PRC military access to its sovereign territory;\n**(5)**\nappropriately prioritize the subject of the PRC's global basing intentions within the context of the overall United States strategic competition with the PRC;\n**(6)**\nfactor in the potential contributions of key allies and partners to help respond to the PRC's pursuit of global basing, many of which\u2014\n**(A)**\nhave historic ties and influence in many of the geographic areas the PRC is targeting for potential future bases; and\n**(B)**\nrely on the same basic intelligence picture to form our baseline understanding of the PRC\u2019s global intentions;\n**(7)**\nestablish and ensure sufficient resourcing for enduring organizational structures to effectively address the issue of PRC global basing intentions; and\n**(8)**\nensure that future force posture, freedom of movement, and other interests of the United States and our allies are not jeopardized by the continued expansion of PRC bases.\n#### 4. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Armed Services of the Senate ;\n**(C)**\nthe Select Committee on Intelligence of the Senate ;\n**(D)**\nthe Committee on Appropriations of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on Armed Services of the House of Representatives ;\n**(G)**\nthe Permanent Select Committee on Intelligence of the House of Representatives ; and\n**(H)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) PLA**\nThe term PLA means the People's Liberation Army of the PRC.\n**(3) PRC**\nThe term PRC means the People's Republic of China.\n**(4) PRC global basing**\nThe term PRC global basing means the establishment of physical locations outside the geographic boundaries of the PRC where the PRC maintains some element of the People\u2019s Liberation Army, PRC intelligence or security forces, or infrastructure designed to support the presence of PRC military, intelligence, or security forces, for the purposes of potential power projection.\n#### 5. Assessment of executive branch's C\u2013PRC global basing strategy\n##### (a) Assessment\nNot later than 180 days after the date of the enactment of this Act, the Director of National Intelligence shall submit an intelligence assessment, in classified form, if needed, to the appropriate congressional committees. The assessment shall analyze the risk posed by PRC global basing to the United States or to any United States allies with respect to their ability to project power, maintain freedom of movement, and protect other interests as a function of the PRC's current or potential locations identified pursuant to subsection (b)(2)(A).\n##### (b) Strategy\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall submit a strategy to the appropriate congressional committees that contains the information described in paragraph (2).\n**(2) Contents**\nThe strategy required under paragraph (1) shall\u2014\n**(A)**\nidentify not fewer than 5 locations of chief concern where the PRC maintains a physical presence, or is suspected to be seeking a physical presence, which could ultimately transition into a PRC global base;\n**(B)**\ninclude a comprehensive listing of executive branch entities currently involved in addressing aspects of PRC global basing, including any resource or personnel constraints limiting the ability to effectively address the issue of PRC global basing intentions;\n**(C)**\ndescribe in detail all executive branch efforts\u2014\n**(i)**\nto mitigate the impacts of the locations referred to in subparagraph (A); or\n**(ii)**\nto prevent the PRC from establishing new global bases; and\n**(D)**\nfor each of the locations referred to in subparagraph (A), identify the actions by the United States or its allies that would be most effective to enable the respective foreign governments to terminate plans for hosting a PRC base.\n##### (c) Task force\nNot later than 90 days after submitting the strategy described in subsection (b), the Secretary of State, in coordination with the Secretary of Defense and other appropriate senior Federal officials, shall establish an interagency task force\u2014\n**(1)**\nto implement the strategy described in section (b) to counter the PRC\u2019s efforts at the locations of chief concern; and\n**(2)**\nto identify mitigation measures that would prevent the PRC from establishing new bases in locations beyond the locations of chief concern identified pursuant to subsection (b)(2)(A).\n##### (d) Quadrennial reviews and reports\nNot later than 4 years after the submission of the strategy required under subsection (b), and not less frequently than once every 4 years thereafter, the Secretary of State, in coordination with the Secretary of Defense, the Director of National Intelligence, and other appropriate senior Federal officials, shall\u2014\n**(1)**\nconduct a review of the Executive Branch\u2019s strategy and overall approach in response to the PRC global basing intentions; and\n**(2)**\nsubmit the results of such review, including the information described in subsection (b)(2), to the appropriate congressional committees.",
      "versionDate": "2025-06-18",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-16",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4458",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COUNTER Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-06-12T18:26:25Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-12T18:26:18Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-12T18:26:11Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-12T18:26:34Z"
          },
          {
            "name": "Homeland security",
            "updateDate": "2025-06-12T18:26:42Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-06-12T18:26:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-10T14:58:47Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1731is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1731rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "COUNTER Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "title": "COUNTER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COUNTER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Combating PRC Overseas and Unlawful Networked Threats through Enhanced Resilience Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T04:08:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of State and the Secretary of Defense to develop a strategy in response to the global basing intentions of the People's Republic of China.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:49Z"
    }
  ]
}
```
