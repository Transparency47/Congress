# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4370?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4370
- Title: PCTEC Act
- Congress: 119
- Bill type: S
- Bill number: 4370
- Origin chamber: Senate
- Introduced date: 2026-04-22
- Update date: 2026-05-13T19:00:40Z
- Update date including text: 2026-05-13T19:00:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-04-22: Introduced in Senate
- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-22: Introduced in Senate

## Actions

- 2026-04-22 - IntroReferral: Introduced in Senate
- 2026-04-22 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-22",
    "latestAction": {
      "actionDate": "2026-04-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4370",
    "number": "4370",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "PCTEC Act",
    "type": "S",
    "updateDate": "2026-05-13T19:00:40Z",
    "updateDateIncludingText": "2026-05-13T19:00:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
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
      "actionDate": "2026-04-22",
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
          "date": "2026-04-22T15:54:37Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4370is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4370\nIN THE SENATE OF THE UNITED STATES\nApril 22, 2026 Mr. Kaine introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish and support primary care team education centers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Primary Care Team Education Centers Act or the PCTEC Act .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto establish and expand primary care team education centers to\u2014\n**(A)**\nenhance and support the capacity of community-based ambulatory patient care centers to serve as sites to develop the next generation of health professionals to care for the needs of communities; and\n**(B)**\ndevelop and implement innovative employment, appointment, and compensation models to enhance and expand preceptors in primary care; and\n**(2)**\nto improve access to care by ensuring that more health professional students have clinical education experiences in multidisciplinary primary care settings.\n#### 3. Primary care team education centers\n##### (a) In general\nPart P of title III of the Public Health Service Act ( 42 U.S.C. 280g et seq. ) is amended by adding at the end the following:\n399V\u20138. Support and development of primary care team education centers (a) Program authorized The Secretary may award grants to eligible entities for the purpose of establishing and expanding primary care team education centers. (b) Amount and duration A grant awarded under subsection (a) shall be for a term of not more than 5 years and the maximum grant award may not be more than $1,000,000 a year. (c) Use of funds An eligible entity receiving a grant under subsection (a) shall use grant funds to establish or expand a primary care team education center to\u2014 (1) develop or enhance partnerships with institutions of higher education that provide a recognized postsecondary credential in health care, or health care organizations that the Secretary has determined are capable of carrying out such a grant or contract, to\u2014 (A) address clinical faculty, clinical site, and clinical preceptor shortages for health professionals by\u2014 (i) establishing mutually beneficial and sustainable agreements for precepting by the clinical staff of the primary care team education center, through innovative employment, appointment, and compensation models designed to enhance\u2014 (I) recruitment and retention of such staff; and (II) the role of such staff in ensuring the effectiveness and sustainability of the clinical site as part of the health professional student clinical education of a partnering entity; and (ii) implementing a plan to address recruitment and retention of primary care team education center clinical staff who have entered into agreements under clause (i), which may include paying preceptor salaries; and (B) support health professional student training in primary care by\u2014 (i) implementing curricula to integrate health professional student clinical education into primary care team education centers, including strategies to address health professional well-being and mental health; and (ii) providing support for health professional students, including assistance for housing near, or transportation to or from, the clinical site during the clinical training period; (2) integrate and expand the role of health professionals not traditionally involved in the eligible entity\u2019s primary care team, such as school nurses in elementary or secondary schools and community health workers, as part of the service continuum of the primary care team education center; and (3) promote career advancement for health professionals employed by the primary care team education center. (d) Award basis In selecting recipients for grants under subsection (a), the Secretary shall give priority to grant applications that\u2014 (1) demonstrate how the program to be supported under the grant will, for the region to be served\u2014 (A) identify the health professions with labor shortages; and (B) increase the number of health professionals with disadvantaged backgrounds working in such health professions; and (2) provide preceptor training and support to encourage eligible preceptors to participate in clinical training, including nurses and advanced practice nurses. (e) Limitation The recipient of a grant under section 749A or 340H shall not be eligible to receive a grant under subsection (a). (f) Technical assistance (1) In general The Secretary shall, directly or through grants or contracts, provide technical assistance for eligible entities receiving grants under subsection (a). (2) Limitation For each year, the Secretary shall use not more than 5 percent of the amount made available to carry out this section for technical assistance under this subsection. (g) Annual report The Secretary shall submit an annual report to Congress on the grants awarded under subsection (a). Each such report shall, at a minimum, include\u2014 (1) the total number of grants awarded under subsection (a); (2) a description of the primary care team education centers supported under each such grant; (3) the number of students, by profession, who engaged in such primary care team education centers during the applicable academic year, in the aggregate and disaggregated by grantee; (4) in the aggregate and disaggregated by grantee\u2014 (A) the number of health professional staff at such primary care team education centers engaged in classroom teaching or clinical precepting under the grant; (B) an estimate of the number of teaching or precepting hours provided under the grant; (C) the number of health professional students, and the number of advanced practice nursing students, trained under the grant; and (D) the number of health care professional preceptors recruited and retained under the grant; and (5) a description of how each grantee met the needs of the health professionals served under the grant. (h) Definitions In this section: (1) Eligible entity The term eligible entity means an entity described in any of clauses (i) through (v) of section 749A(g)(3)(B). (2) Institution of higher education The term institution of higher education has the meaning given the term in section 102 of the Higher Education Act of 1965. (3) Preceptor The term preceptor means a health professional who provides supervision and personalized experiential learning training and instruction and mentoring opportunities in the clinical practice of a health profession to a student in a health profession. (4) Primary care team The term primary care team means a team of 2 or more health providers who provide health services to individuals, families, or communities by working collaboratively with patients and their caregivers, to the extent preferred by each patient, to accomplish shared goals within and across settings in order to achieve coordinated, high-quality care. (i) Authorization of appropriations There is authorized to be appropriated to carry out this section\u2014 (1) $10,000,000 for fiscal year 2027; (2) $25,000,000 for fiscal year 2028; (3) $50,000,000 for fiscal year 2029; and (4) such sums as may be necessary for each fiscal year thereafter. .\n##### (b) Limitation on eligibility for other teaching health center development grants\n**(1) Section 749A**\nSection 749A of the Public Health Service Act ( 42 U.S.C. 293l\u20131 ) is amended\u2014\n**(A)**\nby redesignating subsections (f) and (g) as subsections (g) and (h), respectively; and\n**(B)**\nby inserting after subsection (e) the following:\n(f) Limitation A recipient of a grant under section 399V\u20138 shall not be eligible to receive a grant under this section. .\n**(2) Graduate medical education program teaching health centers**\nSection 340H(a) of the Public Health Service Act ( 42 U.S.C. 256h(a) ) is amended by adding at the end the following:\n(4) Limitation A recipient of a grant under section 399V\u20138 shall not be eligible to receive a payment under this section. .\n**(3) Conforming amendment**\nSection 760(c)(2)(A) of the Public Health Service Act ( 42 U.S.C. 294k(c)(2)(A) ) is amended by striking section 749A(f) and inserting section 749A(g) .",
      "versionDate": "2026-04-22",
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
        "updateDate": "2026-05-13T19:00:40Z"
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
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4370is.xml"
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
      "title": "PCTEC Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-30T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "PCTEC Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Primary Care Team Education Centers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-30T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish and support primary care team education centers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-30T04:48:34Z"
    }
  ]
}
```
