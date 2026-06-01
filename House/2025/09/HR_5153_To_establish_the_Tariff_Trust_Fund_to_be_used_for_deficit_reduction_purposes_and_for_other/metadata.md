# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5153?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5153
- Title: TRUST Act
- Congress: 119
- Bill type: HR
- Bill number: 5153
- Origin chamber: House
- Introduced date: 2025-09-04
- Update date: 2026-03-11T00:49:10Z
- Update date including text: 2026-03-11T00:49:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-09-04: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-09-04: Introduced in House

## Actions

- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Introduced in House
- 2025-09-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5153",
    "number": "5153",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001224",
        "district": "1",
        "firstName": "Nathaniel",
        "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
        "lastName": "Moran",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "TRUST Act",
    "type": "HR",
    "updateDate": "2026-03-11T00:49:10Z",
    "updateDateIncludingText": "2026-03-11T00:49:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-04",
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
          "date": "2025-09-04T13:00:05Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5153ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5153\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 4, 2025 Mr. Moran introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo establish the Tariff Trust Fund to be used for deficit reduction purposes, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tariff Revenue Used to Secure Tomorrow Act or TRUST Act .\n#### 2. Tariff Trust Fund\n##### (a) Establishment\nThere is hereby established in the Treasury of the United States a fund to be known as the Tariff Trust Fund (in this section referred to as the Fund ).\n##### (b) Deposit of funds\nNotwithstanding any other provision of law, if the United States\u2014\n**(1)**\nmaintains a budget deficit for any fiscal year beginning with fiscal year 2026, and\n**(2)**\ncontinues to maintain a budget deficit for the subsequent fiscal year,\namounts collected from the imposition of duties under any provision of law for such subsequent fiscal year that are in excess of the amount collected from the imposition of duties under any provision of law for fiscal year 2025 shall be deposited in the Fund established by subsection (a).\n##### (c) Use of funds\nAmounts deposited in the Fund under subsection (b) shall be transferred to the general fund of the Treasury and used only for deficit reduction.\n##### (d) Effective date\nThis Act shall take effect on the date of the enactment of this Act and shall apply with respect to amounts collected from the imposition of duties beginning on and after October 1, 2025.",
      "versionDate": "2025-09-04",
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
        "updateDate": "2025-09-15T17:49:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-09-04",
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
          "measure-id": "id119hr5153",
          "measure-number": "5153",
          "measure-type": "hr",
          "orig-publish-date": "2025-09-04",
          "originChamber": "HOUSE",
          "update-date": "2026-03-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5153v00",
            "update-date": "2026-03-11"
          },
          "action-date": "2025-09-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Tariff Revenue Used to Secure Tomorrow Act or TRUST Act</strong></p><p>This bill establishes the Tariff Trust Fund within the Treasury and requires certain revenues collected from duties (e.g., tariffs) to be deposited into the fund and used for deficit reduction.</p><p>If the federal government maintains a budget deficit for any fiscal year beginning with FY2026 and continues to maintain a budget deficit for the subsequent fiscal year, the bill requires amounts collected from the imposition of duties for the subsequent fiscal year that exceed the amounts collected from duties for FY2025 to be deposited into the fund established by this bill.\u00a0</p><p>Any amounts deposited into the fund must be transferred to the general fund of the Treasury and may only be used for deficit reduction.\u00a0</p>"
        },
        "title": "TRUST Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5153.xml",
    "summary": {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tariff Revenue Used to Secure Tomorrow Act or TRUST Act</strong></p><p>This bill establishes the Tariff Trust Fund within the Treasury and requires certain revenues collected from duties (e.g., tariffs) to be deposited into the fund and used for deficit reduction.</p><p>If the federal government maintains a budget deficit for any fiscal year beginning with FY2026 and continues to maintain a budget deficit for the subsequent fiscal year, the bill requires amounts collected from the imposition of duties for the subsequent fiscal year that exceed the amounts collected from duties for FY2025 to be deposited into the fund established by this bill.\u00a0</p><p>Any amounts deposited into the fund must be transferred to the general fund of the Treasury and may only be used for deficit reduction.\u00a0</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr5153"
    },
    "title": "TRUST Act"
  },
  "summaries": [
    {
      "actionDate": "2025-09-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Tariff Revenue Used to Secure Tomorrow Act or TRUST Act</strong></p><p>This bill establishes the Tariff Trust Fund within the Treasury and requires certain revenues collected from duties (e.g., tariffs) to be deposited into the fund and used for deficit reduction.</p><p>If the federal government maintains a budget deficit for any fiscal year beginning with FY2026 and continues to maintain a budget deficit for the subsequent fiscal year, the bill requires amounts collected from the imposition of duties for the subsequent fiscal year that exceed the amounts collected from duties for FY2025 to be deposited into the fund established by this bill.\u00a0</p><p>Any amounts deposited into the fund must be transferred to the general fund of the Treasury and may only be used for deficit reduction.\u00a0</p>",
      "updateDate": "2026-03-11",
      "versionCode": "id119hr5153"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5153ih.xml"
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
      "title": "TRUST Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "TRUST Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Tariff Revenue Used to Secure Tomorrow Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:32Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Tariff Trust Fund to be used for deficit reduction purposes, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:30Z"
    }
  ]
}
```
