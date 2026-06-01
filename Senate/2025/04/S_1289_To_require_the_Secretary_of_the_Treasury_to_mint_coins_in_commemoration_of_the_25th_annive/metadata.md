# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1289?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1289
- Title: 25th Anniversary of 9/11 Commemorative Coin Act
- Congress: 119
- Bill type: S
- Bill number: 1289
- Origin chamber: Senate
- Introduced date: 2025-04-03
- Update date: 2026-05-13T11:03:31Z
- Update date including text: 2026-05-13T11:03:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in Senate
- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-03: Introduced in Senate

## Actions

- 2025-04-03 - IntroReferral: Introduced in Senate
- 2025-04-03 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1289",
    "number": "1289",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000555",
        "district": "",
        "firstName": "Kirsten",
        "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
        "lastName": "Gillibrand",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "25th Anniversary of 9/11 Commemorative Coin Act",
    "type": "S",
    "updateDate": "2026-05-13T11:03:31Z",
    "updateDateIncludingText": "2026-05-13T11:03:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-03",
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
        "item": [
          {
            "date": "2025-04-03T18:24:46Z",
            "name": "Referred To"
          },
          {
            "date": "2025-04-03T18:24:46Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "WV"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "NY"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "NC"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "NJ"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TN"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-05-07",
      "state": "TX"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-06-03",
      "state": "ME"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "RI"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CT"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "VA"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "ME"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "SD"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-09-02",
      "state": "OK"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "MI"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "NH"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MT"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NM"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NE"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "AR"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1289is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1289\nIN THE SENATE OF THE UNITED STATES\nApril 3, 2025 Mrs. Gillibrand (for herself, Mrs. Capito , and Mr. Schumer ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of the Treasury to mint coins in commemoration of the 25th anniversary of the September 11, 2001, terrorist attacks on the United States and to support programs at the National September 11 Memorial and Museum at the World Trade Center.\n#### 1. Short title\nThis Act may be cited as the 25th Anniversary of 9/11 Commemorative Coin Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOn September 11, 2001, the United States suffered the deadliest terrorist attacks on United States soil (referred to in this section as the attacks ).\n**(2)**\n2,977 people were killed during the attacks, marking the single worst foreign attack on United States soil since Pearl Harbor in 1941.\n**(3)**\nIn New York City, 2 planes hit the Twin Towers during the attacks, causing both 110-story towers to collapse in less than 2 hours, as well as destroying 5 other buildings in the World Trade Center complex, leaving a death toll of 2,753 people, including all passengers and crew members of American Airlines Flight 11 and all passengers and crew members of United Airlines Flight 175.\n**(4)**\nDuring the attacks, American Airlines Flight 77 struck the side of the Pentagon, killing 184 passengers, crew members, and personnel.\n**(5)**\nIn Pennsylvania, during the attacks, United Airlines Flight 93 crashed near Shanksville, killing all 40 passengers and crew members.\n**(6)**\nThe attacks took the lives of 441 first responders in New York, specifically 343 firefighters from the New York City Fire Department, 37 officers from the Port Authority Police Department, 23 officers from the New York City Police Department, and 38 individuals from other agencies.\n**(7)**\nThe collapse of the towers following the attacks created massive dust clouds that left hundreds of densely populated city blocks covered with harmful contaminants, exposing first responders, local workers, residents, and students.\n**(8)**\nMore than 2 decades after these horrific terrorist attacks took place, the ongoing physical and mental health impacts continue to deeply affect tens of thousands of individuals across the country who were in lower Manhattan and the surrounding area following the attacks, as well as those from around the country who participated in the rescue, recovery, and relief efforts, due to their exposure to the dust, smoke, and debris. Thousands of others have died due to illnesses and injuries relating to the attacks.\n**(9)**\nThe National September 11 Memorial and Museum at the World Trade Center is continuously dedicated to remembering, reflecting, and educating for many generations to come so that the story of September 11, 2001, is never forgotten.\n**(10)**\nThe National September 11 Memorial and Museum at the World Trade Center is committed to supporting family members, survivors, rescue and recovery workers, and military personnel who were affected by the attacks by providing services, education, and programming.\n#### 3. Coin specifications\n##### (a) Denominations\nThe Secretary of the Treasury (referred to in this Act as the Secretary ) shall mint and issue the following coins in commemoration of the 25th anniversary of the September 11, 2001, terrorist attacks on the United States and the establishment of the National September 11 Memorial and Museum at the World Trade Center:\n**(1) $5 gold coins**\nNot more than 50,000 $5 coins, each of which shall\u2014\n**(A)**\nweigh 8.359 grams;\n**(B)**\nhave a diameter of 0.850 inches; and\n**(C)**\ncontain not less than 90 percent gold.\n**(2) $1 silver coins**\nNot more than 400,000 $1 coins, each of which shall\u2014\n**(A)**\nweigh 26.73 grams;\n**(B)**\nhave a diameter of 1.500 inches; and\n**(C)**\ncontain not less than 90 percent silver.\n##### (b) Legal tender\nThe coins minted under this Act shall be legal tender, as provided in section 5103 of title 31, United States Code.\n##### (c) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all coins minted under this Act shall be considered to be numismatic items.\n#### 4. Design of coins\n##### (a) Design requirements\n**(1) In general**\nThe designs of the coins minted under this Act shall be emblematic of the courage, sacrifice, and strength of those individuals who perished in the terrorist attacks of September 11, 2001, the bravery of those who risked their lives to save others that day, and the endurance, resilience, and hope of those who survived. At least 1 such coin shall bear the inscription Never Forget .\n**(2) Designs and inscriptions**\nOn each coin minted under this Act, there shall be\u2014\n**(A)**\na designation of the value of the coin;\n**(B)**\ninscriptions of the words Liberty , In God We Trust , United States of America , and E Pluribus Unum ; and\n**(C)**\nan inscription of the words 25th Anniversary .\n##### (b) Selection\nThe designs for the coins minted under this Act shall be\u2014\n**(1)**\nselected by the Secretary, after consultation with\u2014\n**(A)**\nthe National September 11 Memorial and Museum at the World Trade Center; and\n**(B)**\nthe Commission of Fine Arts; and\n**(2)**\nreviewed by the Citizens Coinage Advisory Committee.\n#### 5. Issuance of coins\n##### (a) Quality of coins\nThe coins minted under this Act shall be issued in uncirculated and proof qualities.\n##### (b) Sense of congress\nIt is the sense of Congress that the coins minted under this Act should be struck at the United States Mint at West Point, New York, to the greatest extent possible.\n##### (c) Period for issuance\nThe Secretary may issue coins minted under this Act only during the 1-year period beginning on January 1, 2027.\n#### 6. Sale of coins\n##### (a) Sale price\nThe coins issued under this Act shall be sold by the Secretary at the price equal to the sum of\u2014\n**(1)**\nthe face value of the coins;\n**(2)**\nthe surcharge provided in section 7(a) with respect to the coins; and\n**(3)**\nthe cost of designing and issuing the coins (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping).\n##### (b) Bulk sales\nThe Secretary shall make bulk sales of the coins issued under this Act at a reasonable discount.\n##### (c) Prepaid orders\n**(1) In general**\nThe Secretary shall accept prepaid orders for the coins minted under this Act before the issuance of the coins.\n**(2) Discount**\nSale prices with respect to prepaid orders under paragraph (1) shall be at a reasonable discount.\n#### 7. Surcharges\n##### (a) In general\nAll sales of coins issued under this Act shall include a surcharge of\u2014\n**(1)**\n$35 per coin for the $5 gold coin; and\n**(2)**\n$10 per coin for the $1 silver coin.\n##### (b) Distribution\nSubject to section 5134(f)(1) of title 31, United States Code, all surcharges received by the Secretary from the sale of coins issued under this Act shall be promptly paid by the Secretary to the National September 11 Memorial and Museum at the World Trade Center to support the operations and maintenance of the National September 11 Memorial and Museum at the World Trade Center.\n##### (c) Audits\nThe National September 11 Memorial and Museum at the World Trade Center shall be subject to the audit requirements of section 5134(f)(2) of title 31, United States Code, with regard to the amounts received under subsection (b).\n##### (d) Limitation\n**(1) In general**\nNotwithstanding subsection (a), no surcharge may be included with respect to the issuance under this Act of any coin during a calendar year if, as of the time of that issuance, the issuance of that coin would result in the number of commemorative coin programs issued during that year to exceed the annual 2 commemorative coin program issuance limitation under section 5112(m)(1) of title 31, United States Code.\n**(2) Guidance**\nThe Secretary may issue guidance to carry out this subsection.\n#### 8. Financial assurances\nThe Secretary shall take such actions as may be necessary to ensure that\u2014\n**(1)**\nminting and issuing coins under this Act result in no net cost to the Federal Government; and\n**(2)**\nno funds, including applicable surcharges, are disbursed to any recipient designated in section 7(b) until the total cost of designing and issuing all of the coins authorized by this Act, including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping, is recovered by the United States Treasury, consistent with sections 5112(m) and 5134(f) of title 31, United States Code.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "1993",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "25th Anniversary of 9/11 Commemorative Coin Act",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-05T12:21:16Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1289is.xml"
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
      "title": "25th Anniversary of 9/11 Commemorative Coin Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:31Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "25th Anniversary of 9/11 Commemorative Coin Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T03:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Treasury to mint coins in commemoration of the 25th anniversary of the September 11, 2001, terrorist attacks on the United States and to support programs at the National September 11 Memorial and Museum at the World Trade Center.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T03:03:24Z"
    }
  ]
}
```
