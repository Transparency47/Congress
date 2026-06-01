# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2292
- Title: Over-the-Counter Monograph Drug User Fee Amendments
- Congress: 119
- Bill type: S
- Bill number: 2292
- Origin chamber: Senate
- Introduced date: 2025-07-15
- Update date: 2026-05-07T13:52:21Z
- Update date including text: 2026-05-07T13:52:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-15: Introduced in Senate
- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 152.
- Latest action: 2025-07-15: Introduced in Senate

## Actions

- 2025-07-15 - IntroReferral: Introduced in Senate
- 2025-07-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2025-07-30 - Committee: Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Committee: Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.
- 2025-09-08 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 152.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-15",
    "latestAction": {
      "actionDate": "2025-07-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2292",
    "number": "2292",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Over-the-Counter Monograph Drug User Fee Amendments",
    "type": "S",
    "updateDate": "2026-05-07T13:52:21Z",
    "updateDateIncludingText": "2026-05-07T13:52:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 152.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Reported by Senator Cassidy with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-30",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-15",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-15",
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
        "item": [
          {
            "date": "2025-09-08T21:26:24Z",
            "name": "Reported By"
          },
          {
            "date": "2025-07-30T14:00:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-15T22:02:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NJ"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2292is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2292\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Banks (for himself and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to revise and extend the user fee program for over-the-counter monograph drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Over-the-Counter Monograph Drug User Fee Amendments .\n#### 2. Finding\nCongress finds that the fees authorized by the amendments made in this Act will be dedicated to OTC monograph drug activities, as set forth in the goals identified for purposes of part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ), in the letters from the Secretary of Health and Human Services to the Chairman of the Committee on Energy and Commerce of the House of Representatives and the Chairman of the Committee on Health, Education, Labor, and Pensions of the Senate, as set forth in the Congressional Record.\n#### 3. Definitions\nSection 744L(9)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371(9)(A) ) is amended\u2014\n**(1)**\nin clause (v), by striking ; or and inserting a semicolon;\n**(2)**\nin clause (vi)\u2014\n**(A)**\nby striking addition and inserting the addition ; and\n**(B)**\nby striking the period and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(vii) the addition or modification of a testing procedure applicable to one or more OTC monograph drugs, provided that such additional or modified testing procedure reflects a voluntary consensus standard with respect to pharmaceutical quality that is\u2014 (I) established by a national or international standards development organization; and (II) recognized by the Secretary through a process described in guidance for industry, initially published in July 2023, or any successor guidance, publicly available on the website of the Food and Drug Administration, which addresses voluntary consensus standards for pharmaceutical quality. .\n#### 4. Authority to assess and use OTC monograph fees\n##### (a) Types of fees\nSection 744M(a)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking on December 31 of the fiscal year or at any time during the preceding 12-month period and inserting at any time during the applicable period specified in clause (ii) for a fiscal year ;\n**(B)**\nby striking Each person and inserting the following:\n(i) Assessment of fees Each person ; and\n**(C)**\nby adding at the end the following:\n(ii) Applicable period For purposes of clause (i), the applicable period is\u2014 (I) for fiscal year 2026, the 12-month period ending on December 31, 2025; (II) for fiscal year 2027, the 9-month period ending on September 30, 2026; and (III) for fiscal year 2028 and each subsequent fiscal year, the 12-month period ending on September 30 of the preceding fiscal year. ;\n**(2)**\nin subparagraph (B)(i), by amending subclause (I) to read as follows:\n(I) has ceased all activities related to OTC monograph drugs prior to\u2014 (aa) for purposes of fiscal year 2026, January 1, 2025; (bb) for purposes of fiscal year 2027, January 1, 2026; and (cc) for purposes of fiscal year 2028 and each subsequent fiscal year, October 1 of the preceding fiscal year; and ; and\n**(3)**\nby amending subparagraph (D) to read as follows:\n(D) Due date (i) Fiscal year 2026 For fiscal year 2026, the facility fees required under subparagraph (A) shall be due on the later of\u2014 (I) the first business day of June of such year; or (II) the first business day after the enactment of an appropriations Act providing for the collection and obligation of fees under this section for such year. (ii) Fiscal year 2027 For fiscal year 2027, the facility fees required under subparagraph (A) shall be due\u2014 (I) in a first installment representing 50 percent of such fee, on the later of\u2014 (aa) October 1, 2026; or (bb) the first business day after the enactment of an appropriations Act providing for the collection and obligation of fees under this section for such year; and (II) in a second installment representing the remaining 50 percent of such fee, on\u2014 (aa) February 1, 2027; or (bb) if an appropriations Act described in subclause (I)(bb) is not in effect on February 1, 2027, the first business day after enactment of such an appropriations Act. (iii) Subsequent fiscal years For fiscal year 2028 and each subsequent fiscal year, the facility fees required under subparagraph (A) shall be due on the later of\u2014 (I) the first business day on or after October 1 of the fiscal year; or (II) the first business day after the date of enactment of an appropriations Act providing for the collection and obligation of fees under this section for the fiscal year. .\n##### (b) Fee revenue amounts\nSection 744M(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(b) ) is amended to read as follows:\n(b) Fee revenue amounts (1) In general For each of the fiscal years 2026 through 2030, fees under subsection (a)(1) shall be established to generate a total facility fee revenue amount equal to the sum of\u2014 (A) the annual base revenue for the fiscal year (as determined under paragraph (2)); (B) the dollar amount equal to the inflation adjustment for the fiscal year (as determined under subsection (c)(1)); (C) the dollar amount equal to the operating reserve adjustment for the fiscal year, if applicable (as determined under subsection (c)(2)); (D) additional direct cost adjustments (as determined under subsection (c)(3)); (E) an additional dollar amount equal to\u2014 (i) $2,373,000 for fiscal year 2026; (ii) $1,233,000 for fiscal year 2027; and (iii) $854,000 for fiscal year 2028; and (F) in the case of a fiscal year for which the Secretary applies the one-time facility fee workload adjustment under subsection (c)(4), the dollar amount equal to such adjustment. (2) Annual base revenue For purposes of paragraph (1), the dollar amount of the annual base revenue for a fiscal year shall be\u2014 (A) for fiscal year 2026, the dollar amount of the total revenue amount established for fiscal year 2025 under this subsection as in effect on the day before the date of enactment of the Over-the-Counter Monograph Drug User Fee Amendments , not including any adjustments made for such fiscal year 2025 under subsection (c)(2), as so in effect; and (B) for fiscal years 2027 through 2030, the dollar amount of the total revenue amount established under this subsection for the previous fiscal year, not including any adjustments made for such previous fiscal year under subsection (c)(2) or (c)(3). .\n##### (c) Adjustments; annual fee setting\nSection 744M(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i)\u2014\n**(i)**\nby striking subsection (b)(2)(B) and inserting subsection (b)(1)(B) ; and\n**(ii)**\nby striking fiscal year 2022 and each subsequent fiscal year and inserting each fiscal year ;\n**(B)**\nin subparagraph (B), by striking fiscal year 2022 and all that follows through the period at the end and inserting the following:\na fiscal year shall be equal to the product of\u2014 (i) for fiscal year 2026\u2014 (I) the fee for fiscal year 2025 under subsection (a)(2); and (II) the inflation adjustment percentage under subparagraph (C); and (ii) for each of fiscal years 2027 through 2030\u2014 (I) the applicable fee under subsection (a)(2) for the preceding fiscal year; and (II) the inflation adjustment percentage under subparagraph (C). ; and\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting the sum of after is equal to ;\n**(ii)**\nby striking clause (i);\n**(iii)**\nby redesignating subclauses (I) and (II) of clause (ii) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(iv)**\nby striking (ii) for each of fiscal years 2024 and 2025, the sum of\u2014 ; and\n**(v)**\nin clause (ii), as so redesignated, by striking Washington-Baltimore, DC\u2013MD\u2013VA\u2013WV and inserting Washington\u2013Arlington\u2013Alexandria\u2013DC\u2013VA\u2013MD\u2013WV ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking fiscal year 2021 and subsequent fiscal years and inserting each fiscal year ;\n**(ii)**\nby striking subsections (b)(1)(B) and (b)(2)(C) and inserting subsection (b)(1)(C) ; and\n**(iii)**\nby striking the number of weeks specified in subparagraph (B) and inserting 10 weeks ;\n**(B)**\nby striking subparagraph (B);\n**(C)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (C), respectively; and\n**(D)**\nin subparagraph (C), as so redesignated, by striking paragraph (4) establishing and inserting paragraph (5) publishing ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subsection (b)(2)(D) and inserting subsection (b)(1)(D) ; and\n**(B)**\nby striking subparagraphs (A) through (E) and inserting the following:\n(A) $135,000 for fiscal year 2026; (B) $300,000 for fiscal year 2027; (C) $55,000 for fiscal year 2028; (D) $30,000 for fiscal year 2029; and (E) $0 for fiscal year 2030. ; and\n**(4)**\nby striking paragraph (4) and inserting the following:\n(4) One-time facility fee workload adjustment (A) In general In addition to the adjustments under paragraphs (1), (2), and (3), the Secretary may further increase the fee revenues and fees through a one-time adjustment made for fiscal year 2028, 2029, or 2030, in accordance with this paragraph. (B) Adjustment described (i) Conditions for adjustment An adjustment under this paragraph may be made for a fiscal year only if\u2014 (I) an adjustment under this paragraph had not been made for any prior fiscal year; (II) the average number of OTC monograph drug facilities subject to a facility fee under subsection (a)(1) over the period of the preceding 3 fiscal years exceeds 1,625; and (III) with respect to facilities described in subclause (II), the average number of such facilities (expressed as a percentage) that appeared on the arrears lists pursuant to subsection (e)(1)(A)(i) over the period of the preceding 3 fiscal years is less than 30 percent. (ii) Amount of adjustment An adjustment under this paragraph for a fiscal year shall equal the product of\u2014 (I) the total facility revenue amount determined under subsection (b) for the fiscal year, exclusive of the adjustment under this paragraph for such fiscal year; and (II) the excess facility percentage described in clause (iii). (iii) Excess facility percentage The excess facility percentage described in this clause is\u2014 (I) the amount by which the average number of OTC monograph drug facilities subject to a facility fee under subsection (a)(1) over the preceding 3 fiscal years exceeds 1,625; divided by (II) 1,625. (5) Annual fee setting The Secretary shall, not later than 60 days before the first day of each fiscal year\u2014 (A) establish for such fiscal year, based on the revenue amounts under subsection (b) and the adjustments provided under this subsection\u2014 (i) OTC monograph drug facility fees under subsection (a)(1); and (ii) OTC monograph order request fees under subsection (a)(2); and (B) publish such fee revenue amounts, facility fees, and OTC monograph order request fees in the Federal Register. .\n##### (d) Crediting and availability of fees\nSection 744M(f) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(f) ) is amended\u2014\n**(1)**\nin paragraph (2)(D)\u2014\n**(A)**\nin the subparagraph heading, by striking in subsequent years ; and\n**(B)**\nby striking (after fiscal year 2021) ; and\n**(2)**\nin paragraph (3), by striking 2021 through 2025 and inserting 2026 through 2030 .\n#### 5. Reauthorization; reporting requirements\nSection 744N of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201373 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking Beginning with fiscal year 2021, and not later than 120 calendar days after the end of each fiscal year thereafter and inserting Not later than 120 calendar days after the end of each fiscal year ; and\n**(B)**\nby striking section 3861(b) of the CARES Act and inserting section 2 of the Over-the-Counter Monograph Drug User Fee Amendments ;\n**(2)**\nin subsection (b), by striking fiscal year 2021 and each subsequent fiscal year and inserting each fiscal year ; and\n**(3)**\nin subsection (d), by striking 2025 each place it appears and inserting 2030 .\n#### 6. Sunset dates\n##### (a) Authorization\nSections 744L and 744M of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 ; 379j\u201372) shall cease to be effective October 1, 2030.\n##### (b) Reporting requirements\nSection 744N of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201373 ) shall cease to be effective January 31, 2031.\n#### 7. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025, or the date of the enactment of this Act, whichever is later, except that fees under part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ) shall be assessed beginning October 1, 2025, regardless of the date of the enactment of this Act.\n#### 8. Savings clause\nNotwithstanding the amendments made by this Act, part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ), as in effect on the day before the date of enactment of this Act, shall continue to be in effect with respect to assessing and collecting any fee required by such part for a fiscal year prior to fiscal year 2026.",
      "versionDate": "2025-07-15",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2292rs.xml",
      "text": "II\nCalendar No. 152\n119th CONGRESS\n1st Session\nS. 2292\nIN THE SENATE OF THE UNITED STATES\nJuly 15, 2025 Mr. Banks (for himself, Mr. Kaine , Mr. Kim , and Mr. Husted ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nSeptember 8, 2025 Reported by Mr. Cassidy , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act to revise and extend the user fee program for over-the-counter monograph drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Over-the-Counter Monograph Drug User Fee Amendments .\n#### 2. Finding\nCongress finds that the fees authorized by the amendments made in this Act will be dedicated to OTC monograph drug activities, as set forth in the goals identified for purposes of part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ), in the letters from the Secretary of Health and Human Services to the Chairman of the Committee on Energy and Commerce of the House of Representatives and the Chairman of the Committee on Health, Education, Labor, and Pensions of the Senate, as set forth in the Congressional Record.\n#### 3. Definitions\nSection 744L(9)(A) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371(9)(A) ) is amended\u2014\n**(1)**\nin clause (v), by striking ; or and inserting a semicolon;\n**(2)**\nin clause (vi)\u2014\n**(A)**\nby striking addition and inserting the addition ; and\n**(B)**\nby striking the period and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(vii) the addition or modification of a testing procedure applicable to one or more OTC monograph drugs, provided that such additional or modified testing procedure reflects a voluntary consensus standard with respect to pharmaceutical quality that is\u2014 (I) established by a national or international standards development organization; and (II) recognized by the Secretary through a process described in guidance for industry, initially published in July 2023, or any successor guidance, publicly available on the website of the Food and Drug Administration, which addresses voluntary consensus standards for pharmaceutical quality. .\n#### 4. Authority to assess and use OTC monograph fees\n##### (a) Types of fees\nSection 744M(a)(1) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby striking on December 31 of the fiscal year or at any time during the preceding 12-month period and inserting at any time during the applicable period specified in clause (ii) for a fiscal year ;\n**(B)**\nby striking Each person and inserting the following:\n(i) Assessment of fees Each person ; and\n**(C)**\nby adding at the end the following:\n(ii) Applicable period For purposes of clause (i), the applicable period is\u2014 (I) for fiscal year 2026, the 12-month period ending on December 31, 2025; (II) for fiscal year 2027, the 9-month period ending on September 30, 2026; and (III) for fiscal year 2028 and each subsequent fiscal year, the 12-month period ending on September 30 of the preceding fiscal year. ;\n**(2)**\nin subparagraph (B)(i), by amending subclause (I) to read as follows:\n(I) has ceased all activities related to OTC monograph drugs prior to\u2014 (aa) for purposes of fiscal year 2026, January 1, 2025; (bb) for purposes of fiscal year 2027, January 1, 2026; and (cc) for purposes of fiscal year 2028 and each subsequent fiscal year, October 1 of the preceding fiscal year; and ; and\n**(3)**\nby amending subparagraph (D) to read as follows:\n(D) Due date (i) Fiscal year 2026 For fiscal year 2026, the facility fees required under subparagraph (A) shall be due on the later of\u2014 (I) the first business day of June of such year; or (II) the first business day after the enactment of an appropriations Act providing for the collection and obligation of fees under this section for such year. (ii) Fiscal year 2027 For fiscal year 2027, the facility fees required under subparagraph (A) shall be due\u2014 (I) in a first installment representing 50 percent of such fee, on the later of\u2014 (aa) October 1, 2026; or (bb) the first business day after the enactment of an appropriations Act providing for the collection and obligation of fees under this section for such year; and (II) in a second installment representing the remaining 50 percent of such fee, on\u2014 (aa) February 1, 2027; or (bb) if an appropriations Act described in subclause (I)(bb) is not in effect on February 1, 2027, the first business day after enactment of such an appropriations Act. (iii) Subsequent fiscal years For fiscal year 2028 and each subsequent fiscal year, the facility fees required under subparagraph (A) shall be due on the later of\u2014 (I) the first business day on or after October 1 of the fiscal year; or (II) the first business day after the date of enactment of an appropriations Act providing for the collection and obligation of fees under this section for the fiscal year. .\n##### (b) Fee revenue amounts\nSection 744M(b) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(b) ) is amended to read as follows:\n(b) Fee revenue amounts (1) In general For each of the fiscal years 2026 through 2030, fees under subsection (a)(1) shall be established to generate a total facility fee revenue amount equal to the sum of\u2014 (A) the annual base revenue for the fiscal year (as determined under paragraph (2)); (B) the dollar amount equal to the inflation adjustment for the fiscal year (as determined under subsection (c)(1)); (C) the dollar amount equal to the operating reserve adjustment for the fiscal year, if applicable (as determined under subsection (c)(2)); (D) additional direct cost adjustments (as determined under subsection (c)(3)); (E) an additional dollar amount equal to\u2014 (i) $2,373,000 for fiscal year 2026; (ii) $1,233,000 for fiscal year 2027; and (iii) $854,000 for fiscal year 2028; and (F) in the case of a fiscal year for which the Secretary applies the one-time facility fee workload adjustment under subsection (c)(4), the dollar amount equal to such adjustment. (2) Annual base revenue For purposes of paragraph (1), the dollar amount of the annual base revenue for a fiscal year shall be\u2014 (A) for fiscal year 2026, the dollar amount of the total revenue amount established for fiscal year 2025 under this subsection as in effect on the day before the date of enactment of the Over-the-Counter Monograph Drug User Fee Amendments , not including any adjustments made for such fiscal year 2025 under subsection (c)(2), as so in effect; and (B) for fiscal years 2027 through 2030, the dollar amount of the total revenue amount established under this subsection for the previous fiscal year, not including any adjustments made for such previous fiscal year under subsection (c)(2) or (c)(3). .\n##### (c) Adjustments; annual fee setting\nSection 744M(c) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372 ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A), in the matter preceding clause (i)\u2014\n**(i)**\nby striking subsection (b)(2)(B) and inserting subsection (b)(1)(B) ; and\n**(ii)**\nby striking fiscal year 2022 and each subsequent fiscal year and inserting each fiscal year ;\n**(B)**\nin subparagraph (B), by striking fiscal year 2022 and all that follows through the period at the end and inserting the following:\na fiscal year shall be equal to the product of\u2014 (i) for fiscal year 2026\u2014 (I) the fee for fiscal year 2025 under subsection (a)(2); and (II) the inflation adjustment percentage under subparagraph (C); and (ii) for each of fiscal years 2027 through 2030\u2014 (I) the applicable fee under subsection (a)(2) for the preceding fiscal year; and (II) the inflation adjustment percentage under subparagraph (C). ; and\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting the sum of after is equal to ;\n**(ii)**\nby striking clause (i);\n**(iii)**\nby redesignating subclauses (I) and (II) of clause (ii) as clauses (i) and (ii), respectively, and adjusting the margins accordingly;\n**(iv)**\nby striking (ii) for each of fiscal years 2024 and 2025, the sum of\u2014 ; and\n**(v)**\nin clause (ii), as so redesignated, by striking Washington-Baltimore, DC\u2013MD\u2013VA\u2013WV and inserting Washington\u2013Arlington\u2013Alexandria\u2013DC\u2013VA\u2013MD\u2013WV ;\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking fiscal year 2021 and subsequent fiscal years and inserting each fiscal year ;\n**(ii)**\nby striking subsections (b)(1)(B) and (b)(2)(C) and inserting subsection (b)(1)(C) ; and\n**(iii)**\nby striking the number of weeks specified in subparagraph (B) and inserting 10 weeks ;\n**(B)**\nby striking subparagraph (B);\n**(C)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (C), respectively; and\n**(D)**\nin subparagraph (C), as so redesignated, by striking paragraph (4) establishing and inserting paragraph (5) publishing ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin the matter preceding subparagraph (A), by striking subsection (b)(2)(D) and inserting subsection (b)(1)(D) ; and\n**(B)**\nby striking subparagraphs (A) through (E) and inserting the following:\n(A) $135,000 for fiscal year 2026; (B) $300,000 for fiscal year 2027; (C) $55,000 for fiscal year 2028; (D) $30,000 for fiscal year 2029; and (E) $0 for fiscal year 2030. ; and\n**(4)**\nby striking paragraph (4) and inserting the following:\n(4) One-time facility fee workload adjustment (A) In general In addition to the adjustments under paragraphs (1), (2), and (3), the Secretary may further increase the fee revenues and fees through a one-time adjustment made for fiscal year 2028, 2029, or 2030, in accordance with this paragraph. (B) Adjustment described (i) Conditions for adjustment An adjustment under this paragraph may be made for a fiscal year only if\u2014 (I) an adjustment under this paragraph had not been made for any prior fiscal year; (II) the average number of OTC monograph drug facilities subject to a facility fee under subsection (a)(1) over the period of the preceding 3 fiscal years exceeds 1,625; and (III) with respect to facilities described in subclause (II), the average number of such facilities (expressed as a percentage) that appeared on the arrears lists pursuant to subsection (e)(1)(A)(i) over the period of the preceding 3 fiscal years is less than 30 percent. (ii) Amount of adjustment An adjustment under this paragraph for a fiscal year shall equal the product of\u2014 (I) the total facility revenue amount determined under subsection (b) for the fiscal year, exclusive of the adjustment under this paragraph for such fiscal year; and (II) the excess facility percentage described in clause (iii). (iii) Excess facility percentage The excess facility percentage described in this clause is\u2014 (I) the amount by which the average number of OTC monograph drug facilities subject to a facility fee under subsection (a)(1) over the preceding 3 fiscal years exceeds 1,625; divided by (II) 1,625. (5) Annual fee setting The Secretary shall, not later than 60 days before the first day of each fiscal year\u2014 (A) establish for such fiscal year, based on the revenue amounts under subsection (b) and the adjustments provided under this subsection\u2014 (i) OTC monograph drug facility fees under subsection (a)(1); and (ii) OTC monograph order request fees under subsection (a)(2); and (B) publish such fee revenue amounts, facility fees, and OTC monograph order request fees in the Federal Register. .\n##### (d) Crediting and availability of fees\nSection 744M(f) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201372(f) ) is amended\u2014\n**(1)**\nin paragraph (2)(D)\u2014\n**(A)**\nin the subparagraph heading, by striking in subsequent years ; and\n**(B)**\nby striking (after fiscal year 2021) ; and\n**(2)**\nin paragraph (3), by striking 2021 through 2025 and inserting 2026 through 2030 .\n#### 5. Reauthorization; reporting requirements\nSection 744N of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201373 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking Beginning with fiscal year 2021, and not later than 120 calendar days after the end of each fiscal year thereafter and inserting Not later than 120 calendar days after the end of each fiscal year ; and\n**(B)**\nby striking section 3861(b) of the CARES Act and inserting section 2 of the Over-the-Counter Monograph Drug User Fee Amendments ;\n**(2)**\nin subsection (b), by striking fiscal year 2021 and each subsequent fiscal year and inserting each fiscal year ; and\n**(3)**\nin subsection (d), by striking 2025 each place it appears and inserting 2030 .\n#### 6. Sunset dates\n##### (a) Authorization\nSections 744L and 744M of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 ; 379j\u201372) shall cease to be effective October 1, 2030.\n##### (b) Reporting requirements\nSection 744N of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201373 ) shall cease to be effective January 31, 2031.\n#### 7. Effective date\nThe amendments made by this Act shall take effect on October 1, 2025, or the date of the enactment of this Act, whichever is later, except that fees under part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ) shall be assessed beginning October 1, 2025, regardless of the date of the enactment of this Act.\n#### 8. Savings clause\nNotwithstanding the amendments made by this Act, part 10 of subchapter C of chapter VII of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 379j\u201371 et seq. ), as in effect on the day before the date of enactment of this Act, shall continue to be in effect with respect to assessing and collecting any fee required by such part for a fiscal year prior to fiscal year 2026.",
      "versionDate": "2025-09-08",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-07-30",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "2529",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to increase the clarity and predictability of the process for developing applications for Rx-to-nonprescription switches.",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-17",
        "text": "Placed on the Union Calendar, Calendar No. 254."
      },
      "number": "4273",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Over-the-Counter Monograph Drug User Fee Amendments",
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
            "name": "Congressional oversight",
            "updateDate": "2025-08-08T15:20:28Z"
          },
          {
            "name": "Drug safety, medical device, and laboratory regulation",
            "updateDate": "2025-08-08T15:20:28Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T17:11:46Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-08-08T15:20:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-07T13:52:20Z"
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
      "date": "2025-07-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2292is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2292rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Over-the-Counter Monograph Drug User Fee Amendments",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-10T04:23:20Z"
    },
    {
      "title": "Over-the-Counter Monograph Drug User Fee Amendments",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T11:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Over-the-Counter Monograph Drug User Fee Amendments",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-29T13:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Food, Drug, and Cosmetic Act to revise and extend the user fee program for over-the-counter monograph drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-29T13:18:19Z"
    }
  ]
}
```
