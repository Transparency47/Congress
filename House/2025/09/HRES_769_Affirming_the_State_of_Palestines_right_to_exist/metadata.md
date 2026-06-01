# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/769
- Title: Original Resolution Affirming the State of Palestine’s Right to Exist
- Congress: 119
- Bill type: HRES
- Bill number: 769
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2025-11-14T13:23:18Z
- Update date including text: 2025-11-14T13:23:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-26 - IntroReferral: Submitted in House
- 2025-09-26 - IntroReferral: Submitted in House
- Latest action: 2025-09-26: Submitted in House

## Actions

- 2025-09-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-26 - IntroReferral: Submitted in House
- 2025-09-26 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/769",
    "number": "769",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000553",
        "district": "9",
        "firstName": "Al",
        "fullName": "Rep. Green, Al [D-TX-9]",
        "lastName": "Green",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "Original Resolution Affirming the State of Palestine\u2019s Right to Exist",
    "type": "HRES",
    "updateDate": "2025-11-14T13:23:18Z",
    "updateDateIncludingText": "2025-11-14T13:23:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-26",
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
          "date": "2025-09-26T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres769ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 769\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Green of Texas submitted the following resolution; which was referred to the Committee on Foreign Affairs\nRESOLUTION\nAffirming the State of Palestine\u2019s right to exist.\nThat the House of Representatives\u2014\n**(1)**\naffirms Palestine\u2019s right to exist and at a future time to become a nation State;\n**(2)**\nrecognizes the two-state solution as the only solution that will secure a lasting peace in the region; and\n**(3)**\nrejects calls for Palestine\u2019s destruction.",
      "versionDate": "2025-09-26",
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
        "name": "International Affairs",
        "updateDate": "2025-09-29T18:23:08Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres769ih.xml"
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
      "title": "Original Resolution Affirming the State of Palestine\u2019s Right to Exist",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T13:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Original Resolution Affirming the State of Palestine\u2019s Right to Exist",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T13:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Affirming the State of Palestine's right to exist.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-27T08:18:16Z"
    }
  ]
}
```
