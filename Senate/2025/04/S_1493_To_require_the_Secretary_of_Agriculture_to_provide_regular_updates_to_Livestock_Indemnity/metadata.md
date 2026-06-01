# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1493?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1493
- Title: Livestock Indemnity Program Improvement Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1493
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2026-01-14T14:07:08Z
- Update date including text: 2026-01-14T14:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1493",
    "number": "1493",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Livestock Indemnity Program Improvement Act of 2025",
    "type": "S",
    "updateDate": "2026-01-14T14:07:08Z",
    "updateDateIncludingText": "2026-01-14T14:07:08Z"
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
          "date": "2025-04-11T02:38:01Z",
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
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1493is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1493\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Rounds (for himself and Mr. Bennet ) introduced the following bill; which was read twice and referred to the Committee on Agriculture, Nutrition, and Forestry\nA BILL\nTo require the Secretary of Agriculture to provide regular updates to Livestock Indemnity Program payment rates to reflect market prices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Livestock Indemnity Program Improvement Act of 2025 .\n#### 2. Livestock indemnity payments\nSection 1501(b)(2) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(b)(2) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A) and (B) as clauses (i) and (ii), respectively, and indenting appropriately;\n**(2)**\nin the matter preceding clause (i) (as so designated), by striking Indemnity and inserting the following:\n(A) In general Indemnity ; and\n**(3)**\nby adding at the end the following:\n(B) Determination of market value The Secretary shall determine the market value described in subparagraph (A)\u2014 (i) in coordination with the Administrator of the Agricultural Marketing Service; (ii) using other appropriate resources, as determined by the Secretary; and (iii) on a quarterly basis. .",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "4322",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Livestock Indemnity Program Improvement Act of 2025",
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
        "updateDate": "2025-05-07T13:38:49Z"
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
          "measure-id": "id119s1493",
          "measure-number": "1493",
          "measure-type": "s",
          "orig-publish-date": "2025-04-10",
          "originChamber": "SENATE",
          "update-date": "2026-01-14"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1493v00",
            "update-date": "2026-01-14"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Livestock Indemnity Program Improvement Act of 2025</strong></p><p>This bill requires the Farm Service Agency (FSA) to update the market value for livestock on a quarterly basis for the purposes of determining Livestock Indemnity Program (LIP) payment rates. The FSA must determine the market value in coordination with the Agricultural Marketing Service and use other appropriate resources.</p><p>As background, LIP\u00a0is an FSA program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack). In general, the rate of payment is 75% of the market value of the affected livestock.</p>"
        },
        "title": "Livestock Indemnity Program Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1493.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Livestock Indemnity Program Improvement Act of 2025</strong></p><p>This bill requires the Farm Service Agency (FSA) to update the market value for livestock on a quarterly basis for the purposes of determining Livestock Indemnity Program (LIP) payment rates. The FSA must determine the market value in coordination with the Agricultural Marketing Service and use other appropriate resources.</p><p>As background, LIP\u00a0is an FSA program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack). In general, the rate of payment is 75% of the market value of the affected livestock.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119s1493"
    },
    "title": "Livestock Indemnity Program Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Livestock Indemnity Program Improvement Act of 2025</strong></p><p>This bill requires the Farm Service Agency (FSA) to update the market value for livestock on a quarterly basis for the purposes of determining Livestock Indemnity Program (LIP) payment rates. The FSA must determine the market value in coordination with the Agricultural Marketing Service and use other appropriate resources.</p><p>As background, LIP\u00a0is an FSA program that provides indemnity payments to eligible livestock owners and contract growers for livestock deaths in excess of normal mortality or reduced sales prices due to specified events (e.g., adverse weather, disease, or animal attack). In general, the rate of payment is 75% of the market value of the affected livestock.</p>",
      "updateDate": "2026-01-14",
      "versionCode": "id119s1493"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1493is.xml"
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
      "title": "Livestock Indemnity Program Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-03T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Livestock Indemnity Program Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Agriculture to provide regular updates to Livestock Indemnity Program payment rates to reflect market prices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:47Z"
    }
  ]
}
```
