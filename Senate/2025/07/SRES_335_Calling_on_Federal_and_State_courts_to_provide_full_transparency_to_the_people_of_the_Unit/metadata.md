# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/335?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/335
- Title: A resolution calling on Federal and State courts to provide full transparency to the people of the United States by unsealing materials concerning Mr. Jeffrey Epstein.
- Congress: 119
- Bill type: SRES
- Bill number: 335
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2025-09-05T16:28:20Z
- Update date including text: 2025-09-05T16:28:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on the Judiciary.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/335",
    "number": "335",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001190",
        "district": "",
        "firstName": "Markwayne",
        "fullName": "Sen. Mullin, Markwayne [R-OK]",
        "lastName": "Mullin",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A resolution calling on Federal and State courts to provide full transparency to the people of the United States by unsealing materials concerning Mr. Jeffrey Epstein.",
    "type": "SRES",
    "updateDate": "2025-09-05T16:28:20Z",
    "updateDateIncludingText": "2025-09-05T16:28:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
          "date": "2025-07-24T18:23:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres335is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 335\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Mullin submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nCalling on Federal and State courts to provide full transparency to the people of the United States by unsealing materials concerning Mr. Jeffrey Epstein.\nThat the Senate\u2014-\n**(1)**\ncalls upon applicable Federal and State courts to immediately unseal all materials, including grand jury materials, sealed as part of any criminal investigation, proceeding, or prosecution of Mr. Jeffrey Epstein or Ms. Ghislaine Maxwell, subject only to continuing redactions to protect victims and preserve ongoing prosecutions; and\n**(2)**\nsupports full transparency and public access to these materials.",
      "versionDate": "2025-07-24",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-09-05T16:28:20Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres335is.xml"
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
      "title": "A resolution calling on Federal and State courts to provide full transparency to the people of the United States by unsealing materials concerning Mr. Jeffrey Epstein.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-26T03:18:22Z"
    },
    {
      "title": "A resolution calling on Federal and State courts to provide full transparency to the people of the United States by unsealing materials concerning Mr. Jeffrey Epstein.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T10:56:22Z"
    }
  ]
}
```
