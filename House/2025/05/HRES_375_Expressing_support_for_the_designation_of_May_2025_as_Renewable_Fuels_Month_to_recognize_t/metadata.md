# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/375?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/375
- Title: Expressing support for the designation of May 2025 as "Renewable Fuels Month" to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.
- Congress: 119
- Bill type: HRES
- Bill number: 375
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-05-29T17:00:19Z
- Update date including text: 2026-05-29T17:00:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House
- 2026-01-22 11:53:10 - Floor: Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.
- 2026-01-22 11:53:10 - Floor: Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.
- Latest action: 2025-05-01: Submitted in House

## Actions

- 2025-05-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-05-01 - IntroReferral: Submitted in House
- 2025-05-01 - IntroReferral: Submitted in House
- 2026-01-22 11:53:10 - Floor: Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.
- 2026-01-22 11:53:10 - Floor: Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/375",
    "number": "375",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Expressing support for the designation of May 2025 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.",
    "type": "HRES",
    "updateDate": "2026-05-29T17:00:19Z",
    "updateDateIncludingText": "2026-05-29T17:00:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H1B000",
      "actionDate": "2026-01-22",
      "actionTime": "11:53:10",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.",
      "type": "Floor"
    },
    {
      "actionCode": "8000",
      "actionDate": "2026-01-22",
      "actionTime": "11:53:10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Pursuant to the provisions of H. Res. 1014, H. Res. 375 is considered passed House as amended.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-01T13:05:00Z",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "H001091",
      "district": "2",
      "firstName": "Ashley",
      "fullName": "Rep. Hinson, Ashley [R-IA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Hinson",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "NE"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
    },
    {
      "bioguideId": "P000607",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Pocan, Mark [D-WI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Pocan",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "WI"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "MN"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "IL"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-05-01",
      "state": "IA"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "IN"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "MI"
    },
    {
      "bioguideId": "W000812",
      "district": "2",
      "firstName": "Ann",
      "fullName": "Rep. Wagner, Ann [R-MO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Wagner",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres375ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 375\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Nunn of Iowa (for himself, Ms. Craig , Mrs. Hinson , Mr. Flood , Ms. Budzinski , Mr. Smith of Nebraska , Mr. Bacon , Mr. Finstad , Mrs. Miller-Meeks , Mr. Pocan , Mr. Stauber , Mr. Sorensen , and Mr. Feenstra ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of May 2025 as Renewable Fuels Month to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of Renewable Fuels Month ; and\n**(2)**\nrecognizes\u2014\n**(A)**\nthe important role renewable fuels play in reducing the carbon impact of the United States;\n**(B)**\nthe ability of renewable fuels to lower fuel prices for consumers;\n**(C)**\nthe support to rural communities that renewable fuel industries provide; and\n**(D)**\nthe opportunity that the production of renewable fuels provides to lessen the reliance of the United States on foreign adversaries.",
      "versionDate": "2025-05-01",
      "versionType": "IH"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres375eh.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 375\nIn the House of Representatives, U. S.,\nJanuary 22, 2026\nRESOLUTION\nExpressing support for the designation of May 2025 as Renewable Fuels Month to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.\nThat the House of Representatives\u2014\n**(1)**\nestablishes the E\u201315 Rural Domestic Energy Council ( Council ), appointed by the Speaker of the House, to develop legislative solutions to address the crisis facing our nation\u2019s farmers and refiners.\n**(2)**\ndirects the Council to investigate topics including, but not limited to, the sale of Ethanol-15, U.S. refinery capacity, the Renewable Fuel Standard Program, Renewable Identification Numbers, access to markets, and federal regulations that hinder American energy dominance.\n**(3)**\ndirects the Council to meet regularly to develop legislative solutions and to submit those solutions to Congress no later than February 15, 2026, with the intent to consider legislation no later than February 25, 2026.",
      "versionDate": "2026-01-22",
      "versionType": "EH"
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
        "actionDate": "2026-05-21",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1315",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of May 2026 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in lowering fuel prices for consumers, lessening reliance on foreign adversaries, supporting rural communities, and reducing carbon impacts.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-05-21",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Voice Vote. (consideration: CR S2435; text: CR S2445)"
      },
      "number": "747",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of May 2026 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in lowering fuel prices for consumers, lessening reliance on foreign adversaries, supporting rural communities, and reducing carbon impacts.",
      "type": "SRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-01-22",
        "actionTime": "11:52:34",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1014",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "House",
          "type": "Procedurally related"
        }
      },
      "title": "Providing for consideration of the bill (H.R. 7148) making further consolidated appropriations for the fiscal year ending September 30, 2026, and for other purposes; providing for consideration of the bill (H.R. 7147) making further consolidated appropriations for the fiscal year ending September 30, 2026, and for other purposes; and for other purposes.",
      "type": "HRES"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-05",
        "text": "Referred to the Committee on Energy and Natural Resources. (text: CR S2759)"
      },
      "number": "203",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution expressing support for the designation of May 2025 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.",
      "type": "SRES"
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
            "name": "Alternative and renewable resources",
            "updateDate": "2026-01-23T16:40:04Z"
          },
          {
            "name": "Climate change and greenhouse gases",
            "updateDate": "2026-01-23T16:40:04Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2026-01-23T16:40:04Z"
          },
          {
            "name": "Energy prices",
            "updateDate": "2026-01-23T16:40:04Z"
          },
          {
            "name": "Rural conditions and development",
            "updateDate": "2026-01-23T16:40:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-05-20T12:27:55Z"
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
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres375ih.xml"
        }
      ],
      "type": "IH"
    },
    {
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres375eh.xml"
        }
      ],
      "type": "EH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "EH",
      "billTextVersionName": "Engrossed in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Expressing support for the designation of May 2025 as Renewable Fuels Month to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.",
      "titleType": "Official Titles from EH (Engrossed in House) bill text",
      "titleTypeCode": "259",
      "updateDate": "2026-01-24T03:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Expressing support for the designation of May 2025 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T08:48:21Z"
    },
    {
      "title": "Expressing support for the designation of May 2025 as \"Renewable Fuels Month\" to recognize the important role that renewable fuels play in reducing carbon impacts, lowering fuel prices for consumers, supporting rural communities, and lessening reliance on foreign adversaries.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T08:06:24Z"
    }
  ]
}
```
