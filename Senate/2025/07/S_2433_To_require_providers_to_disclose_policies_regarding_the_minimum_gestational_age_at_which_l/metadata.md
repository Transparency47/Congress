# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2433?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2433
- Title: Neonatal Care Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2433
- Origin chamber: Senate
- Introduced date: 2025-07-24
- Update date: 2026-05-15T20:39:31Z
- Update date including text: 2026-05-15T20:39:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-24: Introduced in Senate
- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-24: Introduced in Senate

## Actions

- 2025-07-24 - IntroReferral: Introduced in Senate
- 2025-07-24 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-24",
    "latestAction": {
      "actionDate": "2025-07-24",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2433",
    "number": "2433",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Neonatal Care Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-05-15T20:39:31Z",
    "updateDateIncludingText": "2026-05-15T20:39:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-24",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-24",
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
        "item": [
          {
            "date": "2025-07-24T16:26:54Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-24T16:26:54Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "FL"
    },
    {
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "WY"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "MS"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2433is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2433\nIN THE SENATE OF THE UNITED STATES\nJuly 24, 2025 Mr. Cotton (for himself, Mr. Scott of Florida , Ms. Lummis , and Mrs. Hyde-Smith ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo require providers to disclose policies regarding the minimum gestational age at which life-saving care will be provided to an infant in the case of a premature birth.\n#### 1. Short title\nThis Act may be cited as the Neonatal Care Transparency Act of 2025 .\n#### 2. Findings\nCongress finds as follows:\n**(1)**\nDifferent hospitals have varying capacities to resuscitate premature babies.\n**(2)**\nThere are parents of premature babies who have arrived at level 3 and level 4 neonatal intensive care units expecting medical intervention, only to find that life-saving treatment is not offered for babies born before a certain gestational point.\n**(3)**\nSome hospitals in the United States universally forgo intensive care for babies born before 22 weeks gestation, while others provide such care to nearly all babies born alive.\n**(4)**\nData indicates that neonatal outcomes are best for premature babies when the baby is born at a center that consistently intervenes with life-saving treatment.\n**(5)**\nParents deserve a new level of obstetric and neonatal transparency to ensure medical excellence in circumstances of extreme prematurity and parental consent to the course of treatment.\n#### 3. Disclosure requirements\n##### (a) Hospital requirement\nEach hospital shall publicly disclose the policy of such hospital regarding the provision of life-saving care to an infant in the case of a premature birth, including\u2014\n**(1)**\nwhether there is a minimum gestational age at which life-saving care will be provided to an infant in the case of a premature birth;\n**(2)**\nwhether the decision to provide life-saving care to an infant in the case of a premature birth is made on a case-by-case basis; and\n**(3)**\nthe process by which the hospital, in the case of a premature birth or expected premature birth, would transfer the infant and mother to the nearest facility with a neonatal intensive care unit that would provide life-saving care to the infant, if the hospital does not have the capacity to provide life-saving care to such infant.\n##### (b) Practitioner requirement\nEach obstetrician, or other health care practitioner who provides obstetric services to patients, shall, at the first prenatal visit of a patient, disclose to the patient the policy of any hospital at which the obstetrician or practitioner has admitting privileges regarding the provision of life-saving care to an infant in the case of a premature birth, including\u2014\n**(1)**\nwhether there is a minimum gestational age at which life-saving care will be provided to an infant in the case of a premature birth;\n**(2)**\nwhether the decision to provide life-saving care to an infant in the case of a premature birth is made on a case-by-case basis; and\n**(3)**\nthe process by which the hospital, in the case of a premature birth or expected premature birth, would arrange for the transfer the infant and mother to the nearest facility with a neonatal intensive care unit that would provide life-saving care to the infant, if the facility in which the practitioner is providing services does not have the capacity to provide life-saving care to such infant.\n#### 4. Hospital disclosures regarding care for premature births\nSection 1866(a)(1) of the Social Security Act ( 42 U.S.C. 1395cc(a)(1) ) is amended\u2014\n**(1)**\nby moving subparagraphs (W) and (X) 2 ems to the left;\n**(2)**\nin subparagraph (X), by striking and at the end;\n**(3)**\nin subparagraph (Y), by striking the period at the end and inserting , and ; and\n**(4)**\nby inserting after subparagraph (Y) the following new subparagraph:\n(Z) beginning on or after January 1, 2026, in the case of a hospital, to\u2014 (i) satisfy the disclosure requirement under section 3(a) of the Neonatal Care Transparency Act of 2025 ; and (ii) require each practitioner that provides obstetric services at such hospital to satisfy the disclosure requirement under section 3(b) of such Act. .\n#### 5. Prohibiting Federal Medicaid and CHIP funding for hospitals and obstetrics providers that do not satisfy disclosure requirements\n##### (a) In general\nSection 1903(i) of the Social Security Act ( 42 U.S.C. 1396b(i) ) is amended\u2014\n**(1)**\nin paragraph (26), by striking ; or and inserting a semicolon;\n**(2)**\nin paragraph (27), by striking the period at the end and inserting ; or ;\n**(3)**\nby inserting after paragraph (27) the following new paragraph:\n(28) with respect to any amounts expended for care or services furnished under the plan by a hospital or by a health care provider who provides obstetric services to individuals who are eligible for medical assistance under the plan unless such hospital or provider satisfies the disclosure requirements described in section 3 of Neonatal Care Transparency Act of 2025 . ; and\n**(4)**\nin the third sentence, by striking and (18) and inserting (18), and (28) .\n##### (b) Application to CHIP\nSection 2107(e)(1)(O) of the Social Security Act ( 42 U.S.C. 1397gg(e)(1)(O) ) is amended by striking and (17) and inserting (17), and (28) .\n##### (c) Effective date\nThe amendments made by this subsection shall take effect on the date that is 180 days after the date of enactment of this Act.",
      "versionDate": "2025-07-24",
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
        "actionDate": "2026-03-12",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7912",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Neonatal Care Transparency Act of 2026",
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
        "updateDate": "2025-09-24T19:15:08Z"
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
      "date": "2025-07-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2433is.xml"
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
      "title": "Neonatal Care Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-29T11:03:32Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Neonatal Care Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-05T05:08:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require providers to disclose policies regarding the minimum gestational age at which life-saving care will be provided to an infant in the case of a premature birth.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:48Z"
    }
  ]
}
```
