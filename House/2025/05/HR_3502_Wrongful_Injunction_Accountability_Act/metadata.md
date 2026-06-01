# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3502?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3502
- Title: Wrongful Injunction Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 3502
- Origin chamber: House
- Introduced date: 2025-05-19
- Update date: 2025-06-12T08:07:02Z
- Update date including text: 2025-06-12T08:07:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-19: Introduced in House

## Actions

- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Introduced in House
- 2025-05-19 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3502",
    "number": "3502",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "S001228",
        "district": "2",
        "firstName": "Derek",
        "fullName": "Rep. Schmidt, Derek [R-KS-2]",
        "lastName": "Schmidt",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Wrongful Injunction Accountability Act",
    "type": "HR",
    "updateDate": "2025-06-12T08:07:02Z",
    "updateDateIncludingText": "2025-06-12T08:07:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-19",
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
          "date": "2025-05-19T16:00:25Z",
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
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WY"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3502ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3502\nIN THE HOUSE OF REPRESENTATIVES\nMay 19, 2025 Mr. Schmidt (for himself and Ms. Hageman ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo ensure recovery of taxpayer costs and damages in restraining actions wrongfully brought against the United States.\n#### 1. Short title\nThis Act may be cited as the Wrongful Injunction Accountability Act .\n#### 2. Liability arising from inadequate security posted\nIf the United States (including an agency, officer or employee of the United States) is found to have been wrongfully enjoined or restrained under rule 65 of the Federal Rules of Civil Procedure (28 U.S.C. App.) and the security required under subsection (c) of such rule is not ordered by the court or is insufficient to pay the costs and damages sustained by the United States, then the movant shall be liable to the United States for the costs and damages sustained.",
      "versionDate": "2025-05-19",
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
        "name": "Law",
        "updateDate": "2025-05-29T15:26:13Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3502ih.xml"
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
      "title": "Wrongful Injunction Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-28T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wrongful Injunction Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-28T03:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure recovery of taxpayer costs and damages in restraining actions wrongfully brought against the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T03:48:21Z"
    }
  ]
}
```
