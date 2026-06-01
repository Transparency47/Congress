# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1614?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1614
- Title: AVIATE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1614
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2026-03-27T01:40:59Z
- Update date including text: 2026-03-27T01:40:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1614",
    "number": "1614",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "AVIATE Act of 2025",
    "type": "S",
    "updateDate": "2026-03-27T01:40:59Z",
    "updateDateIncludingText": "2026-03-27T01:40:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2025-05-06T16:42:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "NC"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1614is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1614\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Mr. Cruz (for himself, Mr. Budd , and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve a rehabilitation program for certain veterans with service-connected disabilities that include the pursuit of non-degree flight training programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Authorizing Vocational and Instructional Aviation Training for Eligible Veterans Act of 2025 or the AVIATE Act of 2025 .\n#### 2. Authority of Secretary of Veterans Affair to approve non-degree flight training courses as part of vocational rehabilitation programs for certain veterans with service-connected disabilities\n##### (a) In general\nSection 3104(b) of title 38, United States Code, is amended\u2014\n**(1)**\nby inserting (1) before A rehabilitation program ;\n**(2)**\nby striking To the maximum extent practicable and inserting Except as provided under paragraph (2), to the maximum extent practicable ; and\n**(3)**\nby adding at the end the following new paragraph:\n(2) Notwithstanding section 3680A(b) of this title, the Secretary may approve a rehabilitation program for a veteran under this chapter that includes the pursuit of a course of flight training other than one given by an educational institution of higher learning for credit toward a standard college degree the veteran is seeking. .\n##### (b) Applicability\nThe amendments made by subsection (a) shall apply with respect to a rehabilitation program approved on or after August 1, 2025.",
      "versionDate": "2025-05-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-04-09",
        "text": "Forwarded by Subcommittee to Full Committee by Voice Vote."
      },
      "number": "913",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Streamlining Aviation for Eligible Veterans Act of 2025",
      "type": "HR"
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
        "updateDate": "2025-06-03T19:24:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-06",
    "originChamber": "Senate",
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
          "measure-id": "id119s1614",
          "measure-number": "1614",
          "measure-type": "s",
          "orig-publish-date": "2025-05-06",
          "originChamber": "SENATE",
          "update-date": "2026-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1614v00",
            "update-date": "2026-03-27"
          },
          "action-date": "2025-05-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Authorizing Vocational and Instructional Aviation Training for Eligible Veterans Act of 2025 or the AVIATE Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>"
        },
        "title": "AVIATE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1614.xml",
    "summary": {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Authorizing Vocational and Instructional Aviation Training for Eligible Veterans Act of 2025 or the AVIATE Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1614"
    },
    "title": "AVIATE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Authorizing Vocational and Instructional Aviation Training for Eligible Veterans Act of 2025 or the AVIATE Act of 2025</strong></p><p>This bill authorizes the Department of Veterans Affairs (VA) to approve nondegree flight training courses for certain veterans with service-connected disabilities as part of the VA\u2019s vocational rehabilitation programs under the Veteran Readiness and Employment (VR&E) program. Generally, the VR&E program provides job training and other employment-related services to veterans with service-connected disabilities, including long-term employment training courses.</p>",
      "updateDate": "2026-03-27",
      "versionCode": "id119s1614"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1614is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "AVIATE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AVIATE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Authorizing Vocational and Instructional Aviation Training for Eligible Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to authorize the Secretary of Veterans Affairs to approve a rehabilitation program for certain veterans with service-connected disabilities that include the pursuit of non-degree flight training programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:22Z"
    }
  ]
}
```
