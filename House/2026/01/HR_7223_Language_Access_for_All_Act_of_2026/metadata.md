# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7223?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7223
- Title: Language Access for All Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7223
- Origin chamber: House
- Introduced date: 2026-01-22
- Update date: 2026-05-14T08:07:29Z
- Update date including text: 2026-05-14T08:07:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-22: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-01-22: Introduced in House

## Actions

- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Introduced in House
- 2026-01-22 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-22",
    "latestAction": {
      "actionDate": "2026-01-22",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7223",
    "number": "7223",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001188",
        "district": "6",
        "firstName": "Grace",
        "fullName": "Rep. Meng, Grace [D-NY-6]",
        "lastName": "Meng",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Language Access for All Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-14T08:07:29Z",
    "updateDateIncludingText": "2026-05-14T08:07:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-01-22",
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
      "actionDate": "2026-01-22",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-01-22",
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
          "date": "2026-01-22T14:03:30Z",
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
      "bioguideId": "C001080",
      "district": "28",
      "firstName": "Judy",
      "fullName": "Rep. Chu, Judy [D-CA-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Chu",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "NY"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2026-01-22",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
    },
    {
      "bioguideId": "E000297",
      "district": "13",
      "firstName": "Adriano",
      "fullName": "Rep. Espaillat, Adriano [D-NY-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Espaillat",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "G000585",
      "district": "34",
      "firstName": "Jimmy",
      "fullName": "Rep. Gomez, Jimmy [D-CA-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gomez",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "TX"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "DC"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "NY"
    },
    {
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "IL"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MI"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "MI"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
      "state": "CA"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "CT"
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
      "sponsorshipDate": "2026-02-10",
      "state": "VA"
    },
    {
      "bioguideId": "S001159",
      "district": "10",
      "firstName": "Marilyn",
      "fullName": "Rep. Strickland, Marilyn [D-WA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Strickland",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "WA"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-02-10",
      "state": "HI"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "False",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "IN"
    },
    {
      "bioguideId": "F000468",
      "district": "7",
      "firstName": "Lizzie",
      "fullName": "Rep. Fletcher, Lizzie [D-TX-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Fletcher",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "TX"
    },
    {
      "bioguideId": "C001055",
      "district": "1",
      "firstName": "Ed",
      "fullName": "Rep. Case, Ed [D-HI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Case",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "HI"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "CA"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7223ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7223\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 22, 2026 Ms. Meng (for herself, Ms. Chu , Mr. Goldman of New York , and Mr. Vargas ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo improve access to Federal services by individuals with limited English proficiency, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Language Access for All Act of 2026 .\n#### 2. Improving access to Federal services by individuals with limited English proficiency\n##### (a) Ensuring meaningful access\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the head of each agency shall ensure that individuals with LEP can meaningfully access the federally conducted programs and activities of the agency, including by\u2014\n**(A)**\nconsistent with any applicable Language Access Technical Standards established by the agency under subsection (c)\u2014\n**(i)**\ntranslating each vital document or content created for the public into\u2014\n**(I)**\nany languages the agency frequently encounters; and\n**(II)**\nthe dominant languages spoken in the United States based on current U.S. Census data; and\n**(ii)**\nadding multilingual functionality to agency digital and information technology systems to identify and track the spoken and written language needs of people who engage with the agency and to provide documents and content in other languages;\n**(B)**\nproviding oral interpretation, sight translation, and telephonic or remote interpretation services to such individuals;\n**(C)**\nrecognizing, as an alternative to using qualified interpreters or translators, the use of demonstrably bilingual staff of the agency that have been assessed and are qualified to deliver accurate and effective communication as an appropriate method of providing language assistance;\n**(D)**\nacknowledging that, when qualified, such staff may offer service that is faster, more effective, and more cost-efficient than the use of qualified interpreters or translators;\n**(E)**\nnotifying the public of the availability of language assistance, including interpreters, translated documents and digital content, and bilingual staff, through the use of multilingual notices, taglines, signage or demonstrably equivalent alternatives included on documents and digital content the agency creates for the public and in agency buildings and offices; and\n**(F)**\ntraining employees of the agency who interact with the public on any policy or procedure established by the agency to implement the language access plan established by the agency under subsection (b).\n**(2) Public complaint and tracking system**\n**(A) Complaints**\nThe Attorney General shall establish and maintain a publicly accessible system for individuals to submit complaints to the Attorney General regarding barriers to receiving meaningful access, as described under paragraph (1), from an agency.\n**(B) Response**\nThe head of the agency with respect to which the complaint was made shall respond to each complaint that was made not later than 60 days after receipt of the complaint from the Attorney General.\n**(C) Reports**\nThe Attorney General shall publish on the website of the Department of Justice an annual report summarizing the complaints made under subparagraph (A), disaggregated by the agency that is the subject of the complaint, the language with respect to which the agency failed to provide access, and the program or activity to which the person is guaranteed meaningful access under paragraph (1).\n##### (b) Language access plan\n**(1) Establishment**\nNot later than 1 year after the date of the enactment of this Act, the head of each agency shall establish a language access plan to implement subsection (a) that\u2014\n**(A)**\nis practical and effective, readily implemented, and responsive to the particular circumstances and mission of the agency;\n**(B)**\nis consistent with the Language Access Technical Standards issued under subsection (c);\n**(C)**\nis consistent with the standards set forth\u2014\n**(i)**\nin the initial LEP Guidance of the agency;\n**(ii)**\nin the policy guidance document entitled Enforcement of Title VI of the Civil Rights Act of 1964\u2014National Origin Discrimination Against Persons With Limited English Proficiency 65 Fed. Reg. 50, 123 (Aug. 16, 2000); and\n**(iii)**\nin the Attorney General\u2019s memorandum to the heads of Department components issued on November 21, 2022, entitled Strengthening the Federal Government\u2019s Commitment to Language Access ;\n**(D)**\nidentifies which populations containing individuals with LEP are likely to seek access to the services and programs of the agency, including language populations that are emerging, have been historically isolated, are of lesser diffusion, and do not have a commonly used written format;\n**(E)**\ndescribes how multilingual communications will be meaningfully provided to the populations identified pursuant under subparagraph (D), including whether such communications will be provided through oral, visual, or community-based modes of communication as appropriate;\n**(F)**\nin the case that the agency provides assistance during emergency response situations (such as disasters, public health crises, and other urgent circumstances) specifies how multilingual communications will be meaningfully provided to such populations during such situations regardless of whether an official state of emergency has been declared; and\n**(G)**\nsets procedures for the agency with respect to monitoring, evaluating, and improving the performance of the agency in implementing the plan, including\u2014\n**(i)**\nregular assessments of the language access needs of the agency and the effectiveness of the language access provided by the agency;\n**(ii)**\nmeasurable performance indicators addressing timeliness, accuracy, and quality of language assistance services;\n**(iii)**\nmechanisms for collecting and reviewing data on service usage, complaints, and identified barriers;\n**(iv)**\nperiodic internal reviews conducted by the civil rights office of the agency; and\n**(v)**\nprocesses for corrective action and continuous improvement when deficiencies or gaps in meaningful access are identified.\n**(2) Notice and comment**\nThe head of each agency shall publish a proposal for the plan required to be established under paragraph (1) in the Federal Register for a 60-day public comment period to ensure that stakeholders, including individuals with LEP and organizations representing such individuals, have an adequate opportunity to provide input on how the head of such agency carries out the provisions of this Act.\n**(3) Federal Register**\nAfter considering any comments received during the period described under paragraph (2) with respect to plan published under such paragraph, the head of an agency shall\u2014\n**(A)**\nupdate such plan on the basis of such comments as the head of the agency determines appropriate; and\n**(B)**\npublish a finalized version of the plan in the Federal Register.\n**(4) Submission to the Attorney General and to congress**\nNot later than 30 days after the head of an agency establishes the language access plan required by paragraph (1), the head of such agency shall submit such plan to\u2014\n**(A)**\nthe Attorney General; and\n**(B)**\nthe Chair and Ranking Minority Member of\u2014\n**(i)**\nthe Committee on the Judiciary of the House of Representatives;\n**(ii)**\nthe Committee on the Judiciary of the Senate;\n**(iii)**\nthe Committee on Oversight and Government Reform of the House of Representatives; and\n**(iv)**\nthe Committee on Homeland Security and Governmental Affairs of the Senate.\n**(5) Central repository**\nThe Department of Justice shall establish and maintain a publicly available website with the domain name LEP.gov to serve as the central repository for each plan submitted to the Attorney General under paragraph (4)(A).\n##### (c) Language access technical standards\n**(1) Establishment of standard**\nNot later than 1 year after the date of the enactment of this Act, the head of each agency, in consultation with the Attorney General, the National Institute of Standards and Technology, and stakeholders and advocates from non-English-speaking communities, shall establish standards to be known as Language Access Technical Standards to\u2014\n**(A)**\nensure meaningful access to federally conducted programs and activities under subsection (a); and\n**(B)**\nbe used as a measure of progress to evaluate the effectiveness and accuracy of language access for federally conducted programs and activities carried out by each agency.\n**(2) General accessibility requirements**\nThe Language Access Technical Standards shall at a minimum, with respect to the systems and services of the agency\u2014\n**(A)**\nallow individuals with LEP to access any written content provided by the agency in the language of their choice among the agency\u2019s supported languages;\n**(B)**\nensure the functionality, quality, and timeliness of the system and services for all languages;\n**(C)**\nimplement user-friendly interfaces that account for varying literacy and digital skills; and\n**(D)**\nbe culturally determined.\n**(3) Undue burden exception**\n**(A) Written request**\nIn the case that the head of an agency determines that compliance with a specific requirement included in the Language Access Technical Standards established under this subsection would impose an undue burden on the agency, the head of the agency shall submit to the Attorney General a written request to waive such requirement for the agency that identifies\u2014\n**(i)**\nthe specific requirement that would impose such undue burden;\n**(ii)**\nthe nature of the burden; and\n**(iii)**\nany alternative to fulfilling the requirement and why each such alternative is not feasible.\n**(B) Attorney General review**\n**(i) In general**\nNot later than 30 days after receiving a request under subparagraph (A), the Attorney General shall grant or deny the request.\n**(ii) Determination criteria**\nIn determining whether to grant or deny a request under paragraph (2), the Attorney General an agency shall consider whether\u2014\n**(I)**\nindividuals with limited English proficiency are likely to interact with the agency; and\n**(II)**\na failure to provide meaningful language access is likely to result in significant harm, denial of benefits, or diminished civil rights protections.\n**(C) Expiration**\nA grant of a waiver under this subsection shall expire two years after such grant.\n**(D) Record**\nThe Attorney General shall maintain a publicly accessible record of all written requests received under subparagraph (A) in the central repository established under subsection (b)(5).\n**(4) Public participation and comment**\nBefore establishing Language Access Technical Standards, or updating any such standards, the head of an agency shall provide opportunity for public comment and engage communities representing individuals with LEP, including community and cultural organizations that work with individuals with LEP, and providers of professional language services.\n**(5) Updates**\nThe Language Access Technical Standards shall be reviewed at least once every 3 years, and updated as necessary following such review.\n**(6) Adoption**\nThe head of each agency shall certify compliance with the Language Access Technical Standards annually to the Attorney General.\n**(7) Scope**\nThe Language Access Technical Standards shall apply to all agency programs, activities, and communications, including\u2014\n**(A)**\nin-person, telephonic, and virtual interactions;\n**(B)**\npaper and digital content and documents;\n**(C)**\nwebsites, portals, and mobile applications; and\n**(D)**\nartificial intelligence-assisted and machine translation language assistance services, including automated translation, transcription, and interpretation technologies.\n##### (d) AI and automated language assistance services\n**(1) Limitation**\nThe head of an agency\u2014\n**(A)**\nmay not fully replace any qualified language assistance services of the agency with artificial intelligence or machine translation services; and\n**(B)**\nshall require a qualified human translator or interpreter to verify any use of such service or machine translation by the agency.\n**(2) Requirements**\nThe head of each agency shall ensure that any artificial intelligence-assisted language assistance services used by the agency\u2014\n**(A)**\ndo not replace any qualified translators and interpreters;\n**(B)**\npublicly disclose on an annual basis on www.LEP.gov data sources, limitations, confidence levels, and error rates of the service;\n**(C)**\ncomply with section 552a of title 5, United States Code (commonly referred to as the Privacy Act of 1974), the Federal Information Security Modernization Act of 2014, and the E\u2013Government Act of 2002, and protect personal and sensitive information from disclosure;\n**(D)**\nare tested to prevent discrimination based on language, culture, ethnicity, or other protected characteristics, with mitigation strategies documented;\n**(E)**\nare reviewed and validated by qualified translators and interpreters to ensure proper cultural context, idiomatic accuracy, and clarity of the translation or interpretation; and\n**(F)**\nare continuously monitored by the agency for performance, with errors reported and corrective actions for user-reported inaccuracies in translation and interpretation implemented.\n**(3) Best practices**\nNot later than 1 year after the date of the enactment of this Act, the Attorney General shall issue guidance on best practices for the use of artificial intelligence in language assistance services, including validation, monitoring, and accountability measures for such artificial intelligence.\n**(4) Audit requirement**\n**(A) In general**\nThe Inspector General of each agency shall conduct, at least once every two years after the date of the enactment of this Act, an audit of all artificial intelligence-assisted language systems to assess accuracy, fairness, cultural relevance, and compliance with the Language Access Technical Standards established under subsection (c).\n**(B) Report**\nAn Inspector General shall submit to the Attorney General a report on an audit conducted under subparagraph (A), not later than 90 days after such audit is completed.\n**(C) Public transparency**\nThe Attorney General shall make publicly available a summary of the report submitted under subparagraph (B).\n**(5) NIST**\nThe National Institute of Standards and Technology shall provide technical expertise, validation protocols, and standardization tools for artificial intelligence-assisted language assistance services.\n##### (e) Interagency coordination\n**(1) Interagency Language Access Standard Council**\nThe Administrator of General Services shall convene an Interagency Language Access Standards Council to coordinate updates, best practices, and research on emerging technologies.\n**(2) Language Access Working Group**\n**(A) In general**\nThere is established an Language Access Working Group to\u2014\n**(i)**\nserve as a central resource for providing support and technical assistance to agencies in implementing the language access plan of the agency; and\n**(ii)**\ndirectly engage with community groups, individuals with LEP, and other stakeholders to ensure adherence with this Act.\n**(B) Membership**\nThe members of the Group shall be comprised of one Language Access Coordinator from each agency and the Attorney General.\n**(C) Head of group**\nThe Attorney General shall serve as the head of the Group.\n##### (f) Establishment of Language Access Coordinator position\n**(1) Position**\nThere is established in each agency a position to be known as the Language Access Coordinator.\n**(2) Designation**\nThe head of each agency shall designate an officer or employee of the agency to serve as the Language Access Coordinator for the agency.\n**(3) Duties**\nThe Language Access Coordinator shall\u2014\n**(A)**\nserve as point of contact for each language access effort of the agency;\n**(B)**\nshall ensure that each agency component that frequently interacts with individuals with LEP provides, if feasible, mandatory annual training to managers, personnel who frequently communicate with individuals with LEP, and personnel who arrange for language support, on this Act, the language access plan of the agency, and agency procedures for identifying language access needs, providing language assistance services, working with interpreters and translators, requesting document translations, and tracking the use of language access services;\n**(C)**\ndetermine annually whether additional federally conducted programs and activities should be made accessible for individuals with LEP and notify agency components of their responsibility to provide such access; and\n**(D)**\nbeginning on the date that is 3 years after the date of the enactment of this Act, evaluate the language access plan of the agency, including a review of the costs of language assistance services, and propose changes to agency components, as appropriate, to refine such plan.\n##### (g) Noncompliance\nNoncompliance with the requirements of this Act\u2014\n**(1)**\nshall be treated as discrimination under title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ), thereby granting the Department of Justice enforcement authority, including the authority to conduct an investigation, commence an administrative action, and seek civil remedies; and\n**(2)**\nmay trigger administrative, civil, or injunctive remedies by aggrieved parties or the Attorney General.\n##### (h) Definitions\nIn this Act:\n**(1) Agency**\nThe term agency has the meaning given that term in section 551 of title 5, United States Code.\n**(2) Individual with LEP**\nThe term individual with LEP means an individual for whom English is not a primary language and who has a limited ability to read, speak, write, or understand the English language (including an individual who is able to speak or understand the English language, but has a limited ability to read or write the English language).\n**(3) Language assistance services**\nThe term language assistance services means oral and written language assistance services used to provide individuals with LEP meaningful access to, and an equal opportunity to participate fully in, the services, activities, and other programs administered by the Federal Government.\n**(4) Meaningful access**\nThe term meaningful access means access that\u2014\n**(A)**\nresults in accurate, timely, and effective communication at no cost to the individual with LEP; and\n**(B)**\nis comparable to the access provided to individuals who are proficient in English.\n**(5) Primary language**\nThe term primary language means the language in which an individual most effectively communicates.\n**(6) Program or activity**\nThe term program or activity means all the operations of an agency that involve contact with the public, the administration of Federal benefits, or communication with members of the public or program participants.\n**(7) Qualified interpreter or translator**\nThe term qualified interpreter or translator means\u2014\n**(A)**\nan individual who\u2014\n**(i)**\nis capable of effective, accurate, and impartial rendition of spoken or signed communication from one language to another between people who speak, sign, read, or write in a different language, both receptively and expressively, using any necessary specialized vocabulary and with appropriate cultural relevance, either simultaneously or consecutively;\n**(ii)**\ndemonstrates to the Language Access Coordinator of the agency proficiency in and ability to listen to a spoken language, seeing or feeling a signed or manual language, or reading something written in one language and expressing what is being conveyed by that language accurately and with appropriate cultural relevance into another language, either simultaneously or consecutively, including with respect to any specialized term, concept, or any particularized vocabulary or phraseology particular to the program or service concerned that is being conveyed; and\n**(iii)**\nunderstands and adheres to the roles of interpreters or translators, including any confidentiality, ethics, and impartiality rules.\n**(8) Vital document**\nThe term vital document means any written material containing information critical for\u2014\n**(A)**\naccessing or understanding a Federal program or activity or required by law; or\n**(B)**\nobtaining any aid, benefit, service, or training, such as\u2014\n**(i)**\nan application for a benefit or service;\n**(ii)**\na consent or complaint form;\n**(iii)**\na notice of rights and responsibilities; or\n**(iv)**\na letter or notice that requires a response from a beneficiary, applicant, participant, or employee.",
      "versionDate": "2026-01-22",
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
        "updateDate": "2026-03-17T18:54:11Z"
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
      "date": "2026-01-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7223ih.xml"
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
      "title": "Language Access for All Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Language Access for All Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-13T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To improve access to Federal services by individuals with limited English proficiency, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-13T03:49:23Z"
    }
  ]
}
```
