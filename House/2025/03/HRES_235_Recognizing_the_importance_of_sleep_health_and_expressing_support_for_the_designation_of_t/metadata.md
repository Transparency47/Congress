# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/235?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/235
- Title: Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as "Sleep Awareness Week".
- Congress: 119
- Bill type: HRES
- Bill number: 235
- Origin chamber: House
- Introduced date: 2025-03-21
- Update date: 2026-04-14T19:04:08Z
- Update date including text: 2026-04-14T19:04:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-21: Introduced in House
- 2025-03-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-21 - IntroReferral: Submitted in House
- 2025-03-21 - IntroReferral: Submitted in House
- Latest action: 2025-03-21: Submitted in House

## Actions

- 2025-03-21 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-21 - IntroReferral: Submitted in House
- 2025-03-21 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-21",
    "latestAction": {
      "actionDate": "2025-03-21",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/235",
    "number": "235",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "D000631",
        "district": "4",
        "firstName": "Madeleine",
        "fullName": "Rep. Dean, Madeleine [D-PA-4]",
        "lastName": "Dean",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as \"Sleep Awareness Week\".",
    "type": "HRES",
    "updateDate": "2026-04-14T19:04:08Z",
    "updateDateIncludingText": "2026-04-14T19:04:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-21",
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
      "actionDate": "2025-03-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-21",
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
          "date": "2025-03-21T20:00:30Z",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "AL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres235ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 235\nIN THE HOUSE OF REPRESENTATIVES\nMarch 21, 2025 Ms. Dean of Pennsylvania (for herself, Ms. Sewell , and Mrs. Cherfilus-McCormick ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nRecognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as Sleep Awareness Week .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the importance of sleep health as a way to increase health and wellbeing;\n**(2)**\nsupports the designation of a Sleep Awareness Week ;\n**(3)**\nsupports the goals and efforts of Sleep Awareness Week;\n**(4)**\nencourages public health officials, healthcare providers, educators, parents, et al. to do their part to promote adequate sleep;\n**(5)**\nencourages the people of the United States to prioritize their sleep health, practice good habits for sleep health, and discuss their sleep with their health care provider; and\n**(6)**\nrecognizes the continued importance of policies to improve sleep health.",
      "versionDate": "2025-03-21",
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
        "actionDate": "2026-04-09",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1158",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 13, 2026, as \"Sleep Awareness Week\".",
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
        "name": "Health",
        "updateDate": "2025-03-23T11:45:16Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-21",
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
          "measure-id": "id119hres235",
          "measure-number": "235",
          "measure-type": "hres",
          "orig-publish-date": "2025-03-21",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres235v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-03-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of Sleep Awareness Week.</p>"
        },
        "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as \"Sleep Awareness Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres235.xml",
    "summary": {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Sleep Awareness Week.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres235"
    },
    "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as \"Sleep Awareness Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-21",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of Sleep Awareness Week.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres235"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres235ih.xml"
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
      "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as \"Sleep Awareness Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T08:18:46Z"
    },
    {
      "title": "Recognizing the importance of sleep health and expressing support for the designation of the week of March 9 through March 15, 2025, as \"Sleep Awareness Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T08:06:02Z"
    }
  ]
}
```
