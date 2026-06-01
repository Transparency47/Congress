# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/29?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/29
- Title: Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times.
- Congress: 119
- Bill type: HJRES
- Bill number: 29
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-04-17T21:22:30Z
- Update date including text: 2025-04-17T21:22:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/29",
    "number": "29",
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
    "title": "Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times.",
    "type": "HJRES",
    "updateDate": "2025-04-17T21:22:30Z",
    "updateDateIncludingText": "2025-04-17T21:22:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:08:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres29ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 29\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mr. Ogles submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 No person shall be elected to the office of the President more than three times, nor be elected to any additional term after being elected to two consecutive terms, and no person who has held the office of President, or acted as President, for more than two years of a term to which some other person was elected President shall be elected to the office of the President more than twice. .",
      "versionDate": "2025-01-23",
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
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-02-03T17:11:09Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-02-03T17:11:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-01-27T17:23:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hjres29",
          "measure-number": "29",
          "measure-type": "hjres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hjres29v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This joint resolution proposes a constitutional amendment to increase the number of times a person may be elected President.</p><p>The proposed amendment specifies that no person shall be elected to the office of the President (1) more than three times, (2) for any additional term after being elected to two consecutive terms, or (3) more than twice after having served as President for more than two years of a term to which some other person was elected President (for example, if a President died after serving for one year and the Vice\u00a0President became President for the remaining three years of the term, that person may subsequently be elected President no more than two times).</p><p>Currently, under the Twenty-Second Amendment to the U.S. Constitution, a person may not be elected President more than twice. Additionally, no person who has been President, or acted as President, for more than two years of a term to which some other person was elected President may be elected President more than once.</p>"
        },
        "title": "Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hjres/BILLSUM-119hjres29.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment to increase the number of times a person may be elected President.</p><p>The proposed amendment specifies that no person shall be elected to the office of the President (1) more than three times, (2) for any additional term after being elected to two consecutive terms, or (3) more than twice after having served as President for more than two years of a term to which some other person was elected President (for example, if a President died after serving for one year and the Vice\u00a0President became President for the remaining three years of the term, that person may subsequently be elected President no more than two times).</p><p>Currently, under the Twenty-Second Amendment to the U.S. Constitution, a person may not be elected President more than twice. Additionally, no person who has been President, or acted as President, for more than two years of a term to which some other person was elected President may be elected President more than once.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hjres29"
    },
    "title": "Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This joint resolution proposes a constitutional amendment to increase the number of times a person may be elected President.</p><p>The proposed amendment specifies that no person shall be elected to the office of the President (1) more than three times, (2) for any additional term after being elected to two consecutive terms, or (3) more than twice after having served as President for more than two years of a term to which some other person was elected President (for example, if a President died after serving for one year and the Vice\u00a0President became President for the remaining three years of the term, that person may subsequently be elected President no more than two times).</p><p>Currently, under the Twenty-Second Amendment to the U.S. Constitution, a person may not be elected President more than twice. Additionally, no person who has been President, or acted as President, for more than two years of a term to which some other person was elected President may be elected President more than once.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hjres29"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres29ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-24T09:18:20Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to provide that no person shall be elected to the office of the President more than three times.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:15Z"
    }
  ]
}
```
