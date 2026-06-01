# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1288?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1288
- Title: Supporting the designation of May 14, 2026, as "National Scam Survivor Day".
- Congress: 119
- Bill type: HRES
- Bill number: 1288
- Origin chamber: House
- Introduced date: 2026-05-14
- Update date: 2026-05-29T17:01:37Z
- Update date including text: 2026-05-29T17:01:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-14: Introduced in House
- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House
- Latest action: 2026-05-14: Submitted in House

## Actions

- 2026-05-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-05-14 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-14",
    "latestAction": {
      "actionDate": "2026-05-14",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1288",
    "number": "1288",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001213",
        "district": "1",
        "firstName": "Bryan",
        "fullName": "Rep. Steil, Bryan [R-WI-1]",
        "lastName": "Steil",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Supporting the designation of May 14, 2026, as \"National Scam Survivor Day\".",
    "type": "HRES",
    "updateDate": "2026-05-29T17:01:37Z",
    "updateDateIncludingText": "2026-05-29T17:01:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-14",
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
      "actionCode": "1025",
      "actionDate": "2026-05-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
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
          "date": "2026-05-14T14:05:00Z",
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
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "CA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
    },
    {
      "bioguideId": "R000606",
      "district": "8",
      "firstName": "Jamie",
      "fullName": "Rep. Raskin, Jamie [D-MD-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Raskin",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "MD"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "IA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "A000380",
      "district": "1",
      "firstName": "Gabe",
      "fullName": "Rep. Amo, Gabe [D-RI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Amo",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1288ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1288\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2026 Mr. Steil (for himself, Mr. Harder of California , Mr. Meuser , Mr. Raskin , Mr. Nunn of Iowa , Mr. Shreve , and Mr. Amo ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nSupporting the designation of May 14, 2026, as National Scam Survivor Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Scam Survivor Day ;\n**(2)**\nencourages increased public awareness of scams and strategies to prevent or address scams;\n**(3)**\nrecognizes the impact of scams on American citizens and businesses;\n**(4)**\nrecognizes the importance of improving public access to scam prevention resources;\n**(5)**\nsupports the role of Federal and local law enforcement entities in addressing scams;\n**(6)**\nurges a collaborative approach to supporting scam survivors and prevent future scams among governmental, private, and nonprofit organizations; and\n**(7)**\nencourages continued improvements to existing scam prevention resource toolkits, support for scam survivors, and law enforcement efforts to hold scammers accountable.",
      "versionDate": "2026-05-14",
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
        "name": "Commerce",
        "updateDate": "2026-05-29T17:01:37Z"
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
      "date": "2026-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1288ih.xml"
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
      "title": "Supporting the designation of May 14, 2026, as \"National Scam Survivor Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-15T08:18:41Z"
    },
    {
      "title": "Supporting the designation of May 14, 2026, as \"National Scam Survivor Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T08:07:19Z"
    }
  ]
}
```
