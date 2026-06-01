# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/387
- Title: Expressing support for the designation of May 2025 as "National Asthma and Allergy Awareness Month".
- Congress: 119
- Bill type: HRES
- Bill number: 387
- Origin chamber: House
- Introduced date: 2025-05-06
- Update date: 2026-04-07T20:53:37Z
- Update date including text: 2026-04-07T20:53:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in House
- 2025-05-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-06 - IntroReferral: Submitted in House
- 2025-05-06 - IntroReferral: Submitted in House
- Latest action: 2025-05-06: Submitted in House

## Actions

- 2025-05-06 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-05-06 - IntroReferral: Submitted in House
- 2025-05-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/387",
    "number": "387",
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
    "title": "Expressing support for the designation of May 2025 as \"National Asthma and Allergy Awareness Month\".",
    "type": "HRES",
    "updateDate": "2026-04-07T20:53:37Z",
    "updateDateIncludingText": "2026-04-07T20:53:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T14:01:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "V000129",
      "district": "22",
      "firstName": "David",
      "fullName": "Rep. Valadao, David G. [R-CA-22]",
      "isOriginalCosponsor": "True",
      "lastName": "Valadao",
      "middleName": "G.",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres387ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 387\nIN THE HOUSE OF REPRESENTATIVES\nMay 6, 2025 Mrs. Dingell (for herself and Mr. Valadao ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nExpressing support for the designation of May 2025 as National Asthma and Allergy Awareness Month .\nThat the House of Representatives recognizes National Asthma and Allergy Awareness Month and calls upon the American people to observe such month with appropriate ceremonies and activities.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-05-20T13:51:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
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
          "measure-id": "id119hres387",
          "measure-number": "387",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres387v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes National Asthma and Allergy Awareness Month.</p>"
        },
        "title": "Expressing support for the designation of May 2025 as \"National Asthma and Allergy Awareness Month\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres387.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes National Asthma and Allergy Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres387"
    },
    "title": "Expressing support for the designation of May 2025 as \"National Asthma and Allergy Awareness Month\"."
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes National Asthma and Allergy Awareness Month.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres387"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres387ih.xml"
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
      "title": "Expressing support for the designation of May 2025 as \"National Asthma and Allergy Awareness Month\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T08:18:21Z"
    },
    {
      "title": "Expressing support for the designation of May 2025 as \"National Asthma and Allergy Awareness Month\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T08:06:21Z"
    }
  ]
}
```
