# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/112
- Title: Make the Migrant Protection Protocols Mandatory Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 112
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2025-12-05T21:58:17Z
- Update date including text: 2025-12-05T21:58:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/112",
    "number": "112",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Make the Migrant Protection Protocols Mandatory Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:58:17Z",
    "updateDateIncludingText": "2025-12-05T21:58:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T17:50:35Z",
          "name": "Referred To"
        }
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "MT"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "ID"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SD"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "KS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "NC"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "OH"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "False",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s112is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 112\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mrs. Blackburn (for herself, Mr. Daines , Mr. Risch , Mr. Sheehy , Mr. Crapo , Mr. Rounds , Mr. Moran , and Mr. Tillis ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend section 235(b)(2)(C) of the Immigration and Nationality Act to require the implementation of the Migrant Protection Protocols.\n#### 1. Short title\nThis Act may be cited as the Make the Migrant Protection Protocols Mandatory Act of 2025 .\n#### 2. Mandatory implementation of the Migrant Protection Protocols\nSection 235(b)(2)(C) of the Immigration and Nationality Act ( 8 U.S.C. 1225(b)(2)(C) ) is amended by striking may and inserting shall .",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-16",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "551",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Make the Migrant Protection Protocols Mandatory Act of 2025",
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
        "name": "Immigration",
        "updateDate": "2025-02-19T13:22:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119s112",
          "measure-number": "112",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2025-04-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s112v00",
            "update-date": "2025-04-16"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Make the Migrant Protection Protocols Mandatory Act of 2025</strong></p><p>This bill requires the Department of Justice (DOJ) to remove certain non-U.S. nationals (<em>aliens</em> under federal law) from the United States while such an individual's application for admission is pending.</p><p>Specifically, if such an individual arrived by land from a foreign country bordering the United States and the individual is not clearly and beyond a doubt entitled to admission into the United States, DOJ must return that individual to that bordering foreign country while the individual's application for admission is pending. (Currently, DOJ may choose to detain such an individual or return the individual to the bordering foreign country while the application for admission is pending.)</p>"
        },
        "title": "Make the Migrant Protection Protocols Mandatory Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s112.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Make the Migrant Protection Protocols Mandatory Act of 2025</strong></p><p>This bill requires the Department of Justice (DOJ) to remove certain non-U.S. nationals (<em>aliens</em> under federal law) from the United States while such an individual's application for admission is pending.</p><p>Specifically, if such an individual arrived by land from a foreign country bordering the United States and the individual is not clearly and beyond a doubt entitled to admission into the United States, DOJ must return that individual to that bordering foreign country while the individual's application for admission is pending. (Currently, DOJ may choose to detain such an individual or return the individual to the bordering foreign country while the application for admission is pending.)</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s112"
    },
    "title": "Make the Migrant Protection Protocols Mandatory Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Make the Migrant Protection Protocols Mandatory Act of 2025</strong></p><p>This bill requires the Department of Justice (DOJ) to remove certain non-U.S. nationals (<em>aliens</em> under federal law) from the United States while such an individual's application for admission is pending.</p><p>Specifically, if such an individual arrived by land from a foreign country bordering the United States and the individual is not clearly and beyond a doubt entitled to admission into the United States, DOJ must return that individual to that bordering foreign country while the individual's application for admission is pending. (Currently, DOJ may choose to detain such an individual or return the individual to the bordering foreign country while the application for admission is pending.)</p>",
      "updateDate": "2025-04-16",
      "versionCode": "id119s112"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s112is.xml"
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
      "title": "Make the Migrant Protection Protocols Mandatory Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-19T03:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Make the Migrant Protection Protocols Mandatory Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend section 235(b)(2)(C) of the Immigration and Nationality Act to require the implementation of the Migrant Protection Protocols.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:25Z"
    }
  ]
}
```
