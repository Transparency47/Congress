# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/553?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/553
- Title: Censuring Representative Andrew Ogles.
- Congress: 119
- Bill type: HRES
- Bill number: 553
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-08-01T15:59:13Z
- Update date including text: 2025-08-01T15:59:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H3027)
- 2025-06-27 - IntroReferral: Submitted in House
- 2025-06-27 - IntroReferral: Submitted in House
- Latest action: 2025-06-27: Submitted in House

## Actions

- 2025-06-27 - IntroReferral: Referred to the House Committee on Ethics.
- 2025-06-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H3027)
- 2025-06-27 - IntroReferral: Submitted in House
- 2025-06-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/553",
    "number": "553",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000488",
        "district": "13",
        "firstName": "Shri",
        "fullName": "Rep. Thanedar, Shri [D-MI-13]",
        "lastName": "Thanedar",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Censuring Representative Andrew Ogles.",
    "type": "HRES",
    "updateDate": "2025-08-01T15:59:13Z",
    "updateDateIncludingText": "2025-08-01T15:59:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Ethics Committee",
          "systemCode": "hsso00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ethics.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "B00100",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H3027)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-27T13:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ethics Committee",
      "systemCode": "hsso00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres553ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 553\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Thanedar submitted the following resolution; which was referred to the Committee on Ethics\nRESOLUTION\nCensuring Representative Andrew Ogles.\nThat\u2014\n**(1)**\nRepresentative Andrew Ogles be censured;\n**(2)**\nRepresentative Andrew Ogles forthwith present himself in the well of the House of Representatives for the pronouncement of censure; and\n**(3)**\nRepresentative Andrew Ogles be censured with the public reading of this resolution by the Speaker.",
      "versionDate": "2025-06-27",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-08-01T15:59:13Z"
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
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres553ih.xml"
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
      "title": "Censuring Representative Andrew Ogles.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T08:18:21Z"
    },
    {
      "title": "Censuring Representative Andrew Ogles.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T08:06:24Z"
    }
  ]
}
```
