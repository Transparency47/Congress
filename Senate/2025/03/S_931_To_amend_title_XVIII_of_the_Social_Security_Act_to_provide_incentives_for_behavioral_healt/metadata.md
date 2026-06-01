# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/931?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/931
- Title: COMPLETE Care Act
- Congress: 119
- Bill type: S
- Bill number: 931
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-02-19T22:26:08Z
- Update date including text: 2026-02-19T22:26:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/931",
    "number": "931",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "COMPLETE Care Act",
    "type": "S",
    "updateDate": "2026-02-19T22:26:08Z",
    "updateDateIncludingText": "2026-02-19T22:26:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T15:59:52Z",
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
      "sponsorshipDate": "2025-03-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s931is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 931\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Ms. Cortez Masto (for herself and Mr. Cornyn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide incentives for behavioral health integration.\n#### 1. Short title\nThis Act may be cited as the Connecting Our Medical Providers with Links to Expand Tailored and Effective Care or the COMPLETE Care Act .\n#### 2. Medicare incentives for behavioral health integration with primary care\n##### (a) Incentives\n**(1) In general**\nSection 1848(b) of the Social Security Act ( 42 U.S.C. 1395w\u20134(b) ) is amended by adding at the end the following new paragraph:\n(13) Incentives for behavioral health integration (A) In general For services described in subparagraph (B) that are furnished during 2027, 2028, or 2029, instead of the payment amount that would otherwise be determined under this section for such year, the payment amount shall be equal to the applicable percent (as defined in subparagraph (C)) of such payment amount for such year. (B) Services described The services described in this subparagraph are services identified, as of January 1, 2024, by HCPCS codes 99484, 99492, 99493, 99494, G2214, and G0323 (and any successor or similar codes as determined appropriate by the Secretary). (C) Applicable percent In this paragraph, the term applicable percent means, with respect to a service described in subparagraph (A), the following: (i) For services furnished during 2027 , 175 percent. (ii) For services furnished during 2028, 150 percent. (iii) For services furnished during 2029, 125 percent. .\n**(2) Waiver of budget neutrality**\nSection 1848(c)(2)(B)(iv) of such Act ( 42 U.S.C. 1395w\u20134(c)(2)(B)(iv) ) is amended\u2014\n**(A)**\nin subclause (V), by striking and at the end;\n**(B)**\nin subclause (VI), by striking the period at the end and inserting ; and and\n**(C)**\nby adding at the end the following new subclause:\n(VII) the increase in payment amounts as a result of the application of subsection (b)(13) shall not be taken into account in applying clause (ii)(II) for 2027, 2028, or 2029. .\n##### (b) Technical assistance for the adoption of behavioral health integration\n**(1) In general**\nNot later than January 1, 2026, the Secretary of Health and Human Services (in this subsection referred to as the Secretary ) shall enter into contracts or agreements with appropriate entities to offer technical assistance to primary care practices that are seeking to adopt behavioral health integration models in such practices.\n**(2) Behavioral health integration models**\nFor purposes of paragraph (1), behavioral health integration models include the Collaborative Care Model (with services identified as of January 1, 2024, by HCPCS codes 99492, 99493, 99494, and G2214 (and any successor codes)), the Primary Care Behavioral Health model (with services identified as of January 1, 2024, by HCPCS codes 99484 and G0323 (and any successor code)), and other models identified by the Secretary.\n**(3) Implementation**\nNotwithstanding any other provision of law, the Secretary may implement the provisions of this subsection by program instruction or otherwise.\n**(4) Funding**\nIn addition to amounts otherwise available, there is appropriated to the Secretary for each of fiscal years 2025 through 2029, out of any money in the Treasury not otherwise appropriated, such sums as are necessary, to remain available until expended, for purposes of carrying out this subsection.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-31",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2509",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "COMPLETE Care Act",
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
        "updateDate": "2025-03-31T15:45:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s931",
          "measure-number": "931",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s931v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Connecting Our Medical Providers with Links to Expand Tailored and Effective Care or the COMPLETE Care Act</strong></p><p>This bill increases payments and establishes certain requirements\u00a0to support integrated behavioral health services under Medicare.</p><p>Specifically, the bill increases payments for integrated behavioral health services that are provided by physicians under Medicare for 2027-2029, with payments increased by 175% in 2027, 150% in 2028, and 125% in 2029.</p><p>The bill provides funds for FY2025-FY2029 for the Centers for Medicare & Medicaid Services to contract with entities to provide technical assistance to primary care practices that want to adopt models for behavioral health integration.</p>"
        },
        "title": "COMPLETE Care Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s931.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Connecting Our Medical Providers with Links to Expand Tailored and Effective Care or the COMPLETE Care Act</strong></p><p>This bill increases payments and establishes certain requirements\u00a0to support integrated behavioral health services under Medicare.</p><p>Specifically, the bill increases payments for integrated behavioral health services that are provided by physicians under Medicare for 2027-2029, with payments increased by 175% in 2027, 150% in 2028, and 125% in 2029.</p><p>The bill provides funds for FY2025-FY2029 for the Centers for Medicare & Medicaid Services to contract with entities to provide technical assistance to primary care practices that want to adopt models for behavioral health integration.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s931"
    },
    "title": "COMPLETE Care Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Connecting Our Medical Providers with Links to Expand Tailored and Effective Care or the COMPLETE Care Act</strong></p><p>This bill increases payments and establishes certain requirements\u00a0to support integrated behavioral health services under Medicare.</p><p>Specifically, the bill increases payments for integrated behavioral health services that are provided by physicians under Medicare for 2027-2029, with payments increased by 175% in 2027, 150% in 2028, and 125% in 2029.</p><p>The bill provides funds for FY2025-FY2029 for the Centers for Medicare & Medicaid Services to contract with entities to provide technical assistance to primary care practices that want to adopt models for behavioral health integration.</p>",
      "updateDate": "2026-02-19",
      "versionCode": "id119s931"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s931is.xml"
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
      "title": "COMPLETE Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-29T02:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "COMPLETE Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Connecting Our Medical Providers with Links to Expand Tailored and Effective Care",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide incentives for behavioral health integration.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:54Z"
    }
  ]
}
```
