# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1792?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1792
- Title: AI Whistleblower Protection Act
- Congress: 119
- Bill type: S
- Bill number: 1792
- Origin chamber: Senate
- Introduced date: 2025-05-15
- Update date: 2026-05-21T20:40:52Z
- Update date including text: 2026-05-21T20:40:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-15: Introduced in Senate
- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-05-15: Introduced in Senate

## Actions

- 2025-05-15 - IntroReferral: Introduced in Senate
- 2025-05-15 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-15",
    "latestAction": {
      "actionDate": "2025-05-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1792",
    "number": "1792",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "G000386",
        "district": "",
        "firstName": "Chuck",
        "fullName": "Sen. Grassley, Chuck [R-IA]",
        "lastName": "Grassley",
        "party": "R",
        "state": "IA"
      }
    ],
    "title": "AI Whistleblower Protection Act",
    "type": "S",
    "updateDate": "2026-05-21T20:40:52Z",
    "updateDateIncludingText": "2026-05-21T20:40:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-15",
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
      "actionDate": "2025-05-15",
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
          "date": "2025-05-15T19:08:41Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "DE"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "TN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "MN"
    },
    {
      "bioguideId": "H001089",
      "firstName": "Josh",
      "fullName": "Sen. Hawley, Josh [R-MO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hawley",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "MO"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2025-05-15",
      "state": "HI"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1792is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1792\nIN THE SENATE OF THE UNITED STATES\nMay 15, 2025 Mr. Grassley (for himself, Mr. Coons , Mrs. Blackburn , Ms. Klobuchar , Mr. Hawley , and Mr. Schatz ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo prohibit employment discrimination against whistleblowers reporting AI security vulnerabilities or AI violations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Whistleblower Protection Act .\n#### 2. Definitions\nIn this Act:\n**(1) AI security vulnerability**\nThe term AI security vulnerability means any failure or lapse in security that could potentially allow emerging artificial intelligence technology to be acquired by a person (including a foreign entity) by theft or other means.\n**(2) AI violation**\nThe term AI violation means\u2014\n**(A)**\nany violation of Federal law, including rules and regulations, related to or committed during the development, deployment, or use of artificial intelligence; or\n**(B)**\nany failure to appropriately respond to a substantial and specific danger that the development, deployment, or use of artificial intelligence may pose to public safety, public health, or national security.\n**(3) Artificial intelligence**\nThe term artificial intelligence includes any of the following:\n**(A)**\nAn artificial system that performs tasks under varying and unpredictable circumstances without significant human oversight, or that can learn from experience and improve performance when exposed to data sets.\n**(B)**\nAn artificial system developed in computer software, physical hardware, or other context that solves tasks requiring human-like perception, cognition, planning, learning, communication, or physical action.\n**(C)**\nAn artificial system designed to think or act like a human, including cognitive architectures and neural networks.\n**(D)**\nA set of techniques, including machine learning, that are designed to approximate a cognitive task.\n**(E)**\nAn artificial system designed to act rationally, including an intelligent software agent or embodied robot that achieves goals using perception, planning, reasoning, learning, communicating, decision making, and acting.\n**(4) Artificial system**\nThe term artificial system \u2014\n**(A)**\nmeans any data system, software, application, tool, or utility that operates in whole or in part using dynamic or static machine learning algorithms or other forms of artificial intelligence, including in the case\u2014\n**(i)**\nthe data system, software, application, tool, or utility is established primarily for the purpose of researching, developing, or implementing artificial intelligence technology; or\n**(ii)**\nartificial intelligence capability is integrated into another system or agency business process, operational activity, or technology system; and\n**(B)**\ndoes not include any common commercial product within which artificial intelligence is embedded, such as a word processor or map navigation system.\n**(5) Commerce**\nThe terms commerce and industry or activity affecting commerce mean any activity, business, or industry in commerce or in which a labor dispute would hinder or obstruct commerce or the free flow of commerce, and include commerce and any industry affecting commerce , as defined in paragraphs (1) and (3) of section 501 of the Labor Management Relations Act, 1947 (29 U.S.C. 142 (1) and (3)).\n**(6) Covered individual**\nThe term covered individual includes\u2014\n**(A)**\nan employee, including a former employee; and\n**(B)**\nan independent contractor, including a former independent contractor.\n**(7) Emerging artificial intelligence technology**\nThe term emerging artificial intelligence technology , with respect to an AI security vulnerability, means any artificial system that exhibits a level of performance, complexity, or autonomy that is comparable to or exceeds capabilities that are generally considered state-of-the-art as of the time of the AI security vulnerability.\n**(8) Employer**\nThe term employer means any person (including any officer, employee, contractor, subcontractor, agent, company, partnership, or other individual or entity) engaged in commerce or an industry or activity affecting commerce who pays any compensation to a covered individual in exchange for the covered individual providing work to the person.\n#### 3. Anti-retaliation protection for AI whistleblowers\n##### (a) Prohibition against retaliation\nNo employer may, directly or indirectly, discharge, demote, suspend, threaten, blacklist, harass, or in any other manner discriminate against a covered individual in the terms and conditions of employment or post-employment of the covered individual (or the terms and conditions of work provided by the covered individual as an independent contractor) because of any lawful act done by the covered individual\u2014\n**(1)**\nin providing information regarding an AI security vulnerability or AI violation, or any conduct that the covered individual reasonably believes constitutes an AI security vulnerability or AI violation, to\u2014\n**(A)**\nthe appropriate regulatory official or the Attorney General;\n**(B)**\na regulatory or law enforcement agency; or\n**(C)**\nany Member of Congress or any committee of Congress;\n**(2)**\nin initiating, testifying in, or assisting in any investigation or judicial or administrative action of an appropriate regulatory or law enforcement agency or the Department of Justice, or any investigation of Congress, based upon or related to the information described in paragraph (1); or\n**(3)**\nin providing information regarding an AI security vulnerability or AI violation, or any conduct that the covered individual reasonably believes constitutes an AI security vulnerability or AI violation, to\u2014\n**(A)**\na person with supervisory authority over the covered individual at the employer of the covered individual; or\n**(B)**\nanother individual working for the employer described in subparagraph (A) whom the covered individual reasonably believes has the authority to\u2014\n**(i)**\ninvestigate, discover, or terminate the misconduct; or\n**(ii)**\ntake any other action to address the misconduct.\n##### (b) Enforcement\n**(1) In general**\nA covered individual who alleges they are aggrieved by a violation of subsection (a) may seek relief under paragraph (3) by\u2014\n**(A)**\nfiling a complaint with the Secretary of Labor in accordance with the requirements of paragraph (2)(A); or\n**(B)**\nif the Secretary of Labor has not issued a final decision in accordance with such paragraph within 180 days of the filing of a complaint under subparagraph (A), and there is no showing that such a delay is due to the bad faith of the covered individual, bringing an action against the employer at law or in equity in the appropriate district court of the United States, which shall have jurisdiction over such an action without regard to the amount in controversy.\n**(2) Procedure**\n**(A) Department of Labor complaints**\n**(i) In general**\nExcept as provided in clause (ii) and paragraph (3), a complaint filed with the Secretary of Labor under paragraph (1)(A) shall be governed by the rules and procedures set forth in section 42121(b) of title 49, United States Code, including the legal burdens of proof described in such section.\n**(ii) Exceptions**\nWith respect to a complaint filed under paragraph (1)(A), notification required under section 42121(b)(1) of title 49, United States Code, shall be made to each person named in the complaint, including the employer.\n**(B) District court actions**\n**(i) Jury trial**\nA party to an action brought under paragraph (1)(B) shall be entitled to trial by jury.\n**(ii) Statute of limitations**\n**(I) In general**\nAn action may not be brought under paragraph (1)(B)\u2014\n**(aa)**\nmore than 6 years after the date on which the violation of subsection (a) occurs; or\n**(bb)**\nmore than 3 years after the date on which facts material to the right of action are known, or reasonably should have been known, by the covered individual bringing the action.\n**(II) Required action within 10 years**\nNotwithstanding subclause (I), an action under paragraph (1)(B) may not in any circumstance be brought more than 10 years after the date on which the violation occurs.\n**(3) Relief**\nRelief for a covered individual prevailing with respect to a complaint filed under paragraph (1)(A) or an action under paragraph (1)(B) shall include\u2014\n**(A)**\nreinstatement with the same seniority status that the covered individual would have had, but for the violation;\n**(B)**\n2 times the amount of back pay otherwise owed to the covered individual, with interest;\n**(C)**\nthe payment of compensatory damages, which shall include compensation for litigation costs, expert witness fees, and reasonable attorneys\u2019 fees; and\n**(D)**\nany other appropriate remedy with respect to the violation as determined by the Secretary of Labor in a complaint under subparagraph (A) of paragraph (1) or by the court in an action under subparagraph (B) of such paragraph.\n##### (c) Nonenforceability waivers of rights or remedies\nThe rights and remedies provided for in this section may not be waived or altered by any contract, agreement, policy form, or condition of employment (or condition of work as an independent contractor), including by any agreement requiring a covered individual to engage in arbitration, mediation, or any other alternative dispute resolution process prior to seeking relief under subsection (b).",
      "versionDate": "2025-05-15",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2026-04-27",
        "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committees on Energy and Commerce, Agriculture, Oversight and Government Reform, Education and Workforce, the Judiciary, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8516",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "American Leadership in AI Act",
      "type": "HR"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-15",
        "text": "Referred to the House Committee on Education and Workforce."
      },
      "number": "3460",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "AI Whistleblower Protection Act",
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
        "name": "Labor and Employment",
        "updateDate": "2025-06-02T13:23:01Z"
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
      "date": "2025-05-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1792is.xml"
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
      "title": "AI Whistleblower Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T11:03:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI Whistleblower Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit employment discrimination against whistleblowers reporting AI security vulnerabilities or AI violations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:28Z"
    }
  ]
}
```
