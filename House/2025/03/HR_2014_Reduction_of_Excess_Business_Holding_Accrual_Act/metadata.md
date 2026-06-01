# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2014?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2014
- Title: Reduction of Excess Business Holding Accrual Act
- Congress: 119
- Bill type: HR
- Bill number: 2014
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2026-01-14T11:53:45Z
- Update date including text: 2026-01-14T11:53:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2014",
    "number": "2014",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001214",
        "district": "17",
        "firstName": "W.",
        "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
        "lastName": "Steube",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Reduction of Excess Business Holding Accrual Act",
    "type": "HR",
    "updateDate": "2026-01-14T11:53:45Z",
    "updateDateIncludingText": "2026-01-14T11:53:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:04:25Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2014ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2014\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Steube introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 for purposes of the tax on private foundation excess business holdings to treat as outstanding any employee-owned stock purchased by a business enterprise pursuant to certain employee stock ownership retirement plans.\n#### 1. Short title\nThis Act may be cited as the Reduction of Excess Business Holding Accrual Act .\n#### 2. Certain purchases of employee-owned stock disregarded for purposes of foundation tax on excess business holdings\n##### (a) In general\nSection 4943(c)(4)(A) of the Internal Revenue Code of 1986 is amended by adding at the end the following new clauses:\n(v) For purposes of clause (i), subparagraph (D), and paragraph (2), any voting stock which\u2014 (I) is not readily tradable on an established securities market, (II) is purchased by the business enterprise on or after January 1, 2020, from an employee stock ownership plan (as defined in section 4975(e)(7)) in which employees of such business enterprise participate, in connection with a distribution from such plan, and (III) is held by the business enterprise as treasury stock, cancelled, or retired, shall be treated as outstanding voting stock, but only to the extent so treating such stock would not result in permitted holdings exceeding 49 percent (determined without regard to this clause). The preceding sentence shall not apply with respect to the purchase of stock from a plan during the 10-year period beginning on the date the plan is established. (vi) Section 4943(c)(4)(A)(ii) shall not apply with respect to any decrease in the percentage of holdings in a business enterprise by reason of the application of clause (v). .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years ending after the date of the enactment of this Act and to purchases by a business enterprise of voting stock in taxable years beginning after December 31, 2019.",
      "versionDate": "2025-03-10",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1416",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Reduction of Excess Business Holding Accrual Act",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-08T18:56:54Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-10",
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
          "measure-id": "id119hr2014",
          "measure-number": "2014",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-10",
          "originChamber": "HOUSE",
          "update-date": "2026-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2014v00",
            "update-date": "2026-01-14"
          },
          "action-date": "2025-03-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>"
        },
        "title": "Reduction of Excess Business Holding Accrual Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2014.xml",
    "summary": {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr2014"
    },
    "title": "Reduction of Excess Business Holding Accrual Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Reduction of Excess Business Holding Accrual Act</strong></p><p>This bill treats certain stock repurchased by a corporation from an employee stock ownership plan (ESOP) as outstanding voting stock for purposes of the federal excise tax imposed on a private foundation\u2019s excess business holdings. Thus, a private foundation may exclude such stock in calculating present holdings in a corporation and liability for the excise tax. (Exceptions apply.)</p><p>As background, a federal excise tax is imposed on a private foundation that owns\u00a0more than 20% of the voting stock in a corporation, reduced by the percentage of voting stock held by all disqualified persons (excess business holdings). However, a private foundation with excess business holdings on May 26, 1969 (grandfathered private foundation) may own a greater percentage of voting stock in certain circumstances. </p><p>Under the bill, stock is treated as outstanding voting stock if such stock is</p><ul><li>not readily tradable on an established securities market;</li><li>repurchased from an ESOP on or after January 1, 2020; and</li><li>held by the corporation\u00a0as treasury stock, cancelled, or retired.</li></ul><p>However, such stock is not treated as outstanding voting stock if it is repurchased within the first 10 years of establishing the ESOP or, as a result of the repurchase, the permitted holdings of the private foundation would exceed 49% of the voting stock in the corporation.</p><p>Finally, under the bill, such stock does not reduce the percentage of voting stock a grandfathered private foundation may own.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119hr2014"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2014ih.xml"
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
      "title": "Reduction of Excess Business Holding Accrual Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-26T05:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Reduction of Excess Business Holding Accrual Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-26T05:53:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 for purposes of the tax on private foundation excess business holdings to treat as outstanding any employee-owned stock purchased by a business enterprise pursuant to certain employee stock ownership retirement plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-26T05:48:39Z"
    }
  ]
}
```
