# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4957?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4957
- Title: Rural Housing Service Reform Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4957
- Origin chamber: House
- Introduced date: 2025-08-12
- Update date: 2026-05-20T08:07:54Z
- Update date including text: 2026-05-20T08:07:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-12: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-12 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-08-12: Introduced in House

## Actions

- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Introduced in House
- 2025-08-12 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-08-12 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-12",
    "latestAction": {
      "actionDate": "2025-08-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4957",
    "number": "4957",
    "originChamber": "House",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "N000193",
        "district": "3",
        "firstName": "Zachary",
        "fullName": "Rep. Nunn, Zachary [R-IA-3]",
        "lastName": "Nunn",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Rural Housing Service Reform Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:07:54Z",
    "updateDateIncludingText": "2026-05-20T08:07:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-12",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Agriculture, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-08-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-12",
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
          "date": "2025-08-12T13:00:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "systemCode": "hsag00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-08-12T13:00:20Z",
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
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-08-12",
      "state": "MO"
    },
    {
      "bioguideId": "M001136",
      "district": "9",
      "firstName": "Lisa",
      "fullName": "Rep. McClain, Lisa C. [R-MI-9]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-08",
      "state": "MI"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "CO"
    },
    {
      "bioguideId": "S001188",
      "district": "3",
      "firstName": "Marlin",
      "fullName": "Rep. Stutzman, Marlin A. [R-IN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Stutzman",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "IN"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "NY"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "KS"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NC"
    },
    {
      "bioguideId": "F000470",
      "district": "7",
      "firstName": "Michelle",
      "fullName": "Rep. Fischbach, Michelle [R-MN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fischbach",
      "party": "R",
      "sponsorshipDate": "2025-10-17",
      "state": "MN"
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
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "IA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "CO"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4957ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4957\nIN THE HOUSE OF REPRESENTATIVES\nAugust 12, 2025 Mr. Nunn of Iowa (for himself and Mr. Cleaver ) introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Agriculture , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo reform rural housing programs, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Rural Housing Service Reform Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec.\u20021.\u2002Short title; table of contents.\nTitle I\u2014Streamlining and updates\nSec.\u2002101.\u2002Application of multifamily mortgage foreclosure procedures to multifamily mortgages held by the Secretary of Agriculture and preservation of the rental assistance contract upon foreclosure.\nSec.\u2002102.\u2002Study on rural housing loans for housing for low- and moderate-income families.\nSec.\u2002103.\u2002Authorization of appropriations for staffing and IT upgrades.\nSec.\u2002104.\u2002Funding for technical improvements.\nTitle II\u2014Rural housing preservation and revitalization\nSec.\u2002201.\u2002Permanent establishment of housing preservation and revitalization program.\nSec.\u2002202.\u2002Rental assistance contract authority.\nTitle III\u2014Section 504 loans and grants\nSec.\u2002301.\u2002Modifications to loans and grants for minor improvements to farm housing and buildings; income eligibility.\nTitle IV\u2014Rural community development initiative grants\nSec.\u2002401.\u2002Rural community development initiative.\nTitle V\u2014Reports\nSec.\u2002501.\u2002Annual report on rural housing programs.\nSec.\u2002502.\u2002GAO report on Rural Housing Service technology.\nTitle VI\u2014Rural housing voucher program\nSec.\u2002601.\u2002Adjustment to rural development voucher amount.\nSec.\u2002602.\u2002Eligibility for rural housing vouchers.\nSec.\u2002603.\u2002Amount of voucher assistance.\nTitle VII\u2014Transfers to nonprofit organizations\nSec.\u2002701.\u2002Transfer of multifamily rural housing projects.\nTitle VIII\u2014Section 502 loans and guarantees\nSec.\u2002801.\u2002Extension of loan term.\nSec.\u2002802.\u2002Release of liability for section 502 guaranteed borrower upon assumption of original loan by new borrower.\nSec.\u2002803.\u2002Department of Agriculture loan restrictions.\nTitle IX\u2014Accessory dwelling units\nSec.\u2002901.\u2002Loan guarantees.\nTitle X\u2014Time frame for completing application review\nSec.\u20021001.\u2002Application review.\nI\nStreamlining and updates\n#### 101. Application of multifamily mortgage foreclosure procedures to multifamily mortgages held by the Secretary of Agriculture and preservation of the rental assistance contract upon foreclosure\n##### (a) Multifamily mortgage procedures\nSection 363(2) of the Multifamily Mortgage Foreclosure Act of 1981 ( 12 U.S.C. 3702(2) ) is amended\u2014\n**(1)**\nin subparagraph (D), by striking and at the end;\n**(2)**\nin subparagraph (E), by striking the period at the end and inserting ; or ; and\n**(3)**\nby adding at the end the following:\n(F) section 514, 515, or 538 of the Housing Act of 1949 ( 42 U.S.C. 1484 , 1485, 1490p). .\n##### (b) Preservation of contract\nSection 521(d) of the Housing Act of 1949 ( 42 U.S.C. 1490a(d) ) is amended by adding at the end the following:\n(3) Notwithstanding any other provision of law in managing and disposing of any multifamily property that is owned or has a mortgage held by the Secretary, and during the process of foreclosure on any property with a contract for rental assistance under this section\u2014 (A) the Secretary shall maintain any rental assistance payments that are attached to any dwelling units in the property; and (B) the rental assistance contract may be used to provide further assistance to existing projects under 514, 515, or 516. .\n#### 102. Study on rural housing loans for housing for low- and moderate-income families\nNot later than 6 months after the date of enactment of this Act, the Secretary of Agriculture shall conduct a study and submit to Congress a publicly available report on the loan program under section 521 of the Housing Act of 1949 ( 42 U.S.C. 1490a ), including\u2014\n**(1)**\nthe total amount provided by the Secretary in subsidies under such section 521 to borrowers with loans made pursuant to section 502 of such Act ( 42 U.S.C. 1472 );\n**(2)**\nhow much of the subsidies described in paragraph (1) are being recaptured; and\n**(3)**\nthe amount of time and costs associated with recapturing those subsidies.\n#### 103. Authorization of appropriations for staffing and IT upgrades\nThere is authorized to be appropriated to the Secretary of Agriculture for each of fiscal years 2026 through 2030 such sums as may be necessary for increased staffing needs and information technology upgrades to support all Rural Housing Service programs.\n#### 104. Funding for technical improvements\n##### (a) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary of Agriculture such sums as may be necessary for fiscal year 2026 for improvements to the technology of the Rural Housing Service of the Department of Agriculture used to process and manage housing loans.\n##### (b) Availability\nAmounts appropriated pursuant to subsection (a) shall remain available until the date that is 5 years after the date of the appropriation.\n##### (c) Timeline\nThe Secretary of Agriculture shall make the improvements described in subsection (a) during the 5-year period beginning on the date on which amounts are appropriated under subsection (a).\nII\nRural housing preservation and revitalization\n#### 201. Permanent establishment of housing preservation and revitalization program\nTitle V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. ) is amended by adding at the end the following:\n545. Housing preservation and revitalization program (a) Establishment The Secretary shall carry out a program under this section for the preservation and revitalization of multifamily rental housing projects financed under section 514, 515, or 516. (b) Notice of maturing loans (1) To owners On an annual basis, the Secretary shall provide written notice to each owner of a property financed under section 514, 515, or 516 that will mature within the 4-year period beginning upon the provision of the notice, setting forth the options and financial incentives that are available to facilitate the extension of the loan term or the option to decouple a rental assistance contract pursuant to subsection (f). (2) To tenants (A) In general On an annual basis, for each property financed under section 514, 515, or 516, not later than the date that is 2 years before the date that the loan will mature, the Secretary shall provide written notice to each household residing in the property that informs them of\u2014 (i) the date of the loan maturity; (ii) the possible actions that may happen with respect to the property upon that maturity; and (iii) how to protect their right to reside in federally assisted housing, or how to secure housing voucher, after that maturity. (B) Language Notice under this paragraph shall be provided in plain English and shall be translated to other languages in the case of any property located in an area in which a significant number of residents speak such other languages. (c) Loan restructuring Under the program under this section, in any circumstance in which the Secretary proposes a restructuring to an owner or an owner proposes a restructuring to the Secretary, the Secretary may restructure such existing housing loans, as the Secretary considers appropriate, for the purpose of ensuring that those projects have sufficient resources to preserve the projects to provide safe and affordable housing for low-income residents and farm laborers, by\u2014 (1) reducing or eliminating interest; (2) deferring loan payments; (3) subordinating, reducing, or reamortizing loan debt; (4) providing other financial assistance, including advances, payments, and incentives (including the ability of owners to obtain reasonable returns on investment) required by the Secretary; and (5) permanently removing a portion of the housing units from income restrictions when sustained vacancies have occurred. (d) Renewal of rental assistance (1) In general When the Secretary proposes to restructure a loan or agrees to the proposal of an owner to restructure a loan pursuant to subsection (c), the Secretary shall offer to renew the rental assistance contract under section 521(a)(2) for a term that is the shorter of 20 years and the term of the restructured loan, subject to annual appropriations, provided that the owner agrees to bring the property up to such standards that will ensure maintenance of the property as decent, safe, and sanitary housing for the full term of the rental assistance contract. (2) Additional rental assistance With respect to a project described in paragraph (1), if rental assistance is not available for all households in the project for which the loan is being restructured pursuant to subsection (c), the Secretary may extend such additional rental assistance to unassisted households at that project as is necessary to make the project safe and affordable to low-income households. (e) Restrictive use agreements (1) Requirement As part of the preservation and revitalization agreement for a project, the Secretary shall obtain a restrictive use agreement that is recorded and obligates the owner to operate the project in accordance with this title. (2) Term (A) No extension of rental assistance contract Except when the Secretary enters into a 20-year extension of the rental assistance contract for a project, the term of the restrictive use agreement for the project shall be consistent with the term of the restructured loan for the project. (B) Extension of rental assistance contract If the Secretary enters into a 20-year extension of the rental assistance contract for a project, the term of the restrictive use agreement for the project shall be for the longer of\u2014 (i) 20 years; or (ii) the remaining term of the loan for that project. (C) Termination The Secretary may terminate the 20-year use restrictive use agreement for a project before the end of the term of the agreement if the 20-year rental assistance contract for the project with the owner is terminated at any time for reasons outside the control of the owner. (f) Decoupling of rental assistance (1) Renewal of rental assistance contract If the Secretary determines that a loan maturing during the 4-year period beginning upon the provision of the notice required under subsection (b)(1) for a project cannot reasonably be restructured in accordance with subsection (c) because it is not financially feasible or the owner does not agree with the proposed restructuring, and the project was operating with rental assistance under section 521 and the recipient is a borrower under section 514 or 515, the Secretary may renew the rental assistance contract, notwithstanding any requirement under section 521 that the recipient be a current borrower under section 514 or 515, for a term of 20 years, subject to annual appropriations. (2) Additional rental assistance With respect to a project described in paragraph (1), if rental assistance is not available for all households in the project for which the loan is being restructured pursuant to subsection (c), the Secretary may extend such additional rental assistance to unassisted households at that project as is necessary to make the project safe and affordable to low-income households. (3) Rents (A) In general Any agreement to extend the term of the rental assistance contract under section 521 for a project shall obligate the owner to continue to maintain the project as decent, safe, and sanitary housing and to operate the development as affordable housing in a manner that meets the goals of this title. (B) Rent amounts Subject to subparagraph (C), in setting rents, the Secretary\u2014 (i) shall determine the maximum initial rent based on current fair market rents established under section 8 of the United States Housing Act of 1937 ( 42 U.S.C. 1437f ); and (ii) may annually adjust the rent determined under clause (i) by the operating cost adjustment factor as provided under section 524 of the Multifamily Assisted Housing Reform and Affordability Act of 1997 ( 42 U.S.C. 1437f note). (C) Higher rent (i) In general Subparagraph (B) shall not apply if the Secretary determines that the budget-based needs of a project require a higher rent than the rent described in subparagraph (B). (ii) Rent If the Secretary makes a positive determination under clause (i), the Secretary may approve a budget-based rent level for the project. (4) Conditions for approval Before the approval of a rental assistance contract authorized under this section, the Secretary shall require, through an annual notice in the Federal Register, the owner to submit to the Secretary a plan that identifies financing sources and a timetable for renovations and improvements determined to be necessary by the Secretary to maintain and preserve the project. (g) Multifamily housing transfer technical assistance Under the program under this section, the Secretary may provide grants to qualified nonprofit organizations and public housing agencies to provide technical assistance, including financial and legal services, to borrowers under loans under this title for multifamily housing to facilitate the acquisition or preservation of such multifamily housing properties in areas where the Secretary determines there is a risk of loss of affordable housing. (h) Administrative expenses Of any amounts made available for the program under this section for any fiscal year, the Secretary may use not more than $1,000,000 for administrative expenses for carrying out such program. (i) Authorization of appropriations There is authorized to be appropriated for the program under this section such sums as may be necessary for each of fiscal years 2026 through 2030. (j) Rulemaking (1) In general Not later than 180 days after the date of enactment of the Rural Housing Service Reform Act of 2025 , the Secretary shall\u2014 (A) publish an advance notice of proposed rulemaking; and (B) consult with appropriate stakeholders. (2) Interim final rule Not later than 1 year after the date of enactment of the Rural Housing Service Reform Act of 2025 , the Secretary shall publish an interim final rule to carry out this section. .\n#### 202. Rental assistance contract authority\nSection 521(d) of the Housing Act of 1949 ( 42 U.S.C. 1490a(d) ), as amended by section 101(b), is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D), respectively;\n**(B)**\nby inserting after subparagraph (A) the following:\n(B) upon request of an owner of a project financed under section 514 or 515, the Secretary is authorized to enter into renewal of such agreements for a period of 20 years or the term of the loan, whichever is shorter, subject to amounts made available in appropriations Acts; ;\n**(C)**\nin subparagraph (C), as so redesignated, by striking subparagraph (A) and inserting subparagraphs (A) and (B) ; and\n**(D)**\nin subparagraph (D), as so redesignated, by striking subparagraphs (A) and (B) and inserting subparagraphs (A), (B), and (C) ;\n**(2)**\nin paragraph (2), by striking shall and inserting may ; and\n**(3)**\nby adding at the end the following:\n(4) In the case of any rental assistance contract authority that becomes available because of the termination of assistance on behalf of an assisted family\u2014 (A) at the option of the owner of the rental project, the Secretary shall provide the owner a period of not more than 6 months before unused assistance is made available pursuant to subparagraph (B) during which the owner may use such assistance authority to provide assistance on behalf of an eligible unassisted family that\u2014 (i) is residing in the same rental project in which the assisted family resided before the termination; or (ii) newly occupies a dwelling unit in the rental project during that 6-month period; and (B) except for assistance used as provided in subparagraph (A), the Secretary shall use such remaining authority to provide assistance on behalf of eligible families residing in other rental projects originally financed under section 514, 515, or 516. .\nIII\nSection 504 loans and grants\n#### 301. Modifications to loans and grants for minor improvements to farm housing and buildings; income eligibility\nSection 504(a) of the Housing Act of 1949 ( 42 U.S.C. 1474(a) ) is amended\u2014\n**(1)**\nin the first sentence, by inserting and may make a loan to an eligible low-income applicant after applicant ;\n**(2)**\nby inserting Not less than 60 percent of loan funds made available under this section shall be reserved and made available for very low-income applicants. after the first sentence; and\n**(3)**\nby striking $7,500 and inserting $15,000 .\nIV\nRural community development initiative grants\n#### 401. Rural community development initiative\nSubtitle E of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 2009 et seq. ) is amended by adding at the end the following:\n381O. Rural community development initiative (a) Definitions In this section: (1) Eligible entity The term eligible entity means\u2014 (A) a private, nonprofit community-based housing or community development organization; (B) a rural community; or (C) a federally recognized Indian Tribe. (2) Eligible intermediary The term eligible intermediary means a qualified\u2014 (A) private, nonprofit organization; or (B) public organization. (b) Establishment The Secretary shall establish a Rural Community Development Initiative, under which the Secretary shall provide grants to eligible intermediaries to carry out programs to provide financial and technical assistance to eligible entities to develop the capacity and ability of eligible entities to carry out projects to improve housing, community facilities, and community and economic development projects in rural areas. (c) Amount of grants The amount of a grant provided to an eligible intermediary under this section shall be not more than $250,000. (d) Matching funds (1) In general An eligible intermediary receiving a grant under this section shall provide matching funds from other sources, including Federal funds for related activities, in an amount not less than the amount of the grant. (2) Waiver The Secretary may waive paragraph (1) with respect to a project that would be carried out in a persistently poor rural region, as determined by the Secretary. .\nV\nReports\n#### 501. Annual report on rural housing programs\nTitle V of the Housing Act of 1949 ( 42 U.S.C. 1471 et seq. ), as amended by this Act, is amended by adding at the end the following:\n546. Annual report (a) In general The Secretary shall submit to the appropriate committees of Congress and publish on the website of the Department of Agriculture an annual report on rural housing programs carried out under this title, which shall include significant details on the health of Rural Housing Service programs, including\u2014 (1) raw data sortable by programs and by region regarding loan performance; (2) the housing stock of those programs, including information on why properties end participation in those programs, such as for maturation, prepayment, foreclosure, or other servicing issues; and (3) risk ratings for properties assisted under those programs. (b) Protection of information The data included in each report required under subsection (a) may be aggregated or anonymized to protect participant financial or personal information. .\n#### 502. GAO report on Rural Housing Service technology\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to Congress a report that includes\u2014\n**(1)**\nan analysis of how the outdated technology used by the Rural Housing Service impacts participants in the programs of the Rural Housing Service;\n**(2)**\nan estimate of the amount of funding that is needed to modernize the technology used by the Rural Housing Service; and\n**(3)**\nan estimate of the number and type of new employees the Rural Housing Service needs to modernize the technology used by the Rural Housing Service.\nVI\nRural housing voucher program\n#### 601. Adjustment to rural development voucher amount\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of Agriculture shall issue regulations to establish a process for adjusting the voucher amount provided under section 542 of the Housing Act of 1949 ( 42 U.S.C. 1490r ) after the issuance of the voucher following an interim or annual review of the amount of the voucher.\n##### (b) Interim review\nThe interim review described in subsection (a) shall, at the request of a tenant, allow for a recalculation of the voucher amount when the tenant experiences a reduction in income, change in family composition, or change in rental rate.\n##### (c) Annual review\n**(1) In general**\nThe annual review described in subsection (a) shall require tenants to annually recertify the family composition of the household and that the family income of the household does not exceed 80 percent of the area median income at a time determined by the Secretary of Agriculture.\n**(2) Considerations**\nIf a tenant does not recertify the family composition and family income of the household within the time frame required under paragraph (1), the Secretary of Agriculture\u2014\n**(A)**\nshall consider whether extenuating circumstances caused the delay in recertification; and\n**(B)**\nmay alter associated consequences for the failure to recertify based on those circumstances.\n**(3) Effective date**\nFollowing the annual review of a voucher under subsection (a), the updated voucher amount shall be effective on the 1st day of the month following the expiration of the voucher.\n##### (d) Deadline\nThe process established under subsection (a) shall require the Secretary of Agriculture to review and update the voucher amount described in subsection (a) for a tenant not later than 60 days before the end of the voucher term.\n#### 602. Eligibility for rural housing vouchers\nSection 542 of the Housing Act of 1949 ( 42 U.S.C. 1490r ) is amended by adding at the end the following:\n(c) Eligibility of households in sections 514, 515, and 516 projects The Secretary may provide rural housing vouchers under this section for any low-income household (including those not receiving rental assistance) residing for a term longer than the remaining term of their lease that is in effect on the date of prepayment, foreclosure, or mortgage maturity, in a property financed with a loan under section 514 or 515 or a grant under section 516 that has\u2014 (1) been prepaid with or without restrictions imposed by the Secretary pursuant to section 502(c)(5)(G)(ii)(I); (2) been foreclosed; or (3) matured after September 30, 2005. .\n#### 603. Amount of voucher assistance\nNotwithstanding any other provision of law, in the case of any rural housing voucher provided pursuant to section 542 of the Housing Act of 1949 ( 42 U.S.C. 1490r ), the amount of the monthly assistance payment for the household on whose behalf the assistance is provided shall be determined as provided in subsection (a) of such section 542, including providing for interim and annual review of the voucher amount in the event of a change in household composition or income or rental rate.\nVII\nTransfers to nonprofit organizations\n#### 701. Transfer of multifamily rural housing projects\nSection 515 of the Housing Act of 1949 ( 42 U.S.C. 1485 ) is amended\u2014\n**(1)**\nin subsection (h), by adding at the end the following:\n(3) Transfer to nonprofit organizations A nonprofit or public body purchaser, including a limited partnership with a general partner with the principal purpose of providing affordable housing, may purchase a property for which a loan is made or insured under this section that has received a market value appraisal, without addressing rehabilitation needs at the time of purchase, if the purchaser\u2014 (A) makes a commitment to address rehabilitation needs during ownership and long-term use restrictions on the property; and (B) at the time of purchase, accepts long-term use restrictions on the property. ; and\n**(2)**\nin subsection (w)(1), in the first sentence in the matter preceding subparagraph (A), by striking 9 percent and inserting 25 percent .\nVIII\nSection 502 loans and guarantees\n#### 801. Extension of loan term\n##### (a) In general\nSection 502(a)(2) of the Housing Act of 1949 ( 42 U.S.C. 1472(a)(2) ) is amended\u2014\n**(1)**\nby inserting (A) before The Secretary ;\n**(2)**\nin subparagraph (A), as so designated, by striking paragraph and inserting subparagraph ; and\n**(3)**\nby adding at the end the following:\n(B) The Secretary may refinance or modify the period of any loan, including any refinanced loan, made under this section in accordance with terms and conditions as the Secretary shall prescribe, but in no event shall the total term of the loan from the date of the refinance or modification exceed 40 years. .\n##### (b) Application\nThe amendment made under subsection (a) shall apply with respect to loans made under section 502 of the Housing Act of 1949 ( 42 U.S.C. 1472 ) before, on, or after the date of enactment of this Act.\n#### 802. Release of liability for section 502 guaranteed borrower upon assumption of original loan by new borrower\nSection 502(h)(10) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(10) ) is amended to read as follows:\n(10) Transfer and assumption Upon the transfer of property for which a guaranteed loan under this subsection was made and the assumption of the guaranteed loan by an approved eligible borrower, the original borrower of a guaranteed loan under this subsection shall be relieved of liability with respect to the loan. .\n#### 803. Department of Agriculture loan restrictions\n##### (a) Definitions\nIn this section, the terms State and Tribal organization have the meanings given those terms in section 658P of the Child Care and Development Block Grant Act of 1990 ( 42 U.S.C. 9858n ).\n##### (b) Revision\nThe Secretary of Agriculture shall revise section 3555.102(c) of title 7, Code of Federal Regulations, to exclude from the restriction under that section\u2014\n**(1)**\na home-based business that is a licensed, registered, or regulated child care provider under State law or by a Tribal organization; and\n**(2)**\nan applicant that has applied to become a licensed, registered, or regulated child care provider under State law or by a Tribal organization.\nIX\nAccessory dwelling units\n#### 901. Loan guarantees\nSection 502(h)(4) of the Housing Act of 1949 ( 42 U.S.C. 1472(h)(4) ) is amended\u2014\n**(1)**\nby redesignating subparagraphs (A), (B), and (C) as clauses (i), (ii), and (iii), respectively;\n**(2)**\nby striking Loans may be guaranteed and inserting the following:\n(A) Definition In this paragraph, the term accessory dwelling unit means a single, habitable living unit\u2014 (i) with means of separate ingress and egress; (ii) that is usually subordinate in size; (iii) that can be added to, created within, or detached from a primary 1-unit, single-family dwelling; and (iv) in combination with a primary 1-unit, single-family dwelling, constitutes a single interest in real estate. (B) Single-family requirement Loans may be guaranteed ; and\n**(3)**\nby adding at the end the following:\n(C) Rule of construction Nothing in this paragraph shall be construed to prohibit the leasing of an accessory dwelling unit or the use of rental income derived from such a lease to qualify for a loan guaranteed under this subsection\u2014 (i) after the date of enactment of the Rural Housing Service Reform Act of 2025 ; and (ii) if the property that is the subject of the loan was constructed before the date of enactment of the Rural Housing Service Reform Act of 2025 . .\nX\nTime frame for completing application review\n#### 1001. Application review\n##### (a) Sense of Congress\nIt is the sense of Congress, not later than 90 days after the date on which the Secretary of Agriculture receives an application for a loan, grant or combined loan and grant under section 502 or 504 of the Housing Act of 1949 ( 42 U.S.C. 1472 , 1474), the Secretary of Agriculture should\u2014\n**(1)**\nreview the application;\n**(2)**\ncomplete the underwriting;\n**(3)**\nmake a determination of eligibility with respect to the application; and\n**(4)**\nnotify the applicant of determination.\n##### (b) Report\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, and annually thereafter until the date described in paragraph (2), the Secretary of Agriculture shall submit to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives a report\u2014\n**(A)**\ndetailing the timeliness of eligibility determinations and final determinations with respect to applications under section 502 and 504 of the Housing Act of 1949 ( 42 U.S.C. 1472 , 1474), including justifications for any eligibility determinations taking longer than 90 days;\n**(B)**\nthat includes recommendations to shorten the timeline for notifications of eligibility determinations described in paragraph (1) to not more than 90 days.\n**(2) Date described**\nThe date described in this paragraph is the date on which, during the preceding 5-year period, the Secretary of Agriculture provides each eligibility determination described in paragraph (1) during the 90-day period beginning on the date on which each application is received.",
      "versionDate": "2025-08-12",
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
        "actionDate": "2025-04-02",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1260",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Rural Housing Service Reform Act of 2025",
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
        "updateDate": "2025-09-19T14:21:37Z"
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
      "date": "2025-08-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4957ih.xml"
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
      "title": "Rural Housing Service Reform Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-13T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Housing Service Reform Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-13T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reform rural housing programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-13T08:18:21Z"
    }
  ]
}
```
