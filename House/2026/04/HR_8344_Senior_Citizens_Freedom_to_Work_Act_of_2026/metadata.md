# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8344?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8344
- Title: Senior Citizens’ Freedom to Work Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8344
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-21T20:07:53Z
- Update date including text: 2026-04-21T20:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-04-16: Introduced in House

## Actions

- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8344",
    "number": "8344",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M001210",
        "district": "3",
        "firstName": "Gregory",
        "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
        "lastName": "Murphy",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-21T20:07:53Z",
    "updateDateIncludingText": "2026-04-21T20:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionDate": "2026-04-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-16",
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
          "date": "2026-04-16T14:00:50Z",
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
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "NY"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "PA"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8344ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8344\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Murphy (for himself, Ms. Van Duyne , Ms. Tenney , Mr. Smucker , and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend title II of the Social Security Act to repeal the retirement earnings test, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Senior Citizens\u2019 Freedom to Work Act of 2026 .\n#### 2. Repeal of the Retirement Earnings Test\n##### (a) In general\nSubsections (b), (c)(1), (d), (f), (h), (j), and (k) of section 203 of the Social Security Act ( 42 U.S.C. 403 ) are repealed.\n##### (b) Conforming amendments\nSection 203 of such Act (as amended by subsection (a)) is further amended\u2014\n**(1)**\nby redesignating subsections (c), (e), (g), and (l) as subsections (b), (c), (d), and (e), respectively;\n**(2)**\nin subsection (b) (as so redesignated)\u2014\n**(A)**\nby striking Noncovered Work Outside the United States or ;\n**(B)**\nby redesignating paragraphs (2), (3), and (4) as paragraphs (1), (2), and (3), respectively;\n**(C)**\nby striking paragraphs (2), (3), and (4) of ; and\n**(D)**\nby striking the last sentence;\n**(3)**\nin subsection (c) (as so redesignated), by striking subsections (c) and (d) and inserting subsection (b) ;\n**(4)**\nin subsection (d) (as so redesignated), by striking subsection (c) each place it appears and inserting subsection (b) ; and\n**(5)**\nin subsection (e) (as so redesignated), by striking subsection (g) or (h)(1)(A) and inserting subsection (d) .\n##### (c) Additional conforming amendments\n**(1) Provisions relating to benefits terminated upon deportation**\nSection 202(n)(1) of the Social Security Act ( 42 U.S.C. 402(n)(1) ) is amended by striking Section 203(b), (c), and (d) and inserting Section 203(b) .\n**(2) Provisions relating to exemptions from reductions based on early retirement**\nSection 202(q) of such Act ( 42 U.S.C. 402(q) ) is amended\u2014\n**(A)**\nin paragraph (5)(B), by striking section 203(c)(2) and inserting section 203(b)(1) ; and\n**(B)**\nin paragraph (7)(A), by striking deductions under section 203(b), 203(c)(1), 203(d)(1), or 222(b) and inserting deductions on account of work under section 203 (as in effect on the day before the date of the enactment of the Senior Citizens\u2019 Freedom to Work Act of 2026 ) or deductions under section 222(b) .\n**(3) Provisions relating to exemptions from reductions based on disregard of certain entitlements to child\u2019s insurance benefits**\nSection 202(s) of such Act ( 42 U.S.C. 402(s) ) is amended\u2014\n**(A)**\nin paragraph (1), by striking paragraphs (2), (3), and (4) of section 203(c) and inserting paragraphs (1), (2), and (3) of section 203(b) ; and\n**(B)**\nin paragraph (3), by striking The last sentence of subsection (c) of section 203, subsection (f)(1)(C) of section 203, and subsections and inserting Subsections .\n**(4) Provisions relating to suspension of aliens' benefits**\nSection 202(t)(7) of such Act ( 42 U.S.C. 402(t)(7) ) is amended by striking Subsections (b), (c), and (d) and inserting Subsection (b) .\n**(5) Provisions relating to reductions in benefits based on maximum benefits**\nSection 203(a)(3)(B)(iii) of such Act ( 42 U.S.C. 403(a)(3)(B)(iii) ) is amended by striking and subsections (b), (c), and (d) and inserting and subsection (b) .\n**(6) Provisions relating to penalties for misrepresentations concerning earnings for periods subject to deductions on account of work**\nSection 208(a)(1)(C) of such Act ( 42 U.S.C. 408(a)(1)(C) ) is amended by striking under section 203(f) of this title for purposes of deductions from benefits and inserting under section 203 (as in effect on the day before the date of the enactment of the Senior Citizens\u2019 Freedom to Work Act of 2026 ) for purposes of deductions from benefits on account of work .\n**(7) Provisions taking into account earnings in determining benefit computation years**\nClause (I) in the next to last sentence of section 215(b)(2)(A) of such Act ( 42 U.S.C. 415(b)(2)(A) ) is amended by striking no earnings as described in section 203(f)(5) in such year and inserting no wages, and no net earnings from self-employment (in excess of net loss from self-employment), in such year .\n**(8) Provisions relating to rounding of benefits**\nSection 215(g) of such Act ( 42 U.S.C. 415(g) ) is amended by striking and any deduction under section 203(b) .\n**(9) Provisions defining income for purposes of SSI**\nSection 1612(a) of such Act ( 42 U.S.C. 1382a(a) ) is amended\u2014\n**(A)**\nin paragraph (1)(A), by striking as determined under section 203(f)(5)(C) and inserting as defined in the last two sentences of this subsection ; and\n**(B)**\nby adding at the end (after and below paragraph (2)(H)) the following:\nFor purposes of paragraph (1)(A), the term wages means wages as defined in section 209, but computed without regard to the limitations as to amounts of remuneration specified in paragraphs (1), (6)(B), (6)(C), (7)(B), and (8) of section 209(a). In making the computation under the preceding sentence, (A) services which do not constitute employment as defined in section 210, performed within the United States by an individual as an employee or performed outside the United States in the active military or naval services of the United States, shall be deemed to be employment as so defined if the remuneration for such services is not includible in computing the individual's net earnings or net loss from self-employment for purposes of title II, and (B) the term wages shall be deemed not to include (i) the amount of any payment made to, or on behalf of, an employee or any of his or her dependents (including any amount paid by an employer for insurance or annuities, or into a fund, to provide for any such payment) on account of retirement, or (ii) any payment or series of payments by an employer to an employee or any of his or her dependents upon or after the termination of the employee\u2019s employment relationship because of retirement after attaining an age specified in a plan referred to in section 209(a)(11)(B) or in a pension plan of the employer. .\n##### (d) Repeal of deductions on account of work under the Railroad Retirement Program\n**(1) In general**\nSection 2 of the Railroad Retirement Act of 1974 ( 45 U.S.C. 231a ) is amended\u2014\n**(A)**\nby striking subsection (f); and\n**(B)**\nby striking subsection (g)(2) and by redesignating subsection (g)(1) as subsection (g).\n**(2) Conforming amendments**\n**(A)**\nSection 3(f)(1) of such Act ( 45 U.S.C. 231b(f)(1) ) is amended in the first sentence by striking before any reductions under the provisions of section 2(f) of this Act, .\n**(B)**\nSection 4(g)(2) of such Act ( 45 U.S.C. 231c(g)(2) ) is amended\u2014\n**(i)**\nin clause (i), by striking shall, before any deductions under section 2(g) of this Act, and inserting shall ; and\n**(ii)**\nin clause (ii), by striking any deductions under section 2(g) of this Act and before .\n##### (e) Effective date\nThe amendments made by this section shall apply with respect to taxable years ending after December 31, 2026.",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-03-24",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "4184",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-21T17:13:43Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8344ih.xml"
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
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T02:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Senior Citizens\u2019 Freedom to Work Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title II of the Social Security Act to repeal the retirement earnings test, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:36Z"
    }
  ]
}
```
