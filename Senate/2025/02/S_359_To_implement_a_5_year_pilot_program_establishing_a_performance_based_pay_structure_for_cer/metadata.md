# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/359?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/359
- Title: Federal Employee Performance and Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 359
- Origin chamber: Senate
- Introduced date: 2025-02-03
- Update date: 2025-12-05T22:49:11Z
- Update date including text: 2025-12-05T22:49:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-03: Introduced in Senate
- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-03: Introduced in Senate

## Actions

- 2025-02-03 - IntroReferral: Introduced in Senate
- 2025-02-03 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-03",
    "latestAction": {
      "actionDate": "2025-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/359",
    "number": "359",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Federal Employee Performance and Accountability Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:49:11Z",
    "updateDateIncludingText": "2025-12-05T22:49:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-03",
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
      "actionDate": "2025-02-03",
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
          "date": "2025-02-03T20:40:22Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s359is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 359\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2025 Mrs. Blackburn (for herself, Mr. Tillis , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo implement a 5-year pilot program establishing a performance-based pay structure for certain Federal employees in order to enhance productivity, accountability, and employee satisfaction in public service.\n#### 1. Short title\nThis Act may be cited as the Federal Employee Performance and Accountability Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Director**\nThe term Director means the Director of the Office of Management and Budget.\n**(2) Eligible employee**\nThe term eligible employee means an employee of an Executive agency employed in a position that\u2014\n**(A)**\nis\u2014\n**(i)**\nat the GS\u201311, GS\u201312, GS\u201313, GS\u201314, or GS\u201315 level; or\n**(ii)**\na senior-level position, which shall be defined as a position classified above the GS\u201315 level under section 5108 of title 5, United States Code; and\n**(B)**\nhas clearly measurable performance criteria, such as\u2014\n**(i)**\na project management position;\n**(ii)**\na position involving administrative or policy analysis;\n**(iii)**\nan information technology, finance, or procurement specialist;\n**(iv)**\na leadership position that involves managing a team, evaluating program performance, or supervising operations;\n**(v)**\na customer service representative; or\n**(vi)**\na claims processor.\n**(3) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n**(4) Participating agency**\nThe term participating agency means an Executive agency, 1 or more employees of which are participating employees in accordance with section 3(b)(1).\n**(5) Participating employee**\nThe term participating employee means an eligible employee who participates in the Program.\n**(6) Performance metrics**\nThe term performance metrics , with respect to a participating agency, means standards for participating employees tailored to functions that are specific to the participating agency, which may include\u2014\n**(A)**\nproductivity standards, which measure quantifiable outputs such as completed cases, projects, or responses per quarter;\n**(B)**\nquality standards, which measure compliance with protocols, accuracy, and customer satisfaction rates; and\n**(C)**\ntimeliness standards, which measure compliance with processing deadlines, efficiency improvements, and timely task completion.\n**(7) Program**\nThe term Program means the pilot program established under section 3(a).\n#### 3. Pilot program eligibility and program scope\n##### (a) In general\nDuring the 5-year period beginning on the date that is 180 days after the date of enactment of this Act, the Director shall carry out a pilot program that establishes a performance-based pay structure for participating employees.\n##### (b) Participation\n**(1) In general**\nSubject to paragraph (2), the head of each Executive agency shall ensure that not less than 1 percent and not more than 10 percent of eligible employees of the Executive agency participate in the Program.\n**(2) Opt-out**\n**(A) In general**\nThe head of an Executive agency may elect to not have the Executive agency participate in the Program if the head of the Executive agency determines that participation could pose risks to national security or public safety.\n**(B) Transparency requirement**\nIf the head of an Executive agency determines that the Executive agency should not participate in the Program pursuant to subparagraph (A), the head of the Executive agency shall submit to the Director a written justification for the decision.\n#### 4. Performance measurement and accountability\n##### (a) Annual performance metrics\nA participating agency shall establish annual performance metrics for each participating employee related to core functions and public service delivery, focusing on productivity, quality, and timeliness.\n##### (b) Evaluation process\nThe Director shall establish, and each participating agency shall implement, a standardized, objective performance evaluation system that includes periodic review of the performance of a participating employee.\n##### (c) Employee support and training\nA participating agency shall provide training and resources to support participating employees in understanding and meeting performance metrics, including an introductory training course and quarterly performance feedback sessions.\n#### 5. Incentive pay structure and non-monetary benefits\n##### (a) Tiered salary increase structure\n**(1) In general**\nA participating agency shall implement a tiered salary adjustment system for participating employees based on their annual performance evaluations under section 4 under which, effective as of the first day of the first applicable pay period beginning on or after the first day of the second year of the Program, and of each year thereafter, a participating agency shall adjust (if applicable) the rate of basic pay of a participating employee in accordance with this subsection.\n**(2) Tier 1 (exceeds expectations)**\nIn the case of a participating employee who significantly exceeded established performance metrics during the preceding year (referred to in this section as a tier 1 employee ), a participating agency shall increase the rate of basic pay of the participating employee by 15 percent.\n**(3) Tier 2 (meets expectations)**\nIn the case of a participating employee who met established performance metrics during the preceding year (referred to in this section as a tier 2 employee ), a participating agency may not adjust the rate of basic pay of the participating employee.\n**(4) Tier 3 (below expectations)**\nIn the case of a participating employee who did not meet established performance metrics during the preceding year (referred to in this section as a tier 3 employee ), the participating agency shall\u2014\n**(A)**\nreduce the rate of basic pay of the participating employee by 15 percent; and\n**(B)**\nprovide training or development opportunities to assist the participating employee in improving performance.\n##### (b) Bonuses\nThe head of a participating agency, at the discretion of the agency head, may award a bonus to a tier 1 employee.\n##### (c) Non-Monetary benefits\nThe head of a participating agency, at the discretion of the agency head, may provide a tier 1 employee with flexible scheduling, telework options, and other non-monetary benefits or incentives, such as technology upgrades and parking options.\n##### (d) Relation to title 5 pay adjustments, step-Increases, and other monetary benefits\nA participating employee shall not be eligible for any adjustment of pay, advancement in pay, or bonus or other type of additional monetary compensation under title 5, United States Code, based on any service performed while the employee is participating in the Program, including\u2014\n**(1)**\nadjustment of the rate of basic pay under section 5303, 5304, or 5304a of that title;\n**(2)**\nadvancement in pay to a higher rate within the grade in which the employee's position is placed under section 5335 or 5336 of that title;\n**(3)**\nbonuses under section 5753 or 5754 of that title; and\n**(4)**\nperformance awards under section 5384 of that title.\n#### 6. Reporting and accountability\n##### (a) Annual agency productivity reports\n**(1) In general**\nFor each year in which the Program is carried out, a participating agency shall submit a report to the Director that includes the following information:\n**(A) Quantitative outcomes**\nData on cost savings, efficiency gains, and overall productivity metrics.\n**(B) Qualitative outcomes**\nExamples of how productivity improvements have positively impacted public service outcomes and employee satisfaction.\n**(2) OMB oversight and recommendations**\nThe Director shall\u2014\n**(A)**\nreview each report submitted under paragraph (1); and\n**(B)**\nrecommend adjustments to participating agencies as appropriate.\n##### (b) Annual OMB assessments\nFor each year in which the Program is carried out, the Director shall\u2014\n**(1)**\nassess the outcomes of the Program with respect to productivity, budgetary impact, and employee satisfaction; and\n**(2)**\npublish and submit to Congress a report on the assessment conducted under paragraph (1).\n##### (c) Final review\nNot later than 1 year after the date on which the Program terminates, the Comptroller General of the United States and the Director shall assess the success of the Program and submit to Congress a report on the impact of the Program on productivity, budgets, and employee engagement.\n#### 7. Funding\n##### (a) No additional funds\nNo additional funds are authorized to be appropriated to carry out this Act.\n##### (b) Use of existing funds\nThe Office of Management and Budget, the Government Accountability Office, and each participating agency shall carry out the duties of the respective agency under this Act using amounts otherwise made available to that agency.",
      "versionDate": "2025-02-03",
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
        "actionDate": "2025-01-03",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "201",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Federal Employee Performance and Accountability Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-20T18:49:44Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-20T18:49:44Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-20T18:49:44Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-20T18:49:44Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-06-20T18:49:44Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2025-06-20T18:49:44Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-05T15:39:41Z"
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
      "date": "2025-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s359is.xml"
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
      "title": "Federal Employee Performance and Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T05:08:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Federal Employee Performance and Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T05:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to implement a 5-year pilot program establishing a performance-based pay structure for certain Federal employees in order to enhance productivity, accountability, and employee satisfaction in public service.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T05:03:54Z"
    }
  ]
}
```
