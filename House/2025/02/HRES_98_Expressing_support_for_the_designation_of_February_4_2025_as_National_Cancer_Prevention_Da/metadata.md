# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/98?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/98
- Title: Expressing support for the designation of February 4, 2025, as "National Cancer Prevention Day".
- Congress: 119
- Bill type: HRES
- Bill number: 98
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-04-07T20:39:42Z
- Update date including text: 2026-04-07T20:39:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-04 - Committee: Submitted in House
- Latest action: 2025-02-04: Submitted in House

## Actions

- 2025-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-02-04 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/98",
    "number": "98",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000624",
        "district": "6",
        "firstName": "Debbie",
        "fullName": "Rep. Dingell, Debbie [D-MI-6]",
        "lastName": "Dingell",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\".",
    "type": "HRES",
    "updateDate": "2026-04-07T20:39:42Z",
    "updateDateIncludingText": "2026-04-07T20:39:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionCode": "H12100",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:05:20Z",
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
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres98ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 98\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mrs. Dingell (for herself and Mr. James ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nExpressing support for the designation of February 4, 2025, as National Cancer Prevention Day .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National Cancer Prevention Day ;\n**(2)**\nrecognizes all efforts to raise the awareness for the reduction of cancer risks; and\n**(3)**\nrecognizes the devastating effect cancer has on families and wishes to expand knowledge, encourage early detection, and work with friends in the medical and scientific fields to put an end to this deadly disease.",
      "versionDate": "2025-02-04",
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
        "actionDate": "2026-02-04",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1037",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of February 4, 2026, as \"National Cancer Prevention Day\".",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cancer",
            "updateDate": "2025-02-10T19:02:22Z"
          },
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-02-10T19:02:22Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-02-10T19:02:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-02-07T14:00:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hres98",
          "measure-number": "98",
          "measure-type": "hres",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres98v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for the designation of National Cancer Prevention Day.</p>"
        },
        "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres98.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Cancer Prevention Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres98"
    },
    "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\"."
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for the designation of National Cancer Prevention Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres98"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres98ih.xml"
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
      "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-05T12:03:24Z"
    },
    {
      "title": "Expressing support for the designation of February 4, 2025, as \"National Cancer Prevention Day\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-05T09:06:40Z"
    }
  ]
}
```
