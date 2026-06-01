# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2482?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2482
- Title: TRICARE Travel Improvement Act
- Congress: 119
- Bill type: S
- Bill number: 2482
- Origin chamber: Senate
- Introduced date: 2025-07-28
- Update date: 2025-09-19T17:42:55Z
- Update date including text: 2025-09-19T17:42:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-28: Introduced in Senate
- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-28: Introduced in Senate

## Actions

- 2025-07-28 - IntroReferral: Introduced in Senate
- 2025-07-28 - IntroReferral: Read twice and referred to the Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-28",
    "latestAction": {
      "actionDate": "2025-07-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2482",
    "number": "2482",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "H001046",
        "district": "",
        "firstName": "Martin",
        "fullName": "Sen. Heinrich, Martin [D-NM]",
        "lastName": "Heinrich",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "TRICARE Travel Improvement Act",
    "type": "S",
    "updateDate": "2025-09-19T17:42:55Z",
    "updateDateIncludingText": "2025-09-19T17:42:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-28",
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
      "actionDate": "2025-07-28",
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
          "date": "2025-07-28T22:33:29Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2482is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2482\nIN THE SENATE OF THE UNITED STATES\nJuly 28, 2025 Mr. Heinrich introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to reduce the distance required for the Secretary of Defense to reimburse travel expenses relating to specialty care, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the TRICARE Travel Improvement Act .\n#### 2. Reimbursement by the Secretary of Defense for travel expenses relating to specialty care\nSection 1074i of title 10, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking In any case and inserting Except as provided in subsection (b), in any case ; and\n**(B)**\nby striking 100 miles and inserting 50 miles ; and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nby striking the heading and inserting Special rules for exceptional circumstances and military retirees and dependents .\u2014 ;\n**(B)**\nby striking The Secretary of Defense and inserting (1) The Secretary of Defense ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) With respect to military retirees and their dependents, the Secretary shall administer subsection (a) by substituting 100 miles for 50 miles . .",
      "versionDate": "2025-07-28",
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
        "updateDate": "2025-09-19T17:42:55Z"
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
      "date": "2025-07-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2482is.xml"
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
      "title": "TRICARE Travel Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TRICARE Travel Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to reduce the distance required for the Secretary of Defense to reimburse travel expenses relating to specialty care, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:25Z"
    }
  ]
}
```
