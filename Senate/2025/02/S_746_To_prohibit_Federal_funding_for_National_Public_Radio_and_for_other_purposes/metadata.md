# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/746?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/746
- Title: Defund NPR Act
- Congress: 119
- Bill type: S
- Bill number: 746
- Origin chamber: Senate
- Introduced date: 2025-02-26
- Update date: 2025-12-05T22:01:43Z
- Update date including text: 2025-12-05T22:01:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in Senate
- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-26: Introduced in Senate

## Actions

- 2025-02-26 - IntroReferral: Introduced in Senate
- 2025-02-26 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/746",
    "number": "746",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Defund NPR Act",
    "type": "S",
    "updateDate": "2025-12-05T22:01:43Z",
    "updateDateIncludingText": "2025-12-05T22:01:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-26",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-02-26T17:37:06Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s746is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 746\nIN THE SENATE OF THE UNITED STATES\nFebruary 26, 2025 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit Federal funding for National Public Radio, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defund NPR Act .\n#### 2. Prohibition on Federal funding for National Public Radio\n##### (a) In general\nSection 396 of the Communications Act of 1934 ( 47 U.S.C. 396 ) is amended by adding at the end the following:\n(m) Prohibition on Federal funding for National Public Radio (1) In general After the date of enactment of the Defund NPR Act , no Federal funds may, directly or indirectly, be made available to or used to support an organization described in paragraph (2), including through the payment of dues to or the purchase of programming from the organization by a public broadcast station using Federal funds received by the station. (2) Organizations described The organizations described in this paragraph are\u2014 (A) the organization known, as of the date of enactment of the Defund NPR Act , as National Public Radio ; and (B) any successor organization to the organization described in subparagraph (A). .\n##### (b) Technical and conforming amendments\nTitle III of the Communications Act of 1934 ( 47 U.S.C. 301 et seq. ) is amended\u2014\n**(1)**\nin section 396(k) ( 47 U.S.C. 396(k) )\u2014\n**(A)**\nin paragraph (4), in the first sentence, by striking or National Public Radio ; and\n**(B)**\nin paragraph (9), by striking or National Public Radio each place that term appears; and\n**(2)**\nin section 398(b)(1) ( 47 U.S.C. 398(b)(1) ), by striking and National Public Radio .",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-26",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1595",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defund NPR Act",
      "type": "HR"
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
        "updateDate": "2025-03-23T11:19:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
    "originChamber": "Senate",
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
          "measure-id": "id119s746",
          "measure-number": "746",
          "measure-type": "s",
          "orig-publish-date": "2025-02-26",
          "originChamber": "SENATE",
          "update-date": "2025-07-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s746v00",
            "update-date": "2025-07-16"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>"
        },
        "title": "Defund NPR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s746.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119s746"
    },
    "title": "Defund NPR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119s746"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s746is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Defund NPR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defund NPR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit Federal funding for National Public Radio, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:29Z"
    }
  ]
}
```
