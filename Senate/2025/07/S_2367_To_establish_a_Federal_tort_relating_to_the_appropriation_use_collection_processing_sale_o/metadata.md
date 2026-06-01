# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2367?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2367
- Title: AI Accountability and Personal Data Protection Act
- Congress: 119
- Bill type: S
- Bill number: 2367
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2026-03-17T14:40:07Z
- Update date including text: 2026-03-17T14:40:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2367",
    "number": "2367",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
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
    "title": "AI Accountability and Personal Data Protection Act",
    "type": "S",
    "updateDate": "2026-03-17T14:40:07Z",
    "updateDateIncludingText": "2026-03-17T14:40:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T22:41:11Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "sponsorshipDate": "2025-07-21",
      "state": "CT"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "False",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-24",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2367is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2367\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Hawley (for himself and Mr. Blumenthal ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo establish a Federal tort relating to the appropriation, use, collection, processing, sale, or other exploitation of individuals' data without express, prior consent.\n#### 1. Short title\nThis Act may be cited as the AI Accountability and Personal Data Protection Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate, use, collect, process, sell, or otherwise exploit**\nThe term appropriate, use, collect, process, sell, or otherwise exploit includes\u2014\n**(A)**\nthe training of a generative artificial intelligence system that is sold, rented, licensed, or otherwise used by the provider of the generative artificial intelligence system; and\n**(B)**\nthe generation, by a generative artificial intelligence system, of any covered data that pertains to an individual, including content that imitates, replicates, or is substantially derived from the covered data of the individual.\n**(2) Artificial intelligence**\nThe term artificial intelligence has the meaning given that term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(3) Artificial intelligence system**\nThe term artificial intelligence system means any data system, software, hardware, application, tool, or utility that operates, in whole or in part, using artificial intelligence.\n**(4) Covered data**\nThe term covered data \u2014\n**(A)**\nmeans any information, data, or material, regardless of form or format, that\u2014\n**(i)**\nidentifies, relates to, describes, is capable of being associated with, or can reasonably be linked, directly or indirectly, with a specific individual;\n**(ii)**\nis derived, inferred, or generated from information described in clause (i), or is used to derive, infer, or generate information described in clause (i); or\n**(iii)**\nis generated by an individual and is protected by copyright, regardless of whether the copyright has been registered with the United States Copyright Office or any other registration authority; and\n**(B)**\nincludes\u2014\n**(i)**\npersonally identifiable information;\n**(ii)**\nunique identifiers, such as device IDs, advertising IDs, or IP addresses;\n**(iii)**\ngeolocation data;\n**(iv)**\nbiometric information;\n**(v)**\nbehavioral data, such as browsing history or purchasing patterns; or\n**(vi)**\ninferred, derived, or predicted data used to create a profile about an individual or group of individuals.\n**(5) Express, prior consent**\nThe term express, prior consent means a clear, affirmative act by an individual, made in advance of any appropriation, use, collection, processing, sale, or other exploitation of covered data, indicating a freely given, informed, and unambiguous consent to the specific appropriation, use, collection, processing, sale, or other exploitation of covered data of the individual.\n**(6) Generative artificial intelligence system**\nThe term generative artificial intelligence system means an artificial intelligence system that is capable of generating novel text, video, images, audio, and other media based on prompts or other forms of data provided by an individual.\n**(7) Personally identifiable information**\nThe term personally identifiable information means information that can be used to distinguish or trace the identity of an individual, either alone or when combined with other personal or identifying information that is linked or linkable to a specific individual.\n**(8) Predispute arbitration agreement**\nThe term predispute arbitration agreement means an agreement to arbitrate a dispute that has not yet arisen at the time of the making of the agreement.\n**(9) Predispute joint-action waiver**\nThe term predispute joint-action waiver means an agreement, whether or not part of a predispute arbitration agreement, that would prohibit, or waive the right of, one of the parties to the agreement to participate in a joint, class, or collective action in a judicial, arbitral, administrative, or other forum, concerning a dispute that has not yet arisen at the time of the making of the agreement.\n#### 3. Federal tort for misuse of covered data\n##### (a) Liability\nAny person who, in or affecting interstate or foreign commerce, appropriates, uses, collects, processes, sells, or otherwise exploits the covered data of an individual, without the express, prior consent of the individual, shall be liable to the individual in accordance with this section.\n##### (b) Private right of action\n**(1) In general**\nAny individual whose covered data is appropriated, used, collected, processed, sold, or otherwise exploited without the express, prior consent of the individual as described in subsection (a) may bring a civil action in an appropriate district court of the United States or a State court of competent jurisdiction against any person who\u2014\n**(A)**\nengaged in the appropriation, use, collection, processing, sale, or other exploitation of the covered data; or\n**(B)**\naided and abetted another person in the appropriation, use, collection, processing, sale, or other exploitation of the covered data.\n**(2) Remedies**\nAn individual prevailing in a civil action brought under paragraph (1) may recover\u2014\n**(A)**\ncompensatory damages in an amount equal to the greater of\u2014\n**(i)**\nactual damages;\n**(ii)**\ntreble any profits from the appropriation, use, collection, processing, sale, or other exploitation of the covered data of the individual as described in subsection (a); or\n**(iii)**\n$1,000;\n**(B)**\npunitive damages;\n**(C)**\ninjunctive relief; and\n**(D)**\nattorney\u2019s fees and costs.\n**(3) Affirmative defense of consent**\n**(A) In general**\nIt shall be an affirmative defense to a civil action under paragraph (1) brought by or on behalf of an individual whose covered data was appropriated, used, collected, processed, sold, or otherwise exploited if the defendant demonstrates that the individual provided express, prior consent for such appropriation, use, collection, processing, sale, or other exploitation of the covered data of the individual.\n**(B) Invalid grounds for consent**\nConsent to the appropriation, use, collection, processing, sale, or other exploitation of covered data shall not be deemed valid if such consent was obtained\u2014\n**(i)**\nthrough coercion or deception; or\n**(ii)**\nas a condition of using a product or service through which the appropriation, use, collection, processing, sale, or other exploitation of the covered data exceeds what is reasonably necessary to provide that product or service.\n##### (c) Inapplicability of the Federal Arbitration Act\n**(1) In general**\nNotwithstanding any other provision of law, including chapter 1 of title 9, United States Code (commonly known as the Federal Arbitration Act ), a predispute arbitration agreement or predispute joint-action waiver shall not be valid or enforceable with respect to any claim arising under this Act.\n**(2) Unenforceable agreements**\nAny agreement purporting to waive, limit, or preclude the right of an individual to bring an action in a court of law or to participate in a joint, class, collective, or representative action concerning any claim arising under this Act shall be deemed contrary to public policy and shall be null, void, and unenforceable.\n**(3) Determination under Federal law by Federal court**\nAn issue as to whether this Act applies with respect to a dispute shall be determined under Federal law. The applicability of this Act to an agreement to arbitrate and the validity and enforceability of an agreement to which this Act applies shall be determined by a court, rather than an arbitrator, irrespective of whether the party resisting arbitration challenges the arbitration agreement specifically or in conjunction with other terms of the contract containing such agreement, and irrespective of whether the agreement purports to delegate such determinations to an arbitrator.\n**(4) Collective bargaining agreements**\nNothing in this Act shall apply to any arbitration provision in a contract between an employer and a labor organization or between labor organizations, except that no such arbitration provision shall have the effect of waiving the right of a worker to seek judicial enforcement of a right arising under a provision of the Constitution of the United States, a State constitution, or a Federal or State statute, or public policy arising therefrom.\n##### (d) Specific disclosure of third parties required\n**(1) In general**\nConsent required under subsection (a) shall not be valid for the appropriation, use, collection, processing, sale, or other exploitation of covered data by or to any third party unless\u2014\n**(A)**\neach third party is specifically and clearly disclosed to the individual to whom the covered data pertains at the time consent is sought; and\n**(B)**\nthe disclosure described in subparagraph (A) is affirmatively presented to the individual to whom the covered data pertains in a manner that ensures the disclosure is seen and acknowledged.\n**(2) Presentation**\nAny disclosure described in paragraph (1)\u2014\n**(A)**\nshall be presented distinctly and separately from any privacy policy, terms of service, or other general conditions or agreements; and\n**(B)**\nshall not be satisfied by the mere inclusion of a hyperlink or general reference to a privacy policy, user agreement, or other similar document.\n**(3) Invalid consent**\nAny purported consent for the appropriation, use, collection, processing, sale, or other exploitation of covered data by or to any third party obtained solely by inclusion within such general documents described in paragraph (2) or via non-specific or passive disclosure shall be invalid and unenforceable.\n#### 4. Relationship to existing law\n##### (a) No preemption of existing State laws\nNothing in this Act shall be construed to preempt or limit any law, rule, regulation, or common law doctrine of any State that is in effect as of the date of enactment of this Act.\n##### (b) Minimum standard\nThis Act shall be construed as establishing a minimum standard for the tort described in section 3(a), and nothing in this Act shall be deemed to prohibit or restrict the application of any State law, rule, regulation, or common law doctrine that provides greater or additional rights, remedies, or protections than the rights, remedies, and protections provided under this Act.",
      "versionDate": "2025-07-21",
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
        "name": "Law",
        "updateDate": "2026-03-17T14:40:07Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2367is.xml"
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
      "title": "AI Accountability and Personal Data Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-06T04:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI Accountability and Personal Data Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-06T04:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a Federal tort relating to the appropriation, use, collection, processing, sale, or other exploitation of individuals' data without express, prior consent.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-06T04:48:35Z"
    }
  ]
}
```
