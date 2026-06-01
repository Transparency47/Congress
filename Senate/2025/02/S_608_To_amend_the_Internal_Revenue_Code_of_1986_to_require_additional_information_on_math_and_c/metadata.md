# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/608?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/608
- Title: IRS MATH Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 608
- Origin chamber: Senate
- Introduced date: 2025-02-18
- Update date: 2026-03-31T20:14:37Z
- Update date including text: 2026-03-31T20:14:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-02-18: Introduced in Senate
- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S613)
- Latest action: 2025-02-18: Introduced in Senate

## Actions

- 2025-02-18 - IntroReferral: Introduced in Senate
- 2025-02-18 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S613)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-18",
    "latestAction": {
      "actionDate": "2025-02-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/608",
    "number": "608",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "IRS MATH Act of 2025",
    "type": "S",
    "updateDate": "2026-03-31T20:14:37Z",
    "updateDateIncludingText": "2026-03-31T20:14:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-18",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S613)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-18",
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
          "date": "2025-02-18T21:09:42Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s608is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 608\nIN THE SENATE OF THE UNITED STATES\nFebruary 18, 2025 Ms. Warren (for herself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to require additional information on math and clerical error notices.\n#### 1. Short title\nThis Act may be cited as the Internal Revenue Service Math and Taxpayer Help Act of 2025 or the IRS MATH Act of 2025 .\n#### 2. Improvement of notices of math or clerical error\n##### (a) In general\nSection 6213(b)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking errors .\u2014If the taxpayer and inserting \u201c errors .\u2014\n(A) In general If the taxpayer ,\n**(2)**\nby striking Each notice in the second sentence and inserting Subject to subparagraph (B), each notice , and\n**(3)**\nby adding at the end the following new subparagraph:\n(B) Specificity of math or clerical error notice (i) In general The notice provided under subparagraph (A) shall\u2014 (I) be sent to the taxpayer\u2019s last known address, (II) describe the mathematical or clerical error in comprehensive, plain language, including\u2014 (aa) the type of error, (bb) the section of this title to which the error relates, (cc) a description of the nature of the error, and (dd) the specific line of the return on which the error was made, (III) an itemized computation of any direct or incidental adjustments to be made to the return in correction of the error, including any adjustment to the amount of\u2014 (aa) adjusted gross income, (bb) taxable income, (cc) itemized or standard deductions, (dd) nonrefundable credits, (ee) credits under section 24, 25A, 32, 35, or 36B, credits claimed with respect to undistributed long-term capital gains on Form 2439, credits for Federal taxes paid on fuels claimed on Form 4136, and any other refundable credits, (ff) income tax, (gg) other taxes, (hh) total tax, (ii) Federal income tax withheld or excess tax withheld under section 3101 or 3201(a), (jj) estimated tax payments, including amount applied from prior year\u2019s return, (kk) refund or amount owed, (ll) net operating loss carryforwards, or (mm) credit carryforwards, (IV) include the telephone number for the automated phone transcript service, and (V) display the date by which the taxpayer may request to abate any assessment specified in such notice pursuant to paragraph (2)(A), in bold, font size 14, and immediately next to the taxpayer\u2019s address on page 1 of the notice. (ii) No lists of potential errors A notice which provides multiple potential or alternative errors which may be applicable to the return shall not be sufficiently specific for purposes of clause (i)(II); however, if multiple specific errors apply to the return all such errors should be listed. .\n##### (b) Notice of abatement\nParagraph (2) of section 6213(b) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(C) Notice Upon determination of an abatement pursuant to subparagraph (A), the Secretary shall send notice to the taxpayer of such abatement which\u2014 (i) is sent to the taxpayer\u2019s last known address, (ii) describes the abatement in comprehensive, plain language, and (iii) provides an itemized computation of any adjustments to be made to the items described in the notice of mathematical or clerical error, including any changes to any item described in paragraph (1)(B)(i)(III). .\n##### (c) Effective date\nThe amendments made by this section shall apply to notices sent after the date which is 12 months after the date of the enactment of this Act.\n##### (d) Procedures\nNot later than 180 days after the date of the enactment of this Act, the Secretary of the Treasury (or such Secretary's delegate) shall provide for procedures by which a taxpayer may request an abatement pursuant to section 6213(b)(1)(B)(i)(V) of the Internal Revenue Code of 1986 in writing, electronically, by telephone, or in person.\n##### (e) Pilot program\nNot later than 18 months after the date of the enactment of this Act, the Secretary of the Treasury (or such Secretary's delegate), in consultation with the National Taxpayer Advocate, shall\u2014\n**(1)**\nimplement a pilot program to send a trial number of notices, in an amount which is a statistically significant portion of all such notices, of mathematical or clerical error pursuant to section 6213(b) of the Internal Revenue Code of 1986 by certified or registered mail with e-signature confirmation of receipt, and\n**(2)**\nreport to Congress, aggregated by the type of error under section 6213(g) of such Code to which the notices relate, on\u2014\n**(A)**\nthe number of mathematical or clerical errors noticed under the program and the dollar amounts involved,\n**(B)**\nthe number of abatements of tax and the dollar amounts of such abatements, and\n**(C)**\nthe effect of such pilot program on taxpayer response and adjustments or abatements to tax,\nwith conclusions drawn about the effectiveness of certified mail, with and without return receipt, and any other recommendations for improving taxpayer response rates.",
      "versionDate": "2025-02-18",
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
        "actionDate": "2025-11-25",
        "text": "Became Public Law No: 119-39."
      },
      "number": "998",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Internal Revenue Service Math and Taxpayer Help Act",
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
        "updateDate": "2025-05-06T14:15:08Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-18",
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
          "measure-id": "id119s608",
          "measure-number": "608",
          "measure-type": "s",
          "orig-publish-date": "2025-02-18",
          "originChamber": "SENATE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s608v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-02-18",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Internal Revenue Service Math and Taxpayer Help Act of 2025 or the\u00a0IRS MATH Act of 2025</strong></p><p>This bill requires the Internal Revenue Service (IRS) to provide specific information on a notice related to a math or clerical error, send a notice related to an abatement of taxes assessed due to a math or clerical error, provide procedures for requesting such an abatement, and implement a pilot program for sending notices of a math or clerical error.</p><p>Under the bill, a notice sent by the IRS regarding\u00a0a math or clerical error must include</p><ul><li>a clear description of the error and the specific federal tax return line on which the error was made,</li><li>an itemized computation of adjustments required to correct the error,</li><li>the telephone number for the automated transcript service, and</li><li>the deadline for requesting an abatement of any tax assessed due to the error.</li></ul><p>Further, the bill requires the IRS to send a notice related to an abatement of tax assessed due to a math or clerical error that clearly describes the abatement and includes an itemized computation of adjustments to be made to the items described in the notice of the\u00a0error.</p><p>The bill also requires the IRS to</p><ul><li>provide procedures for requesting an abatement of tax assessed due to a math or clerical error,</li><li>implement a pilot program to send notices of a math or clerical error by certified or registered mail, and</li><li>report to Congress certain information about the pilot program.</li></ul>"
        },
        "title": "IRS MATH Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s608.xml",
    "summary": {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Internal Revenue Service Math and Taxpayer Help Act of 2025 or the\u00a0IRS MATH Act of 2025</strong></p><p>This bill requires the Internal Revenue Service (IRS) to provide specific information on a notice related to a math or clerical error, send a notice related to an abatement of taxes assessed due to a math or clerical error, provide procedures for requesting such an abatement, and implement a pilot program for sending notices of a math or clerical error.</p><p>Under the bill, a notice sent by the IRS regarding\u00a0a math or clerical error must include</p><ul><li>a clear description of the error and the specific federal tax return line on which the error was made,</li><li>an itemized computation of adjustments required to correct the error,</li><li>the telephone number for the automated transcript service, and</li><li>the deadline for requesting an abatement of any tax assessed due to the error.</li></ul><p>Further, the bill requires the IRS to send a notice related to an abatement of tax assessed due to a math or clerical error that clearly describes the abatement and includes an itemized computation of adjustments to be made to the items described in the notice of the\u00a0error.</p><p>The bill also requires the IRS to</p><ul><li>provide procedures for requesting an abatement of tax assessed due to a math or clerical error,</li><li>implement a pilot program to send notices of a math or clerical error by certified or registered mail, and</li><li>report to Congress certain information about the pilot program.</li></ul>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s608"
    },
    "title": "IRS MATH Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-02-18",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Internal Revenue Service Math and Taxpayer Help Act of 2025 or the\u00a0IRS MATH Act of 2025</strong></p><p>This bill requires the Internal Revenue Service (IRS) to provide specific information on a notice related to a math or clerical error, send a notice related to an abatement of taxes assessed due to a math or clerical error, provide procedures for requesting such an abatement, and implement a pilot program for sending notices of a math or clerical error.</p><p>Under the bill, a notice sent by the IRS regarding\u00a0a math or clerical error must include</p><ul><li>a clear description of the error and the specific federal tax return line on which the error was made,</li><li>an itemized computation of adjustments required to correct the error,</li><li>the telephone number for the automated transcript service, and</li><li>the deadline for requesting an abatement of any tax assessed due to the error.</li></ul><p>Further, the bill requires the IRS to send a notice related to an abatement of tax assessed due to a math or clerical error that clearly describes the abatement and includes an itemized computation of adjustments to be made to the items described in the notice of the\u00a0error.</p><p>The bill also requires the IRS to</p><ul><li>provide procedures for requesting an abatement of tax assessed due to a math or clerical error,</li><li>implement a pilot program to send notices of a math or clerical error by certified or registered mail, and</li><li>report to Congress certain information about the pilot program.</li></ul>",
      "updateDate": "2025-05-09",
      "versionCode": "id119s608"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s608is.xml"
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
      "title": "IRS MATH Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T01:08:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "IRS MATH Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Internal Revenue Service Math and Taxpayer Help Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T01:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to require additional information on math and clerical error notices.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T01:03:32Z"
    }
  ]
}
```
