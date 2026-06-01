# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/841?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/841
- Title: Romance Scam Prevention Act
- Congress: 119
- Bill type: S
- Bill number: 841
- Origin chamber: Senate
- Introduced date: 2025-03-04
- Update date: 2026-02-04T04:26:29Z
- Update date including text: 2026-02-04T04:26:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-04: Introduced in Senate
- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.
- 2025-09-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 145.
- Latest action: 2025-03-04: Introduced in Senate

## Actions

- 2025-03-04 - IntroReferral: Introduced in Senate
- 2025-03-04 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-03-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.
- 2025-09-02 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.
- 2025-09-02 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 145.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-04",
    "latestAction": {
      "actionDate": "2025-03-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/841",
    "number": "841",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001243",
        "district": "",
        "firstName": "Marsha",
        "fullName": "Sen. Blackburn, Marsha [R-TN]",
        "lastName": "Blackburn",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Romance Scam Prevention Act",
    "type": "S",
    "updateDate": "2026-02-04T04:26:29Z",
    "updateDateIncludingText": "2026-02-04T04:26:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-02",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 145.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-09-02",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute. With written report No. 119-58.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-04",
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
      "actionDate": "2025-03-04",
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
            "date": "2025-09-02T21:07:11Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-12T14:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-04T21:02:27Z",
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
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "True",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "CO"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "GA"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s841is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 841\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mrs. Blackburn (for herself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo require online dating service providers to provide fraud ban notifications to online dating service members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Romance Scam Prevention Act .\n#### 2. Online dating safety\n##### (a) Fraud ban notification\n**(1) In general**\nAn online dating service provider shall provide to a member of the online dating service a fraud ban notification if the member has received a message through the online dating service from a banned member of the online dating service.\n**(2) Required contents**\nA fraud ban notification under paragraph (1) shall include the following:\n**(A)**\nThe username or other profile identifier of the banned member, as well as the most recent time when the member to whom the notification is being provided sent or received a message through the online dating service to or from the banned member.\n**(B)**\nA statement, as applicable, that the banned member identified in subparagraph (A) may have been using a false identity or attempting to defraud members.\n**(C)**\nA statement that a member should not send cash or another form of currency or personal financial information to another member.\n**(D)**\nInformation regarding best practices to avoid online fraud or being defrauded by a member of an online dating service, which may be provided through a link to another web page or disclosure.\n**(E)**\nContact information to reach the customer service department of the online dating service provider.\n**(3) Manner and timing**\n**(A) Manner**\nA fraud ban notification under paragraph (1) shall be\u2014\n**(i)**\nclear and conspicuous; and\n**(ii)**\nprovided by email, text message, or, if consented to by the member receiving the fraud ban notification, other appropriate means of communication.\n**(B) Timing**\n**(i) In general**\nExcept as provided in clauses (ii) and (iii), an online dating service provider shall provide a fraud ban notification under paragraph (1) not later than 24 hours after the fraud ban is initiated against the banned member.\n**(ii) Delay based on judgment of provider**\nIf, in the judgment of the online dating service provider, the circumstances require a fraud ban notification under paragraph (1) to be provided after the 24-hour period described in clause (i), the online dating service provider shall, except as provided in clause (iii), provide the notification not later than 3 days after the day on which the fraud ban is initiated against the banned member.\n**(iii) Delay upon request of law enforcement official**\nIf, due to an ongoing investigation, a law enforcement official requests an online dating service provider to delay providing a fraud ban notification under paragraph (1) beyond the time when the notification is required to be provided under clause (i) or (ii), the online dating service provider\u2014\n**(I)**\nmay not provide the notification before the end of the period of delay (including any extension of such period) requested by the law enforcement official; and\n**(II)**\nshall provide the notification not later than 3 days after the last day of the period of delay (including any extension of such period) requested by the law enforcement official.\n**(4) Limitation of liability**\nAn online dating service provider is not liable to a person in a civil action based on any of the following:\n**(A)**\nThe manner of communication used under paragraph (3)(A) to provide a fraud ban notification to a member under paragraph (1).\n**(B)**\nThe timing of a fraud ban notification under paragraph (3)(B) provided to a member under paragraph (1).\n**(C)**\nThe disclosure of information in a fraud ban notification provided under paragraph (1).\n##### (b) Enforcement\n**(1) Enforcement by the Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of commission**\n**(i) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section,\n**(ii) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(iii) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n**(2) Enforcement by States**\n**(A) In general**\nSubject to subparagraph (B), in any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any person in an act or practice that violates this section, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(B) Rights of the Commission**\n**(i) Notice to the Commission**\n**(I) In general**\nExcept as provided in subclause (III), before initiating a civil action under subparagraph (A), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring such civil action.\n**(II) Contents**\nThe notification required by subclause (I) shall include a copy of the complaint to be filed to initiate the civil action.\n**(III) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by subclause (I) before initiating a civil action under subparagraph (A), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(ii) Intervention by the Commission**\nUpon receiving the notice required by clause (i)(I), the Commission may intervene in the civil action and, upon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(C) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for a violation of this section or a regulation promulgated under this section, no attorney general of a State may bring an action under subparagraph (A) during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this section or a regulation promulgated under this section alleged in the complaint.\n**(D) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(E) Actions by other State officials**\nIn addition to a civil action brought by an attorney general under subparagraph (A), any other consumer protection officer of a State who is authorized by the State to do so may bring a civil action under subparagraph (A), subject to the same requirements and limitations that apply under this paragraph to a civil action brought by an attorney general.\n##### (c) One national standard\n**(1) In general**\nA State, or political subdivision thereof, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of the State, that requires an online dating service provider to notify, prohibits an online dating service provider from notifying, or otherwise affects the manner in which an online dating service provider is required or permitted to notify, a member of the online dating service that the member has received a message from or sent a message to a member whose account or profile on the online dating service is the subject of a fraud ban through the online dating service.\n**(2) Rule of construction**\nThis subsection may not be construed to preempt any law of a State or political subdivision of a State relating to contracts or torts.\n##### (d) Definitions\nIn this section:\n**(1) Banned member**\nThe term banned member means a member of an online dating service whose account or profile on the online dating service is the subject of a fraud ban.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Fraud ban**\nThe term fraud ban means the termination or suspension of the account or profile of a member of an online dating service because, in the judgment of the online dating service provider, there is a significant risk the member will attempt to obtain cash or another form of currency from another member through fraudulent means.\n**(4) Member**\nThe term member means an individual who\u2014\n**(A)**\nsubmits to an online dating service provider the information required by the provider to establish an account or profile on the online dating service; and\n**(B)**\nis allowed by the provider to establish such an account or profile.\n**(5) Online dating service**\nThe term online dating service means a service that\u2014\n**(A)**\nis provided through a website or a mobile application; and\n**(B)**\noffers members access to dating or romantic relationships with other members by arranging or facilitating the social introduction of members.\n**(6) Online dating service provider**\nThe term online dating service provider means a person engaged in the business of offering an online dating service.\n**(7) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n##### (e) Effective date\nThis section shall take effect on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-03-04",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s841rs.xml",
      "text": "II\nCalendar No. 145\n119th CONGRESS\n1st Session\nS. 841\n[Report No. 119\u201358]\nIN THE SENATE OF THE UNITED STATES\nMarch 4, 2025 Mrs. Blackburn (for herself and Mr. Hickenlooper ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nSeptember 2, 2025 Reported by Mr. Cruz , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require online dating service providers to provide fraud ban notifications to online dating service members, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Romance Scam Prevention Act .\n#### 2. Online dating safety\n##### (a) Fraud ban notification\n**(1) In general**\nAn online dating service provider shall provide to a member of the online dating service a fraud ban notification if the member has received a message through the online dating service from a banned member of the online dating service.\n**(2) Required contents**\nA fraud ban notification under paragraph (1) shall include the following:\n**(A)**\nThe username or other profile identifier of the banned member, as well as the most recent time when the member to whom the notification is being provided sent or received a message through the online dating service to or from the banned member.\n**(B)**\nA statement, as applicable, that the banned member identified in subparagraph (A) may have been using a false identity or attempting to defraud members.\n**(C)**\nA statement that a member should not send cash or another form of currency or personal financial information to another member.\n**(D)**\nInformation regarding best practices to avoid online fraud or being defrauded by a member of an online dating service, which may be provided through a link to another web page or disclosure.\n**(E)**\nContact information to reach the customer service department of the online dating service provider.\n**(3) Manner and timing**\n**(A) Manner**\nA fraud ban notification under paragraph (1) shall be\u2014\n**(i)**\nclear and conspicuous; and\n**(ii)**\nprovided by email, text message, or, if consented to by the member receiving the fraud ban notification, other appropriate means of communication.\n**(B) Timing**\n**(i) In general**\nExcept as provided in clauses (ii) and (iii), an online dating service provider shall provide a fraud ban notification under paragraph (1) not later than 24 hours after the fraud ban is initiated against the banned member.\n**(ii) Delay based on judgment of provider**\nIf, in the judgment of the online dating service provider, the circumstances require a fraud ban notification under paragraph (1) to be provided after the 24-hour period described in clause (i), the online dating service provider shall, except as provided in clause (iii), provide the notification not later than 3 days after the day on which the fraud ban is initiated against the banned member.\n**(iii) Delay upon request of law enforcement official**\nIf, due to an ongoing investigation, a law enforcement official requests an online dating service provider to delay providing a fraud ban notification under paragraph (1) beyond the time when the notification is required to be provided under clause (i) or (ii), the online dating service provider\u2014\n**(I)**\nmay not provide the notification before the end of the period of delay (including any extension of such period) requested by the law enforcement official; and\n**(II)**\nshall provide the notification not later than 3 days after the last day of the period of delay (including any extension of such period) requested by the law enforcement official.\n**(4) Limitation of liability**\nAn online dating service provider is not liable to a person in a civil action based on any of the following:\n**(A)**\nThe manner of communication used under paragraph (3)(A) to provide a fraud ban notification to a member under paragraph (1).\n**(B)**\nThe timing of a fraud ban notification under paragraph (3)(B) provided to a member under paragraph (1).\n**(C)**\nThe disclosure of information in a fraud ban notification provided under paragraph (1).\n##### (b) Enforcement\n**(1) Enforcement by the Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of commission**\n**(i) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section,\n**(ii) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act.\n**(iii) Authority preserved**\nNothing in this section may be construed to limit the authority of the Commission under any other provision of law.\n**(2) Enforcement by States**\n**(A) In general**\nSubject to subparagraph (B), in any case in which the attorney general of a State has reason to believe that an interest of the residents of the State has been or is threatened or adversely affected by the engagement of any person in an act or practice that violates this section, the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(B) Rights of the Commission**\n**(i) Notice to the Commission**\n**(I) In general**\nExcept as provided in subclause (III), before initiating a civil action under subparagraph (A), the attorney general of a State shall notify the Commission in writing that the attorney general intends to bring such civil action.\n**(II) Contents**\nThe notification required by subclause (I) shall include a copy of the complaint to be filed to initiate the civil action.\n**(III) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by subclause (I) before initiating a civil action under subparagraph (A), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(ii) Intervention by the Commission**\nUpon receiving the notice required by clause (i)(I), the Commission may intervene in the civil action and, upon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(C) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for a violation of this section or a regulation promulgated under this section, no attorney general of a State may bring an action under subparagraph (A) during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this section or a regulation promulgated under this section alleged in the complaint.\n**(D) Rule of construction**\nFor purposes of bringing a civil action under this subsection, nothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(E) Actions by other State officials**\nIn addition to a civil action brought by an attorney general under subparagraph (A), any other consumer protection officer of a State who is authorized by the State to do so may bring a civil action under subparagraph (A), subject to the same requirements and limitations that apply under this paragraph to a civil action brought by an attorney general.\n##### (c) One national standard\n**(1) In general**\nA State, or political subdivision thereof, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of the State, that requires an online dating service provider to notify, prohibits an online dating service provider from notifying, or otherwise affects the manner in which an online dating service provider is required or permitted to notify, a member of the online dating service that the member has received a message from or sent a message to a member whose account or profile on the online dating service is the subject of a fraud ban through the online dating service.\n**(2) Rule of construction**\nThis subsection may not be construed to preempt any law of a State or political subdivision of a State relating to contracts or torts.\n##### (d) Definitions\nIn this section:\n**(1) Banned member**\nThe term banned member means a member of an online dating service whose account or profile on the online dating service is the subject of a fraud ban.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Fraud ban**\nThe term fraud ban means the termination or suspension of the account or profile of a member of an online dating service because, in the judgment of the online dating service provider, there is a significant risk the member will attempt to obtain cash or another form of currency from another member through fraudulent means.\n**(4) Member**\nThe term member means an individual who\u2014\n**(A)**\nsubmits to an online dating service provider the information required by the provider to establish an account or profile on the online dating service; and\n**(B)**\nis allowed by the provider to establish such an account or profile.\n**(5) Online dating service**\nThe term online dating service means a service that\u2014\n**(A)**\nis provided through a website or a mobile application; and\n**(B)**\noffers members access to dating or romantic relationships with other members by arranging or facilitating the social introduction of members.\n**(6) Online dating service provider**\nThe term online dating service provider means a person engaged in the business of offering an online dating service.\n**(7) State**\nThe term State means each State of the United States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n##### (e) Effective date\nThis section shall take effect on the date that is 1 year after the date of the enactment of this Act.",
      "versionDate": "2025-09-02",
      "versionType": "Reported in Senate"
    }
  ]
}
```

## API Data: subjects

```json
{
  "subjects": [
    {
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-05-14T15:05:05Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-05-14T15:02:58Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2025-05-14T15:03:49Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-05-14T15:02:58Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-05-14T15:02:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-05-14T14:51:03Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-04",
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
          "measure-id": "id119s841",
          "measure-number": "841",
          "measure-type": "s",
          "orig-publish-date": "2025-03-04",
          "originChamber": "SENATE",
          "update-date": "2025-06-27"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s841v00",
            "update-date": "2025-06-27"
          },
          "action-date": "2025-03-04",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Romance Scam Prevention Act</strong></p><p>This bill requires online dating service providers (i.e., mobile applications or websites) to provide users with\u00a0a fraud ban notification if the user has established an account with the service and received a message through the service from a banned user of the service.</p><p>The fraud ban notification must include (1) the username or other profile identifier of the banned user and the most recent time when the user who is receiving the notification sent or received a message through the service\u00a0to or from the banned user, (2) a statement that the banned user may have been using a false identity or\u00a0attempting to defraud other users, (3) a statement that the user should not send cash (or another form of currency) or personal financial information to another user, (4) information about avoiding online fraud (e.g., a link to another website or a disclosure) and (5) contact information for the provider's customer service department.</p><p>The bill provides for enforcement of these requirements by the Federal Trade Commission and state attorneys general.\u00a0\u00a0</p>"
        },
        "title": "Romance Scam Prevention Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s841.xml",
    "summary": {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Romance Scam Prevention Act</strong></p><p>This bill requires online dating service providers (i.e., mobile applications or websites) to provide users with\u00a0a fraud ban notification if the user has established an account with the service and received a message through the service from a banned user of the service.</p><p>The fraud ban notification must include (1) the username or other profile identifier of the banned user and the most recent time when the user who is receiving the notification sent or received a message through the service\u00a0to or from the banned user, (2) a statement that the banned user may have been using a false identity or\u00a0attempting to defraud other users, (3) a statement that the user should not send cash (or another form of currency) or personal financial information to another user, (4) information about avoiding online fraud (e.g., a link to another website or a disclosure) and (5) contact information for the provider's customer service department.</p><p>The bill provides for enforcement of these requirements by the Federal Trade Commission and state attorneys general.\u00a0\u00a0</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s841"
    },
    "title": "Romance Scam Prevention Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-04",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Romance Scam Prevention Act</strong></p><p>This bill requires online dating service providers (i.e., mobile applications or websites) to provide users with\u00a0a fraud ban notification if the user has established an account with the service and received a message through the service from a banned user of the service.</p><p>The fraud ban notification must include (1) the username or other profile identifier of the banned user and the most recent time when the user who is receiving the notification sent or received a message through the service\u00a0to or from the banned user, (2) a statement that the banned user may have been using a false identity or\u00a0attempting to defraud other users, (3) a statement that the user should not send cash (or another form of currency) or personal financial information to another user, (4) information about avoiding online fraud (e.g., a link to another website or a disclosure) and (5) contact information for the provider's customer service department.</p><p>The bill provides for enforcement of these requirements by the Federal Trade Commission and state attorneys general.\u00a0\u00a0</p>",
      "updateDate": "2025-06-27",
      "versionCode": "id119s841"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s841is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-09-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s841rs.xml"
        }
      ],
      "type": "Reported in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Romance Scam Prevention Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-16T12:03:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Romance Scam Prevention Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-09-04T02:08:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Romance Scam Prevention Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-07T16:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require online dating service providers to provide fraud ban notifications to online dating service members, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-07T16:18:24Z"
    }
  ]
}
```
