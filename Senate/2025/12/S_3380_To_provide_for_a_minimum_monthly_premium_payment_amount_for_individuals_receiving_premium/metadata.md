# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3380?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3380
- Title: ACA Marketplace Integrity Act
- Congress: 119
- Bill type: S
- Bill number: 3380
- Origin chamber: Senate
- Introduced date: 2025-12-04
- Update date: 2025-12-11T15:29:48Z
- Update date including text: 2025-12-11T15:29:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in Senate
- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-04: Introduced in Senate

## Actions

- 2025-12-04 - IntroReferral: Introduced in Senate
- 2025-12-04 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3380",
    "number": "3380",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001198",
        "district": "",
        "firstName": "Roger",
        "fullName": "Sen. Marshall, Roger [R-KS]",
        "lastName": "Marshall",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "ACA Marketplace Integrity Act",
    "type": "S",
    "updateDate": "2025-12-11T15:29:48Z",
    "updateDateIncludingText": "2025-12-11T15:29:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T20:44:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-12-08",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3380is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3380\nIN THE SENATE OF THE UNITED STATES\nDecember 4, 2025 Mr. Marshall introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for a minimum monthly premium payment amount for individuals receiving premium tax credits, and to require additional enrollment verification procedures prior to enrollment in qualified health plans.\n#### 1. Short title\nThis Act may be cited as the ACA Marketplace Integrity Act .\n#### 2. Minimum monthly premium payments\nSection 36B(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Limitation The premium assistance amount with respect to any coverage month shall not exceed the excess (if any) of the amount determined under paragraph (2)(A) over $5. .\n#### 3. QHP enrollment verification\nSection 1411(b)(1) of Patient Protection and Affordable Care Act ( 42 U.S.C. 18081(b)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A), by striking ; and and inserting a semicolon;\n**(2)**\nby redesignating subparagraph (B) as subparagraph (C); and\n**(3)**\nby inserting after subparagraph (A) the following:\n(B) government-issued photo identification for each enrollee over the age of 18, and any other documentation as the Administrator of the Centers for Medicare & Medicaid Services may require for purposes of enrollment verification; and .\n#### 4. Marketplace integrity and affordability\nThe final rule entitled Patient Protection and Affordable Care Act; Marketplace Integrity and Affordability (90 Fed. Reg. 27074 (June 25, 2025)) is enacted into law.",
      "versionDate": "2025-12-04",
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
        "updateDate": "2025-12-11T15:29:47Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3380is.xml"
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
      "title": "ACA Marketplace Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T15:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ACA Marketplace Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-10T15:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for a minimum monthly premium payment amount for individuals receiving premium tax credits, and to require additional enrollment verification procedures prior to enrollment in qualified health plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-10T15:18:27Z"
    }
  ]
}
```
