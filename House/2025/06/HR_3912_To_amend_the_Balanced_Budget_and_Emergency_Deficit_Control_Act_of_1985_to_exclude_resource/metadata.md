# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3912?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3912
- Title: Stop the Baseline Bloat Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3912
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2025-09-16T08:05:36Z
- Update date including text: 2025-09-16T08:05:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3912",
    "number": "3912",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "G000576",
        "district": "6",
        "firstName": "Glenn",
        "fullName": "Rep. Grothman, Glenn [R-WI-6]",
        "lastName": "Grothman",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Stop the Baseline Bloat Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-16T08:05:36Z",
    "updateDateIncludingText": "2025-09-16T08:05:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "HI"
    },
    {
      "bioguideId": "G000600",
      "district": "3",
      "firstName": "Marie",
      "fullName": "Rep. Perez, Marie Gluesenkamp [D-WA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Perez",
      "middleName": "Gluesenkamp",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "WA"
    },
    {
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "ME"
    },
    {
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "CA"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "IN"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "VA"
    },
    {
      "bioguideId": "N000190",
      "district": "5",
      "firstName": "Ralph",
      "fullName": "Rep. Norman, Ralph [R-SC-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Norman",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "SC"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-06-27",
      "state": "KS"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3912ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3912\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. Grothman (for himself, Mr. Case , Ms. Perez , Mr. Golden of Maine , Mr. Gray , Mr. Stutzman , Mr. Cline , and Mr. Norman ) introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Balanced Budget and Emergency Deficit Control Act of 1985 to exclude resources designated as an emergency requirement or any resources provided in supplemental appropriations laws from CBO baseline projections for discretionary appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop the Baseline Bloat Act of 2025 .\n#### 2. Changes in the baseline\nSection 257(c) of the Balanced Budget and Emergency Deficit Control Act of 1985 ( 2 U.S.C. 907(c) ) is amended in the second sentence of paragraph (1) by inserting excluding resources designated as an emergency requirement and any resources provided in supplemental appropriation laws, after current year, .",
      "versionDate": "2025-06-11",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-07-22T19:23:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-11",
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
          "measure-id": "id119hr3912",
          "measure-number": "3912",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-11",
          "originChamber": "HOUSE",
          "update-date": "2025-07-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3912v00",
            "update-date": "2025-07-23"
          },
          "action-date": "2025-06-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop the Baseline Bloat Act of 2025</strong></p><p>This bill changes the assumptions that the Congressional Budget Office uses to calculate the baseline for discretionary spending. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) Specifically, the bill changes the assumptions used for the discretionary spending baseline to exclude (1) resources designated as an emergency requirement, and (2) resources provided in supplemental appropriations laws.\u00a0<br/><br/></p>"
        },
        "title": "Stop the Baseline Bloat Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3912.xml",
    "summary": {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop the Baseline Bloat Act of 2025</strong></p><p>This bill changes the assumptions that the Congressional Budget Office uses to calculate the baseline for discretionary spending. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) Specifically, the bill changes the assumptions used for the discretionary spending baseline to exclude (1) resources designated as an emergency requirement, and (2) resources provided in supplemental appropriations laws.\u00a0<br/><br/></p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr3912"
    },
    "title": "Stop the Baseline Bloat Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop the Baseline Bloat Act of 2025</strong></p><p>This bill changes the assumptions that the Congressional Budget Office uses to calculate the baseline for discretionary spending. (A baseline is a projection of federal spending and receipts during a fiscal year under current law.) Specifically, the bill changes the assumptions used for the discretionary spending baseline to exclude (1) resources designated as an emergency requirement, and (2) resources provided in supplemental appropriations laws.\u00a0<br/><br/></p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr3912"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3912ih.xml"
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
      "title": "Stop the Baseline Bloat Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop the Baseline Bloat Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Balanced Budget and Emergency Deficit Control Act of 1985 to exclude resources designated as an emergency requirement or any resources provided in supplemental appropriations laws from CBO baseline projections for discretionary appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T06:18:27Z"
    }
  ]
}
```
