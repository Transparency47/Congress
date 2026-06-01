# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2491?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2491
- Title: ABC Act
- Congress: 119
- Bill type: HR
- Bill number: 2491
- Origin chamber: House
- Introduced date: 2025-03-31
- Update date: 2026-04-15T08:05:44Z
- Update date including text: 2026-04-15T08:05:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-31: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-03-31: Introduced in House

## Actions

- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Introduced in House
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-31 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-31",
    "latestAction": {
      "actionDate": "2025-03-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2491",
    "number": "2491",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "ABC Act",
    "type": "HR",
    "updateDate": "2026-04-15T08:05:44Z",
    "updateDateIncludingText": "2026-04-15T08:05:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
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
      "actionDate": "2025-03-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-31",
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
          "date": "2025-03-31T16:03:20Z",
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
          "date": "2025-03-31T16:03:15Z",
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
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "RI"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "VA"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NC"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
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
      "sponsorshipDate": "2025-03-31",
      "state": "TN"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "KS"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NJ"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "VA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "ME"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "TX"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "FL"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "HI"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-06-24",
      "state": "CA"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "FL"
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
      "sponsorshipDate": "2025-09-11",
      "state": "TN"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MI"
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
      "sponsorshipDate": "2025-10-21",
      "state": "VA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "TX"
    },
    {
      "bioguideId": "R000621",
      "district": "6",
      "firstName": "Emily",
      "fullName": "Rep. Randall, Emily [D-WA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Randall",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "WA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "NE"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2491ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2491\nIN THE HOUSE OF REPRESENTATIVES\nMarch 31, 2025 Mrs. Cammack (for herself, Mr. Magaziner , Mr. Panetta , Mr. Wittman , Ms. Wasserman Schultz , Ms. Ross , Mr. Soto , Mr. Cohen , Mr. Van Drew , Ms. Davids of Kansas , Mr. Langworthy , Mr. Gottheimer , Mrs. Kiggans of Virginia , Mr. Golden of Maine , Mr. Steube , Mr. Pfluger , Ms. Malliotakis , Mr. Lawler , Mr. Buchanan , Mr. Case , and Ms. Omar ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Administrator of the Centers for Medicare & Medicaid Services and the Commissioner of Social Security to review and simplify the processes, procedures, forms, and communications for family caregivers to assist individuals in establishing eligibility for, enrolling in, and maintaining and utilizing coverage and benefits under the Medicare, Medicaid, CHIP, and Social Security programs respectively, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Alleviating Barriers for Caregivers Act or the ABC Act .\n#### 2. Review of Medicare, Medicaid, CHIP, and Social Security to simplify processes. procedures, forms, and communications\n##### (a) Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Centers for Medicare & Medicaid Services.\n**(2) CHIP**\nThe term CHIP means the Children\u2019s Health Insurance Program established under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. ).\n**(3) Commissioner**\nThe term Commissioner means the Commissioner of Social Security.\n**(4) Covered agencies**\nThe term covered agencies means the Centers for Medicare & Medicaid Services and the Social Security Administration.\n**(5) Covered officials**\nThe term covered officials means the Administrator and Commissioner.\n**(6) Covered programs**\nThe term covered programs means Medicare, Medicaid, CHIP, and the Social Security programs.\n**(7) Disability**\nThe term disability has the meaning given such term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(8) Family caregiver**\nThe term family caregiver has the meaning given the term in section 2 of the RAISE Family Caregivers Act ( 42 U.S.C. 3030s note).\n**(9) Medicaid**\nThe term Medicaid means the Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).\n**(10) Medicare**\nThe term Medicare means the Medicare program established under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(11) State**\nThe term State means any of the 50 States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, or the Commonwealth of the Northern Mariana Islands.\n**(12) Social Security programs**\nThe term Social Security programs means each of the following:\n**(A)**\nThe programs for old-age and survivors insurance benefits and disability insurance benefits established under title II of the Social Security Act ( 42 U.S.C. 401 et seq. ).\n**(B)**\nThe program for supplemental security income benefits established under title XVI of such Act ( 42 U.S.C. 1381 et seq. ).\n##### (b) Review of programs\n**(1) In general**\nThe Administrator and the Commissioner shall jointly conduct a review of the eligibility determination and application processes, procedures, forms, and communications of Medicare, Medicaid, CHIP, and the Social Security programs.\n**(2) Goals of the review**\nIn conducting the reviews under paragraph (1), the covered officials shall seek ways to\u2014\n**(A)**\nsimplify and streamline policies and procedures for determining eligibility for, enrolling in, maintaining coverage in, and utilizing the full benefits available under the covered programs;\n**(B)**\nreduce the frequency of family caregivers having to\u2014\n**(i)**\nprovide the same information to covered agencies more than once;\n**(ii)**\ncomplete\u2014\n**(I)**\nmultiple documents for each covered agency; or\n**(II)**\ndocuments requesting the same or similar information for multiple covered agencies; or\n**(iii)**\nprovide information to the covered agencies that\u2014\n**(I)**\nthe covered agencies already have; or\n**(II)**\nthe covered agencies can easily receive from other Federal agencies; and\n**(C)**\nmake it easier for family caregivers to work with the covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans by\u2014\n**(i)**\nproviding information on eligibility for, enrollment in, maintaining coverage in, and utilizing the full benefits available under the covered programs to family caregivers;\n**(ii)**\nimproving communications between family caregivers and employees of covered agencies by\u2014\n**(I)**\ndecreasing call wait times;\n**(II)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans provide timely answers to the questions of family caregivers;\n**(III)**\nimproving the websites of the covered programs\u2014\n**(aa)**\nby making it easier for family caregivers to find information regarding benefit availability, eligibility, and how to maintain coverage; and\n**(bb)**\nby designing such websites to align with the requirements of the Americans with Disabilities Act ( 42 U.S.C. 12101 et seq. ) regarding web design;\n**(IV)**\nimproving the timely access to in-person appointments or meetings between employees of covered agencies and family caregivers;\n**(V)**\nproviding translation or interpretation services for family caregivers for whom English is not their primary language; and\n**(VI)**\nproviding information to family caregivers in accessible formats, including formats compatible with American Sign Language and multiple languages;\n**(iii)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans understand how the covered programs can help family caregivers;\n**(iv)**\nimproving the relationship between family caregivers and the covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans, which may include regularly meeting with family caregivers, individuals entitled to, receiving services from, or filing for, 1 or more of the covered programs, and other stakeholders of the covered programs;\n**(v)**\nensuring that employees of covered agencies and the State agencies responsible for administering State Medicaid and CHIP plans who are responsible for resolving disputes, appeals, and grievances within the covered programs receive education, training, and guidance on specific issues faced by family caregivers who participate in the covered programs; and\n**(vi)**\ntaking other actions the covered officials may identify.\n**(3) Input from family caregivers, organizations, and State entities**\nIn conducting the reviews under paragraph (1), the covered officials shall seek input from\u2014\n**(A)**\nfamily caregivers, including family caregivers with a disability, that have interacted with the covered programs;\n**(B)**\nState, regional, national, and Tribal organizations representing or working with family caregivers or individuals receiving care from family caregivers; and\n**(C)**\nState Medicaid and CHIP programs.\n##### (c) Action\nAfter the reviews under subsection (b) have been completed, the covered officials shall take actions that will simplify and streamline policies and procedures that improve customer service for individuals entitled to, receiving services from, or filing for, any of the covered programs, and family caregivers.\n##### (d) Report to Congress\n**(1) In general**\nNo later than 2 years after the date of enactment of this Act, the covered officials shall each submit a report to the Committee on Finance of the Senate, the Committee on Ways and Means of the House of Representatives, and the Committee on Energy and Commerce of the House of Representatives that details the results of the respective reviews each covered official conducted under subsection (b).\n**(2) Contents of the report**\nThe reports required under paragraph (1) shall contain\u2014\n**(A)**\nissues that the covered officials identified in the reviews and their findings;\n**(B)**\nthe actions that the covered officials are taking to address the issues in subparagraph (A);\n**(C)**\nan estimate on when the actions in subparagraph (B) will be completed;\n**(D)**\nprojected annual costs to implement the actions identified in subparagraph (B); and\n**(E)**\nany recommended change in Federal law to address any issue identified in subparagraph (A).\n**(3) Updated reports**\nThe covered officials shall each submit a report 2 years after submitting the report required under paragraph (1) providing an update to the contents identified in paragraph (2).\n**(4) Publication of the reports**\nThe covered officials shall make the reports required under paragraphs (1) and (3) publicly accessible on the websites of covered agencies.\n##### (e) Reducing red tape for State Medicaid and CHIP programs\nNot later than 1 year after the date of enactment of this Act, the Administrator shall issue a letter to each State Medicaid and CHIP Director to\u2014\n**(1)**\nencourage State Medicaid agencies to conduct reviews of State Medicaid programs and State CHIP programs similar to the reviews conducted at the Federal level under subsection (b);\n**(2)**\nprovide suggestions, informed by the results of such Federal reviews, for promising practices that States could take to reduce administrative burdens on family caregivers in supporting individuals entitled to, receiving service from, or filing for, 1 or more of the covered programs in applying for and receiving assistance under State Medicaid programs and State CHIP programs; and\n**(3)**\nidentify best practices to support family caregivers.",
      "versionDate": "2025-03-31",
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
        "actionDate": "2025-04-01",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1227",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ABC Act",
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
        "name": "Health",
        "updateDate": "2025-04-07T12:59:03Z"
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
      "date": "2025-03-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2491ih.xml"
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
      "title": "ABC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-06T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ABC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Alleviating Barriers for Caregivers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Administrator of the Centers for Medicare & Medicaid Services and the Commissioner of Social Security to review and simplify the processes, procedures, forms, and communications for family caregivers to assist individuals in establishing eligibility for, enrolling in, and maintaining and utilizing coverage and benefits under the Medicare, Medicaid, CHIP, and Social Security programs respectively, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:29Z"
    }
  ]
}
```
