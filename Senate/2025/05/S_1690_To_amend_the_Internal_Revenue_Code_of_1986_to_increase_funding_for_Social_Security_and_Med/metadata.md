# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1690
- Title: Medicare and Social Security Fair Share Act
- Congress: 119
- Bill type: S
- Bill number: 1690
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-12-05T21:53:14Z
- Update date including text: 2025-12-05T21:53:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1690",
    "number": "1690",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Medicare and Social Security Fair Share Act",
    "type": "S",
    "updateDate": "2025-12-05T21:53:14Z",
    "updateDateIncludingText": "2025-12-05T21:53:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T17:41:32Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "MD"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "NJ"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1690is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1690\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Whitehouse (for himself, Ms. Klobuchar , and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase funding for Social Security and Medicare.\n#### 1. Short title\nThis Act may be cited as the Medicare and Social Security Fair Share Act .\n#### 2. Modification of payroll taxes\n##### (a) Wage base for taxes funding social security\n**(1) In general**\nParagraph (1) of section 3121(a) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) in the case of taxes imposed by sections 3101(a) and 3111(a), for any calendar year in which the contribution and benefit base (as determined under section 230 of the Social Security Act) is less than $400,000, so much of the remuneration (other than remuneration referred to in the succeeding paragraphs of this subsection) with respect to employment that has been paid to an individual by an employer during the calendar year as exceeds such contribution and benefit base but does not exceed $400,000; .\n**(2) Conforming amendments**\n**(A) Successor employers**\nSection 3121 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(aa) Special rules for successor employers For purposes of subsection (a)(1), if an employer (hereinafter referred to as successor employer) during any calendar year acquires substantially all the property used in a trade or business of another employer (hereinafter referred to as a predecessor), or used in a separate unit of a trade or business of a predecessor, and immediately after the acquisition employs in his trade or business an individual who immediately prior to the acquisition was employed in the trade or business of such predecessor, then, for the purpose of determining the amount of remuneration paid by the successor employer under such subsection, any remuneration (other than remuneration referred to in the paragraphs succeeding paragraph (1) of subsection (a)) with respect to employment paid (or considered under this subsection as having been paid) to such individual by such predecessor during such calendar year and prior to such acquisition shall be considered as having been paid by such successor employer. .\n**(B) Application to railroad retirement taxes**\nClause (i) of section 3231(e)(2)(A) of such Code is amended to read as follows:\n(i) In general For any calendar year in which the applicable base is less than $400,000, the term compensation does not include so much of the remuneration paid during any calendar year to an individual by an employer for services rendered as an employee to such employer as exceeds the applicable base but does not exceed $400,000. .\n##### (b) Further additional hospital insurance tax on very high income taxpayers\n**(1) In general**\nSection 3101(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Further additional tax In addition to the tax imposed by paragraphs (1) and (2) and the preceding subsection, there is hereby imposed on every taxpayer (other than a corporation, estate, or trust) a tax equal to 1.2 percent of wages which are received with respect to employment (as defined in section 3121(b)) during the taxable year which are in excess of\u2014 (A) in the case of a joint return, $500,000, (B) in the case of a married taxpayer (as defined in section 7703) filing a separate return, \u00bd of the dollar amount determined under subparagraph (A), and (C) in any other case, $400,000. .\n**(2) Collection of tax**\nSection 3102 of such Code is amended by adding at the end the following new subsection:\n(g) Special rules for further additional tax (1) In general In the case of any tax imposed by section 3101(b)(3), subsection (a) shall only apply to the extent to which the taxpayer receives wages from the employer in excess of $400,000, and the employer may disregard the amount of wages received by such taxpayer\u2019s spouse. (2) Collection of amounts not withheld To the extent that the amount of any tax imposed by section 3101(b)(3) is not collected by the employer, such tax shall be paid by the employee. (3) Tax paid by recipient If an employer, in violation of this chapter, fails to deduct and withhold the tax imposed by section 3101(b)(3) and thereafter the tax is paid by the employee, the tax so required to be deducted and withheld shall not be collected from the employer, but this paragraph shall in no case relieve the employer from liability for any penalties or additions to tax otherwise applicable in respect of such failure to deduct and withhold. .\n##### (c) Effective date\nThe amendments made by this section shall apply to remuneration paid, and taxable years beginning, on or after January 1 of the first calendar year that begins after the date of enactment of this Act.\n#### 3. Modification of taxes on self-employment income\n##### (a) Tax on net earnings from self-Employment up to contribution and benefit base and more than $400,000\nParagraph (1) of section 1402(b) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) in the case of the tax imposed by section 1401(a) for any taxable year beginning in a calendar year in which the contribution and benefit base (as determined under section 230 of the Social Security Act) is less than $400,000, the excess (if any) of\u2014 (A) so much of the net earnings from self-employment which is in excess of\u2014 (i) an amount equal to the contribution and benefit base (as determined under section 230 of the Social Security Act) which is effective for the calendar year in which such taxable year begins, reduced (but not below zero) by (ii) the amount of the wages paid to such individual during such taxable year, over (B) the sum of\u2014 (i) the excess (if any) of\u2014 (I) the net earnings from self-employment reduced by the excess (if any) of subparagraph (A)(i) over subparagraph (A)(ii), over (II) $400,000, reduced by such contribution and benefit base, plus (ii) the amount of the wages paid to such individual during such taxable year in excess of such contribution and benefit base and not in excess of $400,000; or .\n##### (b) Further additional hospital insurance tax on very high income taxpayers\n**(1) In general**\nSection 1401(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Further additional tax (A) In general In addition to the tax imposed by paragraphs (1) and (2) and the preceding subsection, there is hereby imposed on every taxpayer (other than a corporation, estate, or trust) for each taxable year a tax equal to 1.2 percent of the self-employment income for such taxable year which is in excess of\u2014 (i) in the case of a joint return, $500,000, (ii) in the case of a married taxpayer (as defined in section 7703) filing a separate return, \u00bd of the dollar amount determined under subparagraph (A), and (iii) in any other case, $400,000. (B) Coordination with FICA The amounts under clause (i), (ii), or (iii) (whichever is applicable) of subparagraph (A) shall be reduced (but not below zero) by the amount of wages taken into account in determining the tax imposed under section 3101(b)(3) with respect to the taxpayer. .\n**(2) No deduction for further additional tax**\n**(A) In general**\nSection 164(f) of such Code is amended by striking section 1401(b)(2) and inserting paragraphs (2) and (3) of section 1401(b) .\n**(B) Deduction for net earnings from self-employment**\nSection 1402(a)(12)(B) of such Code is amended by striking the rate imposed under paragraph (2) of section 1401(b) and inserting the rates imposed under paragraphs (2) and (3) of section 1401(b) .\n**(3) Technical amendment**\nSection 1401(b)(2)(B) of such Code is amended by striking section 3121(b)(2) and inserting section 3101(b)(2) .\n##### (c) Effective date\nThe amendments made by this section shall apply to net earnings from self-employment derived, and taxable years beginning, on or after January 1 of the first calendar year that begins after the date of enactment of this Act.\n#### 4. Taxes on unearned income\n##### (a) Modifications to tax on net investment income\n**(1) In general**\nSection 1411 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Additional amount for certain high income individuals (1) Inclusion of specified net income (A) In general In the case of any individual whose modified adjusted gross income for the taxable year exceeds the high income threshold amount, subsection (a)(1) shall be applied by substituting the greater of specified net income or net investment income for net investment income in subparagraph (A) thereof. (B) Phase-in of increase The increase in the tax imposed under subsection (a)(1) by reason of the application of subparagraph (A) (determined before application of paragraph (2)) shall not exceed the amount which bears the same ratio to the amount of such increase (determined without regard to this paragraph) as\u2014 (i) the excess described in subparagraph (A), bears to (ii) $100,000 ( 1/2 such amount in the case of a married taxpayer (as defined in section 7703) filing a separate return). (2) Additional rate bracket In the case of any individual whose modified adjusted gross income for the taxable year exceeds the high income threshold amount, the amount of tax imposed under subsection (a)(1) shall be increased by an amount equal to 13.6 percent of the lesser of\u2014 (A) the greater of the specified net income or net investment income for the taxable year, or (B) the excess (if any) of\u2014 (i) the modified adjusted gross income for such taxable year, over (ii) the high income threshold amount. (3) Definitions (A) High income threshold amount For purposes of this subsection, the term high income threshold amount means\u2014 (i) except as provided in clause (ii) or (iii), $400,000, (ii) in the case of a taxpayer making a joint return under section 6013 or a surviving spouse (as defined in section 2(a)), $500,000, and (iii) in the case of a married taxpayer (as defined in section 7703) filing a separate return, 1/2 of the dollar amount determined under clause (ii). (B) Specified net income For purposes of this section, the term specified net income means net investment income determined\u2014 (i) without regard to the phrase other than such income which is derived in the ordinary course of a trade or business not described in paragraph (2), in subsection (c)(1)(A)(i), (ii) without regard to the phrase described in paragraph (2) in subsection (c)(1)(A)(ii), (iii) without regard to the phrase other than property held in a trade or business not described in paragraph (2) in subsection (c)(1)(A)(iii), (iv) without regard to paragraphs (2), (3), and (4) of subsection (c), and (v) by treating paragraphs (5) and (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations, in such paragraph (6)) as applying for purposes of subsection (c) of this section. .\n##### (b) Application to trusts and estates\nSection 1411(a)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 3.8 percent and inserting 17.4 percent , and\n**(2)**\nin subparagraph (A) thereof, by striking undistributed net investment income and inserting the greater of undistributed specified net income or undistributed net investment income .\n##### (c) Clarifications with respect to determination of net investment income\n**(1) Certain exceptions**\nSection 1411(c)(6) of the Internal Revenue Code of 1986 is amended to read as follows:\n(6) Special rules Net investment income shall not include\u2014 (A) any item taken into account in determining self-employment income for such taxable year on which a tax is imposed by section 1401(b), (B) wages received with respect to employment on which a tax is imposed under section 3101(b) (determined without regard to section 3101(c)) or 3201(a) (including amounts taken into account under section 3121(v)(2)), and (C) wages received from the performance of services earned outside the United States for a foreign employer. .\n**(2) Net operating losses not taken into account**\nSection 1411(c)(1)(B) of such Code is amended by inserting (other than section 172) after this subtitle .\n**(3) Inclusion of certain foreign income**\n**(A) In general**\nSection 1411(c)(1)(A) of such Code is amended by striking and at the end of clause (ii), by striking over at the end of clause (iii) and inserting and , and by adding at the end the following new clause:\n(iv) any amount includible in gross income under section 951, 951A, 1293, or 1296, over .\n**(B) Proper treatment of certain previously taxed earnings and profits**\nSection 1411(c) of such Code is amended by adding at the end the following new paragraph:\n(7) Certain earnings and profits of foreign corporations (A) In general Except as otherwise provided by the Secretary, a distribution of earnings and profits that is not treated as a dividend for purposes of chapter 1 by reason of section 959(d) or section 1293(c) shall not be treated as a dividend for purposes of this section. (B) Regulations and other guidance The Secretary shall issue regulations or other guidance providing for the treatment of distributions by a foreign corporation after December 31, 2025, of earnings and profits of such foreign corporation which accrued before such date, but which have not been previously subject to tax under this section. .\n##### (d) Transfers of revenues to Old-Age and Survivors, Disability Insurance, and Federal Hospital Insurance Trust Funds\n**(1) Federal Old-Age and Survivors Trust Fund**\n**(A) In general**\nSection 201(a) of the Social Security Act ( 42 U.S.C. 401(a) ) is amended\u2014\n**(i)**\nby striking 100 per centum of ,\n**(ii)**\nby inserting 100 percent of before the taxes each place it appears in paragraphs (1), (2), (3), and (4), and\n**(iii)**\nby striking and at the end of paragraph (3), by striking the period at the end of paragraph (4) and inserting ; and , and by inserting after paragraph (4) the following new paragraph:\n(5) 71.3 percent of the taxes imposed by section 1411 of the Internal Revenue Code of 1986 for any taxable year beginning after December 31, 2025, as determined by the Secretary of the Treasury or the Secretary's delegate based on tax returns under subtitle F of such Code, less the amounts specified in paragraph (3) of subsection (b). .\n**(B) Conforming amendment**\nThe fourth sentence of section 201(a) of such Act ( 42 U.S.C. 401(a) ) is amended by striking clauses (3) and (4) each place it appears and inserting paragraphs (3), (4), and (5) .\n**(2) Federal Disability Insurance Trust Fund**\nSection 201(b) of the Social Security Act ( 42 U.S.C. 401(b) ) is amended\u2014\n**(A)**\nby striking 100 per centum of , and\n**(B)**\nby striking and at the end of paragraph (1), by striking the period at the end of paragraph (2) and inserting ; and , and by inserting after paragraph (2) the following new paragraph:\n(3) 10.3 percent of the taxes imposed by section 1411 of the Internal Revenue Code of 1986 for any taxable year beginning after December 31, 2025, as determined by the Secretary of the Treasury or the Secretary's delegate based on tax returns under subtitle F of such Code. .\n**(3) Federal Hospital Insurance Trust Fund**\nSection 1817(a) of the Social Security Act ( 42 U.S.C. 1395i(a) ) is amended\u2014\n**(A)**\nby striking 100 per centum of ,\n**(B)**\nby inserting 100 percent of before the taxes each place it appears in paragraphs (1) and (2), and\n**(C)**\nby striking and at the end of paragraph (1), by striking the period at the end of paragraph (2) and inserting ; and , and by inserting after paragraph (2) the following new paragraph:\n(3) 28.7 percent of the taxes imposed by section 1411 of the Internal Revenue Code of 1986 for any taxable year beginning after December 31, 2025, as determined by the Secretary of the Treasury or the Secretary's delegate based on tax returns under subtitle F of such Code. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-05-08",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3271",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Medicare and Social Security Fair Share Act",
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
        "updateDate": "2025-06-06T18:24:02Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1690is.xml"
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
      "title": "Medicare and Social Security Fair Share Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medicare and Social Security Fair Share Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase funding for Social Security and Medicare.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:33:16Z"
    }
  ]
}
```
