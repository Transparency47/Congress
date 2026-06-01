# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/464?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/464
- Title: Skills Investment Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 464
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2026-01-10T06:59:16Z
- Update date including text: 2026-01-10T06:59:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-01-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H159)
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- 2025-01-15 - IntroReferral: Sponsor introductory remarks on measure. (CR H159)

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/464",
    "number": "464",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Skills Investment Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-10T06:59:16Z",
    "updateDateIncludingText": "2026-01-10T06:59:16Z"
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
      "actionCode": "B00100",
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H159)",
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
          "date": "2025-01-15T15:00:15Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "OR"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "IL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr464ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 464\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Thompson of Pennsylvania (for himself, Ms. Bonamici , Mr. Fitzpatrick , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide for lifelong learning accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Skills Investment Act of 2025 .\n#### 2. Coverdell lifelong learning accounts\n##### (a) In general\n**(1) Renaming of Coverdell education savings accounts**\nSection 530 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby striking Coverdell education savings account each place it appears and inserting Coverdell lifelong learning account ; and\n**(B)**\nby striking Coverdell education savings accounts in the heading and inserting Coverdell lifelong learning accounts .\n**(2) Conforming amendments**\n**(A)**\nSection 26(b)(2)(E) of the Internal Revenue Code of 1986 is amended by striking Coverdell education savings accounts and inserting Coverdell lifelong learning accounts .\n**(B)**\nSection 72(e)(9) of such Code is amended\u2014\n**(i)**\nby striking Coverdell education savings account and inserting Coverdell lifelong learning account ; and\n**(ii)**\nby striking Coverdell education savings accounts in the heading and inserting Coverdell lifelong learning account s .\n**(C)**\nSection 135(c)(2)(C) of such Code is amended\u2014\n**(i)**\nby striking Coverdell education savings account and inserting Coverdell lifelong learning account ; and\n**(ii)**\nby striking Coverdell education savings accounts in the heading and inserting Coverdell lifelong learning accounts .\n**(D)**\nSection 408A(e)(2)(A)(ii) of such Code is amended by striking Coverdell education savings account and inserting Coverdell lifelong learning account .\n**(E)**\nSection 529(c) of such Code is amended\u2014\n**(i)**\nby striking Coverdell education savings accounts in the heading of paragraph (3)(B)(vi) and inserting Coverdell lifelong learning account ; and\n**(ii)**\nby striking Coverdell education savings account in paragraph (6) and inserting Coverdell lifelong learning account .\n**(F)**\nSection 877A(e)(2) of such Code is amended by striking Coverdell education savings account and inserting Coverdell lifelong learning account .\n**(G)**\nSection 4973 of such Code is amended\u2014\n**(i)**\nby striking Coverdell education savings account each place it appears in subsections (a)(4) and (e)(2)(A) and inserting Coverdell lifelong learning account ;\n**(ii)**\nby striking Coverdell education savings accounts in subsection (e)(1) and inserting Coverdell lifelong learning accounts ; and\n**(iii)**\nby striking Coverdell education savings accounts in the heading of subsection (e) and inserting Coverdell lifelong learning account .\n**(H)**\nSection 4975 of such Code is amended\u2014\n**(i)**\nby striking Coverdell education savings account each place it appears in subsections (c)(5) and (e)(1)(F) and inserting Coverdell lifelong learning account ; and\n**(ii)**\nby striking Coverdell education savings accounts in the heading of subsection (c)(5) and inserting Coverdell lifelong learning accounts .\n**(I)**\nSection 6693(a)(2)(F) of such Code is amended by striking Coverdell education savings accounts and inserting Coverdell lifelong learning accounts .\n**(J)**\nThe table of sections for part VIII of subchapter F of chapter 1 of such Code is amended by striking Coverdell education savings accounts and inserting Coverdell lifelong learning accounts .\n**(3) Treatment of existing accounts**\nFor purposes of section 530(b)(1) of the Internal Revenue Code of 1986, any account established before January 1, 2024, and designated as a Coverdell education savings account shall be deemed to have been designated as a Coverdell lifelong learning account.\n##### (b) Expanded use of accounts\n**(1) Eligible expenses**\n**(A) In general**\nSection 530(b)(2)(A) of the Internal Revenue Code of 1986 is amended by striking and at the end of clause (i), by striking the period at the end of clause (ii) and inserting , and , and by adding at the end the following new clause:\n(iii) qualified educational or skill development expenses (as defined in paragraph (5)). .\n**(B) Qualified educational or skill development expenses**\nSection 530(b) of such Code is amended by adding at the end the following new paragraph:\n(5) Qualified educational or skill development expenses The term qualified educational or skill development expenses means\u2014 (A) expenses paid or incurred\u2014 (i) after the beneficiary attains age 16, and (ii) for participation or enrollment of the beneficiary in services or activities that are\u2014 (I) training services described in section 134(c)(3)(D) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3174(c)(3)(D) ) that are offered by a provider included on the list of eligible providers of training services described in section 122 of such Act ( 29 U.S.C. 3152 ), (II) career and technical education activities defined in section 3 of the Carl D. Perkins Career and Technical Education Act of 2006 ( 20 U.S.C. 2302 ) that are offered through an eligible institution (as defined in such section), (III) career services described in clauses (iii), (iv), and (xi) of section 134(c)(2)(A) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3174(c)(2)(A) ) that are provided by providers eligible under section 134(c)(2)(C) of such Act, (IV) youth activities described in section 129(c)(2) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3164(c)(2) ) that are provided by eligible providers of youth workforce investment activities under section 123 of such Act, or (V) adult education and literacy activities, as defined in section 203 of the Adult Education and Family Literacy Act ( 29 U.S.C. 3272 ), that are provided by eligible providers of adult education and literacy activities under section 231 of such Act ( 29 U.S.C. 3321 ), (B) expenses for transportation required for or provided by any of the services or activities described in subparagraph (A), (C) expenses for testing necessary for enrollment in, or certification in connection with, services or activities described in subparagraph (A), or (D) expenses for the purchase of any computer software (as defined by section 197(e)(3)(B)), computer or peripheral equipment (as defined by section 168(i)(2)(B)), fiber optic cable related to computer use, internet access and related services, if such software, equipment, or services are to be used by the beneficiary for services or activities described in subparagraph (A) during any of the years the beneficiary is participating in or enrolled in any of the services or activities described in subparagraph (A). .\n##### (c) Modification of rules relating to age restrictions and contributions\n**(1) $10,000 account limit after age 30**\n**(A) In general**\nSubparagraph (E) of section 530(b)(1) of the Internal Revenue Code of 1986 is amended by inserting in excess of $10,000 after any balance to the credit of the designated beneficiary .\n**(B) Contribution limit**\nSubparagraph (A) of section 530(b)(1) of such Code is amended by striking or at the end of clause (ii), by striking the period at the end of clause (iii) and inserting , or , and by adding at the end the following new clause:\n(iv) in the case of a beneficiary who is over the age of 30, if such contribution would result in the balance of the account exceeding $10,000. .\n**(2) Increased age limit for contributions**\nClause (ii) of section 530(b)(1)(A) of the Internal Revenue Code of 1986 is amended by striking age 18 and inserting age 70 .\n**(3) Increased contribution limitation for individuals over age 30**\n**(A) In general**\nSection 530(b)(1)(A)(iii) of the Internal Revenue Code of 1986 is amended by inserting ($4,000 in the case of an account the designated beneficiary of which has attained age of 30 before the end of the taxable year) after $2,000 .\n**(B) Conforming amendment**\nSection 4973(e)(1)(A) of such Code is amended by striking $2,000 and inserting the limitation applicable under section 530(b)(1)(A)(iii) .\n**(4) No change in beneficiary after age 30**\nParagraph (6) of section 530(d) of the Internal Revenue Code of 1986 is amended by striking shall not be treated as a distribution for purposes of paragraph (1) if the new beneficiary and inserting\nshall not be treated as a distribution for purposes of paragraph (1) if\u2014 (A) the old beneficiary has not attained age 30 before the date of the change in beneficiary, and (B) the new beneficiary .\n##### (d) Credit for employer contributions\n**(1) In general**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Employee educational skills and development expenses (a) General rule For purposes of section 38, the employee educational skills and development contribution credit determined under this section for any taxable year is 25 percent of the nonelective contributions made by the taxpayer during the taxable year to a Coverdell lifelong learning account (as defined in section 530(b)) the designated beneficiary of which is an employee of the taxpayer. (b) Special rules and definitions For purposes of this section\u2014 (1) Employee (A) Certain employees excluded The term employee shall not include\u2014 (i) an employee within the meaning of section 401(c)(1), (ii) any 2-percent shareholder (as defined in section 1372(b)) of an S corporation, (iii) any 5-percent owner (as defined in section 416(i)(1)(B)(i)) of taxpayer, or (iv) any individual who bears any of the relationships described in subparagraphs (A) through (G) of section 152(d)(2) to, or is a dependent described in section 152(d)(2)(H) of, an individual described in clause (i), (ii), or (iii). (B) Leased employees The term employee shall include a leased employee within the meaning of section 414(n). (2) Nonelective contribution The term nonelective contribution means an employer contribution other than an employer contribution pursuant to a salary reduction arrangement. (3) Aggregation and other rules made applicable (A) Aggregation rules All employers treated as a single employer under subsection (b), (c), (m), or (o) of section 414 shall be treated as a single employer for purposes of this section. (B) Other rules Rules similar to the rules of subsections (c), (d), and (e) of section 52 shall apply. .\n**(2) Credit treated as part of general business credit**\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the employee educational skills and development contribution credit determined under section 45BB(a). .\n**(3) Clerical amendment**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 45BB. Employee educational skills and development expenses. .\n##### (e) Allowance of deduction for beneficiary\n**(1) In general**\nPart VIII of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 224 as section 225 and by inserting after section 223 the following new section:\n224. Coverdell lifelong learning account contributions (a) In general In the case of an individual who\u2014 (1) is the designated beneficiary of a Coverdell lifelong learning account (as defined in section 530(b)(1)), and (2) has attained the age of 18 before the close of the taxable year, there shall be allowed as a deduction an amount equal to the contributions for the taxable year by or on behalf of such individual to the account described in paragraph (1). (b) Recontributed amounts No deduction shall be allowed under this section with respect to a rollover contribution described in section 530(d)(5). .\n**(2) Increase in additional tax**\n**(A) Increase**\n**(i) In general**\nSection 530(d)(4)(A) of the Internal Revenue Code of 1986 is amended by striking 10 percent and inserting 20 percent .\n**(ii) Conforming amendment**\nSection 529(c)(6) of such Code is amended by inserting , except that 10 percent shall be substituted for 20 percent in subparagraph (A) thereof before the period at the end of the first sentence.\n**(B) Modification of tax treatment of deductible contributions**\nParagraph (1) of section 530(d) of such Code is amended to read as follows:\n(1) Inclusion in gross income (A) In general Any distribution shall be includible in the gross income of the distributee as follows: (i) So much of the distribution as is equal to or less than the deductible amount shall be fully included in gross income. (ii) So much of the distribution which exceeds the deductible amount shall be included in gross income in the manner as provided in section 72 (determined by applying such section without regard to any amounts to which clause (i) applies). (B) Deductible amount For purposes of this paragraph, the term deductible amount means the excess of\u2014 (i) the sum of contributions to the account for which a deduction was allowed under section 224 in such year and any preceding taxable year, over (ii) the amount of distributions to which subparagraph (A)(i) applied to in any preceding taxable year. .\n**(3) Clerical amendment**\nThe table of sections for part VIII of subchapter B of chapter 1 of such Code is amended by redesignating the item relating to section 224 as relating to section 225 and by inserting after the item relating to section 223 the following new item:\nSec. 224. Coverdell lifelong learning account contributions. .\n##### (f) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall take effect on January 1, 2026.\n**(2) Eligible expenses**\nThe amendments made by subsection (b) shall apply to distributions made after December 31, 2025.\n**(3) Contributions**\nThe amendments made by paragraphs (1)(B) and (2) of subsection (c) shall apply to contributions made after December 31, 2025.\n**(4) Employer contribution credit and beneficiary deductions**\nThe amendments made by subsections (d) and (e) shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3217",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Skills Investment Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-02-19T19:12:07Z"
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
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr464ih.xml"
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
      "title": "Skills Investment Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T13:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Skills Investment Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T13:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide for lifelong learning accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T13:33:24Z"
    }
  ]
}
```
