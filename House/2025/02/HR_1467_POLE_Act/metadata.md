# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1467
- Title: POLE Act
- Congress: 119
- Bill type: HR
- Bill number: 1467
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-11-11T09:05:17Z
- Update date including text: 2025-11-11T09:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1467",
    "number": "1467",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "POLE Act",
    "type": "HR",
    "updateDate": "2025-11-11T09:05:17Z",
    "updateDateIncludingText": "2025-11-11T09:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:34:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1467ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1467\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Help America Vote Act of 2002 to prohibit the use of Federal funds for the administration of elections for Federal, State, or local office in States which do not have in effect laws to permit units of local government to hold elections for local office in odd-numbered years, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Local Elections Act or the POLE Act .\n#### 2. Findings; sense of Congress\n##### (a) Findings\nCongress finds the following:\n**(1)**\nHolding local elections for public office in odd-numbered years provides greater focus on local candidates and issues.\n**(2)**\nLocal elections held in odd-numbered years allow voters to make more informed decisions about their local representation.\n**(3)**\nHolding all elections in even-numbered years diminishes the attention given to community matters.\n**(4)**\nHolding all elections in even-numbered years overcrowds the ballot, hindering the decision-making process for voters.\n**(5)**\nLocal elected officials directly serve their immediate communities and needs.\n**(6)**\nLocal leaders played a vital role in the founding of the United States.\n**(7)**\nLocal governments are at the core of our Nation\u2019s republic.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nunits of local governments should have the authority to conduct elections for local office in odd-numbered years;\n**(2)**\nlocal elections held in odd-numbered years ensure that local candidates and issues receive greater attention and allow voters to make well-informed choices; and\n**(3)**\nthe most effective form of representation is attained through local governance.\n#### 3. Prohibiting provision of Federal funds for election administration for States not permitting local governments to hold elections for local office in odd-numbered years\n##### (a) Prohibition\nTitle IX of the Help America Vote Act of 2002 ( 52 U.S.C. 21141 et seq. ) is amended by adding at the end the following new section:\n907. Prohibiting provision of Federal funds for election administration for States not permitting local governments to hold elections for local office in odd-numbered years Notwithstanding any other provision of law, no Federal funds may be provided under this Act or any other Act to administer an election for Federal, State, or local office held in a State which does not have in effect a law which permits units of local government in the State to hold elections for local office in odd-numbered years. .\n##### (b) Clerical amendment\nThe table of contents of such Act is amended by adding at the end of the items relating to title IX the following:\nSec. 907. Prohibiting provision of Federal funds for election administration for States not permitting local governments to hold elections for local office in odd-numbered years. .\n##### (c) Effective date\nThe amendments made by this section shall apply with respect to fiscal year 2027 and each succeeding fiscal year.",
      "versionDate": "2025-02-21",
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
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-07-14T15:25:51Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-07-14T15:25:55Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-02T14:58:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1467",
          "measure-number": "1467",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1467v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Our Local Elections Act or the POLE Act</strong></p><p>This bill prohibits a state from receiving federal election administration funds if the state does not permit localities to hold elections for local office in odd-numbered years.</p>"
        },
        "title": "POLE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1467.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Local Elections Act or the POLE Act</strong></p><p>This bill prohibits a state from receiving federal election administration funds if the state does not permit localities to hold elections for local office in odd-numbered years.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr1467"
    },
    "title": "POLE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Local Elections Act or the POLE Act</strong></p><p>This bill prohibits a state from receiving federal election administration funds if the state does not permit localities to hold elections for local office in odd-numbered years.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr1467"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1467ih.xml"
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
      "title": "POLE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POLE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Local Elections Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Help America Vote Act of 2002 to prohibit the use of Federal funds for the administration of elections for Federal, State, or local office in States which do not have in effect laws to permit units of local government to hold elections for local office in odd-numbered years, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:37Z"
    }
  ]
}
```
