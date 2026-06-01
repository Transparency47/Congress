# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1888?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1888
- Title: United States Foundation for International Food Security Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1888
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1888",
    "number": "1888",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "United States Foundation for International Food Security Act of 2025",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-22",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-05-22",
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
          "date": "2025-05-22T17:57:42Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "sponsorshipDate": "2025-05-22",
      "state": "DE"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "AR"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "False",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1888is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1888\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Graham (for himself, Mr. Coons , and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo establish the United States Foundation for International Food Security to leverage private sector investments in order to improve and scale economically viable agricultural production, build food systems to mitigate food shock, reduce malnutrition, and drive economic growth, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the United States Foundation for International Food Security Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. United States Foundation for International Food Security.\nSec. 4. Governance of the Foundation.\nSec. 5. Corporate powers and obligations of the Foundation.\nSec. 6. Outcome-based funding, safeguards, and accountability.\nSec. 7. Ventures, financing, and grants.\nSec. 8. Prohibition of support in countries that support terrorism or violate human rights and of support for sanctioned persons.\nSec. 9. Annual report.\nSec. 10. Authorization of appropriations.\n#### 2. Definitions\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Relations of the Senate ;\n**(2)**\nthe Committee on Agriculture, Nutrition, and Forestry of the Senate;\n**(3)**\nthe Committee on Appropriations of the Senate ;\n**(4)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(5)**\nthe Committee on Agriculture of the House of Representatives ; and\n**(6)**\nthe Committee on Appropriations of the House of Representatives .\n#### 3. United States Foundation for International Food Security\n##### (a) Establishment\n**(1) Finding**\nCongress finds that there has been established, in the District of Columbia, a private, nonprofit corporation, which is known as the United States Foundation for International Food Security (referred to in this Act as the \u201cFoundation\u201d), which is not an agency or establishment of the United States Government.\n**(2) Savings provision**\nNothing in this Act may be construed as\u2014\n**(A)**\nmaking the Foundation an agency or establishment of the United States Government; or\n**(B)**\nmaking any member of the Board of Directors of the Foundation or any officer or employee of the Foundation an employee of the United States.\n**(3) Transfers or consolidation require act of congress**\nNeither the Foundation nor any of its functions, powers, or duties may be transferred to, or consolidated with, any department, agency, or entity of the Federal Government absent an Act of Congress to such effect.\n**(4) Tax-exempt status**\nThe Board shall take all necessary and appropriate steps to ensure that the Foundation is established as an organization described in subsection (c) of section 501 of the Internal Revenue Code of 1986, which exempts the organization from taxation under subsection (a) of such section.\n##### (b) Purposes\nThe purposes of the Foundation are\u2014\n**(1)**\nto accelerate enduring, primarily locally led agriculture investments that foster food security and resilience in the crop, poultry, aquaculture, and livestock industries, that focus on building economically resilient food systems by investing in\u2014\n**(A)**\nfinancing for, distribution of, and training around key inputs required for increasing crop and animal productivity, distribution, and profits;\n**(B)**\ninfrastructure, such as irrigation, warehousing, storage, and food processing, to improve food production and market access through better product quality and the prevention of food loss;\n**(C)**\napplied agricultural research; and\n**(D)**\neconomically viable technology deployment that reduces hunger and increases agriculture production or distribution methods;\n**(2)**\nto prevent unnecessary or inefficient vetting processes, due diligence, project financing, or evaluation reviews by seeking out partnerships and contracting with existing government and nongovernmental entities that have proven track records;\n**(3)**\nto deploy and scale technology and innovation to accelerate food security and agricultural-led economic growth that reduces global hunger and malnutrition;\n**(4)**\nto coordinate with the United States Foundation for International Conservation;\n**(5)**\nto advance the national security interests of the United States;\n**(6)**\nto complement international and government investment and technical assistance mechanisms, such as those employed or managed by the United States International Development Finance Corporation, and United States Government food security programs, to jointly catalyze private and public sector engagement, spur agricultural-led economic growth, and strengthen local food and nutrition systems; and\n**(7)**\nto ensure the effective use of United States taxpayer dollars and the prioritization of United States foreign policy interests.\n#### 4. Governance of the Foundation\n##### (a) Board of Directors\n**(1) Governance**\nThe Foundation shall be governed by a voting Board of Directors (referred to in this section as the Board ) that\u2014\n**(A)**\nshall not exceed 15 members; and\n**(B)**\nmay consult with a nonvoting Board of Advisors when making decisions related to the Foundation\u2019s work.\n**(2) Qualifications**\nIndividuals appointed to the Board shall include individuals who are knowledgeable and experienced in matters relating to\u2014\n**(A)**\nagricultural production, livestock, land management, or forestry;\n**(B)**\nagricultural economics, business development, technology deployment, market access, agribusinesses (including food companies), market access, supply chains, infrastructure, or commodities groups;\n**(C)**\ninternational finance and multilateral governance;\n**(D)**\noutcome-based and impact funding concepts, including the role of impact evaluations and data collection, to measure the progress of ventures, and innovative grantee or investee selection and funding structures;\n**(E)**\nagricultural research and development; or\n**(F)**\nnational security.\n**(3) Limitation on political affiliation**\nThe Directors of the Board shall include members of both major political parties in a relatively equal number.\n**(4) Chairperson**\nA quorum of the voting Directors of the Board shall elect a Chairperson, who shall serve in such position for a 4-year term.\n**(5) Voting**\nAll voting Directors of the Board shall have equal voting rights.\n**(6) Terms; vacancies**\n**(A) Terms**\nThe term of service of each Director may not exceed 5 years and is renewable for not more than 1 additional 5-year term.\n**(B) Vacancies**\nAny vacancy in the membership of the appointed Directors of the Board\u2014\n**(i)**\nshall be filled in accordance with the bylaws of the Foundation;\n**(ii)**\ndoes not affect the power of the remaining appointed Directors to execute the duties of the Board; and\n**(iii)**\nshall be filled by an individual selected in accordance with the bylaws of the Board.\n**(7) Quorum**\nA majority of the current membership of the Board shall constitute a quorum for the transaction of Foundation business.\n**(8) Meetings**\n**(A) In general**\nThe Board shall meet not less frequently than twice per year.\n**(B) Authority**\nThe Board shall maintain full control and decision-making authority of the Foundation.\n**(C) Removal**\nAny Director may be removed from the Board if\u2014\n**(i)**\nthe Director is absent from 2 consecutive regularly scheduled meetings without reasonable cause; or\n**(ii)**\nthe Board, by a majority vote of the other Board members, determines that such Director should be removed from the Board.\n**(9) Reimbursement of expenses**\nDirectors of the Board shall serve without pay, but may be reimbursed for the actual and necessary traveling and subsistence expenses incurred by such members in the performance of their duties on behalf of the Foundation.\n**(10) Not Federal employees**\nAppointment as a Director of the Board shall not constitute employment by, or the holding of an office of, the United States Government for purposes of any Federal law.\n**(11) Duties**\nThe Board shall\u2014\n**(A)**\nestablish bylaws for the Foundation;\n**(B)**\nprovide overall direction for the activities of the Foundation and establish priority activities;\n**(C)**\ncarry out any other necessary activities of the Foundation;\n**(D)**\nhire and evaluate the performance of the Executive Director of the Foundation; and\n**(E)**\ntake steps to limit the Foundation\u2019s administrative expenses to the extent practicable and in accordance with industry standards.\n**(12) Bylaws**\nThe bylaws of the Foundation shall require the Board to establish\u2014\n**(A)**\npolicies for the selection of Directors of the Board, Members of the Board of Advisors, and officers, employees, agents, and contractors of the Foundation;\n**(B)**\npolicies, including ethical standards, for\u2014\n**(i)**\nthe acceptance, solicitation, and disposition of donations and grants to the Foundation; and\n**(ii)**\nthe use and disposition of the assets of the Foundation;\n**(C)**\npolicies that subject all employees, fellows, trainees, and other agents of the Foundation (including all of the Directors of the Board and all of the Members of the Board of Advisors) to prevailing conflict of interest standards for the industry;\n**(D)**\nthe specific duties of the Executive Director of the Foundation;\n**(E)**\npolicies for winding down the activities of the Foundation upon termination, including a plan\u2014\n**(i)**\nto return unobligated appropriations to the Department of the Treasury; and\n**(ii)**\nto donate unspent private and philanthropic contributions to projects that align with the goals and requirements described in this Act; and\n**(F)**\nspecific policies and requirements governing project criteria, measurable outcomes, impact evaluations, and country eligibility requirements.\n##### (b) Board of Advisors composition\n**(1) In general**\nThe nonvoting Board of Advisors may be composed of, at a minimum\u2014\n**(A)**\nmembers of the executive branch of the Federal Government from departments and agencies with expertise that would benefit the Foundation;\n**(B)**\nthe Secretary of State, or the Secretary's designee;\n**(C)**\nthe Chief Executive Officer of the United States International Development Finance Corporation, or his or her designee; and\n**(D)**\n2 deans or other designated faculty members of United States land-grant colleges or universities that have an international agriculture program.\n**(2) Duties**\nThe Board of Advisors shall provide advice and consultation to the Board in accordance with the bylaws of the Foundation.\n**(3) Removal**\nThe Board of Directors may remove an Advisor from the Board of Advisors by majority vote.\n##### (c) Procedures\n**(1) Initial meeting**\nThe Board shall hold its initial meeting not later than 120 days after the date of the enactment of this Act.\n**(2) Organizing principles; appointment of executive director**\nThe Directors of the Board shall name an Executive Director of the Foundation not later than 120 days after the date of the initial meeting of the Board.\n##### (d) Executive Director; staff\n**(1) Executive director**\nThe Board shall hire a qualified individual to serve, at the pleasure of the Board, as the Executive Director of the Foundation.\n**(2) Foundation staff**\nOfficers and employees of the Foundation\u2014\n**(A)**\nmay not be employees of, or hold any office in, the United States Government;\n**(B)**\nshall be appointed without regard to the provisions of\u2014\n**(i)**\ntitle 5, United States Code, governing appointments in the competitive service; and\n**(ii)**\nchapter 51 and subchapter III of chapter 53 of such title, relating to classification and General Schedule pay rates; and\n**(C)**\nshall receive a salary that is commensurate with the salaries of similar positions in similar foundations.\n##### (e) Limitation; conflicts of interests\n**(1) Political participation**\nThe Foundation may not participate or intervene in any political activities on behalf of any candidate for public office in any country.\n**(2) Financial interests**\nAll Directors of the Board, Advisors, officers, and employees of the Foundation are subject to industry standard conflicts of interest protocols set forth in the Foundation bylaws.\n#### 5. Corporate powers and obligations of the Foundation\n##### (a) General authorities\nThe Foundation\u2014\n**(1)**\nmay conduct business throughout the States, territories, and possessions of the United States and in foreign countries;\n**(2)**\nshall have its principal offices in the Washington, DC, metropolitan area; and\n**(3)**\nshall continuously maintain a designated agent in Washington, DC, who is authorized to accept notice or service of process on behalf of the Foundation.\n##### (b) Authorities\nIn addition to powers explicitly authorized under this Act, the Foundation, in order to carry out the purposes described in section 3(b), shall have the usual powers of a corporation headquartered in Washington, DC, including the authority\u2014\n**(1)**\nto accept, receive, solicit, hold, administer, and use any gift, devise, or bequest, either absolutely or in trust, or real or personal property or any income derived from such gift or property, or other interest in such gift or property;\n**(2)**\nto acquire by donation, gift, devise, purchase, or exchange any real or personal property or interest in such property;\n**(3)**\nunless otherwise required by the instrument of transfer, to sell, donate, lease, invest, reinvest, retain, or otherwise dispose of any property or income derived from such property;\n**(4)**\nto complain and defend itself in any court of competent jurisdiction (except that the Directors of the Board shall not be personally liable, except for gross negligence);\n**(5)**\nto enter into legal arrangements with public agencies, private organizations, and persons and to make such payments as may be necessary to carry out the purposes of such contracts or arrangements; and\n**(6)**\nto engage in funding activities, which may include structured or project financing, grants, equity (provided that returns flow back to the Foundation), and concessional lending, for eligible projects, in accordance with section 7.\n##### (c) Federal funds\n**(1) In general**\nThe Foundation may\u2014\n**(A)**\nhold Federal funds made available, but not immediately disbursed; and\n**(B)**\nuse any interest or other investment income earned on such Federal funds to carry out the purposes of the Foundation under this Act.\n**(2) Limitation**\nInvestments by the Foundation made with Federal funds may only be made in\u2014\n**(A)**\ninterest-bearing obligations of the United States; or\n**(B)**\nobligations guaranteed as to both principal and interest by the United States.\n##### (d) Limitation of public liability\nThe United States shall not be liable for any debts, defaults, acts, or omissions of the Foundation. The Federal Government shall be held harmless from any damages or awards ordered by a court against the Foundation.\n#### 6. Outcome-based funding, safeguards, and accountability\n##### (a) Outcome-Based funding\n**(1) In general**\nThe Foundation shall establish a funding strategy that sets targets based on measurable outcomes to be improved in populations served through its investments, including\u2014\n**(A)**\nidentifying and regularly reviewing any such outcomes that advance the purposes described in section 3(b), such as increased crop and animal productivity, increased profit to farmers, or decreased hunger rates; and\n**(B)**\na portfolio, multi-year, approach to Foundation investments in which the failure of any specific program to achieve target outcomes is acceptable if the overall portfolio of projects meets target outcomes.\n**(2) Financing and evaluation process**\nThe Foundation shall establish an efficient and streamlined financing and evaluation process that\u2014\n**(A)**\nprioritizes the achievement of defined outcomes;\n**(B)**\nassesses risk of corruption and employs a strategy to counter corruption;\n**(C)**\nprioritizes funding ventures with partners that are primarily locally based or locally run organizations, entities, and businesses that\u2014\n**(i)**\nachieve such outcomes; and\n**(ii)**\ndemonstrate an ability to sustain the financed project; and\n**(D)**\nfocuses venture evaluations on assessing such outcomes and minimizing unnecessary reporting on project activities.\n##### (b) Accountability\n**(1) Impact evaluations**\nThe achievement of venture outcomes shall be determined through impact evaluations that include a comparison group to determine any measured improvements that are attributable to the funded venture.\n**(2) Methodology assessments**\nFoundation staff may assess the methodology used by grantees or investees that are already running impact evaluations to increase efficiency, and such evaluations may be accepted in place of additional evaluations.\n**(3) Dedicated funding**\nAny grantee or investee that lacks impact evaluation capacity may receive dedicated funding to support in-house evaluations or to contract with independent, external evaluators.\n**(4) Third-party evaluations**\nThe Foundation may pay for third-party evaluations of any grantee's project to verify the results derived from an in-house evaluation.\n##### (c) Safeguards\nThe Foundation shall develop, and incorporate into any agreement for support provided by the Foundation, appropriate safeguards, policies, and guidelines, consistent with internationally recognized best practices.\n##### (d) Independent accountability mechanism\nThe Foundation shall establish or contract for a transparent and independent accountability mechanism, consistent with best practices, which shall provide\u2014\n**(1)**\na compliance review function that assesses whether Foundation-supported ventures adhere to the requirements developed pursuant to subsection (a);\n**(2)**\na dispute resolution function for resolving and remedying concerns between venture implementers regarding the impacts of specific Foundation-supported ventures with respect to such standards; and\n**(3)**\nan advisory function that reports to the Board regarding ventures, policies, and practices.\n#### 7. Ventures, financing, and grants\n##### (a) Venture funding requirements\n**(1) In general**\nThe Foundation shall award funding, which may include project financing, credit risk insurance, grants, concessional lending, or credit, in accordance with this section, for eligible projects described in paragraph (2) that\u2014\n**(A)**\nincrease agricultural productivity and incomes; and\n**(B)**\nensure food security is achieved and sustained, while supporting farmers moving beyond subsistence agriculture to growing higher value crops that can be sold for profit.\n**(2) Eligible ventures**\nA venture qualifies as an eligible venture if the venture seeks\u2014\n**(A)**\nto have cost matching from sources other than the United States Government;\n**(B)**\nto incorporate a set of key independently verified outcomes, which shall be measured by rigorous impact evaluations, such as measuring attributable increases in agricultural yields, infrastructure, or any other eligible use;\n**(C)**\nto not substantially duplicate the work of other funders or institutions or displace current profit-making ventures;\n**(D)**\nto leverage existing infrastructure and community-led development to allow for the immediate launch of ventures;\n**(E)**\nto advance the national security interests of the United States;\n**(F)**\nto demonstrate\u2014\n**(i)**\nthe ability to financially and operationally maintain and build on the outcomes or mission of the venture after the Foundation funding has ended; or\n**(ii)**\na plan to strengthen the capacity of, and transfer skills and technologic tools to, local enterprises, organizations, or institutions to manage projects and other funded entities after the Foundation funding has been expended; and\n**(G)**\nto consider projects that meet the highest needs of food insecure populations based on food security, agriculture, and malnutrition assessments.\n##### (b) Eligible countries for ventures\nBefore entering into any venture agreement pursuant to this section, the Board shall\u2014\n**(1)**\nestablish criteria to determine whether a country is eligible to receive funding for such a venture; and\n**(2)**\nidentify ventures to receive support that\u2014\n**(A)**\nadvance the national security priorities of the United States;\n**(B)**\nhave demonstrated leadership to modernize the country's agricultural food systems, in partnership with the private sector; and\n**(C)**\nare committed\u2014\n**(i)**\nto making policy reforms to help transform, scale, and build enduring food systems;\n**(ii)**\nto cofinancing and sustaining long-term projects implemented by the Foundation; and\n**(iii)**\nto collaborating with stakeholders\u2014\n**(I)**\nto increase agricultural production and crop yields;\n**(II)**\nto scale resilient food systems; and\n**(III)**\nto improve food safety, processing, logistics, and supply chain processes for input and output markets.\n##### (c) Funding authorized\n**(1) In general**\nIn order to maximize the impact of the funding authorized under this section, the Foundation should\u2014\n**(A)**\ncoordinate with other international public and private donors or investors and local organizations active in food security to the extent possible; and\n**(B)**\nseek additional financial and nonfinancial contributions and commitments for its projects from host governments and other organizations.\n**(2) Funding criteria**\nFunding awarded pursuant to this section\u2014\n**(A)**\nshall be provided to ventures that demonstrate progress, during the funding period, in achieving clearly identified performance indicators and outcomes defined in the project agreement, which may include\u2014\n**(i)**\nincreasing agricultural or food production through agriculture research and the competitive delivery of market-based financing, distribution and extension services, and supporting technology commercialization and adoption through such services;\n**(ii)**\nimproving the nutritional status of intended beneficiaries by\u2014\n**(I)**\nincreasing the production, availability, and access of nutritious foods domestically;\n**(II)**\npromoting highly nutritious foods, diet diversification, and nutritional behaviors that improve maternal and child health; and\n**(III)**\nsupporting the expansion of producer market opportunities;\n**(iii)**\nbuilding resilient food systems to help mitigate against future food shocks among vulnerable populations and households; and\n**(iv)**\nidentifying additional revenue sources or financing mechanisms to meet the recurring costs of ventures by serving as a conduit between institutional investors and the agribusiness sector; and\n**(B)**\nmay be terminated if the Board determines that the country receiving such funding\u2014\n**(i)**\nis not meeting applicable requirements under this Act;\n**(ii)**\nis not making progress in achieving the key performance indicators described in the project agreement; or\n**(iii)**\nis not advancing United States national security priorities.\n#### 8. Prohibition of support in countries that support terrorism or violate human rights and of support for sanctioned persons\n##### (a) In general\nThe Foundation may not provide support for any government, or any entity owned or controlled by a government, if the Secretary of State determines that such government\u2014\n**(1)**\nhas repeatedly provided support for acts of international terrorism, as determined under\u2014\n**(A)**\nsection 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) );\n**(B)**\nsection 620A(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371(a) );\n**(C)**\nsection 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or\n**(D)**\nany other relevant provision of law;\n**(2)**\nhas repeatedly engaged with any organizations designated as foreign terrorist organizations by the Secretary in accordance with section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ); or\n**(3)**\nhas engaged in a consistent pattern of gross violations of human rights, as determined under section 116(a) or 502B(a)(2) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151n(a) and 2304(a)(2)) or any other relevant provision of law.\n##### (b) Prohibition of support for sanctioned persons\nThe Foundation may not engage in any dealing prohibited under United States sanctions laws or regulations, including dealings with persons on the list of specially designated persons and blocked persons maintained by the Office of Foreign Assets Control of the Department of the Treasury, except to the extent otherwise authorized by the Secretary of State or the Secretary of the Treasury.\n##### (c) Waiver\nThe President may waive the application of subsections (a) and (b) with respect to any government, or any entity owned or controlled by a government, by notifying the appropriate congressional committees of the intention to exercise such waiver not later than 45 days before the waiver is scheduled to take effect.\n#### 9. Annual report\nNot later than 2 years after the date of the enactment of this Act, and annually thereafter by March 31st of any year during which the Foundation is operational, the Executive Director of the Foundation shall submit to the appropriate congressional committees a report that\u2014\n**(1)**\nhas been approved by the Board of Directors;\n**(2)**\ncontains the expectations of the year ahead; and\n**(3)**\ndescribes\u2014\n**(A)**\nthe goals of the Foundation for the upcoming year, including areas to increase operational efficiency and further advance United States policy objectives and national security;\n**(B)**\nlessons learned and best practices developed through projects funded by the Foundation during the prior fiscal year;\n**(C)**\na project-specific and a portfolio-level report describing\u2014\n**(i)**\nthe progress achieved against key performance indicators and the outcomes described in section 6, and\n**(ii)**\nhow such progress will benefit the American taxpayer;\n**(D)**\nan assessment of\u2014\n**(i)**\nwhether the grant making and financing processes are effective and expeditious;\n**(ii)**\nhow any necessary additional efficiencies can be built into future project selection; and\n**(iii)**\nwhether project evaluations are successfully measuring outcomes;\n**(E)**\nhow the funding and selected projects authorized under this Act were publicized in the selected country to expand recognition for the United States; and\n**(F)**\nan annual financial report from an independent auditor.\n#### 10. Authorization of appropriations\n##### (a) In general\nUsing funds appropriated to the Department of State to carry out chapter 4 of part II of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2346 et seq. ), the Secretary of State is authorized to award an annual grant to the Foundation to enable the Foundation to carry out the purposes specified in section 3(b).\n##### (b) Cost matching requirement\nAmounts authorized to be appropriated pursuant to subsection (a) shall be made available, on a cost matching basis, to the maximum extent practicable, from sources other than the United States Government.\n##### (c) Consultation requirement\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Executive Director of the Foundation shall consult with the Committee on Appropriations of the Senate , the Committee on Foreign Relations of the Senate , the Committee on Agriculture, Nutrition, and Forestry of the Senate , the Committee on Appropriations of the House of Representatives , the Committee on Agriculture of the House of Representatives and the Committee on Foreign Affairs of the House of Representatives regarding the implementation of this Act and the proposed activities of the Foundation.\n##### (d) Prohibition of use of grants for lobbying expenses\nNo grant funds provided by the Foundation pursuant to section 7 may be used for any activity intended to influence legislation pending before Congress.",
      "versionDate": "2025-05-22",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-06-20T18:46:30Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1888is.xml"
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
      "title": "United States Foundation for International Food Security Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-11T03:53:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States Foundation for International Food Security Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-11T03:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish the United States Foundation for International Food Security to leverage private sector investments in order to improve and scale economically viable agricultural production, build food systems to mitigate food shock, reduce malnutrition, and drive economic growth, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-11T03:48:42Z"
    }
  ]
}
```
