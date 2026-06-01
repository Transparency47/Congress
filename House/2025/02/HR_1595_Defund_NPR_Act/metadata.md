# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1595?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1595
- Title: Defund NPR Act
- Congress: 119
- Bill type: HR
- Bill number: 1595
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-12-05T22:01:11Z
- Update date including text: 2025-12-05T22:01:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1595",
    "number": "1595",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001039",
        "district": "3",
        "firstName": "Kat",
        "fullName": "Rep. Cammack, Kat [R-FL-3]",
        "lastName": "Cammack",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Defund NPR Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:01:11Z",
    "updateDateIncludingText": "2025-12-05T22:01:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:06:45Z",
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
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-06-06",
      "state": "CA"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1595ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1595\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mrs. Cammack introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo prohibit Federal funding for National Public Radio, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Defund NPR Act .\n#### 2. Prohibition on Federal funding for National Public Radio\n##### (a) In general\nSection 396 of the Communications Act of 1934 ( 47 U.S.C. 396 ) is amended by adding at the end the following:\n(m) Prohibition on Federal funding for National Public Radio (1) In general After the date of enactment of the Defund NPR Act , no Federal funds may, directly or indirectly, be made available to or used to support an organization described in paragraph (2), including through the payment of dues to or the purchase of programming from the organization by a public broadcast station using Federal funds received by the station. (2) Organizations described The organizations described in this paragraph are\u2014 (A) the organization known, as of the date of enactment of the Defund NPR Act , as National Public Radio ; and (B) any successor organization to the organization described in subparagraph (A). .\n##### (b) Technical and conforming amendments\nTitle III of the Communications Act of 1934 ( 47 U.S.C. 301 et seq. ) is amended\u2014\n**(1)**\nin section 396(k) ( 47 U.S.C. 396(k) )\u2014\n**(A)**\nin paragraph (4), in the first sentence, by striking or National Public Radio ; and\n**(B)**\nin paragraph (9), by striking or National Public Radio each place that term appears; and\n**(2)**\nin section 398(b)(1) ( 47 U.S.C. 398(b)(1) ), by striking and National Public Radio .",
      "versionDate": "2025-02-26",
      "versionType": "Introduced in House"
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
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "746",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Defund NPR Act",
      "type": "S"
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
        "updateDate": "2025-03-18T15:08:27Z"
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
          "measure-id": "id119hr1595",
          "measure-number": "1595",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-07-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1595v00",
            "update-date": "2025-07-16"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>"
        },
        "title": "Defund NPR Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1595.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119hr1595"
    },
    "title": "Defund NPR Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Defund NPR Act</strong></p><p>This bill prohibits federal funding of National Public Radio (NPR) or any successor organization.\u00a0The prohibition includes the payment of dues to or the purchase of programming from NPR by a public broadcast station using federal funds. </p>",
      "updateDate": "2025-07-16",
      "versionCode": "id119hr1595"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1595ih.xml"
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
      "title": "Defund NPR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defund NPR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal funding for National Public Radio, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:50Z"
    }
  ]
}
```
