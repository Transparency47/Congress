# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/922?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/922
- Title: Expressing support for the designation of December 3, 2025, as the "National Day of 3D Printing".
- Congress: 119
- Bill type: HRES
- Bill number: 922
- Origin chamber: House
- Introduced date: 2025-12-03
- Update date: 2026-04-01T21:20:48Z
- Update date including text: 2026-04-01T21:20:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-03: Introduced in House
- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-03 - IntroReferral: Submitted in House
- 2025-12-03 - IntroReferral: Submitted in House
- Latest action: 2025-12-03: Submitted in House

## Actions

- 2025-12-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-12-03 - IntroReferral: Submitted in House
- 2025-12-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-03",
    "latestAction": {
      "actionDate": "2025-12-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/922",
    "number": "922",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Expressing support for the designation of December 3, 2025, as the \"National Day of 3D Printing\".",
    "type": "HRES",
    "updateDate": "2026-04-01T21:20:48Z",
    "updateDateIncludingText": "2026-04-01T21:20:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-03",
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
      "actionDate": "2025-12-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-12-03",
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
          "date": "2025-12-03T15:03:35Z",
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
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "NY"
    },
    {
      "bioguideId": "S001215",
      "district": "11",
      "firstName": "Haley",
      "fullName": "Rep. Stevens, Haley M. [D-MI-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Stevens",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-03",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres922ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 922\nIN THE HOUSE OF REPRESENTATIVES\nDecember 3, 2025 Mr. Foster (for himself, Mr. Takano , Mr. Tonko , and Ms. Stevens ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of December 3, 2025, as the National Day of 3D Printing .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of the National Day of 3D Printing ;\n**(2)**\nrecognizes the economic impact of 3D printing and the positive implications of 3D printing for the United States advanced manufacturing sector; and\n**(3)**\nencourages the promotion and celebration of 3D printing technology.",
      "versionDate": "2025-12-03",
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
        "updateDate": "2025-12-05T16:19:13Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-03",
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
          "measure-id": "id119hres922",
          "measure-number": "922",
          "measure-type": "hres",
          "orig-publish-date": "2025-12-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres922v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2025-12-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of a National Day of 3D Printing and encourages the promotion and celebration of 3D printing technology.</p><p>The resolution also recognizes the economic impact of 3D printing and its positive implications for the U.S. advanced manufacturing sector.</p>"
        },
        "title": "Expressing support for the designation of December 3, 2025, as the \"National Day of 3D Printing\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres922.xml",
    "summary": {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of a National Day of 3D Printing and encourages the promotion and celebration of 3D printing technology.</p><p>The resolution also recognizes the economic impact of 3D printing and its positive implications for the U.S. advanced manufacturing sector.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hres922"
    },
    "title": "Expressing support for the designation of December 3, 2025, as the \"National Day of 3D Printing\"."
  },
  "summaries": [
    {
      "actionDate": "2025-12-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of a National Day of 3D Printing and encourages the promotion and celebration of 3D printing technology.</p><p>The resolution also recognizes the economic impact of 3D printing and its positive implications for the U.S. advanced manufacturing sector.</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hres922"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres922ih.xml"
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
      "title": "Expressing support for the designation of December 3, 2025, as the \"National Day of 3D Printing\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-04T09:18:40Z"
    },
    {
      "title": "Expressing support for the designation of December 3, 2025, as the \"National Day of 3D Printing\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-04T09:06:39Z"
    }
  ]
}
```
