# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5990?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5990
- Title: Whole-Home Repairs Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5990
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2026-05-30T08:06:11Z
- Update date including text: 2026-05-30T08:06:11Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Financial Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5990",
    "number": "5990",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "W000788",
        "district": "5",
        "firstName": "Nikema",
        "fullName": "Rep. Williams, Nikema [D-GA-5]",
        "lastName": "Williams",
        "party": "D",
        "state": "GA"
      }
    ],
    "title": "Whole-Home Repairs Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-30T08:06:11Z",
    "updateDateIncludingText": "2026-05-30T08:06:11Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "D000634",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Downing, Troy [R-MT-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Downing",
      "party": "R",
      "sponsorshipDate": "2025-11-07",
      "state": "MT"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2026-05-29",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5990ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5990\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Ms. Williams of Georgia (for herself and Mr. Downing ) introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo require the Secretary of Housing and Urban Development to establish a pilot program to provide grants to implementing organizations to administer a whole-home repairs program for eligible homeowners and eligible landlords, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Whole-Home Repairs Act of 2025 .\n#### 2. Whole-Home Repairs pilot program\n##### (a) Definitions\nIn this section:\n**(1) Affordable unit**\nThe term affordable unit means a unit for which the monthly rental payment is not more than 30 percent of the gross income of an individual earning at or below 80 percent of the area median income, as defined by the Secretary.\n**(2) Assisted unit**\nThe term assisted unit means a unit that undergoes repair or rehabilitation work through a whole-home repairs program administered by an implementing organization under this section.\n**(3) Eligible homeowner**\nThe term eligible homeowner means a homeowner\u2014\n**(A)**\nwith a household income that\u2014\n**(i)**\nis not more than 80 percent of the area median income; or\n**(ii)**\nmeets the income eligibility requirements for receiving assistance or benefits under a specified program, as defined in paragraph (11); and\n**(B)**\nwho is\u2014\n**(i)**\nan owner of record as evidenced by a publicly recorded deed and occupies the home on which repairs are to be conducted as their principal residence;\n**(ii)**\nan owner-occupant of the manufactured home on which repairs are to be conducted; or\n**(iii)**\nan owner who can demonstrate an ownership interest in the property on which repairs are to be conducted, including a person who has inherited an interest in that property.\n**(4) Eligible landlord**\nThe term eligible landlord means an individual\u2014\n**(A)**\nwho owns, as determined by the relevant implementing organization, fewer than 10 eligible rental properties, with a majority of affordable units and not more than 50 total units, operated as primary residences in which a majority ownership interest is held by the individual, the spouse of the individual, or the dependent children of the individual, or any closely held legal entity controlled by the individual, the spouse of the individual, or the dependent children of the individual, either individually or collectively; and\n**(B)**\nwho agrees to the provisions described in subsection (b)(3).\n**(5) Eligible rental property**\nThe term eligible rental property means a residential property that\u2014\n**(A)**\nis leased, or offered exclusively for lease, as a primary residence by an eligible landlord; and\n**(B)**\nincludes affordable units.\n**(6) Forgivable loan**\nThe term forgivable loan means a loan\u2014\n**(A)**\nmade to an eligible landlord;\n**(B)**\nthat is secured by a lien recorded against a residential property; and\n**(C)**\nthat may be forgiven by the implementing organization not later than the date that is 3 years after the completion of the repairs if the eligible landlord has maintained compliance with the loan agreement described in subsection (b)(3).\n**(7) Implementing organization**\nThe term implementing organization \u2014\n**(A)**\nmeans a unit of general local government or a State that\u2014\n**(i)**\nwill administer a whole-home repairs program through an agency, department, or other entity; or\n**(ii)**\nenter into agreements with 1 or more local governments, municipal authorities, other governmental authorities, including a tribally designated housing entity, or qualified nonprofit organizations, to administer a whole-home repairs program as a subrecipient; and\n**(B)**\ndoes not include a redundant entity in a jurisdiction already served by a grantee under subsection (b).\n**(8) Indian Tribe**\nThe term Indian tribe has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(9) Qualified nonprofit**\nThe term qualified nonprofit means a nonprofit organization that\u2014\n**(A)**\nhas received funding, as a recipient or subrecipient, through\u2014\n**(i)**\nthe Community Development Block Grant program under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. );\n**(ii)**\nthe HOME Investment Partnerships program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. );\n**(iii)**\nthe Lead-Based Paint Hazard Reduction grant program under section 1011 of the Residential Lead-Based Paint Hazard Reduction Act of 1992 ( 42 U.S.C. 4852 ) or a grant under the Healthy Homes Initiative administered by the Secretary pursuant to sections 501 and 502 of the Housing and Urban Development Act of 1970 ( 12 U.S.C. 1701z\u20131 , 1701z\u20132);\n**(iv)**\nthe Self-Help and Assisted Homeownership Opportunity program authorized under section 11 of the Housing Opportunity Program Extension Act of 1996 ( 42 U.S.C. 12805 note);\n**(v)**\na rural housing program under title V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. ); or\n**(vi)**\nthe Neighborhood Reinvestment Corporation established under the Neighborhood Reinvestment Corporation Act ( 42 U.S.C. 8101 et seq. );\n**(B)**\nhas coordinated, performed, or otherwise been engaged in weatherization, lead remediation, or home-repair work for not less than 2 years;\n**(C)**\nhas been certified by the Environmental Protection Agency, or by a State authorized by the Environmental Protection Agency to administer a certification program, as\u2014\n**(i)**\neligible to carry out activities under the lead renovation, repair and painting program; or\n**(ii)**\na Home Certification Organization under the Energy Star program established by section 324A of the Energy Policy and Conservation Act ( 42 U.S.C. 6294a ) or the WaterSense program under section 324B of that Act ( 42 U.S.C. 6294b ), or recognized or otherwise approved by the Environmental Protection Agency as a Home Certification Organization under either of those programs; or\n**(D)**\nis a community development financial institution, as defined in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 ).\n**(10) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(11) Specified program**\nFor purposes of paragraph (3)(A)(ii), the term specified program means any of the following:\n**(A)**\nThe Medicaid program established under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).\n**(B)**\nThe State Children's Health Insurance Program established under title XXI of the Social Security Act ( 42 U.S.C. 1397aa et seq. ).\n**(C)**\nThe supplemental security income benefits program established under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ).\n**(D)**\nThe supplemental nutrition assistance program established under the Food and Nutrition Act of 2008 ( 7 U.S.C. 2011 et seq. ).\n**(E)**\nThe temporary assistance for needy families program established under part A of title IV of the Social Security Act ( 42 U.S.C. 601 et seq. ).\n**(12) State**\nThe term State means\u2014\n**(A)**\neach State of the United States;\n**(B)**\nthe District of Columbia;\n**(C)**\nthe Commonwealth of Puerto Rico;\n**(D)**\nany territory or possession of the United States; and\n**(E)**\nan Indian tribe.\n**(13) Tribally designated housing entity**\nThe term tribally designated housing entity has the meaning given the term in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(14) Whole-home repairs**\nThe term whole-home repairs means modifications, repairs, or updates to homeowner or renter-occupied units to address\u2014\n**(A)**\nphysical and sensory accessibility for individuals with disabilities and older adults, such as bathroom and kitchen modifications, installation of grab bars and handrails, guards and guardrails, lifting devices, ramp additions or repairs, sidewalk addition or repair, or doorway or hallway widening;\n**(B)**\nhabitability and safety concerns, such as repairs needed to ensure residential units are fit for human habitation and free from defective conditions or health and safety hazards; or\n**(C)**\nenergy and water efficiency, resilience, and weatherization.\n##### (b) Pilot program\n**(1) Establishment**\nNot later than 1 year after the date of enactment of this Act, the Secretary shall establish a pilot program to provide grants to implementing organizations to administer a whole-home repairs program for eligible homeowners and eligible landlords.\n**(2) Use of funds**\nAn implementing organization that receives a grant under this subsection\u2014\n**(A)**\nshall provide grants to eligible homeowners to implement whole-home repairs not covered by other Federal home repair programs and up to a maximum amount per unit, which maximum amount should\u2014\n**(i)**\nreflect local construction costs and the level of repairs needed in each unit; and\n**(ii)**\nbe calculated and approved by the Secretary;\n**(B)**\nshall provide loans, which may be forgivable, to eligible landlords to implement whole-home repairs not covered by other Federal home repair programs for individual affordable units, public and common use areas within the property, and common structural elements up to a maximum amount per unit, area, or element, as applicable, which maximum amount should\u2014\n**(i)**\nreflect local construction costs; and\n**(ii)**\nbe calculated and approved by the Secretary;\n**(C)**\nshall evaluate, or provide assistance to eligible homeowners and eligible landlords to evaluate, whole-home repair program funds provided under this subsection with Federal, State, and local home repair programs to provide the greatest benefit to the greatest number of eligible landlords and eligible homeowners and avoid duplication of benefits and redundancies;\n**(D)**\nshall ensure that\u2014\n**(i)**\nall repairs funded or facilitated through an award under this subsection have been completed;\n**(ii)**\nif repairs are not completed and the plan for whole-home repairs is not updated to reflect the new scope of work, that the loan or grant is repaid on a prorated basis based on completed work; and\n**(iii)**\nany unused grant or loan balance is returned to the implementing organization, and is reused by the implementing organization for a new whole-home repair grant or loan under this subsection;\n**(E)**\nmay use not more than 5 percent of the awarded funds to carry out related functions, including workforce training for home repair professions, which shall be related to efforts to increase the number of home repairs performed and approved by the Secretary;\n**(F)**\nmay use not more than 10 percent of the awarded funds for administrative expenses; and\n**(G)**\nshall comply with Federal accessibility requirements and standards under applicable Federal fair housing and civil rights laws and regulations, including section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ).\n**(3) Loan agreement**\nIn a loan agreement with an eligible landlord under this subsection, an implementing organization shall include provisions establishing that the eligible landlord shall, for each eligible rental property for which a loan is used to fund repairs under this subsection\u2014\n**(A)**\ncomply with Federal accessibility requirements and standards under applicable Federal fair housing and civil rights laws and regulations, including section 504 of the Rehabilitation Act of 1973 ( 29 U.S.C. 794 ); and\n**(B)**\n**(i)**\nif the landlord is renting the assisted units available in the eligible rental property to tenants receiving tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ), under another tenant-based rental assistance program administered by the Secretary or the Secretary of Agriculture, or under a tenant-based rental subsidy provided by a State or local government, comply with the program requirements under the relevant tenant-based rental assistance program; or\n**(ii)**\nif the eligible landlord is not renting to tenants receiving rental-based assistance as described in clause (i)\u2014\n**(I)**\n**(aa)**\noffer to extend the lease of current tenants on current terms, other than the terms described in subclause (iv) for not less than 3 years beginning after the completion of the repairs, unless the lease is terminated due to failure to pay rent, performance of an illegal act within the rental unit, or a violation of an obligation of tenancy that the tenants failed to correct after notice; and\n**(bb)**\nif the tenant of an assisted unit moves out of the assisted unit at any point in the 3-year period following the loan agreement, maintain the unit as an affordable unit for the remainder of the 3-year period;\n**(II)**\nprovide documentation verifying that the property, upon completion of approved renovations, has met all applicable State and local housing and building codes;\n**(III)**\nattest that the landlord has no known serious violations of renter protections that have resulted in fines, penalties, or judgments during the preceding 10 years; and\n**(IV)**\ncap annual rent increases for each assisted unit at 5 percent of base rent or inflation, whichever is lower, for not less than 3 years beginning after the completion of the repairs.\n**(4) Application**\n**(A) In general**\nAn implementing organization desiring an award under this subsection shall submit to the Secretary an application that includes\u2014\n**(i)**\nthe geographic scope of the whole-home repairs program to be administered by the implementing organization, including the plan to address need in any rural, suburban, or urban area within a jurisdiction;\n**(ii)**\na plan for selecting subrecipients, if applicable;\n**(iii)**\nhow the implementing organization plans to execute the coordination of Federal, State, and local home repair programs, including programs administered by the Department of Energy or the Department of Agriculture, to increase efficiency and reduce redundancy;\n**(iv)**\navailable data on the need for affordable and quality housing within the geographic scope of the whole-home repairs program, and any plans to preserve affordability through the term of the award;\n**(v)**\nhow the implementing organization plans to process and verify applications for grants from eligible homeowners and applications for loans from eligible landlords; and\n**(vi)**\nsuch other information as the Secretary requires to determine the ability of an applicant to carry out a program under this subsection.\n**(B) Considerations**\nIn making awards under this subsection, the Secretary shall\u2014\n**(i)**\nwith respect to applications submitted by States other than the District of Columbia and the territories of the United States, prioritize those applications with a demonstrated plan to\u2014\n**(I)**\nmake a good faith effort to implement the pilot program in every jurisdiction; and\n**(II)**\nprovide non-metropolitan areas, or subrecipients serving non-metropolitan areas if applicable, with a share of total funds commensurate to their population;\n**(ii)**\naim to select applicants so that the awardees collectively span diverse geographies, with an intent to understand the impact of the pilot program under this subsection in urban, suburban, rural, and Tribal settings; and\n**(iii)**\nnot disqualify implementing organizations that were awarded grants under the pilot program in prior application cycles.\n**(5) Program information**\nThe Secretary shall make available to grant recipients under this subsection information regarding existing Federal programs for which grant recipients may coordinate or provide assistance in coordinating applications for those programs in accordance with paragraph (2)(C).\n**(6) Grant number**\nIn each year in which an award is made under this subsection, the Secretary shall award assistance to\u2014\n**(A)**\nnot less than 2, and not more than 10, implementing organizations, as application numbers and funding permit; and\n**(B)**\nnot more than 1 implementing organization in any State.\n**(7) Loans that are not forgiven**\nIf a loan made by an implementing organization under paragraph (2)(B) is not forgiven, the loan repayment funds shall be reused by the implementing organization for a new whole-home repair grant or loan under this subsection.\n**(8) Supplement, not supplant**\nAmounts awarded under this subsection to implementing organizations shall supplement, not supplant, other Federal, State, and local funds made available to those entities.\n**(9) Streamlining program delivery and ensuring efficiency**\nTo the extent possible, in carrying out the pilot program under this subsection, the Secretary shall\u2014\n**(A)**\nendeavor to improve efficiency of service delivery, as well as the experience of and impact on the taxpayer, by encouraging programmatic collaboration and information sharing across Federal, State, and local programs for home repair or improvement, including programs administered by the Department of Agriculture; and\n**(B)**\nenhance collaboration and cross-agency streamlining efforts that reduce the burdens of multiple income verification processes and applications on the eligible homeowner, the eligible landlord, the implementing organization, and the Federal Government, including by establishing assistance application procedures for income eligibility under this subsection that recognize income eligibility determinations for assistance using any of the criteria under subsection (a)(3)(A) that have been used for assistance applications during the 1-year period preceding the date on which an eligible homeowner or eligible landlord applies for assistance under this subsection.\n**(10) Reporting requirements**\n**(A) Annual report**\nAn implementing organization that receives a grant under this subsection shall submit to the Secretary an annual report on initial funding that includes\u2014\n**(i)**\nthe number of units served, including reporting on both homeownership and rental units, as well as accessible units;\n**(ii)**\nthe average cost per unit for modifications or repairs and the nature of those modifications or repairs, including reporting on accessibility and both homeownership and rental units;\n**(iii)**\nthe number of applications received, served, denied, or not completed, disaggregated by geographic area;\n**(iv)**\nthe aggregated demographic data of grant recipients, which may include data on income range, urban, suburban, and rural residency, age, and racial and ethnic identity;\n**(v)**\nthe aggregated demographic data of loan recipients, which may include data on income range, urban, suburban, and rural residency, age, and racial and ethnic identity;\n**(vi)**\nan affirmation that the implementation organization has complied with the applicable regulations, including compliance with Federal accessibility requirements;\n**(vii)**\nin the first year of receiving a grant, and as certified in subsequent reports, a comprehensive plan to prevent waste, fraud, and abuse in the administration of the pilot program, which shall include, at a minimum\u2014\n**(I)**\na policy enacted and enforced by the implementing organization to monitor ongoing expenditures under this subsection and ensure compliance with applicable regulations;\n**(II)**\na policy enacted and enforced by the implementing organization to detect and deter fraudulent activity, including fraud occurring in individual projects and patterns of fraud by parties involved in the expenditure of funds under this subsection;\n**(III)**\na statement setting forth any violations detected by the implementing organization during the previous calendar year, including details about steps taken to achieve compliance and any remedial measures; and\n**(IV)**\na certification by the chief executive or most senior compliance officer of the organization that the organization maintains sufficient staff and resources to effectively carry out the above-mentioned policies; and\n**(viii)**\nsuch other information as the Secretary may require.\n**(B) Reporting requirement alignment**\nTo limit the costs of implementing the pilot program under this subsection, the Secretary shall endeavor, to the extent possible, to structure reporting requirements such that they align with the data reporting requirements in place for funding streams that implementing organizations are likely to use in partnership with funding from this subsection, including the reporting requirements under\u2014\n**(i)**\nthe Community Development Block Grant program under title I of the Housing and Community Development Act of 1974 ( 42 U.S.C. 5301 et seq. );\n**(ii)**\nthe HOME Investment Partnerships program under subtitle A of title II of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12741 et seq. );\n**(iii)**\nthe Weatherization Assistance Program for low-income persons established under part A of title IV of the Energy Conservation and Production Act ( 42 U.S.C. 6861 et seq. ); and\n**(iv)**\nthe Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4101 et seq. ).\n**(C) Pilot program period reports**\nNot less frequently than twice during the period in which the pilot program established under this subsection operates, the Office of Inspector General of the Department of Housing and Urban Development shall complete an assessment of the implementation of measures to ensure the fair and legitimate use of the pilot program.\n**(D) Summary to Congress**\nThe Secretary shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives an annual report providing a summary of the data provided under subparagraphs (A) and (C) during the 1-year period preceding the report and all data previously provided under those subparagraphs.\n**(11) Funding**\nThe Secretary\u2014\n**(A)**\nis authorized to use up to $30,000,000 of funds made available as provided in appropriations Acts for programs administered by the Office of Lead Hazard Control and Healthy Homes to carry out the pilot program under this subsection; and\n**(B)**\nshall submit to the Committee on Appropriations and the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Appropriations and the Committee on Financial Services of the House of Representatives a report on the appropriations accounts from which the Secretary will derive the funding under subparagraph (A).\n**(12) Environmental review**\nA grant under this subsection shall be\u2014\n**(A)**\ntreated as assistance for a special project for purposes of section 305(c) of the Multifamily Housing Property Disposition Reform Act of 1994 ( 42 U.S.C. 3547 ); and\n**(B)**\nsubject to the regulations promulgated by the Secretary to implement such section.\n**(13) Termination**\nThe pilot program established under this subsection shall terminate on October 1, 2031.",
      "versionDate": "2025-11-07",
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
        "actionDate": "2025-11-12",
        "actionTime": "12:10:52",
        "text": "Held at the desk."
      },
      "number": "2296",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "National Defense Authorization Act for Fiscal Year 2026",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-08-01",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 143."
      },
      "number": "2651",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "ROAD to Housing Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-11-19T13:21:14Z"
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
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5990ih.xml"
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
      "title": "Whole-Home Repairs Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-15T05:23:14Z"
    },
    {
      "title": "Whole-Home Repairs Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-15T05:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Housing and Urban Development to establish a pilot program to provide grants to implementing organizations to administer a whole-home repairs program for eligible homeowners and eligible landlords, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-15T05:18:14Z"
    }
  ]
}
```
