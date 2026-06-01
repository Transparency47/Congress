# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3698?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3698
- Title: Mental Health and MAMA Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3698
- Origin chamber: Senate
- Introduced date: 2026-01-27
- Update date: 2026-02-20T13:44:57Z
- Update date including text: 2026-02-20T13:44:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-01-27: Introduced in Senate
- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-01-27: Introduced in Senate

## Actions

- 2026-01-27 - IntroReferral: Introduced in Senate
- 2026-01-27 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-27",
    "latestAction": {
      "actionDate": "2026-01-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3698",
    "number": "3698",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Mental Health and MAMA Act of 2026",
    "type": "S",
    "updateDate": "2026-02-20T13:44:57Z",
    "updateDateIncludingText": "2026-02-20T13:44:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-27",
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
      "actionDate": "2026-01-27",
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
          "date": "2026-01-27T22:06:35Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "WI"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
      "state": "IL"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2026-01-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3698is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3698\nIN THE SENATE OF THE UNITED STATES\nJanuary 27, 2026 Mrs. Shaheen (for herself, Ms. Baldwin , Ms. Duckworth , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo amend the Public Health Service Act, the Employee Retirement Income Security Act of 1974, and the Internal Revenue Code of 1986 to require that group health plans and health insurance issuers offering group or individual health insurance that provide coverage for mental health services and substance use disorder services provide such services without the imposition of cost-sharing from the diagnosis of pregnancy through the 1-year period following such pregnancy, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Mental Health and Making Access More Affordable Act of 2026 or the Mental Health and MAMA Act of 2026 .\n#### 2. Cost-sharing with respect to mental health services and substance use disorder services for pregnant and postpartum individuals\n##### (a) PHSA\n**(1) In general**\nPart D of title XXVII of the Public Health Service Act ( 42 U.S.C. 300gg\u2013111 et seq. ) is amended by adding at the end the following new section:\n2799A\u201311. Cost-sharing requirements with respect to mental health services and substance use disorder services for pregnant and postpartum individuals (a) In general In the case of a group health plan or a health insurance issuer offering group or individual health insurance coverage that provides a benefit for mental health services or substance use disorder services (including such services which are telehealth services and are provided under such plan or coverage) with respect to plan years beginning on or after the date that is 2 years after the date of enactment of this section, the plan or coverage shall not impose any cost-sharing requirement for such services that are furnished by an in-network provider to a participant, beneficiary, or enrollee under the plan or coverage from the diagnosis of pregnancy (as defined by the Secretary) through the 1-year period beginning on the day after the last day of such pregnancy of such participant, beneficiary, or enrollee (or, in the case of an individual enrolled in such plan or coverage for a portion of such period, during such portion). (b) Definitions In this section: (1) The terms mental health services and substance use disorder services have the meaning given such terms for purposes of section 2726. (2) The term telehealth service means a service that is furnished through telehealth technologies (as defined in section 330I(a)). .\n**(2) Continuity of care**\nSection 2799A\u20133 of the Public Health Service Act ( 42 U.S.C. 300gg\u2013113 ) is amended\u2014\n**(A)**\nin subsection (a)(2)(C), by inserting , in the case of a continuing care patient described in subsection (b)(1)(D)(ii), the date on which such individual is no longer such a continuing care patient with respect to such provider or facility, or in the case of a continuing care patient described in subsection (b)(1) other than in subparagraph (D)(ii) of such subsection, after is provided and ending on ; and\n**(B)**\nby amending subsection (b)(1)(D) to read as follows:\n(D) (i) is pregnant and undergoing a course of treatment for the pregnancy from the provider or facility; or (ii) (I) requires mental health services or substance use disorder services from a provider or facility following a pregnancy; (II) received a course of mental health or substance use disorder treatment from such provider or facility while pregnant; and (III) the last day of such pregnancy occurred during the previous 1-year period; or .\n##### (b) ERISA\n**(1) In general**\nSubpart B of part 7 of subtitle B of title I of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185 et seq. ) is amended by adding at the end the following new section:\n726. Cost-sharing requirements with respect to mental health services and substance use disorder services for pregnant and postpartum individuals (a) In general In the case of a group health plan or a health insurance issuer offering group health insurance coverage that provides a benefit for mental health services or substance use disorder services (including such services which are telehealth services and are provided under such plan or coverage) with respect to plan years beginning on or after the date that is 2 years after the date of enactment of this section, the plan or coverage shall not impose any cost-sharing requirement for such services that are furnished by an in-network provider to a participant or beneficiary under the plan or coverage from the diagnosis of pregnancy (as defined by the Secretary) through the 1-year period beginning on the day after the last day of such pregnancy of such participant or beneficiary (or, in the case of an individual enrolled in such plan or coverage for a portion of such period, during such portion). (b) Definitions In this section: (1) The terms mental health services and substance use disorder services have the meaning given such terms for purposes of section 712. (2) The term telehealth service means a service that is furnished through telehealth technologies (as defined in section 330I(a) of the Public Health Service Act). .\n**(2) Continuity of care**\nSection 718 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1185g ) is amended\u2014\n**(A)**\nin subsection (a)(2)(C), by inserting , in the case of a continuing care patient described in subsection (b)(1)(D)(ii), the date on which such individual is no longer such a continuing care patient with respect to such provider or facility, or in the case of a continuing care patient described in subsection (b)(1) other than in subparagraph (D)(ii) of such subsection, after is provided and ending on ; and\n**(B)**\nby amending subsection (b)(1)(D) to read as follows:\n(D) (i) is pregnant and undergoing a course of treatment for the pregnancy from the provider or facility; or (ii) (I) requires mental health services or substance use disorder services from a provider or facility following a pregnancy; (II) received a course of mental health or substance use disorder treatment from such provider or facility while pregnant; and (III) the last day of such pregnancy occurred during the previous 1-year period; or .\n**(3) Clerical amendment**\nThe table of contents in section 1 of the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ) is amended by inserting after the item relating to section 725 the following new item:\nSec. 726. Cost-sharing requirements with respect to mental health services and substance use disorder services for pregnant and postpartum individuals. .\n##### (c) IRC\n**(1) In general**\nSubchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n9826. Cost-sharing requirements with respect to mental health services and substance use disorder services for pregnant and postpartum individuals (a) In general In the case of a group health plan that provides a benefit for mental health services or substance use disorder services (including such services which are telehealth services and are provided under such plan) with respect to plan years beginning on or after the date that is 2 years after the date of enactment of this section, the plan shall not impose any cost-sharing requirement for such services that are furnished by an in-network provider to a participant or beneficiary under the plan from the diagnosis of pregnancy (as defined by the Secretary) through the 1-year period beginning on the day after the last day of such pregnancy of such participant or beneficiary (or, in the case of an individual enrolled in such plan for a portion of such period, during such portion). (b) Definitions In this section: (1) The terms mental health services and substance use disorder services have the meaning given such terms for purposes of section 9812. (2) The term telehealth service means a service that is furnished through telehealth technologies (as defined in section 330I(a) of the Public Health Service Act). .\n**(2) Continuity of care**\nSection 9818 of the Internal Revenue Code of 1986 is amended\u2014\n**(A)**\nin subsection (a)(2)(C), by inserting , in the case of a continuing care patient described in subsection (b)(1)(D)(ii), the date on which such individual is no longer such a continuing care patient with respect to such provider or facility, or in the case of a continuing care patient described in subsection (b)(1) other than in subparagraph (D)(ii) of such subsection, after is provided and ending on ; and\n**(B)**\nby amending subsection (b)(1)(D) to read as follows:\n(D) (i) is pregnant and undergoing a course of treatment for the pregnancy from the provider or facility; or (ii) (I) requires mental health services or substance use disorder services from a provider or facility following a pregnancy; (II) received a course of mental health or substance use disorder treatment from such provider or facility while pregnant; and (III) the last day of such pregnancy occurred during the previous 1-year period; or .\n**(3) Clerical amendment**\nThe table of sections for subchapter B of chapter 100 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 9826. Cost-sharing requirements with respect to mental health services and substance use disorder services for pregnant and postpartum individuals. .\n##### (d) Effective date\nThe amendments made by subsections (a), (b), and (c) shall apply with respect to plan years beginning on or after the date that is 2 years after the date of enactment of this Act.\n##### (e) FEHBP\n**(1) In general**\nSection 8902(p) of title 5, United States Code, is amended\u2014\n**(A)**\nby striking and 2799A\u20137 and inserting 2799A\u20137, and 2799A\u201311 ;\n**(B)**\nby striking and 722 and inserting 722, and 726 ; and\n**(C)**\nby striking and 9822 and inserting 9822, and 9826 .\n**(2) Effective date**\nThe amendments made by paragraph (1) shall apply with respect to contracts entered into or renewed for contract years beginning on or after the date that is 2 years after the date of enactment of this Act.",
      "versionDate": "2026-01-27",
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
        "actionDate": "2026-01-22",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Education and Workforce, Ways and Means, and Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7227",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Mental Health and MAMA Act of 2026",
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
        "updateDate": "2026-02-20T13:44:57Z"
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
      "date": "2026-01-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3698is.xml"
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
      "title": "Mental Health and MAMA Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mental Health and MAMA Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mental Health and Making Access More Affordable Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Public Health Service Act, the Employee Retirement Income Security Act of 1974, and the Internal Revenue Code of 1986 to require that group health plans and health insurance issuers offering group or individual health insurance that provide coverage for mental health services and substance use disorder services provide such services without the imposition of cost-sharing from the diagnosis of pregnancy through the 1-year period following such pregnancy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T03:48:23Z"
    }
  ]
}
```
