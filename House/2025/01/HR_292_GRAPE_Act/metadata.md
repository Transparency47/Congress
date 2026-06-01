# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/292
- Title: GRAPE Act
- Congress: 119
- Bill type: HR
- Bill number: 292
- Origin chamber: House
- Introduced date: 2025-01-09
- Update date: 2025-05-27T14:12:56Z
- Update date including text: 2025-05-27T14:12:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-09: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.
- Latest action: 2025-01-09: Introduced in House

## Actions

- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Introduced in House
- 2025-01-09 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-14 - Committee: Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-09",
    "latestAction": {
      "actionDate": "2025-01-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/292",
    "number": "292",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "L000600",
        "district": "23",
        "firstName": "Nicholas",
        "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
        "lastName": "Langworthy",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "GRAPE Act",
    "type": "HR",
    "updateDate": "2025-05-27T14:12:56Z",
    "updateDateIncludingText": "2025-05-27T14:12:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-14",
      "committees": {
        "item": {
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on General Farm Commodities, Risk Management, and Credit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-09",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-09",
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
          "date": "2025-01-09T14:31:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-14T18:01:52Z",
              "name": "Referred to"
            }
          },
          "name": "General Farm Commodities, Risk Management, and Credit Subcommittee",
          "systemCode": "hsag16"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr292ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 292\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 9, 2025 Mr. Langworthy introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Federal Crop Insurance Act to require the Federal Crop Insurance Corporation to carry out research and development regarding a policy to insure table, wine, and juice grapes against losses due to a freeze event, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Grape Research And Protection Expansion Act or the GRAPE Act .\n#### 2. Policy to insure table, wine, and juice grapes against losses due to a freeze event\nSection 522(c) of the Federal Crop Insurance Act ( 7 U.S.C. 1522(c) ) is amended by adding at the end the following:\n(20) Table, wine, and juice grapes (A) In general Not later than 1 year after the date of the enactment of this paragraph, the Corporation shall carry out research and development, or offer to enter into 1 or more contracts with 1 or more qualified persons to carry out research and development, regarding a policy to insure table, wine, and juice grapes against losses due to a freeze event. (B) Availability of policy Notwithstanding the last sentence of section 508(a)(1), and section 508(a)(2), not later than 18 months after the date of the enactment of this paragraph, the Corporation shall make available a policy described in subparagraph (A) if the requirements of section 508(h) are met. (C) Report Not later than 2 years after the date of enactment of this paragraph, the Corporation shall submit to the Committees on Appropriations and Agriculture of the House of Representatives and the Committees on Appropriations and Agriculture, Nutrition, and Forestry of the Senate a report that includes\u2014 (i) the results of the research conducted under subparagraph (A); and (ii) a description of the policies made available under this paragraph. .",
      "versionDate": "2025-01-09",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-19T16:43:10Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-09",
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
          "measure-id": "id119hr292",
          "measure-number": "292",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-09",
          "originChamber": "HOUSE",
          "update-date": "2025-02-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr292v00",
            "update-date": "2025-02-25"
          },
          "action-date": "2025-01-09",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Grape Research And Protection Expansion Act or the GRAPE Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure table, wine, and juice grapes against losses due to a freeze event. (Under current law, the term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified FCIP requirements.</p><p>The FCIP must also submit a report to Congress on the research and any resulting policy.</p>"
        },
        "title": "GRAPE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr292.xml",
    "summary": {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grape Research And Protection Expansion Act or the GRAPE Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure table, wine, and juice grapes against losses due to a freeze event. (Under current law, the term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified FCIP requirements.</p><p>The FCIP must also submit a report to Congress on the research and any resulting policy.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr292"
    },
    "title": "GRAPE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-09",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Grape Research And Protection Expansion Act or the GRAPE Act</strong></p><p>This bill requires the federal crop insurance program (FCIP) to provide for the research and development of a policy to insure table, wine, and juice grapes against losses due to a freeze event. (Under current law, the term <em>policy</em> means an insurance policy, plan of insurance, provision of a policy or plan of insurance, and related materials.) The Federal Crop Insurance Corporation, the agency that finances FCIP operations, must make any resulting policy available that meets specified FCIP requirements.</p><p>The FCIP must also submit a report to Congress on the research and any resulting policy.</p>",
      "updateDate": "2025-02-25",
      "versionCode": "id119hr292"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr292ih.xml"
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
      "title": "GRAPE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-06T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "GRAPE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Grape Research And Protection Expansion Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-06T02:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Crop Insurance Act to require the Federal Crop Insurance Corporation to carry out research and development regarding a policy to insure table, wine, and juice grapes against losses due to a freeze event, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-06T02:48:26Z"
    }
  ]
}
```
