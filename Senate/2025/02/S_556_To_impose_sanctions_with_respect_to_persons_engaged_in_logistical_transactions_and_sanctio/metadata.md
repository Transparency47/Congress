# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/556?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/556
- Title: Enhanced Iran Sanctions Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 556
- Origin chamber: Senate
- Introduced date: 2025-02-12
- Update date: 2026-02-27T12:03:20Z
- Update date including text: 2026-02-27T12:03:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-12: Introduced in Senate
- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-02-12: Introduced in Senate

## Actions

- 2025-02-12 - IntroReferral: Introduced in Senate
- 2025-02-12 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-12",
    "latestAction": {
      "actionDate": "2025-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/556",
    "number": "556",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Enhanced Iran Sanctions Act of 2025",
    "type": "S",
    "updateDate": "2026-02-27T12:03:20Z",
    "updateDateIncludingText": "2026-02-27T12:03:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-12",
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
      "actionDate": "2025-02-12",
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
            "date": "2025-02-12T22:45:07Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-12T22:45:07Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-02-12",
      "state": "CT"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "TX"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-12",
      "state": "NE"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "VA"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NV"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "MO"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "GA"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "False",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-03-04",
      "state": "UT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "AZ"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "VA"
    },
    {
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
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
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "False",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "KS"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MD"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MN"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "OH"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "KS"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "WV"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "ND"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "AL"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "WY"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "AR"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "False",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "WA"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "OK"
    },
    {
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "ME"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-05-20",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "TN"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "False",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "SD"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AK"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-07-28",
      "state": "ID"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "OK"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "MT"
    },
    {
      "bioguideId": "C001095",
      "firstName": "Tom",
      "fullName": "Sen. Cotton, Tom [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Cotton",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "AR"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "False",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-10-14",
      "state": "KY"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-09",
      "state": "TX"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "ND"
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-01-12",
      "state": "NM"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s556is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 556\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2025 Mr. Sullivan (for himself, Mr. Blumenthal , Mr. Cornyn , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo impose sanctions with respect to persons engaged in logistical transactions and sanctions evasion relating to oil, gas, liquefied natural gas, and related petrochemical products from the Islamic Republic of Iran, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhanced Iran Sanctions Act of 2025 .\n#### 2. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nthat, in accordance with the Iran Nuclear Weapons Capability and Terrorism Monitoring Act of 2022 ( 22 U.S.C. 8701 note; Public Law 117\u2013263 ), the United States must\u2014\n**(A)**\nensure that the Islamic Republic of Iran does not acquire a nuclear weapons capability;\n**(B)**\nprotect against aggression from the Islamic Republic of Iran manifested through its missiles and drone programs; and\n**(C)**\ncounter regional and global terrorism of the Islamic Republic of Iran in a manner that minimizes the threat posed by state and non-state actors to the interests of the United States;\n**(2)**\nto fully enforce sanctions against all persons involved in the international logistical chain that provide support to the energy sector of the Islamic Republic of Iran;\n**(3)**\nthrough such sanctions, to deny the Islamic Republic of Iran the financial resources required\u2014\n**(A)**\nto fund and facilitate international terrorism;\n**(B)**\nto finance the development of weapons of mass destruction;\n**(C)**\nto engage in destabilizing efforts abroad; and\n**(D)**\nto repress the rights of Iranian citizens; and\n**(4)**\nto strengthen coherence among members of the international community in enforcing sanctions on the malign activity of the Islamic Republic of Iran.\n#### 3. Definitions\nIn this Act:\n**(1) Admitted; alien**\nThe terms admitted and alien have the meanings given those terms in section 101(a) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a) ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations, the Committee on the Judiciary, and the Committee on Banking, Housing, and Urban Affairs of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs, the Committee on the Judiciary, and the Committee on Financial Services of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means a person that is not a United States person, including the government of a foreign country.\n**(4) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(5) Property; interest in property**\nThe terms property and interest in property have the meanings given the terms property and property interest , respectively, in section 576.312 of title 31, Code of Federal Regulations, as in effect on the day before the date of the enactment of this Act.\n**(6) United States person**\nThe term United States person means\u2014\n**(A)**\nan individual who is a United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n#### 4. Imposition of sanctions with respect to persons engaged in logistical transactions of oil, gas, liquefied natural gas, and petrochemical products from the Islamic Republic of Iran\n##### (a) In general\nOn and after the date of the enactment of this Act, the President shall impose the sanctions described in subsection (b) with respect to any foreign person, including any bank or foreign financial institution, insurance provider, flagging registry, pipeline construction or operation facility for liquefied natural gas, that\u2014\n**(1)**\nthe President determines knowingly engaged in, on or after such date of enactment, any transaction involved in, relating or incident to the processing, export, or sale of oil, condensates, gas, liquefied natural gas, or other petrochemical products in whole or in part from the Islamic Republic of Iran;\n**(2)**\nis a subsidiary, successor, or alias of a foreign person described in paragraph (1);\n**(3)**\n**(A)**\ndirectly or indirectly owns or controls a 50 percent or greater interest in or is owned or controlled by a 50 percent or greater interest of a foreign person or foreign persons subject to sanctions pursuant to paragraph (1) or (2); and\n**(B)**\ndirectly or indirectly conducts a significant transaction with, for, or on behalf of a foreign person described in paragraph (1), (2), or (3) of section 3(b) of the Stop Harboring Iranian Petroleum Act ( 22 U.S.C. 8572 );\n**(4)**\nthe President determines is a corporate officer of a foreign person described paragraph (1), (2), or (3); or\n**(5)**\nis an immediate family member of a foreign person described in paragraph (1), (2), or (3).\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall, pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ), block and prohibit all transactions in property and interests in property of a foreign person subject to sanctions pursuant to subsection (a)(1) if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Aliens inadmissible for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nIn the case of an alien subject to sanctions pursuant to subsection (a), the alien is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subparagraph (A) shall be revoked, regardless of when such visa or other entry documentation was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception relating to importation of goods**\n**(A) In general**\nThe requirement to impose sanctions under this section shall not include the authority or a requirement to impose sanctions on the importation of goods.\n**(B) Good defined**\nIn this paragraph, the term good means any article, natural or manmade substance, material, supply, or manufactured product, including inspection and test equipment, and excluding technical data.\n**(2) Exception to comply with international obligations and law enforcement activities**\nSanctions under subsection (b)(2) shall not apply with respect to an alien if admitting or paroling the alien into the United States is necessary\u2014\n**(A)**\nto permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations; or\n**(B)**\nto carry out or assist authorized law enforcement activity in the United States.\n##### (d) Waiver\n**(1) In general**\nThe President may, on a case-by-case basis for a period of not more than 180 days, waive the application of sanctions imposed with respect to a foreign person under this section if the President\u2014\n**(A)**\ncertifies to the appropriate congressional committees that the waiver is vital to the national interests of the United States; and\n**(B)**\nsubmits with the certification required under subparagraph (A) a detailed justification explaining the reasons for the waiver.\n**(2) Renewal of waiver**\nThe President may, on a case-by-case basis, renew a waiver issued under paragraph (1) for additional periods of not more than 180 days each up to a total of 2 years if the President\u2014\n**(A)**\ndetermines that the renewal of the waiver is vital to the national interests of the United States; and\n**(B)**\nnot less than 15 days before the waiver expires, submits to the appropriate congressional committees a report on the renewal of the waiver that includes\u2014\n**(i)**\na justification for the renewal of the waiver; and\n**(ii)**\na detailed plan to phase out the need for any such waiver issued with respect to such foreign person.\n**(3) Termination of waiver authority**\nThe authority to issue a waiver under this subsection shall terminate on February 1, 2029.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out subsection (b)(1).\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (b)(1) or any regulation, license, or order issued to carry out that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (f) Rule of construction\nSection 4(a)(3)(A) shall be construed to be consistent with Frequently Asked Questions 398 through 402, published by the Office of Foreign Assets Control on August 11, 2020, and August 13, 2014, or any successors to such frequently asked questions.\n#### 5. Interagency Working Group on Iranian Sanctions\n##### (a) Establishment\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State shall establish a working group to be known as the Interagency Working Group on Iranian Sanctions (referred to in this section as the Working Group ).\n##### (b) Membership\nThe Working Group shall be composed one or more representatives from each of the following:\n**(1)**\nThe Department of State.\n**(2)**\nThe Department of the Treasury.\n**(3)**\nThe Department of Justice.\n**(4)**\nSuch other Federal departments or agencies as the Secretary of State determines appropriate.\n##### (c) Chair\nThe President shall designate a Chair of the Working Group.\n##### (d) Multilateral contact group\n**(1) Establishment**\nThe Working Group shall endeavor to establish a multilateral contact group with like-minded nations to coordinate international efforts to enforce sanctions imposed with respect to the Islamic Republic of Iran.\n**(2) Duties**\nThe multilateral contact group shall\u2014\n**(A)**\nshare information on evolving sanctions frameworks to identify areas of difference or enforcement gaps;\n**(B)**\nshare information on newly-designated entities,\n**(C)**\nraise awareness of new sanctions evasion practices; and\n**(D)**\ncoordinate on new measures to curb Iranian malign activity, including uranium enrichment activities, ballistic missile production, and support for terrorism.\n#### 6. Private sector reporting on persons engaged in sanctionable activities or sanctions evasion\nSection 36(b) of the State Department Basic Authorities Act of 1956 ( 22 U.S.C. 2708(b) ) is amended\u2014\n**(1)**\nin paragraph (13), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (14), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following paragraph:\n(15) the identification a person described in section 4(a) of the Enhanced Iran Sanctions Act of 2025 or any person that has attempted or is attempting to evade sanctions imposed under such Act with proceeds generated by the sale of intercepted oil, gas, liquefied natural gas, petrochemical products, or related products from the Islamic Republic of Iran. .",
      "versionDate": "2025-02-12",
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
        "actionDate": "2026-01-12",
        "text": "Motion to place bill on Consensus Calendar filed by Mr. Lawler."
      },
      "number": "1422",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Enhanced Iran Sanctions Act of 2025",
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
        "name": "International Affairs",
        "updateDate": "2025-05-07T16:19:28Z"
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
      "date": "2025-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s556is.xml"
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
      "title": "Enhanced Iran Sanctions Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Enhanced Iran Sanctions Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to impose sanctions with respect to persons engaged in logistical transactions and sanctions evasion relating to oil, gas, liquefied natural gas, and related petrochemical products from the Islamic Republic of Iran, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:33:34Z"
    }
  ]
}
```
