# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7056?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7056
- Title: Community Bank Regulatory Tailoring Act
- Congress: 119
- Bill type: HR
- Bill number: 7056
- Origin chamber: House
- Introduced date: 2026-01-14
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-01-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 21.
- 2026-03-19 - Calendars: Placed on the Union Calendar, Calendar No. 480.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.
- Latest action: 2026-01-14: Introduced in House

## Actions

- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Introduced in House
- 2026-01-14 - IntroReferral: Referred to the House Committee on Financial Services.
- 2026-01-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-01-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 21.
- 2026-03-19 - Calendars: Placed on the Union Calendar, Calendar No. 480.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.
- 2026-03-19 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7056",
    "number": "7056",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "B001282",
        "district": "6",
        "firstName": "Andy",
        "fullName": "Rep. Barr, Andy [R-KY-6]",
        "lastName": "Barr",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "Community Bank Regulatory Tailoring Act",
    "type": "HR",
    "updateDate": "2026-05-02T19:06:20Z",
    "updateDateIncludingText": "2026-05-02T19:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-03-19",
      "calendarNumber": {
        "calendar": "U00480"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 480.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-03-19",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-558.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 21.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-22",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-14",
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
            "date": "2026-03-19T16:08:49Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-22T17:59:24Z",
            "name": "Markup By"
          },
          {
            "date": "2026-01-14T15:04:50Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "NJ"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-01-20",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7056ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7056\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo index statutory thresholds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Bank Regulatory Tailoring Act .\n#### 2. Threshold adjustments to account for historical increases in current-dollar United States Gross Domestic Product\n##### (a) Bank holding company act of 1956\nThe Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) is amended\u2014\n**(1)**\nin section 5(c)(3)(C)(ii) ( 12 U.S.C. 1844(c)(3)(C)(ii) ), by striking $1,000,000 and inserting $3,000,000 ; and\n**(2)**\nin section 13(h)(1)(B)(i) ( 12 U.S.C. 1851(h)(1)(B)(i) ), by striking $10,000,000,000 and inserting $15,000,000,000 .\n##### (b) Community reinvestment act of 1977\nSection 809(a) of the Community Reinvestment Act of 1977 ( 12 U.S.C. 2908(a) ) is amended by striking $250,000,000 and inserting $800,000,000 .\n##### (c) Depository institution management interlocks act\nThe Depository Institution Management Interlocks Act ( 12 U.S.C. 3201 et seq. ) is amended\u2014\n**(1)**\nin section 202(4) ( 12 U.S.C. 3201(4) ), by striking $100,000,000 and inserting $600,000,000 ;\n**(2)**\nin section 203(1) ( 12 U.S.C. 3202(1) ), by striking $50,000,000 and inserting $110,000,000 ; and\n**(3)**\nin section 204 ( 12 U.S.C. 3203 )\u2014\n**(A)**\nby striking $2,500,000,000 and inserting $10,000,000,000 ; and\n**(B)**\nby striking $1,500,000,000 and inserting $10,000,000,000 .\n##### (d) Dodd-Frank wall street reform and consumer protection act\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 210 ( 12 U.S.C. 5390 )\u2014\n**(A)**\nin subsection (o), by striking $50,000,000,000 and inserting $105,000,000,000 ; and\n**(B)**\nin subsection (r), by striking $1,000,000 and inserting $5,000,000 ; and\n**(2)**\nin section 956(f) ( 12 U.S.C. 5641(f) ), by striking $1,000,000,000 and inserting $3,000,000,000 .\n##### (e) Federal credit union act\nThe Federal Credit Union Act ( 12 U.S.C. 1751 et seq. ) is amended\u2014\n**(1)**\nin section 202 ( 12 U.S.C. 1782 )\u2014\n**(A)**\nin subsection (a)(6)(C)(iii)\u2014\n**(i)**\nin the heading, by striking DE MINIMUS and inserting DE MINIMIS ; and\n**(ii)**\nby striking $10,000,000 and inserting $34,000,000 ;\n**(B)**\nin subsection (a)(6)(D)\u2014\n**(i)**\nby striking $500,000,000 and inserting $2,000,000,000 ; and\n**(ii)**\nby striking $10,000,000 and inserting $34,000,000 ;\n**(C)**\nin subsection (b)(1)(A), by striking $50,000,000 each place that term appears and inserting $170,000,000 ; and\n**(D)**\nin subsection (c)(1)(A)(iii), by striking $50,000,000 each place that term appears and inserting $170,000,000 ; and\n**(2)**\nin section 216 ( 12 U.S.C. 1790d )\u2014\n**(A)**\nin subsection (f)(2), by striking $10,000,000 and inserting $34,000,000 ;\n**(B)**\nin subsection (i)(4)(B), by striking $5,000,000 and inserting $17,000,000 ;\n**(C)**\nin subsection (j)(2)(A), by striking $25,000,000 and inserting $51,000,000 ; and\n**(D)**\nin subsection (o)(4), by striking $10,000,000 and inserting $34,000,000 .\n##### (f) Federal deposit insurance act\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(1)**\nin section 7(a)(12) ( 12 U.S.C. 1817(a)(12) ), by striking $5,000,000,000 and inserting $8,000,000,000 ;\n**(2)**\nin section 11(p)(1)(A)(i) ( 12 U.S.C. 1821(p)(1)(A)(i) ), by striking $1,000,000 and inserting $5,000,000 ;\n**(3)**\nin section 36 ( 12 U.S.C. 1831m )\u2014\n**(A)**\nin subsection (i), by striking $5,000,000,000 each place that term appears and inserting $21,000,000,000 ; and\n**(B)**\nin subsection (j), by striking $150,000,000 each place that term appears and inserting $800,000,000 ; and\n**(4)**\nin section 38 ( 12 U.S.C. 1831o )\u2014\n**(A)**\nin subsection (b), by striking $300,000,000 and inserting $2,000,000,000 ; and\n**(B)**\nin subsection (k)\u2014\n**(i)**\nby striking $50,000,000 and inserting $110,000,000 ; and\n**(ii)**\nby striking $75,000,000 and inserting $150,000,000 .\n##### (g) Federal home loan bank act\nSection 2(10) of the Federal Home Loan Bank Act ( 12 U.S.C. 1422(10) ) is amended by striking $1,000,000,000 each place that term appears and inserting $3,000,000,000 .\n##### (h) Federal reserve act\nThe Federal Reserve Act ( 12 U.S.C. 221 et seq. ) is amended\u2014\n**(1)**\nin section 7(a)(1) ( 12 U.S.C. 289 ) by striking $10,000,000,000 each place that term appears and inserting $17,000,000,000 ; and\n**(2)**\nin section 22(h)(5)(C) ( 12 U.S.C. 375b(h)(5)(C) ) by striking $100,000,000 and inserting $500,000,000 .\n##### (i) Home mortgage disclosure act of 1975\nThe Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ) is amended\u2014\n**(1)**\nin the second paragraph (3) of section 304(i) ( 12 U.S.C. 2803(i)(3) ; relating to Exemption from certain disclosure requirements ), by striking $30,000,000 and inserting $160,000,000 ; and\n**(2)**\nin section 309(a) ( 12 U.S.C. 2808(a) ), by striking $10,000,000 and inserting $180,000,000 .\n##### (j) Home owners\u2019 loan act\nSection 5(u) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1464(u) ) is amended\u2014\n**(1)**\nin paragraph (2)(A)(i), by striking $500,000 and inserting $3,000,000 ; and\n**(2)**\nin paragraph (2)(A)(ii), by striking $30,000,000 and inserting $160,000,000 .\n##### (k) International lending supervision act of 1983\nSection 909(a)(1) of the International Lending Supervision Act of 1983 ( 12 U.S.C. 3908 ) is amended by striking $20,000,000 and inserting $160,000,000 .\n##### (l) Real estate settlement procedures act of 1974\nSection 3(1)(B)(iv) of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2602(1)(B)(iv) ) is amended by striking $1,000,000 and inserting $19,000,000 .\n##### (m) Revised statutes of the united states\nSection 5136A(a)(2)(D)(ii) of the Revised Statutes of the United States ( 12 U.S.C. 24a(a)(2)(D)(ii) ) is amended by striking $50,000,000,000 and inserting $175,000,000,000 .\n##### (n) Truth in lending act\nSection 129C(b)(2)(F)(i) of the Truth in Lending Act ( 15 U.S.C. 1639c(b)(2)(F)(i) ) is amended by striking $10,000,000,000 and inserting $15,000,000,000 .\n#### 3. Periodic adjustments to thresholds to account for future increases in current-dollar United States Gross Domestic Product\n##### (a) In general\nBy April 1, 2031, and the 1st day of each subsequent 5-year period, the Board of Governors of the Federal Reserve System shall prescribe the amount by which each dollar amount described in section 2 of this Act shall be increased by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the adjustment is calculated under this section, to the published annual value of such index for the calendar year preceding April 1, 2026.\n##### (b) Currency of information\nThe values used in the calculation under subsection (a) shall be, as of the date of the calculation, the values most recently published by the Department of Commerce.\n##### (c) Rounding\n**(1)**\nIf any amount equal to or greater than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000,000, the amount shall be rounded up to the nearest $50,000,000,000.\n**(2)**\nIf any amount less than $100,000,000,000 but equal to or greater than $10,000,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000,000, the amount shall be rounded up to the nearest $5,000,000,000.\n**(3)**\nIf any amount less than $10,000,000,000 but equal to or greater than $1,000,000,000 determined under subsection (a) for any period is not a multiple of $500,000,000, the amount shall be rounded up to the nearest $500,000,000.\n**(4)**\nIf any amount less than $1,000,000,000 but equal to or greater than $100,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000, the amount shall be rounded up to the nearest $50,000,000.\n**(5)**\nIf any amount less than $100,000,000 but equal to or greater than $10,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000, the amount shall be rounded up to the nearest $5,000,000.\n**(6)**\nIf any amount less than $10,000,000 but equal to or greater than $1,000,000 determined under subsection (a) for any period is not a multiple of $500,000, the amount shall be rounded up to the nearest $500,000.\n**(7)**\nIf any amount less than $1,000,000 but equal to or greater than $100,000 determined under subsection (a) for any period is not a multiple of $50,000, the amount shall be rounded up to the nearest $50,000.\n**(8)**\nIf any amount less than $100,000 but equal to or greater than $10,000 determined under subsection (a) for any period is not a multiple of $5,000, the amount shall be rounded up to the nearest $5,000.\n**(9)**\nIf any amount less than $10,000 but equal to or greater than $1,000 determined under subsection (a) for any period is not a multiple of $500, the amount shall be rounded up to the nearest $500.\n**(10)**\nIf any amount less than $1,000 but equal to or greater than $100 determined under subsection (a) for any period is not a multiple of $50, the amount shall be rounded up to the nearest $50.\n**(11)**\nIf any amount less than $100 but equal to or greater than $10 determined under subsection (a) for any period is not a multiple of $5, the amount shall be rounded up to the nearest $5.\n**(12)**\nIf any amount less than $10 but equal to or greater than $1 determined under subsection (a) for any period is not a multiple of $0.50, the amount shall be rounded up to the nearest $0.50.\n##### (d) Publication\nNot later than April 5 of any calendar year in which an adjustment is required to be calculated under subsection (a), the Board of Governors of the Federal Reserve System shall publish in the Federal Register the dollar amounts as so calculated.\n##### (e) Implementation period\nThe increase in the dollar amounts shall take effect on January 1 of the year immediately succeeding any calendar year in which an adjustment is required to be calculated under subsection (a).",
      "versionDate": "2026-01-14",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7056rh.xml",
      "text": "IB\nUnion Calendar No. 480\n119th CONGRESS\n2d Session\nH. R. 7056\n[Report No. 119\u2013558]\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 14, 2026 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nMarch 19, 2026 Additional sponsors: Mr. Gottheimer and Mr. Meuser\nMarch 19, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on January 14, 2026\nA BILL\nTo index statutory thresholds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Community Bank Regulatory Tailoring Act .\n#### 2. Threshold adjustments to account for historical increases in current-dollar United States Gross Domestic Product\n##### (a) Bank holding company act of 1956\nThe Bank Holding Company Act of 1956 ( 12 U.S.C. 1841 et seq. ) is amended\u2014\n**(1)**\nin section 5(c)(3)(C)(ii) ( 12 U.S.C. 1844(c)(3)(C)(ii) ), by striking $1,000,000 and inserting $3,000,000 ; and\n**(2)**\nin section 13(h)(1)(B)(i) ( 12 U.S.C. 1851(h)(1)(B)(i) ), by striking $10,000,000,000 and inserting $15,000,000,000 .\n##### (b) Community reinvestment act of 1977\nSection 809(a) of the Community Reinvestment Act of 1977 ( 12 U.S.C. 2908(a) ) is amended by striking $250,000,000 and inserting $800,000,000 .\n##### (c) Depository institution management interlocks act\nThe Depository Institution Management Interlocks Act ( 12 U.S.C. 3201 et seq. ) is amended\u2014\n**(1)**\nin section 202(4) ( 12 U.S.C. 3201(4) ), by striking $100,000,000 and inserting $600,000,000 ;\n**(2)**\nin section 203(1) ( 12 U.S.C. 3202(1) ), by striking $50,000,000 and inserting $110,000,000 ; and\n**(3)**\nin section 204 ( 12 U.S.C. 3203 )\u2014\n**(A)**\nby striking $2,500,000,000 and inserting $10,000,000,000 ; and\n**(B)**\nby striking $1,500,000,000 and inserting $10,000,000,000 .\n##### (d) Dodd-Frank wall street reform and consumer protection act\nThe Dodd-Frank Wall Street Reform and Consumer Protection Act ( 12 U.S.C. 5301 et seq. ) is amended\u2014\n**(1)**\nin section 210 ( 12 U.S.C. 5390 )\u2014\n**(A)**\nin subsection (o), by striking $50,000,000,000 in each place it appears and inserting $105,000,000,000 ; and\n**(B)**\nin subsection (r), by striking $1,000,000 and inserting $5,000,000 ; and\n**(2)**\nin section 956(f) ( 12 U.S.C. 5641(f) ), by striking $1,000,000,000 and inserting $3,000,000,000 .\n##### (e) Federal credit union act\nThe Federal Credit Union Act ( 12 U.S.C. 1751 et seq. ) is amended\u2014\n**(1)**\nin section 202 ( 12 U.S.C. 1782 )\u2014\n**(A)**\nin subsection (a)(6)(C)(iii)\u2014\n**(i)**\nin the heading, by striking De MINIMUS and inserting De MINIMIS ; and\n**(ii)**\nby striking $10,000,000 and inserting $34,000,000 ;\n**(B)**\nin subsection (a)(6)(D)\u2014\n**(i)**\nby striking $500,000,000 and inserting $2,000,000,000 ; and\n**(ii)**\nby striking $10,000,000 and inserting $34,000,000 ;\n**(C)**\nin subsection (b)(1)(A), by striking $50,000,000 each place that term appears and inserting $170,000,000 ; and\n**(D)**\nin subsection (c)(1)(A)(iii), by striking $50,000,000 each place that term appears and inserting $170,000,000 ; and\n**(2)**\nin section 216 ( 12 U.S.C. 1790d )\u2014\n**(A)**\nin subsection (f)(2), by striking $10,000,000 and inserting $34,000,000 ;\n**(B)**\nin subsection (i)(4)(B), by striking $5,000,000 and inserting $17,000,000 ;\n**(C)**\nin subsection (j)(2)(A), by striking $25,000,000 and inserting $51,000,000 ; and\n**(D)**\nin subsection (o)(4), by striking $10,000,000 and inserting $34,000,000 .\n##### (f) Federal deposit insurance act\nThe Federal Deposit Insurance Act ( 12 U.S.C. 1811 et seq. ) is amended\u2014\n**(1)**\nin section 7(a)(12) ( 12 U.S.C. 1817(a)(12) ), by striking $5,000,000,000 and inserting $8,000,000,000 ;\n**(2)**\nin section 11(p)(1)(A)(i) ( 12 U.S.C. 1821(p)(1)(A)(i) ), by striking $1,000,000 and inserting $5,000,000 ;\n**(3)**\nin section 36 ( 12 U.S.C. 1831m )\u2014\n**(A)**\nin subsection (i), by striking $5,000,000,000 each place that term appears and inserting $21,000,000,000 ; and\n**(B)**\nin subsection (j), by striking $150,000,000 each place that term appears and inserting $800,000,000 ; and\n**(4)**\nin section 38 ( 12 U.S.C. 1831o )\u2014\n**(A)**\nin subsection (b), by striking $300,000,000 and inserting $2,000,000,000 ; and\n**(B)**\nin subsection (k)\u2014\n**(i)**\nby striking $50,000,000 and inserting $110,000,000 ; and\n**(ii)**\nby striking $75,000,000 and inserting $150,000,000 .\n##### (g) Federal home loan bank act\nSection 2(10) of the Federal Home Loan Bank Act ( 12 U.S.C. 1422(10) ) is amended by striking $1,000,000,000 each place that term appears and inserting $3,000,000,000 .\n##### (h) Federal reserve act\nThe Federal Reserve Act ( 12 U.S.C. 221 et seq. ) is amended\u2014\n**(1)**\nin section 7(a)(1) ( 12 U.S.C. 289 ) by striking $10,000,000,000 each place that term appears and inserting $17,000,000,000 ; and\n**(2)**\nin section 22(h)(5)(C) ( 12 U.S.C. 375b(h)(5)(C) ) by striking $100,000,000 and inserting $500,000,000 .\n##### (i) Home mortgage disclosure act of 1975\nThe Home Mortgage Disclosure Act of 1975 ( 12 U.S.C. 2801 et seq. ) is amended\u2014\n**(1)**\nin the second paragraph (3) of section 304(i) ( 12 U.S.C. 2803(i)(3) ); relating to Exemption from certain disclosure requirements ), by striking $30,000,000 and inserting $160,000,000 ; and\n**(2)**\nin section 309(a) ( 12 U.S.C. 2808(a) ), by striking $10,000,000 and inserting $180,000,000 .\n##### (j) Home owners\u2019 loan act\nSection 5(u) of the Home Owners\u2019 Loan Act ( 12 U.S.C. 1464(u) ) is amended\u2014\n**(1)**\nin paragraph (2)(A)(i), by striking $500,000 and inserting $3,000,000 ; and\n**(2)**\nin paragraph (2)(A)(ii), by striking $30,000,000 and inserting $160,000,000 .\n##### (k) International lending supervision act of 1983\nSection 909(a)(1) of the International Lending Supervision Act of 1983 ( 12 U.S.C. 3908(a)(1) ) is amended by striking $20,000,000 and inserting $160,000,000 .\n##### (l) Real estate settlement procedures act of 1974\nSection 3(1)(B)(iv) of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2602(1)(B)(iv) ) is amended by striking $1,000,000 and inserting $19,000,000 .\n##### (m) Revised statutes of the united states\nSection 5136A(a)(2)(D)(ii) of the Revised Statutes of the United States ( 12 U.S.C. 24a(a)(2)(D)(ii) ) is amended by striking $50,000,000,000 and inserting $175,000,000,000 .\n##### (n) Truth in lending act\nSection 129C(b)(2)(F)(i) of the Truth in Lending Act ( 15 U.S.C. 1639c(b)(2)(F)(i) ) is amended by striking $10,000,000,000 and inserting $15,000,000,000 .\n#### 3. Periodic adjustments to thresholds to account for future increases in current-dollar United States Gross Domestic Product\n##### (a) In general\nBy April 1, 2031, and the 1st day of each subsequent 5-year period, the Board of Governors of the Federal Reserve System shall prescribe the amount by which each dollar amount described in section 2 of this Act shall be increased by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the adjustment is calculated under this section, to the published annual value of current-dollar United States gross domestic product for the calendar year preceding April 1, 2026.\n##### (b) Currency of information\nThe values used in the calculation under subsection (a) shall be, as of the date of the calculation, the values most recently published by the Department of Commerce.\n##### (c) Rounding\n**(1)**\nIf any amount equal to or greater than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000,000, the amount shall be rounded up to the nearest $50,000,000,000.\n**(2)**\nIf any amount less than $100,000,000,000 but equal to or greater than $10,000,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000,000, the amount shall be rounded up to the nearest $5,000,000,000.\n**(3)**\nIf any amount less than $10,000,000,000 but equal to or greater than $1,000,000,000 determined under subsection (a) for any period is not a multiple of $500,000,000, the amount shall be rounded up to the nearest $500,000,000.\n**(4)**\nIf any amount less than $1,000,000,000 but equal to or greater than $100,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000, the amount shall be rounded up to the nearest $50,000,000.\n**(5)**\nIf any amount less than $100,000,000 but equal to or greater than $10,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000, the amount shall be rounded up to the nearest $5,000,000.\n**(6)**\nIf any amount less than $10,000,000 but equal to or greater than $1,000,000 determined under subsection (a) for any period is not a multiple of $500,000, the amount shall be rounded up to the nearest $500,000.\n**(7)**\nIf any amount less than $1,000,000 but equal to or greater than $100,000 determined under subsection (a) for any period is not a multiple of $50,000, the amount shall be rounded up to the nearest $50,000.\n**(8)**\nIf any amount less than $100,000 but equal to or greater than $10,000 determined under subsection (a) for any period is not a multiple of $5,000, the amount shall be rounded up to the nearest $5,000.\n**(9)**\nIf any amount less than $10,000 but equal to or greater than $1,000 determined under subsection (a) for any period is not a multiple of $500, the amount shall be rounded up to the nearest $500.\n**(10)**\nIf any amount less than $1,000 but equal to or greater than $100 determined under subsection (a) for any period is not a multiple of $50, the amount shall be rounded up to the nearest $50.\n**(11)**\nIf any amount less than $100 but equal to or greater than $10 determined under subsection (a) for any period is not a multiple of $5, the amount shall be rounded up to the nearest $5.\n**(12)**\nIf any amount less than $10 but equal to or greater than $1 determined under subsection (a) for any period is not a multiple of $0.50, the amount shall be rounded up to the nearest $0.50.\n##### (d) Publication\nNot later than April 5 of any calendar year in which an adjustment is required to be calculated under subsection (a), the Board of Governors of the Federal Reserve System shall publish in the Federal Register the dollar amounts as so calculated.\n##### (e) Implementation period\nThe increase in the dollar amounts shall take effect on January 1 of the year immediately succeeding any calendar year in which an adjustment is required to be calculated under subsection (a).",
      "versionDate": "2026-03-19",
      "versionType": "Reported in House"
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-27T18:36:16Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-27T18:39:01Z"
          },
          {
            "name": "Currency",
            "updateDate": "2026-01-27T18:35:54Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2026-01-27T18:38:47Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2026-01-27T18:35:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-24T17:20:56Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7056ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7056rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Community Bank Regulatory Tailoring Act",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "title": "Community Bank Regulatory Tailoring Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Bank Regulatory Tailoring Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T05:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To index statutory thresholds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T05:48:19Z"
    }
  ]
}
```
