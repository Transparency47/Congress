# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3770?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3770
- Title: Strong Start Act
- Congress: 119
- Bill type: S
- Bill number: 3770
- Origin chamber: Senate
- Introduced date: 2026-02-03
- Update date: 2026-02-23T22:15:49Z
- Update date including text: 2026-02-23T22:15:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in Senate
- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-03: Introduced in Senate

## Actions

- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3770",
    "number": "3770",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000574",
        "district": "",
        "firstName": "Ruben",
        "fullName": "Sen. Gallego, Ruben [D-AZ]",
        "lastName": "Gallego",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Strong Start Act",
    "type": "S",
    "updateDate": "2026-02-23T22:15:49Z",
    "updateDateIncludingText": "2026-02-23T22:15:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T21:53:46Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3770is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3770\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2026 Mr. Gallego introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make new child payments, to provide for American Dream Accounts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strong Start Act .\n#### 2. New child payments\n##### (a) In general\nSubchapter B of chapter 65 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6436. New child payments (a) In general An eligible taxpayer shall be allowed a credit in the amount determined under subsection (b) with respect to each eligible new child of the eligible taxpayer which shall be paid by the Secretary not later than 30 days after the date in which the eligible taxpayer files a claim for such credit. (b) Amount (1) In general The amount of the credit under this subsection with respect to each eligible new child shall be $3,000. (2) Inflation adjustments (A) In general In the case of a taxable year beginning in a calendar year after 2025, the $3,000 dollar amount in paragraph (1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any amount after adjustment under the preceding sentence is not a multiple of $10, such amount shall be rounded to the next lower multiple of $10. (c) Definitions For purposes of this section\u2014 (1) Eligible taxpayer (A) In general The term eligible taxpayer means, with respect to any eligible new child, any taxpayer who\u2014 (i) is the parent (within the meaning of section 152(c)(4)) of the eligible new child, and (ii) who has the same principal place of abode as the eligible new child for the period beginning on the date described in paragraph (2)(A)(i) and ending on the date on which a claim for the credit under this section is made. (B) More than 1 parent claiming eligible new child If the parents claiming any eligible new child do not file a joint claim for the credit under this section together, such child shall be treated as the qualifying child of\u2014 (i) the parent with whom the child resided for the longest period of time described in subparagraph (A)(ii), or (ii) if the child resides with both parents for the same amount of time during such period, the parent with the highest adjusted gross income for the preceding taxable year. (2) Eligible new child (A) In general The term eligible new child means any individual who\u2014 (i) (I) was born to the eligible taxpayer (including through a surrogacy arrangement) after the date of the enactment of this section, (II) has not attained the age of 3 and was adopted by the eligible taxpayer after the date of the enactment of this section, or (III) who has not attained the age of 1 and is placed with the eligible taxpayer by an authorized placement agency or by judgment, decree, or other order of any court of competent jurisdiction after the date of the enactment of this section, (ii) is a citizen or national of the United States, and (iii) who has been issued a social security number (as defined in section 24(h)(7), determined by substituting of the claim for a credit under section 6436 for of such return in clause (ii) thereof). (B) Exception Such term shall not include any individual with respect to whom a credit has been previously allowed under this section to any other person. (d) Taxpayer identification requirement No credit shall be allowed under this section unless the eligible taxpayer has included with the claim for a credit under this section the taxpayer's identification number and such identification number was issued before the date the eligible new child was born or adopted by the taxpayer. (e) Exception from reduction or offset Any payment made to any individual under this section shall not be\u2014 (1) subject to reduction or offset pursuant to subsection (c), (d), (e), or (f) of section 6402 or any similar authority permitting offset, or (2) reduced or offset by other assessed Federal taxes that would otherwise be subject to levy or collection. (f) Restrictions on taxpayers who improperly claimed credit or improperly received payment (1) In general No credit shall be allowed under this section for any taxable year in the disallowance period. (2) Disallowance period For purposes of paragraph (1), the disallowance period is\u2014 (A) the period of 120 calendar months after the most recent calendar month for which there was a final determination that the taxpayer\u2019s claim of credit under this section was due to fraud, and (B) the period of 24 calendar months after the most recent calendar month for which there was a final determination that the taxpayer\u2019s claim of credit under this section was due to reckless or intentional disregard of rules and regulations (but not due to fraud). (g) Regulations The Secretary shall issue such regulations or other guidance as the Secretary determines necessary or appropriate to carry out the purposes of this section, including regulations or guidance with respect to the time and manner for filing a claim for the credit allowed under this section. .\n##### (b) Clerical amendment\nThe table of sections for subchapter B of chapter 65 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 6436. New child payments. .\n#### 3. American dream accounts\n##### (a) Trump accounts renamed American Dream accounts\n**(1) In general**\nEach of the following provisions of the Internal Revenue Code of 1986, as amended by Public Law 119\u201321 , is amended by striking Trump account each place it appears and inserting American Dream account :\n**(A)**\nSection 530A.\n**(B)**\nSection 128.\n**(C)**\nSection 139J.\n**(D)**\nSection 6434.\n**(2) Conforming amendments**\n**(A)**\nSection 530A(h)(4) of the Internal Revenue Code of 1986, as added by Public Law 119\u201321 , is amended by striking Trump Accounts and inserting American Dream accounts .\n**(B)**\nSection 128(c) of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(C)**\nSection 6692(a)(2)(G) of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n##### (b) Permanent extension and indexing of initial government seed contribution program\n**(1) Extension**\nSection 6434(c)(1) of the Internal Revenue Code of 1986, as added by Public Law 119\u201321 , is amended by striking , and before January 1, 2029 .\n**(2) Inflation adjustment**\nSection 6434 of such Code, as added by Public Law 119\u201321 , is amended by adding at the end the following new subsection:\n(j) Inflation adjustment (1) In general In the case of any taxable year beginning after 2026, the $1,000 amount in subsections (a) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (2) Rounding Any increase determined under paragraph (1) shall be rounded to the next nearest multiple of $100. .\n##### (c) Additional government contributions for eligible individuals\n**(1) In general**\nSubchapter B of chapter 65 of the Internal Revenue Code of 1986, as amended by Public Law 119\u201321 , is amended by inserting after section 6434 the following new section:\n6434A. Additional American Dream account contributions (a) In general Each eligible taxpayer shall be treated as making a payment against the tax imposed by subtitle A for the taxable year in an amount equal to the amount determined under subsection (b) with respect to each qualifying child of the taxpayer. (b) Amount (1) In general The amount determined under this subsection with respect to any qualifying child is\u2014 (A) in the case of an eligible taxpayer who is an EITC eligible taxpayer for the taxable year, the sum of\u2014 (i) $750, plus (ii) the amount contributions during the taxable year (not to exceed $250) made to the American Dream account with respect to which the qualifying child is the account beneficiary, and (B) in the case of any other eligible taxpayer, $500. (2) Inflation adjustment (A) In general In the case of any taxable year beginning after 2026, the $750 amount in paragraph (1)(A)(i) and the $500 amount in paragraph (1)(B) shall each be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding Any increase determined under paragraph (1) shall be rounded to the next nearest multiple of $10. (c) Refund of payment The amount treated as a payment under subsection (a) with respect to any qualifying child or the taxpayer shall be paid by the Secretary to the American Dream account with respect to which such qualifying child is the account beneficiary. (d) Definitions and other rules For purposes of this section\u2014 (1) Eligible taxpayer The term eligible taxpayer means, with respect to any taxable year, any taxpayer\u2014 (A) who has a dependent who is a qualifying child, and (B) whose adjusted gross income for the taxable year does not exceed $75,000 ($150,000 in the case of a joint return). (2) EITC eligible taxpayer The term EITC eligible taxpayer means, with respect to any taxable year, an eligible taxpayer who is allowed a credit under section 32 for such taxable year. (3) Qualifying child The term qualifying child means, with respect to any taxable year, any individual who\u2014 (A) is a qualifying child (as defined in section 152(c)) who has not attained the age of 18, (B) is a United States citizen, and (C) is the account beneficiary of an American Dream account. (4) Other rules Rules similar to the rules of subsections (e), (f), (h), and (i) of section 6434 shall apply for purposes of this section. .\n**(2) Application with contribution limits**\nSection 530A(c)(2)(B)(iii) of such Code, as added by Public Law 119\u201321 , is amended by inserting or 6434A after 6434 .\n**(3) Treatment of distributions**\nSection 530A(d)(2)(B) of such Code, as added by Public Law 119\u201321 , is amended by inserting or 6434A after 6434 .\n**(4) Clerical amendment**\nThe table of sections for subchapter B of chapter 65 of such Code, as amended by Public Law 119\u201321 , is amended by inserting after the item relating to section 6434 the following new item:\nSec. 6434A. Additional American Dream account contributions. .\n##### (d) Additional conforming amendments\n**(1)**\nThe heading of part IX of subchapter F of chapter 1 of the Internal Revenue Code of 1986, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(2)**\nThe item relating to section 530A in the table of parts for subchapter F of chapter 1 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(3)**\nThe heading of section 530A of the Internal Revenue Code of 1986, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(4)**\nThe item relating to section 530A in the table of sections for part IX of subchapter F of chapter 1 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(5)**\nThe heading of section 530A(b) of such Code, as added by Public Law 119\u201321 , is amended by striking Trump account and inserting American Dream account .\n**(6)**\nThe heading of section 128 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(7)**\nThe item relating to section 128 in the table of sections for part III of subchapter B of chapter 1 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(8)**\nThe heading of section 139J of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(9)**\nThe item relating to section 139J in the table of sections for part III of subchapter B of chapter 1 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump accounts and inserting American Dream accounts .\n**(10)**\nThe heading of section 6434 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump account contribution pilot program and inserting American Dream account seed contributions .\n**(11)**\nThe item relating to section 6434 in the table of sections for subchapter B of chapter 65 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump account contribution pilot program and inserting American Dream account seed contributions .\n**(12)**\nThe heading of section 6659 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump account contribution pilot program and inserting American Dream account seed contribution .\n**(13)**\nThe item relating to section 128 in the table of sections for part IX of subchapter F of chapter 1 of such Code, as added by Public Law 119\u201321 , is amended by striking Trump account contribution pilot program and inserting American Dream account seed contribution .\n##### (e) Coordination with other means-Tested programs\n**(1) Account funds disregarded for purposes of certain other means-tested federal programs**\nNotwithstanding any other provision of Federal law that requires consideration of 1 or more financial circumstances of an individual, for the purpose of determining eligibility to receive, or the amount of, any assistance or benefit authorized by such provision to be provided to or for the benefit of such individual, any amount (including earnings thereon) in an American Dream account (within the meaning of section 530A of the Internal Revenue Code of 1986) of such individual and any contributions to the American Dream account of the individual shall be disregarded for such purpose with respect to any period before the first day of the calendar year in which such individual attains the age of 18, except that, in the case of the supplemental security income program under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ) any amount (including such earnings) in such American Dream account shall be considered a resource of the designated beneficiary to the extent that such amount exceeds $100,000.\n**(2) Suspension of SSI benefits during periods of excessive account funds**\n**(A) In general**\nThe benefits of an individual under the supplemental security income program under title XVI of the Social Security Act shall not be terminated, but shall be suspended, by reason of excess resources of the individual attributable to an amount in the American Dream account (within the meaning of section 530A of the Internal Revenue Code of 1986) of the individual not disregarded under subsection (a).\n**(B) No impact on medicaid eligibility**\nAn individual who would be receiving payment of such supplemental security income benefits but for the application of paragraph (1) shall be treated for purposes of title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) as if the individual continued to be receiving payment of such benefits.\n##### (f) Automatic enrollment of eligible individuals\nNot later than one year after the date of the enactment of this Act, the Secretary of the Treasury (or the Secretary\u2019s delegate) shall establish a program to\u2014\n**(1)**\ncollect information on whether an individual meets the requirements of subparagraphs (A) and (B) of section 530A(b)(2) of the Internal Revenue Code of 1986, and\n**(2)**\nautomatically establish American Dream accounts (as defined in section 530A of such Code) on behalf of such individual if, based on such information, the Secretary determines such individual is an eligible individual (as defined in section 530A(b)(2)).",
      "versionDate": "2026-02-03",
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
        "updateDate": "2026-02-23T22:15:49Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3770is.xml"
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
      "title": "Strong Start Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strong Start Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make new child payments, to provide for American Dream Accounts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:26Z"
    }
  ]
}
```
