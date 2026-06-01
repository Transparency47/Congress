# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4287
- Title: GRATS Act
- Congress: 119
- Bill type: S
- Bill number: 4287
- Origin chamber: Senate
- Introduced date: 2026-04-14
- Update date: 2026-04-21T03:32:31Z
- Update date including text: 2026-04-21T03:32:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-14: Introduced in Senate
- 2026-04-14 - IntroReferral: Introduced in Senate
- 2026-04-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-04-14: Introduced in Senate

## Actions

- 2026-04-14 - IntroReferral: Introduced in Senate
- 2026-04-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-14",
    "latestAction": {
      "actionDate": "2026-04-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4287",
    "number": "4287",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000779",
        "district": "",
        "firstName": "Ron",
        "fullName": "Sen. Wyden, Ron [D-OR]",
        "lastName": "Wyden",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "GRATS Act",
    "type": "S",
    "updateDate": "2026-04-21T03:32:31Z",
    "updateDateIncludingText": "2026-04-21T03:32:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-14",
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
      "actionDate": "2026-04-14",
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
          "date": "2026-04-14T18:19:47Z",
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
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-14",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4287is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4287\nIN THE SENATE OF THE UNITED STATES\nApril 14, 2026 Mr. Wyden (for himself and Mr. King ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to modify rules for grantor trusts.\n#### 1. Short title\nThis Act may be cited as the Getting Rid of Abusive Trust Schemes Act or the GRATS Act .\n#### 2. Required minimum 15-year term, etc., for grantor retained annuity trusts\n##### (a) In general\nSubsection (b) of section 2702 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), and (3) as subparagraphs (A), (B), and (C), respectively, and by moving such subparagraphs (as so redesignated) 2 ems to the right,\n**(2)**\nby striking For purposes of and inserting the following:\n(1) In general For purposes of ,\n**(3)**\nby striking paragraph (1) or (2) in paragraph (1)(C) (as so redesignated) and inserting subparagraph (A) or (B) , and\n**(4)**\nby adding at the end the following new paragraph:\n(2) Additional requirements with respect to grantor retained annuity trusts For purposes of subsection (a), in the case of an interest described in paragraph (1)(A) (determined without regard to this paragraph) which is retained by the transferor, such interest shall be treated as described in such paragraph only if\u2014 (A) the right to receive the fixed amounts referred to in such paragraph is for a term of not less than 15 years and not more than the life expectancy of the annuitant plus 10 years, (B) such fixed amounts, when determined on an annual basis, do not decrease during the term described in subparagraph (A), and (C) the remainder interest has a value, as determined as of the time of the transfer, which is\u2014 (i) not less than an amount equal to the greater of\u2014 (I) 25 percent of the fair market value of the property transferred to the trust, or (II) $500,000, and (ii) not greater than the fair market value of the property transferred to the trust. .\n##### (b) Effective dates\nThe amendments made by this section shall apply\u2014\n**(1)**\nto trusts created on or after the date of enactment of this Act, and\n**(2)**\nto any portion of a trust established before the date of the enactment of this Act which is attributable to a contribution made on or after such date.\n#### 3. Certain transfers between grantor trust and deemed owner\n##### (a) In general\nPart IV of subchapter O of chapter 1 of the Internal Revenue Code of 1986 is amended by redesignating section 1063 as section 1064 and inserting after section 1062 the following new section:\n1063. Certain transfers between grantor trust and deemed owner (a) In general In the case of any transfer of property for consideration between a trust and a person who is a deemed owner of the trust, such transfer shall be treated as a sale or exchange for purposes of this chapter regardless of the fact that such person is a deemed owner of such trust. (b) Exception Subsection (a) shall not apply to\u2014 (1) any grantor trust which is fully revocable by the deemed owner, (2) any asset-backed securities trust, or (3) any grantor trust which is identified by the Secretary (pursuant to regulations or other guidance) as appropriate to exclude from the application of subsection (a). (c) Definitions For purposes of this section\u2014 (1) Asset-backed securities trust (A) In general The term asset-backed securities trust means any grantor trust\u2014 (i) for which the assets of the trust are mortgage-backed securities or other asset-backed securities, and (ii) which is engaged in securitization transactions. (B) Exception The term asset-backed securities trust shall not include any grantor trust identified by the Secretary (pursuant to regulations or other guidance) as appropriate to exclude from the application of subsection (b)(2). (2) Deemed owner The term deemed owner means, with respect to any trust, any person who is treated as the owner of such trust (or a portion thereof) under subpart E of part 1 of subchapter J. (d) Rule of construction For purposes of subsection (a), a transfer of property for consideration shall include\u2014 (1) any satisfaction of an annuity, or (2) any discharge of debt, by the trust in kind. .\n##### (b) Related taxpayers\nSection 267(b) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking or at the end of paragraph (12),\n**(2)**\nby striking the period at the end of paragraph (13) and inserting ; or , and\n**(3)**\nby adding at the end the following new paragraph:\n(14) A grantor trust and the person treated as the owner of the trust (or portion thereof) under subpart E of part 1 of subchapter J of this chapter. .\n##### (c) Clerical amendments\nThe table of sections for part IV of subchapter O of chapter 1 of the Internal Revenue Code of 1986 is amended by striking the item relating to section 1063 and inserting the following new items:\nSec. 1063. Certain sales to grantor trusts. Sec. 1064. Cross references. .\n##### (d) Effective dates\nThe amendments made by this section shall apply to transfers made after the date of the enactment of this Act.\n#### 4. Payment of tax on income of grantor trust\n##### (a) In general\nSection 2503 of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin subsection (a), by striking The term and inserting Subject to subsection (d), the term , and\n**(2)**\nby inserting after subsection (c) the following:\n(d) Payment of tax on income of grantor trust (1) In general Notwithstanding subsections (b) and (e), an amount equal to the taxes paid on the income of an applicable grantor trust for any calendar year by a person who is the deemed owner of such trust (or portion thereof) shall be treated for purposes of this subtitle as a taxable gift made during such calendar year. (2) Applicable grantor trust For purposes of this subsection, the term applicable grantor trust means any trust\u2014 (A) with respect to which the taxpayer is considered an owner under subpart E of part I of subchapter J of chapter 1, and (B) which is not fully revocable by the taxpayer. (3) Reimbursement by trust Paragraph (1) shall not apply with respect to any amount paid by the deemed owner for any calendar year which is reimbursed by the applicable grantor trust during such calendar year. (4) Date of gift In the case of any amount treated for purposes of this subtitle as a taxable gift pursuant to paragraph (1), such gift shall be deemed to have occurred on the earlier of\u2014 (A) December 31 of the calendar year for which the tax is paid by the person who is the deemed owner, (B) the day before the date of the death of such person, or (C) the date on which such person renounces any right of reimbursement by the applicable grantor trust with respect to the calendar year for which the tax is paid by such person. (5) Deemed owner For purposes of this subsection, the term deemed owner has the same meaning given such term under section 1063(c). .\n##### (b) Conforming amendments\n**(1)**\nSection 2522 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby redesignating subsection (f) as subsection (g), and\n**(B)**\nby inserting after subsection (e) the following new subsection:\n(f) Denial of deduction for payment of tax on income of grantor trust No deduction shall be allowed under this section for any amount which is treated as a gift by reason of section 2503(d). .\n**(2)**\nSection 2523 of such Code is amended by adding at the end the following new subsection:\n(j) Denial of deduction for payment of tax on income of grantor trust No deduction shall be allowed under this section for any amount which is treated as a gift by reason of section 2503(d). .\n##### (c) Effective dates\nThe amendments made by this section shall apply to trusts created on or after the date of enactment of this Act.",
      "versionDate": "2026-04-14",
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
        "updateDate": "2026-04-21T03:32:31Z"
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
      "date": "2026-04-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4287is.xml"
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
      "title": "GRATS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T02:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "GRATS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Getting Rid of Abusive Trust Schemes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to modify rules for grantor trusts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:40Z"
    }
  ]
}
```
