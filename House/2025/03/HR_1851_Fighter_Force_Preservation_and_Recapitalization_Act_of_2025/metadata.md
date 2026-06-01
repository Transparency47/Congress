# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1851?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1851
- Title: Fighter Force Preservation and Recapitalization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1851
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-12-05T22:55:37Z
- Update date including text: 2025-12-05T22:55:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1851",
    "number": "1851",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001298",
        "district": "2",
        "firstName": "Don",
        "fullName": "Rep. Bacon, Don [R-NE-2]",
        "lastName": "Bacon",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Fighter Force Preservation and Recapitalization Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:55:37Z",
    "updateDateIncludingText": "2025-12-05T22:55:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:04:15Z",
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
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CO"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MI"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "OH"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "SD"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "MD"
    },
    {
      "bioguideId": "S001148",
      "district": "2",
      "firstName": "Michael",
      "fullName": "Rep. Simpson, Michael K. [R-ID-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Simpson",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "ID"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
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
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "LA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "sponsorshipWithdrawnDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CO"
    },
    {
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "SC"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MO"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OK"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "IN"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "IN"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "M001199",
      "district": "21",
      "firstName": "Brian",
      "fullName": "Rep. Mast, Brian J. [R-FL-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Mast",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "IN"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "N000015",
      "district": "1",
      "firstName": "Richard",
      "fullName": "Rep. Neal, Richard E. [D-MA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Neal",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MN"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000687",
      "district": "7",
      "firstName": "Kweisi",
      "fullName": "Rep. Mfume, Kweisi [D-MD-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mfume",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "MD"
    },
    {
      "bioguideId": "M001236",
      "district": "14",
      "firstName": "Tim",
      "fullName": "Rep. Moore, Tim [R-NC-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "NC"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "MD"
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
      "sponsorshipDate": "2025-06-24",
      "state": "IN"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-07",
      "state": "AZ"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "AZ"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "ID"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1851ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1851\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Bacon (for himself, Mr. Crow , Mr. Bergman , Ms. Elfreth , Mr. James , Ms. Kaptur , Mr. Harris of Maryland , Mr. Johnson of South Dakota , and Mr. Hoyer ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to preserve and recapitalize the fighter aircraft capabilities of the Air Force and its reserve components, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fighter Force Preservation and Recapitalization Act of 2025 .\n#### 2. Minimum number of fighter aircraft in the Air Force and reserve components of the Air Force\nSection 9062(i) of title 10, United Stats Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking During and inserting Except as provided in paragraph (2), during ;\n**(B)**\nby striking October 1, 2026 and inserting October 1, 2030 ;\n**(C)**\nby striking 1,800 and inserting 1,900 ; and\n**(D)**\nby striking 1,145 and inserting 1,200 ;\n**(2)**\nby redesignating paragraph (2) as paragraph (3);\n**(3)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) (A) Subject to subparagraphs (B) and (C), the Secretary of Defense may temporarily reduce the total aircraft inventory required by paragraph (1) to enable recapitalization of units transitioning from one combat-coded mission fighter aircraft to a new combat-coded fighter aircraft. (B) A temporary reduction authorized under subparagraph (A) shall not\u2014 (i) result in less than 1,800 aircraft in the total aircraft inventory of fighter aircraft at any given time; or (ii) exceed two years. (C) (i) Before authorizing a temporary reduction under subparagraph (A), the Secretary of Defense shall\u2014 (I) provide notification to the congressional defense committees; and (II) identify in such notification the specific units to be recapitalized. (ii) The Secretary of Defense may satisfy the requirement for notification under this subparagraph if the Secretary includes such notification in a fiscal-year quarterly report required by subsection (n). ; and\n**(4)**\nin paragraph (3), as redesignated by paragraph (2), by striking In this subsection: and all that follows through The term primary mission aircraft inventory means and inserting In this subsection, the term primary mission aircraft inventory means .\n#### 3. Annual report on status of total fighter aircraft inventory\nSection 9062 of title 10, United States Code, as amended by section 2, is further amended by adding at the end the following new subsection:\n(n) (1) Not later than 90 days after the date of the enactment of the Fighter Force Preservation and Recapitalization Act of 2025 , and at the end of each fiscal-year quarter thereafter through September 30, 2030, the Secretary of the Air Force shall submit to the congressional defense committees a report describing the status of the total aircraft inventory requirement for fighter aircraft established by subsection (i). (2) Each report required by paragraph (1) shall include the following: (A) The overall number of new advanced capability fighter aircraft, fifth-generation fighter aircraft, and next-generation air dominance fighter aircraft received by the Air Force during the fiscal-year quarter covered by the report. (B) The mission design series prefix of each airframe received. (C) The vendor from which each new fighter aircraft was received. (D) The number of new advanced capability fighter aircraft and fifth-generation fighter aircraft assigned to units of the Regular Air Force, the Air Force Reserve, and the Air National Guard during the fiscal-year quarter covered by the report. (E) The distribution ratios of new fighter aircraft received from vendors during the fiscal-year covered by the report and assigned to units of the Regular Air Force, the Air Force Reserve, and the Air National Guard, including\u2014 (i) the percentage of total new advanced capability fighter aircraft and new fifth-generation fighter aircraft received that were assigned to each component (Regular Air Force, Air Force Reserve, and Air National Guard); and (ii) the percentage of aircraft assigned to each component, disaggregated by mission design series prefix. (F) The number of legacy capability fighter aircraft retired or divested by the Regular Air Force, the Air Force Reserve, and the Air National Guard during the fiscal-year quarter covered by the report, disaggregated by unit. (G) An identification of fighter aircraft units scheduled for recapitalization, including any associated authorizations for a temporary reduction in the minimum total aircraft inventory level for fighter aircraft established by subsection (i). (H) Any notable trends, issues, or challenges related to the receipt and assignment of new fighter aircraft during the fiscal-year quarter covered by the report, including any delays, discrepancies, or other factors that may have impacted such receipt or assignment. (3) Each report required by paragraph (1) shall be submitted in unclassified form, unless the Secretary of the Air Force determines that the inclusion of classified information in the report is necessary, in which case the report may be submitted in classified form or with classified annexes or sections. (4) Notwithstanding any other provision of law, if the Secretary of the Air Force does not submit a report required by paragraph (1) to the congressional defense committees by the deadline established by such paragraph, no funds may be obligated or expended for travel by the Secretary of the Air Force until the report is submitted. .\n#### 4. Recapitalization prioritization of Air Force service-retained fighter fleet\nSection 9062 of title 10, United States Code, as amended by sections 2 and 3, is further amended by adding at the end the following new subsection:\n(o) (1) The Secretary of the Air Force shall ensure that for every four new advanced capability fighter aircraft, fifth-generation fighter aircraft, and next-generation air dominance fighter aircraft accepted by the Air Force, not less than three shall be assigned and delivered to a fighter aircraft squadron of the Air Force that\u2014 (A) exists as of the date of the enactment of the Fighter Force Preservation and Recapitalization Act of 2025 ; and (B) is service retained. (2) For each new advanced capability fighter aircraft, fifth-generation fighter aircraft, or next-generation air dominance fighter aircraft assigned and delivered to a fighter aircraft squadron under paragraph (1), the Secretary of the Air Force may retire a legacy capability fighter aircraft from that squadron on a one-for-one basis. .\n#### 5. Preservation and recapitalization of Air National Guard fighter fleet\nSection 9062 of title 10, United States Code, as amended by sections 2 through 4, is further amended by adding at the end the following new subsection:\n(p) (1) Except as provided in paragraphs (2) and (3), during the period beginning on December 23, 2024, and ending on October 1, 2030, the Secretary of the Air Force\u2014 (A) shall maintain not less than 25 fighter aircraft squadrons of the Air National Guard, including the 25 fighter aircraft squadrons of the Air National Guard in existence as of December 23, 2024; and (B) may not retire, reduce funding for, or place in a status considered excess to the requirements of the possessing command and awaiting disposition instructions (commonly referred to as XJ status) any legacy capability fighter aircraft or fifth-generation fighter aircraft assigned to any of the 25 fighter aircraft squadrons of the Air National Guard in existence as of December 23, 2024. (2) The prohibition under paragraph (1)(B) shall not apply to individual legacy capability fighter aircraft, advanced capability fighter aircraft, or fifth-generation fighter aircraft that the Secretary of the Air Force determines, on a case-by-case basis, to be no longer mission capable and uneconomical to repair because of aircraft accidents, mishaps, or excessive material degradation and non-airworthiness status of certain aircraft. (3) For each new advanced capability fighter aircraft or fifth-generation fighter aircraft assigned and delivered to a fighter aircraft squadron maintained under paragraph (1)(A), the Secretary of the Air Force may retire a legacy capability fighter aircraft from that squadron on a one-for-one basis. (4) Section 2244a of this title shall not apply to the implementation of this subsection. .\n#### 6. Annual recapitalization plan for Air National Guard fighter fleet\nSection 9062 of title 10, United States Code, as amended by sections 2 through 5, is further amended by adding at the end the following new subsection:\n(q) (1) The Secretary of the Air Force, in consultation with the Director of the Air National Guard, shall annually develop a plan to recapitalize the fighter fleet of the Air National Guard. (2) The plan required under paragraph (1) shall\u2014 (A) identify each of the 25 fighter aircraft squadrons of the Air National Guard in existence on the date of the enactment of this subsection; (B) provide a plan for recapitalization of all such squadrons at a similar rate as the fighter aircraft squadrons of the active components of the Armed Forces, with the same combination of legacy capability fighter aircraft and advanced capability fighter aircraft found in fighter aircraft squadrons of the active Air Force; (C) establish a timetable for a plan or actions for the recapitalization proposed under subparagraph (B) through October 1, 2030, disaggregated by fighter aircraft squadron and fiscal year, which shall identify funding required for each fiscal year; (D) assess budgetary effects on the active components of the Armed Forces if the recapitalization plan proposed under subparagraph (B) were implemented in accordance with the timeline established under subparagraph (C); (E) assess the effects of such plan on the operational readiness and personnel readiness of the active and reserve components of the Armed Forces, including the effects of such plan on the ability of such components to meet steady state and contingency force presentation and mission requirements of combatant commanders; and (F) examine the feasibility of acquiring F\u201316 Block 70 fighter aircraft for the Air National Guard. (3) (A) Not later than July 1 of each year through July 1, 2030, the Secretary of the Air Force shall submit to the congressional defense committees a report that includes the plan required under paragraph (1). (B) The report required under subparagraph (A) shall be submitted in unclassified form, but may contain a classified annex. .\n#### 7. Definitions\nSection 9062 of title 10, United States Code, as amended by sections 2 through 6, is further amended by adding at the end the following new subsection:\n(r) In this section: (1) The term advanced capability fighter aircraft \u2014 (A) means any new production variant of an airframe type specified in paragraph (4), including\u2014 (i) the F\u201316 Block 70/72 and any subsequent block; and (ii) the F\u201315EX and any subsequent variant; and (B) does not include a modified or upgraded version of a legacy capability fighter aircraft. (2) The term fifth-generation fighter aircraft means an F\u201322 aircraft or an F\u201335 aircraft. (3) The term fighter aircraft means an aircraft that\u2014 (A) is designated by a mission design series prefix of F\u2013 or A\u2013; (B) includes one or two crewmembers on board the aircraft when in operation; and (C) (i) executes single-role or multi-role missions, including air-to-air combat, air-to-ground attack, air interdiction, suppression or destruction of enemy air defenses, close air support, strike control and reconnaissance, combat search and rescue support, or airborne forward air control; or (ii) operates collaboratively with an uncrewed aircraft operating semi-autonomously in proximity. (4) The term legacy capability fighter aircraft means a pre-fifth-generation fighter aircraft, including\u2014 (A) an F\u201316 aircraft, whether pre-block or post-block; (B) an F\u201315C/D/E aircraft; or (C) an A\u201310C aircraft. (5) The term next-generation air dominance fighter aircraft \u2014 (A) means\u2014 (i) a sixth-generation fighter aircraft capable of interacting collaboratively with uncrewed aircraft operating semi-autonomously in proximity; or (ii) any other fighter aircraft referenced or designated as a sixth-generation airframe; and (B) does not include uncrewed fighter-type aircraft. (6) The term service retained , with respect to a fighter aircraft unit or a fighter aircraft, means that the unit or aircraft\u2014 (A) is controlled by the Regular Air Force, the Air Force Reserve, or the Air National Guard for operational, training, or administrative purposes of the component concerned; and (B) is not assigned to, or under the operational control of, a combatant command or joint task force. .",
      "versionDate": "2025-03-05",
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
        "actionDate": "2025-03-05",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "873",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Fighter Force Preservation and Recapitalization Act of 2025",
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
        "updateDate": "2025-05-20T02:22:08Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1851ih.xml"
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
      "title": "Fighter Force Preservation and Recapitalization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fighter Force Preservation and Recapitalization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to preserve and recapitalize the fighter aircraft capabilities of the Air Force and its reserve components, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T10:48:22Z"
    }
  ]
}
```
