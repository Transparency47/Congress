# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3418?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3418
- Title: COMPETE Act
- Congress: 119
- Bill type: S
- Bill number: 3418
- Origin chamber: Senate
- Introduced date: 2025-12-10
- Update date: 2026-04-14T13:37:35Z
- Update date including text: 2026-04-14T13:37:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in Senate
- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-12-10: Introduced in Senate

## Actions

- 2025-12-10 - IntroReferral: Introduced in Senate
- 2025-12-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3418",
    "number": "3418",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "COMPETE Act",
    "type": "S",
    "updateDate": "2026-04-14T13:37:35Z",
    "updateDateIncludingText": "2026-04-14T13:37:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T19:17:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3418is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3418\nIN THE SENATE OF THE UNITED STATES\nDecember 10, 2025 Mr. Cruz (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure competition in health insurance markets.\n#### 1. Short title\nThis Act may be cited as the Competition and Openness in Markets to Promote Efficiency, Transparency, and Enhanced affordability Act or the COMPETE Act .\n#### 2. Short-term limited duration insurance\nSection 2791(b) of the Public Health Service Act ( 42 U.S.C. 300gg\u201391(b) ) is amended by adding at the end the following:\n(6) Short-term limited duration insurance The term short-term limited duration insurance means a plan providing health insurance coverage pursuant to a contract with a health insurance issuer\u2014 (A) that has an expiration date specified in the contract that is not more than 12 months after the original effective date of the contract; and (B) which may include a renewal guarantee that permits a policyholder to elect to purchase, for periods of time following expiration of the initial contract, another policy or policies at some future date, at a premium that would not reflect any additional underwriting. .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-03-25",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "8082",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COMPETE Act",
      "type": "HR"
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
        "updateDate": "2026-01-08T17:22:56Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3418is.xml"
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
      "title": "COMPETE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-06T06:39:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COMPETE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Competition and Openness in Markets to Promote Efficiency, Transparency, and Enhanced affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-06T06:39:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure competition in health insurance markets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-06T06:33:34Z"
    }
  ]
}
```
