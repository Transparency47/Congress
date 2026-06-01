# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1015?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1015
- Title: A bill to extend the National Flood Insurance Program through December 31, 2026.
- Congress: 119
- Bill type: S
- Bill number: 1015
- Origin chamber: Senate
- Introduced date: 2025-03-13
- Update date: 2026-02-05T17:34:08Z
- Update date including text: 2026-02-05T17:34:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-13: Introduced in Senate
- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1745)
- Latest action: 2025-03-13: Introduced in Senate

## Actions

- 2025-03-13 - IntroReferral: Introduced in Senate
- 2025-03-13 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1745)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-13",
    "latestAction": {
      "actionDate": "2025-03-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1015",
    "number": "1015",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "A bill to extend the National Flood Insurance Program through December 31, 2026.",
    "type": "S",
    "updateDate": "2026-02-05T17:34:08Z",
    "updateDateIncludingText": "2026-02-05T17:34:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-13",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (Sponsor introductory remarks on measure: CR S1745)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-13",
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
          "date": "2025-03-13T15:05:29Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "LA"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1015is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1015\nIN THE SENATE OF THE UNITED STATES\nMarch 13, 2025 Mr. Cassidy (for himself and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo extend the National Flood Insurance Program through December 31, 2026.\n#### 1. Extension of National Flood Insurance Program\n##### (a) Financing\nSection 1309(a) of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4016(a) ) is amended, in the first sentence, by striking September 30, 2023 and inserting December 31, 2026 .\n##### (b) Program expiration\nSection 1319 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4026 ) is amended by striking September 30, 2023 and inserting December 31, 2026 .",
      "versionDate": "2025-03-13",
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
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-10",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "2822",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To extend the National Flood Insurance Program through December 31, 2026.",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-31T13:45:19Z"
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
      "date": "2025-03-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1015is.xml"
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
      "title": "A bill to extend the National Flood Insurance Program through December 31, 2026.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T11:18:20Z"
    },
    {
      "title": "A bill to extend the National Flood Insurance Program through December 31, 2026.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T10:56:33Z"
    }
  ]
}
```
