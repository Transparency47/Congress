# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/334
- Title: To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 334
- Origin chamber: House
- Introduced date: 2025-01-13
- Update date: 2025-02-19T19:43:45Z
- Update date including text: 2026-05-12T16:27:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-13: Introduced in House

## Actions

- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Introduced in House
- 2025-01-13 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/334",
    "number": "334",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "A000372",
        "district": "12",
        "firstName": "Rick",
        "fullName": "Rep. Allen, Rick W. [R-GA-12]",
        "lastName": "Allen",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-02-19T19:43:45Z",
    "updateDateIncludingText": "2026-05-12T16:27:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-13",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-01-13T17:03:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr334ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 334\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 13, 2025 Mr. Allen introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes.\n#### 1. Technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence\nSection 227(d)(3) of the Communications Act of 1934 ( 47 U.S.C. 227(d)(3) ) is amended by inserting (including those created through generative artificial intelligence (genAI), for example voice cloning, and other subsequent technologies as may be deemed appropriate by the Commission) after telephone .",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-02-08T14:07:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119hr334",
          "measure-number": "334",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-13",
          "originChamber": "HOUSE",
          "update-date": "2025-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr334v00",
            "update-date": "2025-02-19"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill provides statutory authority for the application of certain technical and procedural standards to systems that transmit artificial or prerecorded telephone messages generated using artificial intelligence.</p><p>Specifically, the standards require (1) that such messages clearly identify and state the telephone number or address of the individual or entity initiating the call, and (2) that any system making such phone calls release a recipient\u2019s telephone line within five seconds of notification that the recipient has ended the call. Such standards are prescribed and implemented by the Federal Communications Commission (FCC) and apply under current law to any system used to transmit an artificial or prerecorded voice message by telephone.\u00a0</p><p>The bill also permits the FCC to apply the standards to other technologies used to transmit artificial and prerecorded telephone messages as it deems appropriate.\u00a0</p>"
        },
        "title": "To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr334.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for the application of certain technical and procedural standards to systems that transmit artificial or prerecorded telephone messages generated using artificial intelligence.</p><p>Specifically, the standards require (1) that such messages clearly identify and state the telephone number or address of the individual or entity initiating the call, and (2) that any system making such phone calls release a recipient\u2019s telephone line within five seconds of notification that the recipient has ended the call. Such standards are prescribed and implemented by the Federal Communications Commission (FCC) and apply under current law to any system used to transmit an artificial or prerecorded voice message by telephone.\u00a0</p><p>The bill also permits the FCC to apply the standards to other technologies used to transmit artificial and prerecorded telephone messages as it deems appropriate.\u00a0</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr334"
    },
    "title": "To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill provides statutory authority for the application of certain technical and procedural standards to systems that transmit artificial or prerecorded telephone messages generated using artificial intelligence.</p><p>Specifically, the standards require (1) that such messages clearly identify and state the telephone number or address of the individual or entity initiating the call, and (2) that any system making such phone calls release a recipient\u2019s telephone line within five seconds of notification that the recipient has ended the call. Such standards are prescribed and implemented by the Federal Communications Commission (FCC) and apply under current law to any system used to transmit an artificial or prerecorded voice message by telephone.\u00a0</p><p>The bill also permits the FCC to apply the standards to other technologies used to transmit artificial and prerecorded telephone messages as it deems appropriate.\u00a0</p>",
      "updateDate": "2025-02-19",
      "versionCode": "id119hr334"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr334ih.xml"
        }
      ],
      "type": "Introduced in House"
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
      "title": "To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T05:18:30Z"
    },
    {
      "title": "To amend the Communications Act of 1934 to establish technical and procedural standards for artificial or prerecorded voice systems created through generative artificial intelligence, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-14T09:05:54Z"
    }
  ]
}
```
