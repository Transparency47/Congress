# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1116?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1116
- Title: Ensuring Veterans’ Final Resting Place Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1116
- Origin chamber: Senate
- Introduced date: 2025-03-25
- Update date: 2026-03-27T16:20:17Z
- Update date including text: 2026-03-27T16:20:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-25: Introduced in Senate
- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-03-25: Introduced in Senate

## Actions

- 2025-03-25 - IntroReferral: Introduced in Senate
- 2025-03-25 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2025-12-10 - Committee: Committee on Veterans' Affairs. Hearings held.
- 2026-03-18 - Committee: Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-25",
    "latestAction": {
      "actionDate": "2025-03-25",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1116",
    "number": "1116",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025",
    "type": "S",
    "updateDate": "2026-03-27T16:20:17Z",
    "updateDateIncludingText": "2026-03-27T16:20:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Veterans' Affairs. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-25",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-25",
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
        "item": [
          {
            "date": "2026-03-18T20:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-10T21:00:06Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-25T19:05:56Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "ME"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1116is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1116\nIN THE SENATE OF THE UNITED STATES\nMarch 25, 2025 Mr. Banks (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the provision of certain additional burial benefits for individuals for whom an urn or plaque is furnished, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Veterans\u2019 Final Resting Place Act of 2025 .\n#### 2. Department of Veterans Affairs provision of additional burial benefits when an urn or plaque is furnished\n##### (a) In general\nSection 2306(h) of title 38, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking In lieu of furnishing a headstone or marker under this section for and inserting In the case of ; and\n**(B)**\nby striking paragraph (3) and inserting paragraph (2) ;\n**(2)**\nby striking paragraph (2); and\n**(3)**\nby redesignating paragraphs (3) through (5) as paragraphs (2) through (4), respectively.\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to an individual who dies on or after January 5, 2021.",
      "versionDate": "2025-03-25",
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
        "actionDate": "2025-10-17",
        "text": "Placed on the Union Calendar, Calendar No. 295."
      },
      "number": "647",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Cemeteries and funerals",
            "updateDate": "2025-12-12T21:03:52Z"
          },
          {
            "name": "Veterans' organizations and recognition",
            "updateDate": "2025-12-12T21:03:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T17:42:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-25",
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
          "measure-id": "id119s1116",
          "measure-number": "1116",
          "measure-type": "s",
          "orig-publish-date": "2025-03-25",
          "originChamber": "SENATE",
          "update-date": "2025-06-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1116v00",
            "update-date": "2025-06-24"
          },
          "action-date": "2025-03-25",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Ensuring Veterans\u2019 Final Resting Place Act of 2025</strong></p><p>This bill provides that the provision of an urn or commemorative plaque does not prohibit an individual from receiving a headstone or marker or other burial benefits (i.e., interment at a national cemetery) from the Department of Veterans Affairs. Under current law, individuals who request an urn or plaque do so in lieu of being furnished a headstone or burial benefit.</p>"
        },
        "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1116.xml",
    "summary": {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Veterans\u2019 Final Resting Place Act of 2025</strong></p><p>This bill provides that the provision of an urn or commemorative plaque does not prohibit an individual from receiving a headstone or marker or other burial benefits (i.e., interment at a national cemetery) from the Department of Veterans Affairs. Under current law, individuals who request an urn or plaque do so in lieu of being furnished a headstone or burial benefit.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1116"
    },
    "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-25",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Ensuring Veterans\u2019 Final Resting Place Act of 2025</strong></p><p>This bill provides that the provision of an urn or commemorative plaque does not prohibit an individual from receiving a headstone or marker or other burial benefits (i.e., interment at a national cemetery) from the Department of Veterans Affairs. Under current law, individuals who request an urn or plaque do so in lieu of being furnished a headstone or burial benefit.</p>",
      "updateDate": "2025-06-24",
      "versionCode": "id119s1116"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1116is.xml"
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
      "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T11:03:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Veterans\u2019 Final Resting Place Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize the provision of certain additional burial benefits for individuals for whom an urn or plaque is furnished, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:48:22Z"
    }
  ]
}
```
