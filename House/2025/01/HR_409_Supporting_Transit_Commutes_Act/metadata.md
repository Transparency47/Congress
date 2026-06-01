# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/409?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/409
- Title: Supporting Transit Commutes Act
- Congress: 119
- Bill type: HR
- Bill number: 409
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-02T09:05:28Z
- Update date including text: 2025-12-02T09:05:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/409",
    "number": "409",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "A000148",
        "district": "4",
        "firstName": "Jake",
        "fullName": "Rep. Auchincloss, Jake [D-MA-4]",
        "lastName": "Auchincloss",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Supporting Transit Commutes Act",
    "type": "HR",
    "updateDate": "2025-12-02T09:05:28Z",
    "updateDateIncludingText": "2025-12-02T09:05:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:00:10Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-01-15",
      "state": "MA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-01-28",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "DC"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-01-31",
      "state": "NJ"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "NY"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr409ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 409\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Auchincloss (for himself, Mr. Lawler , and Mr. McGovern ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow employers to deduct certain transportation fringe benefits.\n#### 1. Short title\nThis Act may be cited as the Supporting Transit Commutes Act .\n#### 2. Deduction allowed for certain transportation fringe benefits provided by employers\n##### (a) In general\nSection 274(l) of the Internal Revenue Code of 1986 is amended by redesignating paragraph (2) as paragraph (3) and inserting after paragraph (1) the following new paragraph:\n(2) Exception for certain transportation fringe benefits (A) In general Paragraph (1) shall not apply to so much of any qualified transportation fringe described in subparagraph (A) or (B) of section 132(f)(1) as does not exceed the limitation described in section 132(f)(2)(A). (B) Reduced deduction in case of benefits provided under salary reduction agreements In the case of any qualified transportation fringe with respect to which the employee may elect between receiving such fringe and receiving an amount directly in cash, subparagraph (A) shall be applied by substituting 50 percent of so much for so much . .\n##### (b) Conforming amendment\nSection 274(l)(3) of such Code, as redesignated by subsection (a), is amended\u2014\n**(1)**\nby striking this subsection and inserting paragraph (1) , and\n**(2)**\nby inserting for qualified bicycle commuting reimbursement after Exception in the heading thereof.\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2025-01-15",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commuting",
            "updateDate": "2025-04-25T17:54:09Z"
          },
          {
            "name": "Employee benefits and pensions",
            "updateDate": "2025-04-25T17:54:26Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-04-25T17:54:00Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-04-25T17:54:18Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-19T20:01:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr409",
          "measure-number": "409",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-04-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr409v00",
            "update-date": "2025-04-14"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Transit Commutes Act\u00a0</strong></p><p>This bill provides employers a tax deduction for certain transportation fringe benefits given to employees.</p><p>Under the bill, employers may deduct costs for providing employees transportation in a commuter highway vehicle (e.g., van pool) between the employee\u2019s home and place of work or a transit pass. The amount of the deduction cannot exceed the aggregate exclusion amount for such fringe benefits ($325 per month per employee in 2025 and adjusted annually). Further, under the bill, the deduction cannot exceed 50% of such amount for transportation fringe benefits provided under a salary reduction agreement.</p>"
        },
        "title": "Supporting Transit Commutes Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr409.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Transit Commutes Act\u00a0</strong></p><p>This bill provides employers a tax deduction for certain transportation fringe benefits given to employees.</p><p>Under the bill, employers may deduct costs for providing employees transportation in a commuter highway vehicle (e.g., van pool) between the employee\u2019s home and place of work or a transit pass. The amount of the deduction cannot exceed the aggregate exclusion amount for such fringe benefits ($325 per month per employee in 2025 and adjusted annually). Further, under the bill, the deduction cannot exceed 50% of such amount for transportation fringe benefits provided under a salary reduction agreement.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr409"
    },
    "title": "Supporting Transit Commutes Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Transit Commutes Act\u00a0</strong></p><p>This bill provides employers a tax deduction for certain transportation fringe benefits given to employees.</p><p>Under the bill, employers may deduct costs for providing employees transportation in a commuter highway vehicle (e.g., van pool) between the employee\u2019s home and place of work or a transit pass. The amount of the deduction cannot exceed the aggregate exclusion amount for such fringe benefits ($325 per month per employee in 2025 and adjusted annually). Further, under the bill, the deduction cannot exceed 50% of such amount for transportation fringe benefits provided under a salary reduction agreement.</p>",
      "updateDate": "2025-04-14",
      "versionCode": "id119hr409"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr409ih.xml"
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
      "title": "Supporting Transit Commutes Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-08T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Transit Commutes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-08T05:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to allow employers to deduct certain transportation fringe benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-08T05:48:31Z"
    }
  ]
}
```
