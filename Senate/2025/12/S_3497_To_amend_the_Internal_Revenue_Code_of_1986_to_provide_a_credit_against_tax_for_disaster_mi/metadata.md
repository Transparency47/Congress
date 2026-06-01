# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3497?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3497
- Title: Shelter Act
- Congress: 119
- Bill type: S
- Bill number: 3497
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-01-21T05:01:27Z
- Update date including text: 2026-01-21T05:01:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3497",
    "number": "3497",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001267",
        "district": "",
        "firstName": "Michael",
        "fullName": "Sen. Bennet, Michael F. [D-CO]",
        "lastName": "Bennet",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Shelter Act",
    "type": "S",
    "updateDate": "2026-01-21T05:01:27Z",
    "updateDateIncludingText": "2026-01-21T05:01:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T20:29:23Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "LA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3497is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3497\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Bennet (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a credit against tax for disaster mitigation expenditures.\n#### 1. Short title\nThis Act may be cited as the Shelter Act .\n#### 2. Nonrefundable personal credit for disaster mitigation expenditures\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986, as amended by section 70411 of Public Law 119\u201321 , is amended by inserting after section 25F the following new section:\n25G. Disaster mitigation expenditures (a) Allowance of credit (1) In general In the case of an individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 25 percent of the qualified disaster mitigation expenditures made by the taxpayer during such taxable year. (2) Annual limitation Subject to subsection (b), the credit allowed to a taxpayer under paragraph (1) for any taxable year shall not exceed $3,750 (or, in the case of a joint return, $7,500). (3) Cumulative limitation per qualified dwelling unit Subject to subsection (b), the credit allowed under paragraph (1) with respect to a qualified dwelling unit of the taxpayer for any taxable year shall not exceed the excess (if any) of $15,000 over the aggregate credits allowed under such paragraph with respect to such qualified dwelling unit for all prior taxable years ending after December 31, 2025. (b) Income phaseout (1) In general The amount of the credit allowed under subsection (a)(1) for the taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount under such subsection as\u2014 (A) the amount (not less than zero) equal to the adjusted gross income of the taxpayer for such taxable year minus $100,000, bears to (B) $50,000. (2) Inflation adjustment In the case of any taxable year after 2026, each of the dollar amounts under paragraph (1) shall be increased by an amount equal to\u2014 (A) such dollar amount, multiplied by (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (3) Rounding If any reduction determined under paragraph (1) is not a multiple of $50, or any increase under paragraph (2) is not a multiple of $50, such amount shall be rounded to the nearest multiple of $50. (4) Joint return If a joint return is filed by the taxpayer for the taxable year, for purposes of determining the amount of any reduction under paragraph (1) for such taxable year, the dollar amounts under such paragraph (after application of paragraphs (2) and (3)) shall be doubled. (c) Definitions For purposes of this section\u2014 (1) Qualified disaster mitigation expenditure (A) In general Subject to subparagraphs (B) and (C), the term qualified disaster mitigation expenditure means an expenditure relating to a qualified dwelling unit\u2014 (i) for property to\u2014 (I) improve the strength of a roof deck attachment, (II) create a secondary water barrier to prevent water intrusion or mitigate against potential water intrusion from wind-driven rain, (III) improve the durability, impact resistance (not less than class 3 or 4 rating), or fire resistance (not less than class A rating) of a roof covering, (IV) brace gable-end walls, (V) reinforce the connection between a roof and supporting wall, (VI) protect openings from penetration by wind-borne debris, (VII) protect exterior doors and garages from natural hazards, (VIII) complete measures contained in the publication of the Federal Emergency Management Agency entitled Wind Retrofit Guide for Residential Buildings (P\u2013804), (IX) elevate the qualified dwelling unit, as well as utilities, machinery, or equipment, above the base flood elevation or other applicable minimum elevation requirement, (X) seal walls in the basement of the qualified dwelling unit using waterproofing compounds, or (XI) protect propane tanks or other external fuel sources, (ii) to install\u2014 (I) check valves to prevent flood water from backing up into drains, (II) flood vents, breakaway walls or open lattice for homes located in V zones, (III) a stormwater drainage system or improve an existing system, (IV) natural or nature-based features for flood control, including living shorelines, (V) roof coverings, sheathing, flashing, roof and attic vents, eaves, or gutters that conform to ignition-resistant construction standards, (VI) wall components for wall assemblies that conform to ignition-resistant construction standards, (VII) a wall-to-foundation anchor or connector, or a shear transfer anchor or connector, (VIII) wood structural panel sheathing for strengthening cripple walls, (IX) anchorage of the masonry chimney to the framing, (X) prefabricated lateral resisting systems, (XI) a standby generator system consisting of a standby generator and an automatic transfer switch, (XII) a storm shelter that meets the design and construction standards established by the International Code Council and the National Storm Shelter Association (ICC\u2013500), or a safe room that satisfies the criteria contained in\u2014 (aa) the publication of the Federal Emergency Management Agency entitled Safe Rooms for Tornadoes and Hurricanes (P\u2013361), or (bb) the publication of the Federal Emergency Management Agency entitled Taking Shelter from the Storm (P\u2013320), (XIII) a lightning protection system, (XIV) exterior walls, doors, windows, or other exterior dwelling unit elements that conform to ignition-resistant construction standards, (XV) exterior deck or fence components that conform to ignition-resistant construction standards, (XVI) structure-specific water hydration systems, including fire mitigation systems such as interior and exterior sprinkler systems, (XVII) water capture and delivery systems to accommodate drought events or to decrease water use, including the design of such systems, (XVIII) flood openings for fully enclosed areas below the lowest floor of the dwelling unit, (XIX) lateral bracing for wall elements, foundation elements, and garage doors or other large openings to resist seismic loads, or (XX) automatic shutoff valves for water and gas lines, or (iii) for services or equipment to\u2014 (I) create buffers around the qualified dwelling unit through the removal or reduction of flammable vegetation, including vertical clearance of tree branches, (II) create buffers around the dwelling unit through\u2014 (aa) the removal of exterior deck or fence components or ignition-prone landscape features, or (bb) replacement of the components or features described in item (aa) with components or features that conform to ignition-resistant construction standards, (III) perform fire maintenance procedures identified by the Federal Emergency Management Agency or the United States Forest Service, including fuel management techniques such as creating fuel and fire breaks, (IV) replace flammable vegetation with less flammable species, or (V) prevent smoke inhalation, such as air filters or other equipment designed to prevent smoke from entering the dwelling unit, (iv) for property relating to satisfying the standards required for receipt of a FORTIFIED designation or a Wildfire Prepared designation from the Insurance Institute for Business and Home Safety, or any third-party verified certification demonstrating compliance with nationally recognized and consensus-based hazard mitigation or resilience standards, provided that the qualified dwelling unit receives such designation or certifications following installation of such property, or (v) for any other hazard mitigation activity which has been identified by the Secretary, in consultation with the Administrator of the Federal Emergency Management Agency, for mitigation of a natural hazard or compliance with other consensus-based resiliency standards. (B) Hazard-specific applicability (i) In general Subject to clause (ii), the term qualified disaster mitigation expenditure shall only apply to expenditures relating to a qualified dwelling unit which are described in subparagraph (A) if such expenditures address a hazard type identified in the applicable State or tribal Standard State Mitigation Plans or Enhanced State Mitigation Plans, as prepared under section 201.4 or 201.5 of title 44, Code of Federal Regulations (as in effect on the date of enactment of this section). (ii) Negative lists The Secretary, in consultation with the Administrator of the Federal Emergency Management Agency, may publish a list of inapplicable expenditures which are region-specific in order to prohibit the application of subsection (a) for expenditures relating to hazards which are not relevant to the location of the qualified dwelling unit. (C) Exception The term qualified disaster mitigation expenditure shall not include any expenditure or portion thereof which is paid, funded, or reimbursed by a Federal, State, or local government entity, or any political subdivision, agency, or instrumentality thereof. (2) Qualified dwelling unit The term qualified dwelling unit means a dwelling unit which is located\u2014 (A) in the United States or in a territory of the United States, and (B) in an area\u2014 (i) which, during the taxable year or the period of the 5 taxable years preceding such taxable year, has received hazard mitigation assistance through the Federal Emergency Management Agency in regard to any natural disaster which, with respect to the expenditure described in paragraph (1) which is made by the taxpayer, is applicable to such expenditure, and (ii) (I) in which a Federal natural disaster declaration has been made within the preceding 5-year period, (II) which is adjacent to an area described in subclause (I), or (III) which, with respect to any taxable year, has been designated as a community disaster resilience zone (as defined in section 206(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5136(a) )). (d) Limitation (1) In general In the case of an expenditure described in clause (i) or (ii) of subsection (c)(1)(A), such expenditure shall be taken into account in determining the qualified disaster mitigation expenditures made by the taxpayer during the taxable year only if the onsite preparation, assembly, or original installation of the property with respect to which such expenditure is made has been completed in a manner that is deemed to be in compliance with the latest published editions of relevant consensus-based codes, specifications, and standards or any more restrictive Federal, State, or local floodplain management standards and consistent with floodplain management regulations for the local jurisdiction in which the qualified dwelling unit is located. (2) Latest published editions The term latest published editions means, with respect to relevant consensus-based codes, specifications, and standards, either of the 2 most recently published editions. (e) Labor costs For purposes of this section, expenditures for labor costs properly allocable to the onsite preparation, assembly, or original installation of the property described in clause (i) or (ii) of subsection (c)(1)(A) shall be taken into account in determining the qualified disaster mitigation expenditures made by the taxpayer during the taxable year. (f) Inspection costs For purposes of this section, expenditures for the cost of any inspection required under subsection (d) which is properly allocable to the inspection of the preparation, assembly, or installation of the property described in clause (i) or (ii) of subsection (c)(1)(A) shall be taken into account in determining the qualified disaster mitigation expenditures made by the taxpayer during the taxable year. (g) Carryforward of unused credit (1) In general If the credit allowable under subsection (a)(1) for any taxable year exceeds the applicable tax limit for such taxable year, such excess shall be a carryover to each of the 5 succeeding taxable years and, subject to the limitations of paragraph (2), shall be added to the credit allowable by subsection (a)(1) for such succeeding taxable year. (2) Limitation The amount of the unused credit which may be taken into account under paragraph (1) for any taxable year shall not exceed the amount (if any) by which the applicable tax limit for such taxable year exceeds the sum of\u2014 (A) the credit allowable under subsection (a)(1) for such taxable year determined without regard to this subsection, and (B) the amounts which, by reason of this subsection, are carried to such taxable year and are attributable to taxable years before the unused credit year. (3) Applicable tax limit For purposes of this subsection, the term applicable tax limit means the limitation imposed by section 26(a) for the taxable year reduced by the sum of the credits allowable under this subpart (other than this section). (h) Documentation Any taxpayer claiming the credit under this section shall provide the Secretary with adequate documentation regarding the specific qualified disaster mitigation expenditures made by the taxpayer during the taxable year, as well as such other information or documentation as the Secretary may require. .\n##### (b) Conforming amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25F the following new item:\nSec. 25G. Disaster mitigation expenditures. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Business-related credit for disaster mitigation\n##### (a) In general\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 45AA the following new section:\n45BB. Disaster mitigation credit (a) General rule For purposes of section 38, the disaster mitigation credit determined under this section for any taxable year is an amount equal to 25 percent of the qualified disaster mitigation expenditures made by the taxpayer during the taxable year. (b) Maximum credit (1) In general Subject to paragraph (2), the amount of the credit determined under subsection (a) for any taxable year shall not exceed $5,000. (2) Phaseout (A) In general The amount under paragraph (1) for the taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount under such paragraph as\u2014 (i) the amount (not less than zero) equal to the average gross receipts of the taxpayer over the 3 preceding taxable years minus $5,000,000, bears to (ii) $5,000,000. (B) Inflation adjustment In the case of any taxable year after 2026, each of the dollar amounts under subparagraph (A) shall be increased by an amount equal to\u2014 (i) such dollar amount, multiplied by (ii) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2025 for calendar year 2016 in subparagraph (A)(ii) thereof. (C) Rounding If any reduction determined under subparagraph (A) is not a multiple of $50, or any increase under subparagraph (B) is not a multiple of $50, such amount shall be rounded to the nearest multiple of $50. (c) Qualified disaster mitigation expenditure (1) In general For purposes of this section, the term qualified disaster mitigation expenditure has the same meaning given such term under paragraph (1) of section 25G(c), except that place of business shall be substituted for qualified dwelling unit each place it appears in such paragraph. (2) Place of business For purposes of this section, an expenditure shall not be treated as a qualified disaster mitigation expenditure (as defined in paragraph (1)) unless the taxpayer's place of business is located\u2014 (A) in the United States or in a territory of the United States, and (B) in an area\u2014 (i) in which a Federal natural disaster declaration has been made within the preceding 5-year period, (ii) which is adjacent to an area described in clause (i), (iii) which, during the taxable year or the period of the 5 taxable years preceding such taxable year, has received hazard mitigation assistance through the Federal Emergency Management Agency in regard to any natural disaster which, with respect to the expenditure described in section 25G(c)(1) which is made by the taxpayer, is applicable to such expenditure, or (iv) which, with respect to any taxable year, has been designated as a community disaster resilience zone (as defined in section 206(a) of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5136(a) )). (d) Special rules Rules similar to the rules of subsections (d) through (g) of section 25G shall apply for purposes of this section. (e) No double benefit No credit shall be determined under this section with respect to any expenditures for which a credit was allowed under section 25G. .\n##### (b) Conforming amendments\n**(1)**\nSection 38(b) of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the disaster mitigation credit determined under section 45BB(a). .\n**(2)**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 45AA the following new item:\nSec. 45BB. Disaster mitigation credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-12-16",
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
        "actionDate": "2025-12-16",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "6763",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Shelter Act",
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
        "updateDate": "2026-01-12T22:28:30Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3497is.xml"
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
      "title": "Shelter Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-10T09:09:06Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Shelter Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide a credit against tax for disaster mitigation expenditures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:16Z"
    }
  ]
}
```
