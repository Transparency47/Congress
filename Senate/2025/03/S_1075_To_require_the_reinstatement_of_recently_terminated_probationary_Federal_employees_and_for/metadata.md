# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1075?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1075
- Title: MERIT Act
- Congress: 119
- Bill type: S
- Bill number: 1075
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2025-05-20T18:29:20Z
- Update date including text: 2025-05-20T18:29:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1075",
    "number": "1075",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "A000382",
        "district": "",
        "firstName": "Angela",
        "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
        "lastName": "Alsobrooks",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "MERIT Act",
    "type": "S",
    "updateDate": "2025-05-20T18:29:20Z",
    "updateDateIncludingText": "2025-05-20T18:29:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
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
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T17:21:26Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1075is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1075\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Ms. Alsobrooks (for herself, Mr. Van Hollen , Mr. Warner , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo require the reinstatement of recently terminated probationary Federal employees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Model Employee Reinstatement for Ill-advised Termination Act or the MERIT Act .\n#### 2. Definitions\nIn this Act:\n**(1) Affected probationary employee**\nThe term affected probationary employee means an individual who\u2014\n**(A)**\nwas voluntarily or involuntarily separated from service in an Executive agency as part of a mass termination by an Executive agency during the period beginning on January 20, 2025, and ending on the date of enactment of this Act; and\n**(B)**\nimmediately before the separation described in subparagraph (A)\u2014\n**(i)**\noccupied a position in the competitive service, excepted service, or Senior Executive Service, other than under a temporary appointment; and\n**(ii)**\nwas\u2014\n**(I)**\nserving a probationary or trial period under an initial appointment; or\n**(II)**\notherwise not an employee (as defined in section 7511 of title 5, United States Code) because the individual had not completed the required years of current continuous service.\n**(2) Competitive service**\nThe term competitive service has the meaning given the term in section 2102 of title 5, United States Code.\n**(3) Covered separation**\nThe term covered separation means a separation from Government service that is\u2014\n**(A)**\nan involuntary separation from Government service, other than an involuntary separation for retirement under section 3382 of title 5, United States Code; or\n**(B)**\na voluntary separation from Government service for compensation or other incentives offered by the Federal Government.\n**(4) Excepted service**\nThe term excepted service has the meaning given the term in section 2103 of title 5, United States Code.\n**(5) Executive agency**\nThe term Executive agency has the meaning given the term in section 105 of title 5, United States Code.\n**(6) Former employing agency**\nWith respect to an affected probationary employee, the term former employing agency means the Executive agency from which the separation of the individual made the individual an affected probationary employee.\n**(7) Mass termination**\nThe term mass termination means not less than 15 covered separations from service in an Executive agency during a 30-day period pursuant to the same or related actions, directives, orders, or activities by the Federal Government.\n**(8) Previous Federal position**\nThe term previous Federal position means, with respect to an affected probationary employee, the position in the Federal Government occupied by the affected probationary employee in the former employing agency immediately before becoming an affected probationary employee.\n**(9) Senior Executive Service**\nThe term Senior Executive Service has the meaning given the term in section 2101a of title 5, United States Code.\n#### 3. Reinstatement of affected probationary employees\n##### (a) In general\nEach affected probationary employee, other than an affected probationary employee entitled to a payment under subsection (b), is entitled, in accordance with this Act, to\u2014\n**(1)**\nan appointment to a position in the former employing agency of the affected probationary employee that is the same or similar to the previous Federal position of the affected probationary employee; and\n**(2)**\nif the affected probationary employee elects to accept an appointment under paragraph (1), a payment in an amount equal to the amount that the affected probationary employee would have been paid by the former employing agency of the affected probationary employee during the period beginning on the termination date of the affected probationary employee and ending on the date on which the affected probationary employee is so appointed, if the affected probationary employee had not become an affected probationary employee.\n##### (b) Subsequent Federal employment\n**(1) In general**\nExcept as provided in paragraph (4)\u2014\n**(A)**\nan affected probationary employee that was appointed to a new Federal position and occupies such a position as of the date of enactment of this Act is entitled to the payment described in paragraph (2); and\n**(B)**\nan affected probationary employee that was appointed to a new Federal position and does not hold such a position as of the date of enactment of this Act is entitled to\u2014\n**(i)**\nan appointment to a position in the former employing agency of the affected probationary employee that is the same or similar to the previous Federal position of the affected probationary employee; and\n**(ii)**\nif the affected probationary employee elects to accept an appointment under clause (i), the payment described in paragraph (3).\n**(2) Current Federal employee payment described**\nThe payment described in this paragraph is a payment in an amount equal to the difference between\u2014\n**(A)**\nthe amount that the affected probationary employee would have been paid by the former employing agency of the affected probationary employee during the period beginning on the termination date of the affected probationary employee and ending on the date of enactment of this Act; and\n**(B)**\nthe amount equal to the sum of pay earned by the affected probationary employee in any new Federal position to which the affected probationary employee was appointed during the period described in subparagraph (A).\n**(3) Other affected employee payment**\nThe payment described in this paragraph is a payment in an amount equal to the sum of\u2014\n**(A)**\nthe payment described in subparagraph (2); and\n**(B)**\na payment in an amount equal to the amount that the affected probationary employee would have been paid by the former employing agency of the affected probationary employee during the period beginning on the date of enactment of this Act and ending on the date on which the affected probationary employee is appointed under paragraph (1)(B), if the affected probationary employee had not become an affected probationary employee.\n**(4) Exception**\nAn affected probationary employee is not entitled to a payment under paragraph (1) if the amount of that payment is less than zero.\n**(5) New Federal position defined**\nIn this subsection, the term new Federal position means a position in the Federal Government to which an affected probationary employee is appointed after becoming an affected probationary employee.\n##### (c) Payment\n**(1) In general**\nThe former employing agency of an affected probationary employee shall begin making any payment to which that affected probationary employee is entitled under this section not later than 90 days after the pay for each relevant position is determined in accordance with section 5.\n**(2) Method**\nA payment described in subsection (a) or (b) shall be paid in 1 lump sum.\n**(3) Taxation**\nFor purposes of the Internal Revenue Code of 1986, any payment to an individual under subsection (a) or (b) shall be treated as wages paid with respect to the employment of that individual.\n**(4) Pay limits**\nA payment to an affected probationary employee under this section shall be disregarded with respect to any limit on the pay of employees that is applicable to the affected probationary employee.\n**(5) Reinstatement**\nAn appointment under subsection (a)(1) or (b)(1)(B) to a position in the competitive service shall be made without regard to the provisions of subchapter I of chapter 33 of title 5, United States Code.\n##### (d) Employment benefits\nFor the purposes of this section, a position is the same or similar to a previous Federal position with respect to an affected probationary employee only if the employment benefits, including retirement benefits, health insurance, and leave, available to the affected probationary employee in that position match or exceed the employment benefits available to the affected probationary employee in the previous Federal position of the affected probationary employee.\n#### 4. Notice and selection\n##### (a) Notice\nNot later than 30 days after the date of enactment of this Act, the head of each Executive agency shall notify each affected probationary employee for which the Executive agency is the former employing agency of the rights of affected probationary employees under this Act and the method by which the affected probationary employee may inform that Executive agency of the acceptance or rejection an appointment in accordance with subsection (b)(1).\n##### (b) Selection\n**(1) In general**\nAn affected probationary employee entitled to an appointment under section 3 shall inform the former employing agency of the affected probationary employee of the acceptance or rejection of that appointment by that affected probationary employee not later than 30 days after receiving the notice required by subsection (a).\n**(2) Forfeiture**\nAn affected probationary employee entitled to an appointment under section 3 that does not inform the former employing agency of the affected probationary employee in accordance with paragraph (1) shall cease to be entitled to such an appointment.\n##### (c) Agency compliance\nIf an affected probationary employee accepts an appointment under section 3 and informs the former employing agency of the affected probationary employee of that acceptance in accordance with subsection (b), the head of the former employing agency shall make that appointment not later than 30 days after the affected probationary employee so informs the former employing agency.\n#### 5. Separation treatment\nEach affected probationary employee is deemed to have been involuntarily separated without cause from the previous Federal position of the affected probationary employee.\n#### 6. Payment determination\n##### (a) In general\nFor the purposes of this Act, the Director of the Office of Personnel Management shall determine the pay for a position held by an affected probationary employee based on such evidence of the pay of that position as the affected probationary employee may provide, or if the Director determines sufficient evidence has not been so provided to adequately determine the pay for that position, the pay shall be determined by the Director based on such other information as the Director determines appropriate.\n##### (b) Employee information\nAn affected probationary employee may provide evidence of the pay of a position to the Director of the Office of Personnel Management under subsection (a) until the earlier of\u2014\n**(1)**\nthe date that is 60 days after the date on which the affected probationary employee received the notice described in section 4(a); or\n**(2)**\nthe date on which the Director determines the pay for those positions for the purposes of this Act.\n##### (c) Information sharing\nThe head of each Executive agency shall provide to the Director of the Office of Personnel Management such information as the Director may require to carry out this Act.\n#### 7. Reports\n##### (a) Mass termination report\nNot later than 60 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Homeland Security and Governmental Affairs of the Senate and the Committee on Oversight and Government Reform of the House of Representatives a report on the mass terminations during the period beginning on January 20, 2025, and ending on the date of enactment of this Act, including\u2014\n**(1)**\nthe number of employees (as defined in section 2105 of title 5, United States Code) voluntarily or involuntarily separated from Government service as part of those mass terminations, in total and disaggregated by Executive agency;\n**(2)**\nfor employees described in paragraph (1) that were involuntarily separated from Government service as part of those mass terminations, the reasons provided for those involuntary separations;\n**(3)**\nthe number of affected probationary employees;\n**(4)**\nrecommendations for employees described in paragraph (1), other than affected probationary employees, to which the provisions of this Act should apply; and\n**(5)**\nsuch other information as the Comptroller General determines appropriate.\n##### (b) Reinstatement report\nNot later than 90 days after the date of enactment of this Act, the Director of the Office of Personnel Management shall submit to Congress a report on the reinstatement of affected probationary employees under this Act, including the number of affected probationary employees notified under section 4(a) and the number of affected probationary employees that accepted an appointment under this Act.",
      "versionDate": "2025-03-14",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T18:29:20Z"
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
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1075is.xml"
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
      "title": "MERIT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MERIT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Model Employee Reinstatement for Ill-advised Termination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the reinstatement of recently terminated probationary Federal employees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T03:48:17Z"
    }
  ]
}
```
