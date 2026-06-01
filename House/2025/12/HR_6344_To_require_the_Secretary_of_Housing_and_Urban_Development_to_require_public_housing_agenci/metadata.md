# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6344
- Title: CAT Act
- Congress: 119
- Bill type: HR
- Bill number: 6344
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-03-19T08:06:59Z
- Update date including text: 2026-03-19T08:06:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Financial Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6344",
    "number": "6344",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "T000486",
        "district": "15",
        "firstName": "Ritchie",
        "fullName": "Rep. Torres, Ritchie [D-NY-15]",
        "lastName": "Torres",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "CAT Act",
    "type": "HR",
    "updateDate": "2026-03-19T08:06:59Z",
    "updateDateIncludingText": "2026-03-19T08:06:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
          "date": "2025-12-01T17:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6344ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6344\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Torres of New York introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to require public housing agencies to disclose contracts entered into, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Contracting Accountability and Transparency Act or the CAT Act .\n#### 2. Disclosure required\nThe Secretary of Housing and Urban Development shall, not later than 1 year after the date of the enactment of this Act, require each public housing agencies to publicly disclose, on the website of the public housing agency, with respect to each contract entered into by such public housing agency the following information\u2014\n**(1)**\nall material information about the contract, including the goods and service provided;\n**(2)**\nthe vendor;\n**(3)**\nthe date of the solicitation of the contract;\n**(4)**\nthe bids and quotes solicited; and\n**(5)**\nthe official who solicited the contract.",
      "versionDate": "2025-12-01",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-12-19T16:17:16Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6344ih.xml"
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
      "title": "CAT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CAT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Contracting Accountability and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to require public housing agencies to disclose contracts entered into, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:21Z"
    }
  ]
}
```
