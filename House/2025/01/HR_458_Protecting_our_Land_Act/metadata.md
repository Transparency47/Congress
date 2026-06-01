# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/458
- Title: Protecting our Land Act
- Congress: 119
- Bill type: HR
- Bill number: 458
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-02-28T17:47:48Z
- Update date including text: 2025-02-28T17:47:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/458",
    "number": "458",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Protecting our Land Act",
    "type": "HR",
    "updateDate": "2025-02-28T17:47:48Z",
    "updateDateIncludingText": "2025-02-28T17:47:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr458ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 458\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo prohibit the purchase of public or private real estate located in the United States by foreign adversaries and state sponsors of terrorism.\n#### 1. Short title\nThis Act may be cited as the Protecting our Land Act .\n#### 2. Prohibition on purchase of public or private real estate located in the United States by foreign adversaries and state sponsors of terrorism\n##### (a) In general\nNotwithstanding any other provision of law, the President shall direct the heads of the Federal departments and agencies to promulgate rules and regulations to prohibit the purchase of public or private real estate located in the United States by a foreign adversary, a state sponsor of terrorism, any agent or instrumentality of a foreign adversary or a state sponsor of terrorism, or any person owned or controlled by, or affiliated with, a foreign adversary or a state sponsor of terrorism.\n##### (b) Definitions\nIn this section\u2014\n**(1)**\nthe term foreign adversary means any foreign government or foreign nongovernment person engaged in a long-term pattern or serious instances of conduct significantly adverse to the national security of the United States or security and safety of United States persons;\n**(2)**\nthe term state sponsor of terrorism means a country the government of which the Secretary of State determines has repeatedly provided support for international terrorism pursuant to\u2014\n**(A)**\nsection 1754(c)(1)(A) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4318(c)(1)(A) );\n**(B)**\nsection 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 );\n**(C)**\nsection 40 of the Arms Export Control Act ( 22 U.S.C. 2780 ); or\n**(D)**\nany other provision of law; and\n**(3)**\nthe term \u201cUnited States\u201d means the several States, the District of Columbia, the Commonwealth of Puerto Rico, the Commonwealth of the Northern Mariana Islands, American Samoa, Guam, the United States Virgin Islands, and any other territory or possession of the United States.",
      "versionDate": "2025-01-15",
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
        "name": "International Affairs",
        "updateDate": "2025-02-21T12:26:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr458",
          "measure-number": "458",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr458v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting our Land Act</strong></p> <p>This bill requires the President to direct federal agencies to promulgate rules and regulations to prohibit foreign adversaries or state sponsors of terrorism from purchasing real estate located in the United States.</p>"
        },
        "title": "Protecting our Land Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr458.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting our Land Act</strong></p> <p>This bill requires the President to direct federal agencies to promulgate rules and regulations to prohibit foreign adversaries or state sponsors of terrorism from purchasing real estate located in the United States.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr458"
    },
    "title": "Protecting our Land Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting our Land Act</strong></p> <p>This bill requires the President to direct federal agencies to promulgate rules and regulations to prohibit foreign adversaries or state sponsors of terrorism from purchasing real estate located in the United States.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr458"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr458ih.xml"
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
      "title": "Protecting our Land Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T04:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting our Land Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the purchase of public or private real estate located in the United States by foreign adversaries and state sponsors of terrorism.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T04:18:19Z"
    }
  ]
}
```
