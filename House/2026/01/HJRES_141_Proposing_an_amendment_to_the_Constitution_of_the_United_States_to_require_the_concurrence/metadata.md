# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/141
- Title: Proposing an amendment to the Constitution of the United States to require the concurrence of two-thirds of both Houses of Congress for the admission of new States into the Union.
- Congress: 119
- Bill type: HJRES
- Bill number: 141
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-01-26T14:54:34Z
- Update date including text: 2026-01-26T14:54:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/141",
    "number": "141",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B001321",
        "district": "7",
        "firstName": "Tom",
        "fullName": "Rep. Barrett, Tom [R-MI-7]",
        "lastName": "Barrett",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to require the concurrence of two-thirds of both Houses of Congress for the admission of new States into the Union.",
    "type": "HJRES",
    "updateDate": "2026-01-26T14:54:34Z",
    "updateDateIncludingText": "2026-01-26T14:54:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:01:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres141ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 141\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. Barrett submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to require the concurrence of two-thirds of both Houses of Congress for the admission of new States into the Union.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. New States may be admitted by the Congress, on the Concurrence of two thirds of both Houses, into this Union; but no new State shall be formed or erected within the Jurisdiction of any other State; nor any State be formed by the Junction of two or more States, or Parts of States, without the Consent of the Legislatures of the States concerned as well as of the Congress. 2. This article shall be inoperative unless it shall have been ratified as an amendment to the Constitution by the legislatures of the several States within seven years from the date of its submission by the Congress. .",
      "versionDate": "2026-01-21",
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
        "name": "Congress",
        "updateDate": "2026-01-26T14:54:34Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres141ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to require the concurrence of two-thirds of both Houses of Congress for the admission of new States into the Union.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T09:18:21Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to require the concurrence of two-thirds of both Houses of Congress for the admission of new States into the Union.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-22T09:05:58Z"
    }
  ]
}
```
