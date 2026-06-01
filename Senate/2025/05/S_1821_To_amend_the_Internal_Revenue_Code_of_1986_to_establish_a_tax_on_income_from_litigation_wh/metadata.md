# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1821?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1821
- Title: Tackling Predatory Litigation Funding Act
- Congress: 119
- Bill type: S
- Bill number: 1821
- Origin chamber: Senate
- Introduced date: 2025-05-20
- Update date: 2026-04-29T11:03:32Z
- Update date including text: 2026-04-29T11:03:32Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in Senate
- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-20: Introduced in Senate

## Actions

- 2025-05-20 - IntroReferral: Introduced in Senate
- 2025-05-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1821",
    "number": "1821",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000476",
        "district": "",
        "firstName": "Thomas",
        "fullName": "Sen. Tillis, Thomas [R-NC]",
        "lastName": "Tillis",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Tackling Predatory Litigation Funding Act",
    "type": "S",
    "updateDate": "2026-04-29T11:03:32Z",
    "updateDateIncludingText": "2026-04-29T11:03:32Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-20",
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
      "actionDate": "2025-05-20",
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
        "item": [
          {
            "date": "2025-05-20T21:25:16Z",
            "name": "Referred To"
          },
          {
            "date": "2025-05-20T21:25:16Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "OH"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "OH"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-06-05",
      "state": "FL"
    },
    {
      "bioguideId": "G000386",
      "firstName": "Chuck",
      "fullName": "Sen. Grassley, Chuck [R-IA]",
      "isOriginalCosponsor": "False",
      "lastName": "Grassley",
      "party": "R",
      "sponsorshipDate": "2025-06-10",
      "state": "IA"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-10-09",
      "state": "MT"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "MT"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1821is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1821\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2025 Mr. Tillis introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax on income from litigation which is received by third-party entities that provided financing for such litigation.\n#### 1. Short title\nThis Act may be cited as the Tackling Predatory Litigation Funding Act .\n#### 2. Litigation financing\n##### (a) In general\nSubtitle D of the Internal Revenue Code of 1986 is amended by adding at the end the following new chapter:\n50B Litigation Financing Sec. 5000E\u20131. Tax imposed. Sec. 5000E\u20132. Definitions. Sec. 5000E\u20133. Special rules. 5000E\u20131. Tax imposed (a) In general A tax is hereby imposed for each taxable year in an amount equal to the applicable percentage of any qualified litigation proceeds received by a covered party. (b) Applicable percentage For purposes of subsection (a), with respect to any taxable year, the applicable percentage shall be the amount (expressed as a percentage) equal to the sum of\u2014 (1) the highest rate of tax imposed by section 1 for such taxable year, plus (2) 3.8 percentage points. (c) Application of tax for pass-Thru entities In the case of a covered party that is a partnership, S corporation, or other pass-thru entity, the tax imposed under subsection (a) shall be applied at the entity level. 5000E\u20132. Definitions In this chapter\u2014 (1) Civil action (A) In general The term civil action means any civil action, administrative proceeding, claim, or cause of action. (B) Multiple actions The term civil action may, unless otherwise indicated, include more than 1 civil action. (2) Covered party (A) In general The term covered party means, with respect to any civil action, any third party (including an individual, corporation, partnership, or sovereign wealth fund) to such action which\u2014 (i) receives funds pursuant to a litigation financing agreement, and (ii) is not an attorney representing a party to such civil action. (B) Inclusion of domestic and foreign entities Subparagraph (A) shall apply to any third party without regard to whether such party is created or organized in the United States or under the law of the United States or of any State. (3) Litigation financing agreement (A) In general The term litigation financing agreement means, with respect to any civil action, a written agreement\u2014 (i) whereby a third party agrees to provide funds to one of the named parties or any law firm affiliated with such civil action, and (ii) which creates a direct or collateralized interest in the proceeds of such action (by settlement, verdict, judgment or otherwise) which\u2014 (I) is based, in whole or part, on a funding-based obligation to\u2014 (aa) such civil action, (bb) the appearing counsel, (cc) any contractual co-counsel, or (dd) the law firm of such counsel or co-counsel, and (II) is executed with\u2014 (aa) any attorney representing a party to such civil action, (bb) any co-counsel in the litigation with a contingent fee interest in the representation of such party, (cc) any third party that has a collateral-based interest in the contingency fees of the counsel or co-counsel firm which is related, in whole or part, to the fees derived from representing such party, or (dd) any named party in such civil action. (B) Substantially similar agreements The term litigation financing agreement shall include any contract (including any option, forward contract, futures contract, short position, swap, or similar contract) or other agreement which, as determined by the Secretary, is substantially similar to an agreement described in subparagraph (A). (C) Exceptions The term litigation financing agreement shall not include any agreement\u2014 (i) under which the total amount of funds described in subparagraph (A)(i) with respect to an individual civil action is less than $10,000, or (ii) in which the third party described in subparagraph (A)\u2014 (I) has a right to receive proceeds which are derived from, or pursuant to, such agreement that are limited to\u2014 (aa) repayment of the principal of a loan, (bb) repayment of the principal of a loan plus any interest on such loan, provided that the rate of interest does not exceed the greater of\u2014 (AA) 7 percent, or (BB) a rate equal to twice the average annual yield on 30-year United States Treasury securities (as determined for the year preceding the date on which such agreement was executed), or (cc) reimbursement of attorney's fees, or (II) bears a relationship described in section 267(b) to the named party receiving the payment described in subparagraph (A)(i). (4) Qualified litigation proceeds (A) In general The term qualified litigation proceeds means, with respect to any taxable year, an amount equal to the realized gains, net income, or other profit received by a covered party during such taxable year which is derived from, or pursuant to, any litigation financing agreement. (B) Anti-netting Any gains, income, or profit described in subparagraph (A) shall not be reduced or offset by any ordinary or capital loss in the taxable year. (C) Prohibition on exclusion of certain amounts In determining the amount of realized gain under subparagraph (A), amounts described in section 104(a)(2) and 892(a)(1) shall not be excluded. 5000E\u20133. Special rules (a) Withholding of tax on litigation proceeds Any applicable person having the control, receipt, or custody of any proceeds from a civil action (by settlement, judgment, or otherwise) with respect to which such person had entered into a litigation financing agreement shall deduct and withhold from such proceeds a tax equal to 50 percent of the applicable percentage (as determined under section 5000E\u20131(b)) of any payments which are required to be made to a third party pursuant to such agreement. (b) Applicable person For purposes of this section, the term applicable person means any person which\u2014 (1) is a named party in a civil action or a law firm affiliated with such civil action, and (2) has entered into a litigation financing agreement with respect to such civil action. (c) Application of withholding provisions (1) Liability for withheld tax Every person required to deduct and withhold any tax under this chapter is hereby made liable for such tax and is hereby indemnified against the claims and demands of any person for the amount of any payments made in accordance with the provisions of this chapter. (2) Withheld tax as credit to recipient of qualified litigation proceeds Qualified litigation proceeds on which any tax is required to be withheld at the source under this chapter shall be included in the return of the recipient of such proceeds, but any amount of tax so withheld shall be credited against the amount of tax as computed in such return. (3) Tax paid by recipient of qualified litigation proceeds If\u2014 (A) any person, in violation of the provisions of this chapter, fails to deduct and withhold any tax under this chapter, and (B) thereafter the tax against which such tax may be credited is paid, the tax so required to be deducted and withheld shall not be collected from such person, but this paragraph shall in no case relieve such person from liability for interest or any penalties or additions to the tax otherwise applicable in respect of such failure to deduct and withhold. (4) Refunds and credits with respect to withheld tax Where there has been an overpayment of tax under this chapter, any refund or credit made under chapter 65 shall be made to the withholding agent unless the amount of such tax was actually withheld by the withholding agent. .\n##### (b) Exclusion from definition of capital asset\nSection 1221(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (7), by striking or at the end,\n**(2)**\nin paragraph (8), by striking the period at the end and inserting ; or , and\n**(3)**\nby adding at the end the following new paragraph:\n(9) any financial arrangement created by, or any proceeds derived from, a litigation financing agreement (as defined under section 5000E\u20132). .\n##### (c) Removal from gross income\nPart III of subchapter B of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 139I the following new section:\n139J. Qualified litigation proceeds Gross income shall not include any qualified litigation proceeds (as defined in section 5000E\u20132). .\n##### (d) Clerical amendments\n**(1)**\nSection 7701(a)(16) of the Internal Revenue Code of 1986 is amended by inserting 5000E\u20133(c)(1), before 1441 .\n**(2)**\nThe table of chapters for subtitle D of the Internal Revenue Code of 1986 is amended by inserting after the item relating to chapter 50A the following new item:\nChapter 50B\u2014Litigation Financing .\n**(3)**\nThe table of sections for part III of subchapter B of chapter 1 of such Code is amended by inserting after the item relating to section 139I the following new item:\nSec. 139J. Qualified litigation proceeds. .\n##### (e) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-05-20",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "3512",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Tackling Predatory Litigation Funding Act",
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
        "updateDate": "2025-06-06T20:39:01Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1821is.xml"
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
      "title": "Tackling Predatory Litigation Funding Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tackling Predatory Litigation Funding Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-29T01:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a tax on income from litigation which is received by third-party entities that provided financing for such litigation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-29T01:18:34Z"
    }
  ]
}
```
