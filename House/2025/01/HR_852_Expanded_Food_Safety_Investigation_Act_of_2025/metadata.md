# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/852?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/852
- Title: Expanded Food Safety Investigation Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 852
- Origin chamber: House
- Introduced date: 2025-01-31
- Update date: 2025-12-05T22:00:04Z
- Update date including text: 2025-12-05T22:00:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-31: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-31: Introduced in House

## Actions

- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Introduced in House
- 2025-01-31 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-31",
    "latestAction": {
      "actionDate": "2025-01-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/852",
    "number": "852",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "D000216",
        "district": "3",
        "firstName": "Rosa",
        "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
        "lastName": "DeLauro",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Expanded Food Safety Investigation Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:00:04Z",
    "updateDateIncludingText": "2025-12-05T22:00:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-31",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-31",
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
          "date": "2025-01-31T15:08:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "G000551",
      "district": "7",
      "firstName": "Ra\u00fal",
      "fullName": "Rep. Grijalva, Ra\u00fal M. [D-AZ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Grijalva",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "AZ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "CA"
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
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "GA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "IN"
    },
    {
      "bioguideId": "M001196",
      "district": "6",
      "firstName": "Seth",
      "fullName": "Rep. Moulton, Seth [D-MA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Moulton",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MA"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MD"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "MI"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "WI"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr852ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 852\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 31, 2025 Ms. DeLauro (for herself, Mr. Grijalva , Ms. Brownley , Ms. Barrag\u00e1n , Ms. Norton , Mr. Johnson of Georgia , Ms. Schakowsky , Mr. Carson , Mr. Moulton , Mr. Ivey , Ms. Tlaib , and Ms. Meng ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide the Food and Drug Administration with authority to conduct microbial sampling on concentrated animal feeding operations as necessary to facilitate a foodborne illness outbreak investigation, determine the root cause of an outbreak of foodborne illness, or address other public health needs.\n#### 1. Short title\nThis Act may be cited as the Expanded Food Safety Investigation Act of 2025 .\n#### 2. Microbial sampling on concentrated animal feeding operations\n##### (a) In general\nChapter IV of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 341 et seq. ) is amended by adding at the end the following:\n425. Microbial sampling on concentrated animal feeding operations (a) In general The Secretary may request access to a concentrated animal feeding operation in order to conduct microbial sampling, if the Secretary determines that such microbial sampling is necessary in order to facilitate a foodborne illness outbreak investigation, determine the root cause of an outbreak of foodborne illness, or address other public health needs. (b) Granting of reasonable access A concentrated animal feeding operation that receives a request for access under subsection (a) shall provide reasonable access to the Secretary to conduct such microbial sampling, including sampling of plants, animals, water, and the environment, as the Secretary determines appropriate to address the public health need. Such operation may place reasonable conditions on access to the operation, including by specifying a time, place, and manner for sampling, provided that any such conditions do not prevent the Secretary from conducting appropriate sampling within a reasonable period of time. (c) Authority over foods regulated by the Secretary of Agriculture Nothing in this section shall be construed to impose additional requirements by the Secretary, beyond microbial sampling, with respect to food that is within the jurisdiction of the Secretary of Agriculture pursuant to the Federal Meat Inspection Act, the Poultry Products Inspection Act, or the Egg Products Inspection Act. (d) Coordination with other public health agencies The Secretary shall ensure that data collected under this section are made available to the Secretary of Agriculture and relevant State and Federal public health agencies in order to facilitate work in detecting, investigating, or preventing foodborne illness. Nothing in this section shall be construed to limit the rights and exemptions otherwise available under section 552 of title 5, United States Code. (e) Definition In this section, the term concentrated animal feeding operation has the meaning given such term in section 122.23(b) of title 40, Code of Federal Regulations (or any successor regulations). .\n##### (b) Enforcement\nSection 301 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 331 ) is amended by adding at the end the following:\n(jjj) The refusal to provide reasonable access for microbial sampling in accordance with section 425. .",
      "versionDate": "2025-01-31",
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
        "actionDate": "2025-02-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "376",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expanded Food Safety Investigation Act of 2025",
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
            "name": "Agricultural research",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Animal and plant health",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Food supply, safety, and labeling",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Livestock",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Meat",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Medical research",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Veterinary medicine and animal diseases",
            "updateDate": "2025-04-11T14:27:52Z"
          },
          {
            "name": "Water quality",
            "updateDate": "2025-04-11T14:27:52Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-03-03T19:23:44Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-31",
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
          "measure-id": "id119hr852",
          "measure-number": "852",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-31",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr852v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-31",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Expanded Food Safety Investigation Act of </strong><strong>2025</strong></p><p>This bill provides that the Food and Drug Administration (FDA) may, under specified circumstances,\u00a0request access to a concentrated animal-feeding operation (i.e., a stabled or confined animal-feeding operation of a specified size) to conduct microbial sampling.</p><p>Specifically, the bill allows the FDA to request access if the FDA determines that sampling is necessary to facilitate an investigation of a foodborne-illness outbreak, determine the cause of an outbreak, or address other public health needs. Concentrated animal-feeding operations must provide reasonable access for sampling, including sampling of plants, animals, water, and the environment. The bill imposes penalties on operations that refuse to provide reasonable access.\u00a0</p><p>Data collected in sampling efforts under this bill must be shared with the Department of Agriculture and state and federal public health agencies to facilitate the detection, investigation, and prevention of foodborne illness.</p><p></p>"
        },
        "title": "Expanded Food Safety Investigation Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr852.xml",
    "summary": {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanded Food Safety Investigation Act of </strong><strong>2025</strong></p><p>This bill provides that the Food and Drug Administration (FDA) may, under specified circumstances,\u00a0request access to a concentrated animal-feeding operation (i.e., a stabled or confined animal-feeding operation of a specified size) to conduct microbial sampling.</p><p>Specifically, the bill allows the FDA to request access if the FDA determines that sampling is necessary to facilitate an investigation of a foodborne-illness outbreak, determine the cause of an outbreak, or address other public health needs. Concentrated animal-feeding operations must provide reasonable access for sampling, including sampling of plants, animals, water, and the environment. The bill imposes penalties on operations that refuse to provide reasonable access.\u00a0</p><p>Data collected in sampling efforts under this bill must be shared with the Department of Agriculture and state and federal public health agencies to facilitate the detection, investigation, and prevention of foodborne illness.</p><p></p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr852"
    },
    "title": "Expanded Food Safety Investigation Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-31",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Expanded Food Safety Investigation Act of </strong><strong>2025</strong></p><p>This bill provides that the Food and Drug Administration (FDA) may, under specified circumstances,\u00a0request access to a concentrated animal-feeding operation (i.e., a stabled or confined animal-feeding operation of a specified size) to conduct microbial sampling.</p><p>Specifically, the bill allows the FDA to request access if the FDA determines that sampling is necessary to facilitate an investigation of a foodborne-illness outbreak, determine the cause of an outbreak, or address other public health needs. Concentrated animal-feeding operations must provide reasonable access for sampling, including sampling of plants, animals, water, and the environment. The bill imposes penalties on operations that refuse to provide reasonable access.\u00a0</p><p>Data collected in sampling efforts under this bill must be shared with the Department of Agriculture and state and federal public health agencies to facilitate the detection, investigation, and prevention of foodborne illness.</p><p></p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr852"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr852ih.xml"
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
      "title": "Expanded Food Safety Investigation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-28T09:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expanded Food Safety Investigation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-28T09:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide the Food and Drug Administration with authority to conduct microbial sampling on concentrated animal feeding operations as necessary to facilitate a foodborne illness outbreak investigation, determine the root cause of an outbreak of foodborne illness, or address other public health needs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-28T09:03:29Z"
    }
  ]
}
```
