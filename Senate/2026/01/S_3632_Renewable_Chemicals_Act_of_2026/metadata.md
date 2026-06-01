# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3632?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3632
- Title: Renewable Chemicals Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3632
- Origin chamber: Senate
- Introduced date: 2026-01-14
- Update date: 2026-02-10T00:31:06Z
- Update date including text: 2026-02-10T00:31:06Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-14: Introduced in Senate
- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-14: Introduced in Senate

## Actions

- 2026-01-14 - IntroReferral: Introduced in Senate
- 2026-01-14 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-14",
    "latestAction": {
      "actionDate": "2026-01-14",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3632",
    "number": "3632",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Renewable Chemicals Act of 2026",
    "type": "S",
    "updateDate": "2026-02-10T00:31:06Z",
    "updateDateIncludingText": "2026-02-10T00:31:06Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-14",
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
      "actionDate": "2026-01-14",
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
          "date": "2026-01-14T17:27:34Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-01-14",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3632is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3632\nIN THE SENATE OF THE UNITED STATES\nJanuary 14, 2026 Mr. Ricketts (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide credits for the production of renewable chemicals and investments in renewable chemical production facilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Renewable Chemicals Act of 2026 .\n#### 2. Credits for production of renewable chemicals and investments in renewable chemical production facilities\n##### (a) Production of renewable chemicals\n**(1) In general**\nSubpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new section:\n45BB. Credit for production of renewable chemicals (a) In general For purposes of section 38, the production credit for renewable chemicals for any taxable year is an amount (determined separately for each renewable chemical) equal to\u2014 (1) 15 percent of the sales price of each pound of a renewable chemical\u2014 (A) produced\u2014 (i) by the taxpayer, or (ii) for the taxpayer by a contract manufacturer under a binding written agreement, and (B) sold for its fair market value at retail by the taxpayer during the taxable year, reduced by (2) a percentage equal to so much of the percentage of the renewable chemical as is not biobased content. (b) Limitation The amount of the credit determined under subsection (a) with respect to a renewable chemical sold during any taxable year shall not exceed the credit amount allocated for purposes of this section by the Secretary to the taxpayer with respect to such chemical for such taxable year under section 48F. (c) Definitions For purposes of this section\u2014 (1) Renewable chemical The term renewable chemical means any chemical which\u2014 (A) is produced in the United States (or in a territory or possession of the United States) from renewable biomass which is produced in the United States (or in a territory or possession of the United States), (B) is not less than 95 percent biobased content, (C) is not sold or used for the production of any food, feed, fuel, or pharmaceuticals, (D) is approved to use the USDA Certified Biobased Product label under section 9002(b) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8102(b) ), and (E) is a chemical intermediate (as such term is defined in section 3201.109 of title 7, Code of Federal Regulations (or successor regulations)). (2) Biobased content The term biobased content means, with respect to any renewable chemical, the biobased content of the total mass of organic carbon in such chemical (expressed as a percentage), determined by testing representative samples using the American Society for Testing and Materials (ASTM) D6866. (3) Renewable biomass The term renewable biomass has the meaning given such term in section 9001(13) of the Farm Security and Rural Investment Act of 2002 ( 7 U.S.C. 8101(13) ). (d) National limitation on credits for renewable chemicals See section 48F(e) for rules relating to national limitation on credits under this section. (e) Coordination with investment credit for renewable chemical production facilities See section 48F(f) for rules coordinating section 48F with this section. (f) Termination Notwithstanding any other provision of this section or section 48F, the Secretary may not allocate any credit amount under this section to any taxable year which begins more than 5 years after the date of the enactment of this section. .\n**(2) Credit to be part of general business credit**\nSubsection (b) of section 38 of such Code is amended by striking plus at the end of paragraph (40), by striking the period at the end of paragraph (41) and inserting , plus , and by adding at the end the following new paragraph:\n(42) the renewable chemicals production credit determined under section 45BB(a). .\n##### (b) Investment credit in lieu of production credit\n**(1) In general**\nSection 46 of the Internal Revenue Code of 1986 is amended by striking and at the end of paragraph (6), by striking the period at the end of paragraph (7) and inserting , and , and by adding at the end the following new paragraph:\n(8) the renewable chemical production facilities credit. .\n**(2) Renewable chemical production facilities credit**\nSubpart E of part IV of subchapter A of chapter 1 of such Code is amended by inserting after section 48E the following:\n48F. Investment credit for renewable chemical production facilities (a) In general For purposes of section 46, the renewable chemical production facilities credit for any taxable year is an amount equal to 30 percent of the basis of any eligible property which is a part of a renewable chemical production facility placed in service by the taxpayer during such taxable year. (b) Limitation The amount of the credit determined under subsection (a) with respect to a renewable chemical production facility of the taxpayer during any taxable year shall not exceed the credit amount allocated for purposes of this section by the Secretary to the taxpayer for such taxable year under subsection (e). (c) Renewable Chemical Production Facility For purposes of this section\u2014 (1) In general The term renewable chemical production facility means a facility\u2014 (A) which is owned by the taxpayer, (B) which is originally placed in service after the date of the enactment of this section and before the first day of the taxable year which begins 6 years after the date of the enactment of this section, (C) with respect to which\u2014 (i) no credit has been allowed under section 45BB for chemicals produced at such facility in any previous taxable year, and (ii) the taxpayer makes an irrevocable election to have this section apply, and (D) which is primarily used to produce renewable chemicals. (2) Eligible property The term eligible property means any property\u2014 (A) which is\u2014 (i) tangible personal property, or (ii) other tangible property (not including a building or its structural components), but only if such property is used as an integral part of the renewable chemical production facility, and (B) with respect to which depreciation (or amortization in lieu of depreciation) is allowable. (3) Renewable chemical The term renewable chemical has the meaning given such term by section 45BB(c)(1). (d) Certain qualified progress expenditures rules made applicable Rules similar to the rules of subsections (c)(4) and (d) of section 46 (as in effect on the day before the enactment of the Revenue Reconciliation Act of 1990) shall apply for purposes of this section. (e) National limitation on credits for renewable chemicals (1) In general Not later than 180 days after the date of the enactment of this section, the Secretary, in consultation with the Secretary of Agriculture, shall establish a program to allocate credit amounts under this section and section 45BB to taxpayers who produce renewable chemicals for taxable years ending after the date of the enactment of this section. (2) Limitations (A) Aggregate limitation The total amount of credits that may be allocated under such program shall not exceed $500,000,000. (B) Taxpayer limitation The amount of credits that may be allocated to any taxpayer under such program shall not exceed $25,000,000. For purposes of the preceding sentence, all persons treated as a single employer under subsection (a) or (b) of section 52, or subsection (m) or (o) of section 414, shall be treated as one taxpayer. (3) Selection criteria In determining to which taxpayers to make allocations of the credit amount under such program, the Secretary shall take into consideration\u2014 (A) the number of jobs created and maintained (directly and indirectly) in the United States (including territories and possessions of the United States) as a result of such allocation during the credit period and thereafter, (B) the degree to which the production of the renewable chemical demonstrates reduced dependence on imported feedstocks, petroleum, non-renewable resources, or other fossil fuels, (C) the technological innovation involved in the production method of the renewable chemical, (D) the energy efficiency and reduction in lifecycle greenhouse gases of the renewable chemical or of the production method of the renewable chemical, (E) the extent to which the renewable chemical or its production method advances sustainable chemistry, as defined by the Office of Science and Technology Policy, including by\u2014 (i) improving the safety, efficiency, and environmental performance of chemical design, manufacture, or use, (ii) reducing risks to human health, and (iii) enhancing circularity and resource efficiency across the chemical lifecycle, (F) whether there is a reasonable expectation of commercial viability, (G) whether the renewable chemical has an established market, and (H) whether the renewable chemical is currently being produced in commercial quantities. (4) Review and reallocation (A) Review Not later than 6 years after the date of the enactment of this section, the Secretary shall review the credits allocated under this section. (B) Reallocation If the Secretary determines that unused credits are available for reallocation after the review described in subparagraph (A), the Secretary is authorized to conduct an additional program for applications for certification. (5) Disclosure of allocations The Secretary shall, upon making an allocation of credit amount under this section, publicly disclose the identity of the taxpayer and the amount of the credit with respect to such taxpayer. (f) Coordination with production credit for renewable chemicals If a taxpayer makes an election under subsection (c)(1)(C)(ii) with respect to a renewable chemical production facility, a credit shall not be allowed under section 45BB for any renewable chemical produced by such facility. (g) Regulations The Secretary shall issue such regulations or other guidance as may be necessary to carry out this section and section 45BB. (h) Termination The Secretary may not allocate any credit amount under this section to any taxable year which begins more than 5 years after the date of the enactment of this section. .\n##### (c) Credits allowable against alternative minimum tax\nSubparagraph (B) of section 38(c)(4) of the Internal Revenue Code of 1986 is amended by redesignating clauses (x) through (xii) as clauses (xii) through (xiv), respectively, and by inserting after clause (ix) the following new clauses:\n(x) the credit determined under section 45BB, (xi) the credit determined under section 46 to the extent that such credit is attributable to the renewable chemical production facilities credit under section 48F, .\n##### (d) Clerical amendments\n**(1)**\nThe table of sections for subpart D of part IV of subchapter A of chapter 1 of the Internal Revenue Code of 1986 is amended by adding at the end the following new item:\nSec. 45BB. Credit for production of renewable chemicals. .\n**(2)**\nThe table of sections for subpart E of part IV of subchapter A of chapter 1 of such Code is amended by adding at the end the following new item:\nSec. 48F. Investment credit for renewable chemical production facilities. .\n##### (e) Effective dates\nThe amendments made by this section shall apply to renewable chemicals produced and renewable chemical production facilities placed in service after the date of the enactment of this Act, in taxable years ending after such date.",
      "versionDate": "2026-01-14",
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
        "name": "Taxation",
        "updateDate": "2026-02-10T00:31:06Z"
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
      "date": "2026-01-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3632is.xml"
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
      "title": "Renewable Chemicals Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-05T05:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Renewable Chemicals Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-05T05:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide credits for the production of renewable chemicals and investments in renewable chemical production facilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-05T05:48:40Z"
    }
  ]
}
```
