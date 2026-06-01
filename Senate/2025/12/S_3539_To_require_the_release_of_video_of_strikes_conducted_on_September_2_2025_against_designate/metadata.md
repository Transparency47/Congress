# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3539
- Title: A bill to require the release of video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.
- Congress: 119
- Bill type: S
- Bill number: 3539
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-26T17:21:59Z
- Update date including text: 2026-01-26T17:21:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3539",
    "number": "3539",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "A bill to require the release of video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.",
    "type": "S",
    "updateDate": "2026-01-26T17:21:59Z",
    "updateDateIncludingText": "2026-01-26T17:21:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T19:47:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3539is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3539\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo require the release of video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.\n#### 1. Required release to Congress of unedited video of September 2, 2025, boat strikes\nNot later than 10 calendar days after the date of the enactment of this Act, the Secretary of Defense shall make available to all members of Congress unedited video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.\n#### 2. Required public release of video of September 2, 2025, boat strikes\n##### (a) In general\nNot later than 15 calendar days after the date of the enactment of this Act, the Secretary of Defense shall make publicly available on a Department of Defense website video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.\n##### (b) Protection of classified information\nThe Secretary of Defense may remove or obscure such material in the video released under subsection (a) as necessary in order to protect appropriately classified information.",
      "versionDate": "2025-12-17",
      "versionType": "Introduced in Senate"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-26T17:21:59Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3539is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "title": "A bill to require the release of video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-22T03:33:24Z"
    },
    {
      "title": "A bill to require the release of video of strikes conducted on September 2, 2025, against designated terrorist organizations in the area of responsibility of the United States Southern Command.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T11:56:24Z"
    }
  ]
}
```
