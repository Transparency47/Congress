# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2203?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2203
- Title: Innovative FEED Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2203
- Origin chamber: House
- Introduced date: 2025-03-18
- Update date: 2026-05-20T08:08:07Z
- Update date including text: 2026-05-20T08:08:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-18: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-18: Introduced in House

## Actions

- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Introduced in House
- 2025-03-18 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-18",
    "latestAction": {
      "actionDate": "2025-03-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2203",
    "number": "2203",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Innovative FEED Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:07Z",
    "updateDateIncludingText": "2026-05-20T08:08:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-18",
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
      "actionDate": "2025-03-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-18",
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
          "date": "2025-03-18T16:08:10Z",
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IN"
    },
    {
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "ME"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IN"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "SD"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "TX"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark [R-IN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IN"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "OR"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M001222",
      "district": "7",
      "firstName": "Max",
      "fullName": "Rep. Miller, Max L. [R-OH-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "L.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "WA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "OH"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "IA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "MN"
    },
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CO"
    },
    {
      "bioguideId": "F000480",
      "district": "20",
      "firstName": "Vince",
      "fullName": "Rep. Fong, Vince [R-CA-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Fong",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "IN"
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
      "sponsorshipDate": "2025-04-07",
      "state": "ID"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "KS"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "WI"
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
      "sponsorshipDate": "2025-04-17",
      "state": "TX"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "IL"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-05-21",
      "state": "ME"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "WA"
    },
    {
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "KS"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-06-20",
      "state": "IA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "DE"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "MN"
    },
    {
      "bioguideId": "W000830",
      "district": "27",
      "firstName": "George",
      "fullName": "Rep. Whitesides, George [D-CA-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitesides",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "IL"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NC"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
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
      "sponsorshipDate": "2025-09-26",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NM"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "IL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NE"
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
      "sponsorshipDate": "2026-05-19",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2203ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2203\nIN THE HOUSE OF REPRESENTATIVES\nMarch 18, 2025 Mr. Langworthy (for himself, Ms. Schrier , Mr. Baird , Ms. Pingree , Mrs. Houchin , Mr. Costa , Mr. Moolenaar , Ms. Tenney , Mr. Riley of New York , Mr. Johnson of South Dakota , Mr. Pfluger , Mr. Latta , Mr. Joyce of Pennsylvania , Mr. Messmer , Mr. Bentz , Mr. Obernolte , Mr. Miller of Ohio , Mr. Nunn of Iowa , Mr. Feenstra , Mr. Newhouse , Mr. Balderson , Mrs. Miller-Meeks , Mr. Finstad , Mr. Valadao , Mr. Evans of Colorado , and Mr. Fong ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Federal Food, Drug, and Cosmetic Act with respect to the regulation of zootechnical animal food substances.\n#### 1. Short title\nThis Act may be cited as the Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025 .\n#### 2. Regulation of zootechnical animal food substances\n##### (a) Definition\nSection 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ) is amended by adding at the end the following:\n(tt) (1) The term zootechnical animal food substance means a substance that\u2014 (A) is added to the food or drinking water of animals; (B) is intended to\u2014 (i) affect the byproducts of the digestive process of an animal; (ii) reduce the presence of foodborne pathogens of human health significance in an animal intended to be used for food; or (iii) affect the structure or function of the body of the animal, other than by providing nutritive value, by altering the animal\u2019s gastrointestinal microbiome; and (C) achieves its intended effect by acting solely within the gastrointestinal tract of the animal. (2) Such term does not include a substance that\u2014 (A) is intended for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in an animal; (B) is a hormone; (C) is an active moiety in an animal drug, which, prior to the filing of a petition under section 409 was approved under section 512, conditionally approved under section 571, indexed under section 572, or for which substantial clinical investigations have been instituted and for which the existence of such investigations has been made public; (D) is an ionophore; or (E) is otherwise excluded from the definition based on criteria established by the Secretary through notice and comment rulemaking. (3) A zootechnical animal food substance shall be deemed to be a food additive within the meaning of paragraph (s) and its introduction into interstate commerce shall be in accordance with a regulation issued under section 409. A zootechnical animal food substance shall not be considered a drug under paragraph (g)(1)(C) solely because the substance has an intended effect described in subparagraph (1). .\n##### (b) Food additives\nSection 409 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 348 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (3) through (5) as paragraphs (4) through (6), respectively; and\n**(B)**\nby inserting after paragraph (2) the following:\n(3) In the case of a zootechnical animal food substance, such petition shall, in addition to any explanatory or supporting data, contain\u2014 (A) all relevant data bearing on the effect the zootechnical animal food substance is intended to have and the quantity of such substance required to produce the intended effect; and (B) full reports of investigations made with respect to the intended use of such substance, including full information as to the methods and controls used in conducting such investigations. ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nby amending subparagraph (A) of paragraph (1) to read as follows:\n(A) (i) by order establish a regulation (whether or not in accord with that proposed by the petitioner) prescribing\u2014 (I) with respect to one or more proposed uses of the food additive involved, the conditions under which such additive may be safely used (including specifications as to the particular food or classes of food in or on which such additive may be used, the maximum quantity which may be used or permitted to remain in or on such food, the manner in which such additive may be added to or used in or on such food, and any directions or other labeling or packaging requirements for such additive as the Secretary determines necessary to assure the safety of such use); and (II) in the case of a zootechnical animal food substance, the conditions under which such substance may be used to achieve the intended effect; and (ii) notify the petitioner of such order and the reasons for such action; or ; and\n**(B)**\nin paragraph (3)\u2014\n**(i)**\nin subparagraph (A), by striking ; or and inserting a semicolon;\n**(ii)**\nin subparagraph (B), by striking the period and inserting ; or ; and\n**(iii)**\nby adding at the end the following:\n(C) in the case of a zootechnical animal food substance, fails to establish that the proposed use of the substance, under the conditions of use to be specified in the regulation, will achieve the intended effect. ; and\n**(3)**\nby adding at the end the following:\n(l) Zootechnical animal food substances The labeling of a zootechnical animal food substance\u2014 (1) shall include the statement: Not for use in the diagnosis, cure, mitigation, treatment, or prevention of disease in animals. ; and (2) may include statements regarding the intended effect of the substance on the structure or function of the body of animals, as set forth in section 201(tt)(1). .\n##### (c) Misbranded food\nSection 403 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 343 ) is amended by adding at the end the following:\n(z) If it is a zootechnical animal food substance and the labeling of the food does not include the statement required by section 409(l)(1). .\n##### (d) Rule of construction\nNothing in this section, or the amendments made by this section, shall be construed to authorize the Secretary of Health and Human Services to require the use of any zootechnical food substance or food additive (as those terms are defined in section 201 of the Federal Food, Drug, and Cosmetic Act, as amended by subsection (a)).",
      "versionDate": "2025-03-18",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1906",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Innovative FEED Act of 2025",
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
        "updateDate": "2025-04-01T16:05:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-18",
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
          "measure-id": "id119hr2203",
          "measure-number": "2203",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-18",
          "originChamber": "HOUSE",
          "update-date": "2025-09-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2203v00",
            "update-date": "2025-09-03"
          },
          "action-date": "2025-03-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p><p>\u00a0</p>"
        },
        "title": "Innovative FEED Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2203.xml",
    "summary": {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2203"
    },
    "title": "Innovative FEED Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Innovative Feed Enhancement and Economic Development Act of 2025 or the Innovative FEED Act of 2025</strong></p><p>This bill provides for the regulation of zootechnical animal food substances as food additives.</p><p>The bill defines\u00a0<em>zootechnical animal food substance\u00a0</em>as a substance that is added to the food or drinking water of animals and that affects only the animal's gastrointestinal tract, with the intended purpose of affecting the byproducts of the animal's digestion, reducing foodborne pathogens, or altering the animal's gastrointestinal biome.</p><p>The definition does not include substances\u00a0that are used to\u00a0treat or prevent diseases in animals, hormones, or active ingredients of animal drugs. Labels for zootechnical animal food substances must include a disclaimer that the substance may not be used to treat or prevent diseases in animals.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-09-03",
      "versionCode": "id119hr2203"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2203ih.xml"
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
      "title": "Innovative FEED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovative FEED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Innovative Feed Enhancement and Economic Development Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Food, Drug, and Cosmetic Act with respect to the regulation of zootechnical animal food substances.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:18:34Z"
    }
  ]
}
```
