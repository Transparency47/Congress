# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7094?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7094
- Title: No Aid for Russian Energy Act
- Congress: 119
- Bill type: HR
- Bill number: 7094
- Origin chamber: House
- Introduced date: 2026-01-15
- Update date: 2026-03-26T08:06:30Z
- Update date including text: 2026-03-26T08:06:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-15: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-01-15: Introduced in House

## Actions

- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Introduced in House
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-01-15 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-15",
    "latestAction": {
      "actionDate": "2026-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7094",
    "number": "7094",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "D000399",
        "district": "37",
        "firstName": "Lloyd",
        "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
        "lastName": "Doggett",
        "party": "D",
        "state": "TX"
      }
    ],
    "title": "No Aid for Russian Energy Act",
    "type": "HR",
    "updateDate": "2026-03-26T08:06:30Z",
    "updateDateIncludingText": "2026-03-26T08:06:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-15",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-15",
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
          "date": "2026-01-15T14:05:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-01-15T14:05:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NE"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-15",
      "state": "NJ"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "DC"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2026-01-15",
      "state": "IL"
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
      "sponsorshipDate": "2026-01-22",
      "state": "NC"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "OH"
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
      "sponsorshipDate": "2026-02-09",
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
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-03-25",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7094ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7094\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2026 Mr. Doggett (for himself, Mr. Bacon , Mr. Bilirakis , Mr. Cohen , Mr. Fitzpatrick , Mr. Goldman of New York , Mr. Kean , Ms. Norton , and Mr. Quigley ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo prohibit United States persons from providing petroleum equipment or services in the energy sector of the Russian Federation.\n#### 1. Short title\nThis Act may be cited as the No Aid for Russian Energy Act .\n#### 2. Prohibition\n##### (a) In general\nThe President shall prohibit the exportation, reexportation, sale, or supply, directly or indirectly, from the United States, or by a United States person, wherever located, of petroleum equipment and services to any person located in the Russian Federation.\n##### (b) Liability of parent companies for violations of sanctions by foreign subsidiaries\nExcept as provided in subsection (c), not later than 60 days after the date of the enactment of this Act, the President shall prohibit any entity owned or controlled by a United States person and established or maintained outside the United States from knowingly engaging directly or indirectly in any transaction described in subsection (a) that would be prohibited by an order or regulation issued pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) if the transaction were engaged in by a United States person or in the United States.\n##### (c) Exception\nThe prohibitions in subsections (a) and (b) shall not apply with respect to petroleum equipment and services directly related to isotopes derived from petroleum manufacturing that are used for medical, agricultural, or environmental purposes, such as Carbon-13.\n#### 3. Sanctions\n##### (a) In general\nThe President shall impose the sanctions described in subsection (b) on any foreign person that directly or indirectly engages in the exportation, reexportation, sale, or supply, of petroleum equipment and services to any person located in the Russian Federation.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President shall exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a), or is a corporate officer or principal shareholder with a controlling interest in a foreign person described in subsection (a), is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subparagraph (A) regardless of when the visa or other entry documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n#### 4. Administrative measures\n##### (a) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this Act.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out this Act to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (b) Waiver\nThe President may waive the application of sanctions imposed with respect to a United States person or a foreign person (as the case may be) under this section for periods not to exceed 180 days if the President certifies to the appropriate congressional committees not later than 15 days before such waiver is to take effect that the waiver is vital to the national security interests of the United States and includes a description of the specific national security rationale therefor in the certification.\n##### (c) Regulatory authority\n**(1) In general**\nThe President shall, not later than 180 days after the date of the enactment of this Act, prescribe regulations as necessary for the implementation of this Act.\n**(2) Application of certain regulations**\nPursuant to paragraph (1), any regulations that the President prescribes necessary for the implementation of section 3 of this Act shall amend part 587 of title 31, Code of Federal Regulations\n#### 5. Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs and the Committee on the Judiciary of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations and the Committee on the Judiciary of the Senate;\n**(2)**\nthe term foreign person means an individual or entity (as such term is defined in section 587.303 of title 31, Code of Federal Regulations) that is not a United States person;\n**(3)**\nthe term petroleum equipment and services includes\u2014\n**(A)**\nequipment, equipment parts, software and services related to the exploration and production of oil, oil condensates and natural gas; and\n**(B)**\nwith respect to equipment and services described in subparagraph (A)\u2014\n**(i)**\nsoftware support and updates or software packages or applications;\n**(ii)**\ncommercial provision of access to data systems and software packages wherever located, including cloud-based data and software, for the purposes of supporting exploration and production of oil, oil condensates and natural gas;\n**(iii)**\ncommercial arrangements that enable the manufacturing or development of equipment or software under licensing or similar arrangements; and\n**(iv)**\nengineering and consulting services, including\u2014\n**(I)**\nprocess optimization, efficiency improvements, and production planning for petroleum operations;\n**(II)**\noperational guidance and best-practice consultation;\n**(III)**\nfeasibility studies and technical assessments for exploration or production activities; and\n**(IV)**\ncapacity building and training in petroleum sector methodologies; and\n**(v)**\ntechnology transfer and intellectual property licensing, including\u2014\n**(I)**\nlicensing of patents, trademarks, trade secrets, and intellectual property used in petroleum operations;\n**(II)**\nsoftware licensing arrangements enabling proprietary technology use in Russian petroleum operations;\n**(III)**\ncommercial arrangements enabling manufacturing or development of equipment or software under licensing or similar arrangements; and\n**(IV)**\ntransfer of know-how and confidential technical information related to petroleum operations; and\n**(4)**\nthe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States;\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(D)**\na person in the United States.",
      "versionDate": "2026-01-15",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-01-20T15:45:59Z"
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
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7094ih.xml"
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
      "title": "No Aid for Russian Energy Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-16T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Aid for Russian Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-16T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit United States persons from providing petroleum equipment or services in the energy sector of the Russian Federation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T09:18:46Z"
    }
  ]
}
```
