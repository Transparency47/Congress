# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7619?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7619
- Title: Keep Jobs in California Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7619
- Origin chamber: House
- Introduced date: 2026-02-20
- Update date: 2026-03-20T15:28:42Z
- Update date including text: 2026-03-20T15:28:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-20: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-20: Introduced in House

## Actions

- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Introduced in House
- 2026-02-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-20",
    "latestAction": {
      "actionDate": "2026-02-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7619",
    "number": "7619",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Keep Jobs in California Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-20T15:28:42Z",
    "updateDateIncludingText": "2026-03-20T15:28:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-20",
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
          "date": "2026-02-20T16:34:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7619ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7619\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 20, 2026 Mr. Kiley of California introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit a State from imposing a retroactive tax on assets of nonresident individuals.\n#### 1. Short title\nThis Act may be cited as the Keep Jobs in California Act of 2026 .\n#### 2. Prohibition retroactive asset tax on nonresidents\nA State shall not impose a tax on nonresident individuals based on the value of the assets of such individuals if such tax is attributable to the value of such assets for any period before the date of the enactment of the Act that imposes such tax and if such individuals do not reside in such State as of the date of the enactment of such Act.\n#### 3. Effective date\nThis Act shall take effect on January 1, 2026.",
      "versionDate": "2026-02-20",
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
        "updateDate": "2026-03-20T15:28:42Z"
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
      "date": "2026-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7619ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit a State from imposing a retroactive tax on assets of nonresident individuals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T08:07:21Z"
    },
    {
      "title": "Keep Jobs in California Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Keep Jobs in California Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:24Z"
    }
  ]
}
```
