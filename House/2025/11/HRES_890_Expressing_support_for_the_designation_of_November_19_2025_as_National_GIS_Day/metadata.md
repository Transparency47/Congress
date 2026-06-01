# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/890?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/890
- Title: Expressing support for the designation of November 19, 2025, as "National GIS Day".
- Congress: 119
- Bill type: HRES
- Bill number: 890
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2026-04-01T19:39:28Z
- Update date including text: 2026-04-01T19:39:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-11-18 - IntroReferral: Submitted in House
- 2025-11-18 - IntroReferral: Submitted in House
- Latest action: 2025-11-18: Submitted in House

## Actions

- 2025-11-18 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- 2025-11-18 - IntroReferral: Submitted in House
- 2025-11-18 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/890",
    "number": "890",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "A000371",
        "district": "33",
        "firstName": "Pete",
        "fullName": "Rep. Aguilar, Pete [D-CA-33]",
        "lastName": "Aguilar",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Expressing support for the designation of November 19, 2025, as \"National GIS Day\".",
    "type": "HRES",
    "updateDate": "2026-04-01T19:39:28Z",
    "updateDateIncludingText": "2026-04-01T19:39:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres890ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 890\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Aguilar (for himself and Mr. Obernolte ) submitted the following resolution; which was referred to the Committee on Science, Space, and Technology\nRESOLUTION\nExpressing support for the designation of November 19, 2025, as National GIS Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National GIS Day ; and\n**(2)**\nencourages users of Geographic Information System technology (referred to in this resolving clause as GIS ), educators, students, and innovators to continue to employ GIS to\u2014\n**(A)**\nlearn and explore;\n**(B)**\nanalyze and address societal challenges; and\n**(C)**\ndrive economic growth for the betterment of the people of the United States and individuals around the world.",
      "versionDate": "2025-11-18",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-11-20T16:52:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-18",
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
          "measure-id": "id119hres890",
          "measure-number": "890",
          "measure-type": "hres",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres890v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National GIS Day and encourages the continued use of geographic information system (GIS) technology to learn, address societal challenges, and drive economic growth.</p>"
        },
        "title": "Expressing support for the designation of November 19, 2025, as \"National GIS Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres890.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National GIS Day and encourages the continued use of geographic information system (GIS) technology to learn, address societal challenges, and drive economic growth.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hres890"
    },
    "title": "Expressing support for the designation of November 19, 2025, as \"National GIS Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National GIS Day and encourages the continued use of geographic information system (GIS) technology to learn, address societal challenges, and drive economic growth.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hres890"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres890ih.xml"
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
      "title": "Expressing support for the designation of November 19, 2025, as \"National GIS Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-19T10:03:18Z"
    },
    {
      "title": "Expressing support for the designation of November 19, 2025, as \"National GIS Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-19T09:07:00Z"
    }
  ]
}
```
