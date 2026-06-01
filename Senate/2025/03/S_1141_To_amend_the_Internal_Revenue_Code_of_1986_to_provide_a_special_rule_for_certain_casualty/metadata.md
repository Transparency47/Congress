# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1141?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1141
- Title: Disaster Reforestation Act
- Congress: 119
- Bill type: S
- Bill number: 1141
- Origin chamber: Senate
- Introduced date: 2025-03-26
- Update date: 2026-02-11T12:03:24Z
- Update date including text: 2026-02-11T12:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-26: Introduced in Senate
- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-26: Introduced in Senate

## Actions

- 2025-03-26 - IntroReferral: Introduced in Senate
- 2025-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-26",
    "latestAction": {
      "actionDate": "2025-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1141",
    "number": "1141",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Disaster Reforestation Act",
    "type": "S",
    "updateDate": "2026-02-11T12:03:24Z",
    "updateDateIncludingText": "2026-02-11T12:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-26",
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
      "actionDate": "2025-03-26",
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
            "date": "2025-03-26T16:03:41Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-26T16:03:41Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "GA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-26",
      "state": "ME"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "AL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "ME"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "MS"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1141is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1141\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2025 Mr. Cassidy (for himself, Mr. Warnock , Mr. Tuberville , Mr. King , and Mrs. Britt ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a special rule for certain casualty losses of uncut timber.\n#### 1. Short title\nThis Act may be cited as the Disaster Reforestation Act .\n#### 2. Casualty losses of uncut timber\n##### (a) In general\nSection 165(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking For purposes of subsection (a) and inserting the following:\n(1) In general For purposes of subsection (a) , and\n**(2)**\nby adding at the end the following new paragraph:\n(2) Special rule for casualty loss of uncut timber (A) In general In the case of the loss of any uncut timber from fire, storm, or other casualty, or from theft, the basis for determining the amount of the deduction for such loss (as otherwise determined under paragraph (1)) shall not be less than the excess of\u2014 (i) the appraised value of such uncut timber determined immediately before such loss was sustained, over (ii) the salvage value of such timber. (B) Appraisal methods (i) In general With respect to the appraisal of a timber casualty loss described in subparagraph (A)\u2014 (I) the appraisal valuation date shall be not later than 1 year after the casualty loss, and (II) the appraisal shall\u2014 (aa) conform to the Uniform Standards of Professional Appraisal Practice (USPAP), (bb) be limited to the value of the lost timber, and (cc) be completed by a Federal- or State-certified appraiser. (ii) Delay in completion of appraisal (I) In general In the case of any taxpayer who is unable to obtain an appraisal described in clause (i) before the due date of the return of tax (including any extension of time for filing such return) for the taxable year in which the timber casualty loss occurred, the taxpayer may elect to\u2014 (aa) with respect to the return of tax for such taxable year, include an estimate of the value of the uncut timber determined immediately before the loss was sustained, and (bb) upon completion of the appraisal within the period described in clause (i)(I), file an amended return for such taxable year with respect to any adjustment in taxable income as determined pursuant to subclause (II). (II) Adjustment of taxable income With respect to any taxpayer who elects to provide an estimate described in subclause (I)(aa) for any taxable year in which a timber casualty loss occurred, the taxable income of the taxpayer for such taxable year shall be increased or decreased, as applicable, by an amount equal to the difference between\u2014 (aa) the appraised value of such uncut timber determined immediately before such loss was sustained, as determined pursuant to the appraisal described in clause (i), and (bb) the estimate provided by the taxpayer under subclause (I)(aa) with respect to such uncut timber. (C) Exclusion of timber not held for sale Subparagraph (A) shall not apply to any timber unless such timber is held for the purpose of being cut and sold in connection with a trade or business that is not a passive activity within the meaning of section 469. (D) Inclusion of pre-merchantable timber For purposes of this paragraph, the term uncut timber shall not fail to include pre-merchantable timber. (E) Reforestation requirement (i) In general Subparagraph (A) shall not apply unless the uncut timber subject to the loss is reforested (with hardwoods, softwoods, or any combination thereof) by planting, seeding, or appropriate site preparation, not later than the close of the 5-year period beginning on the date of such loss. (ii) Recapture The Secretary shall, by regulations, provide for recapturing the benefit of any deduction allowed under this section with respect to any uncut timber subject to loss to which subparagraph (A) applied if the taxpayer fails to comply with clause (i) during the period provided under such clause. (F) Other casualties For purposes of subparagraph (A), the term other casualty shall include loss of any uncut timber from\u2014 (i) wood-destroying insects, (ii) wood-destroying invasive species, or (iii) severe drought. .\n##### (b) Effective date\nThe amendments made by this section shall apply to losses sustained in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-26",
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
        "actionDate": "2025-01-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "262",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disaster Reforestation Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-09-17T19:57:10Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-17T19:57:10Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-09-17T19:57:10Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-09-17T19:57:10Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-08T19:56:04Z"
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
      "date": "2025-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1141is.xml"
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
      "title": "Disaster Reforestation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Disaster Reforestation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a special rule for certain casualty losses of uncut timber.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:25Z"
    }
  ]
}
```
