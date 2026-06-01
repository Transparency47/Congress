# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1496
- Title: New Markets for State-Inspected Meat and Poultry Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1496
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-08-15T18:09:15Z
- Update date including text: 2025-08-15T18:09:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1496",
    "number": "1496",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "New Markets for State-Inspected Meat and Poultry Act of 2025",
    "type": "S",
    "updateDate": "2025-08-15T18:09:15Z",
    "updateDateIncludingText": "2025-08-15T18:09:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
        "item": {
          "date": "2025-04-11T02:42:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-04-10",
      "state": "ME"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "MT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MN"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "ND"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WY"
    },
    {
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "SD"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WY"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IA"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1496is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1496\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Rounds (for himself, Mr. King , Mr. Daines , Ms. Smith , Mr. Cramer , Mr. Barrasso , Mr. Thune , Ms. Lummis , Mr. Grassley , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to allow the interstate sale of State-inspected meat and poultry, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the New Markets for State-Inspected Meat and Poultry Act of 2025 .\n#### 2. State-inspected meat\nSection 301 of the Federal Meat Inspection Act ( 21 U.S.C. 661 ) is amended\u2014\n**(1)**\nby striking the section designation and inserting the following:\n301. Sale of inspected meat and meat food products ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking In furtherance of this policy in the matter preceding paragraph (1) and all that follows through (1) The Secretary in paragraph (1) and inserting the following:\n(B) State Programs (i) In general The Secretary ;\n**(B)**\nby striking (a) It is and inserting the following:\n(a) State meat inspection program (1) In general (A) Policy It is ; and\n**(C)**\nin paragraph (1)(B) (as so designated)\u2014\n**(i)**\nin clause (i) (as so designated), by striking solely for distribution within such State and inserting for distribution ; and\n**(ii)**\nby adding at the end the following:\n(ii) Interstate commerce (I) In general Notwithstanding any other provision of this Act, the Secretary may allow the shipment in interstate commerce of carcasses, parts of carcasses, meat, and meat food products inspected under the State meat inspection program described in clause (i). (II) Acceptance of interstate shipments of meat and meat food products Notwithstanding any provision of State law, a State or local government shall not prohibit or restrict the movement or sale of meat or meat food products that have been inspected and passed in accordance with this Act for interstate commerce. ;\n**(3)**\nin subsection (b), by striking (b) The appropriate and inserting the following:\n(b) Cooperation of State agency The appropriate ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nby striking (c)(1) If the Secretary and inserting the following:\n(c) Enforcement of federal requirements (1) Designation of States (A) In general If the Secretary ;\n**(B)**\nin paragraph (1) (as so designated)\u2014\n**(i)**\nin subparagraph (A) (as so designated)\u2014\n**(I)**\nin the first sentence, by striking solely for distribution within such State and inserting for distribution ; and\n**(II)**\nin the second sentence, by striking If the Secretary and inserting the following:\n(B) Designation of States (i) In general Except as provided under clause (ii), if the Secretary ;\n**(ii)**\nin subparagraph (B) (as so designated)\u2014\n**(I)**\nin clause (i) (as so designated)\u2014\n**(aa)**\nin the first sentence, by striking wholly ; and\n**(bb)**\nby striking State; Provided , That if and inserting the following:\nState. (ii) Exception If ; and\n**(II)**\nin clause (ii) (as so designated)\u2014\n**(aa)**\nin the first sentence\u2014\n(AA)\nby striking such designation and inserting a designation made under clause (i) ; and\n(BB)\nby striking he each place it appears and inserting the Secretary ; and\n**(bb)**\nin the second sentence, by striking The Secretary shall and inserting the following:\n(C) Publication of designation The Secretary shall ;\n**(iii)**\nin subparagraph (C) (as so designated)\u2014\n**(I)**\nin the first sentence\u2014\n**(aa)**\nby striking if such ; and\n**(bb)**\nby striking were after transactions ; and\n**(II)**\nin the second sentence, by striking Thereafter, upon request and inserting the following:\n(D) Revocation of designation On request ;\n**(iv)**\nin subparagraph (D) (as so designated)\u2014\n**(I)**\nin the first sentence, by striking such designation and inserting a designation made under subparagraph (B)(i) ; and\n**(II)**\nby striking title IV of this Act: And provided further , That, notwithstanding ; and inserting the following:\ntitle IV. (E) Adulterated meat or meat food product (i) In general Notwithstanding ; and\n**(v)**\nin subparagraph (E) (as so designated)\u2014\n**(I)**\nin clause (i) (as so designated)\u2014\n**(aa)**\nin the first sentence\u2014\n(AA)\nby striking within such State ; and\n(BB)\nby striking section 301 of the Act and inserting this section ; and\n**(bb)**\nin the second sentence, by striking If the State and inserting the following:\n(ii) Enforcement If the State ; and\n**(II)**\nin clause (ii) (as so designated), by striking as though engaged in commerce ;\n**(C)**\nin paragraph (2), by striking (2) The provisions and inserting the following:\n(2) Exceptions to inspection The provisions ;\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nby striking (3) Whenever and inserting the following:\n(3) Termination of designation If ; and\n**(ii)**\nby striking he and inserting the Secretary ; and\n**(E)**\nin paragraph (4), by striking (4) The Secretary and inserting the following:\n(4) Report The Secretary ; and\n**(5)**\nin subsection (d), by striking (d) As used in and inserting the following:\n(d) Definition of State In .\n#### 3. State-inspected poultry products\nSection 5 of the Poultry Products Inspection Act ( 21 U.S.C. 454 ) is amended\u2014\n**(1)**\nby striking the section heading and designation and inserting the following:\n5. Sale of inspected poultry products ;\n**(2)**\nin subsection (a)\u2014\n**(A)**\nby striking In furtherance of this policy in the matter preceding paragraph (1) and all that follows through (1) The Secretary in paragraph (1) and inserting the following:\n(B) State Programs (i) In general The Secretary ;\n**(B)**\nby striking (a) It is and inserting the following:\n(a) State poultry product inspection program (1) In general (A) Policy It is ; and\n**(C)**\nin paragraph (1)(B) (as so designated)\u2014\n**(i)**\nin clause (i) (as so designated), by striking solely for distribution within such State and inserting for distribution ; and\n**(ii)**\nby adding at the end the following:\n(ii) Interstate commerce (I) In general Notwithstanding any other provision of this Act, the Secretary may allow the shipment in interstate commerce of poultry products inspected under the State poultry product inspection program described in clause (i). (II) Acceptance of interstate shipments of poultry products Notwithstanding any provision of State law, a State or local government shall not prohibit or restrict the movement or sale of poultry products that have been inspected and passed in accordance with this Act for interstate commerce. ;\n**(3)**\nin subsection (b), by striking (b) The appropriate and inserting the following:\n(b) Cooperation of State agency The appropriate ;\n**(4)**\nin subsection (c)\u2014\n**(A)**\nby striking (c)(1) If the Secretary and inserting the following:\n(c) Enforcement of federal requirements (1) Designation of States (A) In general If the Secretary ;\n**(B)**\nin paragraph (1) (as so designated)\u2014\n**(i)**\nin subparagraph (A) (as so designated)\u2014\n**(I)**\nin the first sentence, by striking solely for distribution within such State and inserting for distribution ; and\n**(II)**\nin the second sentence, by striking If the Secretary and inserting the following:\n(B) Designation of States (i) In general Except as provided under clause (ii), if the Secretary ;\n**(ii)**\nin subparagraph (B) (as so designated)\u2014\n**(I)**\nin clause (i) (as so designated)\u2014\n**(aa)**\nin the first sentence, by striking wholly ; and\n**(bb)**\nby striking State: Provided , That if and inserting the following:\nState. (ii) Exception If ; and\n**(II)**\nin clause (ii) (as so designated)\u2014\n**(aa)**\nin the first sentence\u2014\n(AA)\nby striking such designation and inserting a designation made under clause (i) ; and\n(BB)\nby striking he each place it appears and inserting the Secretary ; and\n**(bb)**\nin the second sentence, by striking The Secretary shall and inserting the following:\n(C) Publication of designation The Secretary shall ;\n**(iii)**\nin subparagraph (C) (as so designated)\u2014\n**(I)**\nin the first sentence\u2014\n**(aa)**\nby striking if such ; and\n**(bb)**\nby striking were after transactions ; and\n**(II)**\nin the second sentence, by striking However, notwithstanding and inserting the following:\n(D) Adulterated poultry product (i) In general Notwithstanding ; and\n**(iv)**\nin subparagraph (D) (as so designated)\u2014\n**(I)**\nin clause (i) (as so designated)\u2014\n**(aa)**\nin the first sentence\u2014\n(AA)\nby striking within such State ; and\n(BB)\nby striking subparagraph (a)(4) of this section and inserting subsection (a)(4) ; and\n**(bb)**\nin the second sentence, by striking If the State and inserting the following:\n(ii) Enforcement If the State ; and\n**(II)**\nin clause (ii) (as so designated), by striking as though engaged in commerce ;\n**(C)**\nin paragraph (2), by striking (2) The provisions and inserting the following:\n(2) Exceptions to inspection The provisions ;\n**(D)**\nin paragraph (3), by striking (3) Whenever and inserting the following:\n(3) Termination of designation If ; and\n**(E)**\nin paragraph (4), by striking (4) The Secretary and inserting the following:\n(4) Report The Secretary ; and\n**(5)**\nin subsection (d), by striking (d) As used in and inserting the following:\n(d) Definition of State In .",
      "versionDate": "2025-04-10",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-07T13:32:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "Senate",
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
          "measure-id": "id119s1496",
          "measure-number": "1496",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2025-08-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1496v00",
            "update-date": "2025-08-15"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>New Markets for State-Inspected Meat and Poultry Act of</strong><strong> 2025</strong></p><p>This bill allows meat and poultry products inspected by State Meat and Poultry Inspection programs to be sold in interstate commerce. Under the inspection programs, the Department of Agriculture Food Safety and Inspection Service allows states that meet certain requirements to inspect meat and poultry.</p><p>The state-inspected products are currently limited to intrastate commerce, unless a state opts into a separate Cooperative Interstate Shipment Program.</p>"
        },
        "title": "New Markets for State-Inspected Meat and Poultry Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1496.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>New Markets for State-Inspected Meat and Poultry Act of</strong><strong> 2025</strong></p><p>This bill allows meat and poultry products inspected by State Meat and Poultry Inspection programs to be sold in interstate commerce. Under the inspection programs, the Department of Agriculture Food Safety and Inspection Service allows states that meet certain requirements to inspect meat and poultry.</p><p>The state-inspected products are currently limited to intrastate commerce, unless a state opts into a separate Cooperative Interstate Shipment Program.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1496"
    },
    "title": "New Markets for State-Inspected Meat and Poultry Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>New Markets for State-Inspected Meat and Poultry Act of</strong><strong> 2025</strong></p><p>This bill allows meat and poultry products inspected by State Meat and Poultry Inspection programs to be sold in interstate commerce. Under the inspection programs, the Department of Agriculture Food Safety and Inspection Service allows states that meet certain requirements to inspect meat and poultry.</p><p>The state-inspected products are currently limited to intrastate commerce, unless a state opts into a separate Cooperative Interstate Shipment Program.</p>",
      "updateDate": "2025-08-15",
      "versionCode": "id119s1496"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1496is.xml"
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
      "title": "New Markets for State-Inspected Meat and Poultry Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "New Markets for State-Inspected Meat and Poultry Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Meat Inspection Act and the Poultry Products Inspection Act to allow the interstate sale of State-inspected meat and poultry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:24Z"
    }
  ]
}
```
