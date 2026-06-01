# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7447?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7447
- Title: Community Risk Training and Response Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7447
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-20T16:50:08Z
- Update date including text: 2026-02-20T16:50:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7447",
    "number": "7447",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "P000620",
        "district": "7",
        "firstName": "Brittany",
        "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
        "lastName": "Pettersen",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Community Risk Training and Response Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-20T16:50:08Z",
    "updateDateIncludingText": "2026-02-20T16:50:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:03:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7447ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7447\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Ms. Pettersen introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo provide grants for technical assistance for State crisis intervention programs.\n#### 1. Short title\nThis Act may be cited as the Community Risk Training and Response Act of 2026 .\n#### 2. Grants\nThe Attorney General shall make grants to States for a term of 1 year in an amount of not less than $200,000 and not more than $500,000 for purposes of providing technical assistance to State and local\u2014\n**(1)**\nlaw enforcement;\n**(2)**\nprosecutors;\n**(3)**\njudges and court staff;\n**(4)**\nhealthcare providers;\n**(5)**\neducators; and\n**(6)**\nagencies designated to coordinate extreme risk protection order implementation,\nto develop standardized extreme risk protection order training, curriculum, and model implementation materials for States, and thereby to ensure consistent, evidence-based processes nationwide and support States in effective, timely implementation of State crisis intervention court proceedings and related programs or initiatives.",
      "versionDate": "2026-02-09",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2026-02-20T16:50:08Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7447ih.xml"
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
      "title": "To provide grants for technical assistance for State crisis intervention programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T09:05:42Z"
    },
    {
      "title": "Community Risk Training and Response Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Risk Training and Response Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    }
  ]
}
```
