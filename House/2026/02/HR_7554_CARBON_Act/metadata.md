# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7554
- Title: CARBON Act
- Congress: 119
- Bill type: HR
- Bill number: 7554
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-03-09T12:21:51Z
- Update date including text: 2026-03-09T12:21:51Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7554",
    "number": "7554",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "O000177",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Onder, Robert F. [R-MO-3]",
        "lastName": "Onder",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "CARBON Act",
    "type": "HR",
    "updateDate": "2026-03-09T12:21:51Z",
    "updateDateIncludingText": "2026-03-09T12:21:51Z"
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
          "date": "2026-02-12T14:05:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7554ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7554\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Onder introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to exclude carbon dioxide, methane, and nitrous oxide from the definition of the term air pollutant .\n#### 1. Short title\nThis Act may be cited as the Curtailing Agency Reach and Bureaucracy Overreach on Net-Zero Act or the CARBON Act .\n#### 2. Exclusion of carbon dioxide, methane, and nitrous oxide\nSection 302(g) of the Clean Air Act ( 42 U.S.C. 7602(g) ) is amended by adding at the end Such term does not include carbon dioxide, methane, or nitrous oxide. .",
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
        "name": "Environmental Protection",
        "updateDate": "2026-03-09T12:21:51Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7554ih.xml"
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
      "title": "CARBON Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T03:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CARBON Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Curtailing Agency Reach and Bureaucracy Overreach on Net-Zero Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-05T03:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to exclude carbon dioxide, methane, and nitrous oxide from the definition of the term \"air pollutant\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-05T03:18:23Z"
    }
  ]
}
```
