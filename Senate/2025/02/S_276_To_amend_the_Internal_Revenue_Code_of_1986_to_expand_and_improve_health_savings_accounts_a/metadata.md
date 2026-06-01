# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/276?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/276
- Title: Personalized Care Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 276
- Origin chamber: Senate
- Introduced date: 2025-01-28
- Update date: 2026-01-09T12:03:22Z
- Update date including text: 2026-01-09T12:03:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in Senate
- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-28: Introduced in Senate

## Actions

- 2025-01-28 - IntroReferral: Introduced in Senate
- 2025-01-28 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/276",
    "number": "276",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Personalized Care Act of 2025",
    "type": "S",
    "updateDate": "2026-01-09T12:03:22Z",
    "updateDateIncludingText": "2026-01-09T12:03:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
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
            "date": "2025-01-28T19:39:43Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-28T19:39:43Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "KS"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s276is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 276\nIN THE SENATE OF THE UNITED STATES\nJanuary 28, 2025 Mr. Cruz (for himself and Mr. Marshall ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to expand and improve health savings accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Personalized Care Act of 2025 .\n#### 2. Health savings account eligibility\n##### (a) In general\nParagraph (1) of section 223(c) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) Eligible individual The term eligible individual means, with respect to any month, any individual if such individual is\u2014 (A) covered under\u2014 (i) a group or individual health plan, (ii) health insurance coverage, including a short term limited duration plan or medical indemnity plan, or (iii) a government plan, including coverage under the Medicare program under part A or part B of title XVIII of the Social Security Act, the Medicaid program under title XIX of such Act, the CHIP program under title XXI of such Act or a qualified CHIP look-alike program (as defined in section 2107(g) of such Act), medical coverage under chapter 55 of title 10, United States Code (including coverage under the TRICARE program), a health care program under chapter 17 or 18 of title 38, United States Code, as determined by the Secretary of Veterans Affairs in coordination with the Secretary of Health and Human Services and the Secretary, a medical care program of the Indian Health Service or a tribal organization, or coverage under chapter 89 of title 5, United States Code, or (B) a participant in a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof), as of the 1st day of such month. .\n##### (b) Conforming amendments\n**(1)**\nSubsection (c) of section 223 of the Internal Revenue Code of 1986 is amended by striking paragraphs (2) and (3) and by redesignating paragraphs (4) and (5) as paragraphs (2) and (3), respectively.\n**(2)**\nParagraphs (2)(A) and (2)(B) of section 223(b) of such Code are each amended by striking a high deductible health plan and inserting a health plan, insurance, or ministry described in subsection (c)(1) .\n**(3)**\nParagraph (8)(A)(ii) of section 223(b) of such Code is amended by striking high deductible health plan and inserting health plan, insurance, or ministry described in subsection (c)(1) .\n**(4)**\nSection 223(g)(1) of such Code is amended\u2014\n**(A)**\nby striking subsections (b)(2) and (c)(2)(A) both places it appears and inserting subsection (b)(2) , and\n**(B)**\nby striking for calendar year 2016 in subparagraph (B) and all that follows through calendar year 2003 . and inserting calendar year 1997 for calendar year 2016 in subparagraph (A)(ii) thereof. .\n**(5)**\nThe heading of subparagraph (B) of section 223(b)(8) of such Code is amended by striking high deductible health plan .\n**(6)**\nSection 26(b)(2)(S) of such Code is amended by striking high deductible health plan .\n**(7)**\nThe heading of paragraph (3) of section 106(e) of such Code is amended by striking high deductible health plan .\n**(8)**\nClause (ii) of section 106(e)(5)(B) of such Code is amended by striking a high deductible health plan and inserting a health plan .\n**(9)**\nParagraph (9) of section 408(d) of such Code is amended\u2014\n**(A)**\nby striking the high deductible health plan covering in subparagraph (C)(i)(I) and inserting health plan, insurance, or ministry of ,\n**(B)**\nby striking a high deductible health plan the first place it appears in subparagraph (C)(ii)(II) and inserting a health plan, insurance, or ministry described in section 223(c)(1) ,\n**(C)**\nby striking a high deductible health plan the second place it appears in subparagraph (C)(ii)(II) and inserting any such plan, insurance, or ministry , and\n**(D)**\nby striking high deductible health plan in the heading of subparagraph (D).\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Increase in HSA contribution limits\n##### (a) In general\nParagraph (2) of section 223(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking $2,250 in subparagraph (A) and inserting $10,800 , and\n**(2)**\nby striking $4,500 in subparagraph (B) and inserting $29,500 .\n##### (b) Cost-of-Living adjustment\nParagraph (1) of section 223(g) of the Internal Revenue Code of 1986, as amended by section 2, is amended\u2014\n**(1)**\nby striking Each and inserting In the case of a taxable year beginning after 2026, each , and\n**(2)**\nby striking calendar year 1997 and inserting calendar year 2025 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 4. Payment of health plan and health insurance premiums from HSA\n##### (a) In general\nParagraph (2) of section 223(d) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking subparagraph (B),\n**(2)**\nby redesignating subparagraphs (C) and (D) as subparagraphs (B) and (C), respectively,\n**(3)**\nby striking Subparagraph (B) shall not apply to any expense for coverage under in subparagraph (B), as so redesignated, and inserting Subparagraph (A) shall not apply to any payment for insurance other than , and\n**(4)**\nin subparagraph (B), as so redesignated\u2014\n**(A)**\nby striking or at the end of clause (iii),\n**(B)**\nby striking the period at the end of clause (iv) and inserting , or , and\n**(C)**\nby adding at the end the following new clause:\n(v) a health plan or health insurance coverage described in subsection (c)(1)(A). .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 5. Treatment of medical care service arrangements\n##### (a) Inclusion as medical expenses\nParagraph (2) of section 223(d) of the Internal Revenue Code of 1986, as amended by section 4, is further amended by adding at the end the following new subparagraph:\n(D) Inclusion of medical care service arrangements The term qualified medical expenses shall include\u2014 (i) periodic fees paid to a physician for a defined set of medical services or for the right to receive medical services on an as-needed basis, and (ii) amounts prepaid for medical services designed to screen for, diagnose, cure, mitigate, treat, or prevent disease and promote wellness. .\n##### (b) Arrangement not To be treated as health insurance\nSubsection (c) of section 223 of the Internal Revenue Code of 1986, as amended by section 2(b), is further amended by adding at the end the following new paragraph:\n(4) Treatment of medical care service arrangements An arrangement under which an individual is provided medical services in exchange for a fixed periodic fee or payment for such services shall not be treated as a health plan, insurance, or arrangement described in paragraph (1). .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 6. Periodic provider fees treated as medical care\n##### (a) In general\nSection 213(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(12) Periodic provider fees Periodic fees paid for a defined set of medical services provided on an as-needed basis shall be treated as amounts paid for medical care. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 7. Restoring lower penalty for nonqualified distributions\n##### (a) In general\nSection 223(e)(4)(A) of the Internal Revenue Code of 1986 is amended by striking 20 percent and inserting 10 percent .\n##### (b) Effective date\nThe amendments made by this section shall apply to distributions made in taxable years beginning after December 31, 2025.\n#### 8. Treatment of health care sharing ministries\n##### (a) Inclusion as medical expenses\nParagraph (2) of section 223(d) of the Internal Revenue Code of 1986, as amended by sections 4 and 5, is further amended by adding at the end the following new subparagraph:\n(E) Inclusion of health care sharing ministries The term qualified medical expenses shall include amounts paid by a member of a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof) for\u2014 (i) the sharing of medical expenses among members, and (ii) administrative fees of the ministry. .\n##### (b) Health care sharing ministry not To Be treated as health insurance\nSubsection (c) of section 223 of the Internal Revenue Code of 1986, as amended by sections 2 and 5, is further amended by adding at the end the following new paragraph:\n(5) Treatment of health care sharing ministries A health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof) shall not be treated as a health plan or insurance for purposes of this title. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 9. Health care sharing ministry fees treated as medical care\n##### (a) In general\nSection 213(d) of the Internal Revenue Code of 1986, as amended by section 6, is further amended by adding at the end the following new paragraph:\n(13) Health care sharing ministries Amounts paid for membership in a health care sharing ministry (as defined in section 5000A(d)(2)(B)(ii) without regard to subclause (IV) thereof) shall be treated as amounts paid for medical care. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-02-28",
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
        "actionDate": "2025-01-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "810",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Personalized Care Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-04-28T21:45:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119s276",
          "measure-number": "276",
          "measure-type": "s",
          "orig-publish-date": "2025-01-28",
          "originChamber": "SENATE",
          "update-date": "2025-05-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s276v00",
            "update-date": "2025-05-05"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Personalized Care Act of </strong><strong>2025</strong></p><p>This bill expands health saving account (HSA) eligibility, increases HSA contribution limits, and makes other HSA-related changes. The bill also expands the definition of medical care for purposes of the itemized tax deduction for unreimbursed medical expenses.</p><p>The bill eliminates the requirement that an individual must be covered by a high-deductible health plan to establish and contribute to an\u00a0HSA. Under the bill, an <em>eligible individual</em> is defined as (1) a health care sharing ministry participant, or (2) individual covered under</p><ul><li>a group or individual health plan;</li><li>health insurance (including a short-term limited duration and medical indemnity plan); or</li><li>a government plan (including Medicare Part A and B, Medicaid, the Children\u2019s Health Insurance Program, certain military and government employee health benefit programs, and the Indian Health Service and tribal organization programs).</li></ul><p>The bill increases annual\u00a0HSA contribution limits to $10,800 (from $4,300 in 2025) for self-only coverage and $29,500 (from $8,550 in 2025) for family coverage, adjusted annually for inflation.</p><p>The bill expands the qualified medical expenses that may be paid for with\u00a0HSA distributions to include health insurance payments (e.g., premiums), direct care fees, and certain amounts paid by health care sharing ministry participants.</p><p>The bill decreases the penalty to 10% (from 20%) for\u00a0nonqualified HSA distributions.\u00a0</p><p>Finally, under the bill, direct care fees and fees paid for membership in a health care sharing ministry qualify as medical care for purposes of the itemized tax deduction for\u00a0unreimbursed medical expenses.</p>"
        },
        "title": "Personalized Care Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s276.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Personalized Care Act of </strong><strong>2025</strong></p><p>This bill expands health saving account (HSA) eligibility, increases HSA contribution limits, and makes other HSA-related changes. The bill also expands the definition of medical care for purposes of the itemized tax deduction for unreimbursed medical expenses.</p><p>The bill eliminates the requirement that an individual must be covered by a high-deductible health plan to establish and contribute to an\u00a0HSA. Under the bill, an <em>eligible individual</em> is defined as (1) a health care sharing ministry participant, or (2) individual covered under</p><ul><li>a group or individual health plan;</li><li>health insurance (including a short-term limited duration and medical indemnity plan); or</li><li>a government plan (including Medicare Part A and B, Medicaid, the Children\u2019s Health Insurance Program, certain military and government employee health benefit programs, and the Indian Health Service and tribal organization programs).</li></ul><p>The bill increases annual\u00a0HSA contribution limits to $10,800 (from $4,300 in 2025) for self-only coverage and $29,500 (from $8,550 in 2025) for family coverage, adjusted annually for inflation.</p><p>The bill expands the qualified medical expenses that may be paid for with\u00a0HSA distributions to include health insurance payments (e.g., premiums), direct care fees, and certain amounts paid by health care sharing ministry participants.</p><p>The bill decreases the penalty to 10% (from 20%) for\u00a0nonqualified HSA distributions.\u00a0</p><p>Finally, under the bill, direct care fees and fees paid for membership in a health care sharing ministry qualify as medical care for purposes of the itemized tax deduction for\u00a0unreimbursed medical expenses.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s276"
    },
    "title": "Personalized Care Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Personalized Care Act of </strong><strong>2025</strong></p><p>This bill expands health saving account (HSA) eligibility, increases HSA contribution limits, and makes other HSA-related changes. The bill also expands the definition of medical care for purposes of the itemized tax deduction for unreimbursed medical expenses.</p><p>The bill eliminates the requirement that an individual must be covered by a high-deductible health plan to establish and contribute to an\u00a0HSA. Under the bill, an <em>eligible individual</em> is defined as (1) a health care sharing ministry participant, or (2) individual covered under</p><ul><li>a group or individual health plan;</li><li>health insurance (including a short-term limited duration and medical indemnity plan); or</li><li>a government plan (including Medicare Part A and B, Medicaid, the Children\u2019s Health Insurance Program, certain military and government employee health benefit programs, and the Indian Health Service and tribal organization programs).</li></ul><p>The bill increases annual\u00a0HSA contribution limits to $10,800 (from $4,300 in 2025) for self-only coverage and $29,500 (from $8,550 in 2025) for family coverage, adjusted annually for inflation.</p><p>The bill expands the qualified medical expenses that may be paid for with\u00a0HSA distributions to include health insurance payments (e.g., premiums), direct care fees, and certain amounts paid by health care sharing ministry participants.</p><p>The bill decreases the penalty to 10% (from 20%) for\u00a0nonqualified HSA distributions.\u00a0</p><p>Finally, under the bill, direct care fees and fees paid for membership in a health care sharing ministry qualify as medical care for purposes of the itemized tax deduction for\u00a0unreimbursed medical expenses.</p>",
      "updateDate": "2025-05-05",
      "versionCode": "id119s276"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s276is.xml"
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
      "title": "Personalized Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Personalized Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to expand and improve health savings accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:29Z"
    }
  ]
}
```
