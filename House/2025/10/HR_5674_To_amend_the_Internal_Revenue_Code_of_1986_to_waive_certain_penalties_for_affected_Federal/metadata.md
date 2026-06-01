# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5674
- Title: Emergency Relief for Federal Workers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5674
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-12-05T22:53:19Z
- Update date including text: 2025-12-05T22:53:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-03 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5674",
    "number": "5674",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Emergency Relief for Federal Workers Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:53:19Z",
    "updateDateIncludingText": "2025-12-05T22:53:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:30:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-03T19:30:05Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sponsorshipDate": "2025-10-03",
      "state": "LA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
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
      "sponsorshipDate": "2025-10-03",
      "state": "GA"
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
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "WI"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
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
      "sponsorshipDate": "2025-10-03",
      "state": "MD"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "AL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MO"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "OH"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "KS"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
    },
    {
      "bioguideId": "S001156",
      "district": "38",
      "firstName": "Linda",
      "fullName": "Rep. S\u00e1nchez, Linda T. [D-CA-38]",
      "isOriginalCosponsor": "False",
      "lastName": "S\u00e1nchez",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "VA"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "WA"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CO"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "GA"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5674ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5674\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mr. Beyer (for himself, Ms. Elfreth , Ms. Norton , Mr. Subramanyam , Ms. McClellan , Mr. Walkinshaw , Mr. Moulton , Ms. Vel\u00e1zquez , Mr. Whitesides , Mr. Jackson of Illinois , Mr. Nadler , Mrs. McIver , Mrs. Watson Coleman , Mr. Carter of Louisiana , Ms. Tlaib , Mr. Johnson of Georgia , Mr. Schneider , Mr. Goldman of New York , Ms. Lois Frankel of Florida , Ms. Moore of Wisconsin , Mr. Thanedar , Mr. Costa , and Mrs. McClain Delaney ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Internal Revenue Code of 1986 to waive certain penalties for affected Federal employees receiving a distribution from the Thrift Savings Plan during a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Emergency Relief for Federal Workers Act of 2025 .\n#### 2. Waiver of 10-percent additional tax on certain financial hardship distributions from Thrift Savings Plan\n##### (a) In general\nParagraph (2) of section 72(t) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(O) Distributions to Federal employees affected by a qualified lapse in appropriations (i) In general Distributions made from the Thrift Savings Plan under subchapter III of chapter 84 of title 5, United States Code, to an individual who is a Federal employee and who is on furlough or who is working without pay due to a qualified lapse in appropriations, if such distributions are made during the period of such qualified lapse in appropriations (including distributions which are in process as of the end of such lapse). (ii) Limitation Subclause (i) shall apply to any distributions only to the extent the aggregate of such distributions does not exceed $30,000 with respect to any qualified lapse in appropriations. (iii) Adjustment for inflation In the case of a taxable year beginning after December 31, 2025, the $30,000 amount in clause (ii) shall be increased by an amount equal to\u2014 (I) such dollar amount, multiplied by (II) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. If any amount after adjustment under the preceding sentence is not a multiple of $100, such amount shall be rounded to the next lower multiple of $100. (iv) Qualified lapse in appropriations For purposes of this subparagraph, the term qualified lapse in appropriations means a period of continuous lapse in Federal appropriations (including a partial lapse) of at least 2 weeks. (v) Other terms For purposes of this subparagraph, the terms furlough and pay have the respective meanings given such terms by section 7511 of title 5, United States Code. .\n##### (b) Effective date\nThe amendment made by this section shall apply to distributions made after September 30, 2025.\n#### 3. Thrift Savings Plan provisions\n##### (a) In-Service withdrawals\nSection 8433(h) of title 5, United States Code, is amended by adding at the end the following:\n(5) (A) In this paragraph\u2014 (i) the term applicable date , with respect to a covered age-based withdrawal or covered hardship withdrawal made during a qualified lapse in appropriations, means the date that is 120 days after the last day of the qualified lapse in appropriations; (ii) the term covered age-based withdrawal means a withdrawal under paragraph (1)(A) made during the period of a qualified lapse in appropriations; (iii) the term covered hardship withdrawal means a withdrawal described in subparagraph (B); (iv) the term furlough has the meaning given the term in section 7511; (v) the term pay has the meaning given the term in section 7511; and (vi) the term qualified lapse in appropriations has the meaning given the term in section 72(t)(2)(O) of the Internal Revenue Code of 1986. (B) The Board shall permit an employee who is on furlough or working without pay due to a qualified lapse in appropriations to make a withdrawal based upon financial hardship under paragraph (1)(B) if\u2014 (i) the withdrawal is made during the period of such qualified lapse in appropriations (including withdrawals which are in process as of the end of such lapse); and (ii) the aggregate amount of any such withdrawals during the period described in clause (i) does not exceed $30,000, subject to adjustments for inflation under subparagraph (E). (C) The Board may not limit the number of covered hardship withdrawals that an employee may make during the period of a qualified lapse in appropriations, subject to the dollar limitation under subparagraph (B)(ii). (D) (i) An individual who makes 1 or more covered hardship withdrawals or 1 or more covered age-based withdrawals during the period of a qualified lapse in appropriations may, before the applicable date, make 1 or more contributions to the Thrift Savings Fund in an aggregate amount not to exceed the lesser of\u2014 (I) the aggregate amount of the withdrawals; or (II) $30,000, subject to adjustments for inflation under subparagraph (E). (ii) An individual who makes a contribution to the Thrift Savings Fund under clause (i) shall, to the extent of the contribution, be treated as having received the covered age-based withdrawal or covered hardship withdrawal, as applicable, in an eligible rollover distribution (as defined in section 402(c)(4) of the Internal Revenue Code of 1986) and as having transferred the amount to the Thrift Savings Fund in a direct trustee to trustee transfer within 60 days of the distribution. (iii) For purposes of sections 401(a)(31), 402(f), and 3405 of the Internal Revenue Code of 1986, a covered age-based withdrawal or covered hardship withdrawal shall not be treated as an eligible rollover distribution. (E) The dollar limitation under subparagraphs (B)(ii) and (D)(i)(II) shall be adjusted for inflation in the same manner as under section 72(t)(2)(O)(iii) of the Internal Revenue Code of 1986. (F) The Board may rely on a written representation from an employee to determine, for purposes of this paragraph, whether the employee has been furloughed or is working without pay due to a qualified lapse in appropriations. (G) The Director may require each agency affected by a qualified lapse in appropriations, as part of the shutdown procedures of the agency, to submit to the Executive Director a list with the name and social security number of each employee of the agency who will be furloughed or will work without pay due to the qualified lapse in appropriations. .\n##### (b) Loans\nSection 8433(g) of title 5, United States Code, is amended by adding at the end the following:\n(5) (A) The Board shall prescribe rules allowing loans to be made under this subsection to employees who are furloughed or working without pay due to a lapse in appropriations, without regard to the period of the lapse in appropriations. (B) For purposes of subparagraph (A), the terms furlough and pay have the meanings given those terms in section 7511. (6) (A) In this paragraph\u2014 (i) the term furlough has the meaning given the term in section 7511; (ii) the term pay has the meaning given the term in section 7511; (iii) the term payment missed because of a shutdown means a payment\u2014 (I) on a loan under this subsection made to an employee who is on furlough or working without pay due to a qualified lapse in appropriations; (II) that is due during the qualified lapse in appropriations; and (III) that was not paid by the employee; and (iv) the term qualified lapse in appropriations has the meaning given the term in section 72(t)(2)(O) of the Internal Revenue Code of 1986. (B) The Board shall prescribe rules providing that the full amount due for outstanding payments missed because of a shutdown by an employee shall be deducted and withheld from the pay provided to the employee for the period of the qualified lapse in appropriations. .\n#### 4. Missed loan payments not to be treated as taxable distribution during a qualified lapse in appropriations\n##### (a) In general\nParagraph (2) of section 72(p) of the Internal Revenue Code of 1986 is amended by redesignating subparagraph (E) as subparagraph (F) and by inserting after subparagraph (D) the following new subparagraph:\n(E) Special rule for missed loan repayment during a qualified lapse in appropriations Subparagraph (A) shall not fail to apply to any loan from the Thrift Savings Plan under subchapter III of chapter 84 of title 5, United States Code, solely because there is a payment missed because of a shutdown (as defined in section 8433(g)(6)(A)(i) of title 5, United States Code) with respect to such loan, and such loan (or any portion of such loan) shall not be treated as a taxable distribution solely because of such missed payment. .\n##### (b) Effective date\nThe amendment made by this section shall apply to missed loan payments the due date for which is after September 30, 2025.",
      "versionDate": "2025-10-03",
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
        "actionDate": "2025-10-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2966",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Emergency Relief for Federal Workers Act of 2025",
      "type": "S"
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
        "updateDate": "2025-10-17T13:05:35Z"
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
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5674ih.xml"
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
      "title": "Emergency Relief for Federal Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Emergency Relief for Federal Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to waive certain penalties for affected Federal employees receiving a distribution from the Thrift Savings Plan during a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:28Z"
    }
  ]
}
```
