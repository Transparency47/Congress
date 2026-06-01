# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1172?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1172
- Title: Honor Farmer Contracts Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1172
- Origin chamber: Senate
- Introduced date: 2025-03-27
- Update date: 2025-11-05T12:03:17Z
- Update date including text: 2025-11-05T12:03:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-27: Introduced in Senate
- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-03-27: Introduced in Senate

## Actions

- 2025-03-27 - IntroReferral: Introduced in Senate
- 2025-03-27 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1172",
    "number": "1172",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001288",
        "district": "",
        "firstName": "Cory",
        "fullName": "Sen. Booker, Cory A. [D-NJ]",
        "lastName": "Booker",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Honor Farmer Contracts Act of 2025",
    "type": "S",
    "updateDate": "2025-11-05T12:03:17Z",
    "updateDateIncludingText": "2025-11-05T12:03:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T16:13:12Z",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "VT"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NM"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-03-27",
      "state": "ME"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MN"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "WI"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-27",
      "state": "VT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "RI"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-04-08",
      "state": "CA"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "MA"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NM"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1172is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1172\nIN THE SENATE OF THE UNITED STATES\nMarch 27, 2025 Mr. Booker (for himself, Ms. Duckworth , Mr. Welch , Mr. Schiff , Mr. Van Hollen , Mr. Wyden , Mr. Heinrich , Mrs. Gillibrand , Mr. King , Ms. Smith , Mr. Markey , Mr. Durbin , Mr. Blumenthal , Ms. Baldwin , Mr. Merkley , Mr. Sanders , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo unfreeze funding for contracts of the Department of Agriculture, to prohibit Farm Service Agency and Natural Resources Conservation Service office closures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Honor Farmer Contracts Act of 2025 .\n#### 2. Department of Agriculture funding and offices\nThe Secretary of Agriculture\u2014\n**(1)**\nshall, immediately after the enactment of this Act, unfreeze funding for and implement all agreements and contracts entered into by the Secretary of Agriculture prior to the date of enactment of this Act;\n**(2)**\nshall, as rapidly as possible after the enactment of this Act, pay all past due amounts owed by the Secretary of Agriculture under the agreements and contracts described in paragraph (1);\n**(3)**\nshall not cancel any signed agreement or contract with a farmer or an entity providing assistance to farmers, unless the farmer or entity has failed to comply with the terms and conditions of the agreement or contract; and\n**(4)**\nshall not close any Farm Service Agency county office, Natural Resources Conservation Service field office, or Rural Development Service Center without providing written notice and justification to Congress not later than 60 days before the date on which the applicable office is intended to be closed.",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-05-06T17:36:11Z"
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
          "measure-id": "id119s1172",
          "measure-number": "1172",
          "measure-type": "s",
          "orig-publish-date": "2025-03-27",
          "originChamber": "SENATE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1172v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-03-27",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Honor Farmer Contracts Act of 2025</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the agreement or contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>"
        },
        "title": "Honor Farmer Contracts Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1172.xml",
    "summary": {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Honor Farmer Contracts Act of 2025</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the agreement or contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1172"
    },
    "title": "Honor Farmer Contracts Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-27",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Honor Farmer Contracts Act of 2025</strong></p><p>This bill requires the Department of Agriculture (USDA) to unfreeze funding for agreements and contracts and\u00a0prohibits USDA from closing certain offices and service centers without notifying Congress in advance.</p><p>Specifically, USDA must (1) unfreeze funding for, and implement, all agreements and contracts entered into by USDA prior to the bill's enactment; and (2) pay all related past due amounts owed by USDA as rapidly as possible.</p><p>Further, the bill prohibits USDA from canceling a signed agreement or contract with a farmer or an entity providing assistance to farmers (unless the farmer or entity is not in compliance with the terms and conditions of the agreement or contract).</p><p>Finally, the bill prohibits USDA from closing Farm Service Agency county offices, Natural Resources Conservation Service field offices, or Rural Development Service Centers without providing written notice and a justification to Congress at least 60 days before the closure.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119s1172"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1172is.xml"
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
      "title": "Honor Farmer Contracts Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T12:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to unfreeze funding for contracts of the Department of Agriculture, to prohibit Farm Service Agency and Natural Resources Conservation Service office closures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T10:56:39Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Honor Farmer Contracts Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:18Z"
    }
  ]
}
```
