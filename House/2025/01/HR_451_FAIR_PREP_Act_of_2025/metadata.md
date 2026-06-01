# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/451?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/451
- Title: FAIR PREP Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 451
- Origin chamber: House
- Introduced date: 2025-01-15
- Update date: 2025-12-05T22:58:38Z
- Update date including text: 2025-12-05T22:58:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-15: Introduced in House

## Actions

- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Introduced in House
- 2025-01-15 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-15",
    "latestAction": {
      "actionDate": "2025-01-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/451",
    "number": "451",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001172",
        "district": "3",
        "firstName": "Adrian",
        "fullName": "Rep. Smith, Adrian [R-NE-3]",
        "lastName": "Smith",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "FAIR PREP Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-05T22:58:38Z",
    "updateDateIncludingText": "2025-12-05T22:58:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T15:03:05Z",
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
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NC"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WV"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NY"
    },
    {
      "bioguideId": "H001082",
      "district": "1",
      "firstName": "Kevin",
      "fullName": "Rep. Hern, Kevin [R-OK-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Hern",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "OK"
    },
    {
      "bioguideId": "A000379",
      "district": "4",
      "firstName": "Mark",
      "fullName": "Rep. Alford, Mark [R-MO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Alford",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MO"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "FL"
    },
    {
      "bioguideId": "W000809",
      "district": "3",
      "firstName": "Steve",
      "fullName": "Rep. Womack, Steve [R-AR-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Womack",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "AR"
    },
    {
      "bioguideId": "V000134",
      "district": "24",
      "firstName": "Beth",
      "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Duyne",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TX"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NE"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-01-28",
      "state": "FL"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-31",
      "state": "NY"
    },
    {
      "bioguideId": "S001224",
      "district": "3",
      "firstName": "Keith",
      "fullName": "Rep. Self, Keith [R-TX-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Self",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001224",
      "district": "1",
      "firstName": "Nathaniel",
      "fullName": "Rep. Moran, Nathaniel [R-TX-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-04",
      "state": "TX"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "T000480",
      "district": "4",
      "firstName": "William",
      "fullName": "Rep. Timmons, William R. [R-SC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Timmons",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "SC"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-21",
      "state": "TX"
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
      "sponsorshipDate": "2025-02-21",
      "state": "GA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "NY"
    },
    {
      "bioguideId": "K000392",
      "district": "8",
      "firstName": "David",
      "fullName": "Rep. Kustoff, David [R-TN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Kustoff",
      "party": "R",
      "sponsorshipDate": "2025-02-24",
      "state": "TN"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "NC"
    },
    {
      "bioguideId": "C001126",
      "district": "15",
      "firstName": "Mike",
      "fullName": "Rep. Carey, Mike [R-OH-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Carey",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "OH"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "IL"
    },
    {
      "bioguideId": "A000369",
      "district": "2",
      "firstName": "Mark",
      "fullName": "Rep. Amodei, Mark E. [R-NV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Amodei",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "NV"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "GA"
    },
    {
      "bioguideId": "B001314",
      "district": "4",
      "firstName": "Aaron",
      "fullName": "Rep. Bean, Aaron [R-FL-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Bean",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "FL"
    },
    {
      "bioguideId": "E000298",
      "district": "4",
      "firstName": "Ron",
      "fullName": "Rep. Estes, Ron [R-KS-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Estes",
      "party": "R",
      "sponsorshipDate": "2025-04-02",
      "state": "KS"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "IN"
    },
    {
      "bioguideId": "L000595",
      "district": "5",
      "firstName": "Julia",
      "fullName": "Rep. Letlow, Julia [R-LA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Letlow",
      "party": "R",
      "sponsorshipDate": "2025-12-03",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr451ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 451\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 15, 2025 Mr. Smith of Nebraska (for himself, Mr. Edwards , Mr. Garbarino , Mrs. Miller of West Virginia , Ms. Tenney , Mr. Hern of Oklahoma , Mr. Alford , Mr. Buchanan , Mr. Womack , Ms. Van Duyne , and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to prohibit certain activities constituting preparation of tax returns by the Secretary of the Treasury, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025 .\n#### 2. Prohibition of certain return preparation\n##### (a) In general\nSection 6020 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(c) Prohibited preparation by Secretary (1) In general Except as provided in section 6014 and subsections (a) and (b) of this section, the Secretary shall not prepare any return of tax imposed by this title or any claim for refund of tax imposed by this title. (2) Prohibition of direct file and comparable programs For purposes of paragraph (1), any return or claim for refund prepared using an electronic tax preparation service operated by the Secretary shall be treated as if such return or claim were prepared by the Secretary. (3) Qualified return preparation programs and IRS Free File partnership Paragraph (2) shall not apply to any return or claim for refund solely because such return or claim for refund was prepared via, or with the assistance of\u2014 (A) a qualified return preparation program (as defined in section 7526A(e)), or (B) the IRS Free File Program as established by the Internal Revenue Service and published in the Federal Register on November 4, 2002 (67 Fed. Reg. 67247), including any subsequent agreements and governing rules established pursuant thereto. (4) Definitions For purposes of this subsection\u2014 (A) Tax return preparation (i) In general The term prepare with respect to any return or claim for refund means\u2014 (I) the completion of any form and schedule needed to compute and report any tax imposed by this title or any claim for refund of such a tax, and (II) the filing of any such return or claim for refund, regardless of whether such return or claim is submitted electronically or on paper. For purposes of the preceding sentence, the preparation of any portion of a return or claim for refund shall be treated as if it were the preparation of such return or claim for refund. (ii) Computation and correction of errors, etc (I) In general Such term shall not include any computation authorized by section 6102 or any other computation or correction of mathematical or clerical errors required or authorized by any provision of chapter 63. (II) Fillable forms Such term shall not include the provision of fillable forms by the Secretary merely because such forms include an automated calculation feature. (B) Electronic tax preparation service The term electronic tax preparation service operated by the Secretary means the free direct e-file tax return system as established by the Internal Revenue Service and published in the Federal Register on December 15, 2023 (88 Fed. Reg. 87057), and September 5, 2024 (89 Fed. Reg. 72699), and any successor program of the Internal Revenue Service which provides an electronic tax preparation service option. .\n##### (b) Effective date\nThe amendment made by this section shall apply to returns filed after the date which is 30 days after the date of the enactment of this Act.\n##### (c) No inference\nThe amendment made by this section shall not be construed to create any inference with respect to the authority of the Secretary of the Treasury (or any delegate of such Secretary) to develop and offer for use any electronic tax filing or tax preparation service option, or otherwise engage in the preparation of any return of tax or any claim for refund of tax imposed by the Internal Revenue Code of 1986, with respect to any taxable year beginning on or before the date of the enactment of this Act.\n#### 3. Limitation on further expenditures circumventing congressional authority\nThe Secretary of the Treasury (or any delegate of such Secretary) may not award or make payment of grants or enter into or maintain any contract, other transaction, or reimbursable agreement for the development or operation of an electronic tax preparation service option after the date of the enactment of this Act unless otherwise authorized by law.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-01-15",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "96",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAIR PREP Act of 2025",
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
        "updateDate": "2025-02-15T14:43:36Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-15",
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
          "measure-id": "id119hr451",
          "measure-number": "451",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-15",
          "originChamber": "HOUSE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr451v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>"
        },
        "title": "FAIR PREP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr451.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr451"
    },
    "title": "FAIR PREP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119hr451"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr451ih.xml"
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
      "title": "FAIR PREP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:59:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FAIR PREP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-13T06:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to prohibit certain activities constituting preparation of tax returns by the Secretary of the Treasury, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-13T06:48:25Z"
    }
  ]
}
```
