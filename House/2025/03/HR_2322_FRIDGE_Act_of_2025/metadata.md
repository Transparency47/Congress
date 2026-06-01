# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2322?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2322
- Title: FRIDGE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2322
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2025-12-05T22:47:35Z
- Update date including text: 2025-12-05T22:47:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-03-25: Introduced in House

## Actions

- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2322",
    "number": "2322",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "FRIDGE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:47:35Z",
    "updateDateIncludingText": "2025-12-05T22:47:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "KS"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NC"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "MN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2322ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2322\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. Feenstra (for himself, Mr. Mann , Mr. Costa , and Mr. Carbajal ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide technical assistance to improve infrastructure in foreign markets for United States agricultural commodities.\n#### 1. Short title\nThis Act may be cited as the Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOne of the largest limiting factors to growing export markets for United States food and agriculture products is insufficient infrastructure capabilities.\n**(2)**\nCurrent trade programs are focused on promoting specific commodities or products, all of which are reliant on a functioning supply chain.\n**(3)**\nThere is a need for dedicated resources to focus on supply chain enhancement in developing countries to enable market expansion and diversification.\n**(4)**\nEach year, billions of tons of fresh and frozen food products and millions of dollars\u2019 worth of United States exports are lost due to poor cold chain systems in developing markets.\n**(5)**\nStrengthening global infrastructure plays an important role in promoting trade, reducing food loss and waste, and improving nutrition.\n#### 3. Technical assistance to improve infrastructure in foreign markets for United States agricultural commodities\nSection 203(c) of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5623(c) ) is amended by adding at the end the following:\n(4) Technical assistance to improve infrastructure in foreign markets for United States agricultural commodities (A) In general As part of the program established under this subsection, the Secretary shall enter into contracts or other agreements with eligible trade organizations to provide needs assessments, training, and other technical assistance to enhance the capabilities of infrastructure in new and developing foreign markets, including infrastructure relating to cold chain capacity, port improvements, and other developments, to ensure United States agricultural commodities are not damaged or lost due to deficiencies of such infrastructure. (B) Authorization of appropriations (i) In general There is authorized to be appropriated to carry out this paragraph $1,000,000 for each of the fiscal years 2026 through 2030. (ii) Rule of construction Amounts authorized to be appropriated under this subparagraph may be used only for the purposes described in subparagraph (A). (iii) Availability Amounts authorized to be appropriated under this subparagraph that are not used to carry out this paragraph are authorized to be made available to carry out the program established under this subsection. .",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-25",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "1119",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FRIDGE Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-12T18:10:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119hr2322",
          "measure-number": "2322",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-25",
          "originChamber": "HOUSE",
          "update-date": "2025-05-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2322v00",
            "update-date": "2025-05-12"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>"
        },
        "title": "FRIDGE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2322.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr2322"
    },
    "title": "FRIDGE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>",
      "updateDate": "2025-05-12",
      "versionCode": "id119hr2322"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2322ih.xml"
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
      "title": "FRIDGE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-04T05:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FRIDGE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-04T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide technical assistance to improve infrastructure in foreign markets for United States agricultural commodities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-04T05:03:48Z"
    }
  ]
}
```
