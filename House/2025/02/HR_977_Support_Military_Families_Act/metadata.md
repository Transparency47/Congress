# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/977?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/977
- Title: Support Military Families Act
- Congress: 119
- Bill type: HR
- Bill number: 977
- Origin chamber: House
- Introduced date: 2025-02-05
- Update date: 2025-06-09T16:54:06Z
- Update date including text: 2025-06-09T16:54:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-05 - IntroReferral: Sponsor introductory remarks on measure. (CR H466)
- Latest action: 2025-02-05: Introduced in House

## Actions

- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Introduced in House
- 2025-02-05 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-02-05 - IntroReferral: Sponsor introductory remarks on measure. (CR H466)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/977",
    "number": "977",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000138",
        "district": "7",
        "firstName": "Eugene",
        "fullName": "Rep. Vindman, Eugene [D-VA-7]",
        "lastName": "Vindman",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Support Military Families Act",
    "type": "HR",
    "updateDate": "2025-06-09T16:54:06Z",
    "updateDateIncludingText": "2025-06-09T16:54:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-05",
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
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-02-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H466)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-05",
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
          "date": "2025-02-05T15:01:15Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "VA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "VA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "AL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr977ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 977\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 5, 2025 Mr. Vindman (for himself and Mr. Wittman ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo permit Federal employees who are spouses of members of the armed forces to engage in telework and remote work, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Support Military Families Act .\n#### 2. Permitting telework or remote work for Federal employees who are military spouses\n##### (a) In general\nNotwithstanding any other law, rule, or regulation, any employee in the executive branch of the Federal Government who is a spouse of a member of the armed forces\u2014\n**(1)**\nshall be exempt from any requirement to return to full-time in-person work; and\n**(2)**\nmay engage in telework or remote work.\n##### (b) Application\nSubsection (a) shall only apply to such a spouse who, prior to January 20, 2025, was eligible to telework or remote work.\n##### (c) GAO report\nNot later than 180 days after the date of the enactment of this section, the Comptroller General of the United States shall submit a report, to the Committee on Oversight and Government Reform of the House of Representatives and the Committee on Homeland Security and Governmental Affairs of the Senate, and publish such report on the public website of the Government Accountability Office. Such report shall include\u2014\n**(1)**\nthe total number of employees described in subsection (a);\n**(2)**\nthe average distance (in miles) such employees would commute if required to report to work in-person at their agency duty station; and\n**(3)**\nthe estimated economic impact of requiring such employees to perform in-person work, including the estimated costs of filling positions becoming vacant and lost productivity costs to the Federal Government.\n##### (d) Definitions\nIn this section, the terms armed forces and civil service have the meaning given those terms in section 2101 of title 5, United States Code.",
      "versionDate": "2025-02-05",
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
            "name": "Commuting",
            "updateDate": "2025-06-09T16:53:50Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-09T16:53:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-09T16:54:06Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-06-09T16:53:31Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-09T16:53:26Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-09T16:54:01Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-09T16:53:56Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-09T16:53:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-04-29T18:42:17Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr977ih.xml"
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
      "title": "Support Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Support Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit Federal employees who are spouses of members of the armed forces to engage in telework and remote work, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T07:18:43Z"
    }
  ]
}
```
