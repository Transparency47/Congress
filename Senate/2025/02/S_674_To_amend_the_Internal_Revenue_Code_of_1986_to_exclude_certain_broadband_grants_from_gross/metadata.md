# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/674?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/674
- Title: Broadband Grant Tax Treatment Act
- Congress: 119
- Bill type: S
- Bill number: 674
- Origin chamber: Senate
- Introduced date: 2025-02-20
- Update date: 2026-01-23T19:02:56Z
- Update date including text: 2026-01-23T19:02:56Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-20: Introduced in Senate
- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-20: Introduced in Senate

## Actions

- 2025-02-20 - IntroReferral: Introduced in Senate
- 2025-02-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-20",
    "latestAction": {
      "actionDate": "2025-02-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/674",
    "number": "674",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "Broadband Grant Tax Treatment Act",
    "type": "S",
    "updateDate": "2026-01-23T19:02:56Z",
    "updateDateIncludingText": "2026-01-23T19:02:56Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-20",
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
      "actionDate": "2025-02-20",
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
          "date": "2025-02-20T22:09:00Z",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "AK"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "VA"
    },
    {
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "AL"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "AZ"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "WV"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2025-02-20",
      "state": "ME"
    },
    {
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "MS"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-02-20",
      "state": "GA"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "ND"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-02-20",
      "state": "NE"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "False",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "WI"
    },
    {
      "bioguideId": "M001153",
      "firstName": "Lisa",
      "fullName": "Sen. Murkowski, Lisa [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Murkowski",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "AK"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "False",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "ID"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s674is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 674\nIN THE SENATE OF THE UNITED STATES\nFebruary 20, 2025 Mr. Moran (for himself, Mr. Warner , Mr. Sullivan , Mr. Kaine , Mr. Tuberville , Mr. Kelly , Mrs. Capito , Mr. King , Mr. Wicker , Mr. Warnock , Mr. Cramer , and Mrs. Fischer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain broadband grants from gross income.\n#### 1. Short title\nThis Act may be cited as the Broadband Grant Tax Treatment Act .\n#### 2. Certain grants for broadband excluded from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new subsection:\n139J. Certain broadband grants (a) In general Gross income shall not include any qualified broadband grant made for purposes of broadband deployment. (b) Denial of double benefit Notwithstanding any other provision of this subtitle, no deduction or credit shall be allowed for, or by reason of, any expenditure to the extent of the amount excluded under subsection (a) for any qualified broadband grant which was provided with respect to such expenditure. The adjusted basis of any property shall be reduced by the amount excluded under subsection (a) which was provided with respect to such property. (c) Qualified broadband grant For purposes of this section, the term qualified broadband grant means\u2014 (1) any grant or subgrant received under the Broadband Equity, Access, and Deployment Program established under section 60102 of the Infrastructure Investment and Jobs Act, (2) any grant or subgrant received under the State Digital Equity Capacity Grant Program established under section 60304 of such Act, (3) any grant received under the Digital Equity Competitive Grant Program established under section 60305 of such Act, (4) any grant received under section 60401 of such Act (relating to middle mile grants), (5) any grant received\u2014 (A) under the broadband loan and grant pilot program established by section 779 of Public Law 115\u2013141 under the Rural Electrification Act of 1936; and (B) from funds made available for such program under the heading Distance Learning, Telemedicine, and Broadband Program under the heading Rural Utilities Service under title I of division J of the Infrastructure Investment and Jobs Act, (6) any grant received from a State, territory, Tribal government, or unit of local government to the extent such grant was\u2014 (A) funded by amounts provided to the State or local government under section 602, 603, or 604 of the Social Security Act, and (B) provided for the stated purposes of making investments in broadband infrastructure, or (7) any grant or subgrant received under section 905 of division N of the Consolidated Appropriations Act, 2021. (d) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item related to section 139I the following new item:\nSec. 139J. Certain broadband grants. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received in taxable years ending after March 11, 2021.",
      "versionDate": "2025-02-20",
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
        "actionDate": "2025-03-05",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1873",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Broadband Grant Tax Treatment Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-06T14:20:57Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-20",
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
          "measure-id": "id119s674",
          "measure-number": "674",
          "measure-type": "s",
          "orig-publish-date": "2025-02-20",
          "originChamber": "SENATE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s674v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-02-20",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2021.</p>"
        },
        "title": "Broadband Grant Tax Treatment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s674.xml",
    "summary": {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2021.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s674"
    },
    "title": "Broadband Grant Tax Treatment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-20",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2021.</p>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s674"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s674is.xml"
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
      "title": "Broadband Grant Tax Treatment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T11:03:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Broadband Grant Tax Treatment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude certain broadband grants from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:18:42Z"
    }
  ]
}
```
