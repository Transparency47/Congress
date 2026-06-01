# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1878?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1878
- Title: IVF Access and Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 1878
- Origin chamber: House
- Introduced date: 2025-03-05
- Update date: 2025-11-18T09:05:26Z
- Update date including text: 2025-11-18T09:05:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-03-05: Introduced in House

## Actions

- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Introduced in House
- 2025-03-05 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1878",
    "number": "1878",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000599",
        "district": "17",
        "firstName": "Michael",
        "fullName": "Rep. Lawler, Michael [R-NY-17]",
        "lastName": "Lawler",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "IVF Access and Affordability Act",
    "type": "HR",
    "updateDate": "2025-11-18T09:05:26Z",
    "updateDateIncludingText": "2025-11-18T09:05:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-05",
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
          "date": "2025-03-05T15:03:40Z",
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
      "bioguideId": "W000804",
      "district": "1",
      "firstName": "Robert",
      "fullName": "Rep. Wittman, Robert J. [R-VA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Wittman",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "L000596",
      "district": "13",
      "firstName": "Anna Paulina",
      "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Luna",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "FL"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1878ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1878\nIN THE HOUSE OF REPRESENTATIVES\nMarch 5, 2025 Mr. Lawler (for himself, Mr. Wittman , and Mrs. Luna ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an income tax credit for fertility treatments.\n#### 1. Short title\nThis Act may be cited as the IVF Access and Affordability Act .\n#### 2. Credit for fertility treatments\n##### (a) In general\nSubpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting before section 24 the following new section:\n23A. Credit for fertility treatments (a) Allowance of credit In the case of an eligible individual, there shall be allowed as a credit against the tax imposed by this chapter for the taxable year an amount equal to the assisted reproductive technology expenses paid or incurred during the taxable year. (b) Limitations (1) Dollar limitation (A) In general The amount of the credit under subsection (a) for any taxable year shall not exceed $20,000. (B) Special rule In the case of two individuals filing a joint return or an individual filing as a surviving spouse (as defined in section 2(a)) with respect to a taxable year in which both individuals, or the individual and the spouse of such individual, incur assisted reproductive technology expenses, subparagraph (A) shall be applied by substituting $40,000 for $20,000 . (2) Income limitation (A) In general The amount otherwise allowable as a credit under subsection (a) for any taxable year shall be reduced (but not below zero) by an amount which bears the same ratio to the amount so allowable as\u2014 (i) the amount (if any) by which the taxpayer\u2019s adjusted gross income exceeds $200,000, bears to (ii) $100,000. (B) Special rule In the case of a joint return or a surviving spouse (as defined in section 2(a)), subparagraph (A) shall be applied by substituting $400,000 for $200,000 and $200,000 for $100,000 . (C) Determination of adjusted gross income For purposes of subparagraph (A), adjusted gross income shall be determined without regard to sections 911, 931, and 933. (3) Denial of double benefit (A) In general Any assisted reproductive technology expense taken into account for purposes of any deduction (or any credit other than the credit allowed under this section) shall be reduced by the amount of the credit allowed under subsection (a) with respect to such expense. (B) Reimbursement No credit shall be allowed under subsection (a) for any expense to the extent that payment for such expense is made, or reimbursement for such expense is received, under any insurance policy or otherwise. (c) Carryforwards of unused credit (1) In general If the credit allowable under subsection (a) exceeds the limitation imposed by section 26(a) for such taxable year reduced by the sum of the credits allowable under this subpart (other than this section and section 25D), such excess shall be carried to the succeeding taxable year and added to the credit allowable under subsection (a) for such succeeding taxable year. (2) Limitation No credit may be carried forward under this subsection to any taxable year after the 5th taxable year after the taxable year in which the credit arose. For purposes of the preceding sentence, credits shall be treated as used on a first-in, first-out basis. (d) Assisted reproductive technology For purposes of this section, the term assisted reproductive technology has the meaning given such term in section 8 of the Fertility Clinic Success Rate and Certification Act of 1992 ( 42 U.S.C. 263a\u20137 ). (e) Eligible individual For purposes of this section, the term eligible individual means the taxpayer, the spouse of the taxpayer, or a dependent of the taxpayer. (f) Special rules (1) Married couples must file joint returns Rules similar to the rules of paragraphs (2), (3), and (4) of section 21(e) shall apply for purposes of this section. (2) Denial of double benefit for dependents No credit shall be allowed under this section to a taxpayer who is a dependent (as defined in section 152(a)) for assisted reproductive technology expenses for which a credit has been claimed by another taxpayer under this section. .\n##### (b) Conforming amendments\n**(1)**\nThe table of sections for subpart A of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by inserting after the item relating to section 23 the following new item:\nSec. 23A. Credit for fertility treatments. .\n**(2)**\nSection 23(c)(1) of such Code is amended by striking section 25D and inserting sections 23A and 25D .\n**(3)**\nSection 25(e)(1)(C) of such Code is amended by inserting , 23A, after 23 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-03-05",
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
        "updateDate": "2025-05-08T14:06:37Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1878ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to provide an income tax credit for fertility treatments.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:33:20Z"
    },
    {
      "title": "IVF Access and Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "IVF Access and Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    }
  ]
}
```
