# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1476
- Title: PLASMA Act
- Congress: 119
- Bill type: HR
- Bill number: 1476
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2025-12-05T22:09:02Z
- Update date including text: 2025-12-05T22:09:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-21 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1476",
    "number": "1476",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001067",
        "district": "9",
        "firstName": "Richard",
        "fullName": "Rep. Hudson, Richard [R-NC-9]",
        "lastName": "Hudson",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "PLASMA Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:09:02Z",
    "updateDateIncludingText": "2025-12-05T22:09:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:38:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-21T20:38:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "K000405",
      "district": "13",
      "firstName": "Brad",
      "fullName": "Rep. Knott, Brad [R-NC-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Knott",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1476ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1476\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Hudson (for himself, Mr. Davis of North Carolina , Mr. Murphy , and Mr. Peters ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to provide a phase-in for plasma-derived products under the manufacturer discount program.\n#### 1. Short title\nThis Act may be cited as the Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act .\n#### 2. Phase-in for plasma-derived products under manufacturer discount program\nSection 1860D\u201314C(g)(4) of the Social Security Act (42 U.S.C. 1395w\u2013114c(g)(4)) is amended\u2014\n**(1)**\nin subparagraph (A), in the matter preceding clause (i), by striking and (C) and inserting , (C), and (D) ;\n**(2)**\nby redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively; and\n**(3)**\nby inserting after subparagraph (C) the following:\n(D) Phase-in for plasma-derived products (i) In general For 2026 and subsequent years, subject to clause (iv), in the case of an applicable drug of a manufacturer that is a plasma-derived product (as defined in clause (ii) ), and that is marketed as of August 16, 2022, and dispensed for an applicable beneficiary, the term discounted price means the specified plasma-derived product percent (as defined in clause (iii) ) of the negotiated price of the applicable drug of the manufacturer. (ii) Plasma-derived product In this subparagraph, the term plasma-derived product means an applicable drug that is a biological product that is derived from human whole blood or plasma. (iii) Specified plasma-derived product percent In this subparagraph, the term specified plasma-derived product percent means, with respect to a year\u2014 (I) for an applicable drug that is a plasma-derived product dispensed for an applicable beneficiary who has not incurred costs, as determined in accordance with section 1860D\u20132(b)(4)(C), for covered part D drugs in the year that are equal to or exceed the annual out-of-pocket threshold specified in section 1860D\u20132(b)(4)(B)(i) for the year\u2014 (aa) for 2026, 99 percent; (bb) for 2027, 98 percent; (cc) for 2028, 95 percent; (dd) for 2029, 92 percent; and (ee) for 2030 and each subsequent year, 90 percent; and (II) for an applicable drug that is a plasma-derived product dispensed for an applicable beneficiary who has incurred costs, as determined in accordance with section 1860D\u20132(b)(4)(C), for covered part D drugs in the year that are equal to or exceed the annual out-of-pocket threshold specified in section 1860D\u20132(b)(4)(B)(i) for the year\u2014 (aa) for 2026, 99 percent; (bb) for 2027, 98 percent; (cc) for 2028, 95 percent; (dd) for 2029, 92 percent; (ee) for 2030, 90 percent; (ff) for 2031, 85 percent; and (gg) for 2032 and each subsequent year, 80 percent. (iv) Limitations This subparagraph shall not apply with respect to the following: (I) Certain drugs dispensed to LIS beneficiaries An applicable drug described in subparagraph (B)(i). (II) Specified small manufacturers An applicable drug described in subparagraph (C)(i). .",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "694",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "PLASMA Act",
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
            "name": "Blood and blood diseases",
            "updateDate": "2025-07-17T17:23:40Z"
          },
          {
            "name": "Drug therapy",
            "updateDate": "2025-07-17T17:23:48Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-07-17T17:24:05Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-07-17T17:24:11Z"
          },
          {
            "name": "Medicare",
            "updateDate": "2025-07-17T17:24:00Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-07-17T17:23:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-18T13:35:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
    "originChamber": "House",
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
          "measure-id": "id119hr1476",
          "measure-number": "1476",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1476v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>"
        },
        "title": "PLASMA Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1476.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1476"
    },
    "title": "PLASMA Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Preserving Life-saving Access to Specialty Medicines in America Act or the PLASMA Act</strong></p><p>This bill phases-in certain price adjustments for plasma-derived products under the Medicare prescription drug benefit's Manufacturer Discount Program.</p><p>Current law requires manufacturers of covered drugs under the Medicare prescription drug benefit to provide a 10% discount for covered drugs during the initial coverage phase (i.e., before a beneficiary reaches the out-of-pocket spending threshold) and a 20% discount during the catastrophic coverage phase (i.e., after a beneficiary reaches the out-of-pocket spending threshold).\u00a0</p><p>The bill phases-in discounts for plasma-derived products over several years, starting with a 1% discount in 2026 for both the initial and catastrophic coverage phases, and ending with a 10% discount beginning in 2030 for the initial coverage phase and a 20% discount beginning in 2032 for the catastrophic coverage phase.</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119hr1476"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1476ih.xml"
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
      "title": "PLASMA Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLASMA Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Preserving Life-saving Access to Specialty Medicines in America Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to provide a phase-in for plasma-derived products under the manufacturer discount program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:27Z"
    }
  ]
}
```
