# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/246?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/246
- Title: Interstate Transport Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 246
- Origin chamber: Senate
- Introduced date: 2025-01-24
- Update date: 2026-02-04T05:06:25Z
- Update date including text: 2026-02-04T05:06:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in Senate
- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-11-18 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.
- 2025-11-18 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.
- 2025-11-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 268.
- Latest action: 2025-01-24: Introduced in Senate

## Actions

- 2025-01-24 - IntroReferral: Introduced in Senate
- 2025-01-24 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-11-18 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.
- 2025-11-18 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.
- 2025-11-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 268.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/246",
    "number": "246",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Interstate Transport Act of 2025",
    "type": "S",
    "updateDate": "2026-02-04T05:06:25Z",
    "updateDateIncludingText": "2026-02-04T05:06:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 268.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-11-18",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz without amendment. With written report No. 119-96.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
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
            "date": "2025-11-18T21:28:15Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-24T18:35:00Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "OR"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "NM"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "MT"
    },
    {
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-01-24",
      "state": "MI"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "ID"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-03",
      "state": "WY"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s246is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 246\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Budd (for himself, Mr. Wyden , Mr. Crapo , Mr. Heinrich , Mr. Daines , Mr. Peters , and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo protect the right of law-abiding citizens to transport knives interstate, notwithstanding a patchwork of local and State prohibitions.\n#### 1. Short title\nThis Act may be cited as the Interstate Transport Act of 2025 .\n#### 2. Interstate transportation of knives\n##### (a) Definitions\nIn this Act:\n**(1) State**\nThe term State means any of the 50 States, the District of Columbia, American Samoa, Guam, Puerto Rico, the Northern Mariana Islands, the Virgin Islands of the United States, and any other territory of the United States.\n**(2) Transport**\nThe term transport \u2014\n**(A)**\nincludes staying in temporary lodging overnight, common carrier misrouting or delays, stops for food, fuel, vehicle maintenance, emergencies, or medical treatment, and any other activity related to the journey of a person; and\n**(B)**\ndoes not include transport of a knife with the intent to commit an offense punishable by imprisonment for a term exceeding 1 year involving the use or threatened use of force against another person, or with knowledge, or reasonable cause to believe, that such an offense is to be committed in the course of, or arising from, the journey.\n##### (b) Transport of knives\n**(1) In general**\nNotwithstanding any other provision of any law or any rule or regulation of a State or any political subdivision thereof, a person who is not otherwise prohibited by any Federal law from possessing, transporting, shipping, or receiving a knife shall be entitled to transport a knife for any lawful purpose from any place where the person may lawfully possess, carry, or transport the knife to any other place where the person may lawfully possess, carry, or transport the knife if\u2014\n**(A)**\nin the case of transport by motor vehicle, the knife\u2014\n**(i)**\nis not directly accessible from the passenger compartment of the motor vehicle; or\n**(ii)**\nin the case of a motor vehicle without a compartment separate from the passenger compartment, is contained in a locked container other than the glove compartment or console; and\n**(B)**\nin the case of transport by means other than a motor vehicle, including any transport over land or on or through water, the knife is contained in a locked container.\n**(2) Limitation**\nThis subsection shall not apply to the transport of a knife or tool in the cabin of a passenger aircraft subject to the rules and regulations of the Transportation Security Administration.\n##### (c) Emergency knives\n**(1) In general**\nA person\u2014\n**(A)**\nmay carry in the passenger compartment of a mode of transportation a knife or tool\u2014\n**(i)**\nthe blades of which consist only of a blunt tipped safety blade, a guarded blade, or both; and\n**(ii)**\nthat is specifically designed for enabling escape in an emergency by cutting safety belts; and\n**(B)**\nshall not be required to secure a knife or tool described in subparagraph (A) in a locked container.\n**(2) Limitation**\nThis subsection shall not apply to the transport of a knife or tool in the cabin of a passenger aircraft subject to the rules and regulations of the Transportation Security Administration.\n##### (d) No arrest\nA person who is transporting a knife in compliance with this section may not be arrested for violation of any law, rule, or regulation of a State or political subdivision of a State related to the possession, transport, or carrying of a knife, unless there is probable cause to believe that the person is not in compliance with subsection (b).\n##### (e) Costs\nIf a person who asserts this section as a claim or defense in a civil or criminal action or proceeding is a prevailing party on the claim or defense, the court shall award costs and reasonable attorney's fees incurred by the person.\n##### (f) Expungement\nIf a person who asserts this section as a claim or defense in a criminal proceeding is a prevailing party on the claim or defense, the court shall enter an order that directs that there be expunged from all official records all references to\u2014\n**(1)**\nthe arrest of the person for the offense as to which the claim or defense was asserted;\n**(2)**\nthe institution of any criminal proceedings against the person relating to such offense; and\n**(3)**\nthe results of the proceedings, if any.\n##### (g) Rule of construction\nNothing in this section shall be construed to limit any right to possess, carry, or transport a knife under applicable State law.",
      "versionDate": "2025-01-24",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s246rs.xml",
      "text": "II\nCalendar No. 268\n119th CONGRESS\n1st Session\nS. 246\n[Report No. 119\u201396]\nIN THE SENATE OF THE UNITED STATES\nJanuary 24, 2025 Mr. Budd (for himself, Mr. Wyden , Mr. Crapo , Mr. Heinrich , Mr. Daines , Mr. Peters , Mr. Risch , Ms. Lummis , and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nNovember 18, 2025 Reported by Mr. Cruz , without amendment\nA BILL\nTo protect the right of law-abiding citizens to transport knives interstate, notwithstanding a patchwork of local and State prohibitions.\n#### 1. Short title\nThis Act may be cited as the Interstate Transport Act of 2025 .\n#### 2. Interstate transportation of knives\n##### (a) Definitions\nIn this Act:\n**(1) State**\nThe term State means any of the 50 States, the District of Columbia, American Samoa, Guam, Puerto Rico, the Northern Mariana Islands, the Virgin Islands of the United States, and any other territory of the United States.\n**(2) Transport**\nThe term transport \u2014\n**(A)**\nincludes staying in temporary lodging overnight, common carrier misrouting or delays, stops for food, fuel, vehicle maintenance, emergencies, or medical treatment, and any other activity related to the journey of a person; and\n**(B)**\ndoes not include transport of a knife with the intent to commit an offense punishable by imprisonment for a term exceeding 1 year involving the use or threatened use of force against another person, or with knowledge, or reasonable cause to believe, that such an offense is to be committed in the course of, or arising from, the journey.\n##### (b) Transport of knives\n**(1) In general**\nNotwithstanding any other provision of any law or any rule or regulation of a State or any political subdivision thereof, a person who is not otherwise prohibited by any Federal law from possessing, transporting, shipping, or receiving a knife shall be entitled to transport a knife for any lawful purpose from any place where the person may lawfully possess, carry, or transport the knife to any other place where the person may lawfully possess, carry, or transport the knife if\u2014\n**(A)**\nin the case of transport by motor vehicle, the knife\u2014\n**(i)**\nis not directly accessible from the passenger compartment of the motor vehicle; or\n**(ii)**\nin the case of a motor vehicle without a compartment separate from the passenger compartment, is contained in a locked container other than the glove compartment or console; and\n**(B)**\nin the case of transport by means other than a motor vehicle, including any transport over land or on or through water, the knife is contained in a locked container.\n**(2) Limitation**\nThis subsection shall not apply to the transport of a knife or tool in the cabin of a passenger aircraft subject to the rules and regulations of the Transportation Security Administration.\n##### (c) Emergency knives\n**(1) In general**\nA person\u2014\n**(A)**\nmay carry in the passenger compartment of a mode of transportation a knife or tool\u2014\n**(i)**\nthe blades of which consist only of a blunt tipped safety blade, a guarded blade, or both; and\n**(ii)**\nthat is specifically designed for enabling escape in an emergency by cutting safety belts; and\n**(B)**\nshall not be required to secure a knife or tool described in subparagraph (A) in a locked container.\n**(2) Limitation**\nThis subsection shall not apply to the transport of a knife or tool in the cabin of a passenger aircraft subject to the rules and regulations of the Transportation Security Administration.\n##### (d) No arrest\nA person who is transporting a knife in compliance with this section may not be arrested for violation of any law, rule, or regulation of a State or political subdivision of a State related to the possession, transport, or carrying of a knife, unless there is probable cause to believe that the person is not in compliance with subsection (b).\n##### (e) Costs\nIf a person who asserts this section as a claim or defense in a civil or criminal action or proceeding is a prevailing party on the claim or defense, the court shall award costs and reasonable attorney's fees incurred by the person.\n##### (f) Expungement\nIf a person who asserts this section as a claim or defense in a criminal proceeding is a prevailing party on the claim or defense, the court shall enter an order that directs that there be expunged from all official records all references to\u2014\n**(1)**\nthe arrest of the person for the offense as to which the claim or defense was asserted;\n**(2)**\nthe institution of any criminal proceedings against the person relating to such offense; and\n**(3)**\nthe results of the proceedings, if any.\n##### (g) Rule of construction\nNothing in this section shall be construed to limit any right to possess, carry, or transport a knife under applicable State law.",
      "versionDate": "2025-01-24",
      "versionType": "Reported in Senate"
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
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-02-10T20:36:31Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-02-10T20:36:11Z"
          },
          {
            "name": "Legal fees and court costs",
            "updateDate": "2025-02-10T20:36:40Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2025-02-10T20:36:18Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-02-10T20:37:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-02-06T11:28:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119s246",
          "measure-number": "246",
          "measure-type": "s",
          "orig-publish-date": "2025-01-24",
          "originChamber": "SENATE",
          "update-date": "2025-07-21"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s246v00",
            "update-date": "2025-07-21"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Interstate Transport Act of 2025</strong></p><p>This bill permits an individual to\u00a0transport a knife between two places (e.g., states) where it is legal to possess, carry, or transport the knife.\u00a0The knife must be transported in compliance with the bill's accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or secure storage requirements.</p>"
        },
        "title": "Interstate Transport Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s246.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interstate Transport Act of 2025</strong></p><p>This bill permits an individual to\u00a0transport a knife between two places (e.g., states) where it is legal to possess, carry, or transport the knife.\u00a0The knife must be transported in compliance with the bill's accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or secure storage requirements.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s246"
    },
    "title": "Interstate Transport Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Interstate Transport Act of 2025</strong></p><p>This bill permits an individual to\u00a0transport a knife between two places (e.g., states) where it is legal to possess, carry, or transport the knife.\u00a0The knife must be transported in compliance with the bill's accessibility and secure storage requirements, unless it is an emergency knife or tool designed to cut seat belts.</p><p>An individual who is transporting a knife in compliance with this bill may not be arrested for a knife violation unless there is probable cause to believe the individual failed to comply with the accessibility or secure storage requirements.</p>",
      "updateDate": "2025-07-21",
      "versionCode": "id119s246"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s246is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s246rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Interstate Transport Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-20T05:38:24Z"
    },
    {
      "title": "Interstate Transport Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Interstate Transport Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the right of law-abiding citizens to transport knives interstate, notwithstanding a patchwork of local and State prohibitions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:25Z"
    }
  ]
}
```
