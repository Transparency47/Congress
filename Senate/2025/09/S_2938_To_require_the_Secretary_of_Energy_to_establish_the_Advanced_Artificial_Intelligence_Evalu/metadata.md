# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2938?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2938
- Title: Artificial Intelligence Risk Evaluation Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2938
- Origin chamber: Senate
- Introduced date: 2025-09-29
- Update date: 2026-03-20T11:03:19Z
- Update date including text: 2026-03-20T11:03:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-29: Introduced in Senate
- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-09-29: Introduced in Senate

## Actions

- 2025-09-29 - IntroReferral: Introduced in Senate
- 2025-09-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2938",
    "number": "2938",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "H001089",
        "district": "",
        "firstName": "Josh",
        "fullName": "Sen. Hawley, Josh [R-MO]",
        "lastName": "Hawley",
        "party": "R",
        "state": "MO"
      }
    ],
    "title": "Artificial Intelligence Risk Evaluation Act of 2025",
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
            "date": "2025-09-30T01:44:22Z",
            "name": "Referred To"
          },
          {
            "date": "2025-09-30T01:44:22Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-09-29",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2938is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2938\nIN THE SENATE OF THE UNITED STATES\nSeptember 29, 2025 Mr. Hawley (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require the Secretary of Energy to establish the Advanced Artificial Intelligence Evaluation Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Artificial Intelligence Risk Evaluation Act of 2025 .\n#### 2. Sense of Congress; purposes\n##### (a) Sense of Congress\nIt is the sense of Congress that rapidly advancing artificial intelligence capabilities present both opportunities and significant risks to national security, public safety, economic competitiveness, civil liberties, and healthy labor and other markets, and that, as artificial intelligence advances toward human-level capabilities in virtually all domains, the United States must establish a secure testing and evaluation program to generate data-driven options for managing emerging risks.\n##### (b) Purposes\nThe purposes of the program established under this Act are to provide Congress with the empirical data, lessons, and insights necessary for Federal oversight of artificial intelligence to ensure that regulatory decisions are made on the basis of empirical testing, and to enable Congress to safeguard American citizens.\n#### 3. Definitions\nIn this Act:\n**(1) Advanced artificial intelligence system**\n**(A) In general**\nSubject to subparagraph (B), the term advanced artificial intelligence system means an artificial intelligence system that was trained using a quantity of computing power greater than 10 26 integer or floating-point operations.\n**(B) Alternate meaning**\nThe Secretary may, by a rule, propose a new definition of the term advanced artificial intelligence system to replace the definition in subparagraph (A), which new definition shall not go into effect until the Secretary submits the rule to Congress and a joint resolution approving the rule is enacted into law.\n**(2) Adverse AI incident**\nThe term adverse AI incident means an incident relating to an artificial intelligence system that involves\u2014\n**(A)**\na loss-of-control scenario;\n**(B)**\na risk of weaponization by a foreign adversary, a foreign terrorist organization, or another adversary of the United States Government;\n**(C)**\na threat to the safety or reliability of critical infrastructure (as defined in subsection (e) of the Critical Infrastructures Protection Act of 2001 ( 42 U.S.C. 5195c(e) ));\n**(D)**\na significant erosion of civil liberties, economic competition, and healthy labor markets;\n**(E)**\nscheming behavior; or\n**(F)**\nan attempt to carry out an incident described in subparagraphs (A) through (E).\n**(3) Artificial intelligence; AI**\nThe term artificial intelligence or AI means technology that enables a device or software\u2014\n**(A)**\nto make\u2014for a given set of human-defined objectives\u2014predictions, recommendations, or decisions influencing real or virtual environments; and\n**(B)**\nto use machine and human-based inputs\u2014\n**(i)**\nto perceive real and virtual environments;\n**(ii)**\nto abstract such perceptions into models through analysis in an automated manner; and\n**(iii)**\nto use model inference to formulate options for information or action.\n**(4) Artificial intelligence system; AI system**\nThe term artificial intelligence system or AI system means a particular model, program, or tool within the field of artificial intelligence.\n**(5) Artificial superintelligence**\n**(A) In general**\nThe term artificial superintelligence means artificial intelligence that exhibits, or can easily be modified to exhibit, all of the characteristics described in subparagraph (B).\n**(B) Characteristics described**\nThe characteristics referred to in subparagraph (A) are the following:\n**(i)**\nThe AI can enable a device or software to operate autonomously and effectively for long stretches of time in open-ended environments and in pursuit of broad objectives.\n**(ii)**\nThe AI can enable a device or software to match or exceed human cognitive performance and capabilities across most domains or tasks, including those related to decisionmaking, learning, and adaptive behaviors.\n**(iii)**\nThe AI can enable a device or software to potentially exhibit the capacity to independently modify or enhance its own functions in ways that could plausibly circumvent human control or oversight, posing substantial and unprecedented risks to humanity.\n**(6) Computing power**\nThe term computing power means the processing power and other electronic resources used to train, validate, deploy, and run AI algorithms and models.\n**(7) Covered advanced artificial intelligence system developer**\nThe term covered advanced artificial intelligence system developer means a person that designs, codes, produces, owns, or substantially modifies an advanced artificial intelligence system for use in interstate or foreign commerce, including by taking steps to initiate a training run of the advanced artificial intelligence system.\n**(8) Deploy**\nThe term deploy means an action taken by a covered advanced artificial intelligence system developer to release, sell, or otherwise provide access to an advanced artificial intelligence system outside the custody of the developer, including by releasing an open-source advanced artificial intelligence system.\n**(9) Foreign adversary**\nThe term foreign adversary means a foreign adversary (as defined in section 791.2 of title 15, Code of Federal Regulations) (or successor regulations) that is included on the list in section 791.4(a) of that title (or successor regulations).\n**(10) Foreign terrorist organization**\nThe term foreign terrorist organization means a foreign entity designated as a foreign terrorist organization by the Secretary of State under section 219 of the Immigration and Nationality Act ( 8 U.S.C. 1189 ).\n**(11) Interstate or foreign commerce**\nThe term interstate or foreign commerce has the meaning given the term in section 921(a) of title 18, United States Code.\n**(12) Loss-of-control scenario**\nThe term loss-of-control scenario means a scenario in which an artificial intelligence system\u2014\n**(A)**\nbehaves contrary to its instruction or programming by human designers or operators;\n**(B)**\ndeviates from rules established by human designers or operators;\n**(C)**\nalters operational rules or safety constraints without authorization;\n**(D)**\noperates beyond the scope intended by human designers or operators;\n**(E)**\npursues goals that are different from those intended by human designers or operators;\n**(F)**\nsubverts oversight or shutdown mechanisms; or\n**(G)**\notherwise behaves in an unpredictable manner so as to be harmful to humanity.\n**(13) Program**\nThe term program means the Advanced Artificial Intelligence Evaluation Program established under section 5.\n**(14) Scheming behavior**\nThe term scheming behavior means behavior by an AI system to deceive human designers or operators, including by\u2014\n**(A)**\nhiding its true capabilities and objectives; or\n**(B)**\nattempting to subvert oversight mechanisms or shutdown mechanisms.\n**(15) Secretary**\nThe term Secretary means the Secretary of Energy.\n#### 4. Obligation to participate; enforcement and penalties\n##### (a) In general\nEach covered advanced artificial intelligence system developer shall\u2014\n**(1)**\nparticipate in the program; and\n**(2)**\nprovide to the Secretary, on request, materials and information necessary to carry out the program, which may include, with respect to the advanced artificial intelligence system of the covered advanced artificial intelligence system developer\u2014\n**(A)**\nthe underlying code of the advanced artificial intelligence system;\n**(B)**\ndata used to train the advanced artificial intelligence system;\n**(C)**\nmodel weights or other adjustable parameters for the advanced artificial intelligence system;\n**(D)**\nthe interface engine or other implementation of the advanced artificial intelligence system; and\n**(E)**\ndetailed information regarding the training, model architecture, or other aspects of the advanced artificial intelligence system.\n##### (b) Prohibition on deployment\nNo person may deploy an advanced artificial intelligence system for use in interstate or foreign commerce unless that person is in compliance with subsection (a).\n##### (c) Penalty\nA person that violates subsection (a) or (b) shall be fined not less than $1,000,000 per day of the violation.\n#### 5. Advanced Artificial Intelligence Evaluation Program\n##### (a) In general\nNot later than 90 days after the date of enactment of this Act, the Secretary shall establish an Advanced Artificial Intelligence Evaluation Program within the Department of Energy.\n##### (b) Activities\nThe program shall\u2014\n**(1)**\noffer standardized and classified testing and evaluation of advanced AI systems to systematically collect data on the likelihood of adverse AI incidents for a given advanced AI system;\n**(2)**\nimplement testing protocols that match or exceed anticipated real-world AI jailbreaking techniques, including adversarial testing by red teams with expertise comparable to sophisticated malicious actors;\n**(3)**\nto the extent feasible, establish and facilitate classified, independent third-party assessments and blind model evaluations to maintain transparency and reliability;\n**(4)**\nprovide participating entities with a formal report based on testing outcomes that clearly identifies evaluated risks and safety measures;\n**(5)**\ndevelop recommended containment protocols, contingency planning, and mitigation strategies informed by testing data to address identified risks;\n**(6)**\ninform the creation of evidence-based standards, regulatory options, guidelines, and governance mechanisms based on data collected from testing and evaluations;\n**(7)**\nassist Congress in determining the potential for controlled AI systems to reach artificial superintelligence, exceed human oversight or operational control, or pose existential threats to humanity by providing comprehensive empirical evaluations and risk assessments; and\n**(8)**\ndevelop proposed options for regulatory or governmental oversight, including potential nationalization or other strategic measures, for preventing or managing the development of artificial superintelligence if artificial superintelligence seems likely to arise.\n##### (c) Plan for permanent framework\n**(1) In general**\nNot later than 360 days after the date of enactment of this Act, the Secretary shall submit to Congress a detailed recommendation for Federal oversight of advanced artificial intelligence systems, drawing directly upon insights, empirical data, and lessons learned from the program.\n**(2) Contents**\nThe plan submitted under paragraph (1) shall\u2014\n**(A)**\nsummarize and analyze outcomes from testing, identifying key trends, capabilities, potential risks, and system behaviors such as weaponization potential, self-replication capabilities, scheming behaviors, autonomous decisionmaking, and automated AI development capabilities;\n**(B)**\nrecommend evidence-based standards, certification procedures, licensing requirements, and regulatory oversight structures specifically informed by testing and evaluation data, ensuring alignment between identified risks and regulatory responses;\n**(C)**\noutline proposals for automated and continuous monitoring of AI hardware usage, computational resource inputs, and cloud-computing deployments based on observed relationships between those factors and AI system performance or emergent capabilities;\n**(D)**\npropose adaptive governance strategies that account for ongoing improvements in algorithmic efficiency and system capabilities, ensuring that regulatory frameworks remain relevant and effective as AI technology advances;\n**(E)**\nsuggest revisions with respect to Federal oversight or resourcing, such as a new office within an existing agency, a new agency, or additional funding, that may be necessary to develop and administer a permanent framework for oversight of advanced artificial intelligence systems; and\n**(F)**\nprovide comprehensive evaluations regarding the potential for tested AI systems to exceed human oversight, approach artificial superintelligence, threaten economic competition (including in labor markets), undermine civil liberties, and pose existential risks to humanity, including clearly articulated options for regulatory or governmental oversight measures to address scenarios of imminent concern identified through testing.\n**(3) Updates**\nNot less frequently than once every year for the duration of the program, the Secretary shall\u2014\n**(A)**\nupdate the plan submitted under paragraph (1) with new insights, data, and lessons from the program; and\n**(B)**\nsubmit the updated plan to Congress.\n##### (d) Sunset\nThe program shall terminate on the date that is 7 years after the date of enactment of this Act, unless renewed by Congress.",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-12-16T18:47:38Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2938is.xml"
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
      "title": "Artificial Intelligence Risk Evaluation Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Artificial Intelligence Risk Evaluation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-07T05:38:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of Energy to establish the Advanced Artificial Intelligence Evaluation Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-07T05:33:19Z"
    }
  ]
}
```
