# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/107?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/107
- Title: Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States.
- Congress: 119
- Bill type: HJRES
- Bill number: 107
- Origin chamber: House
- Introduced date: 2025-07-16
- Update date: 2026-03-31T11:14:35Z
- Update date including text: 2026-03-31T11:14:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-16: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-07-16: Introduced in House

## Actions

- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Introduced in House
- 2025-07-16 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-16",
    "latestAction": {
      "actionDate": "2025-07-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/107",
    "number": "107",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States.",
    "type": "HJRES",
    "updateDate": "2026-03-31T11:14:35Z",
    "updateDateIncludingText": "2026-03-31T11:14:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-16",
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
      "actionDate": "2025-07-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-16",
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
          "date": "2025-07-16T14:06:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres107ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 107\nIN THE HOUSE OF REPRESENTATIVES\nJuly 16, 2025 Ms. Tenney submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. An individual may not vote in any election for public office held in the United States, including any election for Federal, State, or local office, or vote on any ballot initiative or referendum held in the United States, unless the individual is a citizen of the United States. 2. The Congress shall have the power to enforce this article by appropriate legislation. .",
      "versionDate": "2025-07-16",
      "versionType": "IH"
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
        "updateDate": "2025-08-01T16:13:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-16",
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
          "measure-id": "id119hjres107",
          "measure-number": "107",
          "measure-type": "hjres",
          "orig-publish-date": "2025-07-16",
          "originChamber": "HOUSE",
          "update-date": "2026-03-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres107v00",
            "update-date": "2026-03-31"
          },
          "action-date": "2025-07-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment that prohibits an individual who is not a U.S. citizen from voting in federal, state, or local elections for public office or voting on any ballot initiative or referendum held in the United States.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres107.xml",
    "summary": {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that prohibits an individual who is not a U.S. citizen from voting in federal, state, or local elections for public office or voting on any ballot initiative or referendum held in the United States.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hjres107"
    },
    "title": "Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States."
  },
  "summaries": [
    {
      "actionDate": "2025-07-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment that prohibits an individual who is not a U.S. citizen from voting in federal, state, or local elections for public office or voting on any ballot initiative or referendum held in the United States.</p>",
      "updateDate": "2026-03-31",
      "versionCode": "id119hjres107"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres107ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T13:18:20Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to prohibit voting in Federal, State, or local elections by individuals who are not citizens of the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:07Z"
    }
  ]
}
```
