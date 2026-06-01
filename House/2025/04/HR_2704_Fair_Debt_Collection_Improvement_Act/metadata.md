# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2704?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2704
- Title: Fair Debt Collection Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 2704
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2025-05-05T13:53:22Z
- Update date including text: 2025-05-05T13:53:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2704",
    "number": "2704",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001068",
        "district": "9",
        "firstName": "Steve",
        "fullName": "Rep. Cohen, Steve [D-TN-9]",
        "lastName": "Cohen",
        "party": "D",
        "state": "TN"
      }
    ],
    "title": "Fair Debt Collection Improvement Act",
    "type": "HR",
    "updateDate": "2025-05-05T13:53:22Z",
    "updateDateIncludingText": "2025-05-05T13:53:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:06:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2704ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2704\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Cohen introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Fair Debt Collection Practices Act to prohibit debt collectors from collecting, or attempting to collect, on a debt of a consumer with respect to which the statute of limitations has expired, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Debt Collection Improvement Act .\n#### 2. Prohibition on collecting time-barred debt\n##### (a) In general\nThe Fair Debt Collection Practices Act ( 15 U.S.C. 1692 et seq. ) is amended by inserting after section 811 the following:\n811A. Prohibition on collecting time-barred debt A debt collector may not collect, or attempt to collect, any debt of a consumer with respect to which the governing statute of limitations has expired. .\n##### (b) Clerical amendment\nThe table of contents for the Fair Debt Collection Practices Act is amended by inserting after the item relating to section 811 the following:\n811A. Prohibition on collecting time-barred debt. .",
      "versionDate": "2025-04-08",
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
        "updateDate": "2025-05-05T13:53:22Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2704ih.xml"
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
      "title": "Fair Debt Collection Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-18T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Debt Collection Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-18T03:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Fair Debt Collection Practices Act to prohibit debt collectors from collecting, or attempting to collect, on a debt of a consumer with respect to which the statute of limitations has expired, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-18T03:18:25Z"
    }
  ]
}
```
