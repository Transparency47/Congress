# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2790?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2790
- Title: GOSAFE Act
- Congress: 119
- Bill type: HR
- Bill number: 2790
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2026-05-15T20:52:40Z
- Update date including text: 2026-05-15T20:52:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2790",
    "number": "2790",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001208",
        "district": "6",
        "firstName": "Lucy",
        "fullName": "Rep. McBath, Lucy [D-GA-6]",
        "lastName": "McBath",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "GOSAFE Act",
    "type": "HR",
    "updateDate": "2026-05-15T20:52:40Z",
    "updateDateIncludingText": "2026-05-15T20:52:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:01:15Z",
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
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "GA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-09",
      "state": "TX"
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
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "PA"
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
      "sponsorshipDate": "2025-04-09",
      "state": "DC"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "ME"
    },
    {
      "bioguideId": "S001221",
      "district": "3",
      "firstName": "Hillary",
      "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scholten",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
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
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MI"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "MO"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "OR"
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
      "sponsorshipDate": "2025-04-09",
      "state": "NY"
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
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NC"
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
      "sponsorshipDate": "2025-04-09",
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
      "sponsorshipDate": "2025-04-09",
      "state": "AL"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "B001318",
      "district": "0",
      "firstName": "Becca",
      "fullName": "Rep. Balint, Becca [D-VT-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Balint",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "VT"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "MD"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "CA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-08-22",
      "state": "IL"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NJ"
    },
    {
      "bioguideId": "R000620",
      "district": "29",
      "firstName": "Luz",
      "fullName": "Rep. Rivas, Luz M. [D-CA-29]",
      "isOriginalCosponsor": "False",
      "lastName": "Rivas",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "TN"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "CA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MA"
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MN"
    },
    {
      "bioguideId": "M001220",
      "district": "3",
      "firstName": "Morgan",
      "fullName": "Rep. McGarvey, Morgan [D-KY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "McGarvey",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "KY"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "TX"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MN"
    },
    {
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "NY"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CT"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "CO"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "MO"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "AL"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2790ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2790\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mrs. McBath (for herself, Mr. Johnson of Georgia , Mr. Krishnamoorthi , Mr. Auchincloss , Mr. Deluzio , Ms. Garcia of Texas , Ms. Wilson of Florida , Mr. Evans of Pennsylvania , Ms. Scanlon , Ms. Norton , Ms. Pingree , Ms. Scholten , Mr. Davis of Illinois , Mr. Frost , Mr. Carbajal , Mr. Thanedar , Mr. Menendez , Ms. Brownley , Mr. Cleaver , Ms. Salinas , Mr. Goldman of New York , Mr. Schneider , Mr. Gottheimer , Mrs. Foushee , Ms. Kelly of Illinois , Ms. Sewell , and Mr. Casten ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to restrict the possession of certain firearms, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gas-Operated Semi-Automatic Firearms Exclusion Act or the GOSAFE Act .\n#### 2. Restrictions\n##### (a) Definitions\nSection 921(a) of title 18, United States Code, is amended by adding at the end the following:\n(39) The term semi-automatic firearm means any firearm that\u2014 (A) upon initiating the firing sequence, fires the first chambered cartridge and uses a portion of the energy of the firing cartridge to\u2014 (i) extract the expended cartridge case; (ii) chamber the next round; and (iii) prepare the firing mechanism to fire again; (B) requires a separate pull, release, push, or initiation of the trigger to fire each cartridge; and (C) is not a machinegun. (40) The term cycle the action , with respect to a firearm, means to extract the fired cartridge case, chamber the next cartridge, and prepare the firing mechanism to fire again. (41) The term gas-operated , with respect to a semi-automatic firearm, means any firearm that harnesses or traps a portion of the high-pressure gas from a fired cartridge to cycle the action using\u2014 (A) a long stroke piston, where gas is vented from the barrel to a piston that is mechanically fixed to the bolt group and moves to cycle the action; (B) a short stroke piston, where gas is vented from the barrel to a piston that moves separately from the bolt group so that the energy is imparted through a gas piston to cycle the action; (C) a system that traps and vents gas from either the barrel or the chamber to directly strike or impinge the bolt, bolt carrier, or slide assembly, to unlock and cycle the action; (D) a hybrid system that combines elements of a system described in subparagraph (C) with a system described in subparagraph (A) or (B) to capture gas vented from the barrel to cycle the action; (E) a blowback-operated system that directly utilizes the expanding gases of the ignited propellant powder acting on the cartridge case to drive the breechblock or breech bolt rearward; or (F) a recoil-operated system that utilizes the recoil force to unlock the breech bolt and then to complete the cycle of extracting, ejecting, and reloading. (42) The term large capacity ammunition feeding device \u2014 (A) means a magazine, belt, drum, feed strip, helical feeding device, or similar device, including any such device joined or coupled with another in any manner, that\u2014 (i) has an overall capacity of, or that can be readily restored, altered, or converted to accept, more than 10 rounds of ammunition; and (ii) is not permanently fixed; and (B) does not include any device designed to accept, and capable of operating only with, .22 or less caliber rimfire ammunition. .\n##### (b) Prohibitions\nSection 922 of title 18, United States Code, is amended\u2014\n**(1)**\nby inserting after subsection (u) the following:\n(v) (1) Except as provided in paragraph (2) or (4), it shall be unlawful for any person to import, sell, manufacture, transfer, receive, or possess, in or affecting interstate or foreign commerce, a firearm, device, or combination of parts described in subparagraphs (A) through (H), knowing or having reasonable cause to believe that\u2014 (A) the firearm is included on the list of prohibited gas-operated semi-automatic firearms described in section 935(a); (B) the modified non-prohibited firearm, as modified, operates as a firearm included on the list of prohibited gas-operated semi-automatic firearms described in section 935(a); (C) the combination of parts is designed and functions to modify an otherwise non-prohibited firearm so that the firearm, as modified, operates as a gas-operated semi-automatic firearm included on the list of prohibited gas-operated semi-automatic firearms described in section 935(a); (D) the combination of parts is designed to be assembled into a firearm that operates as a firearm included on the list of prohibited gas-operated semi-automatic firearms described in section 935(a); (E) the combination of parts functions to produce a gas-operated semi-automatic cycling action that was not lawfully manufactured as part of an approved firearm design described in section 935(c); (F) the manual, power-driven, or electronic device is primarily designed, or redesigned, so that if the device is attached to a semi-automatic firearm the device\u2014 (i) materially increases the rate of fire of the firearm; or (ii) approximates the action or rate of fire of a machinegun; (G) the device, part, or combination of parts is designed and functions to materially increase the rate of fire of the semi-automatic firearm by eliminating the need for the operator of the firearm to make a separate movement for each individual function of the trigger; or (H) the semi-automatic firearm has been modified in any way that\u2014 (i) materially increases the rate of fire of the firearm; or (ii) approximates the action or rate of fire of a machinegun. (2) Paragraph (1) shall not apply to\u2014 (A) the importation or manufacture by or for, sale or transfer to, or possession by or under the authority of, the United States or any department or agency thereof or a State or Tribe, or a department, agency, or political subdivision thereof; (B) the importation or manufacture for, sale or transfer to, or possession by, a licensee under title I of the Atomic Energy Act of 1954 ( 42 U.S.C. 2011 et seq. ) for purposes of establishing and maintaining an on-site physical security protection system and security organization required by Federal law, or the transfer to, or possession by, a contractor of such a licensee on-site for such purposes or off-site for purposes of licensee-authorized training or transportation of nuclear materials; (C) the possession of a gas-operated semi-automatic firearm that, before the date of enactment of this subsection, was lawfully\u2014 (i) manufactured; and (ii) transferred by the manufacturer to another party; or (D) the transfer of a gas-operated semi-automatic firearm that is lawfully possessed before the date of enactment of this subsection in accordance with subparagraph (C), in which\u2014 (i) the transferee is an immediate family member of the transferor; (ii) the transfer occurs after a licensed importer, licensed manufacturer, or licensed dealer has first taken possession of the firearm for the purpose of complying with subsection (t) before such transfer to the immediate family member occurs; and (iii) upon taking possession of the firearm under clause (ii), the licensee to whom the firearm was transferred under clause (ii) complies with all requirements of this chapter as if the licensee were transferring the firearm from the business inventory of the licensee to the unlicensed transferee. (3) Licensed importers and licensed manufacturers shall mark all gas-operated semi-automatic firearms imported or manufactured under subparagraphs (A) and (B) of paragraph (2) after the date of enactment of this subsection in the manner prescribed by the Attorney General before any transfer under subparagraph (A) or (B) of paragraph (2). (4) For purposes of this subsection\u2014 (A) the term gas-operated semi-automatic firearm does not include\u2014 (i) any firearm designed to accept, and capable of operating only with, .22 caliber rimfire ammunition, provided that such firearm does not have a separate upper and lower receiver; (ii) a rifle that\u2014 (I) is a single-shot rifle; (II) is a breech loading rifle with a capacity not to exceed 2 rounds of ammunition; (III) is a muzzle-loading rifle or smoothbore shoulder-fired firearm; (IV) uses a bolt action, lever action, or pump action to cycle the action of the rifle; or (V) has a permanently fixed magazine with a capacity not to exceed 10 rounds of ammunition that cannot be converted or changed to accept more than 10 rounds of ammunition; (iii) a shotgun that\u2014 (I) is a single-shot shotgun; (II) is a breech loading shotgun with a capacity not to exceed 2 rounds of ammunition; (III) is a muzzle-loading shotgun; (IV) uses a bolt action, lever action, or pump action to cycle the action of the shotgun; (V) is a semi-automatic or auto-loading shotgun; or (VI) has a permanently fixed magazine with a capacity not to exceed 10 rounds of ammunition that cannot be converted or changed to accept more than 10 rounds of ammunition; (iv) a breech loading firearm capable of holding a single cartridge and not more than 2 shotgun shells simultaneously and that must be reloaded after firing those rounds of ammunition; or (v) a handgun that\u2014 (I) is a single-shot handgun; (II) is a breech loading handgun with a capacity not to exceed 2 rounds of ammunition; (III) is a muzzle-loading or smoothbore handgun; (IV) uses a bolt action to cycle the action of the handgun; (V) is a single or double action revolver; (VI) is a single or double action semi-automatic handgun that uses recoil to cycle the action of the handgun; or (VII) has a permanently fixed magazine with a capacity not to exceed 15 rounds of ammunition that cannot be converted or changed to accept more than 15 rounds of ammunition; and (B) the term immediate family member means, with respect to a person\u2014 (i) a spouse, parent, brother or sister, or child of that person, or an individual to whom that person stands in loco parentis; or (ii) any other person living in the household of that person and related to that person by blood or marriage. (w) (1) Except as provided in paragraph (3), it shall be unlawful, on and after the date of enactment of this subsection, for any person to, in or affecting interstate or foreign commerce\u2014 (A) import, sell, manufacture, transfer, or receive a large capacity ammunition feeding device; or (B) possess a large capacity ammunition feeding device manufactured after the date of enactment of this subsection. (2) It shall be unlawful for any person who lawfully owns or possesses a large capacity ammunition feeding device that was manufactured and purchased or transferred before such date of enactment to transfer, in or affecting interstate or foreign commerce, such device after the date of enactment of this subsection. (3) This subsection shall not apply with respect to\u2014 (A) the importation for, manufacture for, sale to, transfer to, or possession by or under the authority of, the United States or any department or agency thereof or a State or Tribe, or a department, agency, or political subdivision thereof; or (B) the importation or manufacture for, sale or transfer to, or possession by, a licensee under title I of the Atomic Energy Act of 1954 ( 42 U.S.C. 2011 et seq. ) for purposes of establishing and maintaining an on-site physical security protection system and security organization required by Federal law, or the transfer to, or possession by, a contractor of such a licensee on-site for such purposes or off-site for purposes of licensee-authorized training or transportation of nuclear materials. (4) Any licensed importer, licensed manufacturer, or other person in possession of a large capacity ammunition feeding device\u2014 (A) shall mark such large capacity ammunition feeding device imported or manufactured under subparagraph (A) or (B) of paragraph (3) after the date of enactment of this subsection in the manner prescribed by the Attorney General before any transfer under subparagraph (A) or (B) of paragraph (3); and (B) may not obliterate or otherwise alter the serial number on such large capacity ammunition feeding device. .\n#### 3. Use of Byrne grants for buy-back programs for gas-operated semi-automatic firearms and large capacity ammunition feeding devices\nSection 501(a)(1) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10152(a)(1) ) is amended by adding at the end the following:\n(J) Compensation for surrendered gas-operated semi-automatic firearms and large capacity ammunition feeding devices, as defined in section 921 of title 18, United States Code, under buy-back programs for gas-operated semi-automatic firearms and large capacity ammunition feeding devices. .\n#### 4. Penalties\nSection 924(a) of title 18, United States Code, is amended by adding at the end the following:\n(9) (A) Whoever violates subsection (v) or (w) of section 922 shall be fined not more than $5,000, imprisoned not more than 12 months, or both, for each offense. (B) Whoever, while in possession of a gas-operated semi-automatic firearm in violation of section 922(v), commits, or attempts to commit, any other Federal offense punishable by imprisonment for a term exceeding 1 year, shall, in addition to the punishment provided for such offense, be fined not more than $250,000, imprisoned for a term not less than 2 years and not more than 10 years, or both. .\n#### 5. Prohibited firearm determinations\n##### (a) Amendment\nChapter 44 of title 18, United States Code, is amended by adding at the end the following:\n935. Prohibited firearm determinations (a) Determination of prohibited firearms For purposes of carrying out section 922(v), not later than 180 days after the date of enactment of this section, the Attorney General, acting through the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives, shall publish, and update, a list of gas-operated semi-automatic firearms in or affecting interstate or foreign commerce that are subject to the prohibition in section 922(v). (b) Responsibilities In carrying out this section, the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives shall\u2014 (1) review applications and appeals from licensed manufacturers submitted under subsections (c) and (d); (2) require that each licensed dealer record purchaser acknowledgment of the list published under subsection (a) before any sale of a firearm that is not prohibited under that list; (3) before removing any gas-operated semi-automatic firearm from the list required under subsection (a), submit to the Attorney General clear and convincing evidence of whether the firearm should be removed from the list; and (4) advise the Attorney General on carrying out the authority described in subsection (a). (c) Applications for approval of firearm designs (1) In general Any semi-automatic firearm designed on or after the date of enactment of this section shall be required to have an approval under this subsection prior to the manufacture, in or affecting interstate or foreign commerce, of such firearm for sale to civilians. (2) Application for approval A licensed manufacturer may file with the Attorney General an application, under penalty of perjury, for approval for a semi-automatic firearm as not subject to the prohibition under section 922(v), which shall contain\u2014 (A) a detailed description of the specifications and operation of the firearm; (B) a physical sample of the firearm; (C) any patent application for the firearm; (D) marketing materials and plans; (E) an explanation of why the firearm should not be subject to the prohibition under section 922(v); (F) a description of any features that prevent modification of the firearm; and (G) any other information the Attorney General shall require. (3) Review of application (A) In general Not later than 240 days after the date on which an application is submitted under paragraph (2), the Attorney General shall review the application and issue a written determination approving or denying the application. (B) Request for information The Attorney General may request any additional information from the manufacturer necessary to make the determination under subparagraph (A). (4) Fees (A) In general Not later than 60 days after the date of enactment of this section, the Attorney General shall determine the appropriate fee structure for application submissions under this subsection by licensed manufacturers. (B) Consideration In determining the fee structure required under subparagraph (A), the Attorney General shall ensure that the fees collected are substantial enough to cover the necessary costs associated with carrying out the activities described in subparagraph (A). (C) Firearm Safety Trust Fund (i) Establishment There is established in the Treasury of the United States a fund to be known as the Firearm Safety Trust Fund . (ii) Deposits Notwithstanding section 3302 of title 31, there shall be deposited in the Firearm Safety Trust Fund\u2014 (I) all taxes collected by the Bureau of Alcohol, Tobacco, Firearms, and Explosives under subchapter A of chapter 53 of the Internal Revenue Code of 1986; and (II) any fees collected under this paragraph. (iii) Availability of amounts All amounts deposited in the Firearm Safety Trust Fund shall\u2014 (I) be deposited as offsetting collections into the Firearm Safety Trust Fund for use by the Attorney General in carrying out the requirements of the GOSAFE Act and the National Firearms Act ( 26 U.S.C. 5849 et seq. ); and (II) remain available until expended. (d) Appeals (1) In general Not later than 90 days after the date on which the Attorney General denies an application under subsection (c)(3), the licensed manufacturer may appeal the determination by filing an appeal with the Attorney General. (2) Review by Attorney General Not later than 180 days after the date on which an appeal is filed under paragraph (1), the Attorney General shall issue a written determination upholding or revising the denial of the application. (3) Judicial review (A) In general Upon a determination by the Attorney General to uphold the denial of an application under paragraph (2), the licensed manufacturer may file a petition for review of the determination in the appropriate district court of the United States. (B) Standard of proof In a review conducted under subparagraph (A), the court may set aside the determination if the determination is found to be arbitrary and capricious. (e) Private right of action (1) In general If the Attorney General, acting through the Director of the Bureau of Alcohol, Tobacco, Firearms, and Explosives, removes any gas-operated semi-automatic firearm from the list of gas-operated semi-automatic firearms required under subsection (a), any person may file an action in an appropriate district court of the United States for review of such removal. (2) Standard of proof In a review conducted under paragraph (1), the court may grant the petitioner injunctive relief if the determination is found to be arbitrary and capricious. (f) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary to carry out this section, and any amounts so appropriated shall remain available until expended. .\n##### (b) Table of sections\nThe table of sections for chapter 44 of title 18, United States Code, is amended by inserting after the item relating to section 934 the following:\n935. Prohibited firearm determinations. .",
      "versionDate": "2025-04-09",
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
        "actionDate": "2025-04-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1370",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "GOSAFE Act",
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
        "updateDate": "2025-05-16T17:41:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
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
          "measure-id": "id119hr2790",
          "measure-number": "2790",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-09",
          "originChamber": "HOUSE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2790v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Gas-Operated Semi-Automatic Firearms Exclusion Act or the GOSAFE Act</strong></p><p>This bill establishes a framework to regulate gas-operated semiautomatic firearms and large capacity ammunition feeding devices under federal firearms laws.</p><p>First, the bill generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a firearm that is or is modified to operate as a prohibited gas-operated semiautomatic firearm;</li><li>a combination of parts that modify or can be\u00a0assembled into\u00a0a prohibited gas-operated semiautomatic firearm, or that produce an unlawful gas-operated semiautomatic cycling action;</li><li>a device or combination of parts designed to materially increase the rate of fire of a semiautomatic firearm; or</li><li>a firearm that is modified to materially increase the rate of fire.</li></ul><p>Second, the bill generally prohibits (1) the import, sale, manufacture, transfer, or receipt of a large capacity ammunition feeding device; or (2) the possession of a large capacity ammunition feeding device manufactured after the date of enactment.\u00a0</p><p>A violation is subject to criminal penalties\u2014a fine, a prison term of up to 12 months, or both, for each violation.\u00a0</p><p>In addition, an individual who possesses a prohibited gas-operated semiautomatic firearm during a\u00a0federal felony offense is subject to additional penalties\u2014a\u00a0fine, a mandatory minimum prison term of two years, or both.</p><p>Finally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender gas-operated semiautomatic firearms and large capacity ammunition feeding devices under a buy-back program.</p>"
        },
        "title": "GOSAFE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2790.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gas-Operated Semi-Automatic Firearms Exclusion Act or the GOSAFE Act</strong></p><p>This bill establishes a framework to regulate gas-operated semiautomatic firearms and large capacity ammunition feeding devices under federal firearms laws.</p><p>First, the bill generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a firearm that is or is modified to operate as a prohibited gas-operated semiautomatic firearm;</li><li>a combination of parts that modify or can be\u00a0assembled into\u00a0a prohibited gas-operated semiautomatic firearm, or that produce an unlawful gas-operated semiautomatic cycling action;</li><li>a device or combination of parts designed to materially increase the rate of fire of a semiautomatic firearm; or</li><li>a firearm that is modified to materially increase the rate of fire.</li></ul><p>Second, the bill generally prohibits (1) the import, sale, manufacture, transfer, or receipt of a large capacity ammunition feeding device; or (2) the possession of a large capacity ammunition feeding device manufactured after the date of enactment.\u00a0</p><p>A violation is subject to criminal penalties\u2014a fine, a prison term of up to 12 months, or both, for each violation.\u00a0</p><p>In addition, an individual who possesses a prohibited gas-operated semiautomatic firearm during a\u00a0federal felony offense is subject to additional penalties\u2014a\u00a0fine, a mandatory minimum prison term of two years, or both.</p><p>Finally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender gas-operated semiautomatic firearms and large capacity ammunition feeding devices under a buy-back program.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr2790"
    },
    "title": "GOSAFE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gas-Operated Semi-Automatic Firearms Exclusion Act or the GOSAFE Act</strong></p><p>This bill establishes a framework to regulate gas-operated semiautomatic firearms and large capacity ammunition feeding devices under federal firearms laws.</p><p>First, the bill generally prohibits the import, sale, manufacture, transfer, receipt, or possession of</p><ul><li>a firearm that is or is modified to operate as a prohibited gas-operated semiautomatic firearm;</li><li>a combination of parts that modify or can be\u00a0assembled into\u00a0a prohibited gas-operated semiautomatic firearm, or that produce an unlawful gas-operated semiautomatic cycling action;</li><li>a device or combination of parts designed to materially increase the rate of fire of a semiautomatic firearm; or</li><li>a firearm that is modified to materially increase the rate of fire.</li></ul><p>Second, the bill generally prohibits (1) the import, sale, manufacture, transfer, or receipt of a large capacity ammunition feeding device; or (2) the possession of a large capacity ammunition feeding device manufactured after the date of enactment.\u00a0</p><p>A violation is subject to criminal penalties\u2014a fine, a prison term of up to 12 months, or both, for each violation.\u00a0</p><p>In addition, an individual who possesses a prohibited gas-operated semiautomatic firearm during a\u00a0federal felony offense is subject to additional penalties\u2014a\u00a0fine, a mandatory minimum prison term of two years, or both.</p><p>Finally, the bill allows a state or local government to use Edward Byrne Memorial Justice Assistance Grant Program funds to compensate individuals who surrender gas-operated semiautomatic firearms and large capacity ammunition feeding devices under a buy-back program.</p>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr2790"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2790ih.xml"
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
      "title": "GOSAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gas-Operated Semi-Automatic Firearms Exclusion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-24T03:53:17Z"
    },
    {
      "title": "GOSAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-24T03:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to restrict the possession of certain firearms, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-24T03:48:25Z"
    }
  ]
}
```
