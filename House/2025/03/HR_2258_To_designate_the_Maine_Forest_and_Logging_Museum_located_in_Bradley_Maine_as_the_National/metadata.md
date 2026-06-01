# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2258?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2258
- Title: To designate the Maine Forest and Logging Museum, located in Bradley, Maine, as the National Museum of Forestry and Logging History.
- Congress: 119
- Bill type: HR
- Bill number: 2258
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2025-05-12T18:21:25Z
- Update date including text: 2025-05-12T18:21:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-03-21: Introduced in House

## Actions

- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-04 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2258",
    "number": "2258",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "G000592",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Golden, Jared F. [D-ME-2]",
        "lastName": "Golden",
        "party": "D",
        "state": "ME"
      }
    ],
    "title": "To designate the Maine Forest and Logging Museum, located in Bradley, Maine, as the National Museum of Forestry and Logging History.",
    "type": "HR",
    "updateDate": "2025-05-12T18:21:25Z",
    "updateDateIncludingText": "2025-05-12T18:21:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-04",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-04T13:14:36Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2258ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2258\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Mr. Golden of Maine introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo designate the Maine Forest and Logging Museum, located in Bradley, Maine, as the National Museum of Forestry and Logging History.\n#### 1. National Museum of Forestry and Logging History\nThe Maine Forest and Logging Museum, located in Bradley, Maine, shall be known and designated as the National Museum of Forestry and Logging History . Any reference in any law, map, regulation, document, record, or other paper of the United States to that museum shall be held to be a reference to the National Museum of Forestry and Logging History.",
      "versionDate": "2025-03-21",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-12T18:21:25Z"
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
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2258ih.xml"
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
      "title": "To designate the Maine Forest and Logging Museum, located in Bradley, Maine, as the National Museum of Forestry and Logging History.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:42Z"
    },
    {
      "title": "To designate the Maine Forest and Logging Museum, located in Bradley, Maine, as the National Museum of Forestry and Logging History.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T08:05:46Z"
    }
  ]
}
```
