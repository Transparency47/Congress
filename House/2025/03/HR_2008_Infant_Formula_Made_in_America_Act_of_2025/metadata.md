# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2008?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2008
- Title: Infant Formula Made in America Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2008
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-12-19T09:07:22Z
- Update date including text: 2025-12-19T09:07:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2008",
    "number": "2008",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Infant Formula Made in America Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:22Z",
    "updateDateIncludingText": "2025-12-19T09:07:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:07:10Z",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CT"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "OH"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2008ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2008\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Nunn of Iowa (for himself, Ms. Houlahan , and Ms. DeLauro ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow an investment credit for certain domestic infant formula manufacturing projects and to allow a domestic production credit for certain infant formula.\n#### 1. Short title\nThis Act may be cited as the Infant Formula Made in America Act of 2025 .\n#### 2. Domestic infant formula manufacturing investment credit\n##### (a) In general\nSubpart E of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 48E the following new section:\n48F. Domestic infant formula manufacturing investment credit (a) In general For purposes of section 46, in the case of an eligible taxpayer, the domestic infant formula manufacturing credit for any taxable year is an amount equal to 30 percent of the qualified investment for such taxable year. (b) Qualified investment (1) In general For purposes of this section, the qualified investment for any taxable year is the basis of eligible property placed in service by the taxpayer during such taxable year which is part of a qualifying infant formula manufacturing project. (2) Certain qualified progress expenditures rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of this section. (3) Limitation The amount which is treated as the qualified investment for all taxable years with respect to any qualifying infant formula manufacturing project shall not exceed the amount designated by the Secretary as eligible for the credit. (c) Definitions For purposes of this section\u2014 (1) Eligible taxpayer (A) In general For purposes of this section, the term eligible taxpayer means a taxpayer if such taxpayer\u2019s total global revenue for the calendar year that precedes the calendar year in which the taxpayer submits an application under subsection (d)(1)(A) does not exceed $750,000,000. (B) Aggregation rules For purposes of this paragraph, all persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single taxpayer. (2) Qualifying infant formula manufacturing project The term qualifying infant formula manufacturing project means a project, any portion of the qualified investment of which is certified by the Secretary under subsection (d) as eligible for a credit under this section, which re-equips, expands, or establishes a facility for the manufacture of eligible infant formula. (3) Eligible property The term eligible property means any property\u2014 (A) which is necessary for the manufacture of eligible infant formula, (B) which is\u2014 (i) tangible personal property, or (ii) other tangible property (not including a building or its structural components), but only if such property is used as an integral part of a facility described in paragraph (2), and (C) with respect to which depreciation (or amortization in lieu of depreciation) is allowable. (4) Eligible infant formula The term eligible infant formula means infant formula that\u2014 (A) may lawfully be sold in the United States, and (B) is manufactured in the United States. (d) Certification (1) In general (A) Establishment Not later than 180 days after the date of the enactment of this section, the Secretary shall establish a qualifying infant formula manufacturing project program to consider and award certifications for qualified investments eligible for credits under this section to qualifying infant formula manufacturing projects. (B) Application period Each applicant for certification under this paragraph shall submit an application\u2014 (i) certifying that not less than 50 percent of the eligible infant formula manufactured using the eligible property to which such application relates during the 1-year period beginning on the date on which the qualifying infant formula manufacturing project is placed in service shall be sold for use in the United States, and (ii) containing such information as the Secretary shall require. (C) Time to meet criteria for certification Each applicant for certification shall have 1 year from the date of acceptance by the Secretary of the application during which to provide to the Secretary evidence that the requirements of the certification have been met. (D) Period of issuance An applicant which receives a certification shall have 3 years from the date of issuance of the certification in order to place the project in service and if such project is not placed in service by that time period, then the certification shall no longer be valid. (2) Limitations (A) Project amount The amount of credit that may be allocated under paragraph (1) shall not exceed $150,000,000. (B) Aggregate amount The total amount of credits that may be allocated under paragraph (1) shall not exceed $750,000,000. (C) Sunset The Secretary may not allocate any credit dollar amount with respect to any project that commences construction after the date that is 10 years after the date of the enactment of this section. (3) Review and redistribution (A) Review Not later than 4 years after the date of enactment of this section, the Secretary shall review the credits allocated under this section as of such date. (B) Redistribution The Secretary may reallocate credits awarded under this section if the Secretary determines that\u2014 (i) there is an insufficient quantity of qualifying applications for certification pending at the time of the review, or (ii) any certification made pursuant to paragraph (1) has been revoked pursuant to paragraph (1)(B) because the project subject to the certification has been delayed as a result of third party opposition or litigation to the proposed project. (C) Reallocation If the Secretary determines that credits under this section are available for reallocation pursuant to the requirements set forth in subparagraph (B), the Secretary is authorized to conduct an additional program for applications for certification. (4) Disclosure of allocations The Secretary shall, upon making a certification under this subsection, publicly disclose the identity of the applicant and the amount of the credit with respect to such applicant. (e) Recapture (1) In general If during the recapture period there is a recapture event, then the tax imposed by this chapter for the taxable year in which such recapture period ends shall be increased by the sum of\u2014 (A) the aggregate decrease in the credits allowed to the taxpayer under section 38 for all prior taxable years which would have resulted if no credit had been determined under this section with respect to the qualifying infant formula manufacturing project, plus (B) interest at the underpayment rate established under section 6621 on the amount determined under subparagraph (A) for each prior taxable year for the period beginning on the due date for filing the return for the prior taxable year involved. (2) Recapture event For purposes of this subsection, the term recapture event means\u2014 (A) a failure by the taxpayer to meet the requirements of the certification made by the taxpayer under subsection (d)(1)(A)(i), or (B) any property with respect to which an allocation was made under this section ceases to be eligible property which is part of a qualifying infant formula manufacturing project. (3) Recapture period For purposes of this subsection, the term recapture period means the 1-year period beginning on the date on which a qualifying infant formula manufacturing project with respect to which an allocation is made under this section is placed in service. (4) No deduction for interest No deduction shall be allowed under this chapter for interest described in paragraph (1)(B). (5) Special rules (A) Tax benefit rule The tax for the taxable year shall be increased under paragraph (1) only with respect to credits allowed by reason of this section which were used to reduce tax liability. In the case of credits not so used to reduce tax liability, the carryforwards and carrybacks under section 39 shall be appropriately adjusted. (B) No credits against tax Any increase in tax under this subsection shall not be treated as a tax imposed by this chapter for purposes of determining the amount of any credit under this chapter or for purposes of section 55. (f) Coordination with rehabilitation credit The qualified investment with respect to any qualifying infant formula manufacturing project for any taxable year shall not include that portion of the basis of any project which is attributable to qualified rehabilitation expenditures (as defined in section 47(c)(2)). (g) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section, including regulations providing for the appropriate conversion of quantities of liquid concentrate eligible infant formula to pounds of dry eligible formula. .\n##### (b) Inclusion in investment credit\nSection 46 of such Code is amended\u2014\n**(1)**\nin paragraph (5) by striking and at the end,\n**(2)**\nin paragraph (6), by striking the period and inserting , and , and\n**(3)**\nby adding after paragraph (6) the following new paragraph:\n(7) the domestic infant formula manufacturing investment credit. .\n##### (c) Credit made transferable\nSection 6418(f)(1) of such Code is amended by adding at the end the following new clause:\n(xii) The domestic infant formula manufacturing investment credit determined under section 48F. .\n##### (d) Elective payment of credit\nSection 6417(b) of such Code is amended by adding at the end the following new paragraph:\n(13) The domestic infant formula manufacturing investment credit determined under section 48F. .\n##### (e) Certain nonrecourse financing excluded from credit base\nSection 49(a)(1)(C) of such Code is amended by striking and at the end of clause (v), by striking the period at the end of clause (vi) and inserting , and , and by adding at the end the following new clause:\n(vii) the basis of any eligible property (as defined in section 48F(c)(3)) which is part of a qualifying infant formula manufacturing project under section 48F. .\n##### (f) Clerical amendment\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 48E the following new item:\nSec. 48F. Domestic infant formula manufacturing investment credit. .\n##### (g) Effective date\nThe amendments made by this section shall apply to projects the construction of which commences after the date of the enactment of this Act.\n#### 3. Infant formula production credit\n##### (a) In general\nSubpart D of part IV of subchapter A of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Infant formula production credit (a) In general In the case of a qualified taxpayer, for purposes of section 38, the infant formula production credit for any taxable year is an amount equal to the product of\u2014 (1) the amount in pounds (determined consistent with regulations issued under section 48F(g) with respect to liquid concentrate) of eligible infant formula manufactured by such taxpayer and sold for use in the United States during such taxable year, multiplied by (2) $2. (b) Qualified taxpayer For purposes of this section, the term qualified taxpayer means, with respect to a taxable year\u2014 (1) a taxpayer if such taxpayer\u2019s total global revenue for the preceding taxable year does not exceed $750,000,000, or (2) a taxpayer to whom a credit was allowed under this section in the preceding taxable year. (c) Eligible infant formula defined For purposes of this section, the term eligible infant formula has the meaning given such term in section 48F. (d) Limitations (1) Maximum amount of formula For purposes of determining the amount of the credit under subsection (a), the amount of eligible infant formula determined under subsection (a) with respect to any taxable year shall not exceed 18,000,000 pounds. (2) 5-year limitation No credit shall be allowed under subsection (a) to a taxpayer for a taxable year unless\u2014 (A) no credit has been allowed to such taxpayer in any prior taxable year, or (B) such taxable year occurs during the 5 taxable year period beginning on the first day of the first taxable year for which a credit was allowed under subsection (a) to such taxpayer. (e) Aggregation rules For purposes of this section, all persons which are treated as a single employer under subsections (a) and (b) of section 52 shall be treated as a single taxpayer. (f) Coordination with investment credit Infant formula produced at a facility with respect to which a credit was allowed under section 48F shall not be taken into account for purposes of subsection (a). .\n##### (b) Credit made transferable\nSection 6418(f)(1) of such Code (as amended by section 2) is amended by adding at the end the following new clause:\n(xiii) The infant formula production credit determined under section 45BB. .\n##### (c) Elective payment of credit\nSection 6417(b) of such Code (as amended by section 2) is amended by adding at the end the following new paragraph:\n(14) The infant formula production credit determined under section 45BB. .\n##### (d) Credit allowed as part of general business credit\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the infant formula production credit determined under section 45BB(a). .\n##### (e) Clerical amendment\nThe table of sections for subpart D of part IV of subchapter A of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Infant formula production credit. .\n##### (f) Effective date\nThe amendments made by this section shall apply to formula manufactured after the date of the enactment of this Act.",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-05-08T19:00:17Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2008ih.xml"
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
      "title": "Infant Formula Made in America Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Infant Formula Made in America Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow an investment credit for certain domestic infant formula manufacturing projects and to allow a domestic production credit for certain infant formula.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:24Z"
    }
  ]
}
```
