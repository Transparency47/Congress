# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/656?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/656
- Title: Protecting Military Parental Leave Evaluations Act
- Congress: 119
- Bill type: HR
- Bill number: 656
- Origin chamber: House
- Introduced date: 2025-01-23
- Update date: 2026-02-04T04:26:27Z
- Update date including text: 2026-02-04T04:26:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-23: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-01-23: Introduced in House

## Actions

- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Introduced in House
- 2025-01-23 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-23",
    "latestAction": {
      "actionDate": "2025-01-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/656",
    "number": "656",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "B000740",
        "district": "5",
        "firstName": "Stephanie",
        "fullName": "Rep. Bice, Stephanie I. [R-OK-5]",
        "lastName": "Bice",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Protecting Military Parental Leave Evaluations Act",
    "type": "HR",
    "updateDate": "2026-02-04T04:26:27Z",
    "updateDateIncludingText": "2026-02-04T04:26:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-23",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-23",
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
          "date": "2025-01-23T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-01-23",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr656ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 656\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 23, 2025 Mrs. Bice (for herself and Ms. Houlahan ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo improve parental leave for members of the Armed Forces.\n#### 1. Short title\nThis Act may be cited as the Protecting Military Parental Leave Evaluations Act .\n#### 2. Improved parental leave for members of the Armed Forces\n##### (a) Findings\nCongress finds the following:\n**(1)**\nIn December 2022, Congress expanded the paid parental leave for members of the Armed Forces to 12 weeks during the 12 months after the birth or adoption of a child of the member and in order to care for such child or the placement of a minor child with the member for adoption or long-term foster care ( 10 U.S.C. 701(h)(1)(A) ).\n**(2)**\nThe expansion of parental leave raises concerns that members who take such leave may receive lower evaluations compared to those who do not.\n**(3)**\nThere is currently no provision to exempt members from evaluations due to parental leave, potentially deterring eligible members from taking this leave.\n**(4)**\nEach Secretary of a military department has been given authority to implement the leave policies but have not provided explicit guidance on how to characterize such leave for the purposes of evaluations.\n**(5)**\nAll Armed Forces have non-rated codes or not observed evaluations to exempt members from evaluations during periods where their performance is not observed, but these do not align across the Armed Forces and do not specifically apply to parental leave.\n**(6)**\nMembers who are parents face unique hardships, and the 12 weeks of paid family leave for both mothers and fathers, for birth and adoption, is designed to balance the care needs of their children with the demands of their unit.\n**(7)**\nExcessive paperwork required to extend the use of the 12 weeks of military family leave beyond one year additionally burdens members and decreases flexibility.\n##### (b) Requirements\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall\u2014\n**(1)**\nprescribe regulations\u2014\n**(A)**\nthat exempt a member of the Armed Forces who is taking parental leave, under subparagraph (A) of paragraph (1) of section 701(h) of title 10, United States Code, that exceeds 31 consecutive days, from a performance evaluation; and\n**(B)**\nunder subparagraph (B) of such paragraph, to authorize a member to take leave under such section during the two-year period beginning on the birth, adoption, or placement described in such paragraph without having to request a waiver from the Secretary concerned; and\n**(2)**\nsubmit to the Committees on Armed Forces of the Senate and House of Representatives a report regarding the implementation of this section.",
      "versionDate": "2025-01-23",
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
            "name": "Employee leave",
            "updateDate": "2025-03-17T16:13:06Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-03-17T16:13:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-02-26T16:29:12Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-23",
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
          "measure-id": "id119hr656",
          "measure-number": "656",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-23",
          "originChamber": "HOUSE",
          "update-date": "2025-04-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr656v00",
            "update-date": "2025-04-17"
          },
          "action-date": "2025-01-23",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protecting Military Parental Leave Evaluations Act</strong></p><p>This bill requires the Department of Defense to prescribe regulations regarding parental leave policies for members of the Armed Forces across all branches.</p><p>Specifically, the regulations must (1) exempt a member from a performance evaluation when such member is taking parental leave that exceeds 31 consecutive days; and (2) authorize a member (without a waiver) to take leave during the two-year period after the birth of a child, adoption of a child, or placement of a minor child in the custody of such member.</p>"
        },
        "title": "Protecting Military Parental Leave Evaluations Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr656.xml",
    "summary": {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Military Parental Leave Evaluations Act</strong></p><p>This bill requires the Department of Defense to prescribe regulations regarding parental leave policies for members of the Armed Forces across all branches.</p><p>Specifically, the regulations must (1) exempt a member from a performance evaluation when such member is taking parental leave that exceeds 31 consecutive days; and (2) authorize a member (without a waiver) to take leave during the two-year period after the birth of a child, adoption of a child, or placement of a minor child in the custody of such member.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr656"
    },
    "title": "Protecting Military Parental Leave Evaluations Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-23",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protecting Military Parental Leave Evaluations Act</strong></p><p>This bill requires the Department of Defense to prescribe regulations regarding parental leave policies for members of the Armed Forces across all branches.</p><p>Specifically, the regulations must (1) exempt a member from a performance evaluation when such member is taking parental leave that exceeds 31 consecutive days; and (2) authorize a member (without a waiver) to take leave during the two-year period after the birth of a child, adoption of a child, or placement of a minor child in the custody of such member.</p>",
      "updateDate": "2025-04-17",
      "versionCode": "id119hr656"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr656ih.xml"
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
      "title": "Protecting Military Parental Leave Evaluations Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-22T06:23:56Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Military Parental Leave Evaluations Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-22T06:23:33Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve parental leave for members of the Armed Forces.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-22T06:19:07Z"
    }
  ]
}
```
