# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6332?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6332
- Title: To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the "Congressman Gerald E. Connolly Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 6332
- Origin chamber: House
- Introduced date: 2025-12-01
- Update date: 2025-12-08T19:05:17Z
- Update date including text: 2025-12-08T19:05:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-01: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported by the Yeas and Nays: 38 - 2.
- Latest action: 2025-12-01: Introduced in House

## Actions

- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Introduced in House
- 2025-12-01 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-02 - Committee: Ordered to be Reported by the Yeas and Nays: 38 - 2.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6332",
    "number": "6332",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000831",
        "district": "11",
        "firstName": "James",
        "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
        "lastName": "Walkinshaw",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\".",
    "type": "HR",
    "updateDate": "2025-12-08T19:05:17Z",
    "updateDateIncludingText": "2025-12-08T19:05:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 38 - 2.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-01",
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
      "actionCode": "Intro-H",
      "actionDate": "2025-12-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-01",
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
        "item": [
          {
            "date": "2025-12-02T17:51:43Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-01T17:02:45Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001108",
      "district": "1",
      "firstName": "James",
      "fullName": "Rep. Comer, James [R-KY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Comer",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "KY"
    },
    {
      "bioguideId": "S000185",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "middleName": "C. \"Bobby\"",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "B001292",
      "district": "8",
      "firstName": "Donald",
      "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Beyer",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
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
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "VA"
    },
    {
      "bioguideId": "G000558",
      "district": "2",
      "firstName": "Brett",
      "fullName": "Rep. Guthrie, Brett [R-KY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Guthrie",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "KY"
    },
    {
      "bioguideId": "T000463",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. Turner, Michael R. [R-OH-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Turner",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OH"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6332ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6332\nIN THE HOUSE OF REPRESENTATIVES\nDecember 1, 2025 Mr. Walkinshaw (for himself, Mr. Comer , Mr. Scott of Virginia , Ms. McClellan , Mr. Beyer , Mr. Subramanyam , Mr. Vindman , Mr. McGuire , Mr. Wittman , Mr. Guthrie , and Mr. Turner of Ohio ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the Congressman Gerald E. Connolly Post Office Building .\n#### 1. Congressman Gerald E. Connolly Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, shall be known and designated as the Congressman Gerald E. Connolly Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Congressman Gerald E. Connolly Post Office Building .",
      "versionDate": "2025-12-01",
      "versionType": "Introduced in House"
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
            "name": "Congressional tributes",
            "updateDate": "2025-12-08T19:45:51Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-12-08T19:45:51Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-12-08T19:45:51Z"
          },
          {
            "name": "Virginia",
            "updateDate": "2025-12-08T19:45:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-08T15:59:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-01",
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
          "measure-id": "id119hr6332",
          "measure-number": "6332",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-01",
          "originChamber": "HOUSE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6332v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-12-01",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6332.xml",
    "summary": {
      "actionDate": "2025-12-01",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\".",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr6332"
    },
    "title": "To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-12-01",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\".",
      "updateDate": "2025-12-02",
      "versionCode": "id119hr6332"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6332ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:23Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 10660 Page Avenue in Fairfax, Virginia, as the \"Congressman Gerald E. Connolly Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T09:05:32Z"
    }
  ]
}
```
