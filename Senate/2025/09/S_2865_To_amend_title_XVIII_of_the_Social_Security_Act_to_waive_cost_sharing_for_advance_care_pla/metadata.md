# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2865?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2865
- Title: Improving Access to Advance Care Planning Act
- Congress: 119
- Bill type: S
- Bill number: 2865
- Origin chamber: Senate
- Introduced date: 2025-09-18
- Update date: 2025-12-17T15:38:49Z
- Update date including text: 2025-12-17T15:38:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in Senate
- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-18: Introduced in Senate

## Actions

- 2025-09-18 - IntroReferral: Introduced in Senate
- 2025-09-18 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2865",
    "number": "2865",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Improving Access to Advance Care Planning Act",
    "type": "S",
    "updateDate": "2025-12-17T15:38:49Z",
    "updateDateIncludingText": "2025-12-17T15:38:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
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
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T16:45:42Z",
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
      "bioguideId": "C001035",
      "firstName": "Susan",
      "fullName": "Sen. Collins, Susan M. [R-ME]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "ME"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2865is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2865\nIN THE SENATE OF THE UNITED STATES\nSeptember 18 (legislative day, September 16), 2025 Mr. Warner (for himself and Ms. Collins ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend title XVIII of the Social Security Act to waive cost-sharing for advance care planning services, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Access to Advance Care Planning Act .\n#### 2. Medicare coverage of advance care planning services\n##### (a) Advance care planning services defined\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended by adding at the end the following new subsection:\n(nnn) Advance care planning services (1) In general The term advance care planning services means services provided by an eligible practitioner (as defined in paragraph (2)) to an individual, a family member of such individual, a caregiver of such individual, or such individual\u2019s representative, to discuss\u2014 (A) the health care preferences of such individual; (B) future health care decisions that may need to be made by, or on behalf of, such individual; and (C) advance directives or other standard forms, which may be completed by, or on behalf of, such individual. (2) Eligible practitioner For purposes of paragraph (1), the term eligible practitioner means\u2014 (A) a physician (as defined in subsection (r)); (B) a physician assistant (as defined in subsection (aa)(5)); (C) a nurse practitioner (as defined in subsection (aa)(5)); (D) a clinical nurse specialist (as defined in subsection (aa)(5)); (E) a clinical social worker (as defined in subsection (hh)(1)) who possesses\u2014 (i) a relevant care planning certification; or (ii) experience providing care planning conversations or similar services, as defined by the Secretary; or (F) any other practitioner determined appropriate by the Secretary. .\n##### (b) Encouraging advance care planning\n**(1) Payment**\nSection 1848(b) of the Social Security Act ( 42 U.S.C. 1395w\u20134(b) ) is amended by adding at the end the following new paragraph:\n(13) Encouraging advance care planning services (A) In general In order to encourage advance care planning services, the Secretary shall, subject to subparagraph (B), make payments (as the Secretary determines to be appropriate) under this section for advance care planning services (as defined in section 1861(nnn)) furnished on or after the date of enactment of this paragraph. (B) Policies related to payment In carrying out this paragraph, with respect to advance care planning services, the Secretary\u2014 (i) shall make payment to only 1 applicable provider for such services furnished to an individual during a period; (ii) shall not make a payment under subparagraph (A) if such payment would be duplicative of a payment that is otherwise made under this title for such services; and (iii) shall not require that an annual wellness visit (as defined in section 1861(hhh)) or an initial preventive physical examination (as defined in section 1861(ww)) be furnished as a condition of payment for such services. .\n**(2) Removing cost-sharing responsibilities for advance care planning services under part B of the Medicare program**\nSection 1833 of the Social Security Act ( 42 U.S.C. 1395l ) is amended\u2014\n**(A)**\nin subsection (a)(1)\u2014\n**(i)**\nin subparagraph (GG), by striking and at the end; and\n**(ii)**\nin subparagraph (HH), by striking the semicolon at the end and inserting the following: , and (II) with respect to advance care planning services (as described in section 1848(b)(13)) furnished on or after January 1, 2027, the amount paid shall be an amount equal to 100 percent of the lesser of the actual charge for such services or the amount determined under such section; and\n**(B)**\nin subsection (b), in the first sentence\u2014\n**(i)**\nby striking , and (13) and inserting (13) ; and\n**(ii)**\nby striking section 1861(n). and inserting the following: section 1861(n), and (14) such deductible shall not apply with respect to advance care planning services (as described in section 1848(b)(13)) furnished on or after January 1, 2027 .\n##### (c) Improvements To advance care planning through telehealth\nSection 1834(m) of the Social Security Act ( 42 U.S.C. 1395m(m) ) is amended\u2014\n**(1)**\nin paragraph (4)(C)\u2014\n**(A)**\nin clause (i), in the matter preceding subclause (I), by striking and (7) and inserting (7), and (10) ; and\n**(B)**\nin clause (ii)(X), by inserting or paragraph (10) before the period at the end; and\n**(2)**\nby adding at the end the following new paragraph:\n(10) Treatment of advance care planning services The geographic requirements described in paragraph (4)(C)(i) shall not apply with respect to telehealth services furnished on or after the date of enactment of this paragraph for purposes of furnishing advance care planning services (as defined in section 1861(nnn)). .\n##### (d) Aligning definitions\nSection 1861 of the Social Security Act ( 42 U.S.C. 1395x ) is amended\u2014\n**(1)**\nin subsection (ww)\u2014\n**(A)**\nin paragraph (1), by striking end-of-life planning (as defined in paragraph (3)) and inserting advance care planning (as defined in subsection (nnn)) ; and\n**(B)**\nby striking paragraph (3); and\n**(2)**\nin subsection (hhh)(2)\u2014\n**(A)**\nby redesignating subparagraph (I) as subparagraph (J);\n**(B)**\nby redesignating subparagraph (I) as subparagraph (J); and\n**(C)**\nby inserting after subparagraph (H) the following new subparagraph:\n(I) Advance care planning services (as defined in subsection (nnn)). .\n#### 3. HHS provider outreach\n##### (a) Outreach\nThe Secretary of Health and Human Services (in this section referred to as the Secretary ) shall conduct outreach to physicians and appropriate non-physician practitioners participating under the Medicare program under title XVIII of the Social Security Act with respect to Medicare payment for advance care planning services furnished to individuals to discuss their health care preferences, identified by Healthcare Common Procedure Coding System (HCPCS) codes 99497 and 99498 (or any successor to such codes). Such outreach shall include a new, comprehensive, one-time education initiative to inform such physicians and practitioners of the addition of such services as a covered benefit under the Medicare program, including the requirements for beneficiary eligibility for such services.\n##### (b) Report\nNot later than 1 year after the date of completion of the outreach described in subsection (a), the Secretary shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives a report on the outreach conducted under subsection (a). Such report shall include a description of the methods used for such outreach.\n#### 4. MedPAC report on the furnishing of advance care planning services and the use of advance care planning codes under the Medicare program\n##### (a) Study\nThe Medicare Payment Advisory Commission (in this section referred to as the Commission ) shall conduct a study on advance care planning under the Medicare program under title XVIII of the Social Security Act. Such study shall include an analysis of\u2014\n**(1)**\nthe furnishing of advance care planning services to Medicare beneficiaries, including\u2014\n**(A)**\nwhich providers are trained to provide such services;\n**(B)**\nwhich providers are eligible to provide such services under the Medicare program;\n**(C)**\nthe length and frequency of the visits for furnishing such services; and\n**(D)**\nany barriers related to providers furnishing, or beneficiaries being furnished, such services;\n**(2)**\nthe use of advance care planning Current Procedural Terminology (CPT) codes to bill for the furnishing of advance care planning services to Medicare beneficiaries, including\u2014\n**(A)**\ncircumstances under which codes other than advance care planning CPT codes are used to bill for such services under the Medicare program and why providers do not use advance care planning CPT codes; and\n**(B)**\nany barriers to providers using advance care planning CPT codes to bill for such services under the Medicare program; and\n**(3)**\nsuch other items determined appropriate by the Commission.\n##### (b) Report\nNot later than June 30, 2027, the Commission shall submit to the Committee on Finance of the Senate and the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives a report on the study conducted under subsection (a), together with recommendations for such legislation and administrative action as the Commission determines appropriate.",
      "versionDate": "2025-09-18",
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
        "updateDate": "2025-12-17T15:38:49Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2865is.xml"
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
      "title": "Improving Access to Advance Care Planning Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-07T05:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Improving Access to Advance Care Planning Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title XVIII of the Social Security Act to waive cost-sharing for advance care planning services, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:24Z"
    }
  ]
}
```
