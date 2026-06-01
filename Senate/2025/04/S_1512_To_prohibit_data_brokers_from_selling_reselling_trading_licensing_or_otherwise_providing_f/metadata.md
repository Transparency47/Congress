# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1512?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1512
- Title: Protecting Military Servicemembers Data from Foreign Adversaries Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1512
- Origin chamber: Senate
- Introduced date: 2025-04-29
- Update date: 2025-05-29T12:53:53Z
- Update date including text: 2025-05-29T12:53:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-29: Introduced in Senate
- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-04-29: Introduced in Senate

## Actions

- 2025-04-29 - IntroReferral: Introduced in Senate
- 2025-04-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-29",
    "latestAction": {
      "actionDate": "2025-04-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1512",
    "number": "1512",
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
    "title": "Protecting Military Servicemembers Data from Foreign Adversaries Act of 2025",
    "type": "S",
    "updateDate": "2025-05-29T12:53:53Z",
    "updateDateIncludingText": "2025-05-29T12:53:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
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
      "actionDate": "2025-04-29",
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
          "date": "2025-04-29T19:37:56Z",
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
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1512is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1512\nIN THE SENATE OF THE UNITED STATES\nApril 29, 2025 Mr. Cassidy (for himself and Ms. Warren ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit data brokers from selling, reselling, trading, licensing, or otherwise providing for consideration lists of military servicemembers to any covered nation or person controlled by a covered nation.\n#### 1. Short title\nThis Act may be cited as the Protecting Military Servicemembers Data from Foreign Adversaries Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Controlled by a covered nation**\nThe term controlled by a covered nation means, with respect to a person, that such person is\u2014\n**(A)**\na foreign person that is domiciled in, is headquartered in, has its principal place of business in, or is organized under the laws of a covered nation;\n**(B)**\nan entity with respect to which 1 or more foreign persons described in subparagraph (A) directly or indirectly owns not less than a 20 percent stake; or\n**(C)**\na person subject to the direction or control of (including an affiliate or subsidiary) a foreign person described in subparagraph (A) or an entity described in subparagraph (B).\n**(3) Covered nation**\nThe term covered nation has the meaning given such term in section 4872(f) of title 10, United States Code.\n**(4) Data broker**\nThe term data broker means a person that knowingly collects and sells, resells, licenses, trades, or otherwise provides or makes available for consideration to third parties the personal information of an individual with whom the business does not have a direct relationship.\n**(5) Military service list**\nThe term military servicemember list means a list that includes personal information (other than public record information) about 1 or more individuals or households which is created for the express or implied purpose of compiling information about individuals who are current or former servicemembers (as that term is defined in section 101 of the Servicemembers Civil Relief Act ( 50 U.S.C. 3911 ).\n#### 3. Prohibiting providing servicemember lists to any covered nation or person controlled by a covered nation\n##### (a) In general\nIt shall be unlawful for a data broker to sell, resell, license, trade, or otherwise provide or make available for consideration a military servicemember list to any covered nation or any person controlled by a covered nation.\n##### (b) Required contracts\nAny data broker selling, reselling, licensing, trading, or otherwise providing or making available for consideration a military servicemember list to any other person shall require by contract that such person may not sell, resell, license, trade, or otherwise provide or make available such list to any covered nation or any person controlled by a covered nation.\n##### (c) Conspiracies and certain transactions\nIt shall be unlawful for any person to\u2014\n**(1)**\ncause or conspire to cause another person to violate subsection (a) or (b); or\n**(2)**\nengage in a transaction that has the purpose of evading such subsections.\n#### 4. Enforcement\n##### (a) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of section 3 shall be treated as a violation of a rule defining an unfair or a deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided in subparagraphs (D) and (E), the Commission shall enforce section 3 in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(B) Privileges and immunities**\nAny person who violates section 3 shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this Act shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Nonprofit organizations**\nNotwithstanding section 4 of the Federal Trade Commission Act ( 15 U.S.C. 44 ) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraphs (A) and (B), with respect to organizations not organized to carry on business for their own profit or that of their members.\n**(E) Independent litigation authority**\nIn any case in which the Commission has reason to believe that a data broker is violating or has violated section 3, the Commission may bring a civil action in an appropriate district court of the United States\u2014\n**(i)**\nto enjoin further violation of such section by such data broker;\n**(ii)**\nto compel compliance with such section; and\n**(iii)**\nto obtain damages, restitution, or other compensation on behalf of aggrieved consumers.\n**(3) Rulemaking**\nPursuant to section 553 of title 5, United States Code, the Commission shall promulgate regulations to carry out the provisions of this Act. The Commission shall issue a final rule by not later than 1 year after the date of enactment of this Act.\n##### (b) Enforcement by States\n**(1) In general**\nIn any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any data broker in a practice that violates section 3, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to\u2014\n**(A)**\nenjoin further violation of such section by such data broker;\n**(B)**\ncompel compliance with such section; and\n**(C)**\nobtain damages, restitution, or other compensation on behalf of such residents.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (iii), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring a civil action under paragraph (1) not later than 10 days before initiating the civil action.\n**(ii) Contents**\nThe notification required by clause (i) with respect to a civil action shall include a copy of the complaint to be filed to initiate the civil action.\n**(iii) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by clause (i) before initiating a civil action under paragraph (1), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(B) Intervention by the Commission**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general of a State under paragraph (1); and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Preemptive action by the Commission**\nIf the Commission institutes a civil action or an administrative action with respect to a violation of section 3, the attorney general of a State may not, during the pendency of such action, bring a civil action under paragraph (1) against any defendant named in the complaint of the Commission for the violation with respect to which the Commission instituted such action.\n**(5) Venue; service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which the defendant\u2014\n**(i)**\nis an inhabitant; or\n**(ii)**\nmay be found.\n#### 5. Report\nNot later than 1 year after the date of enactment of this Act, the Comptroller General of the United States (referred to in this section as the Comptroller General ) shall submit to Congress a report containing\u2014\n**(1)**\nan analysis of\u2014\n**(A)**\nthe enforcement of this Act;\n**(B)**\nwhether additional resources or enforcement authorities may be necessary to protect the national security interests of the United States from threats posed by data brokers selling the sensitive personal information of people in the United States; and\n**(C)**\nwhether the national security interests of the United States would be advanced by expanding the protections of this Act to additional categories of individuals or types of personal information; and\n**(2)**\nrecommendations for such legislation and administrative action as the Comptroller General determines appropriate.",
      "versionDate": "2025-04-29",
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
        "name": "Commerce",
        "updateDate": "2025-05-29T12:53:53Z"
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
      "date": "2025-04-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1512is.xml"
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
      "title": "Protecting Military Servicemembers Data from Foreign Adversaries Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-09T03:38:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Military Servicemembers Data from Foreign Adversaries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-09T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit data brokers from selling, reselling, trading, licensing, or otherwise providing for consideration lists of military servicemembers to any covered nation or person controlled by a covered nation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-09T03:33:25Z"
    }
  ]
}
```
