# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4059?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4059
- Title: SPEED Act
- Congress: 119
- Bill type: HR
- Bill number: 4059
- Origin chamber: House
- Introduced date: 2025-06-20
- Update date: 2025-12-05T22:54:32Z
- Update date including text: 2025-12-05T22:54:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-20: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-21 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-06-20: Introduced in House

## Actions

- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Introduced in House
- 2025-06-20 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-06-21 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-20",
    "latestAction": {
      "actionDate": "2025-06-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4059",
    "number": "4059",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
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
    "title": "SPEED Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:32Z",
    "updateDateIncludingText": "2025-12-05T22:54:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-21",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-20",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-20",
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
          "date": "2025-06-20T15:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-21T20:54:41Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4059ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4059\nIN THE HOUSE OF REPRESENTATIVES\nJune 20, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend MAP\u201321 to modify provisions relating to a categorical exclusion for projects of limited Federal assistance, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small Projects Expedited Execution and Delivery Act or the SPEED Act .\n#### 2. Categorical exclusion for projects of limited Federal assistance\nSection 1317(1) of MAP\u201321 ( 23 U.S.C. 109 note; Public Law 112\u2013141 ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking $6,000,000 and inserting $12,000,000 ; and\n**(2)**\nin subparagraph (B), by striking $35,000,000 and inserting $70,000,000 .",
      "versionDate": "2025-06-20",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "1894",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "SPEED Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-16T13:38:13Z"
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
      "date": "2025-06-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4059ih.xml"
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
      "title": "SPEED Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SPEED Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Projects Expedited Execution and Delivery Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend MAP-21 to modify provisions relating to a categorical exclusion for projects of limited Federal assistance, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:54Z"
    }
  ]
}
```
