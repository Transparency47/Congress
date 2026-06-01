# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2617?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2617
- Title: Reducing Drug Prices for Seniors Act.
- Congress: 119
- Bill type: S
- Bill number: 2617
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-12-02T16:50:04Z
- Update date including text: 2025-12-02T16:50:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2617",
    "number": "2617",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Reducing Drug Prices for Seniors Act.",
    "type": "S",
    "updateDate": "2025-12-02T16:50:04Z",
    "updateDateIncludingText": "2025-12-02T16:50:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T19:26:20Z",
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
      "sponsorshipDate": "2025-07-31",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2617is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2617\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Ms. Rosen (for herself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require that coinsurance for drugs under Medicare part D be based on the drug's net price and not the drug's list price.\n#### 1. Short title\nThis Act may be cited as the Reducing Drug Prices for Seniors Act. .\n#### 2. Requiring that coinsurance for drugs under Medicare part D be based on the drug's net price and not the drug's list price\nSection 1860D\u20132 of the Social Security Act ( 42 U.S.C. 1395w\u2013102 ) is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)(A), in the matter preceding clause (i), by striking and (9) and inserting , (9), and (10) ; and\n**(B)**\nby adding at the end the following new paragraph:\n(10) Requirement that coinsurance for covered part D drugs be based on the net price of the drug (A) In general For plan years beginning on or after January 1, 2026, for costs above the annual deductible specified in paragraph (1) and below the annual out-of-pocket threshold specified in paragraph (4), any coinsurance amount for a covered part D drug (insofar as such covered part D drug is included on the formulary and subject to coinsurance rather than a copayment) shall be calculated based on the net price (and not the list price) of such covered part D drug if such net price is lower than the list price of such covered part D drug. The preceding sentence shall not apply to a covered part D drug described in paragraph (8) or (9). (B) Net price defined In this paragraph, the term net price means, with respect to a covered part D drug, the negotiated price of the covered part D drug under the prescription drug plan or MA\u2013PD plan, net of any manufacturer-provided price concessions (as defined under section 423.100 of title 42, Code of Federal Regulations (or any successor regulation)), as reported for such drug in the Detailed DIR Report (or any successor report) submitted by the sponsor or organization offering the plan for the previous plan year. .\n**(2)**\nin subsection (c), by adding at the end the following new paragraph:\n(7) Requirement that coinsurance for covered part D drugs be based on the net price of the drug The coverage is provided in accordance with subsection (b)(10). .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-02-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1244",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Reducing Drug Prices for Seniors Act",
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
        "updateDate": "2025-09-18T19:18:30Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-31",
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
          "measure-id": "id119s2617",
          "measure-number": "2617",
          "measure-type": "s",
          "orig-publish-date": "2025-07-31",
          "originChamber": "SENATE",
          "update-date": "2025-12-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2617v00",
            "update-date": "2025-12-02"
          },
          "action-date": "2025-07-31",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Reducing Drug Prices for Seniors Act</strong></p><p>This bill requires the coinsurance amount for covered drugs under the Medicare prescription drug benefit to be based on the net price of the drug (i.e., the negotiated price under the prescription drug plan net of any manufacturer price concessions), rather than the list price of the drug, if the net price is lower.</p>"
        },
        "title": "Reducing Drug Prices for Seniors Act."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2617.xml",
    "summary": {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reducing Drug Prices for Seniors Act</strong></p><p>This bill requires the coinsurance amount for covered drugs under the Medicare prescription drug benefit to be based on the net price of the drug (i.e., the negotiated price under the prescription drug plan net of any manufacturer price concessions), rather than the list price of the drug, if the net price is lower.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2617"
    },
    "title": "Reducing Drug Prices for Seniors Act."
  },
  "summaries": [
    {
      "actionDate": "2025-07-31",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Reducing Drug Prices for Seniors Act</strong></p><p>This bill requires the coinsurance amount for covered drugs under the Medicare prescription drug benefit to be based on the net price of the drug (i.e., the negotiated price under the prescription drug plan net of any manufacturer price concessions), rather than the list price of the drug, if the net price is lower.</p>",
      "updateDate": "2025-12-02",
      "versionCode": "id119s2617"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2617is.xml"
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
      "title": "Reducing Drug Prices for Seniors Act.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-09T03:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Reducing Drug Prices for Seniors Act.",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require that coinsurance for drugs under Medicare part D be based on the drug's net price and not the drug's list price.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:34:03Z"
    }
  ]
}
```
