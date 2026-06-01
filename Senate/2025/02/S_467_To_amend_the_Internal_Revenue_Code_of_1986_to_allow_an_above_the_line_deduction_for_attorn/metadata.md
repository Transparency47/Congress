# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/467?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/467
- Title: End Double Taxation of Successful Consumer Claims Act
- Congress: 119
- Bill type: S
- Bill number: 467
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-05-19T17:42:43Z
- Update date including text: 2026-05-19T17:42:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/467",
    "number": "467",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "End Double Taxation of Successful Consumer Claims Act",
    "type": "S",
    "updateDate": "2026-05-19T17:42:43Z",
    "updateDateIncludingText": "2026-05-19T17:42:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T19:51:47Z",
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
      "bioguideId": "M001111",
      "firstName": "Patty",
      "fullName": "Sen. Murray, Patty [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Murray",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "WA"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NH"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "VA"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "CO"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-02-06",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s467is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 467\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Ms. Cortez Masto (for herself, Mrs. Murray , Mrs. Shaheen , Mr. Kaine , Mr. Bennet , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for attorney fees and costs in connection with consumer claim awards.\n#### 1. Short title\nThis Act may be cited as the End Double Taxation of Successful Consumer Claims Act .\n#### 2. Above-the-line deduction for attorney fees and costs in connection with consumer claim awards\n##### (a) In general\nThe first sentence of paragraph (20) of section 62(a) of the Internal Revenue Code of 1986 is amended by inserting or a claim of a consumer protection violation (as defined in subsection (f)) after section 1862(b)(3)(A) of the Social Security Act ( 42 U.S.C. 1395y(b)(3)(A) ) .\n##### (b) Consumer protection violation defined\nSection 62 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(f) Consumer protection violation defined For purposes of subsection (a)(20), the term consumer protection violation means an act that is unlawful under any of the following: (1) Section 987 of title 10, United States Code. (2) Section 6, 8, or 9 of the Real Estate Settlement Procedures Act of 1974 ( 12 U.S.C. 2605 , 2607, or 2608). (3) The Expedited Funds Availability Act ( 12 U.S.C. 4001 et seq. ). (4) The Homeowners Protection Act of 1998 ( 12 U.S.C. 4901 et seq. ). (5) The Truth in Lending Act ( 15 U.S.C. 1601 et seq. ). (6) The Credit Repair Organizations Act ( 15 U.S.C. 1679 et seq. ). (7) The Fair Credit Reporting Act ( 15 U.S.C. 1681 et seq. ). (8) The Equal Credit Opportunity Act ( 15 U.S.C. 1691 et seq. ). (9) The Fair Debt Collection Practices Act ( 15 U.S.C. 1692 et seq. ). (10) The Electronic Fund Transfer Act ( 15 U.S.C. 1693 et seq. ). (11) The Interstate Land Sales Full Disclosure Act ( 15 U.S.C. 1701 et seq. ). (12) The Consumer Product Safety Act ( 15 U.S.C. 2051 et seq. ). (13) The Magnuson-Moss Warranty-Federal Trade Commission Improvement Act ( 15 U.S.C. 2301 et seq. ). (14) The Servicemembers Civil Relief Act ( 50 U.S.C. 3901 et seq. ). (15) Any provision of Federal law prohibiting unfair or deceptive trade or credit practices. (16) Any provision of Federal, State, or local law, or common law claims permitted under Federal, State, or local law\u2014 (A) providing for the enforcement of consumer protection, or (B) regulating any aspect of consumer transactions, including claims for unfair, deceptive, or abusive trade or credit practices, or for other actions that cause harm to an individual by a seller or provider of property, services, securities or other investments, money, or credit for personal, family, or household use. .\n##### (c) Effective date\nThe amendments made by this section shall apply to attorney fees and court costs paid during taxable years ending after the date of the enactment of this Act with respect to any judgment or settlement occurring during such taxable years.",
      "versionDate": "2025-02-06",
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
        "updateDate": "2025-05-05T17:02:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-06",
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
          "measure-id": "id119s467",
          "measure-number": "467",
          "measure-type": "s",
          "orig-publish-date": "2025-02-06",
          "originChamber": "SENATE",
          "update-date": "2026-05-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s467v00",
            "update-date": "2026-05-19"
          },
          "action-date": "2025-02-06",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>End Double Taxation of Successful Consumer Claims Act</strong></p><p>This bill allows an above-the-line tax deduction for court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment for a claim related to\u00a0certain consumer protection violations, subject to limitations. (An above-the-line deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment are included in the individual\u2019s gross income, even if such attorney\u2019s fees are contingent upon the outcome of the claim or paid directly to the individual\u2019s attorney. (Some exceptions apply.) However, under current law, an above-the-line tax deduction is allowed for court costs and attorney\u2019s fees awarded in connection with certain employment and civil rights discrimination claims.</p><p>This bill expands the above-the-line tax deduction for court costs and attorney\u2019s fees paid in connection with certain discrimination claims to include court costs and attorney\u2019s fees awarded as part of a settlement or judgment in a claim for</p><ul><li>unfair, deceptive, or abusive trade or credit practices;</li><li>harm to an individual by a seller or provider of property, services, securities or other investments, money, or credit; or</li><li>certain other consumer protection violations.</li></ul><p>The deduction is allowed to the extent that such amounts are includible in the individual's gross income.\u00a0\u00a0</p>"
        },
        "title": "End Double Taxation of Successful Consumer Claims Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s467.xml",
    "summary": {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>End Double Taxation of Successful Consumer Claims Act</strong></p><p>This bill allows an above-the-line tax deduction for court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment for a claim related to\u00a0certain consumer protection violations, subject to limitations. (An above-the-line deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment are included in the individual\u2019s gross income, even if such attorney\u2019s fees are contingent upon the outcome of the claim or paid directly to the individual\u2019s attorney. (Some exceptions apply.) However, under current law, an above-the-line tax deduction is allowed for court costs and attorney\u2019s fees awarded in connection with certain employment and civil rights discrimination claims.</p><p>This bill expands the above-the-line tax deduction for court costs and attorney\u2019s fees paid in connection with certain discrimination claims to include court costs and attorney\u2019s fees awarded as part of a settlement or judgment in a claim for</p><ul><li>unfair, deceptive, or abusive trade or credit practices;</li><li>harm to an individual by a seller or provider of property, services, securities or other investments, money, or credit; or</li><li>certain other consumer protection violations.</li></ul><p>The deduction is allowed to the extent that such amounts are includible in the individual's gross income.\u00a0\u00a0</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119s467"
    },
    "title": "End Double Taxation of Successful Consumer Claims Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-06",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>End Double Taxation of Successful Consumer Claims Act</strong></p><p>This bill allows an above-the-line tax deduction for court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment for a claim related to\u00a0certain consumer protection violations, subject to limitations. (An above-the-line deduction is subtracted from gross income to calculate adjusted gross income.)</p><p>Under current law, court costs and attorney\u2019s fees awarded to an individual as part of a settlement or judgment are included in the individual\u2019s gross income, even if such attorney\u2019s fees are contingent upon the outcome of the claim or paid directly to the individual\u2019s attorney. (Some exceptions apply.) However, under current law, an above-the-line tax deduction is allowed for court costs and attorney\u2019s fees awarded in connection with certain employment and civil rights discrimination claims.</p><p>This bill expands the above-the-line tax deduction for court costs and attorney\u2019s fees paid in connection with certain discrimination claims to include court costs and attorney\u2019s fees awarded as part of a settlement or judgment in a claim for</p><ul><li>unfair, deceptive, or abusive trade or credit practices;</li><li>harm to an individual by a seller or provider of property, services, securities or other investments, money, or credit; or</li><li>certain other consumer protection violations.</li></ul><p>The deduction is allowed to the extent that such amounts are includible in the individual's gross income.\u00a0\u00a0</p>",
      "updateDate": "2026-05-19",
      "versionCode": "id119s467"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s467is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to allow an above-the-line deduction for attorney fees and costs in connection with consumer claim awards.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:28Z"
    },
    {
      "title": "End Double Taxation of Successful Consumer Claims Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:33Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "End Double Taxation of Successful Consumer Claims Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:26Z"
    }
  ]
}
```
