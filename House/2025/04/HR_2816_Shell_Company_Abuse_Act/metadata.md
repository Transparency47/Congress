# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2816?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2816
- Title: Shell Company Abuse Act
- Congress: 119
- Bill type: HR
- Bill number: 2816
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-04-27T14:56:57Z
- Update date including text: 2026-04-27T14:56:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2816",
    "number": "2816",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "B001324",
        "district": "1",
        "firstName": "Wesley",
        "fullName": "Rep. Bell, Wesley [D-MO-1]",
        "lastName": "Bell",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Shell Company Abuse Act",
    "type": "HR",
    "updateDate": "2026-04-27T14:56:57Z",
    "updateDateIncludingText": "2026-04-27T14:56:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:03:10Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "NE"
    },
    {
      "bioguideId": "C001121",
      "district": "6",
      "firstName": "Jason",
      "fullName": "Rep. Crow, Jason [D-CO-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Crow",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "PA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "NJ"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2816ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2816\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Bell (for himself, Mr. Bacon , Mr. Crow , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo amend title 18, United States Code, to prohibit the establishment of a corporation to conceal election contributions and donations by foreign nationals.\n#### 1. Short title\nThis Act may be cited as the Shell Company Abuse Act .\n#### 2. Prohibition\n##### (a) In general\nChapter 29 of title 18, United States Code, is amended by adding at the end the following:\n612. Establishment of corporation to conceal election contributions and donations by foreign nationals (a) Offense It shall be unlawful for an owner, officer, attorney, or incorporation agent of a corporation, company, or other entity to establish or use the corporation, company, or other entity with the intent to conceal an activity of a foreign national (as defined in section 319 of the Federal Election Campaign Act of 1971 ( 52 U.S.C. 30121 )) prohibited under such section 319. (b) Penalty Any person who violates subsection (a) shall be imprisoned for not more than 5 years, fined under this title, or both. .\n##### (b) Table of sections\nThe table of sections for chapter 29 of title 18, United States Code, is amended by inserting after the item relating to section 611 the following:\n612. Establishment of corporation to conceal election contributions and donations by foreign nationals. .",
      "versionDate": "2025-04-10",
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
        "actionDate": "2026-03-04",
        "text": "Referred to the Committee on House Administration, and in addition to the Committees on Ways and Means, and the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7802",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DISCLOSE Act of 2026",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-03-04",
        "text": "Read twice and referred to the Committee on Rules and Administration."
      },
      "number": "3991",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DISCLOSE Act of 2026",
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
            "name": "Business ethics",
            "updateDate": "2025-08-08T18:28:45Z"
          },
          {
            "name": "Corporate finance and management",
            "updateDate": "2025-08-08T18:28:45Z"
          },
          {
            "name": "Criminal procedure and sentencing",
            "updateDate": "2025-08-08T18:28:45Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-08-08T18:28:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-05-23T14:22:50Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119hr2816",
          "measure-number": "2816",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2816v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><b>Shell Company Abuse Act</b></p> <p>This bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national.</p> <p>A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p>"
        },
        "title": "Shell Company Abuse Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2816.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Shell Company Abuse Act</b></p> <p>This bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national.</p> <p>A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr2816"
    },
    "title": "Shell Company Abuse Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><b>Shell Company Abuse Act</b></p> <p>This bill makes it unlawful to establish or use a corporation, company, or other entity with the intent to conceal an election contribution or donation by a foreign national.</p> <p>A violator is subject to criminal penalties\u2014a fine, a prison term of up to five years, or both.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr2816"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2816ih.xml"
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
      "title": "Shell Company Abuse Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Shell Company Abuse Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 18, United States Code, to prohibit the establishment of a corporation to conceal election contributions and donations by foreign nationals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:29Z"
    }
  ]
}
```
