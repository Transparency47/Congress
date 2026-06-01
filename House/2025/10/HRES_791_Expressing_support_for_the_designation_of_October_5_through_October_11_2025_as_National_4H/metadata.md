# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/791?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/791
- Title: Expressing support for the designation of October 5 through October 11, 2025, as "National 4-H Week".
- Congress: 119
- Bill type: HRES
- Bill number: 791
- Origin chamber: House
- Introduced date: 2025-10-06
- Update date: 2026-04-03T16:21:13Z
- Update date including text: 2026-04-03T16:21:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-06: Introduced in House
- 2025-10-06 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-06 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-06 - IntroReferral: Submitted in House
- 2025-10-06 - IntroReferral: Submitted in House
- Latest action: 2025-10-06: Submitted in House

## Actions

- 2025-10-06 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-06 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-06 - IntroReferral: Submitted in House
- 2025-10-06 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-06",
    "latestAction": {
      "actionDate": "2025-10-06",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/791",
    "number": "791",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Expressing support for the designation of October 5 through October 11, 2025, as \"National 4-H Week\".",
    "type": "HRES",
    "updateDate": "2026-04-03T16:21:13Z",
    "updateDateIncludingText": "2026-04-03T16:21:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-10-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-10-06T19:00:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-10-06T19:00:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "MN"
    },
    {
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-10-06",
      "state": "GA"
    },
    {
      "bioguideId": "H001052",
      "district": "1",
      "firstName": "Andy",
      "fullName": "Rep. Harris, Andy [R-MD-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harris",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres791ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 791\nIN THE HOUSE OF REPRESENTATIVES\nOctober 6, 2025 Mr. Thompson of Pennsylvania (for himself, Ms. Craig , and Mr. Bishop ) submitted the following resolution; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nRESOLUTION\nExpressing support for the designation of October 5 through October 11, 2025, as National 4\u2013H Week .\nThat the House of Representatives\u2014\n**(1)**\nsupports the designation of National 4\u2013H Week ;\n**(2)**\nrecognizes the important role of 4\u2013H as the youth development program of the Nation\u2019s Cooperative Extension System and the Department of Agriculture;\n**(3)**\nencourages all citizens to recognize 4\u2013H for the significant impact the organization and members have made and continue to make by empowering youth with the skills needed to lead for a lifetime; and\n**(4)**\ncelebrates the work of 4\u2013H in developing engaged, healthy, and productive citizens who are Beyond Ready for work and life in a world of change.",
      "versionDate": "2025-10-06",
      "versionType": "IH"
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
        "updateDate": "2025-12-15T18:25:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-06",
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
          "measure-id": "id119hres791",
          "measure-number": "791",
          "measure-type": "hres",
          "orig-publish-date": "2025-10-06",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres791v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-10-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution supports the designation of National 4\u2013H Week and recognizes the important role of 4\u2013H as the youth development\u00a0program of the Cooperative Extension System and the Department of Agriculture.</p>"
        },
        "title": "Expressing support for the designation of October 5 through October 11, 2025, as \"National 4-H Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres791.xml",
    "summary": {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National 4\u2013H Week and recognizes the important role of 4\u2013H as the youth development\u00a0program of the Cooperative Extension System and the Department of Agriculture.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres791"
    },
    "title": "Expressing support for the designation of October 5 through October 11, 2025, as \"National 4-H Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution supports the designation of National 4\u2013H Week and recognizes the important role of 4\u2013H as the youth development\u00a0program of the Cooperative Extension System and the Department of Agriculture.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hres791"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres791ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of October 5 through October 11, 2025, as \"National 4-H Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T08:18:22Z"
    },
    {
      "title": "Expressing support for the designation of October 5 through October 11, 2025, as \"National 4-H Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T08:05:22Z"
    }
  ]
}
```
