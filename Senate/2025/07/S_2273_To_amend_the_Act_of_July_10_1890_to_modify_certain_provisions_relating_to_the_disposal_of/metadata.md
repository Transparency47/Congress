# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2273?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2273
- Title: Wyoming Education Trust Modernization Act
- Congress: 119
- Bill type: S
- Bill number: 2273
- Origin chamber: Senate
- Introduced date: 2025-07-14
- Update date: 2026-04-30T16:20:21Z
- Update date including text: 2026-04-30T16:20:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-14: Introduced in Senate
- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.
- Latest action: 2025-07-14: Introduced in Senate

## Actions

- 2025-07-14 - IntroReferral: Introduced in Senate
- 2025-07-14 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- 2025-12-02 - Committee: Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.
- 2025-12-17 - Committee: Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-14",
    "latestAction": {
      "actionDate": "2025-07-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2273",
    "number": "2273",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "Wyoming Education Trust Modernization Act",
    "type": "S",
    "updateDate": "2026-04-30T16:20:21Z",
    "updateDateIncludingText": "2026-04-30T16:20:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Public Lands, Forests, and Mining. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-14",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
        "item": [
          {
            "date": "2025-12-17T14:30:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-14T22:37:42Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-02T20:00:50Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Public Lands, Forests, and Mining Subcommittee",
          "systemCode": "sseg03"
        }
      },
      "systemCode": "sseg00",
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
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2273is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2273\nIN THE SENATE OF THE UNITED STATES\nJuly 14, 2025 Ms. Lummis (for herself and Mr. Barrasso ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo amend the Act of July 10, 1890, to modify certain provisions relating to the disposal of public land in the State of Wyoming for educational purposes.\n#### 1. Short title\nThis Act may be cited as the Wyoming Education Trust Modernization Act .\n#### 2. Disposal of public land in the State of Wyoming for educational purposes\nThe Act of July 10, 1890 (26 Stat. 222, chapter 664), is amended\u2014\n**(1)**\nin section 5, in the first sentence, by striking interest of and inserting earnings on ;\n**(2)**\nin section 7, by striking interest of and inserting earnings on ; and\n**(3)**\nin section 8, in the first sentence, by striking income thereof and inserting earnings on which .",
      "versionDate": "2025-07-14",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "4328",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Wyoming Education Trust Modernization Act",
      "type": "HR"
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
            "updateDate": "2026-01-07T16:54:41Z"
          },
          {
            "name": "Government trust funds",
            "updateDate": "2026-01-07T16:54:47Z"
          },
          {
            "name": "Land use and conservation",
            "updateDate": "2026-01-07T16:54:37Z"
          },
          {
            "name": "Wyoming",
            "updateDate": "2026-01-07T16:54:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-07-30T22:39:24Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-14",
    "originChamber": "Senate",
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
          "measure-id": "id119s2273",
          "measure-number": "2273",
          "measure-type": "s",
          "orig-publish-date": "2025-07-14",
          "originChamber": "SENATE",
          "update-date": "2026-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2273v00",
            "update-date": "2026-02-10"
          },
          "action-date": "2025-07-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>"
        },
        "title": "Wyoming Education Trust Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2273.xml",
    "summary": {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2273"
    },
    "title": "Wyoming Education Trust Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Wyoming Education Trust Modernization Act</strong></p><p>This bill provides Wyoming with more flexibility to invest the principal of its permanent school fund by allowing the state to use earnings generated from investment of the fund rather than only interest.</p><p>By way of background, Congress created the fund when Wyoming became a state by granting certain federal lands to be held in a trust for the state. Proceeds from school trust land sales, exchanges, or disposals are deposited into the fund to support public schools.</p>",
      "updateDate": "2026-02-10",
      "versionCode": "id119s2273"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2273is.xml"
        }
      ],
      "type": "Introduced in Senate"
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
      "updateDate": "2025-12-18T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Wyoming Education Trust Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Act of July 10, 1890, to modify certain provisions relating to the disposal of public land in the State of Wyoming for educational purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:22Z"
    }
  ]
}
```
