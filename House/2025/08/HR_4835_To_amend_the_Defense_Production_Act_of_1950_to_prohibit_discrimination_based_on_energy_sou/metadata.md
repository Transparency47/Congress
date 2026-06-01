# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4835?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4835
- Title: Strategic Resources Non-discrimination Act
- Congress: 119
- Bill type: HR
- Bill number: 4835
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-01-14T16:23:24Z
- Update date including text: 2026-01-14T16:23:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-08-01: Introduced in House

## Actions

- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Financial Services.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4835",
    "number": "4835",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Strategic Resources Non-discrimination Act",
    "type": "HR",
    "updateDate": "2026-01-14T16:23:24Z",
    "updateDateIncludingText": "2026-01-14T16:23:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4835ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4835\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Defense Production Act of 1950 to prohibit discrimination based on energy source in the use of certain authorities under title I and title III of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strategic Resources Non-discrimination Act .\n#### 2. Limitations on certain authorities under the Defense Production Act of 1950\n##### (a) Domestic energy supplies\nSection 101(c)(1) of the Defense Production Act of 1950 ( 50 U.S.C. 4511(c)(1) ) is amended by inserting , other than for purposes of environmental protection, after domestic energy supplies .\n##### (b) Prohibition on discrimination based on industry\nTitle III of the Defense Production Act of 1950 ( 50 U.S.C. 4531 et seq. ) is amended by adding at the end the following:\n306. Prohibition on discrimination based on energy source In using the authorities under this title, the President may not deny financial support pursuant to sections 301, 302, or 303, other than for the production of energy, based on engagement by a person in the exploration, development, production, utilization, transportation, or sale of fossil fuel-based energy. .",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-12-17",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "3530",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Strategic Resources Non-discrimination Act",
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
        "name": "Energy",
        "updateDate": "2025-09-18T16:59:44Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4835ih.xml"
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
      "title": "Strategic Resources Non-discrimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strategic Resources Non-discrimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Defense Production Act of 1950 to prohibit discrimination based on energy source in the use of certain authorities under title I and title III of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:33:24Z"
    }
  ]
}
```
