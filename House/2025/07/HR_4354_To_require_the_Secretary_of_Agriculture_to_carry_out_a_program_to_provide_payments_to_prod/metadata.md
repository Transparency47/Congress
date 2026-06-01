# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4354?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/4354
- Title: Agricultural Emergency Relief Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4354
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2025-07-29T20:56:56Z
- Update date including text: 2025-07-29T20:56:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/4354",
    "number": "4354",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000460",
        "district": "4",
        "firstName": "Mike",
        "fullName": "Rep. Thompson, Mike [D-CA-4]",
        "lastName": "Thompson",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Agricultural Emergency Relief Act of 2025",
    "type": "HR",
    "updateDate": "2025-07-29T20:56:56Z",
    "updateDateIncludingText": "2025-07-29T20:56:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4354ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4354\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mr. Thompson of California (for himself, Mr. LaMalfa , Mr. Panetta , Mr. Costa , and Mr. Valadao ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to carry out a program to provide payments to producers experiencing certain crop losses as a result of a disaster.\n#### 1. Short title\nThis Act may be cited as the Agricultural Emergency Relief Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Average adjusted gross farm income**\nThe term average adjusted gross farm income , with respect to a producer, means the portion of the average adjusted gross income of the producer that is derived from farming, ranching, or forestry operations.\n**(2) Average adjusted gross income**\nThe term average adjusted gross income , with respect to a producer, means the adjusted gross income (as defined in section 62 of the Internal Revenue Code of 1986) of the producer, as averaged over the 3 taxable years preceding the most recently completed taxable year.\n**(3) Disaster**\n**(A) In general**\nThe term disaster includes\u2014\n**(i)**\na drought;\n**(ii)**\na wildfire;\n**(iii)**\na hurricane;\n**(iv)**\na flood;\n**(v)**\na derecho;\n**(vi)**\nexcessive heat;\n**(vii)**\nexcessive moisture;\n**(viii)**\na winter storm; and\n**(ix)**\na freeze event (including a polar vortex).\n**(B) Determination of drought**\nFor purposes of subparagraph (A)(i), a county shall be considered to have experienced a drought if any area within the county was rated by the U.S. Drought Monitor as experiencing\u2014\n**(i)**\na D2-level drought (commonly known as severe drought ) for 8 or more consecutive weeks; or\n**(ii)**\na D3-level drought (commonly known as extreme drought ), or a higher level of drought intensity, during the applicable calendar year.\n**(4) Federal Crop Insurance**\nThe term Federal Crop Insurance means any crop insurance program under the Federal Crop Insurance Act ( 7 U.S.C. 1501 et seq. ).\n**(5) Noninsured Crop Disaster Assistance Program**\nThe term Noninsured Crop Disaster Assistance Program means the program under section 196 of the Federal Agriculture Improvement and Reform Act of 1996 ( 7 U.S.C. 7333 ).\n**(6) Producer**\n**(A) In general**\nThe term producer means an individual or entity that is eligible to receive assistance under a disaster assistance program administered by the Farm Service Agency.\n**(B) Exclusions**\nThe term producer does not include\u2014\n**(i)**\na joint venture; or\n**(ii)**\na general partnership.\n**(7) Qualified loss**\n**(A) In general**\nThe term qualified loss means a loss in a crop, trees, bushes, or vines incurred by a producer as a consequence of a disaster.\n**(B) Inclusions**\nThe term qualified loss includes\u2014\n**(i)**\na loss incurred by a producer as a result of being prevented from planting a crop due to a disaster;\n**(ii)**\na loss in the quality of a crop, trees, bushes, or vines due to a disaster; and\n**(iii)**\na loss in the quality of a crop (including wine grapes), trees, bushes, or vines due to smoke exposure from a wildfire.\n**(8) Secretary**\nThe term Secretary means the Secretary of Agriculture.\n#### 3. Emergency relief program\n##### (a) Establishment\nThe Secretary shall establish a program under which the Secretary shall provide payments during each crop year to producers that experienced a qualified loss during the crop year.\n##### (b) Application\n**(1) In general**\nTo be eligible to receive a payment under this section for a crop year, a producer shall submit to the Secretary an application, at such time, in such manner, and containing such information as the Secretary may require, including a description of each qualified loss incurred by the producer during the crop year.\n**(2) Approval**\nThe Secretary shall approve an application submitted by a producer under paragraph (1) if the application demonstrates to the satisfaction of the Secretary that the producer has incurred a qualified loss during the applicable crop year.\n##### (c) Provision of payments\n**(1) In general**\nThe Secretary shall provide to each producer the application of whom is approved under subsection (b)(2) a payment for the applicable crop year, in accordance with subsection (d).\n**(2) Requirement to purchase insurance**\nAs a condition of receiving a payment under this section, a producer shall purchase, for each of the 2 succeeding crop years\u2014\n**(A)**\nFederal Crop Insurance, if available; or\n**(B)**\nif Federal Crop Insurance is not available, coverage under the Noninsured Crop Disaster Assistance Program.\n##### (d) Amount of payments\n**(1) In general**\nSubject to subsection (e), the amount of a payment provided to a producer under subsection (c)(1) shall be determined in accordance with\u2014\n**(A)**\nto the maximum extent practicable, a calculation based on data relating to the producer for the applicable crop year that were previously submitted or known to the Secretary, including\u2014\n**(i)**\nany indemnity of the producer under Federal Crop Insurance or payment received by the producer under the Noninsured Crop Disaster Assistance Program;\n**(ii)**\nthe level of coverage of the producer under\u2014\n**(I)**\nFederal Crop Insurance; or\n**(II)**\nthe Noninsured Crop Disaster Assistance Program; and\n**(iii)**\nan appropriate percentage factor, to be established by the Secretary, subject to the condition that the factor shall be not more than 90 percent; or\n**(B)**\nfor a producer that did not purchase coverage under Federal Crop Insurance or the Noninsured Crop Disaster Assistance Program, a calculation based on the revenue of the producer for the applicable crop year, as described in paragraph (2).\n**(2) Revenue-based calculation**\n**(A) Definitions**\nIn this paragraph:\n**(i) Allowable gross revenue**\nThe term allowable gross revenue , with respect to a producer, means the reported revenue of the operations of the producer during a crop year, including from\u2014\n**(I)**\nsales of eligible crops, as identified by the Secretary; or\n**(II)**\nsales resulting from value added in post-production activities.\n**(ii) Benchmark year**\nThe term benchmark year means a crop year in which a producer did not experience a qualified loss.\n**(iii) Disaster year**\nThe term disaster year means a crop year in which a producer experiences a qualified loss.\n**(B) Factors for consideration**\nSubject to subparagraph (C), the revenue-based calculation referred to in paragraph (1)(B) shall take into account\u2014\n**(i)**\nthe allowable gross revenue of the applicable producer during a benchmark year;\n**(ii)**\nthe allowable gross revenue of the applicable producer during the disaster year for which the payment is provided under this section;\n**(iii)**\nthe percentage of the allowable gross revenue described in clause (ii) derived from sales of specialty crops and high-value crops; and\n**(iv)**\nan appropriate percentage factor, to be established by the Secretary, subject to the condition that the factor shall be not more than 70 percent.\n**(C) Vertical integration for producers of wine grapes**\nFor a producer of wine grapes that uses not less than 75 percent of the grapes to produce wine at a facility owned by the producer, a payment provided under this section shall be calculated based on the market rate for wine grapes at the time of calculation, in lieu of the revenue of the producer.\n##### (e) Limitations\nFor each crop year\u2014\n**(1)**\na producer the average adjusted gross farm income of whom is less than 75 percent may receive payments under this section in an amount equal to not more than\u2014\n**(A)**\n$125,000 for the specialty crops and high-value crops of the producer, as determined by the Secretary; and\n**(B)**\n$125,000 for the crops of the producer not described in subparagraph (A);\n**(2)**\na producer the average adjusted gross farm income of whom is 75 percent or more may receive payments under this section in an amount equal to not more than\u2014\n**(A)**\n$900,000 for the specialty crops and high-value crops of the producer, as determined by the Secretary; and\n**(B)**\n$250,000 for the crops of the producer not described in subparagraph (A); and\n**(3)**\nthe total amount of all payments provided to a producer under this section shall be not more than, as applicable\u2014\n**(A)**\nan amount equal to 90 percent of the qualified losses of the producer during the crop year, including any assistance provided under\u2014\n**(i)**\nFederal Crop Insurance; or\n**(ii)**\nthe Noninsured Crop Disaster Assistance Program; or\n**(B)**\nan amount equal to 70 percent of the qualified losses of the producer during the crop year, if the producer did not\u2014\n**(i)**\nobtain a policy or plan of insurance under Federal Crop Insurance for the crops, trees, bushes, or vines incurring the qualified losses; or\n**(ii)**\nfile any required paperwork or pay any service fee under the Noninsured Crop Disaster Assistance Program by the applicable State filing deadline for a noninsurable commodity incurring the qualified losses.\n##### (f) Timing\nThe Secretary shall administer the program under this section simultaneously for\u2014\n**(1)**\nproducers submitting applications using indemnity-based calculations, as described in subsection (d)(1)(A); and\n**(2)**\nproducers submitting applications using revenue-based calculations, as described in subsection (d)(1)(B).\n#### 4. Authorization of appropriations\n##### (a) In general\nThere are authorized to be appropriated to the Secretary such sums as are necessary to carry out this Act for each of fiscal years 2025 through 2030.\n##### (b) Administrative costs\nOf the amounts made available under subsection (a) for each fiscal year, the Secretary may use not more than 1 percent to pay the administrative costs of the Secretary.",
      "versionDate": "2025-07-10",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-29T20:56:56Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4354ih.xml"
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
      "title": "Agricultural Emergency Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Agricultural Emergency Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to carry out a program to provide payments to producers experiencing certain crop losses as a result of a disaster.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T04:48:48Z"
    }
  ]
}
```
