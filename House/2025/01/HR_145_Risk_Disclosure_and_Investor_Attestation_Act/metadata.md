# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/145?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/145
- Title: Risk Disclosure and Investor Attestation Act
- Congress: 119
- Bill type: HR
- Bill number: 145
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-09-02T18:14:24Z
- Update date including text: 2025-09-02T18:14:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/145",
    "number": "145",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "D000626",
        "district": "8",
        "firstName": "Warren",
        "fullName": "Rep. Davidson, Warren [R-OH-8]",
        "lastName": "Davidson",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Risk Disclosure and Investor Attestation Act",
    "type": "HR",
    "updateDate": "2025-09-02T18:14:24Z",
    "updateDateIncludingText": "2025-09-02T18:14:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:12:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr145ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 145\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Davidson introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the Securities Act of 1933 to permit an individual to invest in private issuers upon acknowledging the investment risks, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Risk Disclosure and Investor Attestation Act .\n#### 2. Investor attestation\n##### (a) In general\nSection 2(a)(15) of the Securities Act of 1933 (77b(a)(15)) is amended\u2014\n**(1)**\nby redesignating clause (i) as subparagraph (A);\n**(2)**\nin subparagraph (A), as so redesignated, by striking or at the end;\n**(3)**\nby redesignating clause (ii) as subparagraph (B);\n**(4)**\nin subparagraph (B), as so redesignated, by striking the period at the end and inserting ; and ; and\n**(5)**\nby adding at the end the following:\n(C) with respect to an issuer, any individual that has attested to the issuer that the individual understands the risks of investment in private issuers, using such form as the Commission shall establish, by rule, but which form may not be longer than 2 pages in length. .\n##### (b) Rulemaking\nNot later than the end of the 1-year period beginning on the date of enactment of this Act, the Securities and Exchange Commission shall issue rules to carry out the amendments made by subsection (a), including establishing the form required under such amendments.",
      "versionDate": "2025-01-03",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Business investment and capital",
            "updateDate": "2025-09-02T18:12:53Z"
          },
          {
            "name": "Financial services and investments",
            "updateDate": "2025-09-02T18:14:24Z"
          },
          {
            "name": "Securities",
            "updateDate": "2025-09-02T18:12:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-03-27T13:38:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr145",
          "measure-number": "145",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-03-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr145v00",
            "update-date": "2025-03-27"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Risk Disclosure and Investor Attestation Act</strong></p><p>This bill expands who may be considered an accredited investor for purposes of participating in private offerings of securities. Certain unregistered securities may only be offered to accredited investors.</p><p>Specifically, the bill allows an individual to qualify by certifying to the issuer of securities that the individual understands the risks of investment in private issuers. Currently, accredited investors must satisfy certain requirements indicating their reduced exposure to financial risk, including those related to income, net worth, or knowledge and experience.</p>"
        },
        "title": "Risk Disclosure and Investor Attestation Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr145.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Risk Disclosure and Investor Attestation Act</strong></p><p>This bill expands who may be considered an accredited investor for purposes of participating in private offerings of securities. Certain unregistered securities may only be offered to accredited investors.</p><p>Specifically, the bill allows an individual to qualify by certifying to the issuer of securities that the individual understands the risks of investment in private issuers. Currently, accredited investors must satisfy certain requirements indicating their reduced exposure to financial risk, including those related to income, net worth, or knowledge and experience.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr145"
    },
    "title": "Risk Disclosure and Investor Attestation Act"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Risk Disclosure and Investor Attestation Act</strong></p><p>This bill expands who may be considered an accredited investor for purposes of participating in private offerings of securities. Certain unregistered securities may only be offered to accredited investors.</p><p>Specifically, the bill allows an individual to qualify by certifying to the issuer of securities that the individual understands the risks of investment in private issuers. Currently, accredited investors must satisfy certain requirements indicating their reduced exposure to financial risk, including those related to income, net worth, or knowledge and experience.</p>",
      "updateDate": "2025-03-27",
      "versionCode": "id119hr145"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr145ih.xml"
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
      "title": "Risk Disclosure and Investor Attestation Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Risk Disclosure and Investor Attestation Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Securities Act of 1933 to permit an individual to invest in private issuers upon acknowledging the investment risks, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:22Z"
    }
  ]
}
```
