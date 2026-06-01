# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2667?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2667
- Title: West Bank Violence Prevention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2667
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2667",
    "number": "2667",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "West Bank Violence Prevention Act of 2025",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-08-01",
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
            "date": "2025-08-01T22:09:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-08-01T22:09:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NH"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
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
      "sponsorshipDate": "2025-08-01",
      "state": "DE"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CO"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "VA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "RI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VT"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "CO"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "WA"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "DE"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
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
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "AZ"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "MD"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "WA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-10-30",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MA"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "MA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "HI"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "NV"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "NM"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NV"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NY"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2026-01-28",
      "state": "GA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "NM"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "AZ"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-02-11",
      "state": "ME"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "IL"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2026-03-02",
      "state": "NH"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CT"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "GA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-03-19",
      "state": "WI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "MI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-13",
      "state": "IL"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NJ"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "False",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2667is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2667\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Booker (for himself, Mrs. Shaheen , Mr. Reed , Mr. Coons , Mr. Bennet , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo prevent violence in the West Bank and authorize the imposition of sanctions with respect to any foreign person endangering United States national security and undermining prospects for a two-state solution by committing illegal violent acts.\n#### 1. Short title\nThis Act may be cited as the West Bank Violence Prevention Act of 2025 .\n#### 2. Sanctions with respect to actions threatening peace, security, or stability of the West Bank\n##### (a) In general\nThe President shall impose sanctions described in subsection (b) with respect to any foreign person determined by the President to meet any of the following:\n**(1)**\nTo be responsible for or complicit in, or to have directly or indirectly engaged or attempted to engage in directing, enacting, implementing, planning, ordering, participating in, enforcing, or failing to enforce policies that would prevent, actions that threaten the peace, security, or stability of the West Bank, including the following:\n**(A)**\nAn act of violence targeting civilians.\n**(B)**\nA threat of violence targeting civilians with the intent to coerce or intimidate.\n**(C)**\nEfforts to place civilians in reasonable fear of violence with the purpose or effect of necessitating a change of residence to avoid such violence.\n**(D)**\nDestruction by private persons of physical property, without the consent of the owner, that renders the property unusable, a residence uninhabitable, or agricultural land unworkable.\n**(E)**\nSeizure or dispossession of property by private persons.\n**(2)**\nTo be or have been a leader or official of\u2014\n**(A)**\nan entity, including any government entity, that has engaged in, or members of which have engaged in, any of the activities described in paragraph (1) or (5) related to the leader\u2019s or official\u2019s tenure; or\n**(B)**\nan entity the property and interests in property of which are blocked under this section as a result of activities relating to the leader\u2019s or official\u2019s tenure.\n**(3)**\nTo have materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services to or in support of, any person the property and interests in property of which are blocked under this section.\n**(4)**\nTo be owned or controlled by, or to have acted or purported to act for or on behalf of, directly or indirectly, any person the property and interests in property of which are blocked under this section.\n**(5)**\nTo have committed or have attempted to commit, or to have participated in training to commit, acts of terrorism targeting the West Bank.\n**(6)**\nTo be a leader or official of an entity subject to sanctions under paragraph (5).\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\n**(A) In general**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President shall exercise all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of any foreign person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(B) Matters to be included**\nA prohibition on transactions under subparagraph (A) includes\u2014\n**(i)**\nthe making of any contribution or provision of funds, goods, or services by, to, or for the benefit of any person the property and interests in property of which are blocked pursuant to subparagraph (A); and\n**(ii)**\nthe receipt of any contribution or provision of funds, goods, or services from any such person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (a) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (c) Exceptions\n**(1) Authorized intelligence activities**\nSanctions under this section shall not apply with respect to any activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(2) Humanitarian assistance**\nSanctions under this section shall not apply to\u2014\n**(A)**\nthe conduct or facilitation of a transaction for the provision of agricultural commodities, food, medicine, medical devices, or humanitarian assistance, or for humanitarian purposes; or\n**(B)**\ntransactions that are necessary for or related to the activities described in clause (i).\n**(3) Exception to comply with international obligations and for law enforcement**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States\u2014\n**(A)**\nis necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations; or\n**(B)**\nwould further important United States law enforcement objectives.\n##### (d) National security waiver\nThe President may waive the imposition of sanctions under this section with respect to a foreign person if the President determines that the waiver is in the national security interests of the United States.\n##### (e) Termination of sanctions\nThe President may terminate the application of sanctions under this section with respect to a foreign person if the President certifies to the appropriate congressional committees that\u2014\n**(1)**\nthe person\u2014\n**(A)**\nis not engaging in the activity that was the basis for such sanctions; or\n**(B)**\nhas taken significant, verifiable steps toward stopping the activity that was the basis for such sanctions; and\n**(2)**\nthe President has received reliable assurances that the person will not knowingly engage in any activity subject to sanctions in the future.\n##### (f) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (g) Report required\nNot later than 90 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\nan assessment of the implementation of this section, including\u2014\n**(A)**\nthe names of any persons that have been designated for the imposition of sanctions under this section;\n**(B)**\na description of the sanctions considered and imposed with respect to each such person; and\n**(C)**\na description of the activity each such person engaged in that was the basis for the sanctions;\n**(2)**\na list of persons for which the imposition of sanctions was waived under subsection (d) and a detailed, specific description of the activity each such person engaged in that would have been the basis for imposing sanctions but for the waiver;\n**(3)**\na description of the circumstances in the West Bank relating to acts of violence against civilians and private property and an assessment of whether any of such acts of violence were against United States persons or property owned by United States persons; and\n**(4)**\na description of the actions the United States Government and regional partners are taking to reduce violence against civilians and the destruction of private property in the West Bank.\n##### (h) Definitions\nIn this section:\n**(1) Admission; admitted; alien; etc**\nThe terms admission , admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Agricultural commodity**\nThe term agricultural commodity has the meaning given that term in section 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ).\n**(3) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on Financial Services of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(4) Entity**\nThe term entity means a partnership, association, trust, joint venture, corporation, group, subgroup, or other organization.\n**(5) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(6) Medicine**\nThe term medicine has the meaning given the term drug in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(7) Person**\nThe term person means an individual or entity.\n**(8) United states person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n**(9) Terrorism**\nThe term terrorism means an activity that\u2014\n**(A)**\ninvolves a violent act or an act dangerous to human life, property, or infrastructure; and\n**(B)**\nappears to be intended\u2014\n**(i)**\nto intimidate or coerce a civilian population;\n**(ii)**\nto influence the policy of a government by intimidation or coercion; or\n**(iii)**\nto affect the conduct of a government by mass destruction, assassination, kidnapping, or hostage-taking.",
      "versionDate": "2025-08-01",
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
        "name": "International Affairs",
        "updateDate": "2025-09-18T20:21:13Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2667is.xml"
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
      "title": "West Bank Violence Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "West Bank Violence Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent violence in the West Bank and authorize the imposition of sanctions with respect to any foreign person endangering United States national security and undermining prospects for a two-state solution by committing illegal violent acts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:29Z"
    }
  ]
}
```
