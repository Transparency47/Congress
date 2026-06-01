# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1184?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1184
- Title: Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.
- Congress: 119
- Bill type: HRES
- Bill number: 1184
- Origin chamber: House
- Introduced date: 2026-04-16
- Update date: 2026-04-24T16:13:55Z
- Update date including text: 2026-04-24T16:13:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-04-16: Introduced in House
- 2026-04-16 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-04-16 - IntroReferral: Submitted in House
- Latest action: 2026-04-16: Submitted in House

## Actions

- 2026-04-16 - IntroReferral: Referred to the House Committee on Agriculture.
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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1184",
    "number": "1184",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "H001085",
        "district": "6",
        "firstName": "Chrissy",
        "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
        "lastName": "Houlahan",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
    "type": "HRES",
    "updateDate": "2026-04-24T16:13:55Z",
    "updateDateIncludingText": "2026-04-24T16:13:55Z"
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
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
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
          "date": "2026-04-16T14:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-04-16",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1184ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1184\nIN THE HOUSE OF REPRESENTATIVES\nApril 16, 2026 Ms. Houlahan (for herself and Mr. Meuser ) submitted the following resolution; which was referred to the Committee on Agriculture\nRESOLUTION\nRecognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.\nThat the House of Representatives\u2014\n**(1)**\nsupports the recognition of National Mushroom Day;\n**(2)**\nhonors the Commonwealth of Pennsylvania for its unparalleled contributions to the national mushroom industry; and\n**(3)**\nrecognizes the role mushrooms play in a healthy diet that is rich in whole foods.",
      "versionDate": "2026-04-16",
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
        "actionDate": "2026-04-16",
        "text": "Referred to the Committee on Agriculture, Nutrition, and Forestry. (text: CR S1825)"
      },
      "number": "676",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A resolution recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-04-21T21:30:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-04-16",
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
          "measure-id": "id119hres1184",
          "measure-number": "1184",
          "measure-type": "hres",
          "orig-publish-date": "2026-04-16",
          "originChamber": "HOUSE",
          "update-date": "2026-04-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1184v00",
            "update-date": "2026-04-24"
          },
          "action-date": "2026-04-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>"
        },
        "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1184.xml",
    "summary": {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hres1184"
    },
    "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets."
  },
  "summaries": [
    {
      "actionDate": "2026-04-16",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the recognition of National Mushroom Day and honors Pennsylvania for its contributions to the national mushroom industry.</p>",
      "updateDate": "2026-04-24",
      "versionCode": "id119hres1184"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1184ih.xml"
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
      "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:31Z"
    },
    {
      "title": "Recognizing and honoring National Mushroom Day and the contributions of Chester and Berks Counties to the national mushroom industry and to healthy diets.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-17T13:48:36Z"
    }
  ]
}
```
