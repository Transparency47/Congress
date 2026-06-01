# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4442
- Title: Save America’s Family Forests Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4442
- Origin chamber: Senate
- Introduced date: 2026-04-29
- Update date: 2026-05-13T15:52:33Z
- Update date including text: 2026-05-13T15:52:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-29: Introduced in Senate
- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-29: Introduced in Senate

## Actions

- 2026-04-29 - IntroReferral: Introduced in Senate
- 2026-04-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-29",
    "latestAction": {
      "actionDate": "2026-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4442",
    "number": "4442",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Save America\u2019s Family Forests Act of 2026",
    "type": "S",
    "updateDate": "2026-05-13T15:52:33Z",
    "updateDateIncludingText": "2026-05-13T15:52:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-29",
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
      "actionDate": "2026-04-29",
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
          "date": "2026-04-29T21:54:03Z",
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
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4442is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4442\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2026 Mr. Cassidy (for himself and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow for limited full expensing of certain reforestation expenditures.\n#### 1. Short title\nThis Act may be cited as the Save America\u2019s Family Forests Act of 2026 .\n#### 2. Modification of reforestation expenditure rules\n##### (a) Increase in base expensing amount\nSection 194(b)(1)(B) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin clause (i), by striking $10,000 and inserting $30,000 , and\n**(2)**\nin clause (ii), by striking $5,000 and inserting $15,000 .\n##### (b) Inflation adjustment for base expensing\nSection 194(b)(1) of such Code is amended by adding at the end the following new subparagraph:\n(C) Inflation adjustment (i) In general In the case of any taxable year beginning after 2026, each dollar amount in subparagraph (B) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (ii) Rounding If any increase determined under clause (i) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after December 31, 2026.\n#### 3. Treatment of reforestation expenditures for qualified natural disasters\n##### (a) In general\nPart VI of subchapter B of chapter 1 of subtitle A of the Internal Revenue Code of 1986 is amended by inserting after section 194A the following new section:\n194B. Treatment of reforestation expenditures for qualified natural disasters (a) In general (1) In general In the case of any qualified timber property with respect to which the taxpayer has made an election under this section, there shall be allowed a deduction for the taxable year in an amount equal to the lesser of\u2014 (A) so much of the disaster-related reforestation expenditures paid or incurred by the taxpayer during such taxable year with respect to each qualified timber property of the taxpayer as does not exceed $500,000 ($250,000 in the case of a married taxpayer filing separately) with respect to any such property, or (B) $1,000,000 ($500,000 in the case of a married taxpayer filing separately), in the aggregate for all qualified timber properties with respect to disaster related-reforestation expenditures. (2) Election An election under this section shall be made at such time and in such manner as the Secretary may prescribe, including on an amended return. (3) Determination of marital status For purposes of this section, marital status shall be determined under section 7703(a). (4) Inflation adjustment (A) In general In the case of any taxable year beginning after 2026, each of the dollar amounts in paragraph (1) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (B) Rounding If any increase under subparagraph (A) is not a multiple of $100, such increase shall be rounded to the nearest multiple of $100. (5) Controlled groups (A) In general In the case of a controlled group of corporations or trades or businesses under common control, the limitations of paragraph (1) shall be allocated among the members of such group in accordance with regulations prescribed by the Secretary. (B) Definition For purposes of subparagraph (A), the term controlled group has the meaning given to the term controlled group of corporations in section 1563(a), except that section 1563(a)(1) shall be applied by substituting more than 50 percent for at least 80 percent in each instance. (C) Pass thru entity In the case of a partnership or S corporation, the aggregate amount described in paragraph (1)(B) shall be applied at the partnership or S corporation level, respectively. (b) Definitions and special rules For purposes of this section\u2014 (1) Disaster-related reforestation expenditures (A) In general The term disaster-related reforestation expenditures means reforestation expenditures paid or incurred in connection with uncut timber that was damaged or destroyed as a direct result of a qualified natural disaster which occurred during the 5-year period ending on the date on which such reforestation occurs, determined without regard\u2014 (i) to any expenditure with respect to which the taxpayer has received reimbursement under any governmental reforestation cost-sharing program unless the amounts so reimbursed have been included in the gross income of the taxpayer, and (ii) any expenditures with respect to which a deduction is allowed under section 194(a). (B) Qualified timber property; reforestation expenditures; cost-sharing programs The terms qualified timber property , reforestation expenditures , and cost-sharing programs have the meanings given such terms in section 194(c). (C) Uncut timber The term uncut timber means, with respect to a qualified natural disaster, standing timber that had not been harvested, severed, or otherwise cut before such qualified natural disaster occurred. (D) Qualified natural disaster The term qualified natural disaster means any disaster determined by the President under section 401 of the Robert T. Stafford Disaster Relief and Emergency Assistance Act. (2) Treatment of trusts and estates The aggregate amount of disaster-related reforestation expenditures incurred by any trust or estate shall be apportioned between the income beneficiaries and the fiduciary under regulations prescribed by the Secretary. (3) Coordination with other deductions No deduction shall be allowed under any other provision other this chapter with respect to any expenditure with respect to which a deduction is allowed or allowable under subsection (a) to the taxpayer. (c) Recapture upon early disposition (1) In general If a taxpayer disposes of any qualified timber property (or any timber thereon) with respect to which a deduction was allowed under subsection (a) within the 10-taxable-year period beginning with the taxable year in which such deduction was claimed, such property shall be treated as section 1245 property, and the amount required to be recaptured as ordinary income shall be determined under section 1245 and included in gross income for the taxable year of disposition. (2) Recapture amount For purposes of applying section 1245, the amount subject to recapture shall not exceed the deduction allowed under subsection (a) with respect to such property. (3) Partial dispositions In the case of a disposition of only a portion of the qualified timber property, the applicable portion of the deduction allowed under subsection (a) shall be subject to recapture under section 1245 in the same proportion that the disposed portion bears to the entire property. (4) Exceptions Paragraph (1) shall not apply to a disposition which occurs by reason of\u2014 (A) casualty, condemnation, or governmental taking, or (B) death of the taxpayer. (d) Regulations The Secretary shall prescribe such regulations as necessary or appropriate to carry out this subsection, including rules for determining proportional allocations. .\n##### (b) Clerical amendment\nThe table of section for part VI of subchapter B of chapter 1 of subtitle A is amended by inserting after the item relating to section 194A the following new item:\nSec. 194B. Treatment of reforestation expenditures for qualified natural disasters. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after December 31, 2026.",
      "versionDate": "2026-04-29",
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
        "actionDate": "2026-04-28",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8538",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Save America\u2019s Family Forests Act of 2026",
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
        "updateDate": "2026-05-13T15:52:32Z"
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
      "date": "2026-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4442is.xml"
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
      "title": "Save America\u2019s Family Forests Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-07T02:38:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Save America\u2019s Family Forests Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-07T02:38:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow for limited full expensing of certain reforestation expenditures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-07T02:33:41Z"
    }
  ]
}
```
