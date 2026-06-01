# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/508?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/508
- Title: Bring American Companies Home Act
- Congress: 119
- Bill type: HR
- Bill number: 508
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2025-04-07T13:22:01Z
- Update date including text: 2025-04-07T13:22:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/508",
    "number": "508",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Bring American Companies Home Act",
    "type": "HR",
    "updateDate": "2025-04-07T13:22:01Z",
    "updateDateIncludingText": "2025-04-07T13:22:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:04:30Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr508ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 508\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Mr. Green of Tennessee introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo allow expensing of amounts paid to move business property from China to the United States, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bring American Companies Home Act .\n#### 2. Expensing of amounts paid to move business property from China to the United States\n##### (a) In general\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall establish a program under which amounts paid by a United States person (as defined in section 7701(a)(30)) to move inventory and equipment and supplies used in a trade or business of the taxpayer from China to the United States are allowed as a deduction in the taxable year in which paid by the taxpayer.\n##### (b) Regulations\nThe Secretary of the Treasury (or the Secretary\u2019s delegate) shall issue regulations under the program carried out under subsection (a) that restrict the amounts that may be expensed under such program to business moving expenses (within the meaning of the Internal Revenue Code of 1986 and the regulations and guidance issued thereunder).\n##### (c) Expensing paid for with tariffs collected from China\n**(1) Establishment of trust fund**\nThere is established in the Treasury of the United States a trust fund consisting of such amounts as are appropriated to such trust fund under paragraph (2).\n**(2) Appropriations to trust fund**\nThere are hereby appropriated to such trust fund amounts equivalent to the tariffs collected by the United States on goods manufactured in China.\n**(3) Appropriations from trust fund**\nThere are hereby appropriated from such trust fund to the General Fund of the Treasury amounts equivalent to the reduction in revenue to such General Fund by reason of subsection (a).\n**(4) Timing of transfers, etc**\nRules similar to the rules of section 9601 of the Internal Revenue Code of 1986 shall apply with respect to appropriations to and from such trust fund under paragraphs (2) and (3).",
      "versionDate": "2025-01-16",
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
        "name": "Taxation",
        "updateDate": "2025-02-19T20:05:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
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
          "measure-id": "id119hr508",
          "measure-number": "508",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-16",
          "originChamber": "HOUSE",
          "update-date": "2025-04-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr508v00",
            "update-date": "2025-04-07"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Bring American Companies Home Act </strong></p><p>This bill requires the Department of the Treasury to establish a program and regulations allowing U.S. persons (U.S. citizens or residents, domestic partnerships or corporations, or estates and trusts) to deduct in the tax year incurred costs of moving inventory, equipment, and supplies used in a trade or business from China to the United States.</p><p>The bill also</p><ul><li>establishes a trust fund and appropriates to such fund tariff amounts collected by the United States on goods manufactured in China,</li><li>appropriates from such trust fund to the general fund of the Treasury amounts equivalent to the reduction in revenue resulting from the tax deduction, and</li><li>requires amounts to be transferred between funds at least monthly.<em></em></li></ul>"
        },
        "title": "Bring American Companies Home Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr508.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bring American Companies Home Act </strong></p><p>This bill requires the Department of the Treasury to establish a program and regulations allowing U.S. persons (U.S. citizens or residents, domestic partnerships or corporations, or estates and trusts) to deduct in the tax year incurred costs of moving inventory, equipment, and supplies used in a trade or business from China to the United States.</p><p>The bill also</p><ul><li>establishes a trust fund and appropriates to such fund tariff amounts collected by the United States on goods manufactured in China,</li><li>appropriates from such trust fund to the general fund of the Treasury amounts equivalent to the reduction in revenue resulting from the tax deduction, and</li><li>requires amounts to be transferred between funds at least monthly.<em></em></li></ul>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hr508"
    },
    "title": "Bring American Companies Home Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Bring American Companies Home Act </strong></p><p>This bill requires the Department of the Treasury to establish a program and regulations allowing U.S. persons (U.S. citizens or residents, domestic partnerships or corporations, or estates and trusts) to deduct in the tax year incurred costs of moving inventory, equipment, and supplies used in a trade or business from China to the United States.</p><p>The bill also</p><ul><li>establishes a trust fund and appropriates to such fund tariff amounts collected by the United States on goods manufactured in China,</li><li>appropriates from such trust fund to the general fund of the Treasury amounts equivalent to the reduction in revenue resulting from the tax deduction, and</li><li>requires amounts to be transferred between funds at least monthly.<em></em></li></ul>",
      "updateDate": "2025-04-07",
      "versionCode": "id119hr508"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr508ih.xml"
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
      "title": "Bring American Companies Home Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-13T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bring American Companies Home Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To allow expensing of amounts paid to move business property from China to the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T06:48:26Z"
    }
  ]
}
```
