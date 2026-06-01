# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6760?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6760
- Title: Protecting Access to Affordable Coverage Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6760
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-15T13:25:23Z
- Update date including text: 2026-01-15T13:25:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-16 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

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
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6760",
    "number": "6760",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Protecting Access to Affordable Coverage Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-15T13:25:23Z",
    "updateDateIncludingText": "2026-01-15T13:25:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-16T15:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DC"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NH"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6760ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6760\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mr. Pappas (for himself, Ms. Norton , Ms. Goodlander , and Ms. Johnson of Texas ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend the Patient Protection and Affordable Care Act to facilitate the enrollment of individuals in qualified health plans.\n#### 1. Short title\nThis Act may be cited as the Protecting Access to Affordable Coverage Act of 2025 .\n#### 2. Facilitating the enrollment of individuals in qualified health plans\n##### (a) Extending the open enrollment period for plan year 2026\nSection 1311(c)(6) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(6) ) is amended-\u2014\n**(1)**\nin subparagraph (B), by inserting , subject to subparagraph (E), after as determined by the Secretary ;\n**(2)**\nin subparagraph (C), by striking and at the end;\n**(3)**\nin subparagraph (D), by striking the period and inserting ; and ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(E) an open enrollment period for enrollments for plan year 2026 that begins not later than November 1, 2025, and ends not earlier than May 1, 2026. .\n##### (b) Repeal of certain verification requirements\nThe amendments made by section 71303 of an Act to provide for reconciliation pursuant to title II of H. Con. Res. 14 ( Public Law 119\u201321 ) are repealed, and any provision of law amended by such section is restored or revived as if such amendments had never been enacted.\n##### (c) Ensuring enrollment opportunities for certain individuals\n**(1) In general**\nSection 36B(c)(3)(A) of the Internal Revenue Code of 1986 is amended by striking clause (iii).\n**(2) Establishment of special enrollment period**\n**(A) In general**\nSection 1311(c)(6) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(6) ), as amended by subsection (a), is further amended\u2014\n**(i)**\nin subparagraph (D), by striking and at the end;\n**(ii)**\nin subparagraph (E), by striking the period and inserting ; and ; and\n**(iii)**\nby adding at the end the following new subparagraph:\n(F) a special enrollment period once per month for an individual who is eligible for the advance payment of premium tax credits under section 1412 and whose household income is not expected to exceed 150 percent of the poverty line for a family of the size involved. .\n**(B) Effective date**\nThe amendments made by subparagraph (A) shall apply with respect to plan years beginning on or after January 1, 2026.\n##### (d) Navigator grants\nSection 1311(i) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(i) ) is amended\u2014\n**(1)**\nin paragraph (2), by adding at the end the following new subparagraph:\n(C) Mandatory grant In awarding grants under paragraph (1), the Exchange shall, for each plan year (beginning with plan year 2026)\u2014 (i) award such grants only to entities with a physical presence in the State of such Exchange; and (ii) award such a grant to at least 1 entity described in this paragraph. ;\n**(2)**\nin paragraph (4)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by inserting (financial or otherwise) after interest ;\n**(B)**\nin clause (i), by striking or at the end;\n**(C)**\nin clause (ii), by striking the period and inserting ; or ; and\n**(D)**\nby adding at the end the following new clause:\n(iii) for plan year 2026 or a subsequent plan year\u2014 (I) be an enhanced direct enrollment entity; (II) charge any fees to applicants or enrollees; or (III) request any form of remuneration from or on behalf of any applicant or enrollee. ; and\n**(3)**\nin paragraph (6)\u2014\n**(A)**\nby striking Funding.\u2014 Grants under and inserting\nFunding.\u2014 (A) State Exchanges Grants under ; and\n**(B)**\nby adding at the end the following new subparagraph:\n(B) Federal Exchanges (i) In general For purposes of carrying out this subsection, with respect to Exchanges established and operated by the Secretary pursuant to section 1321(c), the Secretary shall obligate $100,000,000 out of amounts collected through the user fees on participating health insurance issuers pursuant to section 156.50 of title 45, Code of Federal Regulations (or any successor regulations) for fiscal year 2026 and each subsequent fiscal year. Such amount for a fiscal year shall remain available until expended. (ii) Allocation (I) In general The Secretary shall, out of amounts obligated under clause (i) for a fiscal year, allocate to each Exchange established and operated by the Secretary in a State pursuant to section 1321(c), for making grants under paragraph (1) during such fiscal year\u2014 (aa) $1,250,000; plus (bb) an amount that bears the same ratio to the total remaining obligated funds (as defined in subclause (II)) for such fiscal year as the number of individuals enrolled in a qualified health plan offered through an Exchange established in such State, or enrolled under the State plan of such State under title XIX (or waiver of such plan), during the preceding fiscal year bears to the total number of individuals enrolled in such a plan offered through an Exchange established in any State that is a specified State (as defined in subclause (II)) with respect to such fiscal year, or enrolled under the State plan of any such State under title XIX (or waiver of such plan), during such preceding fiscal year. (II) Definitions In this clause: (aa) Total remaining obligated funds The term total remaining obligated funds means, with respect to a fiscal year, $100,000,000, less an amount equal to the product of\u2014 (AA) $1,250,000; and (BB) the number of Exchanges described in clause (i) for such fiscal year. (bb) Specified State The term specified State means, with respect to a fiscal year, a State in which the Secretary establishes and operates an Exchange pursuant to section 1321(c). .",
      "versionDate": "2025-12-16",
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
        "name": "Health",
        "updateDate": "2026-01-15T13:25:23Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6760ih.xml"
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
      "title": "Protecting Access to Affordable Coverage Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting Access to Affordable Coverage Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-14T03:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Patient Protection and Affordable Care Act to facilitate the enrollment of individuals in qualified health plans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-14T03:18:23Z"
    }
  ]
}
```
