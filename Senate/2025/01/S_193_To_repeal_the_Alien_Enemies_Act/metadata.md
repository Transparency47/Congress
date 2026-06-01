# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/193?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/193
- Title: Neighbors Not Enemies Act
- Congress: 119
- Bill type: S
- Bill number: 193
- Origin chamber: Senate
- Introduced date: 2025-01-22
- Update date: 2025-12-05T21:50:49Z
- Update date including text: 2025-12-05T21:50:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in Senate
- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-01-22: Introduced in Senate

## Actions

- 2025-01-22 - IntroReferral: Introduced in Senate
- 2025-01-22 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/193",
    "number": "193",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "H001042",
        "district": "",
        "firstName": "Mazie",
        "fullName": "Sen. Hirono, Mazie K. [D-HI]",
        "lastName": "Hirono",
        "party": "D",
        "state": "HI"
      }
    ],
    "title": "Neighbors Not Enemies Act",
    "type": "S",
    "updateDate": "2025-12-05T21:50:49Z",
    "updateDateIncludingText": "2025-12-05T21:50:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T20:53:00Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "NJ"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernard",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-01-22",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-01-22",
      "state": "MA"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-28",
      "state": "CA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2025-04-30",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s193is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 193\nIN THE SENATE OF THE UNITED STATES\nJanuary 22, 2025 Ms. Hirono (for herself, Mr. Booker , Ms. Duckworth , Mr. Durbin , Mr. Markey , Mr. Sanders , and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo repeal the Alien Enemies Act.\n#### 1. Short title\nThis Act may be cited as the Neighbors Not Enemies Act .\n#### 2. Repeal of Alien Enemies Act\nSections 4067 through 4070 of the Revised Statutes of the United States ( 50 U.S.C. 21\u201324 ) are repealed.",
      "versionDate": "2025-01-22",
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
        "actionDate": "2025-01-22",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "630",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Neighbors Not Enemies Act",
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
        "updateDate": "2025-03-01T16:49:06Z"
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
          "measure-id": "id119s193",
          "measure-number": "193",
          "measure-type": "s",
          "orig-publish-date": "2025-01-22",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s193v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><b>Neighbors Not Enemies Act</b></p> <p>This bill repeals provisions authorizing the President to apprehend and remove from the United States the citizens of a particular nation, if the United States has declared war against that nation or that nation has threatened an invasion against the United States. </p>"
        },
        "title": "Neighbors Not Enemies Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s193.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Neighbors Not Enemies Act</b></p> <p>This bill repeals provisions authorizing the President to apprehend and remove from the United States the citizens of a particular nation, if the United States has declared war against that nation or that nation has threatened an invasion against the United States. </p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s193"
    },
    "title": "Neighbors Not Enemies Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><b>Neighbors Not Enemies Act</b></p> <p>This bill repeals provisions authorizing the President to apprehend and remove from the United States the citizens of a particular nation, if the United States has declared war against that nation or that nation has threatened an invasion against the United States. </p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s193"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s193is.xml"
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
      "title": "Neighbors Not Enemies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-01T11:48:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Neighbors Not Enemies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Alien Enemies Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:26Z"
    }
  ]
}
```
