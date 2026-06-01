# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/199
- Title: A bill to amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.
- Congress: 119
- Bill type: S
- Bill number: 199
- Origin chamber: Senate
- Introduced date: 2025-01-23
- Update date: 2026-04-14T10:56:32Z
- Update date including text: 2026-04-14T10:56:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-23: Introduced in Senate
- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-23: Introduced in Senate

## Actions

- 2025-01-23 - IntroReferral: Introduced in Senate
- 2025-01-23 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/199",
    "number": "199",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C000880",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Crapo, Mike [R-ID]",
        "lastName": "Crapo",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.",
    "type": "S",
    "updateDate": "2026-04-14T10:56:32Z",
    "updateDateIncludingText": "2026-04-14T10:56:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-23",
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
            "date": "2025-01-23T15:36:15Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-23T15:36:15Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "ID"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "OR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "NH"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TN"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "DE"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "TX"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "MT"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "IA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "OR"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NE"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "NC"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "MD"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "VA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-03",
      "state": "AZ"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacklyn",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NV"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NC"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "HI"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "OK"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "MI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "GA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "CO"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "UT"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MS"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "MT"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "LA"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "AK"
    },
    {
      "bioguideId": "K000393",
      "firstName": "John",
      "fullName": "Sen. Kennedy, John [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "LA"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-03-13",
      "state": "KS"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-13",
      "state": "NV"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "WA"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NH"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "AZ"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CO"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "CT"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MI"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "MD"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-07-15",
      "state": "IN"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-30",
      "state": "IN"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-02",
      "state": "DE"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "WY"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "ND"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "SC"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "IL"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s199is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 199\nIN THE SENATE OF THE UNITED STATES\nJanuary 23, 2025 Mr. Crapo (for himself, Mr. Risch , Mr. Wyden , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.\nI\nUnited States-Taiwan expedited double-tax relief act\n#### 101. Short title\nThis title may be cited as the United States-Taiwan Expedited Double-Tax Relief Act .\n#### 102. Special rules for taxation of certain residents of Taiwan\n##### (a) In general\nSubpart D of part II of subchapter N of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 894 the following new section:\n894A. Special rules for qualified residents of Taiwan (a) Certain income from united states sources (1) Interest, dividends, and royalties, etc (A) In general In the case of interest (other than original issue discount), dividends, royalties, amounts described in section 871(a)(1)(C), and gains described in section 871(a)(1)(D) received by or paid to a qualified resident of Taiwan\u2014 (i) sections 871(a), 881(a), 1441(a), 1441(c)(5), and 1442(a) shall each be applied by substituting the applicable percentage (as defined in section 894A(a)(1)(C)) for 30 percent each place it appears, and (ii) sections 871(a), 881(a), and 1441(c)(1) shall each be applied by substituting a United States permanent establishment of a qualified resident of Taiwan for a trade or business within the United States each place it appears. (B) Exceptions (i) In general Subparagraph (A) shall not apply to\u2014 (I) any dividend received from or paid by a real estate investment trust which is not a qualified REIT dividend, (II) any amount subject to section 897, (III) any amount received from or paid by an expatriated entity (as defined in section 7874(a)(2)) to a foreign related person (as defined in section 7874(d)(3)), and (IV) any amount which is included in income under section 860C to the extent that such amount does not exceed an excess inclusion with respect to a REMIC. (ii) Qualified reit dividend For purposes of clause (i)(I), the term qualified REIT dividend means any dividend received from or paid by a real estate investment trust if such dividend is paid with respect to a class of shares that is publicly traded and the recipient of the dividend is a person who holds an interest in any class of shares of the real estate investment trust of not more than 5 percent. (C) Applicable percentage For purposes of applying subparagraph (A)(i)\u2014 (i) In general Except as provided in clause (ii), the term applicable percentage means 10 percent. (ii) Special rules for dividends In the case of any dividend in respect of stock received by or paid to a qualified resident of Taiwan, the applicable percentage shall be 15 percent (10 percent in the case of a dividend which meets the requirements of subparagraph (D) and is received by or paid to an entity taxed as a corporation in Taiwan). (D) Requirements for lower dividend rate (i) In general The requirements of this subparagraph are met with respect to any dividend in respect of stock in a corporation if, at all times during the 12-month period ending on the date such stock becomes ex-dividend with respect to such dividend\u2014 (I) the dividend is derived by a qualified resident of Taiwan, and (II) such qualified resident of Taiwan has held directly at least 10 percent (by vote and value) of the total outstanding shares of stock in such corporation. For purposes of subclause (II), a person shall be treated as directly holding a share of stock during any period described in the preceding sentence if the share was held by a corporation from which such person later acquired that share and such corporation was, at the time the share was acquired, both a connected person to such person and a qualified resident of Taiwan. (ii) Exception for rics and reits Notwithstanding clause (i), the requirements of this subparagraph shall not be treated as met with respect to any dividend paid by a regulated investment company or a real estate investment trust. (2) Qualified wages (A) In general No tax shall be imposed under this chapter (and no amount shall be withheld under section 1441(a) or chapter 24) with respect to qualified wages paid to a qualified resident of Taiwan who\u2014 (i) is not a resident of the United States (determined without regard to subsection (c)(3)(E)), or (ii) is employed as a member of the regular component of a ship or aircraft operated in international traffic. (B) Qualified wages (i) In general The term qualified wages means wages, salaries, or similar remunerations with respect to employment involving the performance of personal services within the United States which\u2014 (I) are paid by (or on behalf of) any employer other than a United States person, and (II) are not borne by a United States permanent establishment of any person other than a United States person. (ii) Exceptions Such term shall not include directors' fees, income derived as an entertainer or athlete, income derived as a student or trainee, pensions, amounts paid with respect to employment with the United States, any State (or political subdivision thereof), or any possession of the United States (or any political subdivision thereof), or other amounts specified in regulations or guidance under subsection (f)(1)(F). (3) Income derived from entertainment or athletic activities (A) In general No tax shall be imposed under this chapter (and no amount shall be withheld under section 1441(a) or chapter 24) with respect to income derived by an entertainer or athlete who is a qualified resident of Taiwan from personal activities as such performed in the United States if the aggregate amount of gross receipts from such activities for the taxable year do not exceed $30,000. (B) Exception Subparagraph (A) shall not apply with respect to\u2014 (i) income which is qualified wages (as defined in paragraph (2)(B), determined without regard to clause (ii) thereof), or (ii) income which is effectively connected with a United States permanent establishment. (b) Income connected with a united states permanent establishment of a qualified resident of taiwan (1) In general (A) In general In lieu of applying sections 871(b) and 882, a qualified resident of Taiwan that carries on a trade or business within the United States through a United States permanent establishment shall be taxable as provided in section 1, 11, 55, or 59A, on its taxable income which is effectively connected with such permanent establishment. (B) Determination of taxable income In determining taxable income for purposes of paragraph (1), gross income includes only gross income which is effectively connected with the permanent establishment. (2) Treatment of dispositions of united states real property In the case of a qualified resident of Taiwan, section 897(a) shall be applied\u2014 (A) by substituting carried on a trade or business within the United States through a United States permanent establishment for were engaged in a trade or business within the United States , and (B) by substituting such United States permanent establishment for such trade or business . (3) Treatment of branch profits taxes In the case of any corporation which is a qualified resident of Taiwan, section 884 shall be applied\u2014 (A) by substituting 10 percent for 30 percent in subsection (a) thereof, and (B) by substituting a United States permanent establishment of a qualified resident of Taiwan for the conduct of a trade or business within the United States in subsection (d)(1) thereof. (4) Special rule with respect to income derived from certain entertainment or athletic activities (A) In general Paragraph (1) shall not apply to the extent that the income is derived\u2014 (i) in respect of entertainment or athletic activities performed in the United States, and (ii) by a qualified resident of Taiwan who is not the entertainer or athlete performing such activities. (B) Exception Subparagraph (A) shall not apply if the person described in subparagraph (A)(ii) is contractually authorized to designate the individual who is to perform such activities. (5) Special rule with respect to certain amounts Paragraph (1) shall not apply to any income which is wages, salaries, or similar remuneration with respect to employment or with respect to any amount which is described in subsection (a)(2)(B)(ii). (c) Qualified resident of taiwan For purposes of this section\u2014 (1) In general The term qualified resident of Taiwan means any person who\u2014 (A) is liable to tax under the laws of Taiwan by reason of such person's domicile, residence, place of management, place of incorporation, or any similar criterion, (B) is not a United States person (determined without regard to paragraph (3)(E)), and (C) in the case of an entity taxed as a corporation in Taiwan, meets the requirements of paragraph (2). (2) Limitation on benefits for corporate entities of taiwan (A) In general Subject to subparagraphs (E) and (F), an entity meets the requirements of this paragraph only if it\u2014 (i) meets the ownership and income requirements of subparagraph (B), (ii) meets the publicly traded requirements of subparagraph (C), or (iii) meets the qualified subsidiary requirements of subparagraph (D). (B) Ownership and income requirements The requirements of this subparagraph are met for an entity if\u2014 (i) at least 50 percent (by vote and value) of the total outstanding shares of stock in such entity are owned directly or indirectly by qualified residents of Taiwan, and (ii) less than 50 percent of such entity\u2019s gross income (and in the case of an entity that is a member of a tested group, less than 50 percent of the tested group\u2019s gross income) is paid or accrued, directly or indirectly, in the form of payments that are deductible for purposes of the income taxes imposed by Taiwan, to persons who are not\u2014 (I) qualified residents of Taiwan, or (II) United States persons who meet such requirements with respect to the United States as determined by the Secretary to be equivalent to the requirements of this subsection (determined without regard to paragraph (1)(B)) with respect to residents of Taiwan. (C) Publicly traded requirements An entity meets the requirements of this subparagraph if\u2014 (i) the principal class of its shares (and any disproportionate class of shares) of such entity are primarily and regularly traded on an established securities market in Taiwan, or (ii) the primary place of management and control of the entity is in Taiwan and all classes of its outstanding shares described in clause (i) are regularly traded on an established securities market in Taiwan. (D) Qualified subsidiary requirements An entity meets the requirement of this subparagraph if\u2014 (i) at least 50 percent (by vote and value) of the total outstanding shares of the stock of such entity are owned directly or indirectly by 5 or fewer entities\u2014 (I) which meet the requirements of subparagraph (C), or (II) which are United States persons the principal class of the shares (and any disproportionate class of shares) of which are primarily and regularly traded on an established securities market in the United States, and (ii) the entity meets the requirements of clause (ii) of subparagraph (B). (E) Only indirect ownership through qualifying intermediaries counted (i) In general Stock in an entity owned by a person indirectly through 1 or more other persons shall not be treated as owned by such person in determining whether the person meets the requirements of subparagraph (B)(i) or (D)(i) unless all such other persons are qualifying intermediate owners. (ii) Qualifying intermediate owners The term qualifying intermediate owner means a person that is\u2014 (I) a qualified resident of Taiwan, or (II) a resident of any other foreign country (other than a foreign country that is a foreign country of concern) that has in effect a comprehensive convention with the United States for the avoidance of double taxation. (iii) Special rule for qualified subsidiaries For purposes of applying subparagraph (D)(i), the term qualifying intermediate owner shall include any person who is a United States person who meets such requirements with respect to the United States as determined by the Secretary to be equivalent to the requirements of this subsection (determined without regard to paragraph (1)(B)) with respect to residents of Taiwan. (F) Certain payments not included In determining whether the requirements of subparagraph (B)(ii) or (D)(ii) are met with respect to an entity, the following payments shall not be taken into account: (i) Arm\u2019s-length payments by the entity in the ordinary course of business for services or tangible property. (ii) In the case of a tested group, intra-group transactions. (3) Dual residents (A) Rules for determination of status (i) In general An individual who is an applicable dual resident and who is described in subparagraph (B), (C), or (D) shall be treated as a qualified resident of Taiwan. (ii) Applicable dual resident For purposes of this paragraph, the term applicable dual resident means an individual who\u2014 (I) is not a United States citizen, (II) is a resident of the United States (determined without regard to subparagraph (E)), and (III) would be a qualified resident of Taiwan but for paragraph (1)(B). (B) Permanent home An individual is described in this subparagraph if such individual\u2014 (i) has a permanent home available to such individual in Taiwan, and (ii) does not have a permanent home available to such individual in the United States. (C) Center of vital interests An individual is described in this subparagraph if\u2014 (i) such individual has a permanent home available to such individual in both Taiwan and the United States, and (ii) such individual's personal and economic relations (center of vital interests) are closer to Taiwan than to the United States. (D) Habitual abode An individual is described in this subparagraph if\u2014 (i) such individual\u2014 (I) does not have a permanent home available to such individual in either Taiwan or the United States, or (II) has a permanent home available to such individual in both Taiwan and the United States but such individual's center of vital interests under subparagraph (C)(ii) cannot be determined, and (ii) such individual has a habitual abode in Taiwan and not the United States. (E) United states tax treatment of qualified resident of taiwan Notwithstanding section 7701, an individual who is treated as a qualified resident of Taiwan by reason of this paragraph for all or any portion of a taxable year shall not be treated as a resident of the United States for purposes of computing such individual's United States income tax liability for such taxable year or portion thereof. (4) Rules of special application (A) Dividends For purposes of applying this section to any dividend, paragraph (2)(D) shall be applied without regard to clause (ii) thereof. (B) Items of income emanating from an active trade or business in taiwan For purposes of this section\u2014 (i) In general Notwithstanding the preceding paragraphs of this subsection, if an entity taxed as a corporation in Taiwan is not a qualified resident of Taiwan but meets the requirements of subparagraphs (A) and (B) of paragraph (1), any qualified item of income such entity derived from the United States shall be treated as income of a qualified resident of Taiwan. (ii) Qualified items of income (I) In general The term qualified item of income means any item of income which emanates from, or is incidental to, the conduct of an active trade or business in Taiwan (other than operating as a holding company, providing overall supervision or administration of a group of companies, providing group financing, or making or managing investments (unless such making or managing investments is carried on by a bank, insurance company, or registered securities dealer in the ordinary course of its business as such)). (II) Substantial activity requirement An item of income which is derived from a trade or business conducted in the United States or from a connected person shall be a qualified item of income only if the trade or business activity conducted in Taiwan to which the item is related is substantial in relation to the same or a complementary trade or business activity carried on in the United States. For purposes of applying this subclause, activities conducted by persons that are connected to the entity described in clause (i) shall be deemed to be conducted by such entity. (iii) Exception This subparagraph shall not apply to any item of income derived by an entity if at least 50 percent (by vote or value) of such entity is owned (directly or indirectly) or controlled by residents of a foreign country of concern. (d) Other definitions and special rules For purposes of this section\u2014 (1) United states permanent establishment (A) In general The term United States permanent establishment means, with respect to a qualified resident of Taiwan, a permanent establishment of such resident which is within the United States. (B) Special rule The determination of whether there is a permanent establishment of a qualified resident of Taiwan within the United States shall be made without regard to whether an entity which is taxed as a corporation in Taiwan and which is a qualified resident of Taiwan controls or is controlled by\u2014 (i) a domestic corporation, or (ii) any other person that carries on business in the United States (whether through a permanent establishment or otherwise). (2) Permanent establishment (A) In general The term permanent establishment means a fixed place of business through which a trade or business is wholly or partly carried on. Such term shall include\u2014 (i) a place of management, (ii) a branch, (iii) an office, (iv) a factory, (v) a workshop, and (vi) a mine, an oil or gas well, a quarry, or any other place of extraction of natural resources. (B) Special rules for certain temporary projects (i) In general A building site or construction or installation project, or an installation or drilling rig or ship used for the exploration or exploitation of the sea bed and its subsoil and their natural resources, constitutes a permanent establishment only if it lasts, or the activities of the rig or ship lasts, for more than 12 months. (ii) Determination of 12-month period For purposes of clause (i), the period over which a building site or construction or installation project of a person lasts shall include any period of more than 30 days during which such person does not carry on activities at such building site or construction or installation project but connected activities are carried on at such building site or construction or installation project by one or more connected persons. (C) Habitual exercise of contract authority treated as permanent establishment Notwithstanding subparagraphs (A) and (B), where a person (other than an agent of an independent status to whom subparagraph (D)(ii) applies) is acting on behalf of a trade or business of a qualified resident of Taiwan and has and habitually exercises an authority to conclude contracts that are binding on the trade or business, that trade or business shall be deemed to have a permanent establishment in the country in which such authority is exercised in respect of any activities that the person undertakes for the trade or business, unless the activities of such person are limited to those described in subparagraph (D)(i) that, if exercised through a fixed place of business, would not make this fixed place of business a permanent establishment under the provisions of that subparagraph. (D) Exclusions (i) In general Notwithstanding subparagraphs (A) and (B), the term permanent establishment shall not include\u2014 (I) the use of facilities solely for the purpose of storage, display, or delivery of goods or merchandise belonging to the trade or business, (II) the maintenance of a stock of goods or merchandise belonging to the trade or business solely for the purpose of storage, display, or delivery, (III) the maintenance of a stock of goods or merchandise belonging to the trade or business solely for the purpose of processing by another trade or business, (IV) the maintenance of a fixed place of business solely for the purpose of purchasing goods or merchandise, or of collecting information, for the trade or business, (V) the maintenance of a fixed place of business solely for the purpose of carrying on, for the trade or business, any other activity of a preparatory or auxiliary character, or (VI) the maintenance of a fixed place of business solely for any combination of the activities mentioned in subclauses (I) through (V), provided that the overall activity of the fixed place of business resulting from this combination is of a preparatory or auxiliary character. (ii) Brokers and other independent agents A trade or business shall not be considered to have a permanent establishment in a country merely because it carries on business in such country through a broker, general commission agent, or any other agent of an independent status, provided that such persons are acting in the ordinary course of their business as independent agents. (3) Tested group The term tested group includes, with respect to any entity taxed as a corporation in Taiwan, such entity and any other entity taxed as a corporation in Taiwan that\u2014 (A) participates as a member with such entity in a tax consolidation, fiscal unity, or similar regime that requires members of the group to share profits or losses, or (B) shares losses with such entity pursuant to a group relief or other loss sharing regime. (4) Connected person Two persons shall be connected persons if one owns, directly or indirectly, at least 50 percent of the interests in the other (or, in the case of a corporation, at least 50 percent of the aggregate vote and value of the corporation\u2019s shares) or another person owns, directly or indirectly, at least 50 percent of the interests (or, in the case of a corporation, at least 50 percent of the aggregate vote and value of the corporation\u2019s shares) in each person. In any case, a person shall be connected to another if, based on all the relevant facts and circumstances, one has control of the other or both are under the control of the same person or persons. (5) Foreign country of concern The term foreign country of concern has the meaning given such term under paragraph (7) of section 9901 of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( 15 U.S.C. 4651(7) ), as added by section 103(a)(4) of the CHIPS Act of 2022). (6) Partnerships; beneficiaries of estates and trusts For purposes of this section\u2014 (A) a qualified resident of Taiwan which is a partner of a partnership which carries on a trade or business within the United States through a United States permanent establishment shall be treated as carrying on such trade or business through such permanent establishment, and (B) a qualified resident of Taiwan which is a beneficiary of an estate or trust which carries on a trade or business within the United States through a United States permanent establishment shall be treated as carrying on such trade or business through such permanent establishment. (7) Denial of benefits for certain payments through hybrid entities For purposes of this section, rules similar to the rules of section 894(c) shall apply. (e) Application (1) In general This section shall not apply to any period unless the Secretary has determined that Taiwan has provided benefits to United States persons for such period that are reciprocal to the benefits provided to qualified residents of Taiwan under this section. (2) Provision of reciprocity The President or his designee is authorized to exchange letters, enter into an agreement, or take other necessary and appropriate steps relative to Taiwan for the reciprocal provision of the benefits described in this section. (f) Regulations or other guidance (1) In general The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the provisions of this section, including such regulations or guidance for\u2014 (A) determining\u2014 (i) what constitutes a United States permanent establishment of a qualified resident of Taiwan, and (ii) income that is effectively connected with such a permanent establishment, (B) preventing the abuse of the provisions of this section by persons who are not (or who should not be treated as) qualified residents of Taiwan, (C) requirements for record keeping and reporting, (D) rules to assist withholding agents or employers in determining whether a foreign person is a qualified resident of Taiwan for purposes of determining whether withholding or reporting is required for a payment (and, if withholding is required, whether it should be applied at a reduced rate), (E) the application of subsection (a)(1)(D)(i) to stock held by predecessor owners, (F) determining what amounts are to be treated as qualified wages for purposes of subsection (a)(2), (G) determining the amounts to which subsection (a)(3) applies, (H) defining established securities market for purposes of subsection (c), (I) the application of the rules of subsection (c)(4)(B), (J) the application of subsection (d)(6) and section 1446, (K) determining ownership interests held by residents of a foreign country of concern, and (L) determining the starting and ending dates for periods with respect to the application of this section under subsection (e), which may be separate dates for taxes withheld at the source and other taxes. (2) Regulations to be consistent with model treaty Any regulations or other guidance issued under this section shall, to the extent practical, be consistent with the provisions of the United States model income tax convention dated February 7, 2016. .\n##### (b) Conforming amendment to withholding tax\nSubchapter A of chapter 3 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n1447. Withholding for qualified residents of taiwan For reduced rates of withholding for certain residents of Taiwan, see section 894A. .\n##### (c) Clerical amendments\n**(1)**\nThe table of sections for subpart D of part II of subchapter N of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 894 the following new item:\nSec. 894A. Special rules for qualified residents of Taiwan.\n**(2)**\nThe table of sections for subchapter A of chapter 3 of such Code is amended by adding at the end the following new item:\nSec. 1447. Withholding for qualified residents of Taiwan.\nII\nUnited States-Taiwan tax agreement Authorization Act\n#### 201. Short title\nThis title may be cited as the United States-Taiwan Tax Agreement Authorization Act .\n#### 202. Definitions\nIn this title:\n**(1) Agreement**\nThe term Agreement means the tax agreement authorized by section 203(a).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations and the Committee on Finance of the Senate; and\n**(B)**\nthe Committee on Ways and Means of the House of Representatives.\n**(3) Approval legislation**\nThe term approval legislation means legislation that approves the Agreement.\n**(4) Implementing legislation**\nThe term implementing legislation means legislation that makes any changes to the Internal Revenue Code of 1986 necessary to implement the Agreement.\n#### 203. Authorization to negotiate and enter into agreement\n##### (a) In general\nSubsequent to a determination under section 894A(e)(1) of the Internal Revenue Code of 1986 (as added by the United States-Taiwan Expedited Double-Tax Relief Act), the President is authorized to negotiate and enter into a tax agreement relative to Taiwan.\n##### (b) Elements of agreement\n**(1) Conformity with bilateral income tax conventions**\nThe President shall ensure that\u2014\n**(A)**\nany provisions included in the Agreement conform with provisions customarily contained in United States bilateral income tax conventions, as exemplified by the 2016 United States Model Income Tax Convention; and\n**(B)**\nthe Agreement does not include elements outside the scope of the 2016 United States Model Income Tax Convention.\n**(2) Incorporation of tax agreements and laws**\nNotwithstanding paragraph (1), the Agreement may incorporate and restate provisions of any agreement, or existing United States law, addressing double taxation for residents of the United States and Taiwan.\n**(3) Authority**\nThe Agreement shall include the following statement: The Agreement is entered into pursuant to the United States-Taiwan Tax Agreement Authorization Act.\n**(4) Entry into force**\nThe Agreement shall include a provision conditioning entry into force upon\u2014\n**(A)**\nenactment of approval legislation and implementing legislation pursuant to section 207; and\n**(B)**\nconfirmation by the Secretary of the Treasury that the relevant authority in Taiwan has approved and taken appropriate steps required to implement the Agreement.\n#### 204. Consultations with congress\n##### (a) Notification upon commencement of negotiations\nThe President shall provide written notification to the appropriate congressional committees of the commencement of negotiations between the United States and Taiwan on the Agreement at least 15 calendar days before commencing such negotiations.\n##### (b) Consultations during negotiations\n**(1) Briefings**\nNot later than 90 days after commencement of negotiations with respect to the Agreement, and every 180 days thereafter until the President enters into the Agreement, the President shall provide a briefing to the appropriate congressional committees on the status of the negotiations, including a description of elements under negotiation.\n**(2) Meetings and other consultations**\n**(A) In general**\nIn the course of negotiations with respect to the Agreement, the Secretary of the Treasury, in coordination with the Secretary of State, shall\u2014\n**(i)**\nmeet, upon request, with the chairman or ranking member of any of the appropriate congressional committees regarding negotiating objectives and the status of negotiations in progress; and\n**(ii)**\nconsult closely and on a timely basis with, and keep fully apprised of the negotiations, the appropriate congressional committees.\n**(B) Elements of consultations**\nThe consultations described in subparagraph (A) shall include consultations with respect to\u2014\n**(i)**\nthe nature of the contemplated Agreement;\n**(ii)**\nhow and to what extent the contemplated Agreement is consistent with the elements set forth in section 203(b); and\n**(iii)**\nthe implementation of the contemplated Agreement, including\u2014\n**(I)**\nthe general effect of the contemplated Agreement on existing laws;\n**(II)**\nproposed changes to any existing laws to implement the contemplated Agreement; and\n**(III)**\nproposed administrative actions to implement the contemplated Agreement.\n#### 205. Approval and implementation of agreement\n##### (a) In general\nThe Agreement may not enter into force unless\u2014\n**(1)**\nthe President, at least 60 days before the day on which the President enters into the Agreement, publishes the text of the contemplated Agreement on a publicly available website of the Department of the Treasury; and\n**(2)**\nthere is enacted into law, with respect to the Agreement, approval legislation and implementing legislation pursuant to section 207.\n##### (b) Entry into force\nThe President may provide for the Agreement to enter into force upon\u2014\n**(1)**\nenactment of approval legislation and implementing legislation pursuant to section 207; and\n**(2)**\nconfirmation by the Secretary of the Treasury that the relevant authority in Taiwan has approved and taken appropriate steps required to implement the Agreement.\n#### 206. Submission to congress of agreement and implementation policy\n##### (a) Submission of agreement\nNot later than 270 days after the President enters into the Agreement, the President or the President\u2019s designee shall submit to Congress\u2014\n**(1)**\nthe final text of the Agreement; and\n**(2)**\na technical explanation of the Agreement.\n##### (b) Submission of implementation policy\nNot later than 270 days after the President enters into the Agreement, the Secretary of the Treasury shall submit to Congress\u2014\n**(1)**\na description of those changes to existing laws that the President considers would be required in order to ensure that the United States acts in a manner consistent with the Agreement; and\n**(2)**\na statement of anticipated administrative action proposed to implement the Agreement.\n#### 207. Consideration of approval legislation and implementing legislation\n##### (a) In general\nThe approval legislation with respect to the Agreement shall include the following: Congress approves the Agreement submitted to Congress pursuant to section 206 of the United States-Taiwan Tax Agreement Authorization Act on ____. , with the blank space being filled with the appropriate date.\n##### (b) Approval legislation committee referral\nThe approval legislation shall\u2014\n**(1)**\nin the Senate, be referred to the Committee on Foreign Relations; and\n**(2)**\nin the House of Representatives, be referred to the Committee on Ways and Means.\n##### (c) Implementing legislation committee referral\nThe implementing legislation shall\u2014\n**(1)**\nin the Senate, be referred to the Committee on Finance; and\n**(2)**\nin the House of Representatives, be referred to the Committee on Ways and Means.\n#### 208. Relationship of agreement to Internal Revenue Code of 1986\n##### (a) Internal revenue code of 1986 to control\nNo provision of the Agreement or approval legislation, nor the application of any such provision to any person or circumstance, which is inconsistent with any provision of the Internal Revenue Code of 1986, shall have effect.\n##### (b) Construction\nNothing in this title shall be construed\u2014\n**(1)**\nto amend or modify any law of the United States; or\n**(2)**\nto limit any authority conferred under any law of the United States, unless specifically provided for in this title.\n#### 209. Authorization of subsequent tax agreements relative to Taiwan\n##### (a) In general\nSubsequent to the enactment of approval legislation and implementing legislation pursuant to section 207\u2014\n**(1)**\nthe term tax agreement in section 203(a) shall be treated as including any tax agreement relative to Taiwan which supplements or supersedes the Agreement to which such approval legislation and implementing legislation relates; and\n**(2)**\nthe term Agreement shall be treated as including such tax agreement.\n##### (b) Requirements, etc., To apply separately\nThe provisions of this title (including section 204) shall be applied separately with respect to each tax agreement referred to in subsection (a).\n#### 210. United States treatment of double taxation matters with respect to Taiwan\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nThe United States addresses issues with respect to double taxation with foreign countries by entering into bilateral income tax conventions (known as tax treaties) with such countries, subject to the advice and consent of the Senate to ratification pursuant to article II of the Constitution.\n**(2)**\nThe United States has entered into more than sixty such tax treaties, which facilitate economic activity, strengthen bilateral cooperation, and benefit United States workers, businesses, and other United States taxpayers.\n**(3)**\nDue to Taiwan\u2019s unique status, the United States is unable to enter into an article II tax treaty with Taiwan, necessitating an agreement to address issues with respect to double taxation.\n##### (b) Statement of policy\nIt is the policy of the United States to\u2014\n**(1)**\nprovide for additional bilateral tax relief with respect to Taiwan, beyond that provided for in section 894A of the Internal Revenue Code of 1986 (as added by the United States-Taiwan Expedited Double-Tax Relief Act), only after entry into force of an Agreement, as provided for in section 205, and only in a manner consistent with such Agreement; and\n**(2)**\ncontinue to provide for bilateral tax relief with sovereign states to address double taxation and other related matters through entering into bilateral income tax conventions, subject to the Senate\u2019s advice and consent to ratification pursuant to article II of the Constitution.",
      "versionDate": "2025-01-23",
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
        "actionDate": "2025-01-16",
        "text": "Received in the Senate and Read twice and referred to the Committee on Finance."
      },
      "number": "33",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.",
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
        "name": "Taxation",
        "updateDate": "2025-02-25T20:52:30Z"
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
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s199is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States-Taiwan Tax Agreement Authorization Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States-Taiwan Expedited Double-Tax Relief Act",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-02-22T06:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:18:52Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide special rules for the taxation of certain residents of Taiwan with income from sources within the United States.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T11:56:32Z"
    }
  ]
}
```
