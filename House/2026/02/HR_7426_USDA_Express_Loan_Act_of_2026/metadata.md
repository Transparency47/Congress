# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7426?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7426
- Title: USDA Express Loan Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7426
- Origin chamber: House
- Introduced date: 2026-02-09
- Update date: 2026-02-18T13:31:57Z
- Update date including text: 2026-02-18T13:31:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-09: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2026-02-09: Introduced in House

## Actions

- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Introduced in House
- 2026-02-09 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-09",
    "latestAction": {
      "actionDate": "2026-02-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7426",
    "number": "7426",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "F000475",
        "district": "1",
        "firstName": "Brad",
        "fullName": "Rep. Finstad, Brad [R-MN-1]",
        "lastName": "Finstad",
        "party": "R",
        "state": "MN"
      }
    ],
    "title": "USDA Express Loan Act of 2026",
    "type": "HR",
    "updateDate": "2026-02-18T13:31:57Z",
    "updateDateIncludingText": "2026-02-18T13:31:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-09",
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
      "actionDate": "2026-02-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-09",
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
          "date": "2026-02-09T17:04:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
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
      "bioguideId": "G000605",
      "district": "13",
      "firstName": "Adam",
      "fullName": "Rep. Gray, Adam [D-CA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Gray",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7426ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7426\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 9, 2026 Mr. Finstad (for himself and Mr. Gray ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Consolidated Farm and Rural Development Act to support the prompt approval of certain loans and loan guarantees, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the USDA Express Loan Act of 2026 .\n#### 2. Prompt approval of loans and loan guarantees\nSection 333A of the of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1983a ) is amended\u2014\n**(1)**\nin subsection (g)\u2014\n**(A)**\nby striking paragraph (1) and inserting the following:\n(1) Real estate and operating guaranteed loans (A) In general The Secretary shall provide to lenders a short, simplified application form for real estate and operating guaranteed loans under this title, for loans of not more than $1,000,000. (B) Notice Within 5 business days after receipt of a complete application to guarantee a farm ownership or operating loan that meets the requirements under subparagraph (A) originated by a Preferred Certified Lender or Certified Lender, the Secretary shall notify the lender as to whether the application is approved or disapproved. (C) Maximum guarantee Notwithstanding any other provision of this Act, the percentage of the principal amount of a loan which may be guaranteed pursuant to this paragraph shall not exceed\u2014 (i) 90 percent, in the case of a loan not exceeding $125,000; (ii) 75 percent, in the case of a loan of more than $125,000 and not more than $500,000; or (iii) 50 percent, in the case of a loan of more than $500,000 and not more than $1,000,000. ; and\n**(B)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively, and inserting after paragraph (1) the following:\n(2) Business and industry guaranteed loans to assist rural entities (A) In general The Secretary shall develop an application process that accelerates, to the maximum extent practicable, the processing of applications for business and industry guaranteed loans to assist rural entities, as described under section 310B(a)(2)(A), for loans not exceeding $400,000. (B) Exception The accelerated application process, as provided under subparagraph (A), shall apply to loans not exceeding $600,000 if there is not a significant increased risk of a default on the loan, as determined by the Secretary. ; and\n**(2)**\nby striking subsection (h).",
      "versionDate": "2026-02-09",
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
        "actionDate": "2026-02-13",
        "text": "Referred to the House Committee on Agriculture."
      },
      "number": "7567",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Farm, Food, and National Security Act of 2026",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-02-11T13:45:41Z"
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
      "date": "2026-02-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7426ih.xml"
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
      "title": "USDA Express Loan Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-10T10:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "USDA Express Loan Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-10T10:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Consolidated Farm and Rural Development Act to support the prompt approval of certain loans and loan guarantees, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-10T10:18:26Z"
    }
  ]
}
```
