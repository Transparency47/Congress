# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/185
- Title: Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025.
- Congress: 119
- Bill type: HRES
- Bill number: 185
- Origin chamber: House
- Introduced date: 2025-03-04
- Update date: 2026-04-07T16:49:12Z
- Update date including text: 2026-04-07T16:49:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in House
- 2025-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-04 - Committee: Submitted in House
- Latest action: 2025-03-04: Submitted in House

## Actions

- 2025-03-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-04 - Committee: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/185",
    "number": "185",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025.",
    "type": "HRES",
    "updateDate": "2026-04-07T16:49:12Z",
    "updateDateIncludingText": "2026-04-07T16:49:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
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
          "date": "2025-03-04T15:01:20Z",
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
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres185ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 185\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2025 Mrs. Cherfilus-McCormick (for herself and Ms. Moore of Wisconsin ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025.\nThat the House of Representatives\u2014\n**(1)**\nsupports the urgent need to prevent, treat, and address obesity as a disease on this World Obesity Day;\n**(2)**\nrecognizes the need to categorize obesity as a disease to reduce the risk of other diseases and related comorbidities.\n**(3)**\nunderstands that genetic, environmental, behavioral factors, and the social determinants of health contribute to obesity; and\n**(4)**\nencourages health care providers and researchers to develop evidence-based strategies for the prevention, diagnosis, and treatment of obesity.",
      "versionDate": "2025-03-04",
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
        "name": "Health",
        "updateDate": "2025-03-07T16:46:18Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119hres185",
          "measure-number": "185",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres185v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the urgent need to prevent, treat, and address obesity as a disease on World Obesity Day.</p>"
        },
        "title": "Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres185.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the urgent need to prevent, treat, and address obesity as a disease on World Obesity Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres185"
    },
    "title": "Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025."
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the urgent need to prevent, treat, and address obesity as a disease on World Obesity Day.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres185"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres185ih.xml"
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
      "title": "Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T10:33:22Z"
    },
    {
      "title": "Recognizing the need of Congress to prevent, address, and treat obesity as a disease in the United States on this World Obesity Day, March 4, 2025.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T09:06:12Z"
    }
  ]
}
```
