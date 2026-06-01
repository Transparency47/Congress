# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3651?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3651
- Title: Protecting Our Protesters Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3651
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2026-04-14T20:39:50Z
- Update date including text: 2026-04-14T20:39:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3651",
    "number": "3651",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "O000173",
        "district": "5",
        "firstName": "Ilhan",
        "fullName": "Rep. Omar, Ilhan [D-MN-5]",
        "lastName": "Omar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Protecting Our Protesters Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T20:39:50Z",
    "updateDateIncludingText": "2026-04-14T20:39:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:06:50Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "MS"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "WA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3651ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3651\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Ms. Omar (for herself, Mr. Thompson of Mississippi , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to clarify the penalty for use of force, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Our Protesters Act of 2025 .\n#### 2. Clarification of deprivation of rights under color of law\nSection 242 of title 18, United States Code, is amended\u2014\n**(1)**\nby striking United States, and inserting United States, including the use of force during a response to a protest, ; and\n**(2)**\nby striking , or may be sentenced to death .",
      "versionDate": "2025-05-29",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-06-20T13:16:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-29",
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
          "measure-id": "id119hr3651",
          "measure-number": "3651",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-29",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3651v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-05-29",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Our Protesters Act of 2025</strong></p><p>This bill modifies the criminal civil rights statute that prohibits deprivation of rights under color of law.</p><p>Current law prohibits the deprivation of federally protected rights, privileges, or immunities by a government official (including a law enforcement officer).</p><p>This bill specifies that use of force during a response to a protest constitutes a deprivation of rights, privileges, or immunities.</p><p>Additionally, the bill removes the death penalty as a penalty option if death results or if certain aggravating factors are present.</p>"
        },
        "title": "Protecting Our Protesters Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3651.xml",
    "summary": {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Protesters Act of 2025</strong></p><p>This bill modifies the criminal civil rights statute that prohibits deprivation of rights under color of law.</p><p>Current law prohibits the deprivation of federally protected rights, privileges, or immunities by a government official (including a law enforcement officer).</p><p>This bill specifies that use of force during a response to a protest constitutes a deprivation of rights, privileges, or immunities.</p><p>Additionally, the bill removes the death penalty as a penalty option if death results or if certain aggravating factors are present.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3651"
    },
    "title": "Protecting Our Protesters Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-29",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Our Protesters Act of 2025</strong></p><p>This bill modifies the criminal civil rights statute that prohibits deprivation of rights under color of law.</p><p>Current law prohibits the deprivation of federally protected rights, privileges, or immunities by a government official (including a law enforcement officer).</p><p>This bill specifies that use of force during a response to a protest constitutes a deprivation of rights, privileges, or immunities.</p><p>Additionally, the bill removes the death penalty as a penalty option if death results or if certain aggravating factors are present.</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr3651"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3651ih.xml"
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
      "title": "Protecting Our Protesters Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T05:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Our Protesters Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to clarify the penalty for use of force, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T05:18:30Z"
    }
  ]
}
```
