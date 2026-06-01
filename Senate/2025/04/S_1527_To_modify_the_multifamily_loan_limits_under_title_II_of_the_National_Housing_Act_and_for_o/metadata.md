# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1527
- Title: Housing Affordability Act
- Congress: 119
- Bill type: S
- Bill number: 1527
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2026-04-14T20:13:31Z
- Update date including text: 2026-04-14T20:13:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1527",
    "number": "1527",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Housing Affordability Act",
    "type": "S",
    "updateDate": "2026-04-14T20:13:31Z",
    "updateDateIncludingText": "2026-04-14T20:13:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
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
          "date": "2025-04-30T16:01:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1527is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1527\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Gallego (for himself and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo modify the multifamily loan limits under title II of the National Housing Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Affordability Act .\n#### 2. Multifamily loan limits\nTitle II of the National Housing Act ( 12 U.S.C. 1707 et seq. ) is amended\u2014\n**(1)**\nin section 206A ( 12 U.S.C. 1712a )\u2014\n**(A)**\nin subsection (a), in the matter following paragraph (7), by striking (commencing in 2004 and all that follows through the period at the end and inserting the following: , commencing on July 1, 2025. The adjustment of the Dollar Amounts shall be calculated by the Secretary using the percentage change in the Price Deflator Index of Multifamily Residential Units Under Construction released by the Bureau of the Census from March of the previous year to March of the year in which the adjustment is made. ; and\n**(B)**\nby amending subsection (b) to read as follows:\n(b) Publication (1) In general The Secretary shall publish in the Federal Register any adjustments made to the Dollar Amounts. (2) Rounding The dollar amount of any adjustment described in paragraph (1) shall be rounded to the next lower dollar. ;\n**(2)**\nin section 207(c)(3)(A) ( 12 U.S.C. 1713(c)(3)(A) )\u2014\n**(A)**\nby striking $38,025 and inserting $167,310 ;\n**(B)**\nby striking $42,120 and inserting $185,328 ;\n**(C)**\nby striking $50,310 and inserting $221,364 ;\n**(D)**\nby striking $62,010 and inserting $272,844 ;\n**(E)**\nby striking $70,200 and inserting $308,880 ;\n**(F)**\nby striking , or not to exceed $17,460 per space ;\n**(G)**\nby striking $43,875 and inserting $193,050 ;\n**(H)**\nby striking $49,140 and inserting $216,216 ;\n**(I)**\nby striking $60,255 and inserting $265,122 ;\n**(J)**\nby striking $75,465 and inserting $332,046 ; and\n**(K)**\nby striking $85,328 and inserting $375,443 ;\n**(3)**\nin section 213(b)(2) ( 12 U.S.C. 1715e(b)(2) )\u2014\n**(A)**\nby striking $41,207 and inserting $181,311 ;\n**(B)**\nby striking $47,511 and inserting $209,048 ;\n**(C)**\nby striking $57,300 and inserting $252,120 ;\n**(D)**\nby striking $73,343 and inserting $322,709 ;\n**(E)**\nby striking $81,708 and inserting $359,515 ;\n**(F)**\nby striking $43,875 and inserting $193,050 ;\n**(G)**\nby striking $49,710 and inserting $218,724 ;\n**(H)**\nby striking $60,446 and inserting $265,962 ;\n**(I)**\nby striking $78,197 and inserting $344,067 ; and\n**(J)**\nby striking $85,836 and inserting $377,678 ;\n**(4)**\nin section 220(d)(3)(B)(iii)(I) ( 12 U.S.C. 1715k(d)(3)(B)(iii)(I) )\u2014\n**(A)**\nby striking $38,025 and inserting $167,310 ;\n**(B)**\nby striking $42,120 and inserting $185,328 ;\n**(C)**\nby striking $50,310 and inserting $221,364 ;\n**(D)**\nby striking $62,010 and inserting $272,844 ;\n**(E)**\nby striking $70,200 and inserting $308,880 ;\n**(F)**\nby striking $43,875 and inserting $193,050 ;\n**(G)**\nby striking $49,140 and inserting $216,216 ;\n**(H)**\nby striking $60,255 and inserting $265,122 ;\n**(I)**\nby striking $75,465 and inserting $332,046 ; and\n**(J)**\nby striking $85,328 and inserting $375,443 ;\n**(5)**\nin section 221(d)(4)(ii)(I) ( 12 U.S.C. 1715l(d)(4)(ii)(I) )\u2014\n**(A)**\nby striking $37,843 and inserting $166,509 ;\n**(B)**\nby striking $42,954 and inserting $188,997 ;\n**(C)**\nby striking $51,920 and inserting $228,448 ;\n**(D)**\nby striking $65,169 and inserting $286,744 ;\n**(E)**\nby striking $73,846 and inserting $324,922 ;\n**(F)**\nby striking $40,876 and inserting $179,854 ;\n**(G)**\nby striking $46,859 and inserting $206,180 ;\n**(H)**\nby striking $56,979 and inserting $250,708 ;\n**(I)**\nby striking $73,710 and inserting $324,324 ; and\n**(J)**\nby striking $80,913 and inserting $356,017 ;\n**(6)**\nin section 231(c)(2)(A) ( 12 U.S.C. 1715v(c)(2)(A) )\u2014\n**(A)**\nby striking $35,978 and inserting $166,509 ;\n**(B)**\nby striking $40,220 and inserting $188,997 ;\n**(C)**\nby striking $48,029 and inserting $228,448 ;\n**(D)**\nby striking $57,798 and inserting $286,744 ;\n**(E)**\nby striking $67,950 and inserting $324,922 ;\n**(F)**\nby striking $40,876 and inserting $179,854 ;\n**(G)**\nby striking $46,859 and inserting $206,180 ;\n**(H)**\nby striking $56,979 and inserting $250,708 ;\n**(I)**\nby striking $73,710 and inserting $324,324 ; and\n**(J)**\nby striking $80,913 and inserting $356,017 ; and\n**(7)**\nin section 234(e)(3)(A) ( 12 U.S.C. 1715y(e)(3)(A) )\u2014\n**(A)**\nby striking $42,048 and inserting $185,011 ;\n**(B)**\nby striking $48,481 and inserting $213,316 ;\n**(C)**\nby striking $58,469 and inserting $257,263 ;\n**(D)**\nby striking $74,840 and inserting $329,296 ;\n**(E)**\nby striking $83,375 and inserting $366,850 ;\n**(F)**\nby striking $44,250 and inserting $194,700 ;\n**(G)**\nby striking $50,724 and inserting $223,186 ;\n**(H)**\nby striking $61,680 and inserting $271,392 ;\n**(I)**\nby striking $79,793 and inserting $351,089 ; and\n**(J)**\nby striking $87,588 and inserting $385,387 .",
      "versionDate": "2025-04-30",
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
        "actionDate": "2025-11-19",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "6132",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Affordability Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-21T12:20:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-30",
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
          "measure-id": "id119s1527",
          "measure-number": "1527",
          "measure-type": "s",
          "orig-publish-date": "2025-04-30",
          "originChamber": "SENATE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1527v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-04-30",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Housing Affordability Act</strong></p><p>This bill increases the Federal Housing Administration\u2019s (FHA's) multifamily housing loan limits for mortgage insurance and requires the use of a more specific inflation index for these limits.</p><p>Specifically, the bill increases the loan limits to qualify for\u00a0FHA mortgage insurance for rental housing, cooperative housing, rehabilitation and neighborhood conservation housing, housing for moderate income and displaced families, housing for elderly persons, and condominiums, and it requires these limits to be indexed to\u00a0the Price Deflator Index of Multifamily Residential Units Under Construction released by the Bureau of the Census. Currently, these limits are indexed to the Consumer Price Index for All Urban Consumers.</p>"
        },
        "title": "Housing Affordability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1527.xml",
    "summary": {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Housing Affordability Act</strong></p><p>This bill increases the Federal Housing Administration\u2019s (FHA's) multifamily housing loan limits for mortgage insurance and requires the use of a more specific inflation index for these limits.</p><p>Specifically, the bill increases the loan limits to qualify for\u00a0FHA mortgage insurance for rental housing, cooperative housing, rehabilitation and neighborhood conservation housing, housing for moderate income and displaced families, housing for elderly persons, and condominiums, and it requires these limits to be indexed to\u00a0the Price Deflator Index of Multifamily Residential Units Under Construction released by the Bureau of the Census. Currently, these limits are indexed to the Consumer Price Index for All Urban Consumers.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1527"
    },
    "title": "Housing Affordability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-30",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Housing Affordability Act</strong></p><p>This bill increases the Federal Housing Administration\u2019s (FHA's) multifamily housing loan limits for mortgage insurance and requires the use of a more specific inflation index for these limits.</p><p>Specifically, the bill increases the loan limits to qualify for\u00a0FHA mortgage insurance for rental housing, cooperative housing, rehabilitation and neighborhood conservation housing, housing for moderate income and displaced families, housing for elderly persons, and condominiums, and it requires these limits to be indexed to\u00a0the Price Deflator Index of Multifamily Residential Units Under Construction released by the Bureau of the Census. Currently, these limits are indexed to the Consumer Price Index for All Urban Consumers.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119s1527"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1527is.xml"
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
      "title": "Housing Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-10T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-10T04:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to modify the multifamily loan limits under title II of the National Housing Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-10T04:33:24Z"
    }
  ]
}
```
