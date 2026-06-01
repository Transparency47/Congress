# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/96?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/96
- Title: FAIR PREP Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 96
- Origin chamber: Senate
- Introduced date: 2025-01-15
- Update date: 2025-12-05T22:58:30Z
- Update date including text: 2025-12-05T22:58:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-15: Introduced in Senate
- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-01-15: Introduced in Senate

## Actions

- 2025-01-15 - IntroReferral: Introduced in Senate
- 2025-01-15 - IntroReferral: Read twice and referred to the Committee on Finance.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/96",
    "number": "96",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "FAIR PREP Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T22:58:30Z",
    "updateDateIncludingText": "2025-12-05T22:58:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-15",
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
      "actionDate": "2025-01-15",
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
          "date": "2025-01-15T18:16:36Z",
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
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MT"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NC"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WY"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "NE"
    },
    {
      "bioguideId": "S001227",
      "firstName": "Eric",
      "fullName": "Sen. Schmitt, Eric [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Schmitt",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "MO"
    },
    {
      "bioguideId": "H000601",
      "firstName": "Bill",
      "fullName": "Sen. Hagerty, Bill [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Hagerty",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "TN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "ID"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "WV"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "KS"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s96is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 96\nIN THE SENATE OF THE UNITED STATES\nJanuary 15, 2025 Mrs. Blackburn (for herself, Mr. Daines , Mr. Tillis , Mr. Barrasso , Mr. Ricketts , Mr. Schmitt , Mr. Hagerty , Mr. Risch , Mrs. Capito , Mr. Marshall , and Mr. Cramer ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to prohibit certain activities constituting preparation of tax returns by the Secretary of the Treasury, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025 .\n#### 2. Prohibition of certain return preparation\n##### (a) In general\nSection 6020 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(c) Prohibited preparation by Secretary (1) In general Except as provided in section 6014 and subsections (a) and (b) of this section, the Secretary shall not prepare any return of tax imposed by this title or any claim for refund of tax imposed by this title. (2) Prohibition of direct file and comparable programs For purposes of paragraph (1), any return or claim for refund prepared using an electronic tax preparation service operated by the Secretary shall be treated as if such return or claim were prepared by the Secretary. (3) Qualified return preparation programs and IRS Free File partnership Paragraph (2) shall not apply to any return or claim for refund solely because such return or claim for refund was prepared via, or with the assistance of\u2014 (A) a qualified return preparation program (as defined in section 7526A(e)), or (B) the IRS Free File Program as established by the Internal Revenue Service and published in the Federal Register on November 4, 2002 (67 Fed. Reg. 67247), including any subsequent agreements and governing rules established pursuant thereto. (4) Definitions For purposes of this subsection\u2014 (A) Tax return preparation (i) In general The term prepare with respect to any return or claim for refund means\u2014 (I) the completion of any form and schedule needed to compute and report any tax imposed by this title or any claim for refund of such a tax, and (II) the filing of any such return or claim for refund, regardless of whether such return or claim is submitted electronically or on paper. For purposes of the preceding sentence, the preparation of any portion of a return or claim for refund shall be treated as if it were the preparation of such return or claim for refund. (ii) Computation and correction of errors, etc (I) In general Such term shall not include any computation authorized by section 6102 or any other computation or correction of mathematical or clerical errors required or authorized by any provision of chapter 63. (II) Fillable forms Such term shall not include the provision of fillable forms by the Secretary merely because such forms include an automated calculation feature. (B) Electronic tax preparation service The term electronic tax preparation service operated by the Secretary means the free direct e-file tax return system as established by the Internal Revenue Service and published in the Federal Register on December 15, 2023 (88 Fed. Reg. 87057), and September 5, 2024 (89 Fed. Reg. 72699), and any successor program of the Internal Revenue Service which provides an electronic tax preparation service option. .\n##### (b) Effective date\nThe amendment made by this section shall apply to returns filed after the date which is 30 days after the date of the enactment of this Act.\n##### (c) No inference\nThe amendment made by this section shall not be construed to create any inference with respect to the authority of the Secretary of the Treasury (or any delegate of such Secretary) to develop and offer for use any electronic tax filing or tax preparation service option, or otherwise engage in the preparation of any return of tax or any claim for refund of tax imposed by the Internal Revenue Code of 1986, with respect to any taxable year beginning on or before the date of the enactment of this Act.\n#### 3. Limitation on further expenditures circumventing congressional authority\nThe Secretary of the Treasury (or any delegate of such Secretary) may not award or make payment of grants or enter into or maintain any contract, other transaction, or reimbursable agreement for the development or operation of an electronic tax preparation service option after the date of the enactment of this Act unless otherwise authorized by law.",
      "versionDate": "2025-01-15",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "451",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "FAIR PREP Act of 2025",
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
        "updateDate": "2025-02-15T14:44:37Z"
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
          "measure-id": "id119s96",
          "measure-number": "96",
          "measure-type": "s",
          "orig-publish-date": "2025-01-15",
          "originChamber": "SENATE",
          "update-date": "2025-03-24"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s96v00",
            "update-date": "2025-03-24"
          },
          "action-date": "2025-01-15",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>"
        },
        "title": "FAIR PREP Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s96.xml",
    "summary": {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s96"
    },
    "title": "FAIR PREP Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-15",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025 or the FAIR PREP Act of 2025</strong></p><p>This bill prohibits the Internal Revenue Service (IRS) from preparing federal tax returns or refund claims, with some exceptions. The bill specifically prohibits the preparation of federal income tax returns or refund claims through the IRS\u2019s Direct File program. (The Direct File program currently allows qualified taxpayers in 25 participating states to prepare and electronically file free federal tax returns through a portal on the IRS\u2019s website.)</p><p>The bill defines <em>prepare</em> with respect to federal tax returns and refund claims as (1) the completion (in whole or in part) of any form or schedule for the purpose of calculating federal taxes or refunds, and (2) the filing (either electronically or on paper) of such federal tax returns or refund claims.</p><p>However, under the bill, federal and state tax returns and refund claims may be prepared through the IRS\u2019s Free File program (a program that allows certain taxpayers to prepare and file free federal and state income tax returns\u00a0using third-party tax-preparation software) or the Volunteer Income Tax Assistance grant program (through which the IRS partners with local community organizations to help low-income and disabled individuals and persons with limited English proficiency prepare and file free federal and state\u00a0income tax returns).</p><p> Further, the Department of the Treasury may not award grants or enter into contracts\u00a0or other transactions for the development or operation of an electronic tax preparation service.\u00a0\u00a0</p>",
      "updateDate": "2025-03-24",
      "versionCode": "id119s96"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s96is.xml"
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
      "title": "FAIR PREP Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-11T05:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "FAIR PREP Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fostering Autonomy in Independent Returns by Prohibiting Redundant and Extralegal Programs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-11T05:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to prohibit certain activities constituting preparation of tax returns by the Secretary of the Treasury, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-11T05:48:34Z"
    }
  ]
}
```
