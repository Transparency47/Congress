# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/77?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/77
- Title: Supporting the designation of January 30, 2025, as "Fred Korematsu Day of Civil Liberties and the Constitution".
- Congress: 119
- Bill type: HRES
- Bill number: 77
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-11-08T09:05:29Z
- Update date including text: 2025-11-08T09:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-28 - Committee: Submitted in House
- Latest action: 2025-01-28: Submitted in House

## Actions

- 2025-01-28 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-01-28 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/77",
    "number": "77",
    "originChamber": "House",
    "policyArea": {
      "name": "Civil Rights and Liberties, Minority Issues"
    },
    "sponsors": [
      {
        "bioguideId": "T000472",
        "district": "39",
        "firstName": "Mark",
        "fullName": "Rep. Takano, Mark [D-CA-39]",
        "lastName": "Takano",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Supporting the designation of January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\".",
    "type": "HRES",
    "updateDate": "2025-11-08T09:05:29Z",
    "updateDateIncludingText": "2025-11-08T09:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-28",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H12100",
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
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
          "date": "2025-01-28T16:11:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "HI"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "CA"
    },
    {
      "bioguideId": "M001188",
      "district": "6",
      "firstName": "Grace",
      "fullName": "Rep. Meng, Grace [D-NY-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Meng",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres77ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 77\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Takano (for himself, Ms. Tokuda , and Ms. Matsui ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nSupporting the designation of January 30, 2025, as Fred Korematsu Day of Civil Liberties and the Constitution .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of a Fred Korematsu Day of Civil Liberties and the Constitution ;\n**(2)**\nrecognizes Fred Korematsu\u2019s bravery and resilience in the face of adversity; and\n**(3)**\nencourages all people to reflect on the importance of political leadership and vigilance and on the values of justice and civil rights during times of uncertainty and emergency.",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-30",
        "text": "Referred to the Committee on the Judiciary. (text: CR S525)"
      },
      "number": "47",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\".",
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
            "name": "Asia",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "Japan",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-02-05T21:04:51Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-02-05T21:04:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Civil Rights and Liberties, Minority Issues",
        "updateDate": "2025-02-04T13:59:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hres77",
          "measure-number": "77",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres77v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Fred Korematsu Day of Civil Liberties and the Constitution.</p><p>It also encourages all people to reflect on the importance of political leadership and vigilance and on the values of justice and civil rights during times of uncertainty and emergency.</p>"
        },
        "title": "Supporting the designation of January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres77.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Fred Korematsu Day of Civil Liberties and the Constitution.</p><p>It also encourages all people to reflect on the importance of political leadership and vigilance and on the values of justice and civil rights during times of uncertainty and emergency.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hres77"
    },
    "title": "Supporting the designation of January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\"."
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Fred Korematsu Day of Civil Liberties and the Constitution.</p><p>It also encourages all people to reflect on the importance of political leadership and vigilance and on the values of justice and civil rights during times of uncertainty and emergency.</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119hres77"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres77ih.xml"
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
      "title": "Supporting the designation of January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T11:48:19Z"
    },
    {
      "title": "Supporting the designation of January 30, 2025, as \"Fred Korematsu Day of Civil Liberties and the Constitution\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-29T09:05:41Z"
    }
  ]
}
```
