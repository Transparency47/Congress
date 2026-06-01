# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/73?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/73
- Title: EMPSA
- Congress: 119
- Bill type: S
- Bill number: 73
- Origin chamber: Senate
- Introduced date: 2025-01-13
- Update date: 2025-02-20T21:13:56Z
- Update date including text: 2025-02-20T21:13:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-13: Introduced in Senate
- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-13: Introduced in Senate

## Actions

- 2025-01-13 - IntroReferral: Introduced in Senate
- 2025-01-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-13",
    "latestAction": {
      "actionDate": "2025-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/73",
    "number": "73",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "EMPSA",
    "type": "S",
    "updateDate": "2025-02-20T21:13:56Z",
    "updateDateIncludingText": "2025-02-20T21:13:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-13",
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
      "actionDate": "2025-01-13",
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
          "date": "2025-01-13T22:50:58Z",
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
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-01-13",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s73is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 73\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2025 Mr. Moran (for himself and Mr. Van Hollen ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVI of the Social Security Act to provide that the supplemental security income benefits of adults with intellectual or developmental disabilities shall not be reduced by reason of marriage.\n#### 1. Short title\nThis Act may be cited as the Eliminating the Marriage Penalty in SSI Act or EMPSA .\n#### 2. Supplemental security income benefits\n##### (a) Eligibility for benefits\nSection 1611(a) of the Social Security Act ( 42 U.S.C. 1382(a) ) is amended by adding at the end the following:\n(4) Notwithstanding paragraphs (1) and (2), each individual\u2014 (A) who has attained 18 years of age, (B) who is diagnosed with an intellectual or developmental disability, (C) whose income, other than income excluded pursuant to section 1612(b), is at a rate of not more than the applicable amount determined under paragraph (1)(A), and (D) whose resources, other than resources excluded pursuant to section 1613(a), are not more than the applicable amount determined under paragraph (3)(B), shall be an eligible individual for purposes of this title. .\n##### (b) Amount of benefit\nSection 1611(b) of such Act ( 42 U.S.C. 1382(b) ) is amended by adding at the end the following:\n(3) Notwithstanding paragraphs (1) and (2), the benefit under this title for an individual described in subsection (a)(4), whether or not the individual has an eligible spouse, shall be payable at the rate in effect for purposes of paragraph (1), reduced by the amount of income, not excluded pursuant to section 1612(b), of such individual. .\n##### (c) Income and resource deeming rules\nSection 1614(f) of such Act ( 42 U.S.C. 1382c(f) ) is amended by adding at the end the following:\n(5) Notwithstanding paragraph (1), for purposes of determining eligibility for, and the amount of, benefits for an individual described in section 1611(a)(4) who is married, such individual's income and resources shall be deemed to not include any income or resources of such spouse. .\n##### (d) Effective date\nThe amendments made by this section shall apply to benefits payable for months that begin more than 180 days after the date of enactment of this Act.",
      "versionDate": "2025-01-13",
      "versionType": "Introduced in Senate"
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
            "name": "Disability and paralysis",
            "updateDate": "2025-02-12T19:37:47Z"
          },
          {
            "name": "Disability assistance",
            "updateDate": "2025-02-12T19:37:42Z"
          },
          {
            "name": "Marriage and family status",
            "updateDate": "2025-02-12T19:37:52Z"
          },
          {
            "name": "Poverty and welfare assistance",
            "updateDate": "2025-02-12T19:37:56Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-02-12T16:34:49Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-13",
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
          "measure-id": "id119s73",
          "measure-number": "73",
          "measure-type": "s",
          "orig-publish-date": "2025-01-13",
          "originChamber": "SENATE",
          "update-date": "2025-02-20"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s73v00",
            "update-date": "2025-02-20"
          },
          "action-date": "2025-01-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Eliminating the Marriage Penalty in SSI Act or EMPSA</strong></p><p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>"
        },
        "title": "EMPSA"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s73.xml",
    "summary": {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Eliminating the Marriage Penalty in SSI Act or EMPSA</strong></p><p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119s73"
    },
    "title": "EMPSA"
  },
  "summaries": [
    {
      "actionDate": "2025-01-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Eliminating the Marriage Penalty in SSI Act or EMPSA</strong></p><p>This bill excludes a spouse's income and resources when determining eligibility for Supplemental Security Income (SSI), and disregards marital status when calculating the SSI benefit amount, for an adult who has a diagnosed intellectual or developmental disability. (SSI is a federal income supplement program designed to help aged, blind, and disabled individuals with limited income and resources meet basic needs.)</p>",
      "updateDate": "2025-02-20",
      "versionCode": "id119s73"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s73is.xml"
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
      "title": "EMPSA",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "EMPSA",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Eliminating the Marriage Penalty in SSI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVI of the Social Security Act to provide that the supplemental security income benefits of adults with intellectual or developmental disabilities shall not be reduced by reason of marriage.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:36Z"
    }
  ]
}
```
