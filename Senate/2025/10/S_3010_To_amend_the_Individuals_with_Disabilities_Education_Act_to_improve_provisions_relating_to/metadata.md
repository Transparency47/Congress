# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3010
- Title: 21st Century Dyslexia Act
- Congress: 119
- Bill type: S
- Bill number: 3010
- Origin chamber: Senate
- Introduced date: 2025-10-15
- Update date: 2026-01-10T07:13:30Z
- Update date including text: 2026-01-10T07:13:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-15: Introduced in Senate
- 2025-10-15 - IntroReferral: Introduced in Senate
- 2025-10-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-15: Introduced in Senate

## Actions

- 2025-10-15 - IntroReferral: Introduced in Senate
- 2025-10-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-15",
    "latestAction": {
      "actionDate": "2025-10-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3010",
    "number": "3010",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
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
    "title": "21st Century Dyslexia Act",
    "type": "S",
    "updateDate": "2026-01-10T07:13:30Z",
    "updateDateIncludingText": "2026-01-10T07:13:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-15",
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
      "actionDate": "2025-10-15",
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
          "date": "2025-10-15T16:38:33Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-15",
      "state": "CO"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-10-15",
      "state": "RI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "AK"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NJ"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-12-04",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3010is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3010\nIN THE SENATE OF THE UNITED STATES\nOctober 15, 2025 Mr. Cassidy (for himself, Mr. Hickenlooper , and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Individuals with Disabilities Education Act to improve provisions relating to dyslexia, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 21st Century Dyslexia Act .\n#### 2. Dyslexia\n##### (a) Definitions\nSection 602 of the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 ) is amended\u2014\n**(1)**\nin paragraph (3)(A), by striking or specific learning disabilities and inserting specific learning disabilities, or dyslexia ;\n**(2)**\nby inserting after paragraph (3) the following:\n(4) Dyslexia The term dyslexia means an unexpected difficulty in reading for an individual who has the intelligence to be a much better reader, most commonly caused by a difficulty in the phonological processing (the appreciation of the individual sounds of spoken language), which affects the ability of an individual to speak, read, and spell. ; and\n**(3)**\nin paragraph (30)\u2014\n**(A)**\nin subparagraph (B), by striking dyslexia, ; and\n**(B)**\nin subparagraph (C), by striking or of environmental and all that follows and inserting or dyslexia .\n##### (b) Provision of accommodations and services\nThe Individuals with Disabilities Education Act is amended by inserting after section 608 ( 20 U.S.C. 1407 ) the following:\n608A. Provision of accommodations and services In determining eligibility for, or providing, an accommodation or service under this title, a local educational agency or other agency shall provide equal access, to the accommodation or service, to all eligible children, including eligible children who are\u2014 (1) children from low-income families; (2) children from families with low socioeconomic status; and (3) children who are limited English proficient. .",
      "versionDate": "2025-10-15",
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
        "actionDate": "2025-10-17",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "5769",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "21st Century Dyslexia Act",
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
        "name": "Education",
        "updateDate": "2025-12-08T14:56:25Z"
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
      "date": "2025-10-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3010is.xml"
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
      "title": "21st Century Dyslexia Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T12:03:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "21st Century Dyslexia Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Individuals with Disabilities Education Act to improve provisions relating to dyslexia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:26Z"
    }
  ]
}
```
