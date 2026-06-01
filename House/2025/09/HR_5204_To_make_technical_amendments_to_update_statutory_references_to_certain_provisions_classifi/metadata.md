# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5204?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5204
- Title: To make technical amendments to update statutory references to certain provisions classified to title 7, title 20, and title 43, United States Code, and to correct related technical errors.
- Congress: 119
- Bill type: HR
- Bill number: 5204
- Origin chamber: House
- Introduced date: 2025-09-08
- Update date: 2026-02-03T19:50:17Z
- Update date including text: 2026-02-03T19:50:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-09-08: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-09-08: Introduced in House

## Actions

- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Introduced in House
- 2025-09-08 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-09-10 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-10 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-08",
    "latestAction": {
      "actionDate": "2025-09-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5204",
    "number": "5204",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "To make technical amendments to update statutory references to certain provisions classified to title 7, title 20, and title 43, United States Code, and to correct related technical errors.",
    "type": "HR",
    "updateDate": "2026-02-03T19:50:17Z",
    "updateDateIncludingText": "2026-02-03T19:50:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-08",
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
        "item": [
          {
            "date": "2025-09-10T20:38:53Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-08T16:02:25Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5204ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5204\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 8, 2025 Mr. Moskowitz introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo make technical amendments to update statutory references to certain provisions classified to title 7, title 20, and title 43, United States Code, and to correct related technical errors.\n#### 1. title 5, united states code\nSection 5109(a) of title 5, United States Code, is amended by striking section 450d of title 7 and inserting section 2204\u20132 of title 7 .\n#### 2. Title 7, United States Code\n**(1)**\nSection 32(a)(1) of the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136w\u20137(a)(1) ) is amended by striking ( 7 U.S.C. 450i(e) ) and inserting ( 7 U.S.C. 3157(e) ) .\n**(2)**\nSection 33(b)(7)(E)(i) of the Federal Insecticide, Fungicide, and Rodenticide Act ( 7 U.S.C. 136w\u20138(b)(7)(E)(i) ) is amended by striking ( 7 U.S.C. 450i(e) ) and inserting ( 7 U.S.C. 3157(e) ) .\n**(3)**\nSection 7521(b) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 3202(b) ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b) ) .\n**(4)**\nSection 1445(b)(3)(B) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3222(b)(3)(B) ) is amended\u2014\n**(A)**\nby striking (79 Stat. 431; 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157 ) ; and\n**(B)**\nby inserting ( 7 U.S.C. 3157 ) after available under section 2 of the Act of August 4, 1965 .\n**(5)**\nSection 1463(c) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3311(c) ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b) , (c)) .\n**(6)**\nSection 1469(a)(1) of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3315(a)(1) ) is amended by striking sections 2(e), 2(f), and 2(h) of the Act of August 4, 1965 (79 Stat. 431; 7 U.S.C. 450i ) and inserting sections 2(f), 2(g), and 2(i) of the Act of August 4, 1965 ( 7 U.S.C. 3157(f) , (g), (i)) .\n**(7)**\nSection 1473 of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3319 ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(c)(1)(B) ) .\n**(8)**\nSection 1671(d) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5924(d) ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(9)**\nSection 1672 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925 ) is amended as follows:\n**(A)**\nSubsection (b)(1) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(B)**\nSubsection (e)(3) is amended by striking ( 7 U.S.C. 450i(b) ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(10)**\nSection 1672B(b) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925b(b) ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(11)**\nSection 1672D(c) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5925f(c) ) is amended by striking ( 7 U.S.C. 450i(b) ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(12)**\nSection 1673(b) of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 5926(b) ) is amended by striking ( 7 U.S.C. 450i(b)(7) ) and inserting ( 7 U.S.C. 3157(b)(7) ) .\n**(13)**\nSection 251(f)(1)(D)(i) of the Department of Agriculture Reorganization Act of 1994 ( 7 U.S.C. 6971(f)(1)(D)(i) ) is amended by striking ( 7 U.S.C. 450i(b) ) and inserting ( 7 U.S.C. 3157(b) ) .\n**(14)**\nSection 413(e)(2) of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7633(e)(2) ) is amended by striking ( 7 U.S.C. 450i(b) ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(15)**\nSection 617(c)(3) of the Agricultural Research, Extension, and Education Reform Act of 1998 ( 7 U.S.C. 7655b(c)(3) ) is amended by striking ( 7 U.S.C. 450i ) and inserting ( 7 U.S.C. 3157(b)(4) , (7), (8), (11)(B)) .\n**(16)**\nSection 7526(c)(1)(A)(i) of the Food, Conservation, and Energy Act of 2008 ( 7 U.S.C. 8114(c)(1)(A)(i) ) is amended by striking ( 7 U.S.C. 450i(b)(7) ) and inserting ( 7 U.S.C. 3157(b)(7) ) .\n**(17)**\nThe last proviso in the 1st paragraph under the heading Animal and Plant Health Inspection Service in title I of H.R. 3037, 99th Congress, incorporated by reference in section 101(a) of Public Law 99\u2013190 , and enacted into law by section 106 of Public Law 100\u2013202 ( 7 U.S.C. 8351 note) is amended by striking (46 Stat. 1468; 7 U.S.C. 426\u2013426b ) and inserting ( 7 U.S.C. 8351 , 8352) .\n**(18)**\nSection 749 of the Agriculture, Rural Development, Food and Drug Administration, and Related Agencies Appropriations Act, 2006 ( 7 U.S.C. 8354 ) is amended by striking sections 426\u2013426c of title 7, United States Code and inserting \u201cthe Act of March 2, 1931 ( 7 U.S.C. 8351 , 8352) and the last proviso in the 1st paragraph under the heading \u2018 Animal and Plant Health Inspection Service \u2019 in title I of the Rural Development, Agriculture, and Related Agencies Appropriations Act, 1988 ( 7 U.S.C. 8353 )\u201d.\n#### 3. TITLE 11, UNITED STATES CODE\nSection 541(b)(3) of title 11, United States Code, is amended by striking ( 20 U.S.C. 1001 et seq. ; 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1001 et seq. ) .\n#### 4. TITLE 16, UNITED STATES CODE\n**(1)**\nSection 339(f)(4)(D) of the Department of the Interior and Related Agencies Appropriations Act, 2000 ( Public Law 106\u2013113 , division B, section 1000(a)(3), 16 U.S.C. 528 note) is amended by\u2014\n**(A)**\nstriking The Act of August 8, 1937 and inserting The Act of August 28, 1937 ( 43 U.S.C. 2601 et seq. ) ; and\n**(B)**\nstriking the Act of May 24, 1939 ( 43 U.S.C. 1181a et seq. ) and inserting the Act of May 24, 1939 ( 43 U.S.C. 2621 et seq. )\n**(2)**\nThe 4th proviso in the last paragraph under the heading federal aid in wildlife restoration in the Interior Department Appropriation Act, 1943 ( 16 U.S.C. 753 ) is amended by striking (5 U. S. C. 563\u2013564) and inserting ( 7 U.S.C. 2279i , 2220) .\n**(3)**\nSection 7(c) of the Cooperative Forestry Assistance Act of 1978 ( 16 U.S.C. 2103c(c) ) is amended by striking ( 7 U.S.C. 428a(a) and inserting ( 7 U.S.C. 2268a(a) ) .\n**(4)**\nSection 10(3) of the Fish and Wildlife Conservation Act of 1980 ( 16 U.S.C. 2909(3) ) is amended by striking (46 Stat. 1468\u20131469; 7 U.S.C. 426\u2013426b ) and inserting ( 7 U.S.C. 8351 , 8352) .\n**(5)**\nSection 814(b)(5) of the Federal Lands Recreation Enhancement Act ( 16 U.S.C. 6813(b)(5) ) is amended by\u2014\n**(A)**\nstriking August 8, 1937 and inserting August 28, 1937 ( 43 U.S.C. 2601 note, 2605) ; and\n**(B)**\nstriking ( 43 U.S.C. 1181f et seq. ) and inserting ( 43 U.S.C. 2621 et seq. ) .\n**(6)**\nSection 3(10) of the Secure Rural Schools and Community Self-Determination Act of 2000 ( 16 U.S.C. 7102(10) ) is amended by\u2014\n**(A)**\nstriking (chapter 876; 50 Stat. 875; 43 U.S.C. 1181f ) and inserting ( 43 U.S.C. 2605 ) ; and\n**(B)**\nstriking (chapter 144; 53 Stat. 753; 43 U.S.C. 1181f\u20131 et seq. ) and inserting ( 43 U.S.C. 2621 et seq. ) .\n#### 5. Title 20, United States Code\nSection 131(c) of the Higher Education Amendments of 1968 ( Public Law 90\u2013575 , 20 U.S.C. 1087\u201351 note) is amended by inserting ( 20 U.S.C. 1087\u201351 et seq. ) after part C of title IV of the Higher Education Act of 1965 .\n#### 6. Title 21, United States Code\nSection 12 of the Act of May 29, 1884 ( 21 U.S.C. 113a ), is amended by inserting ( 7 U.S.C. 3105(a) ) after section 10 (a) of the Bankhead-Jones Act of 1935 .\n#### 7. Title 26, United States Code\nSection 117(c)(2)(C) of the Internal Revenue Code of 1986 ( 26 U.S.C. 117(c)(2)(C) ) is amended by inserting ( 20 U.S.C. 1087\u201358(e) ) after section 448(e) of the Higher Education Act of 1965 .\n#### 8. title 42, united states code\n**(1)**\nSection 257(a) of the Biomass Energy and Alcohol Fuels Act of 1980 ( 42 U.S.C. 8852(a) ) is amended by inserting ( 7 U.S.C. 3104 ) after section 1 of the Bankhead-Jones Act .\n**(2)**\nSection 118 of the National and Community Service Act of 1990 ( 42 U.S.C. 12561 ) is amended as follows:\n**(A)**\nSubsection (b)(5) is amended by striking ( 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1087\u201351 et seq. ) .\n**(B)**\nSubsection (g) is amended by\u2014\n**(i)**\nstriking ( 42 U.S.C. 2753(b)(2)(A) ) and inserting ( 20 U.S.C. 1087\u201353(b)(2)(A) ) ; and\n**(ii)**\nstriking ( 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1087\u201351 et seq. ) .\n**(3)**\nSection 118A(b)(2) of the National and Community Service Act of 1990 ( 42 U.S.C. 12561a(b)(2) ) is amended as follows:\n**(A)**\nSubparagraph (B) is amended by striking ( 42 U.S.C. 2751(c) ) and inserting ( 20 U.S.C. 1087\u201351(c) ) .\n**(B)**\nSubparagraph (C) is amended by striking ( 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1087\u201351 et seq. ) .\n**(4)**\nSection 122(c)(1)(C)(i) of the National and Community Service Act of 1990 ( 42 U.S.C. 12572(c)(1)(C)(i) ) is amended by striking ( 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1087\u201351 et seq. ) .\n**(5)**\nSection 140(a)(3) of the National and Community Service Act of 1990 ( 42 U.S.C. 12594(a)(3) ) is amended by striking ( 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1087\u201351 et seq. ) .\n#### 9. title 43, united states code\n**(1)**\nSection 6 of the Act of June 14, 1926 ( 43 U.S.C. 869\u20134 ), is amended by\u2014\n**(A)**\nstriking ( 43 U.S.C. 1181f ) and inserting ( 43 U.S.C. 2605 ) ; and\n**(B)**\nstriking (53 Stat. 753) and inserting ( 43 U.S.C. 2621 et seq. ) .\n**(2)**\nSection 701(b) of the Federal Land Policy and Management Act of 1976 ( Public Law 94\u2013579 , 43 U.S.C. 1701 note) is amended by\u2014\n**(A)**\nstriking (50 Stat. 874; 43 U.S.C. 1181a\u20131181j ) and inserting ( 43 U.S.C. 2601 et seq. ) ; and\n**(B)**\nstriking (53 Stat. 753) and inserting ( 43 U.S.C. 4621 et seq. ) .\n**(3)**\nSection 305(b) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1735(b) ) is amended by striking (50 Stat. 874; 43 U.S.C. 1181a\u20131181j ) and inserting ( 43 U.S.C. 2601 et seq. ) .\n**(4)**\nSection 401(b)(1) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1751(b)(1) ) is amended by striking (50 Stat. 874; 43 U.S.C. 1181d ) and inserting ( 43 U.S.C. 2603 ) .\n**(5)**\nSection 402(a) of the Federal Land Policy and Management Act of 1976 ( 43 U.S.C. 1752(a) ) is amended by striking (50 Stat. 874, as amended; 43 U.S.C. 1181a\u20131181j ) and inserting ( 43 U.S.C. 2601 et seq. ) .\n**(6)**\nSection 4 of the Act of May 24, 1939 ( 43 U.S.C. 2624 ), is amended by striking (50 Stat. 874) and inserting ( 43 U.S.C. 2601 et seq. ) .\n**(7)**\nSection 3 of the Act of June 24, 1954 ( 43 U.S.C. 2633 ), is amended by\u2014\n**(A)**\ninserting ( 43 U.S.C. 2631 ) after in which the lands described in section 1 of this Act ;\n**(B)**\nstriking (50 Stat. 874) and inserting ( 43 U.S.C. 2605 ) ;\n**(C)**\ninserting ( 43 U.S.C. 2601 et seq. ) after and upon such designation the provisions of that Act ; and\n**(D)**\ninserting ( 43 U.S.C. 2631 ) after in lieu of the lands described in section 1 of this Act .\n#### 10. title 48, united states code\nSection 105(f)(1)(B)(iii) (matter before subclause (I)) of the Compact of Free Association Amendments Act of 2003 ( 48 U.S.C. 1921d(f)(1)(B)(iii) (matter before subclause (I))) is amended by striking ( 20 U.S.C. 1070b et seq. , 42 U.S.C. 2751 et seq. ) and inserting ( 20 U.S.C. 1070b et seq. , 1087\u201351 et seq.) .",
      "versionDate": "2025-09-08",
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
      "legislativeSubjects": {
        "item": {
          "name": "Congressional operations and organization",
          "updateDate": "2025-12-15T21:38:13Z"
        }
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-09-23T18:16:11Z"
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
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5204ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make technical amendments to update statutory references to certain provisions classified to title 7, title 20, and title 43, United States Code, and to correct related technical errors.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-12T06:48:24Z"
    },
    {
      "title": "To make technical amendments to update statutory references to certain provisions classified to title 7, title 20, and title 43, United States Code, and to correct related technical errors.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T08:05:18Z"
    }
  ]
}
```
