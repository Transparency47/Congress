# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/127?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/127
- Title: Whole-Home Repairs Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 127
- Origin chamber: Senate
- Introduced date: 2025-01-16
- Update date: 2026-05-07T20:16:36Z
- Update date including text: 2026-05-07T20:16:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-01-16: Introduced in Senate
- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-01-16: Introduced in Senate

## Actions

- 2025-01-16 - IntroReferral: Introduced in Senate
- 2025-01-16 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/127",
    "number": "127",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "F000479",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Fetterman, John [D-PA]",
        "lastName": "Fetterman",
        "party": "D",
        "state": "PA"
      }
    ],
    "title": "Whole-Home Repairs Act of 2025",
    "type": "S",
    "updateDate": "2026-05-07T20:16:36Z",
    "updateDateIncludingText": "2026-05-07T20:16:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-01-16",
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
      "actionDate": "2025-01-16",
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
        "item": [
          {
            "date": "2025-01-16T20:32:30Z",
            "name": "Referred To"
          },
          {
            "date": "2025-01-16T20:32:30Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "WY"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-01-16",
      "state": "SD"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-01-16",
      "state": "MN"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "False",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "MT"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-02-18",
      "state": "MN"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-25",
      "state": "PA"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2025-03-11",
      "state": "MD"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "False",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-04-10",
      "state": "WV"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "GA"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s127is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 127\nIN THE SENATE OF THE UNITED STATES\nJanuary 16, 2025 Mr. Fetterman (for himself, Ms. Lummis , Mr. Rounds , and Ms. Smith ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo establish a whole-home repairs program for eligible homeowners and eligible landlords, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Whole-Home Repairs Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Affordable unit**\nThe term affordable unit means a unit with a rental payment that is affordable to a tenant with an income at or below 80 percent of the area median income, as defined by the Secretary.\n**(2) Assisted unit**\nThe term assisted unit means a unit that undergoes repair or rehabilitation work through a whole-home repairs program administered by an implementing organization under this Act.\n**(3) Eligible homeowner**\nThe term eligible homeowner means a homeowner\u2014\n**(A)**\nwith a household income that\u2014\n**(i)**\nis not more than 80 percent of the area median income;\n**(ii)**\nis not more than 200 percent of the Federal poverty guidelines, as determined by the Secretary of Health and Human Services; or\n**(iii)**\nmeets the income eligibility criteria of another program used by a Federal agency for programs focusing on families of limited means, as determined by the Secretary; and\n**(B)**\nwho is\u2014\n**(i)**\nan owner of record as evidenced by a publicly recorded deed and occupies the home on which repairs are to be conducted as their principal residence;\n**(ii)**\nan owner-occupant of the manufactured home on which repairs are to be conducted; or\n**(iii)**\nan equitable owner who can demonstrate an ownership interest in the property on which repairs are to be conducted, including a person who has inherited an interest in that property.\n**(4) Eligible landlord**\nThe term eligible landlord means an individual\u2014\n**(A)**\nwho owns, as determined by the relevant implementing organization, fewer than 10 residential rental properties, with a majority of affordable units and not more than 50 total units, operated as primary residences in which a majority ownership interest is held by the individual, the spouse of the individual, or the dependent children of the individual, or any closely held legal entity controlled by the individual, the spouse of the individual, or the dependent children of the individual, either individually or collectively; and\n**(B)**\nwho agrees to the provisions described in section 3(c).\n**(5) Eligible rental property**\nThe term eligible rental property means a residential property that is leased, or offered exclusively for lease, as a primary residence.\n**(6) Forgivable loan**\nThe term forgivable loan means a loan\u2014\n**(A)**\nmade to an eligible landlord;\n**(B)**\nthat is secured by a lien recorded against a residential property; and\n**(C)**\nthat may be forgiven by the implementing organization not later than the date that is 3 years after the completion of the repairs if the eligible landlord has maintained compliance with the loan agreement described in section 3(c).\n**(7) Implementing organization**\nThe term implementing organization \u2014\n**(A)**\nmeans a unit of general local government or a State that will administer a whole-home repairs program through an agency, department, or other entity or enter into agreements with 1 or more local governments, municipal authorities, other governmental authorities, or qualified nonprofits to administer a whole-home repairs program as a subrecipient; and\n**(B)**\ndoes not include a redundant entity in a jurisdiction already served by a grantee under section 3.\n**(8) Indian Tribe**\nThe term Indian Tribe has the meaning given the term Indian tribe in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(9) Qualified nonprofit**\nThe term qualified nonprofit means a nonprofit organization that has\u2014\n**(A)**\nreceived funding, as a recipient or subrecipient, through\u2014\n**(i)**\nthe Community Development Block Grant program under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. );\n**(ii)**\nthe HOME Investment Partnerships program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. );\n**(iii)**\nthe Lead-Based Paint Hazard Reduction grant program under section 1011 of the Residential Lead-Based Paint Hazard Reduction Act of 1992 ( 42 U.S.C. 4852 ) or a grant under the Healthy Homes Initiative administered by the Secretary pursuant to sections 501 and 502 of the Housing and Urban Development Act of 1970 ( 12 U.S.C. 1701z\u20131 , 1701z\u20132);\n**(iv)**\nthe Self-Help and Assisted Homeownership Opportunity program authorized under section 11 of the Housing Opportunity Program Extension Act of 1996 ( 42 U.S.C. 12805 note);\n**(v)**\na rural housing program under title V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. );\n**(vi)**\nthe Neighborhood Reinvestment Corporation established under the Neighborhood Reinvestment Corporation Act ( 42 U.S.C. 8101 et seq. ); or\n**(vii)**\nany other program as determined by the Secretary;\n**(B)**\ncoordinated, performed, or otherwise been engaged in weatherization, lead remediation, or home-repair work for not less than 2 years; or\n**(C)**\nbeen certified by the Environmental Protection Agency, or by a State authorized by the Environmental Protection Agency to administer a certification program, as\u2014\n**(i)**\neligible to carry out activities under the lead renovation, repair and painting program; or\n**(ii)**\na Home Certification Organization under the Energy Star program established by section 324A of the Energy Policy and Conservation Act ( 42 U.S.C. 6294a ) or the WaterSense program under section 324B of that Act ( 42 U.S.C. 6294b ), or recognized or otherwise approved by the Environmental Protection Agency as a Home Certification Organization under either of those programs.\n**(10) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(11) State**\nThe term State means\u2014\n**(A)**\neach State of the United States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico;\n**(D)**\nany territory or possession of the United States; and\n**(E)**\nan Indian Tribe.\n**(12) Whole-home repairs**\nThe term whole-home repairs means modifications, repairs, or updates to homeowner or renter-occupied units to address\u2014\n**(A)**\nphysical and sensory accessibility for individuals with disabilities and older adults, such as bathroom and kitchen modifications, installation of grab bars and handrails, guards and guardrails, lifting devices, ramp additions or repairs, sidewalk addition or repair, or doorway or hallway widening;\n**(B)**\nhabitability and safety concerns, such as repairs needed to ensure residential units are fit for human habitation and free from defective conditions or health and safety hazards;\n**(C)**\nenergy and water efficiency, resilience, and weatherization; or\n**(D)**\nother conditions as determined by the Secretary.\n#### 3. Pilot program\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish a pilot program to provide grants to implementing organizations to administer a whole-home repairs program for eligible homeowners and eligible landlords.\n##### (b) Use of funds\nAn implementing organization that receives a grant under this section\u2014\n**(1)**\nshall provide grants to eligible homeowners to implement whole-home repairs up to a maximum amount per unit, which maximum amount should\u2014\n**(A)**\nreflect local construction costs;\n**(B)**\nbe calculated by the implementing organization; and\n**(C)**\nbe approved by the Secretary;\n**(2)**\nshall provide loans, which may be forgivable loans, to eligible landlords to implement whole-home repairs for individual affordable units, public and common use areas within the property, and common structural elements up to a maximum amount per unit, area, or element, as applicable, which maximum amount should\u2014\n**(A)**\nreflect local construction costs;\n**(B)**\nbe calculated by the implementing organization; and\n**(C)**\nbe approved by the Secretary;\n**(3)**\nshall evaluate, or provide assistance to eligible homeowners and eligible landlords to evaluate, whole-home repair program funds provided under this section with Federal, State, and local home repair programs to provide the greatest benefit to the greatest number of eligible landlords and eligible homeowners and avoid redundancy;\n**(4)**\nshall ensure that\u2014\n**(A)**\nall repairs funded or facilitated through an award under this section have been completed;\n**(B)**\nif repairs are not completed and the plan for whole-home repairs is not updated to reflect the new scope of work, that the loan or grant is repaid on a prorated basis based on completed work; and\n**(C)**\nany unused grant or loan balance is returned to the implementing organization;\n**(5)**\nmay use not more than 10 percent of the awarded funds to carry out related functions, including workforce training, which shall be related to efforts to increase the number of home repairs performed and approved by the Secretary;\n**(6)**\nmay use not more than 10 percent of the awarded funds for administrative expenses; and\n**(7)**\nshall comply with Federal accessibility requirements and standards under applicable Federal fair housing and civil rights laws and regulations, including section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ).\n##### (c) Loan agreement\nIn a loan agreement with an eligible landlord under this section, an implementing organization shall include provisions establishing that the eligible landlord shall, for each eligible rental property for which a loan is used to fund repairs under this section\u2014\n**(1)**\ncomply with Federal accessibility requirements and standards under applicable Federal fair housing and civil rights laws and regulations, including section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ); and\n**(2)**\n**(A)**\nif the landlord is renting the assisted units available in the eligible rental property to tenants receiving tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ), under another tenant-based rental assistance program administered by the Secretary or the Secretary of Agriculture, or under a tenant-based rental subsidy provided by a State or local government, comply with the program requirements under the relevant tenant-based rental assistance program; or\n**(B)**\nif the eligible landlord is not renting to tenants receiving rental-based assistance as described in subparagraph (A)\u2014\n**(i)**\n**(I)**\noffer to extend the lease of current tenants on current terms, other than the terms described in clause (iv), for not less than 3 years beginning after the completion of the repairs, unless the lease is terminated due to failure to pay rent, property damage, performance of an illegal act within the rental unit, a direct threat to the safety of the tenants, or a violation of an obligation of tenancy that the tenants failed to correct after notice; and\n**(II)**\nif the tenant of an assisted unit moves out of the assisted unit at any point in the 3-year period following the loan agreement, maintain the unit as an affordable unit;\n**(ii)**\nprovide documentation verifying that the property, upon completion of approved renovations, has met all applicable State and local housing and building codes;\n**(iii)**\nattest that the landlord has no known serious violations of renter protections that have resulted in fines, penalties, or judgments during the preceding 10 years; and\n**(iv)**\ncap annual rent increases for each assisted unit at 5 percent of base rent or inflation, whichever is lower, for not less than 3 years beginning after the completion of the repairs.\n##### (d) Application\n**(1) In general**\nAn implementing organization desiring an award under this section shall submit to the Secretary an application that includes\u2014\n**(A)**\nthe geographic scope of the whole-home repairs program to be administered by the implementing organization, including the plan to address need in any rural, suburban, or urban area within a jurisdiction;\n**(B)**\na plan for selecting subrecipients, if applicable;\n**(C)**\nhow the implementing organization plans to execute the coordination of Federal, State, and local home repair programs, including programs administered by the Department of Energy or the Department of Agriculture, to increase efficiency and reduce redundancy;\n**(D)**\navailable data on the need for affordable and quality housing, and any plans to preserve affordability through the term of the award;\n**(E)**\nhow the implementing organization plans to process and verify applications for grants from eligible homeowners and applications for loans from eligible landlords; and\n**(F)**\nsuch other information as the Secretary requires to determine the ability of an applicant to carry out a program under this section.\n**(2) Considerations**\nIn making awards under this section, the Secretary shall\u2014\n**(A)**\nwith respect to applications submitted by States other than the District of Columbia and the territories of the United States, prioritize those applications with a demonstrated plan to\u2014\n**(i)**\nmake a good faith effort to implement the pilot program in every jurisdiction; and\n**(ii)**\nprovide non-metropolitan areas, or subrecipients serving non-metropolitan areas if applicable, with a share of total funds commensurate to their population;\n**(B)**\naim to select applicants so that the awardees collectively span diverse geographies, with an intent to understand the impact of the pilot program under this section in urban, suburban, rural, and Tribal settings; and\n**(C)**\nnot disqualify implementing organizations that were awarded grants under the pilot program in prior application cycles.\n##### (e) Program information\nThe Secretary shall make available to grant recipients under this section information regarding existing Federal programs for which grant recipients may coordinate or provide assistance in coordinating applications for those programs in accordance with subsection (b)(3).\n##### (f) Grant number\nIn each year in which an award is made under this section, the Secretary shall award assistance to\u2014\n**(1)**\nnot less than 2, and not more than 10, implementing organizations, as application numbers and funding permit; and\n**(2)**\nnot more than 1 implementing organization in any State.\n##### (g) Loans that are not forgiven\nIf a loan made by an implementing organization under subsection (b)(2) is not forgiven, the loan repayment funds may be reused by the implementing organization for a new whole-home repair grant or loan under this section.\n##### (h) Supplement, not supplant\nAmounts awarded under this section to implementing organizations shall supplement, not supplant, other Federal, State, and local funds made available to those entities.\n##### (i) Streamlining program delivery and ensuring efficiency\nTo the extent possible, in carrying out the pilot program under this section, the Secretary shall\u2014\n**(1)**\nendeavor to improve efficiency of service delivery, as well as the experience of and impact on the taxpayer, by encouraging programmatic collaboration and information sharing across Federal, State, and local programs for home repair or improvement, including programs administered by the Department of the Agriculture; and\n**(2)**\nenhance collaboration and cross-agency streamlining efforts that reduce the burdens of multiple income verification processes and applications on the eligible homeowner, the eligible landlord, the implementing organization, and the Federal Government, including by establishing assistance application procedures for income eligibility under this Act that recognize income eligibility determinations for assistance using any of the criteria under section 2(3)(A) that have been used for assistance applications during the 1-year period preceding the date on which an eligible homeowner or eligible landlord applies for assistance under this Act.\n##### (j) Reporting requirements\n**(1) Annual report**\nAn implementing organization that receives a grant under this section shall submit to the Secretary an annual report on initial funding that includes\u2014\n**(A)**\nthe number of units served, including reporting on both homeownership and rental units;\n**(B)**\nthe average cost per unit for modifications or repairs and the nature of those modifications or repairs, including reporting on both homes and rental units;\n**(C)**\nthe number of applications received, served, denied, or not completed;\n**(D)**\nthe aggregated demographic data of grant recipients, which may include data on income range, urban, suburban, and rural residency, age, and racial and ethnic identity;\n**(E)**\nthe aggregated demographic data of loan recipients, which may include data on income range, urban, suburban, and rural residency, age, and racial and ethnic identity;\n**(F)**\nin the first year of receiving a grant, and as certified in subsequent reports, a comprehensive plan to prevent waste, fraud, and abuse in the administration of the pilot program, which shall include, at a minimum\u2014\n**(i)**\na policy enacted and enforced by the implementing organization to monitor ongoing expenditures under this title and ensure compliance with applicable regulations, including compliance with Federal accessibility requirements;\n**(ii)**\na policy enacted and enforced by the implementing organization to detect and deter fraudulent activity, including fraud occurring in individual projects and patterns of fraud by parties involved in the expenditure of funds under this section;\n**(iii)**\na statement setting forth any violations detected by the implementing organization during the previous calendar year, including details about steps taken to achieve compliance and any remedial measures; and\n**(iv)**\na certification by the chief executive or most senior compliance officer of the organization that the organization maintains sufficient staff and resources to effectively carry out the above-mentioned policies; and\n**(G)**\nsuch other information as the Secretary may require.\n**(2) Reporting requirement alignment**\nTo limit the costs of implementing the pilot program under this section, the Secretary shall endeavor, to the extent possible, to structure reporting requirements such that they align with the data reporting requirements in place for funding streams that implementing organizations are likely to use in partnership with funding from this section, including the reporting requirements under\u2014\n**(A)**\nthe Community Development Block Grant program under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. );\n**(B)**\nthe HOME Investment Partnerships program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. );\n**(C)**\nthe Weatherization Assistance Program for low-income persons established under part A of title IV of the Energy Conservation and Production Act ( 42 U.S.C. 6861 et seq. ); and\n**(D)**\nthe Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ).\n**(3) Pilot program period reports**\nNot less frequently than twice during the period in which the pilot program established under this section operates, the Office of the Inspector General of the Department of Housing and Urban Development shall complete an assessment of the implementation of measures to ensure the fair and legitimate use of the pilot program.\n**(4) Summary to Congress**\nThe Secretary shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives an annual report providing a summary of the data provided under paragraphs (1) and (3) during the 1-year period preceding the report and all data previously provided under those paragraphs.\n##### (k) Funding\nThe Secretary is authorized to use up to $25,000,000 of funds made available as provided in appropriations Acts for programs administered by the Office of Lead Hazard Control and Healthy Homes to carry out the pilot program under this section.\n##### (l) Termination\nThe pilot program established under this section shall terminate on October 1, 2030.",
      "versionDate": "2025-01-16",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional oversight",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Housing and community development funding",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Landlord and tenant",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Low- and moderate-income housing",
            "updateDate": "2025-03-07T18:22:13Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-03-07T18:22:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Housing and Community Development",
        "updateDate": "2025-02-19T13:39:42Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-16",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s127",
          "measure-number": "127",
          "measure-type": "s",
          "orig-publish-date": "2025-01-16",
          "originChamber": "SENATE",
          "update-date": "2026-05-07"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s127v00",
            "update-date": "2026-05-07"
          },
          "action-date": "2025-01-16",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Whole-Home Repairs Act of 2025</strong></p><p>This bill establishes a pilot program through which the Department of Housing and Urban Development provides grants\u00a0to state and local governments to support the ability of certain landlords and low- to moderate-income homeowners to make necessary modifications, repairs, or updates to their properties.</p><p> State and local governments must use the funds they receive under the program to award grants to homeowners and loans to landlords to make changes that address issues such as\u00a0accessibility, habitability, and energy efficiency.\u00a0</p><p>A homeowner is eligible for a grant\u00a0if the homeowner's household income (1) does not exceed 80% of the area median income, (2) does not exceed 200% of the federal poverty guidelines, or (3) meets the income eligibility criteria of another federal program that serves families of limited means.\u00a0A landlord is eligible for a loan (which may be forgivable) if the landlord\u00a0owns fewer than 10 rental properties that have a total of up to 50 units and that mostly consist of units that are affordable\u00a0(i.e., affordable to a tenant with an income that does not exceed 80% of the area median income).</p><p>The program terminates on October 1, 2030.\u00a0</p>"
        },
        "title": "Whole-Home Repairs Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s127.xml",
    "summary": {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Whole-Home Repairs Act of 2025</strong></p><p>This bill establishes a pilot program through which the Department of Housing and Urban Development provides grants\u00a0to state and local governments to support the ability of certain landlords and low- to moderate-income homeowners to make necessary modifications, repairs, or updates to their properties.</p><p> State and local governments must use the funds they receive under the program to award grants to homeowners and loans to landlords to make changes that address issues such as\u00a0accessibility, habitability, and energy efficiency.\u00a0</p><p>A homeowner is eligible for a grant\u00a0if the homeowner's household income (1) does not exceed 80% of the area median income, (2) does not exceed 200% of the federal poverty guidelines, or (3) meets the income eligibility criteria of another federal program that serves families of limited means.\u00a0A landlord is eligible for a loan (which may be forgivable) if the landlord\u00a0owns fewer than 10 rental properties that have a total of up to 50 units and that mostly consist of units that are affordable\u00a0(i.e., affordable to a tenant with an income that does not exceed 80% of the area median income).</p><p>The program terminates on October 1, 2030.\u00a0</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119s127"
    },
    "title": "Whole-Home Repairs Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-16",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Whole-Home Repairs Act of 2025</strong></p><p>This bill establishes a pilot program through which the Department of Housing and Urban Development provides grants\u00a0to state and local governments to support the ability of certain landlords and low- to moderate-income homeowners to make necessary modifications, repairs, or updates to their properties.</p><p> State and local governments must use the funds they receive under the program to award grants to homeowners and loans to landlords to make changes that address issues such as\u00a0accessibility, habitability, and energy efficiency.\u00a0</p><p>A homeowner is eligible for a grant\u00a0if the homeowner's household income (1) does not exceed 80% of the area median income, (2) does not exceed 200% of the federal poverty guidelines, or (3) meets the income eligibility criteria of another federal program that serves families of limited means.\u00a0A landlord is eligible for a loan (which may be forgivable) if the landlord\u00a0owns fewer than 10 rental properties that have a total of up to 50 units and that mostly consist of units that are affordable\u00a0(i.e., affordable to a tenant with an income that does not exceed 80% of the area median income).</p><p>The program terminates on October 1, 2030.\u00a0</p>",
      "updateDate": "2026-05-07",
      "versionCode": "id119s127"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s127is.xml"
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
      "title": "Whole-Home Repairs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-05T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Whole-Home Repairs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-19T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a whole-home repairs program for eligible homeowners and eligible landlords, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-19T03:18:24Z"
    }
  ]
}
```
