# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2653?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2653
- Title: RECHARGE Act
- Congress: 119
- Bill type: S
- Bill number: 2653
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-09-18T20:12:51Z
- Update date including text: 2025-09-18T20:12:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2653",
    "number": "2653",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "RECHARGE Act",
    "type": "S",
    "updateDate": "2025-09-18T20:12:51Z",
    "updateDateIncludingText": "2025-09-18T20:12:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-08-01T20:03:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2653is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2653\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Merkley introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo amend title 23, United States Code, to permit the use of certain electric vehicle charging stations at rest areas on the Interstate System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Recharge your Electric Car on the Highway to Alleviate Range Gaps Effectively Act or the RECHARGE Act .\n#### 2. Use of and access to rest areas on the Interstate System for electric vehicle charging stations\n##### (a) In general\nSection 111 of title 23, United States Code, is amended by adding at the end the following:\n(f) Electric vehicle charging stations (1) In general Notwithstanding subsections (a) and (b), the Secretary shall permit, consistent with section 109(s), electric vehicle charging infrastructure for passenger automobiles (as defined in section 32901(a) of title 49) at rest areas on the Interstate System. (2) Savings clause Nothing in this subsection permits commercial activities on rights-of-way on the Interstate System except as necessary for the charging of electric vehicles in accordance with this subsection. .\n##### (b) Conforming amendments\n**(1) Congestion mitigation and air quality improvement program**\nSection 149(c)(2) of title 23, United States Code, is amended\u2014\n**(A)**\nby striking such stations and inserting such natural gas vehicle refueling stations ; and\n**(B)**\nby striking of title 23, United States Code .\n**(2) Jason's Law**\nSection 1401(d)(2) of the Moving Ahead for Progress in the 21st Century Act ( 23 U.S.C. 137 note; Public Law 112\u2013141 ) is amended by striking Electric vehicle battery charging stations or natural and inserting Natural .\n##### (c) Congressional intent\nNothing in this Act or an amendment made by this Act is intended as a statement of congressional intent with respect to the existing authority of the President or any other Federal agency under section 111 of title 23, United States Code.",
      "versionDate": "2025-08-01",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-18T20:12:51Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2653is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "RECHARGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RECHARGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Recharge your Electric Car on the Highway to Alleviate Range Gaps Effectively Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 23, United States Code, to permit the use of certain electric vehicle charging stations at rest areas on the Interstate System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:18:23Z"
    }
  ]
}
```
