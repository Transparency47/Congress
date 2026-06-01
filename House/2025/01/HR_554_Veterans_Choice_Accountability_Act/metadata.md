# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/554?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/554
- Title: Veteran’s Choice Accountability Act
- Congress: 119
- Bill type: HR
- Bill number: 554
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-10-09T00:11:26Z
- Update date including text: 2025-10-09T00:11:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-02-20 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/554",
    "number": "554",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000804",
        "district": "1",
        "firstName": "Robert",
        "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
        "lastName": "Wittman",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Veteran\u2019s Choice Accountability Act",
    "type": "HR",
    "updateDate": "2025-10-09T00:11:26Z",
    "updateDateIncludingText": "2025-10-09T00:11:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-20T22:38:06Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr554ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 554\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Wittman introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo improve the provision of health care by the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Veteran\u2019s Choice Accountability Act .\n#### 2. Evaluation of fee-basis care provided by Department of Veterans Affairs\nThe Secretary of Veterans Affairs shall evaluate all programs of the Department of Veterans Affairs under which the Secretary furnishes hospital care, medical services, and nursing home care to determine the most intensively used specialized care programs of the Department and to ensure such programs are maintained as centers of excellence.\n#### 3. Evaluation of implementation of VA Budget and Choice Improvement Act\nNot later than two years after the date of the enactment of this Act, the Secretary of Veterans Affairs shall submit to Congress an evaluation of the implementation by the Secretary of the VA Budget and Choice Improvement Act (title IV of Public Law 114\u201341 ).",
      "versionDate": "2025-01-16",
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
            "name": "Congressional oversight",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Health care quality",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Hospital care",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-03-13T16:01:45Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-03-13T16:01:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-19T18:27:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr554",
          "measure-number": "554",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-02-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr554v00",
            "update-date": "2025-02-28"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veteran's Choice Accountability Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to evaluate VA programs that furnish hospital care, medical services, and nursing home care to ensure that the most intensively used specialized care programs are maintained as centers of excellence. The bill also requires the VA to submit an evaluation of the VA's implementation of the VA Budget and Choice Improvement Act.</p>"
        },
        "title": "Veteran\u2019s Choice Accountability Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr554.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran's Choice Accountability Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to evaluate VA programs that furnish hospital care, medical services, and nursing home care to ensure that the most intensively used specialized care programs are maintained as centers of excellence. The bill also requires the VA to submit an evaluation of the VA's implementation of the VA Budget and Choice Improvement Act.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr554"
    },
    "title": "Veteran\u2019s Choice Accountability Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veteran's Choice Accountability Act</strong></p> <p>This bill requires the Department of Veterans Affairs (VA) to evaluate VA programs that furnish hospital care, medical services, and nursing home care to ensure that the most intensively used specialized care programs are maintained as centers of excellence. The bill also requires the VA to submit an evaluation of the VA's implementation of the VA Budget and Choice Improvement Act.</p>",
      "updateDate": "2025-02-28",
      "versionCode": "id119hr554"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr554ih.xml"
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
      "title": "Veteran\u2019s Choice Accountability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veteran\u2019s Choice Accountability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve the provision of health care by the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:19Z"
    }
  ]
}
```
