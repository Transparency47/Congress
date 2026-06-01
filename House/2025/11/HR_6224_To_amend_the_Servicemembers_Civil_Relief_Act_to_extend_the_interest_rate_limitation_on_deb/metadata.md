# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6224?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6224
- Title: Servicemember Student Loan Affordability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6224
- Origin chamber: House
- Introduced date: 2025-11-20
- Update date: 2026-01-21T01:13:47Z
- Update date including text: 2026-01-21T01:13:47Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-18 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-11-20: Introduced in House

## Actions

- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Introduced in House
- 2025-11-20 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-12-18 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6224",
    "number": "6224",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Servicemember Student Loan Affordability Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-21T01:13:47Z",
    "updateDateIncludingText": "2026-01-21T01:13:47Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-18",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T15:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-18T14:08:19Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OR"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "True",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "CA"
    },
    {
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "VA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "OR"
    },
    {
      "bioguideId": "H001066",
      "district": "4",
      "firstName": "Steven",
      "fullName": "Rep. Horsford, Steven [D-NV-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Horsford",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NV"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "DC"
    },
    {
      "bioguideId": "G000586",
      "district": "4",
      "firstName": "Jes\u00fas",
      "fullName": "Rep. Garc\u00eda, Jes\u00fas G. \"Chuy\" [D-IL-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Garc\u00eda",
      "middleName": "G. \"Chuy\"",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6224ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6224\nIN THE HOUSE OF REPRESENTATIVES\nNovember 20, 2025 Mrs. Ramirez (for herself, Ms. Bonamici , Mr. Levin , Ms. McClellan , Ms. Tlaib , Ms. Salinas , Mr. Horsford , Mr. Davis of Illinois , Ms. Norton , and Mr. Garc\u00eda of Illinois ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the Servicemembers Civil Relief Act to extend the interest rate limitation on debt entered into during military service to debt incurred during military service to consolidate or refinance student loans incurred before military service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember Student Loan Affordability Act of 2025 .\n#### 2. Interest rate limitation on debt entered into during military service to consolidate or refinance student loans incurred before military service\n##### (a) In general\nSubsection (a) of section 207 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3937 ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting on debt incurred before service after Limitation to 6 percent ;\n**(2)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively;\n**(3)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) Limitation to 6 percent on debt incurred during military service to consolidate or refinance student loans incurred before military service (A) In general Subject to subparagraph (B), an obligation or liability bearing interest at a rate in excess of 6 percent per year that is incurred by a servicemember, or the servicemember and the servicemember's spouse jointly, during military service to consolidate or refinance one or more student loans incurred by the servicemember before such military service shall not bear an interest at a rate in excess of 6 percent during the period of military service. (B) Limitation Subparagraph (A) shall apply only to the consolidation or refinancing of student loans described in such subparagraph and shall not apply to the consolidation or refinancing of any other obligation or liability. ;\n**(4)**\nin paragraph (3), as redesignated by paragraph (2) of this subsection, by inserting or (2) after paragraph (1) ; and\n**(5)**\nin paragraph (4), as so redesignated, by striking paragraph (2) and inserting paragraph (3) .\n##### (b) Implementation of limitation\nSubsection (b) of such section is amended\u2014\n**(1)**\nin paragraph (1)(A), by striking the interest rate limitation in subsection (a) and inserting an interest rate limitation in paragraph (1) or (2) of subsection (a) ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by striking effective as of date of order to active duty and inserting effective date ; and\n**(B)**\nby inserting before the period at the end the following: in the case of an obligation or liability covered by subsection (a)(1), or as of the date the servicemember (or servicemember and spouse jointly) incurs the obligation or liability concerned under subsection (a)(2) .\n##### (c) Student loan defined\nSubsection (d) of such section is amended by adding at the end the following new paragraph:\n(3) Student loan The term student loan means\u2014 (A) a Federal student loan made, insured, or guaranteed under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ); or (B) a private education loan as that term is defined in section 140(a) of the Truth in Lending Act ( 15 U.S.C. 1650(a) ). .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-11-20",
        "text": "Read twice and referred to the Committee on Veterans' Affairs. (text: CR S8278)"
      },
      "number": "3253",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Servicemember Student Loan Affordability Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-12T16:38:24Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6224ih.xml"
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
      "title": "Servicemember Student Loan Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-11T07:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Servicemember Student Loan Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-11T07:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Servicemembers Civil Relief Act to extend the interest rate limitation on debt entered into during military service to debt incurred during military service to consolidate or refinance student loans incurred before military service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-11T07:18:29Z"
    }
  ]
}
```
