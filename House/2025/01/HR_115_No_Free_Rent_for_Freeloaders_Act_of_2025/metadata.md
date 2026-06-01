# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/115?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/115
- Title: No Free Rent for Freeloaders Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 115
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-10T00:26:13Z
- Update date including text: 2025-12-10T00:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/115",
    "number": "115",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "No Free Rent for Freeloaders Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-10T00:26:13Z",
    "updateDateIncludingText": "2025-12-10T00:26:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Appropriations, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:10:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:09:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr115ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 115\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Appropriations , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish a penalty for the Department of Housing and Urban Development for failure to enforce compliance with the public housing community service and self-sufficiency requirement under law, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the No Free Rent for Freeloaders Act of 2025 .\n#### 2. Monitoring compliance\n##### (a) In general\nThe Inspector General of the Department of Housing and Urban Development shall, on an annual basis and for each public housing agency (as such term is defined in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ))\u2014\n**(1)**\nmonitor the extent of noncompliance with the requirements under section 12(c) of such Act ( 42 U.S.C. 1437j(c) ); and\n**(2)**\ndetermine the aggregate amount provided in Federal subsidies for all public housing dwelling units that were occupied by tenants who were not in compliance with such requirements.\n##### (b) Publication\nNot later than September 30 of each fiscal year, the Inspector General of the Department of Housing and Urban Development shall cause to be published in the Federal Register a statement of the amount determined for such fiscal year pursuant to subsection (a)(2).\n#### 3. Rescission of amounts from HUD management and administration account\n##### (a) In general\nIn each fiscal year, on October 15 or the date specified in subsection (b), whichever occurs later, there is rescinded, from amounts made available for such fiscal year for the Management and Administration account of the Department of Housing and Urban Development, an amount equal to the amount published pursuant to section 2(b) for the preceding fiscal year.\n##### (b) Late appropriations\nIn the case of any fiscal year for which a general appropriation Act for the Department of Housing and Urban Development that provides funds for the Management and Administration account of such Department has not been enacted before October 15, the date specified in this subsection shall be the date of the enactment of such a general appropriation Act.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employment and training programs",
            "updateDate": "2025-02-06T19:15:14Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-02-06T19:15:21Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-02-06T19:15:27Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-02-06T19:15:36Z"
          },
          {
            "name": "National and community service",
            "updateDate": "2025-02-06T19:15:50Z"
          },
          {
            "name": "Public housing",
            "updateDate": "2025-02-06T19:15:57Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-02-04T12:55:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr115",
          "measure-number": "115",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr115v00",
            "update-date": "2025-02-05"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>No Free Rent for Freeloaders Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD), on an annual basis, to</p><ul><li>monitor the extent of noncompliance of public-housing\u00a0tenants with certain community service and economic self-sufficiency requirements,</li><li>determine the aggregate amount provided in federal subsidies for all public-housing dwelling units that were occupied by noncompliant tenants, and</li><li>publish this amount in the Federal Register.</li></ul><p>In each fiscal year, the amount as determined and published for the preceding fiscal year must be rescinded from funds made available for HUD's\u00a0Management and Administration account.</p>"
        },
        "title": "No Free Rent for Freeloaders Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr115.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Free Rent for Freeloaders Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD), on an annual basis, to</p><ul><li>monitor the extent of noncompliance of public-housing\u00a0tenants with certain community service and economic self-sufficiency requirements,</li><li>determine the aggregate amount provided in federal subsidies for all public-housing dwelling units that were occupied by noncompliant tenants, and</li><li>publish this amount in the Federal Register.</li></ul><p>In each fiscal year, the amount as determined and published for the preceding fiscal year must be rescinded from funds made available for HUD's\u00a0Management and Administration account.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr115"
    },
    "title": "No Free Rent for Freeloaders Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>No Free Rent for Freeloaders Act of 2025</strong></p><p>This bill directs the Department of Housing and Urban Development (HUD), on an annual basis, to</p><ul><li>monitor the extent of noncompliance of public-housing\u00a0tenants with certain community service and economic self-sufficiency requirements,</li><li>determine the aggregate amount provided in federal subsidies for all public-housing dwelling units that were occupied by noncompliant tenants, and</li><li>publish this amount in the Federal Register.</li></ul><p>In each fiscal year, the amount as determined and published for the preceding fiscal year must be rescinded from funds made available for HUD's\u00a0Management and Administration account.</p>",
      "updateDate": "2025-02-05",
      "versionCode": "id119hr115"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr115ih.xml"
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
      "title": "No Free Rent for Freeloaders Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "No Free Rent for Freeloaders Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T05:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish a penalty for the Department of Housing and Urban Development for failure to enforce compliance with the public housing community service and self-sufficiency requirement under law, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T05:18:23Z"
    }
  ]
}
```
