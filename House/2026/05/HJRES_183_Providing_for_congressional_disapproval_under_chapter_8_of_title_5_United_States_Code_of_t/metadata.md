# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hjres/183?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-joint-resolution/183
- Title: Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to "Consumer Financial Protection Circular 2023-01: Unlawful Negative Option Marketing Practices".
- Congress: 119
- Bill type: HJRES
- Bill number: 183
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T20:37:38Z
- Update date including text: 2026-05-21T20:37:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-joint-resolution/183",
    "number": "183",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001326",
        "district": "5",
        "firstName": "Janelle",
        "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
        "lastName": "Bynum",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Consumer Financial Protection Circular 2023-01: Unlawful Negative Option Marketing Practices\".",
    "type": "HJRES",
    "updateDate": "2026-05-21T20:37:38Z",
    "updateDateIncludingText": "2026-05-21T20:37:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T16:03:15Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres183ih.xml",
      "text": "IA\n119th CONGRESS\n2d Session\nH. J. RES. 183\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Ms. Bynum submitted the following joint resolution; which was referred to the Committee on Financial Services\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Consumer Financial Protection Circular 2023\u201301: Unlawful Negative Option Marketing Practices .\nThat Congress disapproves the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Consumer Financial Protection Circular 2023\u201301: Unlawful Negative Option Marketing Practices (88 Fed. Reg. 5727 (January 30, 2023)) (90 Fed. Reg. 20086 (May 12, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-05-12",
      "versionType": "IH"
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
        "actionDate": "2026-04-13",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "160",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Consumer Financial Protection Circular 2023-01: Unlawful Negative Option Marketing Practices\".",
      "type": "SJRES"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-21T20:37:38Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hjres/BILLS-119hjres183ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Consumer Financial Protection Circular 2023-01: Unlawful Negative Option Marketing Practices\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T02:48:32Z"
    },
    {
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Consumer Financial Protection Circular 2023-01: Unlawful Negative Option Marketing Practices\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T08:06:03Z"
    }
  ]
}
```
