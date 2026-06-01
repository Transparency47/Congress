# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6690?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6690
- Title: Northern Mariana Islands Medicaid Advancement Act
- Congress: 119
- Bill type: HR
- Bill number: 6690
- Origin chamber: House
- Introduced date: 2025-12-12
- Update date: 2026-01-26T16:45:01Z
- Update date including text: 2026-01-26T16:45:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-12-12: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-12-12: Introduced in House

## Actions

- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Introduced in House
- 2025-12-12 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-12",
    "latestAction": {
      "actionDate": "2025-12-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6690",
    "number": "6690",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000404",
        "district": "",
        "firstName": "Kimberlyn",
        "fullName": "Del. King-Hinds, Kimberlyn [R-MP-At Large]",
        "lastName": "King-Hinds",
        "party": "R",
        "state": "MP"
      }
    ],
    "title": "Northern Mariana Islands Medicaid Advancement Act",
    "type": "HR",
    "updateDate": "2026-01-26T16:45:01Z",
    "updateDateIncludingText": "2026-01-26T16:45:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-12",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-12",
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
          "date": "2025-12-12T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-12-12",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6690ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6690\nIN THE HOUSE OF REPRESENTATIVES\nDecember 12, 2025 Mrs. King-Hinds (for herself and Mr. Moylan ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XI of the Social Security Act to increase the payment limit under Medicaid for the Northern Mariana Islands.\n#### 1. Short title\nThis Act may be cited as the Northern Mariana Islands Medicaid Advancement Act .\n#### 2. Increasing payment limit under Medicaid for the Northern Mariana Islands\nSection 1108(g)(2)(D) of the Social Security Act ( 42 U.S.C. 1308(g)(2)(D) ) is amended\u2014\n**(1)**\nin clause (i), by striking clause (ii) and inserting clauses (ii) through (iv) ;\n**(2)**\nin clause (ii), by striking and at the end; and\n**(3)**\nby adding at the end the following new clause:\n(iv) for fiscal year 2026, the amount determined under subparagraph (E) with respect to American Samoa for such fiscal year; and .",
      "versionDate": "2025-12-12",
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
        "name": "Health",
        "updateDate": "2026-01-08T15:03:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-12-12",
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
          "measure-id": "id119hr6690",
          "measure-number": "6690",
          "measure-type": "hr",
          "orig-publish-date": "2025-12-12",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr6690v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-12-12",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Northern Mariana Islands Medicaid Advancement\u00a0Act</strong></p><p>This bill requires the Medicaid funding cap for the Northern Mariana Islands to be the same as that for American Samoa in FY2026.</p>"
        },
        "title": "Northern Mariana Islands Medicaid Advancement Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr6690.xml",
    "summary": {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northern Mariana Islands Medicaid Advancement\u00a0Act</strong></p><p>This bill requires the Medicaid funding cap for the Northern Mariana Islands to be the same as that for American Samoa in FY2026.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6690"
    },
    "title": "Northern Mariana Islands Medicaid Advancement Act"
  },
  "summaries": [
    {
      "actionDate": "2025-12-12",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Northern Mariana Islands Medicaid Advancement\u00a0Act</strong></p><p>This bill requires the Medicaid funding cap for the Northern Mariana Islands to be the same as that for American Samoa in FY2026.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr6690"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6690ih.xml"
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
      "title": "Northern Mariana Islands Medicaid Advancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Northern Mariana Islands Medicaid Advancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T05:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XI of the Social Security Act to increase the payment limit under Medicaid for the Northern Mariana Islands.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T05:48:20Z"
    }
  ]
}
```
