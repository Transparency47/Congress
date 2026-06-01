# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4409
- Title: Fair Pharmacies for Federal Employees Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4409
- Origin chamber: House
- Introduced date: 2025-07-15
- Update date: 2025-09-11T15:58:42Z
- Update date including text: 2025-09-11T15:58:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-07-15: Introduced in House

## Actions

- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Introduced in House
- 2025-07-15 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4409",
    "number": "4409",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000391",
        "district": "8",
        "firstName": "Raja",
        "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
        "lastName": "Krishnamoorthi",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Fair Pharmacies for Federal Employees Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-11T15:58:42Z",
    "updateDateIncludingText": "2025-09-11T15:58:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T14:01:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "TN"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4409ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4409\nIN THE HOUSE OF REPRESENTATIVES\nJuly 15, 2025 Mr. Krishnamoorthi (for himself and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit the common ownership pharmacy benefit managers and pharmacies that provide services under contracts with Federal health plans for Federal employees.\n#### 1. Short title\nThis Act may be cited as the Fair Pharmacies for Federal Employees Act of 2025 .\n#### 2. Prohibitions relating to anticompetitive pharmacy ownership and contracts\n##### (a) Prohibition on pharmacy or pharmacy benefit manager ownership by entities providing insurance under Federal employee health plans\nIt shall be unlawful for the Office of Personnel Management to contract with a Federal employee health benefit qualified carrier who\u2014\n**(1)**\ndirectly or indirectly owns, operates, controls, or directs the operation of the whole or any part of a pharmacy; or\n**(2)**\ndirectly or indirectly owns, operates, or controls the whole or any part of a pharmacy benefit manager, or is directly or indirectly owned, operated, or has its operation directed by the whole or in any part by a pharmacy benefit manager.\n##### (b) Prohibition on pharmacy ownership by entities providing pharmacy benefit management services under Federal employee health plans\nIt shall be unlawful of the Office of Personnel Management or a Federal employee health benefit qualified carrier to contract or subcontract with a pharmacy benefit manager who directly or indirectly owns, operates, controls, or directs the operation of the whole or any part of a pharmacy.\n##### (c) Rule of construction\nNothing in this section shall be construed to limit the authority of the Federal Trade Commission, the Inspector General of the Department of Justice, the Department of Health and Human Services, or the attorney general of a State under any other provision of law.\n##### (d) Definitions\nIn this section:\n**(1) Health plan**\nThe term health plan means a group insurance policy or contract, medical or hospital service agreement, membership or subscription contract, or similar group arrangement provided by a carrier for the purpose of providing, paying for, or reimbursing expenses for health services.\n**(2) Person**\nThe term person has the meaning given the term in section 8 of the Sherman Act ( 15 U.S.C. 7 ).\n**(3) Pharmacy**\n**(A) In general**\nThe term pharmacy means any person, business, or entity licensed, registered, or otherwise permitted by a State or a territory of the United States to dispense, deliver, or distribute a controlled substance, prescription drug, or other medication\u2014\n**(i)**\nto the general public; or\n**(ii)**\nto a bed patient for immediate administration.\n**(B) Inclusions**\nThe term pharmacy includes\u2014\n**(i)**\na mail-order pharmacy;\n**(ii)**\na specialty pharmacy;\n**(iii)**\na retail pharmacy;\n**(iv)**\na nursing home pharmacy;\n**(v)**\na long-term care pharmacy;\n**(vi)**\na hospital pharmacy;\n**(vii)**\nan infusion or other outpatient treatment pharmacy;\n**(viii)**\nany organization the National Provider Identifier (NPI) registration of which has 1 or more taxonomy codes under the pharmacy section of the National Uniform Claim Committee (or a subsequent organization); and\n**(ix)**\nany other type of pharmacy.\n**(4) Pharmacy benefit manager**\nThe term pharmacy benefit manager means any person, business, or other entity, such as a third-party administrator, regardless of whether such person, business, or entity identifies itself as a pharmacy benefit manager, that, either directly or indirectly through an intermediary (including an affiliate, subsidiary, or agent) or an arrangement with a third party\u2014\n**(A)**\nacts as a negotiator of prices, rebates, fees, or discounts for prescription drugs on behalf of a health plan or health plan sponsor;\n**(B)**\ncontracts with pharmacies to create pharmacy networks and designs and manages such networks; or\n**(C)**\nmanages or administers the prescription drug benefits provided by a health plan, including the processing and payment of claims for prescription drugs, arranging alternative access to or funding for prescription drugs, the performance of utilization management services, including drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, controlling the cost of covered prescription drugs, or the provision of related services.\n**(5) Qualified carrier**\nThe term qualified carrier means a voluntary association, corporation, partnership, or other nongovernmental organization which is lawfully engaged in providing, paying for, or reimbursing the cost of, health services under group insurance policies or contracts, medical or hospital service agreements, membership or subscription contracts, or similar group arrangements, in consideration of premiums or other periodic charges payable to the carrier, including a health benefits plan duly sponsored or underwritten by an employee organization and an association of organizations or other entities described in this paragraph sponsoring a health benefits plan.",
      "versionDate": "2025-07-15",
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
        "name": "Health",
        "updateDate": "2025-09-11T15:58:42Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4409ih.xml"
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
      "title": "Fair Pharmacies for Federal Employees Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair Pharmacies for Federal Employees Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the common ownership pharmacy benefit managers and pharmacies that provide services under contracts with Federal health plans for Federal employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:24Z"
    }
  ]
}
```
