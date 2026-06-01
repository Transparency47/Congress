# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/382?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/382
- Title: Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program.
- Congress: 119
- Bill type: HRES
- Bill number: 382
- Origin chamber: House
- Introduced date: 2025-05-05
- Update date: 2025-07-02T14:44:55Z
- Update date including text: 2025-07-02T14:44:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-05: Introduced in House
- 2025-05-05 - IntroReferral: Referred to the House Committee on Rules.
- 2025-05-05 - IntroReferral: Submitted in House
- 2025-05-05 - IntroReferral: Submitted in House
- Latest action: 2025-05-05: Submitted in House

## Actions

- 2025-05-05 - IntroReferral: Referred to the House Committee on Rules.
- 2025-05-05 - IntroReferral: Submitted in House
- 2025-05-05 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-05",
    "latestAction": {
      "actionDate": "2025-05-05",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/382",
    "number": "382",
    "originChamber": "House",
    "policyArea": {
      "name": "Economics and Public Finance"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program.",
    "type": "HRES",
    "updateDate": "2025-07-02T14:44:55Z",
    "updateDateIncludingText": "2025-07-02T14:44:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-05",
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
          "date": "2025-05-05T16:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NE"
    },
    {
      "bioguideId": "V000135",
      "district": "3",
      "firstName": "Derrick",
      "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Orden",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres382ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 382\nIN THE HOUSE OF REPRESENTATIVES\nMay 5, 2025 Mr. Nunn of Iowa (for himself, Mr. Bacon , and Mr. Van Orden ) submitted the following resolution; which was referred to the Committee on Rules\nRESOLUTION\nProviding a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program.\n#### 1. Point of order on cuts to certain programs in reconciliation measures\n##### (a) In general\nDuring the period beginning on the date of the enactment of this resolution and ending on the last day of the 119th Congress, it shall not be in order in the House of Representatives to consider any reconciliation bill or reconciliation resolution reported pursuant to a concurrent resolution on the budget agreed to under section 301 or 304 of the Congressional Budget and Impoundment Control Act of 1974, or a joint resolution pursuant to section 258C of the Balanced Budget and Emergency Deficit Control Act of 1985, or any amendment thereto or conference report thereon that\u2014\n**(1)**\nreduces enrollment or benefits for any individual described in subsection (b) enrolled in the Medicaid program under title XIX of the Social Security Act; or\n**(2)**\nreduces eligibility or benefits for households with individuals described in such subsection and that participate in the supplemental nutrition assistance program under the Food and Nutrition Act of 2008.\n##### (b) Individuals described\nAn individual described in this subsection is any of the following:\n**(1)**\nAn individual under the age of 19.\n**(2)**\nAn individual age 65 or older.\n**(3)**\nA pregnant woman.\n**(4)**\nAn individual with a disability (as that term is defined in section 223(d) of the Social Security Act).\n##### (c) Exception\nThe point of order under this section shall not apply to any provision in a reconciliation bill or reconciliation resolution that reduces improper payments, eliminates fraudulent billing, or enhances data verification to ensure eligibility for applicable benefits.",
      "versionDate": "2025-05-05",
      "versionType": "IH"
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
        "updateDate": "2025-06-04T13:31:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-05",
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
          "measure-id": "id119hres382",
          "measure-number": "382",
          "measure-type": "hres",
          "orig-publish-date": "2025-05-05",
          "originChamber": "HOUSE",
          "update-date": "2025-07-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hres382v00",
            "update-date": "2025-07-02"
          },
          "action-date": "2025-05-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This resolution establishes a point of order against considering budget reconciliation legislation in the House during the 119th Congress that (1) reduces enrollment or benefits for specified individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that include specified\u00a0individuals and participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>The\u00a0individuals specified in the bill include individuals who are under the age of 19, individuals who are 65 or older, pregnant women, and individuals with a disability.\u00a0</p><p>The point of order does not apply to any provision in reconciliation legislation\u00a0that reduces improper payments, eliminates fraudulent billing, or enhances data verification to ensure eligibility for applicable benefits.</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p>"
        },
        "title": "Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hres/BILLSUM-119hres382.xml",
    "summary": {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes a point of order against considering budget reconciliation legislation in the House during the 119th Congress that (1) reduces enrollment or benefits for specified individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that include specified\u00a0individuals and participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>The\u00a0individuals specified in the bill include individuals who are under the age of 19, individuals who are 65 or older, pregnant women, and individuals with a disability.\u00a0</p><p>The point of order does not apply to any provision in reconciliation legislation\u00a0that reduces improper payments, eliminates fraudulent billing, or enhances data verification to ensure eligibility for applicable benefits.</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hres382"
    },
    "title": "Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program."
  },
  "summaries": [
    {
      "actionDate": "2025-05-05",
      "actionDesc": "Introduced in House",
      "text": "<p>This resolution establishes a point of order against considering budget reconciliation legislation in the House during the 119th Congress that (1) reduces enrollment or benefits for specified individuals enrolled in the Medicaid program, or (2) reduces eligibility or benefits for households that include specified\u00a0individuals and participate in the Supplemental Nutrition Assistance Program (SNAP).</p><p>The\u00a0individuals specified in the bill include individuals who are under the age of 19, individuals who are 65 or older, pregnant women, and individuals with a disability.\u00a0</p><p>The point of order does not apply to any provision in reconciliation legislation\u00a0that reduces improper payments, eliminates fraudulent billing, or enhances data verification to ensure eligibility for applicable benefits.</p><p>(Under current law, reconciliation bills are considered by Congress using expedited legislative procedures that prevent a filibuster and restrict amendments in the Senate.)</p>",
      "updateDate": "2025-07-02",
      "versionCode": "id119hres382"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres382ih.xml"
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
      "title": "Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T08:18:17Z"
    },
    {
      "title": "Providing a point of order in the House of Representatives during the 119th Congress against reconciliation measures that reduce benefits under the Medicaid program or the supplemental nutrition assistance program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-06T08:05:27Z"
    }
  ]
}
```
