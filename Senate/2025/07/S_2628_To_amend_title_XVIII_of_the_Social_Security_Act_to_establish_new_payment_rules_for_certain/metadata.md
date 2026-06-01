# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2628?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2628
- Title: Catastrophic Specialty Hospital Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2628
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2025-12-15T19:40:18Z
- Update date including text: 2025-12-15T19:40:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2628",
    "number": "2628",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000790",
        "district": "",
        "firstName": "Raphael",
        "fullName": "Sen. Warnock, Raphael G. [D-GA]",
        "lastName": "Warnock",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Catastrophic Specialty Hospital Act of 2025",
    "type": "S",
    "updateDate": "2025-12-15T19:40:18Z",
    "updateDateIncludingText": "2025-12-15T19:40:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
          "date": "2025-07-31T21:25:38Z",
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
      "bioguideId": "W000437",
      "firstName": "Roger",
      "fullName": "Sen. Wicker, Roger F. [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Wicker",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "MS"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-10-01",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2628is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2628\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Warnock (for himself and Mr. Wicker ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to establish new payment rules for certain catastrophic specialty hospitals under the Medicare program.\n#### 1. Short title\nThis Act may be cited as the Catastrophic Specialty Hospital Act of 2025 .\n#### 2. Establishing new payment rules for certain catastrophic specialty hospitals under the Medicare program\nSection 1886(m) of the Social Security Act ( 42 U.S.C. 1395ww(m) ) is amended\u2014\n**(1)**\nin paragraph (6)(A)(i), by inserting and paragraph (8) after and (G) ; and\n**(2)**\nby adding at the end the following new paragraph:\n(8) Treatment of certain catastrophic specialty hospitals (A) In general Notwithstanding section 123 of the Medicare, Medicaid, and SCHIP Balanced Budget Refinement Act of 1999 and section 307(b) of the Medicare, Medicaid, and SCHIP Benefits Improvement and Protection Act of 2000, for cost reporting periods beginning on or after the date of the enactment of this subparagraph, the system described in paragraph (1) shall not apply and payment shall be made to a long-term care hospital without regard to such system and without regard to paragraph (6) if such long-term care hospital is designated as a catastrophic specialty hospital under subparagraph (B) with respect to such period. (B) Designation The Secretary shall designate a long-term care hospital as a catastrophic specialty hospital with respect to a cost reporting period if such long-term care hospital meets the following criteria: (i) Of the discharges from the hospital during each cost reporting period occurring during the 3-year period ending on the day before the first day of the cost reporting period for which such hospital seeks such designation, including discharges of individuals not entitled to benefits under part A, at least 80 percent were classified under an MS\u2013LTCH\u2013DRG relating to spinal cord injury or acquired brain injury (as specified by the Secretary) or would have been so classified had such individual been entitled to such benefits. (ii) The hospital offered a continuum of care during such 3-year period that included inpatient care, outpatient care, and a focus on long-term health and wellness for individuals with spinal cord injuries or acquired brain injuries. (iii) The hospital had, for the 1-year period beginning on the first day of such 3-year period and for each subsequent 1-year period occurring during such 3-year period\u2014 (I) at least 175 discharges of individuals (including individuals not entitled to benefits under part A) classified under an MS\u2013LTCH\u2013DRG relating to spinal cord injury (as specified by the Secretary) or that would have been so classified had such individual been so entitled to such benefits; and (II) at least 175 discharges of individuals (including individuals not entitled to benefits under part A) classified under an MS\u2013LTCH\u2013DRG relating to acquired brain injury (as specified by the Secretary) or that would have been so classified had such individual been so entitled to such benefits. (iv) At least 30 percent of inpatients discharged from the hospital during each cost reporting period occurring during such 3-year period (including both individuals entitled to, or enrolled for, benefits under this title and individuals not so entitled or enrolled) were admitted from outside of the State in which such hospital is located, as determined by the States of residency of such inpatients and based on such data submitted by the hospital to the Secretary as the Secretary may require. (v) The hospital has exhibited, during such 3-year period, commitment to neurorehabilitation research in specialty areas, as evidenced by one or more (as determined appropriate by the Secretary) of the following: (I) Employment of full-time dedicated neurorehabilitation research personnel who are primarily focused on spinal cord injury or acquired brain injury neurorehabilitation. (II) Contributions to the field of neurorehabilitation via publications of such personnel in peer reviewed journals in the areas of the neurorehabilitation of spinal cord injuries, acquired brain injuries, and other paralyzing neuromuscular conditions. (III) The maintenance of a clinical training program providing fellowships, residencies, or Master of Public Health programs with a focus on acquired brain injury or spinal cord injury. (IV) Maintenance of an approved medical residency training program (or affiliation with such a program) in neurology or physical medicine and rehabilitation. (C) Length of designation (i) In general A designation made by the Secretary under subparagraph (B) (or a redesignation made by the Secretary under clause (ii)) with respect to a hospital and a cost reporting period (referred to in this clause as the initial cost reporting period ) shall be effective for such initial cost reporting period and each succeeding cost reporting period occurring during the 3-year period beginning on the first day of such initial cost reporting period. (ii) Redesignation The Secretary shall, for the first cost reporting in which a designation (or redesignation) of a hospital as a catastrophic specialty hospital is due to expire under clause (i), determine whether such hospital continues to meet the criteria specified in subparagraph (B) for such cost reporting period. If the Secretary determines that such hospital does continue to meet such criteria for such cost reporting period, the Secretary shall redesignate such hospital as a catastrophic specialty hospital. If the Secretary determines that such hospital does not continue to meet such criteria for such cost reporting period, the Secretary shall\u2014 (I) provide such hospital 60 days to submit additional information demonstrating such hospital\u2019s compliance with such criteria; and (II) if such hospital fails to make such demonstration, allow such designation to expire as of the first day of such cost reporting period. .",
      "versionDate": "2025-07-31",
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
        "actionDate": "2025-09-30",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5644",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Catastrophic Specialty Hospital Act of 2025",
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
        "updateDate": "2025-09-18T20:09:18Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2628is.xml"
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
      "title": "Catastrophic Specialty Hospital Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-02T11:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Catastrophic Specialty Hospital Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T03:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to establish new payment rules for certain catastrophic specialty hospitals under the Medicare program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T03:03:25Z"
    }
  ]
}
```
