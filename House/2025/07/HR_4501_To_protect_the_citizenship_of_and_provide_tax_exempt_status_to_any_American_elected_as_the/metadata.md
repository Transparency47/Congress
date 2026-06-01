# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4501?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4501
- Title: Holy Sovereignty Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 4501
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-04-14T15:32:16Z
- Update date including text: 2026-04-14T15:32:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4501",
    "number": "4501",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001100",
        "district": "3",
        "firstName": "Jeff",
        "fullName": "Rep. Hurd, Jeff [R-CO-3]",
        "lastName": "Hurd",
        "party": "R",
        "state": "CO"
      }
    ],
    "title": "Holy Sovereignty Protection Act",
    "type": "HR",
    "updateDate": "2026-04-14T15:32:16Z",
    "updateDateIncludingText": "2026-04-14T15:32:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
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
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Ways and Means, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:06:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-17T13:06:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
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
      "sponsorshipDate": "2025-07-17",
      "state": "OK"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "WI"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "J000311",
      "district": "3",
      "firstName": "Brian",
      "fullName": "Rep. Jack, Brian [R-GA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Jack",
      "party": "R",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
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
      "sponsorshipDate": "2025-07-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4501ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4501\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Mr. Hurd of Colorado (for himself, Mr. Kelly of Pennsylvania , Mrs. Bice , Mr. Grothman , Mr. Lawler , Mr. Jack , and Mr. Fleischmann ) introduced the following bill; which was referred to the Committee on Ways and Means , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo protect the citizenship of, and provide tax-exempt status to, any American elected as the Supreme Pontiff of the Roman Catholic Church.\n#### 1. Short title\nThis Act may be cited as the Holy Sovereignty Protection Act .\n#### 2. Protection of United States citizenship\n##### (a) In general\nThe United States citizenship of any individual elected as the Supreme Pontiff of the Roman Catholic Church may not be revoked.\n##### (b) Effective date\nThis section shall take effect upon the date of enactment of this Act.\n#### 3. Tax-exempt status\n##### (a) In general\nIn the case of any citizen of the United States, such individual shall be exempt from taxation under subtitle A of the Internal Revenue Code of 1986 with respect to any taxable year any portion of which he is serving as the Supreme Pontiff of the Roman Catholic Church.\n##### (b) Effective date\nThis section shall apply to taxable years ending after May 8, 2025.",
      "versionDate": "2025-07-17",
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
        "name": "Taxation",
        "updateDate": "2025-07-30T23:22:34Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-17",
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
          "measure-id": "id119hr4501",
          "measure-number": "4501",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4501v00",
            "update-date": "2026-04-14"
          },
          "action-date": "2025-07-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Holy Sovereignty Protection Act</strong></p><p>This bill provides that the U.S. citizenship of an individual elected as the Supreme Pontiff of the Roman Catholic Church\u00a0may not be revoked and exempts such individual from federal income taxes for tax years during which the individual serves in such role for any part of the tax year. (As background, the income of a U.S. citizen generally is subject to U.S. income tax regardless of where such income is earned or received or where the individual resides.)\u00a0</p>"
        },
        "title": "Holy Sovereignty Protection Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4501.xml",
    "summary": {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Holy Sovereignty Protection Act</strong></p><p>This bill provides that the U.S. citizenship of an individual elected as the Supreme Pontiff of the Roman Catholic Church\u00a0may not be revoked and exempts such individual from federal income taxes for tax years during which the individual serves in such role for any part of the tax year. (As background, the income of a U.S. citizen generally is subject to U.S. income tax regardless of where such income is earned or received or where the individual resides.)\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr4501"
    },
    "title": "Holy Sovereignty Protection Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Holy Sovereignty Protection Act</strong></p><p>This bill provides that the U.S. citizenship of an individual elected as the Supreme Pontiff of the Roman Catholic Church\u00a0may not be revoked and exempts such individual from federal income taxes for tax years during which the individual serves in such role for any part of the tax year. (As background, the income of a U.S. citizen generally is subject to U.S. income tax regardless of where such income is earned or received or where the individual resides.)\u00a0</p>",
      "updateDate": "2026-04-14",
      "versionCode": "id119hr4501"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4501ih.xml"
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
      "title": "To protect the citizenship of, and provide tax-exempt status to, any American elected as the Supreme Pontiff of the Roman Catholic Church.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-30T12:34:00Z"
    },
    {
      "title": "Holy Sovereignty Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T06:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Holy Sovereignty Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-30T06:53:25Z"
    }
  ]
}
```
