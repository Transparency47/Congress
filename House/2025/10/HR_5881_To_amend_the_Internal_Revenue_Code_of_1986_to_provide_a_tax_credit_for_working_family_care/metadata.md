# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5881?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5881
- Title: Double Dependents Relief Act
- Congress: 119
- Bill type: HR
- Bill number: 5881
- Origin chamber: House
- Introduced date: 2025-10-31
- Update date: 2026-02-06T18:54:58Z
- Update date including text: 2026-02-06T18:54:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-31: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-10-31: Introduced in House

## Actions

- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Introduced in House
- 2025-10-31 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-31",
    "latestAction": {
      "actionDate": "2025-10-31",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5881",
    "number": "5881",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001090",
        "district": "9",
        "firstName": "Josh",
        "fullName": "Rep. Harder, Josh [D-CA-9]",
        "lastName": "Harder",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Double Dependents Relief Act",
    "type": "HR",
    "updateDate": "2026-02-06T18:54:58Z",
    "updateDateIncludingText": "2026-02-06T18:54:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-31",
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
      "actionDate": "2025-10-31",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-31",
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
          "date": "2025-10-31T17:04:35Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5881ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5881\nIN THE HOUSE OF REPRESENTATIVES\nOctober 31, 2025 Mr. Harder of California introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide a tax credit for working family caregivers.\n#### 1. Short title\nThis Act may be cited as the Double Dependents Relief Act .\n#### 2. Credit for working family caregivers\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 25F the following new section:\n25G. Working family caregivers (a) Allowance of credit In the case of an eligible caregiver, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to 30 percent of the qualified expenses paid by the taxpayer during the taxable year which exceed $2,000. (b) Limitation (1) In general The amount allowed as a credit under subsection (a) for the taxable year shall not exceed $10,000. (2) Adjustment for inflation In the case of any taxable year beginning after 2026, the dollar amount contained in paragraph (1) shall be increased by an amount equal to the product of\u2014 (A) such dollar amount, and (B) the medical care cost adjustment determined under section 213(d)(10)(B)(ii) for the calendar year in which the taxable year begins, determined by substituting 2025 for 1996 in subclause (II) thereof. If any increase determined under the preceding sentence is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. (c) Eligible caregiver For purposes of this section, the term eligible caregiver means an individual\u2014 (1) with a dependent who is a qualifying child (as defined in section 152(c)), (2) who during the taxable year pays or incurs qualified expenses in connection with providing care for a qualified care recipient, and (3) who has earned income (as defined in section 32(c)(2)) for the taxable year in excess of $7,500. (d) Qualified care recipient For purposes of this section\u2014 (1) In general The term qualified care recipient means, with respect to any taxable year, any individual who\u2014 (A) is the spouse of the eligible caregiver, or any other person who bears a relationship to the eligible caregiver described in any of subparagraphs (A) through (H) of section 152(d)(2), and (B) has been certified, before the due date for filing the return of tax for the taxable year, by a licensed health care practitioner (as defined in section 7702B(c)(4)) as being an individual with long-term care needs described in paragraph (3) for a period\u2014 (i) which is at least 180 consecutive days, and (ii) a portion of which occurs within the taxable year. (2) Period for making certification Notwithstanding paragraph (1)(B), a certification shall not be treated as valid unless it is made within the 39 1/2 -month period ending on such due date (or such other period as the Secretary prescribes). (3) Individuals with long-term care needs An individual is described in this paragraph if the individual meets any of the following requirements: (A) The individual is at least 6 years of age and\u2014 (i) is unable to perform (without substantial assistance from another individual) at least 2 activities of daily living (as defined in section 7702B(c)(2)(B)) due to a loss of functional capacity, or (ii) requires substantial supervision to protect such individual from threats to health and safety due to severe cognitive impairment and is unable to perform, without reminding or cuing assistance, at least 1 activity of daily living (as so defined) or to the extent provided in regulations prescribed by the Secretary (in consultation with the Secretary of Health and Human Services), is unable to engage in age-appropriate activities. (B) The individual is at least 2 but not 6 years of age and is unable due to a loss of functional capacity to perform (without substantial assistance from another individual) at least 2 of the following activities: eating, transferring, or mobility. (C) The individual is under 2 years of age and requires specific durable medical equipment by reason of a severe health condition or requires a skilled practitioner trained to address the individual\u2019s condition to be available if the individual\u2019s parents or guardians are absent. (e) Qualified expenses For purposes of this section\u2014 (1) In general Subject to paragraph (4), the term qualified expenses means expenditures for goods, services, and supports that\u2014 (A) assist a qualified care recipient with accomplishing activities of daily living (as defined in section 7702B(c)(2)(B)) and instrumental activities of daily living (as defined in section 1915(k)(6)(F) of the Social Security Act ( 42 U.S.C. 1396n(k)(6)(F) )), and (B) are provided solely for use by such qualified care recipient. (2) Adjustment for other tax benefits The amount of qualified expenses otherwise taken into account under paragraph (1) with respect to an individual shall be reduced by the sum of any amounts paid for the benefit of such individual for the taxable year which are\u2014 (A) taken into account under section 21 or 213, or (B) excluded from gross income under section 129, 223(f), or 529A(c)(1)(B). (3) Goods, services, and supports For purposes of paragraph (1), goods, services, and supports (as defined by the Secretary) shall include\u2014 (A) human assistance, supervision, cuing and standby assistance, (B) assistive technologies and devices (including remote health monitoring), (C) environmental modifications (including home modifications), (D) health maintenance tasks (such as medication management), (E) information, (F) transportation of the qualified care recipient, (G) non-health items (such as incontinence supplies), and (H) coordination of and services for people who live in their own home, a residential setting, or a nursing facility, as well as the cost of care in these or other locations. (4) Qualified expenses for eligible caregivers For purposes of paragraph (1), the following shall be treated as qualified expenses if paid or incurred by an eligible caregiver: (A) Expenditures for respite care for a qualified care recipient. (B) Expenditures for counseling, support groups, or training relating to caring for a qualified care recipient. (C) Lost wages for unpaid time off due to caring for a qualified care recipient as verified by an employer. (D) Travel costs of the eligible caregiver related to caring for a qualified care recipient. (E) Expenditures for technologies, as determined by the Secretary, that assist an eligible caregiver in providing care for a qualified care recipient. (5) Human assistance The term human assistance includes the costs of a direct care worker. (6) Documentation An expense shall not be taken into account under this section unless the eligible caregiver substantiates such expense under such regulations or guidance as the Secretary shall provide. (7) Mileage rate For purposes of this section, the mileage rate for the use of a passenger automobile shall be the standard mileage rate used to calculate the deductible costs of operating an automobile for medical purposes. Such rate may be used in lieu of actual automobile-related travel expenses. (8) Coordination with ABLE Accounts Qualified expenses for a taxable year shall not include contributions to an ABLE account (as defined in section 529A). (f) Phase Out Based on Adjusted Gross Income For purposes of this section\u2014 (1) In general The amount of the credit allowable under subsection (a) shall be reduced (but not below zero) by $100 for each $1,000 (or fraction thereof) by which the taxpayer\u2019s modified adjusted gross income exceeds the threshold amount. (2) Modified adjusted gross income The term modified adjusted gross income means adjusted gross income increased by any amount excluded from gross income under section 911, 931, or 933. (3) Threshold amount The term threshold amount means\u2014 (A) $150,000 in the case of a joint return, and (B) $75,000 in any other case. (4) Indexing In the case of any taxable year beginning in a calendar year after 2025, each dollar amount contained in paragraph (3) shall be increased by an amount equal to the product of\u2014 (A) such dollar amount, and (B) the cost-of-living adjustment determined under section 1(f)(3) for the calendar year in which the taxable year begins, determined by substituting calendar year 2024 for calendar year 2016 in subparagraph (A)(ii) thereof. (5) Rounding rule If any increase determined under paragraph (4) is not a multiple of $50, such increase shall be rounded to the next lowest multiple of $50. (g) Identification requirements No credit shall be allowed under this section to a taxpayer with respect to any qualified care recipient unless the taxpayer includes the name and taxpayer identification number of such individual, and the identification number of the licensed health care practitioner certifying such individual, on the return of tax for the taxable year. .\n##### (b) Clerical amendment\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 25F the following new item:\nSec. 25G. Working family caregivers. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-10-31",
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
        "actionDate": "2025-12-18",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Education and Workforce, and Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6900",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Affordability Act of 2025",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "925",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Credit for Caring Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "2036",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Credit for Caring Act of 2025",
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
        "updateDate": "2025-11-20T17:56:30Z"
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
      "date": "2025-10-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5881ih.xml"
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
      "title": "Double Dependents Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-05T10:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Double Dependents Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-05T10:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide a tax credit for working family caregivers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-05T10:48:15Z"
    }
  ]
}
```
