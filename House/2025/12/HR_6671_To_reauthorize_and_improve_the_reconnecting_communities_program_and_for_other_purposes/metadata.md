# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6671?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6671
- Title: REPAIR Infrastructure Act
- Congress: 119
- Bill type: HR
- Bill number: 6671
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-02-26T09:07:05Z
- Update date including text: 2026-02-26T09:07:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2026-02-02 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6671",
    "number": "6671",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "R000579",
        "district": "18",
        "firstName": "Patrick",
        "fullName": "Rep. Ryan, Patrick [D-NY-18]",
        "lastName": "Ryan",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "REPAIR Infrastructure Act",
    "type": "HR",
    "updateDate": "2026-02-26T09:07:05Z",
    "updateDateIncludingText": "2026-02-26T09:07:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-02-02T19:38:27Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "AL"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001231",
      "district": "22",
      "firstName": "John",
      "fullName": "Rep. Mannion, John W. [D-NY-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Mannion",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6671ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6671\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Ryan (for himself and Mr. Figures ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo reauthorize and improve the reconnecting communities program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restoring Essential Public Access and Improving Resilient Infrastructure Act or the REPAIR Infrastructure Act .\n#### 2. Restoring essential public access and improving resilient infrastructure (REPAIR infrastructure) program\n##### (a) Reauthorization\n**(1) In general**\nThere is authorized to be appropriated out of the Highway Trust Fund (other than the Mass Transit Account) $3,000,000,000 for each of fiscal years 2027 through 2031 to carry out the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ), of which\u2014\n**(A)**\n$750,000,000 shall be for planning grants under subsection (c) of that section; and\n**(B)**\n$2,250,000,000 shall be for capital construction grants under subsection (d) of that section.\n**(2) Treatment**\nAmounts made available under paragraph (1) shall be\u2014\n**(A)**\navailable for obligation in the same manner as if those amounts were apportioned under chapter 1 of title 23, United States Code, except that those amounts shall remain available until expended; and\n**(B)**\nadministered as if\u2014\n**(i)**\napportioned under chapter 1 of title 23, United States Code; or\n**(ii)**\nallocated under chapter 2 of title 23, United States Code, in the case of amounts made available to a Tribal government.\n**(3) Conforming amendments**\nSection 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ) is amended\u2014\n**(A)**\nin the section heading, by striking Reconnecting communities pilot and inserting Restoring essential public access and improving resilient infrastructure (REPAIR infrastructure) program ;\n**(B)**\nin subsection (b), in the matter preceding paragraph (1), by striking pilot ; and\n**(C)**\nin subsection (f), by striking the period of fiscal years 2022 through 2026 and inserting the period of fiscal years 2027 through 2031 .\n**(4) Clerical amendment**\nThe table of contents in section 1(b) of the Infrastructure Investment and Jobs Act ( Public Law 117\u201358 ; 135 Stat. 429) is amended by striking the item relating to section 11509 and inserting the following:\nSec. 11509. Restoring essential public access and improving resilient infrastructure (REPAIR infrastructure) program. .\n##### (b) Selection criteria\nSection 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ) is amended\u2014\n**(1)**\nin subsection (c)(4)(B)\u2014\n**(A)**\nin the matter preceding clause (i), by striking the demonstration by the applicant that ;\n**(B)**\nin clause (i), by inserting the demonstration by the applicant that before the eligible facility ;\n**(C)**\nin clause (ii)\u2014\n**(i)**\nin the matter preceding subclause (I), by inserting the demonstration by the applicant that before the eligible facility ; and\n**(ii)**\nin subclause (II), by striking and at the end;\n**(D)**\nin clause (iii)\u2014\n**(i)**\nby inserting the demonstration by the applicant that before on the basis ; and\n**(ii)**\nby striking the period at the end and inserting a semicolon; and\n**(E)**\nby adding at the end the following:\n(iv) if information is available, the extent to which the project will promote\u2014 (I) new or improved affordable transportation options to increase safe mobility and connectivity for all, including for people with disabilities, to promote access to economic activity centers, including workforce housing, jobs, healthcare, grocery stores, schools, places of worship, recreation, childcare, natural infrastructure, and parks; (II) safe accommodation for all users and seamless integration with the surrounding character, context, and land use, with consideration of the economy and public health; or (III) economically thriving communities for individuals to work, live, and play by creating transportation choices for individuals to move freely and have meaningful access to opportunities; (v) if information is available, the extent to which the application demonstrates\u2014 (I) a robust community participation plan that engages community members most impacted by the existing facility; (II) formal partnerships, backed by signed commitment letters and a budget, with organizations based in communities adjacent to the project area, including community-based organizations and community development financial institutions; (III) an approach that meaningfully redresses historic economic and physical barriers and benefits underserved communities; or (IV) a representative community advisory group, advisory board, or other place-based management organization with oversight authority, including a community land trust, community benefit agreement, or other community development activity to redress transportation-related gaps in access; and (vi) if information is available, the extent to which the applicant demonstrates\u2014 (I) creative placemaking; or (II) community restoration, stabilization, and mechanisms to preserve affordability, limit disruption of low-income communities, and prevent displacement of existing residents, such as\u2014 (aa) assistance for renters and legacy homeowners and small businesses; (bb) preservation, rehabilitation, and expansion of location-efficient affordable housing; (cc) mixed-income mixed use development; (dd) affordable commercial spaces; and (ee) other community wealth-building activities. ; and\n**(2)**\nin subsection (d)(4)\u2014\n**(A)**\nby striking the paragraph designation and heading and all that follows through basis of\u2014 in subparagraph (B) in the matter preceding clause (i) and inserting the following:\n(4) Selection criteria (A) Solicitation The Secretary shall solicit applications for capital construction grants. (B) Criteria The Secretary shall evaluate applications received under subparagraph (A) on the basis of\u2014 ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (vii), by striking ; and at the end and inserting and a description of how those feasibility studies provide a basis for better access to daily destinations; ;\n**(ii)**\nin clause (viii)(II), by striking the period at the end and inserting a semicolon; and\n**(iii)**\nby adding at the end the following:\n(ix) a description of how partner resources and other Federal and non-Federal funds will support the project, including a detailed description of all funding commitments, financing, and in-kind support; (x) the extent to which the project will encourage public and private investments to support greater commercial and mixed-income residential development near public transportation, along rural main streets, or in walkable neighborhoods; (xi) the extent to which the project will promote\u2014 (I) new or improved affordable transportation options to increase safe mobility and connectivity for all, including for people with disabilities, to promote access to economic activity centers, including workforce housing, jobs, healthcare, grocery stores, schools, places of worship, recreation, childcare, natural infrastructure, and parks; (II) safe accommodation for all users and seamless integration with the surrounding character, context, and land use, with consideration of the economy and public health; or (III) economically thriving communities for individuals to work, live, and play by creating transportation choices for individuals to move freely and have meaningful access to opportunities; (xii) the extent to which the application demonstrates\u2014 (I) a robust community participation plan that engages community members most impacted by the existing facility; (II) formal partnerships, backed by signed commitment letters and a budget, with organizations based in communities adjacent to the project area, including community-based organizations and community development financial institutions; (III) an approach that meaningfully redresses historic economic and physical barriers and benefits underserved communities; or (IV) a representative community advisory group, advisory board, or other place-based management organization with oversight authority, including a community land trust, community benefit agreement, or other community development activity to redress transportation-related gaps in access; and (xiii) the extent to which the applicant demonstrates\u2014 (I) creative placemaking; or (II) community restoration, stabilization, and mechanisms to preserve affordability, limit disruption of low-income communities, and prevent displacement of existing residents, such as\u2014 (aa) assistance for renters and legacy homeowners and small businesses; (bb) preservation, rehabilitation, and expansion of location-efficient affordable housing; (cc) mixed-income mixed use development; (dd) affordable commercial spaces; and (ee) other community wealth-building activities. ; and\n**(C)**\nby adding at the end the following:\n(C) Additional information An applicant may include in an application under subparagraph (A) information about land use policies that reduce regional displacement pressures in the area in which the project is located, including measurements of, of the land that permits residential use\u2014 (i) the percentage that allows duplexes, accessory dwelling units, or higher unit count; (ii) the percentage that allows triplexes or higher unit count; (iii) the percentage that allows quadruplexes or higher unit count; and (iv) the percentage that has no minimum parking requirements. .\n##### (c) Travel lanes\nSection 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ) is amended\u2014\n**(1)**\nby redesignating subsections (e) through (g) as subsections (f) through (h), respectively; and\n**(2)**\nby inserting after subsection (d) the following:\n(e) Travel lanes Amounts from a grant under this section may not be used for a project that increases the number of travel lanes on an existing highway. .\n#### 3. Eligibility for REPAIR infrastructure program projects\n##### (a) National highway performance program\nSection 119(d)(2) of title 23, United States Code, is amended by adding at the end the following:\n(T) Construction of a project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). .\n##### (b) Surface transportation block grant program\nSection 133 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by inserting after paragraph (3) the following:\n(4) Projects eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). ; and\n**(2)**\nin subsection (c)(2), by striking (5) and inserting (4) .\n##### (c) Highway safety improvement program\nSection 148 of title 23, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby redesignating paragraphs (1) through (16) as paragraphs (2) through (17), respectively;\n**(B)**\nby inserting before paragraph (2) (as so redesignated) the following:\n(1) Divisive roadway infrastructure (A) In general The term divisive roadway infrastructure means a highway or other transportation facility that creates a barrier to community connectivity, including barriers to mobility, access, or economic development, due to high speeds, grade separations, or other design factors. (B) Inclusions The term divisive roadway infrastructure includes\u2014 (i) a limited access highway; (ii) a viaduct; and (iii) any other principal arterial facility. ; and\n**(C)**\nin subparagraph (B) of paragraph (5) (as so redesignated)\u2014\n**(i)**\nby redesignating clause (xxix) as clause (xxx);\n**(ii)**\nby inserting after clause (xxviii) the following:\n(xxix) A project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). ; and\n**(iii)**\nin clause (xxx) (as so redesignated), by striking (xxviii) and inserting (xxix) ;\n**(2)**\nin subsection (c)\u2014\n**(A)**\nin paragraph (1)(A), by striking subsections (a)(13) and inserting subsections (a)(14) ; and\n**(B)**\nin paragraph (2)(A)\u2014\n**(i)**\nin clause (v), by striking and at the end;\n**(ii)**\nin clause (vi), by adding and after the semicolon at the end; and\n**(iii)**\nby adding at the end the following:\n(vii) to evaluate the impacts of divisive roadway infrastructure; ; and\n**(3)**\nin subsection (d)(2)(B)(i), by striking subsection (a)(13) and inserting subsection (a)(14) .\n##### (d) Congestion mitigation and air quality improvement program\nSection 149(b) of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (10)(B), by striking or at the end;\n**(2)**\nin paragraph (11)(B), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(12) if the project is a project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). .\n##### (e) Territorial highway program\nSection 165(c)(6)(A) of title 23, United States Code, is amended by adding at the end the following:\n(viii) Projects eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). .\n##### (f) National highway freight program\nSection 167(h)(5)(C) of title 23, United States Code, is amended\u2014\n**(1)**\nby redesignating clauses (xxii) and (xxiii) as clauses (xxiii) and (xxiv), respectively;\n**(2)**\nby inserting after clause (xxi) the following:\n(xxii) A project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). ; and\n**(3)**\nin clause (xxiii) (as so redesignated), by striking (xxi) and inserting (xxii) .\n##### (g) Rural surface transportation grant program\nSection 173(e)(1) of title 23, United States Code, is amended\u2014\n**(1)**\nin subparagraph (F), by striking or at the end;\n**(2)**\nin subparagraph (G), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(H) a project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ). .\n##### (h) Carbon reduction program\nSection 175(c) of title 23, United States Code, is amended by striking paragraph (2) and inserting the following:\n(2) Flexibility (A) In general If the Secretary makes a certification described in subparagraph (B), a State\u2014 (i) shall first use funds apportioned under section 104(b)(7) for a project eligible for assistance under the REPAIR infrastructure program under section 11509 of the Infrastructure Investment and Jobs Act ( 23 U.S.C. 101 note; Public Law 117\u201358 ), as determined by the Secretary, taking into consideration any projects that received planning grants under that program; and (ii) if funds remain available after carrying out clause (i), in addition to eligible projects under paragraph (1), may use funds apportioned under section 104(b)(7) for a project eligible under section 133(b). (B) Certification A certification referred to in subparagraph (A) is a certification by the Secretary that the State has demonstrated a reduction in transportation emissions\u2014 (i) as estimated on a per capita basis; and (ii) as estimated on a per unit of economic output basis. .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-10",
        "text": "Read twice and referred to the Committee on Environment and Public Works."
      },
      "number": "3413",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "REPAIR Infrastructure Act",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-01-08T15:22:21Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6671ih.xml"
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
      "title": "REPAIR Infrastructure Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REPAIR Infrastructure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restoring Essential Public Access and Improving Resilient Infrastructure Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and improve the reconnecting communities program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:23Z"
    }
  ]
}
```
