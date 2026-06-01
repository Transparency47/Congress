# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1613?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1613
- Title: Tax Relief for New Businesses Act
- Congress: 119
- Bill type: S
- Bill number: 1613
- Origin chamber: Senate
- Introduced date: 2025-05-06
- Update date: 2025-06-06T18:07:50Z
- Update date including text: 2025-06-06T18:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-06: Introduced in Senate
- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-06: Introduced in Senate

## Actions

- 2025-05-06 - IntroReferral: Introduced in Senate
- 2025-05-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-06",
    "latestAction": {
      "actionDate": "2025-05-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1613",
    "number": "1613",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Tax Relief for New Businesses Act",
    "type": "S",
    "updateDate": "2025-06-06T18:07:50Z",
    "updateDateIncludingText": "2025-06-06T18:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-06",
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
      "actionDate": "2025-05-06",
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
          "date": "2025-05-06T16:34:32Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NH"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "WI"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "OR"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "CT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "NM"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "DE"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MI"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-05-06",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1613is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1613\nIN THE SENATE OF THE UNITED STATES\nMay 6, 2025 Ms. Rosen (for herself, Mrs. Shaheen , Ms. Baldwin , Mr. Wyden , Mr. Blumenthal , Ms. Klobuchar , Mr. Heinrich , Mr. Coons , Ms. Slotkin , Mr. Gallego , and Ms. Alsobrooks ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the limitations for deductible new business expenditures, to consolidate provisions for start-up and organizational expenditures, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Tax Relief for New Businesses Act .\n#### 2. New business expenditures\n##### (a) Consolidation of deduction for start-Up and organizational expenditures\n**(1) In general**\nSection 195(a) of the Internal Revenue Code of 1986 is amended by inserting or organizational after start-up .\n**(2) Organizational expenditures**\nSubsection (c) of section 195 of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(3) Organizational expenditures The term organizational expenditures means any expenditure which\u2014 (A) is incident to the creation of a corporation or a partnership, (B) is chargeable to capital account, and (C) is of a character which, if expended incident to the creation of a corporation or a partnership having a limited life, would be amortizable over such life. .\n**(3) Conforming amendments**\n**(A)**\nSection 195(b)(1) is amended\u2014\n**(i)**\nby striking with respect to any start-up expenses and inserting with respect to any active trade or business ,\n**(ii)**\nby striking the amount of start-up expenditures with respect to in subparagraph (A)(i) thereof and inserting the aggregate amount of start-up and organizational expenditures paid in connection with , and\n**(iii)**\nby adding at the end the following flush sentence:\nIn the case of a partnership or S corporation, the election under the preceding sentence shall be made at the entity level. .\n**(B)**\nSection 195(b)(2) of such Code is amended\u2014\n**(i)**\nby striking amortization period.\u2014 In any case and inserting the following:\namortization period.\u2014 (A) In general In any case , and\n**(ii)**\nby adding at the end the following new subparagraph:\n(B) Special partnership rule In the case of a partnership or S corporation, subparagraph (A) shall be applied at the entity level. .\n**(C)**\nSection 195(b) of such Code is amended by striking paragraph (3).\n**(D)**\n**(i)**\nPart VIII of subchapter B of chapter 1 of such Code is amended by striking section 248 (and by striking the item relating to such section in the table of sections for such part).\n**(ii)**\nSection 170(b)(2)(C)(ii) of such Code is amended by striking (except section 248) .\n**(iii)**\nSection 312(n)(3) of such Code is amended by striking Sections 173 and 248 and inserting Section 173 .\n**(iv)**\nSection 535(b)(3) of such Code is amended by striking (except section 248) .\n**(v)**\nParagraphs (3) and (4) of section 545(b) of such Code are each amended by striking (except section 248) .\n**(vi)**\nSection 834(c)(7) of such Code is amended by striking (except section 248) .\n**(vii)**\nSection 852(b)(2)(C) of such Code is amended by striking (except section 248) .\n**(viii)**\nSection 857(b)(2)(A) of such Code is amended by striking (except section 248) .\n**(ix)**\nSection 1363(b) of such Code is amended by inserting and at the end of paragraph (2), by striking paragraph (3), and by redesignating paragraph (4) as paragraph (3).\n**(x)**\nSection 1375(b)(1)(B)(i) of such Code is amended by striking (other than the deduction allowed by section 248, relating to organization expenditures) .\n**(E)**\n**(i)**\nSection 709 of such Code is amended to read as follows:\n709. Treatment of syndication fees No deduction shall be allowed under this chapter to a partnership or to any partner of the partnership for any amounts paid or incurred to promote the sale of (or to sell) an interest in the partnership. .\n**(ii)**\nThe item relating to section 709 in the table of sections for part I of subchapter K of chapter 1 of such Code is amended to read as follows:\nSec. 709. Treatment of syndication fees. .\n**(F)**\nThe heading of section 195 of such Code (and the item relating to such section in the table of sections for part VI of subchapter B of chapter 1 of such Code) are each amended by inserting and organizational after Start-up .\n##### (b) Increase in limitation\nClause (ii) of section 195(b)(1)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking $5,000 and inserting $50,000 , and\n**(2)**\nby striking $50,000 and inserting $150,000 .\n##### (c) Application of net operating loss rules\nSection 172 of the Internal Revenue Code of 1986 is amended by redesignating subsection (g) as subsection (h) and by inserting after subsection (f) the following new subsection:\n(g) Special rules for start-Up and organizational expenditures (1) In general In the case of a taxpayer making an election under this subsection\u2014 (A) this section shall be applied separately to start-up and organizational net operating losses and other net operating losses, (B) in applying this section to start-up and organizational net operating losses\u2014 (i) subsection (a)(2)(B) shall be applied by substituting 100 percent for 80 percent in clause (i) thereof, and (ii) subsection (b)(2)(C) shall not apply, and (C) in applying this section to other net operating losses, for purposes of subsections (a)(2)(B)(ii)(I) and (b)(2), taxable income shall be reduced by the amount of the deduction allowed under this section with respect to start-up and organizational net operating losses. (2) Start-up and organizational net operating loss For purposes of this section, the term start-up and organizational net operating loss means the amount which would be a net operating loss if the only deduction taken into account were the deduction allowed under section 195. (3) Other net operating losses For purposes of this section, the term other net operating loss means the net operating loss determined without regard to the deduction allowed under section 195. (4) Election An election under this section shall be made at such time and in such form and manner as the Secretary shall prescribe. Such an election, once made, shall be irrevocable. .\n##### (d) Effective date\nThe amendments made by this section shall apply to expenses paid or incurred in taxable years beginning after December 31, 2025.",
      "versionDate": "2025-05-06",
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
        "updateDate": "2025-06-06T18:07:50Z"
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
      "date": "2025-05-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1613is.xml"
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
      "title": "Tax Relief for New Businesses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T03:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Tax Relief for New Businesses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T03:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitations for deductible new business expenditures, to consolidate provisions for start-up and organizational expenditures, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T03:48:25Z"
    }
  ]
}
```
