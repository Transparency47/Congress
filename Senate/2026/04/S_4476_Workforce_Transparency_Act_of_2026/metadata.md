# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4476?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4476
- Title: Workforce Transparency Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4476
- Origin chamber: Senate
- Introduced date: 2026-04-30
- Update date: 2026-05-20T16:02:34Z
- Update date including text: 2026-05-20T16:02:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in Senate
- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-04-30: Introduced in Senate

## Actions

- 2026-04-30 - IntroReferral: Introduced in Senate
- 2026-04-30 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4476",
    "number": "4476",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Workforce Transparency Act of 2026",
    "type": "S",
    "updateDate": "2026-05-20T16:02:34Z",
    "updateDateIncludingText": "2026-05-20T16:02:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
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
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T19:19:17Z",
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
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4476is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4476\nIN THE SENATE OF THE UNITED STATES\nApril 30, 2026 Mr. Warner (for himself and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo provide for voluntary disclosure by developers and users of artificial intelligence regarding workforce data and for reporting by the Secretary of Labor regarding the workforce data, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Workforce Transparency Act of 2026 .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nArtificial intelligence systems are already, as of the date of enactment of this Act, widely used by workers, employers, and consumers across sectors of the United States economy.\n**(2)**\nThe most immediate labor-market effects of artificial intelligence are currently occurring at the task, skill, and workflow level, rather than through the wholesale elimination of occupations.\n**(3)**\nResearch shows that artificial intelligence is also improving workforce productivity by accelerating routine cognitive tasks, enabling workers to focus on higher-value functions, and contributing positively to aggregate economic growth, even as adoption and impacts vary by sector and over time. Artificial intelligence also has the potential to create new roles, consistent with previous patterns in which technological change has led to significant changes in the types of jobs people do over time.\n**(4)**\nPolicymakers, workers, educators, and employers lack timely and standardized information about how artificial intelligence systems are being used and how such use affects productivity, skills, and workforce outcomes.\n**(5)**\nAggregated, privacy-preserving transparency, including information voluntarily shared by a covered AI system provider and complementary data published by the Federal Government, can meaningfully improve workforce development, education policy, and economic planning without revealing proprietary information, trade secrets, individual-level data, or other information that would undermine individual privacy.\n**(6)**\nA Federal transparency framework that encourages participation and supports modernization of government data systems can establish a consistent national baseline, reduce fragmentation across States, and provide a level playing field among covered AI system providers.\n##### (b) Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nestablish a Federal framework for aggregated, de-identified transparency or data-sharing regarding use of artificial intelligence systems relevant to workforce impacts;\n**(2)**\nsupport evidence-based workforce, education, and economic policymaking through both voluntary participation by a covered AI system provider and improved Federal labor-market data;\n**(3)**\nprotect individual privacy, confidential business information, and competition; and\n**(4)**\npromote public trust through consistent, responsible, and privacy-preserving data-sharing.\n#### 3. Definitions\nIn this Act:\n**(1) Aggregated workforce transparency data**\nThe term aggregated workforce transparency data means statistical information that\u2014\n**(A)**\nis aggregated across users, accounts, interactions, or customers;\n**(B)**\ndoes not identify or reasonably permit the identification of a particular person, household, or employer; and\n**(C)**\ndoes not disclose\u2014\n**(i)**\nproprietary model weights, training data, source code, or system architecture; or\n**(ii)**\ninformation that a covered AI system provider has contractually defined as confidential or not subject to disclosure.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Covered AI system**\nThe term covered AI system means an artificial intelligence system made available to consumers or businesses other than such a system that is\u2014\n**(A)**\ndesigned and marketed by a person primarily for internal business use by the person;\n**(B)**\nused solely for academic or non-commercial research; or\n**(C)**\ndesigned for a narrow, discrete technical function without general-purpose capabilities.\n**(4) Covered AI system provider**\nThe term covered AI system provider means a person that develops, deploys, or makes available a covered AI system.\n**(5) Enterprise customer**\nThe term enterprise customer means a business, governmental, or institutional customer that accesses a covered AI system pursuant to a negotiated contract governing data use, confidentiality, or disclosure.\n**(6) Participating entity**\nThe term participating entity means a covered AI system provider or enterprise customer that elects to submit data in accordance with section 4(a).\n**(7) Secretary**\nThe term Secretary means the Secretary of Labor.\n#### 4. Workforce transparency reporting\n##### (a) In general\nA participating entity may submit to the Secretary, in accordance with this Act and any regulations promulgated by the Secretary under this Act, aggregated workforce transparency data, including (as reasonably feasible) such data regarding the following:\n**(1) Task or activity level use**\nAggregated distribution of interactions across broad task or activity categories, such as writing, coding, research, analysis, translation, or job-related assistance (as established and periodically updated by the Secretary through notice and comment rulemaking under section 553 of title 5, United States Code).\n**(2) Geographic distribution**\nAggregated distribution of interactions across broad task or activity categories, by State or by metropolitan statistical area or comparable geographic unit.\n**(3) Age ranges**\nAggregated distribution of interactions across broad task or activity categories, by adult age ranges, as reasonably feasible and consistent with privacy safeguards or laws.\n**(4) Temporal trends**\nChanges in usage patterns over time based on task or activity category.\n##### (b) Reporting windows\nThe Secretary shall establish a system for submissions under subsection (a) that allows for such submissions by a participating entity only for aggregated workforce transparency data concerning information that is not more recent than 91 days before the date of the submission, including, for purposes of the first submission by the participating entity, such data with respect to the 2-year period preceding the date on which the participating entity first elects to make such a submission.\n##### (c) Rule of construction\nThis Act shall not be construed to require a covered AI system provider or enterprise customer to elect to submit or otherwise be required to submit aggregated workforce transparency data under this section.\n#### 5. Privacy, security, and confidentiality safeguards\n##### (a) Prohibited disclosures\nA participating entity may not submit under section 4(a)\u2014\n**(1)**\npersonal data or information linked or reasonably linkable to an individual;\n**(2)**\nemployer-specific, customer-specific, or individual-specific performance data;\n**(3)**\ntrade secrets, proprietary algorithms, model weights, training datasets, or source code;\n**(4)**\ninformation that a participating entity is contractually prohibited from disclosing pursuant to agreements or terms with consumers, users, or enterprise, governmental, or institutional customers or that the participating entity otherwise commits to protecting from disclosure in policies or representations, including restrictions or commitments on data use, aggregation, or secondary disclosure; or\n**(5)**\ndata in violation of a contract or other terms with an enterprise customer, consumer, or user, including contractual restrictions on data use, aggregation, disclosure, or secondary analysis.\n##### (b) Compliance with applicable laws\nIn making submissions under section 4(a), a participating entity shall exclude or further aggregate data as necessary to comply with other applicable laws.\n##### (c) Compliance with contract terms\nThis Act shall not be construed to obviate the terms, including privacy or data protections, in any contract between a participating entity and its customers, users, or other consumers.\n##### (d) Safeguards\nIn preparing data for purposes of making submissions under section 4(a) and making such submissions, a participating entity shall apply aggregation, anonymization, and de-identification techniques consistent with guidance issued under section 6(c).\n##### (e) Freedom of information act\nAny aggregated workforce transparency data submitted under section 4(a) shall be exempt from the disclosure requirements under section 552 of title 5, United States Code (commonly known as the Freedom of Information Act ).\n#### 6. Reporting and regulations\n##### (a) Lead agency\nThe Secretary of Labor, acting through the Commissioner of Labor Statistics and in coordination with the Secretary of Commerce acting through the Director of the Bureau of the Census, shall administer this Act.\n##### (b) Data reporting\n**(1) Public database**\nThe Secretary shall establish and maintain a publicly available, online database containing aggregated workforce transparency data derived from submissions under section 4(a).\n**(2) Annual report to Congress**\nThe Secretary shall annually submit a report to Congress summarizing aggregated workforce transparency data derived from submissions under such section.\n**(3) Requirements for data**\nIn carrying out this subsection, the Secretary shall aggregate data from submissions by participating entities under section 4(a) and ensure that any published dataset, analysis, or report does not attribute any submitted data to any specific participating entity or any identifiable person.\n##### (c) Guidance\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue non-binding guidance regarding\u2014\n**(1)**\nstandardized reporting formats and taxonomies for purposes of submissions under section 4(a);\n**(2)**\nacceptable aggregation, anonymization, and privacy-preserving methods for purposes of submissions under such section;\n**(3)**\nprocedures to minimize reporting burden for purposes of such submissions, including alignment with existing Federal data-collection efforts; and\n**(4)**\ndefinitions and classifications for broad task or activity categories used in workforce-related artificial intelligence usage reporting.\n##### (d) Rulemaking\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall issue regulations necessary to carry out this Act.\n**(2) Requirements**\nThe regulations issued under paragraph (1) shall clarify the extent to which a participating entity shall aggregate, anonymize, or otherwise ensure privacy safeguards for aggregated workforce transparency data submitted under section 4(a).\n##### (e) Working group\nThe Secretary, acting through the Commissioner of Labor Statistics and in coordination with other relevant agencies, shall establish a working group to develop a process to publish or enhance public labor-market data that combines age and occupational information, in order to improve understanding of how artificial intelligence affects entry-level workers and early-career professionals.\n#### 7. Prohibition regarding adverse inferences\nA Federal agency may not draw an adverse inference against any covered AI system provider or enterprise customer that elects not to make submissions under section 4(a).\n#### 8. Enforcement\nThe Secretary may seek injunctive relief in any court of competent jurisdiction against a participating entity with respect to aggregated workforce transparency data submitted under section 4(a) that the Secretary determines is a knowing and willful misrepresentation by the entity of the data.\n#### 9. Severability\nIf any provision of this Act or the application of such provision to any person or circumstance is held to be unconstitutional, the remainder of this Act and the application of the provision to any other person or circumstance, shall not be affected.",
      "versionDate": "2026-04-30",
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
        "name": "Labor and Employment",
        "updateDate": "2026-05-20T16:02:33Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4476is.xml"
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
      "title": "Workforce Transparency Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-08T04:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Workforce Transparency Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-08T04:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for voluntary disclosure by developers and users of artificial intelligence regarding workforce data and for reporting by the Secretary of Labor regarding the workforce data, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-08T04:18:33Z"
    }
  ]
}
```
