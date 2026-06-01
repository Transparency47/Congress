# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4196?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4196
- Title: Strengthen Social Security by Taxing Dynastic Wealth Act
- Congress: 119
- Bill type: S
- Bill number: 4196
- Origin chamber: Senate
- Introduced date: 2026-03-25
- Update date: 2026-04-14T19:11:02Z
- Update date including text: 2026-04-14T19:11:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-25: Introduced in Senate
- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-25: Introduced in Senate

## Actions

- 2026-03-25 - IntroReferral: Introduced in Senate
- 2026-03-25 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-25",
    "latestAction": {
      "actionDate": "2026-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4196",
    "number": "4196",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000128",
        "district": "",
        "firstName": "Chris",
        "fullName": "Sen. Van Hollen, Chris [D-MD]",
        "lastName": "Van Hollen",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Strengthen Social Security by Taxing Dynastic Wealth Act",
    "type": "S",
    "updateDate": "2026-04-14T19:11:02Z",
    "updateDateIncludingText": "2026-04-14T19:11:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "actionDate": "2026-03-25",
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
          "date": "2026-03-25T18:40:17Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4196is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4196\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2026 Mr. Van Hollen introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to return the estate, gift, and generation skipping transfer tax to 2009 levels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthen Social Security by Taxing Dynastic Wealth Act .\n#### 2. Estate and gift tax returned to 2009 levels\n##### (a) Estate tax\n**(1) Rate schedule**\nThe table contained in section 2001(c) of the Internal Revenue Code of 1986 is amended by striking the last row and inserting the following:\nOver $1,000,000 but not over $1,250,000\n$345,800, plus 41 percent of the excess of such amount over $1,000,000.\nOver $1,250,000 but not over $1,500,000\n$448,300, plus 43 percent of the excess of such amount over $1,250,000.\nOver $1,500,000\n$555,800, plus 45 percent of the excess of such amount over $1,500,000.\n**(2) Reduction of basic exclusion amount**\nParagraph (3) of section 2010(c) of the Internal Revenue Code of 1986 is amended to read as follows:\n(3) Basic exclusion amount For purposes of this subsection, the basic exclusion amount is $3,500,000. .\n##### (b) Gift tax\n**(1) Limitation on basic exclusion amount for purposes of determining applicable credit amount**\nParagraph (1) of section 2505(a) of the Internal Revenue Code of 1986 is amended by inserting (determined as if the basic exclusion amount were $1,000,000 and the deceased spousal unused exclusion amount was modified under subsection (d)) after calendar year .\n**(2) Modification of deceased spousal unused exclusion amount**\nSection 2505 of such Code is amended by adding at the end the following:\n(d) Modification of deceased spousal unused exclusion amount In the case of a surviving spouse who is the last spouse of the decedent with respect to whom an election is made under section 2010(c)(5), the deceased spousal unused exclusion amount with respect to such surviving spouse shall be determined as if such amount were the lesser of\u2014 (1) $1,000,000, and (2) applicable exclusion amount of the decedent reduced by the amount with respect to which the tentative tax is determined under section 2001(b)(1) on the estate of the decedent. .\n##### (c) Effective date\nThe amendments made by this section shall apply to estates of decedents dying and gifts made after December 31, 2026.\n#### 3. Transfer of estate and gift tax revenue to combined Social Security Trust Fund\n##### (a) In general\nSection 201(a) of the Social Security Act ( 42 U.S.C. 401(a) ) is amended to read as follows:\n(a) There is hereby created on the books of the Treasury of the United States a trust fund to be known as the Social Security Trust Fund . The Social Security Trust Fund shall consist of the securities held by the Secretary of the Treasury for the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and the amount standing to the credit of the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund on the books of the Treasury on January 1, 2027, which securities and amount the Secretary of the Treasury is authorized and directed to transfer to the Social Security Trust Fund, and, in addition, such gifts and bequests as may be made as provided in subsection (i)(1), and such amounts as may be appropriated to, or deposited in, the Social Security Trust Fund as hereinafter provided. There is hereby appropriated to the Social Security Trust Fund for the first fiscal year that begins after January 1, 2027, and for each fiscal year thereafter, out of any moneys in the Treasury not otherwise appropriated, amounts equivalent to 100 percent of\u2014 (1) the taxes imposed by chapter 21 (other than sections 3101(b) and 3111(b)) of the Internal Revenue Code of 1986 with respect to wages (as defined in section 3121 of such Code) reported to the Secretary of the Treasury pursuant to subtitle F of the Internal Revenue Code of 1986, as determined by the Secretary of the Treasury by applying the applicable rates of tax under such chapter (other than sections 3101(b) and 3111(b)) to such wages, which wages shall be certified by the Commissioner of Social Security on the basis of the records of wages established and maintained by such Commissioner in accordance with such reports; (2) the taxes imposed by chapter 2 (other than section 1401(b)) of the Internal Revenue Code of 1986 with respect to self-employment income (as defined in section 1402 of such Code) reported to the Secretary of the Treasury on tax returns under subtitle F of such Code, as determined by the Secretary of the Treasury by applying the applicable rate of tax under such chapter (other than section 1401(b)) to such self-employment income, which self-employment income shall be certified by the Commissioner of Social Security on the basis of the records of self-employment income established and maintained by the Commissioner of Social Security in accordance with such returns; and (3) the taxes imposed by subtitle B of the Internal Revenue Code of 1986, as determined by the Secretary of the Treasury on the basis of tax returns under subpart C of part II of subchapter A of chapter 61 of subtitle F of such Code. The amounts appropriated by paragraphs (1), (2), and (3) shall be transferred from time to time from the general fund in the Treasury to the Social Security Trust Fund, such amounts to be determined on the basis of estimates by the Secretary of the Treasury of the taxes, specified in such paragraphs, paid to or deposited into the Treasury; and proper adjustments shall be made in amounts subsequently transferred to the extent prior estimates were in excess of or were less than the taxes specified in such paragraphs. All amounts transferred to the Social Security Trust Fund under the preceding sentence shall be invested by the Managing Trustee in the same manner and to the same extent as the other assets of the Trust Fund. Notwithstanding the preceding sentence, in any case in which the Secretary of the Treasury determines that the assets of the Trust Fund would otherwise be inadequate to meet the Trust Fund's obligations for any month, the Secretary of the Treasury shall transfer to the Trust Fund on the first day of such month the total amount which would have been transferred to the Trust Fund under this section as in effect on October 1, 1990; and the Trust Fund shall pay interest to the general fund on the amount so transferred on the first day of any month at a rate (calculated on a daily basis, and applied against the difference between the amount so transferred on such first day and the amount which would have been transferred to the Trust Fund up to that day under the procedures in effect on January 1, 1983) equal to the rate earned by the investments of the Trust Fund in the same month under subsection (d). .\n##### (b) Required actuarial analysis\nSection 201(c) of the Social Security Act is amended by striking the fourth sentence in the matter following paragraph (5) and inserting the following: Such report shall also include actuarial analysis of the benefit cost with respect to disabled beneficiaries and their auxiliaries, to retired beneficiaries and their auxiliaries, and to survivor beneficiaries. .\n##### (c) Board of Trustees\n**(1) Board of Trustees of Social Security Trust Fund**\nSection 201(c) of the Social Security Act, as amended by subsection (b) of this section, is further amended in the matter preceding paragraph (1) by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund (hereinafter in this title called the Trust Funds ) and inserting the Social Security Trust Fund (in this title referred to as the Trust Fund ) .\n**(2) Continuity of Board of Trustees**\nThe Board of Trustees of the Social Security Trust Fund created by the amendment made by subsection (a) shall be a continuous body with the Board of Trustees of the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund in operation prior to the effective date of such amendment. Individuals serving as members of the Board of Trustees of the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund as of the effective date of such amendment shall serve the remainder of their term as members of the Board of Trustees of the Social Security Trust Fund.\n##### (d) Conforming amendments related to Social Security Trust Fund\n**(1) Amendment to section heading**\nThe section heading for section 201 of the Social Security Act is amended to read as follows: Social Security Trust Fund .\n**(2) Board of Trustees**\nSection 201(c) of such Act, as amended by subsections (b) and (c)(1), is further amended\u2014\n**(A)**\nin the matter preceding paragraph (1), by striking Board of Trustees of the Trust Funds and inserting Board of Trustees of the Trust Fund ;\n**(B)**\nin paragraph (1), by striking Trust Funds and inserting Trust Fund ;\n**(C)**\nin paragraph (2)\u2014\n**(i)**\nby striking Trust Funds and inserting Trust Fund ; and\n**(ii)**\nby striking their and inserting its ;\n**(D)**\nin paragraph (3), by striking either of the Trust Funds and inserting the Trust Fund ;\n**(E)**\nin paragraph (5)\u2014\n**(i)**\nby striking managing the Trust Funds and inserting managing the Trust Fund ; and\n**(ii)**\nby striking Trust Funds are and inserting Trust Fund is ;\n**(F)**\nin the matter following paragraph (5), by striking Trust Funds each place it appears and inserting Trust Fund ; and\n**(G)**\nin the second sentence in the matter following paragraph (5), by striking whether the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund, individually and collectively, are and inserting whether the Social Security Trust Fund is .\n**(3) Investments**\nSection 201 of such Act is amended in subsections (d) and (e) by striking Trust Funds each place it appears and inserting Trust Fund .\n**(4) Crediting of interest and proceeds to Trust Funds**\nSection 201(f) of such Act is amended\u2014\n**(A)**\nby striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund shall be credited to and form a part of the Federal Old-Age and Survivors Insurance Trust Fund and the Disability Insurance Trust Fund, respectively and inserting the Social Security Trust Fund shall be credited to and form a part of the Social Security Trust Fund ;\n**(B)**\nby striking either of the Trust Funds and inserting the Trust Fund ; and\n**(C)**\nby striking such Trust Fund and inserting the Trust Fund .\n**(5) Administrative costs**\nSection 201(g) of such Act is amended\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin subparagraph (A), by striking Of the amounts authorized to be made available out of the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund under the preceding sentence and all that follows through ( Public Law 103\u2013296 ). ; and\n**(ii)**\nin subparagraph (B)(i)\u2014\n**(I)**\nby striking subclauses (II) and (III) and inserting the following:\n(II) the portion of such costs which should have been borne by the Social Security Trust Fund, ; and\n**(II)**\nby redesignating subclauses (IV) and (V) as subclauses (III) and (IV);\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking Trust Funds and inserting Trust Fund ; and\n**(ii)**\nby striking the last sentence; and\n**(C)**\nin paragraph (4), by striking Trust Funds each place it appears and inserting Trust Fund .\n**(6) Benefit payments**\nSection 201(h) of such Act is amended to read as follows:\n(h) All benefit payments required to be made under this title shall be made only from the Social Security Trust Fund. .\n**(7) Gifts**\nSection 201(i) of such Act is amended\u2014\n**(A)**\nin paragraph (1), by striking the Federal Old-Age and Survivors Insurance Trust Fund, the Federal Disability Insurance Trust Fund and inserting the Social Security Trust Fund ; and\n**(B)**\nin paragraph (2)(B), by striking the Federal Old-Age and Survivors Insurance Trust Fund and inserting the Social Security Trust Fund .\n**(8) Travel expenses**\nSection 201(j) of such Act is amended by striking the Federal Old-Age and Survivors Insurance Trust Fund, or the Federal Disability Insurance Trust Fund (as determined appropriate by the Commissioner of Social Security) and inserting the Social Security Trust Fund .\n**(9) Demonstration projects**\nSection 201(k) of such Act is amended by striking the Federal Disability Insurance Trust Fund and the Federal Old-Age and Survivors Insurance Trust Fund, as determined appropriate by the Commissioner of Social Security and inserting the Social Security Trust Fund .\n**(10) Benefit checks**\nSection 201(m) of such Act is amended\u2014\n**(A)**\nin paragraph (2), by striking each of the Trust Funds and inserting the Social Security Trust Fund ;\n**(B)**\nin paragraph (3), by striking one of the Trust Funds and inserting the Trust Fund ; and\n**(C)**\nby striking such Trust Fund each place it appears and inserting the Trust Fund .\n**(11) Conforming repeals**\n**(A) In general**\nSection 201 of such Act is amended by striking subsections (b), (l), and (n).\n**(B) Redesignations**\nSection 201 of such Act is further amended\u2014\n**(i)**\nby redesignating subsections (c) through (j) as subsections (b) through (i), respectively;\n**(ii)**\nby redesignating subsection (k) as subsection (j); and\n**(iii)**\nby redesignating subsection (m) as subsection (k).\n**(C) References to redesignated sections**\n**(i)**\nSection 201(a) of such Act, as amended by subsection (a) of this section, is further amended\u2014\n**(I)**\nby striking subsection (i)(1) and inserting subsection (h)(1) ; and\n**(II)**\nby striking subsection (d) and inserting subsection (c) .\n**(ii)**\nSection 1131(b)(1) of such Act is amended by striking section 201(g)(1) and inserting section 201(f)(1) .\n##### (e) Other conforming amendments to Social Security Act\n**(1) Title II**\nTitle II of the Social Security Act ( 42 U.S.C. 401 et seq. ) is amended\u2014\n**(A)**\nin section 202(x)(3)(B)(iii), by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund, as appropriate, and inserting the Social Security Trust Fund ;\n**(B)**\nin section 206(d)(5), by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund, as appropriate and inserting the Social Security Trust Fund ;\n**(C)**\nin section 206(e)(3)(B), by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting the Social Security Trust Fund ;\n**(D)**\nin section 208(b)(5)(A), by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund, as appropriate and inserting the Social Security Trust Fund ;\n**(E)**\nin section 215(i)(1)(F)\u2014\n**(i)**\nin clause (i)\u2014\n**(I)**\nby striking the combined balance in the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting the balance in the Social Security Trust Fund ; and\n**(II)**\nby striking and reduced by the outstanding amount of any loan (including interest thereon) theretofore made to either such Fund from the Federal Hospital Insurance Trust Fund under section 201(l) ; and\n**(ii)**\nin clause (ii)\u2014\n**(I)**\nby striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting the Social Security Trust Fund ; and\n**(II)**\nby striking (other than payments and all that follows through from that Account ;\n**(F)**\nin section 217(g)(2), by inserting after the first sentence the following: For purposes of any such revision of the amount determined under paragraph (1) that occurs in a year after 2015, any reference in such paragraph to the Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund shall be deemed to be a reference to the Social Security Trust Fund. ;\n**(G)**\nin section 221(e)\u2014\n**(i)**\nby striking Trust Funds each place it appears and inserting Trust Fund ; and\n**(ii)**\nby striking the last sentence;\n**(H)**\nin section 221(f), by striking Trust Funds and inserting Trust Fund ;\n**(I)**\nin section 222(d)\u2014\n**(i)**\nin the section heading, by striking Trust Funds and inserting Trust Fund ;\n**(ii)**\nin paragraph (1), by striking to the end that savings will accrue to the Trust Funds as a result of rehabilitating such individuals, there are authorized to be transferred from the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting to the end that savings will accrue to the Trust Fund as a result of rehabilitating such individuals, there are authorized to be transferred from the Social Security Trust Fund ; and\n**(iii)**\nby amending paragraph (4) to read as follows:\n(4) The Commissioner of Social Security shall determine according to such methods and procedures as the Commissioner may deem appropriate the total amount to be reimbursed for the cost of services under this subsection. ;\n**(J)**\nin section 228(g)\u2014\n**(i)**\nin the section heading, by striking Federal Old-Age and Survivors Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(ii)**\nin the matter preceding paragraph (1), by striking Federal Old-Age and Survivors Insurance Trust Fund and inserting Social Security Trust Fund ;\n**(K)**\nin section 231(c), by striking Trust Funds each place it appears and inserting Trust Fund ; and\n**(L)**\nin section 234(a)(1), by striking Trust Funds and inserting Trust Fund .\n**(2) Title VII**\nTitle VII of the Social Security Act ( 42 U.S.C. 901 et seq. ) is amended\u2014\n**(A)**\nin section 703(j), by striking Federal Disability Insurance Trust Fund, the Federal Old-Age and Survivors Insurance Trust Fund, and inserting Social Security Trust Fund ;\n**(B)**\nin section 708(c), by striking the OASDI trust fund ratio under section 201(l), after computing ;\n**(C)**\nin section 709\u2014\n**(i)**\nin subsection (a), by striking Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(ii)**\nin subsection (b)\u2014\n**(I)**\nin paragraph (1), by striking section 201(l) or ; and\n**(II)**\nin paragraph (2), by striking Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(D)**\nin section 710\u2014\n**(i)**\nin subsection (a), by striking Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(ii)**\nin subsection (b)\u2014\n**(I)**\nby striking any Trust Fund specified in subsection (a) and inserting the Social Security Trust Fund ; and\n**(II)**\nby striking payments from any such Trust Fund and inserting payments from the Social Security Trust Fund .\n**(3) Title XI**\nTitle XI of the Social Security Act ( 42 U.S.C. 1301 et seq. ) is amended\u2014\n**(A)**\nin section 1106(b), by striking the Federal Old-Age and Survivors Insurance Trust Fund, the Federal Disability Insurance Trust Fund and inserting the Social Security Trust Fund ;\n**(B)**\nin section 1129(e)(2)(A), by striking the Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund, as determined appropriate by the Secretary and inserting the Social Security Trust Fund ;\n**(C)**\nin sections 1131(b)(2) and 1140(c)(2), by striking the Federal Old-Age and Survivors Insurance Trust Fund and inserting the Social Security Trust Fund ;\n**(D)**\nin section 1145(c)\u2014\n**(i)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) the Social Security Trust Fund; ; and\n**(ii)**\nby redesignating paragraphs (3) and (4) as paragraphs (2) and (3), respectively; and\n**(E)**\nin section 1148(j)(1)(A)\u2014\n**(i)**\nin the first sentence, by striking the Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting the Social Security Trust Fund ; and\n**(ii)**\nby striking the second sentence.\n**(4) Title XVIII**\nTitle XVIII of the Social Security Act ( 42 U.S.C. 1395 ) is amended\u2014\n**(A)**\nin section 1817(g), by striking Federal Old-Age and Survivors Insurance Trust Fund and from the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ;\n**(B)**\nin section 1840(a)(2), by striking Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(C)**\nin section 1841(f), by striking Federal Old-Age and Survivors Insurance Trust Fund and from the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund .\n##### (f) Conforming amendments outside of Social Security Act\n**(1) Budget**\n**(A) Off-budget exemption**\nSection 405(a) of the Congressional Budget Act of 1974 ( 2 U.S.C. 655(a) ) is amended by striking Federal Old-Age and Survivors Insurance and Federal Disability Insurance Trust Funds and inserting Social Security Trust Fund .\n**(B) Sequestration exemption**\nSection 255(g)(1)(A) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 905(g)(1)(A) ) is amended by striking Payments to Social Security Trust Funds and inserting Payments to the Social Security Trust Fund .\n**(2) Tax**\n**(A) Taxable wages**\nSection 3121(l)(4) of the Internal Revenue Code of 1986 is amended by striking Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund .\n**(B) Overpayments**\n**(i)**\nSection 6402(d)(3)(C) of the Internal Revenue Code of 1986 is amended by striking Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund, whichever is certified to the Secretary as appropriate by the Commissioner of Social Security and inserting Social Security Trust Fund .\n**(ii)**\nSubsection (f)(2)(B) of section 3720A of title 31, United States Code, is amended by striking Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund, whichever is certified to the Secretary of the Treasury as appropriate by the Commissioner of Social Security and inserting Social Security Trust Fund .\n**(3) False claims penalties**\nSubsection (g)(2) of section 3806 of title 31, United States Code, is amended\u2014\n**(A)**\nin subparagraph (B)\u2014\n**(i)**\nby striking Secretary of Health and Human Services and inserting Commissioner of Social Security ; and\n**(ii)**\nby striking Federal Old-Age and Survivors Insurance Trust Fund and inserting Social Security Trust Fund ; and\n**(B)**\nin subparagraph (C)\u2014\n**(i)**\nby striking Secretary of Health and Human Services and inserting Commissioner of Social Security ; and\n**(ii)**\nby striking Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund .\n**(4) Railroad Retirement Board**\nSection 7 of the Railroad Retirement Act of 1974 ( 45 U.S.C. 231f ) is amended\u2014\n**(A)**\nin subsection (b)(2), by striking Federal Old-Age and Survivors Insurance Trust Fund and the Federal Disability Insurance Trust Fund and inserting Social Security Trust Fund ;\n**(B)**\nin subsection (c)(2)\u2014\n**(i)**\nby striking Secretary of Health, Education, and Welfare each time it appears and inserting Commissioner of Social Security ; and\n**(ii)**\nby striking Federal Old-Age and Survivors Insurance Trust Fund, the Federal Disability Insurance Trust Fund, each time it appears and inserting Social Security Trust Fund ; and\n**(C)**\nin subsection (c)(4), by striking Federal Old-Age and Survivors Insurance Trust Fund, the Federal Disability Insurance Trust Fund, and inserting Social Security Trust Fund .\n##### (g) Rule of construction\nEffective beginning on January 1, 2027, any reference in law to the Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund is deemed to be a reference to the Social Security Trust Fund.\n##### (h) Effective date\nThe amendments made by this section shall take effect on January 1, 2027.",
      "versionDate": "2026-03-25",
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
        "actionDate": "2025-02-27",
        "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials."
      },
      "number": "1700",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Social Security Expansion Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "770",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Social Security Expansion Act",
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
        "updateDate": "2026-04-14T01:29:29Z"
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
      "date": "2026-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4196is.xml"
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
      "title": "Strengthen Social Security by Taxing Dynastic Wealth Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-09T02:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthen Social Security by Taxing Dynastic Wealth Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-09T02:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to return the estate, gift, and generation skipping transfer tax to 2009 levels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-09T02:03:22Z"
    }
  ]
}
```
