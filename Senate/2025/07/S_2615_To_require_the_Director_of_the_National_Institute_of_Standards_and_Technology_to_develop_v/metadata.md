# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2615
- Title: VET Artificial Intelligence Act
- Congress: 119
- Bill type: S
- Bill number: 2615
- Origin chamber: Senate
- Introduced date: 2025-07-31
- Update date: 2026-02-27T12:03:21Z
- Update date including text: 2026-02-27T12:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-31: Introduced in Senate
- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-07-31: Introduced in Senate

## Actions

- 2025-07-31 - IntroReferral: Introduced in Senate
- 2025-07-31 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-31",
    "latestAction": {
      "actionDate": "2025-07-31",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2615",
    "number": "2615",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H000273",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Hickenlooper, John W. [D-CO]",
        "lastName": "Hickenlooper",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "VET Artificial Intelligence Act",
    "type": "S",
    "updateDate": "2026-02-27T12:03:21Z",
    "updateDateIncludingText": "2026-02-27T12:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-31",
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
      "actionDate": "2025-07-31",
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
            "date": "2025-07-31T19:15:33Z",
            "name": "Referred To"
          },
          {
            "date": "2025-07-31T19:15:33Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-07-31",
      "state": "WV"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2026-02-26",
      "state": "MI"
    },
    {
      "bioguideId": "Y000064",
      "firstName": "Todd",
      "fullName": "Sen. Young, Todd [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Young",
      "party": "R",
      "sponsorshipDate": "2026-02-26",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2615is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2615\nIN THE SENATE OF THE UNITED STATES\nJuly 31, 2025 Mr. Hickenlooper (for himself and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Director of the National Institute of Standards and Technology to develop voluntary guidelines and specifications for internal and external assurances of artificial intelligence systems, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Validation and Evaluation for Trustworthy (VET) Artificial Intelligence Act or the VET Artificial Intelligence Act .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto develop consensus-driven, evidence-based voluntary technical guidelines and specifications for internal and external assurances through the testing, evaluation, validation, and verification of artificial intelligence systems, as appropriate based on the intended application, use-case, and risk profile of the artificial intelligence system;\n**(2)**\nto use meaningful assurance to supplement methodologies used to build trust in artificial intelligence systems, increase adoption of artificial intelligence systems, and provide for accountability and governance of artificial intelligence systems; and\n**(3)**\nto further the goals of the Artificial Intelligence Risk Management Framework, including any successor framework, published by the National Institute of Standards and Technology and the Artificial Intelligence Safety Institute pursuant to section 22A(c) of the National Institute of Standards and Technology Act ( 15 U.S.C. 278h\u20131(c) ).\n#### 3. Definitions\nIn this Act:\n**(1) Artificial intelligence system**\nThe term artificial intelligence system means a machine-based system that, for explicit or implicit objectives, infers, from the input the system receives, how to generate outputs, such as predictions, content, recommendations, or decisions, that can influence physical or virtual environments.\n**(2) Deployer**\nThe term deployer means an entity that operates an artificial intelligence system for internal use or for use by a third party.\n**(3) Developer**\nThe term developer \u2014\n**(A)**\nmeans an entity that builds, designs, codes, produces, trains, or owns an artificial intelligence system for internal use or for use by a third party; and\n**(B)**\ndoes not include an entity that is solely a deployer of the artificial intelligence system.\n**(4) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n**(5) External artificial intelligence assurance**\nThe term external artificial intelligence assurance means an independent and impartial evaluation of an artificial intelligence system conducted by a nonaffiliated third party in accordance with the voluntary assurance technical guidelines and specifications described in section 4 or consensus-driven voluntary standards, for the purpose of\u2014\n**(A)**\nverifying claims with respect to the functionality and testing of the artificial intelligence system, including verifying whether it is fit for its intended purpose; or\n**(B)**\nidentifying any significant error or inconsistency in the testing, risk management processes, or internal governance, any substantial vulnerability, or any negative societal impact of the artificial intelligence system.\n**(6) Internal artificial intelligence assurance**\nThe term internal artificial intelligence assurance means an independent evaluation of an artificial intelligence system conducted by the party being evaluated with an internal reporting structure that encourages impartial evaluations and prevents conflicts of interest, for the purpose of\u2014\n**(A)**\nverifying claims with respect to the functionality and testing of the artificial intelligence system, including verifying whether it is fit for its intended purpose; or\n**(B)**\nidentifying any significant error or inconsistency in the testing, risk management process, or internal governance or any substantial vulnerability of the artificial intelligence system.\n**(7) Nonaffiliated third party**\nThe term nonaffiliated third party with respect to the evaluation of an artificial intelligence system, means a person who\u2014\n**(A)**\nis not related by common ownership or affiliated by common corporate control with the developer or deployer of the artificial intelligence system;\n**(B)**\ncan demonstrate financial independence from the developer or deployer of the artificial intelligence system;\n**(C)**\ndoes not employ any individual, who is also employed by the developer or deployer of the artificial intelligence system; and\n**(D)**\nis a qualified evaluator of artificial intelligence systems, with\u2014\n**(i)**\ndemonstrated expertise in relevant technical domains, including\u2014\n**(I)**\ndata privacy and security principles; and\n**(II)**\nrisk management practices in artificial intelligence systems; and\n**(ii)**\nfamiliarity with the relevant details regarding the type of artificial intelligence system being evaluated.\n**(8) Secretary**\nThe term Secretary means the Secretary of Commerce.\n#### 4. Voluntary assurance technical guidelines and specifications for artificial intelligence systems\n##### (a) Voluntary technical guidelines and specifications for assurance\nNot later than 1 year after the date of the enactment of this Act, the Director, in collaboration with public and private sector organizations, including the National Science Foundation and the Department of Energy, shall develop and, not less frequently than every 2 years, shall review and update as the Director considers appropriate, a set of voluntary technical guidelines and specifications for internal artificial intelligence assurance and external artificial intelligence assurance.\n##### (b) Contents\nThe technical guidelines and specifications required by subsection (a) shall\u2014\n**(1)**\nidentify consensus-driven, voluntary standards for internal artificial intelligence assurance and external artificial intelligence assurance that address\u2014\n**(A)**\nsafeguards for consumer privacy;\n**(B)**\nmethods to assess and mitigate harms to individuals by artificial intelligence systems;\n**(C)**\ndataset quality;\n**(D)**\ndocumentation, disclosure, and provenance communications to external parties; and\n**(E)**\ngovernance and process controls;\n**(2)**\nprovide technical guidelines, best practices, methodologies, procedures, and processes, as appropriate, for internal artificial intelligence assurance and external artificial intelligence assurance that effectively address the elements listed in paragraph (1);\n**(3)**\nestablish common definitions and characterizations for testing, evaluating, verifying, and validating methods for internal artificial intelligence assurance and external artificial intelligence assurance;\n**(4)**\nrecommend criteria or approaches for a developer or deployer to determine the frequency and circumstances under which internal artificial intelligence assurance and external artificial intelligence assurance activities should be conducted, accounting for the relevant risk and use-case profile of the artificial intelligence system, and any additional circumstance under which an assurance should be conducted;\n**(5)**\nrecommend criteria or approaches for a developer or deployer to determine the scope of internal artificial intelligence assurance and external artificial intelligence assurance conducted through testing and evaluating, accounting for the relevant risk and use-case profile of the artificial intelligence system, including the minimum information or technical resources that should be provided to the party conducting the assurance to enable assurance activities;\n**(6)**\nprovide guidance for the manner in which a developer or deployer may disclose, as appropriate, the results of an internal or external assurance or carry out corrective actions with respect to an artificial intelligence system following the completion of an internal or external assurance of such system, and guidance on the manner in which a developer or deployer may properly document any corrective action taken;\n**(7)**\nalign with the voluntary consensus standards, including international standards, identified pursuant to paragraph (1) to the fullest extent possible;\n**(8)**\nincorporate the relevant voluntary consensus standards identified pursuant to paragraph (1) and industry best practices to the fullest extent possible;\n**(9)**\nnot prescribe or otherwise require\u2014\n**(A)**\nthe use of any specific solution; or\n**(B)**\nthe use of any specific information or any communications technology product or service; and\n**(10)**\nrecommend methods to protect the confidentiality of sensitive information, including personal data and proprietary knowledge of an artificial intelligence system, that may be obtained during the assurance process.\n##### (c) Stakeholder outreach\nIn developing the voluntary technical guidelines and specifications required by subsection (a), the Director shall\u2014\n**(1)**\nsolicit public comment on at least 1 draft of the technical guidelines and specifications, and provide a reasonable period of not less than 30 days for the submission of comments by interested stakeholders;\n**(2)**\nmake each complete draft of the voluntary technical guidelines and specifications developed under subsection (a) available to the public on the website of the National Institute of Standards and Technology; and\n**(3)**\nconvene workshops, roundtables, and other public forums, as the Director considers appropriate, to consult with relevant stakeholders in industry, academia, civil society, consumer advocacy, workforce development organizations, labor organizations, conformance assessment bodies, and any other sector the Director considers appropriate, on the development of the voluntary technical guidelines and specifications.\n##### (d) Publication\nThe Director shall publish the voluntary technical guidelines and specifications required by subsection (a) as a standalone framework or document available to the public on the website of the National Institute of Standards and Technology.\n#### 5. Qualifications advisory committee\n##### (a) Advisory committee\nNot later than 90 days after the date on which the Director publishes the voluntary technical guidelines and specifications required under section 4(a), the Secretary shall establish the Artificial Intelligence Assurance Qualifications Advisory Committee (referred to in this section as the Advisory Committee ).\n##### (b) Membership\nThe Secretary shall appoint to the Advisory Committee not more than 20 individuals with expertise relating to artificial intelligence systems, including at least 1 representative from each of the following:\n**(1)**\nInstitutions of higher education.\n**(2)**\nOrganizations developing artificial intelligence systems.\n**(3)**\nOrganizations deploying artificial intelligence systems.\n**(4)**\nOrganizations assessing artificial intelligence systems.\n**(5)**\nConsumers or consumer advocacy groups.\n**(6)**\nPublic health organizations.\n**(7)**\nPublic safety organizations.\n**(8)**\nCivil rights organizations.\n**(9)**\nProfessional accreditation organizations.\n**(10)**\nWorkforce development organizations.\n**(11)**\nLabor organizations.\n**(12)**\nNonprofit assurance professional organizations.\n##### (c) Duties\nThe Advisory Committee shall\u2014\n**(1)**\nreview and assess case studies from entities that provide licensure, certification, or accreditation to independent organizations with a primary mission of verifying compliance with applicable statutes, regulations, standards, or guidelines; and\n**(2)**\ndetermine the applicability of the case studies reviewed and assessed under paragraph (1) to the development, maintenance, and use of artificial intelligence systems for the purpose of developing recommendations under subsection (d).\n##### (d) Recommendations\nNot later than 1 year after the date on which the Secretary establishes the Advisory Committee under this section, the Advisory Committee shall submit to the Secretary and Congress and make publicly available a report that includes recommendations for the Secretary to consider regarding\u2014\n**(1)**\nthe qualifications, expertise, professional licensing, independence, and accountability that a party conducting an assurance of an artificial intelligence system should have, including with respect to the type of artificial intelligence system under evaluation and the internal and external assurance processes; and\n**(2)**\nwhether accreditation for internal artificial intelligence assurance and external artificial intelligence assurance can be met through a combination of existing licensure, certification, or accreditation programs.\n##### (e) Termination\nThe Advisory Committee shall terminate not later than 1 year after the date on which the Advisory Committee submits the recommendations required under subsection (d).\n#### 6. Study and report on entities that conduct assurances of artificial intelligence systems\n##### (a) Study\nNot later than 90 days after the date on which the Director publishes the voluntary technical guidelines and specifications required under section 4(a), the Secretary shall commence a study to evaluate the capabilities of the sector of entities that conduct internal artificial intelligence assurances and external artificial intelligence assurances.\n##### (b) Considerations\nIn carrying out the study required by subsection (a), the Secretary shall\u2014\n**(1)**\nassess the capabilities of the sector of entities described in subsection (a) with respect to personnel, technical tools, evaluation methods, computing infrastructure, and physical infrastructure and whether such capabilities are adequate for providing internal artificial intelligence assurances or external artificial intelligence assurances that comport with the voluntary technical guidelines and specifications required under section 4(a);\n**(2)**\nreview the features, best practices, and safeguards employed by such entities to maintain the integrity of confidential or proprietary information of a developer or deployer during an internal artificial intelligence assurance or an external artificial intelligence assurance;\n**(3)**\nassess the market demand for internal artificial intelligence assurances and external artificial intelligence assurances and the availability of such assurers; and\n**(4)**\nassess the feasibility of leveraging an existing facility accredited by the Director under the National Voluntary Laboratory Accreditation Program established under part 285 of title 15, Code of Federal Regulations, to conduct external assurances of artificial intelligence systems.\n##### (c) Report\nNot later than 1 year after the date on which the Secretary commences the study required by subsection (a), the Secretary shall submit to the appropriate committees of Congress and the head of any Federal agency that the Secretary considers relevant, a report that contains the results of the study required by subsection (a), including\u2014\n**(1)**\nrecommendations for improving the capabilities and the availability of the entities assessed in the study;\n**(2)**\ndescriptions of the features, best practices, and safeguards of the entities studied and the effectiveness of such features, practices, or safeguards at implementing the voluntary technical guidelines and specifications required under section 4(a) and at maintaining the integrity of confidential and proprietary information, as described under subsection (b)(2); and\n**(3)**\nany conclusions drawn from the assessment of the facilities described in subsection (b)(4).\n##### (d) Appropriate committees of Congress defined\nIn this section, the term the appropriate committees of Congress means\u2014\n**(1)**\nthe Committee of Commerce, Science, and Transportation of the Senate; and\n**(2)**\nthe Committee on Science, Space, and Technology of the House of Representatives.",
      "versionDate": "2025-07-31",
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
        "updateDate": "2025-09-18T19:43:37Z"
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
      "date": "2025-07-31",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2615is.xml"
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
      "title": "VET Artificial Intelligence Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-27T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "VET Artificial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Validation and Evaluation for Trustworthy (VET) Artificial Intelligence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Director of the National Institute of Standards and Technology to develop voluntary guidelines and specifications for internal and external assurances of artificial intelligence systems, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:18:24Z"
    }
  ]
}
```
