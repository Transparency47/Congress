# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/58?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/58
- Title: Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship.
- Congress: 119
- Bill type: HRES
- Bill number: 58
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2025-12-06T07:03:51Z
- Update date including text: 2025-12-06T07:03:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House
- Latest action: 2025-01-23: Submitted in House

## Actions

- 2025-01-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2025-01-23 - Committee: Submitted in House
- 2025-01-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/58",
    "number": "58",
    "originChamber": "House",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "B001318",
        "district": "",
        "firstName": "Becca",
        "fullName": "Rep. Balint, Becca [D-VT-At Large]",
        "lastName": "Balint",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship.",
    "type": "HRES",
    "updateDate": "2025-12-06T07:03:51Z",
    "updateDateIncludingText": "2025-12-06T07:03:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:08:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres58ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 58\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Ms. Balint submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nCongratulating the University of Vermont men\u2019s soccer team on winning the 2024 National Collegiate Athletic Association Division I men\u2019s soccer national championship.\nThat the House of Representatives\u2014\n**(1)**\ncongratulates the University of Vermont men\u2019s soccer team on winning the 2024 National Collegiate Athletic Association Division I men\u2019s soccer national championship; and\n**(2)**\nrespectfully requests that the Clerk of the House of Representatives transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe interim president of the University of Vermont, Patricia A. Prelock;\n**(B)**\nthe director of athletics of the University of Vermont, Jeff Schulman; and\n**(C)**\nthe head coach of the University of Vermont Catamounts men\u2019s soccer team, Rob Dow.",
      "versionDate": "2025-01-23",
      "versionType": "IH"
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
        "actionDate": "2025-02-04",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S600; text: CR S599)"
      },
      "number": "56",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Sports and Recreation",
        "updateDate": "2025-01-27T22:08:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hres58",
          "measure-number": "58",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-05-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres58v00",
            "update-date": "2025-05-01"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution congratulates the University of Vermont men\u2019s soccer team on winning the 2024 National Collegiate Athletic Association Division I men\u2019s soccer national championship.</p>"
        },
        "title": "Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres58.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution congratulates the University of Vermont men\u2019s soccer team on winning the 2024 National Collegiate Athletic Association Division I men\u2019s soccer national championship.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hres58"
    },
    "title": "Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship."
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution congratulates the University of Vermont men\u2019s soccer team on winning the 2024 National Collegiate Athletic Association Division I men\u2019s soccer national championship.</p>",
      "updateDate": "2025-05-01",
      "versionCode": "id119hres58"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres58ih.xml"
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
      "title": "Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-24T09:18:20Z"
    },
    {
      "title": "Congratulating the University of Vermont men's soccer team on winning the 2024 National Collegiate Athletic Association Division I men's soccer national championship.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-24T09:05:53Z"
    }
  ]
}
```
