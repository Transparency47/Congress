# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1972
- Title: START Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1972
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-06-12T20:44:58Z
- Update date including text: 2025-06-12T20:44:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-27 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1972",
    "number": "1972",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001215",
        "district": "1",
        "firstName": "Mariannette",
        "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
        "lastName": "Miller-Meeks",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "START Act of 2025",
    "type": "HR",
    "updateDate": "2025-06-12T20:44:58Z",
    "updateDateIncludingText": "2025-06-12T20:44:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:02:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-27T18:03:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1972ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1972\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mrs. Miller-Meeks introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to establish the period during which the referral of a veteran, made by a health care provider of the Department of Veterans Affairs, to a non-Department provider, for care or services under the Community Care Program of such Department, remains valid.\n#### 1. Short title\nThis Act may be cited as the Standardizing Treatment and Referral Times Act of 2025 or the START Act of 2025 .\n#### 2. Establishment of period during which a referral under the Community Care Program of the Department of Veterans Affairs remains valid\nSection 1703(a)(2) of title 38, United States Code, is amended by adding at the end the following new subparagraph:\n(E) Ensuring that the period during which the referral of a covered veteran, made by a health care provider of the Department of Veterans Affairs, to a non-Department provider, for care or services under this section, is valid, begins on the day that the covered veteran has the first appointment with such non-Department provider. .",
      "versionDate": "2025-03-10",
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
        "updateDate": "2025-03-26T15:15:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr1972",
          "measure-number": "1972",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2025-06-12"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1972v00",
            "update-date": "2025-06-12"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Standardizing Treatment and Referral Times Act of 2025 or the START Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that the period for a veteran\u2019s referral for non-VA care under the Veterans Community Care Program begins on the day that the veteran has the first appointment with the non-VA provider.</p>"
        },
        "title": "START Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1972.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Standardizing Treatment and Referral Times Act of 2025 or the START Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that the period for a veteran\u2019s referral for non-VA care under the Veterans Community Care Program begins on the day that the veteran has the first appointment with the non-VA provider.</p>",
      "updateDate": "2025-06-12",
      "versionCode": "id119hr1972"
    },
    "title": "START Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Standardizing Treatment and Referral Times Act of 2025 or the START Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to ensure that the period for a veteran\u2019s referral for non-VA care under the Veterans Community Care Program begins on the day that the veteran has the first appointment with the non-VA provider.</p>",
      "updateDate": "2025-06-12",
      "versionCode": "id119hr1972"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1972ih.xml"
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
      "title": "START Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-22T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "START Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Standardizing Treatment and Referral Times Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-22T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to establish the period during which the referral of a veteran, made by a health care provider of the Department of Veterans Affairs, to a non-Department provider, for care or services under the Community Care Program of such Department, remains valid.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-22T05:48:36Z"
    }
  ]
}
```
