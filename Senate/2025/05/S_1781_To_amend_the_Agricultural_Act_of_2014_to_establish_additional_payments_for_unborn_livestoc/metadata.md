# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1781?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1781
- Title: LIP Enhancement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1781
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2025-12-05T21:45:05Z
- Update date including text: 2025-12-05T21:45:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1781",
    "number": "1781",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "C001098",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Cruz, Ted [R-TX]",
        "lastName": "Cruz",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "LIP Enhancement Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:45:05Z",
    "updateDateIncludingText": "2025-12-05T21:45:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
      "committees": {
        "item": {
          "name": "Agriculture, Nutrition, and Forestry Committee",
          "systemCode": "ssaf00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T16:56:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Agriculture, Nutrition, and Forestry Committee",
      "systemCode": "ssaf00",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1781is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1781\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Cruz (for himself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo amend the Agricultural Act of 2014 to establish additional payments for unborn livestock under the livestock indemnity payment program.\n#### 1. Short title\nThis Act may be cited as the Livestock Indemnity Program Enhancement Act of 2025 or the LIP Enhancement Act of 2025 .\n#### 2. Additional payment for unborn livestock\nSection 1501(b) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(b) ) is amended by adding at the end the following:\n(5) Additional payment for unborn livestock (A) In general In the case of unborn livestock death losses incurred on or after January 1, 2024, the Secretary shall make an additional payment to eligible producers on farms that have incurred such losses in excess of the normal mortality due to a condition specified in paragraph (1). (B) Payment rate Additional payments under subparagraph (A) shall be made at a rate\u2014 (i) determined by the Secretary; and (ii) less than or equal to 85 percent of the payment rate established with respect to the lowest weight class of the livestock, as determined by the Secretary, acting through the Administrator of the Farm Service Agency. (C) Payment amount The amount of a payment to an eligible producer that has incurred unborn livestock death losses shall be equal to the payment rate determined under subparagraph (B) multiplied, in the case of livestock described in\u2014 (i) subparagraph (A), (B), or (F) of subsection (a)(4), by 1; (ii) subparagraph (D) of such subsection, by 2; (iii) subparagraph (E) of such subsection, by 12; and (iv) subparagraph (G) of such subsection, by the average number of birthed animals (for one gestation cycle) for the species of each such livestock, as determined by the Secretary. (D) Unborn livestock death losses defined In this paragraph, the term unborn livestock death losses means losses of any livestock described in subparagraph (A), (B), (D), (E), (F), or (G) of subsection (a)(4) that was gestating on the date of the death of the livestock. .",
      "versionDate": "2025-05-15",
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
        "actionDate": "2025-05-15",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "3448",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "LIP Enhancement Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-10T22:58:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-15",
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
          "measure-id": "id119s1781",
          "measure-number": "1781",
          "measure-type": "s",
          "orig-publish-date": "2025-05-15",
          "originChamber": "SENATE",
          "update-date": "2025-08-05"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1781v00",
            "update-date": "2025-08-05"
          },
          "action-date": "2025-05-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Livestock Indemnity Program Enhancement Act of 2025 or the LIP Enhancement Act of 2025</strong></p><p>This bill expands coverage under the Livestock Indemnity Program (LIP) to include unborn livestock as LIP-eligible livestock losses.</p><p>The bill applies to unborn livestock death losses (i.e., losses of any livestock\u00a0that was gestating on the date of the death of the livestock) incurred on or after January 1, 2024.</p><p>LIP is a Farm Service Agency program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack).</p>"
        },
        "title": "LIP Enhancement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1781.xml",
    "summary": {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Livestock Indemnity Program Enhancement Act of 2025 or the LIP Enhancement Act of 2025</strong></p><p>This bill expands coverage under the Livestock Indemnity Program (LIP) to include unborn livestock as LIP-eligible livestock losses.</p><p>The bill applies to unborn livestock death losses (i.e., losses of any livestock\u00a0that was gestating on the date of the death of the livestock) incurred on or after January 1, 2024.</p><p>LIP is a Farm Service Agency program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack).</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s1781"
    },
    "title": "LIP Enhancement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Livestock Indemnity Program Enhancement Act of 2025 or the LIP Enhancement Act of 2025</strong></p><p>This bill expands coverage under the Livestock Indemnity Program (LIP) to include unborn livestock as LIP-eligible livestock losses.</p><p>The bill applies to unborn livestock death losses (i.e., losses of any livestock\u00a0that was gestating on the date of the death of the livestock) incurred on or after January 1, 2024.</p><p>LIP is a Farm Service Agency program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack).</p>",
      "updateDate": "2025-08-05",
      "versionCode": "id119s1781"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1781is.xml"
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
      "title": "LIP Enhancement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-31T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LIP Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Livestock Indemnity Program Enhancement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-31T03:23:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Agricultural Act of 2014 to establish additional payments for unborn livestock under the livestock indemnity payment program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-31T03:18:21Z"
    }
  ]
}
```
