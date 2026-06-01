# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7003?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7003
- Title: BIS STRENGTH Act
- Congress: 119
- Bill type: HR
- Bill number: 7003
- Origin chamber: House
- Introduced date: 2026-01-09
- Update date: 2026-05-18T15:25:25Z
- Update date including text: 2026-05-18T15:25:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-09: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 42 - 2.
- Latest action: 2026-01-09: Introduced in House

## Actions

- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Introduced in House
- 2026-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported by the Yeas and Nays: 42 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-09",
    "latestAction": {
      "actionDate": "2026-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7003",
    "number": "7003",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001229",
        "district": "6",
        "firstName": "Jefferson",
        "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
        "lastName": "Shreve",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "BIS STRENGTH Act",
    "type": "HR",
    "updateDate": "2026-05-18T15:25:25Z",
    "updateDateIncludingText": "2026-05-18T15:25:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "text": "Ordered to be Reported by the Yeas and Nays: 42 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-01-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-09",
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
            "date": "2026-04-22T20:08:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-09T14:00:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-09T14:00:10Z",
          "name": "Referred To"
        }
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
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CA"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "SC"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7003ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7003\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2026 Mr. Shreve (for himself and Ms. Kamlager-Dove ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the Under Secretary of Commerce for Industry and Security to appoint certain personnel in order to attract highly qualified experts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the BIS Strategic Talent Recruitment to Enhance National Guardrails for Technological Handling Act or the BIS STRENGTH Act .\n#### 2. Attracting highly qualified experts to Bureau of Industry and Security\n##### (a) In general\nThe Under Secretary of Commerce for Industry and Security, in order to attract to the Bureau of Industry and Security highly qualified experts in needed occupations (as determined by the Under Secretary), may\u2014\n**(1)**\nconduct an annual study to identify specific gaps in expertise at the Bureau that have been difficult to fill through the civil service and constrain the Bureau\u2019s ability to effectively fulfil the Bureau\u2019s mandate;\n**(2)**\nnotwithstanding any provision of section 3304 or sections 3309 through 3318 of title 5, United States Code, appoint personnel from outside the civil service (as defined in section 2101 of title 5, United States Code) that have the expertise identified pursuant to paragraph (1) to positions in the Bureau of Industry and Security; and\n**(3)**\nprescribe the rates of basic pay for positions to which employees are appointed under paragraph (2) at rates not in excess of the maximum rate of basic pay authorized for senior-level positions under section 5376 of title 5, United States Code, as increased by locality-based comparability payments under section 5304 of that title, notwithstanding any provision of that title governing the rates of pay or classification of employees in the executive branch.\n##### (b) Limitation on term of appointment\n**(1) In general**\nExcept as provided in paragraph (2), the service of an employee under an appointment made pursuant to this section may not exceed 5 years.\n**(2) Extensions**\nThe Under Secretary may, in the case of a particular employee, extend the period to which service is limited under paragraph (1) by not more than one additional year if the Under Secretary determines that such action is necessary to promote the national security or foreign policy of the United States.\n##### (c) Limitation on total annual compensation\nNotwithstanding any other provision of this section or of section 5307 of title 5, United States Code, no additional payments may be paid to an employee under this section in any calendar year if, or to the extent that, the total annual compensation of the employee will exceed the maximum amount of total annual compensation payable to the Vice President under section 104 of title 3, United States Code.\n##### (d) Limitation on number of highly qualified experts\nThe number of highly qualified experts appointed and retained by the Under Secretary under subsection (b)(1) shall not exceed 25 at any time.\n##### (e) Report required\n**(1) In general**\nNot later than 180 days after the date of the enactment of this section, and annually thereafter, the Under Secretary shall submit to the committees specified in paragraph (2) a report that includes\u2014\n**(A)**\na list of areas in which the Under Secretary has identified specific gaps in expertise pursuant to subsection (a)(1);\n**(B)**\nthe steps taken by the Under Secretary to appoint personnel with expertise in such areas from within the civil service during the period specified in paragraph (3);\n**(C)**\nthe number of individuals appointed to the Bureau of Industry and Security under the authority provided by this section during the period specified in paragraph (3);\n**(D)**\na description of the qualifications of such individuals and their responsibilities during that period; and\n**(E)**\na description of the impact of such individuals on carrying out the mission of the Bureau of Industry and Security.\n**(2) Committees specified**\nThe committees specified in this paragraph are\u2014\n**(A)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate;\n**(B)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(C)**\nthe Committee on Foreign Affairs of the House of Representatives.\n**(3) Period specified**\nThe period specified in this paragraph is\u2014\n**(A)**\nin the case of the first report required by paragraph (1), the 180-day period preceding submission of the report; and\n**(B)**\nin the case of any subsequent report required by paragraph (1), the one-year period preceding submission of the report.\n##### (f) Savings provisions\nIn the event that the Under Secretary terminates the authority under this section, in the case of an employee who, on the day before the termination of the authority, is serving in a position pursuant to an appointment under this section\u2014\n**(1)**\nthe termination of the authority does not terminate the employee's employment in that position before the expiration of the lesser of\u2014\n**(A)**\nthe period for which the employee was appointed; or\n**(B)**\nthe period to which the employee's service is limited under subsection (c), including any extension made under this section before the termination of the authority; and\n**(2)**\nthe rate of basic pay prescribed for the position under this section may not be reduced as long as the employee continues to serve in the position without a break in service.\n##### (g) Rule of construction\nNothing in this section shall be construed to waive any requirement regarding background checks or qualifications of applicants to positions with the Bureau of Industry and Security.\n##### (h) Termination\nThe authority provided by this section shall cease to be effective on the date that is 5 years after the date of the enactment of this section.",
      "versionDate": "2026-01-09",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-18T15:25:25Z"
          },
          {
            "name": "Department of Commerce",
            "updateDate": "2026-05-18T15:25:12Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-05-18T15:25:20Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-05-18T15:25:16Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-05-18T15:25:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-26T17:18:07Z"
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
      "date": "2026-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7003ih.xml"
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
      "title": "BIS STRENGTH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T07:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIS STRENGTH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIS Strategic Talent Recruitment to Enhance National Guardrails for Technological Handling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-22T07:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the Under Secretary of Commerce for Industry and Security to appoint certain personnel in order to attract highly qualified experts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T05:33:50Z"
    }
  ]
}
```
