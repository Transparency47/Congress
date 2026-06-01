# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/150?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/150
- Title: Providing amounts for the expenses of the Committee on House Administration in the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 150
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-02-25T12:50:17Z
- Update date including text: 2025-02-25T12:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-21 - Committee: Submitted in House
- Latest action: 2025-02-21: Submitted in House

## Actions

- 2025-02-21 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-21 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/150",
    "number": "150",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Providing amounts for the expenses of the Committee on House Administration in the One Hundred Nineteenth Congress.",
    "type": "HRES",
    "updateDate": "2025-02-25T12:50:17Z",
    "updateDateIncludingText": "2025-02-25T12:50:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:35:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres150ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 150\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Steil submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nProviding amounts for the expenses of the Committee on House Administration in the One Hundred Nineteenth Congress.\n#### 1. Amounts for Committee Expenses\nFor the expenses of the Committee on House Administration (hereafter in this resolution referred to as the Committee ), including the expenses of all staff salaries, there shall be paid, out of the applicable accounts of the House of Representatives for committee salaries and expenses, not more than $16,885,446 for the One Hundred Nineteenth Congress.\n#### 2. Session Limitations\nOf the amount specified in section 1\u2014\n**(1)**\nnot more than $8,031,523 shall be available for expenses incurred during the period beginning at noon on January 3, 2025, and ending immediately before noon on January 3, 2026; and\n**(2)**\nnot more than $8,853,923 shall be available for expenses incurred during the period beginning at noon on January 3, 2026, and ending immediately before noon on January 3, 2027.\n#### 3. Vouchers\nPayments under this resolution shall be made on vouchers authorized by the Committee, signed by the Chairman of the Committee, and approved in the manner directed by the Committee on House Administration.\n#### 4. Regulations\nAmounts made available under this resolution shall be expended in accordance with regulations prescribed by the Committee on House Administration.",
      "versionDate": "2025-02-21",
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
        "updateDate": "2025-02-25T12:50:17Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres150ih.xml"
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
      "title": "Providing amounts for the expenses of the Committee on House Administration in the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T09:48:41Z"
    },
    {
      "title": "Providing amounts for the expenses of the Committee on House Administration in the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T09:06:47Z"
    }
  ]
}
```
