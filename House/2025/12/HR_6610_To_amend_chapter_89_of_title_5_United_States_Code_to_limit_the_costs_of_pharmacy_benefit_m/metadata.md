# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6610?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6610
- Title: Pharmacists Fight Back [in Federal Employee Health Benefit Plans Act]
- Congress: 119
- Bill type: HR
- Bill number: 6610
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-15T08:07:48Z
- Update date including text: 2026-05-15T08:07:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6610",
    "number": "6610",
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
    "title": "Pharmacists Fight Back [in Federal Employee Health Benefit Plans Act]",
    "type": "HR",
    "updateDate": "2026-05-15T08:07:48Z",
    "updateDateIncludingText": "2026-05-15T08:07:48Z"
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
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
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
          "date": "2025-12-11T16:00:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6610ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6610\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Auchincloss (for himself, Mr. Comer , Mrs. Harshbarger , Mr. Carter of Georgia , Mr. Ciscomani , Mr. Moulton , Mr. Deluzio , Ms. Tlaib , Ms. Budzinski , Mr. Krishnamoorthi , Mr. Khanna , Mr. Cohen , Ms. Pressley , Mr. Vicente Gonzalez of Texas , Mr. Moore of Alabama , Mr. Subramanyam , Mr. Pocan , Mr. Bishop , and Ms. McCollum ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend chapter 89 of title 5, United States Code, to limit the costs of pharmacy benefit managers with respect to Federal employee health benefit plans, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pharmacists Fight Back [in Federal Employee Health Benefit Plans Act] .\n#### 2. Pharmacy payment and reimbursement requirements\n##### (a) In general\nSection 8904 of title 5, United States Code, is amended by adding at the end the following new subsection:\n(c) (1) The Office of Personnel Management may not contract for or approve a health benefits plan under section 8903 of this title unless such plan\u2014 (A) requires any pharmacy benefits manager administering prescription drug benefits on behalf of such health benefits plan, either directly or through an affiliate of such pharmacy benefits manager, to\u2014 (i) reimburse an in-network pharmacy for the ingredient cost of a prescription drug in an amount equal to the sum of\u2014 (I) the national average drug acquisition cost for the drug on the day of claim adjudication (or, in the case of a drug that does not appear on the national average drug acquisition cost index, the wholesale acquisition cost for such prescription drug); and (II) the lesser of the amount that is equal to 4 percent of the amount described in subclause (I) or $50; (ii) pay an in-network pharmacy a professional dispensing fee that is equal to the professional dispensing fee paid by the State in which the pharmacy is located under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) for dispensing a prescription drug; and (iii) for any manufacturer rebate such pharmacy benefits manager or affiliate thereof receives in connection with a drug obtained at an in-network pharmacy by an individual pursuant to such prescription drug benefits, such pharmacy benefits manager or affiliate shall\u2014 (I) apply, at the point of sale of such drug, a reduction to the amount of any coinsurance or copayment owed by such individual with respect to such drug, such that the amount of coinsurance or copayment so owed is calculated based on the net cost of the drug, including such rebate; and (II) remit to the carrier for such health benefits plan an amount equal to the amount of such rebate, less the amount by which the coinsurance or copayment owed by such individual with respect to such drug was reduced under subclause (I); (B) prohibits such pharmacy benefits manager and any affiliate thereof from\u2014 (i) directing, ordering, or requiring an individual enrolled in such health benefits plan to use a specific pharmacy, including a pharmacy that is an affiliate of such pharmacy benefits manager, for the purpose of filling a prescription for a prescription drug or receiving services; (ii) advertising, marketing, or promoting a specific pharmacy, including a pharmacy that is an affiliate of such pharmacy benefits manager, over another in-network pharmacy; (iii) creating any network or engaging in any practice, including accreditation or credentialing standards, day supply limitations, or delivery method limitations, that excludes an in-network pharmacy or restricts an in-network pharmacy from filling a prescription for a prescription drug for which benefits are available under such health benefits plan; (iv) directly or indirectly engaging in any practice that attempts to influence or induce a pharmaceutical manufacturer to limit the distribution of a prescription drug to a small number of pharmacies or certain types of pharmacies, or to restrict distribution of such drug to non-affiliate pharmacies; or (v) requiring an individual enrolled in such health benefits plan to reimburse the pharmacy benefits manager or affiliate for the dispensing fee paid to an in-network pharmacy pursuant to subparagraph (A)(ii) with respect to a prescription drug obtained at such pharmacy by such individual, or otherwise increasing the amount owed by such individual with respect to such drug to account for such dispensing fee; (C) prohibits any such pharmacy benefits manager from lowering, imposing a fee on, or otherwise make any adjustment to a prescription drug claim at the time the claim for such drug is adjudicated or after the claim is adjudicated that reduces the amount a pharmacy is reimbursed for such drug pursuant to subparagraph (A), including by charging any fee to such pharmacy that is not associated with a prescription drug claim; and (D) requires the carrier providing such health benefits plan to cooperate with any inspection of such carrier carried out under section 8902b(a)(3)(B) of this title, including by making available to the Office such documents, personnel, and facilities of the carrier as and when determined necessary to Office to carry out such inspection. (2) In this subsection: (A) The term affiliate means an entity, including a pharmacy, that directly or indirectly through one or more intermediaries\u2014 (i) owns, in whole or in part, or controls a pharmacy benefits manager; (ii) is owned, in whole or in part, or controlled by that is a pharmacy benefits manager; or (iii) is a subsidiary of or owned, in whole or in part, or controlled by an entity that owns or controls a pharmacy benefits manager. (B) The term beneficiary means a person who receives prescription drug benefits under a health benefits plan. (C) The term in-network pharmacy means a pharmacy that is licensed by the State board of pharmacy in the State in which such pharmacy is located, that fills or seeks to fill a prescription for a prescription drug for a beneficiary, and is not barred from participating in the program under this chapter under section 8902a. (D) The term pharmacy benefits manager means a person, business entity, affiliate, or other entity that performs pharmacy benefits management services. (E) The term pharmacy benefits management services \u2014 (i) means the managing or administration of a plan or program that pays for, reimburses, and covers the cost of prescription drugs and medical devices; and (ii) includes the processing and payment of claims for prescription drugs and the adjudication of appeals or grievances related to the prescription drug benefit. (F) The term prescription drug means a prescription drug covered by a health benefits plan that is dispensed to a beneficiary for self-administration. .\n##### (b) Noncompliance penalties\n**(1) In general**\nChapter 89 of title 5, United States Code, is amended by inserting after section 8902a the following new section:\n8902b. Pharmacy benefit manager-related sanctions (a) Monetary penalties (1) In general Except as otherwise provided by this subsection and subsection (c), if the Office of Personnel Management determines that a pharmacy benefits manager violated a requirement or prohibition applicable to such pharmacy benefits manager with respect to a health benefits plan pursuant to section 8904(c)(1) of this title, the Office shall, in addition to any other penalties that may be prescribed by law and after consultation with the Attorney General, impose a civil monetary penalty of $10,000 for each such violation\u2014 (A) on such pharmacy benefits manager; and (B) if, during the 10-year period ending on the imposition of such civil monetary penalty, not fewer than five civil monetary penalties have been imposed on such pharmacy benefits manager under this paragraph with respect to health benefit plans provided by the carrier providing such health benefits plan, on such carrier. (2) Maximum penalty amount (A) Pharmacy benefit managers For each carrier providing a health benefits plan with respect to which a pharmacy benefits manager is determined to have committed a violation described in paragraph (1), the total amount of civil monetary penalties imposed on such pharmacy benefits manager under such paragraph for violations with respect to the health benefit plans of such carrier many not exceed $100,000 during any 10-year period. (B) Carriers The total amount of civil monetary penalties imposed on a carrier under paragraph (1) may not exceed $50,000 during any 10-year period. (3) Remediation plan (A) In general Not later than 60 days after the date on which the Office of Personnel Management imposes a civil monetary penalty on a carrier under paragraph (1) with respect to a pharmacy benefits manager that is the fifth such civil monetary penalty imposed on such carrier with respect to such pharmacy benefits manager in a 10-year period, such carrier shall develop and submit to the Office of Personnel Management a plan to ensure that each pharmacy benefit manager administering prescription drug benefits on behalf of a health benefits plan provided by such carrier complies with the requirements and prohibitions applicable to such pharmacy benefit manager pursuant to section 8904(c)(1). (B) Oversight Not later than 60 days after the date on which a carrier submits plan under subparagraph (A), and with such frequency thereafter as determined appropriate by the Office of Personnel Management, the Office of Personnel Management shall inspect such carrier to assess the compliance of such carrier with such plan. (4) Sequential imposition For the purposes of this subsection, any civil monetary penalties concurrently imposed under paragraph (1) shall be deemed to be imposed sequentially. (5) Civil action (A) In general A civil action to recover a civil monetary penalty imposed under this subsection shall be brought by the Attorney General in the name of the United States, and may be brought in the United States district court for the district where the claim involved was presented or where the pharmacy benefits manager or carrier subject to such civil monetary penalty resides. (B) Treatment of amounts recovered Amounts recovered under this subsection shall be paid to the Office of Personnel Management for deposit into the Employees Health Benefits Fund. (6) Deduction from amounts owed The amount of a civil monetary penalty imposed under this subsection may be deducted from any sum then or later owing by the United States to the party against whom the penalty or assessment has been levied. (7) Statute of limitations The Office of Personnel Management may not initiate any action to impose a civil monetary penalty on a pharmacy benefits manager or carrier under this subsection later than 6 years after the date of the violation of the requirement or prohibition by the pharmacy benefits manager for which such civil monetary penalty would be imposed. (b) Debarment (1) In general The Office of Personnel Management shall bar a pharmacy benefits manager from administering prescription drug benefits on behalf of a health benefits plan, either directly of through an affiliate of such pharmacy benefits manager, under the program under this chapter if, in any 10-year period, the Office of Personnel Management imposes 10 or more civil monetary penalties on such pharmacy benefits manager under subsection (a). (2) Effective date Except as provided by subsection (c), debarment of a pharmacy benefits manager under paragraph (1) shall be effective on the date that is 90 days after the date on which the Office of Personnel Management imposes the first civil monetary penalty pursuant to which such pharmacy benefits manager is subject to such debarment. (3) Payment prohibited (A) In general Notwithstanding section 8902(j) or any other provision of this chapter, if, under this section a pharmacy benefits manager is debarred under paragraph (1), no payment may be made by a carrier pursuant to any contract under this chapter (either to such pharmacy benefits manager or by reimbursement) for any service or supply furnished by such pharmacy benefits manager during the period of the debarment. (B) Subcontract contracts Each contract under this chapter shall contain such provisions as may be necessary to carry out subparagraph (A) and the other provisions of this section. (4) Termination The debarment of a pharmacy benefits manager under paragraph (1) shall be immediately terminated if all civil monetary penalties pursuant to which such pharmacy benefits manager is subject to such debarment are overturned or wholly set aside on appeal. (5) Rule of construction For the purposes of this subsection, a civil monetary penalty is a civil monetary penalty pursuant to which a pharmacy benefits manager is subject to debarment under paragraph (1) if such civil monetary penalty is not less than the tenth civil monetary penalty imposed on such pharmacy benefits manager under subsection (a) during a 10-year period that\u2014 (A) has not been appealed and for which the period of appeal has elapsed; or (B) has been appealed, all appeals have been exhausted, and has not be overturned or wholly set aside. (c) Hearing (1) In general The Office of Personnel Management shall not make a determination adverse to a pharmacy benefits manager or carrier under subsection (a) or a determination adverse to a pharmacy benefits manager (b) until such pharmacy benefits manager or carrier, as applicable, has been given reasonable notice and an opportunity for the determination to be made after a hearing as provided in accordance with this subsection. (2) Hearing required Any pharmacy benefits manager or carrier that is the subject of an adverse determination by the Office of Personnel Management under this section shall be entitled to reasonable notice and an opportunity to request a hearing on the record, and to judicial review as provided in this subsection after the Office of Personnel Management makes a final decision regarding such adverse determination. (3) Hearing criteria The Office of Personnel Management shall grant a request for a hearing under paragraph (2) upon a showing that due process rights have not previously been afforded with respect to any finding of fact which is relied upon as a cause for an adverse determination under this section. Such hearing shall be conducted without regard to subchapter II of chapter 5 and chapter 7 of this title by a hearing officer who shall be designated by the Director of the Office of Personnel Management and who shall not otherwise have been involved in the adverse determination being appealed. (4) Request for hearing A request for a hearing under paragraph (2) shall be filed within such period and in accordance with such procedures as the Office of Personnel Management shall prescribe by regulation. (5) Appeal (A) In general Any pharmacy benefits manager or carrier adversely affected by a final decision of the Office of Personnel Management regarding an adverse determination that is made after a hearing under paragraph (2) with respect to such adverse determination and to which such pharmacy benefits manager or carrier was a party may seek review of such final decision in the United States District Court for the District of Columbia or for the district in which the pharmacy benefits manager or carrier resides or has his or her principal place of business by filing a notice of appeal in such court within 60 days after the date the decision is issued, and by simultaneously sending copies of such notice by certified mail to the Director of the Office and to the Attorney General. (B) Answer In answer to an appeal filed under subparagraph (A), the Director of the Office of Personnel Management shall promptly file in the relevant court a certified copy of the transcript of the record of the hearing conducted under paragraph (2) and other evidence upon which the findings and final decision complained of are based. (C) Court authority With respect to an appeal filed under subparagraph (A), the court shall have power to enter, upon the pleadings and evidence of record, a judgment affirming, modifying, or setting aside, in whole or in part, the final decision of the Office of Personnel Management that is the subject of such appeal, with or without remanding the case for a rehearing. The court shall not set aside or remand such final decision unless there is not substantial evidence on the record, taken as whole, to support the such final decision or unless the actions of the Office of Personnel Management with respect to such final decision constitutes an abuse of discretion. (6) Defense forfeiture Matters that were raised or that could have been raised in a hearing under paragraph (2) or an appeal under paragraph (5) may not be raised as a defense to a civil action by the United States to collect a civil monetary penalty imposed under subsection (a). (d) Affiliate; pharmacy benefits manager; prescription drug defined In this section, the terms affiliate , pharmacy benefits manager and prescription drug have the meanings given such terms, respectively, in section 8904(c) of this title. .\n**(2) Clerical amendment**\nThe table of sections for chapter 89 of title 5, United States Code, is amended by inserting after the item relating to section 8902a the following new item:\n8902b. Pharmacy benefit manager-related sanctions. .\n##### (c) Conforming amendment\nSection 8903a(b) of title 5, United States Code, is amended\u2014\n**(1)**\nin paragraph (3), by striking and at the end;\n**(2)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(5) complies with the requirements under section 8904(c). .\n##### (d) Effective date\nThe amendments made by this Act shall take effect on the date that is one year after the date of the enactment of this Act.",
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
        "updateDate": "2026-01-07T18:57:24Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6610ih.xml"
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
      "title": "Pharmacists Fight Back [in Federal Employee Health Benefit Plans Act]",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Pharmacists Fight Back [in Federal Employee Health Benefit Plans Act]",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-03T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend chapter 89 of title 5, United States Code, to limit the costs of pharmacy benefit managers with respect to Federal employee health benefit plans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-03T05:48:24Z"
    }
  ]
}
```
