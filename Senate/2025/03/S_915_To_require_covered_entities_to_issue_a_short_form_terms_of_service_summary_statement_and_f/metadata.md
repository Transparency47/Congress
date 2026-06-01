# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/915?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/915
- Title: TLDR Act
- Congress: 119
- Bill type: S
- Bill number: 915
- Origin chamber: Senate
- Introduced date: 2025-03-10
- Update date: 2025-12-05T21:55:02Z
- Update date including text: 2025-12-05T21:55:02Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in Senate
- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-03-10: Introduced in Senate

## Actions

- 2025-03-10 - IntroReferral: Introduced in Senate
- 2025-03-10 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/915",
    "number": "915",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "TLDR Act",
    "type": "S",
    "updateDate": "2025-12-05T21:55:02Z",
    "updateDateIncludingText": "2025-12-05T21:55:02Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-10",
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
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T22:01:58Z",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Lujan, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s915is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 915\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2025 Mr. Cassidy (for himself and Mr. Luj\u00e1n ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require covered entities to issue a short-form terms of service summary statement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Terms-of-service Labeling, Design, and Readability Act or the TLDR Act .\n#### 2. Standard terms of service summary statement\n##### (a) Deadline for terms of service summary statement\nNot later than 360 days after the date of the enactment of this Act, the Commission shall issue a rule in accordance with section 553 of title 5, United States Code, with regard to a covered entity that publishes or has published a terms of service\u2014\n**(1)**\nthat requires the covered entity to include a truthful and non-misleading short-form terms of service summary statement on the website of the entity;\n**(2)**\nthat requires the covered entity to include a truthful and non-misleading graphic data flow diagram on the website of the entity; and\n**(3)**\nthat requires the covered entity to display the full terms of service of the entity in an interactive data format.\n##### (b) No New Contractual Obligation\nThe requirement to include a summary statement described in subsection (a)(1) does not create any new contractual obligation.\n##### (c) Requirements for short-Form terms of service summary statement\n**(1) In general**\nThe short-form terms of service summary statement described in subsection (a)(1)\u2014\n**(A)**\nshall be accessible to individuals with low levels of literacy and individuals with disabilities, be machine readable, and include tables, graphic icons, hyperlinks, or other means as the Commission may require; and\n**(B)**\nmay be presented differently depending on the interface or type of device on which the statement is being accessed by the user.\n**(2) Location of summary statement and graphic data flow diagram**\nThe summary statement described in subsection (a)(1) shall be placed at the top of the permanent terms of service page of the covered entity, and the graphic data flow diagram described in subsection (a)(2) shall be located immediately below such summary statement.\n**(3) Contents of summary statement**\nThe summary statement described in subsection (a)(1) shall include the following:\n**(A)**\nThe categories of sensitive information that the covered entity processes.\n**(B)**\nThe sensitive information that is required for the basic functioning of the service and what sensitive information is needed for additional features and future feature development.\n**(C)**\nA summary of the legal liabilities of a user and any rights transferred from the user to the covered entity, such as mandatory arbitration, class action waiver, any licensing or sale by the covered entity of the content of the user, and any waiver of moral rights.\n**(D)**\nHistorical versions of the terms of service and change logs.\n**(E)**\nIf the covered entity provides user deletion services, directions for how the user can delete sensitive information or discontinue the use of sensitive information.\n**(F)**\nA list of data breaches from the previous 3 years reported to consumers under existing Federal and State laws.\n**(G)**\nThe effort required by a user to read the entire terms of service text, such as through the total word count and approximate time to read the statement.\n**(H)**\nAny other information the Commission determines to be necessary if that information is included in the terms of service by the covered entity.\n**(4) Additional information required by the Commission**\nIn the rule issued under subsection (a), the Commission shall include a list of other information the Commission determines to be necessary under paragraph (3)(H).\n##### (d) Guidance on graphic data flow diagrams\nNot later than 360 days after the date of the enactment of this Act, the Commission shall publish guidelines on how a covered entity can graphically display how the sensitive information of a user is shared with a subsidiary or corporate affiliate of such entity and how such sensitive information is shared with third parties.\n##### (e) Interactive data format terms of service\nNot later than 360 days after the date of the enactment of this Act, the Commission shall issue a rule in accordance with section 553 of title 5, United States Code, that requires a covered entity to tag portions of the terms of services of the entity according to an interactive data format.\n##### (f) Enforcement\n**(1) Enforcement by the Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of this Act or a regulation promulgated under this Act shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of the Commission**\n**(i) In general**\nThe Commission shall enforce this section and the regulations promulgated under this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(ii) Privileges and immunities**\nAny person who violates this section or a regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(iii) Authority persevered**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(2) Enforcement by States**\n**(A) In general**\nIn any case in which the attorney general of a State has reason to believe that an interest of at least 1,000 residents of that State has been or is threatened or adversely affected by the engagement of any person in a practice that violates this section or a regulation promulgated under this section, the attorney general of the State, as parens patriae, may bring a civil action on behalf of the residents of the State in a district court of the United States of appropriate jurisdiction\u2014\n**(i)**\nto enjoin that practice;\n**(ii)**\nto enforce compliance with this section;\n**(iii)**\nto obtain damages, restitution, or other compensation on behalf of such residents; and\n**(iv)**\nto obtain such other relief as the court may consider to be appropriate.\n**(B) Rights of the Commission**\n**(i) Notice to the Commission**\n**(I) In general**\nExcept as provided in subclause (III), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under subparagraph (A) before initiating the civil action.\n**(II) Contents**\nThe notification required by subclause (I) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(III) Exemption**\nIf it is not feasible for the attorney general of a State to provide the notification required by subclause (I) before initiating a civil action under subparagraph (A), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(ii) Intervention by the Commission**\nThe Commission may\u2014\n**(I)**\nintervene in any civil action brought by the attorney general of a State under subparagraph (A); and\n**(II)**\nupon intervening\u2014\n**(aa)**\nbe heard on all matters arising in the civil action; and\n**(bb)**\nfile petitions for appeal.\n**(C) Construction**\nNothing in this paragraph may be construed to prevent an attorney general of a State from exercising the powers conferred on the attorney general by the laws of that State to\u2014\n**(i)**\nconduct investigations;\n**(ii)**\nadminister oaths or affirmations; or\n**(iii)**\ncompel the attendance of witnesses or the production of documentary and other evidence.\n**(D) Actions by the Commission**\nIn any case in which an action is instituted by or on behalf of the Commission for a violation of this section or a regulation promulgated under this section, a State may not, during the pendency of that action, institute a separate action under subparagraph (A) against any defendant named in the complaint in the action instituted by or on behalf of the Commission for that violation.\n**(E) Venue; Service of process**\n**(i) Venue**\nAny action brought under subparagraph (A) may be brought in\u2014\n**(I)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(II)**\nanother court of competent jurisdiction.\n**(ii) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(I)**\nis an inhabitant; or\n**(II)**\nmay be found.\n##### (g) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Covered entity**\nThe term covered entity \u2014\n**(A)**\nmeans any person that operates a website located on the internet or an online service that is operated for commercial purposes; and\n**(B)**\ndoes not include a small business concern (as defined in section 3 of the Small Business Act ( 15 U.S.C. 632 )).\n**(3) Disability**\nThe term disability has the meaning given the term in section 3 of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12102 ).\n**(4) Interactive data format**\nThe term interactive data format means an electronic data format in which pieces of information are identified using an interactive data standard, such as eXtensible Markup Language (commonly known as XML ), that is a standardized list of electronic tags that mark the information described in subsection (c)(3) within the terms of service of a covered entity.\n**(5) Moral rights**\nThe term moral rights means the rights conferred by section 106A(a) of title 17, United States Code.\n**(6) Process**\nThe term process means any operation or set of operations performed on sensitive information, including collection, analysis, organization, structuring, retaining, using, or otherwise handling sensitive information.\n**(7) Sensitive information**\nThe term sensitive information means any of the following:\n**(A)**\nHealth information.\n**(B)**\nBiometric information.\n**(C)**\nPrecise geolocation information.\n**(D)**\nSocial security number.\n**(E)**\nInformation concerning the race, color, religion, national origin, sex, age, or disability of an individual.\n**(F)**\nThe content and parties to a communication.\n**(G)**\nAudio and video recordings captured through a consumer device.\n**(H)**\nFinancial information, including a bank account number, credit card number, debit card number, or insurance policy number.\n**(I)**\nOnline browsing history, which means information revealing online activities over time or across websites or online services not owned or operated by the covered entity.\n**(8) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(9) Third party**\nThe term third party means, with respect to a covered entity, a person\u2014\n**(A)**\nto which the covered entity disclosed sensitive information; and\n**(B)**\nthat is not\u2014\n**(i)**\nthe covered entity;\n**(ii)**\na subsidiary or corporate affiliate of the covered entity; or\n**(iii)**\na service provider of the covered entity.",
      "versionDate": "2025-03-10",
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
        "actionDate": "2025-03-10",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "2019",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "TLDR Act",
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
        "updateDate": "2025-05-14T16:00:11Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s915is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require covered entities to issue a short-form terms of service summary statement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T18:33:22Z"
    },
    {
      "title": "TLDR Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-27T18:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "TLDR Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Terms-of-service Labeling, Design, and Readability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T18:23:20Z"
    }
  ]
}
```
