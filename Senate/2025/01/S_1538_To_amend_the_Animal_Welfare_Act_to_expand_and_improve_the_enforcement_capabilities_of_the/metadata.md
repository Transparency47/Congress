# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1538?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1538
- Title: Better CARE for Animals Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1538
- Origin chamber: Senate
- Introduced date: 2025-04-30
- Update date: 2025-12-19T12:03:16Z
- Update date including text: 2025-12-19T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-30: Introduced in Senate
- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-30: Introduced in Senate

## Actions

- 2025-04-30 - IntroReferral: Introduced in Senate
- 2025-04-30 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-30",
    "latestAction": {
      "actionDate": "2025-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1538",
    "number": "1538",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Animals"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Better CARE for Animals Act of 2025",
    "type": "S",
    "updateDate": "2025-12-19T12:03:16Z",
    "updateDateIncludingText": "2025-12-19T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-30",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-04-30T19:51:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-04-30",
      "state": "LA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-23",
      "state": "VT"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "NV"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "NV"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "MD"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "IL"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "OR"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "ME"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-14",
      "state": "NM"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-10-20",
      "state": "VT"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-20",
      "state": "DE"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-20",
      "state": "CT"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "CO"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-10-22",
      "state": "NH"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "AZ"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "MD"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "GA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-10-29",
      "state": "HI"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-11-03",
      "state": "WA"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "CO"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "WA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-11-05",
      "state": "NJ"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "VA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "IL"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "HI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "RI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "MN"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "PA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "AZ"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MN"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "VA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1538is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1538\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2025 Mr. Blumenthal (for himself and Mr. Kennedy ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Animal Welfare Act to expand and improve the enforcement capabilities of the Attorney General, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Better Collaboration, Accountability, and Regulatory Enforcement for Animals Act of 2025 or the Better CARE for Animals Act of 2025 .\n#### 2. Strengthening animal welfare enforcement\n##### (a) Definitions\nSection 2 of the Animal Welfare Act (7 U.S.C. 2132) is amended\u2014\n**(1)**\nin subsection (b), by striking of the United States or his representative who shall be an employee of the United States and inserting or a representative of the Secretary of Agriculture, who shall be an employee of the ;\n**(2)**\nin subsection (c)(1), by adding or at the end after the semicolon; and\n**(3)**\nin each of subsections (a) through (o)\u2014\n**(A)**\nby inserting a subsection heading, the text of which comprises the term defined in the subsection;\n**(B)**\nby reordering the subsections so as to appear in alphabetical order based on the subsection headings (as so added); and\n**(C)**\nby redesignating the subsections (as so reordered) appropriately.\n##### (b) Sale or transportation without license\nSection 4 of the Animal Welfare Act (7 U.S.C. 2134) is amended to read as follows:\n4. Sale or transportation without license No dealer or exhibitor shall do any of the following in commerce: exhibit, purchase, offer to purchase, sell, offer to sell, transport, or offer for transportation any animal, unless the dealer or exhibitor has a valid license from the Secretary that has not been suspended. .\n##### (c) Investigations and inspections\nSection 16(c) of the Animal Welfare Act (7 U.S.C. 2146(c)) is amended in the fourth sentence by striking enforce, and to prevent and restrain violations of this Act, and inserting enforce, prevent, and restrain violations of this Act, or any rule, standard, or regulation promulgated pursuant to this Act, .\n##### (d) Civil penalty\nSection 19 of the Animal Welfare Act (7 U.S.C. 2149) is amended\u2014\n**(1)**\nin subsection (d), in the first sentence, by inserting , or any rule, standard, or regulation promulgated thereunder, before shall ; and\n**(2)**\nby adding at the end the following:\n(e) Rewards and certain incidental expenses With respect to the sums received by the Secretary or the Attorney General as penalties or fines for any violation of this Act or any rule, standard, or regulation promulgated thereunder, the Secretary or the Attorney General, as applicable, shall use those sums to pay the reasonable and necessary costs incurred by any person in providing temporary care for any animal pending the disposition of any civil or criminal proceeding alleging a violation of this Act with respect to that animal. .\n##### (e) Enforcement by Attorney General\nThe Animal Welfare Act is amended by inserting after section 19 (7 U.S.C. 2149) the following:\n20. Enforcement by Attorney General (a) In general The Attorney General may bring a civil action in the appropriate district court of the United States for appropriate relief, including a temporary restraining order, preliminary or permanent injunction (including for removal or relocation of animals), license revocation, and civil penalties of up to $10,000 for each violation for each day during which the violation continues, against any person who violates any provision of this Act or any rule, standard, or regulation promulgated thereunder. (b) Seizure and forfeiture of animals (1) In general Any animal that is subjected to conduct that constitutes a violation of this Act, or any rule, standard, or regulation promulgated thereunder, shall be subject to seizure and forfeiture to the United States in accordance with chapter 46 of title 18, United States Code. (2) Costs Any person whose act or omission is the basis for a seizure authorized by subparagraph (1) may be charged a reasonable fee for expenses to the United States relating to the transfer and care of the seized animal. (c) Warrants The judges of the district courts of the United States and United States magistrate judges may, within their respective jurisdictions, on proper oath or affirmation showing probable cause, issue such warrants or other processes as may be required for enforcement of this Act and any rule, standard, or regulation promulgated thereunder. (d) Savings clause (1) Attorney general No action taken by the Attorney General pursuant to this section shall affect or limit the authority of the Secretary to enforce any provision of this Act or any rule, standard, or regulation thereunder. (2) Secretary No action taken by the Secretary shall affect or limit the authority of the Attorney General under this Act. .\n##### (f) Authority To apply for injunctions\nSection 29(b) of the Animal Welfare Act (7 U.S.C. 2159(b)) is amended by striking the second sentence.\n##### (g) Severability\nThe Animal Welfare Act (7 U.S.C. 2131 et seq.) is amended by adding at the end the following:\n30. Severability If any provision of this Act, or the application thereof, is held invalid, the validity of the remainder of this Act and the application of such provision to other persons and circumstances shall not be affected. .\n##### (h) Memorandum of understanding\nNot later than 180 days after the date of enactment of this Act, the Secretary of Agriculture shall enter into a memorandum of understanding with the Attorney General to carry out the authorities granted by the amendments made by this section, including an agreement to provide the Attorney General with timely information about violators who have multiple citations that seriously or adversely affect the health or well-being of an animal.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nsection 16(c) of the Animal Welfare Act (7 U.S.C. 2146(c)) establishes the jurisdiction of Federal courts to address violations of, and cases arising from violations of, that Act and provides the Attorney General with the authority to bring such cases in Federal court; and\n**(2)**\nthe enforcement jurisdiction of the Federal courts, and the corresponding enforcement authority of the Attorney General, include violations of the rules, standards, and regulations promulgated under that Act.",
      "versionDate": "",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-30",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3112",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Better CARE for Animals Act of 2025",
      "type": "HR"
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
        "name": "Animals",
        "updateDate": "2025-05-21T13:41:55Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1538is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Better CARE for Animals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Better CARE for Animals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Better Collaboration, Accountability, and Regulatory Enforcement for Animals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Animal Welfare Act to expand and improve the enforcement capabilities of the Attorney General, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:40Z"
    }
  ]
}
```
