# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4265?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4265
- Title: Freedom to Build Act
- Congress: 119
- Bill type: S
- Bill number: 4265
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-21T14:44:37Z
- Update date including text: 2026-04-21T14:44:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4265",
    "number": "4265",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "H000601",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Hagerty, Bill [R-TN]",
        "lastName": "Hagerty",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Freedom to Build Act",
    "type": "S",
    "updateDate": "2026-04-21T14:44:37Z",
    "updateDateIncludingText": "2026-04-21T14:44:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T21:15:44Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4265is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4265\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mr. Hagerty introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo require the Secretary of Housing and Urban Development to establish a Freedom to Build designation for certain localities.\n#### 1. Short title\nThis Act may be cited as the Freedom to Build Act .\n#### 2. Freedom to Build designation\n##### (a) Establishment\n**(1) In general**\nNot later than 18 months after the date of enactment of this Act, the Secretary of Housing and Urban Development shall establish a Freedom to Build designation for eligible localities that voluntarily qualify under subsection (b) or subsection (c).\n**(2) List**\nThe Secretary of Housing and Urban Development shall maintain and publish on a publicly accessible website a list of all localities that have received a Freedom to Build designation, updated not less frequently than annually.\n**(3) Duration**\nA Freedom to Build designation shall be effective for a 5-year period beginning on the date on which the designation is made and shall be renewable upon a demonstration of continued qualification under subsection (b) or subsection (c).\n**(4) Rule of construction**\nNothing in this subsection shall be construed to require any locality to apply for or obtain a Freedom to Build designation.\n##### (b) Qualification by reform adoption\n**(1) In general**\nA locality may qualify for a Freedom to Build designation by certifying to the Secretary of Housing and Urban Development that the locality has adopted not fewer than the minimum number of reforms specified by the Secretary under paragraph (3) from each of the 3 categories described in paragraph (2).\n**(2) Categories of reform**\nThe Secretary of Housing and Urban Development shall, through notice-and-comment rulemaking, identify specific reforms within each of the following categories:\n**(A) Unleashing construction innovation**\nReforms that remove regulatory barriers to the use of modern construction technologies, materials, and methods, including modular, pre-fabricated, panelized, and other off-site construction techniques, by aligning local requirements with nationally recognized standards and prohibiting differential treatment based on mode of construction. Such reforms may include\u2014\n**(i)**\naligning local codes governing off-site construction with nationally recognized standards, including standards published by the International Code Council;\n**(ii)**\npermitting emerging construction materials and methods without differential treatment based on whether or how a dwelling is fabricated; and\n**(iii)**\nprohibiting local amendments to the model building code that add cost beyond what the nationally recognized code requires, unless the locality demonstrates a specific safety basis for such amendment.\n**(B) Fast-tracking the approval process**\nReforms that reduce the time, cost, and uncertainty of the development approval process and provide builders with meaningful recourse when the process fails. Such reforms may include\u2014\n**(i)**\nby-right approval for projects that conform to applicable zoning and building codes, without discretionary review;\n**(ii)**\nbinding maximum timelines for permit decisions and inspections, with clear remedies for the applicant, which may include deemed approval or immediate administrative appeal, when deadlines are not met;\n**(iii)**\nfull public disclosure of all permits, approvals, inspections, and associated fees that may be required, and prohibition of undisclosed requirements or mid-process cost increases;\n**(iv)**\nlimiting the impact fees and offsite charges to costs with a reasonable nexus to the specific development project;\n**(v)**\nauthorizing builders to use qualified third-party inspectors for required inspections and to select licensed professionals of their choice for required studies;\n**(vi)**\nprotecting approved development plans from the retroactive application of code changes adopted after the date on which approval was granted;\n**(vii)**\nlimiting standing to challenge an approved development to parties who can demonstrate that the development would create a common-law nuisance or an immediate threat to health, safety, or welfare; and\n**(viii)**\nan expedited dispute resolution process for denials and delays, under which the jurisdiction bears the burden of demonstrating that its action is necessary to protect substantial public health, safety, or welfare interests, and under which the builder may recover costs and damages for unreasonable delay.\n**(C) Defending property rights and family freedom**\nReforms that eliminate government mandates that restrict what may be built, how it may be built, who may build it, what energy sources it may use, or what owners and tenants may do with their property, where such mandates exceed what is demonstrably required for prevention of physical injury. Such reforms may include\u2014\n**(i)**\nprohibiting rent control or rent stabilization on dwelling units, which may exempt existing dwellings, for which a certificate of occupancy is first issued after the date of designation;\n**(ii)**\nprotecting the ability of property owners to promptly address nonpayment, lease violations, fraud, and unauthorized occupancy;\n**(iii)**\nprohibiting mandatory below-market set-asides in new development unless the requirement is fully offset by a density bonus, fee waiver, or equivalent incentive voluntarily accepted by the builder;\n**(iv)**\nprohibiting wage, residency, or workforce-composition mandates on housing development projects beyond those imposed by generally applicable State law;\n**(v)**\nrequiring that local building code provisions be consistent with evidence-based standards promulgated by the Secretary of Commerce, the Secretary of Agriculture, the Secretary of Housing and Urban Development, the National Institute of Standards and Technology, or any other Federal agency, and eliminating non-safety-related local additions;\n**(vi)**\nauthorizing builders to comply with a Federally recognized energy rating index as an alternative to prescriptive energy efficiency codes, and prohibiting mandates for electric-vehicle charging infrastructure or on-site renewable energy generation;\n**(vii)**\nprohibiting local ordinances that ban or effectively eliminate the choice of a property owner of a residential energy source;\n**(viii)**\nauthorizing builders to design to any version of the applicable building or energy code adopted within a reasonable period, as determined by the Secretary of Housing and Urban Development, at the time of plan submission, rather than only the most recently adopted edition;\n**(ix)**\nlimiting regulatory layering, including prohibiting State requirements that add to project costs beyond applicable Federal requirements, and prohibiting local requirements that add to project costs beyond applicable State requirements, unless justified by documented jurisdiction-specific health or safety characteristics;\n**(x)**\nprohibiting growth moratoria, construction caps, or geographic containment boundaries that restrict where new housing may be built; and\n**(xi)**\nprohibiting rules or policies that penalize or increase the cost of a housing development on the basis that it is primarily accessible by automobile.\n**(3) Minimum thresholds**\nThe Secretary of Housing and Urban Development shall, through notice-and-comment rulemaking, establish the minimum number of reforms from each category described in paragraph (2) that a locality must adopt to qualify for a Freedom to Build designation. The minimum number shall be not fewer than 3 reforms from each category.\n##### (c) Qualification by housing supply outcomes\n**(1) In general**\nAs an alternative to qualification under subsection (b), a locality may qualify for a Freedom to Build designation by demonstrating sustained housing supply growth meeting an affordability-adjusted target established by the Secretary of Housing and Urban Development under this subsection.\n**(2) Affordability-adjusted target**\nThe Secretary of Housing and Urban Development shall, through notice-and-comment rulemaking, establish a formula for determining the supply growth target applicable to each locality. The formula shall\u2014\n**(A)**\nset a higher supply growth target for localities in housing markets in which housing costs are high and rising, and a lower target, which may be zero, for localities in housing markets in which housing costs are affordable and stable;\n**(B)**\naccount for both the level of housing costs, such as the ratio of median home price to median household income, and the trajectory of housing costs, such as the rate of home price or rent appreciation;\n**(C)**\nmeasure housing costs at the level of the metropolitan statistical area or the housing market area defined by the Secretary, rather than at the level of the individual locality, to prevent a locality from avoiding a supply growth target applicable to its region;\n**(D)**\nmeasure supply growth relative to the affordability-adjusted target rather than by raw production volume; and\n**(E)**\npermit the supply growth target to be met by an individual locality or through documented participation by the locality in a regional housing production compact with one or more other localities.\n**(3) Data sources**\nIn establishing the formula under paragraph (2), the Secretary of Housing and Urban Development shall use existing, publicly available data, which may include the House Price Index published by the Federal Housing Finance Agency, the American Community Survey of the Bureau of the Census, Fair Market Rents published by the Department of Housing and Urban Development, and housing unit counts from the decennial census or the American Community Survey.\n##### (d) Periodic review\nThe Secretary of Housing and Urban Development shall review, and if appropriate update through notice-and-comment rulemaking, the specific reforms identified under subsection (b)(2) and the formula established under subsection (c)(2) not less than once every 5 years after the date on which the regulations are promulgated.\n##### (e) Revocation\n**(1) In general**\nThe Secretary of Housing and Urban Development may revoke the Freedom to Build designation of a locality upon a finding that the locality has\u2014\n**(A)**\nmaterially reversed 1 or more qualifying reforms adopted under subsection (b); or\n**(B)**\nceased to meet the supply growth target under subsection (c), as applicable.\n**(2) Notice**\nBefore revoking a designation under paragraph (1), the Secretary of Housing and Urban Development shall provide the locality with written notice and a period of not less than 180 days to cure the deficiency.\n#### 3. Prioritization of Freedom to Build designated localities in competitive grants\n##### (a) Findings\nCongress finds the following:\n**(1)**\nLocal regulatory barriers, including restrictive zoning, burdensome permitting processes, and cost-increasing mandates, are a significant contributor to housing-supply constraints and rising housing costs across the United States.\n**(2)**\nFederal investments in infrastructure, transportation, and community development generate greater public benefit when the surrounding regulatory environment permits the construction of housing in response to improved accessibility and economic opportunity.\n**(3)**\nCommunities that remove regulatory barriers to homebuilding serve national economic, workforce development, and housing affordability objectives.\n**(4)**\nFederal tax incentives for housing production and investment, including the low-income housing tax credit under section 42 of the Internal Revenue Code of 1986, qualified opportunity zone incentives under section 1400Z\u20132 of such Code, and the new markets tax credit under section 45D of such Code, generate greater returns for taxpayers and produce more housing when deployed in communities with pro-building regulatory environments.\n**(5)**\nFederal housing, transportation, and community development funds achieve greater impact when directed to communities where the regulatory environment enables those investments to produce their intended results. Directing such funds to communities that simultaneously maintain regulatory barriers to the construction those programs are designed to support diminishes the effectiveness and return on the Federal investment.\n**(6)**\nAn adequate and growing supply of housing allows demand growth from rising incomes and declining interest rates to result in expanded homeownership rather than higher home prices, property taxes, and homeowner insurance premiums, thereby protecting the affordability and value of homeownership for current and prospective homeowners.\n**(7)**\nThe Freedom to Build designation established under section 2 provides a reliable and verifiable indicator that a community has committed to a regulatory environment supportive of housing supply growth.\n##### (b) Priority for freedom To build communities\nThe Secretary of Housing and Urban Development shall prioritize applicants that are located in or primarily serve communities with a current Freedom to Build designation under section 2 for any competitive grant administered by the Department of Housing and Urban Development that relates to housing development, community development, or any other competitive grant relating to the construction, modification, rehabilitation, or preservation of housing.\n##### (c) Sense of congress\nIt is the sense of Congress that Federal agencies administering competitive grant programs for infrastructure, transportation, and community development, including the Department of Transportation, the Environmental Protection Agency, and the Department of Agriculture, should consider whether an applicant is located in a locality with a current Freedom to Build designation under section 2 as a positive factor in evaluating applications for such grants where housing supply or community development is relevant to the objectives of the program.",
      "versionDate": "2026-03-26",
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
        "name": "Housing and Community Development",
        "updateDate": "2026-04-21T14:44:37Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4265is.xml"
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
      "title": "Freedom to Build Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-18T02:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Freedom to Build Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-18T02:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Housing and Urban Development to establish a Freedom to Build designation for certain localities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-18T02:48:30Z"
    }
  ]
}
```
