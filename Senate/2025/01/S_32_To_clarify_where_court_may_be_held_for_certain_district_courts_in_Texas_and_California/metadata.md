# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/32?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/32
- Title: LACA
- Congress: 119
- Bill type: S
- Bill number: 32
- Origin chamber: Senate
- Introduced date: 2025-01-08
- Update date: 2025-12-05T21:45:36Z
- Update date including text: 2025-12-05T21:45:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-08: Introduced in Senate
- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-02-12 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S932; text: CR S932)
- 2025-02-12 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-02-12 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-02-12 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-02-13 - Floor: Message on Senate action sent to the House.
- 2025-02-13 10:47:35 - Floor: Received in the House.
- 2025-02-13 10:56:41 - Floor: Held at the desk.
- Latest action: 2025-01-08: Introduced in Senate

## Actions

- 2025-01-08 - IntroReferral: Introduced in Senate
- 2025-01-08 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- 2025-02-12 - Floor: Passed Senate without amendment by Unanimous Consent. (consideration: CR S932; text: CR S932)
- 2025-02-12 - Floor: Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.
- 2025-02-12 - Discharge: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-02-12 - Committee: Senate Committee on the Judiciary discharged by Unanimous Consent.
- 2025-02-13 - Floor: Message on Senate action sent to the House.
- 2025-02-13 10:47:35 - Floor: Received in the House.
- 2025-02-13 10:56:41 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-08",
    "latestAction": {
      "actionDate": "2025-01-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/32",
    "number": "32",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
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
    "title": "LACA",
    "type": "S",
    "updateDate": "2025-12-05T21:45:36Z",
    "updateDateIncludingText": "2025-12-05T21:45:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-02-13",
      "actionTime": "10:56:41",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-02-13",
      "actionTime": "10:47:35",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate without amendment by Unanimous Consent. (consideration: CR S932; text: CR S932)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate without amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2025-02-12",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on the Judiciary discharged by Unanimous Consent.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-08",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-08",
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
        "item": [
          {
            "date": "2025-02-13T01:38:04Z",
            "name": "Discharged From"
          },
          {
            "date": "2025-01-08T16:32:33Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-01-08",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s32is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 32\nIN THE SENATE OF THE UNITED STATES\nJanuary 8, 2025 Mr. Cruz (for himself and Mr. Padilla ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo clarify where court may be held for certain district courts in Texas and California.\n#### 1. Short title\nThis Act may be cited as the Local Access to Courts Act or LACA .\n#### 2. Organization of Texas district courts\nSection 124(b)(2) of title 28, United States Code, is amended, in the matter preceding paragraph (3), by inserting and College Station before the period at the end.\n#### 3. Organization of California district courts\nSection 84(d) of title 28, United States Code, is amended by inserting and El Centro after at San Diego .",
      "versionDate": "2025-01-08",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s32es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 32\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo clarify where court may be held for certain district courts in Texas and California.\n#### 1. Short title\nThis Act may be cited as the Local Access to Courts Act or LACA .\n#### 2. Organization of Texas district courts\nSection 124(b)(2) of title 28, United States Code, is amended, in the matter preceding paragraph (3), by inserting and College Station before the period at the end.\n#### 3. Organization of California district courts\nSection 84(d) of title 28, United States Code, is amended by inserting and El Centro after at San Diego .",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "118",
      "latestAction": {
        "actionDate": "2024-12-17",
        "actionTime": "10:47:31",
        "text": "Held at the desk."
      },
      "number": "5465",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to clarify where court may be held for certain district courts in Texas and California.",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "625",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "LACA",
      "type": "HR"
    },
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
            "updateDate": "2025-02-07T14:38:11Z"
          },
          {
            "name": "State and local courts",
            "updateDate": "2025-02-07T14:38:18Z"
          },
          {
            "name": "Texas",
            "updateDate": "2025-02-07T14:38:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-01-27T13:49:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-08",
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
          "measure-id": "id119s32",
          "measure-number": "32",
          "measure-type": "s",
          "orig-publish-date": "2025-01-08",
          "originChamber": "SENATE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s32v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-08",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.\u00a0</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.\u00a0</p><p>\u00a0</p>"
        },
        "title": "LACA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s32.xml",
    "summary": {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.\u00a0</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s32"
    },
    "title": "LACA"
  },
  "summaries": [
    {
      "actionDate": "2025-01-08",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Local Access to Courts Act or LACA</strong></p><p>This bill adds College Station to the list of places where court must be held in the Galveston Division of the Southern District of Texas.\u00a0</p><p>Additionally, the bill adds El Centro to the list of places where court must be held in the Southern District of California.\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119s32"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s32is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s32es.xml"
        }
      ],
      "type": "Engrossed in Senate"
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
      "updateDate": "2025-02-14T12:03:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "LACA",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-02-13T05:23:18Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Local Access to Courts Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-02-13T05:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LACA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-23T13:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Local Access to Courts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-23T13:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to clarify where court may be held for certain district courts in Texas and California.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-23T13:33:20Z"
    }
  ]
}
```
