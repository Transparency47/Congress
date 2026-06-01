# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1813?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1813
- Title: High-Quality Charter Schools Act
- Congress: 119
- Bill type: S
- Bill number: 1813
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-05-12T16:55:26Z
- Update date including text: 2026-05-12T16:55:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1813",
    "number": "1813",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001184",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Scott, Tim [R-SC]",
        "lastName": "Scott",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "High-Quality Charter Schools Act",
    "type": "S",
    "updateDate": "2026-05-12T16:55:26Z",
    "updateDateIncludingText": "2026-05-12T16:55:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-20",
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
      "actionDate": "2025-05-20",
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
          "date": "2026-03-19T14:00:28Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-20T18:31:43Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "LA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "AL"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1813is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1813\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mr. Scott of South Carolina introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations for the creation or expansion of charter schools.\n#### 1. Short title\nThis Act may be cited as the High-Quality Charter Schools Act .\n#### 2. Tax credit for contributions to eligible charter school organizations\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25E the following new section:\n25F. Contributions to eligible charter school organizations (a) Allowance of credit In the case of an individual who is a citizen or resident of the United States (as defined in section 7701(a)(9)), there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 75 percent of the amount of qualified contributions made by the taxpayer during the taxable year. (b) Amount of credit The credit allowed under subsection (a) in any taxable year shall not exceed an amount equal to the greater of\u2014 (1) 10 percent of the adjusted gross income of the taxpayer for the taxable year, or (2) $5,000. (c) Definitions For purposes of this section\u2014 (1) Charter school The term charter school has the meaning given such term in section 4310 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i ). (2) Eligible charter school organization (A) In general The term eligible charter school organization means an entity which\u2014 (i) is described in section 501(c)(3) and exempt from tax under section 501(a) and is not a private foundation, (ii) is a charter management organization (as defined in section 4310 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221i )), or a charter school, that\u2014 (I) (aa) has received a grant for the replication or expansion of high-quality charter schools under section 4305(b) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7221d(b) ), or (bb) manages or operates a charter school that has been supported under such a grant, or (II) has been selected by a State for eligibility under this section based on a determination by the State that the entity is in the highest 10 percent of charter management organizations (as so defined) or charter schools, as the case may be, for student performance in the State, (iii) separate from any other funds or contributions received by the entity, maintains and accounts for any contributions made by any person for the purpose of the creation or expansion of charter schools operated or managed by such entity, (iv) obtains from an independent certified public accountant annual financial and compliance audits, and (v) certifies to the Secretary (at such time, and in such form and manner, as the Secretary may prescribe) that the audit described in clause (iv) has been completed. (B) Independent certified public accountant For purposes of subparagraph (A), the term independent certified public accountant means, with respect to an organization, a certified public accountant who is not a person described in section 465(b)(3)(A) with respect to such organization or any employee of such organization. (3) Qualified contribution The term qualified contribution means a charitable contribution (as defined by section 170(c)) to an eligible charter school organization in the form of cash or marketable securities for the purpose of the creation or expansion of charter schools managed or operated by such organization. (d) Denial of double benefit Any qualified contribution for which a credit is allowed under this section shall not be taken into account as a charitable contribution for purposes of section 170. (e) Carryforward of unused credit (1) In general If the credit allowable under subsection (a) for any taxable year exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section, section 23, and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year following the fifth taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in first-out basis. (f) Application of volume cap (1) In general Subject to paragraph (2), a qualified contribution shall not be taken into account under this section if such contribution would result in the aggregate amount of credits claimed under this section exceeding the volume cap established under section 4 of the High-Quality Charter Schools Act . (2) State allocations For purposes of the allocation made to a State pursuant to subparagraph (A) of section 4(a)(1) of the High-Quality Charter Schools Act , if a qualified contribution made by an individual residing in such State would result in the aggregate amount of credits claimed under this section by individuals residing in such State exceeding the allocation made to such State pursuant to such subparagraph, such contribution shall only be taken into account under this section if such contribution does not result in the aggregate amount of credits claimed by individuals pursuant to subparagraph (B) of such section exceeding the amount made available pursuant to such subparagraph. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25E the following new item:\nSec. 25F. Contributions to eligible charter school organizations. .\n#### 3. Failure of eligible charter school organization to make expenditures\n##### (a) In general\nChapter 42 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subchapter:\nI Eligible Charter School Organizations Sec. 4969. Failure to expend receipts. 4969. Failure to expend receipts (a) In general In the case of any eligible charter school organization (as defined in section 25F(c)(2)) which has been determined by the Secretary to have failed to satisfy the requirement under subsection (b) for any taxable year, any contribution made to such organization during the first taxable year beginning after the date of such determination shall not be treated as a qualified contribution (as defined in section 25F(c)(3)) for purposes of section 25F. (b) Requirement The requirement described in this subsection is that the amount of qualified contributions of the eligible charter school organization for the taxable year which are expended before the expenditure deadline with respect to such receipts shall not be less than the required expenditure amount with respect to such taxable year. (c) Definitions For purposes of this section\u2014 (1) Required expenditure amount (A) In general The required expenditure amount with respect to a taxable year is the amount equal to 100 percent of qualified contributions for such taxable year\u2014 (i) reduced by the sum of such qualified contributions that are retained for reasonable administrative expenses for the taxable year or are carried to the succeeding taxable year under subparagraph (C), and (ii) increased by the amount of the carryover under subparagraph (C) from the preceding taxable year. (B) Safe harbor for reasonable administrative expenses For purposes of subparagraph (A)(i), if the percentage of total qualified contributions to an eligible charter school organization for a taxable year which are used for administrative purposes related to activities for the creation or expansion of charter schools (as defined in section 25F(c)(1)) operated or managed by such organization is equal to or less than 10 percent, such expenses shall be deemed to be reasonable for purposes of such subparagraph. (C) Carryover With respect to the amount of the total qualified contributions to an eligible charter school organization with respect to any taxable year, an amount not greater than 15 percent of such amount may, at the election of such organization, be carried to the succeeding taxable year. (2) Expenditures The term expenditures includes amounts which are formally committed but not expended. A formal commitment described in the preceding sentence may include qualified contributions set aside for the creation or expansion of charter schools operated or managed by such organization for more than one year. (3) Expenditure deadline The expenditure deadline with respect to qualified contributions for a taxable year is the first day of the fifth taxable year following the taxable year in which such qualified contributions are received by the eligible charter school organization. (4) Qualified contributions The term qualified contributions means contributions eligible for the credit under section 25F. .\n##### (b) Clerical amendment\nThe table of subchapters for chapter 42 of such Code is amended by adding at the end the following new item:\nSubchapter I. Eligible Charter School Organizations .\n#### 4. Volume cap\n##### (a) Allocation\n**(1) In general**\nFor purposes of section 25F(f) of the Internal Revenue Code of 1986 (as added by this Act), the volume cap applicable with respect to such section shall be $5,000,000,000 of tax credits for taxable years beginning in calendar year 2026 and each subsequent year thereafter, with such amount to be allocated as follows:\n**(A)**\n$10,000,000 of tax credits shall be allocated to each State (as defined in section 7701(a)(10) of the Internal Revenue Code of 1986), with such amount to be made available, in the manner described in subsection (b), for any individual residing in such State to claim the credit allowed under section 25F of the Internal Revenue Code of 1986 with respect to any qualified contributions (as defined in such section) made by such individual during any taxable year beginning during such calendar year.\n**(B)**\nWith respect to the amount remaining after the allocation under subparagraph (A), such amount (as adjusted pursuant to paragraph (3)) shall be made available, in the manner described in subsection (b), for any individual to claim the credit allowed under section 25F of the Internal Revenue Code of 1986 with respect to any qualified contributions made by such individual during any taxable year beginning during such calendar year.\n**(2) Carryover**\nThe amount of any allotment to a State under paragraph (1)(A) for any calendar year which is not claimed by taxpayers described in such paragraph during such calendar year shall be added to the allotment provided under paragraph (1)(B) for the subsequent calendar year.\n**(3) Increase in nationwide volume cap**\nFor purposes of paragraph (1)(B), if the Secretary determines during any calendar year that the amount of tax credits allowable under section 25F with respect to qualified contributions made during such calendar year is equal to or greater than 90 percent of the total amount made available under such paragraph for such calendar year, such amount shall be increased by an amount equal to 5 percent of the total amount made available under such paragraph as of January 1 of such calendar year, with such increase to remain in effect for the subsequent calendar year.\n##### (b) First-Come, first-Serve\nFor purposes of applying the volume cap under this section, such volume cap shall be applied based on a first-come, first-serve basis, as determined based on the date on which the taxpayer made the qualified contribution.\n##### (c) Real-Time information\nFor purposes of this section, the Secretary of the Treasury (or the Secretary's delegate) shall develop a system to track the amount of qualified contributions made during the calendar year for which a credit may be claimed under section 25F of the Internal Revenue Code of 1986, with such information to be updated in real time.\n#### 5. Organizational and parental autonomy\n##### (a) Prohibition of control over eligible charter school organizations\n**(1) In general**\nAn eligible charter school organization shall not, by virtue of participation under any provision of this Act or any amendment made by this Act, be regarded as acting on behalf of any governmental entity.\n**(2) Maximum freedom**\nTo the extent permissible by law, this Act, and any amendment made by this Act, shall be construed to allow eligible charter school organizations maximum freedom to provide for the needs of the students served by the charter schools operated or managed by the organization without governmental control.\n##### (b) Definitions\nFor purposes of this section, the terms charter school and eligible charter school organization shall have the same meanings given such terms under section 25F(c) of the Internal Revenue Code of 1986 (as added by section 2(a) of this Act).\n#### 6. Effective date\nThe amendments made by this Act shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-04-09",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2798",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "High-Quality Charter Schools Act",
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
            "name": "Charitable contributions",
            "updateDate": "2026-05-12T16:54:56Z"
          },
          {
            "name": "Elementary and secondary education",
            "updateDate": "2026-05-12T16:55:03Z"
          },
          {
            "name": "Income tax credits",
            "updateDate": "2026-05-12T16:55:10Z"
          },
          {
            "name": "Student aid and college costs",
            "updateDate": "2026-05-12T16:55:18Z"
          },
          {
            "name": "Tax-exempt organizations",
            "updateDate": "2026-05-12T16:55:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-06-06T20:38:08Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1813is.xml"
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
      "title": "High-Quality Charter Schools Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "High-Quality Charter Schools Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow a credit against tax for charitable donations for the creation or expansion of charter schools.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:26Z"
    }
  ]
}
```
