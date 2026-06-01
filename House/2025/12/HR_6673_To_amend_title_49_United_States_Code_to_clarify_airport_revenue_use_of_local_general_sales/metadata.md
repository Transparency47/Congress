# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6673?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6673
- Title: To amend title 49, United States Code, to clarify airport revenue use of local general sales taxes, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6673
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-03T09:05:58Z
- Update date including text: 2026-02-03T09:05:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Aviation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6673",
    "number": "6673",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "S001157",
        "district": "13",
        "firstName": "David",
        "fullName": "Rep. Scott, David [D-GA-13]",
        "lastName": "Scott",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "To amend title 49, United States Code, to clarify airport revenue use of local general sales taxes, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:58Z",
    "updateDateIncludingText": "2026-02-03T09:05:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Aviation.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:38:43Z",
              "name": "Referred to"
            }
          },
          "name": "Aviation Subcommittee",
          "systemCode": "hspw05"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6673ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6673\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. David Scott of Georgia introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to clarify airport revenue use of local general sales taxes, and for other purposes.\n#### 1. Amendments to title 49, United States Code\n##### (a) Written assurances on revenue use\nSection 47107(b) of title 49, United States Code, is amended by adding at the end the following:\n(4) This subsection does not apply to local general sales taxes as provided in section 47133(b)(4). .\n##### (b) Restriction on use of revenues\nSection 47133(b) of title 49, United States Code, is amended by adding at the end the following:\n(4) Local general sales taxes Subsection (a) shall not apply to revenues from generally applicable sales taxes imposed by a local government provided\u2014 (A) the local government had a generally applicable sales tax that did not exclude aviation fuel in effect prior to December 9, 2014; (B) the local government is not a sponsor of a public airport; and (C) a large hub airport, which had more than 35,000,000 enplanements in calendar year 2021, is located within the jurisdiction of the local government. .",
      "versionDate": "2025-12-11",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T15:11:31Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6673ih.xml"
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
      "title": "To amend title 49, United States Code, to clarify airport revenue use of local general sales taxes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:19Z"
    },
    {
      "title": "To amend title 49, United States Code, to clarify airport revenue use of local general sales taxes, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T09:07:04Z"
    }
  ]
}
```
