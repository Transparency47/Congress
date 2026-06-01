# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3571
- Title: Veterans Administration Backlog Accountability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3571
- Origin chamber: House
- Introduced date: 2025-05-21
- Update date: 2025-12-12T09:07:14Z
- Update date including text: 2025-12-12T09:07:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-21: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.
- Latest action: 2025-05-21: Introduced in House

## Actions

- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Introduced in House
- 2025-05-21 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-06 - Committee: Referred to the Subcommittee on Disability Assistance and Memorial Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-21",
    "latestAction": {
      "actionDate": "2025-05-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3571",
    "number": "3571",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "T000474",
        "district": "35",
        "firstName": "Norma",
        "fullName": "Rep. Torres, Norma J. [D-CA-35]",
        "lastName": "Torres",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Veterans Administration Backlog Accountability Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:14Z",
    "updateDateIncludingText": "2025-12-12T09:07:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Disability Assistance and Memorial Affairs.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-21",
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
      "actionDate": "2025-05-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-21",
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
          "date": "2025-05-21T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-06-06T15:43:38Z",
              "name": "Referred to"
            }
          },
          "name": "Disability Assistance and Memorial Affairs Subcommittee",
          "systemCode": "hsvr09"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3571ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3571\nIN THE HOUSE OF REPRESENTATIVES\nMay 21, 2025 Mrs. Torres of California introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Inspector General of the Department of Veterans Affairs to submit to Congress a report on the backlog of disability compensation claims submitted to the Secretary of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Veterans Administration Backlog Accountability Act of 2025 .\n#### 2. Inspector General report on backlog of disability compensation claims submitted to Department of Veterans Affairs\n##### (a) Report\nNot later than 180 days after the date of the enactment of this Act, the Inspector General of the Department of Veterans Affairs shall submit to Congress a report on the backlog of disability compensation claims submitted to the Secretary of Veterans Affairs pursuant to chapter 11 of title 38, United States Code, pending before the Veterans Benefits Administration or the Board of Veterans\u2019 Appeals.\n##### (b) Matters included\nThe report under subsection (a) shall include the following:\n**(1)**\nA description of the status of the backlog described in such subsection.\n**(2)**\nAn assessment of how the Secretary is addressing such backlog, including how the Secretary is recruiting staff to fill open positions within the Department using authorities or amounts available under the Honoring our PACT Act of 2022 ( Public Law 117\u2013168 ).\n**(3)**\nAn assessment of the effect of any reduction in staffing at the Department since January 20, 2025, affects such backlog.\n**(4)**\nAn assessment of how such backlog affects the average amount of time claimants who have submitted disability compensation claims pursuant to chapter 11 of title 38, United States Code, wait for the Secretary to adjudicate those claims.\n**(5)**\nAn assessment of how the Secretary is preparing to address the predicted 50 percent increase in such claims resulting from the Honoring our PACT Act of 2022 ( Public Law 117\u2013168 ).\n**(6)**\nAn overview of how new technologies, such as automated decision support technology, have contributed to the reduction of such backlog.\n**(7)**\nRecommendations by the Inspector General to further reduce such backlog.",
      "versionDate": "2025-05-21",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-05T18:36:37Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-21",
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
          "measure-id": "id119hr3571",
          "measure-number": "3571",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-21",
          "originChamber": "HOUSE",
          "update-date": "2025-06-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3571v00",
            "update-date": "2025-06-13"
          },
          "action-date": "2025-05-21",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Veterans Administration Backlog Accountability Act of 2025</strong></p><p>This bill requires the Office of Inspector General of the Department of Veterans Affairs (VA) to report on the backlog of VA disability compensation claims that are pending before the Veterans Benefits Administration or the Board of Veterans' Appeals.</p>"
        },
        "title": "Veterans Administration Backlog Accountability Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3571.xml",
    "summary": {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Administration Backlog Accountability Act of 2025</strong></p><p>This bill requires the Office of Inspector General of the Department of Veterans Affairs (VA) to report on the backlog of VA disability compensation claims that are pending before the Veterans Benefits Administration or the Board of Veterans' Appeals.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3571"
    },
    "title": "Veterans Administration Backlog Accountability Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-21",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Veterans Administration Backlog Accountability Act of 2025</strong></p><p>This bill requires the Office of Inspector General of the Department of Veterans Affairs (VA) to report on the backlog of VA disability compensation claims that are pending before the Veterans Benefits Administration or the Board of Veterans' Appeals.</p>",
      "updateDate": "2025-06-13",
      "versionCode": "id119hr3571"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3571ih.xml"
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
      "title": "Veterans Administration Backlog Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans Administration Backlog Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Inspector General of the Department of Veterans Affairs to submit to Congress a report on the backlog of disability compensation claims submitted to the Secretary of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:21Z"
    }
  ]
}
```
