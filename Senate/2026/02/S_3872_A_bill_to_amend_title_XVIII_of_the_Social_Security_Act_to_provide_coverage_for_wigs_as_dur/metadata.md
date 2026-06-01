# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3872?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3872
- Title: A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 3872
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-03-30T20:20:13Z
- Update date including text: 2026-03-30T20:20:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3872",
    "number": "3872",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.",
    "type": "S",
    "updateDate": "2026-03-30T20:20:13Z",
    "updateDateIncludingText": "2026-03-30T20:20:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
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
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T19:30:35Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3872is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3872\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Blumenthal introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.\n#### 1. Providing coverage for wigs as durable medical equipment under the Medicare program\n##### (a) In general\nSection 1861(n) of the Social Security Act ( 42 U.S.C. 1395x(n) ) is amended by adding at the end the following new sentence: Such term includes cranial prostheses furnished to an individual, but only where the dermatologist, oncologist, or attending physician of the individual certifies in writing the medical necessity of such prostheses as part of a proposed course of rehabilitative treatment or for hair loss caused by a health condition, including autoimmune diseases, cancer, or chemotherapy. .\n##### (b) Conforming amendment\nSection 1862(a)(1) of the Social Security Act ( 42 U.S.C. 1395y(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (O), by striking and at the end;\n**(2)**\nin subparagraph (P), by striking the semicolon and inserting , and ; and\n**(3)**\nby adding at the end the following new subparagraph:\n(Q) in the case of cranial prostheses (as described in section 1861(n)), which are not certified in the manner described in such section; .",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-02-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7546",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.",
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
        "updateDate": "2026-02-27T16:31:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-12",
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
          "measure-id": "id119s3872",
          "measure-number": "3872",
          "measure-type": "s",
          "orig-publish-date": "2026-02-12",
          "originChamber": "SENATE",
          "update-date": "2026-03-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s3872v00",
            "update-date": "2026-03-30"
          },
          "action-date": "2026-02-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This bill includes medically necessary cranial prostheses (e.g., wigs) as covered durable medical equipment under the Medicare program. </p>"
        },
        "title": "A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s3872.xml",
    "summary": {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill includes medically necessary cranial prostheses (e.g., wigs) as covered durable medical equipment under the Medicare program. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3872"
    },
    "title": "A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes."
  },
  "summaries": [
    {
      "actionDate": "2026-02-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This bill includes medically necessary cranial prostheses (e.g., wigs) as covered durable medical equipment under the Medicare program. </p>",
      "updateDate": "2026-03-30",
      "versionCode": "id119s3872"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3872is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-25T04:48:31Z"
    },
    {
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage for wigs as durable medical equipment under the Medicare program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T11:56:27Z"
    }
  ]
}
```
