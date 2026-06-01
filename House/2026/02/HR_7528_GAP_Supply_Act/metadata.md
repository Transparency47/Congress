# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7528
- Title: GAP Supply Act
- Congress: 119
- Bill type: HR
- Bill number: 7528
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-02-27T19:02:21Z
- Update date including text: 2026-02-27T19:02:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7528",
    "number": "7528",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "GAP Supply Act",
    "type": "HR",
    "updateDate": "2026-02-27T19:02:21Z",
    "updateDateIncludingText": "2026-02-27T19:02:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:00:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7528ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7528\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Carter of Georgia introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend section 503B of the Federal Food, Drug, and Cosmetic Act to enhance the ability of outsourcing facilities to mitigate drug shortages by allowing a short-term period to continue supplying the market after a drug is in shortage.\n#### 1. Short title\nThis Act may be cited as the Growing America\u2019s Pharmaceutical Supply Act or the GAP Supply Act .\n#### 2. Providing for a tail period for outsourcing facilities to compound and distribute drugs in shortage\nSection 503B of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 353b ) is amended\u2014\n**(1)**\nin subsection (a)(2)(A)(ii), by striking at the time and inserting within 180 calendar days ; and\n**(2)**\nin subsection (d)(2)(A), by striking at the time and inserting within 180 calendar days .",
      "versionDate": "2026-02-12",
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
        "updateDate": "2026-02-27T19:02:21Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7528ih.xml"
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
      "title": "GAP Supply Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T09:38:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GAP Supply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T09:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing America\u2019s Pharmaceutical Supply Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T09:38:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 503B of the Federal Food, Drug, and Cosmetic Act to enhance the ability of outsourcing facilities to mitigate drug shortages by allowing a short-term period to continue supplying the market after a drug is in shortage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T09:33:38Z"
    }
  ]
}
```
