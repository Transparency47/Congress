# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3540?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3540
- Title: LISTOS Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3540
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-20T15:13:37Z
- Update date including text: 2026-01-20T15:13:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3540",
    "number": "3540",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "LISTOS Act of 2025",
    "type": "S",
    "updateDate": "2026-01-20T15:13:37Z",
    "updateDateIncludingText": "2026-01-20T15:13:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T21:00:20Z",
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
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "OR"
    },
    {
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CA"
    },
    {
      "bioguideId": "H001042",
      "firstName": "Mazie",
      "fullName": "Sen. Hirono, Mazie K. [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Hirono",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "HI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3540is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3540\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Luj\u00e1n (for himself, Mr. Wyden , Mr. Padilla , and Ms. Hirono ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo ensure that large online platforms are addressing the needs of non-English users.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Language-Inclusive Support and Transparency for Online Services Act of 2025 or the LISTOS Act of 2025 .\n##### (b) Table of contents\nThe table of contents of this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Sense of Congress.\nSec. 3. Duty to ensure consistent enforcement.\nSec. 4. Disclosures on staffing and automated processes.\nSec. 5. Consistent access to tools and documentation.\nSec. 6. Advisory Group.\nSec. 7. Enforcement.\nSec. 8. Regulations.\nSec. 9. Effective dates.\nSec. 10. Definitions.\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nsubstantial and deliberate investments across languages are essential to protect the safety of users online and ensure equitable access to digital spaces;\n**(2)**\nonline platforms have historically under-invested in ensuring non-English content moderation and automated content detection and filtering processes keep pace with their English counterparts, providing little transparency into the efficacy of efforts to detect, review, and remove content that violates laws or platform policies across languages;\n**(3)**\nthis difference in enforcement for platforms' existing policies and uneven moderation practices across both manual and automated processes has increased the proliferation of illegal and harmful content across many languages and the deliberate targeting of non-English-speaking communities for fraud and harassment; and\n**(4)**\nany reform effort for online platform safety must ensure equitable investment across languages in order to promote economic opportunity, public health, and civil rights.\n#### 3. Duty to ensure consistent enforcement\n##### (a) In general\nThe operator of a covered platform shall provide that processes used by the platform for detecting, suppressing, and removing illegal content, or content that otherwise violates platform policies, are reasonably consistent for languages in which the covered platform engages in monetization practices.\n##### (b) Considerations\nAny entity enforcing or promulgating rules under subsection (a) shall take into consideration factors that may impact the covered platform's ability to enforce its policies with respect to content in a given language, including staffing levels and language proficiency, or the effectiveness of automated systems designed to filter or flag content for additional review.\n##### (c) Exceptions\nSubsection (a) shall not apply\u2014\n**(1)**\nto a messaging service provided by a covered platform to the extent that such service employs end-to-end encryption; and\n**(2)**\nto a language in which a covered platform offers a service if such language is used by fewer than 100,000 users of the service for 9 or more of the past 12 months within the United States.\n##### (d) Rule of construction; limitation on regulation\nNothing in this section shall be construed to require, and no regulation issued by the Commission to carry out this section may require, that a covered platform take any particular action on a specific piece of content or class of content.\n#### 4. Disclosures on staffing and automated processes\n##### (a) In general\nThe operator of a covered platform shall, not less than annually, submit to the Commission and make available to the public, in a machine-readable format, a clear and easily comprehensible report on any manual and algorithmic content moderation that the covered platform engaged in during the relevant period. Each such report shall be in compliance with the rules established under subsection (b).\n##### (b) Rules\nThe Commission shall, in accordance with section 8, establish rules for reports under subsection (a). Such rules shall require that a report include the following information:\n**(1) Content moderation staffing**\n**(A) In general**\nThe number of staff employed by the covered platform (whether directly employed by the platform or contracted through a third party) for the purposes of manually reviewing content for removal or other interventions, in aggregate and broken down by\u2014\n**(i)**\nthe countries in which the employees are located;\n**(ii)**\nthe geographic or regional area to which the employees are assigned; and\n**(iii)**\nlanguages spoken by the employees relevant to their employment and their levels of language proficiency.\n**(B) Staff support**\nA description of the training and support provided to content moderation staff, including\u2014\n**(i)**\nthe training processes and guidelines provided;\n**(ii)**\nthe support services, such as mental health services, available to the employee; and\n**(iii)**\nif training or support services differ by factors such as geographic region, languages spoken, or direct-hire versus contracted employees, descriptions and breakdowns of such differences.\n**(2) Automated content detection and decision-making processes**\nIf the covered platform elects to use algorithmic processes to detect content for additional manual review or automated decision-making for content moderation, information on such processes, including\u2014\n**(A)**\nperformance metrics that are monitored to ensure consistent behavior for such processes across languages and the languages that are monitored; and\n**(B)**\nother safeguards in place to ensure consistent behavior of such systems across languages.\n**(3) Monetization across languages**\nThe list of languages in which the covered platform engages in monetization practices and the percentage breakdown by language of the covered platform's revenue throughout the duration of the relevant reporting period.\n**(4) In-language review**\nOf all content that is manually reviewed by staff, provide information on content that is reviewed in the original language used to create the content rather than being subject to automated translation before review, including\u2014\n**(A)**\nthe percentage of content reviewed in the original language for each language in which the covered platform engages in monetization practices; and\n**(B)**\na description of the policies governing whether and to what extent content will be manually reviewed in the original language or automatically translated prior to manual review.\n**(5) Translation and review processes**\nWith respect to the content review practices of the covered platform\u2014\n**(A)**\nthe list of languages in which content is reviewed without translation; and\n**(B)**\nfor languages in which automated translation is applied prior to manual review, a description of\u2014\n**(i)**\nthe process by which content is translated; and\n**(ii)**\nthe process by which that content is reviewed and how, if at all, that process differs from the process used to review content in the original language.\n**(6) Content moderation outcome measures**\n**(A) Number of content takedowns**\nThe number of content takedowns over the relevant reporting period for each language in which the covered platform engages in monetization practices.\n**(B) Response time**\nThe average response time to user-initiated takedown or content review requests over the relevant reporting period for each language in which the covered platform engages in monetization practices.\n**(7) Additional information**\nOther information determined appropriate by the Commission, including additional categories or criteria relevant to the information described in paragraphs (1), (2), and (4).\n#### 5. Consistent access to tools and documentation\nThe operator of a covered platform shall\u2014\n**(1)**\nprovide that all user tools for reporting content for review or automated action are accessible across all languages in which the covered platform offers its service; and\n**(2)**\npost all platform policies and other information concerning acceptable use of the covered platform in the same manner for all languages in which the platform offers its service.\n#### 6. Advisory Group\n##### (a) Establishment\nNot later than 360 days after the date of enactment of this Act, the Commission shall establish a group to be known as the Advisory Group on Language-Sensitive Technologies (referred to in this section as the Advisory Group ).\n##### (b) Duties\n**(1) In general**\nThe Advisory Group shall provide consensus advice and guidance to the Commission on best practices for private enterprises or public entities using covered technology that may have different performance outcomes depending on the underlying language of the content being analyzed in order to ensure the nondiscriminatory application of such technology.\n**(2) Covered technology**\nFor purposes of paragraph (1), the term covered technology means technology used to\u2014\n**(A)**\ndetect and process input language from sources, such as analog text and audio, into a machine-readable format, such as speech and optical character recognition;\n**(B)**\nprocess or generate language stored in a machine-readable format, such as natural language processing, including large language models;\n**(C)**\ndetect and process images and videos into a machine-readable format, or process images or videos stored in a machine-readable format; and\n**(D)**\nmake automated decisions related to content removal, ranking, or presentation to a user of an online platform.\n**(3) Membership**\nThe Commission shall appoint the members of the Advisory Group. In making such appointments, the Commission shall provide that the membership of the Advisory Group\u2014\n**(A)**\nincludes different points of view and background experience; and\n**(B)**\nincludes both Federal employees and non-Federal employee stakeholders, including representatives of communities most impacted by the systemic risks of harmful non-English language content and current or former content moderators and employees of covered platforms.\n**(4) Report**\nThe Commission shall make available on its website the findings of the Advisory Group with recommendations and best practices as reported by the Advisory Group concerning the use of covered technology.\n##### (c) Non-Applicability of the Federal Advisory Committee Act\nChapter 10 of title 5, United States Code, shall not apply to the Advisory Group.\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Advisory Group such sums as are necessary to carry out the requirements of this section.\n#### 7. Enforcement\n##### (a) Enforcement by the Federal Trade Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 3, 4, or 5 shall be treated as a violation of a rule defining an unfair or a deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of Commission**\n**(A) In general**\nThe Commission shall enforce this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates section 3, 4, or 5 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Federal Trade Commission under any other provision of law.\n##### (b) Enforcement by States\n**(1) In general**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any person subject to section 3 or 5 in a practice that violates such section, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States\u2014\n**(A)**\nto enjoin further violation of such section by such person;\n**(B)**\nto compel compliance with such section; and\n**(C)**\nto obtain damages, restitution, or other compensation on behalf of such residents.\n**(2) Scope of jurisdiction**\nThe attorney general of a State may not bring a civil action under this subsection against a person for a violation of section 3 or 5 if the Commission would not be able to bring an enforcement action against the person for such violation under subsection (a) because the person is exempt from coverage under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(3) Rights of Federal Trade Commission**\n**(A) Notice to Federal Trade Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) before initiating the civil action.\n**(ii) Contents**\nThe notification required by clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by Federal Trade Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal.\n**(4) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(5) Preemptive action by Federal Trade Commission**\nIf the Commission institutes a civil action or an administrative action with respect to a violation of section 3 or 5, the attorney general of a State may not, during the pendency of such action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission for the violation with respect to which the Commission instituted such action.\n**(6) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n**(7) Actions by other State officials**\n**(A) In general**\nIn addition to civil actions brought by attorneys general under paragraph (1), any other consumer protection officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n#### 8. Regulations\n##### (a) In general\nThe Commission shall, pursuant to section 553 of title 5, United States Code, promulgate\u2014\n**(1)**\nregulations to carry out the provisions of sections 3 and 4; and\n**(2)**\nsuch other regulations as the Commission determines necessary to carry out the provisions of this Act.\n##### (b) Timing\nThe Commission shall begin the rulemaking process for promulgating regulations to carry out the provisions of sections 3 and 4 not later than 120 days after the date of enactment of this Act.\n#### 9. Effective dates\nThe requirements of sections 3 and 4 shall take effect 120 days after the promulgation by the Commission of regulations to carry out such sections, and the requirements of section 5 shall take effect 120 days after the date of enactment of this Act.\n#### 10. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered platform**\nThe term covered platform means a website, internet application, or mobile internet application that\u2014\n**(A)**\nallows users to create, share, view, or search for and access user-generated or third-party content, including a social media platform, online search engine, and a service with direct or group messaging capabilities; and\n**(B)**\nhas had at least 10,000,000 monthly active users for 3 or more of the past 12 months within the United States.\n**(3) Monetization practices**\nThe term monetization practices means any avenues through which a covered platform might garner revenue, including accepting monetary, in-kind, or other compensation\u2014\n**(A)**\nin exchange for displaying or amplifying specific content; or\n**(B)**\nfrom businesses or other entities to utilize the covered platform as a means to find, charge, or communicate with customers.\n**(4) Platform policies**\nThe term platform policies means any terms, conditions, and clauses, regardless of their name or form, which govern the contractual relationship between a covered platform and a user, or any community guidelines that a covered platform maintains that govern conduct on the covered platform.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-20T15:13:37Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3540is.xml"
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
      "title": "LISTOS Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-17T06:23:43Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "LISTOS Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:41Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Language-Inclusive Support and Transparency for Online Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-17T06:23:41Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that large online platforms are addressing the needs of non-English users.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-17T06:18:42Z"
    }
  ]
}
```
