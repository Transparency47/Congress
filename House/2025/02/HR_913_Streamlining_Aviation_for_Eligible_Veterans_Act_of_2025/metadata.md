# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/913?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/913
- Title: Streamlining Aviation for Eligible Veterans Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 913
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-02-04T04:11:39Z
- Update date including text: 2026-02-04T04:11:39Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-11 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-03-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-03-11 - Committee: Subcommittee Hearings Held
- 2025-04-09 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-04-09 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/913",
    "number": "913",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "O000019",
        "district": "23",
        "firstName": "Jay",
        "fullName": "Rep. Obernolte, Jay [R-CA-23]",
        "lastName": "Obernolte",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Streamlining Aviation for Eligible Veterans Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T04:11:39Z",
    "updateDateIncludingText": "2026-02-04T04:11:39Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-04-09T18:43:29Z",
                "name": "Reported by"
              },
              {
                "date": "2025-04-09T18:42:57Z",
                "name": "Markup by"
              },
              {
                "date": "2025-03-11T17:38:37Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-03-06T22:43:22Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr913ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 913\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Obernolte introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve a rehabilitation program for a certain veterans with service-connected disabilities that include the pursuit of non-degree flight training programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Streamlining Aviation for Eligible Veterans Act of 2025 or the SAFE Veterans Act of 2025 .\n#### 2. Authority of Secretary of Veterans Affair to approve non-degree flight training courses as part of vocational rehabilitation programs for certain veterans with service-connected disabilities\n##### (a) In general\nSection 3104(b) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting (1) before A rehabilitation program ;\n**(2)**\nby striking To the maximum extent practicable and inserting Except as provided under paragraph (2), to the maximum extent practicable ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Notwithstanding section 3680A(b) of this title, the Secretary may approve a rehabilitation program for a veteran under this chapter that includes the pursuit of a course of flight training other than one given by an educational institution of higher learning for credit toward a standard college degree the veteran is seeking. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to a rehabilitation program approved on or after August 1, 2025.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-06",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "1614",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AVIATE Act of 2025",
      "type": "S"
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
            "name": "Aviation and airports",
            "updateDate": "2025-03-21T18:41:45Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-03-21T18:41:55Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-03-21T18:41:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T15:21:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr913",
          "measure-number": "913",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-12-31"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr913v00",
            "update-date": "2025-12-31"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Streamlining Aviation for Eligible Veterans Act of 2025 or the SAFE Veterans Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>"
        },
        "title": "Streamlining Aviation for Eligible Veterans Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr913.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlining Aviation for Eligible Veterans Act of 2025 or the SAFE Veterans Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119hr913"
    },
    "title": "Streamlining Aviation for Eligible Veterans Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Streamlining Aviation for Eligible Veterans Act of 2025 or the SAFE Veterans Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>",
      "updateDate": "2025-12-31",
      "versionCode": "id119hr913"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr913ih.xml"
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
      "title": "Streamlining Aviation for Eligible Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-05T10:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Streamlining Aviation for Eligible Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-05T10:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve a rehabilitation program for a certain veterans with service-connected disabilities that include the pursuit of non-degree flight training programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-05T10:03:51Z"
    }
  ]
}
```
