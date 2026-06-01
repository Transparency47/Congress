# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5737?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5737
- Title: ROOT Act
- Congress: 119
- Bill type: HR
- Bill number: 5737
- Origin chamber: House
- Introduced date: 2025-10-10
- Update date: 2025-12-09T18:18:07Z
- Update date including text: 2025-12-09T18:18:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-10: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-10-10: Introduced in House

## Actions

- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Introduced in House
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-10-10 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-10",
    "latestAction": {
      "actionDate": "2025-10-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5737",
    "number": "5737",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001086",
        "district": "1",
        "firstName": "Diana",
        "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
        "lastName": "Harshbarger",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "ROOT Act",
    "type": "HR",
    "updateDate": "2025-12-09T18:18:07Z",
    "updateDateIncludingText": "2025-12-09T18:18:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
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
      "actionDate": "2025-10-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-10",
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
          "date": "2025-10-10T16:32:15Z",
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
          "date": "2025-10-10T16:32:10Z",
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
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-10-10",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5737ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5737\nIN THE HOUSE OF REPRESENTATIVES\nOctober 10, 2025 Mrs. Harshbarger (for herself and Mr. Moore of Utah ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title XVIII of the Social Security Act to modify data collection requirements for appropriate use criteria for applicable imaging services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Radiology Outpatient Ordering Transmission Act or the ROOT Act .\n#### 2. Modification of appropriate use criteria data collection for applicable imaging services\n##### (a) In general\nSection 1834(q) of the Social Security Act ( 42 U.S.C. 1395m(q) ) is amended\u2014\n**(1)**\nin paragraph (3)(B)(ii)\u2014\n**(A)**\nin subclause (IV), by striking generates and provides to the ordering professional a certification or documentation that ; and\n**(B)**\nby adding at the end the following new subclause:\n(VIII) Beginning January 1, 2026, the mechanism provides to the Secretary\u2014 (aa) the information described in subclauses (III) and (IV); (bb) the information described in paragraph (4)(B); and (cc) such other information as the Secretary determines to be appropriate, at such time, and in such form and manner, as the Secretary may specify. ;\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (A), by striking clause (ii) and inserting the following:\n(ii) beginning January 1, 2026, comply with such requirements as the Secretary may establish. ;\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin the heading, by striking furnishing professional and inserting qualified clinical decision support mechanism ;\n**(ii)**\nin the matter preceding clause (i)\u2014\n**(I)**\nby striking with January 1, 2017 and inserting January 1, 2026 ; and\n**(II)**\nby striking payment for such service may only be made if the claim for the service includes and inserting the qualified decision support mechanism shall maintain and report to the Secretary under subparagraph (F) ; and\n**(iii)**\nin clause (iii), by striking (if different from the furnishing professional) ;\n**(C)**\nin subparagraph (C), by adding at the end the following new clauses:\n(iv) Clinical trials An applicable imaging service that is ordered for an individual as part of a clinical trial. (v) Small and rural practices An applicable imaging service ordered by an ordering professional practicing in a small practice (consisting of 15 or fewer ordering professionals), or a practice in a health professional shortage area (as designated under section 332(a)(1)(A) of the Public Health Service Act) located in a rural area. (vi) Specified exemptions The following types of applicable imaging services: (I) A mammography. (II) A lung cancer screening performed using computed tomography. (III) A colonography performed using computed tomography. (IV) Such other preventive or screening imaging services as the Secretary determines appropriate. ;\n**(D)**\nin subparagraph (D), by adding at the end the following new clause:\n(iv) Any other payment system determined appropriate by the Secretary. ; and\n**(E)**\nby adding at the end the following new subparagraphs:\n(E) Furnishing professional requirement Beginning January 1, 2026, with respect to an applicable imaging service furnished in an applicable setting and paid for under an applicable payment system (as defined in subparagraph (D)), the furnishing professional shall include the national provider identifier of the ordering professional (if different from the furnishing professional) on the claim for the service. (F) Reporting requirements The Secretary shall provide, through guidance or rulemaking, information on appropriate ways that each qualified clinical decision support mechanism may report the information maintained under subparagraph (B) to the Secretary to support the Secretary in implementing paragraphs (5) and (6). ;\n**(3)**\nin paragraph (5)\u2014\n**(A)**\nin the heading, by striking outlier and inserting low compliant ;\n**(B)**\nby striking subparagraphs (A) and (B) and inserting the following:\n(A) In general With respect to applicable imaging services furnished on or after January 1, 2026, the Secretary shall determine on an annual basis the total number of ordering professionals who are designated as low compliant ordering professionals under subparagraph (B). (B) Low compliant ordering professionals The Secretary shall designate ordering professionals with a compliance rate (as determined under subparagraph (D)) lower than an amount determined by the Secretary as low compliant ordering professionals. ;\n**(C)**\nin paragraph (C), by striking outlier and inserting low compliant ;\n**(D)**\nby striking subparagraph (D) and inserting the following:\n(D) Determination of compliance rate (i) In general (I) Compliance rates For applicable imaging services furnished on or after January 1, 2026, the Secretary shall determine a compliance rate (as defined in clause (ii)) for each ordering professional for a period specified by the Secretary. (II) Use of data In determining a compliance rate for an ordering professional under subclause (I), the Secretary shall use data made available to the Secretary by qualified clinical decision support mechanisms published in the list under paragraph (3)(C) that were consulted by the ordering professional for the period specified by the Secretary under subclause (I). (ii) Definition of compliance rate (I) In general In this subparagraph, the term compliance rate means, with respect to the requirement that an ordering professional consult with a qualified decision support mechanism when ordering an applicable imaging service under paragraph (4)(A)(i), the ratio (expressed as a percentage) of\u2014 (aa) the number of claims for orders for an applicable imaging service from such ordering professional during the period specified by the Secretary under clause (i)(I) that provided the qualified decision support mechanism consulted by such ordering professional; and (bb) the total number of orders for an applicable imaging service from such ordering professional during such period. (II) Exclusion of excepted orders In calculating the compliance rate for an ordering professional under subclause (I), the Secretary shall exclude from the total number of orders in item (bb) of such subclause any order for an applicable imaging service described in paragraph (4)(C). ; and\n**(E)**\nin subparagraph (E), by striking outlier and inserting low compliant ;\n**(4)**\nby striking paragraph (6) and inserting the following:\n(6) Study and report on low compliant ordering professionals and utilization of applicable imaging services (A) In general Not later than January 1, 2031, and every 5 years thereafter, the Secretary shall conduct a study regarding the compliance rates calculated under paragraph (5) and submit a report to Congress that\u2014 (i) discusses\u2014 (I) such rates and compliance with this subsection; (II) the impact this subsection has on the utilization of applicable imaging services; and (III) potential mechanisms for improving compliance with this subsection, including\u2014 (aa) prior authorization for applicable imaging services ordered by low compliant ordering professionals; (bb) any payment adjustment related to the services, or a subset of services, that the Secretary may designate under the fee schedule under section 1848; or (cc) other mechanisms determined appropriate by the Secretary; and (ii) proposes alternative compliance rate thresholds for low compliant ordering professionals for purposes of paragraph (5)(B). ; and\n**(5)**\nby adding at the end the following new paragraph:\n(8) Specialty society endorsement In specifying applicable appropriate use criteria for applicable imaging services under paragraph (2) and qualified clinical decision support mechanisms under paragraph (3), the Secretary shall substantially adhere to the approach described in section 414.94 of title 42, Code of Federal Regulations (as in effect on January 1, 2023). .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on January 1, 2026.",
      "versionDate": "2025-10-10",
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
        "actionDate": "2025-05-08",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1692",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Radiology Outpatient Ordering Transmission (ROOT) Act",
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
        "name": "Health",
        "updateDate": "2025-12-09T18:18:07Z"
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
      "date": "2025-10-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5737ih.xml"
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
      "title": "ROOT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-17T11:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ROOT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Radiology Outpatient Ordering Transmission Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-17T11:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title XVIII of the Social Security Act to modify data collection requirements for appropriate use criteria for applicable imaging services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-17T11:18:13Z"
    }
  ]
}
```
