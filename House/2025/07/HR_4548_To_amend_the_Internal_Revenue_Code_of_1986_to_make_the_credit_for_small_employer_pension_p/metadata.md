# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4548?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4548
- Title: Small Nonprofit Retirement Security Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4548
- Origin chamber: House
- Introduced date: 2025-07-21
- Update date: 2026-05-22T08:07:57Z
- Update date including text: 2026-05-22T08:07:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-07-21: Introduced in House

## Actions

- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Introduced in House
- 2025-07-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4548",
    "number": "4548",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "B001260",
        "district": "16",
        "firstName": "Vern",
        "fullName": "Rep. Buchanan, Vern [R-FL-16]",
        "lastName": "Buchanan",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Small Nonprofit Retirement Security Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:57Z",
    "updateDateIncludingText": "2026-05-22T08:07:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-21",
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
      "actionDate": "2025-07-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T16:00:25Z",
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
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "UT"
    },
    {
      "bioguideId": "S001190",
      "district": "10",
      "firstName": "Bradley",
      "fullName": "Rep. Schneider, Bradley Scott [D-IL-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Schneider",
      "middleName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "IL"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle S. [D-OR-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-08-15",
      "state": "OR"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-09-23",
      "state": "DE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-12-09",
      "state": "VA"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-12-19",
      "state": "OH"
    },
    {
      "bioguideId": "U000040",
      "district": "14",
      "firstName": "Lauren",
      "fullName": "Rep. Underwood, Lauren [D-IL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Underwood",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4548ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4548\nIN THE HOUSE OF REPRESENTATIVES\nJuly 21, 2025 Mr. Buchanan (for himself, Mr. Panetta , Mr. Moore of Utah , and Mr. Schneider ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to make the credit for small employer pension plan startup costs and the retirement auto-enrollment credit available to tax-exempt eligible small employers.\n#### 1. Short title\nThis Act may be cited as the Small Nonprofit Retirement Security Act of 2025 .\n#### 2. Retirement credits made available to tax-exempt small employers\n##### (a) Credit for small employer pension plan startup costs\nSection 45E of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(g) Credit made available to tax-Exempt eligible employers (1) In general In the case of a tax-exempt eligible employer, there shall be treated as a credit allowed under section 3111(g), and not as a credit determined under subsection (a), an amount equal to the lesser of\u2014 (A) the amount of the credit determined under this section (without regard to this subsection) with respect to such employer, or (B) the amount of payroll tax paid by the employer during the calendar year in which the taxable year begins. (2) Definitions For purposes of this subsection\u2014 (A) Tax-exempt eligible employer The term tax-exempt eligible employer means an eligible employer which is described in section 501(c) and exempt from taxation under section 501(a). (B) Payroll tax (i) In general The term payroll tax means the tax imposed by section 3111(a). (ii) Special rule A rule similar to the rule of section 24(d)(2)(C) shall apply for purposes of determining the payroll tax paid by an employer. .\n##### (b) Retirement auto-Enrollment credit\nSection 45T of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(d) Credit made available to tax-Exempt eligible employers (1) In general In the case of a tax-exempt eligible employer, there shall be treated as a credit allowed under section 3111(g), and not as a credit determined under subsection (a), an amount equal to the lesser of\u2014 (A) the amount of the credit determined under this section (without regard to this subsection) with respect to such employer, or (B) the amount of payroll tax paid by the employer during the calendar year in which the taxable year begins. (2) Definitions For purposes of this subsection\u2014 (A) Tax-exempt eligible employer The term tax-exempt eligible employer means an eligible employer which is described in section 501(c) and exempt from taxation under section 501(a). (B) Payroll tax (i) In general The term payroll tax means the tax imposed by section 3111(a). (ii) Special rule A rule similar to the rule of section 24(d)(2)(C) shall apply for purposes of determining the payroll tax paid by an employer. .\n##### (c) Payroll credit\nSection 3111 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(g) Credit for certain plans of tax-Exempt employers (1) In general In the case of a tax-exempt eligible employer to which section 45E(g) or section 45T(d) applies, there shall be allowed as a credit against the tax imposed by subsection (a) for calendar quarters in an applicable year an amount equal to the amount determined under section 45E(g)(1) or section 45T(d)(1), whichever is applicable. (2) Limitation The aggregate amount allowed as a credit under this subsection for the calendar quarters in any year shall not exceed the amount of the tax imposed by subsection (a) on wages paid with respect to the employment of all employees of the employer during such year, determined by applying a rule similar to the rule of section 24(d)(2)(C). (3) Definitions For purposes of this subsection\u2014 (A) Tax-exempt eligible employer The term tax-exempt eligible employer means an eligible employer which is described in section 501(c) and exempt from taxation under section 501(a). (B) Applicable year The term applicable year means the calendar year referred to in section 45E(g)(1)(B) or section 45T(d)(1)(B), whichever is applicable. .\n##### (d) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2024.\n##### (e) Transfers of Funds to Old-Age, Survivors, and Disability Trust Fund\nThere are hereby appropriated to the Federal Old-Age and Survivors Trust Fund and the Federal Disability Insurance Trust Fund established under section 201 of the Social Security Act ( 42 U.S.C. 401 ) amounts equal to the reduction in revenues to the Treasury by reason of the amendments made by subsections (a), (b), and (c). Amounts appropriated by the preceding sentence shall be transferred from the general fund at such times and in such manner as to replicate to the extent possible the transfers which would have occurred to such Trust Fund had such amendments not been enacted.",
      "versionDate": "2025-07-21",
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
        "actionDate": "2025-07-21",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "2365",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Small Nonprofit Retirement Security Act of 2025",
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
        "name": "Taxation",
        "updateDate": "2025-08-01T16:57:51Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4548ih.xml"
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
      "title": "Small Nonprofit Retirement Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-31T04:43:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Small Nonprofit Retirement Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-31T04:43:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to make the credit for small employer pension plan startup costs and the retirement auto-enrollment credit available to tax-exempt eligible small employers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-31T04:33:37Z"
    }
  ]
}
```
