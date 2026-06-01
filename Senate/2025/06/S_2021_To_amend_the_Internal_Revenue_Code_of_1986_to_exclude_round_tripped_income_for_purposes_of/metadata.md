# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2021?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2021
- Title: Close the Round-Tripping Loophole Act
- Congress: 119
- Bill type: S
- Bill number: 2021
- Origin chamber: Senate
- Introduced date: 2025-06-11
- Update date: 2025-06-30T17:59:09Z
- Update date including text: 2025-06-30T17:59:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in Senate
- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-11: Introduced in Senate

## Actions

- 2025-06-11 - IntroReferral: Introduced in Senate
- 2025-06-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2021",
    "number": "2021",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Close the Round-Tripping Loophole Act",
    "type": "S",
    "updateDate": "2025-06-30T17:59:09Z",
    "updateDateIncludingText": "2025-06-30T17:59:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
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
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T16:08:40Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "GA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2021is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2021\nIN THE SENATE OF THE UNITED STATES\nJune 11, 2025 Mr. Wyden (for himself, Mr. Warner , Mr. Warnock , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude round-tripped income for purposes of calculating global intangible low-taxed income, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Close the Round-Tripping Loophole Act .\n#### 2. Modification to determination of net deemed intangible income return\n##### (a) In general\nSection 951A(b)(2)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking 10 percent of the aggregate of and inserting\n10 percent of the excess (if any) of\u2014 (i) the aggregate of , and\n**(2)**\nby adding at the end the following new clause:\n(ii) an amount equal to the product of the amount determined under clause (i) and the round-tripping ratio, over .\n##### (b) Round-Tripping ratio\nSection 951A(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Round-tripping ratio For purposes of this subsection\u2014 (A) In general The round-tripping ratio means, with respect to any United States shareholder for any taxable year, the percentage (not greater than 100 percent) which is equal to the ratio which\u2014 (i) the shareholder\u2019s round-tripped net CFC tested income for such taxable year determined under subparagraph (B), bears to (ii) the shareholder\u2019s net CFC tested income for such taxable year, determined without regard to this paragraph. (B) Shareholder\u2019s round-tripped net CFC tested income For purposes of subparagraph (A)(i), a United States shareholder\u2019s round-tripped net CFC tested income for any taxable year is the net CFC tested income of such shareholder which would be determined under subsection (c) for such taxable year if\u2014 (i) the only income taken into account under clause (i) of subsection (c)(2)(A) in determining the tested income or tested loss of each controlled foreign corporation taken into account by such shareholder under subsection (c)(1) for such taxable year were income described in such clause which is derived in connection with\u2014 (I) property\u2014 (aa) which is sold by the taxpayer to any person who is a United States person, or (bb) which the taxpayer cannot establish to the satisfaction of the Secretary is for foreign use, or (II) services provided by the taxpayer which the taxpayer cannot establish to the satisfaction of the Secretary are provided to any person, or with respect to property, not located within the United States, and (ii) the only deductions taken into account under clause (ii) of subsection (c)(2)(A) in determining such tested income or tested loss were deductions properly allocable to income described in clause (i). (C) Foreign use For purposes of this subsection, the determination of whether property is for a foreign use shall be made in the same manner as under section 250(b). (D) Exception for certain small taxpayers (i) In general In the case of any United States shareholder described in clause (ii), the round-tripping ratio shall be 0 percent. (ii) Taxpayer described (I) In general A United States shareholder is described in this clause if the average annual gross receipts of such United States shareholder for the 3-taxable year period ending with the taxable year which precedes such taxable year does not exceed $100,000,000. (II) Application of certain rules Rules similar to the rules of paragraphs (2)(B) and (3) of section 59A(e) shall apply for purposes of this clause. .\n##### (c) Effective date\nThe amendments made by this section shall apply taxable years of foreign corporations beginning after the date of the enactment of this Act, and to taxable years of United States shareholders in which or with which such taxable years of foreign corporations end.\n#### 3. Limitation on deduction for global intangible low-taxed income\n##### (a) In general\nSection 250(a)(1)(B) of the Internal Revenue Code of 1986 is amended to read as follows:\n(B) 50 percent of the excess (if any) of\u2014 (i) the sum of\u2014 (I) the global intangible low-taxed income amount (if any) which is included in the gross income of such domestic corporation under section 951A for such taxable year, and (II) the amount treated as a dividend received by such corporation under section 78 which is attributable to the amount described in subclause (I), over (ii) an amount equal to the product of the amount determined under clause (i) and the round-tripping ratio (as determined under section 951A(b)(3)) of such domestic corporation for such taxable year. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-06-11",
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
        "updateDate": "2025-06-30T17:59:09Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2021is.xml"
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
      "title": "Close the Round-Tripping Loophole Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-21T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Close the Round-Tripping Loophole Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude round-tripped income for purposes of calculating global intangible low-taxed income, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-21T02:48:21Z"
    }
  ]
}
```
