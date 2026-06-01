# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2610
- Title: Protecting Options for Seniors Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2610
- Origin chamber: House
- Introduced date: 2025-04-02
- Update date: 2026-05-21T19:58:08Z
- Update date including text: 2026-05-21T19:58:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-02: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-02: Introduced in House

## Actions

- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Introduced in House
- 2025-04-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-02 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-02",
    "latestAction": {
      "actionDate": "2025-04-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2610",
    "number": "2610",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Protecting Options for Seniors Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-21T19:58:08Z",
    "updateDateIncludingText": "2026-05-21T19:58:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-02",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-02",
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
          "date": "2025-04-02T22:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-02T22:03:15Z",
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
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2610ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2610\nIN THE HOUSE OF REPRESENTATIVES\nApril 2, 2025 Ms. Tenney (for herself, Mr. Langworthy , Mr. Tonko , Mr. Lawler , and Ms. Stefanik ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to address significant under projection of MA local area growth due to wage index reclassification.\n#### 1. Short title\nThis Act may be cited as the Protecting Options for Seniors Act of 2025 .\n#### 2. Addressing significant under projection of MA local area growth due to wage index reclassification\n##### (a) Local adjustment method and applicability\nSection 1853(c) of the Social Security Act ( 42 U.S.C. 1395w\u201323(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin the text preceding subparagraph (A), by striking and (7) and inserting , (6)(D), and (7) ; and\n**(B)**\nin subparagraph (C)(v)(II), by inserting , taking into account any adjustment under paragraph (6)(D) before , but not ; and\n**(2)**\nin paragraph (6)\u2014\n**(A)**\nin the heading, by inserting ; local growth percentage adjustment after defined ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(D) Additional adjustment for significant under projection of local area growth (i) In general Beginning with rates calculated for 2026, for purposes of computing rates for an MA payment area and a year as described in paragraph (1), if such area is an applicable area described in clause (ii), the Secretary shall, with respect to such area, increase the national per capita MA growth percentage determined under this paragraph for such year by the number of percentage points specified in clause (iii)(I) for such area and year. (ii) Applicable area For purposes of clause (i), an applicable area described in this clause is an MA local area with respect to which the weighted average hospital wage index in effect in such area for 2025 (or a subsequent year), as calculated under clause (iv), increased by more than 20 percent as compared to the weighted average hospital wage index in effect in such area during the preceding year (as so calculated). (iii) Local growth percentage (I) In general For purposes of clause (i), with respect to an applicable area described in clause (ii) and a year, the number of percentage points specified in this clause is equal to the product of\u2014 (aa) the percentage calculated under subclause (II) for the area and year, and (bb) the weighting factor calculated under subclause (III) for the area and year. (II) Percentage For purposes of subclause (I), the percentage calculated under this subclause for an applicable area and a year is\u2014 (aa) for 2026, the percentage by which the weighted average hospital wage index in effect in the applicable area for such year, as calculated under clause (iv), increased as compared to the weighted average hospital wage index in effect in such area for 2024 (as so calculated); and (bb) for 2027 and each subsequent year, the percentage by which the weighted average hospital wage index in effect in the applicable area for such year, as calculated under clause (iv), increased as compared to the weighted average hospital wage index in effect in such area during the preceding year (as so calculated). (III) Weighting factor For purposes of subclause (I), the weighting factor calculated under this subclause for an applicable area and a year is equal to\u2014 (aa) the total amount of payments made under sections 1833(t) and 1886 to all area hospitals in such area (including disproportionate share payments made under section 1886(d)(5)(F)) that were subject to adjustment for wage or labor costs, divided by (bb) the total amount of payments made under parts A and B of this title attributable to the payment of claims for items and services furnished in such area, excluding any such payment attributable to a payment and service delivery model being tested under section 1115A, determined using payment information with respect to the most recent calendar year for which information was computed and published under subsection (b)(4), as of the date on which the advance notice under subsection (b)(2) is provided for the year. (iv) Weighted average hospital wage index The weighted average hospital wage index in effect in an MA local area for a year is equal to the average area wage index applicable under section 1886(d)(3)(E) for all area hospitals for such area as of the date on which the advance notice under subsection (b)(2) is provided for the year, weighted by the total amount of payments made under parts A and B of this title to each such area hospital, determined using payment information with respect to the most recent calendar year for which information was computed and published under subsection (b)(4), as of such date. (v) Area hospital defined In this subparagraph, the term area hospital means, with respect to an MA local area and a year, a hospital that is geographically located in such area at any point during such year (without regard to whether such hospital was reclassified to a new geographic area pursuant to section 1886(d)(8)(B), a decision of the Medicare Geographic Classification Review Board under section 1886(d)(10), or a decision of the Secretary). (vi) Requirement of benchmark neutrality Any adjustment made under this subparagraph for an MA payment area and a year shall be made in a manner that ensures that the enrollment-weighted average applicable amount under subsection (k)(1)(B) for all MA payment areas and such year is not greater or less than what it would have been without such adjustment. .\n##### (b) Adjusting the benchmark cap\nSection 1853(k)(1)(B)(i) of the Social Security Act ( 42 U.S.C. 1395w\u201323(k)(1)(B)(i) ) is amended by inserting , taking into account any adjustment under subparagraph (D) of such subsection before , but not .\n##### (c) Adjusting the base payment amount\nSection 1853(n)(2)(E)(ii) of the Social Security Act ( 42 U.S.C. 1395w\u201323(n)(2)(E)(ii) ) is amended\u2014\n**(1)**\nin subclause (I), by inserting , taking into account any adjustment under subparagraph (D) of such subsection before , but not ; and\n**(2)**\nin subclause (II), by inserting or, in the case that the area is an applicable area (as determined under subsection (c)(6)(D)), the amount specified in subclause (I) or the amount specified in subsection (c)(1)(D) for the area for the year, whichever is greater before the period at the end.\n##### (d) Transparency and data sharing\n**(1) In general**\nSection 1853(b)(4) of the Social Security Act ( 42 U.S.C. 1395w\u201323(b)(4) ) is amended by adding at the end the following new subparagraph:\n(E) Total amount paid to each area hospital (as defined in subsection (c)(6)(D)) for the year, computed separately for part A and for part B. .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply beginning with the computation and publication of information for each MA payment area for 2026.",
      "versionDate": "2025-04-02",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-05-05T12:53:59Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-02",
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
          "measure-id": "id119hr2610",
          "measure-number": "2610",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-02",
          "originChamber": "HOUSE",
          "update-date": "2026-05-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2610v00",
            "update-date": "2026-05-21"
          },
          "action-date": "2025-04-02",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Options for Seniors Act of 2025</strong></p><p>This bill increases payments for Medicare Advantage plans in areas in which the average hospital wage index increased by more than 20% compared to the previous year. Payment increases are based on the percentage by which the average hospital wage index increased compared to the previous year and weighted by the proportion of attributable payments in the area.</p>"
        },
        "title": "Protecting Options for Seniors Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2610.xml",
    "summary": {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Options for Seniors Act of 2025</strong></p><p>This bill increases payments for Medicare Advantage plans in areas in which the average hospital wage index increased by more than 20% compared to the previous year. Payment increases are based on the percentage by which the average hospital wage index increased compared to the previous year and weighted by the proportion of attributable payments in the area.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr2610"
    },
    "title": "Protecting Options for Seniors Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-02",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Options for Seniors Act of 2025</strong></p><p>This bill increases payments for Medicare Advantage plans in areas in which the average hospital wage index increased by more than 20% compared to the previous year. Payment increases are based on the percentage by which the average hospital wage index increased compared to the previous year and weighted by the proportion of attributable payments in the area.</p>",
      "updateDate": "2026-05-21",
      "versionCode": "id119hr2610"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2610ih.xml"
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
      "title": "Protecting Options for Seniors Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T04:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Options for Seniors Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-29T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to address significant under projection of MA local area growth due to wage index reclassification.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-29T04:03:21Z"
    }
  ]
}
```
