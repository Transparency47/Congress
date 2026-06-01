# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1357?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1357
- Title: Susan Muffley Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1357
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-04-13T22:20:58Z
- Update date including text: 2026-04-13T22:20:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-13 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1357",
    "number": "1357",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "T000463",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. Turner, Michael R. [R-OH-10]",
        "lastName": "Turner",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Susan Muffley Act of 2025",
    "type": "HR",
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
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-13T14:03:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OH"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "W000806",
      "district": "11",
      "firstName": "Daniel",
      "fullName": "Rep. Webster, Daniel [R-FL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Webster",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WA"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OH"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "GA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OH"
    },
    {
      "bioguideId": "S001213",
      "district": "1",
      "firstName": "Bryan",
      "fullName": "Rep. Steil, Bryan [R-WI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Steil",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "WI"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OH"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "S000929",
      "district": "5",
      "firstName": "Victoria",
      "fullName": "Rep. Spartz, Victoria [R-IN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Spartz",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "IN"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OH"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "FL"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MI"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MI"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-14",
      "state": "MI"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "FL"
    },
    {
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NY"
    },
    {
      "bioguideId": "D000626",
      "district": "8",
      "firstName": "Warren",
      "fullName": "Rep. Davidson, Warren [R-OH-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Davidson",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "OH"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "IN"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-08-26",
      "state": "MI"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AL"
    },
    {
      "bioguideId": "G000591",
      "district": "3",
      "firstName": "Michael",
      "fullName": "Rep. Guest, Michael [R-MS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Guest",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MS"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "MI"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-12-10",
      "state": "OH"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1357ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1357\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Turner of Ohio (for himself, Ms. Kaptur , Ms. Tenney , Ms. Moore of Wisconsin , Mr. Webster of Florida , Mr. Smith of Washington , Mr. Rulli , Mr. Austin Scott of Georgia , Mr. Baird , Mr. Bergman , Mr. Thanedar , Mr. Balderson , Mr. Steil , Mr. Pocan , Mr. Joyce of Ohio , Ms. McDonald Rivet , and Mrs. Spartz ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo increase the benefits guaranteed in connection with certain pension plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Susan Muffley Act of 2025 .\n#### 2. Guaranteed benefit calculation for certain plans\n##### (a) In general\n**(1) Increase to full vested plan benefit**\n**(A) In general**\nFor purposes of determining what benefits are guaranteed under section 4022 of the Employee Retirement Income Security Act of 1974 (in this section referred to as ERISA ) with respect to an eligible participant or beneficiary under a covered plan specified in paragraph (4) in connection with the termination of such plan, the amount of monthly benefits shall be equal to the full vested plan benefit with respect to the participant.\n**(B) No effect on previous determinations**\nNothing in this Act shall be construed to change the allocation of assets and recoveries under sections 4044(a) and 4022(c) of ERISA as previously determined by the Pension Benefit Guaranty Corporation (in the section referred to as the corporation ) for the covered plans specified in paragraph (4), and the corporation\u2019s applicable rules, practices, and policies on benefits payable in terminated single-employer plans shall, except as otherwise provided in this section, continue to apply with respect to such covered plans.\n**(2) Recalculation of certain benefits**\n**(A) In general**\nIn any case in which the amount of monthly benefits with respect to an eligible participant or beneficiary described in paragraph (1) was calculated prior to the date of enactment of this Act, the corporation shall recalculate such amount pursuant to paragraph (1), and shall adjust any subsequent payments of such monthly benefits accordingly, as soon as practicable after such date.\n**(B) Lump-sum payments of past-due benefits**\nNot later than 180 days after the date of enactment of this Act, the corporation, in consultation with the Secretary of the Treasury and the Secretary of Labor, shall make a lump-sum payment to each eligible participant or beneficiary whose guaranteed benefits are recalculated under subparagraph (A) in an amount equal to\u2014\n**(i)**\nin the case of an eligible participant, the excess of\u2014\n**(I)**\nthe total of the full vested plan benefits of the participant for all months for which such guaranteed benefits were paid prior to such recalculation, over\n**(II)**\nthe sum of any applicable payments made to the eligible participant; and\n**(ii)**\nin the case of an eligible beneficiary, the sum of\u2014\n**(I)**\nthe amount that would be determined under clause (i) with respect to the participant of which the eligible beneficiary is a beneficiary if such participant were still in pay status; plus\n**(II)**\nthe excess of\u2014\n**(aa)**\nthe total of the full vested plan benefits of the eligible beneficiary for all months for which such guaranteed benefits were paid prior to such recalculation, over\n**(bb)**\nthe sum of any applicable payments made to the eligible beneficiary.\nNotwithstanding the previous sentence, the corporation shall increase each lump-sum payment made under this subparagraph to account for foregone interest in an amount determined by the corporation designed to reflect a 6 percent annual interest rate on each past-due amount attributable to the underpayment of guaranteed benefits for each month prior to such recalculation.\n**(C) Eligible participants and beneficiaries**\n**(i) In general**\nFor purposes of this section, an eligible participant or beneficiary is a participant or beneficiary who\u2014\n**(I)**\nas of the date of the enactment of this Act, is in pay status under a covered plan or is eligible for future payments under such plan;\n**(II)**\nhas received or will receive applicable payments in connection with such plan (within the meaning of clause (ii)) that does not exceed the full vested plan benefits of such participant or beneficiary; and\n**(III)**\nis not covered by the 1999 agreements between General Motors and various unions providing a top-up benefit to certain hourly employees who were transferred from the General Motors Hourly-Rate Employees Pension Plan to the Delphi Hourly-Rate Employees Pension Plan.\n**(ii) Applicable payments**\nFor purposes of this paragraph, applicable payments to a participant or beneficiary in connection with a plan consist of the following:\n**(I)**\nPayments under the plan equal to the normal benefit guarantee of the participant or beneficiary.\n**(II)**\nPayments to the participant or beneficiary made pursuant to section 4022(c) or otherwise received from the corporation in connection with the termination of the plan.\n**(3) Definitions**\nFor purposes of this subsection\u2014\n**(A) Full vested plan benefit**\nThe term full vested plan benefit means the amount of monthly benefits that would be guaranteed under section 4022 of ERISA as of the date of plan termination with respect to an eligible participant or beneficiary if such section were applied without regard to the phase-in limit in subsection (b)(1) of such Act and the maximum guaranteed benefit limitation in subsection (b)(3) of such Act (including the accrued-at-normal limitation).\n**(B) Normal benefit guarantee**\nThe term normal benefit guarantee means the amount of monthly benefits guaranteed under such section with respect to an eligible participant or beneficiary without regard to this Act.\n**(4) Covered plans**\nThe covered plans specified in this paragraph are the following:\n**(A)**\nThe Delphi Hourly-Rate Employees Pension Plan.\n**(B)**\nThe Delphi Retirement Program for Salaried Employees.\n**(C)**\nThe PHI Non-Bargaining Retirement Plan.\n**(D)**\nThe ASEC Manufacturing Retirement Program.\n**(E)**\nThe PHI Bargaining Retirement Plan.\n**(F)**\nThe Delphi Mechatronic Systems Retirement Program.\n**(5) Treatment of PBGC determinations**\nAny determination made by the corporation under this section concerning a recalculation of benefits or lump-sum payment of past-due benefits shall be subject to administrative review by the corporation. Any new determination made by the corporation under this section shall be governed by the same administrative review process as any other benefit determination by the corporation.\n##### (b) Trust fund for payment of increased benefits\n**(1) Establishment**\nThere is established in the Treasury of the United States a trust fund to be known as the Delphi Full Vested Plan Benefit Trust Fund (hereafter in this subsection referred to as the Fund ), consisting of such amounts as may be appropriated or credited to the Fund as provided in this section.\n**(2) Funding**\nThere is appropriated from the general fund such amounts as are necessary for the costs of the payment of the portion of monthly benefits guaranteed to a participant or beneficiary pursuant to subsection (a) and for necessary administrative and operating expenses of the corporation relating to such payment. The Fund shall be credited with amounts from time to time as the Secretary of the Treasury, in conjunction with the Director of the corporation, determines appropriate, from the general fund of the Treasury.\n**(3) Expenditures from Fund**\nAmounts in the Fund shall be available for the payment of the portion of monthly benefits guaranteed to a participant or beneficiary pursuant to subsection (a) and for necessary administrative and operating expenses of the corporation relating to such payment.\n##### (c) Regulations\nThe corporation, in consultation with the Secretary of the Treasury and the Secretary of Labor, may issue such regulations as necessary to carry out this section.\n##### (d) Tax treatment of lump-Sum payments\n**(1) In general**\nUnless the taxpayer elects (at such time and in such manner as the Secretary may provide) to have this paragraph not apply with respect to any lump-sum payment under subsection (a)(2)(B), the amount of such payment shall be included in the taxpayer\u2019s gross income ratably over the 3-taxable-year period beginning with the taxable year in which such payment is received.\n**(2) Special rules related to death**\n**(A) In general**\nIf the taxpayer dies before the end of the 3-taxable-year period described in paragraph (1), any amount to which paragraph (1) applies which has not been included in gross income for a taxable year ending before the taxable year in which such death occurs shall be included in gross income for such taxable year.\n**(B) Special election for surviving spouses of eligible participants**\nIf\u2014\n**(i)**\na taxpayer with respect to whom paragraph (1) applies dies,\n**(ii)**\nsuch taxpayer is an eligible participant,\n**(iii)**\nthe surviving spouse of such eligible participant is entitled to a survivor benefit from the corporation with respect to such eligible participant, and\n**(iv)**\nsuch surviving spouse elects (at such time and in such manner as the Secretary may provide) the application of this subparagraph,\nsubparagraph (A) shall not apply and any amount which would have (but for such taxpayer\u2019s death) been included in the gross income of such taxpayer under paragraph (1) for any taxable year beginning after the date of such death shall be included in the gross income of such surviving spouse for the taxable year of such surviving spouse ending with or within such taxable year of the taxpayer.",
      "versionDate": "2025-02-13",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-06-04",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "1950",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Susan Muffley Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1895",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Delphi Retirees Pension Restoration Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-22T19:26:22Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2026-01-22T19:26:22Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-01-22T19:26:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Labor and Employment",
        "updateDate": "2025-03-14T11:57:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1357",
          "measure-number": "1357",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2025-09-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1357v00",
            "update-date": "2025-09-09"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Susan Muffley Act of 202</strong><strong>5</strong></p><p>This bill restores the full vested monthly benefits for eligible participants of certain pension plans that were sponsored by Delphi Corporation and terminated as a result of General Motors' bankruptcy in 2009.</p><p>The Pension Benefit Guaranty Corporation (PBGC) must recalculate and adjust each plan participant's monthly benefits payment. The PBGC must also apply the recalculation to previously-made monthly payments and make a lump-sum payment for any additional benefits based on the recalculation.</p><p>The bill establishes and provides appropriations to a fund for the payment of these benefits and specifies how the lump-sum payments are treated for tax purposes.</p>"
        },
        "title": "Susan Muffley Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1357.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Susan Muffley Act of 202</strong><strong>5</strong></p><p>This bill restores the full vested monthly benefits for eligible participants of certain pension plans that were sponsored by Delphi Corporation and terminated as a result of General Motors' bankruptcy in 2009.</p><p>The Pension Benefit Guaranty Corporation (PBGC) must recalculate and adjust each plan participant's monthly benefits payment. The PBGC must also apply the recalculation to previously-made monthly payments and make a lump-sum payment for any additional benefits based on the recalculation.</p><p>The bill establishes and provides appropriations to a fund for the payment of these benefits and specifies how the lump-sum payments are treated for tax purposes.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr1357"
    },
    "title": "Susan Muffley Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Susan Muffley Act of 202</strong><strong>5</strong></p><p>This bill restores the full vested monthly benefits for eligible participants of certain pension plans that were sponsored by Delphi Corporation and terminated as a result of General Motors' bankruptcy in 2009.</p><p>The Pension Benefit Guaranty Corporation (PBGC) must recalculate and adjust each plan participant's monthly benefits payment. The PBGC must also apply the recalculation to previously-made monthly payments and make a lump-sum payment for any additional benefits based on the recalculation.</p><p>The bill establishes and provides appropriations to a fund for the payment of these benefits and specifies how the lump-sum payments are treated for tax purposes.</p>",
      "updateDate": "2025-09-09",
      "versionCode": "id119hr1357"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1357ih.xml"
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
      "title": "Susan Muffley Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Susan Muffley Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To increase the benefits guaranteed in connection with certain pension plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:18:38Z"
    }
  ]
}
```
