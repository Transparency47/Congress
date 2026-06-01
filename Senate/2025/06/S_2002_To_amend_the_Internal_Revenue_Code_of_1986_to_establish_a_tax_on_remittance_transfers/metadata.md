# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2002?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2002
- Title: REMIT Act
- Congress: 119
- Bill type: S
- Bill number: 2002
- Origin chamber: Senate
- Introduced date: 2025-06-10
- Update date: 2025-12-10T21:49:00Z
- Update date including text: 2025-12-10T21:49:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in Senate
- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-10: Introduced in Senate

## Actions

- 2025-06-10 - IntroReferral: Introduced in Senate
- 2025-06-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2002",
    "number": "2002",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001227",
        "district": "",
        "firstName": "Eric",
        "fullName": "Sen. Schmitt, Eric [R-MO]",
        "lastName": "Schmitt",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "REMIT Act",
    "type": "S",
    "updateDate": "2025-12-10T21:49:00Z",
    "updateDateIncludingText": "2025-12-10T21:49:00Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-10",
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
      "actionDate": "2025-06-10",
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
          "date": "2025-06-10T15:11:31Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2002is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2002\nIN THE SENATE OF THE UNITED STATES\nJune 10, 2025 Mr. Schmitt introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a tax on remittance transfers.\n#### 1. Short title\nThis Act may be cited as the Requiring Excise for Migrant Income Transfers Act or the REMIT Act .\n#### 2. Excise tax on remittance transfers\n##### (a) In general\nChapter 36 of the Internal Revenue Code of 1986 is amended by inserting after subchapter B the following new subchapter:\nC Remittance transfers Sec. 4475. Imposition of tax. 4475. Imposition of tax (a) In general There is hereby imposed on any remittance transfer a tax equal to 15 percent of the amount of such transfer. (b) Payment of tax (1) In general The tax imposed by this section with respect to any remittance transfer shall be paid by the sender with respect to such transfer. (2) Collection The remittance transfer provider with respect to any remittance transfer shall collect the amount of the tax imposed under subsection (a) with respect to such transfer from the sender and remit such tax quarterly to the Secretary at such time and in such manner as provided by the Secretary. (3) Secondary liability Where any tax imposed by subsection (a) is not paid at the time the transfer is made, then to the extent that such tax is not collected, such tax shall be paid by the remittance transfer provider. (c) Exception for remittance transfers sent by citizens and nationals of the united states through certain providers (1) In general Subsection (a) shall not apply to any remittance transfer with respect to which the remittance transfer provider is a qualified remittance transfer provider and the sender is a verified United States sender. (2) Qualified remittance transfer provider For purposes of this subsection, the term qualified remittance transfer provider means any remittance transfer provider which enters into a written agreement with the Secretary pursuant to which such provider agrees to verify the status of senders as citizens or nationals of the United States in such manner, and in accordance with such procedures, as the Secretary may specify. (3) Verified united states sender For purposes of this subsection, the term verified United States sender means any sender who is verified by a qualified remittance transfer provider as being a citizen or national of the United States pursuant to an agreement described in paragraph (2). (d) Definitions For purposes of this section, the terms remittance transfer , remittance transfer provider , designated recipient , and sender shall each have the respective meanings given such terms by section 920(g) of the Electronic Fund Transfer Act ( 15 U.S.C. 1693o-1 ; relating to Remittance Transfers ). (e) Application of anti-Conduit rules For purposes of section 7701(l) with respect to any multiple-party arrangements involving the sender, a remittance transfer shall be treated as a financing transaction. .\n##### (b) Refundable income tax credit allowed to citizens and nationals of the united states for excise tax on remittance transfers\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36B the following new section:\n36C. Credit for excise tax on remittance transfers of citizens and nationals of the united states (a) In general In the case of any individual, there shall be allowed as a credit against the tax imposed by this subtitle for any taxable year an amount equal to the aggregate amount of taxes paid by such individual under section 4475 during such taxable year. (b) Social security number requirement (1) In general No credit shall be allowed under this section unless the taxpayer includes on the return of tax for the taxable year\u2014 (A) the individual's social security number, and (B) if the individual is married, the social security number of such individuals's spouse. (2) Social security number For purposes of this subsection, the term social security number has the meaning given such term in section 24(h)(7). (3) Married individuals Rules similar to the rules of section 32(d) shall apply to this section. (c) Substantiation requirements No credit shall be allowed under this section unless the taxpayer demonstrates to the satisfaction of the Secretary that the tax under section 4475 with respect to which such credit is determined\u2014 (1) was paid by the taxpayer, and (2) is with respect to a remittance transfer with respect to which the taxpayer provided to the remittance transfer provider the certification and information referred to in section 6050BB(a)(2). (d) Definitions Any term used in this section which is also used in section 4475 shall have the meaning given such term in section 4475. (e) Application of anti-Conduit rules For rules providing for the application of the anti-conduit rules of section 7701(l) to remittance transfers, see section 4475(e). .\n##### (c) Reporting by remittance transfer providers\n**(1) In general**\nSubpart B of part III of subchapter A of chapter 61 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n6050AA. Returns relating to remittance transfers (a) In general Each remittance transfer provider shall make a return at such time as the Secretary may provide setting forth\u2014 (1) in the case of a qualified remittance transfer provider with respect to remittance transfers to which section 4475(a) does not apply by reason of section 4475(c), the aggregate number and value of such transfers, (2) in the case of any remittance transfer not described in paragraph (1) and with respect to which the sender certifies to the remittance transfer provider an intent to claim the credit under section 36C and provides the information described in paragraph (1)\u2014 (A) the name, address, and social security number of the sender, (B) the amount of tax paid by the sender under section 4475(b)(1), and (C) the amount of tax remitted by the remittance transfer provider under section 4475(b)(2), and (3) in the case of any remittance transfer not included under paragraph (1) or (2)\u2014 (A) the aggregate amount of tax paid under section 4475(b)(1) with respect to such transfers, and (B) the aggregate amount of tax remitted under section 4475(b)(2) with respect to such transfers. (b) Statement To be furnished to named persons Every person required to make a return under subsection (a) shall furnish, at such time as the Secretary may provide, to each person whose name is required to be set forth in such return a written statement showing\u2014 (1) the name and address of the information contact of the required reporting person, and (2) the information described in subsection (a)(2) which relates to such person. (c) Definitions Any term used in this section which is also used in section 4475 shall have the meaning given such term in such section. .\n**(2) Penalties**\nSection 6724(d) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin paragraph (1)(B), by striking or at the end of clause (xxvii), by striking and at the end of clause (xxviii) and inserting or , and by adding at the end the following new clause:\n(xxix) section 6050BB(a) (relating to returns relating to remittance transfers), , and\n**(B)**\nin paragraph (2), by striking or at the end of subparagraph (KK), by striking the period at the end of subparagraph (LL) and inserting , or , and by inserting after subparagraph (LL) the following new subparagraph:\n(MM) section 6050BB(b) (relating to statements relating to remittance transfers). .\n##### (d) Conforming amendments\n**(1)**\nSection 6211(b)(4)(A) of the Internal Revenue Code of 1986 is amended by inserting 36C, after 36B, .\n**(2)**\nSection 6213(g)(2) of such Code is amended by striking and at the end of subparagraph (U), by striking the period at the end of subparagraph (V) and inserting , and , and by inserting after subparagraph (V) the following new subparagraph:\n(W) an omission of a correct social security number under section 36C(b) to be included on a return. .\n**(3)**\nSection 1324(b)(2) of title 31, United States Code, is amended by inserting 36C, after 36B, .\n**(4)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Credit for excise tax on remittance transfers of citizens and nationals of the United States. .\n**(5)**\nThe table of sections for subpart B of part III of subchapter A of chapter 61 of such Code is amended by adding at the end the following new item:\nSec. 6050AA. Returns relating to remittance transfers. .\n**(6)**\nThe table of subchapters for chapter 36 of such Code is amended by inserting after the item relating to subchapter B the following new item:\nSubchapter c\u2014Remittance transfers .\n##### (e) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to transfers made after December 31, 2025.\n**(2) Tax credit**\nThe amendments made by subsection (b), and paragraphs (1) through (4) of subsection (d), shall apply to taxable years ending after December 31, 2025.",
      "versionDate": "2025-06-10",
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
        "actionDate": "2025-09-26",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5595",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Requiring Excise for Migrant Income Transfers Act\u201d or the \u201cREMIT Act.",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-07-04",
        "text": "Became Public Law No: 119-21."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "An act to provide for reconciliation pursuant to title II of H. Con. Res. 14.",
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
        "updateDate": "2025-06-30T17:54:56Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2002is.xml"
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
      "title": "REMIT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T03:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REMIT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Requiring Excise for Migrant Income Transfers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-19T03:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to establish a tax on remittance transfers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-19T03:33:21Z"
    }
  ]
}
```
