# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/60?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/60
- Title: Knife Owners’ Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 60
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-05T21:40:56Z
- Update date including text: 2025-12-05T21:40:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-03-25 - Committee: Committee Consideration and Mark-up Session Held
- 2025-03-25 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/60",
    "number": "60",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Knife Owners\u2019 Protection Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T21:40:56Z",
    "updateDateIncludingText": "2025-12-05T21:40:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 13 - 10.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
        "item": [
          {
            "date": "2025-03-25T16:27:57Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-03T16:07:20Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "TN"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "AL"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "TX"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
    },
    {
      "bioguideId": "C001132",
      "district": "2",
      "firstName": "Elijah",
      "fullName": "Rep. Crane, Elijah [R-AZ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crane",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr60ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 60\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Ogles ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo protect the right of law-abiding citizens to transport knives interstate, notwithstanding a patchwork of State and local prohibitions that burden citizens.\n#### 1. Short title\nThis Act may be cited as the Knife Owners\u2019 Protection Act of 2025 .\n#### 2. Interstate transportation of knives\n##### (a) Definitions\nAs used in this section\u2014\n**(1)**\nthe term State means any of the 50 States, the District of Columbia, American Samoa, Guam, Puerto Rico, the Northern Mariana Islands, the Virgin Islands of the United States, and any other territory of the United States; and\n**(2)**\nthe term transport \u2014\n**(A)**\nincludes staying in temporary lodging overnight, common carrier misrouting or delays, stops for food, fuel, vehicle maintenance, emergencies, medical treatment, and all other activity related to the overall journey of the individual; and\n**(B)**\ndoes not include any transportation of 1 or more knives with the intent to commit any offense punishable by imprisonment for a term exceeding 1 year involving the use or threatened use of force against another, or with knowledge, or reasonable cause to believe, that such an offense is to be committed in the course of, or arising from, such journey.\n##### (b) Requirements\nNotwithstanding any provision of any law or any rule or regulation of the United States, or of a State or any political subdivision of a State, any individual who is not otherwise prohibited by Federal law from possessing, transporting, shipping, or receiving a knife or knives shall be entitled to transport a knife or knives from any place where the individual may lawfully possess, carry, or transport such a knife or knives to any other place where the individual may lawfully possess, carry, or transport such a knife or knives if\u2014\n**(1)**\nin the case of transportation by motor vehicle, the knife is, or the knives are, not directly accessible from the passenger compartment of the transporting motor vehicle, or, in the case of a motor vehicle without a compartment separate from the passenger compartment, the knife is, or the knives are, contained in a locked container, locked glove compartment, or locked console;\n**(2)**\nin the case of transportation by air, the knife is, or the knives are, contained in a locked container and are not in the passenger cabin of the aircraft; or\n**(3)**\nin the case of transportation by other means (including any conveyance over land, or on or through water), the knife is, or the knives are, contained in a locked container.\n##### (c) Emergency knives\n**(1) In general**\nSubject to paragraph (2), any knife or tool designed for enabling escape in an emergency incorporating a blunt tipped safety blade , a guarded blade, or both, for cutting safety belts\u2014\n**(A)**\nmay be carried in the passenger compartment of a transporting motor vehicle; and\n**(B)**\nshall not be required to be secured in a locked container, locked glove compartment, or locked console.\n**(2) Exception**\nThis subsection shall not apply to the transport of any knife or tool described in paragraph (1) in the passenger cabin of an aircraft the passengers of which are subject to airport screening procedures of the Transportation Security Administration.\n##### (d) Temporary lodging\nSubject to the requirements under subsection (b), a knife or knives may be kept accessible in any form of temporary lodging overnight, as described in subsection (a)(2)(A).\n##### (e) No arrest or detention\nAn individual who is transporting a knife or knives in compliance with this section may not be arrested or otherwise detained for violation of any law or any rule or regulation of a State or any political subdivision of a State related to the possession, transportation, or carrying of knives, unless there is probable cause to believe that the individual is in violation of 1 or more of the requirements under subsection (b).\n##### (f) Claim or defense\n**(1) In general**\nAn individual may assert this section as a claim or defense in any civil or criminal action or proceeding.\n**(2) Burden of proof**\nIf an individual asserts this section as a claim or defense in a criminal proceeding, the relevant State or political subdivision shall bear the burden of proving, beyond a reasonable doubt, that the individual was not in compliance with the requirements under subsection (b).\n##### (g) Right of action\n**(1) In general**\nAny individual who, under color of any statute, ordinance, regulation, custom, or usage, of any State or political subdivision of a State, subjects, or causes to be subjected, any individual to the deprivation of the rights, privileges, or immunities set forth in this section, shall be liable to the individual so deprived in an action at law, suit in equity, or other proper proceeding for redress.\n**(2) Attorney's fees**\nWhen an individual asserts this section as a claim or defense, the court shall award the prevailing party (including any party who receives a favorable resolution through a decision by a court, settlement of a claim, withdrawal of criminal charges, or change of a statute or regulation), other than a State or any political subdivision of a State or its employees or representatives, a reasonable attorney\u2019s fee.\n##### (h) Rule of construction\nNothing in this section shall be construed in any way\u2014\n**(1)**\nto limit any right to possess, carry, or transport a knife or knives under applicable State law; or\n**(2)**\nto impose additional restrictions or requirements on interstate travel by air with a knife or knives.",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-01-30",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "346",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Knife Owners\u2019 Protection Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aviation and airports",
            "updateDate": "2025-02-06T15:16:28Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-02-06T15:16:40Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-02-06T15:16:13Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-02-06T15:16:44Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-02-06T15:16:24Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-06T15:16:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-04T13:04:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr60",
          "measure-number": "60",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-04-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr60v00",
            "update-date": "2025-04-22"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Knife Owners\u2019 Protection Act of 2025</strong></p><p>This bill permits an individual to transport a knife between two places (e.g., states) where knife possession, carry, or transport is legal. The knife must be transported in\u00a0compliance with the bill's\u00a0accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested or detained for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or\u00a0secure storage requirements. An individual may assert compliance with this bill as a claim or defense in any civil or criminal proceeding.</p>"
        },
        "title": "Knife Owners\u2019 Protection Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr60.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Knife Owners\u2019 Protection Act of 2025</strong></p><p>This bill permits an individual to transport a knife between two places (e.g., states) where knife possession, carry, or transport is legal. The knife must be transported in\u00a0compliance with the bill's\u00a0accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested or detained for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or\u00a0secure storage requirements. An individual may assert compliance with this bill as a claim or defense in any civil or criminal proceeding.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr60"
    },
    "title": "Knife Owners\u2019 Protection Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Knife Owners\u2019 Protection Act of 2025</strong></p><p>This bill permits an individual to transport a knife between two places (e.g., states) where knife possession, carry, or transport is legal. The knife must be transported in\u00a0compliance with the bill's\u00a0accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested or detained for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or\u00a0secure storage requirements. An individual may assert compliance with this bill as a claim or defense in any civil or criminal proceeding.</p>",
      "updateDate": "2025-04-22",
      "versionCode": "id119hr60"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr60ih.xml"
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
      "title": "Knife Owners\u2019 Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:33:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Knife Owners\u2019 Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To protect the right of law-abiding citizens to transport knives interstate, notwithstanding a patchwork of State and local prohibitions that burden citizens.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:19Z"
    }
  ]
}
```
