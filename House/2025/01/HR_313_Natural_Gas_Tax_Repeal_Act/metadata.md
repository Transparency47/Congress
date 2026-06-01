# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/313
- Title: Natural Gas Tax Repeal Act
- Congress: 119
- Bill type: HR
- Bill number: 313
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-12-06T06:36:09Z
- Update date including text: 2025-12-06T06:36:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/313",
    "number": "313",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "P000048",
        "district": "11",
        "firstName": "August",
        "fullName": "Rep. Pfluger, August [R-TX-11]",
        "lastName": "Pfluger",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Natural Gas Tax Repeal Act",
    "type": "HR",
    "updateDate": "2025-12-06T06:36:09Z",
    "updateDateIncludingText": "2025-12-06T06:36:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
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
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:34:45Z",
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
      "bioguideId": "G000601",
      "district": "12",
      "firstName": "Craig",
      "fullName": "Rep. Goldman, Craig [R-TX-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "TX"
    },
    {
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "R000619",
      "district": "6",
      "firstName": "Michael",
      "fullName": "Rep. Rulli, Michael A. [R-OH-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rulli",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "OH"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr313ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 313\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Pfluger introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo repeal the natural gas tax.\n#### 1. Short title\nThis Act may be cited as the Natural Gas Tax Repeal Act .\n#### 2. Repeal\nSection 136 of the Clean Air Act ( 42 U.S.C. 7436 )(relating to methane emissions and waste reduction incentive program for petroleum and natural gas systems) is repealed.\n#### 3. Rescission\nThe unobligated balance of any amounts made available under section 136 of the Clean Air Act ( 42 U.S.C. 7436 )(as in effect on the day before the date of enactment of this Act) is rescinded.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-01-16",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "143",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Natural Gas Tax Repeal Act",
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
        "name": "Environmental Protection",
        "updateDate": "2025-02-07T15:23:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr313",
          "measure-number": "313",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr313v00",
            "update-date": "2025-03-11"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Natural Gas Tax Repeal Act</strong></p><p>This bill eliminates a program administered by the Environmental Protection Agency that provides support for reducing methane emissions from the oil and gas sector. It also repeals a charge on methane emissions from\u00a0facilities that contain petroleum and natural gas systems and emit 25,000 metric tons or more of greenhouse gases per year.</p>"
        },
        "title": "Natural Gas Tax Repeal Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr313.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Natural Gas Tax Repeal Act</strong></p><p>This bill eliminates a program administered by the Environmental Protection Agency that provides support for reducing methane emissions from the oil and gas sector. It also repeals a charge on methane emissions from\u00a0facilities that contain petroleum and natural gas systems and emit 25,000 metric tons or more of greenhouse gases per year.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr313"
    },
    "title": "Natural Gas Tax Repeal Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Natural Gas Tax Repeal Act</strong></p><p>This bill eliminates a program administered by the Environmental Protection Agency that provides support for reducing methane emissions from the oil and gas sector. It also repeals a charge on methane emissions from\u00a0facilities that contain petroleum and natural gas systems and emit 25,000 metric tons or more of greenhouse gases per year.</p>",
      "updateDate": "2025-03-11",
      "versionCode": "id119hr313"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr313ih.xml"
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
      "title": "Natural Gas Tax Repeal Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-07T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Natural Gas Tax Repeal Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-07T04:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To repeal the natural gas tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-07T04:33:34Z"
    }
  ]
}
```
