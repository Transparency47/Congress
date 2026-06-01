# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5685?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5685
- Title: PNA Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5685
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2026-03-30T18:28:19Z
- Update date including text: 2026-03-30T18:28:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5685",
    "number": "5685",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001160",
        "district": "4",
        "firstName": "Gwen",
        "fullName": "Rep. Moore, Gwen [D-WI-4]",
        "lastName": "Moore",
        "party": "D",
        "state": "WI"
      }
    ],
    "title": "PNA Modernization Act",
    "type": "HR",
    "updateDate": "2026-03-30T18:28:19Z",
    "updateDateIncludingText": "2026-03-30T18:28:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:30:35Z",
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
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NJ"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5685ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5685\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Ms. Moore of Wisconsin (for herself, Mrs. Watson Coleman , Ms. Brownley , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to increase under the Medicaid program the minimum monthly personal needs allowance for institutionalized individuals and couples, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Personal Needs Allowance Modernization Act or the PNA Modernization Act .\n#### 2. Increasing under the Medicaid program the minimum monthly personal needs allowance for institutionalized individuals and couples\nSection 1902(q)(2) of the Social Security Act ( 42 U.S.C. 1396a(q)(2) ) is amended\u2014\n**(1)**\nby inserting after $30 the following: (or, beginning January 1, 2026, $60) ;\n**(2)**\nby inserting after and $60 the following: (or, beginning January 1, 2026, $120) ; and\n**(3)**\nby adding at the end the following new sentence: Whenever benefit amounts under title II of the Social Security Act are increased by any percentage effective with a month after November 2025 as a result of a determination made under section 215(i) of such Act, each of the dollar amounts in effect under the previous sentence for the month before such month shall be increased by the same percentage. .",
      "versionDate": "2025-10-03",
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
        "actionDate": "2026-03-03",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "7778",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Medicaid PNA Modernization Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-12-10T19:17:02Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
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
          "measure-id": "id119hr5685",
          "measure-number": "5685",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2026-01-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5685v00",
            "update-date": "2026-01-15"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Personal Needs Allowance Modernization Act or the PNA Modernization Act\u00a0</strong></p><p>This bill increases the minimum monthly personal needs allowance under Medicaid for an institutionalized individual and couple from $30 to $60 and from $60 to $120, respectively. (The personal needs allowance is deducted from an individual's total income when determining the individual's contribution to the cost of institutionalized care under Medicaid.)</p>"
        },
        "title": "PNA Modernization Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5685.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Personal Needs Allowance Modernization Act or the PNA Modernization Act\u00a0</strong></p><p>This bill increases the minimum monthly personal needs allowance under Medicaid for an institutionalized individual and couple from $30 to $60 and from $60 to $120, respectively. (The personal needs allowance is deducted from an individual's total income when determining the individual's contribution to the cost of institutionalized care under Medicaid.)</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5685"
    },
    "title": "PNA Modernization Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Personal Needs Allowance Modernization Act or the PNA Modernization Act\u00a0</strong></p><p>This bill increases the minimum monthly personal needs allowance under Medicaid for an institutionalized individual and couple from $30 to $60 and from $60 to $120, respectively. (The personal needs allowance is deducted from an individual's total income when determining the individual's contribution to the cost of institutionalized care under Medicaid.)</p>",
      "updateDate": "2026-01-15",
      "versionCode": "id119hr5685"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5685ih.xml"
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
      "title": "PNA Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T09:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PNA Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Personal Needs Allowance Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T09:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to increase under the Medicaid program the minimum monthly personal needs allowance for institutionalized individuals and couples, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T09:48:19Z"
    }
  ]
}
```
