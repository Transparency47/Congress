# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4528?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4528
- Title: Price Gouging Prevention Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4528
- Origin chamber: House
- Introduced date: 2025-07-17
- Update date: 2026-02-24T09:05:38Z
- Update date including text: 2026-02-24T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-17: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-07-17: Introduced in House

## Actions

- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Introduced in House
- 2025-07-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-17 - IntroReferral: Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-17",
    "latestAction": {
      "actionDate": "2025-07-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4528",
    "number": "4528",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "S001145",
        "district": "9",
        "firstName": "Janice",
        "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
        "lastName": "Schakowsky",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Price Gouging Prevention Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-24T09:05:38Z",
    "updateDateIncludingText": "2026-02-24T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-07-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Financial Services, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-07-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-07-17",
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
          "date": "2025-07-17T13:06:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-07-17T13:06:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "DC"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "PA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MI"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "WA"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CA"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "GA"
    },
    {
      "bioguideId": "D000216",
      "district": "3",
      "firstName": "Rosa",
      "fullName": "Rep. DeLauro, Rosa L. [D-CT-3]",
      "isOriginalCosponsor": "True",
      "lastName": "DeLauro",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "CT"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "MN"
    },
    {
      "bioguideId": "G000604",
      "district": "2",
      "firstName": "Maggie",
      "fullName": "Rep. Goodlander, Maggie [D-NH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Goodlander",
      "party": "D",
      "sponsorshipDate": "2025-07-17",
      "state": "NH"
    },
    {
      "bioguideId": "F000477",
      "district": "4",
      "firstName": "Valerie",
      "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Foushee",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "NC"
    },
    {
      "bioguideId": "C001131",
      "district": "35",
      "firstName": "Greg",
      "fullName": "Rep. Casar, Greg [D-TX-35]",
      "isOriginalCosponsor": "False",
      "lastName": "Casar",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "TX"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4528ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4528\nIN THE HOUSE OF REPRESENTATIVES\nJuly 17, 2025 Ms. Schakowsky (for herself, Mr. Deluzio , Ms. Norton , Mr. Nadler , Ms. Scanlon , Ms. Tlaib , Ms. Jayapal , Mr. Tonko , Mr. Khanna , Mr. Johnson of Georgia , Ms. DeLauro , Ms. Craig , and Ms. Goodlander ) introduced the following bill; which was referred to the Committee on Energy and Commerce , and in addition to the Committee on Financial Services , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo make price gouging unlawful, to expand the ability of the Federal Trade Commission to seek permanent injunctions and equitable relief, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Price Gouging Prevention Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Definitions.\nSec. 3. Prevention of price gouging.\nSec. 4. Disclosures in SEC filings.\nSec. 5. Funding.\n#### 2. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Federal Trade Commission.\n**(2) Critical trading partner**\nThe term critical trading partner means a person that has the ability to restrict, impede, or foreclose access to the inputs, customers, partners, goods, services, technology, platform, facilities, or tools of such person in a way that harms competition or limits the ability of the customers or suppliers of such person to carry out business effectively.\n**(3) Exceptional market shock**\nThe term exceptional market shock means\u2014\n**(A)**\nany change or imminently threatened (as determined under guidance issued by the Commission) change in the market for a good or service resulting from a natural disaster, failure or shortage of electric power or other source of energy, concerted labor action, lockout, civil disorder, war, military action, national or local emergency, abrupt or significant shift in trade policy, public health emergency, or any other cause of an atypical disruption in such market; or\n**(B)**\nany period of time during which the President has declared a major disaster or emergency under section 401 or 502, respectively, of the Robert T. Stafford Disaster Relief and Emergency Assistance Act ( 42 U.S.C. 5170 , 5191).\n**(4) Good or service**\nThe term good or service means any good or service offered in commerce.\n**(5) State**\nThe term State means each of the several States, the District of Columbia, each commonwealth, territory, or possession of the United States, and each federally recognized Indian Tribe.\n**(6) Ultimate parent entity**\nThe term ultimate parent entity has the meaning given such term in section 801.1 of title 16, Code of Federal Regulations (or any successor regulation).\n#### 3. Prevention of price gouging\n##### (a) In general\nIt shall be unlawful for a person to sell or offer for sale a good or service at a grossly excessive price, regardless of the person\u2019s position in a supply chain or distribution network.\n##### (b) Affirmative defense\n**(1) In general**\nSubsection (a) shall not apply to the sale, or offering for sale, of a good or service by a person if\u2014\n**(A)**\nthe person\u2019s ultimate parent entity earned less than $100,000,000 in gross revenue from goods or services provided in the United States during the 12-month period preceding the sale or offer that allegedly violates subsection (a); and\n**(B)**\nthe person demonstrates by a preponderance of the evidence that the increase in the price of the good or service involved is directly attributable to additional costs that are\u2014\n**(i)**\nnot within the control of the person; and\n**(ii)**\nincurred by the person in procuring, acquiring, distributing, or providing the good or service.\n**(2) Inflation adjustment**\nBeginning on January 1, 2026, the Commission shall annually adjust the amount specified in paragraph (1)(A) by the percentage change in the consumer price index for all urban consumers published by the Bureau of Labor Statistics for the 12-month period ending on December 31 of the previous year.\n##### (c) Presumptive violations\nA person shall be presumed to be in violation of subsection (a) if, during an exceptional market shock, it is shown by a preponderance of the evidence that the person\u2014\n**(1)**\n**(A)**\nhas unfair leverage; or\n**(B)**\nis using the effects or circumstances related to an exceptional market shock as a pretext to increase prices; and\n**(2)**\nregardless of the person's position in a supply chain or distribution network, sells or offers for sale a good or service at an excessive price compared to\u2014\n**(A)**\nthe average price at which the good or service was sold or offered for sale by the person in the market during the 120-day period preceding such exceptional market shock; or\n**(B)**\nthe price at which the good or service was sold or offered for sale by competing sellers in the market during the exceptional market shock.\n##### (d) Rebuttal\nA person may rebut a presumption under subsection (c) if the person demonstrates by clear and convincing evidence that the increase in the price of the good or service involved is directly attributable to additional costs that are\u2014\n**(1)**\nnot within the control of the person; and\n**(2)**\nincurred by the person in procuring, acquiring, distributing, or providing the good or service.\n##### (e) Unfair leverage\n**(1) In general**\n**(A) Characteristics of unfair leverage**\nFor purposes of subsection (c), a person has unfair leverage if the person\u2014\n**(i)**\nearned at least $1,000,000,000 in gross revenue from goods or services provided in the United States during the 12-month period preceding the sale or offer that allegedly violates subsection (a);\n**(ii)**\ndiscriminates between otherwise equal trading partners in the same market by applying differential prices or conditions;\n**(iii)**\nis a critical trading partner;\n**(iv)**\nengages in unfair, deceptive, or abusive acts or practices;\n**(v)**\nhas a dominant position in\u2014\n**(I)**\nthe conduct of any business, trade, or commerce;\n**(II)**\nany labor market; or\n**(III)**\nthe furnishing of any service; or\n**(vi)**\nhas a characteristic described in a rule promulgated by the Commission that further defines unfair leverage.\n**(B) Presumption of a dominant position**\nFor purposes of subparagraph (A)(v), a person shall be presumed to have a dominant position if\u2014\n**(i)**\nevidence shows that the person is not constrained by meaningful competitive pressures; or\n**(ii)**\nthe person\u2014\n**(I)**\nhas a share of 40 percent or greater of a relevant market as a seller; or\n**(II)**\nhas a share of 30 percent or greater of a relevant market as a buyer.\n**(2) Inflation adjustment**\nBeginning on January 1, 2026, the Commission shall annually adjust the amount specified in paragraph (1)(A)(i) by the percentage change in the consumer price index for all urban consumers published by the Bureau of Labor Statistics for the 12-month period ending on December 31 of the previous year.\n##### (f) Enforcement by the Commission\n**(1) Unfair or deceptive acts or practices**\nA violation of this section or a regulation promulgated under this section shall be treated as a violation of a rule defining an unfair or deceptive act or practice prescribed under section 18(a)(1)(B) of the Federal Trade Commission Act ( 15 U.S.C. 57a(a)(1)(B) ).\n**(2) Powers of the Commission**\n**(A) In general**\nExcept as provided by subparagraphs (D) and (E), the Commission shall enforce this section in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Privileges and immunities**\nAny person who violates this section or a regulation promulgated under this section shall be subject to the penalties and entitled to the privileges and immunities provided in the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ).\n**(C) Authority preserved**\nNothing in this section shall be construed to limit the authority of the Commission under any other provision of law.\n**(D) Independent litigation authority**\nIf the Commission has reason to believe that a person has violated this section, the Commission may bring a civil action in any appropriate United States district court to\u2014\n**(i)**\nenjoin any further such violation by such person;\n**(ii)**\nenforce compliance with this section;\n**(iii)**\nobtain a permanent, temporary, or preliminary injunction;\n**(iv)**\nobtain civil penalties;\n**(v)**\nobtain damages, restitution, or other compensation on behalf of aggrieved consumers; or\n**(vi)**\nobtain any other appropriate equitable relief.\n**(E) Civil penalties**\nIn addition to any other penalties as may be prescribed by law, each violation of this section shall carry a civil penalty not to exceed\u2014\n**(i)**\nif the person who committed the violation does not have unfair leverage (as described in subsection (e)), the lesser of\u2014\n**(I)**\n$25,000; or\n**(II)**\n5 percent of the revenues earned by the person's ultimate parent entity during the preceding 12-month period; or\n**(ii)**\nif the person who committed the violation has unfair leverage, 5 percent of the revenues earned by the person's ultimate parent entity during the preceding 12-month period.\n**(F) Rulemaking**\n**(i) In general**\nThe Commission may promulgate in accordance with section 553 of title 5, United States Code, such rules as may be necessary to carry out this section, including guidelines regarding what circumstances constitute an exceptional market shock or guidelines that provide for additional characteristics that demonstrate that a person has unfair leverage.\n**(ii) Required guidance**\nNot later than 180 days after the date of enactment of this Act, the Commission shall promulgate regulations regarding violations of this section, which shall include guidelines on, for the purposes of this Act, what constitutes a market, a grossly excessive price for a good or service, and an excessive price for a good or service.\n**(iii) Definition of grossly excessive price**\n**(I) In general**\nFor purposes of subsection (a) and the guidelines on what constitutes a grossly excessive price described in clause (ii), the Commission shall define the term grossly excessive price using any metric it deems appropriate.\n**(II) Definition considerations**\nIn formulating the definition in subclause (I), the Commission shall consider whether to provide that such term shall include a price for a good or service that is an amount equal to or greater than 120 percent (or a lesser percentage, as determined appropriate by the Commission) of the average price for such good or service in the market during the 6-month period preceding the sale or offer that allegedly violates subsection (a).\n##### (g) Enforcement by State attorneys general\n**(1) In general**\nIf the attorney general of a State has reason to believe that any person has violated or is violating this section, the attorney general, in addition to any authority it may have to bring an action in State court under the laws of such State, may bring a civil action in any appropriate United States district court or in any other court of competent jurisdiction, including a State court, to\u2014\n**(A)**\nenjoin any further such violation by such person;\n**(B)**\nenforce compliance with this section;\n**(C)**\nobtain a permanent, temporary, or preliminary injunction;\n**(D)**\nobtain civil penalties;\n**(E)**\nobtain damages, restitution, or other compensation on behalf of residents of the State; or\n**(F)**\nobtain any other appropriate equitable relief.\n**(2) Rights of the Commission**\n**(A) Notice to the Commission**\n**(i) In general**\nExcept as provided in clause (ii), before initiating a civil action under paragraph (1), the attorney general of a State shall provide to the Commission a written notice of such action and a copy of the complaint for such action.\n**(ii) Exception**\nIf the attorney general determines that it is not feasible to provide the notice described in clause (i) before initiating a civil action under this subsection, the attorney general shall provide written notice of the action and a copy of the complaint to the Commission immediately upon initiating the civil action.\n**(iii) Jurisdiction not affected**\nAn attorney general failing to provide notice under clause (i) shall not prevent the attorney general or the Commission from having jurisdiction over a civil action brought under paragraph (1) or imperil such civil action in any way.\n**(B) Intervention**\nThe Commission may\u2014\n**(i)**\nintervene in any civil action brought by the attorney general, official, or agency of a State under this subsection; and\n**(ii)**\nupon intervening\u2014\n**(I)**\nbe heard on all matters arising in the civil action; and\n**(II)**\nfile petitions for appeal of a decision in the civil action.\n**(3) Investigatory powers**\nNothing in this subsection may be construed to prevent the attorney general of a State from exercising the powers conferred on the attorney general by the laws of the State to conduct investigations, to administer oaths or affirmations, or to compel the attendance of witnesses or the production of documentary or other evidence.\n**(4) Limitation on State action while Federal action is pending**\nIf the Commission has instituted a civil action for a violation of this section, no State attorney general may, without the approval of the Commission, bring an action under this subsection during the pendency of that action against any defendant named in the complaint of the Commission for any violation of this section alleged in the complaint.\n**(5) Relationship with State-law claims**\nIf the attorney general of a State has authority to bring an action under State law directed at acts or practices that also violate this section, the attorney general may assert a claim under State law and a claim under this section in the same civil action.\n**(6) Venue; Service of process**\n**(A) Venue**\nAny action brought under paragraph (1) may be brought in\u2014\n**(i)**\nthe district court of the United States that meets applicable requirements relating to venue under section 1391 of title 28, United States Code; or\n**(ii)**\nanother court of competent jurisdiction.\n**(B) Service of process**\nIn an action brought under paragraph (1), process may be served in any district in which\u2014\n**(i)**\nthe defendant is an inhabitant, may be found, or transacts business; or\n**(ii)**\nvenue is proper under section 1391 of title 28, United States Code.\n**(7) Actions by other State officials**\n**(A) In general**\nIn addition to civil actions brought by an attorney general under paragraph (1), any other officer of a State who is authorized by the State to do so may bring a civil action under paragraph (1), subject to the same requirements and limitations that apply under this subsection to civil actions brought by attorneys general.\n**(B) Savings provision**\nNothing in this subsection may be construed to prohibit an authorized official of a State from initiating or continuing any proceeding in a court of the State for a violation of any civil or criminal law of the State.\n**(8) Effect on State laws**\nNothing in this section shall preempt or otherwise affect any State or local law.\n#### 4. Disclosures in SEC filings\n##### (a) Definitions\nIn this section:\n**(1) Covered issuer**\nThe term covered issuer means an issuer that\u2014\n**(A)**\nhas a covered quarter; and\n**(B)**\nin the quarter following the covered quarter described in subparagraph (A), is required to submit Form 10\u2013Q or Form 10\u2013K.\n**(2) Covered quarter**\nThe term covered quarter means a quarter during which there is an exceptional market shock.\n**(3) Form 10\u2013K**\nThe term Form 10\u2013K means the form described in section 249.310 of title 17, Code of Federal Regulations, or any successor regulation.\n**(4) Form 10\u2013Q**\nThe term Form 10\u2013Q means the form described in section 240.15d\u201313 of title 17, Code of Federal Regulations, or any successor regulation.\n**(5) Issuer**\nThe term issuer has the meaning given the term in section 3(a) of the Securities Exchange Act of 1934 ( 15 U.S.C. 78c(a) ).\n##### (b) Inclusion in filing\nEach covered issuer, in each Form 10\u2013K or Form 10\u2013Q that the covered issuer is required to file in a quarter following a covered quarter, shall include in the filing the following information with respect to that covered quarter, as compared with the quarter preceding that covered quarter:\n**(1)**\nThe percentage change in the volume of goods or services sold, and the percentage change in the average sales price of those goods or services, which shall be broken down by material product categories, when relevant, and presented in a tabular format.\n**(2)**\nThe gross margins of the covered issuer, which shall be broken down by material product categories, when relevant, and presented in a tabular format.\n**(3)**\nPresented in tabular format, the share of the increase in revenue of the covered issuer that is attributable to\u2014\n**(A)**\na change in the cost of goods or services sold by the covered issuer; and\n**(B)**\na change in the volume of goods or services sold by the covered issuer.\n**(4)**\nThe percentage change in the costs of the covered issuer, which shall be broken down by category and presented in tabular format.\n**(5)**\nIn dollars, the change in the costs of the covered issuer and the revenue of the covered issuer, which shall be presented in tabular format.\n**(6)**\nA detailed narrative disclosure of the pricing strategy of the covered issuer, which shall include\u2014\n**(A)**\nan explanation for any increase in the gross margins of material product categories, including all material causes for such an increase, an explanation of how each such material cause affected such an increase, and a description of the relative importance of each such material cause with respect to such an increase;\n**(B)**\nan explanation for the decisions made by the covered issuer with respect to the prices of goods or services sold by the covered issuer;\n**(C)**\nif the covered issuer increased prices at a rate that was greater than the rate at which the costs incurred by the covered issuer increased, the rationale and objectives for increasing prices in such a manner; and\n**(D)**\na description of conditions under which the covered issuer plans to modify pricing after the date on which the covered issuer submits the filing.\n##### (c) Regulations\nNot later than 180 days after the date of enactment of this Act, the Securities and Exchange Commission shall issue final regulations, or amend existing regulations of the Commission, to carry out this section.\n##### (d) Effective date\nThis section shall take effect on the date on which the Securities and Exchange Commission issues final regulations under subsection (c) or completes the amendments required under that subsection, as applicable.\n#### 5. Funding\nIn addition to amounts otherwise available, there is appropriated to the Commission for fiscal year 2025, out of any money in the Treasury not otherwise appropriated, $1,000,000,000, to remain available until September 30, 2033, for carrying out the work of the Commission.",
      "versionDate": "2025-07-17",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-07-17",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "2321",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Price Gouging Prevention Act of 2025",
      "type": "S"
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
        "updateDate": "2025-09-12T18:45:33Z"
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
      "date": "2025-07-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4528ih.xml"
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
      "title": "Price Gouging Prevention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-14T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Price Gouging Prevention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-14T08:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make price gouging unlawful, to expand the ability of the Federal Trade Commission to seek permanent injunctions and equitable relief, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-14T07:33:23Z"
    }
  ]
}
```
