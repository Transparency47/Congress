# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2288
- Title: Joint Chiefs Reauthorization Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2288
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-01-10T06:56:11Z
- Update date including text: 2026-01-10T06:56:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2288",
    "number": "2288",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Joint Chiefs Reauthorization Act of 2025",
    "type": "S",
    "updateDate": "2026-01-10T06:56:11Z",
    "updateDateIncludingText": "2026-01-10T06:56:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-15",
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
      "actionDate": "2025-07-15",
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
          "date": "2025-07-15T19:53:07Z",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2288is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2288\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Bennet (for himself and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo reauthorize the Joint Chiefs Landscape Restoration Partnership program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Joint Chiefs Reauthorization Act of 2025 .\n#### 2. Joint Chiefs Landscape Restoration Partnership program\nSection 40808 of the Infrastructure Investment and Jobs Act ( 16 U.S.C. 6592d ) is amended\u2014\n**(1)**\nin subsection (a)(2)\u2014\n**(A)**\nin subparagraph (B), by striking or at the end;\n**(B)**\nin subparagraph (C), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(D) to recover from wildfires; or (E) to enhance soil, water, and related natural resources. ;\n**(2)**\nin subsection (b), by adding at the end the following:\n(3) Agency coordination In carrying out the Program, the Chief of the Natural Resources Conservation Service shall\u2014 (A) consider corresponding management plans from the Chief of the Forest Service; and (B) collaborate with the Chief of the Forest Service regarding forestry science and practice, using the best available science. ;\n**(3)**\nin subsection (d)(1)\u2014\n**(A)**\nin subparagraph (A), by inserting and post-wildfire impacts after wildfire risk ; and\n**(B)**\nin subparagraph (F), by inserting , as identified in the corresponding State forest action plan or a similar priority plan (such as a State wildlife or water plan) before the semicolon at the end;\n**(4)**\nin subsection (f), by striking paragraph (2) and inserting the following:\n(2) inconsistently with the prohibitions under the rule of the Forest Service entitled Special Areas; Roadless Area Conservation (66 Fed. Reg. 3244 (January 12, 2001)), and subparts C and D of part 294 of title 36, Code of Federal Regulations, as applicable; ; and\n**(5)**\nin subsections (g)(2) and (h)(1), by striking and 2023 each place it appears and inserting through 2029 .",
      "versionDate": "2025-07-15",
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
        "actionDate": "2025-07-15",
        "text": "Referred to the Committee on Agriculture, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "4412",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Joint Chiefs Reauthorization Act of 2025",
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-09-18T16:02:37Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2288is.xml"
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
      "title": "Joint Chiefs Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Joint Chiefs Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reauthorize the Joint Chiefs Landscape Restoration Partnership program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T06:33:25Z"
    }
  ]
}
```
