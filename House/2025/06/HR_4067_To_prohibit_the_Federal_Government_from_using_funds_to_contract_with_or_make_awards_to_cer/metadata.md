# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4067?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4067
- Title: Protect the First Amendment Act
- Congress: 119
- Bill type: HR
- Bill number: 4067
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2025-07-21T15:11:20Z
- Update date including text: 2025-07-21T15:11:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4067",
    "number": "4067",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000816",
        "district": "25",
        "firstName": "Roger",
        "fullName": "Rep. Williams, Roger [R-TX-25]",
        "lastName": "Williams",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protect the First Amendment Act",
    "type": "HR",
    "updateDate": "2025-07-21T15:11:20Z",
    "updateDateIncludingText": "2025-07-21T15:11:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
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
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:01:10Z",
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
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4067ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4067\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Mr. Williams of Texas (for himself and Mr. McCormick ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the Federal Government from using funds to contract with or make awards to certain entities engaging in censorship, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect the First Amendment Act .\n#### 2. Prohibition on authorization of funding for covered entities and nonprofit organizations or other entities that engage in covered behavior\n##### (a) In general\nNo funds are authorized to be used by the Federal Government, to contract with or grant awards to\u2014\n**(1)**\na covered entity; or\n**(2)**\na nonprofit organization or other entity that engages in covered behavior.\n##### (b) Definitions\nIn this section:\n**(1) Covered entity**\nThe term covered entity means\u2014\n**(A)**\nNewsGuard Technologies, Inc. (doing business as NewsGuard ), or any successor thereto; or\n**(B)**\nDisinformation Index, Inc., Disinformation Index, Ltd., or Global Disinformation Index gUG (collectively doing business as Global Disinformation Index ), or and successor thereto.\n**(2) Covered behavior**\nThe term covered behavior means operations, activities, or products, the function of which is to demonetize or rate the credibility of a domestic entity (including news and other information outlets) based on the lawful speech of such domestic entity by purporting to evaluate whether such speech is misinformation, disinformation, or malinformation.\n**(3) Nonprofit organization**\nThe term nonprofit organization means an organization that is described in section 501(c)(3) of the Internal Revenue Code of 1986 and that is exempt from taxation under section 501(a) of such Code.",
      "versionDate": "2025-06-20",
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
        "updateDate": "2025-07-21T15:11:20Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4067ih.xml"
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
      "title": "Protect the First Amendment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect the First Amendment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Federal Government from using funds to contract with or make awards to certain entities engaging in censorship, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:57Z"
    }
  ]
}
```
