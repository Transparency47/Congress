# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5834?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5834
- Title: Critical Water Supplies for Resilient Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 5834
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-04-10T12:41:25Z
- Update date including text: 2026-04-10T12:41:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-25 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-25 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5834",
    "number": "5834",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Critical Water Supplies for Resilient Communities Act",
    "type": "HR",
    "updateDate": "2026-04-10T12:41:25Z",
    "updateDateIncludingText": "2026-04-10T12:41:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-25",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
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
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:01:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-25T17:01:51Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5834ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5834\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Ms. Wilson of Florida introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to make changes to the program authorizing grants for alternative water source projects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Water Supplies for Resilient Communities Act .\n#### 2. Alternative water source projects\nSection 220 of the Federal Water Pollution Control Act ( 33 U.S.C. 1300 ) is amended\u2014\n**(1)**\nin the section heading, by striking Pilot Program and inserting Grants ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking treatment or ; and\n**(B)**\nby striking paragraph (2) and inserting the following:\n(2) Critical water supply needs The term critical water supply needs means existing or reasonably anticipated future water supply needs that are identified in a plan or assessment, developed with public engagement, for\u2014 (A) comprehensive local, statewide, or regional water supply; or (B) local or regional drought resiliency. ;\n**(3)**\nin subsection (c)\u2014\n**(A)**\nin the subsection heading, by striking Establishment and inserting Authority ; and\n**(B)**\nby striking establish a pilot program to ;\n**(4)**\nby striking subsection (h) and inserting the following:\n(h) Reports On the date on which the budget of the President is submitted to Congress pursuant to section 1105 of title 31, United States Code, for each fiscal year, the Administrator shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Environment and Public Works of the Senate a report describing each alternative water source project funded under this section in the preceding fiscal year, including a description of how each such project addresses the critical water supply needs it is designed to meet. ; and\n**(5)**\nin subsection (i)(1), by striking 2026 and inserting 2031 .",
      "versionDate": "2025-10-24",
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-10T12:41:25Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5834ih.xml"
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
      "title": "Critical Water Supplies for Resilient Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Critical Water Supplies for Resilient Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to make changes to the program authorizing grants for alternative water source projects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T10:03:12Z"
    }
  ]
}
```
