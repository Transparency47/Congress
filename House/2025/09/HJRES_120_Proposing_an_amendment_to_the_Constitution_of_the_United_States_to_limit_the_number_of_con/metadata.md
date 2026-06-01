# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/120?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/120
- Title: Proposing an amendment to the Constitution of the United States to limit the number of consecutive terms that a Member of Congress may serve.
- Congress: 119
- Bill type: HJRES
- Bill number: 120
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-09-24T13:37:45Z
- Update date including text: 2025-09-24T13:37:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/120",
    "number": "120",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001223",
        "district": "2",
        "firstName": "Seth",
        "fullName": "Rep. Magaziner, Seth [D-RI-2]",
        "lastName": "Magaziner",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to limit the number of consecutive terms that a Member of Congress may serve.",
    "type": "HJRES",
    "updateDate": "2025-09-24T13:37:45Z",
    "updateDateIncludingText": "2025-09-24T13:37:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:02:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres120ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 120\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Mr. Magaziner submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to limit the number of consecutive terms that a Member of Congress may serve.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. No person who has been a Senator for two consecutive terms shall again be eligible for election or appointment to the Senate until the date that is one year after the end of such second consecutive term. 2. No person who has been a Representative for five consecutive terms shall again be eligible for election to the House of Representatives until the date that is one year after the end of the fifth consecutive term. 3. For purposes of this article, any term a person serves as a Senator or Representative to fill a vacancy shall not be included in determining the number of consecutive terms that the person has been a Senator or Representative unless the period of time for which the person fills the vacancy is greater than three years in the case of a Senator or greater than one year in the case of a Representative. 4. For the purposes of this article, any term that began before the date of the ratification of this article shall not be included in determining the number of consecutive terms that a person has been a Senator or Representative. .",
      "versionDate": "2025-09-11",
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
        "updateDate": "2025-09-24T13:37:45Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres120ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of consecutive terms that a Member of Congress may serve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T08:18:20Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of consecutive terms that a Member of Congress may serve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-12T08:06:37Z"
    }
  ]
}
```
