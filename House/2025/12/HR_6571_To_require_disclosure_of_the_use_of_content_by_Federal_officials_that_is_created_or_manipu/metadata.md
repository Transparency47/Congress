# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6571?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6571
- Title: REAL Act
- Congress: 119
- Bill type: HR
- Bill number: 6571
- Origin chamber: House
- Introduced date: 2025-12-10
- Update date: 2026-01-08T17:49:52Z
- Update date including text: 2026-01-08T17:49:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-10: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-10: Introduced in House

## Actions

- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Introduced in House
- 2025-12-10 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-10",
    "latestAction": {
      "actionDate": "2025-12-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6571",
    "number": "6571",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000454",
        "district": "11",
        "firstName": "Bill",
        "fullName": "Rep. Foster, Bill [D-IL-11]",
        "lastName": "Foster",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "REAL Act",
    "type": "HR",
    "updateDate": "2026-01-08T17:49:52Z",
    "updateDateIncludingText": "2026-01-08T17:49:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-10",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-10",
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
          "date": "2025-12-10T15:06:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "S000250",
      "district": "17",
      "firstName": "Pete",
      "fullName": "Rep. Sessions, Pete [R-TX-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Sessions",
      "party": "R",
      "sponsorshipDate": "2025-12-10",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6571ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6571\nIN THE HOUSE OF REPRESENTATIVES\nDecember 10, 2025 Mr. Foster (for himself and Mr. Sessions ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require disclosure of the use of content by Federal officials that is created or manipulated using generative artificial intelligence in their publications, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsible and Ethical AI Labeling Act or the REAL Act .\n#### 2. Disclosure of content created or manipulated using generative artificial intelligence\n##### (a) Disclosure requirement\n**(1) Prohibition on Non-Disclosure**\nA Federal official may not publish, disseminate, or otherwise release content created or manipulated using generative artificial intelligence unless such content includes a disclaimer described in paragraph (2).\n**(2) Disclaimer requirements**\nThe disclaimer described in this paragraph\u2014\n**(A)**\nis clear, conspicuous, and prominently displayed or communicated with the content;\n**(B)**\nis written in plain language that is easily understandable to the general public; and\n**(C)**\nincludes the following:\n**(i)**\nA statement that informs the reader the content was created or manipulated using generative artificial intelligence.\n**(ii)**\nA brief explanation of how the content was generated or altered.\n**(iii)**\nA brief explanation of the technology or method used to create or manipulate the content.\n**(3) Exceptions**\nThis subsection does not apply to the following:\n**(A)**\nAny communication not intended for public release.\n**(B)**\nContent created for any classified purpose, if a summary or description of the content that complies with this section is retained by the publishing agency to accompany any unclassified publication of the content.\n**(C)**\nContent that includes any basic graphic or visual element, such as a text overlay, formatting, or other minor adjustment to visual media (such as brightness, contrast, or cropping) that does not materially alter the meaning or context of the content and the content does not otherwise contain content created or manipulated using generative artificial intelligence.\n**(D)**\nAny routine textual draft or other text-based document prepared using a digital tool, including text drafting software enabled by generative artificial intelligence, if such tool is used to enhance efficiency and the draft or document is reviewed by agency staff prior to publication.\n**(E)**\nWith respect to any content published, disseminated, or otherwise released by a Federal official, if such content is\u2014\n**(i)**\nnot related to the official duties of the officer or employee; and\n**(ii)**\nthat is so published, disseminated, or otherwise released on a personal, non-Government social media account or other medium.\n##### (b) Implementation and enforcement\n**(1) Rulemaking authority**\nNot later than 180 days after the date of the enactment of this Act, the Director of the Office of Management and Budget shall issue regulations or policies\u2014\n**(A)**\nto ensure compliance with this section by Federal officials; and\n**(B)**\nthat establish specific guidelines for the formatting, placement, and wording of the disclaimer described in subsection (a)(2) across various media formats.\n**(2) Audits and Reporting**\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter, the President, Vice President, and the head of each agency shall submit to Congress and make available on, with respect to the President or Vice President, a public website of the White House, and with respect to an agency, the public website of the agency, an audit that describes compliance with this section.\n**(3) Correction**\nIf the President, Vice President, or the head of the agency, or the Comptroller General, determines that the President, Vice President, or any officer or employee of an agency has published content created or manipulated using generative artificial intelligence in violation of this section, the President, Vice President, or the head of the agency (as the case may be) shall\u2014\n**(A)**\nto the greatest extent possible, retract such content; and\n**(B)**\nissue a communication that includes\u2014\n**(i)**\na statement that indicates the content was issued in violation this section;\n**(ii)**\na description of factors that led to the publication of the content; and\n**(iii)**\nif appropriate, a version of the content that has been revised to be in compliance with this section, which shall be made publicly available on the applicable website and disseminated, to the extent possible, to the same audience as the initial content.\n##### (c) Penalties\n**(1) Non-Compliance**\n**(A) Corrective action plan required**\nNot later than 30 days after the date on which an individual is found by the Comptroller General or an Inspector General to be in violation of this section, the President, Vice President, or head of that agency (as the case may be) shall submit to the Director of the Office of Management and Budget and Congress a plan that outlines the corrective action that will be taken to ensure compliance with this section.\n**(B) Oversight**\nIf a plan is not submitted pursuant to subparagraph (A), or a Federal official does not comply with such plan or is in violation of this section after implementation of such plan, the Comptroller General shall review the internal controls and procedures of the President, Vice President, or applicable agency and, not later than 30 days after the date of the violation, issue corrective actions that shall be carried out not later than 30 days after the date of issuance of such corrective actions.\n**(2) Accountability**\n**(A) Federal employee**\nAny Federal official who violates this section may be subject to appropriate disciplinary action, including disciplinary action under chapter 75 of title 5, United States Code.\n**(B) Contractors**\nAny Federal contractor responsible for non-compliance with this section may face disciplinary action, including restriction on public-facing communication, contract termination, or other corrective action, as determined necessary by the head of the contracting agency.\n##### (d) Definitions\nIn this section:\n**(1) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code, and includes the Executive Office of the President.\n**(2) Federal official**\nThe term Federal official means\u2014\n**(A)**\nthe President and the Vice President; and\n**(B)**\nany officer or employee of an agency.\n**(3) Generative artificial intelligence**\nThe term generative artificial intelligence means any algorithmic system that uses parameters derived from previously observed or generated data to non-deterministically create or modify digital content, including text, image, video, sound, or any combination thereof.\n##### (e) Effective date\nThis section shall take effect 90 days after the date of the enactment of this Act.",
      "versionDate": "2025-12-10",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-01-08T17:49:51Z"
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
      "date": "2025-12-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6571ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require disclosure of the use of content by Federal officials that is created or manipulated using generative artificial intelligence in their publications, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-29T14:18:19Z"
    },
    {
      "title": "REAL Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-29T14:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "REAL Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Responsible and Ethical AI Labeling Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-29T14:08:20Z"
    }
  ]
}
```
