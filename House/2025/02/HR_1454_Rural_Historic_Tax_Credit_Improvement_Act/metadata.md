# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1454?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1454
- Title: Rural Historic Tax Credit Improvement Act
- Congress: 119
- Bill type: HR
- Bill number: 1454
- Origin chamber: House
- Introduced date: 2025-02-21
- Update date: 2026-01-21T06:44:27Z
- Update date including text: 2026-01-21T06:44:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-21: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-02-21: Introduced in House

## Actions

- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Introduced in House
- 2025-02-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-21",
    "latestAction": {
      "actionDate": "2025-02-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1454",
    "number": "1454",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Rural Historic Tax Credit Improvement Act",
    "type": "HR",
    "updateDate": "2026-01-21T06:44:27Z",
    "updateDateIncludingText": "2026-01-21T06:44:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-21",
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
      "actionDate": "2025-02-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-21",
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
          "date": "2025-02-21T20:31:50Z",
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
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-02-21",
      "state": "NV"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "WV"
    },
    {
      "bioguideId": "M001235",
      "district": "2",
      "firstName": "Riley",
      "fullName": "Rep. Moore, Riley [R-WV-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-21",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1454ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1454\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 21, 2025 Mr. Carey (for himself and Mr. Horsford ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to enhance the rehabilitation credit for buildings in rural areas.\n#### 1. Short title\nThis Act may be cited as the Rural Historic Tax Credit Improvement Act .\n#### 2. Enhancement of rehabilitation credit for buildings in rural areas\n##### (a) In general\nSection 47(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1), by striking For purposes and inserting Except as provided in paragraph (3), for purposes , and\n**(2)**\nby adding at the end the following new paragraphs:\n(3) Applicable rural projects (A) In general In the case of any applicable rural project\u2014 (i) paragraph (1) shall not apply for any qualified rehabilitation expenditures with respect to such project, and (ii) for the taxable year in which such project is placed in service, the rehabilitation credit for such taxable year is an amount equal to\u2014 (I) in the case of a project which is an affordable housing project, 40 percent of the qualified rehabilitation expenditures with respect to such project, or (II) in the case of a project which is not an affordable housing project, 30 percent of the qualified rehabilitation expenditures with respect to such project. (B) Applicable rural project (i) In general For purposes of this section, the term applicable rural project means a qualified rehabilitated building which is located in a rural area. (ii) Limitation In the case of any applicable rural project, the total amount of qualified rehabilitation expenditures which may be taken into account under this section with respect to such project may not exceed $5,000,000. (iii) Rural area For purposes of this paragraph, the term rural area means any area other than\u2014 (I) a city or town that has a population of greater than 50,000 inhabitants, or (II) the urbanized area contiguous and adjacent to a city or town described in subclause (I), as defined by the Bureau of the Census based on the latest decennial census of the United States. (C) Affordable housing project (i) In general For purposes of this paragraph, the term affordable housing project means a project\u2014 (I) in which\u2014 (aa) not less than 50 percent of the aggregate square feet of the completed project is housing, and (bb) with respect to the housing described in item (aa), not less than 50 percent of the aggregate square feet of such housing\u2014 (AA) is new affordable housing, or (BB) continues to provide affordable housing, or (II) in which not less than 33 percent of the aggregate square feet of the completed project\u2014 (aa) is new affordable housing, or (bb) continues to provide affordable housing. (ii) Affordable housing For purposes of this paragraph, the term affordable housing means a decent, safe, and sanitary dwelling, apartment, or other living accommodation for a household whose income does not exceed 80 percent of the median income for the market area (as defined by the Secretary of Housing and Urban Development under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f )). (4) Transfer of credit for applicable rural projects (A) In general Subject to subparagraph (B) and such regulations or other guidance as the Secretary may provide, the taxpayer may transfer all or a portion of the credit determined under paragraph (3) for an applicable rural project. (B) Certification (i) In general A transfer under subparagraph (A) shall be accompanied by a certificate which includes\u2014 (I) the certification for the certified historic structure referred to in subsection (c)(3), (II) the taxpayer\u2019s name, address, tax identification number, date of project completion, and the amount of credit being transferred, (III) the transferee\u2019s name, address, tax identification number, and the amount of credit being transferred, and (IV) such other information as may be required by the Secretary. (ii) Transferability of certificate A certificate issued under this section to a taxpayer shall be transferable to any other taxpayer. (C) Tax treatment relating to certificate (i) Disallowance of deduction No deduction shall be allowed for the amount of consideration paid or incurred by the transferee. (ii) Allowance of credit The amount of credit transferred under subparagraph (A)\u2014 (I) shall not be allowed to the transferor for any taxable year, and (II) shall be allowable to the transferee as a credit determined under this section for the taxable year of the transferee in which such credit is transferred. (iii) Exclusion Gross income shall not include any amount received in connection with the transfer of the certificate. (D) Recapture and other special rules The taxpayer who claims a credit determined under this section by reason of a transfer of an amount of credit under subparagraph (A) with respect to an applicable rural project shall be treated as the taxpayer with respect to such project for purposes of section 50. (E) Information reporting The transferor and the transferee shall each make such reports regarding the transfer of an amount of credit under paragraph (A) and containing such information as the Secretary may require. The reports required by this subsection shall be filed at such time and in such manner as may be required by the Secretary. (F) Regulations The Secretary shall prescribe regulations or other guidance to carry out this paragraph in a manner which is consistent with applicable requirements with respect to transfer of credits under section 6418. .\n##### (b) Recapture for failure To comply with affordable housing requirements\n**(1) In general**\nSection 50(a) of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nby redesignating paragraphs (4) through (6) as paragraphs (5) through (7), respectively, and\n**(B)**\nby inserting after paragraph (3) the following new paragraph:\n(4) Failure to comply with affordable housing requirements under rehabilitation credit (A) In general In the case of any applicable rural project which is an affordable housing project (as such terms are defined in section 47(a)(3)) which is eligible for the rehabilitation credit under section 47(a), if such project violates the requirements under section 47(a)(3)(C) before the close of the recapture period (as described in paragraph (1)), then the tax under this chapter for the taxable year in which such violation occurs shall be increased by 100 percent of the aggregate decrease in the credits allowed under section 38 for all prior taxable years which would have resulted solely from reducing to zero any credit determined under section 46 which is attributable to the rehabilitation credit under section 47(a) with respect to such project. (B) Exception Subparagraph (A) shall not apply if the taxpayer demonstrates to the satisfaction of the Secretary that the violation of the requirements under section 47(a)(3)(C) has been rectified within 45 days of a determination and notice by the Secretary. (C) Regulations and guidance The Secretary shall issue such regulations or other guidance as the Secretary determines necessary or appropriate to carry out the purposes of this paragraph, including regulations or other guidance which provide for requirements for recordkeeping or information reporting for purposes of administering the requirements of this paragraph. .\n**(2) Conforming amendments**\n**(A)**\nSection 50(a)(5) of such Code, as redesignated by paragraph (1), is amended\u2014\n**(i)**\nby striking or any applicable transaction to which paragraph (3)(A) applies and inserting any applicable transaction to which paragraph (3)(A) applies, or any violation to which paragraph (4)(A) applies , and\n**(ii)**\nby striking cessation or applicable transaction and inserting cessation, applicable transaction, or violation .\n**(B)**\nSection 50(a)(7)(C) of such Code, as redesignated by paragraph (1), is amended by striking or (3) and inserting (3), or (4) .\n**(C)**\nSection 1371(d)(1) of such Code is amended by striking section 50(a)(5) and inserting section 50(a)(6) .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.\n#### 3. Elimination of rehabilitation credit basis adjustment\n##### (a) In general\nSection 50(c) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(6) Exception for rehabilitation credit In the case of the rehabilitation credit with respect to any applicable rural project (as defined in section 47(a)(3)), paragraph (1) shall not apply. .\n##### (b) Treatment in case of credit allowed to lessee\nSection 50(d) of such Code is amended by adding at the end the following: In the case of the rehabilitation credit with respect to any applicable rural project (as defined in section 47(a)(3)), paragraph (5)(B) of the section 48(d) referred to in paragraph (5) of this subsection shall not apply. .\n##### (c) Effective date\nThe amendments made by this section shall apply to property placed in service after December 31, 2025.",
      "versionDate": "2025-02-21",
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
        "actionDate": "2025-02-19",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "631",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Rural Historic Tax Credit Improvement Act",
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
        "updateDate": "2025-05-07T14:10:16Z"
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
      "date": "2025-02-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1454ih.xml"
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
      "title": "Rural Historic Tax Credit Improvement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-17T13:08:24Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Historic Tax Credit Improvement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T13:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to enhance the rehabilitation credit for buildings in rural areas.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T13:03:48Z"
    }
  ]
}
```
