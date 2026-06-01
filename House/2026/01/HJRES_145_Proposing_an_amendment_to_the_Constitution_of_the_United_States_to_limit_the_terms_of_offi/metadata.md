# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/145
- Title: Proposing an amendment to the Constitution of the United States to limit the terms of office of the judges of the Supreme Court and inferior courts.
- Congress: 119
- Bill type: HJRES
- Bill number: 145
- Origin chamber: House
- Introduced date: 2026-01-30
- Update date: 2026-02-02T14:42:28Z
- Update date including text: 2026-02-02T14:42:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-30: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-01-30: Introduced in House

## Actions

- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Introduced in House
- 2026-01-30 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-30",
    "latestAction": {
      "actionDate": "2026-01-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/145",
    "number": "145",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
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
    "title": "Proposing an amendment to the Constitution of the United States to limit the terms of office of the judges of the Supreme Court and inferior courts.",
    "type": "HJRES",
    "updateDate": "2026-02-02T14:42:28Z",
    "updateDateIncludingText": "2026-02-02T14:42:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-30",
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
      "actionDate": "2026-01-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-30",
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
          "date": "2026-01-30T15:32:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres145ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 145\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 30, 2026 Mr. Barrett submitted the following joint resolution; which was referred to the Committee on the Judiciary\nJOINT RESOLUTION\nProposing an amendment to the Constitution of the United States to limit the terms of office of the judges of the Supreme Court and inferior courts.\nThat the following article is proposed as an amendment to the Constitution of the United States, which shall be valid to all intents and purposes as part of the Constitution when ratified by the legislatures of three-fourths of the several States:\n\u2014 1. Each judge of the Supreme Court and each inferior court shall be appointed to serve during good behavior for a term of 20 years. 2. No person who has served a term of 20 years as a judge of the Supreme Court or an inferior court shall be eligible for reappointment as a judge in the court in which such term was served. 3. This article shall only apply to an appointment occurring on or after the date of the ratification of this article. .",
      "versionDate": "2026-01-30",
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
        "name": "Law",
        "updateDate": "2026-02-02T14:42:28Z"
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
      "date": "2026-01-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres145ih.xml"
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
      "title": "Proposing an amendment to the Constitution of the United States to limit the terms of office of the judges of the Supreme Court and inferior courts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-31T09:18:20Z"
    },
    {
      "title": "Proposing an amendment to the Constitution of the United States to limit the terms of office of the judges of the Supreme Court and inferior courts.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-31T09:05:30Z"
    }
  ]
}
```
