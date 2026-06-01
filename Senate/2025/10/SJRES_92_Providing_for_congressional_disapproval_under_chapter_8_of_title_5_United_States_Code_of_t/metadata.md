# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/92?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/92
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Highway Administration relating to "Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program"".
- Congress: 119
- Bill type: SJRES
- Bill number: 92
- Origin chamber: Senate
- Introduced date: 2025-10-28
- Update date: 2025-12-09T22:36:03Z
- Update date including text: 2025-12-09T22:36:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-28: Introduced in Senate
- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-10-28: Introduced in Senate

## Actions

- 2025-10-28 - IntroReferral: Introduced in Senate
- 2025-10-28 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-28",
    "latestAction": {
      "actionDate": "2025-10-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/92",
    "number": "92",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
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
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Highway Administration relating to \"Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program\"\".",
    "type": "SJRES",
    "updateDate": "2025-12-09T22:36:03Z",
    "updateDateIncludingText": "2025-12-09T22:36:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-28",
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
      "actionDate": "2025-10-28",
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
          "date": "2025-10-28T16:58:48Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres92is.xml",
      "text": "IIA\n119th CONGRESS\n1st Session\nS. J. RES. 92\nIN THE SENATE OF THE UNITED STATES\nOctober 28, 2025 Mr. Whitehouse introduced the following joint resolution; which was read twice and referred to the Committee on Environment and Public Works\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Highway Administration relating to Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program .\nThat Congress disapproves the rule submitted by the Federal Highway Administration relating to Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program (90 Fed. Reg. 45136 (September 19, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2025-10-28",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-12-09T22:36:03Z"
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
      "date": "2025-10-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sjres/BILLS-119sjres92is.xml"
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
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Highway Administration relating to \"Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program\"\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-30T09:33:16Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Federal Highway Administration relating to \"Rescinding Regulations Regarding Management Systems Pertaining to the Fish and Wildlife Service and the Refuge Roads Program\"\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T10:56:14Z"
    }
  ]
}
```
