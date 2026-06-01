# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8088?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8088
- Title: Growing Deposit Insurance for the Future Act
- Congress: 119
- Bill type: HR
- Bill number: 8088
- Origin chamber: House
- Introduced date: 2026-03-25
- Update date: 2026-04-13T19:08:25Z
- Update date including text: 2026-04-13T19:08:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-03-25: Introduced in House

## Actions

- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Introduced in House
- 2026-03-25 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8088",
    "number": "8088",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "M001204",
        "district": "9",
        "firstName": "Daniel",
        "fullName": "Rep. Meuser, Daniel [R-PA-9]",
        "lastName": "Meuser",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Growing Deposit Insurance for the Future Act",
    "type": "HR",
    "updateDate": "2026-04-13T19:08:25Z",
    "updateDateIncludingText": "2026-04-13T19:08:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T14:02:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8088ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8088\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2026 Mr. Meuser introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Federal Deposit Insurance Act to update the inflation adjustment applicable to deposit insurance and share insurance.\n#### 1. Short title\nThis Act may be cited as the Growing Deposit Insurance for the Future Act .\n#### 2. Insurance inflation adjustment\nSection 11(a)(1)(F)(i) of the Federal Deposit Insurance Act ( 12 U.S.C. 1821(a)(1)(F)(i) ) is amended\u2014\n**(1)**\nby striking 2010 and inserting 2030 ;\n**(2)**\nin subclause (I), by striking $100,000 and inserting the standard maximum deposit insurance amount described in subparagraph (E), before any adjustment as provided under this subparagraph ; and\n**(3)**\nin subclause (II), by striking the date this subparagraph takes effect under the Federal Deposit Insurance Reform Act of 2005 and inserting the date of enactment of the Growing Deposit Insurance for the Future Act .",
      "versionDate": "2026-03-25",
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
        "updateDate": "2026-04-13T19:08:24Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8088ih.xml"
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
      "title": "Growing Deposit Insurance for the Future Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Growing Deposit Insurance for the Future Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T05:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Deposit Insurance Act to update the inflation adjustment applicable to deposit insurance and share insurance.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T05:18:31Z"
    }
  ]
}
```
