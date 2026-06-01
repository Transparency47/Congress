# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/131
- Title: Providing amounts for the expenses of the Committee on Ethics in the One Hundred Nineteenth Congress.
- Congress: 119
- Bill type: HRES
- Bill number: 131
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-12-12T21:26:40Z
- Update date including text: 2025-12-12T21:26:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-13 - Committee: Submitted in House
- Latest action: 2025-02-13: Submitted in House

## Actions

- 2025-02-13 - IntroReferral: Referred to the House Committee on House Administration.
- 2025-02-13 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/131",
    "number": "131",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "G000591",
        "district": "3",
        "firstName": "Michael",
        "fullName": "Rep. Guest, Michael [R-MS-3]",
        "lastName": "Guest",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Providing amounts for the expenses of the Committee on Ethics in the One Hundred Nineteenth Congress.",
    "type": "HRES",
    "updateDate": "2025-12-12T21:26:40Z",
    "updateDateIncludingText": "2025-12-12T21:26:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:03:45Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres131ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 131\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Guest (for himself and Mr. DeSaulnier ) submitted the following resolution; which was referred to the Committee on House Administration\nRESOLUTION\nProviding amounts for the expenses of the Committee on Ethics in the One Hundred Nineteenth Congress.\n#### 1. Amounts for Committee Expenses\nFor the expenses of the Committee on Ethics (hereafter in this resolution referred to as the Committee ), including the expenses of all staff salaries, there shall be paid, out of the applicable accounts of the House of Representatives for committee salaries and expenses, not more than $9,276,290 for the One Hundred Nineteenth Congress.\n#### 2. Session Limitations\nOf the amount specified in section 1\u2014\n**(1)**\nnot more than $4,530,566 shall be available for expenses incurred during the period beginning at noon on January 3, 2025, and ending immediately before noon on January 3, 2026; and\n**(2)**\nnot more than $4,745,724 shall be available for expenses incurred during the period beginning at noon on January 3, 2026, and ending immediately before noon on January 3, 2027.\n#### 3. Vouchers\nPayments under this resolution shall be made on vouchers authorized by the Committee, signed by the Chairman of the Committee, and approved in the manner directed by the Committee on House Administration.\n#### 4. Regulations\nAmounts made available under this resolution shall be expended in accordance with regulations prescribed by the Committee on House Administration.",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional committees",
            "updateDate": "2025-04-24T14:07:34Z"
          },
          {
            "name": "House Committee on Ethics",
            "updateDate": "2025-04-24T14:07:41Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-18T16:23:22Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres131ih.xml"
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
      "title": "Providing amounts for the expenses of the Committee on Ethics in the One Hundred Nineteenth Congress.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T10:18:16Z"
    },
    {
      "title": "Providing amounts for the expenses of the Committee on Ethics in the One Hundred Nineteenth Congress.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:06:08Z"
    }
  ]
}
```
