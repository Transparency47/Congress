# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8094?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8094
- Title: AI Foundation Model Transparency Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8094
- Origin chamber: House
- Introduced date: 2026-03-26
- Update date: 2026-04-09T17:22:19Z
- Update date including text: 2026-04-09T17:22:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2026-03-26: Introduced in House

## Actions

- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Introduced in House
- 2026-03-26 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8094",
    "number": "8094",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001292",
        "district": "8",
        "firstName": "Donald",
        "fullName": "Rep. Beyer, Donald S. [D-VA-8]",
        "lastName": "Beyer",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "AI Foundation Model Transparency Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-09T17:22:19Z",
    "updateDateIncludingText": "2026-04-09T17:22:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-26",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T14:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8094ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8094\nIN THE HOUSE OF REPRESENTATIVES\nMarch 26, 2026 Mr. Beyer (for himself, Mr. Lawler , and Ms. Jacobs ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Federal Trade Commission to establish requirements for making information available to the public about the training data and algorithms used in artificial intelligence foundation models, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Foundation Model Transparency Act of 2026 .\n#### 2. Elements of foundation model transparency\n##### (a) Establishment of requirements\nNot later than 1 year after the date of the enactment of this Act, the Commission, in consultation with the Director of the National Institute of Standards and Technology, the Secretary of Commerce, the Director of the Office of Science and Technology Policy, and other relevant stakeholders (including standards bodies, covered entities, academia, technology experts, and advocates for civil rights and consumers), shall do the following:\n**(1)**\nIn accordance with section 553 of title 5, United States Code, promulgate regulations that:\n**(A)**\nEstablish requirements for covered entities with regard to foundation models to improve transparency of training data, documentation, testing, data collection during inference, and operations of foundation models, before commercial deployment and during the lifecycle of the system.\n**(B)**\nInclude requirements for a covered entity\u2014\n**(i)**\nto submit specified information related to each foundation model provided by the entity to the Commission; and\n**(ii)**\nto make publicly available certain information related to each foundation model provided by the entity.\n**(C)**\nSpecify the form and manner in which the information described in subparagraph (B)(ii) is made publicly available, including the following:\n**(i)**\nInformation that is required to be made available on the website of a covered entity that relates to any foundation model provided by the entity.\n**(ii)**\nInformation that is required to be displayed in a central location on a website hosted by the Commission, including, with respect to a foundation model, information that is substantially similar to the information required under clause (i).\n**(iii)**\nInformation submitted to the Commission that is not required to be publicly displayed, including sensitive or personally identifiable data or information, or information that would compromise the cybersecurity of the foundation model.\n**(iv)**\nA requirement for a human-readable and consumer-friendly format to be used with respect to the information described in clause (i).\n**(v)**\nA requirement for a machine-readable format to be used with respect to the information described under clause (ii).\n**(vi)**\nThe URL for the central location described in clause (ii).\n**(D)**\nProvide an option for a covered entity to be deemed in compliance with some or all of this Act if the covered entity publishes the information determined to be necessary by the Commission pursuant to subsection (a)(1)(A) as part of a larger document, including a system card or model card.\n**(E)**\nSpecify a process for a covered entity to submit the information required under subparagraph (B)(i) to the Commission.\n**(2)**\nIssue guidance to assist covered entities to comply with the standards established under paragraph (1).\n##### (b) Information To include\nThe Commission shall include in the regulations promulgated pursuant to subsection (a)(1)(A), with respect to a foundation model, the following information:\n**(1)**\nA sufficiently detailed summary of the sources of training data, how training data is collected, and whether and how data is collected and retained during inference.\n**(2)**\nA broad description of the size and composition of such training data, including types of demographic information, language information, and other attribute information, while accounting for privacy.\n**(3)**\nA description of data governance procedures.\n**(4)**\nA description of the intended purposes and foreseen limitations or risks of the foundation model, an overview of past edits to such model, the version and date of release of such model, the knowledge cutoff date of the training data of such model, and information on adverse incident monitoring and response procedures.\n**(5)**\nA list of or information about languages supported by the model.\n**(6)**\nA description of the efforts of the covered entity to align the foundation model and the transparency of such model with\u2014\n**(A)**\nthe AI Risk Management Framework (or any successor framework) of the National Institute of Standards and Technology;\n**(B)**\na similar Federal Government-approved consensus technical standard; or\n**(C)**\nthe model specification of any covered entity, including intended model behavior or outcomes and guardrails for the model.\n**(7)**\nPerformance under evaluation, either self-driven or through audit, on public or industry standard benchmarks, including what precautions the foundation model takes to answer or respond to situations with higher levels of risk of providing inaccurate or harmful information, including, if such model responds to such questions, relating to the following:\n**(A)**\nMedical, health, or healthcare questions.\n**(B)**\nBiological, chemical, radiological, or nuclear weapons.\n**(C)**\nNational security.\n**(D)**\nCybersecurity.\n**(E)**\nThreats to critical infrastructure.\n**(F)**\nElections.\n**(G)**\nLaw enforcement.\n**(H)**\nFinancial loan or housing decisions.\n**(I)**\nEducation.\n**(J)**\nEmployment or hiring decisions.\n**(K)**\nPublic services.\n**(L)**\nInformation relating to vulnerable populations, including minors and seniors.\n**(8)**\nInformation on the computational power used to train and operate a foundation model.\n##### (c) Exemptions for specific types of foundation models\nA fully open-source model is exempt from the regulations promulgated by the Commission pursuant to subsection (a).\n##### (d) Consideration of alternative provisions for downstream foundation models\nIn promulgating the regulations and issuing the guidance required by subsection (a), the Commission shall require that a covered entity foundation model that is derived from or built upon another covered entity foundation model, including through the use of an application programming interface\u2014\n**(1)**\nshall publicly provide a URL to the transparency disclosure website of the base foundation model if the base model is in compliance with the regulations promulgated in subsection (a); and\n**(2)**\nshall comply with regulations promulgated in subsection (a) related to any significant change, retraining, or adaptation from such base foundation model.\n##### (e) Alternative provisions for certain covered entities\nThe Commission shall establish a plan to assist small businesses and new businesses that are covered entities with compliance with the regulations promulgated pursuant to subsection (a) and to reduce the burdens imposed by such regulations, including by:\n**(1)**\nPublishing guidance for compliance, including sample guidance and a machine-readable template, to be jointly developed by the Commission and the Director of the National Institute for Standards and Technology, for such covered entities to use that will facilitate compliance with such regulations.\n**(2)**\nProviding one three-month grace period beginning on the date on which a small business or new business becomes a covered entity during which such covered entity is not subject to penalties under this Act or any regulation promulgated pursuant to this Act.\n**(3)**\nProviding a qualified, technically proficient representative to meet on multiple occasions during such grace period with such covered entity to provide guidance to assist the covered entity with compliance with the regulations promulgated pursuant to subsection (a).\n##### (f) Foundation model resources page required\nNot later than 1 year after the date of the enactment of this Act, the Commission shall establish a web page on the website of the Commission that includes recommendations on foundation model transparency for foundation model developers or downstream deployers of a foundation model that are not covered entities, including recommended resources such as the AI Risk Management Framework of the National Institute of Standards and Technology.\n##### (g) Permitted redactions\n**(1) In general**\nIf a covered entity publishes documents or submits information to the Commission to comply with this Act, the covered entity may make redactions to those documents that are necessary\u2014\n**(A)**\nto protect the cybersecurity and security of the covered entity or model, public safety, or the national security of the United States; or\n**(B)**\nto comply with any Federal law.\n**(2) Identification of redactions**\nAny redaction shall be briefly identified and justified in the publication or submission.\n##### (h) Applicability of regulations\nThe regulations required by subsection (a)(1) shall apply beginning on the date that is 90 days after the date on which the Commission promulgates such regulations.\n##### (i) Updates\nNot later than 1 year after the date on which the Commission promulgates the regulations required by subsection (a)(1), and annually thereafter, the Commission, in consultation with the Director of the National Institute of Standards and Technology and the Secretary of Commerce, shall assess the requirements established by the regulations and update the regulations to incorporate any necessary update to such requirements.\n##### (j) Enforcement by Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of a regulation promulgated under subsection (a)(1) shall be treated as a violation of a regulation under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ) regarding unfair or deceptive acts or practices.\n**(2) Powers of Commission**\nExcept as provided in subsection (l)(3)(C)\u2014\n**(A)**\nthe Commission shall enforce the regulations promulgated under subsection (a)(1) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section;\n**(B)**\nany covered entity that violates a regulation promulgated under subsection (a)(1) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act; and\n**(C)**\nthe Commission shall provide covered entities with notice that they are covered entities not less than fourteen days before taking any enforcement action.\n##### (k) Report\nNot later than 1 year after the date of the enactment of this Act, the Commission shall submit to the Committee on Energy and Commerce and the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report on the establishment, implementation, and enforcement of the regulations issued pursuant to subsection (a)(1).\n##### (l) Definitions\nIn this section:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ; Public Law 116\u2013283 ).\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\n**(A) In general**\nThe term covered entity means any person, partnership, or corporation described in subparagraph (C) that provides use of or services from a foundation model which does any of the following:\n**(i)**\nExhibits, or could be easily modified to exhibit, high levels of performance at tasks that could pose a significant risk to security, national economic security, consumer protection, civil rights, national public health or safety, or any combination of those matters.\n**(ii)**\nHas, in aggregate, over 10,000,000 monthly users, including users of second party entities that use such model.\n**(iii)**\nHas in aggregate, over 10,000,000 monthly foundation model download instances if the model is typically downloaded once for use by a user.\n**(iv)**\nWas trained using a quantity of computing power greater than 10 26 integer or floating point operations, including computing used by the entity for the original training run and for any subsequent fine-tuning, reinforcement learning, or other material modifications the entity applies.\n**(B) Updating of thresholds**\nThe Commission, in consultation with the Director of the National Institute of Standards and Technology, the Secretary of Commerce, and the Director of the Office of Science and Technology Policy, may, by regulation promulgated in accordance with section 553 of title 5, United States Code, update the number of monthly output instances for purposes of subparagraph (A)(i), the number of monthly users for purposes of subparagraph (A)(ii), the number of monthly foundation model download instances for purposes of subparagraph (A)(iii), or the quantity of computing power for purposes of subparagraph (A)(iv) as the Commission considers appropriate.\n**(C) Persons, partnerships, and corporations described**\nThe persons, partnerships, and corporations described in this subparagraph are\u2014\n**(i)**\nany person, partnership, or corporation over which the Commission has jurisdiction under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ); and\n**(ii)**\nnotwithstanding section 4, 5(a)(2), or 6 of the Federal Trade Commission Act ( 15 U.S.C. 44 ; 45(a)(2); 46) or any jurisdictional limitation of the Commission\u2014\n**(I)**\nany common carrier subject to the Communications Act of 1934 ( 47 U.S.C. 151 et seq. ) and all Acts amendatory thereof and supplementary thereto; and\n**(II)**\nany organization not organized to carry on business for its own profit or that of its members.\n**(4) Critical infrastructure**\nThe term critical infrastructure has the meaning given that term in subsection (e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c(e) ).\n**(5) Foundation model**\n**(A) In general**\nThe term foundation model means an artificial intelligence model that meets the following requirements:\n**(i)**\nIs trained on broad data.\n**(ii)**\nGenerally uses self-supervision.\n**(iii)**\nGenerally contains at least 1,000,000,000 parameters.\n**(iv)**\nIs designed for generality of output.\n**(v)**\nIs generally applicable across a wide range of contexts, adaptable to a wide range of tasks, or can issue a wide range of outputs in response to inferences.\n**(B) Effect of technical safeguards**\nThe term foundation model includes an artificial intelligence model otherwise described in subparagraph (A) even if such model is provided to users with technical safeguards that attempt to prevent users from taking advantage of any relevant capabilities that may be unsafe for consumer use.\n**(6) Inference**\nThe term inference means, with respect to a foundation model, when such foundation model is operated by a user to produce a result.\n**(7) Minor**\nThe term minor means any individual under the age of 18 years.\n**(8) New business**\nThe term new business means a startup or other new business that has been in operation for less than 1 year.\n**(9) Senior**\nThe term senior means an individual who is 65 years of age or older.\n**(10) Small business**\nThe term small business has the meaning given the term small business concern in section 3(a) of the Small Business Act ( 15 U.S.C. 632(a) ).\n**(11) Training data**\nThe term training data means, with respect to a foundation model, the data on which such foundation model was trained.",
      "versionDate": "2026-03-26",
      "versionType": "Introduced in House"
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
        "updateDate": "2026-04-09T17:22:19Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8094ih.xml"
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
      "title": "AI Foundation Model Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "AI Foundation Model Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Federal Trade Commission to establish requirements for making information available to the public about the training data and algorithms used in artificial intelligence foundation models, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:28Z"
    }
  ]
}
```
