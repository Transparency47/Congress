# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3919?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3919
- Title: Advanced AI Security Readiness Act
- Congress: 119
- Bill type: HR
- Bill number: 3919
- Origin chamber: House
- Introduced date: 2025-06-11
- Update date: 2026-04-17T16:28:01Z
- Update date including text: 2026-04-17T16:28:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-06-11: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Intelligence (Permanent Select).
- Latest action: 2025-06-11: Introduced in House

## Actions

- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Introduced in House
- 2025-06-11 - IntroReferral: Referred to the House Committee on Intelligence (Permanent Select).

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-11",
    "latestAction": {
      "actionDate": "2025-06-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3919",
    "number": "3919",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "L000585",
        "district": "16",
        "firstName": "Darin",
        "fullName": "Rep. LaHood, Darin [R-IL-16]",
        "lastName": "LaHood",
        "party": "R",
        "state": "IL"
      }
    ],
    "title": "Advanced AI Security Readiness Act",
    "type": "HR",
    "updateDate": "2026-04-17T16:28:01Z",
    "updateDateIncludingText": "2026-04-17T16:28:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Intelligence (Permanent Select) Committee",
          "systemCode": "hlig00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Intelligence (Permanent Select).",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-11",
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
          "date": "2025-06-11T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Intelligence (Permanent Select) Committee",
      "systemCode": "hlig00",
      "type": "Select"
    }
  ]
}
```

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-06-11",
      "state": "MI"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "NJ"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-06-11",
      "state": "IL"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "VA"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3919ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3919\nIN THE HOUSE OF REPRESENTATIVES\nJune 11, 2025 Mr. LaHood (for himself, Mr. Moolenaar , Mr. Gottheimer , and Mr. Krishnamoorthi ) introduced the following bill; which was referred to the Permanent Select Committee on Intelligence\nA BILL\nTo direct the Director of the National Security Agency to develop strategies to secure artificial intelligence related technologies.\n#### 1. Short title\nThis Act may be cited as the Advanced AI Security Readiness Act .\n#### 2. AI security playbook\n##### (a) Requirement\nThe Director of the National Security Agency, acting through the Artificial Intelligence Security Center (or successor office), shall develop strategies (in this section referred to as the AI Security Playbook ) to defend covered AI technologies from technology theft by threat actors.\n##### (b) Elements\nThe AI Security Playbook under subsection (a) shall include the following:\n**(1)**\nIdentification of potential vulnerabilities in advanced AI data centers and among advanced AI developers capable of producing covered AI technologies, with a focus on cybersecurity risks and other security challenges that are unique to protecting covered AI technologies and critical components of such technologies (such as threat vectors that do not typically arise, or are less severe, in the context of conventional information technology systems).\n**(2)**\nIdentification of components or information that, if accessed by threat actors, would meaningfully contribute to progress made by the actor with respect to developing covered AI technologies, including with respect to\u2014\n**(A)**\nAI models and key components of such models;\n**(B)**\ncore insights relating to the development of advanced AI systems, including with respect to training such systems, the inferences made by such systems, and the engineering of such systems; and\n**(C)**\nother related information.\n**(3)**\nStrategies to detect, prevent, and respond to cyber threats by threat actors targeting covered AI technologies.\n**(4)**\nIdentification of the levels of security, if any, that would require substantial involvement by the United States Government in the development or oversight of highly advanced AI systems.\n**(5)**\nAnalysis of how the United States Government would be involved to achieve the levels of security identified in paragraph (4), including a description of a hypothetical initiative to build covered AI technology systems in a highly secure governmental environment, considering, at a minimum, cybersecurity protocols, provisions to protect model weights, efforts to mitigate insider threats (including personnel vetting and security clearance adjudication processes), access control procedures, counterintelligence and anti-espionage measures, contingency and emergency response plans, and other strategies that would be used to reduce threats of technology theft by threat actors.\n##### (c) Form\nThe AI Security Playbook under subsection (a) shall include\u2014\n**(1)**\ndetailed methodologies and intelligence assessments, which may be contained in a classified annex; and\n**(2)**\nan unclassified portion with general guidelines and best practices suitable for dissemination to relevant individuals, including in the private sector.\n##### (d) Engagement\n**(1) In general**\nIn developing the AI Security Playbook under subsection (a), the Director shall\u2014\n**(A)**\nengage with prominent AI developers and researchers, as determined by the Director, to assess and anticipate the capabilities of highly advanced AI systems relevant to national security, including by\u2014\n**(i)**\nconducting a comprehensive review of industry documents pertaining to the security of AI systems with respect to preparedness frameworks, scaling policies, risk management frameworks, and other matters;\n**(ii)**\nconducting interviews with subject matter experts;\n**(iii)**\nhosting roundtable discussions and expert panels; and\n**(iv)**\nvisiting facilities used to develop AI; and\n**(B)**\nto leverage existing expertise and research, collaborate with a federally funded research and development center that has conducted research on strategies to secure AI models from nation-state actors and other highly resourced actors.\n**(2) Nonapplicability of FACA**\nNone of the activities described in this subsection shall be construed to establish or use an advisory committee subject to chapter 10 of title 5, United States Code.\n##### (e) Reports\n**(1) Initial report**\nNot later than 90 days after the date of the enactment of this Act, the Director shall submit to the appropriate congressional committees a report on the AI Security Playbook under subsection (a), including a summary of progress on the development of Playbook, an outline of remaining sections, and any relevant insights about AI security.\n**(2) Final report**\nNot later than 270 days after the date of enactment of this Act, the Director shall submit to the appropriate congressional committees a report on the Playbook.\n**(3) Form**\nThe report submitted under paragraph (2)\u2014\n**(A)**\nshall include\u2014\n**(i)**\nan unclassified version suitable for dissemination to relevant individuals, including in the private sector; and\n**(ii)**\na publicly available version; and\n**(B)**\nmay include a classified annex.\n##### (f) Rule of construction\nNothing in subsection (b)(4) shall be construed to authorize or require any regulatory or enforcement action by the United States Government.\n##### (g) Definitions\nIn this section:\n**(1)**\nThe term appropriate congressional committees means the Permanent Select Committee on Intelligence of the House of Representatives and the Select Committee on Intelligence of the Senate.\n**(2)**\nThe terms artificial intelligence and AI have the meaning given the term artificial intelligence in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. note prec. 4061).\n**(3)**\nThe term covered AI technologies means advanced AI (whether developed by the private sector, the United States Government, or a public-private partnership) with critical capabilities that the Director determines would pose a grave national security threat if acquired or stolen by threat actors, such as AI systems that match or exceed human expert performance in relating to chemical, biological, radiological, and nuclear matters, cyber offense, model autonomy, persuasion, research and development, and self-improvement.\n**(4)**\nThe term technology theft means any unauthorized acquisition, replication, or appropriation of covered AI technologies or components of such technologies, including models, model weights, architectures, or core algorithmic insights, through any means, such as cyber attacks, insider threats, and side-channel attacks, or exploitation of public interfaces.\n**(5)**\nThe term threat actors means nation-state actors and other highly resourced actors capable of technology theft.",
      "versionDate": "2025-06-11",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-11-28",
        "text": "Placed on the Union Calendar, Calendar No. 339."
      },
      "number": "5167",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Intelligence Authorization Act for Fiscal Year 2026",
      "type": "HR"
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-07-29T21:06:20Z"
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
      "date": "2025-06-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3919ih.xml"
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
      "title": "Advanced AI Security Readiness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Advanced AI Security Readiness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-17T04:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Director of the National Security Agency to develop strategies to secure artificial intelligence related technologies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-17T04:18:22Z"
    }
  ]
}
```
