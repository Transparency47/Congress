# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/557?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/557
- Title: Honoring the life, achievements, and legacy of Frederick W. Smith.
- Congress: 119
- Bill type: HRES
- Bill number: 557
- Origin chamber: House
- Introduced date: 2025-06-27
- Update date: 2025-08-18T10:29:33Z
- Update date including text: 2025-08-18T10:29:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-27: Introduced in House
- 2025-06-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-27 - IntroReferral: Submitted in House
- 2025-06-27 - IntroReferral: Submitted in House
- Latest action: 2025-06-27: Submitted in House

## Actions

- 2025-06-27 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-06-27 - IntroReferral: Submitted in House
- 2025-06-27 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-27",
    "latestAction": {
      "actionDate": "2025-06-27",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/557",
    "number": "557",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000392",
        "district": "8",
        "firstName": "David",
        "fullName": "Rep. Kustoff, David [R-TN-8]",
        "lastName": "Kustoff",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Honoring the life, achievements, and legacy of Frederick W. Smith.",
    "type": "HRES",
    "updateDate": "2025-08-18T10:29:33Z",
    "updateDateIncludingText": "2025-08-18T10:29:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-06-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-06-27T13:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "G000590",
      "district": "7",
      "firstName": "Mark",
      "fullName": "Rep. Green, Mark E. [R-TN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "O000175",
      "district": "5",
      "firstName": "Andrew",
      "fullName": "Rep. Ogles, Andrew [R-TN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Ogles",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "D000616",
      "district": "4",
      "firstName": "Scott",
      "fullName": "Rep. DesJarlais, Scott [R-TN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "DesJarlais",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres557ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 557\nIN THE HOUSE OF REPRESENTATIVES\nJune 27, 2025 Mr. Kustoff (for himself, Mr. Cohen , Mr. Green of Tennessee , Mr. Ogles , Mr. DesJarlais , Mr. Rose , Mr. Fleischmann , Mr. Burchett , and Mrs. Harshbarger ) submitted the following resolution; which was referred to the Committee on Oversight and Government Reform\nRESOLUTION\nHonoring the life, achievements, and legacy of Frederick W. Smith.\nThat the House of Representatives\u2014\n**(1)**\nhonors the life, achievements, and legacy of Fred Smith for\u2014\n**(A)**\nhis accomplishments as a pioneer who revolutionized the transportation and express delivery industry;\n**(B)**\nhis inspiration to future generations of American community leaders, innovators, and entrepreneurs; and\n**(C)**\nhis dedication to Memphis, a city that he loved dearly and committed to supporting and uplifting throughout his entire life; and\n**(2)**\nrespectfully requests that the Clerk of the House of Representatives transmit an enrolled copy of this resolution to the family of Fred Smith.",
      "versionDate": "2025-06-27",
      "versionType": "IH"
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-07-11T12:17:55Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-27",
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
          "measure-id": "id119hres557",
          "measure-number": "557",
          "measure-type": "hres",
          "orig-publish-date": "2025-06-27",
          "originChamber": "HOUSE",
          "update-date": "2025-08-18"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres557v00",
            "update-date": "2025-08-18"
          },
          "action-date": "2025-06-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution honors the life, achievements, and legacy of Frederick W. Smith, the founder of the company FedEx.\u00a0The resolution also honors his dedication to the city of Memphis, Tennessee.</p>"
        },
        "title": "Honoring the life, achievements, and legacy of Frederick W. Smith."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres557.xml",
    "summary": {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the life, achievements, and legacy of Frederick W. Smith, the founder of the company FedEx.\u00a0The resolution also honors his dedication to the city of Memphis, Tennessee.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres557"
    },
    "title": "Honoring the life, achievements, and legacy of Frederick W. Smith."
  },
  "summaries": [
    {
      "actionDate": "2025-06-27",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution honors the life, achievements, and legacy of Frederick W. Smith, the founder of the company FedEx.\u00a0The resolution also honors his dedication to the city of Memphis, Tennessee.</p>",
      "updateDate": "2025-08-18",
      "versionCode": "id119hres557"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres557ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Honoring the life, achievements, and legacy of Frederick W. Smith.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-28T08:18:22Z"
    },
    {
      "title": "Honoring the life, achievements, and legacy of Frederick W. Smith.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-28T08:06:05Z"
    }
  ]
}
```
