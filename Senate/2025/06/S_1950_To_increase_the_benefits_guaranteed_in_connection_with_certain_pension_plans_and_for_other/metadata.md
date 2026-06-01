# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1950?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1950
- Title: Susan Muffley Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1950
- Origin chamber: Senate
- Introduced date: 2025-06-04
- Update date: 2026-04-13T22:20:58Z
- Update date including text: 2026-04-13T22:20:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-04: Introduced in Senate
- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-06-04: Introduced in Senate

## Actions

- 2025-06-04 - IntroReferral: Introduced in Senate
- 2025-06-04 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-04",
    "latestAction": {
      "actionDate": "2025-06-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1950",
    "number": "1950",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Susan Muffley Act of 2025",
    "type": "S",
    "updateDate": "2026-04-13T22:20:58Z",
    "updateDateIncludingText": "2026-04-13T22:20:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-04",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-04",
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
          "date": "2025-06-04T21:20:28Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "NY"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "OH"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "MI"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "WI"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-06-04",
      "state": "MS"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-09",
      "state": "IN"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-23",
      "state": "MS"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
      "state": "NY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-07-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1950is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1950\nIN THE SENATE OF THE UNITED STATES\nJune 4, 2025 Mr. Husted (for himself, Mrs. Gillibrand , Mr. Moreno , Mr. Peters , Mr. Fetterman , Ms. Baldwin , and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo increase the benefits guaranteed in connection with certain pension plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Susan Muffley Act of 2025 .\n#### 2. Guaranteed benefit calculation for certain plans\n##### (a) In general\n**(1) Increase to full vested plan benefit**\n**(A) In general**\nFor purposes of determining what benefits are guaranteed under section 4022 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1322 ) with respect to an eligible participant or beneficiary under a covered plan specified in paragraph (4) in connection with the termination of such plan, the amount of monthly benefits shall be equal to the full vested plan benefit with respect to the participant.\n**(B) No effect on previous determinations**\nNothing in this Act shall be construed to change the allocation of assets and recoveries under sections 4044(a) and 4022(c) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1344(a) ; 1322(c)) as previously determined by the Pension Benefit Guaranty Corporation (referred to in this section as the corporation ) for the covered plans specified in paragraph (4), and the corporation\u2019s applicable rules, practices, and policies on benefits payable in terminated single-employer plans shall, except as otherwise provided in this section, continue to apply with respect to such covered plans.\n**(2) Recalculation of certain benefits**\n**(A) In general**\nIn any case in which the amount of monthly benefits with respect to an eligible participant or beneficiary described in paragraph (1) was calculated prior to the date of enactment of this Act, the corporation shall recalculate such amount pursuant to paragraph (1), and shall adjust any subsequent payments of such monthly benefits accordingly, as soon as practicable after such date.\n**(B) Lump-sum payments of past-due benefits**\nNot later than 180 days after the date of enactment of this Act, the corporation, in consultation with the Secretary of the Treasury and the Secretary of Labor, shall make a lump-sum payment to each eligible participant or beneficiary whose guaranteed benefits are recalculated under subparagraph (A) in an amount equal to\u2014\n**(i)**\nin the case of an eligible participant, the excess of\u2014\n**(I)**\nthe total of the full vested plan benefits of the participant for all months for which such guaranteed benefits were paid prior to such recalculation, over\n**(II)**\nthe sum of any applicable payments made to the eligible participant; and\n**(ii)**\nin the case of an eligible beneficiary, the sum of\u2014\n**(I)**\nthe amount that would be determined under clause (i) with respect to the participant of which the eligible beneficiary is a beneficiary if such participant were still in pay status; plus\n**(II)**\nthe excess of\u2014\n**(aa)**\nthe total of the full vested plan benefits of the eligible beneficiary for all months for which such guaranteed benefits were paid prior to such recalculation, over\n**(bb)**\nthe sum of any applicable payments made to the eligible beneficiary.\nNotwithstanding\n                            the previous sentence, the corporation shall increase each lump-sum\n                            payment made under this subparagraph to account for foregone interest in\n                            an amount determined by the corporation designed to reflect a 6 percent\n                            annual interest rate on each past-due amount attributable to the\n                            underpayment of guaranteed benefits for each month prior to such\n                            recalculation.\n**(C) Eligible participants and beneficiaries**\n**(i) In general**\nFor purposes of this section, an eligible participant or beneficiary is a participant or beneficiary who\u2014\n**(I)**\nas of the date of the enactment of this Act, is in pay status under a covered plan or is eligible for future payments under such plan;\n**(II)**\nhas received or will receive applicable payments in connection with such plan (within the meaning of clause (ii)) that does not exceed the full vested plan benefits of such participant or beneficiary; and\n**(III)**\nis not covered by the 1999 agreements between General Motors and various unions providing a top-up benefit to certain hourly employees who were transferred from the General Motors Hourly-Rate Employees Pension Plan to the Delphi Hourly-Rate Employees Pension Plan.\n**(ii) Applicable payments**\nFor purposes of this paragraph, applicable payments to a participant or beneficiary in connection with a plan consist of the following:\n**(I)**\nPayments under the plan equal to the normal benefit guarantee of the participant or beneficiary.\n**(II)**\nPayments to the participant or beneficiary made pursuant to section 4022(c) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1322(c) ) or otherwise received from the corporation in connection with the termination of the plan.\n**(3) Definitions**\nFor purposes of this subsection\u2014\n**(A) Full vested plan benefit**\nThe term full vested plan benefit means the amount of monthly benefits that would be guaranteed under section 4022 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1322 ) as of the date of plan termination with respect to an eligible participant or beneficiary if such section were applied without regard to the phase-in limit under subsection (b)(1) of such section and the maximum guaranteed benefit limitation under subsection (b)(3) of such section (including the accrued-at-normal limitation).\n**(B) Normal benefit guarantee**\nThe term normal benefit guarantee means the amount of monthly benefits guaranteed under section 4022 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1322 ) with respect to an eligible participant or beneficiary without regard to this Act.\n**(4) Covered plans**\nThe covered plans specified in this paragraph are the following:\n**(A)**\nThe Delphi Hourly-Rate Employees Pension Plan.\n**(B)**\nThe Delphi Retirement Program for Salaried Employees.\n**(C)**\nThe PHI Non-Bargaining Retirement Plan.\n**(D)**\nThe ASEC Manufacturing Retirement Program.\n**(E)**\nThe PHI Bargaining Retirement Plan.\n**(F)**\nThe Delphi Mechatronic Systems Retirement Program.\n**(5) Treatment of PBGC determinations**\nAny determination made by the corporation under this section concerning a recalculation of benefits or lump-sum payment of past-due benefits shall be subject to administrative review by the corporation. Any new determination made by the corporation under this section shall be governed by the same administrative review process as any other benefit determination by the corporation.\n##### (b) Trust fund for payment of increased benefits\n**(1) Establishment**\nThere is established in the Treasury a trust fund to be known as the Delphi Full Vested Plan Benefit Trust Fund (referred to in this subsection as the Fund ), consisting of such amounts as may be appropriated or credited to the Fund as provided in this section.\n**(2) Funding**\nThere is appropriated, out of amounts in the Treasury not otherwise appropriated, such amounts as are necessary for the costs of payments of the portions of monthly benefits guaranteed to participants and beneficiaries pursuant to subsection (a) and for necessary administrative and operating expenses of the corporation relating to such payments. The Fund shall be credited with amounts from time to time as the Secretary of the Treasury, in coordination with the Director of the corporation, determines appropriate, out of amounts in the Treasury not otherwise appropriated.\n**(3) Expenditures from Fund**\nAmounts in the Fund shall be available for the payment of the portion of monthly benefits guaranteed to a participant or beneficiary pursuant to subsection (a) and for necessary administrative and operating expenses of the corporation relating to such payment.\n##### (c) Regulations\nThe corporation, in consultation with the Secretary of the Treasury and the Secretary of Labor, may issue such regulations as necessary to carry out this section.",
      "versionDate": "2025-06-04",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1357",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Susan Muffley Act of 2025",
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
        "name": "Labor and Employment",
        "updateDate": "2025-06-25T12:23:13Z"
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
      "date": "2025-06-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1950is.xml"
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
      "title": "Susan Muffley Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Susan Muffley Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-12T04:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to increase the benefits guaranteed in connection with certain pension plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-12T04:48:22Z"
    }
  ]
}
```
