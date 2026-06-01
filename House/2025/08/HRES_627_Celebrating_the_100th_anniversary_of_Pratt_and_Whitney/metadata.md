# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/627?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/627
- Title: Celebrating the 100th anniversary of Pratt & Whitney.
- Congress: 119
- Bill type: HRES
- Bill number: 627
- Origin chamber: House
- Introduced date: 2025-08-01
- Update date: 2026-04-07T10:24:42Z
- Update date including text: 2026-04-07T10:24:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-08-01: Introduced in House
- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House
- Latest action: 2025-08-01: Submitted in House

## Actions

- 2025-08-01 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-08-01 - IntroReferral: Submitted in House
- 2025-08-01 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/627",
    "number": "627",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "L000557",
        "district": "1",
        "firstName": "John",
        "fullName": "Rep. Larson, John B. [D-CT-1]",
        "lastName": "Larson",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Celebrating the 100th anniversary of Pratt & Whitney.",
    "type": "HRES",
    "updateDate": "2026-04-07T10:24:42Z",
    "updateDateIncludingText": "2026-04-07T10:24:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-08-01",
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
          "date": "2025-08-01T14:06:00Z",
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
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
    },
    {
      "bioguideId": "C001069",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Courtney, Joe [D-CT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Courtney",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
    },
    {
      "bioguideId": "H001047",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Himes, James A. [D-CT-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Himes",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres627ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 627\nIN THE HOUSE OF REPRESENTATIVES\nAugust 1, 2025 Mr. Larson of Connecticut (for himself, Ms. DeLauro , Mr. Courtney , Mr. Himes , and Mrs. Hayes ) submitted the following resolution; which was referred to the Committee on Energy and Commerce\nRESOLUTION\nCelebrating the 100th anniversary of Pratt & Whitney.\nThat the House of Representatives\u2014\n**(1)**\nproudly celebrates the achievements and legacy of Pratt & Whitney, recognizing a century of excellence in engineering, innovation, and public service;\n**(2)**\ncommends and thanks the countless skilled employees, past and present, who have been the bedrock of Pratt & Whitney\u2019s success, including machinists, engineers, technicians, and veterans; and\n**(3)**\nencourages all citizens to join in honoring the extraordinary contributions of this iconic company to the State of Connecticut, the United States, and the world.",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-07-24",
        "text": "Referred to the Committee on the Judiciary."
      },
      "number": "336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution celebrating the 100th anniversary of Pratt & Whitney.",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-09-12T16:34:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-01",
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
          "measure-id": "id119hres627",
          "measure-number": "627",
          "measure-type": "hres",
          "orig-publish-date": "2025-08-01",
          "originChamber": "HOUSE",
          "update-date": "2026-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres627v00",
            "update-date": "2026-04-07"
          },
          "action-date": "2025-08-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>"
        },
        "title": "Celebrating the 100th anniversary of Pratt & Whitney."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres627.xml",
    "summary": {
      "actionDate": "2025-08-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres627"
    },
    "title": "Celebrating the 100th anniversary of Pratt & Whitney."
  },
  "summaries": [
    {
      "actionDate": "2025-08-01",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution celebrates the achievements and\u00a0legacy of the Connecticut company Pratt & Whitney on its 100<sup>th </sup>anniversary and recognizes the company\u00a0for its excellence in engineering, innovation, and public service.</p><p>It also commends and thanks the past and present skilled employees of Pratt & Whitney, including machinists, engineers, technicians, and veterans.</p>",
      "updateDate": "2026-04-07",
      "versionCode": "id119hres627"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres627ih.xml"
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
      "title": "Celebrating the 100th anniversary of Pratt & Whitney.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-02T08:18:31Z"
    },
    {
      "title": "Celebrating the 100th anniversary of Pratt & Whitney.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-02T08:05:24Z"
    }
  ]
}
```
