# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/853?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/853
- Title: INNOVATE Act
- Congress: 119
- Bill type: S
- Bill number: 853
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-04-07T17:48:22Z
- Update date including text: 2026-04-07T17:48:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-23 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Small Business and Entrepreneurship.
- 2025-07-23 - Committee: Committee on Small Business and Entrepreneurship. Hearings held.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/853",
    "number": "853",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "E000295",
        "district": "",
        "firstName": "Joni",
        "fullName": "Sen. Ernst, Joni [R-IA]",
        "lastName": "Ernst",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "INNOVATE Act",
    "type": "S",
    "updateDate": "2026-04-07T17:48:22Z",
    "updateDateIncludingText": "2026-04-07T17:48:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-23",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
      "committees": {
        "item": {
          "name": "Small Business and Entrepreneurship Committee",
          "systemCode": "sssb00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Small Business and Entrepreneurship. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
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
            "date": "2025-07-23T18:30:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-05T19:30:00Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-03-05T16:37:34Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Small Business and Entrepreneurship Committee",
      "systemCode": "sssb00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s853is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 853\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Ms. Ernst introduced the following bill; which was read twice and referred to the Committee on Small Business and Entrepreneurship\nA BILL\nTo improve the SBIR and STTR programs under the Small Business Act, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Investing in National Next-Generation Opportunities for Venture Acceleration and Technological Excellence or the INNOVATE Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nTITLE I\u2014Promoting Transition for Battle-Ready Technologies\nSec. 101. Enhancing small business success in the STTR program.\nSec. 102. Phase II strategic breakthrough funding.\nSec. 103. Implementation briefings.\nSec. 104. Fixed-price contracts.\nTITLE II\u2014Encouraging Small Business Innovation in All of America\nSec. 201. Encouraging new SBIR and STTR entrants.\nSec. 202. Combating discriminatory practices in the SBIR and STTR programs.\nTITLE III\u2014Streamlining Participation in the SBIR and STTR Programs\nSec. 301. Definition of open topics.\nSec. 302. Reducing administrative burden.\nTITLE IV\u2014Protecting American Innovation from Adversarial Influence\nSec. 401. Definition of foreign risk.\nSec. 402. Bolstering research security of SBIR and STTR awards.\nSec. 403. Strengthening the due diligence program to assess security risks.\nSec. 404. Strengthening agency recovery authority.\nSec. 405. Best practices on investor informational rights.\nSec. 406. GAO report.\nTITLE V\u2014Simplifying SBIR-STTR Commercialization Standards\nSec. 501. Streamlining transition and commercialization rate benchmarks.\nSec. 502. Improving direct to Phase II authorities.\nSec. 503. Improving SBIR-STTR data collection.\nSec. 504. Streamlining program administration.\nSec. 505. Extending SBIR and STTR authorization.\n#### 2. Definitions\nIn this Act, the terms Phase I , Phase II , Phase III , SBIR , and STTR have the meanings given those terms in section 9(e) of the Small Business Act ( 15 U.S.C. 638(e) ).\nI\nPromoting Transition for Battle-Ready Technologies\n#### 101. Enhancing small business success in the STTR program\nSection 9 of the Small Business Act ( 15 U.S.C. 638 et seq. ) is amended\u2014\n**(1)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (6)\u2014\n**(i)**\nin subparagraph (A), by adding and at the end; and\n**(ii)**\nby striking subparagraphs (B) and (C) and inserting the following:\n(B) opportunities for follow-on funding in Phases II and III of the SBIR program; ; and\n**(B)**\nin paragraph (7)\u2014\n**(i)**\nby striking 40 and inserting 50 ; and\n**(ii)**\nby striking 30 and inserting 20 ;\n**(2)**\nin subsection (f)(1)\u2014\n**(A)**\nin subparagraph (H), by striking and at the end;\n**(B)**\nin subparagraph (I), by striking and each fiscal year thereafter, and inserting ; and ; and\n**(C)**\nby adding at the end the following:\n(J) not less than 3.45 percent of such budget in fiscal year 2026 and every year thereafter, ; and\n**(3)**\nin subsection (n)\u2014\n**(A)**\nin paragraph (1)(B)\u2014\n**(i)**\nin clause (iv), by striking and at the end;\n**(ii)**\nin clause (v), by striking and each fiscal year thereafter. and inserting ; and ; and\n**(iii)**\nby adding at the end the following:\n(vi) not less than 0.20 percent for fiscal year 2026 and each fiscal year thereafter. ;\n**(B)**\nby redesignating paragraphs (2) and (3) as paragraphs (3) and (4), respectively; and\n**(C)**\nby inserting after paragraph (1) the following:\n(2) Purpose of STTR program (A) In general Each Federal agency shall use its STTR budget to fund small business concerns conducting fundamental, basic, or other scientific research that stands to benefit most from partnerships with eligible research institutions. (B) DoD and NASA The Department of Defense and the National Aeronautics and Space Administration shall use their STTR budget to solely fund research at technology readiness levels 1, 2, and 3. .\n#### 102. Phase II strategic breakthrough funding\n##### (a) In general\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nby redesignating subsection (y) as paragraph (3), adjusting the margins accordingly, and moving it so as to appear in subsection (ff) after paragraph (2);\n**(2)**\nin subsection (aa), by adding at the end the following:\n(6) Strategic breakthrough allocation The Department of Defense or its components shall not be required to receive a waiver from the Administrator to award a small business concern not more than $30,000,000 when using funds made available under a strategic breakthrough allocation. ;\n**(3)**\nin subsection (ff)\u2014\n**(A)**\nin the subsection heading, by striking and STTR and inserting Phase II ;\n**(B)**\nin paragraph (1), by striking or Phase II STTR award ; and\n**(C)**\nin paragraph (3), as so redesignated\u2014\n**(i)**\nin the paragraph heading, by striking Commercialization Readiness Program and inserting Strategic Breakthrough Awards ;\n**(ii)**\nin subparagraph (A), as so redesignated\u2014\n**(I)**\nin the first sentence, by striking create and administer a Commercialization Readiness Program and inserting provide funding ; and\n**(II)**\nin the second sentence, by striking create and administer a Commercialization Program under this subsection and inserting provide funding under this paragraph ;\n**(iii)**\nin subparagraph (B), as so redesignated\u2014\n**(I)**\nin the first sentence, by striking In carrying out the Commercialization Readiness Program and inserting the following:\n(i) In general In carrying out this paragraph ;\n**(II)**\nin clause (i), as so designated\u2014\n**(aa)**\nby striking shall identify and inserting\nshall\u2014 (I) identify ;\n**(bb)**\nin subclause (I), as so designated, by striking the period at the end and inserting a semicolon; and\n**(cc)**\nby adding at the end the following:\n(II) ensure, in collaboration with SBIR program managers of each component of the Department of Defense, that research programs identified under subclause (I) are analyzed within the programming and budgeting process as budget requests are developed; and (III) provide to the Committee on Small Business and Entrepreneurship of the Senate and the Committees on Small Business and Science, Space, and Technology of the House of Representatives information on the integration of SBIR and STTR awardees in budget rollouts for research, development, testing, and evaluation activities. ; and\n**(III)**\nby adding at the end the following:\n(ii) Award Under this paragraph, a funding agreement may be awarded to a small business concern by the Department of Defense using funds made available under a strategic breakthrough allocation, as defined in subparagraph (C)(i). ;\n**(iv)**\nby striking subparagraphs (C), (D), and (E), as so redesignated, and inserting the following:\n(C) Funding parameters (i) Definition In this subparagraph, the term strategic breakthrough allocation means a required expenditure amount for the Department of Defense within the SBIR allocation under subsection (f)(1) for fiscal year 2026 and every fiscal year thereafter of not less than 0.25 percent of the extramural budget for research or research and development designated for the Department of Defense. (ii) Requirements In the case of a Phase II agreement that is awarded to a small business concern by the Department of Defense using funds made available under a strategic breakthrough allocation, the following requirements shall apply: (I) Award size and period of performance The Department of Defense may award not more than 1 award of not more than $30,000,000 per small business concern, including its affiliates, spinouts, or subsidiaries, from the strategic breakthrough allocation with a period of performance of not more than 48 months. (II) Small business concern requirements The small business concern shall\u2014 (aa) have been awarded not less than 1 prior Phase II award under the SBIR program; (bb) demonstrate not less than 100 percent matching funds through new outside capital or amounts awarded by the Department of Defense under a program other than Phase I and II of the SBIR or STTR program as a result of an award using funds made available under a strategic breakthrough allocation; (cc) have been awarded not more than $50,000,000 in cumulative Department of Defense contracts or awards; and (dd) only be eligible for an award from the strategic breakthrough allocation if the product, process, or technology of the small business concern\u2014 (AA) meets a necessary level of readiness and has a commitment for inclusion in a program objective memorandum from an official with the rank of program executive officer or higher in an acquisition organization of the Department of Defense; (BB) is an effective solution, as determined by market research; and (CC) will meet high priority military requirements or operational needs of a military department through a successful transition and into the acquisition process. (III) Deadline The Department of Defense shall complete any contract awards using strategic breakthrough allocation funds not later than 90 days after receiving a proposal from a small business concern for the award. (IV) Eligible activities Eligible activities by a small business concern using strategic breakthrough allocation funds are\u2014 (aa) design for manufacturing; (bb) establishing manufacturing facilities, tooling, and supply chain capacity; (cc) buying raw materials or inventory; (dd) the integration of products with open interoperability standards; (ee) testing, evaluation, and certification of low-rate production units; and (ff) the purchase of production units and maintenance. (V) Selection criteria In making awards, the Department of Defense shall consider\u2014 (aa) the potential of the small business concern to\u2014 (AA) advance the national security capabilities of the United States; (BB) provide new technologies or processes, or new applications of existing technologies, that will enable new alternatives to existing programs; (CC) provide future cost savings; and (DD) enhance the lethality and efficiency of the United States military; (bb) whether a major system or customer in the Department of Defense has expressed intent to purchase and integrate technology from the small business concern into its operations; and (cc) such other criteria that the Department of Defense determines to be appropriate. (D) Acquisition mechanism The Department of Defense shall establish a mechanism, such as a major system, to provide small business concerns with direct access to program and requirements offices throughout the Department of Defense that may purchase technology from small business concerns under Phase III of the SBIR program of the Department of Defense. (E) Operational needs The Department of Defense shall allow services to provide operational needs statements directly to chiefs of requirements offices. ; and\n**(v)**\nin subparagraph (F), as so redesignated\u2014\n**(I)**\nby amending clause (i) to read as follows:\n(i) set a goal to substantively increase the number of Phase II SBIR contracts awarded by the Secretary that lead to technology transition into programs of record or fielded systems in fiscal year 2028 compared to fiscal year 2025; and ;\n**(II)**\nby striking clause (ii);\n**(III)**\nby redesignating clause (iii) as clause (ii); and\n**(IV)**\nin clause (ii), as so redesignated\u2014\n**(aa)**\nin subclause (I), by adding and at the end;\n**(bb)**\nin subclause (II)\u2014\n(AA)\nby striking through the Commercialization Readiness Program and inserting under a strategic breakthrough allocation ; and\n(BB)\nby striking ; and and inserting a period; and\n**(cc)**\nby striking subclause (III); and\n**(4)**\nby redesignating subsection (xx), entitled Additional Provisions Relating to Solicitation Topics , as subsection (y), and moving it so as to appear after subsection (x).\n##### (b) Technical and conforming amendments\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (i)(1), by striking subsection (y) and inserting subsection (ff)(3) ;\n**(2)**\nin subsection (mm)(1)(D), by striking subsection (y) and inserting subsection (ff)(3) ; and\n**(3)**\nin subsection (tt), by striking (y)(6)(C) and inserting (ff)(3)(F)(ii) .\n#### 103. Implementation briefings\nNot later than 60 days after the date of enactment of this Act, and on a recurrent basis until implementation is complete, the Secretary of Defense shall brief the Committee on Small Business and Entrepreneurship of the Senate and the Committee on Small Business and the Committee on Science, Space, and Technology of the House of Representatives on the implementation of paragraph (3) of section 9(ff) of the Small Business Act ( 15 U.S.C. 638(ff) ), as added by section 102.\n#### 104. Fixed-price contracts\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ) is amended\u2014\n**(1)**\nin subsection (f), by adding at the end the following:\n(5) Fixed-price contract Any funding agreement that is a contract made with expenditures allocated to the SBIR program under paragraph (1) shall be a firm-fixed-price contract (as defined in section 16.202 of the Federal Acquisition Regulation), unless, on a case-by-case basis, the head of the awarding Federal agency makes a written determination to utilize a different contract structure. ; and\n**(2)**\nin subsection (n), as amended by section 101, by adding at the end the following:\n(5) Fixed-price contract Any funding agreement that is a contract made with expenditures allocated to the STTR program under paragraph (1) shall be a firm-fixed-price contract (as defined in section 16.202 of the Federal Acquisition Regulation), unless the head of the awarding Federal agency makes a written determination to utilize a different contract structure. .\nII\nEncouraging Small Business Innovation in All of America\n#### 201. Encouraging new SBIR and STTR entrants\n##### (a) In general\n**(1) Encouraging new SBIR and STTR entrants**\nSection 9(jj) of the Small Business Act ( 15 U.S.C. 638(jj) ) is amended to read as follows:\n(jj) Encouraging new SBIR and STTR entrants (1) Optimizing SBIR and STTR funding A small business concern, including its affiliates, spinouts, or subsidiaries, may not apply to a Phase I or Phase II solicitation under an SBIR or STTR program if the small business concern, including its affiliates, spinouts, or subsidiaries, has previously received over $75,000,000 in funding from SBIR or STTR Phase I and Phase II awards. (2) Primary investigators An individual may not concurrently serve as the primary investigator on more than 1 proposal to a single Phase I solicitation or a single Phase II solicitation. (3) Phase I size standard A small business concern applying for a Phase I award may not have annual receipts (as defined in section 121.104 of title 13, Code of Federal Regulations, or any successor regulation) of more than $40,000,000 for the most recent fiscal year. .\n**(2) Conforming amendment**\nSection 9(tt)(1)(A) of the Small Business Act ( 15 U.S.C. 638(tt)(1)(A) ) by striking , (jj)(6) .\n##### (b) Phase 1A program\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (e)(4)\u2014\n**(A)**\nin subparagraph (A), by striking subparagraph (B) and inserting subparagraph (C) ;\n**(B)**\nby redesignating subparagraphs (B) and (C) as subparagraphs (C) and (D); and\n**(C)**\nby inserting after subparagraph (A), the following:\n(B) a 1A phase for the same purposes as the first phase described under subparagraph (A) and intended to increase accessibility to the program for new entrants, with proposals submitted pursuant to only SBIR open topic announcements; ; and\n**(2)**\nby amending subsection (pp) to read as follows:\n(pp) Phase 1A awards (1) Sense of Congress It is the sense of Congress that\u2014 (A) Phase 1A funds will bring thousands of new small business concerns committed to commercialization of critical technologies into the SBIR program; and (B) in order for participating agencies to benefit from the full scope of American innovation and identify the most promising solutions to scale, Phase 1A awards should fund the strongest technologies in a topic area regardless of\u2014 (i) the location of the small business concern within the United States; or (ii) the educational background of the principal investigator. (2) Authorization The head of each agency with an SBIR program shall allocate not less than 2.5 percent of funding for the SBIR program of the agency to Phase 1A awards. (3) Solicitation A solicitation issued under this subsection shall be conducted as an open topic announcement, as defined in subsection (e). (4) Eligibility In order to be eligible for an award under this subsection, a small business concern, including its affiliates, spinouts, or subsidiaries, shall not have previously received an SBIR or STTR award. (5) Proposal (A) In general A proposal submitted in response to a solicitation under this subsection shall consist of a report of no more than 2 pages in length and shall contain the criteria described in subparagraph (B). (B) Criteria (i) Identification of problem The small business concern shall describe the problem that the proposal is intended to address for the awarding agency and any commercial customer. (ii) Description of solution The small business concern shall describe the proposed solution, including the technical basis for the solution to demonstrate how the solution would address the problem described in the proposal, including the level of maturity of the solution at the time of the proposal. (iii) Impact of the solution The small business concern shall describe how adoption of the proposed solution would produce potential time savings, cost savings, risk reduction, improvement of mission outcomes, or any other beneficial impact for the awarding agency and any commercial customer. (iv) Differentiation The small business concern shall\u2014 (I) identify the state of solutions in use at the time of the proposal to address the problem described in the proposal; and (II) explain how the proposed solution is a unique and novel solution. (v) Commercialization strategy The small business concern shall\u2014 (I) describe how the small business concern intends to fund the proposed solution; and (II) explain the market for the proposed solution, including the intended Government and commercial end users. (6) Award limits (A) Number of awards A small business concern or principal investigator is eligible for not more than 1 Phase 1A award. (B) Amount An award made under this subsection shall be for not more than $40,000. (7) Notification of selection or non-selection Each agency shall notify each small business concern of the award decision of the agency on any proposal submitted by the small business concern not later than 90 days after the date on which the solicitation closes. (8) Application for Phase II award (A) Eligibility A small business concern that receives a Phase 1A award shall be eligible to apply for a Phase II award. (B) Use of funds A small business concern may use funds from a Phase 1A award to develop a proposed solution in pursuit of a subsequent proposal for a Phase I award or a Phase II award. .\n#### 202. Combating discriminatory practices in the SBIR and STTR programs\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (b)(7)(C), by striking owned and controlled by women or by socially and economically disadvantaged individuals and inserting owned by individuals who reside in emerging States or rural areas ;\n**(2)**\nin subsection (e)\u2014\n**(A)**\nin paragraph (18), by striking and at the end;\n**(B)**\nin paragraph (19), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(20) the term emerging State means the 25 States with the fewest combined number of award recipients in the SBIR program and the STTR program that have received their first Phase I award in the previous 10 fiscal years; (21) the term rural area means a county or other political subdivision of a State that the Bureau of the Census has defined as mostly rural or completely rural in the most recent decennial census; ;\n**(3)**\nin subsection (g)(8)(A)\u2014\n**(A)**\nby striking clause (iii);\n**(B)**\nby redesignating clauses (iv), (v), and (vi) as clauses (iii), (iv), and (v), respectively; and\n**(C)**\nin clause (iii), as so redesignated, by striking a socially or economically disadvantaged individual or has a socially or economically disadvantaged individual and inserting an individual who resides in an emerging State or rural area or has an individual who resides in an emerging State or rural area ;\n**(4)**\nin subsection (j)\u2014\n**(A)**\nby adjusting the margins for paragraphs (2) and (3) 2 ems to the left; and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking subparagraph (F);\n**(ii)**\nby redesignating subparagraphs (G), (H), and (I) as subparagraphs (F), (G), and (H); and\n**(iii)**\nin subparagraph (H), as so redesignated, by striking subparagraph (H) and inserting subparagraph (G) ;\n**(5)**\nin subsection (k)(1)(F)\u2014\n**(A)**\nby striking clause (ii);\n**(B)**\nby redesignating clauses (iii), (iv), and (v) as clauses (ii), (iii), and (iv), respectively; and\n**(C)**\nin clause (ii), as so redesignated, by striking a socially or economically disadvantaged individual or has a socially or economically disadvantaged individual and inserting an individual who resides in an emerging State or rural area or has an individual who resides in an emerging State or rural area ;\n**(6)**\nin subsection (o)(9)(A)\u2014\n**(A)**\nby striking clause (iii);\n**(B)**\nby redesignating clauses (iv), (v), and (vi) as clauses (iii), (iv), and (v), respectively; and\n**(C)**\nin clause (iii), as so redesignated, by striking a socially or economically disadvantaged individual or has a socially or economically disadvantaged individual and inserting an individual who resides in an emerging State or rural area or has an individual who resides in an emerging State or rural area ; and\n**(7)**\nin subsection (mm)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin the matter preceding subparagraph (A), by striking and until September 30, 2025 ; and\n**(ii)**\nin subparagraph (F), by striking or abuse to ensure compliance and inserting abuse, or adversarial influence to ensure compliance ;\n**(B)**\nin paragraph (2)(A), by striking to carry out the policy directive required under subsection (j)(2)(F) and and inserting to increase the participation of States with respect to which a low level of SBIR awards have historically been awarded ; and\n**(C)**\nby adding at the end the following:\n(7) Eligibility For an agency to be eligible to utilize funds allocated to the SBIR program of that Federal agency under this subsection, the agency shall not\u2014 (A) consider the race, gender, or ethnicity of the principal investigator, founder, or key personnel of the small business concern applying for an SBIR or STTR award in an award decision under the SBIR or STTR program of the agency; (B) require or consider a statement or plan to promote diversity or equity as part of an application for an SBIR or STTR award under the SBIR or STTR program of the agency; or (C) offer supplemental funds to a recipient of an SBIR or STTR award based on the race, gender, or ethnicity of the principal investigator, founder, or key personnel of a small business concern. .\nIII\nStreamlining Participation in the SBIR and STTR Programs\n#### 301. Definition of open topics\nSection 9(e) of the Small Business Act ( 15 U.S.C. 638(e) ), as amended by section 202(2), is amended by adding at the end the following:\n(22) the term open topic announcement means a solicitation for SBIR or STTR proposals that\u2014 (A) is a generalized problem statement or broad technology area and does not contain any language requiring that the solutions that a small business concern proposes adhere to specific technological specifications; and (B) evaluates the ability of the solution proposed by the small business concern to meet the stated innovation need of the agency or Government end user; and .\n#### 302. Reducing administrative burden\nSection 9(jj) of the Small Business Act ( 15 U.S.C. 638(jj) ), as amended by section 201(a)(1), is amended by adding at the end the following:\n(4) Reducing administrative burden (A) Limit on submissions to a solicitation A small business concern, including its affiliates, spinouts, or subsidiaries, may not submit more than 3 proposals to a single Phase I solicitation or a single Phase II solicitation under subsection (cc). (B) Limit on submissions in a single year A small business concern, including its affiliates, spinouts, or subsidiaries, may not submit more than a combined total of 25 proposals to Phase I solicitations or Phase II solicitations under subsection (cc) published by a single agency, including the components of the agency, in a single fiscal year. .\nIV\nProtecting American Innovation from Adversarial Influence\n#### 401. Definition of foreign risk\nSection 9(e) of the Small Business Act ( 15 U.S.C. 638(e) ), as amended by section 301, is amended by adding at the end the following:\n(23) the term foreign risk means, in the past 10 years, any foreign affiliation, technology licensing agreement, joint venture, contractual or financial obligation (pending or otherwise), investment agreement, research relationship (including co-authorship), or business relationship between\u2014 (A) a small business concern (including all subsidiaries, spinouts, and affiliates) submitting a proposal for an SBIR or STTR program, and covered individuals, owners, or other key personnel of the small business concern; and (B) an individual, research institution, business entity, government, or government-owned entity in a foreign country of concern that is disclosed, as required under subsection (g) or subsection (o), or otherwise identified in the due diligence process, as required under subsection (vv). .\n#### 402. Bolstering research security of SBIR and STTR awards\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (g)\u2014\n**(A)**\nby redesignating paragraphs (15), (16), and (17) as paragraphs (16), (18) and (19), respectively;\n**(B)**\nby inserting after paragraph (14) the following:\n(15) evaluate whether a small business concern presents a risk to national security for any reason, through measures including\u2014 (A) the due diligence process required under subsection (vv); (B) disclosures submitted under this subsection; or (C) coordination with the Inspector General of the agency or the intelligence community (as defined under section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )); ;\n**(C)**\nin paragraph (16), as so redesignated\u2014\n**(i)**\nby striking subparagraph (B);\n**(ii)**\nby striking that\u2014 and all that follows through the small business concern submitting and inserting that the small business concern submitting ;\n**(iii)**\nby redesignating clauses (i), (ii), and (iii) as subparagraphs (A), (B), and (C), respectively, and adjusting the margins accordingly;\n**(iv)**\nin subparagraph (B), as so redesignated, by striking or at the end;\n**(v)**\nin subparagraph (C), as so redesignated, by striking and at the end; and\n**(vi)**\nby adding at the end the following:\n(D) has a foreign risk connecting the small business concern to an entity, including any affiliates, spinouts, or subsidiaries of the entity, or individual on one or more of the following lists: (i) the UFLPA Entity List maintained by the Department of Homeland Security; (ii) the Non-SDN Chinese Military-Industrial Complex Companies List of the Office of Foreign Assets Control maintained by the Department of the Treasury; (iii) the Section 889 Prohibition List established under section 889 of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ) and maintained by the Department of Defense; (iv) the list of Chinese Military companies required under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ) and maintained by the Department of Defense; (v) the Military End User List maintained by the Bureau of Industry and Security of the Department of Commerce; (vi) the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce; (vii) the List of Equipment and Services maintained by the Federal Communications Commission; and (viii) the Withhold Release Orders and Findings List maintained by U.S. Customs and Border Protection; (E) has a foreign risk with a primary source that is classified; or (F) has a foreign risk or another national security risk not listed in statute or regulatory guidance that an agency determines warrants a denial; ;\n**(D)**\nby inserting after paragraph (16), as so redesignated, the following:\n(17) not, and any personnel of the Federal agency including technical points of contact shall not, communicate to an applicant prior to formal notification of an award decision that an application was denied due to a foreign risk; ; and\n**(E)**\nin paragraph (19), as so redesignated\u2014\n**(i)**\nin subparagraph (B), by striking (16)(A) and inserting (18)(A) ; and\n**(ii)**\nin subparagraph (C), by striking (16)(B) and inserting (18)(B) ; and\n**(2)**\nin subsection (o)\u2014\n**(A)**\nby redesignating paragraphs (19), (20), and (21) as paragraphs (20), (22) and (23), respectively;\n**(B)**\nby inserting after paragraph (18) the following:\n(19) evaluate whether a small business concern presents a risk to national security for any reason, through measures including\u2014 (A) the due diligence process required under subsection (vv); (B) disclosures submitted under this subsection; or (C) coordination with the Inspector General of the agency or the intelligence community (as defined under section 3 of the National Security Act of 1947 ( 50 U.S.C. 3003 )); ;\n**(C)**\nin paragraph (20), as so redesignated\u2014\n**(i)**\nby striking subparagraph (B);\n**(ii)**\nby striking that\u2014 and all that follows through the small business concern submitting and inserting that the small business concern submitting ;\n**(iii)**\nby redesignating clauses (i), (ii), and (iii) as subparagraphs (A), (B), and (C), respectively, and adjusting the margins accordingly;\n**(iv)**\nin subparagraph (B), as so redesignated, by striking or at the end;\n**(v)**\nin subparagraph (C), as so redesignated, by striking and at the end; and\n**(vi)**\nby adding at the end the following:\n(D) has a foreign risk connecting the small business concern to an entity, including any affiliates, spinouts, or subsidiaries of the entity, or individual on one or more of the following lists: (i) the UFLPA Entity List maintained by the Department of Homeland Security; (ii) the Non-SDN Chinese Military-Industrial Complex Companies List of the Office of Foreign Assets Control maintained by the Department of the Treasury; (iii) the Section 889 Prohibition List established under section 889 of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ) and maintained by the Department of Defense; (iv) the list of Chinese Military companies required under section 1260H of the William M. (Mac) Thornberry National Defense Authorization Act for Fiscal Year 2021 ( Public Law 116\u2013283 ) and maintained by the Department of Defense; (v) the Military End User List maintained by the Bureau of Industry and Security of the Department of Commerce; (vi) the Entity List maintained by the Bureau of Industry and Security of the Department of Commerce; (vii) the List of Equipment and Services maintained by the Federal Communications Commission; and (viii) the Withhold Release Orders and Findings List maintained by U.S. Customs and Border Protection; (E) has a foreign risk with a primary source that is classified; or (F) has a foreign risk or another national security risk not listed in statute or regulatory guidance that an agency determines warrants a denial; ;\n**(D)**\nby inserting after paragraph (20) the following:\n(21) not, and any personnel of the Federal agency including technical points of contact shall not, communicate to an applicant prior to formal notification of an award decision that an application was denied due to a foreign risk; ; and\n**(E)**\nin paragraph (23), as so redesignated\u2014\n**(i)**\nin subparagraph (B), by striking (20)(A) and inserting (22)(A) ; and\n**(ii)**\nin subparagraph (C), by striking (20)(B) and inserting (22)(B) .\n#### 403. Strengthening the due diligence program to assess security risks\nSection 9(vv)(2) of the Small Business Act ( 15 U.S.C. 638(vv)(2) ) is amended\u2014\n**(1)**\nin subparagraph (B), by striking the period at the end and inserting ; and ; and\n**(2)**\nby adding at the end the following:\n(C) examine any relationship of a small business concern seeking an award to any entity or individual included on the lists, as published on the date of the closing of the solicitation, described under subsections (g)(16)(D) and (o)(20)(D). .\n#### 404. Strengthening agency recovery authority\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (g)(18), as redesignated by section 402\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting , as adjusted for inflation according to the Consumer Price Index published by the Bureau of Labor Statistics, after amounts ;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, before the small business concern ; and\n**(ii)**\nby striking or at the end;\n**(C)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, before there is a change ; and\n**(ii)**\nby striking and at the end; and\n**(D)**\nby adding at the end the following:\n(C) during the 5-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, the small business concern sells, leases, or provides (through joint research, technological licensing, or otherwise) intellectual property that was developed, wholly or in part, using an SBIR award to a foreign entity or individual unless the foreign entity or individual is incorporated in or a citizen of a country that is a member of the North Atlantic Treaty Organization or a major non-NATO ally, as described under section 2321k of title 22, United States Code; or (D) during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, the small business concern sells, leases, or provides (through joint research, technological licensing, or otherwise) intellectual property that was developed, wholly or in part, using an SBIR award to an entity, government, or individual in a foreign country of concern; and ; and\n**(2)**\nin subsection (o)(22), as redesignated by section 402\u2014\n**(A)**\nin the matter preceding subparagraph (A), by inserting , as adjusted for inflation according to the Consumer Price Index published by the Bureau of Labor Statistics, after amounts ;\n**(B)**\nin subparagraph (A)\u2014\n**(i)**\nby inserting during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, before the small business concern ; and\n**(ii)**\nby striking or at the end;\n**(C)**\nin subparagraph (B)\u2014\n**(i)**\nby inserting during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, before there is a change ; and\n**(ii)**\nby striking and at the end; and\n**(D)**\nby adding at the end the following:\n(C) during the 5 year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, the small business concern sells, leases, or provides (through joint research, technological licensing, or otherwise) intellectual property that was developed, wholly or in part, using an STTR award to a foreign entity or individual unless the foreign entity or individual is incorporated in or a citizen of a country that is a member of the North Atlantic Treaty Organization or a major non-NATO ally, as described under section 2321k of title 22, United States Code; or (D) during the 10-year period beginning on the date of the award, or during a longer or indefinite period as determined by the head of the awarding agency as necessary for national security, the small business concern sells, leases, or provides (through joint research, technological licensing, or otherwise) intellectual property that was developed, wholly or in part, using an STTR award to an entity, government, or individual in a foreign country of concern; and .\n#### 405. Best practices on investor informational rights\nSection 9(uu) of the Small Business Act ( 15 U.S.C. 638(uu) ) is amended to read as follows:\n(uu) Best practices on investor informational rights (1) In general The Administrator, in coordination with the heads of all agencies with an SBIR program, the Director of the White House Office of Science and Technology Policy, and the Committee on Foreign Investment in the United States, shall develop best practices to be shared with each recipient of an SBIR or STTR award by the agency granting the award. (2) Contents The best practices developed under paragraph (1) shall include recommendations for protecting the proprietary technology and intellectual property of the small business concern from being shared unintentionally to foreign individuals and entities through informational rights of limited partners in venture capital, hedge fund, or private equity firms that have investments in SBIR or STTR recipients. .\n#### 406. GAO report\nParagraph (4) of section 4(b) of the SBIR and STTR Extension Act of 2022 ( Public Law 117\u2013183 ; 136 Stat. 2194) is amended to read as follows:\n(4) GAO Report (A) In general Not later than 1 year after the date of enactment of the INNOVATE Act , and annually thereafter for 3 years, the Comptroller General of the United States shall conduct a study and submit to the Committee on Small Business and Entrepreneurship and the Committee on Armed Services of the Senate and the Committee on Small Business , the Committee on Armed Services , and the Committee on Science, Space, and Technology of the House of Representatives a report on the implementation and best practices of the due diligence programs established under section 9(vv) of the Small Business Act ( 15 U.S.C. 638(vv) ) across Federal agencies required to establish an SBIR or STTR program. (B) Study The study shall evaluate\u2014 (i) the effectiveness of each Federal agency that participates in the SBIR program or STTR program in identifying\u2014 (I) enhanced risk in cybersecurity practices in SBIR and STTR projects; (II) enhanced risk in patents, including co-authorship with academics in foreign countries of concern in SBIR and STTR projects; (III) enhanced foreign influence risk among employees of small business concerns involved in SBIR and STTR projects; (IV) foreign ownership of a small business concern seeking an award, including the financial ties and obligations (which shall include surety, equity, and debt obligations) in SBIR and STTR projects; and (V) security risks among applicants to the SBIR program or the STTR program, including connections to an entity, including any affiliates, spinouts, or subsidiaries of the entity, or individual on one or more of the lists referenced in subsection (g)(16)(D); (ii) by year, the number of proposals and number of small business concerns with foreign risks by each Federal agency that participates in the SBIR program or STTR program, including a delineation of how many of those small business concerns have previously received an award under the SBIR program or STTR program and the nature of those foreign risks made by each Federal agency; and (iii) the extent to which the Inspector General and counterintelligence authorities of each Federal agency that participates in the SBIR or STTR program effectively conducts investigations, audits, inspections, and outreach relating to the due diligence program to assess security risks in the SBIR or STTR program. .\nV\nSimplifying SBIR-STTR Commercialization Standards\n#### 501. Streamlining transition and commercialization rate benchmarks\nSection 9(qq) of the Small Business Act ( 15 U.S.C. 638(qq) ) is amended\u2014\n**(1)**\nby amending paragraph (1)(A)(ii) to read as follows:\n(ii) for small business concerns that received or receive more than 10 Phase I awards, establish a minimum performance standard with respect to the receipt of Phase II awards that shall be a ratio of at least 0.25 for the number of Phase II awards received as compared to the number of Phase I awards received; and ; and\n**(2)**\nin paragraph (3)\u2014\n**(A)**\nin subparagraph (A), by striking clauses (i) and (ii) and inserting the following:\n(i) In general With respect to a small business concern that received or receives more than 25 Phase I awards, the minimum performance standard shall be a ratio of at least 0.5 for the number of Phase II awards received as compared to the number of Phase I awards received. (ii) Consequence of failure to meet standard If the head of a Federal agency determines that a small business concern is not meeting the applicable increased minimum performance standard established under clause (i), such small business concern may not participate in Phase I of the SBIR or STTR program of that agency during the 1-year period beginning on the date on which such determination is made and the small business concern may not receive more than 5 total Phase I awards from that agency during each 1-year period thereafter until the small business concern surpasses the minimum performance standard established under clause (i). ; and\n**(B)**\nin subparagraph (B)\u2014\n**(i)**\nin clause (i), by striking subclauses (I) and (II) and inserting the following:\n(I) with respect to a small business concern, including its affiliates, spinouts, and subsidiaries, that has received more than 25 Phase II awards over its lifetime, require the sum of the annual receipts (as defined in section 121.104 of title 13, Code of Federal Regulations, or any successor regulation) of the small business concern from sources other than Phase I or Phase II SBIR or STTR awards and investments received by the small business concern to at minimum exceed the sum of the dollars awarded through Phase I and Phase II awards since the date of the first such award; and (II) with respect to a small business concern, including its affiliates, spinouts, and subsidiaries, that receives more than 25 Phase II awards over its lifetime, require a minimum of 65 percent of the sum of the annual receipts (as defined in section 121.104 of title 13, Code of Federal Regulations, or any successor regulation) of the small business concern and investments received by the small business concern during the 3 years preceding the most recent fiscal year come from sources other than Phase I or Phase II SBIR or STTR awards. ; and\n**(ii)**\nby amending clause (ii) to read as follows:\n(ii) Consequence of failure to meet standard If the head of a Federal agency determines that a small business concern is not meeting an applicable increased minimum performance standard modified under clause (i), the small business concern may not apply for additional Phase I awards or Phase II awards until the small business concern has received enough annual receipts from sources other than an SBIR or STTR program to surpass the minimum performance standard established under clause (i). .\n#### 502. Improving direct to Phase II authorities\nSection 9(cc) of the Small Business Act ( 15 U.S.C. 638(cc) ) is amended to read as follows:\n(cc) Phase flexibility (1) Awarding a Phase II award absent a Phase I award Each agency with an SBIR program may provide to a small business concern an award under Phase II of the SBIR program with respect to a project, without regard to whether the small business concern was provided an award under Phase I of an SBIR program with respect to such project, if the head of the agency determines that the small business concern has completed the determinations described in subsection (e)(4)(A) with respect to such project despite not having been provided a Phase I award. (2) Limitations on awards (A) In general Except as provided in subparagraph (B), the head of each agency with an SBIR program may award not more than 10 percent of the funds allocated for the SBIR program of the agency in a given fiscal year under the authority of this subsection. (B) National Institutes of Health and Department of Defense The Director of the National Institutes of Health may award not more than 30 percent of the funds allocated for the SBIR program of the National Institutes of Health in a given fiscal year and the Secretary of Defense may award not more than 30 percent of the funds allocated for the SBIR program of each component in the Department of Defense in a given fiscal year under the authority of this subsection. (C) Limit on eligibility for awards An agency may not make an award under this subsection to a small business concern, including its affiliates, spinouts, and subsidiaries, that has received more than 25 Phase II awards. (D) Limit on number of awards An agency may make not more than 25 awards under this subsection to a small business concern, including its affiliates, spinouts, and subsidiaries. .\n#### 503. Improving SBIR-STTR data collection\n##### (a) Additional data fields in SBIR database\nSection 9(k)(1) of the Small Business Act ( 15 U.S.C. 638(k)(1) ) is amended\u2014\n**(1)**\nin subparagraph (E)(iv), by striking and at the end;\n**(2)**\nin subparagraph (F)(v), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(G) for each award granted, whether the award is classified or designated as\u2014 (i) Phase 1A, under subsection (pp); (ii) direct to Phase II, under subsection (cc); (iii) subsequent Phase II, under subsection (bb)(1); (iv) strategic breakthrough award under subsection (ff)(3); (v) Phase III prime contract award; or (vi) Phase III subcontract award. .\n##### (b) Improving FPDS data tracking\n**(1) In general**\nThe Administrator of General Services shall update the Federal Procurement Data System described in section 1122(a)(4) of title 41, United States Code, or any successor system, to\u2014\n**(A)**\nrequire reporting on whether an award under the SBIR or STTR program is classified or designated as\u2014\n**(i)**\nPhase 1A, under subsection (pp) of section 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act;\n**(ii)**\ndirect to Phase II, under subsection (cc) of such section;\n**(iii)**\nsubsequent Phase II, under subsection (bb)(1) of such section;\n**(iv)**\na strategic breakthrough award under subsection (ff)(3) of such section;\n**(v)**\na Phase III prime contract award; or\n**(vi)**\na Phase III subcontract award;\n**(B)**\nrequire reporting on whether a contract is designated as a Phase III contract; and\n**(C)**\nallow a Government contracting officer, when recording a Phase II or Phase III contract following on from work done by a small business concern during a Phase I or Phase II award to reference an SBIR or STTR contract identification number for relevant prior SBIR or STTR work done.\n**(2) No new funds**\nNo additional funds are authorized to be appropriated for the purpose of carrying out this subsection.\n#### 504. Streamlining program administration\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (bb)(3), by inserting or another component of the same Federal agency after another Federal agency ;\n**(2)**\nin subsection (gg)\u2014\n**(A)**\nin the heading, by striking Pilot Program and inserting Commercialization Readiness Program ;\n**(B)**\nby striking pilot each place the term appears;\n**(C)**\nby striking paragraph (7);\n**(D)**\nby redesignating paragraph (8) as paragraph (7); and\n**(E)**\nby amending paragraph (7), as so redesignated, to read as follows:\n(7) Definition In this subsection, the term covered Federal agency \u2014 (A) means a Federal agency participating in the SBIR program or the STTR program; and (B) does not include the Department of Defense. ;\n**(3)**\nin subsection (hh)\u2014\n**(A)**\nby striking funding .\u2014 and all that follows through Federal agencies participating and inserting funding .\u2014Federal agencies participating ; and\n**(B)**\nby striking paragraph (2);\n**(4)**\nin subsection (ii)(2)(B)\u2014\n**(A)**\nin clause (ii), by adding and at the end;\n**(B)**\nin clause (iii), by striking ; and and inserting a period; and\n**(C)**\nby striking clause (iv);\n**(5)**\nin subsection (qq)(3), by striking subparagraph (I);\n**(6)**\nin subsection (vv)(3), by striking subparagraph (C);\n**(7)**\nby redesignating subsection (yy) as subsection (xx);\n**(8)**\nin subsection (xx), as so redesignated\u2014\n**(A)**\nin the subsection heading, by striking Pilot ;\n**(B)**\nby striking STTR Program .\u2014 and all that follows through Not later than and inserting STTR Program .\u2014Not later than ;\n**(C)**\nby striking paragraph (2); and\n**(D)**\nby striking pilot ;\n**(9)**\nby redesignating subsection (zz) as subsection (yy); and\n**(10)**\nin subsection (yy), as so redesignated\u2014\n**(A)**\nin the subsection heading, by striking Pilot ;\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nin the paragraph heading, by striking Pilot and inserting Program ;\n**(ii)**\nin subparagraph (B), by striking 3.25 and inserting 3.50 ; and\n**(iii)**\nin subparagraph (C), by striking 0.46 and inserting 0.21 ;\n**(C)**\nby striking paragraph (3); and\n**(D)**\nby striking pilot each place the term appears.\n#### 505. Extending SBIR and STTR authorization\nSection 9 of the Small Business Act ( 15 U.S.C. 638 ), as amended by this Act, is amended\u2014\n**(1)**\nin subsection (m), by striking 2025 and inserting 2028 ; and\n**(2)**\nin subsection (n)(1)(A), by striking 2025 and inserting 2028 .",
      "versionDate": "2025-03-05",
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
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-04-02T13:53:43Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-04-02T14:04:33Z"
          },
          {
            "name": "China",
            "updateDate": "2025-04-02T14:04:19Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-04-02T14:14:41Z"
          },
          {
            "name": "Data collection, sharing, protection",
            "updateDate": "2026-04-07T17:48:22Z"
          },
          {
            "name": "Economic performance and conditions",
            "updateDate": "2025-04-02T13:59:25Z"
          },
          {
            "name": "Espionage and treason",
            "updateDate": "2025-04-02T14:07:43Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-04-02T14:12:24Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-04-02T13:51:53Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-04-02T14:12:08Z"
          },
          {
            "name": "Military procurement, research, weapons development",
            "updateDate": "2025-04-02T13:56:52Z"
          },
          {
            "name": "Performance measurement",
            "updateDate": "2025-04-02T14:10:34Z"
          },
          {
            "name": "Product development and innovation",
            "updateDate": "2025-04-02T14:01:36Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-04-02T13:57:05Z"
          },
          {
            "name": "Small business",
            "updateDate": "2025-04-02T13:49:10Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2025-04-02T14:07:32Z"
          },
          {
            "name": "Technology transfer and commercialization",
            "updateDate": "2025-04-02T13:49:26Z"
          },
          {
            "name": "U.S. and foreign investments",
            "updateDate": "2025-04-02T14:03:13Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-03-28T11:56:19Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s853is.xml"
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
      "title": "INNOVATE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "INNOVATE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Investing in National Next-Generation Opportunities for Venture Acceleration and Technological Excellence",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "This Act may be cited as the",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T01:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve the SBIR and STTR programs under the Small Business Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T01:48:24Z"
    }
  ]
}
```
