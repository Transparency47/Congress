# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/526?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/526
- Title: Pharmacy Benefit Manager Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 526
- Origin chamber: Senate
- Introduced date: 2025-02-11
- Update date: 2026-04-08T17:26:38Z
- Update date including text: 2026-04-08T17:26:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-11: Introduced in Senate
- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-02-11: Introduced in Senate

## Actions

- 2025-02-11 - IntroReferral: Introduced in Senate
- 2025-02-11 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-11",
    "latestAction": {
      "actionDate": "2025-02-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/526",
    "number": "526",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "Pharmacy Benefit Manager Transparency Act of 2025",
    "type": "S",
    "updateDate": "2026-04-08T17:26:38Z",
    "updateDateIncludingText": "2026-04-08T17:26:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-11",
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
          "date": "2025-02-11T21:09:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "C000127",
      "firstName": "Maria",
      "fullName": "Sen. Cantwell, Maria [D-WA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cantwell",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "WA"
    },
    {
      "bioguideId": "E000295",
      "firstName": "Joni",
      "fullName": "Sen. Ernst, Joni [R-IA]",
      "isOriginalCosponsor": "True",
      "lastName": "Ernst",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "IA"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "VT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "WV"
    },
    {
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NH"
    },
    {
      "bioguideId": "M001198",
      "firstName": "Roger",
      "fullName": "Sen. Marshall, Roger [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Marshall",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "NM"
    },
    {
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "KS"
    },
    {
      "bioguideId": "H001079",
      "firstName": "Cindy",
      "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
      "isOriginalCosponsor": "True",
      "lastName": "Hyde-Smith",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "MS"
    },
    {
      "bioguideId": "T000476",
      "firstName": "Thomas",
      "fullName": "Sen. Tillis, Thomas [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Tillis",
      "middleName": "Roland",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "NC"
    },
    {
      "bioguideId": "R000605",
      "firstName": "Mike",
      "fullName": "Sen. Rounds, Mike [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Rounds",
      "party": "R",
      "sponsorshipDate": "2025-02-11",
      "state": "SD"
    },
    {
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "False",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-02-18",
      "state": "AR"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-09-15",
      "state": "AZ"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s526is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 526\nIN THE SENATE OF THE UNITED STATES\nFebruary 11, 2025 Mr. Grassley (for himself, Ms. Cantwell , Ms. Ernst , Mr. Welch , Mrs. Capito , Mrs. Shaheen , Mr. Marshall , Mr. Heinrich , Mr. Moran , Mrs. Hyde-Smith , Mr. Tillis , and Mr. Rounds ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prevent unfair and deceptive acts or practices and the dissemination of false information related to pharmacy benefit management services for prescription drugs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Pharmacy Benefit Manager Transparency Act of 2025 .\n#### 2. Prohibition on unfair or deceptive prescription drug pricing practices\n##### (a) Conduct prohibited\nExcept as provided in subsection (b), it shall be unlawful for any pharmacy benefit manager (or affiliate, subsidiary, or agent of a pharmacy benefit manager), directly or indirectly, to engage in any of the following activities related to pharmacy benefit management services:\n**(1)**\nCharge a health plan or payer a different amount for a prescription drug\u2019s ingredient cost or dispensing fee than the amount the pharmacy benefit manager reimburses a pharmacy for the prescription drug\u2019s ingredient cost or dispensing fee where the pharmacy benefit manager retains the amount of any such difference.\n**(2)**\nArbitrarily, unfairly, or deceptively, by contract or any other means, reduce, rescind, or otherwise claw back any reimbursement payment, in whole or in part, to a pharmacist or pharmacy for a prescription drug's ingredient cost or dispensing fee, unless\u2014\n**(A)**\nthe original claim was submitted fraudulently;\n**(B)**\nthe original claim payment was inconsistent with the reimbursement terms in the contract; or\n**(C)**\nthe pharmacist services were not rendered by the pharmacy or pharmacist.\n**(3)**\nArbitrarily, unfairly, or deceptively, by contract or any other means, increase fees or lower reimbursement to a pharmacy in order to offset reimbursement changes instructed by the Federal Government under any health plan funded by the Federal Government.\n##### (b) Exceptions\nA pharmacy benefit manager shall not be in violation of paragraph (1) or (3) of subsection (a) if the pharmacy benefit manager meets the following conditions:\n**(1)**\nThe pharmacy benefit manager, affiliate, subsidiary, or agent passes along or returns 100 percent of any price concession to a health plan or payer, including any rebate, discount, or other price concession.\n**(2)**\nThe pharmacy benefit manager, affiliate, subsidiary, or agent provides full and complete disclosure of\u2014\n**(A)**\nthe cost, price, and reimbursement of a prescription drug to each health plan, payer, and pharmacy with which the pharmacy benefit manager, affiliate, subsidiary, or agent has a contract or agreement to provide pharmacy benefit management services;\n**(B)**\neach fee, markup, and discount charged or imposed by the pharmacy benefit manager, affiliate, subsidiary, or agent to each health plan, payer, and pharmacy with which the pharmacy benefit manager, affiliate, subsidiary, or agent has a contract or agreement for pharmacy benefit management services; or\n**(C)**\nthe aggregate amount of all remuneration the pharmacy benefit manager receives from a prescription drug manufacturer for a prescription drug, including any rebate, discount, administration fee, and any other payment or credit obtained or retained by the pharmacy benefit manager, or affiliate, subsidiary, or agent of the pharmacy benefit manager, pursuant to a contract or agreement for pharmacy benefit management services to a health plan, payer, or any Federal agency (upon the request of the agency).\n#### 3. Prohibition on false information\nIt shall be unlawful for any person to report information related to pharmacy benefit management services to a Federal department or agency if\u2014\n**(1)**\nthe person knew, or reasonably should have known, the information to be false or misleading;\n**(2)**\nthe information was required by law to be reported; and\n**(3)**\nthe false or misleading information reported by the person would affect analysis or information compiled by the Federal department or agency for statistical or analytical purposes with respect to the market for pharmacy benefit management services.\n#### 4. Transparency\n##### (a) Reporting by pharmacy benefit managers\nSubject to subsection (d), not later than 1 year after the date of enactment of this Act, and annually thereafter, each pharmacy benefit manager (or affiliate, subsidiary, or agent of a pharmacy benefit manager) shall report to the Commission and the Secretary of Health and Human Services the following information:\n**(1)**\nThe aggregate amount of the difference between the amount the pharmacy benefit manager was paid by each health plan and the amount that the pharmacy benefit manager paid each pharmacy on behalf of the health plan for prescription drugs.\n**(2)**\nThe aggregate amount of any\u2014\n**(A)**\ngeneric effective rate fee charged to each pharmacy;\n**(B)**\ndirect and indirect remuneration fee charged or other price concession to each pharmacy; and\n**(C)**\npayment rescinded or otherwise clawed back from a reimbursement made to each pharmacy.\n**(3)**\nIf, during the reporting year, the pharmacy benefit manager moved or reassigned a prescription drug to a formulary tier that has a higher cost, higher copayment, higher coinsurance, or higher deductible to a consumer, or a lower reimbursement to a pharmacy, an explanation of the reason why the drug was moved or reassigned from 1 tier to another, including whether the move or reassignment was determined or requested by a prescription drug manufacturer or other entity.\n**(4)**\nWith respect to any pharmacy benefit manager that owns, controls, or is affiliated with a pharmacy, a report regarding any difference in reimbursement rates or practices, direct and indirect remuneration fees or other price concessions, and clawbacks between a pharmacy that is owned, controlled, or affiliated with the pharmacy benefit manager and any other pharmacy.\n##### (b) Report to Congress\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, and annually thereafter, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report that addresses, at a minimum\u2014\n**(A)**\nthe number actions brought by the Commission during the reporting year to enforce this Act and the outcome of each such enforcement action;\n**(B)**\nthe number of open investigations or inquiries into potential violations of this Act as of the time the report is submitted;\n**(C)**\nthe number and nature of complaints received by the Commission relating to an allegation of a violation of this Act during the reporting year;\n**(D)**\nan anonymized summary of the reports filed with the Commission pursuant to subsection (a) for the reporting year;\n**(E)**\nan analysis of the requirements of this Act and whether the implementation of such requirements leads to mergers (including horizontal mergers or vertical mergers) amongst any pharmacy benefit managers, or any pharmacy benefit manager that owns, controls, or is affiliated with a pharmacy, or any pharmacy benefit manager that owns, controls, or is affiliated with a health plan, and the effect of such merger (including the likelihood of a substantial decrease in competition or the potential for a monopoly); and\n**(F)**\npolicy or legislative recommendations to strengthen any enforcement action relating to a violation of this Act, including recommendations to include additional prohibited conduct in section 2(a), and recommendations to encourage more competition and decrease the likelihood of a monopoly in the pharmaceutical supply chain.\n**(2) Formulary design or placement practices**\nNot later than 1 year after the date of enactment of this Act, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate, the Committee on Finance of the Senate, the Committee on Health, Education, Labor, and Pensions of the Senate, the Committee on Ways and Means of the House of Representatives, and the Committee on Energy and Commerce of the House of Representatives a report that addresses the policies, practices, and role of pharmacy benefit managers (including their affiliates, subsidiaries, and agents) regarding formulary design or placement, including\u2014\n**(A)**\nwhether pharmacy benefit managers (including their affiliates, subsidiaries, and agents) use formulary design or placement to increase their gross revenue without an accompanying increase in patient access or decrease in patient cost; or\n**(B)**\nrecommendations to Congress for legislative action addressing such policies, practices, and role of pharmacy benefit managers (including their affiliates, subsidiaries, and agents).\n**(3) Construction**\nNothing in this section shall be construed as authorizing the Commission to disclose any information that is a trade secret or confidential information described in section 552(b)(4) of title 5, United States Code, except as necessary to enforce this Act.\n**(4) Confidentiality**\nThe Commission may disclose the information in a form which does not disclose the identity of a specific pharmacy benefit manager, pharmacy, or health plan for the following purposes:\n**(A)**\nTo permit the Comptroller General of the United States to review the information provided to carry out this Act.\n**(B)**\nTo permit the Director of the Congressional Budget Office to review the information provided.\n##### (c) GAO study\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States shall submit to the Committee on Commerce, Science, and Transportation, the Committee on Finance, and the Committee on Health, Education, Labor, and Pensions of the Senate and to the Committee on Ways and Means and the Committee on Energy and Commerce of the House of Representatives a report that\u2014\n**(1)**\naddresses, at minimum\u2014\n**(A)**\nthe role that pharmacy benefit managers play in the pharmaceutical supply chain;\n**(B)**\nthe state of competition among pharmacy benefit managers, including the market share for the Nation's 10 largest pharmacy benefit managers;\n**(C)**\nthe use of rebates and fees by pharmacy benefit managers, including data for each of the 10 largest pharmacy benefit managers that reflects, for each drug in the formulary of each such pharmacy benefit manager\u2014\n**(i)**\nthe amount of the rebate passed on to patients;\n**(ii)**\nthe amount of the rebate passed on to payors;\n**(iii)**\nthe amount of the rebate kept by the pharmacy benefit manager; and\n**(iv)**\nthe role of fees charged by the pharmacy benefit manager;\n**(D)**\nwhether pharmacy benefit managers structure their formularies in favor of high-rebate prescription drugs over lower-cost, lower-rebate alternatives;\n**(E)**\nthe average prior authorization approval time for each of the 10 largest pharmacy benefit managers;\n**(F)**\nfactors affecting the use of step therapy in each of the 10 largest pharmacy benefit managers;\n**(G)**\nthe extent to which the price that pharmacy benefit managers charge payors, such as the Medicare program under title XXVIII of the Social Security Act ( 42 U.S.C. 1395 et seq. ), State Medicaid programs under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ), the Federal Employees Health Benefits Program under chapter 89 of title 5, United States Code, or private payors, for a drug is more than such pharmacy benefit managers pay the pharmacy for the drug; and\n**(H)**\nthe competitive impact of pharmacy benefit managers' business practices, including the impact that such business practices have on the cost of health plan premiums or prescription drugs for consumers; and\n**(2)**\nprovides recommendations for legislative action to lower the cost of prescription drugs for consumers and payors, improve the efficiency of the pharmaceutical supply chain by lowering intermediary costs, improve competition in pharmacy benefit management, and provide transparency in pharmacy benefit management.\n##### (d) Privacy requirements\nAny entity shall provide information under subsection (a) in a manner consistent with the privacy, security, and breach notification regulations promulgated under section 264(c) of the Health Insurance Portability and Accountability Act of 1996 ( 42 U.S.C. 1320d\u20132 note) (or any successor regulation), and shall restrict the use and disclosure of such information according to such regulations.\n#### 5. Whistleblower protections\n##### (a) In general\nA pharmacy benefit manager, health plan, pharmaceutical manufacturer, pharmacy, or any affiliate, subsidiary, or agent thereof shall not, directly or indirectly, discharge, demote, suspend, diminish, or withdraw benefits from, threaten, harass, or in any other manner discriminate against or adversely impact a covered individual because\u2014\n**(1)**\nthe covered individual, or anyone perceived as assisting the covered individual, takes (or is suspected to have taken or will take) a lawful action in providing to Congress, an agency of the Federal Government, the attorney general of a State, a State regulator with authority over the distribution or insurance coverage of prescription drugs, or a law enforcement agency relating to any act or omission that the covered individual reasonably believes to be a violation of this Act;\n**(2)**\nthe covered individual provides information that the covered individual reasonably believes evidences such a violation to\u2014\n**(A)**\na person with supervisory authority over the covered individual at the pharmacy benefit manager, health plan, pharmaceutical manufacturer, pharmacy, or any affiliate, subsidiary, or agent thereof; or\n**(B)**\nanother individual working for the pharmacy benefit manager, health plan, pharmaceutical manufacturer, pharmacy, or any affiliate, subsidiary, or agent thereof who the covered individual reasonably believes has the authority to investigate, discover, or terminate the violation or to take any other action to address the violation;\n**(3)**\nthe covered individual testifies (or it is suspected that the covered individual will testify) in an investigation or judicial or administrative proceeding concerning such a violation; or\n**(4)**\nthe covered individual assists or participates (or it is expected that the covered individual will assist or participate) in such an investigation or judicial or administrative proceeding.\n##### (b) Enforcement\nAn individual who alleges any adverse action in violation of subsection (a) may bring an action for a jury trial in the appropriate district court of the United States for the following relief:\n**(1)**\nTemporary relief while the case is pending.\n**(2)**\nReinstatement with the same seniority status that the individual would have had, but for the discharge or discrimination.\n**(3)**\nTwice the amount of back pay otherwise owed to the individual, with interest.\n**(4)**\nConsequential and compensatory damages, and compensation for litigation costs, expert witness fees, and reasonable attorneys\u2019 fees.\n##### (c) Waiver of rights and remedies\nThe rights and remedies provided for in this section shall not be waived by any policy form or condition of employment, including by a predispute arbitration agreement.\n##### (d) Predispute arbitration agreements\nNo predispute arbitration agreement shall be valid or enforceable if the agreement requires arbitration of a dispute arising under this section.\n#### 6. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair and deceptive acts or practices**\nA violation of this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraph (C), the Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nSubject to paragraph (3), any person who violates this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Nonprofit organizations and insurance**\nNotwithstanding section 4 or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 , 46), section 2 of McCarran-Ferguson Act ( 15 U.S.C. 1012 ), or any other jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraphs (A) and (B) of this paragraph, with respect to\u2014\n**(i)**\norganizations not organized to carry on business for their own profit or that of their members; and\n**(ii)**\nthe business of insurance, and persons engaged in such business.\n**(D) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(3) Penalties**\n**(A) Additional civil penalty**\nIn addition to any penalty applicable under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ), any person that violates this Act shall be liable for a civil penalty of not more than $1,000,000.\n**(B) Method**\nThe penalties provided by subparagraph (A) shall be obtained in the same manner as civil penalties imposed under section 18(a)(1)(B) of the Federal Trade Commission Act (15 U.S.C. 57a(a(1)(B).\n**(C) Multiple offenses; mitigating factors**\nIn assessing a penalty under subparagraph (A)\u2014\n**(i)**\neach day of a continuing violation shall be considered a separate violation; and\n**(ii)**\nthe court shall take into consideration, among other factors\u2014\n**(I)**\nthe seriousness of the violation;\n**(II)**\nthe efforts of the person committing the violation to remedy the harm caused by the violation in a timely manner; and\n**(III)**\nwhether the violation was intentional.\n##### (b) Enforcement by States\n**(1) In general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates this Act, the attorney general of the State may bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State, before initiating a civil action under paragraph (1), shall provide written notification to the Commission that the attorney general intends to bring such civil action.\n**(ii) Contents**\nThe notification required under clause (i) shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required under clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by the Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Construction**\n**(A) Powers conferred on the attorney general of a State**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(B) ERISA**\nNo civil action brought pursuant to this subsection shall conflict with the Employee Retirement Income Security Act of 1974 ( 29 U.S.C. 1001 et seq. ).\n**(4) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which\u2014\n**(i)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(ii)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(5) Actions by other State officials**\n**(A) In general**\nIf an attorney general lacks appropriate jurisdiction to bring a civil action under paragraph (1), any other officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Clarification of authority**\nThe authority provided by subparagraph (A) shall supplant, and not supplement, the authorities of State attorneys general under paragraph (1).\n**(C) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n##### (c) Affirmative defense\n**(1) In general**\nIn an action brought under this section to enforce section 2, it shall be an affirmative defense, on which the defendant has the burden of persuasion by a preponderance of the evidence, that the conduct alleged to be a violation of section 2 was nonpretextual and reasonably necessary to\u2014\n**(A)**\nprevent a violation of, or comply with, Federal or State law;\n**(B)**\nprotect patient safety; or\n**(C)**\nprotect patient access.\n**(2) Clarification**\nNothing in this subsection shall be construed to prohibit a defendant from raising any other affirmative defense available.\n#### 7. Protection of personal health information\nIn making any disclosure or report required by this Act, a pharmacy benefit manager (including their affiliates, subsidiaries, and agents) shall not include any information that would identify a patient or a provider that issued a prescription.\n#### 8. Effect on State laws\nNothing in this Act shall be construed to preempt, displace, or supplant any State laws, rules, regulations, or requirements, or the enforcement thereof.\n#### 9. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered individual**\nThe term covered individual means a current or former employee, contractor, subcontractor, service provider, or agent of a pharmacy benefit manager, health plan, pharmaceutical manufacturer, pharmacy, or any affiliate, subsidiary, or agent thereof.\n**(3) Health plan**\nThe term health plan means any group or individual health insurance plan or coverage, including any health insurance plan or coverage sponsored or funded by the Federal Government or the government of any State, Territory, or subdivision thereof.\n**(4) Pharmacy benefit manager**\nThe term pharmacy benefit manager means any entity that provides pharmacy benefit management services on behalf of a health plan, a payer, or health insurance issuer.\n**(5) Pharmacy benefit management services**\nThe term pharmacy benefit management services means, pursuant to a written agreement with a payer or health plan offering group or individual health insurance coverage, directly or through an intermediary, the service of\u2014\n**(A)**\nnegotiating terms and conditions, including rebates and price concessions, with respect to a prescription drug on behalf of the health plan, coverage, or payer; or\n**(B)**\nmanaging the prescription drug benefits provided by the health plan, coverage, or payer, which may include formulary management the processing and payment of claims for prescription drugs, the performance of drug utilization review, the processing of drug prior authorization requests, the adjudication of appeals or grievances related to the prescription drug benefit, contracting with network pharmacies, or the provision of related services.\n**(6) Prescription drug**\nThe term prescription drug means\u2014\n**(A)**\na drug, as that term is defined in section 201(g) of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321(g) ), that is\u2014\n**(i)**\napproved by the Food and Drug Administration under section 505 of such Act ( 21 U.S.C. 355 ); and\n**(ii)**\nsubject to the requirements of section 503(b)(1) of such Act ( 21 U.S.C. 353(b)(1) );\n**(B)**\na biological product as that term is defined in section 351 of the Public Health Service Act ( 42 U.S.C. 262(i)(1) ); or\n**(C)**\na product that is biosimilar to, or interchangeable with, a biologic product under section 351 of the Public Health Service Act ( 42 U.S.C. 262(i) ).",
      "versionDate": "2025-02-11",
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
            "name": "Civil actions and liability",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Medical ethics",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Prescription drugs",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "State and local government operations",
            "updateDate": "2025-05-02T14:56:38Z"
          },
          {
            "name": "Supply chain",
            "updateDate": "2026-04-08T17:26:37Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-03-12T16:29:17Z"
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
      "date": "2025-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s526is.xml"
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
      "title": "Pharmacy Benefit Manager Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Pharmacy Benefit Manager Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prevent unfair and deceptive acts or practices and the dissemination of false information related to pharmacy benefit management services for prescription drugs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:02Z"
    }
  ]
}
```
