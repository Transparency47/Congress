# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2937?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2937
- Title: AI LEAD Act
- Congress: 119
- Bill type: S
- Bill number: 2937
- Origin chamber: Senate
- Introduced date: 2025-09-29
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-29: Introduced in Senate
- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S6836-6838)
- Latest action: 2025-09-29: Introduced in Senate

## Actions

- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S6836-6838)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-29",
    "latestAction": {
      "actionDate": "2025-09-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2937",
    "number": "2937",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "AI LEAD Act",
    "type": "S",
    "updateDate": "2026-03-20T11:03:19Z",
    "updateDateIncludingText": "2026-03-20T11:03:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-29",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S6836-6838)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-29",
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
            "date": "2025-09-30T00:00:55Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T00:00:55Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-09-29",
      "state": "MO"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-18",
      "state": "VT"
    },
    {
      "bioguideId": "K000383",
      "firstName": "Angus",
      "fullName": "Sen. King, Angus S., Jr. [I-ME]",
      "isOriginalCosponsor": "False",
      "lastName": "King",
      "middleName": "S.",
      "party": "I",
      "sponsorshipDate": "2026-03-18",
      "state": "ME"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "False",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2937is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2937\nIN THE SENATE OF THE UNITED STATES\nSeptember 29, 2025 Mr. Durbin (for himself and Mr. Hawley ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish legal standards for advanced artificial intelligence products.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Aligning Incentives for Leadership, Excellence, and Advancement in Development Act or the AI LEAD Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nTITLE I\u2014Aligning incentives for safety, innovation and United States competitiveness\nSec. 101. Developer liability for harm to business or consumer.\nSec. 102. Deployer liability for harm to business or consumer.\nTITLE II\u2014Unconscionable liability limitations\nSec. 201. Unconscionable liability limitations.\nTITLE III\u2014Enforcement\nSec. 301. Federal cause of action.\nSec. 302. Special rule for deployers.\nSec. 303. Period of limitations.\nSec. 304. Preemption.\nSec. 305. Severability.\nTITLE IV\u2014Registration of foreign artificial intelligence system providers\nSec. 401. Foreign agent registration requirement.\nSec. 402. Enforcement.\nSec. 403. Public registry.\nTITLE V\u2014Effective date\nSec. 501. Effective date.\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence systems are products that shift decision-making power and responsibility away from humans to software-based systems, often without direct human oversight.\n**(2)**\nThese products, while holding great promise, have caused and will cause harm to businesses and individuals. For example, multiple teenagers have tragically died after being exploited by an artificial intelligence chatbot.\n**(3)**\nUnpredictable allocations of liability jeopardize public safety and the financial well-being of both individuals and entire industries, particularly the small businesses of the United States, and adversely affect the Federal Government and taxpayers.\n**(4)**\nProduct liability law can help to address harms caused by artificial intelligence systems that affect interstate commerce by incentivizing safety, providing certainty to artificial intelligence developers and deployers to continue to innovate, and ensuring the competitiveness of the United States.\n**(5)**\nA Federal products liability framework for artificial intelligence systems will remove barriers to interstate commerce and protect individuals\u2019 due process rights.\n**(6)**\nThis Act establishes Federal legislative guidelines for products liability without implicating expressive speech to ensure more predictable legal outcomes for individuals and industries and promotes business innovation.\n#### 3. Definitions\nIn this Act:\n**(1) Artificial intelligence system**\n**(A) In general**\nThe term artificial intelligence system means any software, data system, application, tool, or utility\u2014\n**(i)**\nthat is capable of making or facilitating predictions, recommendations, actions, or decisions for a given set of human-or machine-defined objectives; and\n**(ii)**\nthat uses machine learning algorithms, statistical or symbolic models, or other algorithmic or computational methods (whether dynamic or static) that affect or facilitate actions or decision-making in real or virtual environments.\n**(B) Inclusion**\nAn artificial intelligence system may be integrated into, or operate in conjunction with, other hardware or software.\n**(2) Claimant**\nThe term claimant means any person, including a class of persons, who brings a liability action.\n**(3) Covered product**\nThe term covered product means an artificial intelligence system.\n**(4) Deployer**\nThe term deployer means a person, including a developer, who uses or operates a covered product for\u2014\n**(A)**\nthe person's own personal or commercial use; or\n**(B)**\nuse by a third party.\n**(5) Design**\nThe term design , with respect to a covered product\u2014\n**(A)**\nmeans the intended or known material characteristics of the covered product; and\n**(B)**\nincludes\u2014\n**(i)**\nany intended or known formulation of the covered product and the usual result of the intended development or other processes used to produce the covered product, including unexpected skills or behaviors that appear in the covered product;\n**(ii)**\nthe selection of any data used for training a covered product through fitting its learnable parameters; and\n**(iii)**\ntraining, testing, auditing, and fine-tuning the covered product.\n**(6) Developer**\nThe term developer means a person who designs, codes, produces, owns, or substantially modifies a covered product for\u2014\n**(A)**\nthe person's own personal or commercial use; or\n**(B)**\nuse by a third party.\n**(7) Express warranty**\nThe term express warranty means any material, positive statement, affirmation of fact, promise, or description relating to a covered product, including any sample or model of a covered product.\n**(8) Harm**\nThe term harm means, with respect to the effect of the use of a covered product\u2014\n**(A)**\ndamage to property other than the covered product itself;\n**(B)**\npersonal physical injury, illness, or death;\n**(C)**\nfinancial or reputational injury;\n**(D)**\nmental or psychological anguish, emotional distress, or distortion of a person\u2019s behavior that would be highly offensive to a reasonable person; or\n**(E)**\nany loss of consortium or services or other loss deriving from any type of harm described in subparagraph (A), (B), (C), or (D).\n**(9) Liability action**\nThe term liability action means a civil action brought under section 301 based on any theory for harm caused by a covered product or covered product use.\n**(10) Person**\nThe person means any individual, corporation, company, association, firm, partnership, society, joint stock company, or other entity, including any government entity or unincorporated association of persons.\n**(11) Substantial modification**\nThe term substantial modification , with respect to a covered product\u2014\n**(A)**\nmeans any deliberate change made to the covered product by a deployer that\u2014\n**(i)**\nwas not authorized or reasonably anticipated by the developer when the covered product left the control of the developer; and\n**(ii)**\nchanges the purpose, use, function, design, or intended use or manner of use of the covered product from that for which the covered product was originally designed, tested, or intended; and\n**(B)**\ndoes not include a modification that solely reduces or mitigates a new or additional risk.\n**(12) Under a legal disability**\nThe term under a legal disability , with respect to a person, means the person lacks the capacity to understand, make, or communicate decisions regarding the person's legal rights\u2014\n**(A)**\nbecause of a mental illness or intellectual disability; or\n**(B)**\nbecause the person is under the age of 18.\nI\nAligning incentives for safety, innovation and United States\n                competitiveness\n#### 101. Developer liability for harm to business or consumer\n##### (a) In general\nIn any liability action, the developer shall be liable to a claimant if the claimant establishes by a preponderance of the evidence\u2014\n**(1)**\nthat\u2014\n**(A)**\nthe developer failed to exercise reasonable care with respect to the design of the covered product; and\n**(B)**\nthe failure to exercise reasonable care was a proximate cause of harm to the claimant;\n**(2)**\nthat\u2014\n**(A)**\nthe developer failed to exercise reasonable care with respect to providing adequate instructions or warnings applicable to the covered product that allegedly caused the harm that is the subject of the complaint; and\n**(B)**\nthe failure to exercise reasonable care with respect to providing adequate instructions or warnings was a proximate cause of harm to the claimant;\n**(3)**\nthat\u2014\n**(A)**\nthe developer made an express warranty applicable to the covered product that allegedly caused the harm that is the subject of the complaint;\n**(B)**\nthe covered product failed to conform to the warranty; and\n**(C)**\nthe failure of the covered product to conform to the warranty was a proximate cause of harm to the claimant; or\n**(4)**\nthat\u2014\n**(A)**\nthe covered product was, at the time of sale or distribution, in a defective condition unreasonably dangerous when used or misused in a reasonably foreseeable manner; and\n**(B)**\nthe defective condition was a proximate cause of the harm to the claimant.\n##### (b) Defective design\n**(1) In general**\nIn any liability action against a developer alleging that a covered product is unreasonably dangerous because of a defective design, as described in subsection (a)(1), the claimant shall be required to prove that, at the time of sale or distribution of the covered product by the developer, the foreseeable risks of harm posed by the covered product could have been reduced or avoided by the adoption of a reasonable alternative design by the developer, and the omission of the alternative design renders the covered product not reasonably safe.\n**(2) Manifestly unreasonable design**\nNotwithstanding paragraph (1), in a liability action described in that paragraph, if the design of a covered product is found to be manifestly unreasonable, a claimant shall not be required to prove the existence of a reasonable alternative design.\n**(3) Circumstantial evidence supporting inference of covered product defect**\nIn a liability action described in subsection (a)(1), it may be inferred that the harm sustained by the claimant was caused by a covered product defect existing at the time of sale or distribution, without proof of a specific defect, when the incident that harmed the claimant\u2014\n**(A)**\nwas of a kind that ordinarily occurs as a result of covered product defect; and\n**(B)**\nwas not, in the particular case, solely the result of causes other than covered product defect existing at the time of sale or distribution.\n**(4) Noncompliance and compliance with required covered product safety statutes or regulations**\n**(A) Noncompliance**\nFor purposes of a liability action described in subsection (a)(1), if a covered product does not comply with an applicable covered product safety statute or administrative regulation, the covered product shall be deemed defective with respect to the risks sought to be reduced by the statute or regulation.\n**(B) Compliance**\nFor purposes of a liability action described in subsection (a)(1), the court may consider a covered product\u2019s compliance with an applicable covered product safety statute or administrative regulation in determining whether the covered product is defective with respect to the risks sought to be reduced by the statute or regulation, but such compliance does not preclude as a matter of law a finding of covered product defect.\n##### (c) Failure to warn\n**(1) In general**\nFor purposes of a liability action described in subsection (a)(2), a covered product shall be considered defective because of inadequate instructions or warnings if\u2014\n**(A)**\nthe foreseeable risks of harm posed by the covered product could have been reduced or avoided by the provision of reasonable instructions or warnings by the developer; and\n**(B)**\nthe omission of the instructions or warnings renders the covered product not reasonably safe.\n**(2) Adequate instruction or warning**\nFor purposes of paragraph (1), an adequate instruction or warning is one that a reasonably prudent person in the same or similar circumstances would have provided with respect to a reasonably foreseeable risk and that communicates sufficient information on the reasonably foreseeable risks and safe use of the covered product, taking into account the characteristics of, and the ordinary knowledge common to, an ordinary user of the covered product.\n**(3) Knowledge**\nIn a liability action described in subsection (a)(2), the claimant shall be required to prove that, at the time the covered product left the developer\u2019s control, the developer knew of or, in light of then-existing scientific and technical knowledge, reasonably should have foreseen, the risk that caused the claimant\u2019s harm.\n**(4) Open and obvious**\n**(A) In general**\nIn a liability action described in subsection (a)(2), a developer shall not be liable for failure to instruct or warn about a foreseeable risk that is open and obvious to the user of the covered product, taking into account the characteristics of, and the ordinary knowledge common to, an ordinary user of the covered product.\n**(B) Minors**\nFor purposes of subparagraph (A), a risk shall be presumed to not be open and obvious to a user of a covered product who is under 18 years old.\n**(5) Noncompliance and compliance with required covered product safety statutes or regulations**\n**(A) Noncompliance**\nIn a liability action described in subsection (a)(2), if a covered product does not comply with an applicable covered product safety statute or administrative regulation, the covered product shall be deemed defective due to inadequate instructions or warnings with respect to the risks sought to be reduced by the statute or regulation.\n**(B) Compliance**\nIn a liability action described in subsection (a)(2), the court may consider a covered product\u2019s compliance with an applicable covered product safety statute or administrative regulation in determining whether the covered product is defective due to inadequate instructions or warnings with respect to the risks sought to be reduced by the statute or regulation, but such compliance does not preclude as a matter of law a finding of covered product defect.\n##### (d) Strict liability of developer for unreasonably dangerous or defective covered products\n**(1) In general**\nIn a liability action described in subsection (a)(4), the developer of a covered product shall be strictly liable for harm caused by the defective condition of the covered product, notwithstanding\u2014\n**(A)**\nthat the developer exercised all possible care in the design or distribution of the covered product; or\n**(B)**\nthat the claimant did not purchase the covered product directly from the developer or otherwise enter into a contractual relationship with the developer.\n**(2) Substantial modification**\nA developer shall not be liable under subsection (a)(4) for harm solely caused by a substantial modification.\n#### 102. Deployer liability for harm to business or consumer\n##### (a) In general\nA deployer shall be deemed to be liable as a developer under section 101 for harm caused by a covered product if\u2014\n**(1)**\nthe deployer makes a substantial modification to the covered product; or\n**(2)**\nthe deployer intentionally misuses the covered product contrary to its intended use and that misuse is the proximate cause of harm to the claimant.\n##### (b) Use intended by developer is not modification or misuse\n**(1) In general**\nFor purposes of subsection (a), a use of a covered product that is intended by the developer of the covered product does not constitute a substantial modification to or misuse of the covered product.\n**(2) Inference of intended use**\nFor purposes of paragraph (1), if a developer does not specify an intended use for a covered product, intended use shall be inferred by the targeted market and manner of distribution.\n##### (c) Licensing\nSubject to section 302, any deployer licensing a covered product shall not be liable to a claimant for a violation of section 101 solely by reason of ownership or use of the covered product.\nII\nUnconscionable liability limitations\n#### 201. Unconscionable liability limitations\n##### (a) Contract with deployer\n**(1) Prohibition**\nA developer may not include language in a contract with a deployer that waives any right, proscribes any forum or procedure, or unreasonably limits liability under this Act or applicable State law related to harm caused by the covered product under section 101.\n**(2) Unenforceable**\nLanguage in a contract that violates paragraph (1) shall be unenforceable.\n##### (b) Terms and conditions\n**(1) Prohibition**\nA developer or a deployer may not include language in terms and conditions relevant to a covered product that waives any right, proscribes any forum or procedure, or unreasonably limits liability under this Act or applicable State law related to harm caused by the covered product under section 101 or 102.\n**(2) Unenforceable**\nLanguage in terms and conditions that violates paragraph (1) shall be unenforceable.\nIII\nEnforcement\n#### 301. Federal cause of action\nThe Attorney General, any attorney general of a State, an individual or the legal representative of such an individual, or a class of individuals may bring a civil action in a district court of the United States against a developer or deployer for a violation of section 101, 102, or 201 to obtain\u2014\n**(1)**\ninjunctive relief;\n**(2)**\nin a case brought by the Attorney General, civil penalties;\n**(3)**\ndamages, restitution, or other compensation on behalf of individuals;\n**(4)**\nreasonable attorney fees and other litigation costs reasonably incurred; or\n**(5)**\nin a case brought by the Attorney General or a State attorney general, such other relief as the Attorney General or State attorney general may consider to be appropriate.\n#### 302. Special rule for deployers\n##### (a) Standing in for the developer\nIf the developer is not a party to a liability action because the developer is not subject to the court's jurisdiction, is insolvent, or cannot otherwise be made to answer for the harm, the deployer may be held liable to the same extent that the developer would have been liable under section 101.\n##### (b) Dismissal of deployer\nA court shall dismiss the deployer from a liability action, upon motion, if\u2014\n**(1)**\nthe developer\u2014\n**(A)**\nis a party to the action; and\n**(B)**\nis subject to the court\u2019s jurisdiction;\n**(2)**\nthe developer is not insolvent or otherwise unable to satisfy any likely judgment; and\n**(3)**\nthe deployer is not otherwise liable under section 102.\n##### (c) Joint fault\n**(1) In general**\nIf both the developer and the deployer contributed to the harm under sections 101 and 102, each person may be held jointly and severally liable for the portion of harm caused by that person's conduct.\n**(2) Rule of construction**\nNothing in this subsection shall limit the right of a claimant to maintain a liability action against the developer, the deployer, or both, if the claimant can establish that each person contributed to the harm under sections 101 and 102.\n##### (d) Indemnification and attorney fees\n**(1) Right to seek indemnification**\nA deployer that is held liable for harm caused by the developer under subsection (a) may pursue indemnification, including the recovery of attorney fees and litigation costs, from the developer.\n**(2) Limitation**\nIf the deployer is determined to be at fault for a portion of the harm under subsection (c), indemnification under paragraph (1) of this subsection shall be limited to the portion of damages, fees, or costs attributable to the conduct of the developer.\n##### (e) Preservation of claimant\u2019s rights\nNothing in this subsection shall limit the right of the claimant to maintain a liability action against the developer, the deployer, or both persons, if the claimant can establish that each person contributed to the harm under sections 101 and 102.\n#### 303. Period of limitations\n##### (a) In general\nExcept as provided in subsection (b), a liability action may be filed not later than 4 years after the date on which the claimant discovered or, in the exercise of reasonable care, should have discovered\u2014\n**(1)**\nthe harm that is the subject of the action; and\n**(2)**\nthe cause of the harm.\n##### (b) Legal disability\nIn the case of a person who is under a legal disability, the period of limitations under subsection (a) for a liability action brought by that person shall be tolled until the person ceases to be under a legal disability.\n##### (c) Tolling\nThe period of limitations under subsection (a) shall be tolled from the date of the filing of a complaint against a developer or deployer to the date that a court enters a final judgment in the case.\n#### 304. Preemption\n##### (a) In general\nThis Act supersedes State law only where State law conflicts with the provisions of this Act.\n##### (b) Minimum protections\nNothing in this Act shall prevent a State from enacting or enforcing protections that align with the principles of harm prevention, accountability, and transparency for a covered product that are stronger than such protections under this Act.\n#### 305. Severability\nIf any provision of this Act, or an amendment made by this Act, is determined to be unenforceable or invalid, the remaining provisions of this Act and amendments made by this Act shall not be affected.\nIV\nRegistration of foreign artificial intelligence system developers\n#### 401. Foreign agent registration requirement\n##### (a) Designation required\nBefore making a covered product available in the United States, a foreign developer shall designate an agent for service of process.\n##### (b) Requirements\nThe designation of an agent under subsection (a) shall\u2014\n**(1)**\nbe in writing and submitted to the Attorney General;\n**(2)**\ninclude a written acceptance by the agent; and\n**(3)**\nspecify the full legal name and address of both the foreign developer and the agent.\n##### (c) Agent qualifications\nA designated agent under subsection (a) shall be a permanent resident of the United States.\n##### (d) Updates\nA foreign developer of a covered product shall notify the Attorney General of any change to the designated agent under subsection (a) or the contact information thereof not later than 15 days after the change.\n#### 402. Enforcement\n##### (a) Prohibition\nA foreign developer of a covered product that fails to designate an agent in accordance with section 401 may not deploy any covered product in the United States.\n##### (b) Enforcement\nThe Attorney General may seek injunctive relief to prevent a violation of subsection (a).\n#### 403. Public registry\nThe Attorney General shall maintain a publicly accessible registry of designated agents of foreign developers of covered products.\nV\nEffective date\n#### 501. Effective date\nThis Act shall apply with respect to any liability action commenced on or after the date of enactment of this Act without regard to whether the harm that is the subject of the liability action or the conduct that caused the harm occurred before that date of enactment.",
      "versionDate": "2025-09-29",
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
        "name": "Commerce",
        "updateDate": "2025-12-09T22:15:22Z"
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
      "date": "2025-09-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2937is.xml"
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
      "title": "AI LEAD Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI LEAD Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Aligning Incentives for Leadership, Excellence, and Advancement in Development Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish legal standards for advanced artificial intelligence products.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:18Z"
    }
  ]
}
```
