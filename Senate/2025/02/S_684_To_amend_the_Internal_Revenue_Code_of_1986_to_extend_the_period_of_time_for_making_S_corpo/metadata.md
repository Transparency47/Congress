# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/684?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/684
- Title: Tax Administration Simplification Act
- Congress: 119
- Bill type: S
- Bill number: 684
- Origin chamber: Senate
- Introduced date: 2025-02-24
- Update date: 2025-12-17T12:03:15Z
- Update date including text: 2025-12-17T12:03:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-24: Introduced in Senate
- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-24: Introduced in Senate

## Actions

- 2025-02-24 - IntroReferral: Introduced in Senate
- 2025-02-24 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-24",
    "latestAction": {
      "actionDate": "2025-02-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/684",
    "number": "684",
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
    "title": "Tax Administration Simplification Act",
    "type": "S",
    "updateDate": "2025-12-17T12:03:15Z",
    "updateDateIncludingText": "2025-12-17T12:03:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-24",
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
      "actionDate": "2025-02-24",
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
          "date": "2025-02-24T20:30:40Z",
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
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-02-24",
      "state": "NV"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s684is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 684\nIN THE SENATE OF THE UNITED STATES\nFebruary 24, 2025 Mrs. Blackburn (for herself and Ms. Cortez Masto ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the period of time for making S corporation elections, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Administration Simplification Act .\n#### 2. Extension of time for making S corporation elections\n##### (a) In general\n**(1) When election made**\nSection 1362(b)(1) of the Internal Revenue Code of 1986 is amended to read as follows:\n(1) In general An election under subsection (a) may be made by a small business corporation for any taxable year not later than the due date for filing the return of the S corporation for such taxable year (including extensions). .\n**(2) Conforming amendments**\n**(A)**\nSection 1362(b)(2) of such Code is amended\u2014\n**(i)**\nby striking during such year and on or before the 15th day of the 3d month of such year in subparagraph (A) and inserting within the period described in paragraph (1) , and\n**(ii)**\nby striking made during the first 2 \u00bd months in the heading thereof.\n**(B)**\nSection 1362(b) of such Code is amended by striking paragraphs (3) and (4) and by redesignating paragraph (5) as paragraph (3).\n**(C)**\nSection 1362(b)(3) of such Code, as redesignated by subparagraph (B), is amended\u2014\n**(i)**\nby striking (determined without regard to paragraph (3)) in subparagraph (A), and\n**(ii)**\nby striking (and paragraph (3) shall not apply) .\n**(D)**\nSection 1362(b) of such Code, as amended by the preceding provisions of this subsection, is amended by adding at the end the following new paragraphs:\n(4) Election on timely filed returns Except as otherwise provided by the Secretary, an election under subsection (a) for any taxable year may be made on a timely filed return of the S corporation for such taxable year. (5) Secretarial authority The Secretary may prescribe such regulations, rules, or other guidance necessary to implement this subsection, including forms or other guidance for making the election in the manner described by this subsection. .\n##### (b) Coordination with certain other provisions\n**(1) Qualified subchapter S subsidiaries**\nSection 1361(b)(3)(B) of the Internal Revenue Code of 1986 is amended by adding at the end the following flush sentence:\nRules similar to the rules of section 1362(b) shall apply with respect to any election under clause (ii). .\n**(2) Qualified subchapter S trusts**\nSection 1361(d)(2) of such Code is amended by striking subparagraph (D).\n##### (c) Revocations\nSection 1362(d)(1) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking subparagraph (D) in subparagraph (C) and inserting subparagraphs (D) and (E) , and\n**(2)**\nby adding at the end the following new subparagraph:\n(E) Authority to treat late revocations as timely If\u2014 (i) a revocation under subparagraph (A) is made for any taxable year after the date prescribed by this paragraph for making such revocation for such taxable year or no such revocation is made for any taxable year, and (ii) the Secretary determines that there was reasonable cause for the failure to timely make such revocation, the Secretary may treat such a revocation as timely made for such taxable year. .\n##### (d) Effective date\n**(1) In general**\nExcept as otherwise provided in this subsection, the amendments made by this section shall apply to elections for taxable years beginning after the last day of the calendar year which includes the date of the enactment of this Act.\n**(2) Revocations**\nThe amendments made by subsection (c) shall apply to revocations made after the date of the enactment of this Act.\n#### 3. Quarterly installments for estimated income tax payments by individuals\n##### (a) In general\nThe table contained in section 6654(c)(2) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking June 15 and inserting July 15 , and\n**(2)**\nby striking September 15 and inserting October 15 .\n##### (b) Effective date\nThe amendments made by this section shall apply to installments due in taxable years beginning after the date of the enactment of this Act.\n#### 4. Extension of mailbox rule to electronic submissions and payments\n##### (a) In general\nSection 7502(c) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the heading, by inserting and payment after filing ,\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the heading, by striking ; electronic filing , and\n**(B)**\nby striking and electronic filing , and\n**(3)**\nby adding at the end the following:\n(3) Electronic filing and payment (A) In general In the case of any document which the Secretary has permitted to be filed by electronic means (or, in the case of any payment, which the Secretary has permitted to be made by electronic means), if such document or payment is\u2014 (i) transmitted by the permitted electronic means to the agency, officer, or office to which the document was required to be filed (or payment was required to be made) on or before the prescribed date (or within the period required) with respect to such document or payment, and (ii) received (or, in the case of a payment, received and accounted for) after the prescribed date or period required with respect to such document or payment, the date that such document or payment was transmitted (as described in clause (i)) shall be deemed to be the date that such document was filed or such payment was made. (B) Regulations Not later than the date which is 1 year after the date of enactment of the Tax Administration Simplification Act , the Secretary shall issue such regulations or other guidance as the Secretary determines necessary to carry out the purposes of this paragraph. .\n##### (b) Effective date\nThe amendments made by subsection (a) shall apply to any document or payment sent on or after the date which is 1 year after the date of enactment of this Act.",
      "versionDate": "2025-02-24",
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
        "updateDate": "2025-05-07T19:57:13Z"
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
      "date": "2025-02-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s684is.xml"
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
      "title": "Tax Administration Simplification Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Administration Simplification Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the period of time for making S corporation elections, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:34:03Z"
    }
  ]
}
```
