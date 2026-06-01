# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7991?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7991
- Title: STOP RGGI Act
- Congress: 119
- Bill type: HR
- Bill number: 7991
- Origin chamber: House
- Introduced date: 2026-03-18
- Update date: 2026-04-02T18:12:03Z
- Update date including text: 2026-04-02T18:12:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-18: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-18: Introduced in House

## Actions

- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Introduced in House
- 2026-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-18",
    "latestAction": {
      "actionDate": "2026-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7991",
    "number": "7991",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "STOP RGGI Act",
    "type": "HR",
    "updateDate": "2026-04-02T18:12:03Z",
    "updateDateIncludingText": "2026-04-02T18:12:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-18",
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
      "actionDate": "2026-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-18",
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
          "date": "2026-03-18T14:02:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7991ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7991\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2026 Mr. Van Drew introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit States from imposing charges for the purpose of funding the Regional Greenhouse Gas Initiative Energy Efficiency Program.\n#### 1. Short title\nThis Act may be cited as the Stop Taxing Our Power Act or the STOP RGGI Act .\n#### 2. Prohibition on State funding of the Regional Greenhouse Gas Initiative Energy Efficiency Program\nNo State may impose a charge for purposes of funding the Regional Greenhouse Gas Initiative Energy Efficiency Program.",
      "versionDate": "2026-03-18",
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
        "name": "Energy",
        "updateDate": "2026-04-02T18:12:02Z"
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
      "date": "2026-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7991ih.xml"
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
      "title": "STOP RGGI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-31T06:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "STOP RGGI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Taxing Our Power Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-31T06:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit States from imposing charges for the purpose of funding the Regional Greenhouse Gas Initiative Energy Efficiency Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T06:33:35Z"
    }
  ]
}
```
