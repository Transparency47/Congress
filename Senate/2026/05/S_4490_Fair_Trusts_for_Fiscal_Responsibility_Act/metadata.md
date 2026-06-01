# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4490?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4490
- Title: Fair Trusts for Fiscal Responsibility Act
- Congress: 119
- Bill type: S
- Bill number: 4490
- Origin chamber: Senate
- Introduced date: 2026-05-12
- Update date: 2026-05-28T20:35:59Z
- Update date including text: 2026-05-28T20:35:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in Senate
- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-05-12: Introduced in Senate

## Actions

- 2026-05-12 - IntroReferral: Introduced in Senate
- 2026-05-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4490",
    "number": "4490",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001111",
        "district": "",
        "firstName": "Patty",
        "fullName": "Sen. Murray, Patty [D-WA]",
        "lastName": "Murray",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Fair Trusts for Fiscal Responsibility Act",
    "type": "S",
    "updateDate": "2026-05-28T20:35:59Z",
    "updateDateIncludingText": "2026-05-28T20:35:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-12",
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
      "actionDate": "2026-05-12",
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
          "date": "2026-05-12T17:13:32Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OR"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "NJ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4490is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4490\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2026 Mrs. Murray (for herself, Mr. Wyden , Mr. Van Hollen , Mr. Booker , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax on the assets of trusts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair Trusts for Fiscal Responsibility Act .\n#### 2. Imposition of tax on assets of trusts\n##### (a) In general\nSubtitle B of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n16 Tax on trust assets SUBCHAPTER A\u2014Tax imposed SUBCHAPTER B\u2014Trust withholding credit account SUBCHAPTER C\u2014Definitions and other rules A Tax imposed Sec. 2901. Imposition of tax. Sec. 2902. Computation of tax. 2901. Imposition of tax (a) In general There is hereby imposed a tax on the net value of all assets of an applicable trust held on the last day of any calendar year. (b) Limitation The amount of tax imposed under this chapter on any applicable trust shall not exceed the excess (if any) of\u2014 (1) product of\u2014 (A) the sum of\u2014 (i) the net value of all assets of the trust held as of the last day of the calendar year, plus (ii) the balance of the trust withholding credit account (as determined under section 2911) as of such day, and (B) the highest rate of tax under section 2001(c) on the estates of decedents dying on such day, over (2) the amount determined under paragraph (1)(A)(ii). 2902. Computation of tax (a) In general The tax imposed by section 2901 shall be equal to the sum of\u2014 (1) 0 percent of so much of the net value of all assets of the trust as does not exceed the 1 percent bracket threshold, (2) 1 percent of so much of the net value of all assets of the trust in excess of the 1 percent bracket threshold but not in excess of the 1.5 percent bracket threshold, (3) 1.5 percent of so much of the net value of all assets of the trust in excess of the 1.5 percent bracket threshold but not in excess of the 2 percent bracket threshold, (4) 2 percent of so much of the net value of all assets of the trust in excess of the 2 percent bracket threshold but not in excess of the 3 percent bracket threshold, plus (5) 3 percent of so much of the net value of all assets of the trust in excess of the 3 percent bracket threshold. (b) Determination of bracket thresholds (1) In general Except as otherwise provided in this chapter\u2014 (A) 1 percent bracket threshold The 1 percent bracket threshold shall be equal to the lesser of\u2014 (i) $50,000,000, or (ii) the sum of\u2014 (I) $0, plus (II) the lowest unused 1 percent bracket amount allocated to the trust from among all beneficiaries of the trust. (B) 1.5 percent bracket threshold The 1.5 percent bracket threshold shall be equal to the lesser of\u2014 (i) $100,000,000, or (ii) the sum of\u2014 (I) the 1 percent bracket threshold, plus (II) the lowest unused 1.5 percent bracket amount allocated to the trust from among all beneficiaries of the trust. (C) 2 percent bracket threshold The 2 percent bracket threshold shall be equal to the lesser of\u2014 (i) $250,000,000, or (ii) the sum of\u2014 (I) the 1.5 percent bracket threshold, plus (II) the lowest unused 2 percent bracket amount allocated to the trust from among all beneficiaries of the trust. (D) 3 percent bracket threshold The 3 percent bracket threshold shall be equal to the lesser of\u2014 (i) $1,000,000,000, or (ii) the sum of\u2014 (I) the 2 percent bracket threshold, plus (II) the lowest unused 3 percent bracket amount allocated to the trust from among all beneficiaries of the trust. (2) Treatment of corporations, partnerships, and trusts In the case of any trust all of the beneficiaries of which are corporations, partnerships, or trusts (after application of the rules of paragraphs (2) and (3) of section 2922(b))\u2014 (A) the 1 percent bracket threshold shall be equal to the amount in effect under paragraph (1)(A)(i), (B) the 1.5 percent bracket threshold shall be equal to the amount in effect under paragraph (1)(B)(i), (C) the 2 percent bracket threshold shall be equal to the amount in effect under paragraph (1)(C)(i), and (D) the 3 percent bracket threshold shall be equal to the amount in effect under paragraph (1)(D)(i). (3) Inflation adjustment (A) In general In the case of any calendar year beginning after 2027, each of the dollar amounts in subparagraphs (A)(i), (B)(i), (C)(i), and (D)(i) of paragraph (1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for such calendar year, determined by substituting in subparagraph (A)(ii) thereof calendar year 2026 for calendar year 2016 . (B) Rounding If any amount as adjusted under subparagraph (A) is not a multiple of $10,000, such dollar amount shall be rounded to the next lowest multiple of $10,000. (c) Allocation of unused bracket amounts (1) In general Except as otherwise provided in this subsection, the amount of any category of unused bracket amount allocated to any trust from a beneficiary shall be equal to the product of\u2014 (A) the maximum amount with respect to such category as determined under paragraph (3)(B), and (B) the ratio of\u2014 (i) the present value of the beneficiary's beneficial interest in such trust (determined as provided in section 6039M(c)(3)), to (ii) the present value of the beneficiary's beneficial interest (as so determined) in all applicable trusts. (2) Election to assign different amounts A beneficiary may elect to allocate the amount of any category of unused bracket amount in a different manner than provided in paragraph (1), except that the aggregate amount of any category of unused bracket amounts allocated to all trusts for which such person is a beneficiary may not exceed the maximum amount with respect to such category as determined under paragraph (3)(B). An election made under this section shall be made at such time and in such manner as specified by the Secretary in regulations. (3) Categories of unused bracket amounts; maximum amount (A) Categories of unused bracket amounts For purposes of this subsection, the categories of unused bracket amounts are\u2014 (i) the unused 1 percent bracket amount, (ii) the unused 1.5 percent bracket amount, (iii) the unused 2 percent bracket amount, and (iv) the unused 3 percent bracket amount. (B) Maximum amount With respect to any person for any calendar year\u2014 (i) the maximum amount with respect to the unused 1 percent bracket amount shall be equal to the amount in effect under subsection (b)(1)(A)(i), (ii) the maximum amount with respect to the unused 1.5 percent bracket amount shall be equal to the amount in effect under subsection (b)(1)(B)(i), (iii) the maximum amount with respect to the unused 2 percent bracket amount shall be equal to the amount in effect under subsection (b)(1)(C)(i), and (iv) the maximum amount with respect to the unused 3 percent bracket amount shall be equal to the amount in effect under subsection (b)(1)(D)(i). (4) Special rule for certain beneficiaries (A) In general In the case of any beneficiary described in subparagraph (B), no amount shall be allocated under this section and the determination of the lowest amount allocated to a trust under subparagraphs (A)(ii)(II), (B)(ii)(II), (C)(ii)(II), and (D)(ii)(II) of subsection (b)(1) shall be determined without regard to such beneficiary. (B) Beneficiaries described A beneficiary is described in this subparagraph if\u2014 (i) such beneficiary is an exempt beneficiary, or (ii) such beneficiary is person described in section 6039M(b)(2). B Trust withholding credit account Sec. 2911. Trust withholding credit account. 2911. Trust withholding credit account (a) In general Under rules established by the Secretary\u2014 (1) each applicable trust which is subject to a tax imposed under this chapter, and (2) each beneficiary of an applicable trust who receives a qualified distribution, shall establish a trust withholding credit account. (b) Additions to account (1) Trusts The balance of the trust withholding credit account for any applicable trust shall be increased by the amount of tax imposed under this chapter which is paid by or on behalf of the trust. (2) Beneficiaries (A) In general The balance of the trust withholding credit account for any beneficiary who receives a qualified distribution shall be increased by the ratable share with respect to such distribution. (B) Distributions to certain corporate shareholders and partners \u2014 (i) In general For purposes of this section, in the case of a qualified distribution to a corporation or partnership with respect to which a shareholder or partner is treated as a beneficiary by reason of section 2922(b)(3)(B), such shareholder or partner (as the case may be) shall be treated as having directly received a qualified distribution in an amount equal to the applicable percentage of the amount of the distribution made to such corporation or partnership. (ii) Applicable percentage For purposes of this subparagraph, the applicable percentage is the percentage of the ownership interest held by such individual in the corporation or partnership at the time of the distribution (determined as provided under section 2922(b)(3)(B)). (C) Limitation In the case of a qualified distribution which is a direct skip from a trust (within the meaning of chapter 13), the amount of the increase under subparagraph (A) shall be reduced by the amount of credit allowed under section 2604(c)(2) (if any) to the trust making the distribution. (c) Subtractions (1) Trusts The balance of the trust withholding credit account for any applicable trust shall be reduced by\u2014 (A) the ratable share with respect to any qualified distribution made by the trust, and (B) in the case of a taxable termination (as defined in section 2612), the sum of\u2014 (i) the amount of any credit allowed under section 2604(a), plus (ii) the product of\u2014 (I) the amount determined under section 2604(a)(1) with respect to such taxable termination, and (II) the excess of 1 over the inclusion ratio (as defined in section 2642). (2) Beneficiaries The balance of the trust withholding credit account for any beneficiary shall be reduced by the amount of credits allowed to the beneficiary under sections 2017, 2604(b), and 2604(c). (d) Qualified distribution For purposes of this section\u2014 (1) In general The term qualified distribution means any distribution which\u2014 (A) is made from an applicable trust which is subject to a tax under this chapter, and (B) is made to any person other than an exempt beneficiary. (2) Special rule for certain trusts In the case of a property in an applicable trust which is includible in the gross estate of an individual, such property shall be treated as distributed from the applicable trust to the individual in a qualified distribution (and such individual shall be treated as the beneficiary of such trust for purposes of subsection (b)(2)) on the earlier of\u2014 (A) the date such property is distributed from the trust, or (B) the date of the death of such individual. (e) Ratable share For purposes of this section, the term ratable share means, with respect to any qualified distribution, the amount which bears the same ratio to the balance of the trust withholding credit account (determined immediately before the qualified distribution) as\u2014 (1) the amount of the qualified distribution, bears to (2) the net value of assets of the trust (determined immediately before the qualified distribution). C Definitions and other rules Sec. 2921. Determination of net value of assets. Sec. 2922. Other definitions and special rules. 2921. Determination of net value of assets (a) In general For purposes of this chapter, the term net value of all assets means, as of any date, the value of all property of the trust, real or personal, tangible or intangible, wherever situated, reduced by any qualified debts owed by the taxpayer. (b) Value of property (1) Tradable assets (A) In general In the case of any tradable asset, the value of such asset shall be the fair market value of such asset. (B) Tradable asset For purposes of this paragraph, the term tradable asset means any asset if\u2014 (i) interests in such asset are traded on an established securities market, (ii) interests in such assets are readily tradable on a secondary market (or the substantial equivalent thereof), (iii) interests in such assets are available on an online or electronic platform that regularly matches, or facilitates the matching of, buyers and sellers of such assets, or (iv) such asset is an asset for which the Secretary determines there is a reasonable basis to determine the asset\u2019s fair market value annually. (2) Other assets (A) In general In the case of any asset which is not a tradable asset, the value of such asset shall be\u2014 (i) in any case in which there has been a qualified appraisal (as defined in section 170(f)(11)(E)) conducted within the 2-year period ending on the date the value is determined for purposes of this chapter, the value determined under such appraisal, and (ii) in any other case, the value of such property determined under such other method as prescribed by the Secretary. (B) Determination where no alternative method If subparagraph (A)(i) does not apply and the Secretary has not prescribed a method under subparagraph (A)(ii), the value of such asset shall be the greater of\u2014 (i) the sum of\u2014 (I) the basis of such asset, and (II) the product of\u2014 (aa) the amount determined under subclause (I), and (bb) the sum of 1 percent and the long-term rate determined under section 1274(d) for the applicable month, compounded semiannually, or (ii) the value of such property determined by a qualified appraisal (as defined in section 170(f)(11)(E)) conducted within the 5-year period ending on the date the value is determined for purposes of this chapter. (C) Applicable month For purposes of subparagraph (B)(i)(II)\u2014 (i) In general Except as provided in clause (ii), the term applicable month means, with respect to any asset, the month in which such asset was acquired by the taxpayer. (ii) Certain assets with carryover basis In the case of any asset the basis in the hands of the taxpayer was determined by reference to the basis in the hands of another person, the term applicable month means the month in which such asset was acquired by such other person. (3) Limitation on discount by reason of family control (A) In general For purposes of this chapter, in the case of any interest in an entity other than an interest which is actively traded (within the meaning of section 1092), if the person who transferred such interest, the transferee, and members of the family of the transferor and transferee have control of such entity immediately before such transfer, no discount shall be allowed\u2014 (i) by reason of the fact that the transferor or transferee does not have control of such entity, (ii) by reason of the lack of marketability of the interest, or (iii) for any other reason. (B) Definitions In this paragraph, the terms control and member of the family have the same meanings given such terms in section 2704(c). (C) Attribution For purposes of this paragraph, the rule of section 2701(e)(3) shall apply for purposes of determining the interests held by any individual. (4) Valuation rules for certain nonbusiness assets held by nontradable entities (A) In general For purposes of this chapter, in the case of any interest in an entity other than an interest which is a tradable asset\u2014 (i) the value of any nonbusiness assets held by the entity with respect to such interest shall be determined as if the owner of the entity directly held its ratable share of such nonbusiness assets (and no valuation discount shall be allowed with respect to such nonbusiness assets), and (ii) such nonbusiness assets shall not be taken into account in determining the value of the interest in the entity and the basis of such nonbusiness assets shall not be taken into account in determining the basis of such interest under paragraph (2)(A)(i). (B) Nonbusiness assets For purposes of this paragraph\u2014 (i) In general The term nonbusiness asset means any asset other than an asset which is used in the active conduct of a trade or business. (ii) Passive assets treated as nonbusiness assets For purposes of clause (i), a passive asset shall be treated as a nonbusiness asset unless\u2014 (I) the asset is property described in paragraph (1) or (4) of section 1221(a) or is a hedge with respect to such property, or (II) the asset is real property used in the active conduct of 1 or more real property trades or businesses (within the meaning of section 469(c)(7)(C)) in which the transferor materially participates and with respect to which the transferor meets the requirements of section 469(c)(7)(B)(ii). (iii) Material participation For purposes of clause (ii)(II), material participation shall be determined under the rules of section 469(h), except that section 469(h)(3) shall be applied without regard to the limitation to farming activity. (iv) Working capital treated as used in trade or business Any asset (including a passive asset) which is held as a part of the reasonably required working capital needs of a trade or business shall be treated as used in the active conduct of a trade or business. (C) Passive asset For purposes of this paragraph, the term passive asset means any\u2014 (i) cash or cash equivalents, (ii) stock in a corporation or any other equity, profits, or capital interest in any entity, (iii) evidence of indebtedness, option, forward or futures contract, notional principal contract, or derivative, (iv) asset described in clause (iii), (iv), or (v) of section 351(e)(1)(B), (v) annuity, (vi) real property used in 1 or more real property trades or businesses (as defined in section 469(c)(7)(C)), (vii) asset (other than a patent, trademark, or copyright) which produces royalty income, (viii) commodity, (ix) collectible (within the meaning of section 408(m)), or (x) any other asset specified in regulations prescribed by the Secretary. (D) Look-thru rule (i) In general If a nonbusiness asset of an entity described in subparagraph (A) consists of a 10-percent interest in any other entity, this paragraph shall be applied by disregarding the 10-percent interest and by treating the entity as holding directly its ratable share of the assets of the other entity. (ii) 10-percent interest The term 10-percent interest means\u2014 (I) in the case of an interest in a corporation, direct ownership of at least 10 percent (by vote or value) of the stock in such corporation, (II) in the case of an interest in a partnership, direct ownership of at least 10 percent of the capital or profits interest in the partnership, and (III) in any other case, direct ownership of at least 10 percent of the beneficial interests in the entity. (c) Qualified debt For purposes of this section\u2014 (1) In general The term qualified debt means any debt other than any debt to a person\u2014 (A) who made a contribution to the trust, (B) who is a beneficiary of the trust, or (C) who is related (within the meaning of section 267(b)) to the trust or to a person described in subparagraph (A) or (B). (2) Treatment of nonrecourse debt In the case of any debt which is nonrecourse debt, the amount of qualified debt shall not exceed the value of the property securing such debt. (d) Regulations Not later than 12 months after the date of the enactment of this section, the Secretary shall establish rules and methods for determining the value of any asset for purposes of this chapter, including rules for the valuation of assets that are not publicly traded or that do not have a readily ascertainable value. 2922. Other definitions and special rules (a) Applicable trust For purposes of this chapter\u2014 (1) In general The term applicable trust means any trust or any portion of a trust to the extent that such trust or portion\u2014 (A) is a United States person described in section 7701(a)(30)(E), (B) has one or more beneficiaries who are United States persons described in section 7701(a)(30), or (C) has one or more living grantors who are United States persons described in section 7701(a)(30)(A). For purposes of this paragraph, a living person who is related (determined under section 267(b), applied by substituting 5 percent for 50 percent each place it appears) to a grantor described in subparagraph (C) shall be treated as a person described in such subparagraph. (2) Exceptions The term applicable trust does not include\u2014 (A) a trust\u2014 (i) which is an organization described in paragraphs (1) through (5) of section 2055(a), or (ii) from which only transfers described in section 2055(a) may be made, (B) a trust described in section 401(a) and exempt from tax under section 501(a), (C) a trust used to facilitate issuance of securities (as determined by the Secretary under regulations), (D) a trust which\u2014 (i) has a maximum duration of less than 1 year, and (ii) is organized and operated exclusively for a commercial purpose determined by the Secretary to be applicable under this subsection, and (E) any trust or portion of a trust wherein the power to revest absolutely in the grantor title to the trust property to which such portion is attributable is exercisable solely by the grantor without the approval or consent of any other person. (b) Determination of beneficiaries; exempt beneficiary For purposes of this chapter\u2014 (1) Contingent beneficiaries (A) In general Except as provided in subparagraph (B), the term beneficiary shall not include any person whose interest in an applicable trust is contingent on the death of another person with an interest in such trust. (B) Exception The term beneficiary shall include a person whose interest in an applicable trust is contingent on the death of another person with an interest in such trust if\u2014 (i) there exists one or more persons whose interest in such trust is not contingent on the death of another person, and (ii) the amount of funds that may be distributed to any such person are limited by the trust instrument or by means other than the sole discretion of the trustee. (2) Treatment of beneficiary trusts If a trust is the beneficiary of another trust, each trust or individual which holds a beneficial interest in such trust shall be treated as a beneficiary of such other trust. (3) Corporations and partnerships (A) In general Except for purposes of subparagraph (B), the term beneficiary shall not include a corporation or a partnership. (B) Treatment of 5-percent owners (i) In general The term beneficiary shall include\u2014 (I) any shareholder of a corporation which is the beneficiary of an applicable trust if such shareholder holds 5 percent or more of the stock (by vote or value) of such corporation, and (II) any partner of a partnership which is the beneficiary of an applicable trust if such partner owns more than 5 percent of the capital or profits interest in the partnership. (ii) Constructive ownership rules For purposes of clause (i), rules similar to the rules of paragraphs (2), (3), (4), and (5) of section 318(a) shall apply. (4) Exempt beneficiary The term exempt beneficiary means any beneficiary which is an organization described in section 2055(a). .\n##### (b) Information reporting\n**(1) In general**\nSubpart A of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by inserting after section 6039L the following new section:\n6039M. Information with respect to trust asset tax (a) Statement of net assets Not later than April 1 of each calendar year, every applicable trust shall file with the Secretary a statement setting forth\u2014 (1) the name and taxpayer identification number of such trust, (2) the net value of assets of such trust as of the last day of the preceding calendar year, (3) the name and taxpayer identification number of each beneficiary of such trust, and (4) the present value of the beneficial interests in the trust of each such beneficiary as of the last day of the preceding calendar year. (b) Allocation of unused bracket amount (1) In general Not later than June 1 of each calendar year, each beneficiary of an applicable trust shall submit to the Secretary a statement setting forth\u2014 (A) the name and taxpayer identification number of such beneficiary, (B) the name and taxpayer identification number of each applicable trust of which such individual is a beneficiary, and (C) the amount of\u2014 (i) the unused 1 percent bracket amount allocated to each such trust under section 2902(c), (ii) the unused 1.5 percent bracket amount allocated to each such trust under section 2902(c), (iii) the unused 2 percent bracket amount allocated to each such trust under section 2902(c), and (iv) the unused 3 percent bracket amount allocated to each such trust under section 2902(c). (2) Exception Paragraph (1) shall not apply to any person if the aggregate present value of beneficial interests in all trusts with respect to which such person is a beneficiary is less than $250,000. (3) Copies to trusts Each beneficiary required to submit a statement under paragraph (1) shall (on or before the day on which the statement was required to be filed) furnish to each applicable trust identified on the statement the information required under paragraph (1) with respect to such applicable trust. (c) Definitions and other rules For purposes of this section\u2014 (1) Applicable trust The term applicable trust has the meaning given such term under chapter 16. (2) Beneficiary The term beneficiary has the meaning given such term under section 2922(b). (3) Present value of beneficial interests The present value of a person's beneficial interest in a trust shall be determined in proportion to the actuarial interest of such person in such trust. .\n**(2) Penalties**\n**(A) Initial statements**\nSection 6724(d)(1) of such Code is amended by striking and at the end of subparagraph (B), by striking and at the end of subparagraph (C), by striking the period at the end of subparagraph (D) and inserting , and , and by inserting after subparagraph (D) the following new subparagraph:\n(E) any statement required to be filed under subsection (a) or (b)(1) of section 6039M. .\n**(B) Copies**\nSection 6724(d)(2) of such Code is amended by striking or at the end of subparagraph (NN), by striking the period at the end of subparagraph (OO) and inserting , or , and by inserting after subparagraph (OO) the following new subparagraph:\n(PP) section 6039M(b)(3). .\n**(3) Clerical amendment**\nThe table of sections for subpart A of part III of subchapter A of chapter 61 of such Code is amended by inserting after the item relating to section 6039L the following new item:\nSec. 6039M. Information with respect to trust asset tax. .\n##### (c) No deduction from income taxes\nSection 275 of the Internal Revenue Code of 1986 is amended by inserting after paragraph (6) the following new paragraph:\n(7) Taxes imposed by chapter 16. .\n##### (d) Clerical amendment\nThe table of chapters for the Internal Revenue Code of 1986 is amended by inserting after the item relating to chapter 15 the following new item:\nChapter 16\u2014Tax on trust assets .\n##### (e) Effective date\nThe amendments made by this section shall apply to calendar years beginning after December 31, 2026.\n#### 3. Coordination with estate and generation-skipping and estate taxes\n##### (a) Tax on generation-Skipping transfers\n**(1) Gross-up of taxable amount**\nSubchapter C of chapter 13 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n2625. Gross up of taxable amount to include additions to trust withholding credit account The taxable amount shall be increased\u2014 (1) in the case of a taxable termination, by the amount which bears the same ratio to the balance of the trust withholding credit account of the trust involved (determined under section 2911 immediately before the taxable termination) as\u2014 (A) the taxable amount (determined without regard to this section), bears to (B) the net value of assets of such trust (determined under chapter 16 immediately before such taxable distribution), and (2) in the case of a taxable distribution or a direct skip from a trust, by the amount which bears the same ratio to the balance of the trust withholding credit account of the trust from which the taxable distribution or direct skip, as the case may be, was made (determined under section 2911 immediately before the taxable distribution) as\u2014 (A) the taxable amount (determined without regard to this section), bears to (B) the net value of assets of such trust (determined under chapter 16 immediately before such taxable distribution). .\n**(2) Credit for trust withholding taxes**\nSubchapter A of chapter 13 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n2604. Credit for previously paid trust asset taxes (a) Taxable terminations In the case of a taxable termination, there shall be allowed a credit against the tax imposed by section 2601 an amount equal to the product of\u2014 (1) the amount which bears the same ratio to the balance of the trust withholding credit account of the trust involved (determined under section 2911 as of the time of the taxable termination) as\u2014 (A) the taxable amount (determined without regard to section 2625), bears to (B) the net value of assets of the trust (determined under chapter 16 as of the date of the taxable termination), and (2) the inclusion ratio. (b) Taxable distributions In the case of a taxable distribution, there shall be allowed a credit against the tax imposed by section 2601 an amount equal to the product of\u2014 (1) the amount which bears the same ratio to the balance of the trust withholding credit account of the transferee involved (determined under section 2911 immediately after the time of the taxable distribution) as\u2014 (A) the taxable amount (determined without regard to section 2625), bears to (B) the net value of assets of the trust (determined under chapter 16 as of the time of the taxable distribution), and (2) the inclusion ratio. (c) Direct skips (1) In general In the case of a direct skip, there shall be allowed a credit against the tax imposed by section 2601 an amount equal to the lesser of\u2014 (A) the product of\u2014 (i) the balance of the trust withholding credit account of the person liable for such tax (determined under section 2911 immediately before the time of the direct skip), and (ii) the inclusion ratio, or (B) the amount of tax so imposed. (2) Direct skips from a trust In the case of a direct skip from a trust, the amount of the credit determined under this subsection shall not exceed the product of\u2014 (A) the amount which bears the same ratio to the balance of the trust withholding credit account of the trust involved (determined under section 2911 immediately before the time of the direct skip) as\u2014 (i) the taxable amount (determined without regard to section 2625), bears to (ii) the net value of assets of the trust (determined under chapter 16 as of the time of the direct skip), and (B) the inclusion ratio. .\n**(3) Clerical amendments**\n**(A)**\nThe table of sections for subchapter A of chapter 13 of such Code is amended by adding at the end the following new item:\nSec. 2604. Credit for previously paid trust asset taxes. .\n**(B)**\nThe table of sections for subchapter A of chapter 13 of such Code is amended by adding at the end the following new item:\nSec. 2625. Gross up of taxable amount to include additions to trust withholding credit account. .\n##### (b) Estate tax\n**(1) Gross up of tax**\n**(A) Citizens and residents**\nPart III of subchapter A of chapter 11 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n2047. Trust withholding credit account balance The gross estate shall include the balance of the trust withholding credit account (determined under section 2911) of the decedent. .\n**(B) Nonresidents not citizens**\nSection 2103 of such Code is amended by adding at the end the following new sentence: For purposes of this section, the balance of the trust withholding credit account shall be treated as situated in the United States. .\n**(2) Credit for previously paid trust withholding taxes**\n**(A) Estates of citizens and residents**\nPart II of subchapter A of chapter 11 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n2017. Credit for previously paid trust asset taxes There shall be allowed as a credit against the tax imposed by section 2001 an amount equal to the balance of the trust withholding credit account (determined under section 2911) of the decedent. .\n**(B) Estates of nonresidents not citizens**\nSection 2102(a) of the Internal Revenue Code of 1986 is amended by striking 2012 and 2013 (relating to gift tax and tax on prior transfers) and inserting 2012, 2013, and 2017 .\n**(C) Refunds of unused credits**\nSection 6401(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Estate tax credit for previously paid trust asset taxes (A) Citizens and residents If the amount allowable as credit under section 2017 exceeds the tax imposed under section 2001 (reduced by the amount of credits allowed under sections 2010 through 2016), the amount of such excess shall be considered an overpayment. (B) Nonresidents not citizens If the amount determined in accordance with section 2017 and allowable as a credit under section 2102 exceeds the tax imposed under section 2011 (reduced by the amount determined in accordance with sections 2012 and 2013 and allowed as a credit under section 2102), the amount of such excess shall be considered an overpayment. .\n**(3) Clerical amendments**\n**(A)**\nThe table of sections for subchapter A of chapter 13 of such Code is amended by adding at the end the following new item:\nSec. 2017. Credit for previously paid trust asset taxes. .\n**(B)**\nThe table of sections for subchapter A of chapter 13 of such Code is amended by adding at the end the following new item:\nSec. 2047. Trust withholding credit account balance. .\n##### (c) Effective date\nThe amendments made by this section shall apply to transfers made in calendar years beginning after, and decedents dying after, December 31, 2026.\n#### 4. Payment of taxes of grantor trusts\n##### (a) In general\nSection 2503 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a), by striking The term and inserting Subject to subsection (d), the term , and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Payment of tax on income of grantor trust (1) In general Notwithstanding subsections (b) and (e), an amount equal to the applicable taxes paid with respect to an applicable grantor trust for any calendar year by a person who is the deemed owner of such trust (or portion thereof) shall be treated for purposes of this subtitle as a taxable gift made during such calendar year. (2) Applicable grantor trust For purposes of this subsection, the term applicable grantor trust means any trustor portion of a trust\u2014 (A) with respect to which the taxpayer is considered an owner under subpart E of part I of subchapter J of chapter 1, and (B) which is not fully revocable by the taxpayer. (3) Applicable taxes For purposes of this subsection, the term applicable taxes means, with respect to any applicable grantor trust\u2014 (A) taxes paid on income, and (B) taxes paid on the value of assets of the trust. (4) Reimbursement by trust Paragraph (1) shall not apply with respect to any amount paid by the deemed owner for any calendar year which is reimbursed by the applicable grantor trust during such calendar year. (5) Date of gift In the case of any amount treated for purposes of this subtitle as a taxable gift pursuant to paragraph (1), such gift shall be deemed to have occurred on the earlier of\u2014 (A) December 31 of the calendar year for which the tax is paid by the person who is the deemed owner, (B) the day before the date of the death of such person, or (C) the date on which such person renounces any right of reimbursement by the applicable grantor trust with respect to the calendar year for which the tax is paid by such person. (6) Deemed owner For purposes of this subsection, the term deemed owner has the same meaning given such term under section 1062(c). .\n##### (b) Conforming amendments\n**(1)**\nSection 2522 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby redesignating subsection (f) as subsection (g), and\n**(B)**\nby inserting after subsection (e) the following new subsection:\n(f) Denial of deduction for payment of tax on income of grantor trust No deduction shall be allowed under this section for any amount which is treated as a gift by reason of section 2503(d). .\n**(2)**\nSection 2523 of such Code is amended by adding at the end the following new subsection:\n(j) Denial of deduction for payment of tax on income of grantor trust No deduction shall be allowed under this section for any amount which is treated as a gift by reason of section 2503(d). .\n##### (c) Effective dates\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act.",
      "versionDate": "2026-05-12",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-05-28T20:35:59Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4490is.xml"
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
      "title": "Fair Trusts for Fiscal Responsibility Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-19T00:53:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Trusts for Fiscal Responsibility Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-19T00:53:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a tax on the assets of trusts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-19T00:48:31Z"
    }
  ]
}
```
