# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/762
- Title: Snap Back Inaccurate SNAP Payments Act
- Congress: 119
- Bill type: HR
- Bill number: 762
- Origin chamber: House
- Introduced date: 2025-01-28
- Update date: 2025-12-05T22:48:05Z
- Update date including text: 2025-12-05T22:48:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-28: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-01-28: Introduced in House

## Actions

- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Introduced in House
- 2025-01-28 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-02-28 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-28",
    "latestAction": {
      "actionDate": "2025-01-28",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/762",
    "number": "762",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000446",
        "district": "4",
        "firstName": "Randy",
        "fullName": "Rep. Feenstra, Randy [R-IA-4]",
        "lastName": "Feenstra",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Snap Back Inaccurate SNAP Payments Act",
    "type": "HR",
    "updateDate": "2025-12-05T22:48:05Z",
    "updateDateIncludingText": "2025-12-05T22:48:05Z"
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
      "actionDate": "2025-01-28",
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
      "actionDate": "2025-01-28",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-28",
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
          "date": "2025-01-28T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-02-28T17:14:59Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr762ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 762\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 28, 2025 Mr. Feenstra (for himself and Mr. Bost ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to improve the calculation and reduce the taxpayer cost of payment errors under the supplemental nutrition assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Snap Back Inaccurate SNAP Payments Act .\n#### 2. Quality control system tolerance level for excluding small errors\nSection 16(c) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2025(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)(ii)\u2014\n**(i)**\nin subclause (I), by striking and at the end;\n**(ii)**\nin subclause (II)\u2014\n**(I)**\nby inserting through fiscal year 2024 after thereafter ; and\n**(II)**\nby striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(III) for fiscal year 2025 and each fiscal year thereafter, $0. ;\n**(B)**\nin subparagraph (C)\u2014\n**(i)**\nin the matter preceding clause (i), by striking may and inserting shall ;\n**(ii)**\nin clause (ii)(I), by inserting , as adjusted under subparagraph (H), if applicable after agency ; and\n**(iii)**\nin clause (iii), by striking 10 and inserting 25 ; and\n**(C)**\nby adding at the end the following:\n(H) Reduction of payment error rate based on percentage of overpayments recouped In determining the liability amount of a State agency under subparagraph (C) for fiscal year 2025 and each fiscal year thereafter, the payment error rate described in clause (ii)(I) of that subparagraph shall be equal to the product obtained by multiplying\u2014 (i) the payment error rate of the State agency for that fiscal year; and (ii) the percentage of the total amount of overpayments of benefits made by the State agency that are not recouped by the State agency under paragraph (9) for that fiscal year. ;\n**(2)**\nby redesignating paragraph (9) as paragraph (10); and\n**(3)**\nby inserting after paragraph (8) the following:\n(9) Recoupment of overpayments Each State agency shall seek to recoup any overpayments of benefits made to benefit recipients. .",
      "versionDate": "2025-01-28",
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
        "actionDate": "2025-01-29",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "302",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Snap Back Inaccurate SNAP Payments Act",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-02-26T21:24:01Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-28",
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
          "measure-id": "id119hr762",
          "measure-number": "762",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-28",
          "originChamber": "HOUSE",
          "update-date": "2025-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr762v00",
            "update-date": "2025-03-03"
          },
          "action-date": "2025-01-28",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Snap Back Inaccurate SNAP Payments Act</strong></p><p>This bill requires states to recoup any overpayments of benefits made to Supplemental Nutrition Assistance Program (SNAP) recipients and adjusts the formula for determining a state's liability rate for overpayments.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. States that have comparatively high payment error rates for two consecutive years are assessed a penalty (i.e., liability amount). The Food and Nutrition Service (FNS) must use a statutory formula to determine the liability amount.</p><p>Under current law, FNS must set a tolerance level for excluding small payment errors in the calculation of payment error rates (e.g., $56 or less in FY2024). This bill reduces the tolerance level for excluding small errors to $0 for FY2025 and each succeeding fiscal year.</p><p>The bill also requires state agencies to recoup any overpayments of benefits made to SNAP beneficiaries.</p><p>The bill adjusts the liability rate formula to reduce the state payment error rate based on the percentage of overpayments recouped by the state. Further, the bill increases the multiplier used in the liability rate\u00a0formula to 25% (from 10%).</p>"
        },
        "title": "Snap Back Inaccurate SNAP Payments Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr762.xml",
    "summary": {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Snap Back Inaccurate SNAP Payments Act</strong></p><p>This bill requires states to recoup any overpayments of benefits made to Supplemental Nutrition Assistance Program (SNAP) recipients and adjusts the formula for determining a state's liability rate for overpayments.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. States that have comparatively high payment error rates for two consecutive years are assessed a penalty (i.e., liability amount). The Food and Nutrition Service (FNS) must use a statutory formula to determine the liability amount.</p><p>Under current law, FNS must set a tolerance level for excluding small payment errors in the calculation of payment error rates (e.g., $56 or less in FY2024). This bill reduces the tolerance level for excluding small errors to $0 for FY2025 and each succeeding fiscal year.</p><p>The bill also requires state agencies to recoup any overpayments of benefits made to SNAP beneficiaries.</p><p>The bill adjusts the liability rate formula to reduce the state payment error rate based on the percentage of overpayments recouped by the state. Further, the bill increases the multiplier used in the liability rate\u00a0formula to 25% (from 10%).</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr762"
    },
    "title": "Snap Back Inaccurate SNAP Payments Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-28",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Snap Back Inaccurate SNAP Payments Act</strong></p><p>This bill requires states to recoup any overpayments of benefits made to Supplemental Nutrition Assistance Program (SNAP) recipients and adjusts the formula for determining a state's liability rate for overpayments.</p><p>As background, the SNAP quality control system measures how accurately SNAP state agencies determine a household\u2019s eligibility and benefit amount and determines overpayments of benefits and underpayments. States that have comparatively high payment error rates for two consecutive years are assessed a penalty (i.e., liability amount). The Food and Nutrition Service (FNS) must use a statutory formula to determine the liability amount.</p><p>Under current law, FNS must set a tolerance level for excluding small payment errors in the calculation of payment error rates (e.g., $56 or less in FY2024). This bill reduces the tolerance level for excluding small errors to $0 for FY2025 and each succeeding fiscal year.</p><p>The bill also requires state agencies to recoup any overpayments of benefits made to SNAP beneficiaries.</p><p>The bill adjusts the liability rate formula to reduce the state payment error rate based on the percentage of overpayments recouped by the state. Further, the bill increases the multiplier used in the liability rate\u00a0formula to 25% (from 10%).</p>",
      "updateDate": "2025-03-03",
      "versionCode": "id119hr762"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr762ih.xml"
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
      "title": "Snap Back Inaccurate SNAP Payments Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-26T05:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Snap Back Inaccurate SNAP Payments Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-26T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to improve the calculation and reduce the taxpayer cost of payment errors under the supplemental nutrition assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-26T05:18:23Z"
    }
  ]
}
```
