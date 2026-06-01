# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1092?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1092
- Title: WIPPES Act
- Congress: 119
- Bill type: S
- Bill number: 1092
- Origin chamber: Senate
- Introduced date: 2025-03-24
- Update date: 2026-03-25T11:31:43Z
- Update date including text: 2026-03-25T11:31:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-24: Introduced in Senate
- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-19 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.
- 2025-09-19 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.
- 2025-09-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 166.
- 2026-03-22 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1521-1522; text of amendment in the nature of a substitute: CR S1521-1522)
- 2026-03-22 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:33 - Floor: Received in the House.
- 2026-03-24 14:11:41 - Floor: Held at the desk.
- Latest action: 2025-03-24: Introduced in Senate

## Actions

- 2025-03-24 - IntroReferral: Introduced in Senate
- 2025-03-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-05-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-19 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.
- 2025-09-19 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.
- 2025-09-19 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 166.
- 2026-03-22 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1521-1522; text of amendment in the nature of a substitute: CR S1521-1522)
- 2026-03-22 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2026-03-24 - Floor: Message on Senate action sent to the House.
- 2026-03-24 14:02:33 - Floor: Received in the House.
- 2026-03-24 14:11:41 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-24",
    "latestAction": {
      "actionDate": "2025-03-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1092",
    "number": "1092",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M001176",
        "district": "",
        "firstName": "Jeff",
        "fullName": "Sen. Merkley, Jeff [D-OR]",
        "lastName": "Merkley",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "WIPPES Act",
    "type": "S",
    "updateDate": "2026-03-25T11:31:43Z",
    "updateDateIncludingText": "2026-03-25T11:31:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-03-24",
      "actionTime": "14:11:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-03-24",
      "actionTime": "14:02:33",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-24",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-03-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S1521-1522; text of amendment in the nature of a substitute: CR S1521-1522)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-03-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 166.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-63.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-24",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-24",
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
            "date": "2025-09-19T17:42:01Z",
            "name": "Reported By"
          },
          {
            "date": "2025-05-21T16:03:34Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-24T20:39:14Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "ME"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-24",
      "state": "ME"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "MA"
    },
    {
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "OR"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "NH"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1092is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1092\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Merkley (for himself, Ms. Collins , Mr. Blumenthal , Mr. King , Mr. Markey , Mrs. Murray , Mr. Padilla , Mr. Wyden , and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require certain products to be labeled with \u2018Do Not Flush\u2019 labeling, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act .\n#### 2. Do not flush labeling\n##### (a) In general\nA covered entity shall label a covered product clearly and conspicuously with the label notice and symbol, in accordance with subsections (b) and (c).\n##### (b) Requirements\n**(1) Cylindrical packaging**\nIn the case of a covered product sold in cylindrical or near-cylindrical packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed; or\n**(B)**\nthe symbol shall be displayed on the principal display panel and the label notice, or a combination of the label notice and symbol, shall be displayed on a flip lid in a manner that covers at least 8 percent of the surface area of the flip lid.\n**(2) Flexible film packaging**\nIn the case of a covered product sold in flexible film packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol shall be displayed on the principal display panel and, if the principal display panel is not on the dispensing side of the packaging, on the dispensing side panel; and\n**(B)**\nthe label notice shall be displayed on either the principal display panel or the dispensing side panel, in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(3) Rigid packaging**\nIn the case of a covered product sold in a refillable tub or other rigid packaging that may be reused by a customer, and that is intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(4) Packaging not intended to dispense individual wipes**\nIn the case of a covered product sold in packaging that is not intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user of the covered product.\n**(5) Bulk packaging**\n**(A) In general**\nIn the case of a covered product sold in bulk at retail, the symbol and label notice shall be displayed on both the outer packaging visible at retail and the individual packaging contained within the outer packaging.\n**(B) Exemption**\nThe following shall be exempt from the requirements of subparagraph (A):\n**(i)**\nIndividually packaged covered products that are contained within outer packaging, are not intended to dispense individual wipes, and have no retail labeling.\n**(ii)**\nOuter packaging that does not obscure the symbol and label notice on individually packaged covered products contained within.\n**(6) Packaging of combined products**\n**(A) Outer packaging**\nThe outer packaging of combined products shall be exempt from the symbol and label notice requirements of subsection (a).\n**(B) Packages less than 3 by 3 inches**\nIn the case of a covered product in packaging smaller than 3 inches by 3 inches (such as an individually packaged wipe in tear-top packaging) and sold as part of a combined product, if a symbol and label notice are placed in a prominent location reasonably visible to the user of the covered product, such covered product shall be considered to be labeled clearly and conspicuously.\n##### (c) Reasonable visibility of symbol and label notice\n**(1) In general**\nA covered entity shall ensure that\u2014\n**(A)**\npackaging seams or folds or other packaging design elements do not obscure the symbol or label notice;\n**(B)**\nthe symbol and label notice are each equal in size to at least 2 percent of the surface area of the principal display panel; and\n**(C)**\nthe symbol and label notice have high contrast with the immediate background of the packaging so that such symbol and label notice may be seen and read by an ordinary individual under customary conditions of purchase and use.\n**(2) Proximity of symbol and label notice**\nA covered entity may display a symbol and label notice either adjacent to or on separate areas of the principal display panel.\n**(3) Exception**\nParagraph (1)(C) does not apply to an embossed symbol or label notice on the flip lid of a covered product sold in cylindrical or near-cylindrical packaging.\n##### (d) Representations of flushability\nWith respect to a covered product, a covered entity may not make any express or implied representation that such covered product can or should be flushed.\n##### (e) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or any regulation promulgated under this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this section and any regulations promulgated under this section by the same means, and with the same jurisdiction, powers, and duties, as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section, and any person who violates this section or any regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Regulations**\nThe Commission may promulgate regulations under section 553 of title 5, United States Code, to implement this section. In developing the regulations, the Commission may consult with the Administrator of the Environmental Protection Agency, the Commissioner of Food and Drugs, the Consumer Product Safety Commission, or any other agency as appropriate.\n**(4) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n##### (f) Preemption of State laws\nNo State or political subdivision of a State may directly or indirectly establish or continue in effect, under any authority, requirements with respect to the Do Not Flush labeling of covered products that are not identical to the requirements of this section and the regulations promulgated under this section.\n##### (g) Definitions\nIn this section:\n**(1) Combined product**\nThe term combined product means two or more products sold in shared retail packaging, of which\u2014\n**(A)**\nat least one of the products is a covered product; and\n**(B)**\nat least one of the products is another consumer product intended to be used in combination with such covered product.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\nThe term covered entity means a manufacturer, wholesaler, supplier, individual or group of individuals, or retailer that is responsible for the labeling or retail packaging of a covered product that is sold or offered for retail sale in the United States.\n**(4) Covered product**\n**(A) In general**\nThe term covered product means a premoistened, nonwoven disposable wipe sold or offered for retail sale\u2014\n**(i)**\nthat is marketed as a baby wipe or diapering wipe; or\n**(ii)**\nthat is a household or personal care wipe (including a wipe described in subparagraph (B)) that\u2014\n**(I)**\nis composed entirely, or in part, of petrochemical-derived fibers; and\n**(II)**\nhas significant potential to be flushed.\n**(B) Inclusions**\nThe wipes described in this subparagraph are\u2014\n**(i)**\nantibacterial wipes and disinfecting wipes;\n**(ii)**\nwipes intended for general purpose cleaning or bathroom cleaning, including toilet cleaning and hard surface cleaning; and\n**(iii)**\nwipes intended for personal care use on the body, including hand sanitizing, makeup removal, feminine hygiene, adult hygiene (including incontinence hygiene), and body cleansing.\n**(5) High contrast**\nThe term high contrast means, with respect to the symbol or label notice, that such symbol or label notice\u2014\n**(A)**\nis either light on a solid dark background or dark on a solid light background; and\n**(B)**\nhas a contrast percentage of at least 70 percent between such symbol or label notice and the background, using the formula (B1\u2013B2)/B1 * 100 = contrast percentage, where B1 is the light reflectance value of the lighter area and B2 is the light reflectance value of the darker area.\n**(6) Label notice**\nThe term label notice means the written phrase Do Not Flush .\n**(7) Principal display panel**\nThe term principal display panel means the side of a product package that is most likely to be displayed, presented, or shown under customary conditions of display for retail sale, and\u2014\n**(A)**\nin the case of a cylindrical or near-cylindrical package, the surface area of which constitutes at least 40 percent of the product package, as measured by multiplying the height by the circumference of the package; or\n**(B)**\nin the case of a flexible film package in which a rectangular prism or near-rectangular prism stack of wipes is housed within the film, the surface area of which is measured by multiplying the length by the width of the side of the package when the flexible packaging film is pressed flat against the stack of wipes on all sides of the stack.\n**(8) State**\nThe term State means each State of the United States, the District of Columbia, and each commonwealth, territory, or possession of the United States.\n**(9) Symbol**\nThe term symbol means the Do Not Flush symbol, as depicted in the most recent edition of the Guidelines for Assessing the Flushability of Disposable Nonwoven Products published by the Association of the Nonwoven Fabrics Industry (INDA) and the European Disposables And Nonwovens Association (EDANA), or an otherwise equivalent symbol adopted by the Commission through rulemaking under this section.\n##### (h) Effective date\nThis section shall apply to a covered entity beginning on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-03-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1092rs.xml",
      "text": "II\nCalendar No. 166\n119th CONGRESS\n1st Session\nS. 1092\n[Report No. 119\u201363]\nIN THE SENATE OF THE UNITED STATES\nMarch 24, 2025 Mr. Merkley (for himself, Ms. Collins , Mr. Blumenthal , Mr. King , Mr. Markey , Mrs. Murray , Mr. Padilla , Mr. Wyden , Mrs. Shaheen , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 19 (legislative day, September 16), 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require certain products to be labeled with \u2018Do Not Flush\u2019 labeling, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act .\n#### 2. Do not flush labeling\n##### (a) In general\nA covered entity shall label a covered product clearly and conspicuously with the label notice and symbol, in accordance with subsections (b) and (c).\n##### (b) Requirements\n**(1) Cylindrical packaging**\nIn the case of a covered product sold in cylindrical or near-cylindrical packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed; or\n**(B)**\nthe symbol shall be displayed on the principal display panel and the label notice, or a combination of the label notice and symbol, shall be displayed on a flip lid in a manner that covers at least 8 percent of the surface area of the flip lid.\n**(2) Flexible film packaging**\nIn the case of a covered product sold in flexible film packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol shall be displayed on the principal display panel and, if the principal display panel is not on the dispensing side of the packaging, on the dispensing side panel; and\n**(B)**\nthe label notice shall be displayed on either the principal display panel or the dispensing side panel, in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(3) Rigid packaging**\nIn the case of a covered product sold in a refillable tub or other rigid packaging that may be reused by a customer, and that is intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(4) Packaging not intended to dispense individual wipes**\nIn the case of a covered product sold in packaging that is not intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user of the covered product.\n**(5) Bulk packaging**\n**(A) In general**\nIn the case of a covered product sold in bulk at retail, the symbol and label notice shall be displayed on both the outer packaging visible at retail and the individual packaging contained within the outer packaging.\n**(B) Exemption**\nThe following shall be exempt from the requirements of subparagraph (A):\n**(i)**\nIndividually packaged covered products that are contained within outer packaging, are not intended to dispense individual wipes, and have no retail labeling.\n**(ii)**\nOuter packaging that does not obscure the symbol and label notice on individually packaged covered products contained within.\n**(6) Packaging of combined products**\n**(A) Outer packaging**\nThe outer packaging of combined products shall be exempt from the symbol and label notice requirements of subsection (a).\n**(B) Packages less than 3 by 3 inches**\nIn the case of a covered product in packaging smaller than 3 inches by 3 inches (such as an individually packaged wipe in tear-top packaging) and sold as part of a combined product, if a symbol and label notice are placed in a prominent location reasonably visible to the user of the covered product, such covered product shall be considered to be labeled clearly and conspicuously.\n##### (c) Reasonable visibility of symbol and label notice\n**(1) In general**\nA covered entity shall ensure that\u2014\n**(A)**\npackaging seams or folds or other packaging design elements do not obscure the symbol or label notice;\n**(B)**\nthe symbol and label notice are each equal in size to at least 2 percent of the surface area of the principal display panel; and\n**(C)**\nthe symbol and label notice have high contrast with the immediate background of the packaging so that such symbol and label notice may be seen and read by an ordinary individual under customary conditions of purchase and use.\n**(2) Proximity of symbol and label notice**\nA covered entity may display a symbol and label notice either adjacent to or on separate areas of the principal display panel.\n**(3) Exception**\nParagraph (1)(C) does not apply to an embossed symbol or label notice on the flip lid of a covered product sold in cylindrical or near-cylindrical packaging.\n##### (d) Representations of flushability\nWith respect to a covered product, a covered entity may not make any express or implied representation that such covered product can or should be flushed.\n##### (e) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or any regulation promulgated under this section shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nThe Commission shall enforce this section and any regulations promulgated under this section by the same means, and with the same jurisdiction, powers, and duties, as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section, and any person who violates this section or any regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(3) Regulations**\nThe Commission may promulgate regulations under section 553 of title 5, United States Code, to implement this section. In developing the regulations, the Commission may consult with the Administrator of the Environmental Protection Agency, the Commissioner of Food and Drugs, the Consumer Product Safety Commission, or any other agency as appropriate.\n**(4) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n##### (f) Preemption of State laws\nNo State or political subdivision of a State may directly or indirectly establish or continue in effect, under any authority, requirements with respect to the Do Not Flush labeling of covered products that are not identical to the requirements of this section and the regulations promulgated under this section.\n##### (g) Definitions\nIn this section:\n**(1) Combined product**\nThe term combined product means two or more products sold in shared retail packaging, of which\u2014\n**(A)**\nat least one of the products is a covered product; and\n**(B)**\nat least one of the products is another consumer product intended to be used in combination with such covered product.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\nThe term covered entity means a manufacturer, wholesaler, supplier, individual or group of individuals, or retailer that is responsible for the labeling or retail packaging of a covered product that is sold or offered for retail sale in the United States.\n**(4) Covered product**\n**(A) In general**\nThe term covered product means a premoistened, nonwoven disposable wipe sold or offered for retail sale\u2014\n**(i)**\nthat is marketed as a baby wipe or diapering wipe; or\n**(ii)**\nthat is a household or personal care wipe (including a wipe described in subparagraph (B)) that\u2014\n**(I)**\nis composed entirely, or in part, of petrochemical-derived fibers; and\n**(II)**\nhas significant potential to be flushed.\n**(B) Inclusions**\nThe wipes described in this subparagraph are\u2014\n**(i)**\nantibacterial wipes and disinfecting wipes;\n**(ii)**\nwipes intended for general purpose cleaning or bathroom cleaning, including toilet cleaning and hard surface cleaning; and\n**(iii)**\nwipes intended for personal care use on the body, including hand sanitizing, makeup removal, feminine hygiene, adult hygiene (including incontinence hygiene), and body cleansing.\n**(5) High contrast**\nThe term high contrast means, with respect to the symbol or label notice, that such symbol or label notice\u2014\n**(A)**\nis either light on a solid dark background or dark on a solid light background; and\n**(B)**\nhas a contrast percentage of at least 70 percent between such symbol or label notice and the background, using the formula (B1\u2013B2)/B1 * 100 = contrast percentage, where B1 is the light reflectance value of the lighter area and B2 is the light reflectance value of the darker area.\n**(6) Label notice**\nThe term label notice means the written phrase Do Not Flush .\n**(7) Principal display panel**\nThe term principal display panel means the side of a product package that is most likely to be displayed, presented, or shown under customary conditions of display for retail sale, and\u2014\n**(A)**\nin the case of a cylindrical or near-cylindrical package, the surface area of which constitutes at least 40 percent of the product package, as measured by multiplying the height by the circumference of the package; or\n**(B)**\nin the case of a flexible film package in which a rectangular prism or near-rectangular prism stack of wipes is housed within the film, the surface area of which is measured by multiplying the length by the width of the side of the package when the flexible packaging film is pressed flat against the stack of wipes on all sides of the stack.\n**(8) State**\nThe term State means each State of the United States, the District of Columbia, and each commonwealth, territory, or possession of the United States.\n**(9) Symbol**\nThe term symbol means the Do Not Flush symbol, as depicted in the most recent edition of the Guidelines for Assessing the Flushability of Disposable Nonwoven Products published by the Association of the Nonwoven Fabrics Industry (INDA) and the European Disposables And Nonwovens Association (EDANA), or an otherwise equivalent symbol adopted by the Commission through rulemaking under this section.\n##### (h) Effective date\nThis section shall apply to a covered entity beginning on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-09-19",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1092es.xml",
      "text": "119th CONGRESS\n2d Session\nS. 1092\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require certain products to be labeled with \u2018Do Not Flush\u2019 labeling, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act .\n#### 2. Do not flush labeling\n##### (a) In general\nA covered entity shall label a covered product with the label notice and symbol, in accordance with subsections (b) and (c).\n##### (b) Requirements\n**(1) Cylindrical packaging**\nIn the case of a covered product sold in cylindrical or near-cylindrical packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed; or\n**(B)**\nthe symbol shall be displayed on the principal display panel and the label notice, or a combination of the label notice and symbol, shall be displayed on a flip lid in a manner that covers at least 8 percent of the surface area of the flip lid.\n**(2) Flexible film packaging**\nIn the case of a covered product sold in flexible film packaging, and intended to dispense individual wipes\u2014\n**(A)**\nthe symbol shall be displayed on the principal display panel and, if the principal display panel is not on the dispensing side of the packaging, on the dispensing side panel; and\n**(B)**\nthe label notice shall be displayed on either the principal display panel or the dispensing side panel, in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(3) Rigid packaging**\nIn the case of a covered product sold in a refillable tub or other rigid packaging that may be reused by a customer, and that is intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user each time a wipe is dispensed.\n**(4) Packaging not intended to dispense individual wipes**\nIn the case of a covered product sold in packaging that is not intended to dispense individual wipes, the symbol and label notice shall be displayed on the principal display panel in a clear and conspicuous location reasonably visible to the user of the covered product.\n**(5) Bulk packaging**\n**(A) In general**\nIn the case of a covered product sold in bulk at retail, the symbol and label notice shall be displayed on both the outer packaging visible at retail and the individual packaging contained within the outer packaging.\n**(B) Exemption**\nThe following shall be exempt from the requirements of subparagraph (A):\n**(i)**\nIndividually packaged covered products that are contained within outer packaging, are not intended to dispense individual wipes, and have no retail labeling.\n**(ii)**\nOuter packaging that does not obscure the symbol and label notice on individually packaged covered products contained within.\n**(6) Packaging of combined products**\n**(A) Outer packaging**\nThe outer packaging of combined products shall be exempt from the symbol and label notice requirements of subsection (a).\n**(B) Packages less than 3 by 3 inches**\nIn the case of a covered product in packaging smaller than 3 inches by 3 inches (such as an individually packaged wipe in tear-top packaging) and sold as part of a combined product, if a symbol and label notice are placed in a prominent location reasonably visible to the user of the covered product, such covered product shall be considered to be labeled clearly and conspicuously.\n##### (c) Reasonable visibility of symbol and label notice\n**(1) In general**\nA covered entity shall ensure that\u2014\n**(A)**\npackaging seams or folds or other packaging design elements do not obscure the symbol or label notice;\n**(B)**\nthe symbol and label notice are each equal in size to at least 2 percent of the surface area of the principal display panel; and\n**(C)**\nthe symbol and label notice have high contrast with the immediate background of the packaging so that such symbol and label notice may be seen and read by an ordinary individual under customary conditions of purchase and use.\n**(2) Proximity of symbol and label notice**\nA covered entity may display a symbol and label notice either adjacent to or on separate areas of the principal display panel.\n**(3) Exception**\nParagraph (1)(C) does not apply to an embossed symbol or label notice on the flip lid of a covered product sold in cylindrical or near-cylindrical packaging.\n##### (d) Representations of flushability\nWith respect to a covered product, a covered entity may not make any express or implied representation that such covered product can or should be flushed.\n##### (e) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(3) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act (15 U.S.C. et seq.).\n**(4) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n##### (f) Commission guidance\nNot later than 180 days after the date of enactment of this Act, the Commission, in consultation with the Administrator of the Environmental Protection Agency, the Commissioner of Food and Drugs, the Consumer Product Safety Commission, and any other agency determined appropriate by the Commission, shall issue guidance to assist covered entities in complying with the requirements of this section.\n##### (g) Limitation on Commission guidance\n**(1) In general**\nNo guidance issued by the Commission with respect to this section shall\u2014\n**(A)**\nconfer any rights on any person, State, or locality; or\n**(B)**\nbind the Commission or any person to the approach recommended in such guidance.\n**(2) Specific violations**\nIn any enforcement action brought under this section, the Commission shall allege a specific violation of a provision of this section.\n**(3) No enforcement actions based on guidance**\nThe Commission may not base an enforcement action on, or execute a consent order based on, practices that are alleged to be inconsistent with any guidance issued under this Act, unless the practices allegedly violate this section.\n##### (h) Preemption of State laws\nNo State or political subdivision of a State may directly or indirectly establish or continue in effect, under any authority, requirements with respect to the Do Not Flush labeling of covered products that are not identical to the requirements of this section.\n##### (i) Definitions\nIn this section:\n**(1) Combined product**\nThe term combined product means two or more products sold in shared retail packaging, of which\u2014\n**(A)**\nat least one of the products is a covered product; and\n**(B)**\nat least one of the products is another consumer product intended to be used in combination with such covered product.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\nThe term covered entity means a manufacturer, wholesaler, supplier, individual or group of individuals, or retailer that is responsible for the labeling or retail packaging of a covered product that is sold or offered for retail sale within the United States.\n**(4) Covered product**\n**(A) In general**\nThe term covered product means a premoistened, nonwoven disposable wipe sold or offered for retail sale\u2014\n**(i)**\nthat is marketed as a baby wipe or diapering wipe; or\n**(ii)**\nthat is a household or personal care wipe (including a wipe described in subparagraph (B)) that\u2014\n**(I)**\nis composed entirely, or in part, of petrochemical-derived fibers; and\n**(II)**\nhas significant potential to be flushed.\n**(B) Inclusions**\nThe wipes described in this subparagraph are\u2014\n**(i)**\nantibacterial wipes and disinfecting wipes;\n**(ii)**\nwipes intended for general purpose cleaning or bathroom cleaning, including toilet cleaning and hard surface cleaning; and\n**(iii)**\nwipes intended for personal care use on the body, including hand sanitizing, makeup removal, feminine hygiene, adult hygiene (including incontinence hygiene), and body cleansing.\n**(5) High contrast**\nThe term high contrast means, with respect to the symbol or label notice, that such symbol or label notice\u2014\n**(A)**\nis either light on a solid dark background or dark on a solid light background; and\n**(B)**\nhas a contrast percentage of at least 70 percent between such symbol or label notice and the background, using the formula (B1\u2013B2)/B1 * 100 = contrast percentage, where B1 is the light reflectance value of the lighter area and B2 is the light reflectance value of the darker area.\n**(6) Label notice**\nThe term label notice means the written phrase Do Not Flush .\n**(7) Principal display panel**\nThe term principal display panel means the side of a product package that is most likely to be displayed, presented, or shown under customary conditions of display for retail sale, and\u2014\n**(A)**\nin the case of a cylindrical or near-cylindrical package, the surface area of which constitutes at least 40 percent of the product package, as measured by multiplying the height by the circumference of the package; or\n**(B)**\nin the case of a flexible film package in which a rectangular prism or near-rectangular prism stack of wipes is housed within the film, the surface area of which is measured by multiplying the length by the width of the side of the package when the flexible packaging film is pressed flat against the stack of wipes on all sides of the stack.\n**(8) State**\nThe term State means each State of the United States, the District of Columbia, and each commonwealth, territory, or possession of the United States.\n**(9) Symbol**\nThe term symbol means the Do Not Flush symbol, as depicted in the most recent edition of the Guidelines for Assessing the Flushability of Disposable Nonwoven Products published by the Association of the Nonwoven Fabrics Industry (INDA) and the European Disposables And Nonwovens Association (EDANA).\n##### (j) Effective date\nThis section shall apply to a covered entity beginning on the date that is 1 year after the date of the enactment of this Act and shall not apply to any covered product packaged or sold before such date.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
        "actionDate": "2025-06-24",
        "text": "Received in the Senate."
      },
      "number": "2269",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "WIPPES Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Cosmetics and personal care",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Environmental Protection Agency (EPA)",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Environmental education",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Environmental regulatory procedures",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Federal Trade Commission (FTC)",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Manufacturing",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-05-22T15:19:25Z"
          },
          {
            "name": "Pest management",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Solid waste and recycling",
            "updateDate": "2025-05-22T15:19:24Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-05-22T15:19:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-14T16:14:19Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-24",
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
          "measure-id": "id119s1092",
          "measure-number": "1092",
          "measure-type": "s",
          "orig-publish-date": "2025-03-24",
          "originChamber": "SENATE",
          "update-date": "2025-06-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1092v00",
            "update-date": "2025-06-18"
          },
          "action-date": "2025-03-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act</strong></p><p>This bill requires entities responsible for the labeling or retail packaging of certain premoistened, nonwoven wipes (e.g., baby wipes, cleaning wipes, or personal care wipes) to label such products clearly and conspicuously with the phrase <em>Do Not Flush</em> and accompanying symbol as depicted under specified industry guidelines.</p><p>The Federal Trade Commission must enforce these requirements\u00a0and may issue regulations to implement the bill.\u00a0</p>"
        },
        "title": "WIPPES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1092.xml",
    "summary": {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act</strong></p><p>This bill requires entities responsible for the labeling or retail packaging of certain premoistened, nonwoven wipes (e.g., baby wipes, cleaning wipes, or personal care wipes) to label such products clearly and conspicuously with the phrase <em>Do Not Flush</em> and accompanying symbol as depicted under specified industry guidelines.</p><p>The Federal Trade Commission must enforce these requirements\u00a0and may issue regulations to implement the bill.\u00a0</p>",
      "updateDate": "2025-06-18",
      "versionCode": "id119s1092"
    },
    "title": "WIPPES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wastewater Infrastructure Pollution Prevention and Environmental Safety Act or the WIPPES Act</strong></p><p>This bill requires entities responsible for the labeling or retail packaging of certain premoistened, nonwoven wipes (e.g., baby wipes, cleaning wipes, or personal care wipes) to label such products clearly and conspicuously with the phrase <em>Do Not Flush</em> and accompanying symbol as depicted under specified industry guidelines.</p><p>The Federal Trade Commission must enforce these requirements\u00a0and may issue regulations to implement the bill.\u00a0</p>",
      "updateDate": "2025-06-18",
      "versionCode": "id119s1092"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1092is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1092rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1092es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "WIPPES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T11:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "WIPPES Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-23T04:23:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Wastewater Infrastructure Pollution Prevention and Environmental Safety Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-03-23T04:23:19Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Wastewater Infrastructure Pollution Prevention and Environmental Safety Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "WIPPES Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-23T04:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "WIPPES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wastewater Infrastructure Pollution Prevention and Environmental Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require certain products to be labeled with 'Do Not Flush' labeling, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T04:48:17Z"
    }
  ]
}
```
