# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/784?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/784
- Title: Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as "National Coffee Day".
- Congress: 119
- Bill type: HRES
- Bill number: 784
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-06T13:04:18Z
- Update date including text: 2026-04-06T13:04:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House
- Latest action: 2025-09-30: Submitted in House

## Actions

- 2025-09-30 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-30 - IntroReferral: Submitted in House
- 2025-09-30 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/784",
    "number": "784",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000487",
        "district": "2",
        "firstName": "Jill",
        "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
        "lastName": "Tokuda",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as \"National Coffee Day\".",
    "type": "HRES",
    "updateDate": "2026-04-06T13:04:18Z",
    "updateDateIncludingText": "2026-04-06T13:04:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:05:25Z",
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
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "SC"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "HI"
    },
    {
      "bioguideId": "H001103",
      "district": "0",
      "firstName": "Pablo",
      "fullName": "Rescom. Hern\u00e1ndez, Pablo Jose [D-PR-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern\u00e1ndez",
      "middleName": "Jose",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "PR"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "T000474",
      "district": "35",
      "firstName": "Norma",
      "fullName": "Rep. Torres, Norma J. [D-CA-35]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "CA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres784ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 784\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Ms. Tokuda (for herself, Mr. Timmons , Mr. Case , Mr. Hern\u00e1ndez , Mr. Tran , Mr. Gottheimer , Mrs. Torres of California , and Ms. Bonamici ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as National Coffee Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Coffee Day ;\n**(2)**\nrecognizes the contributions of coffee growers, importers, roasters, retailers, baristas, researchers, and other workers across the coffee value chain;\n**(3)**\nsupports efforts to strengthen domestic and global coffee supply chains, including investment in agricultural research, climate resilience, and farmer livelihoods;\n**(4)**\nencourages continued scientific research into the health effects of drinking coffee;\n**(5)**\nsupports coffee as a key part of trade and economic policies to build a strong United States coffee market and to advance broad-based social and economic development in coffee-growing countries that advance United States national security interests; and\n**(6)**\ncelebrates coffee\u2019s unique and valuable role in the American culture and economy.",
      "versionDate": "2025-09-30",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-11-19T21:45:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-30",
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
          "measure-id": "id119hres784",
          "measure-number": "784",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-30",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres784v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-09-30",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Coffee Day.</p><p>Among other things, the resolution also supports efforts to strengthen domestic and global coffee supply chains and encourages continued scientific research into the health effects of drinking coffee.</p>"
        },
        "title": "Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as \"National Coffee Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres784.xml",
    "summary": {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Coffee Day.</p><p>Among other things, the resolution also supports efforts to strengthen domestic and global coffee supply chains and encourages continued scientific research into the health effects of drinking coffee.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres784"
    },
    "title": "Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as \"National Coffee Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-09-30",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Coffee Day.</p><p>Among other things, the resolution also supports efforts to strengthen domestic and global coffee supply chains and encourages continued scientific research into the health effects of drinking coffee.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres784"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres784ih.xml"
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
      "title": "Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as \"National Coffee Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T08:48:27Z"
    },
    {
      "title": "Recognizing the value of coffee to the United States and expressing support for September 29, 2025, to be designated as \"National Coffee Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-01T08:05:45Z"
    }
  ]
}
```
