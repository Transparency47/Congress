# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4538
- Title: PAPER Act
- Congress: 119
- Bill type: HR
- Bill number: 4538
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2025-09-11T15:43:29Z
- Update date including text: 2025-09-11T15:43:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4538",
    "number": "4538",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "PAPER Act",
    "type": "HR",
    "updateDate": "2025-09-11T15:43:29Z",
    "updateDateIncludingText": "2025-09-11T15:43:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:07:45Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4538ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4538\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Turner of Ohio introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo prohibit covered entities from requiring consumers to solely use digital monthly statements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Against Paperless and Electronic Requirements Act or the PAPER Act .\n#### 2. Requirement\n##### (a) In general\nEach covered entity shall offer each consumer of such entity the option of receiving paper copies of their monthly statements.\n##### (b) Prohibition\nA covered entity may not condition the use of any services offered by such entity on the sole use of digital monthly statements by a consumer.\n##### (c) Definitions\n**(1) Depository institution**\nThe term depository institution has the meaning given the term in section 3 of the Federal Deposit Act.\n**(2) Credit union**\nThe term credit union has the meaning given the term in section 101 of the Federal Credit Union Act.\n**(3) Covered entity**\nThe term covered entity means a depository institution or a credit union.",
      "versionDate": "2025-07-17",
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
        "updateDate": "2025-09-11T15:43:29Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4538ih.xml"
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
      "title": "PAPER Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:38:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PAPER Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Against Paperless and Electronic Requirements Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T12:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit covered entities from requiring consumers to solely use digital monthly statements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:33:29Z"
    }
  ]
}
```
