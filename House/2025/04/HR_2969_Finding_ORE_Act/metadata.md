# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2969?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2969
- Title: Finding ORE Act
- Congress: 119
- Bill type: HR
- Bill number: 2969
- Origin chamber: House
- Introduced date: 2025-04-17
- Update date: 2026-02-25T09:06:34Z
- Update date including text: 2026-02-25T09:06:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-17: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held
- Latest action: 2025-04-17: Introduced in House

## Actions

- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Introduced in House
- 2025-04-17 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-02-17 - Committee: Referred to the Subcommittee on Energy and Mineral Resources.
- 2026-02-24 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-17",
    "latestAction": {
      "actionDate": "2025-04-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2969",
    "number": "2969",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Finding ORE Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:34Z",
    "updateDateIncludingText": "2026-02-25T09:06:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-24",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-17",
      "committees": {
        "item": {
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Energy and Mineral Resources.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-17",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-17",
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
          "date": "2025-04-17T13:30:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-02-24T15:30:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-02-17T16:00:00Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Energy and Mineral Resources Subcommittee",
          "systemCode": "hsii06"
        }
      },
      "systemCode": "hsii00",
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
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "IL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "FL"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "MI"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-04-17",
      "state": "NY"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "VA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-07",
      "state": "MI"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2969ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2969\nIN THE HOUSE OF REPRESENTATIVES\nApril 17, 2025 Mr. Wittman (for himself, Ms. Castor of Florida , Mr. Moolenaar , Mr. Krishnamoorthi , Mr. Lawler , Ms. Houlahan , Mr. Gimenez , Ms. Stevens , and Mr. Torres of New York ) introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo allow the Secretary of the Interior to enter into memoranda of understanding for the purpose of scientific and technical cooperation in the mapping of critical minerals and rare earth elements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Finding Opportunities for Resource Exploration Act or the Finding ORE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Allied foreign country**\nThe term allied foreign country means a country with which the United States has entered into a mutual defense treaty or other mutual defense agreement.\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Partner foreign country**\nThe term partner foreign country means a country that is a source of a critical mineral or rare earth element.\n**(5) Rare earth element**\nThe term rare earth element means cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, or yttrium.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Geological Survey.\n#### 3. Memorandum of understanding with respect to the mapping of critical minerals and rare earth elements\n##### (a) Memorandum of understanding\nThe Secretary may enter into a memorandum of understanding with 1 or more heads of agencies of partner foreign countries with respect to scientific and technical cooperation in the mapping of critical minerals and rare earth elements.\n##### (b) Objectives\nIn negotiating a memorandum of understanding under subsection (a), the Secretary shall seek to increase the security and resilience of international supply chains for critical minerals and rare earth elements by\u2014\n**(1)**\ncommitting to assisting the partner foreign country through cooperative activities described in subsection (c) that help the partner foreign country map reserves of critical minerals and rare earth elements;\n**(2)**\nensuring that private companies headquartered in the United States or an allied foreign country are offered the right of first refusal in the further development of critical minerals and rare earth elements in the partner foreign country;\n**(3)**\nfacilitating private-sector investment in the exploration and development of critical minerals and rare earth elements, including by leveraging preferential financing from entities such as the United States International Development Finance Corporation and the Export-Import Bank of the United States that prioritizes projects committed to processing minerals in the United States or an allied foreign country; and\n**(4)**\nensuring that mapping data created through the cooperative activities described in subsection (c) is protected against unauthorized access by, or disclosure to, governmental or private entities based in countries that are not\u2014\n**(A)**\na party to the memorandum of understanding; or\n**(B)**\nan allied foreign country.\n##### (c) Cooperative activities\nThe cooperative activities referred to in subsection (b) include\u2014\n**(1)**\nacquisition, compilation, analysis, and interpretation of geologic, geophysical, geochemical, and spectroscopic remote sensing data;\n**(2)**\nprospectivity mapping and mineral resource assessment;\n**(3)**\nanalysis of geoscience data, including developing derivative map products that can help more effectively evaluate the mineral resources of the partner foreign country;\n**(4)**\nscientific collaboration to enhance the understanding and management of the natural resources of the partner foreign country to contribute to the sustainable development of the mineral resources sector of that partner foreign country;\n**(5)**\ntraining and capacity building in each area described in paragraphs (1) through (4);\n**(6)**\nfacilitation of education and specialized training in geoscience and mineral resource management at institutions of higher education;\n**(7)**\ntraining in environmental and workplace standards for relevant officials of the government and private companies of the partner foreign country; and\n**(8)**\ncooperation among entities of the partner foreign country that are a party to the memorandum of understanding and entities in the United States, including Federal departments and agencies, institutions of higher education, research centers, and private companies.\n##### (d) Notification to Congress\nThe Secretary shall notify Congress not later than 30 days before the Secretary intends to enter into a memorandum of understanding under subsection (a).\n##### (e) Collaboration with Secretary of State\nThe Secretary shall collaborate with the Secretary of State in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a);\n**(2)**\nnegotiating a memorandum of understanding under subsection (a); and\n**(3)**\nimplementing a memorandum of understanding entered into under subsection (a).\n##### (f) Consultation with private sector\nThe Secretary shall consult with relevant private sector actors, as the Secretary determines to be appropriate, in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a); and\n**(2)**\nassessing how a memorandum of understanding can best facilitate private sector interest in pursuing the further development of critical minerals and rare earth elements in accordance with the objectives described in subsection (b).",
      "versionDate": "2025-04-17",
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
        "actionDate": "2025-06-18",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 93."
      },
      "number": "1463",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Finding ORE Act",
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
            "name": "Employment and training programs",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Materials",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Metals",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-06-10T15:47:36Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2025-06-10T15:47:36Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-27T15:34:09Z"
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
      "date": "2025-04-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2969ih.xml"
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
      "title": "Finding ORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Finding ORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Finding Opportunities for Resource Exploration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow the Secretary of the Interior to enter into memoranda of understanding for the purpose of scientific and technical cooperation in the mapping of critical minerals and rare earth elements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T03:03:22Z"
    }
  ]
}
```
