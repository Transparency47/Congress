# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/151?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/151
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to "Bulletin 2023-01: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts".
- Congress: 119
- Bill type: SJRES
- Bill number: 151
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-05-21T20:16:11Z
- Update date including text: 2026-05-21T20:16:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/151",
    "number": "151",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Bulletin 2023-01: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts\".",
    "type": "SJRES",
    "updateDate": "2026-05-21T20:16:11Z",
    "updateDateIncludingText": "2026-05-21T20:16:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T19:27:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres151is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 151\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Ms. Hirono introduced the following joint resolution; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Bulletin 2023\u201301: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts .\nThat Congress disapproves the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to Bulletin 2023\u201301: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts (88 Fed. Reg. 17366 (March 23, 2023)) (90 Fed. Reg. 20084 (May 12, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-03-26",
      "versionType": "IS"
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
        "actionDate": "2026-05-12",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "182",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Bulletin 2023-01: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts\".",
      "type": "HJRES"
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
        "updateDate": "2026-04-01T16:02:50Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres151is.xml"
        }
      ],
      "type": "IS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Bulletin 2023-01: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-31T06:18:25Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Consumer Financial Protection relating to the withdrawal of the rule relating to \"Bulletin 2023-01: Unfair Billing and Collection Practices After Bankruptcy Discharges of Certain Student Loan Debts\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T10:56:31Z"
    }
  ]
}
```
