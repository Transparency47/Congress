# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/44?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/44
- Title: A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.
- Congress: 119
- Bill type: S
- Bill number: 44
- Origin chamber: Senate
- Introduced date: 2025-01-09
- Update date: 2025-12-06T06:49:14Z
- Update date including text: 2025-12-06T06:49:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in Senate
- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.
- Latest action: 2025-01-09: Introduced in Senate

## Actions

- 2025-01-09 - IntroReferral: Introduced in Senate
- 2025-01-09 - IntroReferral: Read twice and referred to the Committee on Rules and Administration.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/44",
    "number": "44",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.",
    "type": "S",
    "updateDate": "2025-12-06T06:49:14Z",
    "updateDateIncludingText": "2025-12-06T06:49:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Rules and Administration Committee",
          "systemCode": "ssra00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Rules and Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T19:39:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Rules and Administration Committee",
      "systemCode": "ssra00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "AR"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "True",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "OK"
    },
    {
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-01-09",
      "state": "VA"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-24",
      "state": "WV"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-06-04",
      "state": "AZ"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-06-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s44is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 44\nIN THE SENATE OF THE UNITED STATES\nJanuary 9, 2025 Mr. Coons (for himself, Mr. Boozman , Mr. Lankford , and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Rules and Administration\nA BILL\nTo direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.\n#### 1. Procurement and placement of statue of Benjamin Franklin in the United States Capitol\n##### (a) Obtaining of statue\nNot later than December 31, 2025, the Joint Committee of Congress on the Library (referred to in this section as the Joint Committee ) shall enter into an agreement to obtain a statue of Benjamin Franklin, under such terms and conditions as the Joint Committee considers appropriate consistent with applicable law.\n##### (b) Placement\nNot later than December 31, 2026, the Joint Committee shall place the statue obtained under subsection (a) in a suitable permanent location in the United States Capitol where the statue is accessible to the public during a guided tour of the Capitol provided by the Office of the Capitol Visitor Center.",
      "versionDate": "2025-01-09",
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
        "actionDate": "2025-02-27",
        "text": "Received in the Senate and Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "250",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To direct the Joint Committee on the Library to procure a statue of Benjamin Franklin for placement in the Capitol.",
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
            "name": "Joint Committee on the Library",
            "updateDate": "2025-02-24T19:54:23Z"
          },
          {
            "name": "Monuments and memorials",
            "updateDate": "2025-02-24T19:54:23Z"
          },
          {
            "name": "U.S. Capitol",
            "updateDate": "2025-02-24T19:54:23Z"
          },
          {
            "name": "U.S. history",
            "updateDate": "2025-02-24T19:54:23Z"
          }
        ]
      },
      "policyArea": {
        "name": "Congress",
        "updateDate": "2025-02-10T20:01:39Z"
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
          "measure-id": "id119s44",
          "measure-number": "44",
          "measure-type": "s",
          "orig-publish-date": "2025-01-09",
          "originChamber": "SENATE",
          "update-date": "2025-02-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s44v00",
            "update-date": "2025-02-12"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>"
        },
        "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s44.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s44"
    },
    "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol."
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill requires the Joint Committee on the Library to contract for and place a\u00a0statue of Benjamin Franklin in the Capitol.</p><p>The committee shall place the statue in a permanent public location\u00a0where it is accessible during a guided tour provided by the Capitol Visitor Center.</p><p>The contract must be executed by December 31, 2025, and the\u00a0statue must be placed by\u00a0December 31, 2026.\u00a0</p>",
      "updateDate": "2025-02-12",
      "versionCode": "id119s44"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s44is.xml"
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
      "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:03:36Z"
    },
    {
      "title": "A bill to direct the Joint Committee of Congress on the Library to procure a statue of Benjamin Franklin for placement in the United States Capitol.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-10T11:56:26Z"
    }
  ]
}
```
