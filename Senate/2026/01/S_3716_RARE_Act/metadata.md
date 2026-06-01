# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3716?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3716
- Title: RARE Act
- Congress: 119
- Bill type: S
- Bill number: 3716
- Origin chamber: Senate
- Introduced date: 2026-01-28
- Update date: 2026-02-25T16:24:40Z
- Update date including text: 2026-02-25T16:24:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-28: Introduced in Senate
- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-28: Introduced in Senate

## Actions

- 2026-01-28 - IntroReferral: Introduced in Senate
- 2026-01-28 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-28",
    "latestAction": {
      "actionDate": "2026-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3716",
    "number": "3716",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001230",
        "district": "",
        "firstName": "Tammy",
        "fullName": "Sen. Baldwin, Tammy [D-WI]",
        "lastName": "Baldwin",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "RARE Act",
    "type": "S",
    "updateDate": "2026-02-25T16:24:40Z",
    "updateDateIncludingText": "2026-02-25T16:24:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-28",
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
      "actionDate": "2026-01-28",
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
          "date": "2026-01-28T20:44:38Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3716is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3716\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2026 Ms. Baldwin introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo set forth limitations on exclusive approval or licensure of drugs designated for rare diseases or conditions.\n#### 1. Short title\nThis Act may be cited as the Retaining Access and Restoring Exclusivity Act or the RARE Act .\n#### 2. Limitations on exclusive approval or licensure of orphan drugs\n##### (a) In general\nSection 527 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360cc ) is amended\u2014\n**(1)**\nin subsection (a), in the matter following paragraph (2), by striking same disease or condition and inserting same approved use or indication within such rare disease or condition ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking same rare disease or condition and inserting same approved use or indication for which such 7-year period applies to such already approved or licensed drug ; and\n**(B)**\nin paragraph (1), by inserting , relating to the approved use or indication, after the needs ;\n**(3)**\nin subsection (c)(1), by striking same rare disease or condition as the already approved drug and inserting same use or indication for which the already approved or licensed drug was approved or licensed ; and\n**(4)**\nby adding at the end the following:\n(f) Approved use or indication defined In this section, the term approved use or indication means the use or indication approved under section 505 of this Act or licensed under section 351 of the Public Health Service Act for a drug designated under section 526 for a rare disease or condition. .\n##### (b) Application of amendments\nThe amendments made by subsection (a) shall apply with respect to any drug designated under section 526 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 360bb ), regardless of the date on which the drug was so designated, and regardless of the date on which the drug was approved under section 505 of such Act ( 21 U.S.C. 355 ) or licensed under section 351 of the Public Health Service Act ( 42 U.S.C. 262 ).",
      "versionDate": "2026-01-28",
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
        "actionDate": "2025-12-02",
        "text": "Received in the Senate."
      },
      "number": "1262",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mikaela Naylon Give Kids a Chance Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
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
        "name": "Health",
        "updateDate": "2026-02-25T16:24:40Z"
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
      "date": "2026-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3716is.xml"
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
      "title": "RARE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RARE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Retaining Access and Restoring Exclusivity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to set forth limitations on exclusive approval or licensure of drugs designated for rare diseases or conditions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:27Z"
    }
  ]
}
```
