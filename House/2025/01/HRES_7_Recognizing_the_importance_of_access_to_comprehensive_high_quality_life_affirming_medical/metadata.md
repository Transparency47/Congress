# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/7?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/7
- Title: Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages.
- Congress: 119
- Bill type: HRES
- Bill number: 7
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-01-22T23:15:38Z
- Update date including text: 2025-01-22T23:15:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House
- Latest action: 2025-01-03: Submitted in House

## Actions

- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-01-03 - Committee: Submitted in House
- 2025-01-03 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/7",
    "number": "7",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages.",
    "type": "HRES",
    "updateDate": "2025-01-22T23:15:38Z",
    "updateDateIncludingText": "2025-01-22T23:15:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "Committee"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:11:20Z",
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
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres7ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 7\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona (for himself and Mr. Higgins of Louisiana ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages.\nThat the House of Representatives\u2014\n**(1)**\nexpresses its support for women nationwide to have access to comprehensive, convenient, compassionate, life-affirming, high-quality health care; and\n**(2)**\nrecognizes the high standards established by Pro Women\u2019s Healthcare Centers consortium as standards worth implementing nationwide.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Health care coverage and access",
            "updateDate": "2025-01-15T18:35:30Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-01-15T18:35:30Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-01-15T18:35:30Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-01-15T18:35:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-01-08T18:55:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hres7",
          "measure-number": "7",
          "measure-type": "hres",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-01-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres7v00",
            "update-date": "2025-01-22"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution expresses support for women nationwide to have access to comprehensive, convenient, compassionate, life-affirming, and high-quality health care.</p>"
        },
        "title": "Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres7.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for women nationwide to have access to comprehensive, convenient, compassionate, life-affirming, and high-quality health care.</p>",
      "updateDate": "2025-01-22",
      "versionCode": "id119hres7"
    },
    "title": "Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages."
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution expresses support for women nationwide to have access to comprehensive, convenient, compassionate, life-affirming, and high-quality health care.</p>",
      "updateDate": "2025-01-22",
      "versionCode": "id119hres7"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres7ih.xml"
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
      "title": "Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:39:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Recognizing the importance of access to comprehensive, high-quality, life-affirming medical care for women of all ages.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-07T14:39:24Z"
    }
  ]
}
```
