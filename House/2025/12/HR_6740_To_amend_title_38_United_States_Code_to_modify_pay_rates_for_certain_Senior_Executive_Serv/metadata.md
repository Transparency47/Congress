# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6740?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6740
- Title: VA TRUST Act
- Congress: 119
- Bill type: HR
- Bill number: 6740
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-05-21T08:07:41Z
- Update date including text: 2026-05-21T08:07:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6740",
    "number": "6740",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "VA TRUST Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:41Z",
    "updateDateIncludingText": "2026-05-21T08:07:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
        "item": [
          {
            "date": "2026-05-20T13:25:59Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:45:45Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-12-16T15:02:05Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6740ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6740\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Flood introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to modify pay rates for certain Senior Executive Service employees at the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veterans Affairs Transparency and Reform of the Upper Senior Tenure Act or the VA TRUST Act .\n#### 2. Pay for senior executive positions\n##### (a) Reports on performance awards and bonuses to high-Level employees\nSection 726(b) of title 38, United States Code, is amended by adding at the end the following:\n(4) The appropriations accounts from which amounts were used to pay such an award or bonus. (5) The annual basic rate of pay for each individual awarded the award or bonus. .\n##### (b) Pay for senior executive positions\n**(1) In general**\nSubchapter I of chapter 7 of title 38, United States Code, is amended by adding at the end the following:\n729. Pay for senior executive positions (a) Rates of pay Any individual appointed to a senior executive position within the Department shall receive the annual rate of basic pay applicable to such a position, as determined by the Secretary, in accordance with the pay ranges, structure, and aggregate limitations established for the Senior Executive Service under subchapter VIII of chapter 53 of title 5, including section 5382. (b) Career appointees transferring from other agencies Any career appointee who transfers from another agency to a senior executive position at the Department shall receive the annual rate of basic pay applicable to such position, as determined by the Secretary under subsection (a), and such rate shall be consistent with the individual\u2019s performance and pay level under sections 5383 and 5384 of title 5. (c) Transfers within the Department If any individual occupying a senior executive position at the Department transfers or otherwise moves to another senior executive position within the Department, the individual shall, effective on the first day of the first pay period beginning after the date that the individual first occupies such other position, receive the rate of basic pay established by the Secretary for that position under subsection (a). The Secretary may adjust such rate only to the extent authorized under section 5382 or 5383 of title 5. (d) Definitions In this section, the terms career appointee and senior executive position have the meanings given such terms in section 3132(a) of title 5. .\n**(2) Clerical amendment**\nThe table of sections at the beginning of such subchapter is amended by adding at the end the following new item:\n729. Pay for senior executive positions. .",
      "versionDate": "2025-12-16",
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
            "name": "Department of Veterans Affairs",
            "updateDate": "2026-05-11T17:04:29Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-05-11T16:54:39Z"
          },
          {
            "name": "Wages and earnings",
            "updateDate": "2026-05-11T16:54:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2026-01-08T16:57:17Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6740ih.xml"
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
      "title": "VA TRUST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA TRUST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Affairs Transparency and Reform of the Upper Senior Tenure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to modify pay rates for certain Senior Executive Service employees at the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T11:18:20Z"
    }
  ]
}
```
