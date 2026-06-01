# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6330?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6330
- Title: Federal Relocation Payment Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 6330
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2026-03-17T18:50:17Z
- Update date including text: 2026-03-17T18:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 6.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 6.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6330",
    "number": "6330",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000311",
        "district": "3",
        "firstName": "Brian",
        "fullName": "Rep. Jack, Brian [R-GA-3]",
        "lastName": "Jack",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Federal Relocation Payment Improvement Act",
    "type": "HR",
    "updateDate": "2026-03-17T18:50:17Z",
    "updateDateIncludingText": "2026-03-17T18:50:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 37 - 6.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
            "date": "2025-12-02T17:42:29Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-01T17:01:15Z",
            "name": "Referred To"
          }
        ]
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6330ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6330\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Jack introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to provide for lump-sum relocation payments for Federal employees relocated in the interest of the Government, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Federal Relocation Payment Improvement Act .\n#### 2. Lump-sum relocation payments for relocated Federal employees\n##### (a) In general\nSubchapter II of chapter 57 of title 5, United States Code, is amended by adding at the end the following:\n5739a. Authority for lump sum payment for relocation (a) In general Notwithstanding any other provision of this subchapter, when the head of the agency concerned (or a designee) authorizes or approves, an agency, through the proper disbursing official, may pay to an employee who relocates in the interest of the Government, a one-time lump sum payment in lieu of any payment otherwise authorized or required under this subchapter. (b) Regulations Under section 5738 of this title, the Administrator of General Services shall prescribe regulations necessary for the implementation and administration of this section, including\u2014 (1) when agencies may authorize a one-time lump sum payment under this section or the payments otherwise authorized or required under this subchapter; (2) how agencies will calculate the lump sum amount; and (3) the process for employees to dispute a relocation expenses claim with their agency, notice of the employee\u2019s right to appeal the agency decision to the Civilian Board of Contract Appeals, and citation to the Board\u2019s procedures governing the appeals process. .\n##### (b) Clerical amendment\nThe table of sections for such subchapter is amended by adding after the item relating to section 5739 the following:\n5739a. Authority for lump sum payment for relocation. .",
      "versionDate": "2025-12-01",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-12-05T19:47:53Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-12-05T19:47:49Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-12-05T19:47:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-02T20:33:33Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6330ih.xml"
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
      "title": "Federal Relocation Payment Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Relocation Payment Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to provide for lump-sum relocation payments for Federal employees relocated in the interest of the Government, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:24Z"
    }
  ]
}
```
