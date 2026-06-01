# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2978?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2978
- Title: GUARD Act
- Congress: 119
- Bill type: HR
- Bill number: 2978
- Origin chamber: House
- Introduced date: 2025-04-21
- Update date: 2026-05-20T08:07:10Z
- Update date including text: 2026-05-20T08:07:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-21: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.
- Latest action: 2025-04-21: Introduced in House

## Actions

- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-21 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-13 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-13 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-21",
    "latestAction": {
      "actionDate": "2025-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2978",
    "number": "2978",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "GUARD Act",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:10Z",
    "updateDateIncludingText": "2026-05-20T08:07:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 52 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-13",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-21",
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
        "item": [
          {
            "date": "2026-05-13T15:49:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-21T16:01:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-21T16:01:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "NJ"
    },
    {
      "bioguideId": "F000471",
      "district": "5",
      "firstName": "Scott",
      "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzgerald",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "WI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-08-01",
      "state": "TX"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "IN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "DE"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "TX"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "AL"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "CA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "IL"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "KY"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "WI"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CA"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NM"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "CA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NJ"
    },
    {
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "MT"
    },
    {
      "bioguideId": "L000590",
      "district": "3",
      "firstName": "Susie",
      "fullName": "Rep. Lee, Susie [D-NV-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NV"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "CT"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NC"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "WI"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "S000510",
      "district": "9",
      "firstName": "Adam",
      "fullName": "Rep. Smith, Adam [D-WA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "WA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "VA"
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MN"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "TX"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2026-04-23",
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
      "sponsorshipDate": "2026-04-23",
      "state": "VA"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "IA"
    },
    {
      "bioguideId": "F000482",
      "district": "0",
      "firstName": "Julie",
      "fullName": "Rep. Fedorchak, Julie [R-ND-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Fedorchak",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "ND"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "IL"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "NY"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "False",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "NY"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2978ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2978\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2025 Mr. Nunn of Iowa (for himself, Mr. Gottheimer , and Mr. Fitzgerald ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo permit State, local, and Tribal law enforcement agencies that receive eligible Federal grant funds to use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, and to clarify that Federal law enforcement agencies may assist State, local, and Tribal law enforcement agencies in the use of tracing tools for blockchain and related technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Guarding Unprotected Aging Retirees from Deception Act or the GUARD Act .\n#### 2. Definitions\nIn this Act:\n**(1) Elder financial fraud**\nThe term elder financial fraud means the illegal or improper use of an elderly or adult with a disability\u2019s money, property, or other resources for monetary or personal benefit, profit, or gain.\n**(2) Eligible Federal grant funds**\nThe term eligible Federal grant funds means funds received under the following:\n**(A)**\nThe Department of Justice Economic, High-Technology, White Collar, and Internet Crime Prevention National Training and Technical Assistance Program.\n**(B)**\nThe Department of Justice Information Sharing Training and Technical Assistance Program.\n**(C)**\nThe Department of Justice Internet of Things National Training and Technical Assistance Program.\n**(D)**\nSection 1401 of the Violence Against Women Act Reauthorization Act of 2022 ( 34 U.S.C. 30107 ; relating to Local Law Enforcement Grants for Enforcement of Cybercrimes Against Individuals).\n**(E)**\nThe Department of Justice COPS Technology and Equipment Program.\n**(3) General financial fraud**\nThe term general financial fraud means the intentional misrepresentation of information or identity to deceive others, the unlawful use of a credit card, debit card, or automated teller machine or the use of electronic means to transmit deceptive information, in order to obtain money or other things of value.\n**(4) Pig butchering**\nThe term pig butchering means a confidence and investment fraud in which the victim is gradually lured into making increasing monetary contributions, generally in the form of cryptocurrency, to a seemingly sound investment before the scammer disappears with the contributed monies.\n**(5) Scam**\nThe term scam means a financial crime undertaken through the use of social engineering that uses deceptive inducement to acquire\u2014\n**(A)**\nauthorized access to funds; or\n**(B)**\npersonal or sensitive information that can facilitate the theft of financial assets.\n**(6) State**\nThe term State means each of the several States, the District of Columbia, and each territory of the United States.\n#### 3. Federal grants used for investigating elder financial fraud, pig butchering, and general financial fraud\n##### (a) In general\nState, local, and Tribal law enforcement agencies that receive eligible Federal grant funds may use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, including by\u2014\n**(1)**\nhiring and retaining analysts, agents, experts, and other personnel;\n**(2)**\nproviding training specific to complex financial investigations, including training on\u2014\n**(A)**\ncoordination and collaboration between State, local, Tribal, and Federal law enforcement agencies;\n**(B)**\nassisting victims of financial fraud and exploitation;\n**(C)**\nthe use of blockchain intelligence tools and related capabilities related to emerging technologies identified in the February 2024 Critical and Emerging Technology List Update of the Fast Track Action Subcommittee on Critical and Emerging Technologies of the National Science and Technology Council (the Critical and Emerging Technology List ); and\n**(D)**\nunique aspects of fraud investigations, including transnational financial investigations and emerging technologies identified in the Critical and Emerging Technology List;\n**(3)**\nobtaining software and technical tools to conduct financial fraud and exploitation investigations;\n**(4)**\nencouraging improved data collection and reporting;\n**(5)**\nsupporting training and tabletop exercises to enhance coordination and communication between financial institutions and State, local, Tribal and Federal law enforcement agencies for the purpose of stopping fraud and scams; and\n**(6)**\ndesignating a financial sector liaison to serve as a point of contact for financial institutions to share and exchange with State, local, Tribal and Federal law enforcement agencies information relevant to the investigation of fraud and scams.\n##### (b) Report to grant provider\nEach law enforcement agency that makes use of eligible Federal grant funds for a purpose specified under subsection (a) shall, not later than 1 year after making such use of the funds, issue a report to the Federal agency that provided the eligible Federal grant funds, containing\u2014\n**(1)**\nan explanation of the amount of funds so used, and the specific purpose for which the funds were used;\n**(2)**\nstatistics with respect to elder financial fraud, pig butchering, and general financial fraud in the jurisdiction of the law enforcement agency, along with an analysis of how the use of the funds for a purpose specified under subsection (a) affected such statistics; and\n**(3)**\nan assessment of the ability of the law enforcement agency to deter elder financial fraud, pig butchering, and general financial fraud.\n#### 4. Report on general financial fraud, pig butchering, and elder financial fraud\nNo later than a year after the date of the enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators shall, jointly, submit to Congress a report on efforts and recommendations related to general financial fraud, pig butchering, elder financial fraud, and scams.\n#### 5. Report on the state of scams in the United States\n##### (a) In general\nNot later than 2 years after the date of the enactment of this Act, the Secretary of the Treasury and the Director of the Financial Crimes Enforcement Network in consultation with the Attorney General, the Secretary of Homeland Security, and the appropriate Federal banking agencies and Federal functional regulators shall submit a report to the Congress on the state of scams in the United States that\u2014\n**(1)**\nestimates\u2014\n**(A)**\nthe number of financial fraud, pig butchering, elder financial fraud, and scams committed against American consumers each year, including\u2014\n**(i)**\nattempted scams, including through social media, online dating services, email, impersonation of financial institutions and non-bank financial institutions;\n**(ii)**\nsuccessful scams, including through social media, online dating services, email, impersonation of financial institutions and non-bank financial institutions;\n**(B)**\nthe number of consumers each year that lose money to one or more scams;\n**(C)**\nthe dollar amount of consumer losses to scams each year;\n**(D)**\nthe percentage of scams each year that can be attributed to\u2014\n**(i)**\noverseas actors; and\n**(ii)**\norganized crime;\n**(E)**\nthe number of attempted scams each year that involve the impersonation of phone numbers associated with financial institutions and non-bank financial institutions;\n**(F)**\nan estimate of the number of synthetic identities impersonating American consumers each year;\n**(2)**\nprovides an overview of the Federal civil and criminal enforcement actions brought against the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams in the period covered by the report that includes\u2014\n**(A)**\nthe number of such enforcement actions;\n**(B)**\nan evaluation of the effectiveness of such enforcement actions;\n**(C)**\nan identification of the types of claims brought against the recipients the recipients of the proceeds of financial fraud, pig butchering, elder financial fraud, and scams;\n**(D)**\nan identification of the types of penalties imposed through such enforcement actions;\n**(E)**\nan identification of the types of relief obtained through such enforcement actions; and\n**(F)**\nthe number of such enforcement actions that are connected to a Suspicious Activity Report; and\n**(3)**\nidentifies amounts made available and amounts expended to address financial fraud, pig butchering, elder financial fraud, and scams during the period covered by the report by\u2014\n**(A)**\nthe Bureau of Consumer Financial Protection;\n**(B)**\nthe Department of Justice;\n**(C)**\nthe Federal Bureau of Investigation;\n**(D)**\nthe Federal Communications Commission;\n**(E)**\nthe Board of Governors of the Federal Reserve Board;\n**(F)**\nthe Federal Trade Commission;\n**(G)**\nthe Financial Crimes Enforcement Network;\n**(H)**\nthe Securities and Exchange Commission; and\n**(I)**\nthe Social Security Administration.\n##### (b) Solicitation of public comment\nIn carrying out the report required under subsection (a), the Secretary of the Treasury shall solicit comments from consumers, social media companies, email providers, telecommunications companies, financial institutions, non-bank financial institutions.\n#### 6. Report to Congress\nEach Federal agency that provides eligible Federal grant funds that are used for a purpose specified under section 3(a) shall issue an annual report to the Committee on Financial Services of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate containing the information received from law enforcement agencies under section 3(b).\n#### 7. Federal law enforcement agencies assisting State, local, and tribal law enforcement and fusion centers\nFederal law enforcement agencies may assist State, local, and Tribal law enforcement agencies and fusion centers in the use of tracing tools for blockchain and related technology tools.",
      "versionDate": "2025-04-21",
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
        "actionDate": "2026-02-09",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 317."
      },
      "number": "2544",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "GUARD Act",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-20T13:14:13Z"
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
      "date": "2025-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2978ih.xml"
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
      "title": "GUARD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T04:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GUARD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Guarding Unprotected Aging Retirees from Deception Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit State, local, and Tribal law enforcement agencies that receive eligible Federal grant funds to use such funds for investigating elder financial fraud, pig butchering, and general financial fraud, and to clarify that Federal law enforcement agencies may assist State, local, and Tribal law enforcement agencies in the use of tracing tools for blockchain and related technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T04:18:30Z"
    }
  ]
}
```
