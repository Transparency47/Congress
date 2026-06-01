# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6183?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6183
- Title: To amend the Internal Revenue Code of 1986 to reform certain rules related to health savings accounts.
- Congress: 119
- Bill type: HR
- Bill number: 6183
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2025-12-10T09:05:43Z
- Update date including text: 2025-12-10T09:05:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6183",
    "number": "6183",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to reform certain rules related to health savings accounts.",
    "type": "HR",
    "updateDate": "2025-12-10T09:05:43Z",
    "updateDateIncludingText": "2025-12-10T09:05:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
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
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:07:35Z",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6183ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6183\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mr. Doggett introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to reform certain rules related to health savings accounts.\n#### 1. References\nExcept as otherwise expressly provided, whenever in this Act an amendment or repeal is expressed in terms of an amendment to, or repeal of, a section or other provision, the reference shall be considered to be made to a section or other provision of the Internal Revenue Code of 1986.\n#### 2. Repeal of exception to requirement that penalty-free distributions be for qualified medical expenses\n##### (a) In general\nSection 223(f)(4) is amended by striking subparagraph (C).\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after December 31, 2025.\n#### 3. Income limitation on deductible contributions to health savings accounts\n##### (a) In general\nSection 223(b) is amended by adding at the end the following new paragraph:\n(9) Limitation based on modified adjusted gross income (A) In general The amount otherwise allowable as a deduction under subsection (a) shall be reduced (but not below zero) by an amount which bears the same ratio to the amount so allowable (determined without regard to this paragraph) as\u2014 (i) the amount (if any) by which the taxpayer\u2019s modified adjusted gross income exceeds the applicable income threshold, bears to (ii) $40,000 ($20,000 in the case of a married individual filing a separate return). (B) Applicable income threshold For purposes of this paragraph, the term applicable income threshold means\u2014 (i) in the case of a joint return or surviving spouse (as defined in section 2(a)), $300,000, (ii) in the case of a head of household, $250,000, (iii) in the case of a married individual filing a separate return, $150,000, and (iv) in any other case, $200,000. (C) Modified adjusted gross income For purposes of this paragraph, the term modified adjusted gross income means adjusted gross income determined without regard to this section and sections 911, 931, and 933. .\n##### (b) Treatment of non-deductible contributions\n**(1) Rules for distribution**\nSection 223(f)(2) is amended is amended by striking shall be included in the gross income of such beneficiary. and inserting shall be included in the gross income of the beneficiary as provided in section 72. Rules similar to the rules of section 408(d)(2) shall apply for purposes of the preceding sentence. .\n**(2) Coordination with excise tax on excess contributions**\nSection 4973(g)(1) is amended by inserting (determined without regard to section 223(b)(9)) after section 223 .\n##### (c) Payroll taxes\n**(1) FICA**\nSection 3121(a) is amended by striking or at the end of paragraph (22), by striking the period at the end of paragraph (23) and inserting ; or , and by inserting afer paragraph (23) the following new paragraph:\n(24) (A) for purposes of section 3101, any payment excludable from the employee\u2019s gross income under section 106(d), and (B) for purposes of any other provision of this chapter (including section 3102), any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 106(d). .\n**(2) Railroad Retirement**\nSection 3231(e)(11) is amended to read as follows:\n(11) (A) for purposes of section 3201, any payment excludable from the employee\u2019s gross income under section 106(d), and (B) for purposes of any other provision of this chapter (including section 3202), any payment made to or for the benefit of an employee if at the time of such payment it is reasonable to believe that the employee will be able to exclude such payment from income under section 106(d); .\n##### (d) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n**(2) Payroll taxes**\nThe amendments made by subsection (c) shall apply to payments made after December 31, 2025.\n#### 4. Health savings account reimbursement of medical expenses limited to 2 years\n##### (a) In general\nSection 223(d)(2) is amended by adding at the end the following new subparagraph:\n(E) Reimbursements limited to 2 years An amount paid or distributed from a health savings account to reimburse the account beneficiary for a qualified medical expense shall not be treated as used to pay a qualified medical expense unless such distribution is made not later than 2 years after the date on which such reimbursed qualified medical expense was paid. .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid or distributed from a health savings account after December 31, 2025.\n#### 5. Requirement to substantiate distributions from health savings accounts that are for qualified medical expenses\n##### (a) In general\nSection 223(d)(2), as amended by the preceding provisions of this Act, is amended by adding at the end the following new subparagraph:\n(F) Substantiation requirement (i) In general An amount paid or distributed from a health savings account shall not be treated as used to pay a qualified medical expense unless such amount is substantiated as a qualified medical expense. (ii) Assessment required In the case of any expense with respect to which a provider\u2019s opinion is required to substantiate such expense as a qualified medical expense under clause (i), such opinion shall not constitute substantiation unless\u2014 (I) such opinion is based on an assessment conducted pursuant to a bona fide provider-patient relationship, (II) such assessment is conducted in-person or is an assessment of a type that generally accepted standards of medical practice do not require to be in-person, and (III) the expense is incurred for an item or service of a type that would be typically recommended under generally accepted standards of medical practice. (G) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this subparagraph. .\n##### (b) Determination by trustee\nSection 223(d)(1) is amended by adding at the end the following new subparagraph:\n(F) In the case of any amount paid or distributed from the trust, the trustee shall determine, consistent with the requirements of paragraph (2)(F), whether such amount has been substantiated as a qualified medical expense. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or distributed from a health savings account after December 31, 2025.\n#### 6. Certain expenses not treated as medical care\n##### (a) In general\nSection 223(d)(2), as amended by the preceding provisions of this Act, is amended by adding at the end the following new subparagraph:\n(G) Exclusions For purposes of this paragraph, the amounts paid for the following shall not be treated as paid for medical care: (i) Spa and beauty treatments. (ii) So much of any amounts paid for exercise equipment as exceed $500 in any taxable year. .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid or distributed from a health savings account after December 31, 2025.\n#### 7. Excise tax on excessive health savings account fees\n##### (a) In general\nSubtitle D is amended by adding at the end the following new chapter:\n50B Excessive health savings account fees Sec. 5000E. Excessive health savings account fees. 5000E. Excessive health savings account fees (a) In general There is hereby imposed on the trustee of any health savings account which charges any excessive health savings account fee a tax equal to the excess of\u2014 (1) the amount of such fee, over (2) the reasonable amount of such fee as determined under subsection (b)(3). (b) Excessive health saving account fee For purposes of this section\u2014 (1) Excessive health savings account fee The term excessive health savings account fee means any covered health savings account fee if such fee exceeds the reasonable amount of such fee as determined under paragraph (3). (2) Covered health savings account fee The term covered health savings account fee means any of the following if charged in connection with a health savings account: maintenance fees; transfer fees; fees for paper statements, checks, or replacement cards; withdrawal fees; fees for insufficient funds; fees to ensure that fees do not exceed earnings or account balance; and such other fees or charges as the Secretary may identify for purposes of this paragraph. (3) Reasonable fees With respect to each category of fees described in paragraph (2) and such additional categories or subcategories as the Secretary may provide, the Secretary shall determine the reasonable amount of such fee. (c) Health saving account For purposes of this section, the term health savings account has the meaning given such term in section 223. .\n##### (b) Reporting\nSubpart A of part III of subchapter A of chapter 61 is amended by inserting after section 6039L the following new section:\n6039M. Information regarding health savings account fees (a) In general Each trustee of a health savings account which charges any covered health savings account fee during any calendar year shall, for such calendar year, make a return at such time and in such manner as the Secretary may provide setting forth the information described in subsection (b) and such other information as the Secretary may require. (b) Information (1) In general Each return under subsection (a) shall include, with respect to each category of fee charged, a description of such fee, the number of such fees charged, and the aggregate amount of such fees charged. (2) Separately stated categories The information described in paragraph (1) shall be separately stated based on such demographic or other characteristics as the Secretary may provide. (c) Definitions Terms used in this section which are also used in section 5000E shall have the same meaning as when used in section 5000E. .\n##### (c) Clerical amendments\n**(1)**\nThe table of chapters for subtitle D is amended by adding at the end the following new item:\nChapter 50B\u2014Excessive health savings account fees .\n**(2)**\nThe table of sections for subpart A of part III of subchapter A of chapter 61 is amended by inserting after the item relating to section 6039L the following new item:\nSec. 6039M. Information regarding health savings account fees. .\n##### (d) Effective date\nThe amendments made by this section shall apply to fees charged after December 31, 2025.\n#### 8. Reporting of earnings on cash balances of health savings accounts\n##### (a) In general\nSection 223(h) is amended by adding at the end the following: The reports under paragraph (1) shall include a statement specifying the average yield on cash balances in the health savings account of the account beneficiary for the period covered by the report and a statement of the national average yield on savings account balances for such period (determined in such manner as the Secretary may provide). .\n##### (b) Effective date\nThe amendment made by this section shall apply to reports with respect to periods beginning after December 31, 2025.",
      "versionDate": "2025-11-20",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-11-21T16:33:10Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6183ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to reform certain rules related to health savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-21T13:18:21Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to reform certain rules related to health savings accounts.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:04:15Z"
    }
  ]
}
```
