# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1926?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1926
- Title: Reducing Waste in National Parks Act
- Congress: 119
- Bill type: S
- Bill number: 1926
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-09 - Committee: Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1926",
    "number": "1926",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
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
    "title": "Reducing Waste in National Parks Act",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-09",
      "committees": {
        "item": {
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on National Parks. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-02",
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
          "date": "2025-06-02T22:14:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-09T18:13:11Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "National Parks Subcommittee",
          "systemCode": "sseg04"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "IL"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "PA"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "CT"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-06-02",
      "state": "VT"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MD"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "MA"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "RI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "VT"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1926is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1926\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mr. Merkley (for himself, Ms. Duckworth , Mr. Fetterman , Mr. Murphy , Mr. Sanders , Mr. Van Hollen , Ms. Warren , Mr. Whitehouse , Mr. Wyden , and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo encourage reduction of disposable plastic products in units of the National Park System, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Reducing Waste in National Parks Act .\n#### 2. Disposable plastic products reduction in units of the National Park System\n##### (a) Program for reduction of disposable plastic products in units of the NPS\nNot later than 180 days after the date of the enactment of this Act, the Director shall establish, for the National Park System a program for reduction of disposable plastic products and, if applicable, elimination of the sale and distribution of disposable plastic products under subsection (b). Each regional director shall implement the plan for park units in their region.\n##### (b) Elimination of sale and distribution of disposable plastic products\n**(1) In general**\nEach regional director concerned shall eliminate the sale of water in disposable plastic products and the sale and distribution of other disposable plastic products to the greatest extent feasible in the relevant unit of the National Park System after consideration of the following factors, when applicable, with respect to the relevant unit:\n**(A)**\nThe costs and benefits to the overall operations.\n**(B)**\nThe amount of waste that would be eliminated.\n**(C)**\nThe infrastructure costs and funding sources for bottle refill stations.\n**(D)**\nAny contractual implications with respect to concessioners, including considerations of new leaseholder surrender interest or possessory interest.\n**(E)**\nThe operational costs of bottle refill stations, including utilities and regular public health testing.\n**(F)**\nThe cost and availability of bisphenol A-free reusable containers.\n**(G)**\nThe effect on concessioner and cooperation association sales revenue.\n**(H)**\nThe availability of water within concession food service operations.\n**(I)**\nThe ability to provide visitor education in the unit and online so that visitors may come prepared with their own water bottles.\n**(J)**\nInput from the National Park Service Office of Public Health.\n**(K)**\nThe feasibility of posting signs so that visitors can easily find bottle refill stations.\n**(L)**\nSafety considerations for visitors who may resort to not carrying enough water or drinking from surface water sources with potential exposure to disease.\n**(M)**\nAny input from concessioners and cooperating associations within the relevant unit.\n**(2) Units of NPS previously eliminated sale of water in disposable plastic products**\nWith respect to a unit of the National Park System that did not offer for sale water in disposable plastic products before the date of the enactment of this Act, the applicable superintendent of the relevant unit may continue to not offer for sale water in disposable plastic bottles.\n##### (c) Proactive visitor education strategy\nEach regional director concerned shall develop for the relevant unit of the National Park System a proactive visitor education strategy to address visitor expectations of water availability and explain the rationale for the program and its implementation in the relevant unit.\n##### (d) Continuity within unit of the NPS\nEach regional director concerned shall, to the extent possible, implement the program in a manner that is consistent throughout the relevant unit of the National Park System, including incorporation of such program into any agreement with an organization operating within the relevant unit, including a concessioner operating plan and cooperating association scope of sales.\n##### (e) Biennial evaluation\nEach regional director concerned shall, not less than once every 2 years\u2014\n**(1)**\nconduct an evaluation of the program for the relevant unit of the National Park System, including\u2014\n**(A)**\npublic response to the program;\n**(B)**\nvisitor satisfaction with the availability of water;\n**(C)**\nbuying behavior with respect to products sold in disposable plastic products;\n**(D)**\npublic safety including information on cases of dehydration or exposure to disease from drinking from surface water; and\n**(E)**\ndisposable plastic bottle collection rates; and\n**(2)**\nsubmit the evaluation to the Director and the Secretary of the Interior.\n##### (f) Definitions\nFor the purposes of this Act\u2014\n**(1)**\nthe term Director means the Director of the National Park Service;\n**(2)**\nthe term disposable plastic products includes\u2014\n**(A)**\ndisposable plastic beverage bottles;\n**(B)**\ncarryout bags made from film plastic;\n**(C)**\nplastic food ware, including plastic food ware products marketed as compostable or biodegradable; and\n**(D)**\nexpanded polystyrene products;\n**(3)**\nthe term program means the program for recycling and reduction of disposable plastic products established under subsection (a); and\n**(4)**\nthe term regional director concerned means, with respect to a unit of the National Park System, the regional director of the region of the National Park System in which the relevant unit is located, working in coordination with the superintendent of such unit.",
      "versionDate": "2025-06-02",
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
        "actionDate": "2025-05-23",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "3604",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Reducing Waste in National Parks Act",
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
            "name": "Parks, recreation areas, trails",
            "updateDate": "2025-12-16T15:51:24Z"
          },
          {
            "name": "Solid waste and recycling",
            "updateDate": "2025-12-16T15:51:24Z"
          },
          {
            "name": "Water use and supply",
            "updateDate": "2025-12-16T15:51:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-14T17:26:55Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1926is.xml"
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
      "title": "Reducing Waste in National Parks Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reducing Waste in National Parks Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to encourage reduction of disposable plastic products in units of the National Park System, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:34Z"
    }
  ]
}
```
