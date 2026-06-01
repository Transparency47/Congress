# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5064?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5064
- Title: Save our Safety-Net Hospitals Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5064
- Origin chamber: House
- Introduced date: 2025-08-29
- Update date: 2026-02-05T17:34:35Z
- Update date including text: 2026-02-05T17:34:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-29: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-08-29: Introduced in House

## Actions

- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Introduced in House
- 2025-08-29 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-29",
    "latestAction": {
      "actionDate": "2025-08-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5064",
    "number": "5064",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000598",
        "district": "1",
        "firstName": "Nick",
        "fullName": "Rep. LaLota, Nick [R-NY-1]",
        "lastName": "LaLota",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "Save our Safety-Net Hospitals Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-05T17:34:35Z",
    "updateDateIncludingText": "2026-02-05T17:34:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-29",
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
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-29",
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
          "date": "2025-08-29T17:33:15Z",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-08-29",
      "state": "NY"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "IN"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "NY"
    },
    {
      "bioguideId": "M001163",
      "district": "7",
      "firstName": "Doris",
      "fullName": "Rep. Matsui, Doris O. [D-CA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Matsui",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-10-28",
      "state": "NY"
    },
    {
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "NY"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-12-02",
      "state": "NY"
    },
    {
      "bioguideId": "V000136",
      "district": "2",
      "firstName": "Gabe",
      "fullName": "Rep. Vasquez, Gabe [D-NM-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Vasquez",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "NM"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5064ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5064\nIN THE HOUSE OF REPRESENTATIVES\nAugust 29, 2025 Mr. LaLota (for himself, Mr. Lawler , Mr. Mrvan , and Ms. Clarke of New York ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title XIX of the Social Security Act to modify certain limitations on disproportionate share hospital payment adjustments under the Medicaid program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Save our Safety-Net Hospitals Act of 2025 .\n#### 2. Modifying certain limitations on disproportionate share hospital payment adjustments under the Medicaid program\n##### (a) In general\nSection 1923(g) of the Social Security Act ( 42 U.S.C. 1396r\u20134(g) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by striking (other than a hospital described in paragraph (2)(B)) ;\n**(ii)**\nin clause (i), by inserting with respect to such hospital and year after described in subparagraph (B) ; and\n**(iii)**\nin clause (ii)\u2014\n**(I)**\nin subclause (I), by striking and at the end;\n**(II)**\nin subclause (II), by striking the period and inserting ; and ; and\n**(III)**\nby adding at the end the following new subclause:\n(III) payments made under title XVIII or by an applicable plan (as defined in section 1862(b)(8)(F)) for such services. ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the matter preceding clause (i), by striking in this clause are and inserting in this subparagraph are, with respect to a hospital and a year, ; and\n**(ii)**\nby adding at the end the following new clause:\n(iii) Individuals who are eligible for medical assistance under the State plan or under a waiver of such plan and for whom the State plan or waiver is a payor for such services after application of benefits under title XVIII or under an applicable plan (as defined in section 1862(b)(8)(F)), but only if the hospital has in the aggregate incurred costs exceeding payments under such State plan, waiver, title XVIII, or applicable plan for such services furnished to such individuals during such year. ;\n**(2)**\nby striking paragraph (2);\n**(3)**\nby redesignating paragraph (3) as paragraph (2); and\n**(4)**\nin paragraph (2), as so redesignated, by striking Notwithstanding paragraph (2) of this subsection (as in effect on October 1, 2021), paragraph (2) and inserting Paragraph (2) .\n##### (b) Effective date\n**(1) In general**\nExcept as provided in paragraph (2), the amendments made by this section shall apply to payment adjustments made under section 1923 of the Social Security Act ( 42 U.S.C. 1396r\u20134 ) for Medicaid State plan rate years beginning on or after the date of enactment of this Act.\n**(2) State option to distribute unspent DSH allotments from prior years up to modified cap**\n**(A) In general**\nIf, for any Medicaid State plan rate year that begins on or after October 1, 2021, and before the date of enactment of this Act, a State did not spend the full amount of its Federal fiscal year allotment under section 1923 of the Social Security Act ( 42 U.S.C. 1396r\u20134 ) applicable to that State plan rate year, the State may use the unspent portion of such allotment to increase the amount of any payment adjustment made to a hospital for such rate year, provided that\u2014\n**(i)**\nsuch payment adjustment (as so increased) is consistent with subsection (g) of such section (as amended by this section); and\n**(ii)**\nthe total amount of all payment adjustments for the State plan rate year (as so increased) does not exceed the disproportionate share hospital allotment for the State and applicable Federal fiscal year under subsection (f) of such section.\n**(B) No recoupment of payments already made to hospitals**\nA State shall not recoup any payment adjustment made by the State to a hospital for a Medicaid State plan rate year described in subparagraph (A) if such payment adjustment is consistent with section 1923(g) of such Act ( 42 U.S.C. 1396r\u20134(g) ) as in effect on October 1, 2021.\n**(C) Authority to permit retroactive modification of State plan amendments to allow for increases**\n**(i) In general**\nSubject to paragraph (2), solely for the purpose of allowing a State to increase the amount of a payment adjustment to a hospital for a Medicaid State plan rate year described in subparagraph (A) pursuant to this paragraph, a State may retroactively modify a provision of the Medicaid State plan, a waiver of such plan, or a State plan amendment that relates to such rate year and the Secretary may approve such modification.\n**(ii) Deadline**\nA State may not submit a request for approval of a retroactive modification to a provision of the Medicaid State plan, a waiver of such plan, or a State plan amendment for a Medicaid State plan rate year after the date by which the State is required to submit the independent certified audit for that State plan rate year as required under section 1923(j)(2) of the Social Security Act ( 42 U.S.C. 1396r\u20134(j)(2) ).\n**(D) Reporting**\nIf a State increases a payment adjustment made to a hospital for a Medicaid State plan rate year pursuant to this paragraph, the State shall include information on such increased payment adjustment as part of the next annual report submitted by the State under section 1923(j)(1) of the Social Security Act ( 42 U.S.C. 1396r\u20134(j)(1) ).",
      "versionDate": "2025-08-29",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-09",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2743",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Save Our Safety-Net Hospitals Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2026-02-03",
        "text": "Became Public Law No: 119-75."
      },
      "number": "7148",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Consolidated Appropriations Act, 2026",
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
        "name": "Health",
        "updateDate": "2025-09-19T17:19:55Z"
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
      "date": "2025-08-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5064ih.xml"
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
      "title": "Save our Safety-Net Hospitals Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-03T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Save our Safety-Net Hospitals Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-03T04:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XIX of the Social Security Act to modify certain limitations on disproportionate share hospital payment adjustments under the Medicaid program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-03T04:03:21Z"
    }
  ]
}
```
