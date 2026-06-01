# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/262?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/262
- Title: Disaster Reforestation Act
- Congress: 119
- Bill type: HR
- Bill number: 262
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2026-04-22T08:06:48Z
- Update date including text: 2026-04-22T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/262",
    "number": "262",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "Disaster Reforestation Act",
    "type": "HR",
    "updateDate": "2026-04-22T08:06:48Z",
    "updateDateIncludingText": "2026-04-22T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-09T14:30:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "AL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MS"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NC"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "AL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "GA"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "AR"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "VA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-08-15",
      "state": "AL"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "GA"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-09-23",
      "state": "GA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "WA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "GA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "FL"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "ME"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "NC"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "MI"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NC"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr262ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 262\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Carter of Georgia (for himself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a special rule for certain casualty losses of uncut timber.\n#### 1. Short title\nThis Act may be cited as the Disaster Reforestation Act .\n#### 2. Casualty losses of uncut timber\n##### (a) In general\nSection 165(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking For purposes of subsection (a) and inserting the following:\n(1) In general For purposes of subsection (a) , and\n**(2)**\nby adding at the end the following new paragraph:\n(2) Special rule for casualty loss of uncut timber (A) In general In the case of the loss of any uncut timber from fire, storm, or other casualty, or from theft, the basis for determining the amount of the deduction for such loss (as otherwise determined under paragraph (1)) shall not be less than the excess of\u2014 (i) the appraised value of such uncut timber determined immediately before such loss was sustained, over (ii) the salvage value of such timber. (B) Appraisal methods (i) In general With respect to the appraisal of a timber casualty loss described in subparagraph (A)\u2014 (I) the appraisal valuation date shall be not later than 1 year after the casualty loss, and (II) the appraisal shall\u2014 (aa) conform to the Uniform Standards of Professional Appraisal Practice (USPAP), (bb) be limited to the value of the lost timber, and (cc) be completed by a Federal- or State-certified appraiser. (ii) Delay in completion of appraisal (I) In general In the case of any taxpayer who is unable to obtain an appraisal described in clause (i) before the due date of the return of tax (including any extension of time for filing such return) for the taxable year in which the timber casualty loss occurred, the taxpayer may elect to\u2014 (aa) with respect to the return of tax for such taxable year, include an estimate of the value of the uncut timber determined immediately before the loss was sustained, and (bb) upon completion of the appraisal within the period described in clause (i)(I), file an amended return for such taxable year with respect to any adjustment in taxable income as determined pursuant to subclause (II). (II) Adjustment of taxable income With respect to any taxpayer who elects to provide an estimate described in subclause (I)(aa) for any taxable year in which a timber casualty loss occurred, the taxable income of the taxpayer for such taxable year shall be increased or decreased, as applicable, by an amount equal to the difference between\u2014 (aa) the appraised value of such uncut timber determined immediately before such loss was sustained, as determined pursuant to the appraisal described in clause (i), and (bb) the estimate provided by the taxpayer under subclause (I)(aa) with respect to such uncut timber. (C) Exclusion of timber not held for sale Subparagraph (A) shall not apply to any timber unless such timber is held for the purpose of being cut and sold in connection with a trade or business that is not a passive activity within the meaning of section 469. (D) Inclusion of pre-merchantable timber For purposes of this paragraph, the term uncut timber shall not fail to include pre-merchantable timber. (E) Reforestation requirement (i) In general Subparagraph (A) shall not apply unless the uncut timber subject to the loss is reforested (with hardwoods, softwoods, or any combination thereof) by planting, seeding, or appropriate site preparation, not later than the close of the 5-year period beginning on the date of such loss. (ii) Recapture The Secretary shall, by regulations, provide for recapturing the benefit of any deduction allowed under this section with respect to any uncut timber subject to loss to which subparagraph (A) applied if the taxpayer fails to comply with clause (i) during the period provided under such clause. (F) Other casualties For purposes of subparagraph (A), the term other casualty shall include loss of any uncut timber from\u2014 (i) wood-destroying insects, (ii) wood-destroying invasive species, or (iii) severe drought. .\n##### (b) Effective date\nThe amendments made by this section shall apply to losses sustained in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-09",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-26",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1141",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Disaster Reforestation Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disaster relief and insurance",
            "updateDate": "2025-09-17T19:56:32Z"
          },
          {
            "name": "Forests, forestry, trees",
            "updateDate": "2025-09-17T19:56:32Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-09-17T19:56:32Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-09-17T19:56:32Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-05T15:48:24Z"
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
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr262ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "updateDate": "2025-02-05T02:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Disaster Reforestation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-05T02:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a special rule for certain casualty losses of uncut timber.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T02:18:27Z"
    }
  ]
}
```
