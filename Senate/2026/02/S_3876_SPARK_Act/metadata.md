# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3876?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3876
- Title: SPARK Act
- Congress: 119
- Bill type: S
- Bill number: 3876
- Origin chamber: Senate
- Introduced date: 2026-02-12
- Update date: 2026-04-30T12:55:43Z
- Update date including text: 2026-04-30T12:55:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-02-12: Introduced in Senate
- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- Latest action: 2026-02-12: Introduced in Senate

## Actions

- 2026-02-12 - IntroReferral: Introduced in Senate
- 2026-02-12 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-12",
    "latestAction": {
      "actionDate": "2026-02-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3876",
    "number": "3876",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "SPARK Act",
    "type": "S",
    "updateDate": "2026-04-30T12:55:43Z",
    "updateDateIncludingText": "2026-04-30T12:55:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Small Business and Entrepreneurship.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-02-12",
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
          "date": "2026-02-12T19:32:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "HI"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3876is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3876\nIN THE SENATE OF THE UNITED STATES\nFebruary 12, 2026 Mr. Markey (for himself, Ms. Hirono , and Mr. Booker ) introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo amend the Small Business Act to spur entrepreneurial ecosystems in underserved communities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strengthening Place-based Access, Resources, and Knowledge Act or the SPARK Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nStudies have found that incubators, accelerators, and other similar models are effective at increasing revenues, the number of employees, and the likelihood that the business venture will be successful for participants.\n**(2)**\nAccording to the 2023 Report on Startup Firms Owned by People of Color: Findings from the 2022 Small Business Credit Survey\u2014\n**(A)**\nstartups owned by racial minorities are more than twice as likely to be denied for financing from lenders than non-minority-owned startups; and\n**(B)**\nmission-oriented financial institutions and community-based lenders, including minority depository institutions and community development financial institutions, are critical in helping minority-owned businesses access capital.\n**(3)**\nAccording to the Kauffman Foundation\u2014\n**(A)**\nminority-owned and women-owned businesses are half as likely to have workers than non-minority-owned and men-owned businesses; and\n**(B)**\nif minorities started businesses at the same rate as non-minorities, approximately 9,500,000 jobs would be added to the economy of the United States.\n**(4)**\nAccording to the Center for Rural Innovation\u2014\n**(A)**\nless than 1 percent of all venture capital funding goes to businesses located in rural areas;\n**(B)**\nrural entrepreneurship rates have fallen from 20 percent in the 1980s to just more than 12 percent in the 2010s; and\n**(C)**\nfinancial barriers in rural areas are especially prominent for minority populations.\n**(5)**\nAccording to PitchBook, only 2 percent of all venture capital funding goes to businesses with women founders.\n**(6)**\nAccording to Crunchbase, less than 3 percent of all venture capital funding goes to businesses with Black and Hispanic founders.\n#### 3. Purposes\nThe purposes of the Spark Program established under section 49 of the Small Business Act, as amended by this Act, are to\u2014\n**(1)**\nspur economic growth in underserved communities by creating good paying jobs and increasing access to capital;\n**(2)**\nincrease prospects for success for small business concerns in underserved communities, which often suffer from higher business failure rates than the national average;\n**(3)**\ncreate a pipeline for individuals in underserved and rural markets into small business ownership;\n**(4)**\nclose the gaps that underserved small business concerns often have in terms of revenue and number of employees, which represent lost opportunity for the economy of the United States;\n**(5)**\nencourage collaboration between the Small Business Administration and organizations that serve low-income, minority, and rural communities; and\n**(6)**\ngrow existing incubators and accelerators that are focused on empowering underserved communities and entrepreneurs.\n#### 4. Spark Program\nThe Small Business Act ( 15 U.S.C. 631 et seq. ) is amended\u2014\n**(1)**\nby redesignating section 49 ( 15 U.S.C. 631 note) as section 51; and\n**(2)**\nby inserting after section 48 ( 15 U.S.C. 657u ) the following:\n49. Spark Program (a) Definitions In this section: (1) Accelerator The term accelerator means an organization\u2014 (A) that\u2014 (i) works with a startup or growing small business concern for a predetermined period; (ii) provides mentorship and instruction to scale businesses; and (iii) increases the investment readiness of small business concerns; and (B) that may\u2014 (i) provide, but is not exclusively designed to provide, seed investment in exchange for a small amount of equity; and (ii) offer startup capital or the opportunity to raise capital from outside investors. (2) Eligible entity (A) In general The term eligible entity means an organization operating, or planning to operate\u2014 (i) an accelerator; (ii) an incubator; or (iii) any other small business innovation-focused project, as approved by the Administrator. (B) Inclusions The term eligible entity includes any of the following, if the organization is as described in subparagraph (A): (i) An organization described in section 501(c)(3) of the Internal Revenue Code of 1986. (ii) A community development financial institution, as defined in section 103 of the Community Development Banking and Financial Institutions Act of 1994 ( 12 U.S.C. 4702 ). (iii) A minority depository institution, as defined in section 308(b) of the Financial Institutions Reform, Recovery, and Enforcement Act of 1989 ( 12 U.S.C. 1463 note). (iv) A lender under the program established under section 7(m). (v) A development company that is certified under title V of the Small Business Investment Act of 1958 ( 15 U.S.C. 695 et seq. ). (vi) A Community Advantage Small Business Lending Company, as defined in section 120.10 of title 13, Code of Federal Regulations, or any successor regulation. (vii) An institution described in any of paragraphs (1) through (7) of section 371(a) of the Higher Education Act of 1965 ( 20 U.S.C. 1067q(a) ). (viii) A junior or community college, as defined in section 312 of the Higher Education Act of 1965 ( 20 U.S.C. 1058 ). (3) Federally recognized area of economic distress The term federally recognized area of economic distress means\u2014 (A) a HUBZone, as that term is defined in section 31(b); (B) an area that has been designated as\u2014 (i) an empowerment zone or enterprise community under section 1391 of the Internal Revenue Code of 1986; (ii) a Promise Zone by the Secretary of Housing and Urban Development; or (iii) a low-income neighborhood or moderate-income neighborhood for purposes of the Community Reinvestment Act of 1977 ( 12 U.S.C. 2901 et seq. ); or (C) any area for which a disaster declaration or determination described in subparagraph (A), (B), (C), or (E) of section 7(b)(2) has been made that has not terminated more than 2 years before the date on which an eligible entity enters into a cooperative agreement with the Administration under this section with respect to the area (or later, as determined by the Administrator), except that, in the case of a major disaster described in subparagraph (A) of section 7(b)(2), that period shall be 5 years. (4) Growing; newly established; startup The terms growing , newly established , and startup , with respect to a small business concern, mean growing, newly established, and startup, respectively, within the meanings given those terms under section 7(m). (5) Incubator The term incubator means an organization\u2014 (A) that\u2014 (i) tends to work with startup and newly established small business concerns; and (ii) provides mentorship to startup and newly established small business concerns; and (B) that may\u2014 (i) provide a co-working environment or a month-to-month lease program; and (ii) work with startups or newly established small business concerns for a predetermined period or an open-ended period. (6) Individuals with a disability The term individuals with a disability means more than 1 individual with a disability, as defined in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ). (7) Rural area The term rural area has the meaning given the term in section 7(m)(11). (8) Socially and economically disadvantaged individual The term socially and economically disadvantaged individual means a socially and economically disadvantaged individual within the meaning given that term in section 8(d)(3)(C). (b) Establishment Not later than 1 year after the date of enactment of the Strengthening Place-based Access, Resources, and Knowledge Act , the Administrator shall develop and begin implementing a program (to be known as the Spark Program ) to enter into cooperative agreements with eligible entities under this section. (c) Authority (1) In general The Administrator may\u2014 (A) with respect to eligible entities that have submitted applications for such purpose, enter into cooperative agreements to provide financial assistance to those eligible entities to conduct 5-year projects for the benefit of startup, newly established, or growing small business concerns, which may include cooperatives and community land trusts; and (B) renew a cooperative agreement entered into under this section for additional 3-year periods, in accordance with paragraph (3). (2) Project requirements A project conducted under a cooperative agreement under this section shall\u2014 (A) be carried out in such locations as to provide maximum accessibility and benefits to the small business concerns that the project is intended to serve; (B) have a full-time staff, including a full-time director who shall\u2014 (i) have the authority to make expenditures under the budget of the project; and (ii) manage the activities carried out under the project; (C) include the joint provision of programs and services by the eligible entity and the Administration, which\u2014 (i) shall be jointly developed, negotiated, and agreed upon, with full participation of both parties, pursuant to an executed cooperative agreement between the eligible entity and the Administration; and (ii) shall include\u2014 (I) one-to-one individual counseling, as described in section 21(c)(3)(A); and (II) a formal, structured mentorship program; (D) incorporate continuous upgrades and modifications to the services and programs offered under the project, as needed to meet the changing and evolving needs of the business community; (E) involve working with underserved groups, which include\u2014 (i) women; (ii) socially and economically disadvantaged individuals; (iii) veterans or spouses of veterans; (iv) individuals with disabilities; (v) small business concerns located in rural areas, including startup, newly established, or growing small business concerns located in rural areas; (vi) members of an Indian Tribe individually identified (including parenthetically) in the most recent list published pursuant to section 104 of the Federally Recognized Indian Tribe List Act of 1994 ( 25 U.S.C. 5131 ); (vii) individuals who have completed a term of imprisonment in a Federal, State, or local jail or prison; or (viii) small business concerns, if not less than 50 percent of the employees of the small business concern reside in a low- or moderate-income community; (F) not impose or otherwise collect a fee or other compensation in connection with participation in the programs and services described in subparagraph (C)(ii); and (G) ensure that small business concerns participating in the project have access, including through resource partners, to information concerning Federal, State, and local regulations that affect small business concerns. (3) Continued funding (A) In general An eligible entity that enters into an initial cooperative agreement, or a renewal of a cooperative agreement, under paragraph (1) may submit an application for a 3-year renewal of the cooperative agreement at such time, in such manner, and accompanied by such information as the Administrator may establish. (B) Application and approval criteria (i) Criteria The Administrator shall develop and publish criteria for the consideration and approval of applications for renewals of cooperative agreements by eligible entities under this paragraph, which shall take into account the structure and the stated goals of the project. (ii) Notification Not later than 60 days after the date of the deadline to submit applications for each fiscal year, the Administrator shall approve or deny any application under this paragraph and notify the applicant for each such application. (C) Priority In allocating funds made available for cooperative agreements under this section, the Administrator shall give applications under this paragraph priority over first-time applications for cooperative agreements under paragraph (1)(A). (4) Scope of authority (A) Subject to appropriations The authority of the Administrator to enter into cooperative agreements under this section shall be in effect for each fiscal year only to the extent and in the amounts as are provided in advance in appropriations Acts. (B) Suspension, termination, and failure to renew or extend After the Administrator has entered into a cooperative agreement with an eligible entity under this section, the Administrator may not suspend, terminate, or fail to renew or extend the cooperative agreement unless the Administrator provides the eligible entity with written notification setting forth the reasons for that suspension, termination, or failure and affords the eligible entity an opportunity for a hearing, appeal, or other administrative proceeding under chapter 5 of title 5, United States Code. (5) Limitation on use of funds An eligible entity that has entered into a cooperative agreement under this section may not use any portion of the financial assistance provided under that cooperative agreement to directly provide capital to any participant in any project that is funded with that financial assistance. (d) Criteria (1) In general The Administrator shall\u2014 (A) establish and evaluate in terms of relative importance the criteria the Administrator shall use in awarding cooperative agreements under this section, which shall include\u2014 (i) whether the proposed project will be located in\u2014 (I) a federally recognized area of economic distress; (II) a rural area; or (III) an area lacking sufficient entrepreneurial development resources, as determined by the Administrator; (ii) whether the proposed project demonstrates a commitment, and details a specific plan, to partner with core stakeholders working with small business concerns in the relevant area, including\u2014 (I) investment and lending organizations; (II) nongovernmental organizations; (III) programs of State and local governments that are concerned with aiding small business concerns; (IV) Federal agencies, including the Minority Business Development Agency of the Department of Commerce; and (V) for-profit organizations with an expertise in small business innovation; (iii) whether the proposed project will serve underserved groups described in subsection (c)(2)(E); (iv) whether the proposed project is a local, place-based initiative that seeks to engage local communities and consumers; and (v) whether the proposed project will provide or connect small business concerns with investment, grant-making, or procurement opportunities; (B) make publicly available, including on the website of the Administration, and state in each solicitation for applications for cooperative agreements under this section, the selection criteria and ranking established under subparagraph (A); and (C) evaluate applicants for cooperative agreements under this section in accordance with the selection criteria and ranking established under subparagraph (A). (2) Contents The selection criteria established under paragraph (1)(A) shall consider\u2014 (A) the record of the applicable eligible entity in assisting growing, newly established, and startup small business concerns, including, for each of the 3 full years before the date on which the eligible entity applies for a cooperative agreement under this section (or, if the eligible entity has been in operation for less than 3 years, for the most recent full year the eligible entity was in operation)\u2014 (i) the number and retention rate of growing, newly established, and startup business concerns in the program of the eligible entity; (ii) the average period of participation by growing, newly established, and startup small business concerns in the program of the eligible entity; (iii) the total and median capital raised by growing, newly established, and startup small business concerns participating in the program of the eligible entity; (iv) the number of investments, grants, or loans received by growing, newly established, and startup small business concerns participating in the program of the eligible entity; and (v) the total and median number of employees of growing, newly established, and startup small business concerns participating in the program of the eligible entity; (B) the structure and goals of the applicable project; (C) ties that the applicable eligible entity has to the business community; (D) the resources available for the applicable project; (E) the capabilities of the applicable project, including coordination with local resource partners and local or national lending partners of the Administration; (F) the unique business and economic challenges faced by the community in which the applicable eligible entity is located and businesses in that community; (G) the proposed budget and plan for use of funds; and (H) any other criteria determined appropriate by the Administrator. (e) Program examination (1) In general The Administrator shall\u2014 (A) develop and implement an annual programmatic and financial examination of each project carried out with financial assistance provided under this section, under which each eligible entity entering into a cooperative agreement under this section shall provide to the Administrator\u2014 (i) an itemized cost breakdown of actual expenditures for costs incurred during the preceding year; and (ii) documentation regarding the amount of assistance from non-Federal sources obtained and expended by the eligible entity during the preceding year; and (B) analyze the results of each examination conducted under subparagraph (A) and, based on that analysis, make a determination regarding the programmatic and financial viability of each eligible entity. (2) Conditions for continued funding In determining whether to continue or renew a cooperative agreement under this section, the Administrator\u2014 (A) shall consider the results of the most recent examination of the applicable project under paragraph (1); and (B) may terminate or not renew a cooperative agreement, if\u2014 (i) the Administrator determines that the applicable eligible entity has failed to provide information required to be provided (including information provided for the purpose of the annual report by the Administrator under subsection (l)); or (ii) the information provided by the applicable eligible entity is inadequate. (3) Study and report Not later than 2 years after the date of enactment of the Strengthening Place-based Access, Resources, and Knowledge Act , the Administrator shall\u2014 (A) conduct a study to determine whether the program examination criteria under this subsection and the reporting requirements under subsection (l) should vary or include other metrics based on the type and location of a project; and (B) submit to Congress a report detailing the results of the study conducted under subparagraph (A). (f) Training and technical assistance The Administrator\u2014 (1) shall provide in-person or online training and technical assistance to each eligible entity entering into a cooperative agreement under this section at the beginning of the participation of the eligible entity in the Spark Program in order to build the capacity of the eligible entity and ensure compliance with procedures established by the Administrator; (2) shall ensure that the training and technical assistance described in paragraph (1) is provided at no cost or at a low cost; and (3) may enter into a contract to provide the training or technical assistance described in paragraph (1) with 1 or more organizations with expertise in the entrepreneurial development programs of the Administration, innovation, and entrepreneurial development. (g) Coordination In carrying out a project with financial assistance provided under this section, an eligible entity may coordinate with\u2014 (1) resource and lending partners of the Administration; (2) programs of State and local governments that are concerned with aiding small business concerns; and (3) other Federal agencies, including to provide services to and assist small business concerns in participating in the SBIR and STTR programs, as defined in section 9(e). (h) Funding limit The amount of financial assistance provided to an eligible entity under a cooperative agreement entered into under this section shall be not less than $500,000 during each year. (i) Contract authority (1) In general An eligible entity that has entered into a cooperative agreement under this section may enter into a contract with a Federal department or agency to provide specific assistance to startup, newly established, or growing small business concerns. (2) Performance Performance of a contract entered into under paragraph (1) may not hinder the eligible entity in carrying out the terms of the cooperative agreement under this section. (3) Additional provision Notwithstanding any other provision of law, a contract for assistance under paragraph (1) shall not be applied to any Federal department or agency's small business, woman-owned business, or socially and economically disadvantaged business contracting goal under section 15(g). (j) Privacy requirements (1) In general An eligible entity may not disclose the name, address, or telephone number of any individual or small business concern receiving assistance under this section without the consent of that individual or small business concern, unless\u2014 (A) the Administrator is ordered to make such a disclosure by a court in any civil or criminal enforcement action initiated by a Federal or State agency; or (B) the Administrator considers such a disclosure to be necessary for the purpose of conducting a financial audit of an eligible entity, except that a disclosure under this subparagraph shall be limited to the information necessary for that audit. (2) Administration use of information This subsection shall not\u2014 (A) restrict Administration access to program activity data; or (B) prevent the Administration from using client information (other than the information described in subparagraph (A)) to conduct client surveys. (3) Regulations The Administrator shall issue regulations to establish standards for requiring disclosures during a financial audit under paragraph (1)(B). (k) Publication of information The Administrator shall\u2014 (1) publish information about the program carried out under this section online, including\u2014 (A) on the website of the Administration; and (B) on the social media of the Administration; and (2) request that the resource and lending partners of the Administration and the district offices of the Administration publicize the program carried out under this section. (l) Annual reporting Not later than 1 year after the date on which the Administrator establishes the program under this section, and annually thereafter, the Administrator shall submit to Congress a report on the activities under the program, including\u2014 (1) the number of startup, newly established, and growing small business concerns participating in the project carried out by each eligible entity under a cooperative agreement entered into under this section (referred to in this subsection as participants ), including a breakdown of the owners of the participants by race, gender, veteran status, and urban versus rural location; (2) the retention rate for participants; (3) the total and median amount of capital accessed by participants, including the type of capital accessed; (4) the total and median number of employees of participants; (5) the number and median wage of jobs created by participants; (6) the number of jobs sustained by participants; and (7) information regarding such other metrics as the Administrator determines appropriate, including coordination with other private or public small business assistance programs. (m) Funding (1) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary to carry out this section. (2) Administrative expenses Of the amount made available to carry out this section for any fiscal year, not more than 10 percent may be used by the Administrator for administrative expenses. .\n#### 5. Spark Financing Program\nThe Small Business Act ( 15 U.S.C. 631 et seq. ), as amended by section 4, is amended by inserting after section 49 the following:\n50. Spark Financing Program (a) Definitions In this section: (1) Covered entity The term covered entity means\u2014 (A) an eligible entity; or (B) solely for the purposes of making loans under subsection (c)(3)(A)(ii), another lender or organization determined appropriate by the Administrator. (2) Covered small business concern The term covered small business concern means a small business concern that is\u2014 (A) owned by an individual that is a member of an underserved group described in section 49(c)(2)(E); or (B) located in a federally recognized area of economic distress. (3) Eligible entity; federally recognized area of economic distress; growing; newly established; startup The terms eligible entity , federally recognized area of economic distress , growing , newly established , and startup have the meanings given those terms in section 49(a). (b) Establishment of program Not later than 1 year after the date of enactment of the Strengthening Place-based Access, Resources, and Knowledge Act , the Administrator shall establish, and thereafter the Administrator shall carry out, a grant and loan program (to be known as the Spark Financing Program ), under which, in accordance with the requirements of this section, the Administrator shall provide financial assistance to covered entities, which shall use that financial assistance to make grants or loans to covered small business concerns. (c) Financial assistance to eligible entities (1) In general The Administrator shall provide financial assistance to covered entities under this section as follows: (A) If the covered entity has entered into a cooperative agreement under section 49\u2014 (i) the amount of financial assistance provided under this section shall be not more than $1,000,000 per year; and (ii) the entity\u2014 (I) shall receive financial assistance under this section at the same time that the covered entity receives financial assistance pursuant to that cooperative agreement under section 49; and (II) shall not be required to reapply for funding under this section on an annual basis. (B) If the covered entity has not entered into a cooperative agreement under section 49\u2014 (i) the amount of financial assistance provided under this section shall be not more than $500,000 per year; and (ii) the covered entity shall reapply for financial assistance under this section on an annual basis. (2) Application (A) In general A covered entity seeking financial assistance under this section\u2014 (i) may, if the covered entity seeks to enter into or renew a cooperative agreement under section 49, seek that financial assistance in an application submitted by the covered entity with respect to entering into or renewing that cooperative agreement, as applicable; or (ii) if the covered entity does not seek to enter into a, or is not seeking to renew an existing, cooperative agreement under section 49, shall submit to the Administrator an application seeking that financial assistance. (B) Contents With respect to an application seeking financial assistance under this section, whether or not submitted as part of an application under section 49\u2014 (i) the application shall detail the proposed use of the financial assistance, as provided under paragraph (3); and (ii) the Administrator shall evaluate the application using the criteria described in paragraphs (1) and (2) of section 49(d), except that, for purposes of this clause, any reference in such paragraph (1) or (2) to a cooperative agreement under section 49 shall be deemed to be a reference to financial assistance provided under this section. (3) Uses of financial assistance (A) In general (i) Grants (I) In general Subject to clause (ii), an eligible entity to which financial assistance is provided under this section may use that financial assistance to make grants to covered small business concerns to carry out projects that are directed at the objectives described in section 501(d) of the Small Business Investment Act of 1958 ( 15 U.S.C. 695(d) ). (II) Limitation A covered small business concern may not receive more than $20,000, in total, in grants made under subclause (I). (ii) Loans An eligible entity described in any of clauses (ii) through (vi) of section 49(a)(2)(B), or another lender or organization determined appropriate by the Administrator, may use financial assistance provided under this section to make a loan to a covered small business concern with a significantly lower interest rate than is typical, or with a required equity contribution that is lower than is typical, in order to\u2014 (I) reduce the number of loan applications that are denied because of insufficient collateral; (II) decrease the cost of financing for covered small business concerns; (III) increase the number of covered small business concerns that qualify for financing, in light of\u2014 (aa) the difficulties faced by covered small business concerns in accessing conventional financing; and (bb) the historical exclusion of covered small business concerns from credit markets; (IV) bring more lenders into areas that suffer from under-investment; and (V) bridge public and private financing programs to provide covered small business concerns with a continuum of support. (B) No fee or compensation required A covered small business concern that receives a grant or loan made under subparagraph (A) shall not be required to pay a fee, or to otherwise pay any compensation, to the applicable covered entity with respect to that grant or loan. (4) Verification A covered entity that makes a grant or loan to a covered small business concern using financial assistance provided to the covered entity under this section shall verify the legitimacy of that covered small business concern, which may include collecting the following information from the covered small business concern: (A) A description of the history of the covered small business concern and the nature of the business of the covered small business concern. (B) The amount and purpose of the grant or loan. (C) The most recent financial statements of the covered small business concern. (D) Past financial statements or tax returns of the covered small business concern, as determined appropriate by the Administrator. (E) The tax verification described in section 120.191 of title 13, Code of Federal Regulations, or any successor regulation. (F) A business plan provided by the small business concern. (G) Any other material determined appropriate by the Administrator. (d) Program examination (1) In general The Administrator shall\u2014 (A) develop and implement an examination of the grants and loans made with financial assistance provided under this section, under which each covered entity to which financial assistance is provided under this section shall provide to the Administrator\u2014 (i) documentation establishing metrics to measure success on the use of that financial assistance and detailing whether that use satisfied those metrics; (ii) if the covered entity has made loans with financial assistance provided under this section, default rates for those loans; (iii) if the covered entity has made grants with financial assistance provided under this section, failure rates of the covered small business concerns to which those grants were made; and (iv) any other documentation that the Administrator may require; and (B) analyze the results of the examination conducted under subparagraph (A). (2) Use of examination In determining whether a covered entity described in subsection (c)(1)(A) shall continue to receive financial assistance under this section concurrent with the provision of financial assistance pursuant to a cooperative agreement under section 49, or whether to approve a re-application for financial assistance provided under this section that is submitted by a covered entity described in subsection (c)(1)(B)(ii), the Administrator\u2014 (A) shall consider the results of the most recent examination conducted under paragraph (1); and (B) may withdraw financial assistance provided under this section, or reject such a re-application, if\u2014 (i) the Administrator determines that the applicable covered entity has failed to provide information required to be provided (including information provided for the purpose of the annual report by the Administrator under subsection (h)); or (ii) the information provided by the applicable covered entity is inadequate. (3) Study and report Not later than 2 years after the date of enactment of the Strengthening Place-based Access, Resources, and Knowledge Act , the Administrator shall\u2014 (A) conduct a study to determine whether the program examination criteria under this subsection and the reporting requirements under subsection (h) should vary or include other metrics based on the type and location of a project; and (B) submit to Congress a report detailing the results of the study conducted under subparagraph (A). (e) Training and technical assistance The Administrator\u2014 (1) shall provide in-person or online training and technical assistance to each covered entity to which financial assistance is provided under this section at the beginning of the participation of the covered entity in the program established under this section in order to build the capacity of the covered entity and ensure compliance with procedures established by the Administrator; (2) shall ensure that the training and technical assistance described in paragraph (1) is provided at no cost or at a low cost; and (3) may enter into a contract to provide the training or technical assistance described in paragraph (1) with 1 or more organizations with expertise in the entrepreneurial development programs of the Administration, innovation, and entrepreneurial development. (f) Coordination In making a grant or loan with financial assistance provided under this section, a covered entity may coordinate with\u2014 (1) resource and lending partners of the Administration; (2) programs of State and local governments that are concerned with aiding small business concerns; and (3) other Federal agencies, including to provide services to and assist small business concerns in participating in the SBIR and STTR programs, as defined in section 9(e). (g) Publication of information The Administrator shall\u2014 (1) publish information about the program carried out under this section online, including\u2014 (A) on the website of the Administration; and (B) on the social media of the Administration; and (2) request that the resource and lending partners of the Administration and the district offices of the Administration publicize the program carried out under this section. (h) Annual reporting Not later than 1 year after the date on which the Administrator establishes the program under this section, and annually thereafter, the Administrator shall submit to Congress a report on the activities under the program, including\u2014 (1) the number of grants and loans made using the financial assistance provided under this section; (2) the use of the funds from grants and loans described in subparagraph (A); (3) the amount of financial assistance provided under this section that was expended for each job created or retained through the expenditure of that financial assistance; (4) the number of startup, newly established, and growing covered small business concerns to which grants and loans have been made using financial assistance provided under this section (referred to in this subsection as participants ), including a breakdown of the owners of the participants by race, gender, veteran status, and urban versus rural location; (5) the retention rate for participants; (6) the total and median amount of capital accessed by participants, including the type of capital accessed; (7) the total and median number of employees of participants; (8) the number and median wage of jobs created by participants; (9) the number of jobs sustained by participants; and (10) information regarding such other metrics as the Administrator determines appropriate, including coordination with other private or public small business assistance programs. (i) Funding (1) Authorization of appropriations There are authorized to be appropriated such sums as may be necessary to carry out this section. (2) Administrative expenses Of the amount made available to carry out this section for any fiscal year, not more than 10 percent may be used by the Administrator for administrative expenses. .\n#### 6. Regulations\nNot later than 1 year after the date of enactment of this Act, the Administrator of the Small Business Administration shall promulgate regulations to carry out sections 49 and 50 of the Small Business Act, as amended by this Act, which shall include procedures to\u2014\n**(1)**\nverify the proper use of financial assistance provided under each such section, including a grant or loan made under such section 50 with financial assistance provided under that section; and\n**(2)**\nestablish clawback provisions for any instance of fraud committed with respect to any financial assistance, or any grant or loan, described in paragraph (1) of this section.",
      "versionDate": "2026-02-12",
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
        "actionDate": "2026-03-24",
        "text": "Referred to the House Committee on Small Business."
      },
      "number": "8063",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SPARK Act",
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
        "name": "Commerce",
        "updateDate": "2026-03-04T15:46:47Z"
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
      "date": "2026-02-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3876is.xml"
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
      "title": "SPARK Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-03T06:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "SPARK Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Strengthening Place-based Access, Resources, and Knowledge Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-03T06:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Small Business Act to spur entrepreneurial ecosystems in underserved communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-03T06:18:21Z"
    }
  ]
}
```
