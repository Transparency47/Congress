# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1711?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1711
- Title: STOP China Act
- Congress: 119
- Bill type: S
- Bill number: 1711
- Origin chamber: Senate
- Introduced date: 2025-05-12
- Update date: 2026-05-28T20:20:26Z
- Update date including text: 2026-05-28T20:20:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-12: Introduced in Senate
- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-05-12: Introduced in Senate

## Actions

- 2025-05-12 - IntroReferral: Introduced in Senate
- 2025-05-12 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-12",
    "latestAction": {
      "actionDate": "2025-05-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1711",
    "number": "1711",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "STOP China Act",
    "type": "S",
    "updateDate": "2026-05-28T20:20:26Z",
    "updateDateIncludingText": "2026-05-28T20:20:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-12",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-12",
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
          "date": "2025-05-12T21:32:29Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "WI"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "FL"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MI"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-05-12",
      "state": "MN"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "NE"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-12",
      "state": "TN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "AK"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "IA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1711is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1711\nIN THE SENATE OF THE UNITED STATES\nMay 12, 2025 Mr. Cornyn (for himself, Ms. Baldwin , Mr. Scott of Florida , Mr. Peters , Ms. Smith , Mr. Ricketts , Mrs. Capito , and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo address national security risks and prohibit the use of Federal funds for the procurement of certain vehicles and vehicle technologies produced or provided by entities based in certain countries, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Safeguarding Transit Operations to Prohibit China Act or the STOP China Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe People\u2019s Republic of China (referred to in this section as the PRC ) uses a deliberately intricate web of industrial policies to distort market behavior to achieve dominance in global markets and increase the dependence of the United States on imports from the PRC;\n**(2)**\nthe adoption of PRC-developed technologies in the United States, including those used in certain vehicles, poses a significant risk to national security and threatens the long-term competitiveness of the United States;\n**(3)**\nthe PRC intentionally creates overcapacity and sells products at below-market prices to gain market share and undermine United States domestic supply chains;\n**(4)**\nCongress must continue to confront the military-civil fusion strategy of the PRC and the intrusion of the PRC into the United States transportation market, as Congress has done in the National Defense Authorization Act for Fiscal Year 2020 ( Public Law 116\u201392 ; 133 Stat. 1198) and the FAA Reauthorization Act of 2024 ( Public Law 118\u201363 ; 138 Stat. 1025);\n**(5)**\nUnited States taxpayer dollars should not be used to fund PRC-subsidized vehicle manufacturing or technology companies; and\n**(6)**\nany entity accepting Federal funding must be prevented from procuring certain vehicles\u2014\n**(A)**\nfrom a PRC entity or an entity otherwise related legally or financially to a corporation based in the PRC; or\n**(B)**\nthat contain certain vehicle technologies identified as matters of national security concern.\n#### 3. Prohibitions relating to certain vehicles produced or provided by entities based in certain countries\nSection 5323(u) of title 49, United States Code, is amended\u2014\n**(1)**\nby striking paragraphs (1) and (2) and inserting the following:\n(1) Definitions In this subsection: (A) Covered entity The term covered entity means an entity (including a corporation, partnership, association, organization, or other entity)\u2014 (i) the principal place of business of which is in a covered nation; (ii) that is headquartered in, incorporated in, or otherwise organized under the laws of a covered nation; (iii) that, regardless of where the entity is organized or doing business, is owned or controlled by a covered nation or covered individual, including circumstances in which a covered individual possesses the power to determine, direct, or decide matters affecting the entity\u2014 (I) through\u2014 (aa) the ownership of a majority of the total outstanding voting interest in the entity; (bb) board representation; (cc) proxy voting; (dd) a special share; (ee) contractual arrangements; (ff) formal or informal arrangements to act in concert; or (gg) other means; and (II) regardless of whether that power is\u2014 (aa) direct; or (bb) exercised or unexercised; (iv) is owned or controlled by, a subsidiary of, an affiliate of, or in a joint venture with an entity described in clause (i), (ii), or (iii); (v) is a manufacturer from which the procurement of rolling stock was ever prohibited under this subsections; or (vi) is an owner of, successor of, subsidiary of, affiliate of, or in a joint venture with a manufacturer described in clause (v). (B) Covered funding The term covered funding means any financial assistance made available under this chapter. (C) Covered individual The term covered individual means any individual, wherever located\u2014 (i) whose activities are directly or supervised, directed, controlled, financed, or subsidized, in whole or in majority part, by a covered nation; (ii) who acts as an agent, representative, or employee of a covered nation or an individual described in clause (i); (iii) who acts in any other capacity at the order of, at the request of, or under the direction or control of a covered nation or an individual described in clause (i); or (iv) who\u2014 (I) is a citizen or resident of a covered nation or a country controlled by a covered nation; and (II) is not a citizen or permanent resident of the United States. (D) Covered nation The term covered nation has the meaning given the term in section 4872(d) of title 10. (E) Covered vehicle The term covered vehicle means rolling stock that\u2014 (i) is produced or provided by a covered entity included on the list developed under paragraph (2)(B); or (ii) incorporates an electric power train produced or provided by a covered entity included on the list developed under paragraph (2)(B). (F) Electric power train The term electric power train has the meaning given the term in section 571.305 of title 49, Code of Federal Regulations (as in effect on the date of enactment of the STOP China Act ). (2) Prohibition (A) In general Subject to subparagraph (C), on and after the date of enactment of the STOP China Act , the Secretary may not award or obligate covered funding\u2014 (i) for a contract or subcontract for the procurement of a covered vehicle; or (ii) for the construction, installation, or maintenance of infrastructure to fuel or charge a covered vehicle that is a bus, if the applicable covered vehicle is procured under a contract or subcontract executed on or after the date of enactment of the STOP China Act . (B) List of covered entities (i) In general Not later than 30 days after the date of enactment of the STOP China Act , the United States Trade Representative, in consultation with the Attorney General and the Secretary, shall make publicly available, including on a publicly accessible website, a list of covered entities that produce or provide\u2014 (I) rolling stock to which the prohibition under subparagraph (A) applies; or (II) electric power trains the incorporation of which into rolling stock would render the rolling stock subject to the prohibition under subparagraph (A). (ii) Updates The United States Trade Representative shall update the list required under clause (i)\u2014 (I) based on information provided to the United States Trade Representative by the Attorney General and the Secretary; and (II) not less frequently than\u2014 (aa) once every 90 days during the 180-day period beginning on the date of initial publication of the list under that clause; and (bb) annually thereafter. (C) Exception Notwithstanding subparagraph (A), the Secretary may procure a covered vehicle or construct, install, or maintain infrastructure to fuel or charge a covered vehicle for purposes of\u2014 (i) the inspection or investigation of a motor vehicle or equipment; or (ii) motor vehicle safety research, development, or testing. .\n**(2)**\nin paragraph (4), by striking paragraph (1) each place that term appears and inserting paragraph (2) ;\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nby striking This subsection, including the and inserting The ;\n**(ii)**\nby striking the comma after (4) ;\n**(iii)**\nby inserting that does not utilize covered funds after subcontract ;\n**(iv)**\nby striking rail rolling stock manufacturer described in paragraph (1) and inserting covered entity ;\n**(v)**\nby striking the manufacturer and inserting the covered entity ; and\n**(vi)**\nby striking date of enactment of this subsection and inserting date of enactment of the STOP China Act ;\n**(B)**\nby striking subparagraph (B) and inserting the following:\n(B) Contract completion Notwithstanding paragraph (2), covered funds may be obligated for a contract or subcontract that was eligible for assistance under this chapter under the provisions of this subsection prior to the date of enactment of the STOP China Act until the delivery of rolling stock is complete under such contract. ; and\n**(C)**\nby striking subparagraph (C); and\n**(4)**\nby adding at the end the following:\n(6) Severability If any provision of this subsection, or the application of this subsection to any person or circumstance, is held to be unconstitutional or otherwise invalid, the remainder of this subsection, and the application of the provision to any other person or circumstance, shall not be affected. .\n#### 4. Prohibitions relating to additional vehicles produced or provided by entities based in certain countries\n##### (a) Definitions\nIn this section:\n**(1) Covered entity; covered individual; covered nation; covered vehicle; electric power train**\nThe terms covered entity ; covered individual , covered nation , covered vehicle , and electric power train have the meanings given those terms in section 5323(u)(1) of title 49, United States Code.\n**(2) Covered funding**\nThe term covered funding means any appropriations made available to the Department, other than funds made available under chapter 53 of title 49, United States Code.\n**(3) Department**\nThe term Department means the Department of Transportation.\n**(4) Secretary**\nThe term Secretary means the Secretary of Transportation.\n##### (b) Prohibition\n**(1) In general**\nSubject to paragraph (3), the Department may not award, obligate, allocate, or expend covered funding\u2014\n**(A)**\nfor the procurement of a covered vehicle by the Department or any other agency or person; or\n**(B)**\nfor the construction, installation, or maintenance of infrastructure to fuel or charge a covered vehicle that is a bus, if the applicable covered vehicle is procured under a contract or subcontract executed on or after the date of enactment of this Act.\n**(2) List of covered entities**\n**(A) In general**\nNot later than 30 days after the date of enactment of this Act, the United States Trade Representative, in consultation with the Attorney General and the Secretary, shall make publicly available, including on a publicly accessible website, a list of covered entities that produce or provide\u2014\n**(i)**\ncovered vehicles to which the prohibition under paragraph (1) applies; or\n**(ii)**\nelectric power trains the incorporation of which into a covered vehicle would render the covered vehicle subject to the prohibition under that paragraph.\n**(B) Updates**\nThe United States Trade Representative shall update the list required under subparagraph (A)\u2014\n**(i)**\nbased on information provided to the United States Trade Representative by the Attorney General and the Secretary; and\n**(ii)**\nnot less frequently than\u2014\n**(I)**\nonce every 90 days during the 180-day period beginning on the date of initial publication of the list under that subparagraph; and\n**(II)**\nannually thereafter.\n**(3) Exception**\nNotwithstanding paragraph (1), the Department may procure a covered vehicle or construct, install, or maintain infrastructure to fuel or charge a covered vehicle for purposes of\u2014\n**(A)**\nthe inspection or investigation of a motor vehicle or equipment; or\n**(B)**\nmotor vehicle safety research, development, or testing.\n##### (c) Severability\nIf any provision of this section, or the application of this section to any person or circumstance, is held to be unconstitutional or otherwise invalid, the remainder of this section, and the application of the provision to any other person or circumstance, shall not be affected.",
      "versionDate": "2025-05-12",
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
        "actionDate": "2025-07-15",
        "text": "Referred to the Subcommittee on Highways and Transit."
      },
      "number": "4361",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "STOP China Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-28T12:37:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-12",
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
          "measure-id": "id119s1711",
          "measure-number": "1711",
          "measure-type": "s",
          "orig-publish-date": "2025-05-12",
          "originChamber": "SENATE",
          "update-date": "2026-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1711v00",
            "update-date": "2026-05-28"
          },
          "action-date": "2025-05-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Safeguarding Transit Operations to Prohibit China Act or the STOP China Act\u00a0</strong></p><p>This bill prohibits federal transportation funds from being used to purchase rolling stock (e.g., rail cars or buses) or fueling or charging infrastructure from entities with ties to China, North Korea, Russia, or Iran (i.e.,\u00a0a covered nation). In general, this replaces a current prohibition on the use of Federal Transportation Administration (FTA)\u00a0funds for rolling stock from manufacturers owned or controlled by corporations based in certain countries.</p><p>Specifically, Department of Transportation (DOT)\u00a0funds, which include\u00a0FTA funds,\u00a0may not be used\u00a0for the purchase of rolling stock\u00a0or bus fueling or charging infrastructure from entities with ties to a covered nation. This prohibition also applies to\u00a0vehicles that incorporate electric power trains from such entities.</p><p>The prohibition broadly applies to corporations, joint ventures, individuals, and organizations with ties to covered nations.\u00a0Examples of applicable entities include an individual whose activities are directed or financed by a covered nation or an entity that is owned or controlled by a covered nation or such an individual.</p><p>The United States Trade Representative (USTR) must publish a list of the applicable entities and update the list annually.</p><p>The bill includes an exception for motor vehicles or fueling and charging stations used for (1) inspecting or investigating vehicles or equipment; or (2) vehicle safety research, development, or testing.</p>"
        },
        "title": "STOP China Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1711.xml",
    "summary": {
      "actionDate": "2025-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding Transit Operations to Prohibit China Act or the STOP China Act\u00a0</strong></p><p>This bill prohibits federal transportation funds from being used to purchase rolling stock (e.g., rail cars or buses) or fueling or charging infrastructure from entities with ties to China, North Korea, Russia, or Iran (i.e.,\u00a0a covered nation). In general, this replaces a current prohibition on the use of Federal Transportation Administration (FTA)\u00a0funds for rolling stock from manufacturers owned or controlled by corporations based in certain countries.</p><p>Specifically, Department of Transportation (DOT)\u00a0funds, which include\u00a0FTA funds,\u00a0may not be used\u00a0for the purchase of rolling stock\u00a0or bus fueling or charging infrastructure from entities with ties to a covered nation. This prohibition also applies to\u00a0vehicles that incorporate electric power trains from such entities.</p><p>The prohibition broadly applies to corporations, joint ventures, individuals, and organizations with ties to covered nations.\u00a0Examples of applicable entities include an individual whose activities are directed or financed by a covered nation or an entity that is owned or controlled by a covered nation or such an individual.</p><p>The United States Trade Representative (USTR) must publish a list of the applicable entities and update the list annually.</p><p>The bill includes an exception for motor vehicles or fueling and charging stations used for (1) inspecting or investigating vehicles or equipment; or (2) vehicle safety research, development, or testing.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s1711"
    },
    "title": "STOP China Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Safeguarding Transit Operations to Prohibit China Act or the STOP China Act\u00a0</strong></p><p>This bill prohibits federal transportation funds from being used to purchase rolling stock (e.g., rail cars or buses) or fueling or charging infrastructure from entities with ties to China, North Korea, Russia, or Iran (i.e.,\u00a0a covered nation). In general, this replaces a current prohibition on the use of Federal Transportation Administration (FTA)\u00a0funds for rolling stock from manufacturers owned or controlled by corporations based in certain countries.</p><p>Specifically, Department of Transportation (DOT)\u00a0funds, which include\u00a0FTA funds,\u00a0may not be used\u00a0for the purchase of rolling stock\u00a0or bus fueling or charging infrastructure from entities with ties to a covered nation. This prohibition also applies to\u00a0vehicles that incorporate electric power trains from such entities.</p><p>The prohibition broadly applies to corporations, joint ventures, individuals, and organizations with ties to covered nations.\u00a0Examples of applicable entities include an individual whose activities are directed or financed by a covered nation or an entity that is owned or controlled by a covered nation or such an individual.</p><p>The United States Trade Representative (USTR) must publish a list of the applicable entities and update the list annually.</p><p>The bill includes an exception for motor vehicles or fueling and charging stations used for (1) inspecting or investigating vehicles or equipment; or (2) vehicle safety research, development, or testing.</p>",
      "updateDate": "2026-05-28",
      "versionCode": "id119s1711"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1711is.xml"
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
      "title": "STOP China Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "STOP China Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Safeguarding Transit Operations to Prohibit China Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address national security risks and prohibit the use of Federal funds for the procurement of certain vehicles and vehicle technologies produced or provided by entities based in certain countries, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:46Z"
    }
  ]
}
```
