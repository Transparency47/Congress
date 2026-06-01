# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3581?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3581
- Title: Protect DSH Act
- Congress: 119
- Bill type: HR
- Bill number: 3581
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2025-06-16T13:21:12Z
- Update date including text: 2025-06-16T13:21:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3581",
    "number": "3581",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001120",
        "district": "2",
        "firstName": "Dan",
        "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
        "lastName": "Crenshaw",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Protect DSH Act",
    "type": "HR",
    "updateDate": "2025-06-16T13:21:12Z",
    "updateDateIncludingText": "2025-06-16T13:21:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-05-23T14:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3581ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3581\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Crenshaw introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to delay certain disproportionate share hospital payment reductions under the Medicaid program.\n#### 1. Short title\nThis Act may be cited as the Protect DSH Act .\n#### 2. Delaying DSH Reductions\n##### (a) In general\nSection 1923(f) of the Social Security Act ( 42 U.S.C. 1396r\u20134(f) ) is amended\u2014\n**(1)**\nin paragraph (7)(A)\u2014\n**(A)**\nin clause (i)\u2014\n**(i)**\nin the matter preceding subclause (I), by striking 2026 through 2028 and inserting 2029 through 2031 ; and\n**(ii)**\nin subclause (II), by striking or period ; and\n**(B)**\nin clause (ii), by striking 2026 through 2028 and inserting 2029 through 2031 ; and (2) in paragraph (8), by striking 2027 and inserting 2031 .",
      "versionDate": "2025-05-23",
      "versionType": "Introduced in House"
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
        "name": "Health",
        "updateDate": "2025-06-16T13:21:12Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3581ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Protect DSH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect DSH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to delay certain disproportionate share hospital payment reductions under the Medicaid program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:34Z"
    }
  ]
}
```
