# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6758?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6758
- Title: UPLIFT Act
- Congress: 119
- Bill type: HR
- Bill number: 6758
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-04-10T08:06:12Z
- Update date including text: 2026-04-10T08:06:12Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6758",
    "number": "6758",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "UPLIFT Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:06:12Z",
    "updateDateIncludingText": "2026-04-10T08:06:12Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
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
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:01:30Z",
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
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "DC"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "MI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "CO"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "PA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NY"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NJ"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "IN"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-01-07",
      "state": "CA"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "NJ"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "CT"
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
      "sponsorshipDate": "2026-02-09",
      "state": "VA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6758ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6758\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mrs. McIver (for herself, Ms. Norton , Ms. Tlaib , Ms. Pettersen , Ms. Lee of Pennsylvania , Mr. Goldman of New York , Mrs. Watson Coleman , and Mr. Carson ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to establish a refundable tax credit for residential energy expenditures.\n#### 1. Short title\nThis Act may be cited as the Utility Price Lift In Flux and Transition Act or the UPLIFT Act .\n#### 2. Residential energy expenditures credit\n##### (a) In general\nSubpart C of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after section 36 the following new section:\n36A. Residential energy expenditures credit (a) Allowance of credit In the case of an individual, there shall be allowed as a credit against the tax imposed by this subtitle for an applicable taxable year an amount equal to the residential energy expenditures of the taxpayer for such taxable year. (b) Limitation The credit allowed under this section with respect to any taxpayer for any taxable year shall not exceed $1,200 ($2,400 in the case of a joint return or a head of household (as defined in section 2(b))). (c) Applicable taxable year For purposes of this section\u2014 (1) In general The term applicable taxable year means any taxable year if\u2014 (A) the average of the PCE for the 12-month period ending on December 31 of such taxable year, exceeds (B) 102 percent of the average of the PCE for the 12-month period immediately preceding the period described in subparagraph (A). (2) PCE The term PCE means the implicit price deflator for personal consumption expenditures (as published by the Bureau of Economic Analysis of the Department of Commerce). (d) Residential energy expenditures The term residential energy expenditures means expenditures\u2014 (1) made by the taxpayer for electricity, natural gas, or propane, and (2) used on, or in connection with, a dwelling unit\u2014 (A) located in the United States, (B) owned or rented by the taxpayer, and (C) used by the taxpayer as the taxpayer\u2019s principal residence (within the meaning of section 121). (e) Phaseout based on modified adjusted gross income (1) In general The amount of the credit otherwise allowed under this section shall be reduced by the amount which bears the same ratio to such amount (determined without regard to this subsection) as\u2014 (A) the excess (if any) of\u2014 (i) the taxpayer\u2019s modified adjusted gross income, over (ii) $75,000 ($150,000 in the case of a joint return or a head of household (as defined in section 2(b))), bears to (B) $25,000 ($50,000 in the case of a joint return or a head of household (as defined in section 2(b))). (2) Modified adjusted gross income For purposes of paragraph (1), the term modified adjusted gross income means the adjusted gross income of the taxpayer for the taxable year increased by any amount excluded from gross income under section 911, 931, or 933. (f) Coordination of credit with certain programs (1) Energy assistance programs An amount shall not fail to be treated as a residential energy expenditure of the taxpayer merely because such expenditure is reimbursed to, or paid on behalf of, such taxpayer under any Federal, State, local, or Tribal energy assistance program. (2) Means-tested programs For purposes of any Federal means-tested program, any refund made to an individual (or the spouse of an individual) by reason of this section shall not be treated as income (and shall not be taken into account in determining resources for the month of its receipt and the following month). (g) Regulations The Secretary, in coordination with the Commissioner of the Bureau of Labor Statistics, shall prescribe such regulations or other guidance as may be necessary or appropriate to carry out the purposes of this section. .\n##### (b) Clerical amendments\n**(1)**\nSection 6211(b)(4)(A) of such Code is amended by inserting 36A, after 36, .\n**(2)**\nThe table of sections for subpart C of part IV of subchapter A of chapter 1 of such Code is amended by inserting after the item relating to section 36 the following new item:\nSec. 36A. Residential energy expenditures credit. .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-12-16",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-01-09T16:08:02Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6758ih.xml"
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
      "title": "UPLIFT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "UPLIFT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Utility Price Lift In Flux and Transition Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to establish a refundable tax credit for residential energy expenditures.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:26Z"
    }
  ]
}
```
