# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/121?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/121
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to "Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources".
- Congress: 119
- Bill type: SJRES
- Bill number: 121
- Origin chamber: Senate
- Introduced date: 2026-03-09
- Update date: 2026-03-13T15:47:34Z
- Update date including text: 2026-03-13T15:47:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in Senate
- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2026-03-09: Introduced in Senate

## Actions

- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/121",
    "number": "121",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources\".",
    "type": "SJRES",
    "updateDate": "2026-03-13T15:47:34Z",
    "updateDateIncludingText": "2026-03-13T15:47:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T21:12:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres121is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 121\nIN THE SENATE OF THE UNITED STATES\nMarch 9, 2026 Mr. Whitehouse introduced the following joint resolution; which was read twice and referred to the Committee on Environment and Public Works\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources .\nThat Congress disapproves the rule submitted by the Environmental Protection Agency relating to Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources (90 Fed. Reg. 55671 (December 3, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-03-09",
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
        "name": "Environmental Protection",
        "updateDate": "2026-03-13T15:47:34Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres121is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-12T04:18:38Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Environmental Protection Agency relating to \"Oil and Natural Gas Sector Climate Review: Extension of Deadlines in Standards of Performance for New, Reconstructed, and Modified Sources and Emissions Guidelines for Existing Sources\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T10:56:19Z"
    }
  ]
}
```
