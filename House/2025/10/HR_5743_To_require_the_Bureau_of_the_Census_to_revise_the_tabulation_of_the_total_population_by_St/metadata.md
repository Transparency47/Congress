# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5743?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5743
- Title: One Citizen, One Seat Act
- Congress: 119
- Bill type: HR
- Bill number: 5743
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2026-03-10T23:41:16Z
- Update date including text: 2026-03-10T23:41:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5743",
    "number": "5743",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "One Citizen, One Seat Act",
    "type": "HR",
    "updateDate": "2026-03-10T23:41:16Z",
    "updateDateIncludingText": "2026-03-10T23:41:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:31:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5743ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5743\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Ms. Van Duyne introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Bureau of the Census to revise the tabulation of the total population by State for the 2020 decennial census counting only citizens of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the One Citizen, One Seat Act .\n#### 2. Citizen only census population tabulation\n##### (a) In general\nThe Secretary of Commerce shall revise the tabulation of total population by States for the 2020 decennial census under section 141(a) of title 13, United States Code, to include only individuals who are citizens of the United States.\n##### (b) Distribution\nNot later than 60 days after the date of the enactment of this Act, the Secretary of Commerce shall provide to each State the tabulation of total population for such State as revised under subsection (a).\n##### (c) Federal grant eligibility\nNotwithstanding any other provision of law, beginning on the date that is 60 days after the date on which the Secretary of Commerce provides to a State the tabulation of total population for such State as revised under subsection (a), no grant may be awarded by the Federal Government to such State unless such State\u2014\n**(1)**\nuses only such tabulation as so revised for all purposes for which such State would have used such tabulation prior to such revision; and\n**(2)**\ndoes not otherwise use such tabulation other than as so revised.",
      "versionDate": "2025-10-10",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-09T21:02:04Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5743ih.xml"
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
      "title": "One Citizen, One Seat Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "One Citizen, One Seat Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Bureau of the Census to revise the tabulation of the total population by State for the 2020 decennial census counting only citizens of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:10Z"
    }
  ]
}
```
