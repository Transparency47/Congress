# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/876
- Title: To amend the Defense Base Act to exclude Guam.
- Congress: 119
- Bill type: HR
- Bill number: 876
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-09-29T14:09:51Z
- Update date including text: 2025-09-29T14:09:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/876",
    "number": "876",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "M001219",
        "district": "",
        "firstName": "James",
        "fullName": "Del. Moylan, James C. [R-GU-At Large]",
        "lastName": "Moylan",
        "party": "R",
        "state": "GU"
      }
    ],
    "title": "To amend the Defense Base Act to exclude Guam.",
    "type": "HR",
    "updateDate": "2025-09-29T14:09:51Z",
    "updateDateIncludingText": "2025-09-29T14:09:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:03:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr876ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 876\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Mr. Moylan introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Defense Base Act to exclude Guam.\n#### 1. Inapplicability of Defense Base Act to Guam\nSubsection (b) of section 1 of the Defense Base Act (Chapter 357; 55 Stat. 622; 42 U.S.C. 1651 ) is amended\u2014\n**(1)**\nin paragraph (4), by striking the period at the end and inserting and Guam; ; and\n**(2)**\nby adding at the end the following new paragraph:\n(5) the term Territory or possession outside the continental United States does not include Guam. .",
      "versionDate": "2025-01-31",
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
            "name": "Employee benefits and pensions",
            "updateDate": "2025-09-29T14:09:46Z"
          },
          {
            "name": "Guam",
            "updateDate": "2025-09-29T14:09:34Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-09-29T14:09:51Z"
          },
          {
            "name": "U.S. territories and protectorates",
            "updateDate": "2025-09-29T14:09:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-05-02T16:07:11Z"
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
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr876ih.xml"
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
      "title": "To amend the Defense Base Act to exclude Guam.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-01T04:48:33Z"
    },
    {
      "title": "To amend the Defense Base Act to exclude Guam.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-01T09:05:59Z"
    }
  ]
}
```
