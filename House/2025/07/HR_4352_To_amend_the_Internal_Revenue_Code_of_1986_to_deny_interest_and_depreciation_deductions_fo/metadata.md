# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4352?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4352
- Title: HOMES Act
- Congress: 119
- Bill type: HR
- Bill number: 4352
- Origin chamber: House
- Introduced date: 2025-07-10
- Update date: 2026-01-26T15:16:10Z
- Update date including text: 2026-01-26T15:16:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-07-10: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-10: Introduced in House

## Actions

- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Introduced in House
- 2025-07-10 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4352",
    "number": "4352",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "HOMES Act",
    "type": "HR",
    "updateDate": "2026-01-26T15:16:10Z",
    "updateDateIncludingText": "2026-01-26T15:16:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
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
          "date": "2025-07-10T15:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4352ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4352\nIN THE HOUSE OF REPRESENTATIVES\nJuly 10, 2025 Mrs. Sykes (for herself and Ms. Lee of Pennsylvania ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for taxpayers owning 50 or more single family properties.\n#### 1. Short title\nThis Act may be cited as the Houses Over Middle-Class Exploitation Schemes Act or the HOMES Act .\n#### 2. Disallowance of interest deduction for disqualified single family property owners\n##### (a) In general\nSection 163 of the Internal Revenue Code of 1986 is amended by redesignating subsection (n) as subsection (o) and by inserting after subsection (m) the following new subsection:\n(n) Interest paid by certain disqualified single family property owners (1) In general In the case of a disqualified single family property owner, no deduction shall be allowed under this chapter for any interest paid or accrued in connection with any single family residential rental property owned (directly or indirectly) by such disqualified single family property owner. (2) Exception (A) In general Paragraph (1) shall not apply with respect to interest paid or accrued in the taxable year in which such single family residential rental property is sold. (B) Exception Subparagraph (A) shall not apply unless the sale described in such subparagraph is\u2014 (i) a sale to an individual for use as the principle residence of the individual (within the meaning of section 121), or (ii) a sale to any qualified nonprofit organization. (C) Qualified nonprofit organization (i) In general For purposes of this paragraph, the term qualified nonprofit organization means any organization which\u2014 (I) is not organized for profit, and (II) has as a principal purpose the creation, development, or preservation of affordable housing. (ii) Certain organizations included The term qualified nonprofit organization shall include\u2014 (I) any community development corporation (as defined in section 204(b) of the Department of Veterans Affairs and Housing and Urban Development, and Independent Agencies Appropriations Act, 1997 (12 U.S.C. 1715z\u201311a(b))), (II) any community housing development organization (as defined in section 104 of the Cranston-Gonzales National Affordable Housing Act ( 42 U.S.C. 12704 )), (III) any community-based development organization qualified under section 570.204 of title 24, Code of Federal Regulations, as in effect on the date of the enactment of this subsection, (IV) any land bank, (V) any resident-owned cooperative or community land trust, and (VI) any subsidiary of a public housing agency (as defined in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) )). (iii) Land bank For purposes of this subparagraph, the term land bank means a government entity, agency, or program, or a special purpose nonprofit entity formed by one or more units of government in accordance with State or local land bank enabling law, that has been designated by one or more State or local governments to acquire, steward, and dispose of vacant, abandoned, or other problem properties in accordance with locally-determined priorities and goals. (iv) Community land trust For purposes of this subparagraph, the term community land trust means a nonprofit organization or State or local government or instrumentality that\u2014 (I) use a ground lease or deed covenant with an affordability period of at least 30 years or more to\u2014 (aa) make rental and homeownership units affordable to households; and (bb) stipulate a preemptive option to purchase the affordable rentals or homeownership units so that the affordability of the units is preserved for successive income-eligible households; and (II) monitors properties to ensure affordability is preserved. (3) Disqualified single family property owner For purposes of this subsection\u2014 (A) In general The term disqualified single family property owner means, with respect to any taxable year, any taxpayer who owns (directly or indirectly) 50 or more single family residential rental properties. (B) Aggregation rules All persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one taxpayer for purposes of this section. (C) Modifications (i) In general For purposes of applying subparagraph (B)\u2014 (I) section 52(a) shall be applied by substituting component members for members , and (II) for purposes of applying section 52(b), the term trade or business shall include any activity treated as a trade or business under paragraph (5) or (6) of section 469(c) (determined without regard to the phrase To the extent provided in regulations in such paragraph (6)). (ii) Component member For purposes of this paragraph, the term component member has the meaning given such term by section 1563(b), except that the determination shall be made without regard to section 1563(b)(2). (iii) No inference The modifications made by clause (i) shall not be construed to create any inference with respect to the proper application of section 52 with respect to any other provision of this title. (4) Single family residential rental property For purposes of this subsection\u2014 (A) In general The term single family residential rental property means\u2014 (i) any residential rental property (as defined in section 168(e)(2)(A)(i)) which contains 4 or fewer dwelling units (as defined in section 168(e)(2)(A)(ii)(I)), and (ii) improvements to real property directly related to such dwelling units located on the site of such dwelling units. For purposes of clause (i), each townhouse or rowhouse shall be treated as a separate building. (B) Exception for certain properties Such term shall not include any residential rental property (as so defined)\u2014 (i) with respect to which a credit is allowed under section 42 for such taxable year or any property, or (ii) which\u2014 (I) was constructed by the taxpayer, or (II) acquired by the taxpayer after its construction but before the first date on which any dwelling unit in such property was occupied by a resident. (5) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Application to capitalized amounts\n**(1) In general**\nSection 263A(f)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(D) Exception for certain interest of disqualified single family property owners Subparagraph (A) shall not apply to any interest for which a deduction would be disallowed under section 163(n). .\n**(2) Carrying charges**\nSection 266 of such Code is amended\u2014\n**(A)**\nby striking No deduction and inserting the following:\n(a) In general No deduction , and\n**(B)**\nby adding at the end the following new subsection:\n(b) Special rule for certain interest of disqualified single family property owners No election may be made under this section to treat as chargeable to capital account any interest for which a deduction would be disallowed under section 163(n). .\n##### (c) Effective date\nThe amendments made by this section shall apply to indebtedness incurred in taxable years beginning after the date of the enactment of this Act.\n#### 3. Disallowance of depreciation in connection with property used by disqualified single family property owners\n##### (a) In general\nSection 167 of the Internal Revenue Code of 1986 is amended by redesignating subsection (i) as subsection (j) and by inserting after subsection (h) the following new subsection:\n(i) Deduction disallowed for disqualified single family property owners (1) In general In the case of a disqualified single family property owner, no deduction shall be allowed under this section for any single family residential rental property owned by such disqualified single family property owner. (2) Exception (A) In general Paragraph (1) shall not apply with respect to depreciation deduction which is allowable\u2014 (i) in connection with a single family residential rental property, and (ii) in the taxable year in which such single family residential rental property is sold. (B) Exception Subparagraph (A) shall not apply unless the sale described in clause (ii) thereof is\u2014 (i) a sale to an individual for use as the principle residence of the individual (within the meaning of section 121), or (ii) a sale to any qualified nonprofit organization (as defined in section 163(n)(2)(C)). (3) Definitions For purposes of this subsection, the terms disqualified single family property owner and single family residential rental property have the respective meanings given such terms under section 163(n). (4) Regulations The Secretary shall prescribe such regulations as may be necessary or appropriate to carry out the purposes of this subsection, including regulations to prevent the avoidance of the purposes of this subsection. .\n##### (b) Effective date\nThe amendments made by this section shall apply to property placed in service in taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-07-10",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "969",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Stop Predatory Investing Act",
      "type": "S"
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
        "updateDate": "2025-07-29T21:27:43Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-07-10",
    "originChamber": "House",
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
          "measure-id": "id119hr4352",
          "measure-number": "4352",
          "measure-type": "hr",
          "orig-publish-date": "2025-07-10",
          "originChamber": "HOUSE",
          "update-date": "2026-01-26"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4352v00",
            "update-date": "2026-01-26"
          },
          "action-date": "2025-07-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Houses Over Middle-Class Exploitation Schemes Act or the HOMES Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>"
        },
        "title": "HOMES Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4352.xml",
    "summary": {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Houses Over Middle-Class Exploitation Schemes Act or the HOMES Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr4352"
    },
    "title": "HOMES Act"
  },
  "summaries": [
    {
      "actionDate": "2025-07-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Houses Over Middle-Class Exploitation Schemes Act or the HOMES Act </strong></p><p>This bill prohibits a taxpayer who owns (directly or indirectly) 50 or more single-family\u00a0residential rental properties (disqualified single-family property owner) from claiming a federal tax deduction for interest paid (or accrued) in connection with such properties or a federal tax deduction for depreciation in connection with such properties.</p><p>The bill generally defines a <em>single-family residential rental property</em> as any residential rental property containing four or fewer dwelling units and improvements to real property related to such dwelling units.</p><p>However, under the bill, a disqualified single-family property owner may still claim a tax deduction for interest and depreciation on (1) single-family residential rental property for which the low-income housing tax credit (LIHTC) may be claimed and (2) certain newly constructed single-family residential rental properties. (The LIHTC program awards tax credits for newly-constructed or substantially rehabilitated low-income housing.)</p><p>The bill also allows a disqualified single-family property owner to claim a federal tax deduction for interest or depreciation in connection with a single-family residential rental property in the year such property is sold if it is sold to</p><ul><li>an individual for use as a principal residence;</li><li>a non-profit organization that creates, develops, or preserves affordable housing;</li><li>certain community development organizations;</li><li>a land bank;</li><li>any resident-owned cooperative or community land trust; or</li><li>a public housing agency subsidiary.</li></ul>",
      "updateDate": "2026-01-26",
      "versionCode": "id119hr4352"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4352ih.xml"
        }
      ],
      "type": "Introduced in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "HOMES Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T04:53:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HOMES Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Houses Over Middle-Class Exploitation Schemes Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T04:53:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to deny interest and depreciation deductions for taxpayers owning 50 or more single family properties.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T04:48:46Z"
    }
  ]
}
```
