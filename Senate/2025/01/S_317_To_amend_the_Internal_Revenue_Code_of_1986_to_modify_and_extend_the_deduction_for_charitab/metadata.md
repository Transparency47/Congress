# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/317?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/317
- Title: Charitable Act
- Congress: 119
- Bill type: S
- Bill number: 317
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-12-05T21:59:08Z
- Update date including text: 2025-12-05T21:59:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/317",
    "number": "317",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Charitable Act",
    "type": "S",
    "updateDate": "2025-12-05T21:59:08Z",
    "updateDateIncludingText": "2025-12-05T21:59:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
          "date": "2025-01-29T22:12:55Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NV"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "CO"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "NE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "MN"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "GA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NH"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "UT"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "TN"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "AL"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "SC"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NV"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MS"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "ME"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "NM"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NC"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "AR"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-03-26",
      "state": "NH"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "AZ"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s317is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 317\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Mr. Lankford (for himself, Mr. Coons , Ms. Cortez Masto , Mr. Hickenlooper , Mr. Ricketts , Ms. Klobuchar , Mr. Warnock , Mrs. Shaheen , Mr. Curtis , Mrs. Blackburn , Mr. Moran , Mrs. Britt , Mr. Scott of South Carolina , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify and extend the deduction for charitable contributions for individuals not itemizing deductions.\n#### 1. Short title\nThis Act may be cited as the Charitable Act .\n#### 2. Modification and extension of deduction for charitable contributions for individuals not itemizing deductions\n##### (a) In general\nSubsection (p) of section 170 of the Internal Revenue Code of 1986 is amended to read as follows:\n(p) Special rule for taxpayers who do not elect To itemize deductions In the case of a taxable year beginning in 2026 or 2027, the deduction under this subsection for the taxable year shall be equal to so much of the deduction determined under this section (without regard to this subsection) for such taxable year as does not exceed an amount equal to 1/3 of the amount of the standard deduction with respect to such individual for such taxable year. This subsection shall apply only in the case of an individual who does not elect to itemize deductions for the taxable year. .\n##### (b) Elimination of penalty\n**(1) In general**\nSection 6662(b) of the Internal Revenue Code of 1986 is amended by striking paragraph (9) and by redesignating paragraph (10) as paragraph (9).\n**(2) Increased penalty**\nSection 6662 of such Code is amended by striking subsection (l).\n**(3) Conforming amendments**\n**(A)**\nSections 6662(h)(2)(D) of such Code is amended by striking subsection (b)(10) and inserting subsection (b)(9) .\n**(B)**\nSection 6664(c)(2) of such Code is amended by striking section 6662(b)(10) and inserting section 6662(b)(9) .\n**(C)**\nSection 6751(b)(2)(A) of such Code is amended by striking by reason of paragraph (9) or (10) of subsection (b) thereof and inserting by reason of subsection (b)(9) thereof .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-29",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "801",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Charitable Act",
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
        "name": "Taxation",
        "updateDate": "2025-04-28T21:48:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s317",
          "measure-number": "317",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-06-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s317v00",
            "update-date": "2025-06-03"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Charitable Act</strong></p><p>This bill allows an individual taxpayer who does not itemize their tax deductions to claim a tax deduction for charitable contributions and eliminates the tax penalty for overstating charitable contributions. (Some limitations apply).</p><p>Under the bill, for tax years beginning in 2026 or 2027, an individual taxpayer who does not itemize their tax deductions may deduct charitable contributions of up to one-third of the standard deduction allowed to such individual. (Under current law, an individual taxpayer generally must itemize their tax deductions to deduct charitable contributions.)</p><p>The bill also eliminates the tax penalty for an underpayment of taxes attributable to overstated charitable contributions by taxpayers who do not itemize deductions. (Under current law, taxpayers who claim a deduction under this bill may be assessed a tax penalty in the amount of 50% of the portion of an understatement of tax liability attributable to overstated charitable contributions.)</p>"
        },
        "title": "Charitable Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s317.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Charitable Act</strong></p><p>This bill allows an individual taxpayer who does not itemize their tax deductions to claim a tax deduction for charitable contributions and eliminates the tax penalty for overstating charitable contributions. (Some limitations apply).</p><p>Under the bill, for tax years beginning in 2026 or 2027, an individual taxpayer who does not itemize their tax deductions may deduct charitable contributions of up to one-third of the standard deduction allowed to such individual. (Under current law, an individual taxpayer generally must itemize their tax deductions to deduct charitable contributions.)</p><p>The bill also eliminates the tax penalty for an underpayment of taxes attributable to overstated charitable contributions by taxpayers who do not itemize deductions. (Under current law, taxpayers who claim a deduction under this bill may be assessed a tax penalty in the amount of 50% of the portion of an understatement of tax liability attributable to overstated charitable contributions.)</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s317"
    },
    "title": "Charitable Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Charitable Act</strong></p><p>This bill allows an individual taxpayer who does not itemize their tax deductions to claim a tax deduction for charitable contributions and eliminates the tax penalty for overstating charitable contributions. (Some limitations apply).</p><p>Under the bill, for tax years beginning in 2026 or 2027, an individual taxpayer who does not itemize their tax deductions may deduct charitable contributions of up to one-third of the standard deduction allowed to such individual. (Under current law, an individual taxpayer generally must itemize their tax deductions to deduct charitable contributions.)</p><p>The bill also eliminates the tax penalty for an underpayment of taxes attributable to overstated charitable contributions by taxpayers who do not itemize deductions. (Under current law, taxpayers who claim a deduction under this bill may be assessed a tax penalty in the amount of 50% of the portion of an understatement of tax liability attributable to overstated charitable contributions.)</p>",
      "updateDate": "2025-06-03",
      "versionCode": "id119s317"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s317is.xml"
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
      "title": "Charitable Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Charitable Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify and extend the deduction for charitable contributions for individuals not itemizing deductions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T03:48:18Z"
    }
  ]
}
```
