# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/1118?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-resolution/1118
- Title: Expressing support for the designation of the third week of March as "National CACFP Week".
- Congress: 119
- Bill type: HRES
- Bill number: 1118
- Origin chamber: House
- Introduced date: 2026-03-17
- Update date: 2026-04-06T13:07:51Z
- Update date including text: 2026-04-06T13:07:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-03-17: Introduced in House
- 2026-03-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - IntroReferral: Submitted in House
- 2026-03-17 - IntroReferral: Submitted in House
- Latest action: 2026-03-17: Submitted in House

## Actions

- 2026-03-17 - IntroReferral: Referred to the House Committee on Education and Workforce.
- 2026-03-17 - IntroReferral: Submitted in House
- 2026-03-17 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-17",
    "latestAction": {
      "actionDate": "2026-03-17",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-resolution/1118",
    "number": "1118",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Expressing support for the designation of the third week of March as \"National CACFP Week\".",
    "type": "HRES",
    "updateDate": "2026-04-06T13:07:51Z",
    "updateDateIncludingText": "2026-04-06T13:07:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2026-03-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2026-03-17T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-03-17",
      "state": "PA"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "FL"
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
      "sponsorshipDate": "2026-03-17",
      "state": "MA"
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
      "sponsorshipDate": "2026-03-17",
      "state": "DC"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1118ih.xml",
      "text": "IV\n119th CONGRESS\n2d Session\nH. RES. 1118\nIN THE HOUSE OF REPRESENTATIVES\nMarch 17, 2026 Ms. Bonamici (for herself, Mr. Mackenzie , Ms. Wilson of Florida , Mr. McGovern , Ms. Norton , and Mr. Davis of Illinois ) submitted the following resolution; which was referred to the Committee on Education and Workforce\nRESOLUTION\nExpressing support for the designation of the third week of March as National CACFP Week .\nThat the House of Representatives\u2014\n**(1)**\nrecognizes the role of the child and adult care food program (commonly referred to as CACFP ) in improving the health of the country\u2019s most vulnerable children and adults in Head Start programs, childcare programs, including military childcare, family daycare homes, emergency shelters, adult daycare programs, and after-school care by providing nutritious meals and snacks;\n**(2)**\nurges support for continuing to strengthen CACFP by offering reimbursement for an additional meal or snack for children in care for a full day, reducing area eligibility from 50 percent to 40 percent, offering annual eligibility to for profit childcare centers, factoring in annual food inflation fairly for childcare regardless of setting, and reducing administrative burdens to participation;\n**(3)**\nacknowledges that CACFP can, and should, be an important tool in reducing the costs faced by the care economy, including licensed or approved child or adult care; and\n**(4)**\nsupports the designation of National CACFP Week .",
      "versionDate": "2026-03-17",
      "versionType": "IH"
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
        "actionDate": "2025-03-18",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "228",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Expressing support for the designation of the third week of March 2025 as \"National CACFP Week\".",
      "type": "HRES"
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
        "updateDate": "2026-03-19T22:34:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-03-17",
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
          "measure-id": "id119hres1118",
          "measure-number": "1118",
          "measure-type": "hres",
          "orig-publish-date": "2026-03-17",
          "originChamber": "HOUSE",
          "update-date": "2026-04-06"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres1118v00",
            "update-date": "2026-04-06"
          },
          "action-date": "2026-03-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution recognizes the role of the Child and Adult Care Food Program (commonly referred to as CACFP) in improving the health of the country's most vulnerable children and adults in Head Start programs,\u00a0child care programs, family day care homes, emergency shelters,\u00a0adult day care programs, and after-school care by providing nutritious meals and snacks.</p><p>It also supports the designation of National\u00a0CACFP Week.</p>"
        },
        "title": "Expressing support for the designation of the third week of March as \"National CACFP Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres1118.xml",
    "summary": {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the role of the Child and Adult Care Food Program (commonly referred to as CACFP) in improving the health of the country's most vulnerable children and adults in Head Start programs,\u00a0child care programs, family day care homes, emergency shelters,\u00a0adult day care programs, and after-school care by providing nutritious meals and snacks.</p><p>It also supports the designation of National\u00a0CACFP Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres1118"
    },
    "title": "Expressing support for the designation of the third week of March as \"National CACFP Week\"."
  },
  "summaries": [
    {
      "actionDate": "2026-03-17",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution recognizes the role of the Child and Adult Care Food Program (commonly referred to as CACFP) in improving the health of the country's most vulnerable children and adults in Head Start programs,\u00a0child care programs, family day care homes, emergency shelters,\u00a0adult day care programs, and after-school care by providing nutritious meals and snacks.</p><p>It also supports the designation of National\u00a0CACFP Week.</p>",
      "updateDate": "2026-04-06",
      "versionCode": "id119hres1118"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-03-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hres/BILLS-119hres1118ih.xml"
        }
      ],
      "type": "IH"
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
      "title": "Expressing support for the designation of the third week of March as \"National CACFP Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-18T08:18:34Z"
    },
    {
      "title": "Expressing support for the designation of the third week of March as \"National CACFP Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-18T08:06:45Z"
    }
  ]
}
```
