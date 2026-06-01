# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4203
- Title: WEAR IT Act
- Congress: 119
- Bill type: HR
- Bill number: 4203
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-01-31T03:36:14Z
- Update date including text: 2026-01-31T03:36:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4203",
    "number": "4203",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001183",
        "district": "1",
        "firstName": "David",
        "fullName": "Rep. Schweikert, David [R-AZ-1]",
        "lastName": "Schweikert",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "WEAR IT Act",
    "type": "HR",
    "updateDate": "2026-01-31T03:36:14Z",
    "updateDateIncludingText": "2026-01-31T03:36:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4203ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4203\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Mr. Schweikert (for himself and Mr. Bera ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow certain wearable devices to be purchased using health savings accounts and other spending arrangements and reimbursement accounts.\n#### 1. Short title\nThis Act may be cited as the Wearable Equipment Adoption and Reinforcement and Investment in Technology Act or the WEAR IT Act .\n#### 2. Inclusion of certain wearable devices as qualified medical expenses\n##### (a) HSAs\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the last sentence of subparagraph (A), by striking the period at the end and inserting the following: , and amounts paid for wearable devices shall be treated as paid for medical care to the extent such amounts do not exceed $375 for the taxable year. , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Wearable device For purposes of this paragraph, the term wearable device means a device or software (including subscriptions) that\u2014 (i) is worn on the body or is used primarily in connection with a device that is worn on the body, and (ii) either\u2014 (I) collects and analyzes physiological data for the diagnosis, cure, mitigation, treatment, or prevention of a disease, impairment, or health condition, or (II) assists the rendering of a diagnosis or provides a treatment, mitigation, or cure for any disease, impairment, or health condition. .\n##### (b) Archer MSAs\nSection 220(d)(2)(A) of such Code is amended by striking the period at the end and inserting the following: , and amounts paid for wearable devices (as defined in section 223(d)(2)(E)) shall be treated as paid for medical care to the extent such amounts do not exceed $375 for the taxable year.\n##### (c) Health flexible spending arrangements and health reimbursement arrangements\nSection 106 of such Code is amended by adding at the end the following new subsection:\n(h) Reimbursements for wearable devices For purposes of this section and section 105, expenses incurred for wearable devices (as defined in section 223(d)(2)(E)) shall be treated as incurred for medical care to the extent such amounts do not exceed $375 for the taxable year. .\n##### (d) Effective dates\n**(1) Distributions from savings accounts**\nThe amendments made by subsections (a) and (b) shall apply to amounts paid after December 31, 2025.\n**(2) Reimbursements**\nThe amendment made by subsection (c) shall apply to expenses incurred after December 31, 2025.",
      "versionDate": "2025-06-26",
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
        "name": "Taxation",
        "updateDate": "2025-07-17T19:06:58Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4203ih.xml"
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
      "title": "WEAR IT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "WEAR IT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wearable Equipment Adoption and Reinforcement and Investment in Technology Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow certain wearable devices to be purchased using health savings accounts and other spending arrangements and reimbursement accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:53Z"
    }
  ]
}
```
