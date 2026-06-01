# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7808?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7808
- Title: Debt-to-GDP Transparency and Stabilization Act
- Congress: 119
- Bill type: HR
- Bill number: 7808
- Origin chamber: House
- Introduced date: 2026-03-04
- Update date: 2026-05-21T08:08:53Z
- Update date including text: 2026-05-21T08:08:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-03-04: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-04 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-04: Introduced in House

## Actions

- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Introduced in House
- 2026-03-04 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-04 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7808",
    "number": "7808",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "S001199",
        "district": "11",
        "firstName": "Lloyd",
        "fullName": "Rep. Smucker, Lloyd [R-PA-11]",
        "lastName": "Smucker",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Debt-to-GDP Transparency and Stabilization Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:08:53Z",
    "updateDateIncludingText": "2026-05-21T08:08:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-04",
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
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T15:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-04T15:01:15Z",
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
      "bioguideId": "G000592",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Golden, Jared F. [D-ME-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Golden",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "ME"
    },
    {
      "bioguideId": "C001118",
      "district": "6",
      "firstName": "Ben",
      "fullName": "Rep. Cline, Ben [R-VA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Cline",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "VA"
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
      "sponsorshipDate": "2026-03-04",
      "state": "WA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "NE"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "PA"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-03-04",
      "state": "WI"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "NC"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "AR"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "HI"
    },
    {
      "bioguideId": "S001183",
      "district": "1",
      "firstName": "David",
      "fullName": "Rep. Schweikert, David [R-AZ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Schweikert",
      "party": "R",
      "sponsorshipDate": "2026-05-20",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7808ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7808\nIN THE HOUSE OF REPRESENTATIVES\nMarch 4, 2026 Mr. Smucker (for himself, Mr. Golden of Maine , Mr. Cline , Ms. Perez , Mr. Yakym , Mr. Suozzi , Mr. Bacon , Mr. Meuser , Mr. Panetta , Mr. Grothman , Mr. Peters , and Mr. Davis of North Carolina ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require that the President\u2019s annual budget submission to Congress and any concurrent resolution on the budget include the ratio of the public debt to the estimated gross domestic product of the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Debt-to-GDP Transparency and Stabilization Act .\n#### 2. Ratio of public debt to GDP included in President\u2019s budget submission and concurrent resolution on the budget\n##### (a) President\u2019s budget submission\nSection 1105(a) of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (10), by striking the period at the end and inserting , including the ratio of the public debt to the estimated gross domestic product. ; and\n**(2)**\nby adding at the end the following:\n(39) the ratio of the surplus or deficit to the estimated gross domestic product. .\n##### (b) Concurrent resolution on the budget\nSection 301(a) of the Congressional Budget and Impoundment Control Act of 1974 is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(8) the ratio of the public debt to the estimated gross domestic product; and (9) the ratio of the surplus or deficit to the estimated gross domestic product. .",
      "versionDate": "2026-03-04",
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
        "updateDate": "2026-03-31T21:00:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-04",
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
          "measure-id": "id119hr7808",
          "measure-number": "7808",
          "measure-type": "hr",
          "orig-publish-date": "2026-03-04",
          "originChamber": "HOUSE",
          "update-date": "2026-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7808v00",
            "update-date": "2026-04-01"
          },
          "action-date": "2026-03-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Debt-to-GDP Transparency and Stabilization Act</strong></p><p>This bill requires the President's annual budget and congressional budget resolutions to include (1) the ratio of the public debt to the estimated gross domestic product (GDP), and (2) the ratio of the surplus or deficit to the estimated GDP.\u00a0</p>"
        },
        "title": "Debt-to-GDP Transparency and Stabilization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7808.xml",
    "summary": {
      "actionDate": "2026-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Debt-to-GDP Transparency and Stabilization Act</strong></p><p>This bill requires the President's annual budget and congressional budget resolutions to include (1) the ratio of the public debt to the estimated gross domestic product (GDP), and (2) the ratio of the surplus or deficit to the estimated GDP.\u00a0</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr7808"
    },
    "title": "Debt-to-GDP Transparency and Stabilization Act"
  },
  "summaries": [
    {
      "actionDate": "2026-03-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Debt-to-GDP Transparency and Stabilization Act</strong></p><p>This bill requires the President's annual budget and congressional budget resolutions to include (1) the ratio of the public debt to the estimated gross domestic product (GDP), and (2) the ratio of the surplus or deficit to the estimated GDP.\u00a0</p>",
      "updateDate": "2026-04-01",
      "versionCode": "id119hr7808"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7808ih.xml"
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
      "title": "Debt-to-GDP Transparency and Stabilization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-24T07:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Debt-to-GDP Transparency and Stabilization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-24T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require that the President's annual budget submission to Congress and any concurrent resolution on the budget include the ratio of the public debt to the estimated gross domestic product of the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-24T07:18:35Z"
    }
  ]
}
```
