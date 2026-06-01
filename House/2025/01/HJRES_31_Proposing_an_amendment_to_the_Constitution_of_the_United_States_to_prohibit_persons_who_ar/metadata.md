# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/31?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/31
- Title: Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections.
- Congress: 119
- Bill type: HJRES
- Bill number: 31
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-06-13T18:36:08Z
- Update date including text: 2025-06-13T18:36:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/31",
    "number": "31",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections.",
    "type": "HJRES",
    "updateDate": "2025-06-13T18:36:08Z",
    "updateDateIncludingText": "2025-06-13T18:36:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
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
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:03:45Z",
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
      "bioguideId": "A000375",
      "district": "19",
      "firstName": "Jodey",
      "fullName": "Rep. Arrington, Jodey C. [R-TX-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Arrington",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "TX"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "SC"
    },
    {
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "CO"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "TX"
    },
    {
      "bioguideId": "D000032",
      "district": "19",
      "firstName": "Byron",
      "fullName": "Rep. Donalds, Byron [R-FL-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Donalds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "FL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres31ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 31\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Pfluger (for himself, Mr. Arrington , Mr. Hamadeh of Arizona , Mr. Timmons , and Ms. Boebert ) submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. A person who is not a person lawfully accorded the privilege of residing permanently in the United States, a person owing permanent allegiance to the United States, or a citizen of the United States may not vote in any election for Federal, State, Tribal, or local office, including offices in the District of Columbia or in any of the territories or possessions of the United States. 2. The Congress shall have power to enforce this article by appropriate legislation. .",
      "versionDate": "2025-01-31",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Citizenship and naturalization",
            "updateDate": "2025-06-13T18:36:08Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-06-13T18:35:47Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-06-13T18:35:54Z"
          },
          {
            "name": "Voting rights",
            "updateDate": "2025-06-13T18:36:01Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-02T14:40:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hjres31",
          "measure-number": "31",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-05-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres31v00",
            "update-date": "2025-05-06"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment prohibiting persons who are not U.S. citizens, nationals, or lawful permanent residents from voting in elections.\u00a0Specifically, the joint resolution prohibits such a person from voting in any election for federal, state, tribal, or local office, including offices in the District of Columbia or in any of the territories or possessions of the United States.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres31.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting persons who are not U.S. citizens, nationals, or lawful permanent residents from voting in elections.\u00a0Specifically, the joint resolution prohibits such a person from voting in any election for federal, state, tribal, or local office, including offices in the District of Columbia or in any of the territories or possessions of the United States.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hjres31"
    },
    "title": "Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections."
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment prohibiting persons who are not U.S. citizens, nationals, or lawful permanent residents from voting in elections.\u00a0Specifically, the joint resolution prohibits such a person from voting in any election for federal, state, tribal, or local office, including offices in the District of Columbia or in any of the territories or possessions of the United States.</p>",
      "updateDate": "2025-05-06",
      "versionCode": "id119hjres31"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres31ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-01T09:18:34Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to prohibit persons who are not citizens, nationals, or lawful permanent residents of the United States from voting in elections.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:06:00Z"
    }
  ]
}
```
