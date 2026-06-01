# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6653
- Title: Dye Free Procurement Act
- Congress: 119
- Bill type: HR
- Bill number: 6653
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-01-16T19:00:24Z
- Update date including text: 2026-01-16T19:00:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6653",
    "number": "6653",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
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
    "title": "Dye Free Procurement Act",
    "type": "HR",
    "updateDate": "2026-01-16T19:00:24Z",
    "updateDateIncludingText": "2026-01-16T19:00:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:02:10Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6653ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6653\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Lawler introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the Federal procurement of food that contain certain color additives and prioritize the procurement of products not containing any color additives.\n#### 1. Short title\nThis Act may be cited as the Dye Free Procurement Act .\n#### 2. Prohibition on Federal procurement of food containing certain color additives; prioritization of food not containing any color additive\n##### (a) Prohibition\nThe head of an executive agency may not renew or enter into a contract for the procurement of food that contains a covered color additive.\n##### (b) Priority procurement of food that contains a color additive\nThe head of an executive agency shall prioritize the procurement of food, where available and practicable, that does not contain any color additives.\n##### (c) Definitions\nIn this section:\n**(1) Color additive**\nThe term color additive has the meaning given such term in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 ).\n**(2) Covered color additive**\nThe term covered color additive means each of the following color additives:\n**(A)**\nRed No. 40.\n**(B)**\nYellow No. 5.\n**(C)**\nYellow No. 6.\n**(D)**\nGreen No. 3.\n**(E)**\nBlue No.1.\n**(F)**\nBlue No.2.\n**(G)**\nCitrus Red No.2.\n**(H)**\nOrange B.\n**(3) Executive agency**\nThe term executive agency has the meaning given the term in section 133 of title 41, United States Code.\n**(4) Food**\nThe term food has the meaning given such term in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 301 ).\n##### (d) Applicability\nThis section shall take effect 6 months after the date of the enactment of this Act and shall apply with respect to any contract entered into on and after such effective date.",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-16T19:00:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6653ih.xml"
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
      "title": "Dye Free Procurement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Dye Free Procurement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T05:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the Federal procurement of food that contain certain color additives and prioritize the procurement of products not containing any color additives.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:33:25Z"
    }
  ]
}
```
