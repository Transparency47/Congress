# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2243?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2243
- Title: International Maritime Pollution Accountability Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2243
- Origin chamber: Senate
- Introduced date: 2025-07-10
- Update date: 2026-01-21T05:18:28Z
- Update date including text: 2026-01-21T05:18:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-10: Introduced in Senate
- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.
- Latest action: 2025-07-10: Introduced in Senate

## Actions

- 2025-07-10 - IntroReferral: Introduced in Senate
- 2025-07-10 - IntroReferral: Read twice and referred to the Committee on Environment and Public Works.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-10",
    "latestAction": {
      "actionDate": "2025-07-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2243",
    "number": "2243",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000802",
        "district": "",
        "firstName": "Sheldon",
        "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
        "lastName": "Whitehouse",
        "party": "D",
        "state": "RI"
      }
    ],
    "title": "International Maritime Pollution Accountability Act of 2025",
    "type": "S",
    "updateDate": "2026-01-21T05:18:28Z",
    "updateDateIncludingText": "2026-01-21T05:18:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-10",
      "committees": {
        "item": {
          "name": "Environment and Public Works Committee",
          "systemCode": "ssev00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Environment and Public Works.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-10",
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
          "date": "2025-07-10T15:30:53Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Environment and Public Works Committee",
      "systemCode": "ssev00",
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "NM"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2243is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2243\nIN THE SENATE OF THE UNITED STATES\nJuly 10, 2025 Mr. Whitehouse (for himself, Mr. Padilla , Mr. Heinrich , and Mr. Welch ) introduced the following bill; which was read twice and referred to the Committee on Environment and Public Works\nA BILL\nTo require the Administrator of the Environmental Protection Agency to assess certain fees on shipping and other vessels, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the International Maritime Pollution Accountability Act of 2025 .\n#### 2. Findings\nCongress finds that\u2014\n**(1)**\nthe greenhouse gas emissions from the marine shipping industry\u2014\n**(A)**\naccount for nearly 3 percent of total global anthropogenic carbon dioxide emissions; and\n**(B)**\nare increasing rapidly; and\n**(2)**\nports are a large source of air pollution and contribute to poor air quality in the neighborhoods surrounding the ports, leading to worse health outcomes for those who live in those neighborhoods.\n#### 3. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Calendar quarter**\nThe term calendar quarter means a period of 3 calendar months that ends on, as applicable, March 31, June 30, September 30, or December 31 of the applicable calendar year.\n**(3) Cargo or freight**\nThe term cargo or freight does not include\u2014\n**(A)**\npassengers transported for compensation or hire;\n**(B)**\nfuel intended for use in propelling or powering a vessel;\n**(C)**\nship's stores;\n**(D)**\nsea stores; or\n**(E)**\nthe legitimate equipment necessary to the operation of a vessel.\n**(4) Covered voyage**\n**(A) In general**\nThe term covered voyage means a voyage\u2014\n**(i)**\nmade using a self-propelled vessel of 5,000 gross tonnage or more, the primary purpose of which is transporting cargo or freight; and\n**(ii)**\nthat begins when the vessel leaves the port of origin and terminates when the offloading operations at the final port of call are completed.\n**(B) Exceptions**\nThe term covered voyage does not include a voyage\u2014\n**(i)**\nthat has been included as an OCS source (as defined in subsection (a)(4) of section 328 of the Clean Air Act ( 42 U.S.C. 7627 )) because the voyage has the potential to emit any air pollutant as described in subparagraph (C)(i) of that subsection and is, as a result, regulated pursuant to that section;\n**(ii)**\nmade for the purposes of transporting military cargo, food aid, or supplies for disaster or emergency relief; or\n**(iii)**\nmade using a Jones Act vessel.\n**(5) Criteria air pollutant**\nThe term criteria air pollutant is within the meaning of the Clean Air Act ( 42 U.S.C. 7401 et seq. ).\n**(6) Exclusive economic zone**\nThe term exclusive economic zone has the meaning given the term in section 107 of title 46, United States Code.\n**(7) Final port of call**\nThe term final port of call , with respect to a covered voyage, means, as applicable\u2014\n**(A)**\nthe port in the United States where the vessel making the covered voyage offloaded the last of the cargo or freight of the vessel ultimately bound for the United States that was onboard the vessel on departure from the port of origin; or\n**(B)**\nif the last of the cargo or freight of the vessel ultimately bound for the United States that was onboard the vessel on departure from the port of origin is offloaded in a foreign port, the most recent port of call in the United States prior to offloading the last of the cargo or freight of the vessel that is ultimately bound for the United States.\n**(8) Importer**\nThe term importer means 1 of the parties that qualifies as an importer of record under section 484(a)(2)(B) of the Tariff Act of 1930 ( 19 U.S.C. 1484(a)(2)(B) ).\n**(9) Intermediate port**\nThe term intermediate port , with respect to a covered voyage, means each foreign port of call of the vessel of the covered voyage between the port of origin and the initial port of call of the vessel in the United States.\n**(10) Internal waters**\nThe term internal waters has the meaning given the term in section 2.24 of title 33, Code of Federal Regulations (or successor regulations).\n**(11) Jones Act vessel**\nThe term Jones Act vessel means a documented vessel (as defined in section 106 of title 46, United States Code) with a coastwise endorsement under section 12112 of that title.\n**(12) Port of origin**\n**(A) In general**\nThe term port of origin , with respect to a covered voyage, means the first port of the vessel making the covered voyage after departing which a majority (by mass) of the cargo or freight of the vessel is ultimately bound for the United States.\n**(B) Clarification**\nIn the case in which a vessel, after departing a final port of call for a covered voyage, is carrying cargo the majority (by mass) of which is ultimately bound for the United States\u2014\n**(i)**\nthe vessel shall be considered to be making a new covered voyage; and\n**(ii)**\nthe term port of origin for the new covered voyage shall be considered to be the same as the final port of call for the previous covered voyage.\n**(13) Territorial sea**\nThe term territorial sea has the meaning given the term in section 2.22 of title 33, Code of Federal Regulations (or successor regulations).\n**(14) Ultimately bound for the United States**\nThe term ultimately bound for the United States , with respect to cargo or freight, includes\u2014\n**(A)**\nall cargo or freight that is offloaded in the United States by a vessel making a covered voyage; and\n**(B)**\nall cargo or freight that is\u2014\n**(i)**\ninitially offloaded at an intermediate port; and\n**(ii)**\nsubsequently transported to the United States by sea, land, or air.\n#### 4. Reporting requirements\n##### (a) In general\nBeginning on January 1, 2027, the operator of each covered voyage shall submit to the Administrator the information described in subsection (b).\n##### (b) Information described\nThe information referred to in subsection (a), with respect to a covered voyage, is\u2014\n**(1)**\nthe port of origin;\n**(2)**\nthe total distance traveled from the port of origin to the final port of call;\n**(3)**\nthe total time spent traveling between the port of origin and the final port of call;\n**(4)**\nthe total mass of each type of fuel consumed between the port of origin and the final port of call; and\n**(5)**\nthe total mass of cargo or freight transported between the port of origin and the final port of call;\n**(6)**\neach port of call in the United States;\n**(7)**\neach intermediate port;\n**(8)**\nthe final port of call;\n**(9)**\nthe mass of cargo or freight on-board the applicable vessel on leaving the port of origin;\n**(10)**\nthe percentage of cargo or freight (by mass) offloaded or onloaded at any intermediate port, as compared to the capacity of the applicable vessel and the load of the applicable vessel;\n**(11)**\nthe ultimate destination (by country) of cargo or freight offloaded at intermediate ports;\n**(12)**\nthe mass of cargo or freight on-board the applicable vessel on arrival at or departure from, as applicable, each port of call in the United States;\n**(13)**\nthe total time spent in each port of call in the United States;\n**(14)**\nthe total period of time that the applicable vessel is connected to and reliant on the electrical grid while in port at a port of call in the United States;\n**(15)**\nthe total mass of each type of fuel consumed\u2014\n**(A)**\nin any port of call in the United States; and\n**(B)**\nwithin the exclusive economic zone, the territorial sea, and the internal waters of the United States;\n**(16)**\nthe total period of time spent\u2014\n**(A)**\nnorth of 60 degrees north latitude; or\n**(B)**\nsouth of 60 degrees south latitude;\n**(17)**\nfor each period described in paragraph (16), the total mass of each type of fuel consumed during that period; and\n**(18)**\nany other information that the Administrator determines is necessary to accurately determine the amount of the fees assessed under sections 5 and 6.\n##### (c) Deadline\nThe operator of a covered voyage shall submit the information required under subsection (a) for each covered voyage of the operator that ended during a calendar quarter by not later than 30 days after the end of that calendar quarter.\n#### 5. Fee on lifecycle carbon dioxide-equivalent emissions from cargo vessels\n##### (a) Lifecycle CO 2 -e emissions profile for maritime fuels\nNot later than January 1, 2027, the Administrator shall develop a lifecycle carbon dioxide-equivalent (CO 2 -e) emissions profile for each fuel used in maritime shipping to express the emissions from the combustion of that fuel in carbon dioxide-equivalent per unit mass combusted.\n##### (b) Assessment of fee\n**(1) In general**\nBeginning on January 1, 2027, not later than 30 days after the date on which the Administrator receives from the operator of a covered voyage the information required to be submitted under section 4(a), the Administrator shall assess on the operator a fee with respect to the covered voyage in an amount determined in accordance with paragraph (2).\n**(2) Amount of fee**\n**(A) In general**\nSubject to subparagraph (B) and subsection (d), the amount of a fee assessed under paragraph (1) with respect to a covered voyage shall be the total sum of, for each type of fuel consumed during the covered voyage, the product obtained by multiplying\u2014\n**(i)**\nthe total mass of the fuel consumed during the covered voyage;\n**(ii)**\nthe CO 2 -e emissions of the fuel, expressed in metric tons per unit mass of fuel consumed, as determined under subsection (a); and\n**(iii)**\n$150.\n**(B) Adjustments**\n**(i) Inflation**\nBeginning in calendar year 2028, the Administrator shall annually increase the amount described in subparagraph (A)(iii) by the percentage that is equal to the sum obtained by adding\u2014\n**(I)**\nthe rate of inflation, as determined by the Administrator using the changes for the 12-month period ending the preceding November 30 in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor; and\n**(II)**\n5 percentage points.\n**(ii) Voyages in polar regions**\nFor any portion of a covered voyage that involves travel north of 60 degrees north latitude or south of 60 degrees south latitude, the amount described in subparagraph (A)(iii) with respect to fuel consumed during that portion of the voyage, after adjustment under clause (i), if applicable, shall be tripled.\n**(iii) Crediting amounts paid under global economic measure**\n**(I) Definitions**\nIn this clause:\n**(aa) Annex VI**\nThe term Annex VI means Annex VI of the International Convention for the Prevention of Pollution from Ships, 1973 (if amended in a substantially similar manner, as determined by the Administrator, to the draft regulations described in Circular Letter No. 5005 of the International Maritime Organization, dated April 11, 2025).\n**(bb) Remedial unit; surplus unit**\nThe terms remedial unit and surplus unit have the meanings given those terms under section 3 of Regulation 2 of Annex VI.\n**(II) Adjustment**\nFor any CO 2 -e emissions resulting from a covered voyage for which the operator owes a fee under Annex VI, or would owe a fee under Annex VI but for any surplus units obtained by the operator for the covered voyage, the amount described in subparagraph (A)(iii), after adjustment under clauses (i) and (ii), if applicable, shall be reduced by the applicable Tier 1 or Tier 2 remedial unit cost owed by the operator, or that would be owed by the operator but for the surplus units, for that portion of the covered voyage under Annex VI.\n**(3) Deadline**\nA fee assessed under paragraph (1) shall be due and payable to the Administrator not later than the later of\u2014\n**(A)**\nthe date that is 30 days after the date on which the fee is assessed; and\n**(B)**\nthe end of the calendar year in which the fee is assessed.\n**(4) Penalty**\nIf an operator fails to pay a fee assessed under paragraph (1) by the date described in paragraph (3)\u2014\n**(A)**\nthe amount of the fee shall be increased by 20 percent; and\n**(B)**\nfor each consecutive 30-day period beginning after the date described in paragraph (3), the amount of the fee shall be increased by an additional 20 percent until the date on which the fee is paid to the Administrator.\n##### (c) Alternate fee for imported cargo\n**(1) Definition of qualified importing voyage**\nIn this subsection, the term qualified importing voyage means a voyage made using a vessel\u2014\n**(A)**\nthe primary purpose of which is transporting cargo or freight; and\n**(B)**\nthat, at a foreign port of call, offloads cargo or freight that is ultimately intended to be transported to the United States by sea, land, or air.\n**(2) Requirements**\n**(A) Reporting**\n**(i) In general**\nBeginning on January 1, 2027, each importer for which a qualified importing voyage has cargo or freight that is bound for the United States shall submit to the Administrator the information described in subsection (b) of section 4 in accordance with that section (except as otherwise provided in clause (ii)).\n**(ii) Treatment**\nFor purposes of clause (i), any reference contained in section 4(b) to\u2014\n**(I)**\nthe final port of call shall be considered to be a reference to the foreign port of call within which the cargo or freight of the importer was offloaded from the vessel;\n**(II)**\nthe covered voyage shall be considered to be a reference to the qualified importing voyage; and\n**(III)**\nthe port of origin shall be considered to be a reference to the port at which the cargo or freight bound for the United States was onboarded.\n**(B) Fee**\n**(i) In general**\nBeginning on January 1, 2027, not later than 30 days after the date on which the Administrator receives from an importer described in subparagraph (A)(i) the information required to be submitted under that subparagraph, the Administrator shall assess on the importer the fee described in subsection (b) in accordance with that subsection, but the amount of that fee shall be adjusted as follows:\n**(I)**\nThe amount of the fee shall be prorated for the share (by mass) of the cargo or freight on the vessel making the qualified importing voyage that is ultimately bound for the United States that is being imported by the importer.\n**(II)**\nAfter the adjustment described in subclause (I), the amount of the fee shall be reduced by the amount of the fee, if any, otherwise assessed on the qualified importing voyage pursuant to subsection (b).\n**(ii) Treatment**\nFor purposes of clause (i), any reference in subsection (b) to the covered voyage shall be considered to be a reference to the qualified importing voyage.\n**(C) Enforcement**\nAn importer described in subparagraph (A)(i) may not import the cargo or freight from a qualified importing voyage into the United States until the importer\u2014\n**(i)**\nsubmits the information required under subparagraph (A); and\n**(ii)**\npays the fee assessed under subparagraph (B).\n##### (d) Recognition of foreign pollution fees\nIf a vessel with cargo or freight ultimately bound for the United States, or an operator of such a vessel, is subject to a pollution-based fee by the country of the port of origin of the vessel, any fee assessed on the operator of the vessel or an importer with cargo or freight on that vessel under this section shall be\u2014\n**(1)**\nif the fee from the other country is equal to or more than 50 percent of the fee that would otherwise be assessed under this section, reduced by 50 percent; and\n**(2)**\nif the fee from the other country is less than 50 percent of the fee that would otherwise be assessed under this section, reduced by an amount equal to the amount of the fee from the other country.\n##### (e) Sunset provision\nThis section ceases to apply on the date on which the Administrator publishes in the Federal Register a determination that the International Maritime Organization or another agency of the United Nations has instituted and is enforcing a global fee on lifecycle CO 2 -e emissions from operators of covered voyages that is in an amount equal to or greater than the fees assessed for a covered voyage under this section.\n#### 6. Fees on criteria air pollutants\n##### (a) Emissions profile\nNot later than January 1, 2027, the Administrator shall develop a lifecycle emissions profile for each fuel used in maritime shipping to express the emissions from the combustion of that fuel of each of nitrogen oxides, sulfur dioxide, and fine particulate matter (PM 2.5 ) per unit mass combusted.\n##### (b) Assessment of fee\n**(1) In general**\nBeginning on January 1, 2027, not later than 30 days after the date on which the Administrator receives from the operator of a covered voyage the information required to be submitted under section 4(a), the Administrator shall assess on the operator a fee with respect to the covered voyage in an amount determined in accordance with paragraph (2).\n**(2) Amount of fee**\n**(A) In general**\nSubject to subparagraph (B), the amount of a fee assessed under paragraph (1) shall be the total sum of, for each type of fuel consumed during the covered voyage\u2014\n**(i)**\nthe product obtained by multiplying\u2014\n**(I)**\nthe total mass of the fuel consumed during the covered voyage within the exclusive economic zone, the territorial sea, and the internal waters of the United States;\n**(II)**\nthe quantity of nitrogen oxides emitted by the consumption of the fuel, expressed in pounds per unit mass of fuel consumed, as determined under subsection (a); and\n**(III)**\n$6.30;\n**(ii)**\nthe product obtained by multiplying\u2014\n**(I)**\nthe total mass of the fuel consumed during the covered voyage within the exclusive economic zone, the territorial sea, and the internal waters of the United States;\n**(II)**\nthe quantity of sulfur dioxide emitted by the consumption of the fuel, expressed in pounds per unit mass of fuel consumed, as determined under subsection (a); and\n**(III)**\n$18; and\n**(iii)**\nthe product obtained by multiplying\u2014\n**(I)**\nthe total mass of the fuel consumed during the covered voyage within the exclusive economic zone, the territorial sea, and the internal waters of the United States;\n**(II)**\nthe quantity of fine particulate matter emitted by the consumption of the fuel, expressed in pounds per unit mass of fuel consumed, as determined under subsection (a); and\n**(III)**\n$38.90.\n**(B) Inflation adjustment**\nBeginning in calendar year 2028, the Administrator shall annually increase the amounts described in clauses (i)(III), (ii)(III), and (iii)(III) of subparagraph (A) by the percentage that is equal to the sum obtained by adding\u2014\n**(i)**\nthe rate of inflation, as determined by the Administrator using the changes for the 12-month period ending the preceding November 30 in the Consumer Price Index for All Urban Consumers published by the Bureau of Labor Statistics of the Department of Labor; and\n**(ii)**\n5 percentage points.\n**(3) Deadline**\nA fee assessed under paragraph (1) shall be due and payable to the Administrator not later than the later of\u2014\n**(A)**\nthe date that is 30 days after the date on which the fee is assessed; and\n**(B)**\nthe end of the calendar year in which the fee is assessed.\n**(4) Penalty**\nIf an operator fails to pay a fee assessed under paragraph (1) by the date described in paragraph (3)\u2014\n**(A)**\nthe amount of the fee shall be increased by 20 percent; and\n**(B)**\nfor each consecutive 30-day period beginning after the date described in paragraph (3), the amount of the fee shall be increased by an additional 20 percent until the date on which the fee is paid to the Administrator.\n#### 7. Decarbonizing shipping and ports\n##### (a) Modernizing the Jones Act fleet\n**(1) Definitions**\nIn this subsection:\n**(A) Administrator**\nThe term Administrator means the Administrator of the Maritime Administration.\n**(B) Low-carbon fuel**\nThe term low-carbon fuel means a marine fuel the lifecycle CO 2 -e emissions of which is at least 90 percent less than the lifecycle CO 2 -e emissions of marine fuel oil.\n**(C) Program**\nThe term program means the program established under paragraph (2).\n**(D) Vessel of the United States**\nThe term vessel of the United States has the meaning given the term in section 116 of title 46, United States Code.\n**(2) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Maritime Administration an amount equal to 25 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to award grants, rebates, and low-interest loans, as determined appropriate by the Administrator, to eligible entities\u2014\n**(A)**\nto replace existing Jones Act vessels that use marine fuel oil for propulsion power with vessels that are exclusively propelled using batteries, low-carbon fuels, or other zero-emissions technologies; or\n**(B)**\nto retrofit existing Jones Act vessels that use marine fuel oil for propulsion power into vessels that are exclusively propelled using batteries, low-carbon fuels, or other zero-emissions technologies.\n**(3) Modeled off Diesel Emissions Reduction Act**\nTo the extent practicable, the Administrator shall develop an application process, provide public notification, inform eligible entities of zero-emissions technologies, and submit to Congress an evaluation and report on the efficacy of the program in a manner similar to the national grant program of the Administrator of the Environmental Protection Agency under subtitle G of title VII of the Energy Policy Act of 2005 ( 42 U.S.C. 16131 et seq. ).\n**(4) Eligible entities**\nAn entity eligible for an award under the program is an owner of a Jones Act vessel that currently uses marine fuel oil for propulsion power.\n**(5) Selection**\n**(A) Application**\nAn eligible entity seeking an award under the program shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require, which shall include a certification that an award under the program will be used, as applicable\u2014\n**(i)**\nto purchase, or enter into a contract for the construction of, a vessel that exclusively uses a battery or low-carbon fuels for all propulsion power; or\n**(ii)**\nto retrofit an existing Jones Act vessel that uses marine fuel oil for propulsion power into a vessel that is propelled using batteries or low-carbon fuels.\n**(B) Priority**\nIn selecting the recipients of awards under the program, the Administrator shall give priority to entities the replacement or retrofit of whose vessels would\u2014\n**(i)**\nmaximize the reduction of greenhouse gas emissions;\n**(ii)**\nmaximize the public health benefits from the reduction of criteria air pollutants;\n**(iii)**\nmaximize water quality in ports and other bodies of water;\n**(iv)**\nmaximize public health and environmental benefits from every dollar spent under the program; and\n**(v)**\nalleviate air pollution in poor air quality areas, including\u2014\n**(I)**\nareas identified by the Administrator of the Environmental Protection Agency as in nonattainment or maintenance of national ambient air quality standards promulgated under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for criteria air pollutants; and\n**(II)**\nother areas that receive a disproportionate quantity of air pollution, as determined by the Administrator of the Environmental Protection Agency.\n**(6) Clawback**\nIf the Administrator determines that the recipient of an award under the program has violated the certification required under paragraph (5)(A), the Administrator shall seek reimbursement of the full amount of the award provided to the recipient.\n**(7) Modernizing vessels of the United States**\nIf the Administrator determines that no existing Jones Act vessels are eligible to receive funding under the program, for the duration of that determination, paragraphs (2) through (6) shall be applied by substituting vessel of the United States for Jones Act vessel .\n**(8) Program administration**\nOf the amounts made available under paragraph (2) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program.\n##### (b) Research and development for low-Carbon maritime fuels and low-Emission maritime technologies\n**(1) Definition of eligible entity**\nIn this subsection, the term eligible entity means\u2014\n**(A)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal government;\n**(B)**\na maritime shipping or logistics company;\n**(C)**\na port authority;\n**(D)**\nan accredited institution of higher education;\n**(E)**\na research institution;\n**(F)**\na person engaged in the production, transportation, blending, or storage of sustainable maritime fuel in the United States or feedstocks in the United States that may be used to produce sustainable maritime fuel;\n**(G)**\na person engaged in the development, demonstration, or application of low-emission maritime technologies; and\n**(H)**\na nonprofit entity or nonprofit consortium with experience in sustainable maritime fuels, low-emission maritime technologies, or other clean transportation research programs.\n**(2) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Department of Energy an amount equal to 25 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to award competitive grants to eligible entities to carry out projects in the United States\u2014\n**(A)**\nto produce, transport, blend, or store low-carbon maritime fuels; or\n**(B)**\nto develop, demonstrate, or apply low-emission maritime technologies.\n**(3) Priority**\nIn awarding grants under the program established under paragraph (2), the Secretary of Energy shall give priority to projects that maximize\u2014\n**(A)**\nthe domestic production and deployment of sustainable maritime fuels or the use of low-emission maritime technologies in commercial maritime;\n**(B)**\nreductions in greenhouse gas emissions;\n**(C)**\npublic health benefits from criteria air pollutant reductions;\n**(D)**\nwater quality in ports and other bodies of water;\n**(E)**\npublic health and environmental benefits from every dollar spent under that program; and\n**(F)**\nthe creation of new jobs in the United States.\n**(4) Program administration**\nOf the amounts made available under paragraph (2) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program established under that paragraph.\n##### (c) Workforce development\n**(1) Definitions**\nIn this subsection:\n**(A) Low-carbon fuel**\nThe term low-carbon fuel means a marine fuel the lifecycle CO 2 -e emissions of which is at least 90 percent less than the lifecycle CO 2 -e emissions of marine fuel oil.\n**(B) Maritime academy**\nThe term maritime academy means\u2014\n**(i)**\nthe United States Merchant Marine Academy;\n**(ii)**\na State maritime academy; and\n**(iii)**\na center of excellence for domestic maritime workforce training and education designated under section 51706(a) of title 46, United States Code.\n**(C) Program**\nThe term program means the program established under paragraph (2).\n**(D) Zero-emission port equipment or technology**\nThe term zero-emission port equipment or technology has the meaning given the term in section 133(d) of the Clean Air Act ( 42 U.S.C. 7433(d) ) (as in effect on January 1, 2025).\n**(2) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Environmental Protection Agency an amount equal to 5 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to award grants and rebates to support workforce training and development for the maintenance and operation of zero-emission port equipment or technology and vessels that are propelled using batteries or low-carbon fuels, including training, programming, and curriculum development at maritime academies on the maintenance and operation of zero-emission port equipment or technology and vessels that are propelled using batteries or low-carbon fuels.\n**(3) Eligible entities**\nAn entity eligible to receive an award under the program is\u2014\n**(A)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal agency that has jurisdiction over a port authority or a port;\n**(B)**\na port authority;\n**(C)**\nan air pollution control agency;\n**(D)**\na maritime academy; and\n**(E)**\na private entity that\u2014\n**(i)**\napplies for a grant under this subsection in partnership with an entity described in any of subparagraphs (A) through (D); and\n**(ii)**\nowns, operates, or uses\u2014\n**(I)**\nvessels, the primary purpose of which are transporting cargo or freight, that are propelled using batteries or low-carbon fuels; or\n**(II)**\nthe facilities, cargo-handling equipment, transportation equipment, or related technology of a port.\n**(4) Application**\nAn eligible entity seeking an award under the program shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n**(5) Program administration**\nOf the amounts made available under paragraph (2) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program.\n##### (d) Harbor craft electrification\n**(1) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Environmental Protection Agency an amount equal to 10 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to award grants, rebates, or low-interest loans, as determined appropriate by the Administrator\u2014\n**(A)**\nto replace or retrofit existing harbor craft, except for ferry vessels, with vessels that use batteries for all propulsion power; and\n**(B)**\nto support workforce development and training to support the maintenance, charging, fueling, and operation of vessels described in subparagraph (A).\n**(2) Modeled off Diesel Emissions Reduction Act**\nTo the extent practicable, the Administrator shall develop an application process, provide public notification, inform eligible entities of zero-emissions technologies, and submit to Congress an evaluation and report on the efficacy of the program established under paragraph (1) in a manner similar to the national grant program of the Administrator under subtitle G of title VII of the Energy Policy Act of 2005 ( 42 U.S.C. 16131 et seq. ).\n**(3) Eligible entities**\nAn entity eligible to receive an award under the program established under paragraph (1) is\u2014\n**(A)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal agency that has jurisdiction over a port authority or a port;\n**(B)**\na port authority; and\n**(C)**\na private entity that\u2014\n**(i)**\napplies for an award under this subsection in partnership with an entity described in subparagraph (A) or (B); and\n**(ii)**\nowns, operates, or uses harbor craft, except for ferry vessels.\n**(4) Selection**\n**(A) Application**\nAn eligible entity seeking an award under the program established under paragraph (1) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require, which shall include a certification that an award under the program will be used to purchase a vessel that exclusively uses a battery for all propulsion power.\n**(B) Priority**\nIn selecting the recipients of awards under the program established under paragraph (1), the Administrator shall give priority to entities the replacement or retrofit of whose harbor crafts with vessels that use batteries for all propulsion power would\u2014\n**(i)**\nmaximize the reduction of greenhouse gas emissions;\n**(ii)**\nmaximize the public health benefits from the reduction of criteria air pollutants;\n**(iii)**\nmaximize water quality in ports and other bodies of water;\n**(iv)**\nmaximize public health and environmental benefits from every dollar spent under the program; and\n**(v)**\nalleviate air pollution in poor air quality areas, including\u2014\n**(I)**\nareas identified by the Administrator as in nonattainment or maintenance of national ambient air quality standards promulgated under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for criteria air pollutants; and\n**(II)**\nother areas that receive a disproportionate quantity of air pollution, as determined by the Administrator.\n**(5) Clawback**\nIf the Administrator determines that the recipient of an award under the program established under paragraph (1) has violated the certification required under paragraph (4)(A), the Administrator shall seek reimbursement of the full amount of the award provided to the recipient.\n**(6) Program administration**\nOf the amounts made available under paragraph (1) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program established under that paragraph.\n##### (e) Ferry electrification\n**(1) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Environmental Protection Agency an amount equal to 10 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to award grants, rebates, or low-interest loans, as determined appropriate by the Administrator\u2014\n**(A)**\nto replace or retrofit existing ferry or crew vessels with vessels that use batteries for all propulsion power; and\n**(B)**\nto support workforce development and training to support the maintenance, charging, fueling, and operation of vessels described in subparagraph (A) that use batteries for all propulsion power.\n**(2) Modeled off Diesel Emissions Reduction Act**\nTo the extent practicable, the Administrator shall develop an application process, provide public notification, inform eligible entities of zero-emissions technologies, and submit to Congress an evaluation and report on the efficacy of the program established under paragraph (1) in a manner similar to the national grant program of the Administrator under subtitle G of title VII of the Energy Policy Act of 2005 ( 42 U.S.C. 16131 et seq. ).\n**(3) Eligible entities**\nAn entity eligible to receive an award under the program established under paragraph (1) is\u2014\n**(A)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal agency that has jurisdiction over a ferry line;\n**(B)**\na port authority; and\n**(C)**\na private entity that\u2014\n**(i)**\napplies for an award under this subsection in partnership with an entity described in subparagraph (A) or (B); and\n**(ii)**\nowns, operates, or uses ferry or crew vessels.\n**(4) Selection**\n**(A) Application**\nAn eligible entity seeking an award under the program established under paragraph (1) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require, which shall include a certification that an award under the program will be used to purchase a vessel that exclusively uses a battery for all propulsion power.\n**(B) Priority**\nIn selecting the recipients of awards under the program established under paragraph (1), the Administrator shall give priority to entities the replacement or retrofit of whose ferry or crew vessels with vessels that use batteries for all propulsion power would\u2014\n**(i)**\nmaximize the reduction of greenhouse gas emissions;\n**(ii)**\nmaximize the public health benefits from the reduction of criteria air pollutants;\n**(iii)**\nmaximize water quality in ports and other bodies of water;\n**(iv)**\nmaximize public health and environmental benefits from every dollar spent under the program; and\n**(v)**\nalleviate air pollution in poor air quality areas, including\u2014\n**(I)**\nareas identified by the Administrator as in nonattainment or maintenance of national ambient air quality standards promulgated under section 109 of the Clean Air Act ( 42 U.S.C. 7409 ) for criteria air pollutants; and\n**(II)**\nother areas that receive a disproportionate quantity of air pollution, as determined by the Administrator.\n**(5) Clawback**\nIf the Administrator determines that the recipient of an award under the program established under paragraph (1) has violated the certification required under paragraph (4)(A), the Administrator shall seek reimbursement of the full amount of the award provided to the recipient.\n**(6) Program administration**\nOf the amounts made available under paragraph (1) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program established under that paragraph.\n##### (f) Increased air monitoring in port communities\n**(1) Establishment**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Environmental Protection Agency an amount equal to 5 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to provide grants, rebates, or low-interest loans, as determined appropriate by the Administrator, to create fenceline air monitoring at port boundaries and in communities located within 1 mile of a port boundary.\n**(2) Eligible entities**\nAn entity eligible to receive an award under the program established under paragraph (1) is\u2014\n**(A)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal government;\n**(B)**\na State (including the District of Columbia and territories of the United States), regional, local, or Tribal agency that has jurisdiction over a port authority or port;\n**(C)**\na port authority;\n**(D)**\nan air pollution control agency; and\n**(E)**\na nonprofit entity or nonprofit consortium with experience in air pollution monitoring.\n**(3) Application**\nAn eligible entity seeking an award under the program established under paragraph (1) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n**(4) Program administration**\nOf the amounts made available under paragraph (1) each fiscal year, the Administrator may use not more than 1 percent for the management and oversight of the program established under that paragraph.\n##### (g) Funding of existing programs\n**(1) Clean ports program**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Environmental Protection Agency an amount equal to 15 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to carry out the program established under section 133 of the Clean Air Act ( 42 U.S.C. 7433 ).\n**(2) Oceans and coastal security**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the National Oceanic and Atmospheric Administration an amount equal to 3 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year for deposit into the National Oceans and Coastal Security Fund established under section 904(a) of the National Oceans and Coastal Security Act ( 16 U.S.C. 7503(a) ).\n**(3) Marine Debris Foundation**\nFor fiscal year 2029 and each fiscal year thereafter, there are appropriated, out of any funds in the Treasury not otherwise appropriated, to the Department of Commerce an amount equal to 2 percent of the amounts collected pursuant to fees assessed under sections 5 and 6 during the previous calendar year to carry out subtitle B of title I of the Save Our Seas 2.0 Act ( 33 U.S.C. 4211 et seq. ).",
      "versionDate": "2025-07-10",
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
        "actionDate": "2025-12-01",
        "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation."
      },
      "number": "4341",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "International Maritime Pollution Accountability Act of 2025",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-04T15:38:49Z"
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
      "date": "2025-07-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2243is.xml"
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
      "title": "International Maritime Pollution Accountability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T02:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "International Maritime Pollution Accountability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-25T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Administrator of the Environmental Protection Agency to assess certain fees on shipping and other vessels, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-25T02:18:18Z"
    }
  ]
}
```
