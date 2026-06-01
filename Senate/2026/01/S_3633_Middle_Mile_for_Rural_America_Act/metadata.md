# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3633
- Title: Middle Mile for Rural America Act
- Congress: 119
- Bill type: S
- Bill number: 3633
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-02-04T15:28:33Z
- Update date including text: 2026-02-04T15:28:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3633",
    "number": "3633",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Middle Mile for Rural America Act",
    "type": "S",
    "updateDate": "2026-02-04T15:28:33Z",
    "updateDateIncludingText": "2026-02-04T15:28:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T17:28:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3633is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3633\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mrs. Hyde-Smith (for herself and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Rural Electrification Act of 1936 to reauthorize the expansion of middle mile infrastructure into rural areas.\n#### 1. Short title\nThis Act may be cited as the Middle Mile for Rural America Act .\n#### 2. Expansion of middle mile infrastructure into rural areas\nSection 602(g) of the Rural Electrification Act of 1936 ( 7 U.S.C. 950bb\u20131(g) ) is amended by striking 2018 through 2023 and inserting 2026 through 2031 .",
      "versionDate": "2026-01-14",
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
        "actionDate": "2025-08-26",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5037",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Middle Mile for Rural America Act",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-04T15:28:33Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3633is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Rural Electrification Act of 1936 to reauthorize the expansion of middle mile infrastructure into rural areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-03T11:03:40Z"
    },
    {
      "title": "Middle Mile for Rural America Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T10:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Middle Mile for Rural America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-03T10:53:15Z"
    }
  ]
}
```
