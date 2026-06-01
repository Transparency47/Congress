# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1605
- Title: Separation of Powers Restoration Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1605
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2025-09-15T15:24:54Z
- Update date including text: 2025-09-15T15:24:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 12.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on the Judiciary.
- 2025-05-21 - Committee: Committee Consideration and Mark-up Session Held
- 2025-05-21 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 12.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1605",
    "number": "1605",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000471",
        "district": "5",
        "firstName": "Scott",
        "fullName": "Rep. Fitzgerald, Scott [R-WI-5]",
        "lastName": "Fitzgerald",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Separation of Powers Restoration Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-15T15:24:54Z",
    "updateDateIncludingText": "2025-09-15T15:24:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 15 - 12.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
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
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
            "date": "2025-05-21T14:18:48Z",
            "name": "Markup By"
          },
          {
            "date": "2025-02-26T15:04:35Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "O000177",
      "district": "3",
      "firstName": "Robert",
      "fullName": "Rep. Onder, Robert [R-MO-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Onder",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "MO"
    },
    {
      "bioguideId": "T000165",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Tiffany, Thomas P. [R-WI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Tiffany",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1605ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1605\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Fitzgerald introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 5, United States Code, to clarify the nature of judicial review of agency interpretations of statutory and regulatory provisions.\n#### 1. Short title\nThis Act may be cited as the Separation of Powers Restoration Act of 2025 or the SOPRA .\n#### 2. Judicial review of statutory and regulatory interpretations\nSection 706 of title 5, United States Code, is amended\u2014\n**(1)**\nby striking To the extent necessary and inserting (a) To the extent necessary ;\n**(2)**\nby striking decide all relevant questions of law, interpret constitutional and statutory provisions, and ;\n**(3)**\nby inserting after of the terms of an agency action the following and decide de novo all relevant questions of law, including the interpretation of constitutional and statutory provisions, and rules made by agencies. Notwithstanding any other provision of law, this subsection shall apply in any action for judicial review of agency action authorized under any provision of law. No law may exempt any such civil action from the application of this section except by specific reference to this section ; and\n**(4)**\nby striking The reviewing court shall\u2014 and inserting the following:\n(b) The reviewing court shall\u2014 .",
      "versionDate": "2025-02-26",
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
        "actionDate": "2025-01-08",
        "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs."
      },
      "number": "33",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SOPRA",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2025-06-02T20:18:11Z"
          },
          {
            "name": "Constitution and constitutional amendments",
            "updateDate": "2025-06-02T20:18:11Z"
          },
          {
            "name": "Judicial review and appeals",
            "updateDate": "2025-06-02T20:18:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-07T12:45:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-26",
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
          "measure-id": "id119hr1605",
          "measure-number": "1605",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-26",
          "originChamber": "HOUSE",
          "update-date": "2025-09-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1605v00",
            "update-date": "2025-09-15"
          },
          "action-date": "2025-02-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 202</strong><strong>5 or the SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, and (2) rules made by agencies.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>"
        },
        "title": "Separation of Powers Restoration Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1605.xml",
    "summary": {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 202</strong><strong>5 or the SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, and (2) rules made by agencies.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr1605"
    },
    "title": "Separation of Powers Restoration Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Separation of Powers Restoration Act</strong> <strong>of 202</strong><strong>5 or the SOPRA</strong></p><p>This bill modifies the scope of judicial review of agency actions to authorize courts reviewing agency actions to decide de novo (i.e., without giving deference to the agency's interpretation) all relevant questions of law, including the interpretation of (1) constitutional and statutory provisions, and (2) rules made by agencies.</p><p>No law may exempt a civil action from the standard of review required by this bill except by specific reference to such provision.</p>",
      "updateDate": "2025-09-15",
      "versionCode": "id119hr1605"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1605ih.xml"
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
      "title": "Separation of Powers Restoration Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:53:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Separation of Powers Restoration Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 5, United States Code, to clarify the nature of judicial review of agency interpretations of statutory and regulatory provisions.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:29Z"
    }
  ]
}
```
