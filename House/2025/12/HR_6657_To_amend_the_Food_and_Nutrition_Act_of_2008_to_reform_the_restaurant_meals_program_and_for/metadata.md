# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6657?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6657
- Title: Restaurant Meals Program Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6657
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-05-16T08:07:50Z
- Update date including text: 2026-05-16T08:07:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Nutrition and Foreign Agriculture.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6657",
    "number": "6657",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001233",
        "district": "8",
        "firstName": "Mark",
        "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
        "lastName": "Messmer",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Restaurant Meals Program Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-16T08:07:50Z",
    "updateDateIncludingText": "2026-05-16T08:07:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Nutrition and Foreign Agriculture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
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
          "date": "2025-12-11T16:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:06:29Z",
              "name": "Referred to"
            }
          },
          "name": "Nutrition and Foreign Agriculture Subcommittee",
          "systemCode": "hsag03"
        }
      },
      "systemCode": "hsag00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6657ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6657\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Messmer introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Food and Nutrition Act of 2008 to reform the restaurant meals program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Restaurant Meals Program Reform Act of 2025 .\n#### 2. Restaurant meals program\nSection 9(h) of the Food and Nutrition Act of 2008 ( 7 U.S.C. 2018(h) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking determines that the participation and inserting the following:\ndetermines that\u2014 (A) the private establishment is a retail food store that\u2014 (i) operates a prepared food section, hot bar, or deli counter; (ii) is not primarily engaged in the sale of quick-service or fast-food items, as determined by the Secretary; and (iii) meets all State and local food safety and health standards applicable to grocery stores or supermarkets; and (B) the participation ;\n**(2)**\nby redesignating paragraph (3) as paragraph (6);\n**(3)**\nby inserting after paragraph (2) the following:\n(3) Eligible meals Benefits may be redeemed under the program under this subsection from a private establishment described in paragraph (2)(A) only for meals from a prepared food section, hot bar, or deli counter that\u2014 (A) are intended for immediate consumption; and (B) contain at least\u2014 (i) 1 fruit or vegetable; and (ii) 1 protein, as defined by the Secretary. (4) Single authorization (A) In general A retail food store authorized under section 9 shall not be required to obtain a separate authorization for participating in the program under this section. (B) EBT systems The Secretary shall ensure that State agencies maintain or update EBT card coding and retailer coding systems necessary to restrict redemption of benefits under this subsection to eligible households. (5) Spousal exclusion Notwithstanding any other provision of this Act, a spouse of an individual eligible for benefits under the supplemental nutrition assistance program shall not be eligible to participate in the program under this subsection. ; and\n**(4)**\nin paragraph (6) (as so redesignated), by striking Senate a report on the effectiveness of a and inserting the following:\nSenate, and make publicly available, a report describing\u2014 (A) the number of private establishments participating in the program under this subsection; (B) for each private establishment participating in the program under this subsection\u2014 (i) the name and location of the private establishment; and (ii) the amount of benefits redeemed at the private establishment; (C) the number of individuals receiving benefits under the program under this subsection; (D) the costs of the program under this subsection; and (E) the effectiveness of the .",
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
        "actionDate": "2025-11-20",
        "text": "Read twice and referred to the Committee on Agriculture, Nutrition, and Forestry."
      },
      "number": "3240",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "McSCUSE ME Act of 2025",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-01-07T16:09:21Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6657ih.xml"
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
      "title": "Restaurant Meals Program Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-04T06:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Restaurant Meals Program Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-04T06:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Food and Nutrition Act of 2008 to reform the restaurant meals program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-04T06:18:25Z"
    }
  ]
}
```
