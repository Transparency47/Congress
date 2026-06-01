# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4995?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4995
- Title: Enduring Welcome Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4995
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2026-04-15T08:06:13Z
- Update date including text: 2026-04-15T08:06:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-19 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4995",
    "number": "4995",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000400",
        "district": "37",
        "firstName": "Sydney",
        "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
        "lastName": "Kamlager-Dove",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Enduring Welcome Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-15T08:06:13Z",
    "updateDateIncludingText": "2026-04-15T08:06:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
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
          "date": "2025-08-19T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-19T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NV"
    },
    {
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
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
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "IA"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
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
      "sponsorshipDate": "2025-08-19",
      "state": "GA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "AZ"
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
      "sponsorshipDate": "2025-08-19",
      "state": "DC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "DE"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "MA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "WA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-08-19",
      "state": "PA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "TX"
    },
    {
      "bioguideId": "B001322",
      "district": "5",
      "firstName": "Michael",
      "fullName": "Rep. Baumgartner, Michael [R-WA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Baumgartner",
      "party": "R",
      "sponsorshipDate": "2025-08-22",
      "state": "WA"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "NY"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CO"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IN"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "AS"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "MA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "VA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-09-04",
      "state": "UT"
    },
    {
      "bioguideId": "D000628",
      "district": "2",
      "firstName": "Neal",
      "fullName": "Rep. Dunn, Neal P. [R-FL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Dunn",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "FL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "VT"
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
      "sponsorshipDate": "2025-09-09",
      "state": "NY"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "AZ"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "MI"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "TN"
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
      "sponsorshipDate": "2025-10-17",
      "state": "TN"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2025-10-24",
      "state": "NC"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4995ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4995\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Ms. Kamlager-Dove (for herself, Mr. Lawler , Ms. Titus , Mr. McCaul , Mr. Peters , Mr. Bera , Mr. Nunn of Iowa , Mr. Crenshaw , Mr. Meeks , Mr. Johnson of Georgia , Mr. Stanton , Ms. Norton , Ms. McBride , Mr. Sherman , Mr. Keating , Ms. Jayapal , Mr. Fitzpatrick , Mr. Castro of Texas , and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo modify the responsibilities of the Coordinator for Afghan Relocation Efforts, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enduring Welcome Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe Enduring Welcome program is the safest, most secure legal immigration pathway to the United States.\n**(2)**\nThe resettlement of Afghan allies in the Special Immigrant Visa (SIV) and the United States Refugee Admissions Program (USRAP) P1/P2 pipelines is critical to upholding United States credibility and incentivizing future support for United States servicemembers.\n**(3)**\nFailing to reunite active-duty United States military personnel and veterans with their Afghan family members in the Afghan relocation pipeline is harmful to the United States servicemember community.\n**(4)**\nA review conducted by Department of Justice\u2019s Office of Inspector General released on June 10, 2025, concluded that the process for vetting applicants for Afghan SIVs is rigorous and effective in protecting United States national security.\n**(5)**\nThe permanent authorization of the Coordinator for Afghan Relocation Efforts (CARE) under section 7810 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ) reflects a bipartisan commitment to fulfilling wartime promises and ensuring accountability in United States relocation policy.\n#### 3. Office of the Coordinator for Afghan Relocation Efforts\nSection 7810 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin the subsection heading, by striking of coordinator ; and\n**(B)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby inserting before The Secretary the following: The Secretary shall establish an Office of the Coordinator for Afghan Relocation Efforts in the Department of State. ; and\n**(ii)**\nby inserting before who shall be responsible for the following: who shall be the head of the Office of the Coordinator for Afghan Relocation Efforts, and ;\n**(2)**\nby redesignating subsections (c), (d), and (e) as subsections (d), (e), and (f), respectively; and\n**(3)**\nby inserting after subsection (b) the following:\n(c) Additional responsibilities The Coordinator shall be responsible for\u2014 (1) supporting the voluntary departure of covered persons who request assistance departing Afghanistan; (2) leading coordination of interagency efforts relating to vetting, security screening, and case processing of eligible Afghan allies in the Department of State, in coordination with the Department of Homeland Security and the Department of Defense; (3) facilitating relocation and resettlement logistics in coordination with resettlement support centers and United States-based resettlement agencies; (4) addressing family reunification barriers, including cases involving United States active-duty servicemembers and veterans; (5) coordinating integration support, including trauma recovery and medical care, with other Federal agencies; (6) maintaining and analyzing a centralized, secure database of Afghan applicants, beneficiaries, and relocated individuals to inform operations and ensure transparency; and (7) providing timely information to Congress on the status of Afghan relocation efforts and progress made under this mandate. .\n#### 4. Collection of information and database\n##### (a) Collection of information\nThe Coordinator shall collect information on Afghan applicants, beneficiaries, and relocated individuals to inform operations and ensure transparency, including\u2014\n**(1)**\nthe number of Afghan nationals pursuing admission to the United States as a special immigrant under section 602 of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note), as a refugee under section 207 of such Act ( 8 U.S.C. 1157 ) (whether as priority one or priority 2), or as a parolee under section 212(d)(5)(A) of such Act ( 8 U.S.C. 1182(d)(5)(A) ), disaggregated by whether they are in Afghanistan, the United States, or a third country;\n**(2)**\nthe number of family reunification cases pending, approved, and completed;\n**(3)**\nthe average time between application, vetting, relocation, and resettlement;\n**(4)**\nthe number of individuals who have been denied or administratively closed out, and the reason for such actions;\n**(5)**\nthe number of active-duty United States military and veteran-linked cases involving family separation; and\n**(6)**\nsuch other information as the Secretary of State or Coordinator for Afghan Relocation Efforts may prescribe.\n##### (b) Database\n**(1) In general**\nThe Secretary of State shall establish and maintain a secure, centralized database to maintain the information collected pursuant to subsection (a).\n**(2) Form**\nThe information in the database established pursuant to this subsection may be in classified form to the extent necessary but such information shall be usable for operational reporting, oversight, coordination across relevant Federal departments and agencies, and regular reporting to Congress.\n**(3) Report**\nBeginning on the date that is 30 days after the date on which the database required by this subsection is established, and every 90 days thereafter, the Secretary of State shall submit to the appropriate congressional committees a report on the status of each metric with respect to information that is being collected pursuant to subsection (a).\n##### (c) Notification\nBeginning on and after the date specified in section 7(a), the Secretary of State shall continue to maintain this database required by this section unless the Secretary, with prior consultation with the appropriate congressional committees, provides notification to the appropriate congressional committees that shall include\u2014\n**(1)**\nthe number of covered persons with pending relocation cases or appeals before the United States Government; and\n**(2)**\nthe estimated population of eligible covered persons which remains to be resettled.\n#### 5. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate.\n**(2) Coordinator**\nThe term Coordinator means the Coordinator for Afghan Relocation Efforts appointed pursuant to section 3(a).\n**(3) Covered person**\nThe term covered person means\u2014\n**(A)**\na United States citizen;\n**(B)**\nan immediate relative (as such term is described in section 201(b) of the Immigration and Nationality Act ( 8 U.S.C. 1151 )) with respect to whom a petition has been approved and all required documents have been received;\n**(C)**\nan alien who has been admitted to the United States as a lawful permanent resident;\n**(D)**\na spouse or unmarried child under the age of 21 of an alien described in subparagraph (C) with respect to whom a petition has been approved, all required documents have been received, and who has a current priority date as of the date on which the individual seeks assistance from the Coordinator;\n**(E)**\na principal applicant for special immigrant status under section 602 of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note);\n**(F)**\na spouse or unmarried child under the age of 21 of an alien described in subparagraph (E) who has been issued a visa or with respect to whom the Chief of Mission has approved their application, and with respect to whom all documents have been received;\n**(G)**\nan alien who has been approved to be admitted to the United States as a refugee or spouse or unmarried child under the age of 21 (as of August 14, 2021) of such an alien;\n**(H)**\na spouse or an unmarried child under the age of 21 of an alien admitted to the United States pursuant to the Operations Allies Welcome program (or any successor program); or\n**(I)**\nthe primary caregiver of a surviving child described in section 602(b)(2)(C) of the Afghan Allies Protection Act of 2009 ( 8 U.S.C. 1101 note), or a spouse or an unmarried child under the age of 21 of such a primary caregiver.\n#### 6. Sunset\n##### (a) In general\nExcept as provided in section 4(c), this Act and the authorities provided by this Act shall terminate on the date that is 5 years after the date of the enactment of this Act.\n##### (b) Conforming amendment\nSubsection (f) of section 7810 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ), as redesignated by section 3, is amended by striking 3 and inserting 5 .",
      "versionDate": "2025-08-19",
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
        "name": "International Affairs",
        "updateDate": "2025-09-19T16:28:58Z"
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
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4995ih.xml"
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
      "title": "To modify the responsibilities of the Coordinator for Afghan Relocation Efforts, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T10:08:18Z"
    },
    {
      "title": "Enduring Welcome Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enduring Welcome Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T08:23:16Z"
    }
  ]
}
```
