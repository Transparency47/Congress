# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7549
- Title: National Council on African American History and Culture Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7549
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-04-10T08:05:52Z
- Update date including text: 2026-04-10T08:05:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7549",
    "number": "7549",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "M000687",
        "district": "7",
        "firstName": "Kweisi",
        "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
        "lastName": "Mfume",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "National Council on African American History and Culture Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:52Z",
    "updateDateIncludingText": "2026-04-10T08:05:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MI"
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
      "sponsorshipDate": "2026-02-12",
      "state": "PA"
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
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MD"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "OH"
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
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MO"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IN"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
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
      "sponsorshipDate": "2026-02-12",
      "state": "DC"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MD"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NV"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MD"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MI"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TX"
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
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "MO"
    },
    {
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "IL"
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
      "sponsorshipDate": "2026-02-12",
      "state": "AL"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WA"
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
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "TN"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "WI"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NJ"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7549ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7549\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Mfume (for himself, Ms. Tlaib , Ms. Lee of Pennsylvania , Ms. Schakowsky , Mr. Ivey , Ms. Simon , Ms. Wilson of Florida , Ms. Brown , Ms. Clarke of New York , Mr. Bell , Mr. Carson , Mr. Evans of Pennsylvania , Ms. Moore of Wisconsin , Ms. Norton , Mr. Raskin , Mr. David Scott of Georgia , Ms. Titus , Mr. Olszewski , Ms. Williams of Georgia , Mr. Thanedar , Mr. Veasey , Mr. Johnson of Georgia , Mr. Cleaver , Ms. Kelly of Illinois , Ms. Sewell , Ms. Strickland , Mr. Goldman of New York , Mr. Pallone , Mr. Cohen , Mr. Nadler , Mrs. Beatty , Mr. Pocan , Mrs. Watson Coleman , and Mrs. McBath ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish a National Council on African American History and Culture within the National Endowment for the Humanities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the National Council on African American History and Culture Act of 2026 .\n#### 2. Council on African American History and Culture\n##### (a) Establishment\nThere is established in the National Endowment for the Humanities a National Council on African American History and Culture (referred to in this section as the Council ).\n##### (b) Membership\n**(1) Number and appointment**\nThe Council shall be composed of 12 members appointed by the President, by and with the advice and consent of the Senate.\n**(2) Qualifications**\nThe members of the Council shall be individuals who\u2014\n**(A)**\nare selected from among private citizens of the United States who are recognized for their broad knowledge of, expertise in, or commitment to the preservation and celebration of African American history and culture;\n**(B)**\nare not currently employees of the Federal Government; and\n**(C)**\nhave established records of distinguished service, scholarship, or creativity.\n**(3) Considerations**\nIn appointing members to the Council under paragraph (1), the President\u2014\n**(A)**\nshall give due regard to equitable representation of women, people of color, and individuals with disabilities who are involved in the humanities;\n**(B)**\nshall select such members in a manner that ensures a comprehensive representation of the views of scholars and professional practitioners in the humanities and of the public throughout the United States; and\n**(C)**\nshall ensure that six members are individuals affiliated with the Democratic party and six members are individuals affiliated with the Republican party.\n**(4) Chairperson; vice chairperson**\n**(A) In general**\nThe Chairperson and Vice Chairperson of the Council shall be designated by the President from among the members of the Council. The Vice Chairperson shall act as Chairperson in the absence of the Chairperson.\n**(B) Party affiliation**\nThe Chairperson and Vice Chairperson may not be affiliated with the same political party.\n**(5) Term of office; vacancies; reappointment**\n**(A) In general**\nEach member shall be appointed for a term of five years, except as provided in subparagraphs (B) and (C).\n**(B) Terms of initial appointees**\nAs designated by the President at the time of the appointment, of the members first appointed to the Council under paragraph (1)\u2014\n**(i)**\nsix shall be appointed for terms of three years, three of whom shall be individuals affiliated with the Democratic party and three of whom shall be individuals affiliated with the Republican party; and\n**(ii)**\nsix shall be appointed for terms of five years, three of whom shall be individuals affiliated with the Democratic party and three of whom shall be individuals affiliated with the Republican party.\n**(C) Vacancies**\nAny member appointed to fill a vacancy occurring before the expiration of the term for which the member\u2019s predecessor was appointed shall be appointed only for the remainder of that term. A member may serve after the expiration of that member\u2019s term until a successor has taken office.\n**(D) Reappointment**\nNo member shall be eligible for reappointment during the two-year period following the expiration of such member\u2019s term.\n**(6) Basic pay**\n**(A) Rates of pay**\nMembers shall receive compensation at a rate of 50 percent of the daily rate of the highest rate of basic pay payable for the senior-level positions classified above GS\u201315 pursuant to section 5108 of title 5, United States Code, for each day (including travel time) during which they are engaged in the actual performance of duties vested in the Council.\n**(B) Travel expenses**\nEach member shall receive travel expenses, including per diem in lieu of subsistence, in accordance with applicable provisions under subchapter 1 of chapter 57 of title 5, United States Code.\n**(7) Quorum**\nNine members of the Council shall constitute a quorum. The Council cannot hold hearings without a full quorum.\n**(8) Meetings**\nThe Council shall meet at the call of the Chairperson but not less frequently than twice during each calendar year.\n##### (c) Duties\nThe duties of the Council shall be\u2014\n**(1)**\nto prepare an annual report to be submitted to the Chairperson of the National Endowment for the Humanities on the work of the National Endowment to preserve and celebrate African American history and culture;\n**(2)**\nto gather timely and authoritative information concerning historical developments and cultural trends in African American history and culture, as well as to monitor the work of museums and organizations dedicated to the preservation of African American history and culture, and to analyze and interpret such information for the purpose of determining whether national policy is necessary to further support those efforts;\n**(3)**\nto evaluate the various programs and activities of the National Endowment for the Humanities for the purpose of determining the extent to which such programs and activities are contributing, and the extent to which they are not contributing, to the successful preservation and celebration of African American history and culture, and to make recommendations to the President with respect to such programs and activities;\n**(4)**\nto develop and recommend to the Chairperson national policies to foster and promote the understanding of African American history, the preservation of African American culture, and the celebration of African Americans as contributors to the country\u2019s economic, cultural, and political success; and\n**(5)**\nto make and furnish such studies, reports thereon, and recommendations with respect to matters of cultural preservation and African American history as the Chairperson may request.\n##### (d) Applicability of FACA\nSection 1013(a)(2) of title 5, United States Code (relating to the termination of advisory committees), shall not apply to the Council.\n##### (e) Termination\nThe Council shall terminate 10 years after the date of the enactment of this Act.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3890",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Council on African American History and Culture Act of 2026",
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
        "name": "Arts, Culture, Religion",
        "updateDate": "2026-02-27T17:15:53Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7549ih.xml"
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
      "title": "National Council on African American History and Culture Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-24T07:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "National Council on African American History and Culture Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-24T07:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a National Council on African American History and Culture within the National Endowment for the Humanities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-24T07:03:28Z"
    }
  ]
}
```
