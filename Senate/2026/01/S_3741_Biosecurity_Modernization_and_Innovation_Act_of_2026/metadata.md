# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3741?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3741
- Title: Biosecurity Modernization and Innovation Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3741
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-20T18:07:49Z
- Update date including text: 2026-02-20T18:07:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3741",
    "number": "3741",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "Biosecurity Modernization and Innovation Act of 2026",
    "type": "S",
    "updateDate": "2026-02-20T18:07:49Z",
    "updateDateIncludingText": "2026-02-20T18:07:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T20:46:42Z",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2026-01-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3741is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3741\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Mr. Cotton (for himself and Ms. Klobuchar ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Commerce to promulgate regulations to improve nucleic acid synthesis security, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Biosecurity Modernization and Innovation Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) Covered provider**\nThe term covered provider means a person who\u2014\n**(A)**\nsynthesizes and sells synthetic nucleic acids to persons in the United States; or\n**(B)**\nproduces and distributes or sells, including resellers, equipment for synthesizing nucleic acids, including benchtop synthesizers, to persons in the United States.\n**(2) Director**\nThe term Director means the Director of the Office of Science and Technology Policy.\n**(3) Secretary**\nThe term Secretary means the Secretary of Commerce.\n**(4) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Standards and Technology.\n#### 3. Sense of Congress\nIt is the Sense of Congress that\u2014\n**(1)**\nthe field of biotechnology is accelerating and the United States is at risk of losing its biotechnology leadership to foreign adversaries;\n**(2)**\nthis acceleration of the field brings the United States into a period of both great opportunity and risk;\n**(3)**\npolicymaking for biosecurity, biosafety, and responsible innovation needs to be flexible to keep pace with advances in the biotechnology and ensure an environment that allows biotechnology research and industry to flourish;\n**(4)**\nthe current landscape of biosecurity and biosafety authorities is spread among multiple agencies, contributing to slow policymaking, which, coupled with the rapid advancement of biotechnology, becomes outdated quickly;\n**(5)**\nprevious studies conducted by the Government Accountability Office, the National Security Commission for Emerging Biotechnology, and several presidential administrations have already identified gaps in the Federal Government\u2019s oversight of biosecurity and biosafety risks;\n**(6)**\nthe United States Government needs to streamline biosecurity and biosafety authorities to ensure efficiency and clarity;\n**(7)**\ngene synthesis technology is becoming increasingly sophisticated and accessible, along with the ability to design novel nucleic acid sequences;\n**(8)**\nboth of these factors described in paragraph (7) may increase the risk of the development and deployment of new pathogens by bad actors; and\n**(9)**\ngene synthesis screening of orders and customers is immediately needed to mitigate risk in the short-term, which will act as a stopgap while the United States Government develops a comprehensive biosecurity and biosafety strategy that is appropriate for the dynamic and rapidly advancing field of biotechnology.\n#### 4. Nucleic acid synthesis security\n##### (a) Regulations required\nNot later than 1 year after the date of the enactment of this Act, the Secretary shall, in coordination with the Under Secretary and the heads of such other agencies as the Secretary considers appropriate, establish and maintain by regulation the following:\n**(1)**\nA requirement for covered providers to implement screening protocols for all sequences of concern included in the list established and maintained under paragraph (3). Such protocols shall\u2014\n**(A)**\ninclude the ability for privacy-preserving submission of information regarding orders for potential sequences of concern to a mechanism, which may be maintained by the Secretary or an independent organization designated by the Secretary, for facilitating effective split order detection across covered providers, utilizing the list established and maintained under paragraph (3); and\n**(B)**\nprioritize the mitigation of misuse of sequences capable of creating pathogens with pandemic potential.\n**(2)**\nA requirement for covered providers to implement screening protocols to verify the identity and legitimacy of customers.\n**(3)**\nA list of sequences of concern, which shall be determined by the Secretary in consultation with such heads of Federal departments and agencies, industry experts, academics, and researchers as the Secretary considers appropriate.\n**(4)**\nA system for reviewing and updating on a regular basis the list of sequences of concern established and maintained under paragraph (3) that\u2014\n**(A)**\nuses a docket to allow for privacy-preserving submissions from the public on recommendations for the list of sequences of concern;\n**(B)**\nincludes an expedited procedure to rapidly add sequences of concern to the list on a provisional basis, which may include, as far as technically feasible, automatic procedures such as algorithmic literature scanning, industry self-reporting, or inter-agency submissions; and\n**(C)**\nincorporates strong data security and confidentiality standards.\n**(5)**\nA conformity assessment system to verify that covered providers are adhering to the requirements established and maintained under paragraphs (1) and (2), which will include\u2014\n**(A)**\nan auditing process to ensure orders and customers have been scrutinized appropriately, including procedures to conduct adversarial testing (sometimes referred to as red-teaming ) at random intervals to ensure compliance; and\n**(B)**\na process to revoke conformity status of covered providers that fail to maintain compliance with the requirements established and maintained under paragraphs (1) and (2), including the establishment of a grace period for covered providers who have failed auditing or adversarial testing under subparagraph (B) to demonstrate compliance or mitigation steps.\n**(6)**\nSafeguards to ensure regulations promulgated under this subsection avoid unnecessary burden on innovation and industry by\u2014\n**(A)**\nallowing covered providers to offer an expedited review process for institutional customers, including accredited institutions of higher education, with demonstrated records of legitimacy;\n**(B)**\nproviding exemptions from customer screening requirements for sequences or products that are clearly non-hazardous and pose no credible threat to public health and safety based on scientific literature and industry best practices for biosecurity screening; and\n**(C)**\nconducting regular consultations with relevant experts to determine exempted sequences and minimize regulatory burden while maintaining security effectiveness.\n**(7)**\nA requirement that any person who receives Federal funds can only purchase nucleic acid synthesis products from a covered provider in compliance with the requirements in paragraphs (1) and (2).\n**(8)**\nA program to provide technical assistance upon request of a covered provider, including assistance with orders whose screening results are ambiguous, subject to determination by the Secretary, in consultation with the heads of such other Federal departments and agencies as the Secretary considers appropriate.\n##### (b) National Institute of Standards and Technology requirements\nThe Under Secretary shall develop best practices, technical standards, and other tools needed to support the administration of subsection (a), including the following:\n**(1)**\nTesting and evaluation of customer and order screening protocols to improve accuracy, efficacy, and reliability, and to support the conformity assessment system under of subsection (a)(5).\n**(2)**\nEvaluation of the sequences recommended for the list established and updated under paragraphs (3) and (4) of subsection (a), including by developing best practices and guidelines for determining if a novel sequence is a sequence of concern.\n**(3)**\nResearch and prototype sequence-to-function models to supplement the system established and maintained under subsection (a)(4).\n##### (c) Updates\nAs frequently as the Secretary considers appropriate to account for technological advances, but not less frequently than once every 2 years, the Secretary shall review and update the regulations promulgated under subsection (a).\n##### (d) Protection of customer information\nAny information about a customer included in a submission under paragraph (1)(A) or (4)(A) of subsection (a) shall, if applicable, be exempt from records access under section 552(b)(4) of title 5, United States Code.\n##### (e) Relationship with other Federal guidelines and recommendations\nThe regulations established and maintained under paragraphs (1) and (2) of subsection (a) shall supplant any Federal guidelines or recommendations relating to nucleic acid synthesis screening that\u2014\n**(1)**\nwere in effect before the date of the enactment of this Act; and\n**(2)**\nare voluntary.\n##### (f) Civil enforcement\n**(1) Civil action**\nThe Attorney General may bring a civil action in a court of competent jurisdiction against any person who violates a requirement promulgated under paragraph (1) or (2) of subsection (a), including through providing false or misleading information or engaging in other deceptive practices, or does not demonstrate compliance within the grace period set forth by subsection (a)(5)(C).\n**(2) Powers of the court**\nIn an action brought under paragraph (1), the court may\u2014\n**(A)**\nenjoin a violation described in paragraph (1); or\n**(B)**\naward damages under paragraph (3).\n**(3) Award of damages**\nA person who violates a requirement as described in paragraph (1) is liable for statutory damages\u2014\n**(A)**\nin the case of an individual, in the sum of not more than $500,000, adjusted from time to time under paragraph (4); and\n**(B)**\nin the case of a person who is not an individual, in the sum of not more than $750,000, adjusted from time to time under paragraph (4).\n**(4) Adjustments for inflation**\nEffective on October 1 of each year (beginning in the first fiscal year after the date of the enactment of this Act), the dollar amounts in effect under paragraph (3) shall be increased by a percentage equal to the percentage by which the Consumer Price Index for all urban consumers (U.S. city average) increased during the 12-month period ending with the last month for which Consumer Price Index data is available. In the event that such Consumer Price Index does not increase during such period, the dollar amount in effect under such paragraph during the previous fiscal year shall be maintained.\n##### (g) Reports to Congress\nNot less frequently than once each year, the Secretary shall submit to Congress a report on the administration of this section. Each such report shall include an overview of how many covered providers have been verified by the conformity assessment system established and maintained under subsection (a)(5).\n#### 5. Establishment of biotechnology governance sandbox\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Under Secretary shall, in collaboration with the heads of such Federal agencies as the Under Secretary considers relevant and with such persons in the private sector, academia, and civil society as the Under Secretary considers appropriate, establish a biotechnology governance sandbox environment.\n##### (b) Responsibilities\nThrough the governance sandbox developed under subsection (a), the Under Secretary shall\u2014\n**(1)**\nprovide secure testing of innovations or tools developed to advance the science of biosecurity, biosafety, and responsible biotechnology innovation;\n**(2)**\nfoster participation of nongovernmental experts in the development and testing of appropriate levels and methods of governance, to achieve the goals of\u2014\n**(A)**\nensuring the continued global competitiveness of biotechnology innovations in the United States;\n**(B)**\nbolstering the national security posture of the United States; and\n**(C)**\nstrengthening the ability of the United States to robustly analyze emerging threats, anticipate concerns, and govern proactively in the biotechnology space;\n**(3)**\ncarry out biological measurement research to support the development and improvement of technical standards for biosecurity, biosafety, and responsible biotechnology innovation; and\n**(4)**\nreport annually to the Secretary of Commerce on the administration of paragraph (2) and whether any promising governance strategies have resulted from the development and testing.\n##### (c) Access to environments\nThe Under Secretary may contract with the private sector or coordinate with other Federal agencies to access environments necessary to provide testing under subsection (b)(1).\n#### 6. Streamlining biosecurity and biosafety authorities across the Federal Government\n##### (a) Assessment and plan required\nNot later than 90 days after the date of the enactment of this Act, the Director shall, in collaboration with the heads of such Federal agencies as the Director considers relevant\u2014\n**(1)**\nassess the current state of biosecurity and biosafety oversight by the Federal Government; and\n**(2)**\ndevelop, based on the findings of the Director with respect to the assessment conducted under paragraph (1), an implementation plan to make oversight of biosecurity and biosafety by the Federal Government more effective and efficient.\n##### (b) Elements of assessment\nThe assessment required by subsection (a)(1) shall include the following:\n**(1)**\nA full accounting of Federal biosecurity and biosafety authorities and programs, including which agencies hold these authorities, whether these authorities are exercised effectively, and where there are overlaps or redundancies, real or perceived, in regulatory and enforcement authorities.\n**(2)**\nEngagement with industry stakeholders and academia to understand where there are challenges with compliance, communication, and information sharing.\n**(3)**\nIdentification of gaps in funding or other Government support for the development of research, innovation, and tools that advance the science of applied biosecurity, biosafety, and responsible biotechnology innovation.\n**(4)**\nIdentification of gaps in current Federal biosecurity and biosafety authorities and whether these gaps are hindering effective and efficient governance and assessment of emerging risks and opportunities in biotechnology.\n**(5)**\nAn evaluation of how consolidation of biosecurity and biosafety guidelines, authorities, and regulations across Federal agencies, including the regulations established and maintained under section 4(a), should be implemented to make oversight more effective and efficient and to address the gaps in such guidelines, authorities, and regulations, including those identified under paragraphs (3) and (4).\n##### (c) Report to Congress\n**(1) In general**\nNot later than 90 days after the date on which the Director completes the assessment required by paragraph (1) of subsection (a) and the implementation plan required by paragraph (2) of such subsection, the Director shall submit to Congress\u2014\n**(A)**\na report on the findings of the Director with respect to the assessment; and\n**(B)**\na copy of the implementation plan.\n**(2) Contents**\nThe report submitted pursuant to paragraph (1)(A) shall include the following:\n**(A)**\nThe findings of the Director with respect to the assessment conducted pursuant to subsection (a)(1).\n**(B)**\nRecommendations for legislative or administrative action to support the implementation plan developed under subsection (a)(2), according to\u2014\n**(i)**\nwhat, if any, new biosecurity and biosafety authorities are needed; and\n**(ii)**\nwhere the Federal Government can consolidate biosecurity and biosafety authorities, including which, if any, should be reside under a common government entity, and whether this necessitates establishing a new government entity.\n##### (d) Implementation\n**(1) In general**\nNot later than 90 days after the date on which the Director completes the implementation plan required by subsection (a)(2), the Director shall commence implementing the plan through administrative action in accordance with applicable provisions of law.\n**(2) Governance strategies**\nIn carrying out the implementation plan developed under subsection (a)(2), the Director shall consider which, if any, of the governance strategies reported under section 5(b)(4) should be included in the plan.",
      "versionDate": "2026-01-29",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-02-20T18:07:49Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3741is.xml"
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
      "title": "Biosecurity Modernization and Innovation Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T05:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Biosecurity Modernization and Innovation Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T05:23:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Commerce to promulgate regulations to improve nucleic acid synthesis security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T05:18:37Z"
    }
  ]
}
```
