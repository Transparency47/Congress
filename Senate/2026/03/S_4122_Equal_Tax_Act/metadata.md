# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4122?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4122
- Title: Equal Tax Act
- Congress: 119
- Bill type: S
- Bill number: 4122
- Origin chamber: Senate
- Introduced date: 2026-03-17
- Update date: 2026-03-31T21:35:34Z
- Update date including text: 2026-03-31T21:35:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-17: Introduced in Senate
- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-17: Introduced in Senate

## Actions

- 2026-03-17 - IntroReferral: Introduced in Senate
- 2026-03-17 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4122",
    "number": "4122",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Equal Tax Act",
    "type": "S",
    "updateDate": "2026-03-31T21:35:34Z",
    "updateDateIncludingText": "2026-03-31T21:35:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-17",
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
      "actionDate": "2026-03-17",
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
          "date": "2026-03-17T21:52:13Z",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-17",
      "state": "VT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "OR"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4122is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4122\nIN THE SENATE OF THE UNITED STATES\nMarch 17, 2026 Mr. Markey (for himself, Mr. Sanders , Mr. Merkley , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to equalize treatment of capital gains and earned income.\n#### 1. Short title\nThis Act may be cited as the Equal Tax Act .\n#### 2. Preferential rates for dividends and capital gains limited to incomes of $1,000,000 or less\n##### (a) In general\nSection 1(h) of the Internal Revenue Code of 1986 is amended by inserting on so much of such gain as does not cause the taxable income of the taxpayer to exceed $1,000,000 (computed after taking into account all other taxable income of the taxpayer) after the tax imposed by this section for such taxable year .\n##### (b) Treatment of qualifying family farm or business\nSection 1(h) of such Code, as amended by subsection (a), is further amended by inserting and without regard to gain realized from the transfer by gift or bequest of a qualifying family farm or business described in section 139M(c) after all other taxable income of the taxpayer .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.\n#### 3. Deemed realization of capital gains at time of gift or death\n##### (a) Treatment as sale\n**(1) In general**\nPart IV of subchapter P of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n1261. Gains from certain property transferred by gift or upon death (a) In general Any property which is transferred by gift or at death shall be treated as sold for its fair market value on the date of such gift or death. (b) Exceptions (1) Spouse or surviving spouse This section shall not apply to a transfer of property to the spouse or surviving spouse of the transferor (or to a qualified spousal trust). (2) Certain tangible personal property In the case of tangible personal property, this section shall only apply to the following: (A) Property held in connection with a trade or business. (B) Property held for investment. (C) Collectibles (as defined in section 408(m) (determined without regard to paragraph (3) thereof)). (3) Charitable contributions This section shall not apply to any transfer to an organization described in section 170(c). (c) Special rules for trusts (1) Certain grantor trusts In the case of any property which\u2014 (A) is held in a trust of which the grantor or another person is treated as the owner under subpart E of part I of subchapter J of chapter 1, and (B) is includible in the gross estate of the grantor or such other person under chapter 11, such property shall be treated as transferred under subsection (a) when the grantor or such other person ceases to be treated as the owner of such property, or such property ceases to be includible in the gross estate of the grantor or such other person (including by reason of the death of the grantor or such other person, or the distribution of such property to a person other than the grantor or such other person). (2) Other trusts In the case of any property held in trust and not described in paragraph (1), such property shall be treated as transferred under subsection (a) upon the transfer of such property to a trust. (3) Transfers from and modifications of trusts The Secretary may by regulation prescribe such rules to treat the modification of the terms of a trust or the transfer or distribution of trust assets (including to another trust) as a transfer described in subsection (a) as are necessary or appropriate to prevent the avoidance of this section. (4) Generation-skipping trusts At the end of each 30-year period for which any property is continuously held in trust (other than property described in paragraph (1)), such property shall be treated as transferred pursuant to subsection (a). (5) Qualifying spousal trust (A) In general The property of a qualifying spousal trust shall be treated as transferred under subsection (a)\u2014 (i) upon the death of the spousal beneficiary, (ii) upon the distribution of such property from such trust to any person other than the spousal beneficiary, or (iii) at such time such property ceases to be held by a qualifying spousal trust. (B) Qualifying spousal trust For purposes of this section, a trust is a qualifying spousal trust if\u2014 (i) the sole beneficiary of such trust is the spouse, or surviving spouse of the transferor, or (ii) such spouse or surviving spouse is the sole life tenant, or sole income beneficiary, of such trust. (d) Exclusion of certain gifts In the case of gifts (other than gifts of future interests in property) made to any person during the taxable year, so much of the dollar amount of such gifts to such person as does not exceed the amount in effect for the calendar year under section 2503(b) in which the taxable year begins shall not be taken into account under subsection (a) for such taxable year. Where there has been a transfer to any person of a present interest in property, the possibility that such interest may be diminished by the exercise of a power shall be disregarded in applying this subsection, if no part of such interest will at any time pass to any other person. (e) Regulations The Secretary shall prescribe such regulations as may be necessary to prevent the avoidance of the purposes of this section. .\n**(2) Clerical amendment**\nThe table of sections for part IV of subchapter P of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 1261. Gains from certain property transferred by gift or upon death. .\n##### (b) Coordination of related party loss rules\nSection 267 of such Code is amended by adding at the end the following new subsection:\n(h) Property treated as sold at death Subsection (a)(1) shall not apply to any property that is transferred at death and treated as sold under section 1261. .\n##### (c) Treatment of basis for gifts and bequests to which tax applies\n**(1) Elimination of carryover basis for gifts**\nSection 1015(a) of such Code is amended\u2014\n**(A)**\nby striking If the property and inserting the following:\n(1) Gifts before January 1, 2027 If the property ;\n**(B)**\nby inserting , and before January 1, 2027 after after December 31, 1920 ; and\n**(C)**\nby adding at the end the following new paragraph:\n(2) Gifts after December 31, 2026 If the property was acquired by gift after December 31, 2026, the basis shall be the fair market value of such property at the time of the gift. .\n**(2) Rules for transfers between spouses**\n**(A) In general**\nSection 1041(b) of such Code is amended to read as follows:\n(b) Transferee has transferor\u2019s basis In the case of any transfer of property described in subsection (a), the basis of the transferee in the property shall be the adjusted basis of the transferor. .\n**(B) Transfers at death**\nSection 1041(a) of such Code is amended by inserting (including at death) after transfer of property .\n**(C) Conforming amendments**\n**(i)**\nSection 1014 of such Code is amended by adding at the end the following new subsection:\n(g) Property acquired from decedent spouse In the case of property which passes from the decedent to (or in trust for the benefit of) the decedent\u2019s surviving spouse in a transfer described in section 1041(a)(1), the basis of such property in the hands of the transferee shall be determined under section 1041(b) and not this section. .\n**(ii)**\nSection 1015(e) of such Code is amended by striking 1041(b)(2) and inserting 1041(b) .\n**(3) Basis must be consistent with gains recognized in deemed realization**\n**(A) Property acquired from decedent**\nSection 1014 of such Code, as amended by the preceding provisions of this Act, is amended by adding at the end the following new subsection:\n(h) Basis must be consistent with gains recognized in deemed realization The basis of any property to which subsection (a) applies shall not exceed the amount for which the property was treated as sold under section 1261. .\n**(B) Property acquired by gift**\nSection 1015 of such Code is amended by adding at the end the following new subsection:\n(f) Basis must be consistent with gains recognized in deemed realization The basis of any property to which subsection (a)(2) applies shall not exceed the amount for which the property was treated as sold under section 1261. .\n##### (d) Conforming amendments\n**(1)**\nSection 7477(a) of such Code is amended by striking chapter 12 and inserting chapter 1 or 12 .\n**(2)**\nSection 7517(a) of such Code is amended by striking chapter 11 and inserting chapter 1, 11 .\n##### (e) Effective date\nThe amendments made by this section shall apply to transfers by gift, or at death by decedents dying, after December 31, 2026.\n#### 4. Exclusion of certain amounts of realized capital gain\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 140 the following new section:\n139M. Exclusion of gain from transfers of appreciated assets at death (a) In general Gross income shall not include\u2014 (1) so much of the net capital gain for the taxable year from transfers at death to which 1261(a) applies as does not exceed $1,000,000, and (2) in the case of property that is a qualifying family farm or business that meets the certification requirement of subsection (d), 50 percent of so much of any gain from a transfer described in paragraph (1) as exceeds $1,000,000. (b) Inflation adjustment (1) In general In the case of any taxable year beginning after 2027, the $1,000,000 amounts in subsection (a) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting in subparagraph (A)(ii) thereof calendar year 2026 for calendar year 2016 . (2) Rounding If the dollar amount in subsection (a), after being increased under paragraph (1), is not a multiple of $10,000, such amount shall be rounded to the next lowest multiple of $10,000. (c) Definitions For purposes of this section\u2014 (1) Qualifying family farm or business The term qualifying family farm or business means real property located in the United States if during periods aggregating 3 years or more of the 5-year period ending on the date of the bequest of such real property, such real property was used as a farm for farming purposes or a family business. (2) Other definitions The terms farm and farming purposes , and material participation have the respective meanings given such terms by paragraphs (4) and (5) of section 2032A(e), respectively. (d) Use certification as farm for farming purposes or family business The certification requirement of this subsection is a certification that the use of the qualifying family farm or business referred to in subsection (a) will be as a farm for farming purposes or family business (as the case may be) for not less than the 120-month period beginning on the date of the bequest referred to in subsection (a). (e) Special rules For purposes of this section, the following rules shall apply: (1) Rules similar to the rules of subsections (e) and (f) of section 121. (2) Rules similar to the rules of paragraphs (4) and (5) of section 2032A(b) and paragraph (3) of section 2032A(e). (f) Treatment of disposition or change in use of property (1) In general If, as of the close of any taxable year, there is a recapture event with respect to any qualifying family farm or business transferred to the taxpayer in a bequest described in subsection (a), then the tax of the taxpayer under this chapter for such taxable year shall be increased by an amount equal to the product of\u2014 (A) the amount determined by dividing\u2014 (i) the amount of gain excluded from gross income of the taxpayer under subsection (a)(2) on the date such property was transferred to the taxpayer, over (ii) 120, and (B) the number of full months remaining in the 120-month term described in subsection (d) as of the date of such recapture event. (2) Recapture event defined For purposes of this subsection, the term recapture event means\u2014 (A) Cessation of operation The cessation of the operation of any property the sale or exchange of which to the taxpayer is described in subsection (a) as a qualifying family farm or business. (B) Change in ownership (i) In general Except as provided in clause (ii), the disposition of a taxpayer\u2019s interest in any property the sale or exchange of which to the taxpayer is described in subsection (a). (ii) Agreement to assume recapture liability Clause (i) shall not apply if the person acquiring such interest in the property agrees in writing to assume the recapture liability of the person disposing of such interest in effect immediately before such disposition. In the event of such an assumption, the person acquiring the interest in the property shall be treated as the taxpayer for purposes of assessing any recapture liability (computed as if there had been no change in ownership). (3) Special rules (A) No credits against tax Any increase in tax under this subsection shall not be treated as a tax imposed by this chapter for purposes of determining the amount of any credit under subpart A, B, or D of part IV of subchapter A. (B) No recapture by reason of hardship The increase in tax under this subsection shall not apply to any disposition of property or cessation of the operation of any property as a farm for farming purposes by reason of any hardship as determined by the Secretary. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting before the item relating to section 140 the following new item:\nSec. 139M. Exclusion of gain from transfers of appreciated assets at death. .\n##### (c) Effective date\nThe amendments made by this section shall apply to transfers at death by decedents dying after December 31, 2026, in taxable years beginning after such date.\n#### 5. Information reporting of certain gifts\n##### (a) In general\nSubpart B of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6050BB. Returns relating to certain gifts and bequests (a) In general In the case of an applicable transfer, the individual making such gift, or the executor in the case of a transfer at death, shall furnish to the Secretary the following information: (1) The name and taxpayer identification number of the person to whom such transfer was made. (2) A description of the property transferred. (3) The fair market value of the property transferred and the basis of such property to the transferee. (b) Applicable transfer (1) In general For purposes of this section, the term applicable transfer means\u2014 (A) any gift (other than a covered security (as defined in section 6045(g)(3))) which is taken into account under section 1261, and (B) so much of any transfer at death (other than such a covered security) which is so taken into account under section 1261 and the gain from which is includible in gross income for the taxable year of such transfer. (2) De minimis (A) Gifts For gifts exceeding the limitation for such year under section 2503(b) and not taken into account under section 1261, see subsection (d) thereof. (B) Transfers at death For amount of gain excluded from gross income in case of a transfer at death, see section 139M(a). (c) Statements To Be furnished to persons with respect to whom information is required Every person required to make a return under subsection (a) shall furnish to each person whose name is required to set forth in such return a written statement showing the information described in subsection (a). (d) Timing The returns and statements required under this section shall be furnished at such time and in such form and manner as the Secretary shall by regulation prescribe. .\n##### (b) Clerical amendment\nThe table of sections for subpart B of part III of subchapter A of chapter 61 of such Code is amended by adding at the end the following new item:\nSec. 6050BB. Returns relating to certain gifts. .\n##### (c) Effective date\nThe amendments made by this section shall apply to transfers after December 31, 2026, in taxable years beginning after such date.\n#### 6. Extension of time for payment of tax\n##### (a) Extension of time\n**(1) In general**\nSubchapter B of chapter 62 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6168. Extension of time for payment of capital gains on certain assets realized by reason of death (a) 5-Year installment payment (1) In general In the case of any gain with respect to eligible property that is recognized under section 1261 by reason of the death of the taxpayer, the taxpayer may elect to pay part or all of tax imposed on such gain in 2 or more (but not exceeding 5) equal installments. (2) Date for payment of installments If an election is made under paragraph (1), the first installment shall be paid not later than the date on which the tax for the taxable year in which the gain described in paragraph (1) occurs is due, and each succeeding installment shall be paid on or before the date which is 1 year after the date prescribed by this paragraph for payment of the preceding installment. (b) Eligible capital asset For purposes of this section, the term eligible property means any property other than personal property of a type which is actively traded (within the meaning of section 1092(d)(1)). (c) Portion of tax eligible The amount of tax to which this section applies shall not exceed the excess of\u2014 (1) the tax computed under chapter 1 (determined after application of section 1261), over (2) the tax computed under chapter 1 (determined without regard to section 1261). (d) Election Any election under subsection (a) shall be made not later than the time prescribed by section 6072 for filing the return of tax imposed under chapter 1 (including extensions thereof), and shall be made in such manner as the Secretary shall by regulations prescribe. If an election under subsection (a) is made, the provisions of this subtitle shall apply as though the Secretary were extending the time for payment of the tax. (e) Proration of deficiency to installments If an election is made under subsection (a) to pay any part of the tax imposed under chapter 1 in installments and a deficiency has been assessed, the deficiency shall (subject to the limitation provided by subsection (a)(2)) be prorated to the installments payable under subsection (a). The part of the deficiency so prorated to any installment the date for payment of which has not arrived shall be collected at the same time as, and as a part of, such installment. The part of the deficiency so prorated to any installment the date for payment of which has arrived shall be paid upon notice and demand from the Secretary. This subsection shall not apply if the deficiency is due to negligence, to intentional disregard of rules and regulations, or to fraud with intent to evade tax. (f) Time for payment of interest If the time for payment of any amount of tax has been extended under this section, interest payable under section 6601 on any unpaid portion shall be paid annually at the same time as, and as part of, each installment payment of the tax. (g) Regulations The Secretary shall prescribe such regulations as may be necessary to the application of this section. (h) Cross-References (1) Security For authority of the Secretary to require security in the case of an extension under this section, see section 6165. (2) Interest For provisions relating to interest on tax payable in installments under this section, see subsection (k) of section 6601. .\n**(2) Coordination with transferee liability**\nSection 6109 of such Code is amended by redesignating subsections (g), (h), and (i) as subsections (h), (i), and (j), respectively, and by inserting after subsection (f) the following new subsection:\n(g) Period of assessment in case of extension of time for payment of tax under section 1261 For purposes of subsection (c), the period of limitation for assessment against the transferor of any tax imposed under section 1261 the payment of which is extended under section 6168 shall not be treated as expiring earlier than the due date for the last payment under (a)(2) of such section. .\n**(3) Clerical amendment**\nThe table of sections for subpart B of chapter 62 of such Code is amended by adding at the end the following new item:\nSec. 6168. Extension of time for payment of capital gains on certain assets realized by reason of death. .\n##### (b) Interest\nSection 6601 of such Code is amended by redesignating subsection (k) as subsection (l) and by inserting after subsection (j) the following new subsection:\n(k) Special rate for tax extended under section 6168 If the time for payment of an amount of tax imposed by section 1261 is extended as provided in section 6168, in lieu of the annual rate provided by subsection (a), interest shall be paid at a rate equal to 45 percent of the annual rate provided by subsection (a). For purposes of this subsection, the amount of any deficiency which is prorated to installments payable under section 6168 shall be treated as an amount of tax payable in installments under such section. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2026.\n#### 7. Limitation on use of like-kind exchanges to avoid tax on real estate gains\n##### (a) Limitation on nonrecognition of gain\nSection 1031(a) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(4) Limitations (A) Annual limitation The amount of gain excluded from recognition under paragraph (1) with respect to any property of the taxpayer during the taxable year which is not qualified property shall not exceed $500,000. (B) Aggregate limitation The aggregate amount of gain excluded from recognition under subparagraph (A) by the taxpayer for all taxable years shall not exceed $1,000,000. (C) Qualified property For purposes of this paragraph, the term qualified property means property\u2014 (i) which is used for farming purposes, or (ii) which is exchanged for property that will serve the same specific purpose. .\n##### (b) Effective date\nThe amendment made by this section shall apply to exchanges of real property after December 31, 2026.\n#### 8. Limitation on deduction for qualified business income\n##### (a) In general\nSection 199A(a)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subparagraph (A), by striking the taxable income of the taxpayer for the taxable year and inserting so much of the taxable income of the taxpayer for the taxable year as does not exceed $1,000,000 , and\n**(2)**\nin subparagraph (B), by striking the net capital gain (as defined in section 1(h)) of the taxpayer for such taxable year and inserting all income of the taxpayer for such taxable year other than qualified business income .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2026.",
      "versionDate": "2026-03-17",
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
        "actionDate": "2025-09-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Equal Tax Act",
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
        "updateDate": "2026-03-31T21:35:34Z"
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
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4122is.xml"
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
      "title": "Equal Tax Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equal Tax Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to equalize treatment of capital gains and earned income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:38Z"
    }
  ]
}
```
