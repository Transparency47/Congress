# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4007?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4007
- Title: Family Grocery and Farmer Relief Act
- Congress: 119
- Bill type: S
- Bill number: 4007
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-03-27T11:03:21Z
- Update date including text: 2026-03-27T11:03:21Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S883-887)
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on the Judiciary. (text: CR S883-887)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4007",
    "number": "4007",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "S000148",
        "district": "",
        "firstName": "Charles",
        "fullName": "Sen. Schumer, Charles E. [D-NY]",
        "lastName": "Schumer",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Family Grocery and Farmer Relief Act",
    "type": "S",
    "updateDate": "2026-03-27T11:03:21Z",
    "updateDateIncludingText": "2026-03-27T11:03:21Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on the Judiciary. (text: CR S883-887)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
          "date": "2026-03-05T18:12:58Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "VT"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2026-03-05",
      "state": "VT"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "AZ"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "S001194",
      "firstName": "Brian",
      "fullName": "Sen. Schatz, Brian [D-HI]",
      "isOriginalCosponsor": "True",
      "lastName": "Schatz",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "HI"
    },
    {
      "bioguideId": "D000563",
      "firstName": "Richard",
      "fullName": "Sen. Durbin, Richard J. [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Durbin",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "IL"
    },
    {
      "bioguideId": "M000133",
      "firstName": "Edward",
      "fullName": "Sen. Markey, Edward J. [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Markey",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "MA"
    },
    {
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "M001169",
      "firstName": "Christopher",
      "fullName": "Sen. Murphy, Christopher [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Murphy",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "CT"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "RI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "sponsorshipWithdrawnDate": "2026-03-26",
      "state": "MD"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "False",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2026-03-10",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4007is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4007\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Mr. Schumer (for himself, Mr. Booker , Mr. Welch , Ms. Warren , Mr. Sanders , Mr. Gallego , Mr. Merkley , Mr. Schatz , Mr. Durbin , Mr. Markey , Mr. Kim , Mr. Murphy , and Mr. Whitehouse ) introduced the following bill; which was read twice and referred to the Committee on the Judiciary\nA BILL\nTo restore competition in the meatpacking industry by reducing excessive concentration and market power and ultimately reduce prices for American consumers, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Family Grocery and Farmer Relief Act .\n#### 2. Findings and purposes\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe meatpacking industry in the United States is highly concentrated, with a small number of firms controlling a dominant share of beef, chicken, and pork slaughtering and processing.\n**(2)**\n4 firms control 85 percent of the beef market and 67 percent of the pork market, which is up from 36 percent and 34 percent, respectively, in 1980.\n**(3)**\n4 firms control more than 60 percent of the market in chicken processing.\n**(4)**\nThe scale and market dominance of large meatpacking firms create substantial barriers to entry and expansion for independent and regional processors, limiting competitive alternatives for producers and consumers.\n**(5)**\nThis highly consolidated meatpacking market has real consequences for farmers, workers, and consumers.\n**(6)**\nMeatpackers have repeatedly used their market power in ways that suppress wages, destroy jobs through strategic plant shutdowns, and subject workers to extremely dangerous conditions while prices are to their advantage.\n**(7)**\nExtreme concentration in meatpacking has resulted in diminished bargaining power for independent producers, increased vulnerability to unfair and discriminatory practices, and reduced economic viability for rural communities.\n**(8)**\nConsumers are paying more for meat, with the Department of Agriculture reporting that ground beef prices have increased about 16.4 percent since last year. Meanwhile, increased revenue is not flowing to farmers and ranchers as\u2014\n**(A)**\nin 1970, 70 percent of the consumer\u2019s beef dollar went to cattle ranchers, but today, ranchers\u2019 share of the consumer's beef dollar is closer to 30 percent; and\n**(B)**\nprofits remain with the big 4 covered meatpacking enterprises.\n**(9)**\nThe public interest requires competitive, transparent, and resilient markets for essential food products.\n##### (b) Purposes\nThe purposes of this Act are to\u2014\n**(1)**\nrestore competition in the meatpacking industry by reducing excessive concentration and market power;\n**(2)**\nprohibit and reverse mergers and acquisitions in the meatpacking sector that have materially lessened competition;\n**(3)**\nauthorize and require structural separation, divestiture, or breakup of dominant meatpacking firms, where necessary, to restore competitive market conditions;\n**(4)**\nensure that no firm retains or expands market power in United States food and agricultural markets through capital obtained by corruption, bribery, or other unlawful conduct;\n**(5)**\ndeny competitive advantage derived from foreign state-backed or non-market financing that undermines fair competition in United States markets;\n**(6)**\nprotect independent cattle producers from abusive, coercive, or discriminatory practices arising from excessive buyer concentration;\n**(7)**\nensure that any restructuring of the industry results in safer, fairer, and more sustainable jobs for workers across the supply chain;\n**(8)**\npromote the growth and viability of independent and regional meat processors; and\n**(9)**\nhelp bring prices down for families in the United States.\n#### 3. Definitions\nIn this Act:\n**(1) Beef meatpacking market**\nThe term beef meatpacking market means the market for cattle slaughter and beef processing in the United States, including the national beef market and regional beef markets.\n**(2) Commission**\nThe term Commission means the Federal Trade Commission.\n**(3) Covered feedlot**\nThe term covered feedlot means a feedlot with a capacity of 24,000 head of cattle or more.\n**(4) Covered foreign-controlled meatpacking enterprise**\nThe term covered foreign-controlled covered meatpacking enterprise means\u2014\n**(A)**\nJBS S.A. and its affiliates; and\n**(B)**\nany other entity, as determined by rule by the Commission.\n**(5) Covered meatpacking enterprise**\n**(A) In general**\nSubject to subparagraph (B), the term covered meatpacking enterprise has the meaning given the term packer in section 201 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 191 ).\n**(B) Rulemaking**\nNot later than 90 days after the date of enactment of this Act, the Commission shall, by rule, define for purposes of this Act\u2014\n**(i)**\na de minimus threshold of volume or revenue below which a person shall be excluded from the definition of a covered meatpacking enterprise under subparagraph (A); and\n**(ii)**\nthe requirements that place a person under common control or in affiliation with a covered meatpacking enterprise such that the entity shall be included in the definition of a covered meatpacking enterprise under subparagraph (A).\n**(6) CR 4**\nThe term CR4 means the sum of the market shares of the 4 largest firms in the relevant market.\n**(7) Farmers\u2019 cooperative**\nThe term farmers\u2019 cooperative means an organization exempt from taxation under section 521 of the Internal Revenue Code of 1986.\n**(8) Feedlot**\nThe term feedlot \u2014\n**(A)**\nmeans any facility that is used in its entirety or in part for the purpose of feeding livestock to be slaughtered, or to be sold for slaughter, by another; and\n**(B)**\ndoes not include feeding incidental to the sale or transportation of livestock.\n**(9) HHI**\nThe term HHI means the Herfindahl-Hirschman Index, calculated as the sum of the squares of the market shares of all firms in the relevant market.\n**(10) Line of protein**\nThe term line of protein means livestock, livestock products (as defined in section 2 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 182 )), poultry, poultry products (as defined in section 4 of the Poultry Products Inspection Act ( 21 U.S.C. 453 )), meats, or meat food products (as defined in section 1 of the Federal Meat Inspection Act ( 21 U.S.C. 601 )) in each of the following product categories:\n**(A)**\nBeef (including cattle slaughter, beef processing, and beef products).\n**(B)**\nPork (including hog slaughter, pork processing, and pork products).\n**(C)**\nPoultry (including chicken slaughter, processing, and chicken products).\n**(D)**\nAny additional category, as the Commission may, by rule, designate to prevent evasion of this Act.\n**(11) Market share**\nThe term market share means the share of total slaughter or processing capacity, volume, or sales in the relevant market, as determined by rule by the Commission.\n**(12) National beef market**\nThe term national beef market means the market of the United States as a whole, or such broader integrated geographic market as the Commission determines appropriate, for the slaughter of cattle and processing of beef products.\n**(13) Regional beef market**\nThe term regional beef market means a geographic market defined by reference to the regional direct slaughter cattle reporting regions of the Department of Agriculture, or any successor system of regional delineation the Commission determines better reflects competitive conditions.\nI\nBreaking up the meatpacking industry\n#### 101. Limitation on operation in multiple lines of protein\n##### (a) Prohibition\n**(1) In general**\nIt shall be unlawful for a covered meatpacking enterprise to own, control, or operate any entity or combination of entities that engaged in more than 1 line of protein in the United States, in or affecting interstate or foreign commerce.\n**(2) Prohibition on new acquisitions**\nOn and after the date of enactment of this Act, no covered meatpacking enterprise may acquire, directly or indirectly, control of assets or operations in a line of protein other than the line of protein in which the covered meatpacking enterprise already engages, in violation of paragraph (1).\n##### (b) Divestiture required\nThe Commission shall require divestiture pursuant to section 102 of any covered meatpacking enterprise that violates subsection (a).\n#### 102. Divestiture authority\n##### (a) Commission authority\n**(1) In general**\nWith respect to any violation of section 101, the Commission shall develop and oversee a divestiture plan for the covered meatpacking enterprise that provides for\u2014\n**(A)**\nthe sale of assets to 1 or more independent entities; or\n**(B)**\nthe creation of 1 or more new, independent entities through spin-off or other structural separation.\n**(2) Standards**\nIn exercising its authority under paragraph (1), the Commission shall\u2014\n**(A)**\nact in a manner consistent with the public interest in promoting competition, protecting consumers, producers, and workers, and ensuring a resilient food supply, as described in section 602; and\n**(B)**\nto the maximum extent practicable, structure divestitures under this section so as to\u2014\n**(i)**\navoid reconcentration of assets;\n**(ii)**\nencourage ownership and control of divested assets by farmers\u2019 cooperatives, worker owned enterprises, and other small or mid sized businesses; and\n**(iii)**\nprevent reacquisition of divested assets by firms whose market power contributed to the need for divestiture.\n##### (b) Transition; compliance plans\n**(1) In general**\nNot later than 120 days after the date of enactment of this Act, the Commission shall develop a plan for the divestiture of each covered meatpacking enterprise that, as of the date of enactment of this Act, is engaged in the processing of more than 1 line of protein in violation of section 101.\n**(2) Comment**\nNot later than 30 days after the development of a plan under this section, a covered meatpacking enterprise shall submit to the Commission any comments on the plan.\n**(3) Approval of plan**\nFollowing the end of the comment period under paragraph (2), the Commission shall consider and respond to significant comments received under that paragraph and approve a final version of the plan.\nII\nSpecific rules for consolidation in beef meatpacking market\n#### 201. Prohibition on unlawful horizontal consolidation\nThe Commission shall require divestiture pursuant to section 202, as applicable, if in a regional beef market or in a national beef market\u2014\n**(1)**\nthe HHI exceeds 1800;\n**(2)**\nthe CR4 exceeds 50 percent; or\n**(3)**\nany covered meatpacking enterprise has a market share of 30 percent or more.\n#### 202. Regional and national beef market divestiture authority and process\n##### (a) In general\nDivestiture under this section may consist of\u2014\n**(1)**\nsale of 1 or more entities, facilities, or business units to 1 or more independent entities; or\n**(2)**\nthe creation of 1 or more new, independent entities, including through spin-offs or other structural separation.\n##### (b) Divestiture in regional beef markets\n**(1) In general**\n**(A) Violation under HHI or CR4 measures**\nWith respect to a condition described in paragraph (1) or (2) of section 201, the Commission shall order divestiture in the regional market as follows:\n**(i)**\nThe largest covered meatpacking enterprise in the regional beef market that owns multiple beef slaughter or processing entities in that region shall divest its largest entity, facility, or business unit in that region.\n**(ii)**\nAfter the divestiture required under clause (i), the Commission shall reassess the concentration in the regional beef market under section 201(a).\n**(iii)**\nIf 1 or more thresholds described in section 201 is met after the reassessment under clause (ii), the Commission shall repeat the process described in clauses (i) and (ii) as necessary, including by ordering further divestitures, until no threshold described in section 201 is met or until the Commission determines that further divestiture would not reduce market concentration.\n**(B) Violation under single firm market share measure**\nWith respect to a condition described in section 201(3), the Commission shall order divestiture in the regional market of the covered meatpacking enterprise meeting that condition.\n**(2) Use of equitable powers to deconcentrate the market**\nIf the Commission is unable to order further divestitures under subparagraph (A)(iii) of paragraph (1) and 1 or more thresholds described in section 201 is still met, such as if the largest covered meatpacking enterprise has only 1 entity, facility, or business unit in the market which cannot be divided, the Commission shall use all equitable powers to otherwise deconcentrate the market until the Commission determines that none of the thresholds described in section 201 are met.\n##### (c) Divestiture in national beef market\nIn the national beef market, the Commission shall apply a substantially similar process to the process described in subsection (b), as appropriate, to require divestiture by covered meatpacking enterprises (including by ordering divestiture of specified entities, facilities, or business units, or other assets) and use all equitable powers to deconcentrate the market until the Commission determines that none of the thresholds described in section 201 are met.\n#### 203. Vertical consolidation\n##### (a) Findings\nCongress finds that the long-term supply contracts and similar arrangements between large packers and large feedlots can be functionally equivalent to ownership, leading over time to consolidation of feedlots, reduced demand for cattle from independent producers, and diminished competition.\n##### (b) Prohibition\nNo covered meatpacking enterprise in the beef line of protein may slaughter, in any calendar year, more than 10 percent of the cattle produced by any single covered feedlot.\n##### (c) Private right of action\n**(1) In general**\nIf a covered meatpacking enterprise violates subsection (b), any feedlot owner or operator that sold some percentage less than 10 percent of its cattle to that covered meatpacking enterprise during the calendar year of the violation may bring a civil action against the covered meatpacking enterprise in the Federal judicial district in which the feedlot is located or in an appropriate United States district court to recover\u2014\n**(A)**\nan amount equal to 3 times the difference between the highest price the covered meatpacking enterprise paid for cattle from any covered feedlot and the lowest price the feedlot owner or operator received for cattle during the calendar year of the violation multiplied by the total number of cattle the feedlot owner or operator sold overall during that calendar year; and\n**(B)**\nreasonable costs and attorney\u2019s fees.\n**(2) Civil penalty to address private injuries**\nThe Commission may impose on any covered meatpacking enterprise violating subsection (b) a civil penalty equal to the amount described in paragraph (1)(A) with respect to each feedlot owner or operator that sold less than 10 percent of its cattle to the covered meatpacking enterprise and shall use the amount recovered to compensate such feedlots.\nIII\nProhibiting foreign leverage over the domestic beef and pork markets\n#### 301. Findings\nCongress finds the following:\n**(1)**\nA significant portion of domestic beef, pork, and chicken processing capacity is owned or controlled by foreign-based multinational corporations, raising concerns relating to food system resilience, transparency, and national security.\n**(2)**\nJBS S.A., a foreign-based multinational corporation, is the largest beef processor operating in the United States and has obtained substantial domestic meatpacking assets through a sustained acquisition strategy.\n**(3)**\nIn 2020, J&F Investimentos S.A. (the parent company of JBS S.A.) agreed to pay more than $280,000,000 to settle Department of Justice and Securities and Exchange Commission charges relating to bribery and other corrupt practices involving foreign government officials to obtain preferential financing and other financial advantages from state-backed institutions. Capital obtained through such corrupt practices was used, in whole or in part, to finance acquisitions of meatpacking and food processing assets in the United States.\n**(4)**\nThe use of corruption-derived or preferential state-backed financing to acquire United States agricultural assets distorted competitive conditions and disadvantaged firms that relied on lawful, market-based financing.\n**(5)**\nThe People\u2019s Republic of China has an increasing footprint in the food supply chain in the United States, with Smithfield Foods, owned by the WH Group of the People's Republic of China, holding a major position in United States pork processing and announcing in January 2026 its acquisition of Nathan\u2019s Famous, an iconic brand of the United States.\n**(6)**\nWhen major processing capacity and widely recognized brands in the United States move under the control of a foreign parent company, the public deserves to know how that affects competition, pricing power, and national security.\n#### 302. Divestiture plans for covered foreign-controlled meatpacking enterprises\n##### (a) In general\nIt shall be unlawful for any covered foreign-controlled meatpacking enterprise to operate in interstate commerce in the United States.\n##### (b) Divestiture required\n**(1) In general**\nNot later than 120 days after the date of enactment of this Act, the Commission shall require each covered foreign-controlled meatpacking enterprise violating subsection (a) to carry out a divestiture plan under paragraph (2).\n**(2) Structure**\nA divestiture plan of a covered foreign-controlled meatpacking enterprise under this paragraph shall\u2014\n**(A)**\nbe developed by the Commission; and\n**(B)**\nrequire the covered foreign-controlled meatpacking enterprise to divest its United States meatpacking and food processing operations, which may require that such operations be\u2014\n**(i)**\ntransferred to 1 or more new, independent entities headquartered, incorporated, and controlled by persons domiciled in the United States; or\n**(ii)**\nsold to 1 or more entities, subject to conditions necessary to preserve and enhance competition and safeguard national security interests, including, as appropriate, in consultation with relevant national security agencies.\n**(3) Standards**\nIn exercising its authority under paragraph (1), the Commission shall\u2014\n**(A)**\nact in a manner consistent with the public interest in promoting competition, protecting consumers, producers, and workers, and ensuring a resilient food supply, as described in section 602; and\n**(B)**\nto the maximum extent practicable, structure divestitures under this section so as to\u2014\n**(i)**\navoid reconcentration of assets;\n**(ii)**\nencourage ownership and control of divested assets by farmers\u2019 cooperatives, worker owned enterprises, and other small or mid sized businesses; and\n**(iii)**\nprevent reacquisition of divested assets by firms whose market power contributed to the need for divestiture.\n**(4) Consideration of corruption and unlawful conduct**\nIn designing the divestiture plan under this paragraph, the Commission may take into account prior admissions and findings relating to corruption, bribery, and other unlawful conduct used to obtain financing for United States acquisitions, including settlements and judgments under the Foreign Corrupt Practices Act of 1977 ( 15 U.S.C. 78dd\u20131 et seq. ).\n**(5) Extension**\nWith respect to a covered foreign-controlled meatpacker, the Commission may grant a single extension of not more than 90 days of the date on which the prohibition under subsection (a) would otherwise apply to the covered foreign-controlled meatpacking enterprise if the Commission certifies to Congress that\u2014\n**(A)**\na path to executing a divestiture under this subsection has been identified with respect to such covered foreign-controlled meatpacking enterprise;\n**(B)**\nevidence of significant progress toward executing such divestiture has been produced with respect to such covered foreign-controlled meatpacking enterprise; and\n**(C)**\nthere are in place the relevant binding legal agreements to enable execution of such divestiture during the period of such extension.\n#### 303. Review of other foreign-controlled meatpacking enterprises\n##### (a) Study and report\nNot later than 180 days after the date of enactment of this Act, the Commission shall complete a study of the business practices, financing, ownership structures, and competitive effects of all foreign-controlled entities with significant meatpacking and related operations in the United States, including those of entities engaged in beef or pork production and processing.\n##### (b) Consultation\nIn conducting the study under subsection (a), the Commission shall consult with appropriate national security agencies, including the Department of Defense, the Department of Homeland Security, the Office of the Director of National Intelligence, the Department of Agriculture, the Department of Justice, and any other relevant agency as determined by the Commission.\n##### (c) Authority To determine need for divestment\n**(1) In general**\nThe Commission may determine, based on the study and consultations under subsections (a) and (b), that divestment, structural separation, or other remedial action is needed with respect to such foreign-controlled entities to protect competition, national security, or the resilience of the United States food system.\n**(2) Congressional review**\n**(A) Submission**\nBefore the Commission may require divestment, structural separation, or other remedial action under paragraph (1), the Commission shall submit to each House of Congress the determination under that paragraph and Congress shall review the determination pursuant to subparagraph (B).\n**(B) Review**\nCongress may, by an Act of Congress, block a determination submitted under subparagraph (A) through the congressional disapproval procedure set forth in section 802 of title 5, United States Code.\n**(C) Requirement**\nUpon the expiration of the review period under subparagraph (B), the Commission may require the divestiture, structural separation, or other remedial action determined under paragraph (1).\n##### (d) Report to Congress\nNot later than 120 days after the date of enactment of this Act, the Commission shall submit to Committee on Commerce, Science, and Transportation of the Senate , the Select Committee on Intelligence of the Senate , the Committee on the Judiciary of the Senate , the Committee on Energy and Commerce of the House of Representatives , the Permanent Select Committee on Intelligence of the House of Representatives , and the Committee on the Judiciary of the House of Representatives a report that includes a divestment decision with respect to each foreign-controlled meatpacking enterprise.\nIV\nBringing Prices Down for the American Family\n#### 401. Findings\nCongress finds the following:\n**(1)**\nFamilies across the United States face persistently high prices for meat, which contribute significantly to overall food costs and household financial strain.\n**(2)**\nConcentration and limited competition in meat supply chains and retail markets can facilitate unfair and unjustly discriminatory pricing practices, including price discrimination that disadvantages certain retail grocers and the communities they serve.\n**(3)**\nUnfair and unjustly discriminatory prices and price discrimination for meat products can result in higher prices, reduced availability, and fewer choices for consumers, particularly in rural areas, low-income communities, and communities already experiencing limited grocery access.\n**(4)**\nSection 406 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 227 ), confers authority on the Commission with respect to the retail sale of meat, meat food products, and livestock products in unmanufactured form. Under section 406 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 227 ), the Commission may exercise its authority, including its authority under the Federal Trade Commission Act, to prevent unfair methods of competition and unfair or deceptive acts or practices in or affecting commerce in connection with such retail sales.\n**(5)**\nThe authority extends to conduct that results in unfair and unjustly discriminatory retail meat prices and to price discrimination in meat, which drives prices higher for independent, smaller, or neighborhood grocery stores, where such conduct constitutes an unfair method of competition or an unfair or deceptive act or practice.\n**(6)**\nSection 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) declares unlawful unfair methods of competition and unfair or deceptive acts or practices in or affecting commerce and authorizes the Commission to prevent such conduct through investigations, administrative proceedings, and judicial enforcement, including with respect to retail and wholesale sales of meat, meat food products, and livestock products in unmanufactured form where such sales are in or affect commerce.\n**(7)**\nThe Commission's authority under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), including as informed by its policy statements and enforcement precedent, provides an important tool to challenge unfair methods of competition, coordinated conduct, exclusionary practices, and unfair or deceptive acts or practices in retail and wholesale meat markets that may drive up prices, restrict output, or otherwise harm consumers, small and independent grocers, and fair competition.\n**(8)**\nCongress intends that the Commission fully and proactively utilize its authority under section 406 of the Packers and Stockyards Act, 1921, its authority under Section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), and all other applicable laws, to identify, prevent, and remedy unfair and unjustly discriminatory retail and wholesale meat prices and price discrimination that harms consumers, honest businesses, and competition.\n**(9)**\nThe authority of the Commission under section 6(b) of the Federal Trade Commission Act ( 15 U.S.C. 46(b) ) to require reports and answers to specific questions from persons, partnerships, and corporations enables the Commission to study and report on market structure, pricing practices, and competitive conditions in retail and wholesale meat markets, thereby informing effective enforcement and policymaking.\n#### 402. Report on maximizing authority under section 406 of the packers and stockyards act, 1921, and related Federal trade commission authorities\n##### (a) Report required\nNot later than 180 days after the date of enactment of this Act, the Commission shall submit to the congressional committees described in subsection (c) a report describing how the Commission is using and maximizing, and plans to further maximize\u2014\n**(1)**\nits authorities under section 406 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 227 ) and section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) to address\u2014\n**(A)**\nunfair and unjustly discriminatory retail and wholesale prices for meat, meat food products, and livestock products in unmanufactured form; and\n**(B)**\nprice discrimination in meat, including beef and pork, that results in higher prices or otherwise less favorable terms for independent, smaller, or neighborhood grocery stores; and\n**(2)**\nits authority under section 6(b) of the Federal Trade Commission Act ( 15 U.S.C. 46(b) ) to conduct studies and obtain information, including compulsory process where appropriate, regarding the structure, conduct, and performance of retail and wholesale meat markets, and the pricing, contracting, and merchandising practices of firms operating in those markets.\n##### (b) Contents\nThe report required under subsection (a) shall include, at a minimum\u2014\n**(1)**\na description of the Commission's interpretation of its authority under section 406 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 227 ), and section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), as those authorities apply to unfair and unjustly discriminatory retail and wholesale meat prices and to price discrimination in meat affecting retail grocers;\n**(2)**\na description of any policies, guidance, rules, or enforcement priorities the Commission has adopted, revised, or is considering to better detect, deter, and remedy such conduct using its authority under section 406 of the Packers and Stockyards Act, 1921 ( 7 U.S.C. 227 ), section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ), and other applicable statutes;\n**(3)**\na summary of any investigations, enforcement actions, or other proceedings, initiated or completed during the 180-day period beginning on the date of enactment of this Act, that involve alleged unfair and unjustly discriminatory retail or wholesale meat prices or price discrimination in meat affecting retail grocers, to the extent practicable and consistent with the protection of confidential or law-enforcement-sensitive information;\n**(4)**\nan assessment of how unfair and unjustly discriminatory pricing, and price discrimination in meat affecting retail grocers, may contribute to higher prices or reduced access to meat products for consumers in particular geographic areas or demographic groups;\n**(5)**\na description of the Commission's coordination with the Department of Agriculture, the Department of Justice, and any other relevant Federal or State agencies with respect to unfair and unjustly discriminatory retail and wholesale meat prices and price discrimination affecting retail grocers;\n**(6)**\nany recommendations for additional statutory authority, resources, or other measures that the Commission determines would enhance its ability to address unfair and unjustly discriminatory retail and wholesale meat prices and price discrimination in meat that harms competition and consumers;\n**(7)**\na description of how the Commission has used, or plans to use, its authority under section 6(b) of the Federal Trade Commission Act ( 15 U.S.C. 46(b) ) to study and obtain information regarding retail and wholesale meat pricing, fees, discounts, allowances, and other terms or practices that may result in unfair or unjustly discriminatory prices or price discrimination affecting independent, smaller, or neighborhood grocery stores; and\n**(8)**\nan identification of any studies initiated, ongoing, or completed under section 6(b) of the Federal Trade Commission Act ( 15 U.S.C. 46(b) ) that relate to retail or wholesale meat markets, food retailing, or related pricing and merchandising practices, and a discussion of how the results of such studies inform, or are expected to inform, the Commission's enforcement, policy development, and coordination with other Federal or State agencies with respect to unfair and unjustly discriminatory retail or wholesale meat prices and price discrimination.\n##### (c) Committees\nThe congressional committees described in this subsection are the following:\n**(1)**\nThe Committee on Commerce, Science, and Transportation of the Senate .\n**(2)**\nThe Committee on Agriculture, Nutrition, and Forestry of the Senate .\n**(3)**\nThe Committee on the Judiciary of the Senate .\n**(4)**\nThe Committee on Energy and Commerce of the House of Representatives .\n**(5)**\nThe Committee on Agriculture of the House of Representatives .\n**(6)**\nThe Committee on the Judiciary of the House of Representatives .\nV\nFunding the development of new competitors\n#### 501. Funding for farmer\u2019s cooperatives and small business concerns\n##### (a) Definitions\nIn this section:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Small Business Administration.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na farmers\u2019 cooperative; and\n**(B)**\na small business concern (within the meaning of section 3 of the Small Business Act ( 15 U.S.C. 632 )).\n##### (b) Authority\nThe Administrator may provide financial assistance, loan guarantees, technical assistance, and other assistance to eligible entities for the purpose of acquiring, operating, or expanding meatpacking plants or facilities divested pursuant to this Act.\n##### (c) Applications\nAn eligible entity seeking assistance under subsection (b) shall submit to the Administrator an application at such time, in such manner, and containing such information as the Administrator may require.\n##### (d) Preference\nIn evaluating applications submitted under subsection (c), the Administrator shall, to the extent consistent with sound underwriting and program integrity, give preference to eligible entities proposing to use such assistance for locally or regionally focused operations that will enhance competition for livestock and benefit producers and consumers.\n##### (e) Authorization of appropriations\nThere are authorized to be appropriated to the Administrator such sums as are necessary to carry out this section.\nVI\nRulemaking and enforcement authority\n#### 601. Enforcement authority\n##### (a) Enforcement\n**(1) Failure to divest as required**\n**(A) In general**\nA failure to divest pursuant to this Act shall be deemed to be an unlawful method of competition in violation of section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ). The Commission shall enforce divestitures under this Act in the same manner, by the same means, and with the same jurisdiction, powers, and duties as though all applicable terms and provisions of the Federal Trade Commission Act ( 15 U.S.C. 41 et seq. ) were incorporated into and made a part of this section.\n**(B) Persons subject to the Packers and Stockyards Act**\nNotwithstanding section 5(a)(2) of the Federal Trade Commission Act ( 15 U.S.C. 45(a)(2) ) or any jurisdictional limitation of the Commission, the Commission shall also enforce this Act, in the same manner provided in subparagraph (A), with respect to persons, partnerships, or corporations insofar as they are subject to the Packers and Stockyards Act, 1921 ( 7 U.S.C. 181 et seq. ).\n**(C) Penalties for failure to divest**\n**(i) In general**\nThe Commission shall impose a civil penalty equal to 10 percent of the revenue of the violator during the period of violation for any failure to divest pursuant to this Act.\n**(ii) Enhanced penalty**\nThe Commission shall impose a civil penalty equal to 3 times the amount of any damages under section 5 of the Federal Trade Commission Act ( 15 U.S.C. 45 ) for any knowing violation of this Act.\n**(2) Civil action**\n**(A) In general**\nThe Commission is authorized to bring a civil action in an appropriate district court of the United States to enforce any divestment plan, order, or condition imposed under this Act, including to enjoin violations, compel compliance, or obtain other appropriate relief.\n**(B) Remedies**\nIn an action under subparagraph (A), the court may grant any appropriate equitable relief, including specific performance, modification of divestiture terms (only on motion of the Commission), appointment of a monitor, disgorgement or restitution, or such other relief as the interests of justice and competition may require.\n##### (b) Use of penalty funds\nThe Commission shall use any civil penalties or other amounts recovered under this Act to promote competition, including by funding the development of new competitors under title V.\n##### (c) Requests for information and assistance\nThe Department of Agriculture shall comply with all requests for information and expert assistance made by the Commission in carrying out this Act.\n#### 602. Rulemaking\n##### (a) Objectives\nIn promulgating all rules under this Act relating to required divestitures and divestment plans, the Commission shall aim to\u2014\n**(1)**\ndiscourage monopolistic practices;\n**(2)**\nstrengthen and preserve the competitive position of small business concerns;\n**(3)**\nfoster the development of new independent enterprises; and\n**(4)**\npreference farmers\u2019 cooperatives and small businesses in divestment plans.\n##### (b) Requirements\n**(1) In general**\nNot later than 90 days after the date of enactment of this Act, the Commission shall promulgate, in accordance with section 553 of title 5, United States Code, such rules and regulations as are necessary to carry out this Act, including rules relating to\u2014\n**(A)**\ndefinitions of markets for cattle slaughter and beef processing in the United States;\n**(B)**\nstandards and requirements for divestitures under this Act; and\n**(C)**\nin consultation with national security agencies, an identification of all covered foreign-controlled meatpacking enterprises.\n**(2) Failure to promulgate regulations**\nIf no regulations have been promulgated by the Commission on or before the date described in this subsection, the requirements of this section shall still apply.",
      "versionDate": "2026-03-05",
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
        "name": "Agriculture and Food",
        "updateDate": "2026-03-24T00:58:26Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4007is.xml"
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
      "title": "Family Grocery and Farmer Relief Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-27T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Family Grocery and Farmer Relief Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to restore competition in the meatpacking industry by reducing excessive concentration and market power and ultimately reduce prices for American consumers, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:30Z"
    }
  ]
}
```
