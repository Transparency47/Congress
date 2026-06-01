# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/94?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hjres/94
- Title: Proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.
- Congress: 119
- Bill type: HJRES
- Bill number: 94
- Origin chamber: House
- Introduced date: 2025-04-29
- Update date: 2025-05-08T18:07:11Z
- Update date including text: 2025-05-08T18:07:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-29: Introduced in House

## Actions

- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Introduced in House
- 2025-04-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hjres/94",
    "number": "94",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B001309",
        "district": "2",
        "firstName": "Tim",
        "fullName": "Rep. Burchett, Tim [R-TN-2]",
        "lastName": "Burchett",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
    "type": "HJRES",
    "updateDate": "2025-05-08T18:07:11Z",
    "updateDateIncludingText": "2025-05-08T18:07:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T14:04:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres94ih.xml",
      "text": "IA\n119th CONGRESS\n1st Session\nH. J. RES. 94\nIN THE HOUSE OF REPRESENTATIVES\nApril 29, 2025 Mr. Burchett submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States within seven years after the date of its submission for ratification:\n\u2014 1. No person who has served three terms as a Representative shall be eligible for election to the House of Representatives. For purposes of this section, the election of a person to fill a vacancy in the House of Representatives shall be included as one term in determining the number of terms that such person has served as a Representative if the person fills the vacancy for more than one year. 2. No person who has served two terms as a Senator shall be eligible for election or appointment to the Senate. For purposes of this section, the election or appointment of a person to fill a vacancy in the Senate shall be included as one term in determining the number of terms that such person has served as a Senator if the person fills the vacancy for more than three years. 3. This article shall not apply to any person serving a term as a Member of Congress on the date of the ratification of this article. .",
      "versionDate": "2025-04-29",
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
        "updateDate": "2025-05-08T18:07:11Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hjres/BILLS-119hjres94ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-30T08:18:16Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to limit the number of terms that a Member of Congress may serve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-30T08:05:56Z"
    }
  ]
}
```
