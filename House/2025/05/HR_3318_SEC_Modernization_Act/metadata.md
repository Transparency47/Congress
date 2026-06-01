# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3318?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3318
- Title: SEC Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 3318
- Origin chamber: House
- Introduced date: 2025-05-09
- Update date: 2025-05-22T17:49:27Z
- Update date including text: 2025-05-22T17:49:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-09: Introduced in House
- 2025-05-09 - IntroReferral: Introduced in House
- 2025-05-09 - IntroReferral: Introduced in House
- 2025-05-09 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-05-09: Introduced in House

## Actions

- 2025-05-09 - IntroReferral: Introduced in House
- 2025-05-09 - IntroReferral: Introduced in House
- 2025-05-09 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-09",
    "latestAction": {
      "actionDate": "2025-05-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3318",
    "number": "3318",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000634",
        "district": "2",
        "firstName": "Troy",
        "fullName": "Rep. Downing, Troy [R-MT-2]",
        "lastName": "Downing",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "SEC Modernization Act",
    "type": "HR",
    "updateDate": "2025-05-22T17:49:27Z",
    "updateDateIncludingText": "2025-05-22T17:49:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-09",
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
      "actionDate": "2025-05-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-09",
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
          "date": "2025-05-09T17:00:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3318ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3318\nIN THE HOUSE OF REPRESENTATIVES\nMay 9, 2025 Mr. Downing introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the reorganization of certain offices within the Securities and Exchange Commission, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the SEC Modernization Act .\n#### 2. Commission organization\n##### (a) Changes to the organization of the Commission\n**(1) In general**\nThe Securities and Exchange Commission shall\u2014\n**(A)**\ntransfer the Office of the Secretary, the Office of the Ethics Counsel, and the Office of International Affairs into the Office of the General Counsel, with the heads of each transferred office reporting directly to the General Counsel;\n**(B)**\ntransfer the Office of the Chief Accountant, the Office of Credit Ratings, and the Office of Municipal Securities into the Division of Corporate Finance, with the heads of each transferred office reporting directly to the head of the Division of Corporate Finance;\n**(C)**\nmerge the Office of Legislative and Intergovernmental Affairs into the Office of Public Affairs, with the head of the larger of the two merged offices (by number of employees) becoming the head of the merged office, and such head reporting directly to the Chief of Staff; and\n**(D)**\ntransfer the Office of Investor Education and Advocacy into the Office of the Investor Advocate, with the head of the Office of Investor Education and Advocacy reporting directly to the Investor Advocate.\n**(2) Preservation of Commission authority**\nParagraph (1) shall not prohibit the Commission from reorganizing the offices described in such paragraph in the future, if the Commission determines such reorganization is necessary or appropriate in the public interest or for the protection of investors.\n##### (b) Regional office consolidation\nThe Securities and Exchange Commission shall, if the Commission determines it appropriate, consolidate the regional offices of the Commission.",
      "versionDate": "2025-05-09",
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
        "updateDate": "2025-05-22T17:49:27Z"
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
      "date": "2025-05-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3318ih.xml"
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
      "title": "SEC Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SEC Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the reorganization of certain offices within the Securities and Exchange Commission, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:28Z"
    }
  ]
}
```
