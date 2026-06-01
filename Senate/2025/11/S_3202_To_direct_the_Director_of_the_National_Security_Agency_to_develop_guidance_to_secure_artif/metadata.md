# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3202?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3202
- Title: Advanced Artificial Intelligence Security Readiness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3202
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2025-12-18T19:51:33Z
- Update date including text: 2025-12-18T19:51:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Select Committee on Intelligence.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3202",
    "number": "3202",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Advanced Artificial Intelligence Security Readiness Act of 2025",
    "type": "S",
    "updateDate": "2025-12-18T19:51:33Z",
    "updateDateIncludingText": "2025-12-18T19:51:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Intelligence (Select) Committee",
          "systemCode": "slin00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Select Committee on Intelligence.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T17:45:48Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Intelligence (Select) Committee",
      "systemCode": "slin00",
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
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3202is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3202\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Young (for himself and Mr. Kelly ) introduced the following bill; which was read twice and referred to the Select Committee on Intelligence\nA BILL\nTo direct the Director of the National Security Agency to develop guidance to secure artificial intelligence related technologies, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Advanced Artificial Intelligence Security Readiness Act of 2025 .\n#### 2. Artificial intelligence security guidance\n##### (a) Requirement\nThe Director of the National Security Agency, acting through the Artificial Intelligence Security Center (or successor office), shall develop and disseminate security guidance that identifies potential vulnerabilities in covered artificial intelligence technologies and artificial intelligence supply chains, with a focus on cybersecurity risks and security challenges that are unique to protecting artificial intelligence systems, associated computing environments, or the wider artificial intelligence supply chain from theft or sabotage by foreign threat actors.\n##### (b) Elements\nThe guidance developed and disseminated under subsection (a) shall include the following:\n**(1)**\nIdentification of potential vulnerabilities and cybersecurity challenges that are unique to protecting covered artificial intelligence technologies and the artificial intelligence supply chain, such as threat vectors that are less common or severe in conventional information technology systems.\n**(2)**\nIdentification of elements of the artificial intelligence supply chain that, if accessed by threat actors, would meaningfully contribute to the actor\u2019s ability to develop covered artificial intelligence technologies or compromise the confidentiality, integrity, or availability of artificial intelligence systems or associated artificial intelligence supply chains.\n**(3)**\nStrategies to identify, protect, detect, respond to, and recover from cyber threats posed by threat actors targeting covered artificial intelligence technologies, including\u2014\n**(A)**\nprocedures to protect model weights or other competitively sensitive model artifacts;\n**(B)**\nways to mitigate insider threats, including personnel vetting processes;\n**(C)**\nnetwork access control procedures;\n**(D)**\ncounterintelligence and anti-espionage measures; and\n**(E)**\nother measures that can be used to reduce threats of technology theft or sabotage by foreign threat actors.\n##### (c) Form\nThe guidance developed and disseminated under subsection (a) shall include\u2014\n**(1)**\ndetailed best practices, principles, and guidelines in unclassified form, which may include a classified annex; and\n**(2)**\nclassified materials for conducting security briefings for service providers.\n##### (d) Engagement\nIn developing the guidance required by subsection (a), the Director shall\u2014\n**(1)**\nengage with prominent artificial intelligence developers and researchers, as determined by the Director, to assess and anticipate the capabilities of highly advanced artificial intelligence systems relevant to national security, including by\u2014\n**(A)**\nconducting a comprehensive review of publicly available industry documents pertaining to the security of artificial intelligence systems with respect to preparedness frameworks, scaling policies, risk management frameworks, and other matters;\n**(B)**\nconducting interviews with subject matter experts;\n**(C)**\nhosting roundtable discussions and expert panels; and\n**(D)**\nvisiting facilities used to develop artificial intelligence;\n**(2)**\nleverage existing expertise and research, collaborate with relevant National Laboratories, university affiliated research centers, and any federally funded research and development center that has conducted research on strategies to secure artificial intelligence models from nation-state actors and other highly resourced actors; and\n**(3)**\nconsult, as appropriate, with other departments and agencies of the Federal Government as the Director determines relevant, including the Bureau of Industry and Security of the Department of Commerce, the Center for Artificial Intelligence Standards and Innovation of the National Institute of Standards and Technology, the Department of Homeland Security, and the Department of Defense.\n##### (e) Reports\n**(1) Initial report**\nNot later than 180 days after the date of the enactment of this Act, the Director shall submit to the congressional intelligence committees a report on the guidance required by subsection (a), including a summary of progress on the development of the guidance, an outline of remaining sections, and any relevant insights about artificial intelligence security.\n**(2) Final report**\nNot later than 365 days after the date of enactment of this Act, the Director shall submit to the congressional intelligence committees a report on the guidance required by subsection (a).\n**(3) Form**\nThe report submitted under paragraph (2)\u2014\n**(A)**\nshall include\u2014\n**(i)**\nan unclassified version suitable for dissemination to relevant individuals, including in the private sector; and\n**(ii)**\na publicly available version; and\n**(B)**\nmay include a classified annex.\n##### (f) Definitions\nIn this section:\n**(1)**\nThe term artificial intelligence has the meaning given such term in section 238(g) of the John S. McCain National Defense Authorization Act for Fiscal Year 2019 ( Public Law 115\u2013232 ; 10 U.S.C. note prec. 4061).\n**(2)**\nThe term artificial intelligence supply chain means artificial intelligence models computing environments for performing model training or inference tasks, training or test data, frameworks, or other components or model artifacts necessary for the training, management, or maintenance of any artificial intelligence system.\n**(3)**\nThe term congressional intelligence committees means the Select Committee on Intelligence of the Senate and the Permanent Select Committee on Intelligence of the House of Representatives.\n**(4)**\nThe term covered artificial intelligence technologies means advanced artificial intelligence (whether developed by the private sector, the United States Government, or a public-private partnership) with critical capabilities that the Director determines would pose a grave national security threat if acquired or stolen by threat actors, such as artificial intelligence systems that match or exceed human expert performance in chemical, biological, radiological, and nuclear matters, cyber offense, model autonomy, persuasion, research and development, and self-improvement.\n**(5)**\nThe term technology theft means any unauthorized acquisition, replication, or appropriation of covered artificial intelligence technologies or components of such technologies, including models, model weights, architectures, or core algorithmic insights, through any means, such as cyber attacks, insider threats, and side-channel attacks, or exploitation of public interfaces.\n**(6)**\nThe term threat actors means nation-state actors and other highly resourced actors capable of technology theft or sabotage.",
      "versionDate": "2025-11-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-18T19:51:33Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3202is.xml"
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
      "title": "Advanced Artificial Intelligence Security Readiness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-17T04:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Advanced Artificial Intelligence Security Readiness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Director of the National Security Agency to develop guidance to secure artificial intelligence related technologies, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:17Z"
    }
  ]
}
```
