# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3148?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3148
- Title: SALUTE Act
- Congress: 119
- Bill type: HR
- Bill number: 3148
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2025-12-12T09:08:07Z
- Update date including text: 2025-12-12T09:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3148",
    "number": "3148",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000311",
        "district": "3",
        "firstName": "Brian",
        "fullName": "Rep. Jack, Brian [R-GA-3]",
        "lastName": "Jack",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "SALUTE Act",
    "type": "HR",
    "updateDate": "2025-12-12T09:08:07Z",
    "updateDateIncludingText": "2025-12-12T09:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "S001189",
      "district": "8",
      "firstName": "Austin",
      "fullName": "Rep. Scott, Austin [R-GA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "AL"
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
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "PA"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "AL"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "AL"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
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
      "sponsorshipDate": "2025-05-01",
      "state": "GA"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley M. [R-WV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "WV"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "FL"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MO"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IN"
    },
    {
      "bioguideId": "S001220",
      "district": "5",
      "firstName": "Dale",
      "fullName": "Rep. Strong, Dale W. [R-AL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Strong",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "AL"
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
      "sponsorshipDate": "2025-05-01",
      "state": "TX"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "VA"
    },
    {
      "bioguideId": "A000055",
      "district": "4",
      "firstName": "Robert",
      "fullName": "Rep. Aderholt, Robert B. [R-AL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Aderholt",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "AL"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
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
      "sponsorshipDate": "2025-05-05",
      "state": "AL"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "GA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "NC"
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
      "sponsorshipDate": "2025-06-03",
      "state": "VA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
      "state": "TX"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "VA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "IN"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "NV"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "MD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "OH"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3148ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3148\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Jack (for himself, Mr. Austin Scott of Georgia , Mr. Figures , Mr. Carter of Georgia , Mr. Bresnahan , Mr. McCormick , Mr. Moore of Alabama , Ms. Sewell , Mr. Collins , Mr. Gill of Texas , Mr. Bishop , Mr. Moore of West Virginia , Mr. Fine , Mrs. Wagner , Mrs. Houchin , Mr. Strong , Mr. Goldman of Texas , Mr. McGuire , Mr. Aderholt , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Defense to carry out a pilot program to assist certain members of the Armed Forces and dependents with additional supplemental coverage relating to cancer.\n#### 1. Short title\nThis Act may be cited as the Supporting America\u2019s Leaders Undergoing Tough Expenses Act or the SALUTE Act .\n#### 2. Pilot program to assist certain members of the Armed Forces and dependents with additional supplemental coverage relating to cancer\n##### (a) Establishment\nNot later than September 30, 2026, the Secretary of Defense shall establish a pilot program under which a covered individual may obtain supplemental insurance for noncovered expenses under a fixed indemnity supplemental benefit plan described in subsection (b)(1).\n##### (b) Agreement\n**(1) In general**\nIn carrying out the pilot program under subsection (a), the Secretary shall enter into an agreement with not more than two companies to each offer one or more fixed indemnity supplemental benefit plans that\u2014\n**(A)**\nmeet the requirements for a supplemental insurance plan under section 199.2 of title 32, Code of Federal Regulations, and the exception in section 199.8(b)(4) of such title, as in effect on the date of the enactment of this Act;\n**(B)**\nare provided under a separate policy, certificate, or contract;\n**(C)**\nprovide no coordination with any other health benefit plan; and\n**(D)**\nare designed to help participants pay noncovered expenses.\n**(2) Duration**\nAn agreement entered into under paragraph (1) shall be for a period of at least three years.\n**(3) Requirements**\nIn entering an agreement under paragraph (1) with a company, the Secretary\u2014\n**(A)**\nmay not select the company unless the company is licensed in each State;\n**(B)**\nshall award the contract based on the expertise of the company;\n**(C)**\nshall negotiate the terms and conditions of the fixed indemnity supplemental benefit plan provided under the contract, including with respect to the ability of the company to communicate with individuals not enrolled in the plan and whether such communication may include information on other insurance products;\n**(D)**\nshall negotiate the cost of coverage with the company that will cover the participants who elect to enroll in such plan;\n**(E)**\nshall provide a method for verification of the eligibility of applicants and procedures for determination of eligibility; and\n**(F)**\nshall provide a method for payroll deduction of premiums.\n**(4) Provision of information**\nThe Secretary shall provide information to covered individuals regarding the pilot program under subsection (a) by making available on the online portal of the TRICARE program the following information:\n**(A)**\nA notice of availability of a fixed indemnity supplemental benefit plan provided under the pilot program.\n**(B)**\nA description of how to enroll in such plan.\n**(C)**\nA description and explanation of the benefits provided under such plan.\n**(D)**\nA description of the costs to the individual through premiums and remittances to a company providing such plan.\n##### (c) Election To enroll\nA covered individual may elect to enroll in a fixed indemnity supplemental benefit plan provided under the pilot program under subsection (a).\n##### (d) Limitations on authorization of appropriations\nNone of the amounts authorized to be appropriated by this Act to carry out the pilot program may be used to subsidize the cost of a fixed indemnity supplemental benefit plan provided under the pilot program under subsection (a).\n##### (e) Treatment of companies\nFor purposes of the pilot program under subsection (a), companies selected to carry out the activities in subsection (b) shall not be considered contractors of the Federal Government.\n##### (f) Preemption\nThe provisions of this section shall supersede the laws of any State except with respect to State laws relating to licensing of an insurance company or plan solvency of such a company.\n##### (g) Report\nNot later than three years after the date on which the pilot program under subsection (a) commences, the Secretary shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report regarding such pilot program, including the following:\n**(1)**\nA description of the insurance products provided through a fixed indemnity supplemental benefit plan provided under the pilot program under subsection (a).\n**(2)**\nThe number of covered individuals who enrolled in such a plan.\n**(3)**\nFeedback and examples of use cases by such individuals.\n**(4)**\nA determination by the Secretary with respect to whether such pilot program should be made permanent.\n##### (h) Sunset\nUnless the Secretary makes a determination under subsection (g)(4) to make the pilot program under subsection (a) permanent, the pilot program under subsection (a) shall terminate on the day that is five years after the date of the enactment of this Act.\n##### (i) Definitions\nIn this section:\n**(1)**\nThe term covered individual means the following:\n**(A)**\nA member of the Army, Navy, Marine Corps, Air Force, or Space Force.\n**(B)**\nA dependent (as defined in section 1072 of title 10, United States Code) of such a member who is enrolled in the TRICARE program.\n**(2)**\nThe term noncovered expense means, with respect to a covered individual, any expenses relating to the screening for and diagnosis and treatment of cancer that are not otherwise covered by the health care benefits the individuals receives under chapter 55 of title 10, United States Code.\n**(3)**\nThe term State has the meaning given such term in section 901 of title 32, United States Code.\n**(4)**\nThe term TRICARE program has the meaning given that term in section 1072 of title 10, United States Code.",
      "versionDate": "2025-05-01",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-04T15:41:33Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3148ih.xml"
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
      "title": "SALUTE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-24T09:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SALUTE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting America\u2019s Leaders Undergoing Tough Expenses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-24T09:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Defense to carry out a pilot program to assist certain members of the Armed Forces and dependents with additional supplemental coverage relating to cancer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-24T09:48:16Z"
    }
  ]
}
```
