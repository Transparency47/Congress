# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1388?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1388
- Title: Fair-Value Accounting and Budget Act
- Congress: 119
- Bill type: HR
- Bill number: 1388
- Origin chamber: House
- Introduced date: 2025-02-14
- Update date: 2025-05-07T14:39:06Z
- Update date including text: 2025-05-07T14:39:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-14: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-14 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-14: Introduced in House

## Actions

- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Introduced in House
- 2025-02-14 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-14 - IntroReferral: Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-14",
    "latestAction": {
      "actionDate": "2025-02-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1388",
    "number": "1388",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "N000190",
        "district": "5",
        "firstName": "Ralph",
        "fullName": "Rep. Norman, Ralph [R-SC-5]",
        "lastName": "Norman",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Fair-Value Accounting and Budget Act",
    "type": "HR",
    "updateDate": "2025-05-07T14:39:06Z",
    "updateDateIncludingText": "2025-05-07T14:39:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on the Budget, and in addition to the Committee on Rules, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-14",
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
          "date": "2025-02-14T18:33:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-14T18:33:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
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
      "isOriginalCosponsor": "True",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "WI"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-14",
      "state": "TX"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1388ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1388\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 14, 2025 Mr. Norman (for himself, Mr. Grothman , Mr. Weber of Texas , and Mr. Self ) introduced the following bill; which was referred to the Committee on the Budget , and in addition to the Committee on Rules , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to provide for fair-value credit estimates, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fair-Value Accounting and Budget Act .\n#### 2. Fair-value credit estimates\n##### (a) Fair-Value estimates\nPart A of title IV of the Congressional Budget and Impoundment Control Act of 1974 is amended by adding at the end the following:\n407. Fair-value credit estimates (a) Fair-Value estimates Any estimate prepared by the Director of the Congressional Budget Office for a measure that establishes or modifies any program providing loans or loan guarantees shall provide a fair-value estimate of such loan or loan guarantee program. (b) Baseline estimates The Congressional Budget Office shall include estimates of loan and loan guarantee programs, on a fair-value and credit reform basis, as practicable, in the Office\u2019s publication entitled The Budget and Economic Outlook (or any successor report). (c) Enforcement If the Director of the Congressional Budget Office provides an estimate pursuant to subsection (a), the chair of the Committee on the Budget of the House of Representatives or the Senate shall use such estimate to determine compliance with this Act and other budget enforcement requirements. (d) Annual report In 2026 and each year thereafter, not later than 90 days after the date the President submits to Congress a budget under section 1105(a) of title 31, United States Code, the Director of the Office of Management and Budget shall submit a report, to the Committees on the Budget of the House of Representatives and the Senate, on fair-value estimates of the cost of Federal credit programs. (e) Definition of fair-Value In carrying out this section, the Director of the Congressional Budget Office and the Director of the Office of Management and Budget shall use the definition of fair-value as set forth in the publication of the Government Accounting Standards Board, issued in February 2015, entitled Fair Value Measurement and Application . .\n##### (b) Clerical amendment\nThe table of contents for the Congressional Budget and Impoundment Control Act of 1974 Act set forth in section 1(b) of such Act is amended by inserting after the item relating to section 406 the following new item:\nSec. 407. Fair-value credit estimates. .",
      "versionDate": "2025-02-14",
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
        "name": "Economics and Public Finance",
        "updateDate": "2025-05-06T14:45:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-14",
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
          "measure-id": "id119hr1388",
          "measure-number": "1388",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-14",
          "originChamber": "HOUSE",
          "update-date": "2025-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1388v00",
            "update-date": "2025-05-07"
          },
          "action-date": "2025-02-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fair-Value Accounting and Budget Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide certain fair-value estimates of federal loan and loan guarantee programs. Under the bill, the <em>fair value </em>is the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date. Fair-value estimates generally use private-market interest rates to estimate the cost of a loan program rather than rates based on Treasury securities.</p><p>The bill requires CBO to include fair-value estimates in (1) any estimate prepared for a measure that establishes or modifies a loan or loan guarantee program, and (2) its publication titled<em> The Budget and Economic Outlook. </em>If CBO provides a fair-value estimate pursuant to this bill, the chairs of the congressional budget committees must use the estimate to determine compliance with budget enforcement requirements.\u00a0\u00a0</p><p>The bill also requires the Office of Management and Budget to submit an annual report to Congress on fair-value estimates of the costs of federal credit programs.\u00a0\u00a0</p>"
        },
        "title": "Fair-Value Accounting and Budget Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1388.xml",
    "summary": {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair-Value Accounting and Budget Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide certain fair-value estimates of federal loan and loan guarantee programs. Under the bill, the <em>fair value </em>is the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date. Fair-value estimates generally use private-market interest rates to estimate the cost of a loan program rather than rates based on Treasury securities.</p><p>The bill requires CBO to include fair-value estimates in (1) any estimate prepared for a measure that establishes or modifies a loan or loan guarantee program, and (2) its publication titled<em> The Budget and Economic Outlook. </em>If CBO provides a fair-value estimate pursuant to this bill, the chairs of the congressional budget committees must use the estimate to determine compliance with budget enforcement requirements.\u00a0\u00a0</p><p>The bill also requires the Office of Management and Budget to submit an annual report to Congress on fair-value estimates of the costs of federal credit programs.\u00a0\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1388"
    },
    "title": "Fair-Value Accounting and Budget Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fair-Value Accounting and Budget Act</strong></p><p>This bill requires the Congressional Budget Office (CBO) to provide certain fair-value estimates of federal loan and loan guarantee programs. Under the bill, the <em>fair value </em>is the price that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants at the measurement date. Fair-value estimates generally use private-market interest rates to estimate the cost of a loan program rather than rates based on Treasury securities.</p><p>The bill requires CBO to include fair-value estimates in (1) any estimate prepared for a measure that establishes or modifies a loan or loan guarantee program, and (2) its publication titled<em> The Budget and Economic Outlook. </em>If CBO provides a fair-value estimate pursuant to this bill, the chairs of the congressional budget committees must use the estimate to determine compliance with budget enforcement requirements.\u00a0\u00a0</p><p>The bill also requires the Office of Management and Budget to submit an annual report to Congress on fair-value estimates of the costs of federal credit programs.\u00a0\u00a0</p>",
      "updateDate": "2025-05-07",
      "versionCode": "id119hr1388"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1388ih.xml"
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
      "title": "Fair-Value Accounting and Budget Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T12:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fair-Value Accounting and Budget Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:38:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to provide for fair-value credit estimates, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:33:36Z"
    }
  ]
}
```
