# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/149?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/149
- Title: Lead by Example Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 149
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-03-07T16:08:22Z
- Update date including text: 2025-03-07T16:08:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-01-03 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-06 - Committee: Referred to the Subcommittee on Health.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/149",
    "number": "149",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Lead by Example Act of 2025",
    "type": "HR",
    "updateDate": "2025-03-07T16:08:22Z",
    "updateDateIncludingText": "2025-03-07T16:08:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-01-03",
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
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
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
          "date": "2025-01-03T16:15:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-06T17:43:49Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-01-03T16:15:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr149ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 149\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on House Administration , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo ensure that Members of Congress and Congressional staff receive health care from the Department of Veterans Affairs instead of under the Federal Health Benefits Program or health care exchanges.\n#### 1. Short title\nThis Act may be cited as the Lead by Example Act of 2025 .\n#### 2. Health care furnished by Department of Veterans Affairs to Members of Congress and Congressional staff\n##### (a) Health care benefits\nNotwithstanding any other provision of law, beginning January 3, 2027, the only health care plan that the Federal Government may make available to Members of Congress and Congressional staff with respect to their service as a Member of Congress or Congressional staff shall be health care provided through the Department of Veterans Affairs, including at facilities of the Department and non-Department facilities pursuant to chapter 17 of title 38, United States Code, and any other provision of law authorizing the Secretary of Veterans Affairs to furnish such care to veterans, as if such Members and staff were veterans.\n##### (b) Implementation plan\nNot later than September 15, 2025, the Secretary of Veterans Affairs and the Director of the Office of Personnel Management shall jointly submit to Congress a plan to carry out subsection (a), including recommendations for any legislative actions the Secretary and the Director determine necessary to carry out such subsection.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term Congressional staff means the employees described in section 2107(1) of title 5, United States Code.\n**(2)**\nThe term Member of Congress means a Member of the Senate or the House of Representatives, a Delegate to the House of Representatives, and the Resident Commissioner from Puerto Rico.\n**(3)**\nThe term non-Department facility has the meaning given that term in section 1701 of title 38, United States Code.",
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
            "name": "Congressional officers and employees",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Health facilities and institutions",
            "updateDate": "2025-03-05T15:30:45Z"
          },
          {
            "name": "Members of Congress",
            "updateDate": "2025-03-05T15:30:45Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-02-26T20:04:15Z"
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
          "measure-id": "id119hr149",
          "measure-number": "149",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr149v00",
            "update-date": "2025-03-07"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Lead by Example Act of </strong><strong>2025</strong></p><p>This bill provides that, beginning January 3, 2027, the only health care plan the federal government may make available to Members of Congress and congressional staff shall be health care provided through the Department of Veterans Affairs (VA).</p><p>By September 15, 2025, the VA and the Office of Personnel Management shall jointly submit to Congress a plan to carry out this bill, including recommendations for any necessary legislative actions.</p>"
        },
        "title": "Lead by Example Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr149.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lead by Example Act of </strong><strong>2025</strong></p><p>This bill provides that, beginning January 3, 2027, the only health care plan the federal government may make available to Members of Congress and congressional staff shall be health care provided through the Department of Veterans Affairs (VA).</p><p>By September 15, 2025, the VA and the Office of Personnel Management shall jointly submit to Congress a plan to carry out this bill, including recommendations for any necessary legislative actions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr149"
    },
    "title": "Lead by Example Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Lead by Example Act of </strong><strong>2025</strong></p><p>This bill provides that, beginning January 3, 2027, the only health care plan the federal government may make available to Members of Congress and congressional staff shall be health care provided through the Department of Veterans Affairs (VA).</p><p>By September 15, 2025, the VA and the Office of Personnel Management shall jointly submit to Congress a plan to carry out this bill, including recommendations for any necessary legislative actions.</p>",
      "updateDate": "2025-03-07",
      "versionCode": "id119hr149"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr149ih.xml"
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
      "title": "Lead by Example Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T11:08:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Lead by Example Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T11:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure that Members of Congress and Congressional staff receive health care from the Department of Veterans Affairs instead of under the Federal Health Benefits Program or health care exchanges.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T11:03:25Z"
    }
  ]
}
```
