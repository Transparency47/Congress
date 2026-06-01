# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/701?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/701
- Title: REDUCE Food Prices Act
- Congress: 119
- Bill type: HR
- Bill number: 701
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-03-09T16:56:08Z
- Update date including text: 2026-03-09T16:56:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/701",
    "number": "701",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001207",
        "district": "11",
        "firstName": "Mikie",
        "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
        "lastName": "Sherrill",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "REDUCE Food Prices Act",
    "type": "HR",
    "updateDate": "2026-03-09T16:56:08Z",
    "updateDateIncludingText": "2026-03-09T16:56:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
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
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:08:35Z",
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
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "CT"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr701ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 701\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Sherrill (for herself and Mrs. Hayes ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide tax incentives for the establishment and operation of small food retail businesses in areas with high food retail concentration and low levels of competition.\n#### 1. Short title\nThis Act may be cited as the Restoring Establishment Deductions and Uplifting Competition to Ease Food Prices Act or the REDUCE Food Prices Act .\n#### 2. Increased rehabilitation tax credit for qualified small food retail businesses\n##### (a) In general\nSection 47 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(e) Special rule for qualified small food retail businesses (1) In general In the case of a qualified rehabilitated building placed in service by a qualified small food retail business, subsection (a)(2) shall be applied by substituting 25 percent for 20 percent . (2) Qualified small food retail business defined (A) In general For purposes of paragraph (1), the term qualified small food retail business means a business\u2014 (i) which is described in section 38(c)(5) (determined by applying $200,000,000 for $50,000,000 in such section), (ii) at least 70 percent of the annual average gross receipts of which are attributable to the retail sale of food or produce, and (iii) which is located in a low-competition area. (B) Low-competition area For purposes of subparagraph (A), the term low-competition area means a county with respect to which the Herfindahl-Hirschman Index for the retail food sector, as measured by the Economic Research Service of the United States Department of Agriculture, is at or above a level of 1,400. .\n##### (b) Effective date\nThe amendment made by this section shall apply to property placed in service after the date of the enactment of this Act.\n#### 3. Increased work opportunity tax credit for qualified small food retail businesses\n##### (a) In general\nSection 51(b)(3) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking The amount and inserting\n(A) In general The amount , and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) Increased limitation for qualified small food retail businesses In the case of wages paid by an employer that is a qualified small food retail business (as defined in section 47(e)(2)(A)), subparagraph (A) shall be applied\u2014 (i) by substituting $8,000 for $6,000 , (ii) by substituting $14,000 for $12,000 , (iii) by substituting $16,000 for $14,000 , and (iv) by substituting $26,000 for $24,000 . .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 4. Increased bonus depreciation for qualified small food retail businesses\n##### (a) In general\nSection 168(k) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(10) Special rule for qualified small food retail businesses (A) Increased applicable percentage for property placed in service by qualified small food retail businesses In the case of property placed in service by a taxpayer that is a qualified small food retail business (as defined in section 47(e)(2)(A)), paragraph (6) shall be applied\u2014 (i) in subparagraph (A)\u2014 (I) by substituting 70 percent for 60 percent each place it appears, (II) by substituting 50 percent for 40 percent each place it appears, and (III) by substituting 30 percent for 20 percent each place it appears, and (ii) in subparagraph (B)\u2014 (I) by substituting 70 percent for 60 percent each place it appears, (II) by substituting 50 percent for 40 percent each place it appears, and (III) by substituting 30 percent for 20 percent each place it appears. (B) Increased applicable percentage for plants bearing fruits and nuts planted or grafted by qualified small food retail businesses In the case of plants bearing fruits and nuts planted or grafted by a taxpayer that is a qualified small food retail business (as defined in section 47(e)(2)(A)), paragraph (6)(C) shall be applied\u2014 (i) by substituting 70 percent for 60 percent each place it appears, (ii) by substituting 50 percent for 40 percent each place it appears, and (iii) by substituting 30 percent for 20 percent each place it appears. .\n##### (b) Effective date\nThe amendments made by this section shall apply to property placed in service, or plants planted or grafted, after the date of the enactment of this Act.\n#### 5. Increased qualified business income deduction for qualified small food retail businesses\n##### (a) In general\nSection 199A of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Special rule for qualified small food retail businesses In the case of a qualified small food retail business (as defined in section 47(e)(2)(A)), subsection (a)(2) shall be applied by substituting 25 percent for 20 percent . .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.\n#### 6. New food retail business tax credit\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. New food retail business credit (a) In general For purposes of section 38, in the case of a new small food retail business, the new food retail business credit under this section for the taxable year is an amount equal to 15 percent of qualified investment amounts paid or incurred during the taxable year. (b) Definitions For purposes of this section\u2014 (1) New food retail business The term new food retail business means a qualified small food retail business (as defined in section 47(e)(2)(A)) which began operations during the previous three taxable years. (2) Qualified investment amounts The term qualified investment amounts means amounts paid for capital investment in the property, facilities, or equipment of a business premises used for retail sales of the new food retail business. .\n##### (b) Credit part of general business credit\nSection 38(b) of the Internal Revenue Code of 1986 is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the new food retail business credit determined under section 45BB(a). .\n##### (c) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. New food retail business credit. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-01-23",
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
        "name": "Taxation",
        "updateDate": "2025-03-01T13:10:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr701",
          "measure-number": "701",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2026-03-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr701v00",
            "update-date": "2026-03-09"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Restoring Establishment Deductions and Uplifting Competition to Ease Food Prices Act or the REDUCE Food Prices Act</strong></p><p>This bill establishes a new tax credit for certain food retail businesses. The bill also increases bonus depreciation, the qualified business income (QBI) tax deduction, the rehabilitation tax credit (also known as the historic preservation tax credit), and the work opportunity tax credit (WOTC) for the businesses.</p><p>The bill establishes a new tax credit (as part of the general business tax credit) in the amount of 15% of certain capital investments by a qualified small food retail business in the first three years of operation.</p><p>The bill defines a <em>qualified small food retail business</em> as a private or closely-held company, a partnership, or a sole proprietorship (1) with annual average gross receipts of $200 million or less for the three tax years preceding the current tax year, (2) with at least 70% of its annual average gross receipts attributable to the retail sale of food or produce, and (3) located in a low-competition area.</p><p>The bill also increases</p><ul><li>bonus depreciation percentages for certain property placed into service by a qualified small food retail business,</li><li>the QBI tax deduction for\u00a0qualified small food retail business,</li><li>the rehabilitation tax credit for qualified rehabilitation expenses incurred by a qualified small food retail business, and</li><li>the\u00a0WOTC for wages paid by a qualified small food retail business to eligible workers.</li></ul>"
        },
        "title": "REDUCE Food Prices Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr701.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Establishment Deductions and Uplifting Competition to Ease Food Prices Act or the REDUCE Food Prices Act</strong></p><p>This bill establishes a new tax credit for certain food retail businesses. The bill also increases bonus depreciation, the qualified business income (QBI) tax deduction, the rehabilitation tax credit (also known as the historic preservation tax credit), and the work opportunity tax credit (WOTC) for the businesses.</p><p>The bill establishes a new tax credit (as part of the general business tax credit) in the amount of 15% of certain capital investments by a qualified small food retail business in the first three years of operation.</p><p>The bill defines a <em>qualified small food retail business</em> as a private or closely-held company, a partnership, or a sole proprietorship (1) with annual average gross receipts of $200 million or less for the three tax years preceding the current tax year, (2) with at least 70% of its annual average gross receipts attributable to the retail sale of food or produce, and (3) located in a low-competition area.</p><p>The bill also increases</p><ul><li>bonus depreciation percentages for certain property placed into service by a qualified small food retail business,</li><li>the QBI tax deduction for\u00a0qualified small food retail business,</li><li>the rehabilitation tax credit for qualified rehabilitation expenses incurred by a qualified small food retail business, and</li><li>the\u00a0WOTC for wages paid by a qualified small food retail business to eligible workers.</li></ul>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr701"
    },
    "title": "REDUCE Food Prices Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Restoring Establishment Deductions and Uplifting Competition to Ease Food Prices Act or the REDUCE Food Prices Act</strong></p><p>This bill establishes a new tax credit for certain food retail businesses. The bill also increases bonus depreciation, the qualified business income (QBI) tax deduction, the rehabilitation tax credit (also known as the historic preservation tax credit), and the work opportunity tax credit (WOTC) for the businesses.</p><p>The bill establishes a new tax credit (as part of the general business tax credit) in the amount of 15% of certain capital investments by a qualified small food retail business in the first three years of operation.</p><p>The bill defines a <em>qualified small food retail business</em> as a private or closely-held company, a partnership, or a sole proprietorship (1) with annual average gross receipts of $200 million or less for the three tax years preceding the current tax year, (2) with at least 70% of its annual average gross receipts attributable to the retail sale of food or produce, and (3) located in a low-competition area.</p><p>The bill also increases</p><ul><li>bonus depreciation percentages for certain property placed into service by a qualified small food retail business,</li><li>the QBI tax deduction for\u00a0qualified small food retail business,</li><li>the rehabilitation tax credit for qualified rehabilitation expenses incurred by a qualified small food retail business, and</li><li>the\u00a0WOTC for wages paid by a qualified small food retail business to eligible workers.</li></ul>",
      "updateDate": "2026-03-09",
      "versionCode": "id119hr701"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr701ih.xml"
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
      "title": "REDUCE Food Prices Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-25T05:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REDUCE Food Prices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Establishment Deductions and Uplifting Competition to Ease Food Prices Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-25T05:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide tax incentives for the establishment and operation of small food retail businesses in areas with high food retail concentration and low levels of competition.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:18:37Z"
    }
  ]
}
```
