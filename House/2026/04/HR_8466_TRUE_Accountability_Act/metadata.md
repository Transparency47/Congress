# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8466?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8466
- Title: TRUE Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 8466
- Origin chamber: House
- Introduced date: 2026-04-23
- Update date: 2026-05-01T08:09:19Z
- Update date including text: 2026-05-01T08:09:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-23: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.
- Latest action: 2026-04-23: Introduced in House

## Actions

- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Introduced in House
- 2026-04-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-29 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-23",
    "latestAction": {
      "actionDate": "2026-04-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8466",
    "number": "8466",
    "originChamber": "House",
    "policyArea": {
      "name": "Emergency Management"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "TRUE Accountability Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:09:19Z",
    "updateDateIncludingText": "2026-05-01T08:09:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 40 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-29",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
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
      "actionDate": "2026-04-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-23",
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
            "date": "2026-04-29T13:08:42Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-23T13:01:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8466ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8466\nIN THE HOUSE OF REPRESENTATIVES\nApril 23, 2026 Mr. Biggs of Arizona (for himself and Mr. Subramanyam ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require certain agencies to develop plans for internal control in the event of an emergency or crisis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taxpayer Resources Used in Emergencies Accountability Act or the TRUE Accountability Act .\n#### 2. OMB guidance\n##### (a) Plans for emergency spending\nSubchapter IV of chapter 33 of title 31, United States Code is amended by adding at the end the following new section:\n3359. Requirement for financial and administrative controls for emergency spending (a) Definitions In this section: (1) Covered agency The term covered agency means an agency described in section 901(b). (2) Director The term Director means the Director of the Office of Management and Budget. (3) Internal control The term internal control means a process that is\u2014 (A) affected by the management and other personnel of an entity; and (B) designed to provide reasonable assurance with respect to the achievement of objectives relating to\u2014 (i) effectiveness and efficiency of operations; (ii) reliability of financial reporting; and (iii) compliance with applicable law. (b) Guidance (1) In general Not later than 180 days after the date of the enactment of this section, the Director shall issue, and every 3 years thereafter review and if necessary update, guidance to covered agencies for the development of plans for internal control that are ready or adaptable for immediate use in a future disaster, pandemic, economic relief, or other such emergency supplemental appropriations legislative measure. (2) Contents The guidance issued under paragraph (1) shall\u2014 (A) incorporate relevant governmentwide documents and best practices for preventing improper payments and mitigating fraud risks in Federal programs, including the documents of the Government Accountability Office entitled A Framework for Managing Improper Payments in Emergency Assistance Programs and A Framework for Managing Fraud Risks in Federal Programs (or any successor document); and (B) require a plan for internal control of each covered agency to include\u2014 (i) the identification of a senior official of the covered agency to be responsible and accountable for the implementation of the plan; and (ii) policies and procedures to timely\u2014 (I) in accordance with paragraph (3), assess the risks of improper payments and fraud relating to the implementation of any supplemental appropriation, or other increase in budget authority, that may be made available to the covered agency for a purpose relating to implementing a disaster, pandemic, economic relief, or other such emergency supplemental appropriations legislative measure; (II) develop and implement mitigation strategies to reduce the risks described in subclause (I), including any change to internal controls, to ensure that, to the greatest extent possible, appropriate controls are in place prior to the expenditure of funds; and (III) adopt real-time, data driven payment monitoring techniques to identify and reduce improper and fraudulent payments, such as anomaly detection, volume plausibility checks, and network analysis. (3) Assessment of risk The assessment of risk required by paragraph (2)(B)(ii)(I) shall include at a minimum\u2014 (A) a substantive evaluation of the risk of financial loss to the Federal Government caused by improper payments and fraud; and (B) an identification of the risk tolerance for the agency program or activity. (c) Plan submission (1) In general Not later than 1 year after the date of the enactment of this section, the head of each covered agency head shall submit to the Director the plan required by subsection (b)(2)(B). (2) Revisions Not later than 3 years after the date on which the head of a covered agency submits a plan under paragraph (1), and not less frequently than once every 3 years thereafter, the head of each covered agency shall\u2014 (A) review and, if necessary, revise the plan of the covered agency; and (B) submit to the Director any revised plan of the covered agency. (3) Submission to Congress Not later than 15 months after the date of the enactment of this section, and not less frequently than annually thereafter, the Director shall assemble and submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives the plans submitted by covered agencies under paragraph (1) and a summary of the plans to help agencies prepare to implement such plans, including any action planned to harmonize the agency programs and activities and any legislative recommendations for a future disaster, pandemic, economic relief, or other emergency supplemental appropriation. .\n##### (b) Technical and conforming amendment\nThe table of sections for chapter 33 of title 31, United States Code, is amended by inserting after the item relating to section 3358 the following:\n3359. Requirement for financial and administrative controls for emergency spending. .\n##### (c) No additional funds\nNo additional funds are authorized to be appropriated for the purpose of carrying out this Act.",
      "versionDate": "2026-04-23",
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
        "name": "Emergency Management",
        "updateDate": "2026-04-29T20:30:24Z"
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
      "date": "2026-04-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8466ih.xml"
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
      "title": "TRUE Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRUE Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taxpayer Resources Used in Emergencies Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require certain agencies to develop plans for internal control in the event of an emergency or crisis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-28T05:48:27Z"
    }
  ]
}
```
