# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6379?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6379
- Title: Shadow Wolves Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 6379
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-16T08:07:24Z
- Update date including text: 2026-05-16T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Homeland Security.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6379",
    "number": "6379",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "C001133",
        "district": "6",
        "firstName": "Juan",
        "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
        "lastName": "Ciscomani",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Shadow Wolves Improvement Act",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:24Z",
    "updateDateIncludingText": "2026-05-16T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Homeland Security.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-04T21:12:23Z",
              "name": "Referred to"
            }
          },
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "systemCode": "hshm00",
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
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6379ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6379\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Ciscomani (for himself and Mr. Suozzi ) introduced the following bill; which was referred to the Committee on Homeland Security\nA BILL\nTo enhance the effectiveness of the Shadow Wolves Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Shadow Wolves Improvement Act .\n#### 2. Enhancing the effectiveness of the Shadow Wolves Program\n##### (a) In general\nSubtitle D of title IV of the Homeland Security Act of 2002 ( 6 U.S.C. 251 et seq. ) is amended by adding at the end the following:\n448. Shadow Wolves Program (a) Mission and goals The Director of U.S. Immigration and Customs Enforcement (referred to in this section as the Director ), in coordination with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall specify the mission and goals of the Shadow Wolves Program. (b) Staffing The Director shall determine\u2014 (1) the number of special agents needed to staff the Shadow Wolves Program nationally; and (2) the knowledge, skills, and abilities that such special agents shall be required to possess. (c) Strategy Not later than 180 days after the date of the enactment of the Shadow Wolves Improvement Act , the Director, in consultation with appropriate representatives of partnering Tribal governments, including the Tohono O'odham Nation, shall update the strategy required under section 3 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) by adding\u2014 (1) measurable objectives to achieve the retention and recruitment of law enforcement officers, and the expansion goals set forth in the strategy; (2) a timeline for achieving such goals; and (3) milestones for recruiting qualified special agents for the Shadow Wolves Program to meet the target identified in the staffing needs assessment required under subsection (b)(1). (d) Provision of information The Director shall provide, to all GS\u20131801 Tactical Officers who are employed as Shadow Wolves by Homeland Security Investigations as of the date of the enactment of the Shadow Wolves Improvement Act , written information that will help them make an informed decision about reclassifying as special agents, including\u2014 (1) individualized information regarding how reclassification would affect pay, including changes to overtime pay, and retirement compensation; (2) steps such officers are required to complete to be reclassified as special agents, including\u2014 (A) whether they must meet training requirements; (B) a description of those requirements; (C) whether they are exempt from physical fitness, medical, or polygraph examinations; and (D) whether they are eligible for overtime pay during such training; and (3) any other relevant information that the Director believes would help such officers make an informed decision regarding such reclassification. (e) Succession plan The Director shall develop a plan for the timely recruitment of qualified individuals to fill vacant special agent positions in the Shadow Wolves Program that will result from anticipated retirements. (f) Program expansion The Director shall\u2014 (1) develop criteria for evaluating and selecting additional tribal lands on which additional Shadow Wolves units may be located, including the amount of additional funding necessary and potential sources for such funding; and (2) in developing such criteria, give consideration to tribal lands located in proximity to existing facilities that provide Federal law enforcement training. .\n##### (b) Clerical amendment\nThe table of contents for the Homeland Security Act of 2002 ( 6 U.S.C. 101 et seq. ) is amended by inserting after the item relating to section 447 the following:\nSec. 448. Shadow Wolves Program. .\n#### 3. Report to Congress on implementation of Shadow Wolves Program enhancements\n##### (a) Definitions\nIn this section:\n**(1) Director**\nThe term Director means the Director of U.S. Immigration and Customs Enforcement.\n**(2) Relevant congressional committees**\nThe term relevant congressional committees means\u2014\n**(A)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Homeland Security of the House of Representatives ; and\n**(D)**\nthe Committee on the Judiciary of the House of Representatives .\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, the Director shall submit a report to the relevant congressional committees that describes the progress that has been made towards the full implementation of\u2014\n**(1)**\nsection 448 of the Homeland Security Act of 2002, as added by section 2(a), including the required coordination with appropriate representatives of the Tohono O\u2019odham Nation and other partnering Tribal governments, to specify the mission and goals of the Shadow Wolves Program, which shall include tracking, interdiction, and investigation; and\n**(2)**\nsection 2(4) of the Shadow Wolves Enhancement Act, as added by section 4.\n#### 4. Conversion of experienced Shadow Wolves to career appointment in the competitive service\nSection 2 of the Shadow Wolves Enhancement Act ( Public Law 117\u2013113 ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and at the end;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) to noncompetitively convert Shadow Wolves, after their successful completion of three years as Shadow Wolves, regardless of location assigned, from the excepted service to career or career conditional appointments in the competitive service. .\n#### 5. No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2025-12-03",
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
        "actionDate": "2025-11-03",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 251."
      },
      "number": "572",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shadow Wolves Improvement Act",
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
        "name": "Immigration",
        "updateDate": "2026-01-05T16:14:01Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6379ih.xml"
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
      "title": "Shadow Wolves Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T05:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shadow Wolves Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance the effectiveness of the Shadow Wolves Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T05:03:57Z"
    }
  ]
}
```
