# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7865?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7865
- Title: American Consumer Tariff Rebate Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7865
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-03-11T23:01:17Z
- Update date including text: 2026-03-11T23:01:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7865",
    "number": "7865",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001063",
        "district": "28",
        "firstName": "Henry",
        "fullName": "Rep. Cuellar, Henry [D-TX-28]",
        "lastName": "Cuellar",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "American Consumer Tariff Rebate Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-11T23:01:17Z",
    "updateDateIncludingText": "2026-03-11T23:01:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:00:30Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7865ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7865\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Cuellar introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo provide direct refunds to taxpayers for increased consumer costs attributable to tariffs imposed without congressional authorization.\n#### 1. Short title\nThis Act may be cited as the American Consumer Tariff Rebate Act of 2026 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArticle I, Section 8 of the Constitution vests exclusively in Congress the authority to lay and collect duties and tariffs.\n**(2)**\nDuties imposed pursuant to Presidential action under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) without express congressional authorization resulted in increased consumer prices nationwide.\n**(3)**\nThe Congressional Budget Office and the Joint Economic Committee have estimated that total consumer costs attributable to such tariffs are approximately $231,350,000,000.\n**(4)**\nCongress has a responsibility to provide direct restitution to taxpayers for these unlawful cost increases, and to prioritize working families by excluding very high-income taxpayers and using the resulting savings to increase refunds for taxpayers raising children.\n#### 3. Definitions\nIn this Act:\n**(1) Covered tariffs**\nThe term covered tariffs means duties imposed pursuant to Presidential action under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) that were subsequently determined to lack congressional authorization.\n**(2) Eligible return**\nThe term eligible return means a Federal individual income tax return filed for the most recent taxable year for which sufficient information is available, including returns filed as\u2014\n**(A)**\nsingle;\n**(B)**\nmarried filing jointly;\n**(C)**\nmarried filing separately;\n**(D)**\nhead of household; or\n**(E)**\nqualifying surviving spouse.\n**(3) Qualified child**\nThe term qualified child has the meaning given in section 24(c) of the Internal Revenue Code of 1986.\n**(4) Secretary**\nThe term Secretary means the Secretary of the Treasury or the Secretary\u2019s delegate.\n#### 4. Establishment of taxpayer rebate\n##### (a) In general\nThe Secretary shall provide a one-time direct payment to each Eligible Return in accordance with this section.\n##### (b) Income limitation\nNo payment shall be made under this Act with respect to any return reporting adjusted gross income exceeding $400,000 for the most recent taxable year for which sufficient information is available.\n##### (c) Aggregate limitation\nThe total amount of payments made under this Act shall not exceed $231,350,000,000.\n##### (d) Determination of base amount\n**(1)**\nThe Secretary shall determine a Base Amount such that, if payments were made under subsection (e) with respect to all Eligible Returns (without regard to subsection (b)), the total amount of such payments would equal $231,350,000,000.\n**(2)**\nIn calculating the Base Amount, the Secretary shall calculate such amount by dividing $231,350,000,000 by the sum of\u2014\n**(A)**\nthe number of Eligible Returns filed as single;\n**(B)**\nthe number of Eligible Returns filed as married filing separately;\n**(C)**\n1.5 multiplied by the number of Eligible Returns filed as head of household; and\n**(D)**\n2 multiplied by the sum of\u2014\n**(i)**\nthe number of Eligible Returns filed as married filing jointly; and\n**(ii)**\nthe number of Eligible Returns filed as qualifying surviving spouse.\n##### (e) Payment amounts by filing status\nSubject to subsection (b), the payment for an Eligible Return shall be\u2014\n**(1)**\nin the case of a return filed as single, an amount equal to 100 percent of the Base Amount;\n**(2)**\nin the case of a return filed as married filing separately, an amount equal to 100 percent of the Base Amount;\n**(3)**\nin the case of a return filed as head of household, an amount equal to 150 percent of the Base Amount;\n**(4)**\nin the case of a return filed as married filing jointly, an amount equal to 200 percent of the Base Amount; or\n**(5)**\nin the case of a return filed as qualifying surviving spouse, an amount equal to 200 percent of the Base Amount.\n#### 5. Child bonus funded by high-income exclusion\n##### (a) In general\nIn addition to any amount paid under section 4, the Secretary shall pay a Child Bonus with respect to any Eligible Return that\u2014\n**(1)**\nis not excluded under section 4(b); and\n**(2)**\nclaims one or more Qualified Children.\n##### (b) Fixed amount\nThe Child Bonus shall be equal to $125 for each Qualified Child claimed on such return.\n##### (c) Funding and cap\n**(1) Use of savings**\nAmounts paid under this section shall be paid solely from amounts not paid due to the income limitation under section 4(b).\n**(2) Limitation**\nTotal payments under this section, together with total payments under section 4, shall not exceed $231,350,000,000.\n##### (d) Proration authority\nIf the Secretary determines that the amount available under subsection (c)(1) is insufficient to pay the full Child Bonus amounts specified in subsection (b), the Secretary shall reduce each Child Bonus payment on a pro rata basis so that the aggregate limitation under section 4(c) is not exceeded.\n##### (e) Coordination\nThe Secretary shall, to the maximum extent practicable, disburse the Child Bonus as part of the same payment as the section 4 rebate.\n#### 6. Method of distribution\n##### (a) Automatic distribution\nPayments shall be issued automatically using information available to the Internal Revenue Service.\n##### (b) Means of payment\nPayments may be made by\u2014\n**(1)**\ndirect deposit;\n**(2)**\npaper check; or\n**(3)**\nprepaid debit card.\n##### (c) Non-filers\nThe Secretary shall establish a simplified filing procedure for individuals who did not file a return for the most recent taxable year but would otherwise have been eligible to file.\n#### 7. Administration\n##### (a)\nThe Secretary may prescribe such guidance, regulations, and procedures as are necessary to carry out this Act.\n##### (b)\nThe Secretary may round payment amounts to the nearest whole dollar or other administratively practical increment and shall implement such rounding in a manner that does not cause total payments to exceed $231,350,000,000.\n#### 8. Report to Congress\nNot later than 90 days after enactment, and every 60 days thereafter until all payments are distributed, the Secretary shall submit to Congress a report detailing\u2014\n**(1)**\nthe number of payments issued by filing status under section 4;\n**(2)**\nthe number of returns receiving a Child Bonus and the aggregate number of Qualified Children claimed for purposes of section 5;\n**(3)**\nthe total amount disbursed under section 4 and under section 5; and\n**(4)**\nthe remaining unobligated balance, if any, under the $231,350,000,000 aggregate limitation.",
      "versionDate": "2026-03-09",
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
        "updateDate": "2026-03-11T23:01:16Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7865ih.xml"
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
      "title": "American Consumer Tariff Rebate Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-10T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "American Consumer Tariff Rebate Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-10T08:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide direct refunds to taxpayers for increased consumer costs attributable to tariffs imposed without congressional authorization.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-10T08:18:31Z"
    }
  ]
}
```
