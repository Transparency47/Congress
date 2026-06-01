# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4346?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4346
- Title: Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4346
- Origin chamber: Senate
- Introduced date: 2026-04-20
- Update date: 2026-05-01T19:11:13Z
- Update date including text: 2026-05-01T19:11:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-04-20: Introduced in Senate
- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2026-04-20: Introduced in Senate

## Actions

- 2026-04-20 - IntroReferral: Introduced in Senate
- 2026-04-20 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-20",
    "latestAction": {
      "actionDate": "2026-04-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4346",
    "number": "4346",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026",
    "type": "S",
    "updateDate": "2026-05-01T19:11:13Z",
    "updateDateIncludingText": "2026-05-01T19:11:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-04-20",
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
          "date": "2026-04-20T21:19:38Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "MO"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4346is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4346\nIN THE SENATE OF THE UNITED STATES\nApril 20, 2026 Mr. Whitehouse (for himself, Mr. Hawley , and Mr. Durbin ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo amend title 11, United States Code, to make the filing of a petition for relief under chapter 11 that is objectively futile or in subjective bad faith a cause for dismissal of the case, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026 .\n#### 2. Conversion or dismissal under chapter 11\nSection 1112 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)(A), by striking within a reasonable period of time and inserting not later than 24 months after the date of the filing of the petition ; and\n**(B)**\nin paragraph (4)\u2014\n**(i)**\nsubparagraph (O), by striking and at the end;\n**(ii)**\nin subparagraph (P), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(Q) with respect to the dismissal of a case under this chapter, the filing of a petition for relief or the continuation of a case under this title that is\u2014 (i) objectively futile; or (ii) in subjective bad faith. ; and\n**(2)**\nby adding at the end the following:\n(g) (1) For the purpose of subsection (b)(4)(Q), the court shall presume that a petition has been filed or that a case is continuing under this title in subjective bad faith if the court determines that the debtor manufactured the venue for the case. (2) The presumption under paragraph (1) may be rebutted only based on clear and convincing evidence. (h) (1) For the purpose of subsection (b)(4)(Q), the court shall conclusively presume that a petition has been filed or that a case is continuing under this title in subjective bad faith if the court determines that\u2014 (A) a purpose or effect of the filing or continuation is to\u2014 (i) gain a tactical litigation advantage; (ii) impose undue delay upon creditors; or (iii) cap the total amount of the liability of the debtor to 2 or more creditors holding protected claims (as defined in section 362(p)(1)) that the debtor or any affiliate has property of value sufficient to pay in full as those claims would come due; (B) during the 4-year period preceding the date of the filing of the petition, the debtor was the subject of, or was formed or organized in connection with, a divisional merger or similar transaction changing the corporate structure of and affecting the financial condition of the debtor or an affiliate; (C) during the 4-year period preceding the date of the filing of the petition, the debtor engaged in a transfer of substantial assets to or for benefit of or incurred substantial obligations from or for the benefit of any insider or affiliate that, notwithstanding subsections (e) through (g) and (j) of section 546, is avoidable under section 544(b) or subsection (a)(1) or (e) of section 548; or (D) the debtor does not have a valid reorganizational purpose. (2) In making a determination under paragraph (1)(D), the court shall consider and give weight to whether any appointed creditors\u2019 committee supports the dismissal of the case. (i) In a determination under subsection (g) or (h), the debtor shall have the burden of proof. .\n#### 3. Limitations on certain stays and injunctions\nSection 105 of title 11, United States Code, is amended by adding at the end the following:\n(e) Notwithstanding subsection (a) of this section, any provision of title 28, the Federal Rules of Bankruptcy Procedure, or any applicable nonbankruptcy law, the court may not issue any order, process, or judgment that has the purpose or effect of overriding or nullifying section 362(b)(27) of this title. .\n#### 4. Automatic stay\nSection 362 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (b)\u2014\n**(A)**\nby redesignating paragraphs (27), (28), and (29) as paragraphs (28), (29), and (30), respectively; and\n**(B)**\nby inserting after paragraph (26) the following:\n(27) under subsection (a) of this section, of the commencement or continuation, including the issuance or employment of process, of a judicial, administrative, or other action or proceeding against an entity that is not a debtor in a case under this title, or any act to obtain or recover property of such entity, on account of or with respect to a protected claim against such entity, the debtor, or the estate (including a protected claim that is property of the debtor or the estate against such entity), if, during the 4-year period preceding the date of the filing of the petition, the debtor was the subject of, or was formed or organized in connection with, a divisional merger, spinoff, corporate restructuring, or other transaction changing the corporate structure of, and affecting the financial condition of, the debtor or an affiliate; ; and\n**(2)**\nby adding at the end the following:\n(p) For the purposes of paragraph (27): (1) The term protected claim means\u2014 (A) a claim that\u2014 (i) is against a nondebtor entity or against property of a nondebtor entity that is alleged to be directly or indirectly liable for a claim described in subparagraph (B) against the debtor; and (ii) arises by reason of\u2014 (I) the nondebtor entity\u2019s ownership of a financial interest in the debtor, a past or present affiliate of the debtor, or a predecessor in interest of the debtor; (II) the nondebtor entity\u2019s involvement in the management of the debtor or a predecessor in interest of the debtor or the nondebtor entity\u2019s service as an officer, director, or employee of the debtor or a related party; (III) the nondebtor entity\u2019s provision of insurance to the debtor or a related party; or (IV) the nondebtor entity\u2019s involvement in a transaction changing the corporate structure, or in a loan or other financial transaction affecting the financial condition, of the debtor or a related party, including\u2014 (aa) involvement in providing financing (debt or equity) or advice to an entity involved in such a transaction; or (bb) acquiring or selling a financial interest in an entity as part of such a transaction; or (B) a claim\u2014 (i) against the debtor or a nondebtor entity or property of the debtor or a nondebtor entity; (ii) relating to injury, contamination, damage, or loss, including any claim for reimbursement, indemnity, contribution, or subrogation; (iii) affecting, directly or indirectly, not fewer than 100 individuals on or after the date of the filing of the petition; (iv) allegedly caused, directly or indirectly, by the presence of, or exposure to, a product, material, or substance designed, marketed, manufactured, sold, modified, extracted, serviced, or in any way used by the debtor or the nondebtor entity; and (v) arising, directly or indirectly, from acts or omissions, of the debtor, a predecessor in interest of the debtor, or a past or present affiliate of the debtor. (2) The term related party has the meaning given the term in section 524(g)(4)(A)(iii). .\n#### 5. Technical amendments\n##### (a) Setoff\nSection 553 of title 11, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (2)(B)(ii), by striking 362(b)(27) and inserting 362(b)(28) ; and\n**(B)**\nin paragraph (3)(C), by striking 362(b)(27) and inserting 362(b)(28) ; and\n**(2)**\nin subsection (b)(1), by striking 362(b)(27) and inserting 362(b)(28) .\n##### (b) Relief that may be granted upon filing petition for recognition\nSection 1519(f) of title 11, United States Code, is amended by striking (27) and inserting (28) .\n##### (c) Relief that may be granted upon recognition\nSection 1521(f) of title 11, United States Code, is amended by striking (27) and inserting (28) .\n#### 6. Application and rule of construction\nThis Act and the amendments made by this Act shall\u2014\n**(1)**\napply with respect to any case under title 11, United States Code, filed or pending on or after the date of enactment of this Act; and\n**(2)**\nnot be construed to affect the validity of any final judgment or order confirming a plan under chapter 11 of title 11, United States Code, that was entered before the date of enactment of this Act.",
      "versionDate": "2026-04-20",
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
        "actionDate": "2026-04-20",
        "text": "Referred to the House Committee on the Judiciary."
      },
      "number": "8393",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-05-01T19:11:13Z"
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
      "date": "2026-04-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4346is.xml"
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
      "title": "Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Consumer Protection and Corporate Accountability in Bankruptcy Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 11, United States Code, to make the filing of a petition for relief under chapter 11 that is objectively futile or in subjective bad faith a cause for dismissal of the case, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:37Z"
    }
  ]
}
```
