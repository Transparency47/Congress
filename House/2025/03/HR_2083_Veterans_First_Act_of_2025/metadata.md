# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2083?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2083
- Title: Veterans First Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2083
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-12-05T22:59:12Z
- Update date including text: 2025-12-05T22:59:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2083",
    "number": "2083",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "T000490",
        "district": "2",
        "firstName": "David",
        "fullName": "Rep. Taylor, David [R-OH-2]",
        "lastName": "Taylor",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Veterans First Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:59:12Z",
    "updateDateIncludingText": "2025-12-05T22:59:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:02:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NY"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "MO"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "NC"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "OH"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "AL"
    },
    {
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-03-31",
      "state": "CA"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "MN"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "NE"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "SC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2083ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2083\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Taylor (for himself, Mr. Hunt , Mr. LaLota , Mr. Wied , Mr. Onder , and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nTo rescind an amount appropriated to the United States Agency for International Development and appropriate such amount to the Department of Veterans Affairs for the construction of State homes for veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans First Act of 2025 .\n#### 2. Funding for grants for construction of State homes for veterans\n##### (a) Rescission\nFrom the unobligated balance of amounts made available to the United States Agency for International Development, $2,000,000,000 is hereby permanently rescinded.\n##### (b) Appropriation\nThere is appropriated to the Department of Veterans Affairs $2,000,000,000 for grants to assist States to acquire or construct State nursing home and domiciliary facilities and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in State homes, for furnishing care to veterans as authorized by sections 8131 through 8138 of title 38, United States Code, to remain available until expended.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "1424",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Veterans First Act of 2025",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-09T12:55:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2083",
          "measure-number": "2083",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2083v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>"
        },
        "title": "Veterans First Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2083.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr2083"
    },
    "title": "Veterans First Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans First Act of 2025</strong></p><p>This bill rescinds $2 billion of the unobligated funds that were provided to the U.S. Agency for International Development. It also provides $2 billion in appropriations to the Department of Veterans Affairs for grants to assist states to acquire or construct state nursing home and\u00a0domiciliary facilities\u00a0and to remodel, modify, or alter existing hospital, nursing home, and domiciliary facilities in state homes for furnishing care to veterans,\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr2083"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2083ih.xml"
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
      "title": "Veterans First Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T02:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans First Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T02:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To rescind an amount appropriated to the United States Agency for International Development and appropriate such amount to the Department of Veterans Affairs for the construction of State homes for veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T02:03:22Z"
    }
  ]
}
```
