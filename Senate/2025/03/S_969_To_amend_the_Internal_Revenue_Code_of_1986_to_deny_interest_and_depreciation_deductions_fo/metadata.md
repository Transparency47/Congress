# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/969?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/969
- Title: Stop Predatory Investing Act
- Congress: 119
- Bill type: S
- Bill number: 969
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-01-23T19:39:12Z
- Update date including text: 2026-01-23T19:39:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/969",
    "number": "969",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Stop Predatory Investing Act",
    "type": "S",
    "updateDate": "2026-01-23T19:39:12Z",
    "updateDateIncludingText": "2026-01-23T19:39:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
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
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T22:33:52Z",
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
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "OR"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "WI"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "AZ"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "RI"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-03-11",
      "state": "VT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MN"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "VT"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "CT"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "NJ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-10-27",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s969is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 969\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Warnock (for himself, Ms. Smith , Mr. Wyden , Ms. Baldwin , Ms. Warren , Mr. Gallego , Mr. Reed , Mr. Sanders , Ms. Klobuchar , Mr. Welch , Mr. Blumenthal , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for taxpayers owning 50 or more single family properties.\n#### 1. Short title\nThis Act may be cited as the Stop Predatory Investing Act .\n#### 2. Disallowance of interest deduction for disqualified single family property owners\n##### (a) In general\nSection 163 of the Internal Revenue Code of 1986 is amended by redesignating subsection (n) as subsection (o) and by inserting after subsection (m) the following new subsection:\n(n) Interest paid by certain disqualified single family property owners (1) In general In the case of a disqualified single family property owner, no deduction shall be allowed under this chapter for any interest paid or accrued in connection with any single family residential rental property owned (directly or indirectly) by such disqualified single family property owner. (2) Exception (A) In general Paragraph (1) shall not apply with respect to interest paid or accrued in the taxable year in which such single family residential rental property is sold. (B) Exception Subparagraph (A) shall not apply unless the sale described in such subparagraph is\u2014 (i) a sale to an individual for use as the principle residence of the individual (within the meaning of section 121), or (ii) a sale to any qualified nonprofit organization. (C) Qualified nonprofit organization (i) In general For purposes of this paragraph, the term qualified nonprofit organization means any organization which\u2014 (I) is not organized for profit, and (II) has as a principal purpose the creation, development, or preservation of affordable housing. (ii) Certain organizations included The term qualified nonprofit organization shall include\u2014 (I) any community development corporation (as defined in section 204(b) of the Department of Veterans Affairs and Housing and Urban Development, and Independent Agencies Appropriations Act, 1997 (12 U.S.C. 1715z\u201311a(b)), (II) any community housing development organization (as defined in section 104 of the Cranston-Gonzales National Affordable Housing Act ( 42 U.S.C. 12704 ), (III) any community-based development organization qualified under section 570.204 of title 24, Code of Federal Regulations, as in effect on the date of the enactment of this subsection, (IV) any land bank, (V) any resident-owned cooperative or community land trust, and (VI) any subsidiary of a public housing agency (as defined in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) ). (iii) Land bank For purposes of this subparagraph, the term land bank means a government entity, agency, or program, or a special purpose nonprofit entity formed by one or more units of government in accordance with State or local land bank enabling law, that has been designated by one or more State or local governments to acquire, steward, and dispose of vacant, abandoned, or other problem properties in accordance with locally-determined priorities and goals. (iv) Community land trust For purposes of this subparagraph, the term community land trust means a nonprofit organization or State or local government or instrumentality that\u2014 (I) use a ground lease or deed covenant with an affordability period of at least 30 years or more to\u2014 (aa) make rental and homeownership units affordable to households; and (bb) stipulate a preemptive option to purchase the affordable rentals or homeownership units so that the affordability of the units is preserved for successive income-eligible households; and (II) monitors properties to ensure affordability is preserved. (3) Disqualified single family property owner For purposes of this subsection\u2014 (A) In general The term disqualified single family property owner means, with respect to any taxable year, any taxpayer who owns (directly or indirectly) 50 or more single family residential rental properties. (B) Aggregation rules All persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one taxpayer for purposes of this section. (C) Modifications (i) In general For purposes of applying subparagraph (B)\u2014 (I) section 52(a) shall be applied by substituting component members for members , and (II) for purposes of applying section 52(b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations in such paragraph (6)). (ii) Component member For purposes of this paragraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to section 1563(b)(2). (iii) No inference The modifications made by clause (i) shall not be construed to create any inference with respect to the proper application of section 52 with respect to any other provision of this title. (4) Single family residential rental property For purposes of this subsection\u2014 (A) In general The term single family residential rental property means\u2014 (i) any residential rental property (as defined in section 168(e)(2)(A)(i)) which contains 4 or fewer dwelling units (as defined in section 168(e)(2)(A)(ii)(I)), and (ii) improvements to real property directly related to such dwelling units located on the site of such dwelling units. For purposes of clause (i), each townhouse or rowhouse shall be treated as a separate building. (B) Exception for certain properties Such term shall not include any residential rental property (as so defined)\u2014 (i) with respect to which a credit is allowed under section 42 for such taxable year or any property, or (ii) which\u2014 (I) was constructed by the taxpayer, or (II) acquired by the taxpayer after its construction but before the first date on which any dwelling unit in such property was occupied by a resident. (5) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Application to capitalized amounts\n**(1) In general**\nSection 263A(f)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Exception for certain interest of disqualified single family property owners Subparagraph (A) shall not apply to any interest for which a deduction would be disallowed under section 163(n). .\n**(2) Carrying charges**\nSection 266 of such Code is amended\u2014\n**(A)**\nby striking No deduction and inserting the following:\n(a) In general No deduction , and\n**(B)**\nby adding at the end the following new subsection:\n(b) Special rule for certain interest of disqualified single family property owners No election may be made under this section to treat as chargeable to capital account any interest for which a deduction would be disallowed under section 163(n). .\n##### (c) Effective date\nThe amendments made by this section shall apply to indebtedness incurred in taxable years beginning after the date of the enactment of this Act.\n#### 3. Disallowance of depreciation in connection with property used by disqualified single family property owners\n##### (a) In general\nSection 167 of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Deduction disallowed for disqualified single family property owners (1) In general In the case of a disqualified single family property owner, no deduction shall be allowed under this section for any single family residential rental property owned by such disqualified single family property owner. (2) Exception (A) In general Paragraph (1) shall not apply with respect to depreciation deduction which is allowable\u2014 (i) in connection with a single family residential rental property, and (ii) in the taxable year in which such single family residential rental property is sold. (B) Exception Subparagraph (A) shall not apply unless the sale described in clause (ii) thereof is\u2014 (i) a sale to an individual for use as the principle residence of the individual (within the meaning of section 121), or (ii) a sale to any qualified nonprofit organization (as defined in section 163(n)(2)(C)). (3) Definitions For purposes of this subsection, the terms disqualified single family property owner and single family residential rental property have the respective meanings given such terms under section 163(n). (4) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Effective date\nThe amendments made by this section shall apply to property placed in service in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-07-10",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4352",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HOMES Act",
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
        "updateDate": "2025-05-08T19:08:31Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119s969",
          "measure-number": "969",
          "measure-type": "s",
          "orig-publish-date": "2025-03-11",
          "originChamber": "SENATE",
          "update-date": "2026-01-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s969v00",
            "update-date": "2026-01-23"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Stop Predatory Investing Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>"
        },
        "title": "Stop Predatory Investing Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s969.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Predatory Investing Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s969"
    },
    "title": "Stop Predatory Investing Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Stop Predatory Investing Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>",
      "updateDate": "2026-01-23",
      "versionCode": "id119s969"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s969is.xml"
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
      "title": "Stop Predatory Investing Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Stop Predatory Investing Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-29T02:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for taxpayers owning 50 or more single family properties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:18:57Z"
    }
  ]
}
```
