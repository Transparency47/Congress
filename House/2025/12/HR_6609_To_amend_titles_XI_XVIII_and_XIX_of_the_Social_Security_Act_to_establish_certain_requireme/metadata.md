# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6609?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6609
- Title: Pharmacists Fight Back in Medicare and Medicaid Act
- Congress: 119
- Bill type: HR
- Bill number: 6609
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-15T08:08:28Z
- Update date including text: 2026-05-15T08:08:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6609",
    "number": "6609",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "A000148",
        "district": "4",
        "firstName": "Jake",
        "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
        "lastName": "Auchincloss",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Pharmacists Fight Back in Medicare and Medicaid Act",
    "type": "HR",
    "updateDate": "2026-05-15T08:08:28Z",
    "updateDateIncludingText": "2026-05-15T08:08:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:00:10Z",
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
          "date": "2025-12-11T16:00:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TN"
    },
    {
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "KY"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AZ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "PA"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MI"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "TN"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-12-11",
      "state": "AL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "VA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "WI"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "GA"
    },
    {
      "bioguideId": "M001143",
      "district": "4",
      "firstName": "Betty",
      "fullName": "Rep. McCollum, Betty [D-MN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McCollum",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000821",
      "district": "4",
      "firstName": "Bruce",
      "fullName": "Rep. Westerman, Bruce [R-AR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Westerman",
      "party": "R",
      "sponsorshipDate": "2025-12-23",
      "state": "AR"
    },
    {
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "GA"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "KY"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "ID"
    },
    {
      "bioguideId": "M001228",
      "district": "2",
      "firstName": "Celeste",
      "fullName": "Rep. Maloy, Celeste [R-UT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Maloy",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "UT"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "KY"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "MI"
    },
    {
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2026-01-09",
      "state": "TX"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "GA"
    },
    {
      "bioguideId": "R000575",
      "district": "3",
      "firstName": "Mike",
      "fullName": "Rep. Rogers, Mike D. [R-AL-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AL"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "AL"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
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
      "sponsorshipDate": "2026-04-14",
      "state": "AL"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "KS"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "False",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "MI"
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
      "sponsorshipDate": "2026-05-04",
      "state": "NY"
    },
    {
      "bioguideId": "P000609",
      "district": "6",
      "firstName": "Gary",
      "fullName": "Rep. Palmer, Gary J. [R-AL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Palmer",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "AL"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6609ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6609\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Auchincloss (for himself, Mrs. Harshbarger , Mr. Comer , Mr. Carter of Georgia , Mr. Ciscomani , Mr. Moulton , Mr. Deluzio , Mr. Peters , Ms. Tlaib , Ms. Budzinski , Mr. Krishnamoorthi , Mr. Khanna , Mr. Lynch , Mr. Goldman of Texas , Mr. Cohen , Ms. Pressley , Mr. Vicente Gonzalez of Texas , Mr. Moore of Alabama , Mr. Subramanyam , Mr. Pocan , Mr. Bishop , and Ms. McCollum ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles XI, XVIII, and XIX of the Social Security Act to establish certain requirements under Medicare and Medicaid with respect to prescription drug benefits and pharmacy benefit managers.\n#### 1. Short title\nThis Act may be cited as the Pharmacists Fight Back in Medicare and Medicaid Act .\n#### 2. Establishing certain requirements with respect to PBMs\n##### (a) Medicare\n**(1) Prescription drug plans**\nSection 1860D\u201312 of the Social Security Act ( 42 U.S.C. 1395w\u2013112 ) is amended by adding at the end the following new subsection:\n(h) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2027: (1) In general Each contract entered into with a PDP sponsor under this part with respect to a prescription drug plan offered by such sponsor shall provide\u2014 (A) that the sponsor (and any pharmacy benefit manager acting on behalf of such sponsor, including any affiliate of such PBM, as applicable)\u2014 (i) shall comply with the pharmacy payment requirements described in paragraph (2) ; (ii) shall comply with the rebate pass-through requirements described in paragraph (3) ; (iii) shall comply with the reporting requirement described in paragraph (4) ; and (iv) may not engage in steering; and (B) that any pharmacy benefit manager acting on behalf of such sponsor has a written agreement with the PDP sponsor under which the PBM, and any affiliate of such PBM, as applicable, agrees to meet the requirements described in subparagraph (A). (2) Pharmacy payment requirements For purposes of paragraph (1)(A)(i) , the pharmacy payment requirements described in this paragraph are, with respect to a PDP sponsor (and a PBM acting on behalf of such sponsor, including any affiliate of such PBM, as applicable) the following: (A) The sponsor, PBM, or affiliate reimburses an in-network pharmacy for the ingredient cost of a covered part D drug in an amount equal to the sum of\u2014 (i) the national average drug acquisition cost for the drug as of the day that the pharmacy submits a claim for payment for such drug (as determined based upon the retail survey prices obtained under section 1927(f)(1)), or, in the case of a drug for which no such national average drug acquisition cost is available, the wholesale acquisition cost for such drug as of such day; and (ii) an amount equal to 4 percent of the amount described in clause (i), or $50, whichever is less. (B) With respect to each covered part D drug obtained from an in-network pharmacy by an individual enrolled in the prescription drug plan, the sponsor, PBM, or affiliate\u2014 (i) pays such pharmacy a dispensing fee that is equal to the dispensing fee paid for such drug under the State plan under title XIX in the State in which such pharmacy is located, as reported by the State under section 1927(f)(2); and (ii) does not require such individual to reimburse such dispensing fee or otherwise increase the amount owed by such individual with respect to such drug to account for such dispensing fee. (C) The sponsor, PBM, or affiliate does not impose any fee or other payment requirement upon an in-network pharmacy that would have the effect of reducing the amount received by the pharmacy under the other provisions of this paragraph. (3) Rebate pass-through requirements For purposes of paragraph (1)(A)(ii) , the rebate pass-through requirements described in this paragraph are, with respect to a PDP sponsor (and a PBM acting on behalf of such sponsor, including any affiliate of such PBM, as applicable), that, in the case that such sponsor, PBM, or affiliate receives a manufacturer rebate in connection with a covered part D drug\u2014 (A) in the case that such drug is obtained from an in-network pharmacy by an individual enrolled in the prescription drug plan, the PDP sponsor, PBM, or affiliate applies, at the point of sale of such drug, a reduction to the amount of any coinsurance or copayment owed by such individual with respect to such drug, such that the amount of coinsurance or copayment so owed is calculated based on an amount equal to the reimbursement amount for such drug determined under paragraph (2)(A) , less the amount of such rebate (or, in the case of a rebate described in paragraph (5)(B)(ii), the amount of such rebate that is attributable to such drug and such individual); and (B) in the case that the entity receiving the manufacturer rebate in connection with such drug is a PBM (or any affiliate of such PBM), the PBM (or affiliate) remits to the PDP sponsor an amount (in this subparagraph referred to as the rebate remittance payment ) equal to the amount of such rebate (or, in the case of a rebate described in paragraph (5)(B)(ii), the amount of such rebate that is attributable to such drug and such individual), less the amount by which the coinsurance or copayment owed by an individual enrolled in the prescription drug plan with respect to such drug was reduced pursuant to subparagraph (A) ; and (C) in the case that such drug is obtained from an in-network pharmacy by an individual enrolled in the prescription drug plan who is a subsidy eligible individual (as defined in section 1860D\u201314(a)(3)), the PDP sponsor remits to the Secretary, at such time and in such manner as the Secretary may specify\u2014 (i) in the case that the entity receiving the manufacturer rebate in connection with such drug is a PBM (or any affiliate of such PBM), the amount received by the sponsor under subparagraph (B) with respect to such drug and such individual; and (ii) in the case that the entity receiving the manufacturer rebate in connection with such drug is the PDP sponsor, an amount equal to the amount of such rebate (or, in the case of a rebate described in paragraph (5)(B)(ii), the amount of such rebate that is attributable to such drug and such individual), less the amount by which the coinsurance or copayment owed by such individual with respect to such drug was reduced pursuant to subparagraph (A) . (4) Reporting requirement For purposes of paragraph (1)(A)(iii) , the reporting requirement described in this paragraph is, with respect to a PBM and any affiliate of such PBM, that, not later than July 1, 2028, and not less frequently than annually thereafter, the PBM (or affiliate) submits to the PDP sponsor and to the Secretary a report containing a certification that, during the preceding year, such PBM (or affiliate)\u2014 (A) complied with the requirements under paragraphs (2) and (3); and (B) did not engage in steering. (5) Definitions For purposes of this subsection: (A) Affiliate The term affiliate means, with respect to a PBM or PDP sponsor, an entity that, directly or indirectly\u2014 (i) owns, controls, or has an investment interest in such PBM or PDP sponsor; (ii) is owned by such PBM or PDP sponsor or controlled by such PBM or PDP sponsor; (iii) that such PBM or PDP sponsor has an investment interest in; or (iv) is under common ownership or corporate control of such PBM or PDP sponsor. (B) Manufacturer rebate The term manufacturer rebate \u2014 (i) means any price concession (including any payment, discount, administration fee, credit, incentive, or penalty) provided by the manufacturer of a covered part D drug (or any affiliate, subsidiary, third party, or intermediary of such manufacturer) to a PDP sponsor (or any PBM acting on behalf of such sponsor, including any affiliate of such PBM, as applicable), in connection with the furnishing of such covered part D drug to an individual enrolled in a prescription drug plan offered by such sponsor; and (ii) includes any such price concession that is determined based upon\u2014 (I) the aggregate volume of such covered part D drug (or a group of covered part D drugs that includes such part D drug) furnished to individuals enrolled in a prescription drug plan offered by such sponsor; or (II) the furnishing of any service provided to the manufacturer by such sponsor (or any PBM acting on behalf of such sponsor, or any affiliate of such PBM (including an off-shore entity or group purchasing organization), as applicable) in connection with the furnishing of such covered part D drug (or a group of covered part D drugs that includes such part D drug). (C) Pharmacy benefit manager; PBM The terms pharmacy benefit manager and PBM mean a person, business entity, affiliate, or other entity that performs pharmacy benefits management services. (D) Pharmacy benefits management services The term pharmacy benefits management services \u2014 (i) means the managing or administration of a plan or program that pays for, reimburses, and covers the cost of prescription drugs and medical devices; and (ii) includes the processing and payment of claims for prescription drugs and the adjudication of appeals or grievances related to qualified prescription drug coverage under this part. (E) Steering The term steering means, with respect to a PDP sponsor (and any PBM acting on behalf of such sponsor, including any affiliate of such PBM, as applicable)\u2014 (i) directing, ordering, or requiring an enrollee in a prescription drug plan to use a specific pharmacy, including an affiliate pharmacy, for the purpose of filling a prescription for a covered part D drug or receiving services from a pharmacist; (ii) offering or implementing a prescription drug plan design that\u2014 (I) requires an enrollee in a prescription drug plan to utilize a pharmacy, including an affiliate pharmacy; or (II) increases costs to the PDP sponsor or an enrollee, including by requiring an enrollee to pay the full cost for a covered part D drug when such enrollee chooses not to use an affiliate pharmacy; (iii) advertising, marketing, or promoting a pharmacy, including an affiliate pharmacy, in a manner that encourages enrollees to choose such pharmacy over another in-network pharmacy; (iv) creating more than one network of pharmacies with respect to a prescription drug plan such that an in-network pharmacy belonging to a specific network (such as a preferred pharmacy network, narrow pharmacy network, or specialty pharmacy network) receives preferential treatment, or engaging in any practice (including accreditation or credentialing standards, day supply limitations, or delivery method limitations) that has the effect of excluding an in-network pharmacy from participation in the network of the PDP sponsor or restricting an in-network pharmacy from filling a prescription for a covered part D drug; or (v) engaging in any practice that attempts to influence or induce a manufacturer of a covered part D drug to limit the distribution of such drug to a small number of pharmacies or certain types of pharmacies, or to restrict distribution of such drug to non-affiliate pharmacies. .\n**(2) Requirement to deduct expected rebate amounts from plan bids**\nSection 1860D\u201311(b)(2)(C) of the Social Security Act ( 42 U.S.C. 1395w\u2013111(b)(2)(C) ) is amended\u2014\n**(A)**\nin clause (iii), by striking and at the end;\n**(B)**\nby redesignating clause (iv) as clause (v); and\n**(C)**\nby inserting after clause (iii) the following new clause:\n(iv) with respect to bids beginning with plan year 2027, assumptions regarding any rebate remittance payments provided under section 1860D\u201312(h)(3)(B), subtracted from the actuarial value to produce such bid; and .\n**(3) MA\u2013PD plans**\nSection 1857(f)(3) of the Social Security Act ( 42 U.S.C. 1395w\u201327(f)(3) ) is amended by adding at the end the following new subparagraph:\n(F) Requirements relating to pharmacy benefit managers For plan years beginning on or after January 1, 2027, section 1860D\u201312(h). .\n##### (b) Medicaid\n**(1) In general**\nSection 1927 of the Social Security Act ( 42 U.S.C. 1396r\u20138 ) is amended\u2014\n**(A)**\nin subsection (e), by adding at the end the following new paragraph:\n(6) Requirements related to pharmacy benefit managers A contract between the State and a pharmacy benefit manager, or a contract between the State and a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D) and collectively referred to in this paragraph as the entity ) that includes provisions making the entity responsible for coverage of covered outpatient drugs dispensed to individuals enrolled with the entity, shall require\u2014 (A) that the entity or PBM (as applicable) does not engage in steering; (B) that any payment made by the entity or the PBM (as applicable) for such a drug and related administrative services (as applicable), including payments made by a PBM on behalf of the State or entity, is equal to\u2014 (i) the ingredient cost of such drug, which shall be in an amount equal to the sum of\u2014 (I) the national average drug acquisition cost for the drug as of the day that the pharmacy submits a claim for payment for such drug (as determined based upon the retail survey prices obtained under subsection (f)(1)), or, in the case of a drug for which no such national average drug acquisition cost is available, the wholesale acquisition cost for such drug as of such day; and (II) an amount equal to 4 percent of the amount described in item (aa) , or $50, whichever is less; and (ii) a dispensing fee that is equal to the dispensing fee paid for such drug under the State plan under this title in the State in which such pharmacy is located, as reported by the State under subsection (f)(2); and (C) that, in the case that the entity or PBM (as applicable) receives from a manufacturer of a covered outpatient drug a rebate or discount in connection with the furnishing of such drug to an individual enrolled under the State plan (or waiver of such plan), the entity or PBM remits to the State an amount equal to the amount of such rebate. ; and\n**(B)**\nin subsection (k), by adding at the end the following new paragraphs:\n(13) Pharmacy benefit manager; PBM The terms pharmacy benefit manager and PBM have the meaning given such terms in section 1860D\u201312(h)(C). (14) Steering The term steering has the meaning given such term in section 1860D\u201312(h)(E), except that any reference in such section to the PDP sponsor is deemed a reference to a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)) that is responsible for coverage of covered outpatient drugs, and any reference to a covered part D drug is deemed a reference to a covered outpatient drug. .\n**(2) Conforming amendments**\nSection 1903(m) of such Act ( 42 U.S.C. 1396b(m) ) is amended\u2014\n**(A)**\nin paragraph (2)(A)(xiii)\u2014\n**(i)**\nby striking and (III) and inserting (III) ;\n**(ii)**\nby inserting before the period at the end the following: , and (IV) if the contract includes provisions making the entity responsible for coverage of covered outpatient drugs, the entity shall comply with the requirements of section 1927(e)(6) ; and\n**(iii)**\nby moving the margin 2 ems to the left; and\n**(B)**\nby adding at the end the following new paragraph:\n(10) No payment shall be made under this title to a State with respect to expenditures incurred by the State for payment for services provided by an other specified entity (as defined in paragraph (9)(D)(iii)) unless such services are provided in accordance with a contract between the State and such entity which satisfies the requirements of paragraph (2)(A)(xiii). .\n**(3) Effective date**\nThe amendments made by this subsection shall apply to contracts between States and managed care entities, other specified entities, or pharmacy benefit managers that have an effective date beginning on or after January 1, 2027.\n##### (c) Penalties for noncompliant PBMs\n**(1) Criminal penalties**\nSection 1128B of the Social Security Act ( 42 U.S.C. 1320a\u20137b ) is amended by adding at the end the following new subsection:\n(i) Whoever provides pharmacy benefits management services on behalf of a prescription drug plan sponsor under part D of title XVIII or a medicaid managed care organization under title XIX and\u2014 (1) knowingly and willfully fails to comply with the pharmacy payment requirements under section 1860D\u201312(h)(2) or section 1927(e)(6)(A), as applicable; (2) knowingly and willfully engages in steering (as defined in section 1860D\u201312(h)); or (3) knowingly and willfully fails to comply with the rebate pass-through requirements under section 1860D\u201312(h)(3) or section 1927(e)(6)(C), as applicable, shall be guilty of a felony and upon conviction thereof shall be fined not more than $1,000,000, or imprisoned for not more than 10 years, or both. .\n**(2) Civil monetary penalties**\nSection 1128A(a) of the Social Security Act (42 U.S.C. 1320a\u20137a(a)) is amended\u2014\n**(A)**\nin paragraph (10), by adding or at the end;\n**(B)**\nby inserting after paragraph (10) the following new paragraph:\n(11) commits an act described in section 1128B(i); ; and\n**(C)**\nin the first sentence\u2014\n**(i)**\nby striking or in cases under paragraph (9) and inserting in cases under paragraph (9) ; and\n**(ii)**\nby striking fact) and inserting fact, or in cases under paragraph (11), $1,000,000 for each such act) .\n**(3) Effective date**\nThe amendments made by this subsection shall apply beginning on January 1, 2027.\n#### 3. Improving prescription drug transparency under the Medicaid program\nSection 1927(f) of the Social Security Act ( 42 U.S.C. 1396r\u20138(f) ) is amended\u2014\n**(1)**\nin the subsection heading, by striking retail and inserting covered outpatient drug ; and\n**(2)**\nin paragraph (1)\u2014\n**(A)**\nin the paragraph heading, by striking retail and inserting covered outpatient drug ;\n**(B)**\nin subparagraph (A)(i), by striking retail community pharmacy and inserting pharmacy that dispenses covered outpatient drugs, including a retail community pharmacy, mail-order pharmacy, specialty pharmacy, nursing home pharmacy, long-term care facility pharmacy, hospital pharmacy, or clinic pharmacy (but not including a charitable pharmacy or a not-for-profit pharmacy) ;\n**(C)**\nin subparagraph (C)\u2014\n**(i)**\nin clause (i)\u2014\n**(I)**\nby striking retail ; and\n**(II)**\nby striking prescription and inserting covered outpatient ; and\n**(ii)**\nin clause (ii), by striking retail community ;\n**(D)**\nin subparagraph (D)(ii), by striking retail ;\n**(E)**\nin subparagraph (E), by striking the term retail each place it appears; and\n**(F)**\nby adding at the end the following new subparagraphs:\n(F) Survey reporting In order to meet the requirement of section 1902(a)(54), a State shall require that any pharmacy in the State that receives any payment, reimbursement, administrative fee, discount, rebate, or other price concession related to the dispensing of a covered outpatient drug to an individual receiving benefits under this title, regardless of whether such payment, reimbursement, fee, discount, rebate, or other price concession is received directly from the State or a managed care entity or other specified entity (as such terms are defined in section 1903(m)(9)(D)), or is received indirectly from a pharmacy benefits manager or another entity that has a contract with the State or a managed care entity or other specified entity (as so defined)\u2014 (i) shall respond to surveys conducted under this paragraph; and (ii) shall include in each such response the pharmacy\u2019s acquisition price for each such drug, net of all such payments, reimbursements, administrative fees, discounts, rebates, and other price concessions (or, in the case that the pharmacy is unable to determine the net acquisition cost for such a drug at the time that the survey is received, the pharmacy\u2019s negotiated price for such drug). (G) Survey information The Secretary shall make information on national drug acquisition prices obtained under this paragraph publicly available. Such information shall include at least the following: (i) The monthly response rate to the survey, including a list of pharmacies not in compliance with subparagraph (F). (ii) The sampling methodology and number of pharmacies sampled monthly. (iii) Information on price concessions to each pharmacy, including discounts, rebates, and other price concessions, to the extent that such information is available during the survey period. (H) Limitation on use of applicable non-retail pharmacy pricing information No State shall use pricing information reported by a pharmacy that is not a retail pharmacy to develop or inform reimbursement rates for retail community pharmacies. .",
      "versionDate": "2025-12-11",
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
        "name": "Health",
        "updateDate": "2026-01-07T18:58:27Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6609ih.xml"
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
      "title": "Pharmacists Fight Back in Medicare and Medicaid Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pharmacists Fight Back in Medicare and Medicaid Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles XI, XVIII, and XIX of the Social Security Act to establish certain requirements under Medicare and Medicaid with respect to prescription drug benefits and pharmacy benefit managers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T05:48:22Z"
    }
  ]
}
```
