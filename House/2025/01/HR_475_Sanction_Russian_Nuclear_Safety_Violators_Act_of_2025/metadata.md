# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/475?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/475
- Title: Sanction Russian Nuclear Safety Violators Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 475
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-10-22T08:05:45Z
- Update date including text: 2025-10-22T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-16 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/475",
    "number": "475",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Sanction Russian Nuclear Safety Violators Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-22T08:05:45Z",
    "updateDateIncludingText": "2025-10-22T08:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:10:25Z",
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
          "date": "2025-01-16T14:10:20Z",
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
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MA"
    },
    {
      "bioguideId": "C001091",
      "district": "20",
      "firstName": "Joaquin",
      "fullName": "Rep. Castro, Joaquin [D-TX-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Castro",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "C001078",
      "district": "11",
      "firstName": "Gerald",
      "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Connolly",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "VA"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NV"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TN"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "RI"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
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
      "sponsorshipDate": "2025-02-05",
      "state": "IL"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "VA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr475ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 475\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Meeks (for himself, Mr. Keating , Mr. Castro of Texas , Mr. Connolly , Mr. Costa , Ms. Titus , Mr. Cohen , Mr. Amo , Mr. Foster , Mr. Veasey , Mr. Bera , Mr. Krishnamoorthi , Mr. Quigley , and Mr. Boyle of Pennsylvania ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the imposition of sanctions with respect to any foreign person endangering the integrity or safety of the Zaporizhzhia nuclear power plant.\n#### 1. Short title\nThis Act may be cited as the Sanction Russian Nuclear Safety Violators Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nOn February 24, 2022, the Government of the Russian Federation, led by Vladimir Putin, launched an unprovoked, full-scale invasion of Ukraine.\n**(2)**\nRussian forces have illegally occupied the Zaporzhzhia nuclear power plant, the largest nuclear power plant in Europe, and have placed Russian military equipment within the power plant.\n**(3)**\nOfficials from the Russian Federations State Atomic Energy Corporation Rosatom have been present at the plant since March 2022 and have requested information on confidential issues regarding the plant\u2019s operations.\n**(4)**\nThe International Atomic Energy Association IAEA has stated that the presence of Rosatom officials is a significant safety concern and could lead to technical interference in the plant\u2019s operations, and has found that the power plant has structural damage in places due to shelling caused by Russia\u2019s invasion of Ukraine.\n**(5)**\nThe Director General has stated that failing to demilitarize the Zaporizhzhia nuclear power plant is playing with fire .\n**(6)**\nIn May 2023, Russia evacuated citizens from the region around Zaporizhzhia, including personnel who operate the plant, further exacerbating concerns about the plant\u2019s stability and safety.\n#### 3. Sanctions\n##### (a) In general\nThe President shall impose sanctions described in subsection (b) with respect to any foreign person that has endangered the integrity, safety, or undermined Ukrainian operational control of the Zaporizhzhia Nuclear Power Station located in southeastern Ukraine since the Russian Federation launched an unprovoked, full-scale invasion of Ukraine.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subparagraph (A) regardless of when the visa or other entry documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(3) Exception related to ukrainian operational control**\nSanctions under this section shall not apply to any foreign person seeking to reestablish Ukrainian operational control of the Zaporizhzhia Nuclear Power Station or the surrounding region.\n##### (d) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this subtitle.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated under section 403(b) to carry out paragraph (1)(A) to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (e) Waiver\nThe President may waive the application of sanctions imposed with respect to a foreign person under this section if the President certifies to the appropriate congressional committees not later than 15 days before such waiver is to take effect that the waiver is vital to the national security interests of the United States.\n##### (f) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate;\n**(2)**\nthe term foreign person means an individual or entity that is not a United States person;\n**(3)**\nthe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States;\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(D)**\na person in the United States.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Nuclear power",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2025-05-14T13:32:03Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-05-14T13:32:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-02-20T14:22:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr475",
          "measure-number": "475",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr475v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Sanction Russian Nuclear Safety Violators Act of 2025</strong></p><p>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons who endanger the integrity\u00a0or safety\u00a0of the Zaporizhzhia nuclear power plant in southeastern Ukraine or who undermine Ukrainian operational control of the power plant.\u00a0The bill provides certain exceptions\u00a0to such sanctions (1) to comply with international obligations, (2) to provide humanitarian assistance, or (3) for those seeking to reestablish Ukrainian operational control of the Zaporizhzhia nuclear power plant.</p>"
        },
        "title": "Sanction Russian Nuclear Safety Violators Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr475.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sanction Russian Nuclear Safety Violators Act of 2025</strong></p><p>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons who endanger the integrity\u00a0or safety\u00a0of the Zaporizhzhia nuclear power plant in southeastern Ukraine or who undermine Ukrainian operational control of the power plant.\u00a0The bill provides certain exceptions\u00a0to such sanctions (1) to comply with international obligations, (2) to provide humanitarian assistance, or (3) for those seeking to reestablish Ukrainian operational control of the Zaporizhzhia nuclear power plant.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr475"
    },
    "title": "Sanction Russian Nuclear Safety Violators Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Sanction Russian Nuclear Safety Violators Act of 2025</strong></p><p>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons who endanger the integrity\u00a0or safety\u00a0of the Zaporizhzhia nuclear power plant in southeastern Ukraine or who undermine Ukrainian operational control of the power plant.\u00a0The bill provides certain exceptions\u00a0to such sanctions (1) to comply with international obligations, (2) to provide humanitarian assistance, or (3) for those seeking to reestablish Ukrainian operational control of the Zaporizhzhia nuclear power plant.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr475"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr475ih.xml"
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
      "title": "To authorize the imposition of sanctions with respect to any foreign person endangering the integrity or safety of the Zaporizhzhia nuclear power plant.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T09:06:37Z"
    },
    {
      "title": "Sanction Russian Nuclear Safety Violators Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Sanction Russian Nuclear Safety Violators Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T03:08:15Z"
    }
  ]
}
```
