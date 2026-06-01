# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8587?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8587
- Title: Safeguarding Honest Speech Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8587
- Origin chamber: House
- Introduced date: 2026-04-29
- Update date: 2026-05-20T19:48:14Z
- Update date including text: 2026-05-20T19:48:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-04-29: Introduced in House

## Actions

- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Introduced in House
- 2026-04-29 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8587",
    "number": "8587",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "O000175",
        "district": "5",
        "firstName": "Andrew",
        "fullName": "Rep. Ogles, Andrew [R-TN-5]",
        "lastName": "Ogles",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Safeguarding Honest Speech Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T19:48:14Z",
    "updateDateIncludingText": "2026-05-20T19:48:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T13:03:45Z",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "AZ"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8587ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8587\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2026 Mr. Ogles (for himself, Ms. Boebert , Mr. Clyde , Mr. Crane , Mr. Gosar , and Mr. Weber of Texas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the use of funds to implement, administer, or enforce measures requiring certain employees to refer to an individual by the preferred pronouns of such individual or a name other than the legal name of such individual, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Honest Speech Act of 2026 .\n#### 2. No Federal funds for compelled language\n##### (a) In general\nNotwithstanding any other provision of law, no funds may be used for the purpose of implementing, administering, or enforcing any rule, policy, guidance, recommendation, or memoranda requiring an employee or contractor of any Federal agency or Department to use\u2014\n**(1)**\nanother person\u2019s preferred pronouns if they are incompatible with such a person\u2019s sex; or\n**(2)**\na name other than a person\u2019s legal name when referring to such a person.\n##### (b) Enforcement\n**(1) In general**\nAll Federal agencies and Departments shall ensure that, not later than 30 days following a written notice from any employee or contractor regarding an alleged violation of subsection (a), a formal response to the notice is issued to the employee or contractor.\n**(2) Private right of action**\nIn the case that the formal response in subsection (a) does not represent a satisfactory outcome for a Federal employee or contractor, any employee or contractor aggrieved by a violation of subsection (a) may commence a civil action against the Federal agency or Department responsible for the alleged violation.\n**(3) Relief**\nIn any action under this subsection, the court may award appropriate relief, including\u2014\n**(A)**\ntemporary, preliminary, or permanent injunctive relief;\n**(B)**\ncompensatory damages;\n**(C)**\npunitive or exemplary damages, which may not exceed $100,000; and\n**(D)**\nreasonable fees for attorneys.\n**(4) Statute of limitations**\nAn action under this subsection shall be brought not later than one year after the date on which the alleged violation of subsection (a) occurred.\n##### (c) Definitions\nIn this section:\n**(1) Female**\nThe term female refers to an individual who has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes eggs for fertilization.\n**(2) Male**\nThe term male refers to an individual who has, had, will have, or would have, but for a developmental or genetic anomaly or historical accident, the reproductive system that at some point produces, transports, and utilizes sperm for fertilization.\n**(3) Sex**\nThe term sex refers to biological sex, either male or female.\n**(4) Person**\nThe term person refers to a natural person.",
      "versionDate": "2026-04-29",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-20T19:48:14Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8587ih.xml"
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
      "title": "Safeguarding Honest Speech Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safeguarding Honest Speech Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the use of funds to implement, administer, or enforce measures requiring certain employees to refer to an individual by the preferred pronouns of such individual or a name other than the legal name of such individual, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:38Z"
    }
  ]
}
```
