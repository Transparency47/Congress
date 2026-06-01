# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4184
- Title: Senior Citizens’ Freedom to Work Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4184
- Origin chamber: Senate
- Introduced date: 2026-03-24
- Update date: 2026-04-21T20:07:52Z
- Update date including text: 2026-04-21T20:07:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-24: Introduced in Senate
- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-24: Introduced in Senate

## Actions

- 2026-03-24 - IntroReferral: Introduced in Senate
- 2026-03-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-24",
    "latestAction": {
      "actionDate": "2026-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4184",
    "number": "4184",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
    "type": "S",
    "updateDate": "2026-04-21T20:07:52Z",
    "updateDateIncludingText": "2026-04-21T20:07:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-24",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-24",
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
          "date": "2026-03-24T20:57:39Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4184is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4184\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2026 Mr. Scott of Florida (for himself and Mr. Tuberville ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title II of the Social Security Act to repeal the retirement earnings test, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Senior Citizens\u2019 Freedom to Work Act of 2026 .\n#### 2. Repeal of the Retirement Earnings Test\n##### (a) In general\nSubsections (b), (c)(1), (d), (f), (h), (j), and (k) of section 203 of the Social Security Act ( 42 U.S.C. 403 ) are repealed.\n##### (b) Conforming amendments\nSection 203 of such Act (as amended by subsection (a)) is further amended\u2014\n**(1)**\nby redesignating subsections (c), (e), (g), and (l) as subsections (b), (c), (d), and (e), respectively;\n**(2)**\nin subsection (b) (as so redesignated)\u2014\n**(A)**\nin the heading, by striking Noncovered Work Outside the United States or ;\n**(B)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (1), (2), and (3), respectively; and\n**(C)**\nin the flush text following paragraph (3) (as so redesignated)\u2014\n**(i)**\nby striking paragraphs (2), (3), and (4) of ; and\n**(ii)**\nby striking the last sentence;\n**(3)**\nin subsection (c) (as so redesignated), by striking subsections (c) and (d) and inserting subsection (b) ;\n**(4)**\nin subsection (d) (as so redesignated), by striking subsection (c) each place it appears and inserting subsection (b) ; and\n**(5)**\nin subsection (e) (as so redesignated), by striking subsection (g) or (h)(1)(A) and inserting subsection (d) .\n##### (c) Additional conforming amendments\n**(1) Provisions relating to benefits terminated upon deportation**\nSection 202(n)(1) of the Social Security Act ( 42 U.S.C. 402(n)(1) ) is amended, in the flush text following subparagraph (C), by striking Section 203(b), (c), and (d) and inserting Section 203(b) .\n**(2) Provisions relating to exemptions from reductions based on early retirement**\nSection 202(q) of such Act ( 42 U.S.C. 402(q) ) is amended\u2014\n**(A)**\nin paragraph (5)(B), by striking section 203(c)(2) and inserting section 203(b)(1) ; and\n**(B)**\nin paragraph (7)(A), by striking deductions under section 203(b), 203(c)(1), 203(d)(1), or 222(b) and inserting deductions on account of work under section 203 (as in effect on the day before the date of the enactment of the Senior Citizens\u2019 Freedom to Work Act of 2026 ) or deductions under section 222(b) .\n**(3) Provisions relating to exemptions from reductions based on disregard of certain entitlements to child\u2019s insurance benefits**\nSection 202(s) of such Act ( 42 U.S.C. 402(s) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking paragraphs (2), (3), and (4) of section 203(c) and inserting paragraphs (1), (2), and (3) of section 203(b) ; and\n**(B)**\nin paragraph (3), by striking The last sentence of subsection (c) of section 203, subsection (f)(1)(C) of section 203, and subsections and inserting Subsections .\n**(4) Provisions relating to suspension of aliens' benefits**\nSection 202(t)(7) of such Act ( 42 U.S.C. 402(t)(7) ) is amended by striking Subsections (b), (c), and (d) and inserting Subsection (b) .\n**(5) Provisions relating to reductions in benefits based on maximum benefits**\nSection 203(a)(3)(B)(iii) of such Act ( 42 U.S.C. 403(a)(3)(B)(iii) ) is amended by striking and subsections (b), (c), and (d) and inserting and subsection (b) .\n**(6) Provisions relating to penalties for misrepresentations concerning earnings for periods subject to deductions on account of work**\nSection 208(a)(1)(C) of such Act ( 42 U.S.C. 408(a)(1)(C) ) is amended by striking under section 203(f) of this title for purposes of deductions from benefits and inserting under section 203 (as in effect on the day before the date of the enactment of the Senior Citizens\u2019 Freedom to Work Act of 2026 ) for purposes of deductions from benefits on account of work .\n**(7) Provisions taking into account earnings in determining benefit computation years**\nClause (I) in the next to last sentence of section 215(b)(2)(A) of such Act ( 42 U.S.C. 415(b)(2)(A) ) is amended by striking no earnings as described in section 203(f)(5) in such year and inserting no wages, and no net earnings from self-employment (in excess of net loss from self-employment), in such year .\n**(8) Provisions relating to rounding of benefits**\nSection 215(g) of such Act ( 42 U.S.C. 415(g) ) is amended by striking and any deduction under section 203(b) .\n**(9) Provisions defining income for purposes of SSI**\nSection 1612(a) of such Act ( 42 U.S.C. 1382a(a) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking as determined under section 203(f)(5)(C) and inserting as defined in the last two sentences of this subsection ; and\n**(B)**\nby adding at the end (after and below paragraph (2)(H)) the following:\nFor purposes of paragraph (1)(A), the term wages means wages as defined in section 209, but computed without regard to the limitations as to amounts of remuneration specified in paragraphs (1), (6)(B), (6)(C), (7)(B), and (8) of section 209(a). In making the computation under the preceding sentence, (A) services which do not constitute employment as defined in section 210, performed within the United States by an individual as an employee or performed outside the United States in the active military or naval services of the United States, shall be deemed to be employment as so defined if the remuneration for such services is not includible in computing the individual's net earnings or net loss from self-employment for purposes of title II, and (B) the term wages shall be deemed not to include (i) the amount of any payment made to, or on behalf of, an employee or any of his or her dependents (including any amount paid by an employer for insurance or annuities, or into a fund, to provide for any such payment) on account of retirement, or (ii) any payment or series of payments by an employer to an employee or any of his or her dependents upon or after the termination of the employee\u2019s employment relationship because of retirement after attaining an age specified in a plan referred to in section 209(a)(11)(B) or in a pension plan of the employer. .\n##### (d) Repeal of deductions on account of work under the Railroad Retirement Program\n**(1) In general**\nSection 2 of the Railroad Retirement Act of 1974 ( 45 U.S.C. 231a ) is amended\u2014\n**(A)**\nby striking subsection (f); and\n**(B)**\nby striking subsection (g)(2) and by redesignating subsection (g)(1) as subsection (g).\n**(2) Conforming amendments**\n**(A)**\nSection 3(f)(1) of such Act ( 45 U.S.C. 231b(f)(1) ) is amended in the first sentence by striking before any reductions under the provisions of section 2(f) of this Act, .\n**(B)**\nSection 4(g)(2) of such Act ( 45 U.S.C. 231c(g)(2) ) is amended\u2014\n**(i)**\nin clause (i), by striking shall, before any deductions under section 2(g) of this Act, and inserting shall ; and\n**(ii)**\nin clause (ii), by striking any deductions under section 2(g) of this Act and before .\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to taxable years beginning after the date of enactment of this Act.",
      "versionDate": "2026-03-24",
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
        "actionDate": "2026-04-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8344",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-09T15:02:41Z"
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
      "date": "2026-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4184is.xml"
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
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title II of the Social Security Act to repeal the retirement earnings test, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:29Z"
    }
  ]
}
```
