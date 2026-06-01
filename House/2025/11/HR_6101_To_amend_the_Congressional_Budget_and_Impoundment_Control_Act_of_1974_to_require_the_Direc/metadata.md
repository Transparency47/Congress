# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6101?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6101
- Title: CBO Oversight Act
- Congress: 119
- Bill type: HR
- Bill number: 6101
- Origin chamber: House
- Introduced date: 2025-11-18
- Update date: 2025-12-10T19:03:28Z
- Update date including text: 2025-12-10T19:03:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-18: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on the Budget.
- Latest action: 2025-11-18: Introduced in House

## Actions

- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Introduced in House
- 2025-11-18 - IntroReferral: Referred to the House Committee on the Budget.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6101",
    "number": "6101",
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
    "title": "CBO Oversight Act",
    "type": "HR",
    "updateDate": "2025-12-10T19:03:28Z",
    "updateDateIncludingText": "2025-12-10T19:03:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-18",
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
      "text": "Referred to the House Committee on the Budget.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T15:02:50Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6101ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6101\nIN THE HOUSE OF REPRESENTATIVES\nNovember 18, 2025 Mr. Norman introduced the following bill; which was referred to the Committee on the Budget\nA BILL\nTo amend the Congressional Budget and Impoundment Control Act of 1974 to require the Director of the Congressional Budget Office to provide testimony at annual hearings held by the Committees on the Budget of the House of Representatives and the Senate, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the CBO Oversight Act .\n#### 2. Congressional Budget Office annual hearings requirement\n##### (a) In general\nTitle II of the Congressional Budget and Impoundment Control Act of 1974 ( 2 U.S.C. 601 et seq. ) is amended by inserting after section 203 the following new section:\n204. Congressional Budget Office annual hearings requirement During each calendar year, at the request of the chair of the Committee on the Budget of the House of Representatives or the Senate, the Director shall provide testimony at two hearings at each such Committee by the end of the calendar year. Such hearings may address any issue such Committees deem appropriate, including reviewing the accuracy of the baseline projections and estimates prepared by the Office during the most recently completed fiscal year. .\n##### (b) Clerical amendment\nThe table of contents in section 1(b) of such Act is amended by inserting after the item relating to section 203 the following:\nSec. 204. Congressional Budget Office annual hearings requirement. .",
      "versionDate": "2025-11-18",
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
        "updateDate": "2025-12-09T21:57:05Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-18",
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
          "measure-id": "id119hr6101",
          "measure-number": "6101",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-18",
          "originChamber": "HOUSE",
          "update-date": "2025-12-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6101v00",
            "update-date": "2025-12-10"
          },
          "action-date": "2025-11-18",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>CBO Oversight Act</strong></p><p>This bill requires the Director of the Congressional Budget Office (CBO) to provide testimony annually at hearings held by the House and Senate Budget\u00a0Committees.</p><p>Specifically, at the request of the chair of either committee, the Director must provide testimony at two hearings held by the committee by the end of the calendar year. The hearings may address any issue that the committee deems appropriate, including reviewing the accuracy of the baseline projections and estimates prepared by CBO during the most recently completed fiscal year.</p>"
        },
        "title": "CBO Oversight Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6101.xml",
    "summary": {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBO Oversight Act</strong></p><p>This bill requires the Director of the Congressional Budget Office (CBO) to provide testimony annually at hearings held by the House and Senate Budget\u00a0Committees.</p><p>Specifically, at the request of the chair of either committee, the Director must provide testimony at two hearings held by the committee by the end of the calendar year. The hearings may address any issue that the committee deems appropriate, including reviewing the accuracy of the baseline projections and estimates prepared by CBO during the most recently completed fiscal year.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119hr6101"
    },
    "title": "CBO Oversight Act"
  },
  "summaries": [
    {
      "actionDate": "2025-11-18",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>CBO Oversight Act</strong></p><p>This bill requires the Director of the Congressional Budget Office (CBO) to provide testimony annually at hearings held by the House and Senate Budget\u00a0Committees.</p><p>Specifically, at the request of the chair of either committee, the Director must provide testimony at two hearings held by the committee by the end of the calendar year. The hearings may address any issue that the committee deems appropriate, including reviewing the accuracy of the baseline projections and estimates prepared by CBO during the most recently completed fiscal year.</p>",
      "updateDate": "2025-12-10",
      "versionCode": "id119hr6101"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6101ih.xml"
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
      "title": "CBO Oversight Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "CBO Oversight Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-27T01:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Congressional Budget and Impoundment Control Act of 1974 to require the Director of the Congressional Budget Office to provide testimony at annual hearings held by the Committees on the Budget of the House of Representatives and the Senate, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-27T01:48:20Z"
    }
  ]
}
```
