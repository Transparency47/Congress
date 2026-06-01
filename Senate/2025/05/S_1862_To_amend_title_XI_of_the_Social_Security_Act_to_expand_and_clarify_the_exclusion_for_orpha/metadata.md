# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1862?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1862
- Title: ORPHAN Cures Act
- Congress: 119
- Bill type: S
- Bill number: 1862
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-12-05T21:54:24Z
- Update date including text: 2025-12-05T21:54:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S3119)
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S3119)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1862",
    "number": "1862",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "ORPHAN Cures Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:24Z",
    "updateDateIncludingText": "2025-12-05T21:54:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S3119)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T15:15:07Z",
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
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-22",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1862is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1862\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Barrasso (for himself and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XI of the Social Security Act to expand and clarify the exclusion for orphan drugs under the Drug Price Negotiation Program.\n#### 1. Short title\nThis Act may be cited as the Optimizing Research Progress Hope And New Cures Act or the ORPHAN Cures Act .\n#### 2. Expanding and clarifying the exclusion for orphan drugs under the Drug Price Negotiation Program\nSection 1192(e) of the Social Security Act ( 42 U.S.C. 1320f\u20131(e) ) is amended\u2014\n**(1)**\nin paragraph (1), by adding at the end the following new subparagraph:\n(C) Treatment of former orphan drugs In calculating the amount of time that has elapsed with respect to the approval of a drug or licensure of a biological product under subparagraph (A)(ii) and subparagraph (B)(ii), respectively, the Secretary shall not take into account any period during which such drug or product was a drug described in paragraph (3)(A). ; and\n**(2)**\nin paragraph (3)(A)\u2014\n**(A)**\nby striking only one rare disease or condition and inserting one or more rare diseases or conditions ; and\n**(B)**\nby striking such disease or condition and inserting one or more rare diseases or conditions (as such term is defined in section 526(a)(2) of the Federal Food, Drug, and Cosmetic Act) .",
      "versionDate": "2025-05-22",
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
        "actionDate": "2025-02-06",
        "text": "Sponsor introductory remarks on measure. (CR H535-536)"
      },
      "number": "946",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ORPHAN Cures Act",
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
        "updateDate": "2025-06-13T13:42:46Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-22",
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
          "measure-id": "id119s1862",
          "measure-number": "1862",
          "measure-type": "s",
          "orig-publish-date": "2025-05-22",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1862v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-05-22",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Optimizing Research Progress Hope And New Cures Act or the ORPHAN Cures Act</strong></p><p>This bill modifies certain provisions under the Medicare Drug Price Negotiation Program with respect to orphan drugs.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation. The program does not apply to orphan drugs that are approved to treat only one rare disease or condition.</p><p>The bill modifies these provisions so as to exclude any period in which a drug was an orphan drug from market approval calculations. It also excludes orphan drugs that are approved to treat more than one rare disease or condition from the program.</p>"
        },
        "title": "ORPHAN Cures Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1862.xml",
    "summary": {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Optimizing Research Progress Hope And New Cures Act or the ORPHAN Cures Act</strong></p><p>This bill modifies certain provisions under the Medicare Drug Price Negotiation Program with respect to orphan drugs.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation. The program does not apply to orphan drugs that are approved to treat only one rare disease or condition.</p><p>The bill modifies these provisions so as to exclude any period in which a drug was an orphan drug from market approval calculations. It also excludes orphan drugs that are approved to treat more than one rare disease or condition from the program.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1862"
    },
    "title": "ORPHAN Cures Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-22",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Optimizing Research Progress Hope And New Cures Act or the ORPHAN Cures Act</strong></p><p>This bill modifies certain provisions under the Medicare Drug Price Negotiation Program with respect to orphan drugs.</p><p>The Medicare Drug Price Negotiation Program requires the Centers for Medicare & Medicaid Services to negotiate the prices of certain prescription drugs under Medicare beginning in 2026. Among other requirements, drugs must have had market approval for at least 7 years (for drug products) or 11 years (for biologics) to qualify for negotiation. The program does not apply to orphan drugs that are approved to treat only one rare disease or condition.</p><p>The bill modifies these provisions so as to exclude any period in which a drug was an orphan drug from market approval calculations. It also excludes orphan drugs that are approved to treat more than one rare disease or condition from the program.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s1862"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1862is.xml"
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
      "title": "ORPHAN Cures Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ORPHAN Cures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Optimizing Research Progress Hope And New Cures Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XI of the Social Security Act to expand and clarify the exclusion for orphan drugs under the Drug Price Negotiation Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:22Z"
    }
  ]
}
```
