# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2668?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2668
- Title: HOME Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2668
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-12-05T21:59:28Z
- Update date including text: 2025-12-05T21:59:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2668",
    "number": "2668",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Housing and Community Development"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "HOME Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:59:28Z",
    "updateDateIncludingText": "2025-12-05T21:59:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-01",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
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
        "item": {
          "date": "2025-08-01T22:51:55Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2668is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2668\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Ms. Rosen introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo protect consumers from price gouging of residential rental and sale prices, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Housing Oversight and Mitigating Exploitation Act of 2025 or the HOME Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Affordable housing crisis period**\nThe term affordable housing crisis period means the period during which the prohibition under section 3(a)(1) applies in the United States.\n**(2) Secretary**\nThe term Secretary means the Secretary of Housing and Urban Development.\n**(3) Single-family housing**\nThe term single-family housing means a residence consisting of 1 to 4 dwelling units, but does not include a dwelling unit in a condominium or cooperative housing project.\n**(4) United States**\nThe term United States includes each of the 50 States, the District of Columbia, and any territory or possession of the United States.\n#### 3. Unconscionable pricing of residential rental and sale prices during affordable housing crises\n##### (a) Unconscionable pricing\n**(1) Prohibition**\nIf the Secretary publishes in the Federal Register a determination that the United States is experiencing an affordable housing crisis, it shall be unlawful, during the affordable housing crisis period, for any person to rent a dwelling unit or sell any single-family housing in the United States at a price that\u2014\n**(A)**\nis unconscionably excessive; and\n**(B)**\nindicates the lessor or seller is exploiting the circumstances related to an affordable housing crisis to increase prices unreasonably.\n**(2) Considerations for affordable housing crisis determination**\nFor purposes of determining whether the United States is experiencing an affordable housing crisis, the Secretary shall consider\u2014\n**(A)**\nthe interest rates applicable to mortgage loans;\n**(B)**\nthe effective Federal funds rate;\n**(C)**\nthe refinance rates applicable to mortgage loans, including for fixed-fixed loans, fixed-variable loans, and variable-fixed loans;\n**(D)**\nthe median rental home price in the United States;\n**(E)**\nthe median home sale price in the United States;\n**(F)**\nthe median household income in the United States; and\n**(G)**\nthe declaration of a major disaster or emergency under the section 401 or 501, respectively, of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 , 5191).\n**(3) Duration**\nThe prohibition described in paragraph (1)\u2014\n**(A)**\nmay not apply for a period of more than 30 consecutive days, but may be renewed for such consecutive periods, each not to exceed 30 days, as the Secretary determines appropriate; and\n**(B)**\nmay apply for a period of time not to exceed 1 week before a reasonably foreseeable affordable housing crisis period.\n**(4) Factors considered**\n**(A) In general**\nIn determining whether a person has violated paragraph (1), there shall be taken into account, among other factors, the aggravating factors described in subparagraph (B) and the mitigating factor described in subparagraph (C).\n**(B) Aggravating factors**\nThe aggravating factors described in this subparagraph are the following:\n**(i)**\nWhether the amount charged by such person grossly exceeds the average price at which the housing unit was offered for rental or sale by such person during\u2014\n**(I)**\nthe 30-day period before the date on which the determination that the area is experiencing an affordable housing crisis was made under paragraph (1); or\n**(II)**\nanother appropriate benchmark period, as determined by the Secretary.\n**(ii)**\nWhether the amount charged by such person grossly exceeds the price at which the same or a similar housing unit was readily obtainable for rental or purchase in the same area from other sellers during the affordable housing crisis period.\n**(C) Mitigating factor**\nThe mitigating factor described in this subparagraph is whether the quantity of any housing dwelling units such person made available for rental or sale in an area covered by the affordable housing crisis period during the 30-day period following the date on which the affordable housing crisis period was determined increased over the quantity such person made available for rental or sale during the 30-day period before the date on which the affordable housing crisis period was determined, taking into account any usual seasonal demand variation.\n**(5) Advance notice**\nThe Secretary shall provide advance notice prior to the publication of the determination under paragraph (1) for persons to comply with the prohibition described in paragraph (1).\n##### (b) Affirmative defense\nIt shall be an affirmative defense in any civil action or administrative action to enforce subsection (a), with respect to the renting out or sale of housing by a person, that the increase in the rental or sale price of such housing reasonably reflects additional costs that were paid, incurred, or reasonably anticipated by such person, or reasonably reflects additional risks taken by such person, to rent or sell such housing unit under the circumstances.\n##### (c) Rule of construction\nThis section may not be construed to cover a transaction on a futures market.\n##### (d) Enforcement\n**(1) HUD**\nThe Secretary shall enforce violations of subsection (a) of this section\u2014\n**(A)**\nin the same manner, by the same means, and with the same jurisdiction, powers, and duties as the Federal Trade Commission has under the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) with respect to violations of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of such Act ( 15 U.S.C. 57a(a)(1)(B) ); and\n**(B)**\nas though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section, except that any reference in such terms and provisions to the Commission shall be treated as referring to the Secretary.\n**(2) Enforcement at retail level by State Attorneys General**\n**(A) In general**\nIf the chief law enforcement officer of a State, or an official or agency designated by a State, has reason to believe that any person has violated or is violating subsection (a), the chief law enforcement officer, official, or agency of the State, in addition to any authority it may have to bring an action in State court under its laws, may bring a civil action in any appropriate United States district court or in any other court of competent jurisdiction to\u2014\n**(i)**\nenjoin further such violation by such person;\n**(ii)**\nenforce compliance with such subsection;\n**(iii)**\nobtain civil penalties; and\n**(iv)**\nobtain damages, restitution, or other compensation on behalf of residents of the State.\n**(B) Notice**\nThe State shall serve written notice to the Secretary of any civil action under subparagraph (A) before initiating such civil action. The notice shall include a copy of the complaint to be filed to initiate such civil action, except that if it is not feasible for the State to provide such prior notice, the State shall provide such notice immediately upon instituting such civil action.\n**(C) Authority to intervene**\nUpon receipt of the notice required by subparagraph (B), the Secretary may intervene in such civil action and upon intervening\u2014\n**(i)**\nbe heard on all matters arising in such civil action; and\n**(ii)**\nfile petitions for appeal of a decision in such civil action.\n**(D) Construction**\nFor purposes of bringing any civil action under subparagraph (A), nothing in this paragraph shall prevent the chief law enforcement officer of a State from exercising the powers conferred on the chief law enforcement officer by the laws of such State to conduct investigations or to administer oaths or affirmations or to compel the attendance of witnesses or the production of documentary and other evidence.\n**(E) Limitation on state action while Federal action is pending**\nIf the Secretary has instituted a civil action or an administrative action for violation of subsection (a), a chief law enforcement officer, official, or agency of a State may not bring an action under this paragraph during the pendency of that action against any defendant named in the complaint of the Secretary or another agency for any violation of this Act alleged in the complaint.\n**(F) Rule of construction**\nThis paragraph may not be construed to prohibit an authorized State official from proceeding in State court to enforce a civil or criminal statute of such State.\n##### (e) Low-Income housing assistance\n**(1) Deposit of funds**\nAmounts collected in any penalty under subsection (d)(1) shall be deposited in the Housing Trust Fund established under section 1338 of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568 ).\n**(2) Use of funds**\nTo the extent provided for in advance in appropriations Acts, the amounts deposited in the Fund shall be used to increase and preserve the supply of rental housing affordable to extremely low- and very low-income families, including homeless families, in accordance with section 1338 of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4568 ).\n##### (f) Effect on other laws\n**(1) Other authority of Federal Housing Administration**\nNothing in this section may be construed to limit the authority of the Secretary under any other provision of law.\n**(2) State law**\nNothing in this section preempts any State law.\n#### 4. HUD investigation and report on housing prices\n##### (a) Investigation\n**(1) In general**\nThe Secretary shall conduct an investigation to determine if the prices for rental housing units or sale of single-family housing are being manipulated by reducing housing capacity or by any other form of market manipulation or artificially increased by price gouging practices.\n**(2) Consideration**\nIn conducting the investigation under paragraph (1), the Secretary may consider the impact of mergers and acquisitions in the real estate industry, including mergers and acquisitions involving developers, managers, owners, and investors.\n##### (b) Report\n**(1) In general**\nNot later than 270 days after the date of enactment of this Act, the Secretary shall submit to the Congress a report on the investigation conducted under subsection (a).\n**(2) Contents**\nThe report shall include\u2014\n**(A)**\na long-term strategy for the Department of Housing and Urban Development and the Congress to address manipulation of rental housing markets and markets for sale of single-family housing, and in preparing the strategy the Secretary shall utilize data on race, gender, and socioeconomic status; and\n**(B)**\na description and analysis of how non-occupant investors in single-family housing impact underserved communities.\n##### (c) Exemption from Paperwork Reduction Act\nChapter 35 of title 44, United States Code, shall not apply to the collection of information under subsection (a).\n##### (d) Authorization of appropriations\nThere is authorized to be appropriated to the Secretary to carry out this section $1,000,000 for fiscal year 2024.\n#### 5. Housing cost monitoring and enforcement within HUD\n##### (a) In general\nThe Secretary shall establish within the Department of Housing and Urban Development the Housing Monitoring and Enforcement Unit (in this section referred to as the Unit ).\n##### (b) Duties of the unit\n**(1) Primary responsibility**\nThe primary responsibility of the Unit shall be to assist the Secretary in protecting the public interest by continuously and comprehensively collecting, monitoring, and analyzing rental housing market data, data for markets for sale of single-family housing, and data on investor-owned, non-owner occupied housing units, in order to\u2014\n**(A)**\nsupport transparent and competitive market practices;\n**(B)**\nidentify any market manipulation, including by collecting and analyzing data on race, gender, and socioeconomic status, any reporting of false information, any use of market power to disadvantage consumers, or any other unfair method of competition; and\n**(C)**\nfacilitate enforcement of penalties against persons in violation of relevant statutory prohibitions.\n**(2) Specific duties**\nIn order to carry out the responsibility under paragraph (1), the Unit shall assist the Secretary in carrying out the following duties:\n**(A)**\nReceiving, compiling, and analyzing relevant buying and selling activity in order to identify and investigate anomalous market trends and suspicious behavior.\n**(B)**\nDetermining whether excessive concentration or exclusive control of housing-related infrastructure may allow or result in anti-competitive behaviors.\n**(C)**\nObtaining a data-sharing agreement with State and local jurisdictions, housing agencies, and relevant public and private data sources to receive and archive information on housing purchases by institutional investors within a given area.\n#### 6. Investigations of excessive housing purchases\nThe Secretary shall monitor purchases of single-family housing in each housing market area in the United States, as determined by the Secretary, to determine whether any single purchaser of such housing, including any purchaser that is an institutional investor, is purchasing an excessive amount of such housing made available for sale in any such market area. If the Secretary determines that any single purchaser has purchased more than 5 percent of the single-family housing made available for sale in any market area over a 3-year period, or if, in aggregate, large institutional investors have purchased more than 25 percent of the single-family housing made available for sale in any market area over a 1-year period, the Secretary shall conduct an investigation to determine the purposes of and circumstances involved in such purchases, including price gouging, market manipulation, and unfair investment practices that drive homeowners out of the market.\n#### 7. Identification of unfair screening practices\nThe Secretary, the Federal Trade Commission, and the Bureau of Consumer Financial Protection shall jointly\u2014\n**(1)**\ncarry out a program to collect information to identify practices that unfairly prevent applicants and tenants of rental housing from accessing or staying in housing, including the establishment and use of tenant or applicant background checks, the use of algorithms in tenant screenings, the provision of adverse action notices by landlords and property management companies, and the use of information regarding tenant income sources; and\n**(2)**\nsubmit a report to the Congress annually describing the information collected under the program carried out pursuant to paragraph (1).\n#### 8. Limitation on Fannie Mae and Freddie Mac investments\nSubpart A of part 2 of subtitle A of the Federal Housing Enterprises Financial Safety and Soundness Act of 1992 ( 12 U.S.C. 4541 et seq. ) is amended by adding at the end the following new section:\n1329. Limitation on enterprise investments The Director shall, by regulations issued after notice and opportunity for interested parties to comment at a public hearing, establish standards and criteria for the purchase by the enterprises of mortgages on multifamily rental housing as the Director considers necessary to ensure basic renter protections and prevent egregious rent increases for tenants in such housing. .\n#### 9. Review of anti-competitive behaviors\nThe Attorney General and the Federal Trade Commission shall jointly conduct a review to identify any anti-competitive behaviors in the single-family housing and residential rental markets, including anti-competitive information sharing, and not later than 1 year after the date of enactment of this Act shall submit a report to the Congress setting forth the findings of such review.",
      "versionDate": "2025-08-01",
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
        "actionDate": "2025-05-06",
        "text": "Referred to the Committee on Financial Services, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3214",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "HOME Act of 2025",
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
        "name": "Housing and Community Development",
        "updateDate": "2025-09-18T19:21:38Z"
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
      "date": "2025-08-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2668is.xml"
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
      "title": "HOME Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-21T12:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HOME Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Housing Oversight and Mitigating Exploitation Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-09T03:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to protect consumers from price gouging of residential rental and sale prices, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-09T03:34:01Z"
    }
  ]
}
```
