# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1873
- Title: Broadband Grant Tax Treatment Act
- Congress: 119
- Bill type: HR
- Bill number: 1873
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2026-05-08T08:06:47Z
- Update date including text: 2026-05-08T08:06:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1873",
    "number": "1873",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000376",
        "district": "16",
        "firstName": "Mike",
        "fullName": "Rep. Kelly, Mike [R-PA-16]",
        "lastName": "Kelly",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Broadband Grant Tax Treatment Act",
    "type": "HR",
    "updateDate": "2026-05-08T08:06:47Z",
    "updateDateIncludingText": "2026-05-08T08:06:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-03-05",
      "state": "CA"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-31",
      "state": "NC"
    },
    {
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-04-17",
      "state": "GA"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "GA"
    },
    {
      "bioguideId": "J000301",
      "district": "0",
      "firstName": "Dusty",
      "fullName": "Rep. Johnson, Dusty [R-SD-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "R",
      "sponsorshipDate": "2025-04-28",
      "state": "SD"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-05-05",
      "state": "CA"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
      "state": "IN"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "KS"
    },
    {
      "bioguideId": "R000603",
      "district": "7",
      "firstName": "David",
      "fullName": "Rep. Rouzer, David [R-NC-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Rouzer",
      "party": "R",
      "sponsorshipDate": "2025-08-05",
      "state": "NC"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "IA"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-07",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1873ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1873\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Kelly of Pennsylvania (for himself and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude certain broadband grants from gross income.\n#### 1. Short title\nThis Act may be cited as the Broadband Grant Tax Treatment Act .\n#### 2. Certain grants for broadband excluded from gross income\n##### (a) In general\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new subsection:\n139J. Certain broadband grants (a) In general Gross income shall not include any qualified broadband grant made for purposes of broadband deployment. (b) Denial of double benefit Notwithstanding any other provision of this subtitle, no deduction or credit shall be allowed for, or by reason of, any expenditure to the extent of the amount excluded under subsection (a) for any qualified broadband grant which was provided with respect to such expenditure. The adjusted basis of any property shall be reduced by the amount excluded under subsection (a) which was provided with respect to such property. (c) Qualified broadband grant For purposes of this section, the term qualified broadband grant means\u2014 (1) any grant or subgrant received under the Broadband Equity, Access, and Deployment Program established under section 60102 of the Infrastructure Investment and Jobs Act, (2) any grant or subgrant received under the State Digital Equity Capacity Grant Program established under section 60304 of such Act, (3) any grant received under the Digital Equity Competitive Grant Program established under section 60305 of such Act, (4) any grant received under section 60401 of such Act (relating to middle mile grants), (5) any grant received\u2014 (A) under the broadband loan and grant pilot program established by section 779 of Public Law 115\u2013141 under the Rural Electrification Act of 1936; and (B) from funds made available for such program under the heading Distance Learning, Telemedicine, and Broadband Program under the heading Rural Utilities Service under title I of division J of the Infrastructure Investment and Jobs Act, (6) any grant received from a State, territory, Tribal government, or unit of local government to the extent such grant was\u2014 (A) funded by amounts provided to the State or local government under section 602, 603, or 604 of the Social Security Act, and (B) provided for the stated purposes of making investments in broadband infrastructure, or (7) any grant or subgrant received under section 905 of division N of the Consolidated Appropriations Act, 2021. (d) Regulations The Secretary shall issue such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Clerical amendment\nThe table of sections for part III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item related to section 139I the following new item:\nSec. 139J. Certain broadband grants. .\n##### (c) Effective date\nThe amendments made by this section shall apply to amounts received in taxable years ending after March 11, 2023.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-20",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "674",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Broadband Grant Tax Treatment Act",
      "type": "S"
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
        "updateDate": "2025-05-08T14:08:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-05",
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
          "measure-id": "id119hr1873",
          "measure-number": "1873",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-05",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1873v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-03-05",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2023.</p>"
        },
        "title": "Broadband Grant Tax Treatment Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1873.xml",
    "summary": {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2023.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr1873"
    },
    "title": "Broadband Grant Tax Treatment Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-05",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Broadband Grant Tax Treatment Act</strong></p><p>This bill excludes from gross income (for federal tax purposes) certain grants received for broadband deployment.</p><p>As background, contributions of capital to a corporation generally are not taxable income. However, under an exception enacted in 2017 by the Tax Cuts and Jobs Act, grants from a government or civic organization are not contributions to capital and, thus, treated as taxable income. Prior to the Tax Cuts and Jobs Act, the\u00a0Internal Revenue Service (IRS) considered certain grants from a government or civic organization\u00a0contributions of capital and, thus, not taxable income.</p><p>The bill specifically excludes from gross income grants received for broadband deployment from the</p><ul><li>National Telecommunications and Information Administration (NTIA) Broadband Equity, Access, and Deployment Program;</li><li>NTIA State Digital Equity Capacity Grant Program;</li><li>NTIA Digital Equity Competitive Grant Program;</li><li>NTIA Enabling Middle Mile Broadband Infrastructure Program;</li><li>Department of Agriculture ReConnect Program;</li><li>Coronavirus State and Local\u00a0Fiscal Recovery Funds\u00a0and the Coronavirus Capital Projects Fund; and</li><li>NTIA Tribal Broadband Connectivity Program and the Broadband Infrastructure Program.</li></ul><p>The bill also requires the IRS to issue guidance on the exclusion from gross income of such grants.</p><p>The bill applies to funds received in tax years ending after March 11, 2023.</p>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr1873"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1873ih.xml"
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
      "title": "Broadband Grant Tax Treatment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:53:27Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Broadband Grant Tax Treatment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude certain broadband grants from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:48:28Z"
    }
  ]
}
```
