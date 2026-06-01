# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1456?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1456
- Title: Gun Trafficker Detection Act
- Congress: 119
- Bill type: HR
- Bill number: 1456
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-02-03T23:12:18Z
- Update date including text: 2026-02-03T23:12:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1456",
    "number": "1456",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Gun Trafficker Detection Act",
    "type": "HR",
    "updateDate": "2026-02-03T23:12:18Z",
    "updateDateIncludingText": "2026-02-03T23:12:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:36:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "K000385",
      "district": "2",
      "firstName": "Robin",
      "fullName": "Rep. Kelly, Robin L. [D-IL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
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
      "sponsorshipDate": "2025-02-21",
      "state": "DC"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "RI"
    },
    {
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
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
      "sponsorshipDate": "2025-02-21",
      "state": "NY"
    },
    {
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "OH"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NC"
    },
    {
      "bioguideId": "D000617",
      "district": "1",
      "firstName": "Suzan",
      "fullName": "Rep. DelBene, Suzan K. [D-WA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "DelBene",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "WA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "IL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MI"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "PA"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NJ"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "MA"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "True",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "A000148",
      "district": "4",
      "firstName": "Jake",
      "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Auchincloss",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MA"
    },
    {
      "bioguideId": "T000482",
      "district": "3",
      "firstName": "Lori",
      "fullName": "Rep. Trahan, Lori [D-MA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Trahan",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "MA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1456ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1456\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Casten (for himself, Ms. Kelly of Illinois , Ms. Norton , Mr. Magaziner , Mrs. McIver , Ms. Titus , Ms. Vel\u00e1zquez , Ms. Clarke of New York , Mr. Goldman of New York , Ms. Brown , Mrs. Foushee , Ms. DelBene , Ms. Scanlon , Mr. Krishnamoorthi , Mr. Thanedar , Mr. Evans of Pennsylvania , Mrs. Watson Coleman , Mr. Moulton , and Mr. Min ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo require lost or stolen firearms to be reported to law enforcement authorities within 48 hours, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gun Trafficker Detection Act .\n#### 2. Reporting of lost or stolen firearms to law enforcement authorities\n##### (a) Reporting requirement\n**(1) In general**\nSection 922 of title 18, United States Code, is amended by adding at the end the following:\n(aa) (1) Within 48 hours after a person not licensed under this chapter who owns a firearm that has been shipped or transported in, or has been possessed in or affecting, interstate or foreign commerce, discovers or reasonably should have discovered the theft or loss of the firearm, the person shall report the theft or loss to the Attorney General. If the report to the Attorney General is not submitted through a web portal created by the Attorney General for such purpose, the person shall report the theft or loss to local law enforcement authorities. (2) Within 72 hours after the Attorney General receives a report through the web portal pursuant to paragraph (1), the Attorney General shall notify the chief law enforcement officer of the jurisdiction in which the theft or loss occurred of the name and address of the reporting person. .\n**(2) Reporting**\n**(A) Creation of web-based portal**\nWithin 180 days after the date of the enactment of this Act, the Attorney General shall create a web-based electronic portal, which members of the public may use to report the theft or loss of a firearm to the Attorney General pursuant to section 922(aa) of title 18, United States Code, that includes a notice to users of the penalties under section 924(a)(1) of such title for knowingly making a false statement or representation in such a report.\n**(B) Use of funds requirements**\nSection 502(a) of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10153(a) ) is amended by adding at the end the following:\n(7) An assurance that, for each fiscal year covered by an application, the applicant will use not less than 5 percent of the total amount of the grant award for the fiscal year to study and implement effective management and collection of data relating to lost or stolen firearms reported to a law enforcement agency of the applicant under section 922(aa) of title 18, United States Code, unless the applicant has ensured, and the Attorney General has certified, that the applicant has in effect such laws and procedures as are necessary to ensure that each such report is forwarded to the National Crime Information Center. .\n**(3) Penalties**\nSection 924 of title 18, United States Code, is amended by adding at the end the following:\n(q) With respect to a violation of section 922(aa), the Attorney General shall, after notice and opportunity for a hearing\u2014 (1) (A) in the case of a first violation, subject the person to a civil money penalty of not more than $1,000; or (B) in the case of a second or subsequent violation, subject the person to a civil money penalty of not more than $5,000; and (2) in the case of any violation, notify the person of the prohibitions set forth in section 922(bb). .\n##### (b) Prohibition on firearm receipt after multiple convictions\n**(1) In general**\nSection 922 of title 18, United States Code, as amended by subsection (a)(1) of this section, is amended by adding at the end the following:\n(bb) (1) It shall be unlawful for a person who has been twice assessed a civil money penalty under section 924(q) to receive a firearm during the 1-year period that begins with the date of the most recent such assessment. (2) It shall be unlawful for a person who has been thrice assessed a civil money penalty under section 924(q) to receive a firearm during the 5-year period that begins with the date of the most recent such assessment. .\n**(2) Penalties**\nSection 924(a)(5) of title 18, United States Code, is amended by striking or (t) and inserting (t), or (bb) .\n##### (c) Prohibition on false reporting\nSection 924(a)(1)(A) of title 18, United States Code, is amended by striking chapter or and inserting chapter, in reporting a lost or stolen firearm pursuant to section 922(aa), or .\n##### (d) Updating of national instant criminal background check system\n**(1) In general**\nWithin 6 months after the date of the enactment of this Act, the Attorney General shall promulgate such rules as are necessary to ensure that\u2014\n**(A)**\nthe national instant criminal background check system takes account of section 922(bb) of title 18, United States Code, in performing the functions of the system; and\n**(B)**\nall persons licensed under chapter 44 of such title provide notice of the penalties for violations of section 922(aa) of such title to any person not so licensed who acquires a firearm from the licensee.\n**(2) Conforming amendments**\n**(A)**\nThe following provisions of section 103 of the Brady Handgun Violence Prevention Act ( 34 U.S.C. 40901 ) are each amended by striking (g) or (n) and inserting (g), (n), or (bb) :\n**(i)**\nSubparagraphs (A), (C), (F)(iii)(I), and (G)(i) of subsection (e)(1).\n**(ii)**\nSubsection (g).\n**(iii)**\nSubsection (i)(2).\n**(iv)**\nSubsection (l)(3)(B).\n**(B)**\nThe following provisions of title 18, United States Code, are each amended by striking (g) or (n) and inserting (g), (n), or (bb) :\n**(i)**\nSubparagraphs (B)(ii) and (C)(iii)(II) of section 922(t)(1).\n**(ii)**\nSection 923(g)(3)(B).\n**(iii)**\nSection 925A(2).\n**(C)**\nParagraphs (2), (4), and (5) of section 922(t) of title 18, United States Code, are each amended by striking (g), or (n) and inserting (g), (n), or (bb) .\n#### 3. Effective date\nThis Act and the amendments made by this Act shall take effect 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-02-21",
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
            "updateDate": "2025-07-14T15:22:41Z"
          },
          {
            "name": "Crimes against property",
            "updateDate": "2025-07-14T15:22:57Z"
          },
          {
            "name": "Criminal justice information and records",
            "updateDate": "2025-07-14T15:23:07Z"
          },
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-07-14T15:22:36Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-07-14T15:23:02Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-14T15:22:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-18T14:53:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-21",
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
          "measure-id": "id119hr1456",
          "measure-number": "1456",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-21",
          "originChamber": "HOUSE",
          "update-date": "2026-02-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1456v00",
            "update-date": "2026-02-03"
          },
          "action-date": "2025-02-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Gun Trafficker Detection Act</strong></p><p>This bill requires individual gun owners to report lost or stolen firearms to law enforcement.</p><p>Specifically, the bill requires gun owners to report a lost or stolen firearm to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) or local law enforcement within 48 hours of discovery. A gun owner who fails to report a lost or stolen firearm is subject to a civil penalty of up to $1,000 for the first violation; a civil penalty of up to $5,000 and a one-year prohibition on receiving a firearm for the second violation; and a civil penalty of up to $5,000 and a five-year prohibition on receiving a firearm for the third or subsequent violation. Further, a gun owner who receives a firearm while subject to a one-year or five-year prohibition on such receipt is subject to criminal penalties\u2014a fine, a prison term of up to one year, or both.\u00a0</p><p>Additionally, the bill prohibits making false statements or misrepresentations with respect to the information required in a report of a lost or stolen firearm. A violation is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.\u00a0</p><p>The bill directs the ATF to create a web-based portal where individuals can report lost or stolen firearms. It also requires states to use at least 5% of funds under the Edward Byrne Memorial Justice Assistance Grant program to collect and manage data about lost or stolen firearms reported to local law enforcement.\u00a0</p>"
        },
        "title": "Gun Trafficker Detection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1456.xml",
    "summary": {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gun Trafficker Detection Act</strong></p><p>This bill requires individual gun owners to report lost or stolen firearms to law enforcement.</p><p>Specifically, the bill requires gun owners to report a lost or stolen firearm to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) or local law enforcement within 48 hours of discovery. A gun owner who fails to report a lost or stolen firearm is subject to a civil penalty of up to $1,000 for the first violation; a civil penalty of up to $5,000 and a one-year prohibition on receiving a firearm for the second violation; and a civil penalty of up to $5,000 and a five-year prohibition on receiving a firearm for the third or subsequent violation. Further, a gun owner who receives a firearm while subject to a one-year or five-year prohibition on such receipt is subject to criminal penalties\u2014a fine, a prison term of up to one year, or both.\u00a0</p><p>Additionally, the bill prohibits making false statements or misrepresentations with respect to the information required in a report of a lost or stolen firearm. A violation is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.\u00a0</p><p>The bill directs the ATF to create a web-based portal where individuals can report lost or stolen firearms. It also requires states to use at least 5% of funds under the Edward Byrne Memorial Justice Assistance Grant program to collect and manage data about lost or stolen firearms reported to local law enforcement.\u00a0</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr1456"
    },
    "title": "Gun Trafficker Detection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Gun Trafficker Detection Act</strong></p><p>This bill requires individual gun owners to report lost or stolen firearms to law enforcement.</p><p>Specifically, the bill requires gun owners to report a lost or stolen firearm to the Bureau of Alcohol, Tobacco, Firearms and Explosives (ATF) or local law enforcement within 48 hours of discovery. A gun owner who fails to report a lost or stolen firearm is subject to a civil penalty of up to $1,000 for the first violation; a civil penalty of up to $5,000 and a one-year prohibition on receiving a firearm for the second violation; and a civil penalty of up to $5,000 and a five-year prohibition on receiving a firearm for the third or subsequent violation. Further, a gun owner who receives a firearm while subject to a one-year or five-year prohibition on such receipt is subject to criminal penalties\u2014a fine, a prison term of up to one year, or both.\u00a0</p><p>Additionally, the bill prohibits making false statements or misrepresentations with respect to the information required in a report of a lost or stolen firearm. A violation is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.\u00a0</p><p>The bill directs the ATF to create a web-based portal where individuals can report lost or stolen firearms. It also requires states to use at least 5% of funds under the Edward Byrne Memorial Justice Assistance Grant program to collect and manage data about lost or stolen firearms reported to local law enforcement.\u00a0</p>",
      "updateDate": "2026-02-03",
      "versionCode": "id119hr1456"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1456ih.xml"
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
      "title": "Gun Trafficker Detection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gun Trafficker Detection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require lost or stolen firearms to be reported to law enforcement authorities within 48 hours, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:52Z"
    }
  ]
}
```
