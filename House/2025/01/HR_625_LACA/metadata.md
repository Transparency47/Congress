# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/625?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/625
- Title: LACA
- Congress: 119
- Bill type: HR
- Bill number: 625
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-06-10T22:00:53Z
- Update date including text: 2025-06-10T22:00:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/625",
    "number": "625",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M001157",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
        "lastName": "McCaul",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LACA",
    "type": "HR",
    "updateDate": "2025-06-10T22:00:53Z",
    "updateDateIncludingText": "2025-06-10T22:00:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:01:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr625ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 625\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. McCaul (for himself and Mr. Ruiz ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo clarify where court may be held for certain district courts in Texas and California.\n#### 1. Short title\nThis Act may be cited as the Local Access to Courts Act or LACA .\n#### 2. Organization of Texas district courts\nSection 124(b)(2) of title 28, United States Code, is amended, in the matter preceding paragraph (3), by inserting and College Station before the period at the end.\n#### 3. Organization of California district courts\nSection 84(d) of title 28, United States Code, is amended by inserting and El Centro after at San Diego .",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-03-05",
        "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 16 - 11."
      },
      "number": "1702",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "JUDGES Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-02-13",
        "actionTime": "10:56:41",
        "text": "Held at the desk."
      },
      "number": "32",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LACA",
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
            "name": "California",
            "updateDate": "2025-03-12T14:52:48Z"
          },
          {
            "name": "State and local courts",
            "updateDate": "2025-03-12T14:52:48Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-03-12T14:52:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-02-20T16:13:04Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr625",
          "measure-number": "625",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr625v00",
            "update-date": "2025-03-17"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p>"
        },
        "title": "LACA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr625.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr625"
    },
    "title": "LACA"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.</p>",
      "updateDate": "2025-03-17",
      "versionCode": "id119hr625"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr625ih.xml"
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
      "title": "LACA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-20T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "LACA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Local Access to Courts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-20T02:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To clarify where court may be held for certain district courts in Texas and California.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-20T02:03:17Z"
    }
  ]
}
```
