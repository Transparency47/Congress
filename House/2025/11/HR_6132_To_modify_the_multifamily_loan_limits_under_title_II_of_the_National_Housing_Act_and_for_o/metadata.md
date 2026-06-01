# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6132?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6132
- Title: Housing Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 6132
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2026-03-25T08:05:35Z
- Update date including text: 2026-03-25T08:05:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6132",
    "number": "6132",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000594",
        "district": "15",
        "firstName": "Monica",
        "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
        "lastName": "De La Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Housing Affordability Act",
    "type": "HR",
    "updateDate": "2026-03-25T08:05:35Z",
    "updateDateIncludingText": "2026-03-25T08:05:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
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
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6132ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6132\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Ms. De La Cruz (for herself and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo modify the multifamily loan limits under title II of the National Housing Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Affordability Act .\n#### 2. Multifamily loan limits\nTitle II of the National Housing Act ( 12 U.S.C. 1707 et seq. ) is amended\u2014\n**(1)**\nin section 206A ( 12 U.S.C. 1712a )\u2014\n**(A)**\nin subsection (a), in the matter following paragraph (7), by striking (commencing in 2004 and all that follows through the period at the end and inserting the following: , commencing on January 1, 2026. The adjustment of the Dollar Amounts shall be calculated by the Secretary using the percentage change in the Price Deflator Index of Multifamily Residential Units Under Construction released by the Bureau of the Census from March of the previous year to March of the year in which the adjustment is made. ; and\n**(B)**\nby amending subsection (b) to read as follows:\n(b) Publication (1) In general The Secretary shall publish in the Federal Register any adjustments made to the Dollar Amounts. (2) Rounding The dollar amount of any adjustment described in paragraph (1) shall be rounded to the next lower dollar. ;\n**(2)**\nin section 207(c)(3)(A) ( 12 U.S.C. 1713(c)(3)(A) )\u2014\n**(A)**\nby striking $38,025 and inserting $167,310 ;\n**(B)**\nby striking $42,120 and inserting $185,328 ;\n**(C)**\nby striking $50,310 and inserting $221,364 ;\n**(D)**\nby striking $62,010 and inserting $272,844 ;\n**(E)**\nby striking $70,200 and inserting $308,880 ;\n**(F)**\nby striking , or not to exceed $17,460 per space ;\n**(G)**\nby striking $43,875 and inserting $193,050 ;\n**(H)**\nby striking $49,140 and inserting $216,216 ;\n**(I)**\nby striking $60,255 and inserting $265,122 ;\n**(J)**\nby striking $75,465 and inserting $332,046 ; and\n**(K)**\nby striking $85,328 and inserting $375,443 ;\n**(3)**\nin section 213(b)(2) ( 12 U.S.C. 1715e(b)(2) )\u2014\n**(A)**\nby striking $41,207 and inserting $181,311 ;\n**(B)**\nby striking $47,511 and inserting $209,048 ;\n**(C)**\nby striking $57,300 and inserting $252,120 ;\n**(D)**\nby striking $73,343 and inserting $322,709 ;\n**(E)**\nby striking $81,708 and inserting $359,515 ;\n**(F)**\nby striking $43,875 and inserting $193,050 ;\n**(G)**\nby striking $49,710 and inserting $218,724 ;\n**(H)**\nby striking $60,446 and inserting $265,962 ;\n**(I)**\nby striking $78,197 and inserting $344,067 ; and\n**(J)**\nby striking $85,836 and inserting $377,678 ;\n**(4)**\nin section 220(d)(3)(B)(iii)(I) ( 12 U.S.C. 1715k(d)(3)(B)(iii)(I) )\u2014\n**(A)**\nby striking $38,025 and inserting $167,310 ;\n**(B)**\nby striking $42,120 and inserting $185,328 ;\n**(C)**\nby striking $50,310 and inserting $221,364 ;\n**(D)**\nby striking $62,010 and inserting $272,844 ;\n**(E)**\nby striking $70,200 and inserting $308,880 ;\n**(F)**\nby striking $43,875 and inserting $193,050 ;\n**(G)**\nby striking $49,140 and inserting $216,216 ;\n**(H)**\nby striking $60,255 and inserting $265,122 ;\n**(I)**\nby striking $75,465 and inserting $332,046 ; and\n**(J)**\nby striking $85,328 and inserting $375,443 ;\n**(5)**\nin section 221(d)(4)(ii)(I) ( 12 U.S.C. 1715l(d)(4)(ii)(I) )\u2014\n**(A)**\nby striking $37,843 and inserting $166,509 ;\n**(B)**\nby striking $42,954 and inserting $188,997 ;\n**(C)**\nby striking $51,920 and inserting $228,448 ;\n**(D)**\nby striking $65,169 and inserting $286,744 ;\n**(E)**\nby striking $73,846 and inserting $324,922 ;\n**(F)**\nby striking $40,876 and inserting $179,854 ;\n**(G)**\nby striking $46,859 and inserting $206,180 ;\n**(H)**\nby striking $56,979 and inserting $250,708 ;\n**(I)**\nby striking $73,710 and inserting $324,324 ; and\n**(J)**\nby striking $80,913 and inserting $356,017 ;\n**(6)**\nin section 231(c)(2)(A) ( 12 U.S.C. 1715v(c)(2)(A) )\u2014\n**(A)**\nby striking $35,978 and inserting $166,509 ;\n**(B)**\nby striking $40,220 and inserting $188,997 ;\n**(C)**\nby striking $48,029 and inserting $228,448 ;\n**(D)**\nby striking $57,798 and inserting $286,744 ;\n**(E)**\nby striking $67,950 and inserting $324,922 ;\n**(F)**\nby striking $40,876 and inserting $179,854 ;\n**(G)**\nby striking $46,859 and inserting $206,180 ;\n**(H)**\nby striking $56,979 and inserting $250,708 ;\n**(I)**\nby striking $73,710 and inserting $324,324 ; and\n**(J)**\nby striking $80,913 and inserting $356,017 ; and\n**(7)**\nin section 234(e)(3)(A) ( 12 U.S.C. 1715y(e)(3)(A) )\u2014\n**(A)**\nby striking $42,048 and inserting $185,011 ;\n**(B)**\nby striking $48,481 and inserting $213,316 ;\n**(C)**\nby striking $58,469 and inserting $257,263 ;\n**(D)**\nby striking $74,840 and inserting $329,296 ;\n**(E)**\nby striking $83,375 and inserting $366,850 ;\n**(F)**\nby striking $44,250 and inserting $194,700 ;\n**(G)**\nby striking $50,724 and inserting $223,186 ;\n**(H)**\nby striking $61,680 and inserting $271,392 ;\n**(I)**\nby striking $79,793 and inserting $351,089 ; and\n**(J)**\nby striking $87,588 and inserting $385,387 .",
      "versionDate": "2025-11-19",
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
        "actionDate": "2025-04-30",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1527",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Housing Affordability Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-01T19:36:35Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6132ih.xml"
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
      "title": "Housing Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-29T05:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Housing Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-29T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To modify the multifamily loan limits under title II of the National Housing Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-29T05:48:35Z"
    }
  ]
}
```
