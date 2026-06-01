# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1463?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1463
- Title: Finding ORE Act
- Congress: 119
- Bill type: S
- Bill number: 1463
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-02-17T19:05:15Z
- Update date including text: 2026-02-17T19:05:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 93.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 93.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1463",
    "number": "1463",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Finding ORE Act",
    "type": "S",
    "updateDate": "2026-02-17T19:05:15Z",
    "updateDateIncludingText": "2026-02-17T19:05:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 93.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-06-18",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-05",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
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
        "item": [
          {
            "date": "2025-06-18T18:23:41Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-10T19:20:07Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "True",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "IN"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "TX"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1463is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1463\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Coons (for himself, Mr. Young , Mr. Hickenlooper , and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo allow the Secretary of the Interior to enter into memoranda of understanding for the purpose of scientific and technical cooperation in the mapping of critical minerals and rare earth elements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Finding Opportunities for Resource Exploration Act or the Finding ORE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Allied foreign country**\nThe term allied foreign country means a country with which the United States has entered into a mutual defense treaty or other mutual defense agreement.\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Partner foreign country**\nThe term partner foreign country means a country that is a source of a critical mineral or rare earth element.\n**(5) Rare earth element**\nThe term rare earth element means cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, or yttrium.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Geological Survey.\n#### 3. Memorandum of understanding with respect to the mapping of critical minerals and rare earth elements\n##### (a) Memorandum of understanding\nThe Secretary may enter into a memorandum of understanding with 1 or more heads of agencies of partner foreign countries with respect to scientific and technical cooperation in the mapping of critical minerals and rare earth elements.\n##### (b) Objectives\nIn negotiating a memorandum of understanding under subsection (a), the Secretary shall seek to increase the security and resilience of international supply chains for critical minerals and rare earth elements by\u2014\n**(1)**\ncommitting to assisting the partner foreign country through cooperative activities described in subsection (c) that help the partner foreign country map reserves of critical minerals and rare earth elements;\n**(2)**\nensuring that private companies headquartered in the United States or an allied foreign country are offered the right of first refusal in the further development of critical minerals and rare earth elements in the partner foreign country;\n**(3)**\nfacilitating private-sector investment in the exploration and development of critical minerals and rare earth elements, including by leveraging preferential financing from entities such as the United States International Development Finance Corporation and the Export-Import Bank of the United States that prioritizes projects committed to processing minerals in the United States or an allied foreign country; and\n**(4)**\nensuring that mapping data created through the cooperative activities described in subsection (c) is protected against unauthorized access by, or disclosure to, governmental or private entities based in countries that are not\u2014\n**(A)**\na party to the memorandum of understanding; or\n**(B)**\nan allied foreign country.\n##### (c) Cooperative activities\nThe cooperative activities referred to in subsection (b) include\u2014\n**(1)**\nacquisition, compilation, analysis, and interpretation of geologic, geophysical, geochemical, and spectroscopic remote sensing data;\n**(2)**\nprospectivity mapping and mineral resource assessment;\n**(3)**\nanalysis of geoscience data, including developing derivative map products that can help more effectively evaluate the mineral resources of the partner foreign country;\n**(4)**\nscientific collaboration to enhance the understanding and management of the natural resources of the partner foreign country to contribute to the sustainable development of the mineral resources sector of that partner foreign country;\n**(5)**\ntraining and capacity building in each area described in paragraphs (1) through (4);\n**(6)**\nfacilitation of education and specialized training in geoscience and mineral resource management at institutions of higher education;\n**(7)**\ntraining in relevant international standards for relevant officials of the government and private companies of the partner foreign country; and\n**(8)**\ncooperation among entities of the partner foreign country that are a party to the memorandum of understanding and entities in the United States, including Federal departments and agencies, institutions of higher education, research centers, and private companies.\n##### (d) Notification to Congress\nThe Secretary shall notify Congress not later than 30 days before the Secretary intends to enter into a memorandum of understanding under subsection (a).\n##### (e) Collaboration with Secretary of State\nThe Secretary shall collaborate with the Secretary of State in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a);\n**(2)**\nnegotiating a memorandum of understanding under subsection (a); and\n**(3)**\nimplementing a memorandum of understanding entered into under subsection (a).\n##### (f) Consultation with private sector\nThe Secretary shall consult with relevant private sector actors, as the Secretary determines to be appropriate, in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a); and\n**(2)**\nassessing how a memorandum of understanding can best facilitate private sector interest in pursuing the further development of critical minerals and rare earth elements in accordance with the objectives described in subsection (b).",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1463rs.xml",
      "text": "II\nCalendar No. 93\n119th CONGRESS\n1st Session\nS. 1463\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Coons (for himself, Mr. Young , Mr. Hickenlooper , Mr. Cornyn , and Mr. Cruz ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo allow the Secretary of the Interior to enter into memoranda of understanding for the purpose of scientific and technical cooperation in the mapping of critical minerals and rare earth elements, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Finding Opportunities for Resource Exploration Act or the Finding ORE Act .\n#### 2. Definitions\nIn this Act:\n**(1) Allied foreign country**\nThe term allied foreign country means a country with which the United States has entered into a mutual defense treaty or other mutual defense agreement.\n**(2) Critical mineral**\nThe term critical mineral has the meaning given the term in section 7002(a) of the Energy Act of 2020 ( 30 U.S.C. 1606(a) ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Partner foreign country**\nThe term partner foreign country means a country that is a source of a critical mineral or rare earth element.\n**(5) Rare earth element**\nThe term rare earth element means cerium, dysprosium, erbium, europium, gadolinium, holmium, lanthanum, lutetium, neodymium, praseodymium, promethium, samarium, scandium, terbium, thulium, ytterbium, or yttrium.\n**(6) Secretary**\nThe term Secretary means the Secretary of the Interior, acting through the Director of the United States Geological Survey.\n#### 3. Memorandum of understanding with respect to the mapping of critical minerals and rare earth elements\n##### (a) Memorandum of understanding\nThe Secretary may enter into a memorandum of understanding with 1 or more heads of agencies of partner foreign countries with respect to scientific and technical cooperation in the mapping of critical minerals and rare earth elements.\n##### (b) Objectives\nIn negotiating a memorandum of understanding under subsection (a), the Secretary shall seek to increase the security and resilience of international supply chains for critical minerals and rare earth elements by\u2014\n**(1)**\ncommitting to assisting the partner foreign country through cooperative activities described in subsection (c) that help the partner foreign country map reserves of critical minerals and rare earth elements;\n**(2)**\nensuring that private companies headquartered in the United States or an allied foreign country are offered the right of first refusal in the further development of critical minerals and rare earth elements in the partner foreign country;\n**(3)**\nfacilitating private-sector investment in the exploration and development of critical minerals and rare earth elements, including by leveraging preferential financing from entities such as the United States International Development Finance Corporation and the Export-Import Bank of the United States that prioritizes projects committed to processing minerals in the United States or an allied foreign country; and\n**(4)**\nensuring that mapping data created through the cooperative activities described in subsection (c) is protected against unauthorized access by, or disclosure to, governmental or private entities based in countries that are not\u2014\n**(A)**\na party to the memorandum of understanding; or\n**(B)**\nan allied foreign country.\n##### (c) Cooperative activities\nThe cooperative activities referred to in subsection (b) include\u2014\n**(1)**\nacquisition, compilation, analysis, and interpretation of geologic, geophysical, geochemical, and spectroscopic remote sensing data;\n**(2)**\nprospectivity mapping and mineral resource assessment;\n**(3)**\nanalysis of geoscience data, including developing derivative map products that can help more effectively evaluate the mineral resources of the partner foreign country;\n**(4)**\nscientific collaboration to enhance the understanding and management of the natural resources of the partner foreign country to contribute to the sustainable development of the mineral resources sector of that partner foreign country;\n**(5)**\ntraining and capacity building in each area described in paragraphs (1) through (4);\n**(6)**\nfacilitation of education and specialized training in geoscience and mineral resource management at institutions of higher education;\n**(7)**\ntraining in relevant international standards for relevant officials of the government and private companies of the partner foreign country; and\n**(8)**\ncooperation among entities of the partner foreign country that are a party to the memorandum of understanding and entities in the United States, including Federal departments and agencies, institutions of higher education, research centers, and private companies.\n##### (d) Notification to Congress\nThe Secretary shall notify Congress not later than 30 days before the Secretary intends to enter into a memorandum of understanding under subsection (a).\n##### (e) Collaboration with Secretary of State\nThe Secretary shall collaborate with the Secretary of State in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a);\n**(2)**\nnegotiating a memorandum of understanding under subsection (a); and\n**(3)**\nimplementing a memorandum of understanding entered into under subsection (a).\n##### (f) Consultation with private sector\nThe Secretary shall consult with relevant private sector actors, as the Secretary determines to be appropriate, in\u2014\n**(1)**\nprioritizing and selecting partner foreign countries with which to enter into a memorandum of understanding under subsection (a); and\n**(2)**\nassessing how a memorandum of understanding can best facilitate private sector interest in pursuing the further development of critical minerals and rare earth elements in accordance with the objectives described in subsection (b).",
      "versionDate": "2025-06-18",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-04-17",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2969",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Finding ORE Act",
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
            "name": "Employment and training programs",
            "updateDate": "2025-06-09T14:52:44Z"
          },
          {
            "name": "Geography and mapping",
            "updateDate": "2025-06-09T14:50:35Z"
          },
          {
            "name": "Materials",
            "updateDate": "2025-06-09T14:54:26Z"
          },
          {
            "name": "Metals",
            "updateDate": "2025-06-09T14:54:15Z"
          },
          {
            "name": "Mining",
            "updateDate": "2025-06-09T14:46:39Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2025-06-09T14:51:05Z"
          },
          {
            "name": "Strategic materials and reserves",
            "updateDate": "2025-06-09T14:54:03Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-14T18:55:29Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1463is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1463rs.xml"
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
      "title": "Finding ORE Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Finding Opportunities for Resource Exploration Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "title": "Finding ORE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Finding ORE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Finding Opportunities for Resource Exploration Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to allow the Secretary of the Interior to enter into memoranda of understanding for the purpose of scientific and technical cooperation in the mapping of critical minerals and rare earth elements, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:41Z"
    }
  ]
}
```
