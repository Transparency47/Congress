# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/608
- Title: COVER Now Act
- Congress: 119
- Bill type: HR
- Bill number: 608
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2026-02-04T05:06:18Z
- Update date including text: 2026-02-04T05:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/608",
    "number": "608",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "COVER Now Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:18Z",
    "updateDateIncludingText": "2026-02-04T05:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:04:50Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TN"
    },
    {
      "bioguideId": "C000537",
      "district": "6",
      "firstName": "James",
      "fullName": "Rep. Clyburn, James E. [D-SC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyburn",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "SC"
    },
    {
      "bioguideId": "C001063",
      "district": "28",
      "firstName": "Henry",
      "fullName": "Rep. Cuellar, Henry [D-TX-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Cuellar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "E000299",
      "district": "16",
      "firstName": "Veronica",
      "fullName": "Rep. Escobar, Veronica [D-TX-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Escobar",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
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
      "sponsorshipDate": "2025-01-22",
      "state": "AL"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MS"
    },
    {
      "bioguideId": "T000489",
      "district": "18",
      "firstName": "Sylvester",
      "fullName": "Rep. Turner, Sylvester [D-TX-18]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
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
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "GA"
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
      "sponsorshipDate": "2025-01-22",
      "state": "FL"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MO"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "VA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sponsorshipDate": "2025-01-22",
      "state": "MD"
    },
    {
      "bioguideId": "C001130",
      "district": "30",
      "firstName": "Jasmine",
      "fullName": "Rep. Crockett, Jasmine [D-TX-30]",
      "isOriginalCosponsor": "False",
      "lastName": "Crockett",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "TX"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "FL"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr608ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 608\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Doggett (for himself, Mr. Bishop , Mr. Casar , Ms. Castor of Florida , Mr. Castro of Texas , Mr. Cohen , Mr. Clyburn , Mr. Cuellar , Ms. Escobar , Mr. Figures , Mrs. Fletcher , Ms. Lois Frankel of Florida , Ms. Garcia of Texas , Mr. Green of Texas , Mr. Johnson of Georgia , Ms. Johnson of Texas , Mrs. McBath , Mrs. Cherfilus-McCormick , Mr. David Scott of Georgia , Ms. Sewell , Mr. Soto , Mr. Thompson of Mississippi , Mr. Turner of Texas , Mr. Veasey , Ms. Wasserman Schultz , Ms. Williams of Georgia , Ms. Wilson of Florida , Ms. Adams , Mr. Cleaver , Mr. Connolly , Ms. Norton , and Mr. Raskin ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to provide for a demonstration project under the Medicaid program for political subdivisions of States to provide medical assistance for the expansion population under such program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cover Outstanding Vulnerable Expansion-eligible Residents Now Act or the COVER Now Act .\n#### 2. Demonstration project for political subdivisions of States to provide medical assistance for Medicaid expansion population\n##### (a) In general\nSection 1902 of the Social Security Act is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (86), by striking at the end and ;\n**(B)**\nin paragraph (87), by striking the period at the end and inserting ; and ; and\n**(C)**\nby inserting after paragraph (87) the following new paragraph:\n(88) provide, at the option of the qualifying political subdivisions of a State, for a demonstration project described in subsection (uu). ; and\n**(2)**\nby adding at the end the following new subsection:\n(uu) Demonstration project for political subdivisions of States To provide medical assistance for expansion population (1) In general Notwithstanding section subsection (a)(5), the Secretary shall conduct a demonstration project under which the Secretary shall, subject to paragraph (9), select qualifying political subdivisions described in paragraph (2) to provide, in accordance with the requirements of this subsection, medical assistance for individuals described in subclause (VIII) of subsection (a)(10)(A)(i) who reside in such political subdivisions in accordance with the timeline specified under paragraph (8). (2) Waiver authority The Secretary may waive the requirements of paragraphs (1) and (5) of subsection (a) relating to statewideness and relating to single state agency, respectively. (3) Qualifying political subdivision A qualifying political subdivision described in this paragraph is\u2014 (A) a political subdivision\u2014 (i) located in a State that has not elected to provide medical assistance for individuals described in subclause (VIII) of subsection (a)(10)(A)(i) as of the date of the enactment of this subsection; and (ii) submits an application to the Secretary\u2014 (I) at such time, in such manner, and containing such information as the Secretary may require; and (II) which has undergone a process for public notice and comment at the political subdivision level, including public hearings, sufficient to ensure a meaningful level of public input; or (B) any number of political subdivisions described in subparagraph (A) which form a partnership for purposes of implementing the demonstration project under this subsection. (4) Length of demonstration project (A) In general Subject to subparagraph (B), a qualifying political subdivision selected to participate in the demonstration project under this subsection or partnership described in paragraph (3)(B) (referred to in this subsection as a participating political subdivision ) shall provide medical assistance for individuals described in subclause (VIII) of subsection (a)(10)(A)(i) for seven years or through the day before the date on which the State in which such political subdivision is located provides for medical assistance under the State plan (or a waiver of such plan) for such individuals, whichever is shorter. (B) Extension A participating political subdivision that participates in the demonstration project under this subsection for five years may extend its participation in the demonstration project by submitting an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require. Under such extension, such political subdivision shall provide medical assistance for individuals described in subclause (VIII) of subsection (a)(10)(A)(i) for up to an additional five years or through the day before the date on which the State in which such political subdivision is located provides for medical assistance under the State plan (or a waiver of such plan) for such individuals, whichever is shorter. (C) Automatic enrollment in case of States that elect to provide medical assistance for expansion population In the case of a participating political subdivision whose participation in the demonstration project under this subsection ends because the State in which such political subdivision is located elects to provide for medical assistance under the State plan (or a waiver of such plan) for individuals described in subclause (VIII) of subsection (a)(10)(A)(i), such State shall automatically enroll under such State plan (or waiver) any eligible and enrolled individual so described receiving medical assistance from such political subdivision and coverage for such individual under such State plan (or waiver) beginning with the first day on which the State provides medical assistance under such State plan (or waiver) for individuals described in subclause (VIII) of subsection (a)(10)(A)(i). (5) Payments (A) In general The Secretary shall pay a participating political subdivision the Federal matching percentage specified in subparagraph (B) for amounts expended by such political subdivision to provide medical assistance for individuals described in subclause (VIII) of subsection (a)(10)(A)(i). (B) Calculation of Federal and non-Federal share Except as provided under clause (ii) and subparagraph (C), the calculation and payment of the Federal and non-Federal share of expenditures for medical assistance under a demonstration described in paragraph (1) shall be calculated in accordance with section 1903 as if the qualifying political subdivision was a State. (C) Federal matching percentage The Federal matching percentage specified in this subparagraph, with respect to a participating political subdivision and the demonstration project under this subsection, is\u2014 (i) 100 percent for calendar quarters in the first three years that such political subdivision participates in such demonstration project, if applicable; (ii) with respect to a participating political subdivision which\u2014 (I) includes a rural political subdivision (as defined by the Office of Management and Budget), 100 percent for calendar quarters in the fourth year that such political subdivision participates in such demonstration project, if applicable; and (II) does not include a rural political subdivision (as defined by the Office of Management and Budget), 95 percent for calendar quarters in the fourth year that such political subdivision participates in such demonstration project, if applicable; (iii) with respect to a participating political subdivision which\u2014 (I) includes a rural political subdivision (as defined by the Office of Management and Budget), 95 percent for calendar quarters in the fifth year that such political subdivision participates in such demonstration project, if applicable; and (II) does not include a rural political subdivision (as defined by the Office of Management and Budget), 94 percent for calendar quarters in the fifth year that such political subdivision participates in such demonstration project, if applicable; (iv) with respect to a participating political subdivision which\u2014 (I) includes a rural political subdivision (as defined by the Office of Management and Budget), 94 percent for calendar quarters in the sixth year that such political subdivision participates in such demonstration project, if applicable; and (II) does not include a rural political subdivision (as defined by the Office of Management and Budget), 93 percent for calendar quarters in the sixth year that such political subdivision participates in such demonstration project, if applicable; (v) with respect to a participating political subdivision which\u2014 (I) includes a rural political subdivision (as defined by the Office of Management and Budget), 93 percent for calendar quarters in the seventh year that such political subdivision participates in such demonstration project, if applicable; and (II) does not include a rural political subdivision (as defined by the Office of Management and Budget), 90 percent for calendar quarters in the seventh year that such political subdivision participates in such demonstration project, if applicable; and (vi) 90 percent for calendar quarters in the eighth year and any subsequent years thereafter that such political subdivision participates in such demonstration project, if applicable. (6) Comparability of benefits to essential health benefits The medical assistance made available by a participating political subdivision to individuals described in subclause (VIII) of subsection (a)(10)(A)(i) shall consist of coverage described in subsection (k)(1). (7) Reduction in Federal funding for medical assistance for states that take certain actions (A) In general In the case of a State that does any of the prohibited items described in subparagraph (B), the Secretary shall withhold from the amount otherwise payable under section 1903 an amount equal to 25 percent of the amount of administrative costs under the State plan under title XIX during a calendar. (B) Prohibited items For purposes of subparagraph (A), a State may not\u2014 (i) shift the costs of providing medical assistance to individuals enrolled under a State plan under title XIX to a political subdivision that establishes a demonstration project under this subsection by disenrolling such individuals from the State plan to the demonstration project of the political subdivision; (ii) withhold or reduce any kind of funding or State support to political subdivision on account of the political subdivision\u2019s establishment of a demonstration project; (iii) increase taxes on taxpayers of a political subdivision on account of the political subdivision\u2019s establishment of a demonstration project; (iv) require a political subdivision to increase or lower a tax rate required by the political subdivision on account of the political subdivision\u2019s establishment of a demonstration project; (v) prohibit a political subdivision from participating in a demonstration project pursuant to this subsection; (vi) prohibit a political subdivision from participating in a Federal demonstration project, establishing or expanding a health coverage program, contracting or otherwise entering into an agreement with the Centers for Medicare & Medicaid Services, or receiving Federal funding directly from a Federal agency; (vii) prohibit a health care provider, hospital, federally qualified health center, or rural health clinic from\u2014 (I) accepting patients with health coverage provided by a political subdivision; (II) accepting payments from a political subdivision; (III) making payments, including taxes, to a political subdivision; or (IV) participating in the State Medicaid program on account of participation in a demonstration project pursuant to this subsection; (viii) refuse to allow a political subdivision to rely on State Medicaid systems and State Medicaid agency staff to implement a demonstration project, including\u2014 (I) the State\u2019s Medicaid eligibility check and enrollment system; (II) provider payment system; (III) claims processing system; (IV) fair hearing system; and (V) Federal reporting requirement system; or (ix) take any other punitive action against a political subdivision that establish a demonstration project. (8) Timeline specified For purposes of paragraph (1), the timeline specified in this paragraph shall require\u2014 (A) not later than 180 days after the date of the enactment of this subsection, the Secretary to promulgate any regulations necessary to carry out this subsection, including\u2014 (i) the application requirements for a political subdivision to apply for a demonstration project, criteria on which applications will be reviewed, and how long political subdivisions have to begin the demonstration once an application is approved; and (ii) the application of all requirements under section 1903 to a participating political subdivision as if it was a State; (B) not later than 180 days after receiving an application from a qualifying political subdivision described in paragraph (3), the Secretary to transmit a notice to such qualifying political subdivision of the application\u2019s approval or rejection, and in case of a rejection an explanation for the rejection; and (C) not later than 7 years after the approval of an application, the Secretary to transmit a notice to such qualifying political subdivision of the application\u2019s approval or rejection for an extension under this subsection. (9) Limitation on number of demonstration projects The Secretary may not approve more than 100 demonstration projects under this subsection, which may consist of demonstration projects implemented by a single participating political subdivision or implemented as partnerships formed by multiple participating political subdivisions (as described in paragraph (3)(B)). (10) Application without regard to budget neutrality The Secretary shall not require, as a condition for carrying out the demonstration project under this subsection, that the demonstration project ensure that such model is budget neutral initially with respect to expenditures under the applicable title. (11) Report Not later than 4 years after the first date of the demonstration project, the Secretary shall submit a report to Congress on\u2014 (A) the effect of the demonstration project on\u2014 (i) the number of beneficiaries enrolled in demonstration projects under this subsection; and (ii) the amount of uncompensated care costs for State Medicaid plans; and (B) whether any States with a demonstration project under this subsection have expanded Medicaid coverage under the Patient Protection and Affordable Care Act. .\n##### (b) Payment to States\nSection 1903(a) of the Social Security Act ( 42 U.S.C. 1396b(a) ) is amended\u2014\n**(1)**\nin paragraph (6), by striking at the end plus ;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; plus ; and\n**(3)**\nby adding at the end the following new paragraph:\n(8) an amount equal to an increase of 5 percentage points to Federal matching percentage for administrative costs for every 100,000 individuals described in paragraph (1) of section 1115(g) who are enrolled in a demonstration project of a participating political subdivision (as referred to in paragraph (4)(A) of such section) during a calendar quarter. .",
      "versionDate": "2025-01-22",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-03T18:09:39Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-03-03T18:09:39Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-03T18:09:39Z"
          },
          {
            "name": "Medicaid",
            "updateDate": "2025-03-03T18:09:39Z"
          },
          {
            "name": "State and local finance",
            "updateDate": "2025-03-03T18:09:39Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-03-03T18:09:39Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-24T20:23:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr608",
          "measure-number": "608",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr608v00",
            "update-date": "2025-03-10"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Cover Outstanding Vulnerable Expansion-eligible Residents Now Act or the COVER Now Act</b></p> <p>This bill establishes a demonstration program to allow local governments to provide health benefits to the Medicaid expansion population in states that have not expanded Medicaid. </p> <p>Under the program, local governments may provide coverage for individuals who are newly eligible for Medicaid under the Patient Protection and Affordable Care Act (i.e., the Medicaid expansion population) for a maximum of 10 years, or until their respective states expand Medicaid. The bill provides a 100% federal matching rate for the first three years of program participation.</p> <p>The bill prohibits states from taking certain actions against participating localities, such as withholding funding, increasing taxes, or restricting provider participation. States that violate these requirements are subject to certain funding penalties.</p>"
        },
        "title": "COVER Now Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr608.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Cover Outstanding Vulnerable Expansion-eligible Residents Now Act or the COVER Now Act</b></p> <p>This bill establishes a demonstration program to allow local governments to provide health benefits to the Medicaid expansion population in states that have not expanded Medicaid. </p> <p>Under the program, local governments may provide coverage for individuals who are newly eligible for Medicaid under the Patient Protection and Affordable Care Act (i.e., the Medicaid expansion population) for a maximum of 10 years, or until their respective states expand Medicaid. The bill provides a 100% federal matching rate for the first three years of program participation.</p> <p>The bill prohibits states from taking certain actions against participating localities, such as withholding funding, increasing taxes, or restricting provider participation. States that violate these requirements are subject to certain funding penalties.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr608"
    },
    "title": "COVER Now Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Cover Outstanding Vulnerable Expansion-eligible Residents Now Act or the COVER Now Act</b></p> <p>This bill establishes a demonstration program to allow local governments to provide health benefits to the Medicaid expansion population in states that have not expanded Medicaid. </p> <p>Under the program, local governments may provide coverage for individuals who are newly eligible for Medicaid under the Patient Protection and Affordable Care Act (i.e., the Medicaid expansion population) for a maximum of 10 years, or until their respective states expand Medicaid. The bill provides a 100% federal matching rate for the first three years of program participation.</p> <p>The bill prohibits states from taking certain actions against participating localities, such as withholding funding, increasing taxes, or restricting provider participation. States that violate these requirements are subject to certain funding penalties.</p>",
      "updateDate": "2025-03-10",
      "versionCode": "id119hr608"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr608ih.xml"
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
      "title": "COVER Now Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "COVER Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cover Outstanding Vulnerable Expansion-eligible Residents Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-21T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to provide for a demonstration project under the Medicaid program for political subdivisions of States to provide medical assistance for the expansion population under such program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T04:48:32Z"
    }
  ]
}
```
