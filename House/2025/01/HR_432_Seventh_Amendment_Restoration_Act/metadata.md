# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/432?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/432
- Title: Seventh Amendment Restoration Act
- Congress: 119
- Bill type: HR
- Bill number: 432
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-05-24T08:05:46Z
- Update date including text: 2025-05-24T08:05:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/432",
    "number": "432",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Seventh Amendment Restoration Act",
    "type": "HR",
    "updateDate": "2025-05-24T08:05:46Z",
    "updateDateIncludingText": "2025-05-24T08:05:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:05:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr432ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 432\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo authorize the removal of an action from an administrative law judge of any administrative agency to a district court of the United States.\n#### 1. Short title\nThis Act may be cited as the Seventh Amendment Restoration Act .\n#### 2. Removal of case\nSection 702 of title 5, United States Code, is amended\u2014\n**(1)**\nby striking A person suffering and inserting the following:\n(a) In general A person suffering ; and\n**(2)**\nby adding at the end the following:\n(b) Removal (1) In general If a person against whom an action is brought before an agency hearing officer of any administrative agency desires to remove that action to any district court in which the person resides or has a principal place of business, such person shall file in such district court a notice of removal in the same manner in which a notice of removal from a State court is filed under section 1446 of title 28, United States Code. (2) Agency hearing officer defined In this subsection, the term agency hearing officer means an administrative law judge or another agency employee authorized to hear the action. .",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative remedies",
            "updateDate": "2025-02-27T15:20:06Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-27T15:20:01Z"
          },
          {
            "name": "Judicial procedure and administration",
            "updateDate": "2025-02-27T15:20:13Z"
          },
          {
            "name": "Jurisdiction and venue",
            "updateDate": "2025-02-27T15:20:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-02-11T20:18:47Z"
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
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr432ih.xml"
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
      "title": "Seventh Amendment Restoration Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Seventh Amendment Restoration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the removal of an action from an administrative law judge of any administrative agency to a district court of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:38Z"
    }
  ]
}
```
