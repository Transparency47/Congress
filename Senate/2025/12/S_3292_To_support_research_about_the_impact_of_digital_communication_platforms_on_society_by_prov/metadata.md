# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3292?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3292
- Title: Platform Accountability and Transparency Act
- Congress: 119
- Bill type: S
- Bill number: 3292
- Origin chamber: Senate
- Introduced date: 2025-12-01
- Update date: 2026-01-09T12:03:23Z
- Update date including text: 2026-01-09T12:03:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-01: Introduced in Senate
- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-12-01: Introduced in Senate

## Actions

- 2025-12-01 - IntroReferral: Introduced in Senate
- 2025-12-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-01",
    "latestAction": {
      "actionDate": "2025-12-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3292",
    "number": "3292",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "Platform Accountability and Transparency Act",
    "type": "S",
    "updateDate": "2026-01-09T12:03:23Z",
    "updateDateIncludingText": "2026-01-09T12:03:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
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
      "actionDate": "2025-12-01",
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
            "date": "2025-12-01T23:30:06Z",
            "name": "Referred To"
          },
          {
            "date": "2025-12-01T23:30:06Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "LA"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-01-08",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3292is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3292\nIN THE SENATE OF THE UNITED STATES\nDecember 1, 2025 Mr. Coons (for himself and Mr. Cassidy ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo support research about the impact of digital communication platforms on society by providing privacy-protected, secure pathways for independent research on data held by large internet companies.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Platform Accountability and Transparency Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. Qualified research projects, qualified researchers, and qualified data and information.\nSec. 4. Obligations and immunity for platforms.\nSec. 5. Obligations and immunity for qualified researchers.\nSec. 6. Reporting.\nSec. 7. Enforcement.\nSec. 8. Establishing a safe harbor for research on platforms.\nSec. 9. Rulemaking authority.\nSec. 10. Authorization of appropriations.\nSec. 11. Severability.\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) NSF**\nThe term NSF means the National Science Foundation.\n**(3) Personal information**\nThe term personal information means any information, regardless of how the information is collected, inferred, or obtained that is linked or reasonably linkable to a specific consumer or consumer device.\n**(4) Platform**\nThe term platform means any entity subject to the jurisdiction of the Commission under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ) that\u2014\n**(A)**\noperates a website, desktop application, augmented or virtual reality application, or mobile application that\u2014\n**(i)**\npermits a person to become a registered user, establish an account, or create a profile for the purpose of allowing the user to create, share, and view user-generated content through such an account or profile;\n**(ii)**\nenables 1 or more users to generate content that can be viewed by other users of the platform; and\n**(iii)**\nprimarily serves as a medium for users to interact with content generated by other users of the platform and for the platform to deliver ads to users; and\n**(B)**\nhas at least 50,000,000 unique monthly users in the United States for a majority of the months in the most recent 12-month period.\n**(5) Qualified data and information**\n**(A) In general**\nSubject to subparagraph (B), the term qualified data and information means data and information from a platform\u2014\n**(i)**\nthat the NSF determines is necessary to allow a qualified researcher to carry out a qualified research project; and\n**(ii)**\nthat\u2014\n**(I)**\nis feasible for the platform to provide;\n**(II)**\nis proportionate to the needs of the qualified researchers to complete the qualified research project;\n**(III)**\nwill not cause the platform undue burden in providing the data and information to the qualified researcher; and\n**(IV)**\nwould not be otherwise available to the qualified researcher.\n**(B) Exclusions**\nSuch term does not include any of the following:\n**(i)**\nDirect and private messages between users.\n**(ii)**\nBiometric information, such as a fingerprint, voiceprint, eye retinas, irises, or other unique biological patters or characteristics.\n**(iii)**\nPrecise geospatial information.\n**(6) Qualified researcher**\n**(A) In general**\nSubject to subparagraph (B), the term qualified researcher means a researcher affiliated with a United States university or a United States nonprofit organization (as described in section 501(c) of the Internal Revenue Code of 1986) that is specifically identified in a research proposal that is approved as a qualified research project pursuant to section 3.\n**(B) Exclusion**\nSuch term does not include a researcher who is affiliated with a Federal, State, local, or tribal law enforcement or intelligence agency.\n**(7) Qualified research project**\nThe term qualified research project means a research plan that has been approved pursuant to section 3.\n**(8) State**\nThe term State means each of the 50 States of the United States, the District of Columbia, Puerto Rico, the Virgin Islands, American Samoa, Guam, and the Northern Mariana Islands.\n**(9) User**\nThe term user means a person that uses a platform for any purpose, including advertisers and sellers, regardless of whether that person has an account or is otherwise registered with the platform.\n#### 3. Qualified research projects, qualified researchers, and qualified data and information\n##### (a) Establishment\nNot later than 1 year after the date of enactment of this Act, the NSF shall establish, in consultation with the Commission, a research program to review research applications for approval as qualified research projects.\n##### (b) Research program requirements\nThe research program established by the NSF and the Commission under this section shall\u2014\n**(1)**\nprovide that the NSF shall\u2014\n**(A)**\nestablish a process to solicit research applications in order to identify qualified research projects;\n**(B)**\nreview research applications for scientific merit;\n**(C)**\nensure research applications identify proposed qualified researchers;\n**(D)**\npublish guidelines and criteria to be used by the NSF in determining how it will review research applications seeking approval to be a qualified research project;\n**(E)**\nidentify, in consultation with the Commission, what data and information in a platform\u2019s possession will be qualified data and information for the purposes of carrying out a qualified research project;\n**(F)**\nensure that approved research applications do not request data described in section 2(6)(B); and\n**(G)**\nprescribe and publish guidelines and criteria, in consultation with the Commission, used to determine how the NSF and Commission will identify qualified data and information necessary to conduct a qualified research project;\n**(2)**\nprovide that the Commission shall\u2014\n**(A)**\nreview research applications for privacy and cybersecurity risks;\n**(B)**\nfor each qualified research project, establish appropriate privacy and cybersecurity safeguards that a platform must implement in the provision of, and with which qualified researchers must comply to access, qualified data and information that a platform is required to share with qualified researchers pursuant to a qualified research project, and such safeguards\u2014\n**(i)**\nmust account for the relative sensitivity of the qualified data and information involved and be sufficient to protect such data and information; and\n**(ii)**\nmay include alternative protections, as appropriate and in consideration of the aims of the qualified research project, including\u2014\n**(I)**\nencryption of the data in transit and when not in use;\n**(II)**\ndelivery of the data in a format that employs methods to prevent qualified researchers from identifying individuals in the dataset;\n**(III)**\ndata access logs; and\n**(IV)**\nkeystroke logs;\n**(C)**\nin the case of each qualified research project, consider whether to require the platform to provide a secure physical or virtual environment to facilitate delivery of the qualified data and information;\n**(D)**\nestablish appropriate privacy and cybersecurity safeguards that a qualified researcher must implement when receiving, storing, or analyzing qualified data and information or generating new data using such qualified data and information, including inferential data based on such qualified data and information, and such safeguards may include a requirement that a qualified researcher delete qualified data and information after completion of a qualified research project, however any such safeguard must provide the qualified researcher the ability to retain enough information about the qualified data and information to allow the researcher or their peers to recreate the qualified research project upon request to, and approval from, the NSF and Commission pursuant to this section;\n**(E)**\npublish a list of criteria for determining the privacy and cybersecurity safeguards required for qualified data and information related to a qualified research project;\n**(F)**\nprovide a platform that is the subject of a qualified research project with the opportunity to provide comment about the privacy and cybersecurity safeguards required for the qualified research project;\n**(G)**\nprovide researchers with the opportunity to provide comment about the privacy and cybersecurity safeguards required for a qualified research project;\n**(H)**\nestablish a process to ensure that qualified researchers will be able to comply with any such privacy and cybersecurity safeguards; and\n**(I)**\npublish a list of criteria for determining whether qualified researchers will be able to comply with any such privacy and cybersecurity safeguards;\n**(3)**\nprovide that a research application may not be denied on grounds of the race, color, age, sex, national origin, political affiliation, or disability of the researcher;\n**(4)**\nprovide that a research application shall not be approved as a qualified research project unless it\u2014\n**(A)**\nhas been approved by an institutional review board;\n**(B)**\nhas been deemed exempt from institutional review board review; or\n**(C)**\nis excluded from the criteria for institutional review board review;\n**(5)**\nprovide a platform the opportunity to comment on and appeal to the NSF and the Commission the approval of a qualified research project for which the platform is required to provide qualified data and information to qualified researcher the grounds that\u2014\n**(A)**\nthe platform cannot provide the qualified data and information;\n**(B)**\nproviding access to the qualified data and information would lead to significant vulnerabilities in the security of the platform\u2019s service or user privacy; or\n**(C)**\nthe privacy and cybersecurity safeguards established by the Commission are not sufficient to protect the qualified data and information; and\n**(6)**\nrequire that any analysis by a qualified researcher derived from a qualified research project that the qualified researcher intends to publish undergo prepublication review by the Commission to ensure that the analysis does not expose personal information, or trade secrets.\n##### (c) Qualified researcher capacity\nA qualified research project may not proceed unless the proposed qualified researchers can demonstrate that they have the capacity to comply with the privacy and cybersecurity safeguards established for the qualified research project.\n##### (d) Aim of project\nA research application shall not be approved as a qualified research project unless it is in the public interest, aims to study activity on a platform, and is used for noncommercial purposes.\n##### (e) No judicial review\nA determination by the Commission or the NSF under this section regarding whether a research application will be deemed a qualified research project shall not be subject to judicial review.\n##### (f) No government access\nIf a platform provides qualified data and information to a qualified researcher, no government entity may seek access to such qualified data and information from the qualified researcher.\n##### (g) Researcher consortia\nThe Commission and NSF shall establish procedures and necessary safeguards under this section that allow for consortia of researchers to apply to seek data for the purpose of conducting a series of qualified research projects.\n#### 4. Obligations and immunity for platforms\n##### (a) Provision of qualified data and information\nA platform shall provide access to qualified data and information relating to a qualified research project to a qualified researcher under the terms and privacy and cybersecurity safeguards dictated by the Commission pursuant to section 3 for the purpose of carrying out the qualified research project.\n##### (b) Continued access to qualified data and information\n**(1) In general**\nA platform may not restrict or terminate a qualified researcher\u2019s access to qualified data and information for an ongoing qualified research project unless the platform has a reasonable belief that the qualified researcher is not acting in accordance with the cybersecurity and privacy safeguards required for the qualified research project pursuant to section 3.\n**(2) Notice and review of change to access**\nIf a platform restricts or terminates a qualified researcher's access to qualified data and information for an ongoing qualified research project\u2014\n**(A)**\nthe platform shall, within a reasonable time (as established by the Commission), inform the Commission in writing that the platform has restricted or terminated the qualified researcher's access to the qualified data and information; and\n**(B)**\nthe Commission shall promptly review the platform's decision and determine whether the qualified researcher has violated the privacy and cybersecurity safeguards established for the qualified research project.\n##### (c) Notice to platform users\nThe Commission shall issue regulations requiring that platforms, through posting of notices or other appropriate means, keep users informed of their privacy protections and the information that the platform is required to share with qualified researchers under this Act.\n##### (d) Safe harbor\nNo cause of action under State or Federal law arising solely from the release of qualified data and information to qualified researchers in furtherance of a qualified research project may be brought against any platform that complies with the Act.\n##### (e) Right of review\nIf a platform fails to provide all of the qualified data and information required under the terms of a qualified research project to the qualified researcher conducting the project, the qualified researcher or the researcher's affiliated university or non-profit organization may bring an action in district court for injunctive relief or petition the Commission to bring an enforcement action against the platform.\n##### (f) Security\nNothing in this Act shall be construed to restrict a platform\u2019s ability to\u2014\n**(1)**\ntake immediate steps to protect an interest that is essential for the life or physical safety of a natural person; or\n**(2)**\nrespond to security incidents, identity theft, fraud, harassment, malicious or deceptive activities, or illegal activity, preserve the integrity of security of systems, or investigate or report those responsible for such actions.\n#### 5. Obligations and immunity for qualified researchers\n##### (a) Scope of permitted use of qualified data and information\nEach qualified researcher who accesses qualified data and information shall use the qualified data and information\u2014\n**(1)**\nonly for the purposes of conducting research authorized under the terms of the qualified research project involved; and\n**(2)**\nin accordance with the privacy and cybersecurity safeguards prescribed by the Commission for the qualified research project.\n##### (b) Protection of personal information\nA qualified researcher that is provided access to qualified data and information for purposes of a qualified research project may not\u2014\n**(1)**\nattempt to reidentify, disclose, publish, or use for commercial purpose personal information derived from such qualified data and information; or\n**(2)**\ndisclose such qualified data and information to a third party for any reason.\n##### (c) Effect of violation of information and privacy standards\nQualified researchers who intentionally, recklessly, or negligently violate the privacy and cybersecurity safeguards prescribed by the Commission for a qualified research project may be subject to both civil and criminal enforcement, under applicable Federal, State, and local laws. The Commission may refer any such violation to the Department of Justice or the appropriate State law enforcement agency.\n#### 6. Reporting\nNot later than 24 months after the date of enactment of this Act, and annually thereafter, the NSF and the Commission shall submit to the Congress a joint report regarding the operation of this Act, which shall include a detailed statement of all qualified research projects, including with respect to each such project:\n**(1)**\nThe identity of any authorized qualified researcher and the institution the researcher is affiliated with.\n**(2)**\nThe platforms required to provide qualified data and information to qualified researchers.\n**(3)**\nThe categories of qualified data and information each platform was required to provide.\n**(4)**\nThe terms of the privacy and cybersecurity safeguards prescribed by the Commission to ensure the security of the qualified data and information.\n**(5)**\nAny recommendations for improvements to the operation of this Act in order to facilitate its aim of providing enhanced platform transparency.\n#### 7. Enforcement\n##### (a) Unfair or deceptive act or practice\n**(1) In general**\nA platform's failure to comply with subsection (a) or (b) of section 4, or a qualified researcher's failure to comply with subsection (a) or (b) of section 5, shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce the provisions of this Act specified in paragraph (1) in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person that violates the provisions of this Act specified in paragraph (1) shall be subject to the penalties, and entitled to the privileges and immunities, provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Rule of construction**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (b) Regulations\nThe Commission shall have the authority to promulgate, in the manner prescribed by 5 U.S.C. 553 , such rules and regulations as it may deem necessary to carry out its responsibilities under this Act.\n##### (c) Attorney's fees and other costs\nIn the event any enforcement action is appealed, the prevailing party in the action may, in the discretion of the court, recover the costs of the action including reasonable investigative costs and attorneys' fees.\n#### 8. Establishing a safe harbor for research on platforms\n##### (a) Definitions\nIn this section:\n**(1) Covered information**\nThe term covered information means\u2014\n**(A)**\npublicly available information, including publicly available information recommended, targeted, or otherwise amplified or de-amplified to an individual or research account; and\n**(B)**\ninformation about advertisements shown on the platform.\n**(2) Covered method of digital investigation**\nThe term covered method of digital investigation means\u2014\n**(A)**\nthe collection of information from a platform\u2019s user-facing interface, including by navigating the interface or the use of a browser extension or plug-in to collect information from the interface, through automated means; and\n**(B)**\nthe creation or use of research accounts, including accounts designed to observe information that is recommended, targeted, amplified, or de-amplified to minors.\n**(3) Journalism**\nThe term journalism includes the gathering, preparing, collecting, photographing, recording, writing, editing, reporting, or investigating news or information that concerns local, national, or international events or other matters of public concern for dissemination to the public.\n**(4) Publicly available information**\n**(A) In general**\nThe term publicly available information means any information that a person has a reasonable basis to believe has been lawfully made available to the general public.\n**(B) Limitations**\nThe term publicly available information does not include any of the following:\n**(i)**\nAny obscene visual depiction (as such term is used in section 1460 of title 18, United States Code).\n**(ii)**\nBiometric information.\n**(iii)**\nGenetic information.\n**(iv)**\nIntimate images, authentic or generated by a computer or by artificial intelligence, known to be nonconsensual.\n**(5) Reasonable measures to protect individual privacy**\nThe term reasonable measures to protect individual privacy includes reasonable measures to\u2014\n**(A)**\navoid the collection and retention of publicly available information that would readily identify an individual, alone or in combination with other information, that is extraneous to the research or journalism project;\n**(B)**\nprevent the theft and accidental disclosure of any information collected;\n**(C)**\nensure that the relevant information is not used for any purpose other than the purpose of informing the general public about matters of public concern; and\n**(D)**\nrestrict the publication or other disclosure of any information that would readily identify an individual, alone or in combination with other information, except if such individual is\u2014\n**(i)**\nan advertiser and the information concerns an advertisement;\n**(ii)**\na public official, candidate for public office, or public figure; or\n**(iii)**\nan adult and the individual has provided consent that is freely given, specific, informed, and express to the publication or disclosure.\n**(6) Research account**\nThe term research account means an account on a platform that is created and used solely\u2014\n**(A)**\nfor the purpose of a journalism or research project on the platform; and\n**(B)**\nfor no longer than is necessary to complete such project.\n##### (b) Safe harbor\n**(1) In general**\nNo cause of action may be brought or maintained by a platform, or by the owner or operator of a platform, in any proceeding against any person for collecting covered information, as part of a journalism or research project on the platform, notwithstanding that such collection may violate the terms of service of the platform, if\u2014\n**(A)**\nthe information is collected through a covered method of digital investigation;\n**(B)**\nthe purpose of the project is to inform the general public about matters of public concern; and\n**(C)**\nwith respect to any such information collected\u2014\n**(i)**\nthe information is not used, retained, disclosed, or transferred for any purpose other than the purpose described in subparagraph (B); and\n**(ii)**\nthe person who collects the information takes reasonable measures to protect individual privacy.\n**(2) Clarification**\nA person shall not be considered to be accessing without authorization or exceeding the authorized access of a platform solely based on the collection of covered information on the platform through a covered method of digital investigation that complies with the conditions of this section.\n**(3) Rule of construction**\nParagraph (1) shall not be construed to protect the collection of covered information to train a large language model.\n##### (c) Rulemaking\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary of Commerce shall issue regulations to further clarify the terms defined in subsection (a) and ensure that\u2014\n**(A)**\nwith respect to the use of research accounts, reasonable measures have been taken to avoid misleading individuals on a platform; and\n**(B)**\nreasonable measures have been taken to avoid materially burdening the technical operation of the platform.\n**(2) Exception**\nA regulation issued under this subsection may not further define the term journalism as defined under paragraph (3) of subsection (a) or the phrase matters of public concern as used in this section.\n##### (d) Rule of construction\nThis section shall not be construed to create or expand liability under any law for any person.\n##### (e) Prohibition against compelled disclosure to government entities\nA person who otherwise establishes entitlement to the safe harbor described in subsection (b) may not be required (by a subpoena, court order, or otherwise) to divulge to a department or agency of the United States or any State or political subdivision thereof in furtherance of an investigation or legal process about an individual any information related to such individual obtained from a platform under this section.\n#### 9. Rulemaking authority\n##### (a) Additional reporting requirements\n**(1) In general**\nIn consultation with the NSF, the Commission may, in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations that require platforms to make available to qualified researchers data, metrics, or other information that the Commission determines will facilitate independent research in the public interest into activity on platforms.\n**(2) Factors**\nIn exercising its authority under this subsection, the Commission shall consider the extent to which disclosures under this subsection may facilitate collaboration amongst qualified researchers and alleviate burdens on platforms and qualified researchers as compared to qualified research projects conducted pursuant to section 3.\n**(3) Form and frequency; retention of information**\nThe Commission shall specify in the regulations the required form and frequency of reporting or disclosures, as well as how long data, metrics, or other information should be retained and made available. It may require the information be provided in a form that is accessible for analysis by qualified researchers, such as through an application programming interface.\n**(4) Consultation**\nThe Commission shall further consult with the National Institutes of Health and other relevant government agencies, as appropriate, in exercising its authority under this subsection.\n**(5) Applicability of prior sections**\nFor data made available to qualified researchers under this section, the Commission shall establish privacy and cybersecurity safeguards applicable to platforms and qualified researchers in the manner described in section 3 for data made available under that section. The obligations and immunities for platforms and qualified researchers described in sections 4 and 5 shall apply to data disclosed to qualified researchers under this section, and the provisions of section 7 may be invoked to enforce this section.\n##### (b) Transparency of certain content and user accounts\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Commission shall, in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations to require platforms to make available to the public on an ongoing basis, in a specific section of their online interface, through a searchable and reliable tool that allows multicriteria queries and through application programming interfaces, a repository containing information regarding reasonably public content on the platform that\u2014\n**(A)**\nhas been highly disseminated; or\n**(B)**\nwas originated or spread by major public accounts.\n**(2) Disclosure of public content samplings**\nThe regulations issued under paragraph (1) shall further require platforms to disclose on an ongoing basis statistically representative samplings of reasonably public content, including, at a minimum, a sampling that is weighted by the number of impressions the content receives.\n**(3) Required information**\nThe information required to be disclosed about content described in paragraphs (1) and (2) shall include, as appropriate\u2014\n**(A)**\nthe user-generated content itself, including any text, images, videos, links, and keywords;\n**(B)**\nplatform-generated content displayed in connection with the user-generated content, including any dates, labels, disclaimers, or metrics;\n**(C)**\nmetrics about the extent of dissemination of or engagement with the content, including the number of impressions, reach, and engagements;\n**(D)**\ninformation about the extent to which the content was recommended, amplified, or restricted by platform algorithms or policies;\n**(E)**\nreasonably public information about the user accounts responsible for the content; and\n**(F)**\npublic uniform resource locators that uniquely link to the content and identify related materials such as the parent content, replying content, and cross-posted content.\n**(4) Highly disseminated content**\nAs part of the regulations issued under paragraph (1), the Commission shall define highly disseminated according to metrics that the Commission deems appropriate (which may include engagement, views, reach, impressions, or other metrics), provided that a piece of content must have been viewed by at least 10,000 unique users to qualify.\n**(5) Major public accounts**\nAs part of the regulations issued under paragraph (1), the Commission shall define major public accounts as it deems appropriate, provided that, at a minimum, major public accounts are restricted to reasonably public accounts whose content is followed by at least 25,000 users or otherwise regularly reaches at least 25,000 users per month.\n**(6) Treatment of content that has been removed**\nThe regulations described in paragraph (1) shall provide guidance regarding disclosure of content that is removed by the user or platform subsequent to its dissemination.\n**(7) Frequency**\nTo the extent practicable, the Commission shall require this information to be updated so as to provide a real-time understanding of the content described in paragraphs (1) and (2).\n##### (c) Transparency of advertising\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Commission shall, in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations to require platforms to disclose on an ongoing basis information regarding advertising on the platform. These regulations shall require platforms to compile and disclose publicly in a specific section of their online interface, through a searchable and reliable tool that allows multicriteria queries and through application programming interfaces, a repository containing the information referred to in paragraph (2), for the entire period during which they present an advertisement and until 1 year after the advertisement was presented for the last time on their online interfaces. Platforms shall ensure that the repository does not contain any personal information of the recipients of the service to whom the advertisement was or could have been presented.\n**(2) Information required**\nThe information required to be included in the repository required under paragraph (1) shall include at least all of the following information:\n**(A)**\nThe content of the advertisement, including the name of the product, service, or brand, and the subject matter of the advertisement.\n**(B)**\nThe natural or legal person on whose behalf the advertisement is presented.\n**(C)**\nThe natural or legal person who paid for the advertisement, if that person is different from the person referred to in subparagraph (B).\n**(D)**\nThe period during which the advertisement was presented.\n**(E)**\nWhether the advertisement was intended to be presented specifically to 1 or more particular groups of recipients of the service and if so, the main parameters used for that purpose including where applicable the main parameters used to exclude 1 or more of such particular groups.\n**(F)**\nThe total number of recipients of the service reached and, where applicable, aggregate numbers broken down by group or groups of recipients that the advertisement specifically targeted.\n**(G)**\nInformation about the extent to which the advertisement was recommended, amplified, or restricted by platform algorithms or policies.\n**(3) Treatment of removed ads**\nThe regulations described in paragraph (1) shall provide guidance regarding disclosure of ads that are removed by the user or platform subsequent to its dissemination.\n**(4) Frequency**\nTo the extent practicable, the Commission shall require this information to be updated so as to provide a real-time understanding of the content described in paragraph (2).\n##### (d) Transparency of algorithms and company metrics and data\n**(1) In general**\nNot later than 1 year after enactment of this Act, the Commission shall, in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations to require platforms to report publicly on their use of recommender or ranking algorithms and metrics.\n**(2) Required information**\nThe reporting required under paragraph (1) shall be at least semiannual and include, as appropriate\u2014\n**(A)**\na description of all consumer-facing product features that made use of recommender or ranking algorithms during the reporting period;\n**(B)**\na summary of signals used as inputs to the described recommender or ranking algorithms, including an explanation of which rely on user data, an explanation of the types of user data relied upon, and ranked based on the significance of their impact on the algorithms\u2019 outputs;\n**(C)**\na summary of the processes or predictions used by the platform to assess the signals incorporated into the recommender or ranking algorithm and to score or rank content (such as predictions of future user engagement), ranked based on the significance of their impact on the algorithms\u2019 outputs;\n**(D)**\na summary of the optimization objectives of the described recommender or ranking algorithms;\n**(E)**\na summary of metrics calculated by the platform to assess product changes or new features, or as a basis to assess performance or calculate employee or executive compensation, with an assessment of their relative importance in company decision making;\n**(F)**\nsignificant changes during the reporting period from the last report; and\n**(G)**\nother information about the recommender or ranking algorithms that the Commission deems appropriate.\n**(3) Implementation**\nIn implementing this section, the Commission shall ensure that the reporting is useful and actionable while ensuring that platforms are not required to disclose trade secrets.\n##### (e) Transparency of content moderation and violating content\n**(1) In general**\nNot later than 1 year after the date of enactment of this Act, the Commission shall, in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations to require platforms to issue a public report on an ongoing basis information regarding content moderation and content violating platform policies.\n**(2) Required information**\nThe information required to be disclosed under paragraph (1) shall include, as appropriate\u2014\n**(A)**\nstatistics regarding the amount of content that the platform determined violated its policies, broken down by\u2014\n**(i)**\nthe violated policy;\n**(ii)**\nthe action taken in response to the violation;\n**(iii)**\nthe methods the platform used to identify the violating content (such as artificial intelligence, user report, human moderator review, or other means);\n**(iv)**\nthe extent to which the content was recommended, amplified, or restricted by platform algorithms or policies; and\n**(v)**\ngeographic and demographic factors as the Commission deems appropriate;\n**(B)**\nstatistics regarding the number of times violating content was viewed by users and the number of users who viewed it;\n**(C)**\nestimates by the platform about the prevalence of violating content (including as measured by the number of impressions of violating content), broken down by\u2014\n**(i)**\nthe violated policy;\n**(ii)**\ngeographic and demographic factors; and\n**(iii)**\nother factors the Commission deems appropriate; and\n**(D)**\nthe number of orders received from governmental authorities, categorized by the type of violating content concerned, and the average time needed for taking the action specified in those orders.\n##### (f) Data dictionaries\nNot later than 1 year after the date of enactment of this Act, the Commission shall, in consultation with the NSF and in accordance with section 553 of title 5, United States Code, and subject to subsection (g), issue regulations to require platforms to disclose, and update periodically, data dictionaries to inform and facilitate researcher data access requests. Such data dictionaries shall include descriptions of significant datasets in the platform\u2019s possession relating to content on, or users of, the platform, enforcement of content policy, or advertising, as necessary or appropriate to inform and facilitate researcher data access requests.\n##### (g) Privacy, confidentiality, and platform integrity\nThe Commission shall ensure that any reporting or disclosures required pursuant to this section do not infringe upon reasonable expectations of personal privacy of users of platforms or of other persons, or require dissemination of trade secrets. If necessary, the Commission may require withholding of information otherwise required to be disclosed to meet this requirement. The Commission shall further consider the effect of disclosures on risks to platform integrity or the susceptibility of the platform to manipulation or inauthentic behavior, and may limit or reduce the information required to be disclosed if necessary to address a substantial such risk.\n##### (h) Variation\nIn implementing this section, the Commission may vary the requirements it imposes on platforms based on the size of the platform and scope of its services.\n##### (i) Definitions\nIn this section:\n**(1) Engagement**\nThe term engagement means, with respect to content on a platform, the number of times a user interacts with the content, whether through comments, indications of approval or disapproval (such as likes or dislikes), reshares, or any other form of active interaction.\n**(2) Impression**\nThe term impression means, with respect to content on a platform, the display or delivery of the content to a user, regardless of whether the user engages with the content.\n**(3) Prevalence of violating content**\nThe term prevalence of violating content means a platform\u2019s estimate of the number of impressions of content that violates its moderation policies among its users, regardless of whether the platform ever identifies that particular content as violating.\n**(4) Reach**\nThe term reach means, with respect to content on a platform, the number of users to whom the content is displayed or delivered during a particular period, regardless of how many times it is delivered to them.\n**(5) Real-time understanding**\nThe term real-time understanding means an understanding of content on a platform that is up-to-date within less than 24 hours.\n**(6) Reasonably public**\nThe term reasonably public means information that the author made available in a manner and under such circumstances such that the author does not retain a reasonable expectation of privacy in the information. The fact that a user may need to register or create an account with a platform to view information does not preclude it from being deemed reasonably public.\n**(7) Recommender or ranking algorithm**\nThe term recommender or ranking algorithm means a fully or partially automated system used by a platform to suggest in its online interface specific information to recipients of the service offered by the platform, or to prioritize that information, including as a result of a search initiated by the recipient of the service or otherwise determining the relative order or prominence of information displayed. This includes any computational process, including one derived from machine learning or other artificial intelligence techniques, that processes personal information or other data for the purpose of determining the order or manner that a set of information is provided, recommended to, or withheld from a user of a platform, including the provision of commercial content, the display of social media posts, recommendations of user or group accounts to follow or associate with, or any other method of content selection, amplification, or restriction.\n#### 10. Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this Act for fiscal year 2026 and each succeeding fiscal year.\n#### 11. Severability\nIf any provision of this Act, or the application of such provision to any person or circumstance, is held to be unconstitutional, the remainder of this Act, and the application of the remaining provisions of this Act, to any person or circumstance, shall not be affected.",
      "versionDate": "2025-12-01",
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
        "updateDate": "2025-12-18T17:09:22Z"
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
      "date": "2025-12-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3292is.xml"
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
      "title": "Platform Accountability and Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Platform Accountability and Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T06:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support research about the impact of digital communication platforms on society by providing privacy-protected, secure pathways for independent research on data held by large internet companies.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T06:18:31Z"
    }
  ]
}
```
