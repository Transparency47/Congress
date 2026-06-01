# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/213
- Title: To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 213
- Origin chamber: House
- Introduced date: 2025-01-06
- Update date: 2025-02-12T09:00:44Z
- Update date including text: 2025-02-12T09:00:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-06: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-07 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-06: Introduced in House

## Actions

- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Introduced in House
- 2025-01-06 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-07 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-06",
    "latestAction": {
      "actionDate": "2025-01-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/213",
    "number": "213",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-02-12T09:00:44Z",
    "updateDateIncludingText": "2025-02-12T09:00:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-07",
      "committees": {
        "item": {
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-06",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-06",
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
          "date": "2025-01-06T17:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-07T14:34:35Z",
              "name": "Referred to"
            }
          },
          "name": "Railroads, Pipelines, and Hazardous Materials Subcommittee",
          "systemCode": "hspw14"
        }
      },
      "systemCode": "hspw00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr213ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 213\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 6, 2025 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes.\n#### 1. Prohibition on provision of Federal financial assistance for certain high-speed rail development project\nNo Federal financial assistance may be provided to the State of California for a high-speed rail corridor development project that is the same or substantially similar to the project that is the subject of Cooperative Agreement No. FR\u2013HSR\u20130118\u201312\u201301\u201301 entered into between the California High-Speed Rail Authority and the Federal Railroad Administration.",
      "versionDate": "2025-01-06",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-02-04T13:07:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-06",
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
          "measure-id": "id119hr213",
          "measure-number": "213",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-06",
          "originChamber": "HOUSE",
          "update-date": "2025-02-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr213v00",
            "update-date": "2025-02-06"
          },
          "action-date": "2025-01-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill prohibits the state of California from receiving federal funds for a high-speed rail corridor development project.\u00a0Specifically, the prohibition applies to a project\u00a0in California that is the same or substantially similar to the project that is the subject of an FY2010 cooperative agreement entered into on November 18, 2011, between the California High-Speed Rail Authority (CHSRA) and the Federal Railroad Administration (FRA).</p><p>As background,\u00a0CHSRA has received various federal grants for\u00a0the California High-Speed Rail\u00a0program,\u00a0a project led by the state of California with the goal of implementing a high-speed rail\u00a0system capable of speeds exceeding 200 miles per hour between Los Angeles and San Francisco. The FRA terminated the specific FY2010\u00a0cooperative agreement on May 16, 2019.</p>"
        },
        "title": "To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr213.xml",
    "summary": {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the state of California from receiving federal funds for a high-speed rail corridor development project.\u00a0Specifically, the prohibition applies to a project\u00a0in California that is the same or substantially similar to the project that is the subject of an FY2010 cooperative agreement entered into on November 18, 2011, between the California High-Speed Rail Authority (CHSRA) and the Federal Railroad Administration (FRA).</p><p>As background,\u00a0CHSRA has received various federal grants for\u00a0the California High-Speed Rail\u00a0program,\u00a0a project led by the state of California with the goal of implementing a high-speed rail\u00a0system capable of speeds exceeding 200 miles per hour between Los Angeles and San Francisco. The FRA terminated the specific FY2010\u00a0cooperative agreement on May 16, 2019.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr213"
    },
    "title": "To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-06",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill prohibits the state of California from receiving federal funds for a high-speed rail corridor development project.\u00a0Specifically, the prohibition applies to a project\u00a0in California that is the same or substantially similar to the project that is the subject of an FY2010 cooperative agreement entered into on November 18, 2011, between the California High-Speed Rail Authority (CHSRA) and the Federal Railroad Administration (FRA).</p><p>As background,\u00a0CHSRA has received various federal grants for\u00a0the California High-Speed Rail\u00a0program,\u00a0a project led by the state of California with the goal of implementing a high-speed rail\u00a0system capable of speeds exceeding 200 miles per hour between Los Angeles and San Francisco. The FRA terminated the specific FY2010\u00a0cooperative agreement on May 16, 2019.</p>",
      "updateDate": "2025-02-06",
      "versionCode": "id119hr213"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr213ih.xml"
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
      "title": "To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-29T12:19:01Z"
    },
    {
      "title": "To prohibit the use of Federal financial assistance for a certain high-speed rail development project in the State of California, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-07T14:06:25Z"
    }
  ]
}
```
