# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/39?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/sjres/39
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Internal Revenue Service relating to "Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit".
- Congress: 119
- Bill type: SJRES
- Bill number: 39
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2025-05-09T13:42:14Z
- Update date including text: 2025-05-09T13:42:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/sjres/39",
    "number": "39",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000577",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Lee, Mike [R-UT]",
        "lastName": "Lee",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Internal Revenue Service relating to \"Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit\".",
    "type": "SJRES",
    "updateDate": "2025-05-09T13:42:14Z",
    "updateDateIncludingText": "2025-05-09T13:42:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-03-26T22:29:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres39is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 39\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Lee introduced the following joint resolution; which was read twice and referred to the Committee on Finance\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Internal Revenue Service relating to Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit .\nThat Congress disapproves the rule submitted by the Internal Revenue Service relating to Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit (90 Fed. Reg. 4006 (January 15, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2025-03-26",
      "versionType": "IS"
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
        "name": "Taxation",
        "updateDate": "2025-05-09T13:42:14Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres39is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Internal Revenue Service relating to \"Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:08:22Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Internal Revenue Service relating to \"Section 45Y Clean Electricity Production Credit and Section 48E Clean Electricity Investment Credit\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T10:56:21Z"
    }
  ]
}
```
