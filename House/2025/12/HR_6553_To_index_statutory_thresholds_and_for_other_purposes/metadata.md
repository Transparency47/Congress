# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6553?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6553
- Title: TIER Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6553
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-05-02T19:06:20Z
- Update date including text: 2026-05-02T19:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 457.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.
- 2026-02-25 - Calendars: Placed on the Union Calendar, Calendar No. 457.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.
- 2026-02-25 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6553",
    "number": "6553",
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
    "title": "TIER Act of 2025",
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
      "actionDate": "2026-02-25",
      "calendarNumber": {
        "calendar": "U00457"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 457.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-02-25",
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
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-532.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 33 - 19.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-10",
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
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
            "date": "2026-02-25T18:51:34Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T19:02:21Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T19:02:07Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T15:04:10Z",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "PA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "TX"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "NC"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "FL"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "OK"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6553ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6553\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo index statutory thresholds, and for other purposes.\n#### 1. Short title\nThis act may be cited as the Tailoring and Indexing Enhanced Regulations Act of 2025 or the TIER Act of 2025 .\n#### 2. Threshold adjustments to account for historical increases in current-dollar united states gross domestic product\n##### (a) Federal Reserve Act\nThe second subsection (s) (relating to assessments) of section 11 of the Federal Reserve Act ( 12 U.S.C. 248(s) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking $100,000,000,000 each place that term appears and inserting $150,000,000,000 ; and\n**(2)**\nin paragraph (3), by striking between $100,000,000,000 and $250,000,000,000 and inserting between $150,000,000,000 and $370,000,000,000 .\n##### (b) Bank Holding Company Act of 1956\nSection 4(k)(6)(B)(ii) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843(k)(6)(B)(ii) ) is amended, by striking $10,000,000,000 and inserting $15,000,000,000 .\n##### (c) Financial Stability Act of 2010\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is amended\u2014\n**(1)**\nin section 116(a) ( 12 U.S.C. 5326(a) ), by striking $250,000,000,000 and inserting $370,000,000,000 ;\n**(2)**\nin section 121(a) ( 12 U.S.C. 5331(a) ), by striking $250,000,000,000 and inserting $370,000,000,000 ;\n**(3)**\nin section 163(b) ( 12 U.S.C. 5363(b) )\u2014\n**(A)**\nby striking $250,000,000,000 each place that term appears and inserting $370,000,000,000 ; and\n**(B)**\nby striking $10,000,000,000 and inserting $15,000,000,000 ;\n**(4)**\nin section 164 ( 12 U.S.C. 5364 ), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(5)**\nin section 165 ( 12 U.S.C. 5365 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(ii)**\nin paragraph (2)(C), by striking $100,000,000,000 and inserting $150,000,000,000 ;\n**(B)**\nin subsection (h)(2), by striking $50,000,000,000 each place that term appears and inserting $75,000,000,000 ;\n**(C)**\nin subsection (i)(2)(A), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(D)**\nin subsection (j)(1), by striking $250,000,000,000 and inserting $370,000,000,000 .\n##### (d) Economic Growth, Regulatory Relief, and Consumer Protection Act\nSection 401(f) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 12 U.S.C. 5365 note) is amended by striking $250,000,000,000 and inserting $370,000,000,000 .\n#### 3. Periodic adjustments to thresholds to account for future increases in current-dollar United States gross domestic product\n##### (a) In general\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is further amended by adding at the end the following:\n177. Periodic adjustments to thresholds to account for increases in current-dollar United States gross domestic product (a) In general By April 1, 2031, and the 1st day of each subsequent 5-year period, the Board of Governors shall increase the thresholds described in subsection (b) by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the adjustment is calculated under this section, to the published annual value of such index for the calendar year preceding April 1, 2026. (b) Covered thresholds The thresholds described in this subsection are the following: (1) Each bank holding company or savings and loan holding company total consolidated asset amount in the second subsection (s) (relating to assessments) of section 11 of the Federal Reserve Act. (2) Each bank holding company total consolidated asset amount in\u2014 (A) sections 116(a), 121(a), 163(b), 164, 165(a)(1), 165(h)(2), 165(j)(1) of this Act; and (B) section 401(f) of the Economic Growth, Regulatory Relief, and Consumer Protection Act. (3) Each financial company total consolidated asset amount in section 165(i)(2)(A) of this Act. (c) Currency of information The values used in the calculation under subsection (a) shall be, as of the date of the calculation, the values most recently published by the Department of Commerce. (d) Rounding (1) If any amount equal to or greater than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000,000, the amount shall be rounded up to the nearest $50,000,000,000. (2) If any amount less than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000,000, the amount shall be rounded up to the nearest $5,000,000,000. (e) Publication Not later than April 5 of any calendar year in which an adjustment is required to be calculated under subsection (a), the Board of Governors shall publish in the Federal Register the amounts as so calculated. (f) Implementation period Any increase in amounts determined under subsection (a) shall take effect on January 1 of the year immediately succeeding the calendar year in which the increase is required to be calculated under subsection (a). 178. Adjustments to thresholds established by rule to account for increases in current-dollar United States gross domestic product (a) Agency review Not later than June 30, 2026, and the 1st day of each subsequent 5-year period, the Board of Governors, the Comptroller of the Currency, and the Corporation shall, to the extent applicable, review\u2014 (1) any regulation\u2014 (A) implementing section 165 of this Act; or (B) making specific cross-reference to any regulation of the Board of Governors implementing section 165 of this Act; and (2) any asset threshold or other quantitative threshold in such regulations implementing section 165 of this Act, or in such regulations making specific cross-reference to any regulation of the Board of Governors implementing section 165 of this Act, the amount of which is not prescribed by statute. (b) Modifications required The Board of Governors, the Comptroller of the Currency, and the Corporation shall modify any such thresholds identified by each review conducted under subsection (a) by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the modification is calculated under this section, to the published annual value of such index for the calendar year preceding the effective date of such threshold, as each respective agency shall determine as appropriate for such regulations. In making such determination, the Board of Governors, the Comptroller of the Currency, and the Corporation shall\u2014 (1) use the values for current-dollar United States gross domestic product most recently published by the Department of Commerce as of the date of commencement of the review; (2) seek to establish, to the extent feasible, uniform thresholds for use by each such agency, taking into account the entities regulated by each such agency and the purposes for which such threshold was established; and (3) seek to adjust such thresholds, to the extent feasible, with rounding consistent with section 177(d) of this Act. (c) Report Upon conclusion of each review required under subsection (a), each of the Board of Governors, the Comptroller of the Currency, and the Corporation shall transmit a report to Congress containing a description of any modification of any regulation such agency made pursuant to subsection (b). .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended by inserting after the item relating to section 176 the following:\nSec. 177 Periodic adjustments to thresholds to account for increases in current-dollar United States gross domestic product. Sec. 178. Adjustments to thresholds established by rule to account for increases in current-dollar United States gross domestic product. .",
      "versionDate": "2025-12-10",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6553rh.xml",
      "text": "IB\nUnion Calendar No. 457\n119th CONGRESS\n2d Session\nH. R. 6553\n[Report No. 119\u2013532]\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Barr introduced the following bill; which was referred to the Committee on Financial Services\nFebruary 25, 2026 Additional sponsors: Mr. Meuser , Mr. Williams of Texas , Mr. Moore of North Carolina , Ms. Salazar , Mr. Lucas , Mr. Sessions , and Mr. Nunn of Iowa\nFebruary 25, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on December 10, 2025\nA BILL\nTo index statutory thresholds, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tailoring and Indexing Enhanced Regulations Act of 2025 or the TIER Act of 2025 .\n#### 2. Threshold adjustments to account for historical increases in current-dollar united states gross domestic product\n##### (a) Federal Reserve Act\nThe second subsection (s) (relating to assessments) of section 11 of the Federal Reserve Act ( 12 U.S.C. 248(s) ) is amended\u2014\n**(1)**\nin paragraph (2), by striking $100,000,000,000 each place that term appears and inserting $150,000,000,000 ; and\n**(2)**\nin paragraph (3), by striking between $100,000,000,000 and $250,000,000,000 and inserting between $150,000,000,000 and $370,000,000,000 .\n##### (b) Bank Holding Company Act of 1956\nSection 4(k)(6)(B)(ii) of the Bank Holding Company Act of 1956 ( 12 U.S.C. 1843(k)(6)(B)(ii) ) is amended, by striking $10,000,000,000 and inserting $15,000,000,000 .\n##### (c) Financial Stability Act of 2010\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is amended\u2014\n**(1)**\nin section 116(a) ( 12 U.S.C. 5326(a) ), by striking $250,000,000,000 and inserting $370,000,000,000 ;\n**(2)**\nin section 121(a) ( 12 U.S.C. 5331(a) ), by striking $250,000,000,000 and inserting $370,000,000,000 ;\n**(3)**\nin section 163(b) ( 12 U.S.C. 5363(b) )\u2014\n**(A)**\nby striking $250,000,000,000 each place that term appears and inserting $370,000,000,000 ; and\n**(B)**\nby striking $10,000,000,000 and inserting $15,000,000,000 ;\n**(4)**\nin section 164 ( 12 U.S.C. 5364 ), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(5)**\nin section 165 ( 12 U.S.C. 5365 )\u2014\n**(A)**\nin subsection (a)\u2014\n**(i)**\nin paragraph (1), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(ii)**\nin paragraph (2)(C), by striking $100,000,000,000 and inserting $150,000,000,000 ;\n**(B)**\nin subsection (h)(2), by striking $50,000,000,000 each place that term appears and inserting $75,000,000,000 ;\n**(C)**\nin subsection (i)(2)(A), by striking $250,000,000,000 and inserting $370,000,000,000 ; and\n**(D)**\nin subsection (j)(1), by striking $250,000,000,000 and inserting $370,000,000,000 .\n##### (d) Economic Growth, Regulatory Relief, and Consumer Protection Act\nSection 401(f) of the Economic Growth, Regulatory Relief, and Consumer Protection Act ( 12 U.S.C. 5365 note) is amended by striking $250,000,000,000 and inserting $370,000,000,000 .\n#### 3. Periodic adjustments to thresholds to account for future increases in current-dollar United States gross domestic product\n##### (a) In general\nThe Financial Stability Act of 2010 ( 12 U.S.C. 5311 et seq. ) is further amended by adding at the end the following:\n177. Periodic adjustments to thresholds to account for increases in current-dollar United States gross domestic product (a) In general By April 1, 2031, and the 1st day of each subsequent 5-year period, the Board of Governors shall increase the thresholds described in subsection (b) by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the adjustment is calculated under this section, to the published annual value of such index for the calendar year preceding April 1, 2026. (b) Covered thresholds The thresholds described in this subsection are the following: (1) Each bank holding company or savings and loan holding company total consolidated asset amount in the second subsection (s) (relating to assessments) of section 11 of the Federal Reserve Act. (2) Each bank holding company total consolidated asset amount in\u2014 (A) sections 116(a), 121(a), 163(b), 164, 165(a)(1), 165(h)(2), 165(j)(1) of this Act; and (B) section 401(f) of the Economic Growth, Regulatory Relief, and Consumer Protection Act. (3) Each financial company total consolidated asset amount in section 165(i)(2)(A) of this Act. (c) Currency of information The values used in the calculation under subsection (a) shall be, as of the date of the calculation, the values most recently published by the Department of Commerce. (d) Rounding (1) If any amount equal to or greater than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $50,000,000,000, the amount shall be rounded up to the nearest $50,000,000,000. (2) If any amount less than $100,000,000,000 determined under subsection (a) for any period is not a multiple of $5,000,000,000, the amount shall be rounded up to the nearest $5,000,000,000. (e) Publication Not later than April 5 of any calendar year in which an adjustment is required to be calculated under subsection (a), the Board of Governors shall publish in the Federal Register the amounts as so calculated. (f) Implementation period Any increase in amounts determined under subsection (a) shall take effect on January 1 of the year immediately succeeding the calendar year in which the increase is required to be calculated under subsection (a). 178. Adjustments to thresholds established by rule to account for increases in current-dollar United States gross domestic product (a) Agency review Not later than June 30, 2026, and the 1st day of each subsequent 5-year period, the Board of Governors, the Comptroller of the Currency, and the Corporation shall, to the extent applicable, review\u2014 (1) any regulation\u2014 (A) implementing section 165 of this Act; or (B) making specific cross-reference to any regulation of the Board of Governors implementing section 165 of this Act; and (2) any asset threshold or other quantitative threshold in such regulations implementing section 165 of this Act, or in such regulations making specific cross-reference to any regulation of the Board of Governors implementing section 165 of this Act, the amount of which is not prescribed by statute. (b) Modifications required The Board of Governors, the Comptroller of the Currency, and the Corporation shall modify any such thresholds identified by each review conducted under subsection (a) by the ratio, if greater than 1, of the annual value of current-dollar United States gross domestic product, published by the Department of Commerce, for the calendar year preceding the year in which the modification is calculated under this section, to the published annual value of such index for the calendar year preceding the effective date of such threshold, as each respective agency shall determine as appropriate for such regulations. In making such determination, the Board of Governors, the Comptroller of the Currency, and the Corporation shall\u2014 (1) use the values for current-dollar United States gross domestic product most recently published by the Department of Commerce as of the date of commencement of the review; (2) seek to establish, to the extent feasible, uniform thresholds for use by each such agency, taking into account the entities regulated by each such agency and the purposes for which such threshold was established; and (3) seek to adjust such thresholds, to the extent feasible, with rounding consistent with section 177(d) of this Act. (c) Report Upon conclusion of each review required under subsection (a), each of the Board of Governors, the Comptroller of the Currency, and the Corporation shall transmit a report to Congress containing a description of any modification of any regulation such agency made pursuant to subsection (b). .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Dodd-Frank Wall Street Reform and Consumer Protection Act is amended by inserting after the item relating to section 176 the following:\nSec. 177. Periodic adjustments to thresholds to account for increases in current-dollar United States gross domestic product. Sec. 178. Adjustments to thresholds established by rule to account for increases in current-dollar United States gross domestic product. .",
      "versionDate": "2026-02-25",
      "versionType": "Reported in House"
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
        "actionDate": "2026-04-20",
        "text": "Placed on the Union Calendar, Calendar No. 535."
      },
      "number": "6955",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Main Street Act",
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
            "name": "Bank accounts, deposits, capital",
            "updateDate": "2026-01-28T16:27:10Z"
          },
          {
            "name": "Banking and financial institutions regulation",
            "updateDate": "2026-01-28T16:27:32Z"
          },
          {
            "name": "Currency",
            "updateDate": "2026-01-28T16:26:38Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2026-01-28T16:26:45Z"
          },
          {
            "name": "Financial crises and stabilization",
            "updateDate": "2026-01-28T16:27:26Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2026-01-28T16:35:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-12-15T19:30:46Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6553ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-02-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr6553rh.xml"
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
      "title": "TIER Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:19Z"
    },
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Tailoring and Indexing Enhanced Regulations Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-02-26T07:23:19Z"
    },
    {
      "title": "TIER Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-13T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TIER Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tailoring and Indexing Enhanced Regulations Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-13T09:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To index statutory thresholds, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T09:03:26Z"
    }
  ]
}
```
