# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6040?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6040
- Title: RESET Act
- Congress: 119
- Bill type: HR
- Bill number: 6040
- Origin chamber: House
- Introduced date: 2025-11-12
- Update date: 2025-12-10T16:56:56Z
- Update date including text: 2025-12-10T16:56:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-12: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-11-12: Introduced in House

## Actions

- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Introduced in House
- 2025-11-12 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-12",
    "latestAction": {
      "actionDate": "2025-11-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6040",
    "number": "6040",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "R000612",
        "district": "6",
        "firstName": "John",
        "fullName": "Rep. Rose, John W. [R-TN-6]",
        "lastName": "Rose",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "RESET Act",
    "type": "HR",
    "updateDate": "2025-12-10T16:56:56Z",
    "updateDateIncludingText": "2025-12-10T16:56:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-12",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-12",
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
          "date": "2025-11-12T17:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6040ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6040\nIN THE HOUSE OF REPRESENTATIVES\nNovember 12, 2025 Mr. Rose introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo repeal provisions relating to notification to Senate offices regarding legal process on disclosure of Senate data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Repealing Enrichment for Senators Exploited by Targeting Act or the RESET Act .\n#### 2. Repeal of senate notification requirements relating to legal process on disclosures of senate data\nSection 213 of title II of division C of the Continuing Appropriations, Agriculture, Legislative Branch, Military Construction and Veterans Affairs, and Extensions Act, 2026, and the amendments made by such section, are hereby repealed and shall have no force or effect.",
      "versionDate": "2025-11-12",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-20",
        "text": "Received in the Senate."
      },
      "number": "6019",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To repeal certain provisions relating to notification to Senate offices regarding legal process on disclosure of Senate data, and for other purposes.",
      "type": "HR"
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
        "name": "Congress",
        "updateDate": "2025-12-10T16:56:56Z"
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
      "date": "2025-11-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6040ih.xml"
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
      "title": "RESET Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-09T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "RESET Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Repealing Enrichment for Senators Exploited by Targeting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-09T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal provisions relating to notification to Senate offices regarding legal process on disclosure of Senate data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-09T10:18:22Z"
    }
  ]
}
```
