# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/734?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/734
- Title: To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture.
- Congress: 119
- Bill type: HR
- Bill number: 734
- Origin chamber: House
- Introduced date: 2025-01-24
- Update date: 2025-03-25T17:40:28Z
- Update date including text: 2025-03-25T17:40:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-24: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-24: Introduced in House

## Actions

- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Introduced in House
- 2025-01-24 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-24",
    "latestAction": {
      "actionDate": "2025-01-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/734",
    "number": "734",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001212",
        "district": "1",
        "firstName": "Barry",
        "fullName": "Rep. Moore, Barry [R-AL-1]",
        "lastName": "Moore",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture.",
    "type": "HR",
    "updateDate": "2025-03-25T17:40:28Z",
    "updateDateIncludingText": "2025-03-25T17:40:28Z"
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
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-24",
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
      "actionDate": "2025-01-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-24",
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
          "date": "2025-01-24T14:00:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:14:46Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr734ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 734\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 24, 2025 Mr. Moore of Alabama introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture.\n#### 1. Public comment on quality control guidance\nSection 16(c) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(c) ) is amended by adding at the end the following:\n(10) Public comment on quality control guidance (A) In general The Secretary shall provide notice and make available for public comment for a period of not fewer than 60 days any new or updated guidance proposing substantive changes for conducting quality control reviews prior to any such guidance being finalized. (B) Scope The requirement in (A) shall be applicable to any proposed guidance reasonably expected to require state agencies to make changes to systems, procedures, or staffing pertaining to quality control reviews or that impact verification requirements for supplemental nutrition assistance program recipients. (C) Exception In the case of an urgent and immediate need, the Secretary may issue interim final guidance simultaneous with the notice and comment requirements required in (A). .",
      "versionDate": "2025-01-24",
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
        "updateDate": "2025-03-01T13:46:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-24",
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
          "measure-id": "id119hr734",
          "measure-number": "734",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-24",
          "originChamber": "HOUSE",
          "update-date": "2025-03-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr734v00",
            "update-date": "2025-03-25"
          },
          "action-date": "2025-01-24",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill requires the Department of Agriculture (USDA) to provide a notice and comment period prior to making certain substantive changes to the Supplemental Nutrition Assistance Program (SNAP) quality control system, with exceptions.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. State agencies must conduct quality control reviews of their SNAP caseloads and report these findings to the USDA Food and Nutrition Service.</p><p>The bill requires USDA to provide a notice and public comment period of at least 60 days prior to finalizing any new or updated guidance that proposes substantive changes for conducting quality control reviews. This applies to any proposed guidance reasonably expected to require state agencies to make changes to systems, procedures, or staffing pertaining to quality control reviews or that impact verification requirements for SNAP recipients.</p><p>In the case of an urgent and immediate need, USDA may issue interim final guidance simultaneously with the notice and comment requirements.</p>"
        },
        "title": "To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr734.xml",
    "summary": {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Agriculture (USDA) to provide a notice and comment period prior to making certain substantive changes to the Supplemental Nutrition Assistance Program (SNAP) quality control system, with exceptions.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. State agencies must conduct quality control reviews of their SNAP caseloads and report these findings to the USDA Food and Nutrition Service.</p><p>The bill requires USDA to provide a notice and public comment period of at least 60 days prior to finalizing any new or updated guidance that proposes substantive changes for conducting quality control reviews. This applies to any proposed guidance reasonably expected to require state agencies to make changes to systems, procedures, or staffing pertaining to quality control reviews or that impact verification requirements for SNAP recipients.</p><p>In the case of an urgent and immediate need, USDA may issue interim final guidance simultaneously with the notice and comment requirements.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr734"
    },
    "title": "To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture."
  },
  "summaries": [
    {
      "actionDate": "2025-01-24",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill requires the Department of Agriculture (USDA) to provide a notice and comment period prior to making certain substantive changes to the Supplemental Nutrition Assistance Program (SNAP) quality control system, with exceptions.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. State agencies must conduct quality control reviews of their SNAP caseloads and report these findings to the USDA Food and Nutrition Service.</p><p>The bill requires USDA to provide a notice and public comment period of at least 60 days prior to finalizing any new or updated guidance that proposes substantive changes for conducting quality control reviews. This applies to any proposed guidance reasonably expected to require state agencies to make changes to systems, procedures, or staffing pertaining to quality control reviews or that impact verification requirements for SNAP recipients.</p><p>In the case of an urgent and immediate need, USDA may issue interim final guidance simultaneously with the notice and comment requirements.</p>",
      "updateDate": "2025-03-25",
      "versionCode": "id119hr734"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr734ih.xml"
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
      "title": "To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-25T05:03:28Z"
    },
    {
      "title": "To amend the Food and Nutrition Act of 2008 with respect to the issuance of quality control guidance issued by the Secretary of Agriculture.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-25T09:05:50Z"
    }
  ]
}
```
