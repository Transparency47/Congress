# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7540?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7540
- Title: United States-Israel FUTURES Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7540
- Origin chamber: House
- Introduced date: 2026-02-12
- Update date: 2026-05-20T08:08:41Z
- Update date including text: 2026-05-20T08:08:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-12: Introduced in House

## Actions

- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Introduced in House
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-12 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7540",
    "number": "7540",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "United States-Israel FUTURES Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:41Z",
    "updateDateIncludingText": "2026-05-20T08:08:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T14:06:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-12T14:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "NC"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NJ"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "IN"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig A. [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "B001282",
      "district": "6",
      "firstName": "Andy",
      "fullName": "Rep. Barr, Andy [R-KY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Barr",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "KY"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "NJ"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "FL"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2026-02-25",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NJ"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "NJ"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "CA"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "F000472",
      "district": "18",
      "firstName": "Scott",
      "fullName": "Rep. Franklin, Scott [R-FL-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Franklin",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TN"
    },
    {
      "bioguideId": "M000194",
      "district": "1",
      "firstName": "Nancy",
      "fullName": "Rep. Mace, Nancy [R-SC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mace",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "SC"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "MN"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "WI"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "FL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "IL"
    },
    {
      "bioguideId": "P000048",
      "district": "11",
      "firstName": "August",
      "fullName": "Rep. Pfluger, August [R-TX-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Pfluger",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "TX"
    },
    {
      "bioguideId": "E000235",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Ezell, Mike [R-MS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ezell",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MS"
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
      "sponsorshipDate": "2026-03-12",
      "state": "VA"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "MI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-12",
      "state": "NY"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2026-03-12",
      "state": "AL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NY"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2026-03-25",
      "state": "NE"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "H001067",
      "district": "9",
      "firstName": "Richard",
      "fullName": "Rep. Hudson, Richard [R-NC-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Hudson",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "NC"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "WV"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "KS"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "IA"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "TN"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "NC"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "TX"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "TN"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7540ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7540\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 12, 2026 Mr. Jackson of Texas (for himself and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Foreign Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo enhance bilateral defense cooperation between the United States and Israel, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the United States-Israel Framework for Upgraded Technologies, Unified Research, and Enhanced Security Act of 2026 or the United States-Israel FUTURES Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States and Israel\u2014\n**(A)**\nare bound by shared democratic values, strategic interests, and deep cultural and technological ties; and\n**(B)**\ncan benefit from further joint innovation and rapid technology deployment in facing common and evolving security challenges;\n**(2)**\nIsrael is a strategic and capable ally of the United States that advances United States strategic interests, strengthens United States military capabilities, and bolsters the United States economy;\n**(3)**\nas a global leader and innovator in the development of defense technology, Israel is a close foreign defense partner of the United States;\n**(4)**\non September 14, 2016, the United States and Israel signed a 10-year memorandum of understanding reaffirming the importance of continuing annual United States military assistance to Israel and cooperative missile defense programs in a way that enhances the security and bilateral relationship between the two countries;\n**(5)**\nthe United States-Israel defense partnership, through sustained joint research and development, has yielded critical advances in both countries\u2019 national security capabilities in areas such as missile defense, directed energy, counter drone, anti-tunneling, counterterrorism, and emerging technologies;\n**(6)**\nto maintain Israel\u2019s qualitative military edge while deterring adversaries and ensuring mutual security, the United States and Israel must expand cooperation in emerging domains; and\n**(7)**\nto grow American technological supremacy, the United States must leverage the unique capabilities offered by each country and more rapidly integrate jointly developed and Israeli-origin defense technologies into United States military systems, programs of record, and the defense industrial base.\n#### 3. Establishment of the United States-Israel Defense Technology Cooperation Initiative\n##### (a) Establishment\nThe Secretary of Defense, with the concurrence of the Minister of Defense of Israel, shall establish a cooperative initiative, to be known as the United States-Israel Defense Technology Cooperation Initiative , to expand and accelerate bilateral defense technology research, development, testing, evaluation, integration, and industrial cooperation by\u2014\n**(1)**\nidentifying jointly developed or Israeli-origin technologies with operational utility for integration into United States systems and programs of record;\n**(2)**\nconducting collaborative research initiatives involving government, private sector, and academic institutions in the United States and Israel, in a manner that protects sensitive technology and information and the national security interests of the United States and Israel;\n**(3)**\nfacilitating the transition of technologies from research and development into procurement and acquisition pathways;\n**(4)**\nestablishing frameworks for joint ventures, licensing agreements, and United States-based co-production or manufacturing partnerships with Israeli industry;\n**(5)**\ncoordinating with relevant Department of Defense components, including the Irregular Warfare Technical Support Directorate, capability development and innovation divisions, the Defense Innovation Unit, the United States-Israel Operations Technology Working Group, the Defense Advanced Research Projects Agency, the Missile Defense Agency and United States Space Command, and the military services, to align efforts and avoid duplication; and\n**(6)**\npromoting joint training exercises and information-sharing mechanisms to enhance operational readiness to deploy jointly developed technologies.\n##### (b) Initiative domains\nThe Initiative shall be carried out through cooperative efforts in domains such as the following:\n**(1)**\nCounter-Unmanned Systems including aerial, maritime, and ground platforms.\n**(2)**\nAnti-tunneling and subterranean threats.\n**(3)**\nMissile and air defense technologies, including Golden Dome for America.\n**(4)**\nArtificial intelligence, quantum, machine learning, and autonomous systems.\n**(5)**\nDirected energy and advanced sensing.\n**(6)**\nCyber defense, electronic warfare, and digital resilience.\n**(7)**\nBiotechnology, biomanufacturing, and medical defense.\n**(8)**\nNetwork integration, data fusion, and contested logistics.\n**(9)**\nDefense industrial base cooperation, manufacturing, and co-production.\n**(10)**\nOther emerging technologies as jointly agreed by the United States and Israel.\n##### (c) Activities in coordination with other Federal departments and agencies\nThe Secretary of Defense shall coordinate activities under the Initiative with the Secretary of State, the Secretary of Commerce, and the heads of other relevant Federal departments and agencies, to ensure consistency with existing laws and regulations.\n#### 4. Reporting\n##### (a) Interim progress update\nNot later than 180 days after the date of enactment of this Act, the Secretary of Defense shall provide to the congressional defense committees an interim briefing or written update describing\u2014\n**(1)**\nsteps taken to stand up the initiative;\n**(2)**\nearly coordination with Israeli counterparts;\n**(3)**\ninitial technology areas identified for accelerated cooperation and technologies with operational utility for integration into United States systems and programs of record;\n**(4)**\nDepartment of Defense components designated to lead implementation; and\n**(5)**\nany early transition, prototyping, or integration activities initiated during the period covered by the update.\n##### (b) Annual report\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Secretary of Defense shall submit to the congressional defense committees a report on implementation of the program established under this section. Each such report shall include\u2014\n**(1)**\na description of activities conducted under the program;\n**(2)**\nan assessment of progress made in advancing shared national security interests;\n**(3)**\nan assessment of the program\u2019s collaboration with other relevant Federal programs, including the United States-Israel operations-technology working group and United States-Israel cooperative programs run by the capability development and innovation division and the irregular warfare technical support directorate;\n**(4)**\na description of technologies transitioned into United States acquisition programs or fielded systems;\n**(5)**\na description of partnerships established with United States and Israeli industry; and\n**(6)**\nrecommendations for future priorities and assessment of resource needs, including further authorities necessary to promote the long-term integration of joint capabilities between the United States and Israel.\n##### (c) Form\nEach report required under subsection (b) shall be submitted in unclassified form but may include a classified annex.\n##### (d) Public transparency\nThe Secretary of Defense shall make available on a publicly accessible website of the Department of Defense periodic, unclassified updates, to the maximum extent practicable, on activities conducted under the Initiative, including a description of how these activities contribute to American technological and military supremacy. Such updates shall be made in a manner that ensures that classified information or other information that would compromise operational security, export controls, or sensitive technology are not released.\n##### (e) Congressional defense committees defined\nIn this Act, the term congressional defense committees means the Committees on Appropriations and Armed Services of the House of Representatives and of the Senate.\n#### 5. Authorization of appropriations\nThere is authorized to be appropriated $150,000,000 for each of fiscal years 2027 through 2029 to carry out this Act.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "3855",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United States-Israel Framework for Upgraded Technologies, Unified Research, and Enhanced Security (FUTURES) Act of 2026",
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
        "name": "International Affairs",
        "updateDate": "2026-03-09T22:52:32Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7540ih.xml"
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
      "title": "United States-Israel FUTURES Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "United States-Israel Framework for Upgraded Technologies, Unified Research, and Enhanced Security Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "title": "United States-Israel FUTURES Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-07T04:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance bilateral defense cooperation between the United States and Israel, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-07T04:18:29Z"
    }
  ]
}
```
