# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/948
- Title: SAFE HOME Act
- Congress: 119
- Bill type: HR
- Bill number: 948
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2025-07-25T14:22:47Z
- Update date including text: 2025-07-25T14:22:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/948",
    "number": "948",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000401",
        "district": "3",
        "firstName": "Kevin",
        "fullName": "Rep. Kiley, Kevin [R-CA-3]",
        "lastName": "Kiley",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "SAFE HOME Act",
    "type": "HR",
    "updateDate": "2025-07-25T14:22:47Z",
    "updateDateIncludingText": "2025-07-25T14:22:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:03:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr948ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 948\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Kiley of California introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a refundable credit against tax for wildfire mitigation expenditures.\n#### 1. Short title\nThis Act may be cited as the Supporting Affordable Fire Emergency Hardening through Optimized Mitigation Efforts Act or the SAFE HOME Act .\n#### 2. Refundable personal credit for wildfire mitigation expenditures\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 (relating to refundable credits) is amended by inserting after section 36B the following new section:\n36C. Wildfire mitigation expenditures (a) Allowance of credit In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 25 percent of the qualified wildfire mitigation expenditures made by the taxpayer during such taxable year. (b) Maximum credit (1) In general Subject to paragraphs (2) and (3), the credit allowed under subsection (a) for any taxable year shall not exceed $25,000. (2) Phaseout (A) In general The amount under paragraph (1) for the taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount under such paragraph as\u2014 (i) the excess (if any) of\u2014 (I) the taxpayer\u2019s adjusted gross income for such taxable year, over (II) $200,000, bears to (ii) $100,000. (B) Inflation adjustment In the case of any taxable year after 2024, each of the dollar amounts under subparagraph (A) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2023 for calendar year 2016 in subparagraph (A)(ii) thereof. (C) Rounding If any reduction determined under subparagraph (A) is not a multiple of $50, or any increase under subparagraph (B) is not a multiple of $50, such amount shall be rounded to the nearest multiple of $50. (c) Definitions For purposes of this section\u2014 (1) Qualified wildfire mitigation expenditure (A) In general The term qualified wildfire mitigation expenditure means an expenditure relating to a qualified dwelling unit\u2014 (i) for property to improve fire resistance (not less than a class A rating) of a roof covering, (ii) to install\u2014 (I) roof coverings, sheathing, flashing, roof and attic vents, eaves, or gutters that conform to ignition-resistant construction standards, (II) wall components for wall assemblies that conform to ignition-resistant construction standards, (III) exterior walls, doors, windows, or other exterior dwelling unit elements that conform to ignition-resistant construction standards, (IV) exterior deck or fence components that conform to ignition-resistant construction standards, or (V) structure-specific water hydration systems, including fire mitigation systems such as interior and exterior sprinkler systems, or (iii) for services or equipment to\u2014 (I) create buffers around the qualified dwelling unit through the removal or reduction of flammable vegetation, including vertical clearance of tree branches, (II) create buffers around the dwelling unit through\u2014 (aa) the removal of exterior deck or fence components or ignition-prone landscape features, or (bb) replacement of the components or features described in item (aa) with components that conform to ignition-resistant construction standards, (III) perform fire maintenance procedures identified by the Federal Emergency Management Agency or the United States Forest Service, including fuel management techniques such as creating fuel and fire breaks, (IV) replace flammable vegetation with less flammable species, or (V) prevent smoke inhalation, such as air filters or other equipment designed to prevent smoke from entering the dwelling unit. (B) Exception The term qualified wildfire mitigation expenditure shall not include any expenditure or portion thereof which is paid, funded, or reimbursed by a Federal, State, or local government entity, or any political subdivision, agency, or instrumentality thereof. (2) Qualified dwelling unit The term qualified dwelling unit means a dwelling unit which is\u2014 (A) located\u2014 (i) in the United States or in a territory of the United States, and (ii) in an area\u2014 (I) in which a Federal natural disaster declaration has been made within the preceding 10-year period with respect to a wildfire, (II) which is adjacent to an area described in subclause (I), (III) which, during the taxable year or the period of the 10 taxable years preceding such taxable year, has received hazard mitigation assistance through the Federal Emergency Management Agency in regard to any wildfire which, with respect to the expenditure described in paragraph (1) which is made by the taxpayer, is applicable to such expenditure, or (IV) which, with respect to any taxable year, has been designated as a community disaster resilience zone (as defined in section 206(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5136(a) )) as the result of a wildfire, and (B) used as a primary residence by the taxpayer. (d) Documentation Any taxpayer claiming the credit under this section shall provide the Secretary with adequate documentation regarding the specific qualified wildfire mitigation expenditures made by the taxpayer during the taxable year, as well as such other information or documentation as the Secretary may require. (e) Termination of credit The credit allowed under this section shall not apply to wildfire mitigation expenditures made after December 31, 2032. .\n##### (b) Conforming amendment\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 36B the following new item:\nSec. 36C. Wildfire mitigation expenditures. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-02-04",
      "versionType": "Introduced in House"
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
        "updateDate": "2025-04-16T15:30:48Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-04",
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
          "measure-id": "id119hr948",
          "measure-number": "948",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-04",
          "originChamber": "HOUSE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr948v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-02-04",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Supporting Affordable Fire Emergency Hardening through Optimized Mitigation Efforts Act or the SAFE HOME Act</strong></p><p>This bill establishes a new refundable tax credit (through 2032) for costs incurred by an individual to improve the fire resistance of a primary residence. (Certain requirements and limitations apply.)</p><p>The amount of the tax credit is 25% of unreimbursed qualified wildfire mitigation expenses up to $25,000. The tax credit begins to phase out for individuals with an adjusted gross income exceeding $200,000, such that the tax credit is completely phased out for individuals with an adjusted gross income of $300,000 or more.</p><p> Wildfire mitigation expenses that qualify for the tax credit include</p><ul><li>property to improve the fire-resistance of a roof;</li><li>installation of ignition-resistant property (e.g., sheathing, flashing, roof and attic vents, or certain exterior elements) or structure-specific water hydration systems;</li><li>services or equipment to create a buffer around the residence or to replace flammable vegetation with less flammable vegetation;</li><li>services or equipment for certain fire maintenance procedures; and</li><li>services or equipment to prevent smoke inhalation (e.g., air filters).</li></ul><p>Further, such expenses must be incurred with respect to a primary residence located (1) in the United States; and (2) in an area that, due to a wildfire, received a federal disaster declaration within the prior 10 years or that is adjacent to such area, that received certain hazard mitigation assistance in the tax year or the\u00a0prior 10 years, or that is a community disaster resilience zone (or received such designation for any tax year).</p>"
        },
        "title": "SAFE HOME Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr948.xml",
    "summary": {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Affordable Fire Emergency Hardening through Optimized Mitigation Efforts Act or the SAFE HOME Act</strong></p><p>This bill establishes a new refundable tax credit (through 2032) for costs incurred by an individual to improve the fire resistance of a primary residence. (Certain requirements and limitations apply.)</p><p>The amount of the tax credit is 25% of unreimbursed qualified wildfire mitigation expenses up to $25,000. The tax credit begins to phase out for individuals with an adjusted gross income exceeding $200,000, such that the tax credit is completely phased out for individuals with an adjusted gross income of $300,000 or more.</p><p> Wildfire mitigation expenses that qualify for the tax credit include</p><ul><li>property to improve the fire-resistance of a roof;</li><li>installation of ignition-resistant property (e.g., sheathing, flashing, roof and attic vents, or certain exterior elements) or structure-specific water hydration systems;</li><li>services or equipment to create a buffer around the residence or to replace flammable vegetation with less flammable vegetation;</li><li>services or equipment for certain fire maintenance procedures; and</li><li>services or equipment to prevent smoke inhalation (e.g., air filters).</li></ul><p>Further, such expenses must be incurred with respect to a primary residence located (1) in the United States; and (2) in an area that, due to a wildfire, received a federal disaster declaration within the prior 10 years or that is adjacent to such area, that received certain hazard mitigation assistance in the tax year or the\u00a0prior 10 years, or that is a community disaster resilience zone (or received such designation for any tax year).</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr948"
    },
    "title": "SAFE HOME Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-04",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Supporting Affordable Fire Emergency Hardening through Optimized Mitigation Efforts Act or the SAFE HOME Act</strong></p><p>This bill establishes a new refundable tax credit (through 2032) for costs incurred by an individual to improve the fire resistance of a primary residence. (Certain requirements and limitations apply.)</p><p>The amount of the tax credit is 25% of unreimbursed qualified wildfire mitigation expenses up to $25,000. The tax credit begins to phase out for individuals with an adjusted gross income exceeding $200,000, such that the tax credit is completely phased out for individuals with an adjusted gross income of $300,000 or more.</p><p> Wildfire mitigation expenses that qualify for the tax credit include</p><ul><li>property to improve the fire-resistance of a roof;</li><li>installation of ignition-resistant property (e.g., sheathing, flashing, roof and attic vents, or certain exterior elements) or structure-specific water hydration systems;</li><li>services or equipment to create a buffer around the residence or to replace flammable vegetation with less flammable vegetation;</li><li>services or equipment for certain fire maintenance procedures; and</li><li>services or equipment to prevent smoke inhalation (e.g., air filters).</li></ul><p>Further, such expenses must be incurred with respect to a primary residence located (1) in the United States; and (2) in an area that, due to a wildfire, received a federal disaster declaration within the prior 10 years or that is adjacent to such area, that received certain hazard mitigation assistance in the tax year or the\u00a0prior 10 years, or that is a community disaster resilience zone (or received such designation for any tax year).</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119hr948"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr948ih.xml"
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
      "title": "SAFE HOME Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-06T07:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFE HOME Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Supporting Affordable Fire Emergency Hardening through Optimized Mitigation Efforts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-06T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a refundable credit against tax for wildfire mitigation expenditures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-06T07:18:41Z"
    }
  ]
}
```
