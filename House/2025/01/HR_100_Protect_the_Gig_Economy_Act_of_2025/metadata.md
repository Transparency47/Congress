# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/100?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/100
- Title: Protect the Gig Economy Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 100
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-07T15:43:38Z
- Update date including text: 2025-03-07T15:43:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/100",
    "number": "100",
    "originChamber": "House",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Protect the Gig Economy Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-07T15:43:38Z",
    "updateDateIncludingText": "2025-03-07T15:43:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:21:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr100ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 100\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend Rule 23 of the Federal Rules of Civil Procedure to protect the gig economy and small businesses that operate in large part through contractor services from the threat of costly class action litigation, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect the Gig Economy Act of 2025 .\n#### 2. Protecting the gig economy from class actions\nRule 23(a) of the Federal Rules of Civil Procedure is amended\u2014\n**(1)**\nin paragraph (3), by striking and at the end;\n**(2)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(3)**\nby inserting after paragraph (4) the following:\n(5) the claim does not allege the misclassification of employees as independent contractors. .",
      "versionDate": "2025-01-03",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-02-06T19:05:00Z"
          },
          {
            "name": "Self-employed",
            "updateDate": "2025-02-06T19:05:07Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-02-03T15:25:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr100",
          "measure-number": "100",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr100v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect the Gig Economy Act of 2025</strong></p><p>This bill expands the list of preliminary requirements that must be satisfied before a class action lawsuit may be brought in federal court.</p><p>Specifically, before a party may bring a class action lawsuit in federal court, the court must first determine that a new, fifth requirement has been met: that the claim does not allege misclassification of employees as independent contractors.</p>"
        },
        "title": "Protect the Gig Economy Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr100.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect the Gig Economy Act of 2025</strong></p><p>This bill expands the list of preliminary requirements that must be satisfied before a class action lawsuit may be brought in federal court.</p><p>Specifically, before a party may bring a class action lawsuit in federal court, the court must first determine that a new, fifth requirement has been met: that the claim does not allege misclassification of employees as independent contractors.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr100"
    },
    "title": "Protect the Gig Economy Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect the Gig Economy Act of 2025</strong></p><p>This bill expands the list of preliminary requirements that must be satisfied before a class action lawsuit may be brought in federal court.</p><p>Specifically, before a party may bring a class action lawsuit in federal court, the court must first determine that a new, fifth requirement has been met: that the claim does not allege misclassification of employees as independent contractors.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr100"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr100ih.xml"
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
      "title": "Protect the Gig Economy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T10:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect the Gig Economy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T10:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend Rule 23 of the Federal Rules of Civil Procedure to protect the \"gig economy\" and small businesses that operate in large part through contractor services from the threat of costly class action litigation, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T10:18:26Z"
    }
  ]
}
```
