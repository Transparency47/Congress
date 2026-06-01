# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/442?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/442
- Title: AIM HIGH Act
- Congress: 119
- Bill type: S
- Bill number: 442
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:50:14Z
- Update date including text: 2025-12-05T21:50:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/442",
    "number": "442",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "AIM HIGH Act",
    "type": "S",
    "updateDate": "2025-12-05T21:50:14Z",
    "updateDateIncludingText": "2025-12-05T21:50:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T17:14:41Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s442is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 442\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Cruz introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to direct the Secretary of the Air Force to operate a Technical Training Center of Excellence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act .\n#### 2. Air Force Technical Training Center of Excellence\nChapter 903 of title 10, United States Code, is amended by adding at the end the following new section:\n9026. Air Force Technical Training Center of Excellence (a) Establishment The Secretary of the Air Force shall operate a Technical Training Center of Excellence. The head of the Center shall be the designee of the Commander of the Airmen Development Command. (b) Purposes The purposes of the Center shall be to\u2014 (1) facilitate collaboration among all Air Force technical training installations; (2) serve as a premier training location for all maintainers throughout the military departments; (3) publish a set of responsibilities aimed at driving excellence, innovation, and leadership across all technical training specialties; (4) advocate for innovative improvements in curriculum, facilities, and medial; (5) foster outreach with industry and academia; (6) identify and promulgate best practices, standards, and benchmarks; (7) create a hub of excellence for the latest advancements in aviation technology and training methodologies; and (8) carry out such other responsibilities as the Secretary determines appropriate. (c) Location The Secretary shall select a location for the Center that is an Air Force installation that provides technical training and maintenance proficiency. .",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Armed Services."
      },
      "number": "1072",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AIM HIGH Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Aviation and airports",
            "updateDate": "2025-06-13T18:43:44Z"
          },
          {
            "name": "Military education and training",
            "updateDate": "2025-06-13T18:43:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-05T13:39:32Z"
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
          "measure-id": "id119s442",
          "measure-number": "442",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s442v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>"
        },
        "title": "AIM HIGH Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s442.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s442"
    },
    "title": "AIM HIGH Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act or the AIM HIGH Act</strong></p><p>This bill requires the Department of the Air Force to operate a Technical Training Center of Excellence. Among other duties, the center must (1) facilitate collaboration among all Air Force technical training installations; and (2) identify and promulgate best practices, standards, and benchmarks.\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119s442"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s442is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 10, United States Code, to direct the Secretary of the Air Force to operate a Technical Training Center of Excellence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:30Z"
    },
    {
      "title": "AIM HIGH Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AIM HIGH Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advancing Innovation and Maintenance through Headquarters for Instruction, Growth, and High-tech training Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
