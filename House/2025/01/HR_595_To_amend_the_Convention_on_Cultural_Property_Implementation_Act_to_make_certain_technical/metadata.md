# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/595?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/595
- Title: To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials.
- Congress: 119
- Bill type: HR
- Bill number: 595
- Origin chamber: House
- Introduced date: 2025-01-21
- Update date: 2026-02-17T16:47:10Z
- Update date including text: 2026-02-17T16:47:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-21: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-21: Introduced in House

## Actions

- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Introduced in House
- 2025-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-21",
    "latestAction": {
      "actionDate": "2025-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/595",
    "number": "595",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials.",
    "type": "HR",
    "updateDate": "2026-02-17T16:47:10Z",
    "updateDateIncludingText": "2026-02-17T16:47:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-21",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-21",
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
          "date": "2025-01-21T17:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "SD"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "NV"
    },
    {
      "bioguideId": "O000086",
      "district": "4",
      "firstName": "Burgess",
      "fullName": "Rep. Owens, Burgess [R-UT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Owens",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "UT"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-01-21",
      "state": "CA"
    },
    {
      "bioguideId": "S001199",
      "district": "11",
      "firstName": "Lloyd",
      "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Smucker",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
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
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "MD"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "LA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "UT"
    },
    {
      "bioguideId": "W000816",
      "district": "25",
      "firstName": "Roger",
      "fullName": "Rep. Williams, Roger [R-TX-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "TX"
    },
    {
      "bioguideId": "L000491",
      "district": "3",
      "firstName": "Frank",
      "fullName": "Rep. Lucas, Frank D. [R-OK-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Lucas",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-06-24",
      "state": "OK"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-25",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-08-12",
      "state": "NY"
    },
    {
      "bioguideId": "S001193",
      "district": "14",
      "firstName": "Eric",
      "fullName": "Rep. Swalwell, Eric [D-CA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Swalwell",
      "party": "D",
      "sponsorshipDate": "2025-12-02",
      "state": "CA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-01-22",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr595ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 595\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2025 Ms. Van Duyne (for herself, Mr. Johnson of South Dakota , Mr. Amodei of Nevada , Mr. Owens , and Ms. Jacobs ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials.\n#### 1. Amendments to Convention on Cultural Property Implementation Act\n##### (a) Definitions\nSection 302 of the Convention on Cultural Property Implementation Act ( 19 U.S.C. 2601 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (8), (9), (10), and (11) as paragraphs (9), (10), (11), and (12), respectively; and\n**(2)**\nby inserting after paragraph (7) the following:\n(8) The term numismatic material includes coins, tokens, paper money, medals and related objects. .\n##### (b) Import restrictions\nSection 307 of the Convention on Cultural Property Implementation Act ( 19 U.S.C. 2606 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1), by striking ; or at the end and inserting a comma;\n**(B)**\nin paragraph (2)(B), by adding or at the end; and\n**(C)**\nby inserting after paragraph (2)(B) (as amended) the following:\n(3) in the case of such material that is numismatic material, satisfactory evidence that the material was acquired lawfully, is of a known type, and is not known to be the direct product of illicit excavations within a State Party, ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(B), by striking and at the end;\n**(B)**\nin paragraph (2)(B), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(3) for purposes of subsection (b)(3), one or more declarations under oath by the importer or the person for whose account the material is imported, stating that, to the best of his knowledge, the numismatic material\u2014 (A) was acquired lawfully in one or more States Party; (B) was lawfully exported from a State Party in which the numismatic material was acquired; (C) is of a type known to exist in multiple examples which has been published in a reference work on numismatics; and (D) is not known to be the direct product of illicit excavations within another State Party after the effective date for import restrictions on numismatic material granted to that State Party. ; and\n**(3)**\nby adding at the end the following:\n(e) No other documentation required The customs officer reviewing the satisfactory evidence shall not require any documentation or statements additional to that which is set forth in subsection (c) unless the customs officer has probable cause based on documentary evidence to believe that the satisfactory evidence is false or fraudulent. .",
      "versionDate": "2025-01-21",
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
            "name": "Currency",
            "updateDate": "2025-03-26T19:52:50Z"
          },
          {
            "name": "Customs enforcement",
            "updateDate": "2025-03-26T19:52:44Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-03-26T19:52:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-03-20T20:05:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-21",
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
          "measure-id": "id119hr595",
          "measure-number": "595",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-21",
          "originChamber": "HOUSE",
          "update-date": "2026-02-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr595v00",
            "update-date": "2026-02-17"
          },
          "action-date": "2025-01-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill revises the standard for providing satisfactory evidence to U.S. Customs and Border Protection (CBP) regarding the importation of numismatic material (i.e., coins, tokens, paper money, medals, and related objects) into the United States.</p><p>Current law generally prohibits the importation of designated archaeological or ethnological material that is exported from certain countries that are a party to the 1970 UNESCO Convention on the Means of Prohibiting and Preventing the Illicit Import, Export and Transfer of Ownership of Cultural Property. Importation is allowed if the country issues a certification or other documentation certifying the exportation was not in violation of the country's laws. The United States implements its obligations through the Convention on Cultural Property Implementation Act.</p><p>Under current law,\u00a0CBP must seize imports of designated archaeological or ethnological material\u00a0unless the importer establishes by certain documentation or satisfactory evidence that the material is admissible into the United States.\u00a0</p><p>This bill specifies the standard for satisfactory evidence with respect to numismatic material. Specifically, the bill allows for the import of numismatic material with evidence that the numismatic material was acquired and exported lawfully, is of a known type, and is not known to be the direct product of illicit excavations within certain countries\u00a0after the effective date for any import restrictions on such material.\u00a0</p><p>The bill prohibits CBP, when reviewing satisfactory evidence, from requiring other\u00a0documentation unless there is probable cause to believe the presented evidence is false or fraudulent.</p>"
        },
        "title": "To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr595.xml",
    "summary": {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill revises the standard for providing satisfactory evidence to U.S. Customs and Border Protection (CBP) regarding the importation of numismatic material (i.e., coins, tokens, paper money, medals, and related objects) into the United States.</p><p>Current law generally prohibits the importation of designated archaeological or ethnological material that is exported from certain countries that are a party to the 1970 UNESCO Convention on the Means of Prohibiting and Preventing the Illicit Import, Export and Transfer of Ownership of Cultural Property. Importation is allowed if the country issues a certification or other documentation certifying the exportation was not in violation of the country's laws. The United States implements its obligations through the Convention on Cultural Property Implementation Act.</p><p>Under current law,\u00a0CBP must seize imports of designated archaeological or ethnological material\u00a0unless the importer establishes by certain documentation or satisfactory evidence that the material is admissible into the United States.\u00a0</p><p>This bill specifies the standard for satisfactory evidence with respect to numismatic material. Specifically, the bill allows for the import of numismatic material with evidence that the numismatic material was acquired and exported lawfully, is of a known type, and is not known to be the direct product of illicit excavations within certain countries\u00a0after the effective date for any import restrictions on such material.\u00a0</p><p>The bill prohibits CBP, when reviewing satisfactory evidence, from requiring other\u00a0documentation unless there is probable cause to believe the presented evidence is false or fraudulent.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr595"
    },
    "title": "To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials."
  },
  "summaries": [
    {
      "actionDate": "2025-01-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill revises the standard for providing satisfactory evidence to U.S. Customs and Border Protection (CBP) regarding the importation of numismatic material (i.e., coins, tokens, paper money, medals, and related objects) into the United States.</p><p>Current law generally prohibits the importation of designated archaeological or ethnological material that is exported from certain countries that are a party to the 1970 UNESCO Convention on the Means of Prohibiting and Preventing the Illicit Import, Export and Transfer of Ownership of Cultural Property. Importation is allowed if the country issues a certification or other documentation certifying the exportation was not in violation of the country's laws. The United States implements its obligations through the Convention on Cultural Property Implementation Act.</p><p>Under current law,\u00a0CBP must seize imports of designated archaeological or ethnological material\u00a0unless the importer establishes by certain documentation or satisfactory evidence that the material is admissible into the United States.\u00a0</p><p>This bill specifies the standard for satisfactory evidence with respect to numismatic material. Specifically, the bill allows for the import of numismatic material with evidence that the numismatic material was acquired and exported lawfully, is of a known type, and is not known to be the direct product of illicit excavations within certain countries\u00a0after the effective date for any import restrictions on such material.\u00a0</p><p>The bill prohibits CBP, when reviewing satisfactory evidence, from requiring other\u00a0documentation unless there is probable cause to believe the presented evidence is false or fraudulent.</p>",
      "updateDate": "2026-02-17",
      "versionCode": "id119hr595"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr595ih.xml"
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
      "title": "To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Convention on Cultural Property Implementation Act to make certain technical corrections to facilitate the lawful trade and collecting of numismatic materials.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T04:18:28Z"
    }
  ]
}
```
