# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/131
- Title: A resolution designating the third week of March 2025 as "National CACFP Week".
- Congress: 119
- Bill type: SRES
- Bill number: 131
- Origin chamber: Senate
- Introduced date: 2025-03-14
- Update date: 2026-03-27T21:36:53Z
- Update date including text: 2026-03-27T21:36:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in Senate
- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-03-14 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1785; text: CR S1783)
- Latest action: 2025-03-14: Introduced in Senate

## Actions

- 2025-03-14 - IntroReferral: Introduced in Senate
- 2025-03-14 - Floor: Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.
- 2025-03-14 - Floor: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1785; text: CR S1783)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/131",
    "number": "131",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001236",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Boozman, John [R-AR]",
        "lastName": "Boozman",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "A resolution designating the third week of March 2025 as \"National CACFP Week\".",
    "type": "SRES",
    "updateDate": "2026-03-27T21:36:53Z",
    "updateDateIncludingText": "2026-03-27T21:36:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1785; text: CR S1783)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-14",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-14",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres131ats.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 131\nIN THE SENATE OF THE UNITED STATES\nMarch 14, 2025 Mr. Boozman (for himself and Ms. Klobuchar ) submitted the following resolution; which was considered and agreed to\nRESOLUTION\nDesignating the third week of March 2025 as National CACFP Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week beginning on March 16, 2025, as National CACFP Week ; and\n**(2)**\nrecognizes the role of the Child and Adult Care Food Program in improving the health of the most vulnerable children and adults in child care centers, family day care homes, emergency shelters, adult day care facilities, and after-school care in the United States by providing nutritious meals and snacks.",
      "versionDate": "2025-03-14",
      "versionType": "ATS"
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
        "actionDate": "2026-03-22",
        "text": "Submitted in the Senate, considered, and agreed to without amendment and with a preamble by Unanimous Consent. (consideration: CR S1523; text: CR S1517-1518)"
      },
      "number": "656",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A resolution designating the third week of March 2026 as \"National CACFP Week\".",
      "type": "SRES"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commemorative events and holidays",
            "updateDate": "2025-05-19T20:22:39Z"
          },
          {
            "name": "Food assistance and relief",
            "updateDate": "2025-05-19T20:25:43Z"
          },
          {
            "name": "Nutrition and diet",
            "updateDate": "2025-05-19T20:31:15Z"
          }
        ]
      },
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-05-19T15:26:32Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119sres131",
          "measure-number": "131",
          "measure-type": "sres",
          "orig-publish-date": "2025-03-14",
          "originChamber": "SENATE",
          "update-date": "2025-05-22"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119sres131v00",
            "update-date": "2025-05-22"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p>This resolution designates the week beginning on March 16, 2025, as National CACFP Week. It also recognizes the role of the Child and Adult Care Food Program (CACFP) in improving the health of the children and adults in child care centers, family day care homes, emergency shelters, adult day care facilities, and after-school care in the United States by providing nutritious meals and snacks.</p>"
        },
        "title": "A resolution designating the third week of March 2025 as \"National CACFP Week\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/sres/BILLSUM-119sres131.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates the week beginning on March 16, 2025, as National CACFP Week. It also recognizes the role of the Child and Adult Care Food Program (CACFP) in improving the health of the children and adults in child care centers, family day care homes, emergency shelters, adult day care facilities, and after-school care in the United States by providing nutritious meals and snacks.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119sres131"
    },
    "title": "A resolution designating the third week of March 2025 as \"National CACFP Week\"."
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in Senate",
      "text": "<p>This resolution designates the week beginning on March 16, 2025, as National CACFP Week. It also recognizes the role of the Child and Adult Care Food Program (CACFP) in improving the health of the children and adults in child care centers, family day care homes, emergency shelters, adult day care facilities, and after-school care in the United States by providing nutritious meals and snacks.</p>",
      "updateDate": "2025-05-22",
      "versionCode": "id119sres131"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres131ats.xml"
        }
      ],
      "type": "ATS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "A resolution designating the third week of March 2025 as \"National CACFP Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-15T10:56:18Z"
    },
    {
      "title": "A resolution designating the third week of March 2025 as \"National CACFP Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-15T10:56:18Z"
    }
  ]
}
```
