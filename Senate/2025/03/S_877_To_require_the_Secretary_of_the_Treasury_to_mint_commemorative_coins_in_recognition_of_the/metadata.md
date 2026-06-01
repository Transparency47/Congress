# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/877?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/877
- Title: Roberto Clemente Commemorative Coin Act
- Congress: 119
- Bill type: S
- Bill number: 877
- Origin chamber: Senate
- Introduced date: 2025-03-06
- Update date: 2026-01-28T12:03:16Z
- Update date including text: 2026-01-28T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-06: Introduced in Senate
- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1605-1606)
- Latest action: 2025-03-06: Introduced in Senate

## Actions

- 2025-03-06 - IntroReferral: Introduced in Senate
- 2025-03-06 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1605-1606)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/877",
    "number": "877",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Roberto Clemente Commemorative Coin Act",
    "type": "S",
    "updateDate": "2026-01-28T12:03:16Z",
    "updateDateIncludingText": "2026-01-28T12:03:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs. (text: CR S1605-1606)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-06",
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
            "date": "2025-03-06T16:12:42Z",
            "name": "Referred To"
          },
          {
            "date": "2025-03-06T16:12:42Z",
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
      "sponsorshipDate": "2025-03-06",
      "state": "WV"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "HI"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "TX"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-01-27",
      "state": "ME"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-27",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s877is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 877\nIN THE SENATE OF THE UNITED STATES\nMarch 6, 2025 Mr. Schumer (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of the Treasury to mint commemorative coins in recognition of the life and legacy of Roberto Clemente.\n#### 1. Short title\nThis Act may be cited as the Roberto Clemente Commemorative Coin Act .\n#### 2. Findings\nThe Congress finds the following:\n**(1)**\nRoberto Clemente Walker was born on August 18, 1934, to Don Melchor Clemente and Luisa Walker in Barrio San Ant\u00f3n, Carolina, Puerto Rico, as the youngest of 7 children.\n**(2)**\nClemente excelled in athletics as a youngster and, at the age of 17, was playing for the Santurce Cangrejeros Crabbers of the Puerto Rican Baseball League.\n**(3)**\nIn 1954, the Pittsburgh Pirates selected Clemente in the first round of the Major League Baseball Rule 5 draft.\n**(4)**\nPirates center fielder Earl Smith wore jersey number 21 until he parted ways with the team in April 1955, and Clemente wore number 13 until then.\n**(5)**\nIn 1955, Clemente made his Major League debut as he went on to play for the Pittsburgh Pirates, starting as a right fielder.\n**(6)**\nWhen the team traveled to Richmond, Virginia, for games or Florida for spring training, Clemente encountered Jim Crow laws for the first time when the Black players had to stay at a separate, inferior hotel and were refused the option to dine with their White counterparts.\n**(7)**\nClemente was known for being a proud Afro-Latino and protested the discrimination that Latin and Black ball players encountered.\n**(8)**\nClemente was known for defending the rights of Black and Brown people, both on the field and in the streets.\n**(9)**\nAfter the assassination of Martin Luther King, Jr., in 1968, Clemente and his teammates refused to play until after the funerals and even wrote a public statement showing their respect for Dr. King.\n**(10)**\nClemente became a union leader in the incipient Major League Baseball Players Association and defended players\u2019 rights to demand better working conditions and benefits.\n**(11)**\nIn every city where the Pirates played, Clemente visited sick children in hospitals.\n**(12)**\nClemente established training clinics, providing baseball lessons and fun for boys and girls in Pittsburgh, his home island of Puerto Rico, and throughout Latin America.\n**(13)**\nIn 1958, Clemente enlisted in the United States Marine Corps Reserve after the 1958 season and spent 6 months on active duty at Parris Island, South Carolina, and Camp LeJeune, North Carolina.\n**(14)**\nClemente served until 1964 and was inducted into the Marine Corps Sports Hall of Fame in 2003.\n**(15)**\nBy the end of his career, Clemente had joined the exclusive 3,000-hit club, was selected to 15 All-Star teams, and won 12 Gold Gloves, 2 World Series, and a National League MVP award.\n**(16)**\nIn Clemente\u2019s 18 seasons with Pittsburgh he won 4 batting titles, hit 240 home runs, and posted a lifetime .317 batting average.\n**(17)**\nIn late 1972, a 6.3 magnitude earthquake ravaged Managua, Nicaragua, and killed 5,000 people.\n**(18)**\nIn his philanthropic spirit, Clemente sent shipments of humanitarian aid to the country.\n**(19)**\nAfter learning that 3 previous shipments had been diverted by corrupt Somoza Government officials, Clemente decided to accompany one of the aid shipments.\n**(20)**\nThe four-engine DC\u20137 plane Clemente chartered for a flight on New Year\u2019s Eve crashed in the Atlantic Ocean immediately after takeoff from the coast of Isla Verde, Puerto Rico.\n**(21)**\nOn December 31, 1972, Clemente died in the plane crash at the age of 38 years young.\n**(22)**\nSince 1973, Major League Baseball gives out the Roberto Clemente Award to one player in the league who best exemplifies the game of baseball, sportsmanship, community involvement and the individual\u2019s contribution to his team .\n**(23)**\nIn 2002, Major League Baseball declared the first annual Roberto Clemente Day.\n**(24)**\nIn 2021, Major League Baseball announced September 15 would be the permanent date of Roberto Clemente Day to coincide with the beginning of Hispanic Heritage month.\n**(25)**\nClemente was the first Latino player to accomplish many feats in Major League Baseball.\n**(26)**\nClemente was the first Puerto Rican, and first person of Latino heritage, to win a World Series as a starter, be named league MVP, be named World Series MVP, and be elected to the Hall of Fame.\n**(27)**\nClemente was posthumously elected to the National Baseball Hall of Fame in 1973, being the first National League baseball player to receive the mandatory 5-year waiting period waiver.\n**(28)**\nClemente was a legend in life and death, a baseball star, a humanitarian activist, and a symbol of Latin American pride.\n#### 3. Coin specifications\n##### (a) Denominations\nThe Secretary of the Treasury (hereafter in this Act referred to as the Secretary ) shall mint and issue the following coins:\n**(1) $5 gold coins**\nNot more than 50,000 $5 coins, which shall\u2014\n**(A)**\nweigh 8.359 grams;\n**(B)**\nhave a diameter of 0.850 inches; and\n**(C)**\ncontain not less than 90 percent gold.\n**(2) $1 silver coins**\nNot more than 400,000 $1 coins, which shall\u2014\n**(A)**\nweigh 26.73 grams;\n**(B)**\nhave a diameter of 1.500 inches; and\n**(C)**\ncontain not less than 90 percent silver.\n**(3) Half-dollar clad coins**\nNot more than 750,000 half-dollar coins which shall\u2014\n**(A)**\nweigh 11.34 grams;\n**(B)**\nhave a diameter of 1.205 inches; and\n**(C)**\nbe minted to the specifications for half-dollar coins contained in section 5112(b) of title 31, United States Code.\n##### (b) Legal tender\nThe coins minted under this Act shall be legal tender, as provided in section 5103 of title 31, United States Code.\n##### (c) Numismatic items\nFor purposes of sections 5134 and 5136 of title 31, United States Code, all coins minted under this Act shall be considered to be numismatic items.\n#### 4. Design of coins\n##### (a) Design requirements\n**(1) In general**\nThe designs of the coins minted under this Act shall be emblematic of the life of Roberto Clemente, including his human rights activism and baseball stardom legacy. At least 1 obverse design shall bear the image of Roberto Clemente.\n**(2) Designation and inscriptions**\nOn each coin minted under this Act, there shall be\u2014\n**(A)**\nan inscription of Roberto Clemente;\n**(B)**\na designation of the value of the coin;\n**(C)**\nan inscription of the year 2027 ; and\n**(D)**\ninscriptions of the words Liberty , In God We Trust , United States of America , and E Pluribus Unum .\n##### (b) Selection\nThe designs for the coins minted under this Act shall be\u2014\n**(1)**\nselected by the Secretary after consultation with the Roberto Clemente Foundation, Roberto Clemente\u2019s living family members, and the Commission of the Fine Arts; and\n**(2)**\nreviewed by the Citizens Coinage Advisory Committee.\n#### 5. Issuance of coins\n##### (a) Quality of coins\nCoins minted under this Act shall be issued in uncirculated and proof qualities.\n##### (b) Period for issuance\nThe Secretary may issue coins under this Act only during the 1-year period beginning on January 1, 2027.\n#### 6. Sale of coins\n##### (a) Sale price\nThe coins issued under this Act shall be sold by the Secretary at a price equal to the sum of\u2014\n**(1)**\nthe face value of the coins;\n**(2)**\nthe surcharge provided in section 7(a) with respect to such coins; and\n**(3)**\nthe cost of designing and issuing the coins (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping).\n##### (b) Bulk sales\nThe Secretary shall make bulk sales of the coins issued under this Act at a reasonable discount.\n##### (c) Prepaid orders\n**(1) In general**\nThe Secretary shall accept prepaid orders for the coins minted under this Act before the issuance of such coins.\n**(2) Discount**\nSale prices with respect to prepaid orders under paragraph (1) shall be at a reasonable discount.\n#### 7. Surcharges\n##### (a) In general\nAll sales of coins issued under this Act shall include\u2014\n**(1)**\na surcharge of $35 per coin for the $5 coins;\n**(2)**\na surcharge of $10 per coin for the $1 coins; and\n**(3)**\na surcharge of $5 per coin for the half-dollar coins.\n##### (b) Distribution\nSubject to section 5134(f) of title 31, United States Code, all surcharges received by the Secretary from the sale of coins issued under this Act shall be paid to the Roberto Clemente Foundation to be used for general expenses associated with the fulfillment of the mission of the Roberto Clemente Foundation, including for costs associated with educational, youth sports, and disaster relief historic preservation.\n##### (c) Audits\nThe Roberto Clemente Foundation, shall be subject to the audit requirements of section 5134(f)(2) of title 31, United States Code, with regard to the amounts received under subsection (b).\n##### (d) Limitation\nNotwithstanding subsection (a), no surcharge may be included with respect to the issuance under this Act of any coin during a calendar year if, as of the time of such issuance, the issuance of such coin would result in the number of commemorative coin programs issued during such year to exceed the annual 2 commemorative coin program issuance limitation under section 5112(m)(1) of title 31, United States Code (as in effect on the date of the enactment of this Act). The Secretary may issue guidance to carry out this subsection.\n#### 8. Financial assurances\nThe Secretary shall take such actions as may be necessary to ensure that\u2014\n**(1)**\nminting and issuing coins under this Act will not result in any net cost to the United States Government; and\n**(2)**\nno funds, including applicable surcharges, shall be disbursed to any recipient designated in section 7 until the total cost of designing and issuing all of the coins authorized by this Act (including labor, materials, dies, use of machinery, overhead expenses, marketing, and shipping) is recovered by the United States Treasury, consistent with sections 5112(m) and 5134(f) of title 31, United States Code.",
      "versionDate": "2025-03-06",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Financial Services."
      },
      "number": "1787",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Roberto Clemente Commemorative Coin Act",
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
        "updateDate": "2025-03-28T12:37:09Z"
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
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s877is.xml"
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
      "title": "Roberto Clemente Commemorative Coin Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-28T12:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Roberto Clemente Commemorative Coin Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of the Treasury to mint commemorative coins in recognition of the life and legacy of Roberto Clemente.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:49Z"
    }
  ]
}
```
