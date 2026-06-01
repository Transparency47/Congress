# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/622?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/622
- Title: To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 622
- Origin chamber: House
- Introduced date: 2025-01-22
- Update date: 2025-03-12T08:07:37Z
- Update date including text: 2025-03-12T08:07:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-22: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-01-22: Introduced in House

## Actions

- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Introduced in House
- 2025-01-22 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-22",
    "latestAction": {
      "actionDate": "2025-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/622",
    "number": "622",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "K000388",
        "district": "1",
        "firstName": "Trent",
        "fullName": "Rep. Kelly, Trent [R-MS-1]",
        "lastName": "Kelly",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-03-12T08:07:37Z",
    "updateDateIncludingText": "2025-03-12T08:07:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-28",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-22",
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
      "actionDate": "2025-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-22",
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
          "date": "2025-01-22T15:02:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:13:25Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr622ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 622\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2025 Mr. Kelly of Mississippi introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes.\n#### 1. Annual funding\nSection 1241(a)(3)(B) of the Food Security Act of 1985 ( 16 U.S.C. 3841(a)(3)(B) ) is amended to read as follows:\n(B) for the conservation stewardship program under subchapter B of that chapter, $1,800,000,000 for each of fiscal years 2025 through 2031. .\n#### 2. Transfer of funds\n$5,020,000,000 of the unobligated balances of amount appropriated or otherwise made available under section 21001 of Public Law 117\u2013169 (commonly referred to ask the Inflation Reduction Act of 2022) is hereby transferred to the Secretary of Agriculture to carry out, using the facilities and authorities of the Commodity Credit Corporation, the conservation stewardship program under subchapter B of chapter 4 of subtitle D of title XII of the Food Security Act of 1985 ( 16 U.S.C. 3839aa\u201321 et seq. ).",
      "versionDate": "2025-01-22",
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
        "updateDate": "2025-02-25T15:09:41Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-22",
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
          "measure-id": "id119hr622",
          "measure-number": "622",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-22",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr622v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-22",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill increases funding for the Conservation Stewardship Program. As background, this Department of Agriculture program provides financial and technical assistance to agricultural\u00a0producers to maintain and improve existing conservation systems and to adopt additional conservation activities in a comprehensive manner on a producer's entire operation.</p>"
        },
        "title": "To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr622.xml",
    "summary": {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases funding for the Conservation Stewardship Program. As background, this Department of Agriculture program provides financial and technical assistance to agricultural\u00a0producers to maintain and improve existing conservation systems and to adopt additional conservation activities in a comprehensive manner on a producer's entire operation.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr622"
    },
    "title": "To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2025-01-22",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill increases funding for the Conservation Stewardship Program. As background, this Department of Agriculture program provides financial and technical assistance to agricultural\u00a0producers to maintain and improve existing conservation systems and to adopt additional conservation activities in a comprehensive manner on a producer's entire operation.</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr622"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr622ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-21T08:48:25Z"
    },
    {
      "title": "To amend the Food Security Act of 1985 to increase funding for the conservation stewardship program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-23T09:05:49Z"
    }
  ]
}
```
