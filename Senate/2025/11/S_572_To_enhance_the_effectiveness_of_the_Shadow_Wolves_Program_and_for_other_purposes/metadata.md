# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/572?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/572
- Title: Shadow Wolves Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 572
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2026-01-10T07:09:34Z
- Update date including text: 2026-01-10T07:09:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 251.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- 2025-07-30 - Committee: Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Committee: Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.
- 2025-11-03 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 251.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/572",
    "number": "572",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Shadow Wolves Improvement Act",
    "type": "S",
    "updateDate": "2026-01-10T07:09:34Z",
    "updateDateIncludingText": "2026-01-10T07:09:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-03",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 251.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-11-03",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Reported by Senator Paul with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Homeland Security and Governmental Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-13",
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
            "date": "2025-11-03T21:59:01Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-13T17:41:03Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "AZ"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "ND"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OK"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s572is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 572\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Gallego (for himself, Mr. Kelly , Mr. Hoeven , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo enhance the effectiveness of the Shadow Wolves Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shadow Wolves Improvement Act .\n#### 2. Enhancing the effectiveness of the Shadow Wolves Program\n##### (a) In general\nSubtitle D of title IV of the Homeland Security Act of 2002 ( 6 U.S.C. 251 et seq. ) is amended by adding at the end the following:\n448. Shadow Wolves Program (a) Mission and goals The Director of U.S. Immigration and Customs Enforcement (referred to in this section as the Director ), in coordination with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall specify the mission and goals of the Shadow Wolves Program. (b) Staffing The Director shall determine\u2014 (1) the number of special agents needed to staff the Shadow Wolves Program nationally; and (2) the knowledge, skills, and abilities that such special agents shall be required to possess. (c) Strategy Not later than 180 days after the date of the enactment of the Shadow Wolves Improvement Act , the Director, in consultation with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall update the strategy required under section 3 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) by adding\u2014 (1) measurable objectives to achieve the retention and recruitment of law enforcement officers, and the expansion goals set forth in the strategy; (2) a timeline for achieving such goals; and (3) milestones for recruiting qualified special agents for the Shadow Wolves Program to meet the target identified in the staffing needs assessment required under subsection (b)(1). (d) Provision of information The Director shall provide, to all GS\u20131801 Tactical Officers who are employed as Shadow Wolves by Homeland Security Investigations as of the date of the enactment of the Shadow Wolves Improvement Act , written information that will help them make an informed decision about reclassifying as special agents, including\u2014 (1) individualized information regarding how reclassification would affect pay, including changes to overtime pay, and retirement compensation; (2) steps such officers are required to complete to be reclassified as special agents, including\u2014 (A) whether they must meet training requirements; (B) a description of those requirements; (C) whether they are exempt from physical fitness, medical, or polygraph examinations; and (D) whether they are eligible for overtime pay during such training; and (3) any other relevant information that the Director believes would help such officers make an informed decision regarding such reclassification. (e) Succession plan The Director shall develop a plan for the timely recruitment of qualified individuals to fill vacant special agent positions in the Shadow Wolves Program that will result from anticipated retirements. (f) Program expansion The Director shall\u2014 (1) develop criteria for evaluating and selecting additional tribal lands on which additional Shadow Wolves units may be located, including the amount of additional funding necessary and potential sources for such funding; and (2) in developing such criteria, give consideration to tribal lands located in proximity to existing facilities that provide Federal law enforcement training. .\n##### (b) Clerical amendment\nThe table of contents for the Homeland Security Act of 2002 ( 6 U.S.C. 101 et seq. ) is amended by inserting after the item relating to section 447 the following:\nSec. 448. Shadow Wolves Program. .\n#### 3. Report to Congress on implementation of Shadow Wolves Program enhancements\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of U.S. Immigration and Customs Enforcement.\n**(2) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Homeland Security of the House of Representatives ; and\n**(D)**\nthe Committee on the Judiciary of the House of Representatives .\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Director shall submit a report to the relevant congressional committees that describes the progress that has been made towards the full implementation of\u2014\n**(1)**\nsection 448 of the Homeland Security Act of 2002, as added by section 2(a), including the required coordination with appropriate representatives of the Tohono O\u2019odham Nation and other partnering Tribal governments, to specify the mission and goals of the Shadow Wolves Program, which shall include tracking, interdiction, and investigation; and\n**(2)**\nsection 2(4) of the Shadow Wolves Enhancement Act, as added by section 4.\n#### 4. Conversion of experienced Shadow Wolves to career appointment in the competitive service\nSection 2 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) to noncompetitively convert Shadow Wolves, after their successful completion of three years as Shadow Wolves, regardless of location assigned, from the excepted service to career or career conditional appointments in the competitive service. .",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s572rs.xml",
      "text": "II\nCalendar No. 251\n119th CONGRESS\n1st Session\nS. 572\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Gallego (for himself, Mr. Kelly , Mr. Hoeven , and Mr. Lankford ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nNovember 3, 2025 Reported by Mr. Paul , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo enhance the effectiveness of the Shadow Wolves Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shadow Wolves Improvement Act .\n#### 2. Enhancing the effectiveness of the Shadow Wolves Program\n##### (a) In general\nSubtitle D of title IV of the Homeland Security Act of 2002 ( 6 U.S.C. 251 et seq. ) is amended by adding at the end the following:\n448. Shadow Wolves Program (a) Mission and goals The Director of U.S. Immigration and Customs Enforcement (referred to in this section as the Director ), in coordination with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall specify the mission and goals of the Shadow Wolves Program. (b) Staffing The Director shall determine\u2014 (1) the number of special agents needed to staff the Shadow Wolves Program nationally; and (2) the knowledge, skills, and abilities that such special agents shall be required to possess. (c) Strategy Not later than 180 days after the date of the enactment of the Shadow Wolves Improvement Act , the Director, in consultation with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall update the strategy required under section 3 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) by adding\u2014 (1) measurable objectives to achieve the retention and recruitment of law enforcement officers, and the expansion goals set forth in the strategy; (2) a timeline for achieving such goals; and (3) milestones for recruiting qualified special agents for the Shadow Wolves Program to meet the target identified in the staffing needs assessment required under subsection (b)(1). (d) Provision of information The Director shall provide, to all GS\u20131801 Tactical Officers who are employed as Shadow Wolves by Homeland Security Investigations as of the date of the enactment of the Shadow Wolves Improvement Act , written information that will help them make an informed decision about reclassifying as special agents, including\u2014 (1) individualized information regarding how reclassification would affect pay, including changes to overtime pay, and retirement compensation; (2) steps such officers are required to complete to be reclassified as special agents, including\u2014 (A) whether they must meet training requirements; (B) a description of those requirements; (C) whether they are exempt from physical fitness, medical, or polygraph examinations; and (D) whether they are eligible for overtime pay during such training; and (3) any other relevant information that the Director believes would help such officers make an informed decision regarding such reclassification. (e) Succession plan The Director shall develop a plan for the timely recruitment of qualified individuals to fill vacant special agent positions in the Shadow Wolves Program that will result from anticipated retirements. (f) Program expansion The Director shall\u2014 (1) develop criteria for evaluating and selecting additional tribal lands on which additional Shadow Wolves units may be located, including the amount of additional funding necessary and potential sources for such funding; and (2) in developing such criteria, give consideration to tribal lands located in proximity to existing facilities that provide Federal law enforcement training. .\n##### (b) Clerical amendment\nThe table of contents for the Homeland Security Act of 2002 ( 6 U.S.C. 101 et seq. ) is amended by inserting after the item relating to section 447 the following:\nSec. 448. Shadow Wolves Program. .\n#### 3. Report to Congress on implementation of Shadow Wolves Program enhancements\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of U.S. Immigration and Customs Enforcement.\n**(2) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Homeland Security of the House of Representatives ; and\n**(D)**\nthe Committee on the Judiciary of the House of Representatives .\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Director shall submit a report to the relevant congressional committees that describes the progress that has been made towards the full implementation of\u2014\n**(1)**\nsection 448 of the Homeland Security Act of 2002, as added by section 2(a), including the required coordination with appropriate representatives of the Tohono O\u2019odham Nation and other partnering Tribal governments, to specify the mission and goals of the Shadow Wolves Program, which shall include tracking, interdiction, and investigation; and\n**(2)**\nsection 2(4) of the Shadow Wolves Enhancement Act, as added by section 4.\n#### 4. Conversion of experienced Shadow Wolves to career appointment in the competitive service\nSection 2 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) to noncompetitively convert Shadow Wolves, after their successful completion of three years as Shadow Wolves, regardless of location assigned, from the excepted service to career or career conditional appointments in the competitive service. .",
      "versionDate": "2025-11-03",
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
        "actionDate": "2025-12-03",
        "text": "Referred to the House Committee on Homeland Security."
      },
      "number": "6379",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shadow Wolves Improvement Act",
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
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-08-27T16:58:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-27T16:58:57Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2025-08-27T16:58:57Z"
          },
          {
            "name": "Federal-Indian relations",
            "updateDate": "2025-08-27T16:59:06Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-08-27T16:59:14Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2025-08-27T16:58:57Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-08-27T16:58:57Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-08-27T16:59:24Z"
          },
          {
            "name": "Smuggling and trafficking",
            "updateDate": "2025-08-27T16:58:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-03-10T18:06:56Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s572is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-11-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s572rs.xml"
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
      "title": "Shadow Wolves Improvement Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-05T03:53:12Z"
    },
    {
      "title": "Shadow Wolves Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-04T12:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shadow Wolves Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance the effectiveness of the Shadow Wolves Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:20Z"
    }
  ]
}
```
