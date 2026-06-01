# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1222
- Title: Financial Freedom Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1222
- Origin chamber: Senate
- Introduced date: 2025-04-01
- Update date: 2025-12-05T21:58:46Z
- Update date including text: 2025-12-05T21:58:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-01: Introduced in Senate
- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-04-01: Introduced in Senate

## Actions

- 2025-04-01 - IntroReferral: Introduced in Senate
- 2025-04-01 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-01",
    "latestAction": {
      "actionDate": "2025-04-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1222",
    "number": "1222",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Financial Freedom Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:58:46Z",
    "updateDateIncludingText": "2025-12-05T21:58:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-01",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-04-01",
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
          "date": "2025-04-01T16:38:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WY"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "WV"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-04-01",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1222is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1222\nIN THE SENATE OF THE UNITED STATES\nApril 1 (legislative day, March 31), 2025 Mr. Tuberville (for himself, Ms. Lummis , Mr. Justice , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit the Secretary of Labor from constraining the range or type of investments that may be offered to participants and beneficiaries of individual retirement accounts who exercise control over the assets in such accounts.\n#### 1. Short title\nThis Act may be cited as the Financial Freedom Act of 2025 .\n#### 2. Fiduciary duties with respect to pension plan investments\nSection 404(a) of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1104(a) ) is amended by adding at the end the following:\n(3) (A) In the case of a pension plan that provides for individual accounts and permits a participant or beneficiary to exercise control over the assets in the participant's or beneficiary's account, nothing in paragraph (1)\u2014 (i) requires a fiduciary to select, or prohibits a fiduciary from selecting, any particular type of investment alternative, provided that a fiduciary provides the participant or beneficiary an opportunity to choose, from a broad range of investment alternatives, the manner in which some or all of the assets of the participant's or beneficiary's account are invested, according to regulations prescribed by the Secretary; or (ii) requires that any particular type of investment be either favored or disfavored, other than on the basis of the investment\u2019s risk-return characteristics, in the context of the plan fiduciary\u2019s objective of providing investment alternatives suitable for providing benefits for participants and beneficiaries. (B) In the event that a fiduciary selects a self-directed brokerage window as an investment alternative for a plan described in subparagraph (A)\u2014 (i) the Secretary shall not issue any regulations or subregulatory guidance constraining or prohibiting the range or type of investments that may be offered through such brokerage window; (ii) subsection (c) shall apply to such self-directed brokerage window; and (iii) the diversification requirement of paragraph (1)(C) and the prudence requirement of paragraph (1)(B) are not violated by the fiduciary\u2019s selection of a self-directed brokerage window as an investment alternative or as a result of the exercise of a participant or beneficiary\u2019s control over the assets in such self-directed brokerage window. .",
      "versionDate": "2025-04-01",
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
        "actionDate": "2025-04-01",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "2544",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Financial Freedom Act of 2025",
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
        "name": "Labor and Employment",
        "updateDate": "2025-04-11T12:45:53Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-01",
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
          "measure-id": "id119s1222",
          "measure-number": "1222",
          "measure-type": "s",
          "orig-publish-date": "2025-04-01",
          "originChamber": "SENATE",
          "update-date": "2025-06-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1222v00",
            "update-date": "2025-06-26"
          },
          "action-date": "2025-04-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Financial Freedom Act of 2025</strong></p><p>This bill prohibits the Department of Labor from limiting the type or range of investments that fiduciaries may offer participants and beneficiaries in certain employer-sponsored retirement plans. The bill applies to certain defined contribution plans that permit participants or beneficiaries to exercise control over the assets in the account, such as a 401(k) plan that allows participants or beneficiaries to select additional investment options through a self-directed brokerage window.</p>"
        },
        "title": "Financial Freedom Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1222.xml",
    "summary": {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Freedom Act of 2025</strong></p><p>This bill prohibits the Department of Labor from limiting the type or range of investments that fiduciaries may offer participants and beneficiaries in certain employer-sponsored retirement plans. The bill applies to certain defined contribution plans that permit participants or beneficiaries to exercise control over the assets in the account, such as a 401(k) plan that allows participants or beneficiaries to select additional investment options through a self-directed brokerage window.</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119s1222"
    },
    "title": "Financial Freedom Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Financial Freedom Act of 2025</strong></p><p>This bill prohibits the Department of Labor from limiting the type or range of investments that fiduciaries may offer participants and beneficiaries in certain employer-sponsored retirement plans. The bill applies to certain defined contribution plans that permit participants or beneficiaries to exercise control over the assets in the account, such as a 401(k) plan that allows participants or beneficiaries to select additional investment options through a self-directed brokerage window.</p>",
      "updateDate": "2025-06-26",
      "versionCode": "id119s1222"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1222is.xml"
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
      "title": "Financial Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-11T02:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Financial Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-11T02:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit the Secretary of Labor from constraining the range or type of investments that may be offered to participants and beneficiaries of individual retirement accounts who exercise control over the assets in such accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-11T02:33:24Z"
    }
  ]
}
```
