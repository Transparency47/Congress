# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/548
- Title: HSA Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 548
- Origin chamber: House
- Introduced date: 2025-01-16
- Update date: 2026-02-25T09:06:12Z
- Update date including text: 2026-02-25T09:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-16: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-16: Introduced in House

## Actions

- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Introduced in House
- 2025-01-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-16",
    "latestAction": {
      "actionDate": "2025-01-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/548",
    "number": "548",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "V000134",
        "district": "24",
        "firstName": "Beth",
        "fullName": "Rep. Van Duyne, Beth [R-TX-24]",
        "lastName": "Van Duyne",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "HSA Modernization Act",
    "type": "HR",
    "updateDate": "2026-02-25T09:06:12Z",
    "updateDateIncludingText": "2026-02-25T09:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-16",
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
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-16",
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
          "date": "2025-01-16T14:02:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "C001120",
      "district": "2",
      "firstName": "Dan",
      "fullName": "Rep. Crenshaw, Dan [R-TX-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Crenshaw",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "PA"
    },
    {
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-24",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr548ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 548\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 16, 2025 Ms. Van Duyne (for herself, Mr. Crenshaw , and Mr. Meuser ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to modernize health savings accounts.\n#### 1. Short title\nThis Act may be cited as the HSA Modernization Act .\n#### 2. Individuals without service-connected disability and eligible for certain veterans benefits permitted to contribute to health savings accounts\n##### (a) In general\nSection 223(c)(1)(C) of the Internal Revenue Code of 1986 is amended by striking for a service-connected disability (within the meaning of section 101(16) of title 38, United States Code) .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 3. Individuals entitled to part A of Medicare by reason of age allowed to contribute to health savings accounts\n##### (a) In general\nSection 223(c)(1)(B) of the Internal Revenue Code of 1986 is amended by striking and at the end of clause (ii), by striking the period at the end of clause (iii) and inserting , and , and by adding at the end the following new clause:\n(iv) entitlement to hospital insurance benefits under part A of title XVIII of the Social Security Act by reason of section 226(a) of such Act. .\n##### (b) Treatment of health insurance purchased from account\nSection 223(d)(2)(C)(iv) of such Code is amended by inserting and who is not an eligible individual after who has attained the age specified in section 1811 of the Social Security Act .\n##### (c) Coordination with penalty on distributions not used for qualified medical expenses\nSection 223(f)(4)(C) of such Code is amended by striking Subparagraph (A) and inserting Except in the case of an eligible individual, subparagraph (A)\n##### (d) Conforming amendment\nSection 223(b)(7) of such Code is amended by inserting (other than an entitlement to benefits described in subsection (c)(1)(B)(iv)) after Social Security Act .\n##### (e) Effective date\nThe amendments made by this section shall apply to months beginning after December 31, 2025, in taxable years ending after such date.\n#### 4. Individuals eligible for Indian Health Service assistance not disqualified from health savings accounts\n##### (a) In general\nSection 223(c)(1) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(E) Special rule for individuals eligible for assistance under Indian Health Service programs For purposes of subparagraph (A)(ii), an individual shall not be treated as covered under a health plan described in such subparagraph merely because the individual receives hospital care or medical services under a medical care program of the Indian Health Service or of a tribal organization. .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 5. Allowance of bronze and catastrophic plans in connection with health savings accounts\n##### (a) In general\nSection 223(c)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(H) Bronze and catastrophic plans treated as high deductible health plans The term high deductible health plan shall include any plan described in subsection (d)(1)(A) or (e) of section 1302 of the Patient Protection and Affordable Care Act. .\n##### (b) Effective date\nThe amendment made by this section shall apply to months beginning after December 31, 2025, in taxable years ending after such date.\n#### 6. Safe harbor for absence of deductible for mental health services\n##### (a) In general\nSection 223(c)(2) of the Internal Revenue Code of 1986, as amended by this Act, is amended by adding at the end the following new subparagraph:\n(I) Safe harbor for absence of deductible for mental health services A plan shall not fail to be treated as a high deductible health plan by reason of failing to have a deductible for not more than the first $500 of any mental health benefits (as defined in section 9812(e)(4)) specified by the plan for purposes of this subparagraph. .\n##### (b) Effective date\nThe amendments made by this section shall apply to plan years beginning after December 31, 2025.\n#### 7. Special rule for certain medical expenses incurred before establishment of health savings account\n##### (a) In general\nSection 223(d)(2) of the Internal Revenue Code of 1986 is amended by adding at the end the following new subparagraph:\n(E) Treatment of certain medical expenses incurred before establishment of account If a health savings account is established during the 60-day period beginning on the date that coverage of the account beneficiary under a high deductible health plan begins, then, solely for purposes of determining whether an amount paid is used for a qualified medical expense, such account shall be treated as having been established on the date that such coverage begins. .\n##### (b) Effective date\nThe amendment made by this section shall apply with respect to coverage beginning after December 31, 2025.\n#### 8. Allow both spouses to make catch-up contributions to the same health savings account\n##### (a) In general\nSection 223(b)(5) of the Internal Revenue Code of 1986 is amended to read as follows:\n(5) Special rule for married individuals with family coverage (A) In general In the case of individuals who are married to each other, if both spouses are eligible individuals and either spouse has family coverage under a high deductible health plan as of the first day of any month\u2014 (i) the limitation under paragraph (1) shall be applied by not taking into account any other high deductible health plan coverage of either spouse (and if such spouses both have family coverage under separate high deductible health plans, only one such coverage shall be taken into account), (ii) such limitation (after application of clause (i)) shall be reduced by the aggregate amount paid to Archer MSAs of such spouses for the taxable year, and (iii) such limitation (after application of clauses (i) and (ii)) shall be divided equally between such spouses unless they agree on a different division. (B) Treatment of additional contribution amounts If both spouses referred to in subparagraph (A) have attained age 55 before the close of the taxable year, the limitation referred to in subparagraph (A)(iii) which is subject to division between the spouses shall include the additional contribution amounts determined under paragraph (3) for both spouses. In any other case, any additional contribution amount determined under paragraph (3) shall not be taken into account under subparagraph (A)(iii) and shall not be subject to division between the spouses. .\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 9. Maximum contribution limit to health savings account increased to amount of deductible and out-of-pocket limitation\n##### (a) Self-Only coverage\nSection 223(b)(2)(A) of the Internal Revenue Code of 1986 is amended by striking $2,250 and inserting the amount in effect under subsection (c)(2)(A)(ii)(I) .\n##### (b) Family coverage\nSection 223(b)(2)(B) of such Code is amended by striking $4,500 and inserting the amount in effect under subsection (c)(2)(A)(ii)(II) .\n##### (c) Conforming amendments\nSection 223(g)(1) of such Code is amended\u2014\n**(1)**\nby striking subsections (b)(2) and both places it appears and inserting subsection , and\n**(2)**\nin subparagraph (B), by striking determined by and all that follows through calendar year 2003 . and inserting determined by substituting calendar year 2003 for calendar year 2016 in subparagraph (A)(ii) thereof. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.\n#### 10. Clarification of treatment of distributions from health savings account for long-term care services\n##### (a) In general\nSection 223(d)(2)(A) of the Internal Revenue Code of 1986 is amended by inserting before the last sentence the following: Such term includes amounts paid for qualified long-term care services (as defined in section 7702B(c)). .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid after the date of the enactment of this Act.\n##### (c) No inference\nNothing contained in this section or the amendment made thereby shall be construed to create any inference with respect to any amounts paid on or before such date.",
      "versionDate": "2025-01-16",
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
        "actionDate": "2025-01-15",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "444",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Native American Health Savings Improvement Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-04-08",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2745",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Catch Up Act",
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
        "name": "Taxation",
        "updateDate": "2025-02-15T13:18:53Z"
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
      "date": "2025-01-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr548ih.xml"
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
      "title": "HSA Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T11:08:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "HSA Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-14T11:08:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to modernize health savings accounts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-14T11:03:20Z"
    }
  ]
}
```
