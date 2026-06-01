# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2081?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2081
- Title: RISE Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2081
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-07-08T13:21:18Z
- Update date including text: 2025-07-08T13:21:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2081",
    "number": "2081",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "RISE Act of 2025",
    "type": "S",
    "updateDate": "2025-07-08T13:21:18Z",
    "updateDateIncludingText": "2025-07-08T13:21:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
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
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T20:00:17Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2081is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2081\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Ms. Lummis introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish immunity from civil liability for certain artificial intelligence developers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible Innovation and Safe Expertise Act of 2025 or the RISE Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence systems have rapidly advanced in capability and are increasingly being deployed across professional services, including healthcare, law, finance, and other sectors critical to the economy.\n**(2)**\nIndustry leaders have publicly acknowledged the development of increasingly powerful artificial intelligence systems, with some discussing the potential for artificial general intelligence and superintelligence that could fundamentally reshape the society of the United States.\n**(3)**\nThe current lack of clarity regarding liability for artificial intelligence errors creates uncertainty that impedes the responsible integration of these beneficial technologies into professional services and economic activity.\n**(4)**\nMany artificial intelligence systems operate with limited transparency regarding their capabilities, limitations, and default instructions, making it difficult for professional users to assess appropriate use cases and for legal systems to fairly allocate responsibility when errors occur.\n**(5)**\nLearned professionals who utilize artificial intelligence tools in serving clients have professional obligations to understand the capabilities and limitations of the tools they employ, requiring access to clear information about system specifications and performance characteristics.\n**(6)**\nEstablishing clear standards for artificial intelligence transparency, coupled with appropriate liability frameworks, will promote responsible innovation while ensuring that the benefits and risks of artificial intelligence systems are properly understood and managed as these technologies continue to advance.\n**(7)**\nThe development of artificial intelligence systems that may significantly impact the future of human civilization warrants a governance approach that balances innovation incentives with robust transparency requirements and appropriate allocation of responsibility among developers, professional users, and other stakeholders.\n#### 3. Definitions\nIn this Act:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Client**\nThe term client means a person that\u2014\n**(A)**\nengages the services of a learned professional;\n**(B)**\nrelies upon the expertise, judgment, and advice of the learned professional; and\n**(C)**\nhas a relationship with the learned professional that is governed by professional standards, codes of conduct, or regulations.\n**(3) Developer**\nThe term developer means a person that\u2014\n**(A)**\ncreates, designs, programs, trains, modifies, or substantially contributes to the creation or modification of an artificial intelligence product;\n**(B)**\nexercises control over the design specifications, functionality, capabilities, limitations, or intended uses of an artificial intelligence product; or\n**(C)**\nmarkets, distributes, licenses, or makes available an artificial intelligence product under their own name, brand, or trademark, regardless of whether the person creates the original underlying technology of the artificial intelligence product.\n**(4) Error**\nThe term error means\u2014\n**(A)**\nany output, action, recommendation, or material omission by an artificial intelligence product that is false, misleading, fabricated, deceptive, or incomplete in a manner that a reasonable developer could foresee would cause harm; or\n**(B)**\nany failure of an artificial intelligence product to perform a function or task that the artificial intelligence product expressly or implicitly represents itself as capable of performing.\n**(5) Learned professional**\nThe term learned professional means an individual who\u2014\n**(A)**\npossesses specialized education, training, knowledge, or skill in a profession;\n**(B)**\nis licensed, certified, or otherwise authorized by an appropriate Federal or State authority to practice in that profession;\n**(C)**\nis bound by professional standards, ethical obligations, and a duty of care to clients; and\n**(D)**\nexercises independent professional judgment when using tools, including artificial intelligence products, in the course of rendering professional services.\n**(6) Model card**\nThe term model card means a publicly available technical document in which a developer describes, consistent with industry standards and as rigorously as or more rigorously than industry peers, the training data sources, evaluation methodology, performance metrics, intended uses, limitations, and risk mitigations, including detection, evaluation, management, and safeguards against errors, of an artificial intelligence product.\n**(7) Model specification**\nThe term model specification \u2014\n**(A)**\nmeans the text or other configuration instructions of an artificial intelligence product\u2014\n**(i)**\nsupplied by a developer;\n**(ii)**\nthat establish the intended base behavior, tone, constraints, or goals of the artificial intelligence product; and\n**(iii)**\nthat materially influence the outputs of the artificial intelligence product across users or sessions, including the system prompt provided to the model before engaging with user queries; and\n**(B)**\nincludes\u2014\n**(i)**\nthe system prompt and any other text or images that the artificial intelligence product receives that are not visible to the end user;\n**(ii)**\nany constitution or analogous guiding document used when training or fine\u2011tuning of an artificial intelligence product, including in automated schemes in which an artificial intelligence system trains another artificial intelligence system; and\n**(iii)**\nthe instructions, rubrics, or other guidance provided to human raters or evaluators of an artificial intelligence product the feedback of whom is used to train or fine-tune the artificial intelligence product.\n#### 4. Conditional immunity from civil liability for artificial intelligence developers\n##### (a) Safe harbor eligibility\nA developer shall be immune from civil liability for errors generated by an artificial intelligence product when used by a learned professional in the course of providing professional services to a client if the developer\u2014\n**(1)**\nprior to deployment of the artificial intelligence product, publicly releases and continuously maintains\u2014\n**(A)**\nthe model card for the artificial intelligence product; and\n**(B)**\nthe model specification for the artificial intelligence product, which may include redactions\u2014\n**(i)**\nonly relating to information that would reveal trade secrets unrelated to the safety of the artificial intelligence product; and\n**(ii)**\nonly if the developer furnishes contemporaneously with each redaction a written justification for the redaction identifying the basis for withholding the information as a trade secret; and\n**(2)**\nprovides clear and conspicuous documentation to learned professionals describing the known limitations, failure modes, and appropriate domains of use for the artificial intelligence product.\n##### (b) Scope of immunity\nThe immunity provided under subsection (a) shall be conferred to a developer only for acts or omissions that do not constitute recklessness or willful misconduct by the developer.\n##### (c) Duty To update\nImmunity under subsection (a) relating to an artificial intelligence product shall not apply to a developer\u2014\n**(1)**\nthat does not update the model card, model specification, and documentation with respect to the artificial intelligence product as described in subsection (a)(1) by the date that is 30 days after the date on which the developer\u2014\n**(A)**\ndeploys a new version of the artificial intelligence product; or\n**(B)**\ndiscovers a new and material failure mode affecting the artificial intelligence product; and\n**(2)**\nof which the failure to make an update described in paragraph (1) by the applicable date described in that paragraph proximately causes a harm occurring after that date.\n##### (d) Preemption\n**(1) Express preemption**\nThis section shall apply to any claim arising under State law against a developer for an error arising from the use of an artificial intelligence product by a learned professional in providing professional services if the developer is immune from civil liability under subsection (a).\n**(2) Claims not preempted**\nNothing in this section shall apply to a claim arising under State law against a developer based on fraud, knowing misrepresentation, or conduct outside the scope of professional use of an artificial intelligence product by a learned professional.\n#### 5. Preservation of other immunities and privileges\nNothing in this Act shall be construed to affect any immunity from civil liability established by Federal or State law or available at common law that is not related to the immunity established under section 4(a).\n#### 6. Effective date; applicability\nThis Act\u2014\n**(1)**\nshall take effect on December 1, 2025; and\n**(2)**\nshall apply to acts or omissions occurring on or after the date described in paragraph (1).",
      "versionDate": "2025-06-12",
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
        "updateDate": "2025-07-08T13:21:18Z"
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
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2081is.xml"
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
      "title": "RISE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-26T06:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "RISE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responsible Innovation and Safe Expertise Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-26T06:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish immunity from civil liability for certain artificial intelligence developers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-26T06:48:23Z"
    }
  ]
}
```
