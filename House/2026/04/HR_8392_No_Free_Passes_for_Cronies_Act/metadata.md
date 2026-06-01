# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8392?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8392
- Title: No Free Passes for Cronies Act
- Congress: 119
- Bill type: HR
- Bill number: 8392
- Origin chamber: House
- Introduced date: 2026-04-20
- Update date: 2026-05-01T18:27:56Z
- Update date including text: 2026-05-01T18:27:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2026-04-20: Introduced in House

## Actions

- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Introduced in House
- 2026-04-20 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8392",
    "number": "8392",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "S001205",
        "district": "5",
        "firstName": "Mary Gay",
        "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
        "lastName": "Scanlon",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "No Free Passes for Cronies Act",
    "type": "HR",
    "updateDate": "2026-05-01T18:27:56Z",
    "updateDateIncludingText": "2026-05-01T18:27:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-20",
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
      "actionDate": "2026-04-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T16:04:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8392ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8392\nIN THE HOUSE OF REPRESENTATIVES\nApril 20, 2026 Ms. Scanlon introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend the Federal Rules of Criminal Procedure to provide for when the government may move the court to dismiss an indictment, information, or complaint, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Free Passes for Cronies Act .\n#### 2. Motion by the government to dismiss an indictment, information, or complaint\nRule 48(a) of the Federal Rules of Criminal Procedure is amended to read as follows:\n(a) Motion by the government The government may move the court to dismiss an indictment, information, or complaint. The court may, upon consideration of the interests of justice, grant or deny such motion, except that the court may not grant such a motion to dismiss the prosecution during trial without the defendant\u2019s consent. .",
      "versionDate": "2026-04-20",
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
        "updateDate": "2026-05-01T18:27:56Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8392ih.xml"
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
      "title": "No Free Passes for Cronies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-25T04:38:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Free Passes for Cronies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-25T04:38:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Rules of Criminal Procedure to provide for when the government may move the court to dismiss an indictment, information, or complaint, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-25T04:33:38Z"
    }
  ]
}
```
