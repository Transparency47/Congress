# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6738?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6738
- Title: Protecting Ballot Measures From Foreign Influence Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6738
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-04-10T12:51:18Z
- Update date including text: 2026-04-10T12:51:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on House Administration.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on House Administration.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6738",
    "number": "6738",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001118",
        "district": "6",
        "firstName": "Ben",
        "fullName": "Rep. Cline, Ben [R-VA-6]",
        "lastName": "Cline",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-10T12:51:18Z",
    "updateDateIncludingText": "2026-04-10T12:51:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on House Administration.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "WA"
    },
    {
      "bioguideId": "B000740",
      "district": "5",
      "firstName": "Stephanie",
      "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bice",
      "middleName": "I.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "OK"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
    },
    {
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NE"
    },
    {
      "bioguideId": "L000583",
      "district": "11",
      "firstName": "Barry",
      "fullName": "Rep. Loudermilk, Barry [R-GA-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Loudermilk",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
    },
    {
      "bioguideId": "H001077",
      "district": "3",
      "firstName": "Clay",
      "fullName": "Rep. Higgins, Clay [R-LA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Higgins",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "LA"
    },
    {
      "bioguideId": "H001095",
      "district": "38",
      "firstName": "Wesley",
      "fullName": "Rep. Hunt, Wesley [R-TX-38]",
      "isOriginalCosponsor": "True",
      "lastName": "Hunt",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001240",
      "district": "6",
      "firstName": "Addison",
      "fullName": "Rep. McDowell, Addison P. [R-NC-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McDowell",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "NC"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-12-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6738ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6738\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Cline (for himself, Ms. Perez , Mrs. Bice , Mr. McGuire , Mr. Smith of Nebraska , Mr. Loudermilk , Mr. Higgins of Louisiana , Mr. Hunt , and Mr. McDowell ) introduced the following bill; which was referred to the Committee on House Administration\nA BILL\nTo amend the Federal Election Campaign Act of 1971 to prohibit contributions and donations by foreign nationals in connection with ballot initiatives and referenda.\n#### 1. Short title\nThis Act may be cited as the Protecting Ballot Measures From Foreign Influence Act of 2025 .\n#### 2. Prohibition on contributions and donations by foreign nationals in connection with ballot initiatives and referenda\n##### (a) Prohibition\nSection 319(a)(1)(A) of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121(a)(1)(A) ) is amended by inserting , or a State or local ballot initiative or ballot referendum after election .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to contributions and donations made on or after the date of enactment of this Act.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-10-22",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "3028",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-08T17:52:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-16",
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
          "measure-id": "id119hr6738",
          "measure-number": "6738",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-16",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6738v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2025-12-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>"
        },
        "title": "Protecting Ballot Measures From Foreign Influence Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6738.xml",
    "summary": {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6738"
    },
    "title": "Protecting Ballot Measures From Foreign Influence Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-12-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Ballot Measures From Foreign Influence Act</strong> <strong>of 2025</strong></p><p>This bill prohibits contributions or donations by foreign nationals in connection with state or local ballot initiatives or referenda.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr6738"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6738ih.xml"
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
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-08T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Ballot Measures From Foreign Influence Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-08T06:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Election Campaign Act of 1971 to prohibit contributions and donations by foreign nationals in connection with ballot initiatives and referenda.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-08T06:03:17Z"
    }
  ]
}
```
