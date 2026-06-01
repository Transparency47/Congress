# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7231?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7231
- Title: Lobbyist Loophole Closure Act
- Congress: 119
- Bill type: HR
- Bill number: 7231
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-02-11T14:46:16Z
- Update date including text: 2026-02-11T14:46:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7231",
    "number": "7231",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Lobbyist Loophole Closure Act",
    "type": "HR",
    "updateDate": "2026-02-11T14:46:16Z",
    "updateDateIncludingText": "2026-02-11T14:46:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "NY"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7231ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7231\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Mrs. Ramirez (for herself, Ms. Williams of Georgia , Mr. Mullin , and Ms. Simon ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Lobbying Disclosure Act of 1995 to expand the scope of individuals and activities which are subject to the requirements of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Lobbyist Loophole Closure Act .\n#### 2. Expanding scope of individuals and activities subject to requirements of Lobbying Disclosure Act of 1995\n##### (a) Coverage of individuals providing legislative, political, and strategic counseling services\n**(1) Treatment of legislative, political, and strategic counseling services in support of lobbying contacts as lobbying activity**\nSection 3(7) of the Lobbying Disclosure Act of 1995 ( 2 U.S.C. 1602(7) ) is amended\u2014\n**(A)**\nby striking efforts and inserting any efforts ; and\n**(B)**\nby striking research and other background work and inserting the following: counseling in support of such preparation and planning activities, research, and other background work .\n**(2) Treatment of lobbying contact made with support of counseling services as lobbying contact made by individual providing services**\nSection 3(8) of such Act ( 2 U.S.C. 1602(8) ) is amended by adding at the end the following new subparagraph:\n(C) Treatment of providers of counseling services Any individual, with authority to director or substantially influence any lobbying contact made by another individual, and for financial or other compensation provides counseling services in support of preparation and planning activities which are treated as lobbying activities under paragraph (7) for that other individual\u2019s lobbying contact and who has knowledge that the specific lobbying contact was made, shall be considered to have made the same lobbying contact at the same time in the same manner to the covered executive branch official or covered legislative branch official involved. .\n##### (b) Reduction of percentage exemption for determination of threshold of lobbying contacts required for individuals To register as lobbyists\nSection 3(10) of such Act ( 2 U.S.C. 1602(10) ) is amended by striking less than 20 percent and inserting less than 10 percent .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to lobbying contacts made on or after the date of the enactment of this Act.",
      "versionDate": "2026-01-22",
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
        "updateDate": "2026-02-11T14:46:16Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7231ih.xml"
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
      "title": "Lobbyist Loophole Closure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lobbyist Loophole Closure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T04:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Lobbying Disclosure Act of 1995 to expand the scope of individuals and activities which are subject to the requirements of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T04:18:19Z"
    }
  ]
}
```
