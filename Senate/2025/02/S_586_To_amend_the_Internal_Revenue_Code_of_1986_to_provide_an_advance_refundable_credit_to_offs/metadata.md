# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/586?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/586
- Title: Flood Insurance Affordability Tax Credit Act
- Congress: 119
- Bill type: S
- Bill number: 586
- Origin chamber: Senate
- Introduced date: 2025-02-13
- Update date: 2025-09-29T14:44:53Z
- Update date including text: 2025-09-29T14:44:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in Senate
- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-13: Introduced in Senate

## Actions

- 2025-02-13 - IntroReferral: Introduced in Senate
- 2025-02-13 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/586",
    "number": "586",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Flood Insurance Affordability Tax Credit Act",
    "type": "S",
    "updateDate": "2025-09-29T14:44:53Z",
    "updateDateIncludingText": "2025-09-29T14:44:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T18:16:57Z",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s586is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 586\nIN THE SENATE OF THE UNITED STATES\nFebruary 13, 2025 Mr. Cassidy (for himself and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an advance refundable credit to offset certain flood insurance premiums, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Flood Insurance Affordability Tax Credit Act .\n#### 2. Refundable credit for certain flood insurance coverage\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Refundable credit for certain flood insurance coverage (a) In general There shall be allowed as a credit against the tax imposed by this subtitle for any taxable year an amount equal to 33 percent of the applicable flood insurance premiums paid or incurred by the taxpayer during the taxable year. (b) Limitation based on household income (1) In general The amount of the credit allowed under subsection (a) (determined without regard to this subsection) shall be reduced (but not below zero) by the amount which bears the same ratio to such credit as\u2014 (A) the excess (if any) of\u2014 (i) the taxpayer's household income for such taxable year, over (ii) an amount equal to 350 percent of the poverty line for a family of the size involved, bears to (B) the phaseout amount. (2) Phaseout amount For purposes of this subsection, the phaseout amount with respect to any taxpayer for any taxable year is the excess of\u2014 (A) an amount equal to 435 percent of the poverty line for a family of the size involved, over (B) an amount equal to 350 percent of the poverty line for a family of the size involved. (3) Terms related to income and families Rules similar to the rules of section 36B(d) shall apply for purposes of determining family size, household income, and the poverty line. (c) Applicable flood insurance premiums For purposes of this section, the term applicable flood insurance premiums means premiums paid or incurred to insure the principal residence (within the meaning of section 121) of the taxpayer under the program established under the National Flood Insurance Act of 1968 ( 42 U.S.C. 4001 et seq. ). (d) Other rules (1) No credit for married individuals filing separate returns If the taxpayer is a married individual (within the meaning of section 7703), this section shall apply only if the taxpayer and the taxpayer's spouse file a joint return for the taxable year. (2) Denial of credit to dependents No credit shall be allowed under this section to any individual with respect to whom a deduction under section 151 is allowable to another taxpayer for a taxable year beginning in the calendar year in which such individual's taxable year begins. (e) Reconciliation of credit and advance credit The amount of the credit allowed under this section for any taxable year shall be reduced (but not below zero) by the amount of any advance payment of such credit under section 7527B. (f) Regulations The Secretary shall prescribe such regulations as may be necessary to carry out the provisions of this section, including regulations which provide for the coordination of the credit allowed under this section with the program for advance payment of the credit under section 7527B. .\n##### (b) Disallowance of deduction\nSection 280C of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(i) Credit for certain flood insurance coverage No deduction shall be allowed for the portion of the applicable flood insurance premiums (as defined in section 36C) which is equal to the amount of the credit determined for the taxable year under section 36C(a) with respect to such premiums. .\n##### (c) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting , 36C after 36B .\n**(2)**\nParagraph (2) of section 1324(b) of title 31, United States Code, is amended by inserting , 36C after 36B .\n##### (d) Clerical amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Refundable credit for certain flood insurance coverage. .\n##### (e) Effective date\nThe amendments made by this section shall apply to amounts paid or incurred in taxable years beginning after the date of the enactment of this Act.\n#### 3. Advance payments\n##### (a) In general\nChapter 77 of the Internal Revenue Code of 1986 is amended by inserting after section 7527A the following new section:\n7527B. Advance payment of credit for certain flood insurance coverage (a) In general The Secretary shall establish a program for making payments of applicable flood insurance premiums (as defined in section 36C(c)) on behalf of applicable individuals to the Administrator of the Federal Emergency Management Agency for such individuals. (b) Limitation on advance payments during any taxable year (1) In general The Secretary may make payments under subsection (a) only to the extent that the total amount of such payments made on behalf of any applicable individual during the taxable year does not exceed 33 percent of the applicable flood insurance premiums (as defined in section 36C) paid or incurred by the applicable individual during such taxable year (reduced as provided under section 36C(b) based on applicable information). (2) Applicable information For purposes of paragraph (1), the term applicable information means\u2014 (A) tax return information for the most recent taxable year for which the Secretary determines information is available, or (B) such other information as the Secretary determines is reliable to determine the amount (if any) of any reduction under section 36C(b). (c) Applicable individual For purposes of this section, the term applicable individual means any individual who elects the application of this section (in such form and manner as provided by the Secretary). .\n##### (b) Clerical amendment\nThe table of sections for chapter 77 of such Code is amended by inserting after the item relating to section 7527A the following new item:\nSec. 7527B. Advance payment of credit for certain flood insurance coverage. .",
      "versionDate": "2025-02-13",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-05-06T16:33:47Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119s586",
          "measure-number": "586",
          "measure-type": "s",
          "orig-publish-date": "2025-02-13",
          "originChamber": "SENATE",
          "update-date": "2025-09-29"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s586v00",
            "update-date": "2025-09-29"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Flood Insurance Affordability Tax Credit Act</strong></p><p>This bill establishes a new refundable tax credit for up to 33% of the flood insurance premiums paid (or incurred) under the National Flood Insurance Program to insure a principal residence. The bill also requires the Internal Revenue Service (IRS) to establish a program for paying the tax credit in advance.</p><p>Under the bill, the tax credit for flood insurance premiums may be reduced depending on the taxpayer\u2019s household income in relation to the federal poverty line (FPL). The tax credit begins to phase out once a taxpayer\u2019s household income is 350% of the FPL and is completely phased out once a taxpayer\u2019s household income reaches 435% of the FPL. (Other limitations may apply.)</p><p>Further, the tax credit for flood premiums may not be claimed by a married taxpayer who files a separate federal income tax return or a taxpayer who may be claimed as a dependent.</p><p>Finally, the bill requires the IRS to establish a program that allows a taxpayer to receive the allowable tax credit amount for flood insurance premiums (based on tax return information for the most recent tax year available) in advance.</p>"
        },
        "title": "Flood Insurance Affordability Tax Credit Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s586.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Flood Insurance Affordability Tax Credit Act</strong></p><p>This bill establishes a new refundable tax credit for up to 33% of the flood insurance premiums paid (or incurred) under the National Flood Insurance Program to insure a principal residence. The bill also requires the Internal Revenue Service (IRS) to establish a program for paying the tax credit in advance.</p><p>Under the bill, the tax credit for flood insurance premiums may be reduced depending on the taxpayer\u2019s household income in relation to the federal poverty line (FPL). The tax credit begins to phase out once a taxpayer\u2019s household income is 350% of the FPL and is completely phased out once a taxpayer\u2019s household income reaches 435% of the FPL. (Other limitations may apply.)</p><p>Further, the tax credit for flood premiums may not be claimed by a married taxpayer who files a separate federal income tax return or a taxpayer who may be claimed as a dependent.</p><p>Finally, the bill requires the IRS to establish a program that allows a taxpayer to receive the allowable tax credit amount for flood insurance premiums (based on tax return information for the most recent tax year available) in advance.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s586"
    },
    "title": "Flood Insurance Affordability Tax Credit Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Flood Insurance Affordability Tax Credit Act</strong></p><p>This bill establishes a new refundable tax credit for up to 33% of the flood insurance premiums paid (or incurred) under the National Flood Insurance Program to insure a principal residence. The bill also requires the Internal Revenue Service (IRS) to establish a program for paying the tax credit in advance.</p><p>Under the bill, the tax credit for flood insurance premiums may be reduced depending on the taxpayer\u2019s household income in relation to the federal poverty line (FPL). The tax credit begins to phase out once a taxpayer\u2019s household income is 350% of the FPL and is completely phased out once a taxpayer\u2019s household income reaches 435% of the FPL. (Other limitations may apply.)</p><p>Further, the tax credit for flood premiums may not be claimed by a married taxpayer who files a separate federal income tax return or a taxpayer who may be claimed as a dependent.</p><p>Finally, the bill requires the IRS to establish a program that allows a taxpayer to receive the allowable tax credit amount for flood insurance premiums (based on tax return information for the most recent tax year available) in advance.</p>",
      "updateDate": "2025-09-29",
      "versionCode": "id119s586"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s586is.xml"
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
      "title": "Flood Insurance Affordability Tax Credit Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-14T03:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Flood Insurance Affordability Tax Credit Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-14T03:38:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide an advance refundable credit to offset certain flood insurance premiums, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-14T03:33:38Z"
    }
  ]
}
```
