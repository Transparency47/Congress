# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8148
- Title: Prediction Market RISK Act
- Congress: 119
- Bill type: HR
- Bill number: 8148
- Origin chamber: House
- Introduced date: 2026-03-27
- Update date: 2026-04-14T13:57:52Z
- Update date including text: 2026-04-23T16:27:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-27: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-03-27: Introduced in House

## Actions

- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Introduced in House
- 2026-03-27 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-27",
    "latestAction": {
      "actionDate": "2026-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8148",
    "number": "8148",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001196",
        "district": "6",
        "firstName": "Seth",
        "fullName": "Rep. Moulton, Seth [D-MA-6]",
        "lastName": "Moulton",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Prediction Market RISK Act",
    "type": "HR",
    "updateDate": "2026-04-14T13:57:52Z",
    "updateDateIncludingText": "2026-04-23T16:27:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-27",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-27",
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
          "date": "2026-03-28T01:34:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8148ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8148\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2026 Mr. Moulton introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo reaffirm the Commodity Futures Trading Commission\u2019s authority to enforce prohibited activity on prediction markets.\n#### 1. Short title\nThis Act may be cited as the Prediction Market Restrictions on Insider Speculation and Knowledge-Trading Act or the Prediction Market RISK Act .\n#### 2. Definition\nThe term prediction market contract means any financial instrument, contract, or derivative listed on or offered by a platform engaged in interstate commerce and tied to the occurrence or non-occurrence of a future event, including market-based event contracts.\n#### 3. CFTC authority to enforce prohibited transactions occurring in relation to a prediction market contract\nSection 4(c) and section 6(c) of the Commodity Exchange Act ( 7 U.S.C. 7a\u20132(c) ) apply to illegal trading practices occurring with relation to a prediction market contract.",
      "versionDate": "2026-03-27",
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
        "updateDate": "2026-04-14T13:57:52Z"
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
      "date": "2026-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8148ih.xml"
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
      "title": "Prediction Market RISK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-08T12:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prediction Market RISK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Prediction Market Restrictions on Insider Speculation and Knowledge-Trading Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-08T12:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reaffirm the Commodity Futures Trading Commission's authority to enforce prohibited activity on prediction markets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-08T12:18:46Z"
    }
  ]
}
```
