# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/402
- Title: A resolution recognizing Lloyd Ashburn Williams's unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.
- Congress: 119
- Bill type: SRES
- Bill number: 402
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-09-24T13:29:05Z
- Update date including text: 2025-09-24T13:29:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6736: 1)
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S6736: 1)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/402",
    "number": "402",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "A resolution recognizing Lloyd Ashburn Williams's unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
    "type": "SRES",
    "updateDate": "2025-09-24T13:29:05Z",
    "updateDateIncludingText": "2025-09-24T13:29:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S6736: 1)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T16:52:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres402is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 402\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Schumer submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nRecognizing Lloyd Ashburn Williams\u2019s unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.\nThat the Senate recognizes Lloyd Ashburn Williams\u2019s unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "versionDate": "2025-09-18",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-09-24T13:29:05Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres402is.xml"
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
      "title": "A resolution recognizing Lloyd Ashburn Williams's unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-23T04:18:17Z"
    },
    {
      "title": "A resolution recognizing Lloyd Ashburn Williams's unparalleled dedication to fostering economic empowerment, cultural pride, and social equity in Harlem.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T10:56:22Z"
    }
  ]
}
```
