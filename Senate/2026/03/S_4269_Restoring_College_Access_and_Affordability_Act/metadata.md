# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4269?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4269
- Title: Restoring College Access and Affordability Act
- Congress: 119
- Bill type: S
- Bill number: 4269
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-30T11:03:21Z
- Update date including text: 2026-04-30T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4269",
    "number": "4269",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "B001277",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Blumenthal, Richard [D-CT]",
        "lastName": "Blumenthal",
        "party": "D",
        "state": "CT"
      }
    ],
    "title": "Restoring College Access and Affordability Act",
    "type": "S",
    "updateDate": "2026-04-30T11:03:21Z",
    "updateDateIncludingText": "2026-04-30T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T21:50:42Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NM"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NJ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "OR"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "MD"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "VA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4269is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4269\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Blumenthal (for himself, Mr. Luj\u00e1n , Mr. Booker , Mr. Merkley , Ms. Alsobrooks , and Mr. Kaine ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo repeal certain student loan provisions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring College Access and Affordability Act .\n#### 2. Loan limits\nSection 81001 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n#### 3. Loan repayment\n##### (a) Loan repayment\nSection 82001 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n##### (b) Deferment; forbearance\nSection 82002 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n##### (c) Public service loan forgiveness\nSection 82004 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n#### 4. Pell Grants\n##### (a) Eligibility\nSection 83001 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n##### (b) Federal Pell Grant exclusion relating to other grant aid\nSection 83004 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n#### 5. Ineligibility based on low earning outcomes\nSection 454(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1087d(c) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking Notwithstanding section 481(b), and inserting the following:\n(A) In General Notwithstanding section 481(b), ;\n**(B)**\nby striking an educational program and inserting a covered educational program ; and\n**(C)**\nby adding at the end the following:\n(B) Covered educational program In this subsection, the term covered educational program means an eligible program under this title that is\u2014 (i) a program of training to prepare students for gainful employment in a recognized occupation (such as a program that awards a certificate or credential), or a program that awards an associate's degree; (ii) a program that awards an associate's degree or a baccalaureate degree; or (iii) a program that awards a graduate or professional degree, or graduate certificate. ;\n**(2)**\nin paragraph (2), by striking An educational program at an institution is described in this paragraph if the program awards an undergraduate degree, graduate or professional degree, or graduate certificate, for which and inserting A covered educational program at an institution is described in this paragraph if the program is a program for which ;\n**(3)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking an educational program and inserting a covered educational program ;\n**(ii)**\nin clause (iii)(I), by striking an educational program that awards a baccalaureate or lesser degree, and inserting a covered educational program described in clause (i) or (ii) of paragraph (1)(B), ; and\n**(iii)**\nin clause (iii)(II), by striking a graduate or professional program, and inserting a covered educational program described in clause (iii) of paragraph (1)(B), ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the matter preceding clause (i), by striking an educational program and inserting a covered educational program ;\n**(ii)**\nin clause (i), in the matter preceding subclause (I), by striking that awards a baccalaureate or lesser degree and inserting that is a covered educational program described in clause (i) or (ii) of paragraph (1)(B), ; and\n**(iii)**\nin clause (ii), in the matter preceding subclause (I), by striking that is a graduate or professional program and inserting that is a covered educational program described in clause (iii) of paragraph (1)(B), ;\n**(4)**\nin paragraph (4)\u2014\n**(A)**\nby striking an educational program and inserting a covered educational program ; and\n**(B)**\nby inserting covered before educational programs ;\n**(5)**\nin paragraph (5)\u2014\n**(A)**\nby striking An educational program and inserting A covered educational program ; and\n**(B)**\nby striking the educational program and inserting the covered educational program ;\n**(6)**\nin paragraph (6)(A)\u2014\n**(A)**\nby striking an educational program and inserting a covered educational program ; and\n**(B)**\nby striking the educational program and inserting the covered educational program , each place the term appears; and\n**(7)**\nin paragraph (7), by striking an educational program and inserting a covered educational program .\n#### 6. Regulatory Relief\n##### (a) Delay of rule relating to borrower defense to repayment\nSection 85001 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n##### (b) Delay of rule relating to closed school discharges\nSection 85002 of the Act titled An Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ; 139 Stat. 72) is repealed and any law or regulation referred to in such section shall be applied as if such section and the amendments made by such section had not been enacted.\n#### 7. Modification of excise tax on endowment income of private colleges and universities\n##### (a) In general\nSubsection (a) of section 4968 of the Internal Revenue Code of 1986 is amended by striking the applicable percentage and inserting 1.4 percent .\n##### (b) Conforming amendments\n**(1)**\nSection 4968 of the Internal Revenue Code of 1986 is amended by striking subsection (b) and by redesignating subsections (c), (d), (e), (f), (g), and (h) as subsections (b), (c), (d), (e), (f), and (g), respectively.\n**(2)**\nSubsection (e) of section 4968 of such Code is amended by striking (c) and (d) and inserting (b) and (c) .\n**(3)**\nParagraph (1) of section 4968(g) of such Code is amended by striking (d) and (f) and inserting (c) and (e) .\n**(4)**\nSubsection (o) of section 6033 of such Code is amended\u2014\n**(A)**\nby striking 4968(c) both places it appears and inserting 4968(b) , and\n**(B)**\nby striking 4968(e) in paragraph (2) thereof and inserting 4968(d) .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-03-26",
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
        "name": "Education",
        "updateDate": "2026-04-21T13:54:28Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4269is.xml"
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
      "title": "Restoring College Access and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring College Access and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-17T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal certain student loan provisions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-17T03:48:25Z"
    }
  ]
}
```
