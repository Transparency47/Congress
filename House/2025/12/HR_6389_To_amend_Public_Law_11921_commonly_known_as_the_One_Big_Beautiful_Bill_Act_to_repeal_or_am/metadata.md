# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6389?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6389
- Title: Upholding Protections for Unaccompanied Children Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6389
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-05-16T08:07:24Z
- Update date including text: 2026-05-16T08:07:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-12-04 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.
- Latest action: 2025-12-03: Introduced in House

## Actions

- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-03 - IntroReferral: Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-04 - Committee: Referred to the Subcommittee on Border Security and Enforcement.
- 2025-12-04 - Committee: Referred to the Subcommittee on Transportation and Maritime Security.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6389",
    "number": "6389",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000599",
        "district": "10",
        "firstName": "Daniel",
        "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
        "lastName": "Goldman",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Upholding Protections for Unaccompanied Children Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:24Z",
    "updateDateIncludingText": "2026-05-16T08:07:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Transportation and Maritime Security Subcommittee",
          "systemCode": "hshm07"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Transportation and Maritime Security.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Border Security and Enforcement Subcommittee",
          "systemCode": "hshm11"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Border Security and Enforcement.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
      "committees": {
        "item": {
          "name": "Homeland Security Committee",
          "systemCode": "hshm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "text": "Referred to the Committee on the Judiciary, and in addition to the Committee on Homeland Security, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Homeland Security Committee",
      "subcommittees": {
        "item": [
          {
            "activities": {
              "item": {
                "date": "2025-12-04T21:11:56Z",
                "name": "Referred to"
              }
            },
            "name": "Border Security and Enforcement Subcommittee",
            "systemCode": "hshm11"
          },
          {
            "activities": {
              "item": {
                "date": "2025-12-04T21:11:56Z",
                "name": "Referred to"
              }
            },
            "name": "Transportation and Maritime Security Subcommittee",
            "systemCode": "hshm07"
          }
        ]
      },
      "systemCode": "hshm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-03T15:00:20Z",
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
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "WA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
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
      "sponsorshipDate": "2025-12-03",
      "state": "DC"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
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
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "ME"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NV"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "PA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IN"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "OR"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "HI"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "AZ"
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
      "sponsorshipDate": "2025-12-03",
      "state": "NC"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "True",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MN"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CO"
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
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NM"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "IL"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "True",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NJ"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "GA"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "MD"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CT"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "NJ"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "OR"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6389ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6389\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Goldman of New York (for himself, Mrs. Ramirez , Ms. Jayapal , Mr. Casar , Mr. Garcia of California , Ms. Jacobs , Ms. Simon , Ms. Norton , Mr. Davis of Illinois , Ms. Schakowsky , Mr. Correa , Ms. Tlaib , Ms. Pingree , Ms. Titus , Ms. Lee of Pennsylvania , Ms. Clarke of New York , Mr. Krishnamoorthi , Mr. Carson , Ms. Salinas , Ms. Tokuda , Ms. Lofgren , Ms. Meng , Ms. Chu , Mr. Quigley , Ms. Ansari , Ms. Ross , Mr. Lieu , Ms. Morrison , Ms. DeGette , Ms. McClellan , Mr. Huffman , Mrs. Torres of California , Ms. Stansbury , Mr. Garc\u00eda of Illinois , and Ms. Crockett ) introduced the following bill; which was referred to the Committee on the Judiciary , and in addition to the Committee on Homeland Security , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) to repeal or amend certain provisions that undermine protections and heighten dangers for unaccompanied children, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Upholding Protections for Unaccompanied Children Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUnaccompanied children are among the world\u2019s most vulnerable individuals. Without protection in their countries of origin, they have fled to the United States often on their own to escape extreme violence, sexual abuse, human trafficking, and other dangers.\n**(2)**\nIn recognition of this vulnerability, Congress has traditionally ensured protections for unaccompanied children on a broad bipartisan basis.\n**(3)**\nCongress reaffirmed this bipartisan commitment through passage of the William Wilberforce Trafficking Victims Protection Reauthorization Act of 2008 ( TVPRA ) which passed, among other purposes, to ensure that unaccompanied children are screened properly to identify signs of trafficking or other protection concerns, placed in the least restrictive setting that is in the best interest of the child, and accorded a full and fair legal process, distinguished by child-sensitive procedures, for pursuing humanitarian relief.\n**(4)**\nThe One Big Beautiful Bill Act ( Public Law 119\u201321 ) erects barriers to TVPRA protections and other longstanding safeguards for unaccompanied children, weakening due process and heightening these children\u2019s vulnerability to human trafficking, exploitation, and abuse.\n**(5)**\nThis legislation imposes an unprecedented fee structure that limits or outright blocks unaccompanied children\u2019s ability to pursue humanitarian protection in the United States, requiring onerous fees from unaccompanied children to seek asylum and other legal relief runs contrary to the TVPRA\u2019s mandate to govern these children\u2019s applications in ways that take into account their specialized needs. It also creates opportunities for traffickers and abusers skilled in leveraging debt to coerce children into sex and labor trafficking and other forms of exploitation.\n**(6)**\nThe Trump administration has sought to rely upon One Big Beautiful Bill Act provisions that provide funding for the removal of unaccompanied children to summarily return children throughout the Nation to their countries of origin without due process. These returns run counter to TVPRA requirements that the Secretary of the Department of Homeland Security place unaccompanied children from countries other than Mexico and Canada in Office of Refugee Resettlement custody, where they receive screenings for trafficking and other protection concerns by legal services providers, and that these children are afforded an appropriate legal process before an immigration judge. Summarily returned children face grave risks of trafficking and other harms.\n**(7)**\nThe American Academy of Pediatrics and other leading medical groups have warned that there is no evidence that any amount of time in detention is safe for children and that detention itself poses a threat to child health.\n**(8)**\nThe One Big Beautiful Bill Act provides funding for carrying out potentially physically intrusive examinations of unaccompanied children in the Department of Homeland Security and Office of Refugee Resettlement custody without any guardrails to protect against inappropriate application and misconduct and despite risks of retraumatizing children who may be fleeing abuse or exploitation.\n**(9)**\nThe One Big Beautiful Bill Act provides funding to the Office of Refugee Resettlement that will further fuel the Trump administration\u2019s systematic targeting of unaccompanied children\u2019s family members for immigration enforcement. After the Administration eliminated safeguards that restricted the Office of Refugee Resettlement from sharing information on unaccompanied children\u2019s sponsors with the Department of Homeland Security for purposes of immigration enforcement, Immigration and Customs Enforcement has taken enforcement actions against numerous sponsors who lack immigration status. These actions have split families apart, caused children profound trauma, and deterred loving parents and other family members from coming forward to sponsor children in Office of Refugee Resettlement custody, depriving children of safe sponsorship options and dramatically increasing those children\u2019s periods of government detention.\n#### 3. Fees\n##### (a) Asylum fee\nSection 100002 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(f) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n##### (b) Employment authorization document fee\nSection 100003 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(d) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n##### (c) Special immigrant juvenile fee\n**(1) Repeal**\nSection 100005 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is repealed.\n**(2) Clarification**\nThe Secretary of Homeland Security may not impose a fee in connection with any alien, parent, or legal guardian of an alien applying for special immigrant juvenile status under section 101(a)(27)(J) ( 8 U.S.C. 1101(a)(27)(J) ).\n##### (d) Annual asylum fee\nSection 100009 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(e) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n##### (e) Employment authorization renewal fees\n**(1) Employment Authorization for Parolees**\nSection 100010 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(e) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n**(2) Employment authorization for asylum applicants**\nSection 100011 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(e) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n**(3) Employment authorization for aliens granted temporary protected status**\nSection 100012 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(e) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n##### (f) Immigration court fees\nSection 100013 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by adding at the end the following:\n(l) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n##### (g) In absentia removal fee\nSection 100016(c) of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by inserting before the period at the end the following: , or in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ) .\n##### (h) Border apprehension fee\nSection 100017 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is amended by inserting at the end the following:\n(e) Exception This section shall not apply in the case of any individual who is, or was previously determined to be, an unaccompanied alien child, as defined in section 462(g)(2) of the Homeland Security Act of 2002 ( 6 U.S.C. 279(g)(2) ). .\n#### 4. Upholding protection screenings and a fair legal process\nSection 100051(8) of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ) is repealed.\n#### 5. Limitations body examinations\n##### (a) Body Examinations conducted by the Department of Homeland Security\nSection 100051(11) of Public Law 119\u201321 is repealed.\n##### (b) Body Examinations conducted by the Office of Refugee Resettlement\nSection 87001(b)(3) of Public Law 119\u201321 is repealed.\n#### 6. Sponsor information sharing\nSection 87001 of Public Law 119\u201321 (commonly known as the One Big Beautiful Bill Act ), as amended by this Act, is further amended by adding at the end the following:\n(f) Limitation on information sharing The Secretary of Health and Human Services shall ensure that information obtained under this section is not shared with Department of Homeland Security or any other Federal agency for the purpose of enforcing the immigration laws (as such term is defined in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 )). .\n#### 7. Refund of fees\nNot later than 180 days after the date of enactment of this Act, the Secretary of Homeland Security and the Attorney General shall refund each fee paid under a provision of law repealed or amended by this Act to each individual who paid such fee.",
      "versionDate": "2025-12-03",
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
        "name": "Immigration",
        "updateDate": "2026-01-05T16:04:39Z"
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
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6389ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Public Law 119-21 (commonly known as the \"One Big Beautiful Bill Act\") to repeal or amend certain provisions that undermine protections and heighten dangers for unaccompanied children, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-19T12:39:55Z"
    },
    {
      "title": "Upholding Protections for Unaccompanied Children Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Upholding Protections for Unaccompanied Children Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-19T12:23:18Z"
    }
  ]
}
```
