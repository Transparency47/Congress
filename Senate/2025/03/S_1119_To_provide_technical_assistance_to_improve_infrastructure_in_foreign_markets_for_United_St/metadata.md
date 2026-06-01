# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1119?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1119
- Title: FRIDGE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1119
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2025-12-17T12:03:15Z
- Update date including text: 2025-12-17T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1119",
    "number": "1119",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "FRIDGE Act of 2025",
    "type": "S",
    "updateDate": "2025-12-17T12:03:15Z",
    "updateDateIncludingText": "2025-12-17T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T19:37:29Z",
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
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "PA"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1119is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1119\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Banks (for himself and Mr. Fetterman ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo provide technical assistance to improve infrastructure in foreign markets for United States agricultural commodities.\n#### 1. Short title\nThis Act may be cited as the Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nOne of the largest limiting factors to growing export markets for United States food and agriculture products is insufficient infrastructure capabilities.\n**(2)**\nCurrent trade programs are focused on promoting specific commodities or products, all of which are reliant on a functioning supply chain.\n**(3)**\nThere is a need for dedicated resources to focus on supply chain enhancement in developing countries to enable market expansion and diversification.\n**(4)**\nEach year, billions of tons of fresh and frozen food products and millions of dollars\u2019 worth of United States exports are lost due to poor cold chain systems in developing markets.\n**(5)**\nStrengthening global infrastructure plays an important role in promoting trade, reducing food loss and waste, and improving nutrition.\n#### 3. Technical assistance to improve infrastructure in foreign markets for United States agricultural commodities\nSection 203(c) of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5623(c) ) is amended by adding at the end the following:\n(4) Technical assistance to improve infrastructure in foreign markets for United States agricultural commodities (A) In general As part of the program established under this subsection, the Secretary shall enter into contracts or other agreements with eligible trade organizations to provide needs assessments, training, and other technical assistance to enhance the capabilities of infrastructure in new and developing foreign markets, including infrastructure relating to cold chain capacity, port improvements, and other developments, to ensure United States agricultural commodities are not damaged or lost due to deficiencies of such infrastructure. (B) Authorization of appropriations (i) In general There is authorized to be appropriated to carry out this paragraph $1,000,000 for each of the fiscal years 2026 through 2030. (ii) Rule of construction Amounts authorized to be appropriated under this subparagraph may be used only for the purposes described in subparagraph (A). (iii) Availability Amounts authorized to be appropriated under this subparagraph that are not used to carry out this paragraph are authorized to be made available to carry out the program established under this subsection. .",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-03-25",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "2322",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FRIDGE Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-12T18:12:48Z"
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
          "measure-id": "id119s1119",
          "measure-number": "1119",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-05-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1119v00",
            "update-date": "2025-05-13"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>"
        },
        "title": "FRIDGE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1119.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1119"
    },
    "title": "FRIDGE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025 or the FRIDGE Act of 2025 </strong></p><p>This bill expands the Foreign Market Development Cooperator Program to include funding for technical assistance for infrastructure-related projects to ensure U.S. agricultural commodities are not damaged or lost due to infrastructure deficiencies in new and developing markets. This Foreign Agricultural Service (FAS) program funds projects that address long-term opportunities to reduce foreign import constraints or expand export growth opportunities.</p><p>Specifically, the bill directs FAS to enter into contracts or other agreements with trade organizations to enhance the infrastructure capabilities (including cold chain capacity and port improvements) in new and developing foreign markets through needs assessments, training, and other technical assistance.</p>",
      "updateDate": "2025-05-13",
      "versionCode": "id119s1119"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1119is.xml"
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
      "title": "FRIDGE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FRIDGE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fortifying Refrigeration Infrastructure and Developing Global Exports Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide technical assistance to improve infrastructure in foreign markets for United States agricultural commodities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:23Z"
    }
  ]
}
```
