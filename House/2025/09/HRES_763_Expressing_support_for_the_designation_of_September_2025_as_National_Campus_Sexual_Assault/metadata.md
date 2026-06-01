# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/763?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/763
- Title: Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month.
- Congress: 119
- Bill type: HRES
- Bill number: 763
- Origin chamber: House
- Introduced date: 2025-09-23
- Update date: 2026-04-02T19:44:03Z
- Update date including text: 2026-04-02T19:44:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-23: Introduced in House
- 2025-09-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House
- Latest action: 2025-09-23: Submitted in House

## Actions

- 2025-09-23 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-09-23 - IntroReferral: Submitted in House
- 2025-09-23 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-23",
    "latestAction": {
      "actionDate": "2025-09-23",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/763",
    "number": "763",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "N000147",
        "district": "",
        "firstName": "Eleanor",
        "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
        "lastName": "Norton",
        "party": "D",
        "state": "DC"
      }
    ],
    "title": "Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month.",
    "type": "HRES",
    "updateDate": "2026-04-02T19:44:03Z",
    "updateDateIncludingText": "2026-04-02T19:44:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-09-23",
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
          "date": "2025-09-23T13:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres763ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 763\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 23, 2025 Ms. Norton submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month.\nThat the House of Representatives supports the designation of National Campus Sexual Assault Awareness Month.",
      "versionDate": "2025-09-23",
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
        "name": "Education",
        "updateDate": "2026-04-01T13:15:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-23",
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
          "measure-id": "id119hres763",
          "measure-number": "763",
          "measure-type": "hres",
          "orig-publish-date": "2025-09-23",
          "originChamber": "HOUSE",
          "update-date": "2026-04-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres763v00",
            "update-date": "2026-04-02"
          },
          "action-date": "2025-09-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National Campus Sexual Assault Awareness Month.</p>"
        },
        "title": "Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres763.xml",
    "summary": {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Campus Sexual Assault Awareness Month.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hres763"
    },
    "title": "Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month."
  },
  "summaries": [
    {
      "actionDate": "2025-09-23",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National Campus Sexual Assault Awareness Month.</p>",
      "updateDate": "2026-04-02",
      "versionCode": "id119hres763"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres763ih.xml"
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
      "title": "Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-24T08:18:16Z"
    },
    {
      "title": "Expressing support for the designation of September 2025 as National Campus Sexual Assault Awareness Month.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-24T08:05:42Z"
    }
  ]
}
```
