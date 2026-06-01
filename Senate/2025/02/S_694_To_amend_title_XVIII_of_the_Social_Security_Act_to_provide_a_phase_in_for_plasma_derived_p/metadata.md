# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/694?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/694
- Title: PLASMA Act
- Congress: 119
- Bill type: S
- Bill number: 694
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2025-12-05T22:48:17Z
- Update date including text: 2025-12-05T22:48:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/694",
    "number": "694",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "PLASMA Act",
    "type": "S",
    "updateDate": "2025-12-05T22:48:17Z",
    "updateDateIncludingText": "2025-12-05T22:48:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T22:20:07Z",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "AZ"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "NC"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s694is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 694\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mr. Tillis (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide a phase-in for plasma-derived products under the manufacturer discount program.\n#### 1. Short title\nThis Act may be cited as the Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act .\n#### 2. Phase-in for plasma-derived products under manufacturer discount program\nSection 1860D\u201314C(g)(4) of the Social Security Act (42 U.S.C. 1395w\u2013114c(g)(4)) is amended\u2014\n**(1)**\nin subparagraph (A), in the matter preceding clause (i), by striking and (C) and inserting , (C), and (D) ;\n**(2)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively; and\n**(3)**\nby inserting after subparagraph (C) the following:\n(D) Phase-in for plasma-derived products (i) In general For 2026 and subsequent years, subject to clause (iv), in the case of an applicable drug of a manufacturer that is a plasma-derived product (as defined in clause (ii) ), and that is marketed as of August 16, 2022, and dispensed for an applicable beneficiary, the term discounted price means the specified plasma-derived product percent (as defined in clause (iii) ) of the negotiated price of the applicable drug of the manufacturer. (ii) Plasma-derived product In this subparagraph, the term plasma-derived product means an applicable drug that is a biological product that is derived from human whole blood or plasma. (iii) Specified plasma-derived product percent In this subparagraph, the term specified plasma-derived product percent means, with respect to a year\u2014 (I) for an applicable drug that is a plasma-derived product dispensed for an applicable beneficiary who has not incurred costs, as determined in accordance with section 1860D\u20132(b)(4)(C), for covered part D drugs in the year that are equal to or exceed the annual out-of-pocket threshold specified in section 1860D\u20132(b)(4)(B)(i) for the year\u2014 (aa) for 2026, 99 percent; (bb) for 2027, 98 percent; (cc) for 2028, 95 percent; (dd) for 2029, 92 percent; and (ee) for 2030 and each subsequent year, 90 percent; and (II) for an applicable drug that is a plasma-derived product dispensed for an applicable beneficiary who has incurred costs, as determined in accordance with section 1860D\u20132(b)(4)(C), for covered part D drugs in the year that are equal to or exceed the annual out-of-pocket threshold specified in section 1860D\u20132(b)(4)(B)(i) for the year\u2014 (aa) for 2026, 99 percent; (bb) for 2027, 98 percent; (cc) for 2028, 95 percent; (dd) for 2029, 92 percent; (ee) for 2030, 90 percent; (ff) for 2031, 85 percent; and (gg) for 2032 and each subsequent year, 80 percent. (iv) Limitations This subparagraph shall not apply with respect to the following: (I) Certain drugs dispensed to LIS beneficiaries An applicable drug described in subparagraph (B)(i). (II) Specified small manufacturers An applicable drug described in subparagraph (C)(i). .",
      "versionDate": "2025-02-24",
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
        "actionDate": "2025-02-21",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1476",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PLASMA Act",
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
            "name": "Blood and blood diseases",
            "updateDate": "2025-07-17T17:25:05Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-07-17T17:25:05Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-07-17T17:25:05Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-17T17:25:05Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-17T17:25:05Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-07-17T17:25:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-21T14:06:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-24",
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
          "measure-id": "id119s694",
          "measure-number": "694",
          "measure-type": "s",
          "orig-publish-date": "2025-02-24",
          "originChamber": "SENATE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s694v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-02-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>"
        },
        "title": "PLASMA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s694.xml",
    "summary": {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s694"
    },
    "title": "PLASMA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119s694"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s694is.xml"
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
      "title": "PLASMA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PLASMA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preserving Life-saving Access to Specialty Medicines in America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide a phase-in for plasma-derived products under the manufacturer discount program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T03:18:33Z"
    }
  ]
}
```
