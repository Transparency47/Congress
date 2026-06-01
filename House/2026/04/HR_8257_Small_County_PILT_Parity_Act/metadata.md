# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8257?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8257
- Title: Small County PILT Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 8257
- Origin chamber: House
- Introduced date: 2026-04-14
- Update date: 2026-04-21T22:48:44Z
- Update date including text: 2026-04-21T22:48:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2026-04-14: Introduced in House

## Actions

- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Introduced in House
- 2026-04-14 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8257",
    "number": "8257",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Small County PILT Parity Act",
    "type": "HR",
    "updateDate": "2026-04-21T22:48:44Z",
    "updateDateIncludingText": "2026-04-21T22:48:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-14",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T16:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "bioguideId": "Z000018",
      "district": "1",
      "firstName": "Ryan",
      "fullName": "Rep. Zinke, Ryan K. [R-MT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Zinke",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "MT"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8257ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8257\nIN THE HOUSE OF REPRESENTATIVES\nApril 14, 2026 Mr. Hurd of Colorado (for himself, Mr. Zinke , and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend section 6903 of title 31, United States Code, to provide for additional population tiers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Small County PILT Parity Act .\n#### 2. Adjustment for low-population units of general local government\nSection 6903(c) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), by striking 4,999 and inserting 499 ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the matter preceding the table\u2014\n**(i)**\nby striking 5,000 and inserting 500 ; and\n**(ii)**\nby striking (rounding and inserting (except for the first population value, rounding ; and\n**(B)**\nby striking the table and inserting the following:\nIf population equals\u2014 the limitation is equal to the population times\u2014 500 $514.50 1,000 $404.56 2,000 $320.75 3,000 $289.14 4,000 $262.84 5,000 $231.25 6,000 $216.56 7,000 $203.90 8,000 $189.24 9,000 $176.57 10,000 $161.82 11,000 $157.69 12,000 $153.48 13,000 $147.18 14,000 $142.98 15,000 $138.73 16,000 $136.64 17,000 $134.51 18,000 $132.44 19,000 $130.35 20,000 $128.30 21,000 $126.14 22,000 $124.04 23,000 $124.04 24,000 $121.95 25,000 $119.85 26,000 $117.73 27,000 $117.73 28,000 $117.73 29,000 $115.65 30,000 $115.65 31,000 $113.53 32,000 $113.53 33,000 $111.40 34,000 $111.40 35,000 $109.28 36,000 $109.28 37,000 $107.20 38,000 $107.20 39,000 $105.13 40,000 $105.13 41,000 $102.99 42,000 $100.93 43,000 $100.93 44,000 $98.78 45,000 $98.78 46,000 $96.72 47,000 $96.72 48,000 $94.61 49,000 $94.61 50,000 $92.50. .",
      "versionDate": "2026-04-14",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-12-02",
        "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held."
      },
      "number": "1175",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Small County PILT Parity Act",
      "type": "S"
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
        "updateDate": "2026-04-21T21:57:41Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8257ih.xml"
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
      "title": "Small County PILT Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T08:23:37Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small County PILT Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T08:23:35Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend section 6903 of title 31, United States Code, to provide for additional population tiers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T08:18:44Z"
    }
  ]
}
```
