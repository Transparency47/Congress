# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1416?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1416
- Title: Reduction of Excess Business Holding Accrual Act
- Congress: 119
- Bill type: S
- Bill number: 1416
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-14T13:38:28Z
- Update date including text: 2026-01-14T13:38:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1416",
    "number": "1416",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Reduction of Excess Business Holding Accrual Act",
    "type": "S",
    "updateDate": "2026-01-14T13:38:28Z",
    "updateDateIncludingText": "2026-01-14T13:38:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-10",
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
        "item": {
          "date": "2025-04-10T16:12:56Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1416is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1416\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 for purposes of the tax on private foundation excess business holdings to treat as outstanding any employee-owned stock purchased by a business enterprise pursuant to certain employee stock ownership retirement plans.\n#### 1. Short title\nThis Act may be cited as the Reduction of Excess Business Holding Accrual Act .\n#### 2. Certain purchases of employee-owned stock disregarded for purposes of foundation tax on excess business holdings\n##### (a) In general\nSection 4943(c)(4)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clauses:\n(v) For purposes of clause (i), subparagraph (D), and paragraph (2), any voting stock which\u2014 (I) is not readily tradable on an established securities market, (II) is purchased by the business enterprise on or after January 1, 2020, from an employee stock ownership plan (as defined in section 4975(e)(7)) in which employees of such business enterprise participate, in connection with a distribution from such plan, and (III) is held by the business enterprise as treasury stock, cancelled, or retired, shall be treated as outstanding voting stock, but only to the extent so treating such stock would not result in permitted holdings exceeding 49 percent (determined without regard to this clause). The preceding sentence shall not apply with respect to the purchase of stock from a plan during the 10-year period beginning on the date the plan is established. (vi) Clause (ii) shall not apply with respect to any decrease in the percentage of holdings in a business enterprise by reason of the application of clause (v). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2014",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Reduction of Excess Business Holding Accrual Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-12T20:13:40Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
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
          "measure-id": "id119s1416",
          "measure-number": "1416",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1416v00",
            "update-date": "2026-01-14"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>"
        },
        "title": "Reduction of Excess Business Holding Accrual Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1416.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119s1416"
    },
    "title": "Reduction of Excess Business Holding Accrual Act"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119s1416"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1416is.xml"
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
      "title": "Reduction of Excess Business Holding Accrual Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-02T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reduction of Excess Business Holding Accrual Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-02T02:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 for purposes of the tax on private foundation excess business holdings to treat as outstanding any employee-owned stock purchased by a business enterprise pursuant to certain employee stock ownership retirement plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-02T02:18:22Z"
    }
  ]
}
```
