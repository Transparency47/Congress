# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/182?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/182
- Title: Default Prevention Act
- Congress: 119
- Bill type: HR
- Bill number: 182
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-05-20T18:08:37Z
- Update date including text: 2026-05-20T18:08:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/182",
    "number": "182",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001177",
        "district": "5",
        "firstName": "Tom",
        "fullName": "Rep. McClintock, Tom [R-CA-5]",
        "lastName": "McClintock",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Default Prevention Act",
    "type": "HR",
    "updateDate": "2026-05-20T18:08:37Z",
    "updateDateIncludingText": "2026-05-20T18:08:37Z"
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
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
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
          "date": "2025-01-03T16:23:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr182ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 182\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. McClintock introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo ensure the payment of interest and principal of the debt of the United States.\n#### 1. Short title\nThis Act may be cited as the Default Prevention Act .\n#### 2. Payment of obligations\n##### (a) In general\nAt any time that the debt of the United States Government subject to limitation under section 3101 of title 31, United States Code, has reached the limitation imposed under such section, the Secretary of the Treasury (hereafter in this section referred to as the Secretary ) shall\u2014\n**(1)**\npay Tier I obligations as such obligations become due,\n**(2)**\nissue such obligations under chapter 31 of title 31, United States Code, as\u2014\n**(A)**\nare necessary to make the payments described in paragraph (1), or\n**(B)**\nare to be held exclusively by a trust fund referred to in subsection (b)(1)(A),\n**(3)**\npay Tier III obligations only to the extent that the Secretary can still pay all Tier II obligations as such obligations become due,\n**(4)**\npay Tier IV obligations only to the extent that the Secretary can still pay all Tier II and Tier III obligations as such obligations become due,\n**(5)**\npay Tier V obligations only to the extent that the Secretary can still pay all Tier II, Tier III, and Tier IV obligations as such obligations become due, and\n**(6)**\nsubmit to the Committee on Ways and Means of the House of Representatives and the Committee on Finance of the Senate a weekly written report containing the information described in subsection (d).\n##### (b) Definitions\nFor purposes of this section\u2014\n**(1) Tier I obligations**\nThe term Tier I obligations means payments necessary to provide any of the following:\n**(A)**\nPayment with legal tender pursuant to the authority provided under section 3123 of title 31, United States Code, of principal and interest on debt held by\u2014\n**(i)**\nthe public,\n**(ii)**\nthe Federal Old-Age and Survivors Insurance Trust Fund or the Federal Disability Insurance Trust Fund, or\n**(iii)**\nthe Federal Hospital Insurance Trust Fund or the Federal Supplementary Medical Insurance Trust Fund.\n**(B)**\nPayments under the Medicare program under title XVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ).\n**(2) Tier II obligations**\nThe term Tier II obligations means payments necessary to provide any of the following:\n**(A)**\nAny obligation of the Department of Defense.\n**(B)**\nBenefits under laws administered by the Secretary of Veterans Affairs.\n**(3) Tier III obligations**\nThe term Tier III obligations means any obligation of the United States which is not a Tier I, Tier II, Tier IV, or Tier V obligation.\n**(4) Tier IV obligations**\nThe term Tier IV obligations means any payment which constitutes any of the following:\n**(A)**\nCompensation for any Federal employee for official time under section 7131 of such title 5, United States Code.\n**(B)**\nAny payment for travel expenses for any officer or employee of the Executive branch of Government, including the President and Vice President, unless such payment is a Tier I or Tier II obligation.\n**(C)**\nCompensation of any officer or employee of the Executive branch of Government (other than an individual in the competitive service, as defined in section 2102 of title 5, United States Code), including the President and Vice President, unless such compensation is a Tier I or Tier II obligation.\n**(5) Tier V obligations**\nThe term Tier V obligations means compensation of any Member of Congress (as that term is defined in section 2106 of title 5, United States Code).\n##### (c) Coordination with public debt limit\nObligations issued under subsection (a)(2) shall not be taken into account as subject to the limitation imposed under section 3101(b) of title 31, United States Code. The preceding sentence shall not apply with respect to any obligation after the first date (after the issuance of such obligation) on which any modification or suspension of such limitation takes effect.\n##### (d) Weekly reports\nThe written report referred to in subsection (a)(6) shall include, with respect to the period covered by such report\u2014\n**(1)**\nthe amount of Tier I obligations paid under subsection (a)(1) during such period,\n**(2)**\nthe amount of obligations issued under subsection (a)(2) during such period, and\n**(3)**\nthe amount of Tier II obligations, Tier III obligations, Tier IV obligations, and Tier V obligations which were paid during such period (stated separately for each tier) and the aggregate amount of such obligations which were due and unpaid as of the close of such period (stated separately for each tier).\n##### (e) No inference with respect to existing authority to prioritize payments\nDuring any period with respect to which this section does not apply, nothing in this section shall be interpreted to restrict the authority of the Secretary to prioritize the payment of certain obligations over other obligations.",
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
            "name": "Budget deficits and national debt",
            "updateDate": "2025-03-05T15:37:14Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-05T15:37:14Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-03-05T15:37:14Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2025-03-05T15:37:14Z"
          },
          {
            "name": "Social security and elderly assistance",
            "updateDate": "2025-03-05T15:37:14Z"
          }
        ]
      },
      "policyArea": {
        "name": "Economics and Public Finance",
        "updateDate": "2025-02-27T13:31:56Z"
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
          "measure-id": "id119hr182",
          "measure-number": "182",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2026-05-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr182v00",
            "update-date": "2026-05-20"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Default Prevention Act</strong></p><p>This bill exempts certain obligations of the federal government from the statutory debt limit and establishes requirements for paying and prioritizing\u00a0obligations after the debt limit is reached.</p><p>If the debt limit is reached, the bill requires the Department of the Treasury to continue issuing debt and making payments necessary to (1) pay the principal and interest on debt held by the public, the Social Security trust funds, and the Medicare trust funds; and (2) pay Medicare benefits. The bill also exempts these obligations from the debt limit until the debt limit has been modified or suspended.\u00a0</p><p>The bill also establishes requirements for prioritizing the remaining obligations after the debt limit has been reached. Specifically,\u00a0Treasury may not</p><ul><li>pay any remaining obligations unless it can still pay\u00a0obligations of the Department of Defense and any obligations necessary to provide benefits under laws administered by the Department of Veterans Affairs;</li><li>pay obligations related to the compensation of federal employees for official time; government travel for executive branch officers or employees; and the compensation of the President, the Vice President, and other members of the executive branch (other than individuals in the competitive service) unless all other obligations except for compensation of Members of Congress can still be paid; and</li><li>compensate Members of Congress unless all other obligations can still be paid.</li></ul><p>Finally, the bill requires Treasury to provide weekly reports to Congress regarding new debt issued and obligations that have been paid or not paid under the bill.</p>"
        },
        "title": "Default Prevention Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr182.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Default Prevention Act</strong></p><p>This bill exempts certain obligations of the federal government from the statutory debt limit and establishes requirements for paying and prioritizing\u00a0obligations after the debt limit is reached.</p><p>If the debt limit is reached, the bill requires the Department of the Treasury to continue issuing debt and making payments necessary to (1) pay the principal and interest on debt held by the public, the Social Security trust funds, and the Medicare trust funds; and (2) pay Medicare benefits. The bill also exempts these obligations from the debt limit until the debt limit has been modified or suspended.\u00a0</p><p>The bill also establishes requirements for prioritizing the remaining obligations after the debt limit has been reached. Specifically,\u00a0Treasury may not</p><ul><li>pay any remaining obligations unless it can still pay\u00a0obligations of the Department of Defense and any obligations necessary to provide benefits under laws administered by the Department of Veterans Affairs;</li><li>pay obligations related to the compensation of federal employees for official time; government travel for executive branch officers or employees; and the compensation of the President, the Vice President, and other members of the executive branch (other than individuals in the competitive service) unless all other obligations except for compensation of Members of Congress can still be paid; and</li><li>compensate Members of Congress unless all other obligations can still be paid.</li></ul><p>Finally, the bill requires Treasury to provide weekly reports to Congress regarding new debt issued and obligations that have been paid or not paid under the bill.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119hr182"
    },
    "title": "Default Prevention Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Default Prevention Act</strong></p><p>This bill exempts certain obligations of the federal government from the statutory debt limit and establishes requirements for paying and prioritizing\u00a0obligations after the debt limit is reached.</p><p>If the debt limit is reached, the bill requires the Department of the Treasury to continue issuing debt and making payments necessary to (1) pay the principal and interest on debt held by the public, the Social Security trust funds, and the Medicare trust funds; and (2) pay Medicare benefits. The bill also exempts these obligations from the debt limit until the debt limit has been modified or suspended.\u00a0</p><p>The bill also establishes requirements for prioritizing the remaining obligations after the debt limit has been reached. Specifically,\u00a0Treasury may not</p><ul><li>pay any remaining obligations unless it can still pay\u00a0obligations of the Department of Defense and any obligations necessary to provide benefits under laws administered by the Department of Veterans Affairs;</li><li>pay obligations related to the compensation of federal employees for official time; government travel for executive branch officers or employees; and the compensation of the President, the Vice President, and other members of the executive branch (other than individuals in the competitive service) unless all other obligations except for compensation of Members of Congress can still be paid; and</li><li>compensate Members of Congress unless all other obligations can still be paid.</li></ul><p>Finally, the bill requires Treasury to provide weekly reports to Congress regarding new debt issued and obligations that have been paid or not paid under the bill.</p>",
      "updateDate": "2026-05-20",
      "versionCode": "id119hr182"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr182ih.xml"
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
      "title": "Default Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T06:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Default Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T06:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the payment of interest and principal of the debt of the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T06:03:37Z"
    }
  ]
}
```
