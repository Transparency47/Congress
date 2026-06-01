# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2784
- Title: Congressional Tribute to Constance Baker Motley Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2784
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2026-04-17T13:24:39Z
- Update date including text: 2026-04-17T13:24:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2784",
    "number": "2784",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
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
    "title": "Congressional Tribute to Constance Baker Motley Act of 2025",
    "type": "S",
    "updateDate": "2026-04-17T13:24:39Z",
    "updateDateIncludingText": "2026-04-17T13:24:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T18:28:12Z",
          "name": "Referred To"
        }
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
      "state": "ME"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NY"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CT"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-09-11",
      "state": "ME"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NH"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "CA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "PA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NJ"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "WI"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "RI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "HI"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MN"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NV"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "RI"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "DE"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "DE"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NM"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "OR"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "MD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "WA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "VT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "NM"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2784is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2784\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Blumenthal (for himself, Ms. Collins , Mr. Schumer , Mr. Murphy , Mrs. Gillibrand , Mr. King , Mrs. Shaheen , Mr. Padilla , Mr. Fetterman , Ms. Hirono , Mr. Durbin , Mr. Booker , Ms. Baldwin , Mr. Whitehouse , Mr. Merkley , Ms. Alsobrooks , Mr. Schatz , Ms. Klobuchar , Ms. Cortez Masto , Mr. Reed , Mr. Coons , Ms. Blunt Rochester , Mr. Luj\u00e1n , Mr. Wyden , Mr. Markey , Mr. Van Hollen , Mrs. Murray , Mr. Welch , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo award posthumously the Congressional Gold Medal to Constance Baker Motley, in recognition of her enduring contributions and service to the United States.\n#### 1. Short title\nThis Act may be cited as the Congressional Tribute to Constance Baker Motley Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nConstance Baker Motley was born in 1921, in New Haven, Connecticut, the daughter of immigrants from the Caribbean island of Nevis.\n**(2)**\nIn 1943, Constance Baker Motley graduated from New York University with a Bachelor of Arts degree in economics.\n**(3)**\nUpon receiving a law degree from Columbia University in 1946, Constance Baker Motley became a staff attorney at the National Association for the Advancement of Colored People Legal Defense and Educational Fund, Inc. (referred to in this Act as the LDF ), and fought tirelessly for 2 decades alongside Thurgood Marshall and other leading civil rights lawyers to dismantle segregation throughout the United States.\n**(4)**\nConstance Baker Motley was the only female attorney on the LDF legal team that won the landmark desegregation case, Brown v. Board of Education, 347 U.S. 483 (1954).\n**(5)**\nConstance Baker Motley argued 10 major civil rights cases before the Supreme Court of the United States, winning all but 1, including the case brought on behalf of James Meredith challenging the refusal of the University of Mississippi to admit him.\n**(6)**\nConstance Baker Motley\u2019s only loss before the Supreme Court of the United States in Swain v. Alabama, 380 U.S. 202 (1965), a case in which the Supreme Court refused to proscribe race-based peremptory challenges in cases involving African-American defendants, and which was later reversed in Batson v. Kentucky, 476 U.S. 79 (1986), on grounds that were largely asserted by Constance Baker Motley in the Swain case.\n**(7)**\nIn 1964, Constance Baker Motley became the first African-American woman elected to the New York State Senate.\n**(8)**\nIn 1965, Constance Baker Motley became the first African-American woman, and the first woman, to serve as president of the Borough of Manhattan.\n**(9)**\nConstance Baker Motley, in her capacity as an elected public official in New York, continued to fight for civil rights, dedicating herself to the revitalization of the inner city and improvement of urban public schools and housing.\n**(10)**\nIn 1966, Constance Baker Motley was appointed by President Lyndon B. Johnson as a judge on the United States District Court for the Southern District of New York.\n**(11)**\nThe appointment of Constance Baker Motley made her the first African-American woman, and only the fifth woman, appointed and confirmed for a Federal judgeship.\n**(12)**\nIn 1982, Constance Baker Motley was elevated to Chief Judge of the United States District Court for the Southern District of New York, the largest Federal trial court in the United States.\n**(13)**\nConstance Baker Motley assumed senior status in 1986, and continued serving on the United States District Court for the Southern District of New York with distinction for nearly 2 decades.\n**(14)**\nConstance Baker Motley passed away on September 28, 2005, and is survived by her son, Joel W. Motley III, 3 grandchildren, and nieces and nephews in Connecticut and in other States.\n**(15)**\nSeptember 14, 2021, was the 100th anniversary of the birth of Constance Baker Motley.\n#### 3. Congressional gold medal\n##### (a) Presentation authorized\nThe Speaker of the House of Representatives and the President pro tempore of the Senate shall make appropriate arrangements for the posthumous presentation, on behalf of Congress, of a gold medal of appropriate design in commemoration of Constance Baker Motley, in recognition of her enduring contributions and service to the United States.\n##### (b) Design and striking\nFor purposes of the presentation referred to in subsection (a), the Secretary of the Treasury (referred to in this Act as the Secretary ) shall strike a gold medal with suitable emblems, devices, and inscriptions, to be determined by the Secretary. The design shall bear an image of, and an inscription of the name of, Constance Baker Motley .\n##### (c) Presentation\nWith respect to the presentation referred to in subsection (a), the gold medal shall be presented to Constance Baker Motley\u2019s son, Joel Motley III, and her niece, Constance Royster.\n##### (d) Disposition of medal\nFollowing the presentation referred to in subsection (a), the gold medal shall be given to Joel Motley III.\n#### 4. Duplicate medals\nThe Secretary may strike and sell duplicates in bronze of the gold medal struck under section 3, at a price sufficient to cover the costs of the medals, including labor, materials, dies, use of machinery, and overhead expenses.\n#### 5. Status of medals\n##### (a) National medal\nMedals struck under this Act are national medals for purposes of chapter 51 of title 31, United States Code.\n##### (b) Numismatic items\nFor purposes of section 5134 of title 31, United States Code, all medals struck under this Act shall be considered to be numismatic items.\n#### 6. Authority to use fund amounts; proceeds of sale\n##### (a) Authority To use fund amounts\nThere is authorized to be charged against the United States Mint Public Enterprise Fund such amounts as may be necessary to pay for the costs of the medals struck under this Act.\n##### (b) Proceeds of sale\nAmounts received from the sale of duplicate bronze medals authorized under section 4 shall be deposited into the United States Mint Public Enterprise Fund.",
      "versionDate": "2025-09-11",
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
        "actionDate": "2025-09-11",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "5309",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Congressional Tribute to Constance Baker Motley Act of 2025",
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
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-11-19T12:08:36Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2784is.xml"
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
      "title": "Congressional Tribute to Constance Baker Motley Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Congressional Tribute to Constance Baker Motley Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to award posthumously the Congressional Gold Medal to Constance Baker Motley, in recognition of her enduring contributions and service to the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:24Z"
    }
  ]
}
```
