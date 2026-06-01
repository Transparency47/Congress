# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1903?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1903
- Title: A bill to prohibit changes to Medicare and Medicaid in reconciliation.
- Congress: 119
- Bill type: S
- Bill number: 1903
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-06-13T17:55:19Z
- Update date including text: 2025-06-13T17:55:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Budget. (Sponsor introductory remarks on measure: CR S3119)
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on the Budget. (Sponsor introductory remarks on measure: CR S3119)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1903",
    "number": "1903",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000122",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Reed, Jack [D-RI]",
        "lastName": "Reed",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "A bill to prohibit changes to Medicare and Medicaid in reconciliation.",
    "type": "S",
    "updateDate": "2025-06-13T17:55:19Z",
    "updateDateIncludingText": "2025-06-13T17:55:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "ssbu00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Budget. (Sponsor introductory remarks on measure: CR S3119)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T19:22:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Budget Committee",
      "systemCode": "ssbu00",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1903is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1903\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Reed (for himself, Mr. Heinrich , and Mr. Markey ) introduced the following bill; which was read twice and referred to the Committee on the Budget\nA BILL\nTo prohibit changes to Medicare and Medicaid in reconciliation.\n#### 1. Prohibition on changes to Medicare and Medicaid in reconciliation\nSection 310(g) of the Congressional Budget Act of 1974 ( 2 U.S.C. 641(g) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking the Social Security Act and inserting Social Security, Medicare, and Medicaid ;\n**(2)**\nby striking recommendations with respect to the old-age and inserting the following: \u201crecommendations with respect to\u2014\n(1) the old-age ;\n**(3)**\nby striking the period at the end and inserting a semicolon; and\n**(4)**\nby adding at the end the following:\n(2) the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ); or (3) the Medicaid program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ). .",
      "versionDate": "2025-05-22",
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
        "name": "Health",
        "updateDate": "2025-06-13T17:55:19Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1903is.xml"
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
      "title": "A bill to prohibit changes to Medicare and Medicaid in reconciliation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:43Z"
    },
    {
      "title": "A bill to prohibit changes to Medicare and Medicaid in reconciliation.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-23T10:56:15Z"
    }
  ]
}
```
