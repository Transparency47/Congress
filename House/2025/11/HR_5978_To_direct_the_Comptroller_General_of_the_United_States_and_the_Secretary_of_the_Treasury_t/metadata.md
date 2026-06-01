# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5978
- Title: Foreign Remittance Accountability and Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 5978
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-11-20T17:50:14Z
- Update date including text: 2025-11-20T17:50:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5978",
    "number": "5978",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001224",
        "district": "3",
        "firstName": "Keith",
        "fullName": "Rep. Self, Keith [R-TX-3]",
        "lastName": "Self",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Foreign Remittance Accountability and Transparency Act",
    "type": "HR",
    "updateDate": "2025-11-20T17:50:14Z",
    "updateDateIncludingText": "2025-11-20T17:50:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:05:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5978ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5978\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Self introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the Comptroller General of the United States and the Secretary of the Treasury to investigate and report on foreign government programs that facilitate Federal tax evasion.\n#### 1. Short title\nThis Act may be cited as the Foreign Remittance Accountability and Transparency Act .\n#### 2. Study and report\n##### (a) Study\nThe Comptroller General of the United States (hereinafter the Comptroller General ), in consultation with the Secretary of the Treasury (or the Secretary\u2019s delegate), shall conduct a study on foreign government programs that facilitate Federal tax evasion. In conducting the study, the Comptroller General shall\u2014\n**(1)**\nidentify foreign programs explicitly designed to support remittance transfers from individuals in the United States,\n**(2)**\ndetermine whether programs identified in paragraph (1) bypass the tax laws or reporting laws of the United States and whether such bypass is intentional, and\n**(3)**\nidentify the scope, financial volume, and policy implications of programs identified in paragraph (1).\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, the Comptroller General shall submit to Congress a report that contains\u2014\n**(1)**\nthe results of the study required by subsection (a), and\n**(2)**\npolicy recommendations for enforcement or regulatory responses to such results.",
      "versionDate": "2025-11-07",
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
        "name": "Taxation",
        "updateDate": "2025-11-20T17:50:14Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5978ih.xml"
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
      "title": "Foreign Remittance Accountability and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-12T15:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Foreign Remittance Accountability and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-12T15:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General of the United States and the Secretary of the Treasury to investigate and report on foreign government programs that facilitate Federal tax evasion.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-12T15:03:17Z"
    }
  ]
}
```
