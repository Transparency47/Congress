# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/314?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/314
- Title: Hotel Fees Transparency Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 314
- Origin chamber: Senate
- Introduced date: 2025-01-29
- Update date: 2025-10-09T03:26:24Z
- Update date including text: 2025-10-09T03:26:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-29: Introduced in Senate
- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 49.
- 2025-05-14 - Floor: Star Print ordered on the reported bill.
- Latest action: 2025-01-29: Introduced in Senate

## Actions

- 2025-01-29 - IntroReferral: Introduced in Senate
- 2025-01-29 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- 2025-02-05 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.
- 2025-04-28 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 49.
- 2025-05-14 - Floor: Star Print ordered on the reported bill.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-29",
    "latestAction": {
      "actionDate": "2025-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/314",
    "number": "314",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "K000367",
        "district": "",
        "firstName": "Amy",
        "fullName": "Sen. Klobuchar, Amy [D-MN]",
        "lastName": "Klobuchar",
        "party": "D",
        "state": "MN"
      }
    ],
    "title": "Hotel Fees Transparency Act of 2025",
    "type": "S",
    "updateDate": "2025-10-09T03:26:24Z",
    "updateDateIncludingText": "2025-10-09T03:26:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Star Print ordered on the reported bill.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 49.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
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
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment. With written report No. 119-15.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-01-29",
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
      "actionDate": "2025-01-29",
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
            "date": "2025-04-28T20:09:52Z",
            "name": "Reported By"
          },
          {
            "date": "2025-02-05T15:00:22Z",
            "name": "Markup By"
          },
          {
            "date": "2025-01-29T21:18:02Z",
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
      "bioguideId": "M000934",
      "firstName": "Jerry",
      "fullName": "Sen. Moran, Jerry [R-KS]",
      "isOriginalCosponsor": "True",
      "lastName": "Moran",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "KS"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2025-01-29",
      "state": "NV"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-01-29",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s314is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 314\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Klobuchar (for herself, Mr. Moran , Ms. Cortez Masto , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo prohibit unfair and deceptive advertising of prices for hotel rooms and other places of short-term lodging, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hotel Fees Transparency Act of 2025 .\n#### 2. Prohibition on unfair and deceptive advertising of hotel rooms and other short-term rental prices\n##### (a) Prohibition\n**(1) In general**\nIt shall be unlawful for a covered entity to display, advertise, market, or offer in interstate commerce, including through direct offerings, third-party distribution, or metasearch referrals, a price for covered services that does not clearly, conspicuously, and prominently\u2014\n**(A)**\ndisplay the total services price, if a price is displayed, in any advertisement, marketing, or price list wherever the covered services are displayed, advertised, marketed, or offered for sale;\n**(B)**\ndisclose to any individual who seeks to purchase covered services the total services price at the time the covered services are first displayed to the individual and anytime thereafter throughout the covered services purchasing process; and\n**(C)**\ndisclose, prior to the final purchase, any tax, fee, or assessment imposed by any government entity, quasi-government entity, or government-created special district or program on the sale of covered services.\n**(2) Individual components**\nProvided that such displays are less prominent than the total service price required in paragraph (1), nothing in this Act shall be construed to prohibit the display of\u2014\n**(A)**\nindividual components of the total price; or\n**(B)**\ndetails of other items not required by paragraph (1).\n**(3) Indemnification provisions**\nNothing in this section shall be construed to prohibit any covered entity from entering into a contract with any other covered entity that contains an indemnification provision with respect to price or fee information disclosed, exchanged, or shared between the covered entities that are parties to the contract.\n##### (b) Enforcement\n**(1) Enforcement by the Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of subsection (a) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of the Commission**\n**(i) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(ii) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(iii) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(2) Enforcement by States**\n**(A) In general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates subsection (a), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(B) Rights of the Commission**\n**(i) Notice to the Commission**\n**(I) In general**\nExcept as provided in subclause (III), the attorney general of a State, before initiating a civil action under subparagraph (A) shall notify the Commission in writing that the attorney general intends to bring such civil action.\n**(II) Contents**\nThe notification required by subclause (I) shall include a copy of the complaint to be filed to initiate the civil action.\n**(III) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by subclause (I) before initiating a civil action under subparagraph (A), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(ii) Intervention by the Commission**\nThe Commission may\u2014\n**(I)**\nintervene in any civil action brought by the attorney general of a State under subparagraph (A); and\n**(II)**\nupon intervening\u2014\n**(aa)**\nbe heard on all matters arising in the civil action; and\n**(bb)**\nfile petitions for appeal.\n**(C) Investigatory powers**\nNothing in this paragraph may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(D) Action by the Commission**\nWhenever a civil action has been instituted by or on behalf of the Commission for violation of subsection (a), no attorney general of a State may, during the pendency of that action, institute an action under subparagraph (A) against any defendant named in the complaint in that action for a violation of subsection (a) alleged in such complaint.\n**(E) Venue; service of process**\n**(i) Venue**\nAny action brought under subparagraph (A) may be brought in\u2014\n**(I)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(II)**\nanother court of competent jurisdiction.\n**(ii) Service of process**\nIn an action brought under subparagraph (A), process may be served in any district in which\u2014\n**(I)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(II)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(F) Actions by other State officials**\n**(i) In general**\nIn addition to civil actions brought by an attorney general under subparagraph (A), any other officer of a State who is authorized by the State to do so may bring a civil action under subparagraph (A), subject to the same requirements and limitations that apply under this paragraph to civil actions brought by attorneys general.\n**(ii) Savings provision**\nNothing in this paragraph may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n**(3) Affirmative defense**\nIn any action pursuant to paragraph (1) or (2), an intermediary or third-party online seller may assert an affirmative defense if such intermediary or third-party online seller\u2014\n**(A)**\nestablished procedures to receive up-to-date price information from hotels or short-term rentals, or agents acting on behalf of a hotel or short-term rental;\n**(B)**\nrelied in good faith on information provided to the intermediary or third-party online seller by a hotel or short-term rental, or agent acting on behalf of such hotel or short-term rental, and such information was inaccurate at the time it was provided to the intermediary or third-party online seller; and\n**(C)**\ntook prompt action to remove or correct any false or inaccurate information about the total services price after receiving notice that such information was false or inaccurate.\n##### (c) Preemption\n**(1) In general**\nA State, or political subdivision of a State, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of the State, that prohibits a covered entity from advertising, displaying, marketing, or otherwise offering, or otherwise affects the manner in which a covered entity may advertise, display, market, or otherwise offer, for sale in interstate commerce, including through a direct offering, third-party distribution, or metasearch referral, a price of a reservation for a covered service, and that requires fee disclosure, unless the law requires the total services price to include each service fee, as defined in subsection (d)(8), and in accordance with subsection (a)(1).\n**(2) Rule of Construction**\nThis section may not be construed to\u2014\n**(A)**\npreempt any law of a State or political subdivision of a State relating to contracts or torts; or\n**(B)**\npreempt any law of a State or political subdivision of a State to the extent that such law relates to an act of fraud, unauthorized access to personal information, or notification of unauthorized access to personal information.\n##### (d) Definitions\nIn this Act:\n**(1) Base services price**\nThe term base services price \u2014\n**(A)**\nmeans, with respect to the covered services provided by a hotel or short-term rental, the price in order to obtain the covered services of the hotel or short-term rental; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany service fee;\n**(ii)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(iii)**\nassessment fees of a government-created special district or program; or\n**(iv)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\nThe term covered entity means a person, partnership, or corporation with respect to whom the Commission has jurisdiction under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ), including\u2014\n**(A)**\na hotel or short-term rental;\n**(B)**\na third-party online seller; or\n**(C)**\nan intermediary.\n**(4) Covered services**\nThe term covered services \u2014\n**(A)**\nmeans the temporary provision of a room, building, or other lodging facility; and\n**(B)**\ndoes not include the provision of a meeting room, banquet services, or catering services.\n**(5) Hotel**\nThe term hotel means an establishment that is\u2014\n**(A)**\nprimarily engaged in providing a covered service to the general public; and\n**(B)**\npromoted, advertised, or marketed in interstate commerce or for which such establishment's services are sold in interstate commerce.\n**(6) Intermediary**\nThe term intermediary means an entity that operates either as a business-to-business platform, consumer-facing platform, or both, that displays, including through direct offerings, third-party distribution, or metasearch referral, a price for covered services or price comparison tools for consumers seeking covered services.\n**(7) Optional product or service**\nThe term optional product or service means a product or service that an individual does not need to purchase to use or obtain covered services\n**(8) Service fee**\nThe term service fee \u2014\n**(A)**\nmeans a charge imposed by a covered entity that must be paid in order to obtain covered services; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(ii)**\nany assessment fees of a government-created special district or program; or\n**(iii)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n**(9) Short-term rental**\nThe term short-term rental means a property, including a single-family dwelling or a unit in a condominium, cooperative, or time-share, that provides covered services (either with respect to the entire property or a part of the property) to the general public\u2014\n**(A)**\nin exchange for a fee;\n**(B)**\nfor periods shorter than 30 consecutive days; and\n**(C)**\nis promoted, advertised, or marketed in interstate commerce or for which such property\u2019s services are sold in interstate commerce.\n**(10) State**\nThe term State means each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n**(11) Third-party online seller**\nThe term third-party online seller means any person other than a hotel or short-term rental that sells covered services or offers for sale covered services with respect to a hotel or short-term rental in a transaction facilitated on the internet.\n**(12) Total services price**\nThe term total services \u2014\n**(A)**\nmeans, with respect to covered services, the total cost of the covered services, including the base services price and any service fees; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(ii)**\nany assessment fees of a government-created special district or program; or\n**(iii)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n##### (e) Effective date\nThe prohibition under subsection (a) shall take effect 450 days after the date of the enactment of this Act and shall apply to advertisements, displays, marketing, and offers of covered services of a covered entity made on or after such date.",
      "versionDate": "2025-01-29",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s314rs.xml",
      "text": "II\nCalendar No. 49\n119th CONGRESS\n1st Session\nS. 314\n[Report No. 119\u201315]\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2025 Ms. Klobuchar (for herself, Mr. Moran , Ms. Cortez Masto , and Mrs. Capito ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 28, 2025 Reported by Mr. Cruz , with an amendment Insert the part printed in italic\nA BILL\nTo prohibit unfair and deceptive advertising of prices for hotel rooms and other places of short-term lodging, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Hotel Fees Transparency Act of 2025 .\n#### 2. Prohibition on unfair and deceptive advertising of hotel rooms and other short-term rental prices\n##### (a) Prohibition\n**(1) In general**\nIt shall be unlawful for a covered entity to display, advertise, market, or offer in interstate commerce, including through direct offerings, third-party distribution, or metasearch referrals, a price for covered services that does not clearly, conspicuously, and prominently\u2014\n**(A)**\ndisplay the total services price, if a price is displayed, in any advertisement, marketing, or price list wherever the covered services are displayed, advertised, marketed, or offered for sale;\n**(B)**\ndisclose to any individual who seeks to purchase covered services the total services price at the time the covered services are first displayed to the individual and anytime thereafter throughout the covered services purchasing process; and\n**(C)**\ndisclose, prior to the final purchase, any tax, fee, or assessment imposed by any government entity, quasi-government entity, or government-created special district or program on the sale of covered services.\n**(2) Individual components**\nProvided that such displays are less prominent than the total service price required in paragraph (1), nothing in this Act shall be construed to prohibit the display of\u2014\n**(A)**\nindividual components of the total price; or\n**(B)**\ndetails of other items not required by paragraph (1).\n**(3) Indemnification provisions**\nNothing in this section shall be construed to prohibit any covered entity from entering into a contract with any other covered entity that contains an indemnification provision with respect to price or fee information disclosed, exchanged, or shared between the covered entities that are parties to the contract.\n##### (b) Enforcement\n**(1) Enforcement by the Commission**\n**(A) Unfair or deceptive acts or practices**\nA violation of subsection (a) shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(B) Powers of the Commission**\n**(i) In general**\nThe Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this Act.\n**(ii) Privileges and immunities**\nAny person who violates this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(iii) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(2) Enforcement by States**\n**(A) In general**\nIf the attorney general of a State has reason to believe that an interest of the residents of the State has been or is being threatened or adversely affected by a practice that violates subsection (a), the attorney general of the State may, as parens patriae, bring a civil action on behalf of the residents of the State in an appropriate district court of the United States to obtain appropriate relief.\n**(B) Rights of the Commission**\n**(i) Notice to the Commission**\n**(I) In general**\nExcept as provided in subclause (III), the attorney general of a State, before initiating a civil action under subparagraph (A) shall notify the Commission in writing that the attorney general intends to bring such civil action.\n**(II) Contents**\nThe notification required by subclause (I) shall include a copy of the complaint to be filed to initiate the civil action.\n**(III) Exception**\nIf it is not feasible for the attorney general of a State to provide the notification required by subclause (I) before initiating a civil action under subparagraph (A), the attorney general shall notify the Commission immediately upon instituting the civil action.\n**(ii) Intervention by the Commission**\nThe Commission may\u2014\n**(I)**\nintervene in any civil action brought by the attorney general of a State under subparagraph (A); and\n**(II)**\nupon intervening\u2014\n**(aa)**\nbe heard on all matters arising in the civil action; and\n**(bb)**\nfile petitions for appeal.\n**(C) Investigatory powers**\nNothing in this paragraph may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(D) Action by the Commission**\nWhenever a civil action has been instituted by or on behalf of the Commission for violation of subsection (a), no attorney general of a State may, during the pendency of that action, institute an action under subparagraph (A) against any defendant named in the complaint in that action for a violation of subsection (a) alleged in such complaint.\n**(E) Venue; service of process**\n**(i) Venue**\nAny action brought under subparagraph (A) may be brought in\u2014\n**(I)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(II)**\nanother court of competent jurisdiction.\n**(ii) Service of process**\nIn an action brought under subparagraph (A), process may be served in any district in which\u2014\n**(I)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(II)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(F) Actions by other State officials**\n**(i) In general**\nIn addition to civil actions brought by an attorney general under subparagraph (A), any other officer of a State who is authorized by the State to do so may bring a civil action under subparagraph (A), subject to the same requirements and limitations that apply under this paragraph to civil actions brought by attorneys general.\n**(ii) Savings provision**\nNothing in this paragraph may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n**(3) Affirmative defense**\nIn any action pursuant to paragraph (1) or (2), an intermediary or third-party online seller may assert an affirmative defense if such intermediary or third-party online seller\u2014\n**(A)**\nestablished procedures to receive up-to-date price information from hotels or short-term rentals, or agents acting on behalf of a hotel or short-term rental;\n**(B)**\nrelied in good faith on information provided to the intermediary or third-party online seller by a hotel or short-term rental, or agent acting on behalf of such hotel or short-term rental, and such information was inaccurate at the time it was provided to the intermediary or third-party online seller; and\n**(C)**\ntook prompt action to remove or correct any false or inaccurate information about the total services price after receiving notice that such information was false or inaccurate.\n##### (c) Preemption\n**(1) In general**\nA State, or political subdivision of a State, may not maintain, enforce, prescribe, or continue in effect any law, rule, regulation, requirement, standard, or other provision having the force and effect of law of the State, or political subdivision of the State, that prohibits a covered entity from advertising, displaying, marketing, or otherwise offering, or otherwise affects the manner in which a covered entity may advertise, display, market, or otherwise offer, for sale in interstate commerce, including through a direct offering, third-party distribution, or metasearch referral, a price of a reservation for a covered service, and that requires fee disclosure, unless the law requires the total services price to include each service fee, as defined in subsection (d)(8), and in accordance with subsection (a)(1).\n**(2) Rule of Construction**\nThis section may not be construed to\u2014\n**(A)**\npreempt any law of a State or political subdivision of a State relating to contracts or torts; or\n**(B)**\npreempt any law of a State or political subdivision of a State to the extent that such law relates to an act of fraud, unauthorized access to personal information, or notification of unauthorized access to personal information.\n##### (d) Definitions\nIn this Act:\n**(1) Base services price**\nThe term base services price \u2014\n**(A)**\nmeans, with respect to the covered services provided by a hotel or short-term rental, the price in order to obtain the covered services of the hotel or short-term rental; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany service fee;\n**(ii)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(iii)**\nassessment fees of a government-created special district or program; or\n**(iv)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered entity**\nThe term covered entity means a person, partnership, or corporation with respect to whom the Commission has jurisdiction under section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ), including\u2014\n**(A)**\na hotel or short-term rental;\n**(B)**\na third-party online seller; or\n**(C)**\nan intermediary.\n**(4) Covered services**\nThe term covered services \u2014\n**(A)**\nmeans the temporary provision of a room, building, or other lodging facility; and\n**(B)**\ndoes not include the provision of a meeting room, banquet services, or catering services.\n**(5) Hotel**\nThe term hotel means an establishment that is\u2014\n**(A)**\nprimarily engaged in providing a covered service to the general public; and\n**(B)**\npromoted, advertised, or marketed in interstate commerce or for which such establishment's services are sold in interstate commerce.\n**(6) Intermediary**\nThe term intermediary means an entity that operates either as a business-to-business platform, consumer-facing platform, or both, that displays, including through direct offerings, third-party distribution, or metasearch referral, a price for covered services or price comparison tools for consumers seeking covered services.\n**(7) Optional product or service**\nThe term optional product or service means a product or service that an individual does not need to purchase to use or obtain covered services\n**(8) Service fee**\nThe term service fee \u2014\n**(A)**\nmeans a charge imposed by a covered entity that must be paid in order to obtain covered services; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(ii)**\nany assessment fees of a government-created special district or program; or\n**(iii)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n**(9) Short-term rental**\nThe term short-term rental means a property, including a single-family dwelling or a unit in a condominium, cooperative, or time-share, that provides covered services (either with respect to the entire property or a part of the property) to the general public\u2014\n**(A)**\nin exchange for a fee;\n**(B)**\nfor periods shorter than 30 consecutive days; and\n**(C)**\nis promoted, advertised, or marketed in interstate commerce or for which such property\u2019s services are sold in interstate commerce.\n**(10) State**\nThe term State means each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n**(11) Third-party online seller**\nThe term third-party online seller means any person other than a hotel or short-term rental that sells covered services or offers for sale covered services with respect to a hotel or short-term rental in a transaction facilitated on the internet.\n**(12) Total services price**\nThe term total services price \u2014\n**(A)**\nmeans, with respect to covered services, the total cost of the covered services, including the base services price and any service fees; and\n**(B)**\ndoes not include\u2014\n**(i)**\nany taxes or fees imposed by a government or quasi-government entity;\n**(ii)**\nany assessment fees of a government-created special district or program; or\n**(iii)**\nany charges or fees for an optional product or service associated with the covered services that may be selected by a purchaser of covered services.\n##### (e) Effective date\nThe prohibition under subsection (a) shall take effect 450 days after the date of the enactment of this Act and shall apply to advertisements, displays, marketing, and offers of covered services of a covered entity made on or after such date.",
      "versionDate": "2025-04-28",
      "versionType": "Reported in Senate"
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
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Inflation and prices",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Landlord and tenant",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Marketing and advertising",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "Service industries",
            "updateDate": "2025-03-20T13:45:38Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-03-20T13:45:38Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-02-26T21:09:33Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-29",
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
          "measure-id": "id119s314",
          "measure-number": "314",
          "measure-type": "s",
          "orig-publish-date": "2025-01-29",
          "originChamber": "SENATE",
          "update-date": "2025-05-28"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s314v00",
            "update-date": "2025-05-28"
          },
          "action-date": "2025-01-29",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>Hotel Fees Transparency Act of 2025</strong></p><p>This bill requires providers of short-term lodging (e.g., hotels, short-term rentals, and third-party online sellers) to include certain price information when displaying, advertising, or marketing reservations for lodging.</p><p>Specifically, such providers must\u00a0(1) display the total services price, including the base price and any service fees, if a price is displayed in an advertisement. marketing material, or a price list;\u00a0(2) disclose the total services price at the time the services are first displayed to an individual seeking to purchase such services and anytime thereafter during the purchasing process; and\u00a0(3) disclose, prior to the final purchase, any tax, fee, or assessment imposed\u00a0by any government entity (or quasi-government entity) on the sale of such services.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials).</p>"
        },
        "title": "Hotel Fees Transparency Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s314.xml",
    "summary": {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hotel Fees Transparency Act of 2025</strong></p><p>This bill requires providers of short-term lodging (e.g., hotels, short-term rentals, and third-party online sellers) to include certain price information when displaying, advertising, or marketing reservations for lodging.</p><p>Specifically, such providers must\u00a0(1) display the total services price, including the base price and any service fees, if a price is displayed in an advertisement. marketing material, or a price list;\u00a0(2) disclose the total services price at the time the services are first displayed to an individual seeking to purchase such services and anytime thereafter during the purchasing process; and\u00a0(3) disclose, prior to the final purchase, any tax, fee, or assessment imposed\u00a0by any government entity (or quasi-government entity) on the sale of such services.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials).</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s314"
    },
    "title": "Hotel Fees Transparency Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-29",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>Hotel Fees Transparency Act of 2025</strong></p><p>This bill requires providers of short-term lodging (e.g., hotels, short-term rentals, and third-party online sellers) to include certain price information when displaying, advertising, or marketing reservations for lodging.</p><p>Specifically, such providers must\u00a0(1) display the total services price, including the base price and any service fees, if a price is displayed in an advertisement. marketing material, or a price list;\u00a0(2) disclose the total services price at the time the services are first displayed to an individual seeking to purchase such services and anytime thereafter during the purchasing process; and\u00a0(3) disclose, prior to the final purchase, any tax, fee, or assessment imposed\u00a0by any government entity (or quasi-government entity) on the sale of such services.</p><p>The bill provides for enforcement by the Federal Trade Commission and state attorneys general (or other authorized state officials).</p>",
      "updateDate": "2025-05-28",
      "versionCode": "id119s314"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s314is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s314rs.xml"
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
      "title": "Hotel Fees Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-15T11:03:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Hotel Fees Transparency Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-04-30T03:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Hotel Fees Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T15:23:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit unfair and deceptive advertising of prices for hotel rooms and other places of short-term lodging, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T15:18:19Z"
    }
  ]
}
```
