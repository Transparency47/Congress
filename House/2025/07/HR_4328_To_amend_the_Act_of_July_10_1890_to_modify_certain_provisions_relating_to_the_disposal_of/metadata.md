# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4328?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4328
- Title: Wyoming Education Trust Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 4328
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-04-06T19:15:41Z
- Update date including text: 2026-04-06T19:15:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Natural Resources.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4328",
    "number": "4328",
    "originChamber": "House",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "H001096",
        "district": "",
        "firstName": "Harriet",
        "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
        "lastName": "Hageman",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Wyoming Education Trust Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-06T19:15:41Z",
    "updateDateIncludingText": "2026-04-06T19:15:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:04:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4328ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4328\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Ms. Hageman introduced the following bill; which was referred to the Committee on Natural Resources\nA BILL\nTo amend the Act of July 10, 1890, to modify certain provisions relating to the disposal of public land in the State of Wyoming for educational purposes.\n#### 1. Short title\nThis Act may be cited as the Wyoming Education Trust Modernization Act .\n#### 2. Disposal of public land in the State of Wyoming for educational purposes\nThe Act of July 10, 1890 (26 Stat. 222, chapter 664), is amended\u2014\n**(1)**\nin section 5, in the first sentence, by striking interest of and inserting earnings on ;\n**(2)**\nin section 7, by striking interest of and inserting earnings on ; and\n**(3)**\nin section 8, in the first sentence, by striking income thereof and inserting earnings on which .",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-12-17",
        "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably."
      },
      "number": "2273",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Wyoming Education Trust Modernization Act",
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
            "name": "Education programs funding",
            "updateDate": "2026-01-07T16:55:08Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-01-07T16:55:08Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T16:55:08Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2026-01-07T16:55:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:28:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
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
          "measure-id": "id119hr4328",
          "measure-number": "4328",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-10",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4328v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2025-07-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>"
        },
        "title": "Wyoming Education Trust Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4328.xml",
    "summary": {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4328"
    },
    "title": "Wyoming Education Trust Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hr4328"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4328ih.xml"
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
      "title": "Wyoming Education Trust Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T13:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Wyoming Education Trust Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T13:38:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Act of July 10, 1890, to modify certain provisions relating to the disposal of public land in the State of Wyoming for educational purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T13:33:22Z"
    }
  ]
}
```
