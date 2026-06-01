# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3982?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3982
- Title: AI Fraud Accountability Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3982
- Origin chamber: Senate
- Introduced date: 2026-03-04
- Update date: 2026-03-24T01:21:15Z
- Update date including text: 2026-03-24T01:21:15Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-04: Introduced in Senate
- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2026-03-04: Introduced in Senate

## Actions

- 2026-03-04 - IntroReferral: Introduced in Senate
- 2026-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-04",
    "latestAction": {
      "actionDate": "2026-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3982",
    "number": "3982",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001232",
        "district": "",
        "firstName": "Tim",
        "fullName": "Sen. Sheehy, Tim [R-MT]",
        "lastName": "Sheehy",
        "party": "R",
        "state": "MT"
      }
    ],
    "title": "AI Fraud Accountability Act of 2026",
    "type": "S",
    "updateDate": "2026-03-24T01:21:15Z",
    "updateDateIncludingText": "2026-03-24T01:21:15Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-04",
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
      "actionDate": "2026-03-04",
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
          "date": "2026-03-04T16:39:28Z",
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
      "bioguideId": "B001303",
      "firstName": "Lisa",
      "fullName": "Sen. Blunt Rochester, Lisa [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Blunt Rochester",
      "party": "D",
      "sponsorshipDate": "2026-03-04",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3982is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3982\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2026 Mr. Sheehy (for himself and Ms. Blunt Rochester ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish protections against digital impersonation fraud, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the AI Fraud Accountability Act of 2026 .\n#### 2. Criminal prohibition on use of digital impersonations to commit fraud\n##### (a) In general\nSection 223 of the Communications Act of 1934 (47 U.S.C. 223) is amended\u2014\n**(1)**\nby redesignating subsection (i) as subsection (j); and\n**(2)**\nby inserting after subsection (h) the following:\n(i) Use of digital impersonations To commit fraud (1) Definitions In this subsection: (A) Digital impersonation The term digital impersonation means any visual or audio depiction of\u2014 (i) an identifiable individual created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual or audio depiction, that, when viewed or listened to as a whole by a reasonable person, is indistinguishable from an authentic visual or audio depiction of the individual; or (ii) an imaginary individual created through the use of software, machine learning, artificial intelligence, or any other computer-generated or technological means, including by adapting, modifying, manipulating, or altering an authentic visual or audio depiction of an imaginary individual, that, when viewed or listened to as a whole by a reasonable person, is indistinguishable from a visual or audio depiction of a real individual. (B) Identifiable individual The term identifiable individual means an individual\u2014 (i) who appears in whole or in part, or is heard, in a digital impersonation; and (ii) whose face, likeness, voice, or other distinguishing characteristic (including a unique birthmark or other recognizable feature) is displayed or heard in connection with such digital impersonation. (2) Offense (A) In general Subject to subparagraph (B), it shall be unlawful for a person, in interstate or foreign communications, to falsely pose as an identifiable individual or imaginary individual, in a manner intended to be taken as genuine, in a digital impersonation, with intent to defraud a person of any money, paper, document, or thing of value. (B) Exceptions Subparagraph (A) shall not apply to a lawfully authorized investigative, protective, or intelligence activity of\u2014 (i) a law enforcement agency of the United States, a State, or a political subdivision of a State; or (ii) an intelligence agency of the United States; (3) Penalties Any person who violates paragraph (2) shall be fined under title 18, United States Code, imprisoned not more than 3 years, or both. (4) Threats Any person who intentionally threatens to commit the offense under paragraph (2) for the purpose of intimidation, coercion, extortion, or to create mental distress shall be punished as provided in paragraph (3). (5) Forfeiture (A) In general The court, in imposing a sentence on any person convicted of a violation of paragraph (2), shall order, in addition to any other sentence imposed and irrespective of any other sentence imposed and irrespective of any provision of State law, that the person forfeit to the United States\u2014 (i) the person\u2019s interest in property, real or personal, constituting or derived from any gross proceeds of the violation, or any property traceable to such property, obtained or retained directly or indirectly as a result of the violation; and (ii) any personal property of the person used, or intended to be used, in any manner or part, to commit or to facilitate the commission of the violation. (B) Procedures Section 413 of the Controlled Substances Act (21 U.S.C. 853), with the exception of subsections (a) and (d), shall apply to the criminal forfeiture of property under subparagraph (A). (6) Extraterritorial jurisdiction There is extraterritorial Federal jurisdiction over an offense under paragraph (2). .\n##### (b) Defenses\nSection 223(e)(1) of the Communications Act of 1934 (47 U.S.C. 223(e)(1)) is amended by striking or (h) and inserting (h), or (i) .\n#### 3. Protection against digital impersonation fraud\n##### (a) Prohibition\n**(1) In general**\nSubject to paragraph (2), it shall be unlawful for a person, in interstate or foreign commerce, to falsely pose as an identifiable or imaginary individual in a manner intended to be taken as genuine, in a digital impersonation, with intent to defraud a person of any money, paper, document, or thing of value.\n**(2) Exception**\nThe prohibition described in paragraph (1) shall not apply to a lawfully authorized investigative, protective, or intelligence activity of\u2014\n**(A)**\na law enforcement agency of the United States, a State, or a political subdivision of a State; or\n**(B)**\nan intelligence agency of the United States.\n##### (b) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of subsection (a) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act (15 U.S.C. 57a(a)(1)(B)).\n**(2) Powers of the Commission**\n**(A) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act (15 U.S.C. 41 et seq.) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates subsection (a) shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act (15 U.S.C. 41 et seq.).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n##### (c) Definitions\nFor purposes of this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Digital impersonation; identifiable individual**\nThe terms digital impersonation and identifiable individual have the meaning given such terms in section 223(i) of the Communications Act of 1934 (47 U.S.C. 223(i)), as added by section 2 of this Act.\n#### 4. Working group on digital impersonation fraud\n##### (a) Definitions\nIn this section:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Science, Space, and Technology of the House of Representatives.\n**(2) Digital forensics**\nThe term digital forensics means scientific or technical practices used to recognize, collect, analyze, or interpret digital evidence for the purposes of investigating crimes or other incidents, including the use of digital impersonation to commit fraud.\n**(3) Digital impersonation**\nThe term digital impersonation has the meaning given that term in section 223(i) of the Communications Act of 1934 (47 U.S.C. 223(i)), as added by section 2 of this Act.\n**(4) Director**\nThe term Director means the Director of the National Institute of Standards and Technology.\n##### (b) Establishment of Working Group\n**(1) In general**\nNot later than 30 days after the date of the enactment of this Act, the Secretary of Commerce, acting through the Director, shall convene a working group (referred to in this section as the Working Group ) to engage in technical discussions and research for the development of best practices and recommendations for the recognition, detection, prevention, and tracing of digital impersonations used in violation of section 223(i) of the Communications Act of 1934 (47 U.S.C. 223(i)), as amended by section 2 of this Act, and section 3(a) of this Act.\n**(2) Composition**\nThe Working Group shall consist of\u2014\n**(A)**\nrepresentatives from\u2014\n**(i)**\nthe Department of Justice;\n**(ii)**\nthe Federal Trade Commission;\n**(iii)**\nFederal, State, and local government law enforcement agencies; and\n**(iv)**\nprivate sector industries, including\u2014\n**(I)**\nfinancial services;\n**(II)**\nhealth care;\n**(III)**\nretail and e-commerce;\n**(IV)**\ntelecommunications; and\n**(V)**\ndigital platforms, including social media platforms; and\n**(B)**\nscientists and engineers with expertise in\u2014\n**(i)**\ndigital forensics; and\n**(ii)**\nartificial intelligence, including the generation or detection of digital impersonations.\n##### (c) Public workshop\nThe Director shall\u2014\n**(1)**\nconvene not less than 1 public workshop to solicit input from stakeholders on the best practices and recommendations developed under subsection (b)(1); and\n**(2)**\nincorporate such input into the best practices and recommendations as the Director considers appropriate.\n##### (d) Publication of best practices and recommendations\nNot later than 1 year after the date of the enactment of this Act, the Director shall publish on a publicly accessible website of the National Institute of Standards and Technology a report that contains the best practices and recommendations developed pursuant to subsection (b)(1) and modified under subsection (c)(2).\n##### (e) Annual review and updates\nNot later than 2 years after the date of the enactment of this Act, and not less frequently than once each year thereafter, the Director shall\u2014\n**(1)**\nreview the best practices and recommendations developed under this section; and\n**(2)**\nupdate the best practices and recommendations published under subsection (d) as the Director considers appropriate pursuant to the most recent review conducted pursuant to paragraph (1) of this subsection.\n##### (f) Report to Congress\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the Director shall submit to the appropriate committees of Congress a report that summarizes\u2014\n**(1)**\nthe meetings and collaboration of the Working Group during the year preceding the submission of the report; and\n**(2)**\nthe work planned by the Working Group for the year following the submission of the report.\n##### (g) Sunset\nThe requirements of this section shall terminate on the date that is 10 years after the date of the enactment of this Act.\n#### 5. Cooperation with foreign law enforcement agencies\n##### (a) List of countries with highest occurrence of violations\nNot later than 90 days after the date of enactment of this section, the Federal Trade Commission (in this section referred to as the Commission ), in consultation with the Attorney General and the Secretary of State, shall identify a list of the top 10 foreign countries where the highest occurrence of violations of section 2 or 3 originate and harm individuals located in the United States or a territory thereof.\n##### (b) FTC international agreements\n**(1) In general**\nUsing the list of foreign countries identified under subsection (a), the Commission, in coordination with the Secretary of State, may enter into agreements with such foreign countries to ensure the cooperation of any foreign law enforcement agency in the Commission's enforcement of this Act.\n**(2) Requirements**\nAny agreement entered into by the Commission under paragraph (1) shall be subject to the requirements described in section 6(j)(4) of the Federal Trade Commission Act (15 U.S.C. 46(j)(4)).\n**(3) Report to Congress**\nNot later than 1 year after the date of enactment of this section, and annually thereafter, the Commission shall submit to the Committee on Commerce, Science, and Transportation of the Senate and the Committee on Energy and Commerce of the House of Representatives a report on the implementation of this subsection during the reporting period, including\u2014\n**(A)**\nany new agreements with foreign countries (as described in paragraph (1)) entered into during such period;\n**(B)**\nany negotiations regarding new agreements or modifications to agreements with foreign countries during such period;\n**(C)**\na description of the Commission's coordination with foreign law enforcement agencies to enforce alleged violations of section 3; and\n**(D)**\nany challenges with cooperation of foreign law enforcement agencies (including with respect to foreign countries without an agreement under paragraph (1)) in the enforcement of section 3.\n##### (c) DOJ review of international law enforcement agency agreements\n**(1) In general**\nNot later than 1 year after the date of enactment of this section, and not less frequently than every 5 years thereafter, the Attorney General shall review and, as necessary and consistent with authorities under applicable law, modify international agreements with foreign law enforcement agencies in foreign countries identified under subsection (a) to encourage assistance with the enforcement of violations of section 223(i) of the Communications Act of 1934, as added by section 2 of this Act, that originate outside the United States.\n**(2) Report**\nNot later than 1 year after the date of enactment of this section, and every 5 years thereafter, the Attorney General shall submit to the Committee on Commerce, Science, and Transportation of the Senate, the Committee on the Judiciary of the Senate, the Committee on Energy and Commerce of the House of Representatives, and the Committee on the Judiciary of the House of Representatives a report that includes\u2014\n**(A)**\nan analysis of the review conducted under paragraph (1);\n**(B)**\na description of any modifications to international agreements described in paragraph (1) pursued by the Attorney General; and\n**(C)**\nrecommendations to strengthen the enforcement of violations of section 223(i) of the Communications Act of 1934, as added by section 2 of this Act, that\u2014\n**(i)**\noriginate outside the United States; and\n**(ii)**\nharm United States persons located in the United States.\n#### 6. Savings clause\nNothing in this Act shall be construed to restrict parody, satire, journalism, or any other rights, privileges, or immunities protected by the First Amendment to the Constitution of the United States.",
      "versionDate": "",
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
        "actionDate": "2026-03-04",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on the Judiciary, Science, Space, and Technology, and Foreign Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7786",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "AI Fraud Accountability Act",
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
        "name": "Commerce",
        "updateDate": "2026-03-20T15:10:58Z"
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
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3982is.xml"
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
      "title": "AI Fraud Accountability Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-19T03:23:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "AI Fraud Accountability Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-19T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish protections against digital impersonation fraud, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-19T03:18:22Z"
    }
  ]
}
```
