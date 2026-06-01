# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/13?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hconres/13
- Title: Providing that George Washington's "Farewell Address" shall be read at the beginning of each Congress.
- Congress: 119
- Bill type: HCONRES
- Bill number: 13
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-02-18T17:35:28Z
- Update date including text: 2025-02-18T17:35:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the House Committee on Rules.
- 2025-02-14 - Committee: Submitted in House
- Latest action: 2025-02-14: Submitted in House

## Actions

- 2025-02-14 - IntroReferral: Referred to the House Committee on Rules.
- 2025-02-14 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hconres/13",
    "number": "13",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Providing that George Washington's \"Farewell Address\" shall be read at the beginning of each Congress.",
    "type": "HCONRES",
    "updateDate": "2025-02-18T17:35:28Z",
    "updateDateIncludingText": "2025-02-18T17:35:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-02-14T18:30:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres13ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 13\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Bacon submitted the following concurrent resolution; which was referred to the Committee on Rules\nCONCURRENT RESOLUTION\nProviding that George Washington\u2019s Farewell Address shall be read at the beginning of each Congress.\n#### 1. Rule\nOn the first day of the first regular session of each Congress, George Washington\u2019s Farewell Address shall be read aloud\u2014\n**(1)**\nin the Senate by a Senator designated by the majority leader of the Senate; and\n**(2)**\nin the House of Representatives by a Representative designated by the Speaker of the House.\n#### 2. Exercise of rulemaking power\nThis resolution is adopted by Congress\u2014\n**(1)**\nas an exercise of the rulemaking power of the House of Representatives and the Senate, respectively, and as such it shall be considered as part of the rules of each House, respectively, or of that House to which it specifically applies, and such rule shall supersede other rules only to the extent that it is inconsistent therewith; and\n**(2)**\nwith full recognition of the constitutional right of either House to change such rules (so far as relating to such rules (so far as relating to such House) at any time, in the same manner, and to the same extent as in the case of any other rule of such House.",
      "versionDate": "2025-02-14",
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
        "name": "Congress",
        "updateDate": "2025-02-18T17:35:28Z"
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
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres13ih.xml"
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
      "title": "Providing that George Washington's \"Farewell Address\" shall be read at the beginning of each Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-15T09:18:22Z"
    },
    {
      "title": "Providing that George Washington's \"Farewell Address\" shall be read at the beginning of each Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-15T09:06:43Z"
    }
  ]
}
```
