# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/85?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/85
- Title: Celebrating the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act on April 13, 2026, and recognizing its significant impact on the sustainable and profitable management of the Nation's fishery resources.
- Congress: 119
- Bill type: HCONRES
- Bill number: 85
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-21T04:16:48Z
- Update date including text: 2026-04-30T16:27:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-16 - IntroReferral: Submitted in House
- Latest action: 2026-04-16: Submitted in House

## Actions

- 2026-04-16 - IntroReferral: Referred to the House Committee on Natural Resources.
- 2026-04-16 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-16",
    "latestAction": {
      "actionDate": "2026-04-16",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/85",
    "number": "85",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001068",
        "district": "2",
        "firstName": "Jared",
        "fullName": "Rep. Huffman, Jared [D-CA-2]",
        "lastName": "Huffman",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Celebrating the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act on April 13, 2026, and recognizing its significant impact on the sustainable and profitable management of the Nation's fishery resources.",
    "type": "HCONRES",
    "updateDate": "2026-04-21T04:16:48Z",
    "updateDateIncludingText": "2026-04-30T16:27:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-16",
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
      "actionCode": "1025",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
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
          "date": "2026-04-16T14:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
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
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "OR"
    },
    {
      "bioguideId": "K000375",
      "district": "9",
      "firstName": "William",
      "fullName": "Rep. Keating, William R. [D-MA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Keating",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres85ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. CON. RES. 85\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Mr. Huffman (for himself, Ms. Hoyle of Oregon , and Mr. Keating ) submitted the following concurrent resolution; which was referred to the Committee on Natural Resources\nCONCURRENT RESOLUTION\nCelebrating the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act on April 13, 2026, and recognizing its significant impact on the sustainable and profitable management of the Nation\u2019s fishery resources.\nThat Congress\u2014\n**(1)**\nrecognizes and celebrates the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act (MSA) ( 16 U.S.C. 1801 et seq. ) and its enduring influence on vibrant coastal economies and healthy marine ecosystems;\n**(2)**\ncelebrates the people who commit and risk their lives to provide seafood and nutrition to the Nation;\n**(3)**\ncommends the State and Federal resource managers, fishermen, industry representatives, Indigenous and Tribal members, scientists, conservationists, and other experts who uphold the principles of the MSA and work collaboratively to steward fishery resources in the Nation\u2019s best interests; and\n**(4)**\nreaffirms its commitment to a strong science-based MSA to maintain healthy and profitable fisheries and to provide a foundation to address modern challenges, such as persistent overfishing, changing ocean and ecosystem conditions, fishery disasters, and illegal, unregulated, and unreported fishing practices by foreign fleets that are affecting fishing communities and the productivity of fisheries in the United States.",
      "versionDate": "2026-04-16",
      "versionType": "IH"
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
        "name": "Public Lands and Natural Resources",
        "updateDate": "2026-04-21T04:16:47Z"
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
      "date": "2026-04-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hconres/BILLS-119hconres85ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Celebrating the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act on April 13, 2026, and recognizing its significant impact on the sustainable and profitable management of the Nation's fishery resources.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:28Z"
    },
    {
      "title": "Celebrating the 50th anniversary of the Magnuson-Stevens Fishery Conservation and Management Act on April 13, 2026, and recognizing its significant impact on the sustainable and profitable management of the Nation's fishery resources.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T13:49:08Z"
    }
  ]
}
```
