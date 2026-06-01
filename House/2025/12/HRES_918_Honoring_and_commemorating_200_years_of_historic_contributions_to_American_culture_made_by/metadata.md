# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/918?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/918
- Title: Honoring and commemorating 200 years of historic contributions to American culture made by the city of Akron.
- Congress: 119
- Bill type: HRES
- Bill number: 918
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2025-12-03T15:43:28Z
- Update date including text: 2025-12-03T15:43:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-01 - IntroReferral: Submitted in House
- 2025-12-01 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4975-4976)
- Latest action: 2025-12-01: Submitted in House

## Actions

- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-01 - IntroReferral: Submitted in House
- 2025-12-01 - IntroReferral: Submitted in House
- 2025-12-02 - IntroReferral: Sponsor introductory remarks on measure. (CR H4975-4976)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/918",
    "number": "918",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Honoring and commemorating 200 years of historic contributions to American culture made by the city of Akron.",
    "type": "HRES",
    "updateDate": "2025-12-03T15:43:28Z",
    "updateDateIncludingText": "2025-12-03T15:43:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-12-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H4975-4976)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres918ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 918\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mrs. Sykes submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nHonoring and commemorating 200 years of historic contributions to American culture made by the city of Akron.\nThat the House of Representatives\u2014\n**(1)**\nhonors and commemorates 200 years of historic contributions to American culture made by the city of Akron;\n**(2)**\nrecognizes the city\u2019s longstanding history of fighting for economic, gender, and racial justice; and\n**(3)**\nencourages Akron to continue standing up to injustices and supporting workers\u2019 rights for another 200 years.",
      "versionDate": "2025-12-01",
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
        "updateDate": "2025-12-02T19:47:24Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres918ih.xml"
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
      "title": "Honoring and commemorating 200 years of historic contributions to American culture made by the city of Akron.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:26Z"
    },
    {
      "title": "Honoring and commemorating 200 years of historic contributions to American culture made by the city of Akron.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T09:05:53Z"
    }
  ]
}
```
