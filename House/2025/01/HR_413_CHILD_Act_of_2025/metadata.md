# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/413?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/413
- Title: CHILD Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 413
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-05-15T08:12:12Z
- Update date including text: 2025-05-15T08:12:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/413",
    "number": "413",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "CHILD Act of 2025",
    "type": "HR",
    "updateDate": "2025-05-15T08:12:12Z",
    "updateDateIncludingText": "2025-05-15T08:12:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:03:35Z",
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
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "True",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "CA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "IA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MI"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "IA"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "RI"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr413ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 413\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mrs. Bice (for herself, Ms. S\u00e1nchez , Mr. Feenstra , Ms. Houlahan , Mr. Moolenaar , Mr. Nunn of Iowa , Mr. Torres of New York , and Mr. Magaziner ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to index dependent care assistance programs to inflation.\n#### 1. Short title\nThis Act may be cited as the Combating High Inflation Limiting Daycare Act of 2025 or the CHILD Act of 2025 .\n#### 2. Increased maximum contribution to dependent care assistance programs\n##### (a) In general\nSection 129(a)(2)(A) of the Internal Revenue Code of 1986 is amended by striking $5,000 ($2,500 and inserting $10,000 ($5,000 .\n##### (b) Cost-of-Living adjustment\nSection 129 of such Code is amended by adding at the end the following new subsection:\n(f) Inflation adjustment (1) In general Each dollar amount in this section shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which such taxable year begins, determined by substituting calendar year 2023 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding If any increase under paragraph (1) is not a multiple of $50, such increase shall be rounded to the nearest multiple of $50. .\n##### (c) Removing deadwood\nSection 129(a)(2) of such Code is amended by striking subparagraph (D).\n##### (d) Effective date\nThe amendments made by this section shall apply to calendar years beginning after December 31, 2024.",
      "versionDate": "2025-01-15",
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
        "updateDate": "2025-02-18T12:44:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr413",
          "measure-number": "413",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr413v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Combating High Inflation Limiting Daycare Act of 2025 or the CHILD Act of 2025</strong></p><p>This bill increases the maximum annual amount that may be contributed to a dependent care assistance program (generally known as a dependent care flexible spending account [FSA]).</p><p>Under the bill, the maximum annual amount that may be contributed to a dependent care\u00a0FSA increases from $5,000 ($2,500 for married taxpayers who file separate federal tax returns) to $10,000 ($5,000 for married taxpayers who file separate federal tax returns) and is adjusted annually for inflation.</p>"
        },
        "title": "CHILD Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr413.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating High Inflation Limiting Daycare Act of 2025 or the CHILD Act of 2025</strong></p><p>This bill increases the maximum annual amount that may be contributed to a dependent care assistance program (generally known as a dependent care flexible spending account [FSA]).</p><p>Under the bill, the maximum annual amount that may be contributed to a dependent care\u00a0FSA increases from $5,000 ($2,500 for married taxpayers who file separate federal tax returns) to $10,000 ($5,000 for married taxpayers who file separate federal tax returns) and is adjusted annually for inflation.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr413"
    },
    "title": "CHILD Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Combating High Inflation Limiting Daycare Act of 2025 or the CHILD Act of 2025</strong></p><p>This bill increases the maximum annual amount that may be contributed to a dependent care assistance program (generally known as a dependent care flexible spending account [FSA]).</p><p>Under the bill, the maximum annual amount that may be contributed to a dependent care\u00a0FSA increases from $5,000 ($2,500 for married taxpayers who file separate federal tax returns) to $10,000 ($5,000 for married taxpayers who file separate federal tax returns) and is adjusted annually for inflation.</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr413"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr413ih.xml"
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
      "title": "CHILD Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CHILD Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Combating High Inflation Limiting Daycare Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T07:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to index dependent care assistance programs to inflation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T07:18:37Z"
    }
  ]
}
```
