# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/3454
- Title: Protecting Our Constitution and Communities Act
- Congress: 119
- Bill type: HR
- Bill number: 3454
- Origin chamber: House
- Introduced date: 2025-05-15
- Update date: 2025-06-23T18:10:11Z
- Update date including text: 2025-06-23T18:10:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-05-15: Introduced in House

## Actions

- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Introduced in House
- 2025-05-15 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-15 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/3454",
    "number": "3454",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "L000607",
        "district": "16",
        "firstName": "Sam",
        "fullName": "Rep. Liccardo, Sam T. [D-CA-16]",
        "lastName": "Liccardo",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Protecting Our Constitution and Communities Act",
    "type": "HR",
    "updateDate": "2025-06-23T18:10:11Z",
    "updateDateIncludingText": "2025-06-23T18:10:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T14:01:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-15T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "GA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "OH"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MO"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "PR"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
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
      "sponsorshipDate": "2025-05-15",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MI"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NJ"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "LA"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NV"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MD"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "CA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "VA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NY"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "WA"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "IL"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "RI"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "NY"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "IL"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "TX"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3454ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3454\nIN THE HOUSE OF REPRESENTATIVES\nMay 15, 2025 Mr. Liccardo (for himself, Mr. Min , Mr. Vindman , Mr. Raskin , Mr. Nadler , Mr. Fields , Ms. Ansari , Ms. Brownley , Mr. Johnson of Georgia , Mrs. Beatty , Mr. Soto , Mr. Cohen , Mr. Cleaver , Mr. Sherman , Mr. Khanna , Mr. Hern\u00e1ndez , Mr. Huffman , Mr. Ruiz , Mr. Lynch , Ms. Tlaib , Mr. Mullin , Mr. Swalwell , Mrs. Watson Coleman , Mr. Carter of Louisiana , Ms. Lee of Nevada , Mr. Goldman of New York , Mr. Carbajal , Mrs. McClain Delaney , Ms. Johnson of Texas , Ms. Jacobs , Mr. Subramanyam , Mr. Kennedy of New York , Ms. Crockett , Ms. Strickland , Mr. Schneider , and Mr. Amo ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to provide a private right of action with respect to violations of such Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Constitution and Communities Act .\n#### 2. Findings and intent of Congress with respect to Congressional Budget and Impoundment Control Act of 1974\nSection 1001 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 681 ) is amended to read as follows:\n1001. Findings and intent of Congress (a) Findings Congress finds the following: (1) Article I of the Constitution of the United States vests the legislative power, and particularly the exclusive power of the purse, in Congress. (2) Article II, Section 3 of the Constitution of the United States vests the executive power in the President subject to the express obligation that the President take care that the laws be faithfully executed, including those laws by which Congress exercises its Article I power of the purse. (3) Congress alone has the constitutional power to appropriate funds, and the President has the obligation to faithfully execute those laws and to obligate as well as expend funds that have been lawfully appropriated. (4) Constitutional scholars and practitioners agree that appropriations place both a ceiling and a floor on executive spending. As later Chief Justice, then-Assistant Attorney General of the Office of Legal Counsel, William H. Rehnquist affirmed, there is neither reason nor precedent for the President to have a constitutional power to decline to spend appropriated funds. W.H. Rehnquist, Presidential Authority to Impound Funds Appropriated for Assistance to Federally Impacted Schools, 1 Op. O.L.C. 303309 (1969). While serving as Associate White House Counsel, current Chief Justice John Roberts, Jr. acknowledged that no area seems more clearly the province of Congress than the power of the purse. Memorandum from John G. Roberts, Jr., for Fred F. Fielding on Impoundment Authority (August 15, 1985). (5) This understanding was demonstrated by the Congressional Budget and Impoundment Control Act of 1974, which was enacted as soon as claims of constitutional authority for impoundment threatened to upset historical practice. (6) This Act thereby codifies the longstanding separation-of-powers principle that the President has no constitutional authority to impound funds that Congress has already appropriated for a particular policy purpose. After the President signed the Act into law, subsequent practice has continued to confirm this separation-of-powers understanding among the branches. (7) The U.S. Supreme Court has stated, [t]o contend that the obligation imposed on the President to see the laws faithfully executed implies a power to forbid their execution is a novel construction of the Constitution, and entirely inadmissible. Kendall v. United States ex Rel. Stokes, 37 U.S. 524, 525 (1838). More recently, the U.S. Supreme Court confirmed that where legislation was intended to provide a firm commitment of substantial sums . . . . [w]e cannot believe that Congress . . . scuttled the entire effort by providing the Executive with the seemingly limitless power to withhold funds from allotment and obligation. Train v. City of New York, 420 U.S. 35, 45 (1975). As later Justice, then-Judge Brett Kavanaugh wrote in In re Aiken County, 725 F.3d 255, 261 n.1 (D.C. Cir. 2013), [e]ven the president does not have unilateral authority to refuse to spend the funds. . (8) When taking measures that are incompatible with the will of Congress, the President\u2019s power is at its lowest ebb in an area where the President has no plenary constitutional powers, and Congress\u2019 powers are plenary. Youngstown Sheet & Tube Co. v. Sawyer, 343 U.S. 579, 673 (1952) (Jackson, J. concurring). The President therefore has no constitutional authority to impound appropriated funds contrary to the express will of Congress. (9) Interpretation of this Act and compliance with its provisions is a legal question within the purview of Article III courts and not a political question. (10) When the Executive fails to release funds following a lawful withholding under the Impoundment Control Act of 1974 or fails to obligate or expend funds that have been appropriated by Congress, private parties experience a particularized and immediate injury. (b) Disclaimer Nothing contained in this Act, or in any amendments made by this Act, shall be construed as\u2014 (1) asserting or conceding the constitutional powers or limitations of either the Congress or the President; (2) ratifying or approving any impoundment heretofore or hereafter executed or approved by the President or any other Federal officer or employee, except insofar as pursuant to statutory authorization then in effect; (3) superseding any provision of law which requires the obligation of budget authority or the making of outlays thereunder; or (4) to prevent adjudication on the merits by Article III courts of claims related to failures to obligate or expend budget authority. (c) Sense of Congress It is the sense of Congress that the only mechanisms by which the President is allowed to fail to obligate or expend funds provided by law are those provided under sections 1012 and 1013 of this Act. .\n#### 3. Clarification with respect to definition of contingencies\nSection 1011 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 682 ) is amended\u2014\n**(1)**\nin paragraph (4), by striking and at the end;\n**(2)**\nin paragraph (5), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(6) contingencies means unforeseen events or circumstances that could not have been reasonably anticipated, which necessitate immediate and temporary adjustments due to urgent and demonstrable needs, where such action is consistent with statutory and constitutional limitations on executive budgetary authority. .\n#### 4. Authority of Comptroller General\nSection 1015 of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 686 ) is amended by adding at the end the following new subsections:\n(c) Legal interpretation of Comptroller General In any determination regarding applicability or enforcement of sections 1001 through 1015, the legal interpretation of the Comptroller General of the United States, acting through the Government Accountability Office, shall be accorded substantial deference. (d) Executive Branch assistance The Executive Branch shall provide timely access to all necessary and appropriate records and information to facilitate the Comptroller General\u2019s review of potential violations of the Act. (e) Reports to Congress Any failure to comply with the Comptroller General\u2019s determination regarding an impoundment shall be reported to Congress for appropriate legislative or judicial action. .\n#### 5. Remedy in the case of violations of Congressional Budget and Impoundment Control Act of 1974\n##### (a) In general\nThe Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 621 et seq. ) is amended by adding at the end the following new title:\nXI Right of Action for Violations 1101. Private right of action (a) In general Any person aggrieved by a violation of title X with respect to the withholding of budget authority that is required to be made available under such title may institute a civil action in a United States district court against the United States and any Federal employee for preventive relief, including an application in a United States district court for a permanent or temporary injunction, restraining order, or other order. (b) Damages (1) In general Any person aggrieved by a violation under subsection (a) may recover equitable and legal relief (including compensatory and punitive damages), reasonable attorney\u2019s fees (including expert fees), and costs. Damages shall amount to the sum of compensatory and punitive damages or $1,000 per harmed person per violation, whichever is greater. (2) Treble damages If a court finds that a violation under subsection (a) occurred in bad faith, the court shall award damages in an amount equal to 3 times the amount otherwise to be awarded under paragraph (1). (3) Personal liability A Federal employee shall be personally liable for the payment of any damages awarded in an action under this section in the case of a knowing violation of this Act. (4) Waiver of immunity A Federal employee who violates this Act shall not be immune under the Tenth Amendment to the Constitution of the United States, the Eleventh Amendment to the Constitution of the United States, the doctrine of sovereign immunity, the doctrine of qualified immunity, or any other source of law from an action in a United States district court of competent jurisdiction challenging such violation. 1102. Right of action of States and local agencies (a) In general Any State, county, city, district, special district, Tribal government, or unit of local government (or any department or agency of any State, county, city, district, special district, Tribal government, or unit of local government) aggrieved by a violation of title X with respect to the withholding of budget authority that is required to be made available under such title may institute a civil action in a United States district court against the United States and any Federal employee for preventive relief, including an application in a United States district court for a permanent or temporary injunction, restraining order, or other order. (b) Damages (1) In general Any State, county, city, district, special district, Tribal government, or unit of local government (or any department or agency of any State, county, city, district, special district, Tribal government, or unit of local government) aggrieved by a violation under subsection (a) may recover equitable and legal relief (including compensatory and punitive damages), reasonable attorney\u2019s fees (including expert fees), and costs. (2) Treble damages If a court finds that a violation under subsection (a) occurred in bad faith, the court shall award damages in an amount equal to 3 times the amount otherwise to be awarded under paragraph (1). (3) Personal liability A Federal employee shall be personally liable for the payment of any damages awarded in an action under this section in the case of a knowing violation of this Act. (4) Waiver of immunity A Federal employee who violates this Act shall not be immune under the Tenth Amendment to the Constitution of the United States, the Eleventh Amendment to the Constitution of the United States, the doctrine of sovereign immunity, the doctrine of qualified immunity, or any other source of law from an action in a United States district court of competent jurisdiction challenging such violation. (c) State defined In this section, the term State includes the District of Columbia, the Commonwealth of Puerto Rico, Guam, American Samoa, the United States Virgin Islands, and the Commonwealth of the Northern Mariana Islands. 1103. Definitions For purposes of this title, the following definitions apply: (1) Federal employee The term Federal employee means\u2014 (A) a political appointee; or (B) a special Government employee as defined by section 202 of title 18, United States Code. (2) Political appointee The term political appointee means an individual who is\u2014 (A) employed in a position described under sections 5312 through 5316 of title 5 (relating to the Executive Schedule); or (B) a limited term appointee, limited emergency appointee, or noncareer appointee in the Senior Executive Service, as defined under paragraphs (5), (6), and (7), respectively, of section 3132(a) of title 5. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 621 note) is amended by adding at the end the following new items:\nTitle XI\u2014Right of Action for Violations Sec. 1101. Private right of action. Sec. 1102. Right of action of States and local agencies. Sec. 1103. Definitions. .\n#### 6. Justiciability and severability\n##### (a) In general\nTitle X of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 686 ) is amended by inserting after section 1017 the following new section:\n1018. Justiciability (a) In general If, under this part, budget authority is required to be made available for obligation or expenditure and such budget authority is not made available for obligation or expenditure, such action or failure to take action shall constitute final agency action within the meaning of section 704 of title 5, United States Code. Such action or failure to act is not committed to agency discretion by law within the meaning of section 701 of title 5, United States Code. (b) Rule of construction This section shall not be construed to prevent the President from proposing budget authority for deferral or rescission under section 1012 or 1013. 1019. Severability If any provision of this Act, or the application thereof, is held invalid, the validity of the remainder of this Act and its application to other circumstances shall not be affected thereby. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 621 note) is amended by inserting after the item relating to section 1017 the following new items:\nSec. 1018. Justiciability. Sec. 1019. Severability. .",
      "versionDate": "2025-05-15",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-06-23T18:10:11Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3454ih.xml"
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
      "title": "Protecting Our Constitution and Communities Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-27T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Constitution and Communities Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-27T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to provide a private right of action with respect to violations of such Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-27T04:33:17Z"
    }
  ]
}
```
