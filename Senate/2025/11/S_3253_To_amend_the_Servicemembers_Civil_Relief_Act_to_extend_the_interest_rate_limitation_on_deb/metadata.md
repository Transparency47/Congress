# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3253?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3253
- Title: Servicemember Student Loan Affordability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3253
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-01-21T01:12:20Z
- Update date including text: 2026-01-21T01:12:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs. (text: CR S8278)
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs. (text: CR S8278)

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3253",
    "number": "3253",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Servicemember Student Loan Affordability Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T01:12:20Z",
    "updateDateIncludingText": "2026-01-21T01:12:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs. (text: CR S8278)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
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
          "date": "2025-11-20T19:08:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NY"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "False",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "CA"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "False",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "NJ"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3253is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3253\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Durbin (for himself, Ms. Duckworth , and Mrs. Gillibrand ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo amend the Servicemembers Civil Relief Act to extend the interest rate limitation on debt entered into during military service to debt incurred during military service to consolidate or refinance student loans incurred before military service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Servicemember Student Loan Affordability Act of 2025 .\n#### 2. Interest rate limitation on debt entered into during military service to consolidate or refinance student loans incurred before military service\n##### (a) In general\nSubsection (a) of section 207 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3937 ) is amended\u2014\n**(1)**\nin paragraph (1), by inserting on debt incurred before service after Limitation to 6 percent ;\n**(2)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively;\n**(3)**\nby inserting after paragraph (1) the following new paragraph (2):\n(2) Limitation to 6 percent on debt incurred during military service to consolidate or refinance student loans incurred before military service (A) In general Subject to subparagraph (B), an obligation or liability bearing interest at a rate in excess of 6 percent per year that is incurred by a servicemember, or the servicemember and the servicemember's spouse jointly, during military service to consolidate or refinance one or more student loans incurred by the servicemember before such military service shall not bear an interest at a rate in excess of 6 percent during the period of military service. (B) Limitation Subparagraph (A) shall apply only to the consolidation or refinancing of student loans described in such subparagraph and shall not apply to the consolidation or refinancing of any other obligation or liability. ;\n**(4)**\nin paragraph (3), as redesignated by paragraph (2) of this subsection, by inserting or (2) after paragraph (1) ; and\n**(5)**\nin paragraph (4), as so redesignated, by striking paragraph (2) and inserting paragraph (3) .\n##### (b) Implementation of limitation\nSubsection (b) of such section is amended\u2014\n**(1)**\nin paragraph (1)(A), by striking the interest rate limitation in subsection (a) and inserting an interest rate limitation in paragraph (1) or (2) of subsection (a) ; and\n**(2)**\nin paragraph (2)\u2014\n**(A)**\nin the paragraph heading, by striking effective as of date of order to active duty and inserting effective date ; and\n**(B)**\nby inserting before the period at the end the following: in the case of an obligation or liability covered by subsection (a)(1), or as of the date the servicemember (or servicemember and spouse jointly) incurs the obligation or liability concerned under subsection (a)(2) .\n##### (c) Student loan defined\nSubsection (d) of such section is amended by adding at the end the following new paragraph:\n(3) Student loan The term student loan means\u2014 (A) a Federal student loan made, insured, or guaranteed under title IV of the Higher Education Act of 1965 ( 20 U.S.C. 1070 et seq. ); or (B) a private education loan as that term is defined in section 140(a) of the Truth in Lending Act ( 15 U.S.C. 1650(a) ). .",
      "versionDate": "2025-11-20",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Subcommittee on Economic Opportunity."
      },
      "number": "6224",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Servicemember Student Loan Affordability Act of 2025",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-19T17:34:59Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3253is.xml"
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
      "title": "Servicemember Student Loan Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T06:38:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Servicemember Student Loan Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T06:38:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Servicemembers Civil Relief Act to extend the interest rate limitation on debt entered into during military service to debt incurred during military service to consolidate or refinance student loans incurred before military service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T06:33:35Z"
    }
  ]
}
```
