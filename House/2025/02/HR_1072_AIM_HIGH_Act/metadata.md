# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1072?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1072
- Title: AIM HIGH Act
- Congress: 119
- Bill type: HR
- Bill number: 1072
- Origin chamber: House
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:48:53Z
- Update date including text: 2025-12-05T21:48:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-02-06: Introduced in House

## Actions

- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Introduced in House
- 2025-02-06 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1072",
    "number": "1072",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "AIM HIGH Act",
    "type": "HR",
    "updateDate": "2025-12-05T21:48:53Z",
    "updateDateIncludingText": "2025-12-05T21:48:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T15:05:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1072ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1072\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 6, 2025 Mr. Jackson of Texas introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to direct the Secretary of the Air Force to operate a Technical Training Center of Excellence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act .\n#### 2. Air Force Technical Training Center of Excellence\nChapter 903 of title 10, United States Code, is amended by adding at the end the following new section:\n9026. Air Force Technical Training Center of Excellence (a) Establishment The Secretary of the Air Force shall operate a Technical Training Center of Excellence. The head of the Center shall be the designee of the Commander of the Airmen Development Command. (b) Purposes The purposes of the Center shall be to\u2014 (1) facilitate collaboration among all Air Force technical training installations; (2) serve as a premier training location for all maintainers throughout the military departments; (3) publish a set of responsibilities aimed at driving excellence, innovation, and leadership across all technical training specialties; (4) advocate for innovative improvements in curriculum, facilities, and medial; (5) foster outreach with industry and academia; (6) identify and promulgate best practices, standards, and benchmarks; (7) create a hub of excellence for the latest advancements in aviation technology and training methodologies; and (8) carry out such other responsibilities as the Secretary determines appropriate. (c) Location The Secretary shall select a location for the Center that is an Air Force installation that provides technical training and maintenance proficiency. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Read twice and referred to the Committee on Armed Services."
      },
      "number": "442",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AIM HIGH Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aviation and airports",
            "updateDate": "2025-06-13T18:43:24Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-06-13T18:43:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-04-30T14:35:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119hr1072",
          "measure-number": "1072",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-06",
          "originChamber": "HOUSE",
          "update-date": "2025-04-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1072v00",
            "update-date": "2025-04-30"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>"
        },
        "title": "AIM HIGH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1072.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119hr1072"
    },
    "title": "AIM HIGH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>",
      "updateDate": "2025-04-30",
      "versionCode": "id119hr1072"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1072ih.xml"
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
      "title": "AIM HIGH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T03:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AIM HIGH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T03:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to direct the Secretary of the Air Force to operate a Technical Training Center of Excellence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T03:03:33Z"
    }
  ]
}
```
