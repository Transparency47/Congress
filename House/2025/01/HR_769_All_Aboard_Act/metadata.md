# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/769?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/769
- Title: All Aboard Act
- Congress: 119
- Bill type: HR
- Bill number: 769
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-07-01T14:18:05Z
- Update date including text: 2025-07-01T14:18:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-29 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-01-29 - Committee: Referred to the Subcommittee on Railroads, Pipelines, and Hazardous Materials.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/769",
    "number": "769",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000583",
        "district": "5",
        "firstName": "Josh",
        "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
        "lastName": "Gottheimer",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "All Aboard Act",
    "type": "HR",
    "updateDate": "2025-07-01T14:18:05Z",
    "updateDateIncludingText": "2025-07-01T14:18:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:05:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-01-29T15:43:26Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "NJ"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr769ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 769\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Gottheimer (for himself and Mr. Kean ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 49, United States Code, to direct the Secretary of Transportation to issue regulations under which Amtrak is responsible for refunding rail passengers the cost of certain rail transportation that was canceled or delayed due to a failure of Amtrak, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the All Aboard Act .\n#### 2. Accountability of Amtrak for unfulfilled fares caused by maintenance and other failures\n##### (a) In general\nChapter 243 of title 49, United States Code, is amended by adding at the end the following new section:\n24324. Right of rail passengers to recover certain unfulfilled fare (a) In general Not later than 180 days after the date of enactment of the All Aboard Act, the Secretary of Transportation shall issue regulations to ensure that any person who purchases covered rail passenger transportation receives a refund equal to the rate the person paid for such transportation, at the expense of Amtrak and in accordance with this section, if due to a failure of Amtrak, such transportation, or a part of such transportation, is\u2014 (1) canceled; or (2) delayed such that the transportation is completed more than 3 hours after the expected completion time as of the time of the purchase. (b) Determination of cause (1) Causation For purposes of subsection (a), a cancellation or delay is not a failure of Amtrak if the cancellation or delay is attributable to forces or persons uncontrollable by Amtrak. (2) Dispute procedures In carrying out subsection (a), the Secretary shall issue regulations that include\u2014 (A) procedures for determining if a cancellation or delay is subject to subsection (a); and (B) procedures by which Amtrak can dispute that a cancellation or delay is subject to subsection (a), including that the cancellation or delay was due to a failure of Amtrak. (c) Refund issuance (1) Timing A provider of covered rail passenger transportation shall issue a refund with respect to a cancellation or delay described in subsection (a)\u2014 (A) if Amtrak does not dispute that the cancellation or delay is due to a failure of Amtrak\u2014 (i) if the covered rail passenger transportation is purchased with credit, a voucher, or rewards points issued by the provider of such transportation, not later than 7 days after the cancellation or delay; or (ii) if the covered rail passenger transportation is purchased with cash, as soon as is feasible after the cancellation or delay; or (B) if Amtrak disputes, pursuant to the procedures established under subsection (b)(2), that the cancellation or delay is subject to subsection (a), not later than a date\u2014 (i) which is after the date on which a final determination is issued that the cancellation or delay is subject to subsection (a); and (ii) determined by the Secretary to be prompt and feasible. (2) Form A refund under subsection (a) shall be issued to a purchaser of covered rail passenger transportation in the form of payment used by the purchaser. (d) Amtrak reimbursement of other rail carriers Amtrak shall, upon request from a rail carrier that issues a refund under subsection (a), reimburse the rail carrier in the amount equal to the refund. (e) Noncompliance Amtrak may not receive Federal funds for any period during which the Secretary determines that Amtrak is noncompliant with this section. (f) Applicability This section shall apply for any fiscal year in which Amtrak accepts Federal funds. (g) Covered rail passenger transportation defined In this section, the term covered rail passenger transportation means\u2014 (1) rail passenger transportation provided by, or on behalf, of Amtrak; or (2) commuter rail passenger transportation that travels over rails owned by Amtrak, regardless of if such transportation is provided by Amtrak or another rail carrier. .\n##### (b) Replacement of Amtrak asset maintenance strategy\n**(1) Report**\nNot later than 6 months after the date of enactment of this Act, Amtrak shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report including\u2014\n**(A)**\nan identification of each asset maintenance strategy that Amtrak could adopt as a replacement for a run-to-fail maintenance model; and\n**(B)**\nthe estimated cost of implementing each asset maintenance strategy identified pursuant to subparagraph (A).\n**(2) Ban on run-to-fail model**\nAmtrak may not use a run-to-fail maintenance model after the date that is 2 years after the date of enactment of this Act.\n**(3) Implementation of new asset maintenance strategy**\nNot later than 2 years after the date of enactment of this Act, Amtrak shall implement an asset maintenance strategy identified in the report under paragraph (1).\n##### (c) Run-to-Fail maintenance model defined\nIn this section, the term run-to-fail maintenance model means an asset maintenance strategy under which an asset (including equipment and infrastructure used for passenger rail transportation) is retired from use only at such time as\u2014\n**(1)**\nthe asset is no longer capable of fulfilling an intended use; or\n**(2)**\nthe age of the asset exceeds the manufacturer-estimated lifespan of the asset.\n##### (d) Clerical amendment\nThe table of sections for chapter 243 of title 49, United States Code, is amended by adding at the end the following:\n24324. Right of rail passengers to recover certain unfulfilled fare. .",
      "versionDate": "2025-01-28",
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
        "updateDate": "2025-03-01T17:02:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr769",
          "measure-number": "769",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr769v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>All Aboard Act</strong></p><p>This bill requires Amtrak to issue refunds to rail passengers for the purchase price of rail\u00a0passenger transportation that is cancelled or delayed due to a failure of Amtrak.</p><p>Specifically, the Department of Transportation (DOT) must issue regulations requiring Amtrak to issue full refunds to passengers\u00a0for the purchase price of the covered rail passenger transportation if there is a cancellation or a delay of more than three hours in the journey completion time that is due to a failure of Amtrak.</p><p>Under the bill,\u00a0<em>covered rail passenger\u00a0transportation\u00a0</em>means (1) rail passenger transportation provided by, or on behalf of, Amtrak; or (2) commuter rail passenger transportation\u00a0that travels over Amtrak-owned rails, regardless of whether it is\u00a0provided by Amtrak or other rail carriers.</p><p>The regulations must include procedures for (1) determining if a cancellation or delay is due to a failure of Amtrak, and (2) Amtrak to dispute that a cancellation or delay is subject to the refund requirements.</p><p>The bill\u00a0prohibits Amtrak from receiving federal funds for any period during which DOT determines that Amtrak is\u00a0noncompliant with these requirements.</p><p>Amtrak must submit a report to Congress on alternative asset maintenance strategies to replace\u00a0the <em>run-to-fail maintenance model</em> (i.e., using passenger rail equipment and infrastructure until it no longer works or exceeds its estimated lifespan), including the cost of the strategies. Within two years of this bill's enactment,\u00a0Amtrak must (1) stop using a run-to-fail maintenance model, and (2) implement a new asset maintenance strategy.\u00a0</p>"
        },
        "title": "All Aboard Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr769.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>All Aboard Act</strong></p><p>This bill requires Amtrak to issue refunds to rail passengers for the purchase price of rail\u00a0passenger transportation that is cancelled or delayed due to a failure of Amtrak.</p><p>Specifically, the Department of Transportation (DOT) must issue regulations requiring Amtrak to issue full refunds to passengers\u00a0for the purchase price of the covered rail passenger transportation if there is a cancellation or a delay of more than three hours in the journey completion time that is due to a failure of Amtrak.</p><p>Under the bill,\u00a0<em>covered rail passenger\u00a0transportation\u00a0</em>means (1) rail passenger transportation provided by, or on behalf of, Amtrak; or (2) commuter rail passenger transportation\u00a0that travels over Amtrak-owned rails, regardless of whether it is\u00a0provided by Amtrak or other rail carriers.</p><p>The regulations must include procedures for (1) determining if a cancellation or delay is due to a failure of Amtrak, and (2) Amtrak to dispute that a cancellation or delay is subject to the refund requirements.</p><p>The bill\u00a0prohibits Amtrak from receiving federal funds for any period during which DOT determines that Amtrak is\u00a0noncompliant with these requirements.</p><p>Amtrak must submit a report to Congress on alternative asset maintenance strategies to replace\u00a0the <em>run-to-fail maintenance model</em> (i.e., using passenger rail equipment and infrastructure until it no longer works or exceeds its estimated lifespan), including the cost of the strategies. Within two years of this bill's enactment,\u00a0Amtrak must (1) stop using a run-to-fail maintenance model, and (2) implement a new asset maintenance strategy.\u00a0</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr769"
    },
    "title": "All Aboard Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>All Aboard Act</strong></p><p>This bill requires Amtrak to issue refunds to rail passengers for the purchase price of rail\u00a0passenger transportation that is cancelled or delayed due to a failure of Amtrak.</p><p>Specifically, the Department of Transportation (DOT) must issue regulations requiring Amtrak to issue full refunds to passengers\u00a0for the purchase price of the covered rail passenger transportation if there is a cancellation or a delay of more than three hours in the journey completion time that is due to a failure of Amtrak.</p><p>Under the bill,\u00a0<em>covered rail passenger\u00a0transportation\u00a0</em>means (1) rail passenger transportation provided by, or on behalf of, Amtrak; or (2) commuter rail passenger transportation\u00a0that travels over Amtrak-owned rails, regardless of whether it is\u00a0provided by Amtrak or other rail carriers.</p><p>The regulations must include procedures for (1) determining if a cancellation or delay is due to a failure of Amtrak, and (2) Amtrak to dispute that a cancellation or delay is subject to the refund requirements.</p><p>The bill\u00a0prohibits Amtrak from receiving federal funds for any period during which DOT determines that Amtrak is\u00a0noncompliant with these requirements.</p><p>Amtrak must submit a report to Congress on alternative asset maintenance strategies to replace\u00a0the <em>run-to-fail maintenance model</em> (i.e., using passenger rail equipment and infrastructure until it no longer works or exceeds its estimated lifespan), including the cost of the strategies. Within two years of this bill's enactment,\u00a0Amtrak must (1) stop using a run-to-fail maintenance model, and (2) implement a new asset maintenance strategy.\u00a0</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr769"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr769ih.xml"
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
      "title": "All Aboard Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "All Aboard Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to direct the Secretary of Transportation to issue regulations under which Amtrak is responsible for refunding rail passengers the cost of certain rail transportation that was canceled or delayed due to a failure of Amtrak, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:19Z"
    }
  ]
}
```
