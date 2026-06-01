# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2396
- Title: Honor Farmer Contracts Act
- Congress: 119
- Bill type: HR
- Bill number: 2396
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-07-17T11:31:10Z
- Update date including text: 2025-07-17T11:31:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-04-18 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2396",
    "number": "2396",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "V000136",
        "district": "2",
        "firstName": "Gabe",
        "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
        "lastName": "Vasquez",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "Honor Farmer Contracts Act",
    "type": "HR",
    "updateDate": "2025-07-17T11:31:10Z",
    "updateDateIncludingText": "2025-07-17T11:31:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-18",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:07:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-04-18T21:10:00Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "L000273",
      "district": "3",
      "firstName": "Teresa",
      "fullName": "Rep. Leger Fernandez, Teresa [D-NM-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Leger Fernandez",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NM"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "HI"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "MD"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "IL"
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "KS"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2396ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2396\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Vasquez (for himself, Ms. Pingree , Mr. Riley of New York , and Mr. McGovern ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo unfreeze funding for contracts of the Department of Agriculture, to prohibit Farm Service Agency and Natural Resources Conservation Service office closures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honor Farmer Contracts Act .\n#### 2. Department of Agriculture funding and offices\nThe Secretary of Agriculture shall\u2014\n**(1)**\nimmediately after the enactment of this Act, unfreeze funding for and implement all written agreements and contracts entered into by the Secretary of Agriculture prior to the date of enactment of this Act;\n**(2)**\nas rapidly as possible after the enactment of this Act, pay all past due amounts owed by the Secretary of Agriculture under agreements and contracts described in paragraph (1);\n**(3)**\nnot cancel any signed agreement or contract with a farmer or an entity providing assistance to farmers, unless the farmer or entity has failed to comply with the terms and conditions of the contract; and\n**(4)**\nnot close any Farm Service Agency county office, Natural Resources Conservation Service field office, or Rural Development Local Service Center without providing written notice and justification to Congress not later than 60 days before the date on which the applicable office or center is intended to be closed.",
      "versionDate": "2025-03-27",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-06T17:21:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-27",
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
          "measure-id": "id119hr2396",
          "measure-number": "2396",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-27",
          "originChamber": "HOUSE",
          "update-date": "2025-06-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2396v00",
            "update-date": "2025-06-25"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Honor Farmer Contracts Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>"
        },
        "title": "Honor Farmer Contracts Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2396.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honor Farmer Contracts Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2396"
    },
    "title": "Honor Farmer Contracts Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Honor Farmer Contracts Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>",
      "updateDate": "2025-06-25",
      "versionCode": "id119hr2396"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2396ih.xml"
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
      "title": "Honor Farmer Contracts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:10Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honor Farmer Contracts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-06T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To unfreeze funding for contracts of the Department of Agriculture, to prohibit Farm Service Agency and Natural Resources Conservation Service office closures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:48:24Z"
    }
  ]
}
```
