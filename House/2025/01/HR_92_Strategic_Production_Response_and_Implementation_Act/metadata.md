# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/92?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/92
- Title: Strategic Production Response and Implementation Act
- Congress: 119
- Bill type: HR
- Bill number: 92
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-02-13T14:38:46Z
- Update date including text: 2025-02-13T14:38:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/92",
    "number": "92",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "B001302",
        "district": "5",
        "firstName": "Andy",
        "fullName": "Rep. Biggs, Andy [R-AZ-5]",
        "lastName": "Biggs",
        "party": "R",
        "state": "AZ"
      }
    ],
    "title": "Strategic Production Response and Implementation Act",
    "type": "HR",
    "updateDate": "2025-02-13T14:38:46Z",
    "updateDateIncludingText": "2025-02-13T14:38:46Z"
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
          "date": "2025-01-03T16:10:20Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr92ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 92\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Biggs of Arizona introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo provide for the development of a plan to increase oil and gas production under oil and gas leases of Federal lands under the jurisdiction of the Secretary of Agriculture, the Secretary of Energy, the Secretary of the Interior, and the Secretary of Defense in conjunction with a drawdown of petroleum reserves from the Strategic Petroleum Reserve.\n#### 1. Short title\nThis Act may be cited as the Strategic Production Response and Implementation Act .\n#### 2. Compensatory production increase plan\nSection 161 of the Energy Policy and Conservation Act ( 42 U.S.C. 6241 ) is amended by adding at the end the following new subsection:\n(k) Plan (1) In general Except in the case of a severe energy supply interruption described in subsection (d), the Secretary may not execute the first drawdown of petroleum products in the Reserve after the date of enactment of this subsection, whether through sale, exchange, or loan, until the Secretary has developed and implemented a plan to increase the percentage of Federal lands (including submerged lands of the Outer Continental Shelf) under the jurisdiction of the Secretary of Agriculture, the Secretary of Energy, the Secretary of the Interior, and the Secretary of Defense leased for oil and gas production by the same percentage as the percentage of petroleum in the Strategic Petroleum Reserve that is to be drawn down in that first and subsequent drawdowns, subject to the limitation under paragraph (2). (2) Limitation The plan required by paragraph (1) shall not provide for a total increase in the percentage of Federal lands described in paragraph (1) leased for oil and gas production in excess of 10 percent. (3) Consultation The Secretary shall prepare the plan required by paragraph (1) in consultation with the Secretary of Agriculture, the Secretary of the Interior, and the Secretary of Defense. .",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-02-04T12:23:54Z"
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
          "measure-id": "id119hr92",
          "measure-number": "92",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-13"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr92v00",
            "update-date": "2025-02-13"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Strategic Production Response and Implementation Act</strong></p><p>This bill modifies the Energy Policy and Conservation Act to prohibit\u00a0the Department of Energy (DOE) from drawing down petroleum products in the Strategic Petroleum Reserve until DOE develops and implements a plan to increase the percentage of federal lands leased for oil and gas production. The increase must be equal to\u00a0the percentage of petroleum in the Strategic Petroleum Reserve that is to be drawn down. However, the bill does not apply to a drawdown of\u00a0petroleum products in the case of a severe energy supply interruption, which is permitted under current law.\u00a0</p><p>The plan must not provide for a total increase in the percentage of federal lands leased for oil and gas production in excess of 10%.</p>"
        },
        "title": "Strategic Production Response and Implementation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr92.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strategic Production Response and Implementation Act</strong></p><p>This bill modifies the Energy Policy and Conservation Act to prohibit\u00a0the Department of Energy (DOE) from drawing down petroleum products in the Strategic Petroleum Reserve until DOE develops and implements a plan to increase the percentage of federal lands leased for oil and gas production. The increase must be equal to\u00a0the percentage of petroleum in the Strategic Petroleum Reserve that is to be drawn down. However, the bill does not apply to a drawdown of\u00a0petroleum products in the case of a severe energy supply interruption, which is permitted under current law.\u00a0</p><p>The plan must not provide for a total increase in the percentage of federal lands leased for oil and gas production in excess of 10%.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr92"
    },
    "title": "Strategic Production Response and Implementation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Strategic Production Response and Implementation Act</strong></p><p>This bill modifies the Energy Policy and Conservation Act to prohibit\u00a0the Department of Energy (DOE) from drawing down petroleum products in the Strategic Petroleum Reserve until DOE develops and implements a plan to increase the percentage of federal lands leased for oil and gas production. The increase must be equal to\u00a0the percentage of petroleum in the Strategic Petroleum Reserve that is to be drawn down. However, the bill does not apply to a drawdown of\u00a0petroleum products in the case of a severe energy supply interruption, which is permitted under current law.\u00a0</p><p>The plan must not provide for a total increase in the percentage of federal lands leased for oil and gas production in excess of 10%.</p>",
      "updateDate": "2025-02-13",
      "versionCode": "id119hr92"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr92ih.xml"
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
      "title": "Strategic Production Response and Implementation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-31T07:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strategic Production Response and Implementation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-31T07:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the development of a plan to increase oil and gas production under oil and gas leases of Federal lands under the jurisdiction of the Secretary of Agriculture, the Secretary of Energy, the Secretary of the Interior, and the Secretary of Defense in conjunction with a drawdown of petroleum reserves from the Strategic Petroleum Reserve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-31T07:48:42Z"
    }
  ]
}
```
