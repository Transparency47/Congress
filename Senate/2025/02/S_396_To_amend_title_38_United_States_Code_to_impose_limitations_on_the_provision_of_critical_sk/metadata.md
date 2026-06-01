# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/396
- Title: Stop GREED Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 396
- Origin chamber: Senate
- Introduced date: 2025-02-04
- Update date: 2025-04-29T17:22:01Z
- Update date including text: 2025-04-29T17:22:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in Senate
- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- Latest action: 2025-02-04: Introduced in Senate

## Actions

- 2025-02-04 - IntroReferral: Introduced in Senate
- 2025-02-04 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/396",
    "number": "396",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Stop GREED Act of 2025",
    "type": "S",
    "updateDate": "2025-04-29T17:22:01Z",
    "updateDateIncludingText": "2025-04-29T17:22:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T21:25:35Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-05",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s396is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 396\nIN THE SENATE OF THE UNITED STATES\nFebruary 4, 2025 Mr. Moran (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to impose limitations on the provision of critical skill incentives to employees of the Department of Veterans Affairs in Senior Executive Services positions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Government Rewards Enriching Executives in the District Act of 2025 or the Stop GREED Act of 2025 .\n#### 2. Limitations on provision of incentives for critical skills to Senior Executive Service employees of Department of Veterans Affairs\nSection 706(d) of title 38, United States Code, is amended by adding at the end the following:\n(7) (A) Subject to subparagraph (B)(ii), a critical skill incentive may not be provided under paragraph (1) to an employee of the Department employed in a Senior Executive Service position, or a position in another comparable system for senior-level Government employees, as defined by the Secretary, whose position is at the Central Office of the Department, including the Veterans Health Administration, the Veterans Benefits Administration, and the National Cemetery Administration, regardless of the actual location where the employee performs the functions of the position. (B) (i) A critical skill incentive provided under paragraph (1) to an employee of the Department employed in a Senior Executive Service position, or a position in another comparable system for senior-level Government employees, as defined by the Secretary, not described in subparagraph (A) of this paragraph may only be provided\u2014 (I) on an individual basis and may not be provided to a group of such employees; and (II) upon approval of the following officers or those serving in an acting capacity: (aa) The Under Secretary for Benefits, the Under Secretary for Health, or the Under Secretary for Memorial Affairs. (bb) The Assistant Secretary for Human Resources and Administration. (cc) The Director of the Office of Management or the Chief Financial Officer. (dd) The Assistant Secretary for Accountability and Whistleblower Protection. (ee) The General Counsel. (ff) Such other officers as the Secretary determines appropriate. (ii) In the case of an employee of the Department employed in a Senior Executive Service position, or a position in another comparable system for senior-level Government employees, as defined by the Secretary, whose position is primarily at the Central Office of the Department, but who performs some portion of the employee\u2019s job function at other facilities of the Department, as defined by the Secretary, not at Central Office\u2014 (I) the employee shall not be considered described in subparagraph (A) with respect to the portion of the employee\u2019s job function that is based out of non-Central Office facilities of the Department; and (II) any critical skill incentive provided under paragraph (1) to the employee for the portion of the employee\u2019s job function that is based out of facilities of the Department other than the Central Office shall be proportionate to the time spent at those Department facilities. (C) (i) Not later than one year after the date of the enactment of the Stop Government Rewards Enriching Executives in the District Act of 2025 , and not less frequently than once each year thereafter, the Secretary shall submit to the Committee on Veterans' Affairs of the Senate and the Committee on Veterans' Affairs of the House of Representatives an annual report on the employees of the Department employed in a Senior Executive Service position, or a position in another comparable system for senior-level Government employees, as defined by the Secretary, who were provided a critical skill incentive under paragraph (1). (ii) Reports submitted pursuant to clause (i) may be submitted by incorporating their contents into other congressionally mandated reports to the committees described in such clause. (D) In this paragraph, the term Senior Executive Service position has the meaning given such term in section 3132(a) of title 5. .",
      "versionDate": "2025-02-04",
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
        "actionTime": "12:27:43",
        "text": "Held at the desk."
      },
      "number": "423",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "PRO Veterans Act of 2025",
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
            "name": "Congressional oversight",
            "updateDate": "2025-04-11T18:24:48Z"
          },
          {
            "name": "Department of Veterans Affairs",
            "updateDate": "2025-04-11T18:24:33Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-04-11T18:24:19Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T15:58:18Z"
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
          "measure-id": "id119s396",
          "measure-number": "396",
          "measure-type": "s",
          "orig-publish-date": "2025-02-04",
          "originChamber": "SENATE",
          "update-date": "2025-04-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s396v00",
            "update-date": "2025-04-29"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Government Rewards Enriching Executives in the District Act of 2025 or the Stop GREED Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from providing certain senior level employees with a critical skill incentive, which is generally a payment bonus for employees possessing a high-demand skill or skill that is at a shortage. Specifically, the VA may not provide such an incentive to an employee in a Senior Executive Service position or other comparable position at the central office of the VA (e.g., the Veterans Health Administration), regardless of the actual location where the employee performs the functions of the position.</p><p>The bill also provides that an incentive may be provided to senior-level employees on an individual basis and upon approval by specified officers (e.g., the Under Secretary for Health). Additionally, senior-level employees whose positions are primarily at the central office of the VA but perform some portion of the job function\u00a0at other VA facilities are exempt from the prohibition.</p><p>The VA must report to Congress annually regarding senior-level employees who were provided a critical skill incentive.</p>"
        },
        "title": "Stop GREED Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s396.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Government Rewards Enriching Executives in the District Act of 2025 or the Stop GREED Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from providing certain senior level employees with a critical skill incentive, which is generally a payment bonus for employees possessing a high-demand skill or skill that is at a shortage. Specifically, the VA may not provide such an incentive to an employee in a Senior Executive Service position or other comparable position at the central office of the VA (e.g., the Veterans Health Administration), regardless of the actual location where the employee performs the functions of the position.</p><p>The bill also provides that an incentive may be provided to senior-level employees on an individual basis and upon approval by specified officers (e.g., the Under Secretary for Health). Additionally, senior-level employees whose positions are primarily at the central office of the VA but perform some portion of the job function\u00a0at other VA facilities are exempt from the prohibition.</p><p>The VA must report to Congress annually regarding senior-level employees who were provided a critical skill incentive.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s396"
    },
    "title": "Stop GREED Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Government Rewards Enriching Executives in the District Act of 2025 or the Stop GREED Act of 2025</strong></p><p>This bill prohibits the Department of Veterans Affairs (VA) from providing certain senior level employees with a critical skill incentive, which is generally a payment bonus for employees possessing a high-demand skill or skill that is at a shortage. Specifically, the VA may not provide such an incentive to an employee in a Senior Executive Service position or other comparable position at the central office of the VA (e.g., the Veterans Health Administration), regardless of the actual location where the employee performs the functions of the position.</p><p>The bill also provides that an incentive may be provided to senior-level employees on an individual basis and upon approval by specified officers (e.g., the Under Secretary for Health). Additionally, senior-level employees whose positions are primarily at the central office of the VA but perform some portion of the job function\u00a0at other VA facilities are exempt from the prohibition.</p><p>The VA must report to Congress annually regarding senior-level employees who were provided a critical skill incentive.</p>",
      "updateDate": "2025-04-29",
      "versionCode": "id119s396"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s396is.xml"
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
      "title": "Stop GREED Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-07T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop GREED Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Government Rewards Enriching Executives in the District Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T04:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 38, United States Code, to impose limitations on the provision of critical skill incentives to employees of the Department of Veterans Affairs in Senior Executive Services positions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T04:18:24Z"
    }
  ]
}
```
