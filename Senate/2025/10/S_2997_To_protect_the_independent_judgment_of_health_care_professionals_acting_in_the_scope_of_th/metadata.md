# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2997?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2997
- Title: Right to Override Act
- Congress: 119
- Bill type: S
- Bill number: 2997
- Origin chamber: Senate
- Introduced date: 2025-10-09
- Update date: 2025-12-09T17:29:09Z
- Update date including text: 2025-12-09T17:29:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-09: Introduced in Senate
- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-10-09: Introduced in Senate

## Actions

- 2025-10-09 - IntroReferral: Introduced in Senate
- 2025-10-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-09",
    "latestAction": {
      "actionDate": "2025-10-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2997",
    "number": "2997",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
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
    "title": "Right to Override Act",
    "type": "S",
    "updateDate": "2025-12-09T17:29:09Z",
    "updateDateIncludingText": "2025-12-09T17:29:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-09",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-09",
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
          "date": "2025-10-09T19:58:35Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-10-09",
      "state": "CT"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-10-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2997is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2997\nIN THE SENATE OF THE UNITED STATES\nOctober 9, 2025 Mr. Markey (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo protect the independent judgment of health care professionals acting in the scope of their practice in overriding AI/CDSS outputs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Right to Override Act .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short\n                    title.\nSec. 2. Table\n                    of contents.\nSec. 3.\n                    Definitions.\nTITLE I\u2014Policies\n                    for using and overriding AI/CDSS\nSec. 101.\n                    Policies with respect to using and overriding AI/CDSS.\nSec. 102.\n                    Enforcement.\nSec. 103.\n                    Regulations.\nTITLE II\u2014Adverse\n                    employment actions; whistleblower protections\nSec. 201.\n                    Prohibition on adverse employment actions.\nSec. 202.\n                    Whistleblower protections.\nSec. 203.\n                    Enforcement.\nSec. 204.\n                    Regulations.\nTITLE\n                    III\u2014General provisions\nSec. 301.\n                    Educational materials for covered entities and health care\n                    professionals.\nSec. 302.\n                    State enforcement.\nSec. 303. Rule\n                    of construction.\nSec. 304.\n                    Non-preemption.\n#### 3. Definitions\nIn this Act:\n**(1) Adverse employment action**\nThe term adverse employment action , with respect to a health care professional, includes\u2014\n**(A)**\nthe termination, suspension, or demotion of the health care professional from a job;\n**(B)**\nany disciplinary action or retaliatory investigation against the health care professional;\n**(C)**\nthe imposition of a work schedule that is more burdensome to the health care professional;\n**(D)**\nthe failure of the health care professional to receive, or any adverse adjustment in the ability of the health care professional to receive, a promotion;\n**(E)**\nthe denial of the health care professional in receiving or being eligible to receive\u2014\n**(i)**\ncompensation, including the denial of an increase in compensation; or\n**(ii)**\nany other job-related benefit or opportunity, including for telework, training, or travel;\n**(F)**\nrevocation of admitting privileges;\n**(G)**\na reassignment of a duty or the assignment of a duty inappropriate for the job, skill set, or experience of the health care professional;\n**(H)**\na change in the ability to practice at a location for which the health care professional would otherwise be able;\n**(I)**\nan adverse evaluation or performance review;\n**(J)**\nany other modification to the terms, conditions, or privileges of employment or work of the health care professional that, from the perspective of a reasonable person, puts the health care professional in a materially adverse position when compared to the position of the professional prior to the modification; and\n**(K)**\nany other action or inaction that results in the health care professional being in a materially adverse position when compared to the position of the professional prior to the action or inaction.\n**(2) Artificial intelligence clinical decision support system; AI/CDSS**\nThe term artificial intelligence clinical decision support system or AI/CDSS means technology that\u2014\n**(A)**\nsupports decision-making based on algorithms, or models, based in clinical practice guidelines or that derive relationships from training data, including such algorithms or models that are developed using unsupervised learning models; and\n**(B)**\nproduces an output that results in a prediction, classification, recommendation, evaluation, or analysis.\n**(3) AI/CDSS output**\nThe term AI/CDSS output means any recommendation, decision, or other output of AI/CDSS.\n**(4) Commerce; industry or activity affecting commerce**\nThe terms commerce and industry or activity affecting commerce have the meanings given such terms in section 101 of the Family and Medical Leave Act of 1993 ( 29 U.S.C. 2611 ).\n**(5) Covered entity**\nThe term covered entity \u2014\n**(A)**\nmeans any individual or entity that\u2014\n**(i)**\nemploys, or otherwise engages in the performance of work for remuneration, a health care professional; and\n**(ii)**\nis engaged in commerce (including government), or an industry or activity affecting commerce (including government); and\n**(B)**\nincludes such an individual or entity that is\u2014\n**(i)**\na health care facility in any setting, such as a nurse's office in a school setting; or\n**(ii)**\na health plan or an administrator of a health plan.\n**(6) Engaged in the performance of work for remuneration**\nThe term engaged in the performance of work for remuneration , with respect to an individual performing work for a covered entity, includes the individual having admitting privileges for the covered entity without regard to whether such individual is employed by such entity.\n**(7) Health care professional**\nThe term health care professional \u2014\n**(A)**\nmeans an individual\u2014\n**(i)**\nlicensed, registered, or certified under Federal or State laws or regulations to provide health care services; or\n**(ii)**\nrequired to be so licensed, registered, or certified but that is exempted by other statute or regulation; and\n**(B)**\nincludes\u2014\n**(i)**\nan individual described in subparagraph (A) without regard to whether the individual works at a health care facility, including a home health aide or a home care provider; and\n**(ii)**\nan individual who is employed by, or otherwise engaged in the performance of work for remuneration for, a health plan to make prior authorization determinations or other determinations regarding coverage under a health plan.\n**(8) Health care services**\nThe term health care services means any services that relate to\u2014\n**(A)**\nthe diagnosis, prevention, or treatment of any human disease or impairment;\n**(B)**\nthe assessment or care of the health of human beings; or\n**(C)**\nmaking prior authorization determinations or other determinations regarding coverage under a health plan.\n**(9) Health plan**\nThe term health plan has the meaning given the term in section 3000 of the Public Health Service Act ( 42 U.S.C. 300jj ).\n**(10) Override**\nThe term override , with respect to an AI/CDSS output, means making a decision contrary to such output.\n**(11) Override data**\nThe term override data \u2014\n**(A)**\nmeans any data related to adherence to or deviation from AI/CDSS outputs; and\n**(B)**\nincludes\u2014\n**(i)**\nany such data that is metadata or audit data; or\n**(ii)**\nany such data related to a particular health care professional or group of health care professionals, or related to a particular AI/CDSS.\n**(12) State**\nThe term State has the meaning given the term in section 3000 of the Public Health Service Act.\nI\nPolicies for using and overriding AI/CDSS\n#### 101. Policies with respect to using and overriding AI/CDSS\n##### (a) In general\nA covered entity that uses AI/CDSS shall\u2014\n**(1)**\nadopt and adhere to a policy with respect to such usage\u2014\n**(A)**\nthat ensures that AI/CDSS outputs are not substituted for the independent judgment of a health care professional employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity while such health care professional is acting in the scope of practice of such health care professional;\n**(B)**\nthat allows such a health care professional to override an AI/CDSS output in a timely manner if, at the time of the override, in the judgment of the health care professional acting in the scope of practice of the health care professional, such an override is appropriate for the patient, or as necessary to comply with applicable law, including civil rights law;\n**(C)**\nthat allows health care professionals and their representatives to provide feedback on AI/CDSS, including incorrect or biased outputs that require frequent override; and\n**(D)**\nthat prohibits the sharing of override data on\u2014\n**(i)**\na specific health care professional; or\n**(ii)**\na group of health care professionals when the identity of those professionals can be reasonably inferred;\n**(2)**\ninform health care professionals employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity, and the representatives of such health care professionals, of the policy under paragraph (1), including the presence of AI/CDSS in the workplace and the ability of such health care professionals to override an AI/CDSS output;\n**(3)**\nprovide training to such health care professionals on\u2014\n**(A)**\nhow to use AI/CDSS;\n**(B)**\nthe circumstances where an AI/CDSS override is appropriate;\n**(C)**\nhow to override an AI/CDSS output;\n**(D)**\nAI/CDSS development processes and any data or other inputs involved in such processes; and\n**(E)**\nany potential limitations for AI/CDSS, including any potential areas of bias in the AI/CDSS;\n**(4)**\nestablish and maintain an AI/CDSS committee that shall\u2014\n**(A)**\nconvene upon the date that is later of\u2014\n**(i)**\nthe date of the adoption of AI/CDSS at the covered entity; or\n**(ii)**\n120 days after the date of enactment of this Act;\n**(B)**\nbe comprised of at least as many non-managers as managers;\n**(C)**\ninclude membership of any labor organization, or other authorized representative, of health care professionals employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity;\n**(D)**\nprovide consultation to the covered entity in developing policies and practices related to the use of AI/CDSS, including policy required under subparagraphs (A) through (D) of paragraph (1); and\n**(E)**\nmeet at least quarterly to\u2014\n**(i)**\nreview implementation of policies adopted by the covered entity with respect to AI/CDSS; and\n**(ii)**\nreport to the covered entity on findings and suggestions for improvements; and\n**(5)**\nreview\u2014\n**(A)**\nall findings and suggestions from the AI/CDSS committee provided under paragraph (4)(E)(ii); and\n**(B)**\nany other feedback from health care professionals employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity on the AI/CDSS technology and the policies of the entity with respect to such technology, including by reviewing any such feedback on patterns of issues with the AI/CDSS, such as incorrect or biased outputs that require frequent override.\n##### (b) Data sharing exception\nThe prohibition under subsection (a)(1)(D) shall not apply\u2014\n**(1)**\nin a case in which a covered entity is informing a patient or an authorized representative of a patient about a decision rendered in the administration of the care of such patient; or\n**(2)**\nin a case of a civil, criminal, or administrative action involving medical malpractice, negligence, or violation of any law.\n##### (c) Oversight mechanism\nNothing in this Act shall prohibit a covered entity from reviewing the performance outcomes of AI/CDSS.\n#### 102. Enforcement\n##### (a) In general\nExcept as provided in subsection (c), the Secretary of Health and Human Services, acting through the Office for Civil Rights (referred to in this title as the Secretary ), shall receive, investigate, and attempt to resolve, including through imposing civil monetary penalties, complaints of violations of this title in the same manner as the Secretary receives, investigates, and attempts to resolve, including through imposing civil monetary penalties, complaints of violations of part C of title XI of the Social Security Act ( 42 U.S.C. 1320d et seq. ).\n##### (b) Civil monetary penalties\nThe provisions of section 1128A of the Social Security Act ( 42 U.S.C. 1320a\u20137a ) (other than subsections (a) and (b) and the second sentence of subsection (f)) shall apply to the imposition of a civil monetary penalty under this section in the same manner as such provisions apply to the imposition of a penalty under such section 1128A.\n##### (c) Exception\nNo complaint of a violation of this title shall be referred to the Attorney General for investigation as a criminal violation.\n#### 103. Regulations\n##### (a) In general\nThe Secretary may prescribe such regulations as may be necessary to carry out this title.\n##### (b) Consultation\nIn prescribing any regulations authorized under this section, the Secretary\u2014\n**(1)**\nshall consult with the Secretary of Labor; and\n**(2)**\nmay consult with\u2014\n**(A)**\nother Federal agencies that have expertise in artificial intelligence or health care; and\n**(B)**\nother Federal agencies that have jurisdiction over labor and employment issues, including the Equal Employment Opportunity Commission, the Department of Justice, and the National Labor Relations Board.\nII\nAdverse employment actions; whistleblower protections\n#### 201. Prohibition on adverse employment actions\nNo covered entity shall take an adverse employment action against a health care professional employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity because the health care professional overrides an AI/CDSS output in a manner consistent with the requirements under section 101.\n#### 202. Whistleblower protections\nNo covered entity shall discriminate or retaliate (including through intimidation, threats, coercion, or harassment) against any individual employed by, or otherwise engaged in the performance of work for remuneration for, the covered entity\u2014\n**(1)**\nbecause the individual exercises, or attempts to exercise, any right provided under this Act; or\n**(2)**\nbecause the individual (or another individual or representative acting at the request of the individual) has\u2014\n**(A)**\nfiled a written or oral complaint to the covered entity or a Federal, State, local, or Tribal government entity of a possible violation of this Act;\n**(B)**\nsought assistance or intervention with respect to an AI/CDSS-related concern from the covered entity, a Federal, State, local, or Tribal government, or any individual or entity representing workers;\n**(C)**\ninstituted, caused to be instituted, or otherwise participated in any inquiry or proceeding under or related to this Act;\n**(D)**\ngiven, or is about to give, any information in connection with any inquiry or proceeding relating to any right provided under this Act;\n**(E)**\ntestified, or is about to testify, in any inquiry or proceeding relating to any right provided under this Act; or\n**(F)**\ndiscussed a possible violation of this Act with a co-worker.\n#### 203. Enforcement\n##### (a) Enforcement by Department of Labor\n**(1) Investigation**\n**(A) In general**\nTo ensure compliance with this title, the Secretary of Labor (referred to in this title as the Secretary )\u2014\n**(i)**\nshall have\u2014\n**(I)**\nthe investigative authority provided under section 11(a) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(a) ); and\n**(II)**\nthe subpoena authority provided under section 9 of such Act ( 29 U.S.C. 209 ); and\n**(ii)**\nmay require, by general or special orders, a covered entity to file with the Secretary, in such form as the Secretary may prescribe, annual or special reports or answers in writing to specific questions (including information and records) as the Secretary may require as to the organization, business, conduct, practices, management, and relation to other corporations, partnerships, and individuals, of the covered entity.\n**(B) Reports and answers**\nA covered entity shall file any reports and answers (including information and records) required under subparagraph (A)(ii) in such manner, including under oath or otherwise, and within such reasonable time period as the Secretary may require.\n**(C) Joint investigations**\nThe Secretary may conduct investigations and make requests for information, as authorized under this Act, on a joint basis with another Federal agency, a State attorney general, or a State agency.\n**(D) Obligation to keep, preserve, and make available records**\nA covered entity shall make, keep, preserve, and make available to the Secretary records pertaining to compliance with this title in accordance with section 11(c) of the Fair Labor Standards Act of 1938 ( 29 U.S.C. 211(c) ) and in accordance with any regulation or order issued by the Secretary.\n**(2) Enforcement**\nThe Secretary shall receive, investigate, and attempt to resolve complaints of violations of this title in the same manner that the Secretary receives, investigates, and attempts to resolve complaints of violations of sections 6 and 7 of the Fair Labor Standards Act of 1938 (29 U.S.C. 206 and 207).\n**(3) Civil monetary penalties**\nSubject to subsection (c), the Secretary may impose a civil monetary penalty on any person that violates this title\u2014\n**(A)**\nin an amount of not more than $76,987 per violation; or\n**(B)**\nfor repeat violations, in an amount of not more than $769,870 per violation.\n**(4) Administrative complaints**\nAn individual adversely affected by an alleged violation of this title may\u2014\n**(A)**\nfile a complaint of a violation of this title with the Secretary; and\n**(B)**\ndesignate a representative of a labor organization, regardless of the relationship between the individual and the labor organization, to\u2014\n**(i)**\nfile the complaint on behalf of the individual; or\n**(ii)**\nrepresent the individual for purposes of engagement with the Secretary regarding such complaint, including being present at worker interviews and participating in workplace inspections, conferences, and settlement negotiations.\n**(5) Litigation**\nThe Solicitor of Labor may appear for and represent the Secretary on any litigation brought under this subsection. If the Secretary determines that a covered entity has violated this title, the Secretary may file a civil action in any appropriate United States district court to obtain injunctive relief to enforce this title.\n**(6) Burdens of proof**\nAll complaints under this subsection shall be governed by the legal burdens of proof set forth in section 42121(b) of title 49, United States Code.\n##### (b) Private right of action\n**(1) In general**\nNotwithstanding any action by the Secretary under subsection (a), any individual adversely affected by an alleged violation of this title (or a representative on behalf of such individual) may commence a civil action against any covered entity that violates this title in any Federal court of competent jurisdiction.\n**(2) Relief**\n**(A) In general**\nIn a civil action brought under paragraph (1) in which the individual described in such paragraph prevails, the court may award the individual\u2014\n**(i)**\ndamages of\u2014\n**(I)**\nan amount equal to the sum of any actual damages including back pay sustained by the individual; or\n**(II)**\nnot more than treble damages;\n**(ii)**\nstatutory damages described in subparagraph (B);\n**(iii)**\ninjunctive relief;\n**(iv)**\nequitable relief;\n**(v)**\nreasonable attorney fees and litigation costs; and\n**(vi)**\nwhile the action is pending, temporary relief, including temporary reinstatement.\n**(B) Statutory damages**\n**(i) In general**\nThe court may, in accordance with clause (ii), award statutory damages under subparagraph (A)(ii) against a covered entity in the following amounts:\n**(I)**\nFor each violation of section 201 (regarding adverse employment actions), the court may award damages of an amount (subject to subsection (c)) of not less than $5,000 and not more than $20,000.\n**(II)**\nFor each violation of section 202 (regarding whistleblower protections), the court may award damages of an amount (subject to subsection (c)) of not less than $10,000 and not more than $100,000.\n**(ii) Considerations for statutory damages**\nIn determining the amount of statutory damages assessed under this subparagraph against a covered entity, the court shall consider any relevant circumstances presented by the parties to the action, including\u2014\n**(I)**\nthe nature and seriousness of the violation;\n**(II)**\nthe number of violations;\n**(III)**\nthe persistence of the misconduct;\n**(IV)**\nthe length of time over which the misconduct occurred;\n**(V)**\nthe willfulness of the misconduct; and\n**(VI)**\nthe assets, liabilities, and net worth of the covered entity.\n**(3) Remedies for State workers**\n**(A) Waiver of sovereign immunity**\nA State\u2019s receipt or use of Federal financial assistance for any program or activity of a State shall constitute a waiver of sovereign immunity, under the 11th Amendment to the Constitution of the United States or otherwise, to a suit under this subsection for the relief described in paragraph (2) authorized under this subsection brought by an individual employed under, or otherwise engaged in the performance of work for remuneration under, that program or activity.\n**(B) Official capacity**\nAn official of a State may be sued in the official capacity of the official by any individual who has complied with the procedures under this paragraph, for injunctive relief that is authorized under this subsection. In such a suit the court may award to the prevailing party those costs authorized by section 722 of the Revised Statutes ( 42 U.S.C. 1988 ).\n**(C) Applicability**\nWith respect to a particular program or activity, subparagraph (A) applies to conduct that occurs\u2014\n**(i)**\nafter the date of enactment of this Act; and\n**(ii)**\non or after the day on which a State first receives or uses Federal financial assistance for that program or activity.\n**(4) Definition of program or activity**\nIn this subsection, the term program or activity has the meaning given the term in section 606 of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d\u20134a ).\n##### (c) Inflation adjustment\n**(1) In general**\nSubject to paragraphs (2) and (3), the Secretary, not later than September 1 of each calendar year, shall adjust the dollar amounts referred to in subsections (a)(3) and (b)(2)(B)(i) by the percent increase, if any, in the consumer price index for all urban consumers (United States city average), or a successor index, as determined by the Bureau of Labor Statistics, or a successor agency, for the most recent 12-month period for which data is available.\n**(2) Rounding**\nAny adjustment under paragraph (1) that is not a multiple of $10 shall be rounded to the nearest multiple of $10.\n**(3) Publication**\nThe Secretary shall publish the adjusted amounts under paragraph (1) in the Federal Register, and on the official website of the Department of Labor, not later than October 1, of the applicable calendar year for the increase under such paragraph.\n**(4) Effective date**\nEach adjustment under paragraph (1) shall take effect on January 1 of the first calendar year beginning after the date of the increase under such paragraph.\n##### (d) Arbitration and class action\nNotwithstanding any other provision of law, no predispute arbitration agreement or predispute joint-action waiver shall be valid or enforceable with respect to any alleged violation of this title.\n#### 204. Regulations\n##### (a) In general\nThe Secretary may prescribe such regulations as may be necessary to carry out this title.\n##### (b) Consultation\nIn prescribing any regulations authorized under this section, the Secretary\u2014\n**(1)**\nshall consult with the Secretary of Health and Human Services; and\n**(2)**\nmay consult with\u2014\n**(A)**\nother Federal agencies that have expertise in artificial intelligence or health care; and\n**(B)**\nother Federal agencies that have jurisdiction over labor and employment issues, including the Equal Employment Opportunity Commission, the Department of Justice, and the National Labor Relations Board.\nIII\nGeneral provisions\n#### 301. Educational materials for covered entities and health care professionals\nNot later than 1 year after the date of enactment of this Act, the Secretary of Health and Human Services, in consultation with the Secretary of Labor, shall develop and disseminate education materials for\u2014\n**(1)**\ncovered entities with respect to the compliance of such entities with the requirements under this Act; and\n**(2)**\nhealth care professionals to inform such professionals of their rights and protections under this Act.\n#### 302. State enforcement\n##### (a) In general\nIn any case in which a State attorney general or a State privacy regulator has reason to believe that an interest of the residents of a State has been or is adversely affected by any covered entity that violates any provision of this Act, the State attorney general or State privacy regulator, as parens patriae, may bring a civil action on behalf of the residents of the State in an appropriate State court or an appropriate district court of the United States to\u2014\n**(1)**\nenjoin further violation of such provision by the covered entity;\n**(2)**\ncompel compliance with such provision;\n**(3)**\nobtain damages, civil penalties, restitution, or other compensation on behalf of the residents of the State; or\n**(4)**\nobtain reasonable attorney\u2019s fees and other litigation costs reasonably incurred.\n##### (b) Rights of agency\nBefore initiating a civil action under subsection (a), the State attorney general or State privacy regulator, as the case may be, shall notify the Secretary in writing of such civil action. Upon receiving such notice, the Secretary may\u2014\n**(1)**\nintervene in such action; and\n**(2)**\nupon intervening\u2014\n**(A)**\nbe heard on all matters arising in such civil action; and\n**(B)**\nfile petitions for appeal of a decision in such action.\n##### (c) Preemptive action by agency\nIn any case in which a civil action is instituted by or on behalf of the Secretary for a violation of this Act, a State attorney general or State privacy regulator may not, during the pendency of such action, institute a civil action against any defendant named in the complaint in the action instituted by or on behalf of the Secretary for a violation that is alleged in such complaint. In a case brought by the Secretary that affects the interests of a State, the State attorney general or State privacy regulator may intervene as of right pursuant to the Federal Rules of Civil Procedure.\n##### (d) Preservation of State powers\nExcept as provided in subsection (c), no provision of this Act shall be construed as altering, limiting, or affecting the authority of a State attorney general or State privacy regulator to\u2014\n**(1)**\nbring an action or other regulatory proceeding arising solely under the laws in effect in that State; or\n**(2)**\nexercise the powers conferred on the State attorney general or State privacy regulator by the laws of the State, including the ability to conduct investigations, administer oaths or affirmations, or compel the attendance of witnesses or the production of documentary or other evidence.\n##### (e) Definition of Secretary\nIn this section, the term Secretary means\u2014\n**(1)**\nwith respect to a violation of title I, the Secretary of Health and Human Services; and\n**(2)**\nwith respect to a violation of title II, the Secretary of Labor.\n#### 303. Rule of construction\nNothing in this Act shall protect a health care professional from a medical malpractice or negligence claim for health care services provided through overriding an AI/CDSS output.\n#### 304. Non-preemption\nNothing in this Act shall preempt a State law or collective bargaining agreement.",
      "versionDate": "2025-10-09",
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
        "name": "Health",
        "updateDate": "2025-12-09T17:29:09Z"
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
      "date": "2025-10-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2997is.xml"
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
      "title": "Right to Override Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T03:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Right to Override Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect the independent judgment of health care professionals acting in the scope of their practice in overriding AI/CDSS outputs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:16Z"
    }
  ]
}
```
