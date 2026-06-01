# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7596?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7596
- Title: Improving Housing Access Act
- Congress: 119
- Bill type: HR
- Bill number: 7596
- Origin chamber: House
- Introduced date: 2026-02-17
- Update date: 2026-03-20T18:22:34Z
- Update date including text: 2026-03-20T18:22:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-17: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-02-17: Introduced in House

## Actions

- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Introduced in House
- 2026-02-17 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-17",
    "latestAction": {
      "actionDate": "2026-02-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7596",
    "number": "7596",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Improving Housing Access Act",
    "type": "HR",
    "updateDate": "2026-03-20T18:22:34Z",
    "updateDateIncludingText": "2026-03-20T18:22:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-17",
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
      "actionDate": "2026-02-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-17",
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
          "date": "2026-02-17T16:01:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7596ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7596\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 17, 2026 Mr. Lawler introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo direct the Comptroller General of the United States to conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled.\n#### 1. Short title\nThis Act may be cited as the Improving Housing Access Act .\n#### 2. Improving housing for the elderly and disabled\nThe Comptroller General of the United States shall, not later than 1 year after the date of the enactment of this section, conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled, including any potential impacts of providing capital advances for\u2014\n**(1)**\nthe program for supportive housing for the elderly under section 202 of the Housing Act of 1959; and\n**(2)**\nthe program for supportive housing for persons with disabilities under section 811 of the Cranston-Gonzalez National Affordable Housing Act.",
      "versionDate": "2026-02-17",
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
        "actionDate": "2025-12-19",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "4856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Revitalizing America\u2019s Housing Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-03",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3969",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Improving Housing Access Act",
      "type": "S"
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
        "name": "Housing and Community Development",
        "updateDate": "2026-03-02T18:20:44Z"
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
      "date": "2026-02-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7596ih.xml"
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
      "title": "Improving Housing Access Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-25T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Housing Access Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-25T06:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Comptroller General of the United States to conduct a study that identifies options to remove barriers and improve housing for persons who are elderly or disabled.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T06:33:38Z"
    }
  ]
}
```
