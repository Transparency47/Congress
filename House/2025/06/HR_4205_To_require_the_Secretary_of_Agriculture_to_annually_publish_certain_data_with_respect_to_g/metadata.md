# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4205?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4205
- Title: Fairness in Vineyard Data Act
- Congress: 119
- Bill type: HR
- Bill number: 4205
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-05-19T12:31:05Z
- Update date including text: 2026-05-19T12:31:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4205",
    "number": "4205",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000478",
        "district": "24",
        "firstName": "Claudia",
        "fullName": "Rep. Tenney, Claudia [R-NY-24]",
        "lastName": "Tenney",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Fairness in Vineyard Data Act",
    "type": "HR",
    "updateDate": "2026-05-19T12:31:05Z",
    "updateDateIncludingText": "2026-05-19T12:31:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:02:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "M001206",
      "district": "25",
      "firstName": "Joseph",
      "fullName": "Rep. Morelle, Joseph D. [D-NY-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Morelle",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4205ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4205\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Ms. Tenney (for herself and Mr. Morelle ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo require the Secretary of Agriculture to annually publish certain data with respect to grape production, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fairness in Vineyard Data Act .\n#### 2. Grape production data\n##### (a) In general\nThe Secretary of Agriculture, acting through the Administrator of the National Agricultural Statistics Service, shall\u2014\n**(1)**\nnot later than 1 year after the date of the enactment of this Act\u2014\n**(A)**\nconduct a survey on grape production in each State, including\u2014\n**(i)**\ntotal acreage; and\n**(ii)**\nproduction, utilization, and acreage by type, variety, county, and year planted; and\n**(B)**\nmake publicly available on the website of the National Agricultural Statistics Service the results of such survey and the data from such survey; and\n**(2)**\nnot later than 2 years after the date of the enactment of this Act and annually for the 3 years thereafter, make publicly available on the website of the National Agricultural Statistics Service data from the 5 States with the highest grape production in the preceding year, as determined using data from the survey required under paragraph (1)(A).\n##### (b) Authorization of appropriations\n**(1) Survey**\nThere is authorized to be appropriated to carry out subparagraphs (A) and (B) of subsection (a)(1) $2,500,000 for fiscal year 2026.\n**(2) Publication of data**\nThere is authorized to be appropriated to carry out subsection (a)(2) $1,500,000 for each of fiscal years 2027 through 2030.",
      "versionDate": "2025-06-26",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-07-11T17:47:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-26",
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
          "measure-id": "id119hr4205",
          "measure-number": "4205",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-26",
          "originChamber": "HOUSE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4205v00",
            "update-date": "2026-05-19"
          },
          "action-date": "2025-06-26",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fairness in Vineyard Data Act</strong></p><p>This bill requires the National Agricultural Statistics Service (NASS) to conduct a survey, within one year of the bill's enactment, on grape production in each state and publish the data on the NASS website.\u00a0In each of the following four years, NASS must make publicly available on the website data from the five states with the highest grape production in the preceding year.\u00a0</p>"
        },
        "title": "Fairness in Vineyard Data Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4205.xml",
    "summary": {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness in Vineyard Data Act</strong></p><p>This bill requires the National Agricultural Statistics Service (NASS) to conduct a survey, within one year of the bill's enactment, on grape production in each state and publish the data on the NASS website.\u00a0In each of the following four years, NASS must make publicly available on the website data from the five states with the highest grape production in the preceding year.\u00a0</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr4205"
    },
    "title": "Fairness in Vineyard Data Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-26",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fairness in Vineyard Data Act</strong></p><p>This bill requires the National Agricultural Statistics Service (NASS) to conduct a survey, within one year of the bill's enactment, on grape production in each state and publish the data on the NASS website.\u00a0In each of the following four years, NASS must make publicly available on the website data from the five states with the highest grape production in the preceding year.\u00a0</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119hr4205"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4205ih.xml"
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
      "title": "Fairness in Vineyard Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-08T07:23:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fairness in Vineyard Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-08T07:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Agriculture to annually publish certain data with respect to grape production, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-08T07:18:50Z"
    }
  ]
}
```
