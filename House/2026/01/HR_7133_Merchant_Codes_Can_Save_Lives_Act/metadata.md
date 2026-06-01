# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7133?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7133
- Title: Merchant Codes Can Save Lives Act
- Congress: 119
- Bill type: HR
- Bill number: 7133
- Origin chamber: House
- Introduced date: 2026-01-16
- Update date: 2026-04-02T21:13:32Z
- Update date including text: 2026-04-02T21:13:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-16: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-01-16: Introduced in House

## Actions

- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Introduced in House
- 2026-01-16 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-16",
    "latestAction": {
      "actionDate": "2026-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7133",
    "number": "7133",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "F000476",
        "district": "10",
        "firstName": "Maxwell",
        "fullName": "Rep. Frost, Maxwell [D-FL-10]",
        "lastName": "Frost",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Merchant Codes Can Save Lives Act",
    "type": "HR",
    "updateDate": "2026-04-02T21:13:32Z",
    "updateDateIncludingText": "2026-04-02T21:13:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-16",
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
      "actionDate": "2026-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-16",
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
          "date": "2026-01-16T20:01:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7133ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7133\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2026 Mr. Frost introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit States from prohibiting or otherwise deterring the usage of any merchant category code established by the International Organization for Standardization, including codes that identify firearm merchants and ammunition merchants.\n#### 1. Short title\nThis Act may be cited as the Merchant Codes Can Save Lives Act .\n#### 2. Preemption relating to merchant category codes\nSection 5313 of title 31, United States Code, is amended by inserting after subsection (g) the following:\n(h) Merchant category code usage (1) In general No State may prohibit or otherwise deter the usage of any merchant category code established by the International Organization for Standardization for identifying firearm merchants or payment card transactions involving the purchase of a firearm, firearm ammunition, ammunition components for use with firearms, or firearm accessories. (2) Enforcement The Attorney General may bring a civil action in the appropriate district court to enforce this subsection. .",
      "versionDate": "2026-01-16",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-04-02T21:13:32Z"
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
      "date": "2026-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7133ih.xml"
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
      "title": "Merchant Codes Can Save Lives Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Merchant Codes Can Save Lives Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T13:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit States from prohibiting or otherwise deterring the usage of any merchant category code established by the International Organization for Standardization, including codes that identify firearm merchants and ammunition merchants.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T13:03:39Z"
    }
  ]
}
```
