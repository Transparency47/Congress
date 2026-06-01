# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/476
- Title: No Russian Tunnel to Crimea Act
- Congress: 119
- Bill type: HR
- Bill number: 476
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-05-20T14:15:52Z
- Update date including text: 2026-05-20T14:15:52Z
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/476",
    "number": "476",
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
    "title": "No Russian Tunnel to Crimea Act",
    "type": "HR",
    "updateDate": "2026-05-20T14:15:52Z",
    "updateDateIncludingText": "2026-05-20T14:15:52Z"
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
          "date": "2025-01-16T14:10:40Z",
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
          "date": "2025-01-16T14:10:35Z",
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SC"
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
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "NJ"
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
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr476ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 476\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Meeks (for himself, Mr. Connolly , Mr. Wilson of South Carolina , Mr. Amo , Mr. Keating , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the imposition of sanctions with respect to any foreign person who knowingly participates in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean peninsula.\n#### 1. Short title\nThis Act may be cited as the No Russian Tunnel to Crimea Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nIn February and March 2014, the Russian Federation invaded the Crimean peninsula and annexed Crimea, internationally recognized as Ukrainian territory.\n**(2)**\nFollowing its annexation of Crimea, the Russian Federation constructed the Kerch Strait Bridge to connect the Russian mainland with the Crimean peninsula.\n**(3)**\nOn February 24, 2022, the Government of the Russian Federation, led by Vladimir Putin, launched an unprovoked, full-scale invasion of Ukraine.\n**(4)**\nThe Russian Federation has used Crimea as an integral part of its full scale invasion of Ukraine, including to house Russian troops, store ammunition and weapons, and host the Black Sea Fleet.\n**(5)**\nIn October 2023, it was publicly reported that Russian and Chinese business officials met and exchanged emails to discuss building a tunnel from the Russian mainland to illegally occupied Crimea.\n#### 3. Sanctions\n##### (a) In general\nThe President shall impose sanctions described in subsection (b) with respect to any foreign person who knowingly participates in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean peninsula.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Asset blocking**\nNotwithstanding the requirements of section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President may exercise of all powers granted to the President by that Act to the extent necessary to block and prohibit all transactions in all property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Visas, admission, or parole**\n**(A) In general**\nAn alien who the Secretary of State or the Secretary of Homeland Security (or a designee of one of such Secretaries) knows, or has reason to believe, is described in subsection (a) is\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible for a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe issuing consular officer, the Secretary of State, or the Secretary of Homeland Security (or a designee of one of such Secretaries) shall, in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ), revoke any visa or other entry documentation issued to an alien described in subparagraph (A) regardless of when the visa or other entry documentation is issued.\n**(ii) Effect of revocation**\nA revocation under clause (i)\u2014\n**(I)**\nshall take effect immediately; and\n**(II)**\nshall automatically cancel any other valid visa or entry documentation that is in the alien\u2019s possession.\n##### (c) Exceptions\n**(1) Exception to comply with international obligations**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien if admitting or paroling the alien into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(2) Exception relating to the provision of humanitarian assistance**\nSanctions under this section may not be imposed with respect to transactions or the facilitation of transactions for\u2014\n**(A)**\nthe sale of agricultural commodities, food, medicine, or medical devices;\n**(B)**\nthe provision of humanitarian assistance;\n**(C)**\nfinancial transactions relating to humanitarian assistance; or\n**(D)**\ntransporting goods or services that are necessary to carry out operations relating to humanitarian assistance.\n**(3) Exception for intelligence, law enforcement, and national security activities**\nSanctions under this section shall not apply to any authorized intelligence, law enforcement, or national security activities of the United States.\n##### (d) Classified information\nIn any judicial review of a determination made under this section, if the determination was based on classified information (as defined in section 1(a) of the Classified Information Procedures Act) such information may be submitted to the reviewing court ex parte and in camera. This subsection does not confer or imply any right to judicial review.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided to the President under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties provided for in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to a person that violates, attempts to violate, conspires to violate, or causes a violation of regulations promulgated to carry out this section to the same extent that such penalties apply to a person who commits an unlawful act described in section 206(a) of that Act.\n##### (f) Waiver\nThe President may waive the application of sanctions imposed with respect to a foreign person under this section if the President certifies to the appropriate congressional committees not later than 15 days before such waiver is to take effect that the waiver is important to the national security interests of the United States.\n##### (g) Definitions\nIn this section\u2014\n**(1)**\nthe term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate;\n**(2)**\nthe term foreign person means an individual or entity that is not a United States person; and\n**(3)**\nthe term United States person means\u2014\n**(A)**\na United States citizen;\n**(B)**\na permanent resident alien of the United States;\n**(C)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(D)**\na person in the United States.",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2026-05-20T14:15:52Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2025-05-14T13:32:54Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-05-14T13:32:54Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-04-17T16:34:37Z"
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
          "measure-id": "id119hr476",
          "measure-number": "476",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr476v00",
            "update-date": "2025-04-23"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Russian Tunnel to Crimea Act</strong><br/>\u00a0<br/>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons that knowingly participate in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean Peninsula.<br/>\u00a0<br/>The bill provides exceptions to these sanctions in certain circumstances (such as providing humanitarian assistance or to comply with international obligations). The President may also waive such sanctions on the basis of U.S. national security interests.</p>"
        },
        "title": "No Russian Tunnel to Crimea Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr476.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Russian Tunnel to Crimea Act</strong><br/>\u00a0<br/>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons that knowingly participate in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean Peninsula.<br/>\u00a0<br/>The bill provides exceptions to these sanctions in certain circumstances (such as providing humanitarian assistance or to comply with international obligations). The President may also waive such sanctions on the basis of U.S. national security interests.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr476"
    },
    "title": "No Russian Tunnel to Crimea Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Russian Tunnel to Crimea Act</strong><br/>\u00a0<br/>This bill requires the President to impose visa- and property-blocking sanctions on foreign persons that knowingly participate in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean Peninsula.<br/>\u00a0<br/>The bill provides exceptions to these sanctions in certain circumstances (such as providing humanitarian assistance or to comply with international obligations). The President may also waive such sanctions on the basis of U.S. national security interests.</p>",
      "updateDate": "2025-04-23",
      "versionCode": "id119hr476"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr476ih.xml"
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
      "title": "No Russian Tunnel to Crimea Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-09T08:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Russian Tunnel to Crimea Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-09T08:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the imposition of sanctions with respect to any foreign person who knowingly participates in the construction, maintenance, or repair of a tunnel or bridge that connects the Russian mainland with the Crimean peninsula.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-09T08:48:23Z"
    }
  ]
}
```
