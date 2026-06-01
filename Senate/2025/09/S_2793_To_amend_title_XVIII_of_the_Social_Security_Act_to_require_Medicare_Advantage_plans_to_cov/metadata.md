# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2793?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2793
- Title: Ensuring Access to Essential Providers Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2793
- Origin chamber: Senate
- Introduced date: 2025-09-11
- Update date: 2025-09-29T13:00:33Z
- Update date including text: 2025-09-29T13:00:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in Senate
- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-11: Introduced in Senate

## Actions

- 2025-09-11 - IntroReferral: Introduced in Senate
- 2025-09-11 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2793",
    "number": "2793",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Ensuring Access to Essential Providers Act of 2025",
    "type": "S",
    "updateDate": "2025-09-29T13:00:33Z",
    "updateDateIncludingText": "2025-09-29T13:00:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-11",
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
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T20:33:45Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2793is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2793\nIN THE SENATE OF THE UNITED STATES\nSeptember 11, 2025 Mr. Cassidy (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to require Medicare Advantage plans to cover items and services furnished by certain essential community providers within a service area, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Ensuring Access to Essential Providers Act of 2025 .\n#### 2. Medicare Advantage Essential Community Providers\nSection 1852(d) of the Social Security Act ( 42 U.S.C. 1395w\u201322(d) ) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nin subparagraph (D), by striking and at the end;\n**(B)**\nin subparagraph (E), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new subparagraph:\n(F) the organization meets the essential community provider standard, as described in paragraph (7). ; and\n**(2)**\nby adding at the end the following new paragraph:\n(7) Essential community provider standard (A) In general For purposes of paragraph (1)(F) and subject to subparagraph (B), in order to meet the essential community provider standard, an MA organization shall\u2014 (i) include an amount (determined by the Secretary) of available essential community providers (as described in subparagraph (E)) in each MA plan's service area in the provider network and offer to contract with each essential community provider in the service area of each plan; (ii) include in its provider network a sufficient number and a geographic distribution, as determined by the Secretary, of available essential community providers, where available, to ensure low-income individuals, individuals residing in rural areas, or individuals residing in areas designated as health professional shortage areas under section 332(a)(1)(A) of the Public Health Service Act within the service area of the MA organization have reasonable and timely access to a broad range of such providers; and (iii) meet the payment requirements to Federally qualified health centers, as described in subparagraph (C). (B) Justification for not meeting standard (i) In general If an MA plan does not meet the essential community provider standard described in subparagraph (A), the MA organization offering such plan shall include as part of the information required to be submitted under section 1854(a)\u2014 (I) an explanation regarding why the plan was unable to meet such standard; and (II) a narrative justification describing how the provider network of such plan\u2014 (aa) provides an adequate level of service for low-income enrollees or individuals residing in areas designated as health professional shortage areas within the service area of such plan; and (bb) will move toward satisfaction of the essential community provider standard prior to the start of the next plan year. (ii) Insufficient justification If the Secretary determines that the MA organization does not sufficiently explain why the applicable MA plan does not meet the essential community provider standard in the information described in clause (i), the Secretary shall not approve such plan. (C) Payment to Federally qualified health centers An MA organization shall pay a Federally qualified health center for an item or service an amount consistent with section 1857(e)(3). (D) Clarification Nothing in this paragraph may be construed to require an MA plan to provide coverage for a specific medical procedure. (E) Essential Community Provider For purposes of this paragraph, the term essential community provider means a provider that serves predominantly low-income, medically underserved individuals, including\u2014 (i) a Federally qualified health center and any similar clinic; (ii) a facility funded by the program under title XXVI of the Public Health Service Act ( 42 U.S.C. 300ff\u201311 et seq. ; commonly referred to as the Ryan White HIV/AIDS Program ); (iii) a facility operated by the Indian Health Service, an Indian tribe or tribal organization, or an urban Indian organization (as defined in section 4 of the Indian Health Care Improvement Act); (iv) a hospital, including an inpatient hospital, a hospital receiving or eligible to receive disproportionate share hospital payments under section 1886(d)(5)(F), a hospital classified as a rural referral center under section 1886(d)(5)(C), a sole community hospital (as defined in section 1886(d)(5)(D)(iii)), a free-standing cancer hospital (as described in section 1886(d)(1)(B)(v)), and a critical access hospital (as defined in section 1861(mm)(1)); (v) a mental health or substance use treatment facility; (vi) any other entity that serves predominantly low-income, medically underserved individuals, including\u2014 (I) an entity receiving funds under section 318 of the Public Health Service Act (relating to treatment of sexually transmitted diseases) through a State or unit of local government, but only if the entity is certified by the Secretary pursuant to section 340B(a)(7) of such Act; (II) a tuberculosis clinic; (III) a comprehensive hemophilia diagnostic treatment center receiving a grant under section 501(a)(2); and (IV) a black lung clinic receiving funds under section 427(a) of the Black Lung Benefits Act; (vii) a medicare-dependent, small rural hospital (as defined in section 1886(d)(4)(G)(iv)); and (viii) any provider determined appropriate by the Secretary, which may include any provider determined by the Secretary to be an essential community provider under section 1311(c)(1)(C) of the Patient Protection and Affordable Care Act ( 42 U.S.C. 18031(c)(1)(C) ). .",
      "versionDate": "2025-09-11",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2025-09-29T13:00:33Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2793is.xml"
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
      "title": "Ensuring Access to Essential Providers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-26T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Access to Essential Providers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-26T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to require Medicare Advantage plans to cover items and services furnished by certain essential community providers within a service area, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-26T03:48:17Z"
    }
  ]
}
```
