# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1477?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1477
- Title: Housing for All Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1477
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-05T21:46:13Z
- Update date including text: 2025-12-05T21:46:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1477",
    "number": "1477",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "P000145",
        "district": "",
        "firstName": "Alex",
        "fullName": "Sen. Padilla, Alex [D-CA]",
        "lastName": "Padilla",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Housing for All Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:46:13Z",
    "updateDateIncludingText": "2025-12-05T21:46:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T20:40:24Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NJ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "MA"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "HI"
    },
    {
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "CA"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "OR"
    },
    {
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-04-10",
      "state": "NM"
    },
    {
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2025-06-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1477is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1477\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Padilla (for himself, Mr. Booker , Mr. Heinrich , Ms. Hirono , Mr. Markey , Mr. Schatz , Mr. Schiff , Mr. Wyden , and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo address the homelessness and housing crises, to move toward the goal of providing for a home for all Americans, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Housing for All Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Addressing the housing shortage\nSec. 101. Housing Trust Fund.\nSec. 102. Section 202 supportive housing for the elderly program.\nSec. 103. Section 811 supportive housing for people with disabilities.\nSec. 104. HOME Investment Partnerships Program.\nSec. 105. Technical assistance for navigating Federal and State housing funding sources.\nSec. 106. Permanent authorization of United States Interagency Council on Homelessness and establishment of racial equity commission.\nTITLE II\u2014Addressing homelessness\nSec. 201. Expansion of housing choice voucher program.\nSec. 202. Project-based rental assistance.\nSec. 203. Emergency solutions grant program.\nSec. 204. Continuum of care grant program.\nSec. 205. Program administration, training, technical assistance, and capacity building.\nSec. 206. GAO report on eviction data.\nTITLE III\u2014Investing in innovative community-driven solutions\nSec. 301. Safe parking program grants.\nSec. 302. Hotel, motel, and commercial acquisitions and conversions to permanent housing.\nSec. 303. Eviction protection grant program.\nSec. 304. Mobile crisis intervention teams grants.\nSec. 305. Library consortium pilot grants.\nSec. 306. Report on inclusive transit-oriented development to enhance climate mitigation and disaster resiliency.\nSec. 307. Establishing an innovation pilot within the carbon reduction program.\nSec. 308. Making infill housing and other transportation efficiency projects eligible for RAISE grants.\nSec. 309. Homelessness and behavioral health care coordination.\n#### 2. Definitions\nIn this Act:\n**(1) At risk of homelessness**\nThe term at risk of homelessness has the meaning given the term in section 401 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360 ).\n**(2) Homeless; homeless person**\nThe terms homeless and homeless person have the meanings given those terms in section 103 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11302 ).\n**(3) Indian Tribe; tribally designated housing entity**\nThe terms Indian Tribe and tribally designated housing entity have the meanings given those terms in section 4 of the Native American Housing Assistance and Self-Determination Act of 1996 ( 25 U.S.C. 4103 ).\n**(4) Justice system-involved**\nThe term justice system-involved includes individuals who are or have been incarcerated or held in municipal, State, or Federal jails, prisons, juvenile facilities, or other types of detention facilities, who have been held in pre-trial or post-conviction detention, who have an arrest or conviction regardless of whether they were detained or incarcerated, who have been held in immigration detention, or, with respect to youth, who are or have been held in the custody of the Office of Refugee Resettlement of the Department of Health and Human Services.\n**(5) Population at higher risk of homelessness**\n**(A) In general**\nThe term population at higher risk of homelessness means a group of individuals that is defined by a common characteristic and that has been found to experience homelessness, housing instability, or to be cost-burdened at a rate higher than that of the general public.\n**(B) Higher rate**\nInformation that may be used in demonstrating such a higher rate includes data generated by the Federal Government, by State or municipal governments, by peer-reviewed research, and by organizations having expertise in working with or advocating on behalf of homeless, housing unstable, or cost-burdened groups.\n**(C) Included populations**\nSuch term shall include populations for which such higher rate has already been demonstrated, including Asian, Black, Latino, Native American, Native Hawaiian, Pacific Islander and other communities of color, individuals with disabilities, including mental health disabilities, elderly individuals, foster and former foster youth, lesbian, gay, bisexual, transgender, and queer individuals, gender non-binary and gender non-conforming individuals, veterans, and such additional communities and individuals as the Secretary may include after receiving public comment.\n**(6) Public housing agency**\nThe term public housing agency has the meaning given the term in section 3(b)(6) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(6) ).\n**(7) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\nI\nAddressing the housing shortage\n#### 101. Housing Trust Fund\nSection 1338(a) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568(a) ) is amended by adding at the end the following:\n(3) Authorization of appropriations There is authorized to be appropriated to the Housing Trust Fund $45,000,000,000 for each of fiscal years 2025 through 2034. .\n#### 102. Section 202 supportive housing for the elderly program\nThere is authorized to be appropriated to the Secretary for fiscal year 2025, to remain available until September 30, 2034\u2014\n**(1)**\n$2,500,000,000 for the supportive housing for the elderly program authorized under section 202 of the Housing Act of 1959 ( 12 U.S.C. 1701q ), which shall be used\u2014\n**(A)**\nfor capital advance awards in accordance with section 202(c)(1) of the Housing Act of 1959 ( 12 U.S.C. 1701q(c)(1) ) to recipients that are eligible under that Act;\n**(B)**\nfor section 8 project-based rental assistance contracts in accordance with section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), for capital advance projects; and\n**(C)**\nfor service coordinators;\n**(2)**\n$15,000,000, to provide technical assistance to support State-level efforts to improve the design and delivery of voluntary supportive services for residents of any housing assisted under the Housing Act of 1959 ( Public Law 101\u2013625 ) and other housing supporting low-income older adults; and\n**(3)**\n$125,000,000 for the costs to the Secretary of administration and oversight.\n#### 103. Section 811 supportive housing for people with disabilities\nThere is authorized to be appropriated to the Secretary for fiscal year 2025, to remain available until September 30, 2034\u2014\n**(1)**\n$900,000,000 for capital advances, including amendments to capital advance contracts, for supportive housing for persons with disabilities, as authorized by section 811 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 8013 ), for project rental assistance for supportive housing for persons with disabilities under subsection (d)(2) of such section 811 ( 42 U.S.C. 8013 ), for project assistance contracts pursuant to section 202(h) of the Housing Act of 1959 ( 12 U.S.C. 1701q(h) ), and for project rental assistance to State housing finance agencies and other appropriate entities as authorized under subsection (b)(3) of such section 811 ( 42 U.S.C. 8013 );\n**(2)**\n$15,000,000 for providing technical assistance to support State-level efforts to integrate housing assistance and voluntary supportive services for residents of housing receiving such assistance; and\n**(3)**\n$87,000,000 for the costs to the Secretary of administration and oversight.\n#### 104. HOME Investment Partnerships Program\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary for fiscal year 2025, to remain available until September 30, 2034\u2014\n**(1)**\n$40,000,000,000, for activities and assistance for the HOME Investment Partnerships Program (in this section referred to as the HOME program ), as authorized under title II of the Cranston-Gonzalez National Affordable Housing Act (42 U.S. 12721 et seq.);\n**(2)**\n$100,000,000 to make new awards to or increase prior awards to existing technical assistance providers, including for technical assistance to grantees regarding best practices for coordination of available funds provided under this section with other forms of assistance, such as with project-based rental assistance; and\n**(3)**\n$360,000,000 for the costs to the Secretary of administration and oversight of the HOME program and the Housing Trust Fund established under section 1338(a) of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568(a) ).\n##### (b) Administration\nNotwithstanding subsections (c) and (d)(1) of section 212 of the Cranston-Gonzalez National Affordable Housing Act ( 42 U.S.C. 12742 ), eligible grantees may use not more than 15 percent of their allocations under this section for administrative and planning costs.\n#### 105. Technical assistance for navigating Federal and State housing funding sources\n##### (a) Establishment\nThe Secretary shall establish a grant program to provide technical assistance to States relating to the understanding of the relationship between Federal and State housing funding sources and how to best use those sources to finance housing projects in the State, such as permanent supportive housing, including resources, tools, and products that\u2014\n**(1)**\nprovide assistance on coordinating a single application for multiple funding sources;\n**(2)**\nprovide assistance on consolidating funding sources and implementing reporting requirements at the State level; and\n**(3)**\nsupport staff capacity within State housing finance agencies to maintain the collaborations and systems necessary to better align types of funding with need and expand access to housing stability.\n##### (b) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary such sums as may be necessary, to remain available until expended, to carry out this section.\n#### 106. Permanent authorization of United States Interagency Council on Homelessness and establishment of racial equity commission\nTitle II of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11311 et seq. ) is amended\u2014\n**(1)**\nin section 208 ( 42 U.S.C. 11318 ), by striking the first sentence and inserting the following: There is authorized to be appropriated for each fiscal year $10,000,000 to carry out this title. ; and\n**(2)**\nby striking section 209 ( 42 U.S.C. 11319 ) and inserting the following:\n209. Racial equity commission (a) Establishment of commission (1) In general There is established a commission to be known as the Commission on Racial Equity in Housing (in this section referred to as the Commission ) to support the Council with efforts to conduct research into, collect, analyze, and make publicly available data on, and provide leadership and coordination for furthering racial equity in housing, examining the impacts of structural racism on housing and homelessness, and the effectiveness of intervention strategies to address these impacts. (2) Reporting The Commission shall report to the Executive Director of the Council and work in partnership with employees of the Council. (b) Membership (1) Composition The Commission shall be composed of 14 members, who shall be\u2014 (A) appointed by the Executive Director of the Council not later than January 1, 2026; and (B) fairly balanced in terms of points of view represented and background experience. (2) Qualifications Each member of the Commission shall have\u2014 (A) proven expertise in directing, assembling, or applying capital resources from a variety of sources to the successful development of affordable housing, assisted living facilities, or health care facilities; (B) lived experience with homelessness; or (C) demonstrated experience in\u2014 (i) homeless services, affordable housing, or housing law; and (ii) racial equity work. (3) Co-chairpersons The Executive Director shall appoint 2 co-chairpersons of the Commission from among the members of the Commission. (4) Vacancies Any vacancy on the Commission shall not affect its powers and shall be filled in the manner in which the original appointment was made. (5) Prohibition of pay Members of the Commission shall serve without pay. (6) Travel expenses Each member of the Commission shall receive travel expenses, including per diem in lieu of subsistence, in accordance with sections 5702 and 5703 of title 5, United States Code. (7) Quorum A majority of the members of the Commission shall constitute a quorum but a lesser number may hold hearings. (8) Meetings The Commission shall meet at the call of the co-chairpersons of the Commission. (c) Director and staff (1) Director The Commission shall have a Director who shall be\u2014 (A) appointed by the co-chairpersons of the Commission; and (B) paid at a rate not to exceed the rate of basic pay payable for level V of the Executive Schedule under section 5316 of title 5, United States Code. (2) Staff The Commission may appoint personnel as appropriate subject to the provisions of title 5, United States Code, governing appointments in the competitive service, and who shall be paid in accordance with the provisions of chapter 51 and subchapter III of chapter 53 of that title relating to classification and General Schedule pay rates. (3) Experts and consultants The Council may procure temporary and intermittent services to support the work of the Commission under section 3109(b) of title 5, United States Code, but at rates for individuals not to exceed the daily equivalent of the maximum annual rate of basic pay payable for the General Schedule. (4) Staff of Federal agencies Upon request of the Council and the Commission, the head of any Federal department or agency may detail, on a reimbursable basis, any of the personnel of that department or agency to the Commission to assist it in carrying out its duties under this section. (d) Duties The Commission shall\u2014 (1) work with the Council to make recommendations, inform, and participate in efforts to conduct research into, collect, analyze, and make publicly available data on, and provide leadership and coordination for furthering racial equity in housing, examining the impacts of structural racism on housing and homelessness, and the effectiveness of intervention strategies to address these impacts; and (2) work with the Council to implement the Federal Strategic Plan to Prevent and End Homelessness. (e) Reports The Council shall submit to Congress, the Secretary of Housing and Urban Development, the Secretary of Health and Human Services, the Secretary of Transportation, the Secretary of Education, the Secretary of Labor, the Secretary of Defense, the Secretary of Agriculture, the Secretary of Veterans Affairs, the Secretary of the Treasury, the Attorney General, the Secretary of the Interior, the Chair of the Federal Reserve, the Comptroller of the Currency, the Director of the Office of Thrift Supervision, the Chair of the Federal Deposit Insurance Corporation, and such other individuals as the Commission determines relevant an annual report on research findings with recommendations to improve racial equity in housing and to disrupt processes that preserve and reinforce racism and racial disparities in housing and homelessness services. (f) Termination Section 1013 of title 5, United States Code, shall not apply to the Commission. (g) Authorization of appropriations There is authorized to be appropriated such sums as may be necessary to carry out this section. .\nII\nAddressing homelessness\n#### 201. Expansion of housing choice voucher program\n##### (a) Definitions\nIn this section:\n**(1) Eligible household**\nThe term eligible household means a family who initially\u2014\n**(A)**\nhas an income that does not exceed 50 percent of the maximum income limitation for extremely low-income families established by the Secretary pursuant to section 3(b)(2)(C) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b)(2)(C) ); or\n**(B)**\nis an extremely low-income family that includes an individual who is an individual who is a recipient of supplemental security income benefits under title XVI of the Social Security Act ( 42 U.S.C. 1381 et seq. ).\n**(2) Extremely low-income family; State**\nThe terms extremely low-income family and State have the meanings given those terms in section 3(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437a(b) ).\n##### (b) Expanded vouchers\n**(1) Funding**\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, for providing incremental vouchers for rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) in accordance with this section for each of fiscal years 2025 through 2028, the amount necessary to fund\u2014\n**(A)**\nthe number of incremental vouchers required to be allocated under paragraph (2);\n**(B)**\nannual renewals of the vouchers allocated under paragraph (2); and\n**(C)**\nadministrative fees for vouchers allocated under paragraph (2).\n**(2) Allocation**\n**(A) Incremental vouchers**\nThe Secretary shall allocate 500,000 incremental vouchers in fiscal year 2025 and 1,000,000 incremental vouchers in increments of 500,000 in each calendar year from 2026 through 2028 under this section to public housing agencies pursuant to section 213(d) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 1439(d) ).\n**(B) Selection criteria**\nThe Secretary shall, by notice in the Federal Register, establish selection criteria under section 213(d) of the Housing and Community Development Act of 1974 ( 42 U.S.C. 1439(d) ) that prioritizes housing needs among eligible households and severe housing hardship, such as experiencing homelessness, overcrowding, or evictions.\n##### (c) Entitlement to vouchers\n**(1) In general**\nOn and after the date that is 5 years after the date of enactment of this Act, any family that is otherwise eligible for tenant-based rental assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) shall be entitled to that rental assistance during any period that the family is an eligible household.\n**(2) Funding**\nThere is appropriated, out of any money in the Treasury not otherwise appropriated, such sums as may be necessary\u2014\n**(A)**\nto provide assistance under section 8(o) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(o) ) in accordance with the entitlement under paragraph (1) of this subsection for each eligible household in the amount determined under such section 8(o); and\n**(B)**\nto provide administrative fees under section 8(q) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(q) ) in connection with each voucher for assistance provided pursuant to subparagraph (A) of this paragraph.\n#### 202. Project-based rental assistance\n##### (a) Authorization of appropriations\nIn addition to amounts otherwise available, there is authorized to be appropriated to the Secretary for fiscal year 2025, to remain available until September 30, 2034\u2014\n**(1)**\n$14,500,000,000 for the project-based rental assistance program, as authorized under section 8(b) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(b) ), subject to the terms and conditions of subsection (b) of this section;\n**(2)**\n$40,000,000 for providing technical assistance to recipients of or applicants for project-based rental assistance or to States allocating the project-based rental assistance; and\n**(3)**\n$200,000,000 for the costs to the Secretary of administration and oversight.\n##### (b) Terms and conditions\n**(1) Authority**\nNotwithstanding section 8(a) of the United States Housing Act of 1937 ( 42 U.S.C. 1437f(a) ), the Secretary may use amounts made available under this section\u2014\n**(A)**\nto provide assistance payments with respect to newly constructed housing, existing housing, or substantially rehabilitated non-housing structures for use as new multifamily housing in accordance with this section and the provisions of section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ); and\n**(B)**\nfor performance-based contract administrators for project-based assistance under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), for carrying out this section and section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ).\n**(2) Project-based rental assistance**\n**(A) In general**\nThe Secretary may make assistance payments using amounts made available under this section pursuant to contracts with owners or prospective owners who agree to construct housing, to substantially rehabilitate existing housing, to substantially rehabilitate non-housing structures for use as new multifamily housing, or to attach the assistance to newly constructed housing in which some or all of the units shall be available for occupancy by very low-income families in accordance with the provisions of section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ), under terms determined by the Secretary.\n**(B) Priority**\nIn awarding contracts pursuant to this section, the Secretary shall give priority to owners or prospective owners of multifamily housing projects located or to be located in areas of high opportunity, as defined by the Secretary, in areas experiencing economic growth or rising housing prices to prevent displacement or secure affordable housing for low-income households, or that serve people at risk of homelessness or that integrate additional units that are accessible for persons with mobility impairments and persons with hearing or visual impairments beyond those required by applicable Federal accessibility standards.\n#### 203. Emergency solutions grant program\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary for fiscal year 2025 $5,000,000,000, to remain available until September 30, 2034, to make grants under the emergency solutions grant program authorized under subtitle B of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11371 et seq. ).\n##### (b) Maximum allocation for emergency shelter activities\nA recipient of a grant using amounts appropriated under subsection (a) in any fiscal year may not use an amount of the assistance for emergency shelter activities that exceeds the greater of\u2014\n**(1)**\n40 percent of the aggregate amount of that assistance provided for the grantee for that fiscal year; or\n**(2)**\nthe amount expended by the grantee for emergency shelter activities during fiscal year 2010.\n#### 204. Continuum of care grant program\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary for fiscal year 2025 $15,000,000,000, to remain available until the end of fiscal year 2034, to make grants under the Continuum of Care Program authorized under subtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ).\n##### (b) Minimum allocation for permanent housing for homeless individuals and families with disabilities\nOf amounts appropriated under subsection (a) for a fiscal year, not less than 50 percent shall be used for permanent housing for homeless individuals with disabilities and homeless families that include such an individual who is an adult or a minor head of household if no adult is present in the household.\n##### (c) Prioritization of continuum of care\nIn awarding grants using amounts appropriated under subsection (a), the Secretary shall prioritize funding for applicants that provide documentation of coordination with certain systems serving young people and can answer questions regarding how the applicant works with child welfare organizations, the juvenile and adult justice system, and institutions of mental and physical health to ensure that participants in the programs are not released into homelessness.\n#### 205. Program administration, training, technical assistance, and capacity building\nIn addition to amounts otherwise available, there is authorized to be appropriated for fiscal year 2025, to remain available until expended\u2014\n**(1)**\n$1,000,000,000 to the Secretary for the costs to the Secretary of administering and overseeing the implementation of this title and the programs of the Department of Housing and Urban Development generally and new awards or increasing prior awards to provide training, technical assistance, and capacity building related to the programs of the Department of Housing and Urban Development;\n**(2)**\n$5,000,000 to the United States Interagency Council on Homelessness for necessary expenses in carrying out the functions of the Council pursuant to title II of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11311 et seq. ); and\n**(3)**\n$10,000,000 to the Secretary for necessary salaries and expenses of the Office of the Inspector General of the Department of Housing and Urban Development in carrying out chapter 4 of title 5, United States Code.\n#### 206. GAO report on eviction data\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report that examines\u2014\n**(1)**\nwith respect to eviction moratoriums during the COVID\u201319 pandemic\u2014\n**(A)**\nhow eviction moratoriums have contributed to housing stability;\n**(B)**\nan analysis of formal and informal evictions during the periods in which the moratoriums were in effect; and\n**(C)**\nan economic analysis of how the eviction moratoriums saved public funds, such as by reducing shelter costs;\n**(2)**\nwhether women, Black, Hispanic, and other minority renters disproportionately faced eviction during the COVID\u201319 pandemic, and an accounting of the disproportionate risk of eviction faced by veterans, children, the elderly, and individuals living with disabilities during the COVID\u201319 pandemic;\n**(3)**\nthe barriers that exist to collecting the data related to paragraphs (1) and (2);\n**(4)**\nthe barriers that exist to collecting, digitizing, and standardizing data from the beginning to the end of the eviction process, such as pre-eviction information, the renter\u2019s race or ethnicity, age and gender, as well as the composition of the household and landlord data; and\n**(5)**\na study of the relationship between emergency rental assistance distribution and eviction patterns, as well as how emergency rental assistance affected evictions, during the periods in which the eviction moratoriums were in effect during the COVID\u201319 pandemic.\nIII\nInvesting in innovative community-driven solutions\n#### 301. Safe parking program grants\n##### (a) Definitions\nIn this section:\n**(1) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na unit of general purpose local government;\n**(B)**\nan Indian Tribe or a tribally designated housing entity;\n**(C)**\na nonprofit organization that provides services to homeless persons; or\n**(D)**\na collaborative applicant or other organization or entity funded under the Continuum of Care Program under subtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ).\n**(2) Essential service**\nThe term essential service means an essential service described in section 576.102 of title 24, Code of Federal Regulations, or any successor regulation.\n**(3) Safe parking program**\nThe term safe parking program means a program that\u2014\n**(A)**\nprovides a homeless person living in a vehicle, including a motor home, with a safe place to park the vehicle overnight to facilitate a transition to more stable housing; and\n**(B)**\nprovides permanent rehousing services and essential services.\n##### (b) Establishment of program\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish a grant program to provide amounts to eligible entities for costs associated with\u2014\n**(1)**\nthe establishment and operation of a new safe parking program; or\n**(2)**\nthe operation of a safe parking program in existence as of the date on which amounts are provided.\n##### (c) Grant term\nThe term of a grant awarded under subsection (b) shall be 5 years.\n##### (d) Amount\n**(1) In general**\nDuring the 5-year term of a grant awarded under subsection (b), the Secretary shall distribute 20 percent of the grant amounts each year.\n**(2) Cap**\nAn eligible entity may not receive more than $5,000,000 in grant amounts under subsection (b).\n##### (e) Applications\n**(1) In general**\nTo be eligible to receive a grant under subsection (b), an eligible entity shall submit an application to the Secretary at the time, in the manner, and containing the information that the Secretary requires, including a description of how the eligible entity will use any amounts received.\n**(2) Priority**\nThe Secretary shall give priority to applications from eligible entities that serve homeless persons in underserved areas (as defined in section 81.2 of title 24, Code of Federal Regulations, or any successor regulation).\n##### (f) Use of funds\nExcept as provided in subsection (h), any eligible entity that is awarded a grant under subsection (b) shall use the grant amounts for costs associated with\u2014\n**(1)**\nestablishing and operating a safe parking program;\n**(2)**\nproviding permanent rehousing assistance to families using the safe parking program, such as case management services;\n**(3)**\nemploying staff who maintain the safety and health of participants in the safe parking program and monitor program compliance with subtitle C of title IV of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11381 et seq. ), if applicable;\n**(4)**\nestablishing and maintaining the operation of hygiene facilities and restrooms for homeless persons;\n**(5)**\nmaintaining the vehicles of homeless persons using a safe parking program and providing gas for those persons to use their vehicles for activities that will help them obtain or maintain housing, including\u2014\n**(A)**\ndriving to work, school, or medical appointments; and\n**(B)**\nsearching for a home; or\n**(6)**\nentering data and information into a homeless management information system (as that term is used in section 402(f)(3) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360a(f)(3) )).\n##### (g) Multiple locations\nAn eligible entity may use amounts provided under subsection (b) to establish or continue operating a safe parking program at multiple locations.\n##### (h) Alternative use of funds\nIf an eligible entity determines that a safe parking program is no longer necessary, the eligible entity may, after approval from the Secretary, use amounts provided under subsection (b) for activities that are eligible for the use of Emergency Solutions Grants Program amounts under section 415 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11374 ).\n##### (i) Rehousing and case management services\nA homeless person who makes use of a safe parking program established or operated using amounts awarded under subsection (b) shall not be required to accept case management or rehousing services offered as part of the program.\n##### (j) Reports to Congress\n**(1) Initial report**\nNot later than 180 days after the last day of the second fiscal year beginning after the date of enactment of this Act, the Secretary shall submit to Congress an initial report on the impact of grants awarded under subsection (b), including, to the extent determinable, any data about\u2014\n**(A)**\nthe number of homeless persons living in vehicles in the geographic region over which the eligible entity has jurisdiction, or in which the eligible entity operates, during each of the 7 previous years;\n**(B)**\nthe demographics and number of homeless persons who choose to participate in a safe parking program; and\n**(C)**\nthe number of homeless persons who choose to participate in a safe parking program and exit into permanent housing.\n**(2) Final report**\nNot later than 180 days after the last day of the fifth fiscal year beginning after the date of enactment of this Act, the Secretary shall submit to Congress a final report on the impact of grants awarded under subsection (b), including, to the extent determinable, any data described in subparagraphs (A), (B), and (C) of paragraph (1) of this subsection.\n##### (k) Termination of grant program\nThe Secretary may not award a grant under subsection (b) after the last day of the fifth fiscal year beginning after the date of enactment of this Act.\n##### (l) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $25,000,000 for each of the first 5 fiscal years beginning after the date of enactment of this Act.\n#### 302. Hotel, motel, and commercial acquisitions and conversions to permanent housing\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary for fiscal year 2025, $500,000,000, to remain available until September 30, 2033, for\u2014\n**(1)**\nprojects related to the acquisition, rehabilitation, renovation, or conversion of transitional housing, temporary shelters, and other spaces, such as hotels, motels, government-owned properties, and commercial business spaces such as shopping malls, to address urgent safety and public health needs for individuals experiencing homelessness and housing instability, provided that the funds are used for non-congregate shelter or creating more permanent supportive housing; and\n**(2)**\nsupportive services for individuals housed in the spaces described in paragraph (1), including\u2014\n**(A)**\nactivities listed in section 401(29) of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11360(29) );\n**(B)**\nhousing counseling; and\n**(C)**\nhomeless prevention services.\n##### (b) Implementation\nThe Secretary shall have authority to issue such regulations or other notices, guidance, forms, instructions, and publications as may be necessary or appropriate to carry out the programs, projects, or activities authorized under this section, including to ensure that such programs, projects, or activities are completed in a timely and effective manner.\n#### 303. Eviction protection grant program\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary for fiscal year 2025, $800,000,000, to remain available until September 30, 2033, for an eviction protection grant program established by the Secretary to support experienced legal service providers in providing legal assistance at no cost to low-income tenants at risk of or subject to eviction.\n##### (b) Implementation\nThe Secretary shall have authority to issue such regulations or other notices, guidance, forms, instructions, and publications as may be necessary or appropriate to carry out the programs, projects, or activities authorized under this section, including to ensure that such programs, projects, or activities are completed in a timely and effective manner.\n#### 304. Mobile crisis intervention teams grants\n##### (a) Grant authorization\nThe Attorney General may make grants to States, units of local government, public and community defender systems, and nonprofit organizations to create or expand mobile crisis intervention teams to address homelessness and reduce recidivism.\n##### (b) Application\n**(1) In general**\nAn entity seeking a grant under this section shall submit to the Attorney General an application at such time, in such manner, and containing such information as the Attorney General may reasonably require, including an assurance described in paragraph (2).\n**(2) Assurance described**\nAn assurance described in this paragraph is an assurance that\u2014\n**(A)**\nthe entity has in place a policy protecting employees, individuals, and communities served by the entity from discrimination under applicable civil rights laws; and\n**(B)**\nthe policy described in subparagraph (A) includes protection from discrimination on the basis of gender-related identity, appearance, mannerisms, or other gender-related characteristics of an individual, regardless of the individual\u2019s designated sex at birth.\n**(3) Nonprofit expertise**\nIn addition to the assurance described in paragraph (2), a nonprofit organization seeking a grant under this section shall demonstrate in the application submitted under this subsection that the organization has a proven history of\u2014\n**(A)**\nsuccessful engagement with populations experiencing homelessness and housing instability, including members of a population at higher risk of homelessness; or\n**(B)**\nassisting communities to engage in alternatives to penalizing homelessness.\n##### (c) Use of funds\nAn entity that receives a grant under this section may use funds received under this section for creating, supporting, expanding, or studying mobile crisis intervention teams that are trained to provide stabilization services to individuals with an urgent medical or psychological need, as an alternative to a law enforcement response, which teams may include healthcare professionals, mental health professionals, addiction counselors, housing referral specialists, groups serving or representing justice system-involved or homeless individuals, and other related resource providers.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $50,000,000 for the first fiscal year beginning after the date of enactment of this Act and for each of the 9 succeeding fiscal years thereafter.\n#### 305. Library consortium pilot grants\nPart A of title V of the Public Health Service Act ( 42 U.S.C. 290aa et seq. ) is amended by adding at the end the following:\n506B. Library consortium pilot grants (a) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) an eligible library; (B) a library agency that is an official agency of a State or other unit of government and is charged by the law governing it with the extension and development of public library services within its jurisdiction; (C) an eligible library consortium; or (D) a library association that exists on a permanent basis, serves libraries or library professionals on a national, regional, State, or local level, and engages in activities designed to advance the well-being of libraries and the library profession. (2) Eligible library The term eligible library means\u2014 (A) a public library; (B) an elementary or secondary school library; (C) a library that is operated by an institution of higher education; (D) a research library or archive that is not an integral part of an institution of higher education and that makes publicly available library services and materials that are suitable for scholarly research and not otherwise available; or (E) a Tribal library. (3) Eligible library consortium The term eligible library consortium means a local, statewide, regional, interstate, or international cooperative association of library entities that provides for the systematic and effective coordination of the resources of eligible libraries, and information centers that work to improve the services delivered to the clientele of these libraries. (b) Grant program From amounts made available under this section for a fiscal year, the Assistant Secretary shall award grants, on a competitive basis, to eligible entities to enable those eligible entities to carry out pilot programs to address the needs of homeless individuals or individuals at risk of homelessness. (c) Use of funds (1) In general Each eligible entity receiving funds under this section may use such funds to provide programs or resources that address the needs of homeless individuals or individuals at risk of homelessness by\u2014 (A) connecting them with resources to help them transition to stable, independent or supported living, through the eligible entity\u2019s own activities or through subgrants to eligible libraries, as appropriate; (B) providing homeless individuals or individuals at risk of homelessness with programs on issues such as health, mortgage or rental assistance, and applying for government benefits; or (C) partnering with other community organizations or the locality\u2019s department of public health for outreach activities and connections to other relevant services. (2) Criteria for subgrants In awarding a subgrant under this section, an eligible entity shall\u2014 (A) require eligible libraries desiring a subgrant to submit an application containing\u2014 (i) the estimated number of homeless individuals or individuals at risk of homelessness that will be served under the homelessness-related programs to be funded by the subgrant; and (ii) any other criteria established by the grantee in the application submitted under subsection (d); and (B) give preference to eligible libraries that propose to carry out programs or develop resources that integrate existing Federal or State programs that serve homeless individuals or individuals at risk of homelessness. (d) Application An eligible entity desiring a grant under this section shall submit an application at such time, in such manner, and containing such information as the Assistant Secretary may require. Each application shall include\u2014 (1) a description of the homelessness-related programs or resources that the eligible entity will support (in accordance with subsection (c)(1)) either through its own activities or through subgrants to eligible libraries; (2) a description of how community or governmental partners will be involved in the homelessness-related programs or resources provided by the eligible entity; and (3) in the case of projects that the eligible entity intends to carry out through subgrants\u2014 (A) a description of how the eligible entity will make subgrants, including any priorities or considerations that will be applied in making such subgrants; (B) a description of how the eligible entity will disseminate, in a timely manner, information regarding the subgrants, and the application process for such subgrants; (C) a description of the criteria that the eligible entity will require for the programs carried out by subgrantees with funds awarded by that eligible entity; and (D) an assurance that each eligible library that receives a subgrant will use the funds from that subgrant to provide programs that primarily serve homeless individuals or individuals at risk of homelessness. (e) Consultation In carrying out this section, the Assistant Secretary\u2014 (1) shall consult with the Director of the Institute of Museum and Library Services and the Secretary of Housing and Urban Development; and (2) may consult with the Interagency Council on Homelessness or any other appropriate Federal agency or office to help ensure that funds are disbursed and utilized effectively. (f) Reports Each eligible entity receiving a grant under this section for a fiscal year shall prepare and submit a report to the Assistant Secretary, in such form and containing such information, as the Assistant Secretary may reasonably require to determine the extent to which funds provided under this section have been effective in carrying out the purposes of this section. (g) Authorization of appropriations There is authorized to be appropriated to carry out this section $10,000,000 for the first fiscal year beginning after the date of enactment of this section and for each of the 9 succeeding fiscal years thereafter. .\n#### 306. Report on inclusive transit-oriented development to enhance climate mitigation and disaster resiliency\nNot later than 180 days after the date of enactment of this Act, the Secretary shall submit to Congress a report on how to add a focus to housing programs of the Department of Housing and Urban Development on\u2014\n**(1)**\ninfill projects that better connect people to jobs and transit and reduce greenhouse gas emissions; and\n**(2)**\nsupporting developers and local governments constructing units on existing or underused urban land close to city amenities and transportation.\n#### 307. Establishing an innovation pilot within the carbon reduction program\nSection 175(c) of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (1), in the matter preceding subparagraph (A), by striking paragraph (2) and inserting paragraphs (2) and (3) ; and\n**(2)**\nby adding at the end the following:\n(3) Innovation pilot (A) In general In addition to eligible projects under paragraphs (1) and (2), funds apportioned to a State under section 104(b)(7) may be used for innovative strategies to reduce transportation emissions, including associated infrastructure improvements that will increase the share of nonmotorized trips and improve the efficiency of existing surface transportation infrastructure to address carbon reduction. (B) Notice Not later than 120 days after the date of enactment of this paragraph, the Secretary shall provide notice and guidance for interested entities to participate in activities under subparagraph (A). (C) Exclusion Funds used to carry out a project under subparagraph (A) may not be used on a project that increases net capacity for vehicular travel. .\n#### 308. Making infill housing and other transportation efficiency projects eligible for RAISE grants\nSection 6702(a)(3) of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (G), by striking and at the end;\n**(2)**\nby redesignating subparagraph (H) as subparagraph (I); and\n**(3)**\nby inserting after subparagraph (G) the following:\n(H) a project or series of projects to reduce transportation emissions, including associated infrastructure improvements to support infill development or transit-oriented development, and to increase nonmotorized trips, subject to the conditions that\u2014 (i) the project or series of projects shall directly improve the efficiency of existing surface transportation infrastructure; and (ii) the Federal share for the project or series of projects shall be used to fund only the elements of the project or series that provide public benefits; and .\n#### 309. Homelessness and behavioral health care coordination\n##### (a) Definitions\nIn this section:\n**(1) Behavioral health**\nThe term behavioral health includes mental health and substance use.\n**(2) Eligible entity**\nThe term eligible entity means an entity described in section 402(c)(4) that is eligible for a competitive grant under subsection (b).\n**(3) Person experiencing homelessness**\nThe term person experiencing homelessness has the same meaning as the terms homeless , homeless individual , and homeless person , as defined in section 103 of the McKinney-Vento Homeless Assistance Act ( 42 U.S.C. 11302 ).\n**(4) Substance use disorder**\nThe term substance use disorder means the disorder that occurs when the recurrent use of alcohol or drugs, or both, causes clinically significant impairment, including health problems, disability, and failure to meet major responsibilities at work, school, or home.\n**(5) Tribal organization**\nThe term Tribal organization \u2014\n**(A)**\nhas the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 3504 ); and\n**(B)**\nincludes entities that serve Native Hawaiians, as defined in section 338K(c) of the Public Health Service Act ( 42 U.S.C. 254s(c) ).\n##### (b) Establishment of grant program\nThe Secretary, in consultation with the working group established under subsection (c), shall establish a grant program to award competitive grants to eligible entities to build or increase the capacity of the eligible entity for the better coordination of health care and homelessness services for people\u2014\n**(1)**\nexperiencing homelessness and significant behavioral health issues, including substance use disorder; and\n**(2)**\nwho are voluntarily seeking assistance.\n##### (c) Working group\n**(1) Establishment**\nThe Secretary shall establish an interagency working group to provide advice to the Secretary in carrying out the program established under subsection (b).\n**(2) Composition**\nThe working group established under paragraph (1) shall include representatives from the Department of Housing and Urban Development, the United States Interagency Council on Homelessness, the Department of Health and Human Services, the Department of Agriculture, and Bureau of Indian Affairs, to be appointed by the heads of such agencies.\n**(3) Development of assistance tools**\nNot later than 1 year after the date of enactment of this Act, the working group established under paragraph (1) shall\u2014\n**(A)**\ndevelop training, tools, and other technical assistance materials that simplify homelessness services for providers of health care and simplify health care services for providers of homelessness services by identifying the basic elements the health and homelessness sectors need to understand about the other; and\n**(B)**\ncirculate the materials described in subparagraph (A) to interested entities, particularly eligible entities that apply for grants awarded pursuant to this section.\n##### (d) Capacity-Building grants\n**(1) In general**\nThe Secretary shall award 5-year grants to eligible entities, which shall be used only to build or increase capacities to coordinate health care and homelessness services.\n**(2) Prohibition**\nNone of the proceeds from the grants awarded pursuant to this subsection may be used to pay for\u2014\n**(A)**\nhealth care, with the exception of efforts to increase the availability of Naloxone and provide training for the administration of Naloxone; or\n**(B)**\nrent.\n**(3) Amount**\nThe amount awarded to an eligible entity under a grant under this subsection shall not exceed $500,000.\n**(4) Eligibility**\nTo be eligible to receive a grant under this subsection, an entity shall\u2014\n**(A)**\nbe\u2014\n**(i)**\na governmental entity at the county, city, regional, or locality level;\n**(ii)**\nan Indian Tribe, a tribally designated housing entity, a Tribal organization, or an urban Indian organization;\n**(iii)**\na public housing agency administering housing choice vouchers; or\n**(iv)**\na continuum of care or nonprofit organization designated by the continuum of care;\n**(B)**\nbe responsible for homelessness services;\n**(C)**\nprovide such assurances as the Secretary shall require that, in carrying out activities with amounts from the grant, the entity will ensure that services are culturally competent, meet the needs of the people being served, and follow trauma-informed best practices to address those needs using a harm reduction approach; and\n**(D)**\ndemonstrate how the capacity of the entity to coordinate health care and homelessness services to better serve people experiencing homelessness and significant behavioral health issues, including substance use disorder, can be increased through\u2014\n**(i)**\nthe designation of a governmental official as a coordinator for making connections between health and homelessness services and developing a strategy for using those services in a holistic way to help people experiencing homelessness and behavioral health conditions such as substance use disorder, including those with co-occurring conditions;\n**(ii)**\nimprovements in infrastructure at the systems level;\n**(iii)**\nimprovements in technology for voluntary remote monitoring capabilities, including internet and video, which can allow for more home- and community-based behavioral health care services and ensure such improvements maintain effective communication requirements for persons with disabilities and program access for persons with limited English proficiency;\n**(iv)**\nimprovements in connections to health care services delivered by providers experienced in behavioral health care and people experiencing homelessness;\n**(v)**\nefforts to increase the availability of Naloxone and provide training for the administration of Naloxone; and\n**(vi)**\nany additional activities identified by the Secretary that will advance the coordination of homelessness assistance, housing, and behavioral health care services and other health care services.\n**(5) Eligible activities**\nAn eligible entity receiving a grant under this subsection may use the grant to cover costs related to\u2014\n**(A)**\nhiring system coordinators; and\n**(B)**\nadministrative costs, including staffing costs, technology costs, and other such costs identified by the Secretary.\n**(6) Distribution of funds**\nAn eligible entity receiving a grant under this subsection may distribute all or a portion of the grant amounts to private nonprofit organizations, other government entities, public housing agencies, tribally designated housing entities, or other entities as determined by the Secretary to carry out programs and activities in accordance with this section.\n**(7) Oversight requirements**\n**(A) Annual reports**\nNot later than 6 years after the date on which grant amounts are first received by an eligible entity under this subsection, the eligible entity shall submit to the Secretary a report on the activities carried out under the grant, which shall include, with respect to activities carried out with grant amounts in the community served\u2014\n**(i)**\nmeasures of outcomes relating to whether people experiencing homelessness and significant behavioral health issues, including substance use disorder, who sought help from an entity that received a grant\u2014\n**(I)**\nwere housed and did not experience intermittent periods of homelessness;\n**(II)**\nwere voluntarily enrolled in treatment and recovery programs;\n**(III)**\nexperienced improvements in their health;\n**(IV)**\nobtained access to specific primary care providers; and\n**(V)**\nhave health care plans that meet their individual needs, including access to mental health and substance use disorder treatment and recovery services;\n**(ii)**\nhow grant funds were used; and\n**(iii)**\nany other matters determined appropriate by the Secretary.\n**(B) Rule of construction**\nNothing in this paragraph may be construed to condition the receipt of future housing and other services by individuals assisted with activities and services provided with grant amounts on the outcomes detailed in the reports submitted under this paragraph.\n##### (e) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $20,000,000 for each of fiscal years 2025 through 2030, of which not less than 5 percent of such funds shall be awarded to Indian Tribes, tribally designated housing entities, and Tribal organizations.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-17",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committees on the Judiciary, Energy and Commerce, and Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "2945",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Housing for All Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-05-20T13:38:21Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1477is.xml"
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
      "title": "Housing for All Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing for All Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-03T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to address the homelessness and housing crises, to move toward the goal of providing for a home for all Americans, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-03T03:18:21Z"
    }
  ]
}
```
