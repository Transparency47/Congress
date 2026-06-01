# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3498?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3498
- Title: EQIP Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3498
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-02-26T12:03:17Z
- Update date including text: 2026-02-26T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3498",
    "number": "3498",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "EQIP Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-02-26T12:03:17Z",
    "updateDateIncludingText": "2026-02-26T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
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
        "item": [
          {
            "date": "2025-12-16T20:30:14Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-16T20:30:14Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "UT"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3498is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3498\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Booker (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Food Security Act of 1985 to make adjustments to the environmental quality incentives program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the EQIP Improvement Act of 2025 .\n#### 2. Environmental Quality Incentives Program reforms\n##### (a) In general\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended\u2014\n**(1)**\nin subsection (d), by striking paragraph (2) and inserting the following:\n(2) Limitation on payments A payment to a producer for performing a practice may not exceed, as determined by the Secretary\u2014 (A) except as provided in subparagraphs (B) through (D), 75 percent of the costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training; (B) 40 percent of the costs associated with planning, design, materials, equipment, installation, labor, management, maintenance, or training for\u2014 (i) an access road; (ii) an animal mortality facility; (iii) an aquaculture pond; (iv) clearing and snagging; (v) a dam; (vi) a dam using a diversion; (vii) a dike; (viii) a diversion; (ix) a fish raceway or tank; (x) an irrigation pipeline; (xi) an irrigation reservoir; (xii) land clearing; (xiii) land smoothing; (xiv) a livestock pipeline; (xv) obstruction removal; (xvi) a pond; (xvii) a pumping plant; (xviii) spoil spreading; (xix) a surface drain using a field ditch; (xx) a main or lateral surface drain; (xxi) a vertical drain; (xxii) a waste facility closure; (xxiii) a waste storage facility; (xxiv) waste transfer; or (xxv) a waste treatment lagoon; (C) 100 percent of income foregone by the producer; or (D) in the case of a practice that includes 1 or more elements described in subparagraphs (A) through (C)\u2014 (i) 75 percent of the costs incurred with respect to any elements described in subparagraph (A); (ii) 40 percent of the costs incurred with respect to any elements described in subparagraph (B); and (iii) 100 percent of the income forgone with respect to any elements described in subparagraph (C). ; and\n**(2)**\nin subsection (f), by striking the subsection designation and heading and all that follows through For each in paragraph (2)(B) and inserting the following:\n(f) Allocation of funding for wildlife habitat For each .\n##### (b) Limitation on payments\nSection 1240G of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20137 ) is amended by striking $450,000 and inserting $150,000 .\n##### (c) Report to Congress\nSection 1240B of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u20132 ) is amended by adding at the end the following:\n(k) Annual report to Congress Not less frequently than once each year, the Secretary shall submit to Congress a report describing\u2014 (1) the amount obligated under the program with respect to each category of practice, with information categorized by fiscal year and State; and (2) the amount obligated under the program in each State, with information categorized by fiscal year and the size of the operation of each producer. .",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-06-25",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4133",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "EQIP Improvement Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-09T16:13:21Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3498is.xml"
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
      "title": "EQIP Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-26T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EQIP Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Food Security Act of 1985 to make adjustments to the environmental quality incentives program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:22Z"
    }
  ]
}
```
