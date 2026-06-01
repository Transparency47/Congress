# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/762
- Title: Expressing support for the designation of September 23, 2025, as "Mary Church Terrell Day", and calling on Congress to recognize Mary Church Terrell's lasting contributions to the civil rights and women's rights movements.
- Congress: 119
- Bill type: HRES
- Bill number: 762
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2025-09-25T14:42:46Z
- Update date including text: 2025-09-25T14:42:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House
- Latest action: 2025-09-23: Submitted in House

## Actions

- 2025-09-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/762",
    "number": "762",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Expressing support for the designation of September 23, 2025, as \"Mary Church Terrell Day\", and calling on Congress to recognize Mary Church Terrell's lasting contributions to the civil rights and women's rights movements.",
    "type": "HRES",
    "updateDate": "2025-09-25T14:42:46Z",
    "updateDateIncludingText": "2025-09-25T14:42:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
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
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:00:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres762ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 762\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Ms. Norton submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of September 23, 2025, as Mary Church Terrell Day , and calling on Congress to recognize Mary Church Terrell\u2019s lasting contributions to the civil rights and women\u2019s rights movements.\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Mary Church Terrell Day ; and\n**(2)**\ncalls on Congress to recognize Mary Church Terrell\u2019s lasting contributions to the civil rights and women\u2019s rights movements.",
      "versionDate": "2025-09-23",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-09-25T14:42:46Z"
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
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres762ih.xml"
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
      "title": "Expressing support for the designation of September 23, 2025, as \"Mary Church Terrell Day\", and calling on Congress to recognize Mary Church Terrell's lasting contributions to the civil rights and women's rights movements.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T08:18:24Z"
    },
    {
      "title": "Expressing support for the designation of September 23, 2025, as \"Mary Church Terrell Day\", and calling on Congress to recognize Mary Church Terrell's lasting contributions to the civil rights and women's rights movements.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T08:05:42Z"
    }
  ]
}
```
