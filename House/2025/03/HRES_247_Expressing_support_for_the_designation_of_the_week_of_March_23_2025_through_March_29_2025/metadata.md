# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/247?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/247
- Title: Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as "National Cleaning Week".
- Congress: 119
- Bill type: HRES
- Bill number: 247
- Origin chamber: House
- Introduced date: 2025-03-25
- Update date: 2026-04-08T13:01:17Z
- Update date including text: 2026-04-08T13:01:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in House
- 2025-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House
- Latest action: 2025-03-25: Submitted in House

## Actions

- 2025-03-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-25 - IntroReferral: Submitted in House
- 2025-03-25 - IntroReferral: Submitted in House

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/247",
    "number": "247",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\".",
    "type": "HRES",
    "updateDate": "2026-04-08T13:01:17Z",
    "updateDateIncludingText": "2026-04-08T13:01:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-25",
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
      "actionDate": "2025-03-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-25",
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
          "date": "2025-03-25T14:01:15Z",
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-03-25",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres247ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 247\nIN THE HOUSE OF REPRESENTATIVES\nMarch 25, 2025 Mr. LaHood (for himself and Mr. Krishnamoorthi ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of the week of March 23, 2025, through March 29, 2025, as National Cleaning Week .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the commitment and essential services provided by the cleaning industry in maintaining clean and sanitary conditions; and\n**(2)**\nsupports the designation of National Cleaning Week to continue to promote safe and clean environments at work, in schools, and at home.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2026-03-19",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1127",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Expressing support for the designation of the week of March 22, 2026, through March 28, 2026, as \"National Cleaning Week\".",
      "type": "HRES"
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
        "updateDate": "2025-03-26T17:41:19Z"
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
          "measure-id": "id119hres247",
          "measure-number": "247",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-25",
          "originChamber": "HOUSE",
          "update-date": "2026-04-08"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres247v00",
            "update-date": "2026-04-08"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the essential services provided by the cleaning industry in maintaining sanitary conditions and supports the designation of National Cleaning Week to promote safe and clean environments at work, in schools, and at home.</p>"
        },
        "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres247.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the essential services provided by the cleaning industry in maintaining sanitary conditions and supports the designation of National Cleaning Week to promote safe and clean environments at work, in schools, and at home.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hres247"
    },
    "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the essential services provided by the cleaning industry in maintaining sanitary conditions and supports the designation of National Cleaning Week to promote safe and clean environments at work, in schools, and at home.</p>",
      "updateDate": "2026-04-08",
      "versionCode": "id119hres247"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres247ih.xml"
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
      "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T08:18:22Z"
    },
    {
      "title": "Expressing support for the designation of the week of March 23, 2025, through March 29, 2025, as \"National Cleaning Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T08:06:46Z"
    }
  ]
}
```
