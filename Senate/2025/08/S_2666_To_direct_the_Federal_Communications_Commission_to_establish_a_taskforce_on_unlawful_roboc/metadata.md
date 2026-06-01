# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2666?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2666
- Title: Foreign Robocall Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 2666
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2026-05-26T18:35:35Z
- Update date including text: 2026-05-26T18:35:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-10-21 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-01",
    "latestAction": {
      "actionDate": "2025-08-01",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2666",
    "number": "2666",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "B001305",
        "district": "",
        "firstName": "Ted",
        "fullName": "Sen. Budd, Ted [R-NC]",
        "lastName": "Budd",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Foreign Robocall Elimination Act",
    "type": "S",
    "updateDate": "2026-05-26T18:35:35Z",
    "updateDateIncludingText": "2026-05-26T18:35:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-21",
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
      "actionDate": "2025-08-01",
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
      "actionDate": "2025-08-01",
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
            "date": "2025-10-21T14:00:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-21T14:00:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-08-01T22:25:50Z",
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
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "VT"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-02-12",
      "state": "OH"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2026-02-12",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2666is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2666\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Budd (for himself and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo direct the Federal Communications Commission to establish a taskforce on unlawful robocalls, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Foreign Robocall Elimination Act .\n#### 2. Interagency taskforce on unlawful robocalls\n##### (a) Definitions\nIn this section:\n**(1) Commission**\nThe term Commission means the Federal Communications Commission.\n**(2) Consortium**\nThe term Consortium means the consortium described in section 13(d) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ).\n**(3) Federal agency**\nThe term Federal agency has the meaning given the term agency in section 551 of title 5, United States Code.\n**(4) Taskforce**\nThe term taskforce means the taskforce on unlawful robocalls established under subsection (b).\n**(5) Unlawful robocall**\nThe term unlawful robocall means a telephone call made in violation of subsection (b) or (e) of section 227 of the Communications Act of 1934 ( 47 U.S.C. 227 ).\n##### (b) Establishment\nNot later than 270 days after the date of enactment of this Act, the Commission, after consultation with the Federal Trade Commission and the Attorney General, shall establish a taskforce on unlawful robocalls.\n##### (c) Membership\n**(1) In general**\nThe taskforce shall be composed of the following members:\n**(A)**\n**(i)**\nA representative of each Federal agency that the Chairman of the Commission, in consultation with the Chairman of the Federal Trade Commission and the Attorney General, considers appropriate.\n**(ii)**\nWith respect to each Federal agency considered under clause (i) to be appropriate, the Chairman of the Commission shall appoint a representative of that Federal agency to the taskforce based on the recommendations of the head of that Federal agency.\n**(B)**\nSeven representatives of private sector entities, to be appointed as described in paragraph (2)\u2014\n**(i)**\n3 of whom shall be representatives from private sector entities with expertise in combating unlawful robocalls, including\u2014\n**(I)**\nvoice service providers;\n**(II)**\nanalytics providers;\n**(III)**\ntechnologists; and\n**(IV)**\ntechnology experts;\n**(ii)**\n1 of whom shall be a representative from the Consortium;\n**(iii)**\n1 of whom shall be a representative of a marketing business that communicates with consumers by telephone as part of the normal course of business of that marketing business;\n**(iv)**\n1 of whom shall be a representative of a business or nonprofit organization that communicates with consumers by telephone for non-marketing purposes on a regular basis; and\n**(v)**\n1 of whom shall be a representative of an organization that advocates on behalf of customers and who has relevant experience and expertise in combating unlawful robocalls.\n**(2) Appointment of representatives of private sector entities**\n**(A) In general**\nNotwithstanding any provision of chapter 10 of title 5, United States Code, the members of the taskforce described in paragraph (1)(B) shall be jointly appointed by the Chairman of the Commission, the Chairman of the Federal Trade Commission, and the Attorney General.\n**(B) Inability to reach agreement**\n**(i) In general**\nSubject to clauses (ii) and (iii), if the Chairman of the Commission, the Chairman of the Federal Trade Commission, and the Attorney General cannot reach agreement regarding an appointment described in subparagraph (A), as determined by the Chairman of the Commission, the Chairman of the Commission shall make that appointment.\n**(ii) Notice of appointments**\nNot later than 48 hours before appointing a member to the taskforce under clause (i), the Chairman of the Commission shall provide notice of the proposed appointment to the commissioners of the Commission.\n**(iii) Request for vote**\n**(I) In general**\nExcept as provided in subclause (II), if, after receiving notice under clause (ii) of a proposed appointment under clause (i), not fewer than 2 commissioners of the Commission request that the proposed appointment be subject to a vote of the Commission, the Chairman of the Commission may not make that appointment unless a majority of the commissioners of the Commission vote to approve the appointment.\n**(II) Inapplicability**\nSubclause (I) shall have no force or effect during any period in which there has been a vacancy with respect to a position as commissioner of the Commission for more than 180 days.\n##### (d) Report\n**(1) In general**\nThe taskforce shall prepare a report on unlawful robocalls, which shall contain recommendations and advice for Federal agencies with jurisdiction relevant to combating unlawful robocalls, and for Congress, regarding the most effective ways to combat unlawful robocalls made into the United States from outside the United States.\n**(2) Matters to be studied**\nIn preparing the report required under paragraph (1), the taskforce shall\u2014\n**(A)**\ncompare the estimated number of suspected unlawful robocalls made within the United States with the estimated number of unlawful robocalls made into the United States from outside the United States;\n**(B)**\ndetermine which foreign countries serve as the foreign points of departure for the highest volume of unlawful robocalls made into the United States;\n**(C)**\ndetermine the magnitude of financial loss and the number of instances of stolen identity that occur within the United States each year as a result of unlawful robocalls made from outside the United States;\n**(D)**\nexamine methods for encouraging the adoption of caller identification authentication technology in foreign countries;\n**(E)**\nexamine and provide information on options for how countries can collaborate on solutions to authenticate and verify international calls, including relevant analytics relating to unlawful robocalls and technical options that can be used with respect to that authentication and verification;\n**(F)**\nexamine how better implementation of technical solutions, such as traceback and caller identification authentication technology in foreign originating countries, would improve coordination between the United States and foreign countries in combating unlawful robocalls;\n**(G)**\ndetermine whether\u2014\n**(i)**\nthe technical standards commonly known as STIR/SHAKEN adequately provide call authentication for unlawful robocalls from foreign originating providers or foreign intermediate providers through gateway providers in the United States; and\n**(ii)**\nit would be desirable to encourage other countries to adopt the standards described in clause (i);\n**(H)**\ndetermine if coordination with respect to technologies and incentives to combat unlawful robocalls placed from outside the United States into the United States can help inform strategies to combat potentially fraudulent, or otherwise unlawful, text messages sent from persons outside the United States to persons within the United States;\n**(I)**\nexamine ways to provide incentives to foreign countries to cooperate with law enforcement efforts in the United States to combat unlawful robocalls;\n**(J)**\nexamine whether any Federal agency, or any other organization, that combats unlawful robocalls needs additional resources in order to more effectively combat unlawful robocalls made into the United States from outside the United States;\n**(K)**\nspecifically consider whether the ability of the Attorney General to conduct enforcement activities with respect to unlawful robocalls would be increased through the establishment of an office within the Department of Justice dedicated to those enforcement activities;\n**(L)**\nexamine how increased criminal penalties based on the volume of unlawful robocalls could help prevent unlawful robocalls made into the United States;\n**(M)**\nexamine how many enforcement activities the Attorney General has undertaken in the year preceding the date on which the preparation of the report begins, including in response to referrals made by the Commission;\n**(N)**\nspecifically determine how the Attorney General has pursued forfeiture amounts in enforcement activities with respect to unlawful robocalls;\n**(O)**\nseek input, as appropriate, from technologists and private sector innovators to find solutions for combating unlawful robocalls; and\n**(P)**\nidentify a list of best practices regarding the identification and blocking of unlawful robocalls that telephone service providers and providers of technology solutions can voluntarily implement to improve the effectiveness of mitigating unlawful robocalls made into the United States from outside the United States.\n**(3) Report to Congress**\nNot later than 360 days after the date on which the taskforce is established under subsection (b), the taskforce shall submit to Congress the report prepared under this subsection.\n##### (e) Use of funds\nNotwithstanding section 1346 of title 31, United States Code, funds made available by this or any other Act to the Commission, the Federal Trade Commission, or the Department of Justice may be used by the applicable Federal agency for coordination with, participation in, or recommendations involving the taskforce, as required under this section.\n##### (f) Termination\nThe taskforce shall terminate on the date that is 90 days after the date on which the taskforce submits to Congress the report prepared under subsection (d), as required under paragraph (3) of that subsection.\n#### 3. FCC notice provision\nSection 13(d)(2) of the Pallone-Thune TRACED Act ( Public Law 116\u2013105 ) is amended by striking annually and inserting once every 3 years .",
      "versionDate": "2025-08-01",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-11-14T19:03:41Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-11-14T19:04:59Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-11-14T19:02:38Z"
          },
          {
            "name": "Foreign and international corporations",
            "updateDate": "2025-11-14T19:03:13Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-11-14T19:04:53Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-11-14T19:04:46Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-11-14T19:02:46Z"
          },
          {
            "name": "Right of privacy",
            "updateDate": "2025-11-14T19:06:26Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2025-11-14T19:02:31Z"
          }
        ]
      },
      "policyArea": {
        "name": "Science, Technology, Communications",
        "updateDate": "2025-09-18T19:25:35Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-08-01",
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
          "measure-id": "id119s2666",
          "measure-number": "2666",
          "measure-type": "s",
          "orig-publish-date": "2025-08-01",
          "originChamber": "SENATE",
          "update-date": "2026-04-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2666v00",
            "update-date": "2026-04-09"
          },
          "action-date": "2025-08-01",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Foreign Robocall Elimination Act</strong></p><p>This bill establishes an interagency task force on unlawful\u00a0robocalls to advise federal agencies and Congress on combating robocalls made from outside of the United States.</p><p>The bill also increases the term applicable to the Federal Communications Commission\u2019s designation of an industry-led consortium to trace the origin of suspected unlawful\u00a0robocalls. Under current law, the commission must annually seek applications from industry groups to serve as the designated consortium; under the bill, the commission must seek applications once every three years.</p>"
        },
        "title": "Foreign Robocall Elimination Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2666.xml",
    "summary": {
      "actionDate": "2025-08-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Foreign Robocall Elimination Act</strong></p><p>This bill establishes an interagency task force on unlawful\u00a0robocalls to advise federal agencies and Congress on combating robocalls made from outside of the United States.</p><p>The bill also increases the term applicable to the Federal Communications Commission\u2019s designation of an industry-led consortium to trace the origin of suspected unlawful\u00a0robocalls. Under current law, the commission must annually seek applications from industry groups to serve as the designated consortium; under the bill, the commission must seek applications once every three years.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s2666"
    },
    "title": "Foreign Robocall Elimination Act"
  },
  "summaries": [
    {
      "actionDate": "2025-08-01",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Foreign Robocall Elimination Act</strong></p><p>This bill establishes an interagency task force on unlawful\u00a0robocalls to advise federal agencies and Congress on combating robocalls made from outside of the United States.</p><p>The bill also increases the term applicable to the Federal Communications Commission\u2019s designation of an industry-led consortium to trace the origin of suspected unlawful\u00a0robocalls. Under current law, the commission must annually seek applications from industry groups to serve as the designated consortium; under the bill, the commission must seek applications once every three years.</p>",
      "updateDate": "2026-04-09",
      "versionCode": "id119s2666"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2666is.xml"
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
      "title": "Foreign Robocall Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-13T12:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Foreign Robocall Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the Federal Communications Commission to establish a taskforce on unlawful robocalls, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:48:36Z"
    }
  ]
}
```
