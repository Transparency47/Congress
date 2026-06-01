# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3763?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3763
- Title: ALS Better Care Act
- Congress: 119
- Bill type: S
- Bill number: 3763
- Origin chamber: Senate
- Introduced date: 2026-02-03
- Update date: 2026-03-31T23:15:45Z
- Update date including text: 2026-03-31T23:15:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-03: Introduced in Senate
- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-02-03: Introduced in Senate

## Actions

- 2026-02-03 - IntroReferral: Introduced in Senate
- 2026-02-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3763",
    "number": "3763",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "ALS Better Care Act",
    "type": "S",
    "updateDate": "2026-03-31T23:15:45Z",
    "updateDateIncludingText": "2026-03-31T23:15:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-03",
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
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T17:58:54Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3763is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3763\nIN THE SENATE OF THE UNITED STATES\nFebruary 3, 2026 Ms. Murkowski (for herself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to provide coverage of ALS-related services under the Medicare program for individuals diagnosed with amyotrophic lateral sclerosis, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the ALS Better Care Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nAmyotrophic lateral sclerosis (in this section, referred to as ALS ) is a progressive and debilitating neurodegenerative disease.\n**(2)**\nKey services that include (but are not limited to) providing specialized physician or nurse practitioner support, occupational therapy support, speech pathology support, physical therapy, dietary support, respiratory support, registered nurse support, and coordination of the furnishing of durable medical equipment are crucial for managing the complex medical needs of ALS patients.\n**(3)**\nStudies have shown ALS clinics that provide these key services to ALS patients extend these patients\u2019 lifespans and improve the quality of their lives.\n**(4)**\nThese key services are furnished by a range of healthcare professionals.\n**(5)**\nFacilities providing care to ALS patients currently face inadequate Medicare reimbursement for the key services they offer to these patients.\n**(6)**\nInsufficient reimbursement creates significant challenges for facilities specializing in ALS care, resulting in extended wait times for patients in need of crucial services and hampering the ability of these facilities to innovate and improve the quality of care provided to ALS patients.\n**(7)**\nImproved reimbursement rates would encourage facilities to invest in research, innovation, and technology, leading to enhanced treatment options for ALS and improved patient outcomes.\n**(8)**\nRemote medical management options for individuals suffering from ALS must be a crucial part of access to care for such individuals, especially those living in rural areas or care deserts.\n**(9)**\nTelehealth is an essential management option referred to in paragraph (8) and can assist in delivering timely and comprehensive care, as ALS patients living in rural areas or care deserts often face challenges in accessing specialized ALS care and could otherwise be required to travel long travel distances\u2014often with caregivers or family members.\n**(10)**\nTelehealth is especially important in maintaining access to care for ALS patients as the disease progresses and ALS patients have more limited mobility, which may make it challenging to attend in-person appointments regularly.\n**(11)**\nLow funding and difficulty in staffing for ALS clinical trials delay the development and availability of potential treatments and therapies for individuals living with the disease.\n**(12)**\nInadequate funding for ALS clinical trials also impedes the ability to attract and retain qualified researchers, clinicians, and support staff, limiting the overall progress and success of these trials.\n#### 3. Providing for coverage of ALS-related services under the medicare program for individuals diagnosed with amyotrophic lateral sclerosis\n##### (a) In general\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (s)(2)\u2014\n**(A)**\nby adding and at the end of subparagraph (JJ); and\n**(B)**\nby adding at the end the following new subparagraph:\n(KK) ALS-related services (as defined in subsection (nnn)) furnished on or after January 1, 2027; ; and\n**(2)**\nby adding at the end the following new subsection:\n(nnn) ALS-Related services (1) ALS-related services The term ALS-related services means the following items and services that are furnished to a covered ALS individual in an outpatient setting by a qualified provider (as defined in section 1834(aa)(6)) (or by another provider of services under an arrangement made by a qualified provider) for the care and treatment of such an individual with respect to the progression of amyotrophic lateral sclerosis: (A) Specialized physician or nurse practitioner support. (B) Occupational therapy support. (C) Speech pathology support. (D) Physical therapy. (E) Dietary support. (F) Respiratory support. (G) Registered nurse support. (H) Coordination of the furnishing of durable medical equipment necessary for the management of the complex medical needs of a covered ALS individual. (2) Covered ALS individual The term covered ALS individual means an individual who is medically determined to have amyotrophic lateral sclerosis (as described in section 226(h)). .\n##### (b) Payment for ALS-Related services\nSection 1834 of the Social Security Act ( 42 U.S.C. 1395m ) is amended by adding at the end the following new subsections:\n(aa) Payment for ALS-Related services (1) In general The Secretary shall implement a payment system under which a single payment determined in accordance with the succeeding paragraphs is made to a qualified provider (as defined in paragraph (6)) for ALS-related services (as defined in paragraph (1) of section 1861(nnn)) furnished to a covered ALS individual (as defined in paragraph (2) of such section) during a visit, in addition to any other payment that may be made for such services under this title. (2) Base payment amount (A) In general The amount of the single payment described in paragraph (1) for ALS-related services furnished during a year is equal to\u2014 (i) for 2027, $800; (ii) for 2028, $800 (or, if greater, the payment amount recommended by the Comptroller General of the United States in the report described in subparagraph (C)); and (iii) for 2029 and each subsequent year\u2014 (I) the amount for the preceding year, increased by the ALS services market basket percentage increase (as defined in clause (i) of subparagraph (B)) for such year; or (II) in the case such year is an applicable year (as defined in clause (ii) of such subparagraph), the payment amount recommended by the Comptroller General in the most recent report submitted under subparagraph (C), if greater than the amount that would be determined for such year under subclause (I). (B) Definitions In this paragraph: (i) ALS services market basket percentage increase The term ALS services market basket percentage increase means, for a year, the Secretary\u2019s estimate of the percentage increase in costs of an appropriate mix, as determined by the Secretary, of items and services that are ALS-related services over the preceding year. (ii) Applicable year The term applicable year means 2030 and every third year thereafter. (C) Report by the Comptroller General (i) In general Not later than January 1, 2027, and not later than January 1 of every third year thereafter, the Comptroller General of the United States shall, in consultation with qualified providers eligible for payment under this subsection, submit to the Secretary a report that recommends a single payment amount for ALS-related services that takes into account the average amount of payment for each item or service included in ALS-related services that the Comptroller General estimates would have been payable\u2014 (I) under this title for such a service based on per patient utilization data from whichever single year during the covered period (as defined in clause (ii)) with respect to such report has the highest per patient utilization of ALS-related services, even if such service is not payable for a particular covered ALS individual because of the application of section 1862(a)(1)(A) with respect to an item or service provided to such individual; (II) in the case an estimate is unable to be determined pursuant to subclause (I), by health insurance issuers and group health plans (as such terms are defined in section 2791 of the Public Health Service Act) and MA plans under part C for such a service, based on such data from whichever single year during the covered period with respect to such report has the highest per patient utilization of ALS-related services; and (III) in the case an estimate is unable to be determined pursuant to subclause (II), based on the recommendation of the Specialty Society Relative Value Scale Update Committee of the American Medical Association or the estimate of the Comptroller General for such a service. (ii) Definition of covered period In this subparagraph, the term covered period means\u2014 (I) with respect to the first report submitted under this subparagraph, 2022 through 2024; (II) with respect to the second such report, 2026 through 2028; and (III) with respect to the third report and each subsequent report, the period that begins 3 years after the covered period for the preceding report. (3) Payment adjustments The payment system under this subsection shall include a payment adjustment\u2014 (A) for each qualified provider that is participating in at least one clinical trial identified on the clinicaltrials.gov database (or any successor database) of the National Institutes of Health to account for the increased cost borne by such a qualified provider during such a clinical trial; and (B) for a medical service or technology which is furnished as a part of ALS-related services for which, as determined by the Secretary\u2014 (i) payment under this subsection for such service or technology was not being made in the preceding year; and (ii) the cost of such service or technology is not insignificant in relation to the payment amount (as determined under this subsection) payable for ALS-related services. (4) Mechanism for payments For purposes of making payments for ALS-related services, the Secretary shall establish a mechanism under the payment system under this subsection which makes payment when a qualified provider submits a claim for payment which includes, with respect to a covered ALS individual, an alphanumeric code issued under the International Classification of Diseases, 10th Revision, Clinical Modification ( ICD\u201310\u2013CM ) and its subsequent revisions that is for the treatment of a diagnosis of amyotrophic lateral sclerosis. (5) No cost sharing Payment under this subsection shall be made only on an assignment-related basis without any cost sharing. (6) Qualified provider In this section, the term qualified provider means a provider of services that\u2014 (A) is capable of furnishing ALS-related services; and (B) meets requirements as the Secretary prescribes by regulation to implement subparagraph (A), in consultation with\u2014 (i) covered ALS individuals and their representatives; (ii) physicians who provide ALS-related services and their representatives; and (iii) professional and non-profit organizations with expertise in amyotrophic lateral sclerosis. (7) Implementation (A) In general Except as provided under subparagraph (B), the Secretary may implement the provisions of this subsection by program instruction or otherwise. (B) Rulemaking The Secretary shall implement paragraph (6), through notice and comment rulemaking. .\n##### (c) Conforming amendments\n**(1) Section 1833(t)**\nSection 1833(t) of the Social Security Act ( 42 U.S.C. 1395(t) ) is amended by adding at the end the following new paragraph:\n(23) Ensuring supplemental payments for ALS-related services Any covered OPD service furnished to a covered ALS individual (as defined in section 1861(nnn)(2)) that is otherwise payable to a qualified provider (as defined in section 1834(aa)(6)) pursuant to paragraph (4) shall be payable under such paragraph notwithstanding any payment made under section 1834(aa). .\n**(2) Definition of arrangements**\nSection 1861(w)(1) of the Social Security Act ( 42 U.S.C. 1395x(w)(1) ) is amended by inserting qualified provider (as defined in section 1834(aa)(6)) with respect to ALS-related services (as defined in subsection (nnn)), before or hospice program .\n#### 4. Report on challenges with respect to the administration and staffing of amyotrophic lateral sclerosis clinical trials\nNot later than 90 days after the date of the enactment of this Act, the Secretary of Health and Human Services, acting through the Director of the National Institute of Neurological Disorders and Stroke of the National Institutes of Health, shall submit to Congress and publish on the internet website of the agency a report that identifies\u2014\n**(1)**\nany challenges with respect to the administration and staffing of clinical trials for the prevention, diagnosis, mitigation, treatment, or cure of amyotrophic lateral sclerosis;\n**(2)**\nactions that the Director of the National Institute of Neurological Disorders and Stroke can take to address such challenges; and\n**(3)**\nany legislative recommendations (including requests for appropriations) to further improve the administration of such clinical trials.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2026-02-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7336",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "ALS Better Care Act",
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
        "updateDate": "2026-02-26T17:48:09Z"
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
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3763is.xml"
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
      "title": "ALS Better Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-21T04:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "ALS Better Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-21T04:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to provide coverage of ALS-related services under the Medicare program for individuals diagnosed with amyotrophic lateral sclerosis, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-21T04:48:22Z"
    }
  ]
}
```
