# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4962?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4962
- Title: Toll of Tariffs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4962
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2026-05-26T16:00:02Z
- Update date including text: 2026-05-26T16:00:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4962",
    "number": "4962",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001221",
        "district": "3",
        "firstName": "Hillary",
        "fullName": "Rep. Scholten, Hillary J. [D-MI-3]",
        "lastName": "Scholten",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "Toll of Tariffs Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-26T16:00:02Z",
    "updateDateIncludingText": "2026-05-26T16:00:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:03:00Z",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "OH"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "True",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "CA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2026-01-09",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4962ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4962\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Ms. Scholten (for herself, Mr. Landsman , and Mr. Tran ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo direct the United States International Trade Commission to carry out a study on the inflationary impact of the tariffs imposed by certain Executive orders and to report to Congress the findings of such study.\n#### 1. Short title\nThis Act may be cited as the Toll of Tariffs Act of 2025 .\n#### 2. United states international trade commission study and report on inflationary effects of tariffs\n##### (a) Study\nThe United States International Trade Commission (in this Act referred to as the \u201cCommission\u201d) shall carry out a study on the inflationary impact of the tariffs imposed by Executive orders issued during the period beginning on or after January 20, 2025, and ending on the date of enactment of this Act.\n##### (b) Report\nNot later than 60 days after the date of enactment of this Act, the Commission shall submit to Congress a report containing\u2014\n**(1)**\nthe results of the study under subsection (a); and\n**(2)**\nimpacts to the Consumer Price Index for All Urban Consumers (CPI\u2013U) and in comparable measures tracking price changes in non-urban areas, as determined by the Bureau of Labor Statistics, of the tariffs described in subsection (a).",
      "versionDate": "2025-08-12",
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
        "name": "Foreign Trade and International Finance",
        "updateDate": "2025-09-15T17:27:28Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-12",
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
          "measure-id": "id119hr4962",
          "measure-number": "4962",
          "measure-type": "hr",
          "orig-publish-date": "2025-08-12",
          "originChamber": "HOUSE",
          "update-date": "2026-05-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4962v00",
            "update-date": "2026-05-26"
          },
          "action-date": "2025-08-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Toll of Tariffs Act of 2025</strong></p><p>This bill requires the U.S. International Trade Commission to study and report to Congress on the inflationary impact of the tariffs imposed by executive orders issued during the period beginning on or after January 20, 2025, and ending on the date of the bill's enactment.</p>"
        },
        "title": "Toll of Tariffs Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4962.xml",
    "summary": {
      "actionDate": "2025-08-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Toll of Tariffs Act of 2025</strong></p><p>This bill requires the U.S. International Trade Commission to study and report to Congress on the inflationary impact of the tariffs imposed by executive orders issued during the period beginning on or after January 20, 2025, and ending on the date of the bill's enactment.</p>",
      "updateDate": "2026-05-26",
      "versionCode": "id119hr4962"
    },
    "title": "Toll of Tariffs Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-08-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Toll of Tariffs Act of 2025</strong></p><p>This bill requires the U.S. International Trade Commission to study and report to Congress on the inflationary impact of the tariffs imposed by executive orders issued during the period beginning on or after January 20, 2025, and ending on the date of the bill's enactment.</p>",
      "updateDate": "2026-05-26",
      "versionCode": "id119hr4962"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4962ih.xml"
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
      "title": "To direct the United States International Trade Commission to carry out a study on the inflationary impact of the tariffs imposed by certain Executive orders and to report to Congress the findings of such study.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-16T08:05:47Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Toll of Tariffs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-16T03:53:18Z"
    },
    {
      "title": "Toll of Tariffs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-16T03:53:18Z"
    }
  ]
}
```
