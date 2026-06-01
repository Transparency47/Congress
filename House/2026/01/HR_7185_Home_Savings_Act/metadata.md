# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7185?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7185
- Title: Home Savings Act
- Congress: 119
- Bill type: HR
- Bill number: 7185
- Origin chamber: House
- Introduced date: 2026-01-21
- Update date: 2026-04-10T08:05:51Z
- Update date including text: 2026-04-10T08:05:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-21: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2026-01-21: Introduced in House

## Actions

- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Introduced in House
- 2026-01-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-21",
    "latestAction": {
      "actionDate": "2026-01-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7185",
    "number": "7185",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001239",
        "district": "5",
        "firstName": "John",
        "fullName": "Rep. McGuire, John J. [R-VA-5]",
        "lastName": "McGuire",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "Home Savings Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:51Z",
    "updateDateIncludingText": "2026-04-10T08:05:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-21",
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
      "actionDate": "2026-01-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-21",
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
          "date": "2026-01-21T15:02:05Z",
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
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-01-30",
      "state": "TX"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "GA"
    },
    {
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "NC"
    },
    {
      "bioguideId": "C001137",
      "district": "5",
      "firstName": "Jeff",
      "fullName": "Rep. Crank, Jeff [R-CO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Crank",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "CO"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2026-04-09",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7185ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7185\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 21, 2026 Mr. McGuire introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude from gross income certain retirement plan distributions used for a down payment or closing costs for a principal residence, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Home Savings Act .\n#### 2. Exclusion from gross income of retirement plan distributions used for a down payment or closing costs for a principal residence\n##### (a) In general\n**(1) Defined contribution plans**\nSection 402 of the Internal Revenue Code of 1986 is amended by adding at the end the following new subsection:\n(m) Distributions for a down payment or closing costs for a principal residence (1) In general The gross income of an employee for any taxable year shall not include any distribution from a defined contribution plan of such employee to the extent that such distribution is used for a down payment or closing costs associated with acquiring a principal residence of\u2014 (A) the employee, or (B) an eligible relative of the employee. (2) Definitions For purposes of this subsection\u2014 (A) Eligible relative The term eligible relative means, with respect to any employee\u2014 (i) the spouse of the employee, or (ii) any child, grandchild, or ancestor of\u2014 (I) the employee, or (II) the spouse of the employee. (B) Defined contribution plan The term defined contribution plan has the meaning given the term in section 414(i). (C) Principal residence The term principal residence has the same meaning as when used in section 121. (3) Application of section 72 Rules similar to the rules of section 408(d)(10)(C) shall apply for purposes of this subsection, by taking into account all amounts in the defined contribution plan to which the employee has nonforfeitable right in lieu of all amounts in all individual retirement plans of the individual. (4) Gift tax treatment So much of any transfer of a distribution described in paragraph (1) by the employee to an eligible relative as is used by such eligible relative for a down payment or closing costs associated with acquiring a principal residence of such eligible relative shall not be treated as a gift for purposes of section 2503(a). (5) Termination date Paragraph (1) shall not apply to distributions made in taxable years beginning after December 31, 2030. .\n**(2) Certain annuity plans**\nSection 403 of such Code is amended by adding at the end the following new subsection:\n(d) Distributions for a down payment or closing costs for a principal residence (1) In general The rules of section 402(m) shall apply to distributions under an annuity plan described in subsection (a) or an annuity contract described in subsection (b). (2) Termination date Paragraph (1) shall not apply to distributions made in taxable years beginning after December 31, 2030. .\n**(3) Individual retirement plans**\nSection 408(d) of such Code is amended by adding at the end the following new paragraph:\n(10) Distributions for a down payment or closing costs for a principal residence (A) In general The gross income of an individual for any taxable year shall not include any distribution from an individual retirement plan of such individual to the extent that such distribution is used for a down payment or closing costs associated with acquiring a principal residence of\u2014 (i) the individual, or (ii) an eligible relative of the individual. (B) Definitions For purposes of this paragraph\u2014 (i) Eligible relative The term eligible relative means, with respect to any individual\u2014 (I) the spouse of the individual, or (II) any child, grandchild, or ancestor of\u2014 (aa) the individual, or (bb) the spouse of the individual. (ii) Individual retirement plan The term individual retirement plan has the meaning given the term in section 7701. (iii) Principal residence The term principal residence has the same meaning as when used in section 121. (C) Application of section 72 Notwithstanding section 72, in determining the extent to which a distribution is used for a down payment or closing costs pursuant to subparagraph (A), the entire amount of the distribution shall be treated as includible in gross income without regard to such subparagraph to the extent that such amount does not exceed the aggregate amount which would have been so includible if all amounts in all individual retirement plans of the individual were distributed during such taxable year and all such plans were treated as 1 contract for purposes of determining under section 72 the aggregate amount which would have been so includible. Proper adjustments shall be made in applying section 72 to other distributions in such taxable year and subsequent taxable years. (D) Gift tax treatment So much of any transfer of a distribution described in subparagraph (A) by the individual to an eligible relative as is used by such eligible relative for a down payment or closing costs associated with acquiring a principal residence of such eligible relative shall not be treated as a gift for purposes of section 2503(a). (E) Termination date Subparagraph (A) shall not apply to distributions made in taxable years beginning after December 31, 2030. .\n**(4) 457 (b) plans**\nSection 457(e) of such Code is amended by adding at the end the following new paragraph:\n(19) Distributions for a down payment or closing costs for a principal residence (A) In general The rules of section 402(m) shall apply to distributions under an eligible deferred compensation plan established and maintained by an employer described in paragraph (1)(A). (B) Termination date Subparagraph (A) shall not apply to distributions made in taxable years beginning after December 31, 2030. .\n##### (b) Effective date\nThe amendments made by this section shall apply to distributions made in taxable years beginning after December 31, 2025.",
      "versionDate": "2026-01-21",
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
        "updateDate": "2026-02-13T18:12:03Z"
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
      "date": "2026-01-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7185ih.xml"
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
      "title": "Home Savings Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Home Savings Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-11T06:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to exclude from gross income certain retirement plan distributions used for a down payment or closing costs for a principal residence, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-11T06:18:17Z"
    }
  ]
}
```
