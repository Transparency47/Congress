# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4076
- Title: Insurrection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4076
- Origin chamber: House
- Introduced date: 2025-06-23
- Update date: 2026-02-21T09:05:52Z
- Update date including text: 2026-02-21T09:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-23: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-23: Introduced in House

## Actions

- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Introduced in House
- 2025-06-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-23 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-23",
    "latestAction": {
      "actionDate": "2025-06-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4076",
    "number": "4076",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000530",
        "district": "17",
        "firstName": "Christopher",
        "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
        "lastName": "Deluzio",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Insurrection Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:52Z",
    "updateDateIncludingText": "2026-02-21T09:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-23",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-23",
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
          "date": "2025-06-23T16:00:40Z",
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
          "date": "2025-06-23T16:00:35Z",
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
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "CA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "OR"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CO"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OR"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MI"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "DC"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TX"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "IL"
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
      "sponsorshipDate": "2025-10-10",
      "state": "GA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "OR"
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
      "sponsorshipDate": "2025-10-14",
      "state": "NY"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-17",
      "state": "IL"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "OR"
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
      "sponsorshipDate": "2025-10-17",
      "state": "NY"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NH"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "NY"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "False",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TN"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "TX"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NC"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CT"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "PA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "TX"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "WA"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-01-20",
      "state": "CO"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2026-01-21",
      "state": "TX"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "R000305",
      "district": "2",
      "firstName": "Deborah",
      "fullName": "Rep. Ross, Deborah K. [D-NC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Ross",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "NC"
    },
    {
      "bioguideId": "A000381",
      "district": "3",
      "firstName": "Yassamin",
      "fullName": "Rep. Ansari, Yassamin [D-AZ-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Ansari",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "AZ"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "MD"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "VT"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "CO"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4076ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4076\nIN THE HOUSE OF REPRESENTATIVES\nJune 23, 2025 Mr. Deluzio introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo provide limited authority to use the Armed Forces to suppress insurrection or rebellion and quell domestic violence.\n#### 1. Short title\nThis Act may be cited as the Insurrection Act of 2025 .\n#### 2. Limited authority to use the Armed Forces to suppress insurrection or rebellion and quell domestic violence\n##### (a) Statement of constitutional authority\nThis section represents an exercise of Congress\u2019s authorities under\u2014\n**(1)**\nclauses 14, 15, 16, and 18 of section 8 of article I of the Constitution of the United States;\n**(2)**\nsection 4 of article IV of the Constitution of the United States; and\n**(3)**\nsection 5 of the 14th Amendment to the Constitution of the United States.\n##### (b) Amendments to insurrection provisions in title 10, United States Code\nChapter 13 of title 10, United States Code, is amended by striking sections 251 through 255 and inserting the following new sections:\n251. Statement of policy It is the policy of the United States that domestic deployment of the Armed Forces for the purposes set forth in this chapter should be a last resort and should be ordered only if State and local authorities in the State concerned are unable or otherwise fail to suppress the insurrection or rebellion, quell the domestic violence, or enforce the laws that are being obstructed, and Federal civilian law enforcement authorities are unable to do so. 252. Triggering circumstances (a) In general The authorities granted to the President by section 253 may be exercised only if\u2014 (1) there is an insurrection or rebellion in a State\u2014 (A) against the State or local government, in such numbers, or with such force or capacity, as to overwhelm State or local authorities, and the chief executive of the State requests assistance under this chapter; or (B) against the Government of the United States, in such numbers, or with such force or capacity, as to overwhelm State or local authorities; (2) there is domestic violence in a State that is sufficiently widespread or severe as to overwhelm State or local authorities, and the chief executive of the State, or super majority of the State legislature, requests assistance under this chapter; or (3) there is, within a State\u2014 (A) obstruction of the execution of State or Federal law that has the effect of depriving any party or class of the people of that State of a right, privilege, immunity, or protection named in the Constitution and secured by law, and State or local authorities or Federal civilian law enforcement personnel are unable, fail, or refuse to protect that right, privilege, or immunity, or to give that protection; (B) obstruction of the execution of Federal law by private actors where such obstruction creates an immediate threat to public safety and the use of State or local authorities and Federal civilian law enforcement personnel is insufficient to ensure execution of the law and\u2014 (i) the private actors are in such numbers, or with such force or capacity, as to overwhelm State or local authorities and Federal civilian law enforcement personnel; or (ii) State or local authorities and Federal civilian law enforcement personnel otherwise fail to address the obstruction; or (C) obstruction of the execution of Federal law by the State or its agents, where the use of Federal civilian law enforcement personnel is insufficient to ensure execution of the law. (b) Rules of construction (1) Subsection (a)(3)(A) shall be construed to encompass the obstruction of any provision of the Voting Rights Act of 1965 ( 52 U.S.C. 10301 et seq. ) or section 2004 of the Revised Statutes ( 52 U.S.C. 10101 ) regarding protection of the right to vote. Any deployment of the Armed Forces in such circumstances shall be subject to section 2003 of the Revised Statutes ( 52 U.S.C. 10102 ), sections 592 and 593 of title 18, and any other applicable statutory limitations designed to protect the right to vote. (2) In any situation covered by subsection (a)(3)(A), the State shall be considered to have denied the equal protection of the laws secured by the Constitution. 253. Authority of the President (a) In general Subject to subsection (b) and sections 254 through 257, the President may, if the conditions specified in section 252 are met, order to active duty any reserve component forces and use the Armed Forces to suppress the insurrection or rebellion, quell the domestic violence, or enforce the laws that are being obstructed. (b) Limitations (1) During any deployment of the Armed Forces under subsection (a), the Armed Forces shall remain subordinate to the chain of command prescribed in section 162(b) of this title. (2) Any part of the Armed Forces employed to suppress an insurrection or rebellion, quell domestic violence, or enforce the law under the authorities granted by subsection (a) must operate under the Standing Rules for the Use of Force. (3) Nothing in this chapter shall be construed to authorize\u2014 (A) suspension of the writ of habeas corpus; or (B) any action that violates Federal law or, where consistent with Federal law, State law. (c) Standing Rules for the Use of Force In this section, the term Standing Rules for the Use of Force means Chairman of the Joint Chiefs of Staff Instruction (CJCSI) 3121.01B, dated June 13, 2005, and entitled, Standing Rules of Engagement/Standing Rules for the Use of Force for U.S. Forces , or any successor instruction. 254. Consultation with Congress; proclamation to disperse; reporting requirement; effective periods of authorities (a) Consultation The President shall, to the maximum extent practicable, consult with Congress before exercising the authorities granted under section 253. (b) Proclamation Before exercising the authorities granted by section 253, the President shall, by proclamation immediately transmitted to Congress and the Federal Register\u2014 (1) specify which paragraph and, where applicable, subparagraph and clause, of section 252(a) provides the basis for such exercise of authority; and (2) order the lawbreakers to disperse peaceably within a reasonable, limited time period. (c) Report Contemporaneously with the proclamation required under subsection (b), the President shall submit to the President pro tempore of the Senate and the Speaker of the House of Representatives a written report setting forth the following: (1) The circumstances necessitating the exercise of the authorities granted to the President by section 253. (2) Where applicable, a certification by the Attorney General of the United States that the chief executive of the State in question has requested assistance under this chapter or that State authorities are unable or have otherwise failed to address the circumstances necessitating exercise of the President\u2019s authorities under section 253. (3) Certification by the Attorney General of the United States that options other than the use of the Armed Forces have been exhausted, or that those options would likely be insufficient to resolve the situation and that delay would likely cause significant harm. (4) A description of the size, mission, scope, and expected duration of the use of the Armed Forces, with a certification by the relevant Service Secretary or Secretaries that, in their best military advice and opinion, the Armed Forces to be called for duty are trained, equipped, and able to complete the assigned mission. 255. Congressional approval (a) Temporary effective periods (1) Any authority made available under section 253 shall terminate 7 days after the President makes the proclamation required under section 254(b) unless\u2014 (A) there is enacted into law a joint resolution of approval under subsection (b) with respect to the proclamation; or (B) there is a material and significant change in factual circumstances that are set forth in a new proclamation and report to Congress as provided in subsections (b) and (c) of section 254. (2) Notwithstanding subparagraphs (A) and (B) of paragraph (1), no authority may be exercised after the 7-day period described in such paragraph if the exercise of authority has been enjoined by a court of competent jurisdiction. (3) If Congress is physically unable to convene as a result of an insurrection, rebellion, domestic violence, or obstruction of law described in a proclamation issued pursuant to section 254(b), the 7-day period described in paragraph (1) shall begin on the first day Congress convenes for the first time after the insurrection, rebellion, domestic violence, or obstruction of law. (b) Effect of a joint resolution of approval If there is enacted into law a joint resolution of approval as defined in subsection (d), then any authority made available under this chapter may be exercised with respect to the insurrection, rebellion, or domestic violence described in the proclamation that is the subject of such resolution for 14 days from the date of the enactment of such resolution, except that such exercise of authority must terminate if enjoined by a court of competent jurisdiction on the ground that it violates the terms of this chapter, the Constitution of the United States, or other applicable Federal law. (c) Renewal of joint resolutions of approval An exercise of authority subject to a joint resolution of approval may not be exercised for longer than 14 days, unless\u2014 (1) there is enacted into law another joint resolution of approval renewing the President\u2019s authority pursuant to section 253; or (2) there has been a material and significant change in factual circumstances that are set forth in a new proclamation and report to Congress as provided in subsections (b) and (c) of section 254. (d) Joint resolution of approval defined In this section, the term joint resolution of approval means a joint resolution that contains only the following provisions after its resolving clause: (1) A provision approving the exercise of authority specified by the President in a proclamation made under subsection (b) of section 254. (2) A statement that the exercise of authority may continue for a period of 14 days unless enjoined by a court of competent jurisdiction on the ground that it violates the terms of this chapter, the Constitution of the United States, or other applicable Federal or State law. (e) Procedures for consideration of joint resolutions of approval (1) Introduction A joint resolution of approval may be introduced in either House of Congress by any member of that House at any time that authority under section 253 is in effect pursuant to a proclamation made under section 254(b) or a joint resolution of approval enacted into law pursuant to subsection (b). (2) Requests to convene Congress during recesses If, when the President transmits to Congress a proclamation under section 254(b) or at any time that authority under section 253 is in effect as described in paragraph (1), Congress has adjourned sine die or has adjourned for any period in excess of 3 calendar days, the majority leader of the Senate and the Speaker of the House of Representatives, or their respective designees, acting jointly after consultation with and with the concurrence of the minority leader of the Senate and the minority leader of the House, shall notify the Members of the Senate and House, respectively, to reassemble at such place and time as they may designate if, in their opinion, the public interest shall warrant it. (3) Committee referral A joint resolution of approval shall be referred in each House of Congress to the committee or committees having jurisdiction over the emergency authorities invoked by the proclamation under section 254(b) that are the subject of the joint resolution. (4) Consideration in Senate In the Senate, the following shall apply: (A) Reporting and discharge If the committee to which a joint resolution of approval has been referred has not reported it at the end of 3 calendar days after its introduction, that committee shall be automatically discharged from further consideration of the resolution and it shall be placed on the calendar. (B) Proceeding to consideration Notwithstanding Rule XXII of the Standing Rules of the Senate, when the committee to which a joint resolution of approval is referred has reported the resolution, or when that committee is discharged under subparagraph (A) from further consideration of the resolution, it is at any time thereafter in order (even though a previous motion to the same effect has been disagreed to) for a motion to proceed to the consideration of the joint resolution, and all points of order against the joint resolution (and against consideration of the joint resolution) are waived. The motion to proceed is subject to 4 hours of debate divided evenly between those favoring and those opposing the joint resolution of approval. The motion is not subject to amendment, or to a motion to postpone, or to a motion to proceed to the consideration of other business. (C) Floor consideration A joint resolution of approval shall be subject to 10 hours of consideration, to be divided evenly between those favoring and those opposing the joint resolution of approval. (D) Amendments No amendments shall be in order with respect to a joint resolution of approval. (E) Motion to reconsider final vote A motion to reconsider a vote on passage of a joint resolution of approval shall not be in order. (F) Appeals Points of order, including questions of relevancy, and appeals from the decision of the Presiding Officer, shall be decided without debate. (5) Consideration in House of Representatives In the House of Representatives, the following shall apply: (A) Reporting and discharge If any committee to which a joint resolution of approval has been referred has not reported it to the House within 3 calendar days after the date of referral, such committee shall be discharged from further consideration of the joint resolution. (B) Proceeding to consideration (i) In general Beginning on the third legislative day after each committee to which a joint resolution of approval has been referred reports it to the House or has been discharged from further consideration of the joint resolution, and except as provided in clause (ii), it shall be in order to move to proceed to consider the joint resolution in the House. The previous question shall be considered as ordered on the motion to its adoption without intervening motion. The motion shall not be debatable. A motion to reconsider the vote by which the motion is disposed of shall not be in order. (ii) Subsequent motions to proceed to joint resolution of approval A motion to proceed to consider a joint resolution of approval shall not be in order after the House has disposed of another motion to proceed on that resolution. (C) Floor consideration Upon adoption of the motion to proceed in accordance with subparagraph (B)(i), the joint resolution of approval shall be considered as read. The previous question shall be considered as ordered on the joint resolution to final passage without intervening motion except 2 hours of debate, equally divided and controlled by the sponsor of the joint resolution (or a designee) and an opponent. A motion to reconsider the vote on passage of the joint resolution shall not be in order. (D) Amendments No amendments shall be in order with respect to a joint resolution of approval. (6) Receipt of resolution from other House If, before passing a joint resolution of approval, one House receives a joint resolution of approval from the other House, then\u2014 (A) the joint resolution of the other House shall not be referred to a committee and shall be deemed to have been discharged from committee on the day it is received; and (B) the procedures set forth in paragraphs (4) and (5), as applicable, shall apply in the receiving House to the joint resolution received from the other House to the same extent as such procedures apply to a joint resolution of the receiving House. (f) Rule of construction The enactment of a joint resolution of approval under this section shall not be interpreted to serve as a grant or modification by Congress of statutory authority of the President. (g) Rules of the House and Senate This section is enacted by Congress\u2014 (1) as an exercise of the rulemaking power of the Senate and the House of Representatives, respectively, and as such is deemed a part of the rules of each House, respectively, but applicable only with respect to the procedure to be followed in the House in the case of joint resolutions described in this section, and supersedes other rules only to the extent that it is inconsistent with such other rules; and (2) with full recognition of the constitutional right of either House to change the rules (so far as relating to the procedure of that House) at any time, in the same manner, and to the same extent as in the case of any other rule of that House. 256. Termination of authority (a) In general Any exercise of authority specified by the President in a proclamation made under subsection (b) of section 254 shall terminate on the earliest of\u2014 (1) the date provided for in section 255(a); (2) the date provided for in section 255(b); (3) the date specified in an Act of Congress terminating the authority; (4) the date specified in a proclamation of the President terminating the emergency; or (5) the date of a revocation of a request for assistance under this chapter by the chief executive of the State in question. (b) Effect of termination (1) In general Effective on the date of the termination of authority under subsection (a)\u2014 (A) except as provided by paragraph (2), any powers or authorities exercised by reason of the authority shall cease to be exercised; (B) any amounts reprogrammed or transferred under any provision of law with respect to the exercise of authority that remain unobligated on that date shall be returned and made available for the purpose for which such amounts were appropriated; and (C) any contracts entered into under any provision of law relating to the execution of authority shall be terminated. (2) Savings provision The termination of an exercise of authority under this chapter shall not affect\u2014 (A) any legal action taken or pending legal proceeding not finally concluded or determined on the date of the termination under subsection (a); (B) any legal action or legal proceeding based on any act committed prior to that date; or (C) any rights or duties that matured or penalties that were incurred prior to that date. 257. Judicial review (a) In general Notwithstanding, and without prejudice to, any other provision of law, any individual or entity (including a State or local government) that is injured by, or has a credible fear of injury from, the use of members of the Armed Forces under this chapter may bring a civil action for declaratory or injunctive relief. In any action under this section, the district court shall have jurisdiction to decide any question of law or fact arising under this chapter, including challenges to the legal basis for members of the Armed Forces to be acting under this chapter. (b) Standard of review A determination that the conditions specified in section 252 are met shall be upheld if supported by substantial evidence. (c) Expedited consideration It shall be the duty of the applicable district court of the United States and the Supreme Court of the United States to advance on the docket and to expedite to the greatest possible extent the disposition of any matter brought under this section. (d) Appeals (1) In general The Supreme Court of the United States shall have jurisdiction of an appeal from a final decision of a district court of the United States in a civil action brought under this section. (2) Filing deadline A party shall file an appeal under paragraph (1) not later than 30 days after the court issues a final decision under subsection (a). 258. State defined For purposes of this chapter, the term State includes the Commonwealth of Puerto Rico, the District of Columbia, Guam, and the Virgin Islands. 259. Limitation on use of National Guard members performing training or other duty for certain purposes A member of the National Guard performing training or other duty under section 502(a) or (f) of title 32 may not be used to suppress a domestic insurrection or rebellion, quell domestic violence, or enforce the law. .\n##### (c) Conforming amendments\n**(1) Use of State defense forces**\nSection 109(c) of title 32, United States Code, is amended by inserting , except as provided by section 253 of title 10 after armed forces .\n**(2) Table of sections**\nThe table of sections at the beginning of chapter 13 of title 10, United States Code, is amended to read as follows:\nSec. 251. Statement of policy. 252. Triggering circumstances. 253. Authority of the President. 254. Consultation with Congress; proclamation to disperse; reporting requirement; effective periods of authorities. 255. Congressional approval. 256. Termination. 257. Judicial review. 258. State defined. 259. Limitation on use of National Guard members performing training or other duty for certain purposes. .",
      "versionDate": "2025-06-23",
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
        "actionDate": "2025-06-12",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "2070",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Insurrection Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-17T15:47:05Z"
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
      "date": "2025-06-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4076ih.xml"
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
      "title": "Insurrection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:13:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Insurrection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T13:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide limited authority to use the Armed Forces to suppress insurrection or rebellion and quell domestic violence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T13:48:19Z"
    }
  ]
}
```
