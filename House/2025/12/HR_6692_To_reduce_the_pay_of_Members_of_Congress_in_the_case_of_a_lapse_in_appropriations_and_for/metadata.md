# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6692?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6692
- Title: FUBAR Act
- Congress: 119
- Bill type: HR
- Bill number: 6692
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-01-08T15:02:29Z
- Update date including text: 2026-01-08T15:02:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-12 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-12 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6692",
    "number": "6692",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "M001216",
        "district": "7",
        "firstName": "Cory",
        "fullName": "Rep. Mills, Cory [R-FL-7]",
        "lastName": "Mills",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "FUBAR Act",
    "type": "HR",
    "updateDate": "2026-01-08T15:02:29Z",
    "updateDateIncludingText": "2026-01-08T15:02:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-12T14:02:20Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6692ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6692\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mr. Mills introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reduce the pay of Members of Congress in the case of a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Failed to Uphold the Budget? Allowance: Reduced Act or the FUBAR Act .\n#### 2. Reduction of pay\n##### (a) Reduction of pay\nNotwithstanding section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ), if on any day during a session of Congress there is a lapse in appropriations for any Federal agency or department as a result of a failure to enact a regular appropriations bill or continuing resolution, the rate of pay with respect to each Member of Congress for the period beginning on the first such day and ending on the last day of such session shall be one dollar.\n##### (b) Member of Congress defined\nIn this section, the term Member of Congress means an individual serving in a position under subparagraph (A), (B), or (C) of section 601(a) of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 4501 ).\n##### (c) Effective date\nThis section shall apply with respect to days occurring after the date of the next regularly scheduled general election for Federal office held after the date of the enactment of this Act.",
      "versionDate": "2025-12-12",
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
        "name": "Congress",
        "updateDate": "2026-01-08T15:02:28Z"
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
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6692ih.xml"
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
      "title": "FUBAR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FUBAR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Failed to Uphold the Budget? Allowance: Reduced Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce the pay of Members of Congress in the case of a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:19Z"
    }
  ]
}
```
