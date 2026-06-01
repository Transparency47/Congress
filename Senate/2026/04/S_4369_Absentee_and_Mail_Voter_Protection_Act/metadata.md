# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4369
- Title: Absentee and Mail Voter Protection Act
- Congress: 119
- Bill type: S
- Bill number: 4369
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-04T22:13:04Z
- Update date including text: 2026-05-04T22:13:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2026-04-22: Introduced in Senate

## Actions

- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4369",
    "number": "4369",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Absentee and Mail Voter Protection Act",
    "type": "S",
    "updateDate": "2026-05-04T22:13:04Z",
    "updateDateIncludingText": "2026-05-04T22:13:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T16:02:26Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "IL"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MD"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "WI"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CO"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CT"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "DE"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NJ"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "WA"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "DE"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NV"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "IL"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "AZ"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NY"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NM"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CO"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "HI"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "AZ"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NJ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-22",
      "state": "ME"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MN"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NM"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CT"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "WA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NV"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-04-22",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "NH"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "OR"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MI"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4369is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4369\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Padilla (for himself, Mr. Peters , Mr. Durbin , Mr. Schumer , Mr. Merkley , Ms. Alsobrooks , Ms. Baldwin , Mr. Bennet , Mr. Blumenthal , Ms. Blunt Rochester , Mr. Booker , Ms. Cantwell , Mr. Coons , Ms. Cortez Masto , Ms. Duckworth , Mr. Gallego , Mrs. Gillibrand , Mr. Heinrich , Mr. Hickenlooper , Ms. Hirono , Mr. Kaine , Mr. Kelly , Mr. Kim , Mr. King , Ms. Klobuchar , Mr. Luj\u00e1n , Mr. Markey , Mr. Murphy , Mrs. Murray , Ms. Rosen , Mr. Sanders , Mr. Schiff , Mrs. Shaheen , Mr. Van Hollen , Mr. Warner , Ms. Warren , Mr. Welch , Mr. Whitehouse , Mr. Wyden , Ms. Slotkin , and Mr. Reed ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo repeal an executive order relating to Federal elections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Absentee and Mail Voter Protection Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nArticle 1, section 4 of the Constitution of the United States clearly demonstrates that the power to make or alter any regulations regarding the time, place, and manner of elections lies with Congress and the States, not with the President.\n**(2)**\nOn May 20, 1993, President William J. Clinton signed the National Voter Registration Act of 1993 ( Public Law 103\u201331 ), which was passed with bipartisan support.\n**(3)**\nOn October 29, 2002, President George W. Bush signed the Help America Vote Act of 2002 ( Public Law 107\u2013252 ), which was passed on an overwhelmingly bipartisan basis.\n**(4)**\nThe Help America Vote Act of 2002 established the Election Assistance Commission, an independent and evenly divided bipartisan agency to assist States with new standards and improve election administration.\n**(5)**\nNeither the National Voter Registration Act of 1993 nor the Help America Vote Act of 2002 provide any authority for any of the actions directed by Executive Order 14399 (91 Fed. Reg. 17125) to create State citizenship lists for Federal election purposes based on unreliable Federal databases or to bar the Postal Service from delivering mail ballots unless States use lists provided to them or approved by the Federal Government.\n**(6)**\nPennsylvania and New Jersey enacted some of the earliest laws to allow voting away from home in 1813 and 1815 in the context of the War of 1812 and many States granted absentee voting for military service members in 1864 during the Civil War. In the early 20th century, States such as Virginia, Indiana, and Wisconsin enacted absentee voting for several reasons. In 1924, President Calvin Coolidge and First Lady Grace Coolidge voted by mail according to Massachusetts absentee voting procedures from Washington, DC.\n**(7)**\nAll 50 States, the District of Columbia, and territories allow absentee voting. As of March 22, 2026\u2014\n**(A)**\n28 States (Alaska, Arizona, Florida, Georgia, Idaho, Illinois, Iowa, Kansas, Maine, Maryland, Massachusetts, Michigan, Minnesota, Montana, Nebraska, New Jersey, New Mexico, New York, North Carolina, North Dakota, Ohio, Oklahoma, Pennsylvania, Rhode Island, South Dakota, Virginia, Wisconsin, and Wyoming) offer no-excuse absentee voting; and\n**(B)**\n8 States (California, Colorado, Hawaii, Nevada, Oregon, Utah, Vermont, and Washington) and the District of Columbia provide universal vote-by-mail.\n**(8)**\nMore than 28,000,000 Americans voted by mail or absentee ballot in 2016, over 66,000,000 in 2020 during the COVID\u201319 pandemic, and over 48,000,000 Americans voted by mail in the 2024 general election. President Donald Trump has voted by mail on at least three occasions by his own admission, including in New York in 2018, Florida in 2020, and again in Florida in 2026.\n**(9)**\nVote by mail has been used successfully and securely by members of the United States military for many decades and throughout major conflicts. Hundreds of thousands of members of the United States military and United States citizens living abroad relied on mail-in ballots to cast their vote in 2024 and the Uniformed and Overseas Citizens Absentee Voting Act ( 52 U.S.C. 20301 et seq. ) requires all 50 States, the District of Columbia, and the territories of American Samoa, Guam, Puerto Rico, and the Virgin Islands to permit covered voters to register to vote absentee, and requires the Federal Government to expedite transmission of completed ballots.\n**(10)**\nThe United States Postal Service is an independent establishment governed by a bipartisan Board of Governors which has the power to appoint the Postmaster General and exercise postal power, and cannot regulate or refuse to carry State-issued mail ballot envelopes at the direction of the President.\n**(11)**\nThe Postal Service delivered nearly 100,000,000 ballots for the November 2024 general election and took extraordinary measures to ensure timely delivery of election mail in 2024 and will need to take action in the 2026 election cycle to again ensure timely delivery of election mail, including State-issued mail ballot envelopes.\n**(12)**\nExecutive Order 14399 (91 Fed. Reg. 17125), issued by President Donald J. Trump on March 31, 2026, entitled Ensuring Citizenship Verification and Integrity in Federal Elections , greatly exceeds the authority of the Executive branch, is illegal and unconstitutional, and would disenfranchise tens of millions of American voters.\n#### 3. Repeal of Executive Order\n##### (a) In general\nExecutive Order 14399 (91 Fed. Reg. 17125) shall have no force or effect.\n##### (b) Prohibition on use of funds for similar orders\n**(1) In general**\nNo Federal funds may be used to implement, administer, enforce, or carry out Executive Order 14399 (91 Fed. Reg. 17125) or any similar order.\n**(2) Postal service**\nThe United States Postal Service may not use any funds, including funds available under section 2003 or 2011 of title 39, United States Code, to implement, administer, enforce, or carry out such Executive order or any similar order.\n#### 4. Prohibition on use of funds with respect to certain other activities\n##### (a) National voter registration database\nNotwithstanding any other provision of law, no Federal funds may be used by the Department of Homeland Security, the Social Security Administration, the Department of Justice, or any other agency\u2014\n**(1)**\nto create a national voter registration database or a national citizenship database for Federal election purposes;\n**(2)**\nto use existing databases or systems to compile citizenship lists for Federal election purposes; or\n**(3)**\nto provide for the national collection of State voter registration lists or citizenship lists for Federal election purposes.\n##### (b) Mail-In and absentee ballots\nNotwithstanding any other provision of law\u2014\n**(1)**\nno Federal funds may be used by the Department of Commerce or any other agency\u2014\n**(A)**\nfor any purpose relating to the regulation of mail-in and absentee ballots in Federal elections; or\n**(B)**\nto determine the eligibility of a voter to cast a ballot through the mail in Federal elections; and\n**(2)**\nthe United States Postal Service may not use any funds, including funds available under section 2003 or 2011 of title 39, United States Code\u2014\n**(A)**\nto regulate the mailability of mail-in and absentee ballots in Federal elections; or\n**(B)**\nto determine the eligibility of a voter to cast a ballot through the mail in Federal elections.\n##### (c) Compelling production of State voter registration lists\nNotwithstanding any other provision of law, no Federal funds may be used by the Department of Justice to bring or continue a civil action against any State to compel the production of statewide voter registration lists under section 303 of the Civil Rights Act of 1960 ( 52 U.S.C. 20703 ), section 303 of the Help America Vote Act of 2002 ( 52 U.S.C. 21083 ), or any other Federal law.\n##### (d) Sharing of voter registration lists\n**(1) In general**\nNothing in section 8 of the National Voter Registration Act of 1993 ( 52 U.S.C. 20507 ), section 401 of the Help America Vote Act of 2002 ( 52 U.S.C. 21111 ), or any other provision of law shall be construed to grant any authority to share statewide voter registration lists between any two Federal agencies, or to conduct data matching activities with any such registration lists using any system of records.\n**(2) Prohibition of funds**\n**(A) In general**\nNo Federal funds may be used by any agency for any activity described in paragraph (1).\n**(B) Postal service**\nThe United States Postal Service may not use any funds, including funds available under section 2003 or 2011 of title 39, United States Code, to carry out any activity described in paragraph (1).\n##### (e) Definitions\nFor purposes of this section, the terms agency and system of records have the meaning given those terms under section 552a of title 5, United States Code (commonly known as the Privacy Act of 1974 ).",
      "versionDate": "2026-04-22",
      "versionType": "Introduced in Senate"
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-05-04T22:13:04Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4369is.xml"
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
      "title": "Absentee and Mail Voter Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Absentee and Mail Voter Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal an executive order relating to Federal elections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:35Z"
    }
  ]
}
```
