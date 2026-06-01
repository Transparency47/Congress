# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1396?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1396
- Title: Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1396
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-02-23T20:00:01Z
- Update date including text: 2026-02-23T20:00:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1396",
    "number": "1396",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C000127",
        "district": "",
        "firstName": "Maria",
        "fullName": "Sen. Cantwell, Maria [D-WA]",
        "lastName": "Cantwell",
        "party": "D",
        "state": "WA"
      }
    ],
    "title": "Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025",
    "type": "S",
    "updateDate": "2026-02-23T20:00:01Z",
    "updateDateIncludingText": "2026-02-23T20:00:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T20:36:46Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "TN"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1396is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1396\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Ms. Cantwell (for herself, Mrs. Blackburn , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require transparency with respect to content and content provenance information, to protect artistic content, and for other purposes.\n#### 1. Short title; table of contents\nThis Act may be cited as the Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthere is a lack of\u2014\n**(A)**\nvisibility into how artificial intelligence systems work;\n**(B)**\ntransparency regarding the information used to train such systems; and\n**(C)**\nconsensus-based standards and practices to guide the development and deployment of such systems;\n**(2)**\nit is becoming increasingly difficult to assess the nature, origins, and authenticity of digital content that has been generated or modified algorithmically;\n**(3)**\nthese deficiencies negatively impact the public and, particularly, the journalists, publishers, broadcasters, and artists whose content is used to train these systems and is manipulated to produce synthetic content and synthetically-modified content that competes unfairly in the digital marketplace with covered content; and\n**(4)**\nthe development and adoption of consensus-based standards would mitigate these impacts, catalyze innovation in this nascent industry, and put the United States in a position to lead the development of artificial intelligence systems moving forward.\n#### 3. Definitions\nIn this title:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Artificial intelligence blue-teaming**\nThe term artificial intelligence blue-teaming means an effort to conduct operational vulnerability evaluations and provide mitigation techniques to entities who have a need for an independent technical review of the security posture of an artificial intelligence system.\n**(3) Artificial intelligence red-teaming**\nThe term artificial intelligence red-teaming means structured adversarial testing efforts of an artificial intelligence system to identify risks, flaws, and vulnerabilities of the artificial intelligence system, such as harmful outputs from the system, unforeseen or undesirable system behaviors, limitations, or potential risks associated with the misuse of the system.\n**(4) Content provenance information**\nThe term content provenance information means state-of-the-art, machine-readable information documenting the origin and history of a piece of digital content, such as an image, a video, audio, or text.\n**(5) Covered content**\nThe term covered content means a digital representation, such as text, an image, or audio or video content, of any work of authorship described in section 102 of title 17, United States Code.\n**(6) Covered platform**\nThe term covered platform means a website, internet application, or mobile application available to users in the United States, including a social networking site, video sharing service, search engine, or content aggregation service available to users in the United States, that either\u2014\n**(A)**\ngenerates at least $50,000,000 in annual revenue; or\n**(B)**\nhad at least 25,000,000 monthly active users for not fewer than 3 of the 12 months immediately preceding any conduct by the covered platform in violation of this Act.\n**(7) Deepfake**\nThe term deepfake means synthetic content or synthetically-modified content that\u2014\n**(A)**\nappears authentic to a reasonable person; and\n**(B)**\ncreates a false understanding or impression.\n**(8) Director**\nThe term Director means the Under Secretary of Commerce for Intellectual Property and Director of the United States Patent and Trademark Office.\n**(9) Synthetic content**\nThe term synthetic content means information, including works of human authorship such as images, videos, audio clips, and text, that has been wholly generated by algorithms, including by artificial intelligence.\n**(10) Synthetically-modified content**\nThe term synthetically-modified content means information, including works of human authorship such as images, videos, audio clips, and text, that has been significantly modified by algorithms, including by artificial intelligence.\n**(11) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Standards and Technology.\n**(12) Watermarking**\nThe term watermarking means the act of embedding information that is intended to be difficult to remove into an output, including an output such as text, an image, an audio, a video, software code, or any other digital content or data, for the purposes of verifying the authenticity of the output or the identity or characteristics of its provenance, modifications, or conveyance\n#### 4. Facilitation of development of standards for content provenance information and detection of synthetic content and synthetically-modified content\n##### (a) In general\nThe Under Secretary shall establish a public-private partnership to facilitate the development of standards regarding content provenance information technologies and the detection of synthetic content and synthetically-modified content, including with respect to the following:\n**(1)**\nFacilitating the development of guidelines and voluntary, consensus-based standards and best practices for watermarking, content provenance information, synthetic content and synthetically-modified content detection, including for images, audio, video, text, and multimodal content, the use of data to train artificial intelligence systems, and such other matters relating to transparency of synthetic media as the Under Secretary considers appropriate.\n**(2)**\nFacilitating the development of guidelines, metrics, and practices to evaluate and assess tools to detect and label synthetic content, synthetically-modified content, and non-synthetic content, including artificial intelligence red-teaming and artificial intelligence blue-teaming.\n**(3)**\nEstablishing grand challenges and prizes in coordination with the Defense Advanced Research Projects Agency and the National Science Foundation to detect and label synthetic content, synthetically-modified content, and non-synthetic content and to develop cybersecurity and other countermeasures to defend against tampering with detection tools, watermarks, or content provenance information.\n##### (b) Consultation\nIn developing the standards described in subsection (a), the Under Secretary shall consult with the Register of Copyrights and the Director.\n#### 5. National Institute of Standards and Technology research, development, and public education regarding synthetic content and synthetically-modified content\n##### (a) Research and development\nThe Under Secretary shall carry out a research program to enable advances in measurement science, standards, and testing relating to the robustness and efficacy of\u2014\n**(1)**\ntechnologies for synthetic content and synthetically-modified content detection, watermarking, and content provenance information; and\n**(2)**\ncybersecurity protections and other countermeasures used to prevent tampering with such technologies.\n##### (b) Public education campaigns regarding synthetic content\nNot later than 1 year after the date of enactment of this Act, the Under Secretary shall, in consultation with the Register of Copyrights and the Director, carry out a public education campaign regarding synthetic content and synthetically-modified content (including deepfakes), watermarking, and content provenance information.\n#### 6. Requirements for content provenance information; prohibited acts\n##### (a) Content provenance information\n**(1) Synthetic content and synthetically-modified content**\nBeginning on the date that is 2 years after the date of enactment of this Act, any person who, for a commercial purpose, makes available in interstate commerce a tool used for the primary purpose of creating synthetic content or synthetically-modified content shall\u2014\n**(A)**\ntaking into consideration the content provenance information standards established under section 4, provide users of such tool with the ability to include content provenance information that indicates the piece of digital content is synthetic content or synthetically-modified content for any synthetic content or synthetically-modified content created by the tool; and\n**(B)**\nin the event a user opts to include content provenance information under subparagraph (A), establish, to the extent technically feasible, reasonable security measures to ensure that such content provenance information is machine-readable and not easily removed, altered, or separated from the underlying content.\n**(2) Covered content**\nBeginning on the date that is 2 years after the date of enactment of this Act, any person who, for a commercial purpose, makes available in interstate commerce a tool used for the primary purpose of creating or substantially modifying covered content shall\u2014\n**(A)**\ntaking into consideration the content provenance information standards established under section 4, provide users of such tool with the ability to include content provenance information for any covered content created or significantly modified by the tool; and\n**(B)**\nin the event a user opts to include content provenance information under subparagraph (A), establish, to the extent technically feasible, reasonable security measures to ensure that such content provenance information is machine-readable and not easily removed, altered, or separated from the underlying content.\n##### (b) Removal of content provenance information\n**(1) In general**\nIt shall be unlawful for any person to knowingly remove, alter, tamper with, or disable content provenance information in furtherance of an unfair or deceptive act or practice in or affecting commerce.\n**(2) Covered platforms**\n**(A) In general**\nSubject to subparagraph (B), it shall be unlawful for a covered platform, to remove, alter, tamper with, or disable content provenance information or to separate the content provenance information from the content so that the content provenance information cannot be accessed by users of the platform.\n**(B) Exception for security research**\nA covered platform shall not be liable for a violation of subparagraph (A) if such covered platform removes, alters, tampers with, or disables content provenance information for a purpose necessary, proportionate, and limited to perform research to enhance the security of the covered platform.\n##### (c) Prohibition on non-Consensual use of covered content that has attached or associated content provenance information\nIt shall be unlawful for any person, for a commercial purpose, to knowingly use any covered content that has content provenance information that is attached to or associated with such covered content or covered content from which the person knows or should know that content provenance information has been removed or separated in violation of subsection (b), in order to train a system that uses artificial intelligence or an algorithm or to generate synthetic content or synthetically-modified content unless such person obtains the express, informed consent of the person who owns the covered content, and complies with any terms of use pertaining to the use of such content, including terms regarding compensation for such use, as required by the owner of copyright in such content.\n#### 7. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this title.\n**(B) Privileges and immunities**\nAny person who violates this Act, or a regulation promulgated under this Act shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Enforcement by States\n**(1) In general**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any person in a practice that violates this Act, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to\u2014\n**(A)**\nenjoin further violation of this Act by such person;\n**(B)**\ncompel compliance with this Act;\n**(C)**\nobtain damages, restitution, or other compensation on behalf of such residents; and\n**(D)**\nobtain such other relief as the court may consider to be appropriate.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) before initiating the civil action.\n**(ii) Contents**\nThe notification required by clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by the commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Action by the Commission**\nIf the Commission institutes a civil action or an administrative action with respect to a violation of this Act, the attorney general of a State may not, during the pendency of such action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission for the violation with respect to which the Commission instituted such action.\n**(5) Venue; service or process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n**(6) Actions by other State officials**\n**(A) In general**\nIn addition to civil actions brought by attorneys general under paragraph (1), any other officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n**(7) Damages**\nIf a person brings a civil action for a violation of this Act pursuant to subsection (c) and receives any monetary damages, the court shall reduce the amount of any damages awarded under this subsection by the amount of monetary damages awarded to such person.\n##### (c) Enforcement by private parties and government entities\n**(1) In general**\nAny person who owns covered content that has content provenance information that is attached to or associated with such covered content may bring a civil action in a court of competent jurisdiction against\u2014\n**(A)**\nany person or covered platform for removing, altering, tampering with, or disabling such content provenance information in violation of subsection (b)(1) or (b)(2) of section 6; and\n**(B)**\nany person for using such covered content in violation of section 6(c).\n**(2) Relief**\nIn a civil action brought under paragraph (1) in which the plaintiff prevails, the court may award the plaintiff declaratory or injunctive relief, compensatory damages, and reasonable litigation expenses, including a reasonable attorney\u2019s fee.\n**(3) Statute of limitations**\nAn action for a violation of this Act brought under this subsection may be commenced not later than 4 years after the date upon which the plaintiff discovers or should have discovered the facts giving rise to such violation.\n#### 8. Rule of construction\nThis Act does not impair or in any way alter the rights of copyright owners under any other applicable law.\n#### 9. Severability\nIf any provision of this Act, or an amendment made by this Act, is determined to be unenforceable or invalid, the remaining provisions of this Act and the amendments made by this Act shall not be affected.",
      "versionDate": "2025-04-09",
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
        "updateDate": "2025-05-19T15:54:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-09",
    "originChamber": "Senate",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119s1396",
          "measure-number": "1396",
          "measure-type": "s",
          "orig-publish-date": "2025-04-09",
          "originChamber": "SENATE",
          "update-date": "2026-02-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s1396v00",
            "update-date": "2026-02-23"
          },
          "action-date": "2025-04-09",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025</strong></p><p>This bill requires certain tools used to create or modify digital content, including artificial intelligence (AI), to allow users to embed in such content information documenting its origin and history. This is known as <em>content provenance information</em>. The bill also prohibits the removal or alteration of content provenance information in certain circumstances.</p><p>Specifically, tools used for the primary purpose of creating or significantly modifying content via algorithms, or creating or substantially modifying digital representations of copyrighted work, must allow users to include content provenance information in the resulting digital content.</p><p>Further, the bill prohibits certain large websites and applications (e.g., social media applications) from removing, altering, tampering with, or disabling content provenance information; and it prohibits any individual or entity from taking such actions in furtherance of an unfair or deceptive act in commerce.</p><p>Finally, the bill prohibits certain commercial uses of digital representations of copyrighted work that has associated content provenance information without the consent of the work\u2019s owner. Specifically, such representations may not be used to (1) train a system that uses AI or an algorithm, or (2) create algorithmically generated or modified content.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials). Owners of digital representations of copyrighted content with associated content provenance information may also bring suit to enforce violations related to their content.</p>"
        },
        "title": "Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s1396.xml",
    "summary": {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025</strong></p><p>This bill requires certain tools used to create or modify digital content, including artificial intelligence (AI), to allow users to embed in such content information documenting its origin and history. This is known as <em>content provenance information</em>. The bill also prohibits the removal or alteration of content provenance information in certain circumstances.</p><p>Specifically, tools used for the primary purpose of creating or significantly modifying content via algorithms, or creating or substantially modifying digital representations of copyrighted work, must allow users to include content provenance information in the resulting digital content.</p><p>Further, the bill prohibits certain large websites and applications (e.g., social media applications) from removing, altering, tampering with, or disabling content provenance information; and it prohibits any individual or entity from taking such actions in furtherance of an unfair or deceptive act in commerce.</p><p>Finally, the bill prohibits certain commercial uses of digital representations of copyrighted work that has associated content provenance information without the consent of the work\u2019s owner. Specifically, such representations may not be used to (1) train a system that uses AI or an algorithm, or (2) create algorithmically generated or modified content.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials). Owners of digital representations of copyrighted content with associated content provenance information may also bring suit to enforce violations related to their content.</p>",
      "updateDate": "2026-02-23",
      "versionCode": "id119s1396"
    },
    "title": "Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-09",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025</strong></p><p>This bill requires certain tools used to create or modify digital content, including artificial intelligence (AI), to allow users to embed in such content information documenting its origin and history. This is known as <em>content provenance information</em>. The bill also prohibits the removal or alteration of content provenance information in certain circumstances.</p><p>Specifically, tools used for the primary purpose of creating or significantly modifying content via algorithms, or creating or substantially modifying digital representations of copyrighted work, must allow users to include content provenance information in the resulting digital content.</p><p>Further, the bill prohibits certain large websites and applications (e.g., social media applications) from removing, altering, tampering with, or disabling content provenance information; and it prohibits any individual or entity from taking such actions in furtherance of an unfair or deceptive act in commerce.</p><p>Finally, the bill prohibits certain commercial uses of digital representations of copyrighted work that has associated content provenance information without the consent of the work\u2019s owner. Specifically, such representations may not be used to (1) train a system that uses AI or an algorithm, or (2) create algorithmically generated or modified content.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials). Owners of digital representations of copyrighted content with associated content provenance information may also bring suit to enforce violations related to their content.</p>",
      "updateDate": "2026-02-23",
      "versionCode": "id119s1396"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1396is.xml"
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
      "title": "Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T03:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Content Origin Protection and Integrity from Edited and Deepfaked Media Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T03:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require transparency with respect to content and content provenance information, to protect artistic content, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T03:18:26Z"
    }
  ]
}
```
