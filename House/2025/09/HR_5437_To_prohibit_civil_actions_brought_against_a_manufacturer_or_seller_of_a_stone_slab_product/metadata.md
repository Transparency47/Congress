# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5437?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5437
- Title: Protection of Lawful Commerce in Stone Slab Products Act
- Congress: 119
- Bill type: HR
- Bill number: 5437
- Origin chamber: House
- Introduced date: 2025-09-17
- Update date: 2026-05-21T08:08:44Z
- Update date including text: 2026-05-21T08:08:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-17: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-09-17: Introduced in House

## Actions

- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Introduced in House
- 2025-09-17 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-17",
    "latestAction": {
      "actionDate": "2025-09-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5437",
    "number": "5437",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Protection of Lawful Commerce in Stone Slab Products Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:44Z",
    "updateDateIncludingText": "2026-05-21T08:08:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-17",
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
      "actionDate": "2025-09-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-17",
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
          "date": "2025-09-17T14:04:10Z",
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
      "bioguideId": "B001302",
      "district": "5",
      "firstName": "Andy",
      "fullName": "Rep. Biggs, Andy [R-AZ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-09-17",
      "state": "AZ"
    },
    {
      "bioguideId": "E000294",
      "district": "6",
      "firstName": "Tom",
      "fullName": "Rep. Emmer, Tom [R-MN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Emmer",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "False",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "CA"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "MN"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-11-20",
      "state": "NJ"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "MN"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "FL"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "FL"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "SC"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "TX"
    },
    {
      "bioguideId": "M001218",
      "district": "7",
      "firstName": "Richard",
      "fullName": "Rep. McCormick, Richard [R-GA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "GA"
    },
    {
      "bioguideId": "V000139",
      "district": "7",
      "firstName": "Matt",
      "fullName": "Rep. Van Epps, Matt [R-TN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Epps",
      "party": "R",
      "sponsorshipDate": "2026-05-13",
      "state": "TN"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5437ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5437\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 17, 2025 Mr. McClintock (for himself and Mr. Biggs of Arizona ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo prohibit civil actions brought against a manufacturer or seller of a stone slab product for harm resulting from the alteration of such a product by a fabricator, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protection of Lawful Commerce in Stone Slab Products Act .\n#### 2. Findings; purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nCivil actions have been commenced against manufacturers and sellers of certain stone slab products, including those used for kitchen countertops and similar applications. These products are not inherently dangerous and upon their manufacture and entry into the stream of commerce, they do not pose an inherent risk of injury to human beings.\n**(2)**\nThese civil actions seek money damages from manufacturers and sellers by persons who claim personal injuries as a result of exposure to silica dust produced during the alteration of such products in the course of their employment by third-party fabricators. The manufacturers and sellers of these products have no control over these fabricators.\n**(3)**\nThe alteration of such products is heavily regulated by Federal and State workplace safety laws and regulations, including section 1910.1053 of title 29, Code of Federal Regulations, and California Labor Code Section 5204, which require a variety of safety measures that fabricators must employ in order to mitigate the risk of potential injuries posed by silica dust. However, some fabricators fail to comply with these requirements and thereby expose their employees and others to the potential harms that these laws and regulations are intended to prevent.\n**(4)**\nBusinesses located or conducting business in the United States that are engaged in interstate and foreign commerce through the lawful design, manufacture, marketing, distribution, importation, or sale to third-parties of certain stone slab products are not responsible, and should not be held liable, for the alleged injuries caused by those who alter the product in a way that is unsafe or violates Federal and State laws and regulations.\n**(5)**\nThe possibility of imposing liability on an entire industry for alleged injuries that are solely caused by others is an abuse of the legal system, erodes public confidence in our Nation\u2019s laws, invites the disassembly and destabilization of other industries and economic sectors lawfully competing in the free enterprise system of the United States, and constitutes an unreasonable burden on interstate and foreign commerce of the United States.\n**(6)**\nA proliferation of frivolous lawsuits against manufacturers and sellers of stone slab products for alleged workplace injuries caused by the actions of third-parties unrelated to and beyond the control of these manufacturers and sellers may further limit access to courts by straining the resources of the legal system and depriving deserving parties of their legitimate rights to relief.\n##### (b) Purposes\nThe purposes of this Act are as follows:\n**(1)**\nTo prohibit civil actions against manufacturers and sellers of stone slab products for injuries caused by exposure to respirable silica or other substances arising from or relating to the fabrication of such products by third-parties.\n**(2)**\nTo preserve consumers\u2019 access to a supply of stone slab products, to protect manufacturers and sellers from frivolous civil actions alleging liability for such injuries, and to preserve a lawful industry that employs tens of thousands of Americans in several States.\n**(3)**\nTo prevent the use of such civil actions to impose unreasonable burdens on interstate and foreign commerce.\n**(4)**\nTo exercise congressional power under article IV, section 1 of the Constitution (the Full Faith and Credit Clause).\n#### 3. Prohibition on bringing of qualified civil actions in Federal or State court\n##### (a) In general\nA qualified civil action may not be brought in any Federal or State court.\n##### (b) Dismissal of pending actions\nA qualified civil action that is pending on the date of enactment of this Act shall be dismissed, as soon as is practicable after the date of enactment of this Act, by the court in which the action is pending.\n#### 4. Definitions\nIn this Act:\n**(1) Fabrication**\nThe term fabrication means the process of altering a qualified product by cutting, drilling, shaping, polishing, grinding, or other means.\n**(2) Qualified civil action**\nThe term qualified civil action means a civil action brought against a manufacturer or seller of a qualified product for injuries arising from or related to the fabrication by another party of a qualified product, including those caused by exposure to respirable silica or other substances.\n**(3) Qualified product**\nThe term qualified product means a stone slab product, including such a product made with quartz, mineral, crystal, glass, porcelain, or other stone, ceramic or similar material, that has been shipped or transported in interstate or foreign commerce.\n**(4) Seller**\nThe term seller means an importer, a distributer, a retailer, or a supplier of a qualified product.\n**(5) State**\nThe term State includes each of the several States of the United States, the District of Columbia, the Commonwealth of Puerto Rico, the United States Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands, and any other territory or possession of the United States, and any political subdivision of any such place.",
      "versionDate": "2025-09-17",
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
        "name": "Law",
        "updateDate": "2025-11-17T18:42:57Z"
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
      "date": "2025-09-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5437ih.xml"
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
      "title": "Protection of Lawful Commerce in Stone Slab Products Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-30T04:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protection of Lawful Commerce in Stone Slab Products Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-30T04:38:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit civil actions brought against a manufacturer or seller of a stone slab product for harm resulting from the alteration of such a product by a fabricator, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:22Z"
    }
  ]
}
```
