# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2823?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2823
- Title: Climate Change Financial Risk Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2823
- Origin chamber: House
- Introduced date: 2025-04-10
- Update date: 2026-03-02T23:10:13Z
- Update date including text: 2026-03-02T23:10:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-10: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-04-10: Introduced in House

## Actions

- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Introduced in House
- 2025-04-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-10 - IntroReferral: Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2823",
    "number": "2823",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "C001117",
        "district": "6",
        "firstName": "Sean",
        "fullName": "Rep. Casten, Sean [D-IL-6]",
        "lastName": "Casten",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Climate Change Financial Risk Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-02T23:10:13Z",
    "updateDateIncludingText": "2026-03-02T23:10:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-10",
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
      "text": "Referred to the Committee on Financial Services, and in addition to the Committee on Energy and Commerce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-10",
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
          "date": "2025-04-10T13:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-10T13:04:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MA"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MO"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "MD"
    },
    {
      "bioguideId": "C001112",
      "district": "24",
      "firstName": "Salud",
      "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Carbajal",
      "middleName": "O.",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-04-29",
      "state": "IN"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "RI"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "CA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-02-24",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2823ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2823\nIN THE HOUSE OF REPRESENTATIVES\nApril 10, 2025 Mr. Casten introduced the following bill; which was referred to the Committee on Financial Services , and in addition to the Committee on Energy and Commerce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Board of Governors of the Federal Reserve System, in consultation with the heads of other relevant Federal agencies, to develop and conduct financial risk analyses relating to climate change, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Climate Change Financial Risk Act of 2025 .\n#### 2. Sense of congress\nIt is the sense of Congress that\u2014\n**(1)**\n2024 was the warmest year on record globally and the first calendar year that the average global temperature exceeded 1.5 degrees Celsius above pre-industrial levels;\n**(2)**\nif current trends continue, average global temperatures over the long term are likely to surpass 1.5 degrees Celsius above pre-industrial levels between 2030 and 2050;\n**(3)**\nglobal temperature rise has already resulted in an increased number of heavy rainstorms, coastal flooding events, heat waves, hurricanes, wildfires, and other extreme events;\n**(4)**\nsince 1980\u2014\n**(A)**\nthe number of extreme weather events per year that cost the people of the United States more than $1,000,000,000 per event, accounting for inflation, has increased significantly; and\n**(B)**\nthe total cost of extreme weather events in the United States has exceeded $2,915,000,000,000;\n**(5)**\nas physical impacts from climate change are manifested across multiple sectors of the economy of the United States\u2014\n**(A)**\nclimate-related economic risks will continue to increase;\n**(B)**\nclimate-related extreme weather events will disrupt energy and transportation systems in the United States, which will result in more frequent and longer-lasting power outages, fuel shortages, and service disruptions in critical sectors across the economy of the United States;\n**(C)**\nprojected increases in extreme heat conditions will lead to decreases in labor productivity in agriculture, construction, and other critical economic sectors;\n**(D)**\nfood and livestock production will be impacted in regions that experience increases in heat and drought, and small rural communities will struggle to find the resources needed to adapt to those changes; and\n**(E)**\nsea level rise and more frequent and intense extreme weather events will\u2014\n**(i)**\nincreasingly disrupt and damage private property and critical infrastructure;\n**(ii)**\ndrastically increase insured and uninsured losses; and\n**(iii)**\ncause supply chain disruptions;\n**(6)**\nadvances in energy efficiency and renewable energy technologies, as well as climate policies and shifting societal preferences, will\u2014\n**(A)**\nreduce global demand for fossil fuels; and\n**(B)**\nexpose transition risks for fossil fuel companies and investors domestically and globally, and for companies and investors in other energy-intensive industries, which could include trillions of dollars of stranded assets around the world;\n**(7)**\nclimate change poses uniquely far-reaching risks to the financial services industry, including with respect to credit, counterparty, and market risks, due to the number of sectors and locations impacted and the potentially irreversible scale of damage;\n**(8)**\nweaknesses in how a financial institution identifies, measures, monitors, and controls for the physical risks and transition risks associated with climate change could adversely affect the safety and soundness of a financial institution;\n**(9)**\nfinancial institutions must take a consistent approach to assessing climate-related financial risks and incorporating those risks into existing risk management practices, which should be informed by scenario analysis;\n**(10)**\nthe Board of Governors conducts annual assessments of the capital adequacy and capital planning practices of the largest and most complex banking organizations (referred to in this section as stress tests ) in order to promote a safe, sound, and efficient banking and financial system;\n**(11)**\nas of the date of enactment of this Act\u2014\n**(A)**\nthe stress tests conducted by the Board of Governors are not designed to reflect the physical risks or transition risks posed by climate change; and\n**(B)**\nthe Board of Governors has conducted 1 pilot climate scenario analysis exercise with only 6 United States banking organizations;\n**(12)**\nthe Board of Governors\u2014\n**(A)**\nhas stated that economic effects of climate change and the transition to a lower carbon economy pose an emerging risk to the safety and soundness of financial institutions and the financial stability of the United States;\n**(B)**\nhas the authority under section 39 of the Federal Deposit Insurance Act ( 12 U.S.C. 1831p\u20131 ) and section 165 of the Financial Stability Act of 2010 ( 12 U.S.C. 5365 ) to take into account the potentially systemic impact of climate-related risks on the financial system to preserve the safety and soundness of supervised institutions and the financial stability of the United States; and\n**(C)**\nshould develop new analytical tools with longer time horizons to accurately assess and manage the risks described in subparagraph (B);\n**(13)**\nthe Climate-Related Market Risk Subcommittee of the Commodity Futures Trading Commission has identified the importance of researching climate-related sub-systemic shocks to financial markets and institutions in particular sectors and regions of the United States ; and\n**(14)**\nthe Financial Stability Oversight Council likewise identified [c]limate change [a]s an emerging threat to the financial stability of the United States and recommended that members of the Council, including the Board of Governors, take action to strengthen the financial system and make it more resilient to climate-related shocks and vulnerabilities .\n#### 3. Definitions\nIn this Act:\n**(1) Bank holding company**\nThe term bank holding company has the meaning given the term in section 102(a) of the Financial Stability Act of 2010 ( 12 U.S.C. 5311(a) ).\n**(2) Board of Governors**\nThe term Board of Governors means the Board of Governors of the Federal Reserve System.\n**(3) Climate science leads**\nThe term climate science leads means\u2014\n**(A)**\nthe Administrator of the National Oceanic and Atmospheric Administration;\n**(B)**\nthe Administrator of the Environmental Protection Agency;\n**(C)**\nthe Secretary of Energy;\n**(D)**\nthe Assistant Secretary for the Office of International Affairs of the Department of Energy;\n**(E)**\nthe Administrator of the National Aeronautics and Space Administration;\n**(F)**\nthe Assistant Secretary for the Bureau of Oceans and International Environmental and Scientific Affairs of the Department of State;\n**(G)**\nthe Director of the United States Geological Survey;\n**(H)**\nthe Secretary of the Interior;\n**(I)**\nthe Director of the National Climate Assessment;\n**(J)**\nthe individual from the United States elected to the Intergovernmental Panel on Climate Change Bureau;\n**(K)**\nthe Permanent Representative of the United States to the World Meteorological Organization; and\n**(L)**\nthe head of any other Federal agency that the Board of Governors determines to be appropriate.\n**(4) Covered entity**\nThe term covered entity means\u2014\n**(A)**\na nonbank financial company or bank holding company that has not less than $250,000,000,000 in total consolidated assets; and\n**(B)**\na nonbank financial company or bank holding company\u2014\n**(i)**\nthat has not less than $100,000,000,000 in total consolidated assets; and\n**(ii)**\nwith respect to which the Board of Governors determines the application of subparagraph (C) of section 165(i)(1) of the Financial Stability Act of 2010 ( 12 U.S.C. 5365(i)(1) ), as added by section 6 of this Act, is appropriate\u2014\n**(I)**\nto\u2014\n**(aa)**\nprevent or mitigate risks to the financial stability of the United States; or\n**(bb)**\npromote the safety and soundness of the company; and\n**(II)**\nafter taking into consideration\u2014\n**(aa)**\nthe capital structure, riskiness, complexity, financial activities, and size of the company, including the financial activities of any subsidiary of the company; and\n**(bb)**\nany other risk-related factor that the Board of Governors determines to be appropriate.\n**(5) Nonbank financial company**\nThe term nonbank financial company has the meaning given the term in section 102(a)(4)(C) of the Financial Stability Act of 2010 ( 12 U.S.C. 5311(a)(4)(C) ).\n**(6) Physical risks**\nThe term physical risks means financial risks to assets, locations, operations, or value chains that result from exposure to physical, climate-related effects, including from\u2014\n**(A)**\nincreased average global temperatures;\n**(B)**\nincreased severity and frequency of extreme weather events;\n**(C)**\nincreased flooding;\n**(D)**\nsea level rise;\n**(E)**\nocean acidification;\n**(F)**\nincreased severity and frequency of heat waves;\n**(G)**\nincreased frequency of wildfires;\n**(H)**\ndecreased arability of farmland; and\n**(I)**\ndecreased availability of fresh water.\n**(7) Surveyed entity**\nThe term surveyed entity means a bank holding company, nonbank financial company, or other entity that\u2014\n**(A)**\nis supervised by the Board of Governors, the Office of the Comptroller of the Currency, or the Federal Deposit Insurance Corporation;\n**(B)**\nhas total consolidated assets of not less than $10,000,000,000; and\n**(C)**\nis not a covered entity.\n**(8) Technical Development Group**\nThe term Technical Development Group means the Climate Risk Scenario Technical Development Group established under section 4(a).\n**(9) Transition risks**\nThe term transition risks means financial risks that are attributable to climate change mitigation and adaptation, including efforts to reduce greenhouse gas emissions and strengthen resilience to the impacts of climate change, including\u2014\n**(A)**\ncosts relating to\u2014\n**(i)**\ninternational treaties and agreements;\n**(ii)**\nFederal, State, and local policies;\n**(iii)**\nnew technologies;\n**(iv)**\nchanging markets;\n**(v)**\nreputational impacts relevant to changing consumer behavior; and\n**(vi)**\nlitigation; and\n**(B)**\na loss in the value, or the stranding, of assets due to any of the costs described in subparagraph (A).\n**(10) Value chain**\nThe term value chain \u2014\n**(A)**\nmeans the total lifecycle of a product or service, both before and after production of the product or service, as applicable; and\n**(B)**\nmay include the sourcing of materials, production, and disposal with respect to the product or service described in subparagraph (A).\n#### 4. Climate Risk Scenario Technical Development Group\n##### (a) Establishment\nThe Board of Governors shall establish a technical advisory group to be known as the Climate Risk Scenario Technical Development Group .\n##### (b) Membership\n**(1) Composition**\nThe Technical Development Group shall be composed of 10 members\u2014\n**(A)**\n5 of whom shall be climate scientists, with a demonstrated record of peer-reviewed publications and professional contributions to climate modeling, climate risk assessment, or related areas; and\n**(B)**\n5 of whom shall be economists, with expertise in either the United States financial system or the financial risks posed by climate change.\n**(2) Selection**\nThe Board of Governors shall select the members of the Technical Development Group after consultation with the climate science leads.\n##### (c) Duties\nThe Technical Development Group shall\u2014\n**(1)**\nprovide recommendations to the Board of Governors regarding the development of, and updates to, the climate change risk scenarios under section 5;\n**(2)**\nafter the establishment of the climate change risk scenarios under section 5, determine the financial and economic risks resulting from those scenarios;\n**(3)**\nmake any final work product, and any information used in the development of the final work product, publicly available;\n**(4)**\nprovide technical assistance to covered entities in assessing physical risks or transition risks; and\n**(5)**\nprovide publicly available resources to entities that are not covered entities to help those entities assess physical risks and transition risks.\n##### (d) Prohibition on compensation\nMembers of the Technical Development Group shall serve without pay.\n##### (e) Inapplicability of chapter 10 of title 5, United States Code\nChapter 10 of title 5, United States Code, shall not apply with respect to the Technical Development Group.\n#### 5. Development and updating of climate change risk scenarios\n##### (a) In general\n**(1) Initial development**\nNot later than 1 year after the date of enactment of this Act, the Board of Governors, in coordination with the climate science leads, and taking into consideration the recommendations of the Technical Development Group, shall develop 3 separate climate change risk scenarios as follows:\n**(A)**\nOne scenario that assumes an average increase in global temperatures of 1.5 degrees Celsius above pre-industrial levels.\n**(B)**\nOne scenario that assumes an average increase in global temperatures of 2 degrees Celsius above pre-industrial levels.\n**(C)**\nOne scenario that\u2014\n**(i)**\nassumes the likely and very likely average increase in global temperatures that can be expected, taking into consideration the extent to which national policies and actions relating to climate change have been implemented, as of the date on which the scenario is developed; and\n**(ii)**\ndoes not take into consideration commitments for national policies and actions relating to climate change that, as of the date described in clause (i), have not been implemented.\n**(2) International coordination**\nIn developing and updating the 3 scenarios required under this subsection, the Board of Governors shall take into consideration analytical tools and best practices developed by international banking supervisors relating to climate risks and scenario analysis in an effort to develop consistent and comparable data-driven scenarios.\n**(3) Recommendations**\nIf the Technical Development Group determines that the average increase in global temperatures described in subparagraph (A) or (B) of paragraph (1) is no longer scientifically valid, the Technical Development Group may recommend that the Board of Governors, in coordination with the climate science leads, update the average increase in global temperatures described in the applicable subparagraph to reflect the most current assessment of climate change science.\n##### (b) Considerations\nIn developing and updating each of the 3 scenarios required under subsection (a), the Board of Governors, in coordination with the climate science leads, shall account for physical risks and transition risks that may disrupt business operations across the global economy, including through\u2014\n**(1)**\ndisruptions with respect to\u2014\n**(A)**\nthe sourcing of materials;\n**(B)**\nproduction;\n**(C)**\ntransportation; and\n**(D)**\nthe disposal of products and services;\n**(2)**\nchanges in the availability and prices of raw materials and other inputs;\n**(3)**\nchanges in agricultural production and with respect to food security;\n**(4)**\ndirect damages to fixed assets;\n**(5)**\nincreases in costs associated with insured or uninsured losses;\n**(6)**\nchanges in asset values;\n**(7)**\nimpacts on\u2014\n**(A)**\naggregate demand for products and services;\n**(B)**\nlabor productivity;\n**(C)**\nasset liquidity; and\n**(D)**\ncredit availability;\n**(8)**\nmass migration and increases in disease and mortality rates;\n**(9)**\ninternational conflict, as such conflict relates to global economic activity and output; and\n**(10)**\nchanges in any other microeconomic or macroeconomic condition that the Board of Governors, in coordination with the climate science leads, determines to be relevant.\n#### 6. Climate-related enhanced supervision for certain nonbank financial companies and bank holding companies\nSection 165(i)(1) of the Financial Stability Act of 2010 ( 12 U.S.C. 5365(i)(1) ) is amended\u2014\n**(1)**\nin subparagraph (B)(i), by inserting except as provided in subparagraph (C)(ii)(I), before shall provide ; and\n**(2)**\nby adding at the end the following:\n(C) Biennial tests required (i) Definitions In this subparagraph\u2014 (I) the term capital distribution has the meaning given the term in section 225.8(d)(4) of title 12, Code of Federal Regulations, as in effect on the date of enactment of this subparagraph; (II) the term capital policy has the meaning given the term in section 225.8(d)(7) of title 12, Code of Federal Regulations, as in effect on the date of enactment of this subparagraph; and (III) the terms climate science leads and covered entity have the meanings given those terms in section 3 of the Climate Change Financial Risk Act of 2025 . (ii) Tests (I) In general The Board of Governors, in coordination with the appropriate primary financial regulatory agencies and the climate science leads, shall conduct biennial analyses in which each covered entity shall be subject to evaluation, under an adverse set of conditions, of whether that covered entity has the capital, on a total consolidated basis, necessary to absorb financial losses that would arise under each climate change risk scenario developed under section 5 of the Climate Change Financial Risk Act of 2025 . (II) Initial tests With respect to each of the first 3 analyses conducted under subclause (I)\u2014 (aa) the covered entity to which such an analysis applies shall not be subject to any adverse consequences as a result of the analysis; and (bb) the Board of Governors shall\u2014 (AA) not later than 60 days after the date on which the Board of Governors completes the analysis, make a summary of the analysis publicly available; and (BB) submit a copy of the results of the analysis to the Committee on Banking, Housing, and Urban Affairs of the Senate and the Committee on Financial Services of the House of Representatives. (III) Climate risk resolution plan (aa) In general Except with respect to the first analysis conducted under subclause (I), each covered entity shall, before being subject to an analysis under that subclause, submit to the Board of Governors a resolution plan with respect to climate risk planning (referred to in this subclause as a climate risk resolution plan ), which shall be based on the results of the most recently conducted analysis of the covered entity under that subclause. (bb) Contents Each climate risk resolution plan required under item (aa) shall include\u2014 (AA) a capital policy with respect to climate risk planning; and (BB) qualitative and quantitative targets for balance sheet and off-balance sheet exposures, and other business operations, that remedy vulnerabilities identified in the most recently conducted analysis of the applicable covered entity under subclause (I). (cc) Rejection The Board of Governors may object to a climate risk resolution plan submitted by a covered entity under item (aa) if the Board of Governors determines that\u2014 (AA) the covered entity has not demonstrated that such plan is reasonable to maintain capital above each minimum regulatory capital ratio on a pro forma basis under the adverse set of conditions described in subclause (I); (BB) the climate risk resolution plan is otherwise not reasonable or appropriate, including because the climate risk resolution plan no longer provides fair services to vulnerable and disadvantaged communities; (CC) the assumptions and analysis underlying the climate risk resolution plan, or the methodologies and practices that support that plan, are not reasonable or appropriate; or (DD) the climate risk resolution plan otherwise constitutes an unsafe or unsound practice. (dd) General distribution limitation If the Board of Governors objects to a climate risk resolution plan submitted by a covered entity under item (aa), the covered entity may not make any capital distribution, other than a capital distribution arising from the issuance of a regulatory capital instrument eligible for inclusion in the numerator of a minimum regulatory capital ratio. .\n#### 7. Sub-systemic exploratory survey\n##### (a) Development of survey\nThe Board of Governors, in consultation with the Comptroller of the Currency and the Board of Directors of the Federal Deposit Insurance Corporation, shall develop a survey to assess\u2014\n**(1)**\nthe ability of surveyed entities to withstand each climate risk scenario developed under section 5;\n**(2)**\nwhich surveyed entities possess a large concentration of business activities in geographical areas or industries that are significantly exposed to the short- and long-term impacts of climate change; and\n**(3)**\nhow the surveyed entities identified under paragraph (2) plan to make adaptations to the business models and capital planning of those entities in response to the risks presented in each climate change risk scenario developed under section 5.\n##### (b) Administration of survey\n**(1) Initial administration**\n**(A) In general**\nNot later than 1 year after the completion of the first analysis under subparagraph (C) of section 165(i)(1) of the Financial Stability Act of 2010 ( 12 U.S.C. 5365(i)(1) ), as added by section 6 of this Act, the Board of Governors, in consultation with the Comptroller of the Currency and the Board of Directors of the Federal Deposit Insurance Corporation, shall administer the survey developed under subsection (a) to each surveyed entity.\n**(B) Assessment and report**\nNot later than 18 months after the date on which the Board of Governors completes the administration of the survey under subparagraph (A), the Board of Governors shall publicly release a report that\u2014\n**(i)**\nsummarizes the results of the survey; and\n**(ii)**\nanalyzes whether the planned actions of the surveyed entities, in the aggregate, are plausible and would be effective.\n**(2) Subsequent administration**\n**(A) In general**\nNot later than 2 years after the date on which the Board of Governors releases the report required under paragraph (1)(B), and biennially thereafter, the Board of Governors shall readminister to each surveyed entity the survey developed under subsection (a).\n**(B) Subsequent report**\nNot later than 180 days after the date on which each survey described under subparagraph (A) is completed, the Board of Governors shall publicly release a report that summarizes the results of the survey, which shall include the analysis described in paragraph (1)(B)(ii).\n##### (c) Effect of survey participation\nIn any report released with respect to a survey conducted under this section, the Board of Governors may not identify any individual surveyed entity that responded to the survey.\n##### (d) Rule of construction\nNothing in this section may be construed to preclude the Board of Governors from pursuing an enforcement action against a surveyed entity because of a violation discovered by the Board of Governors during an examination of the surveyed entity that is independent of a survey administered under this section.",
      "versionDate": "2025-04-10",
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
        "actionDate": "2025-04-10",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "1471",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Climate Change Financial Risk Act of 2025",
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-05-19T14:29:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-10",
    "originChamber": "House",
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
          "measure-id": "id119hr2823",
          "measure-number": "2823",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-10",
          "originChamber": "HOUSE",
          "update-date": "2026-03-02"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2823v00",
            "update-date": "2026-03-02"
          },
          "action-date": "2025-04-10",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Climate Change Financial Risk Act of 2025</strong></p><p>This bill addresses climate change risk and its potential impact on the financial system.</p><p>The Federal Reserve Board must develop financial risk analyses relating to climate change for certain large nonbank financial companies and bank holding companies. Specifically, these entities must be evaluated every two years on whether they have the capital necessary to absorb financial losses that would arise under several different climate change risk scenarios.\u00a0In response to the results of the evaluation, entities must develop and submit for approval a climate risk resolution plan. The plan must include a capital policy with respect to climate risk planning and targets to remedy identified vulnerabilities. If the plan is not approved, the entity\u2019s ability to make capital distributions is restricted.\u00a0</p><p>The bill also establishes the Climate Risk Scenario Technical Development Group to provide recommendations to the board regarding climate change risk scenarios, and determine the financial and economic risks of these scenarios.</p><p>The board must develop a survey to assess (1) the ability of other large financial institutions to withstand each scenario, (2) which surveyed entities have activities in geographical areas or industries that are significantly exposed to the impacts of climate change, and (3) how these surveyed entities plan to adapt to risks presented in each scenario.\u00a0</p>"
        },
        "title": "Climate Change Financial Risk Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2823.xml",
    "summary": {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Climate Change Financial Risk Act of 2025</strong></p><p>This bill addresses climate change risk and its potential impact on the financial system.</p><p>The Federal Reserve Board must develop financial risk analyses relating to climate change for certain large nonbank financial companies and bank holding companies. Specifically, these entities must be evaluated every two years on whether they have the capital necessary to absorb financial losses that would arise under several different climate change risk scenarios.\u00a0In response to the results of the evaluation, entities must develop and submit for approval a climate risk resolution plan. The plan must include a capital policy with respect to climate risk planning and targets to remedy identified vulnerabilities. If the plan is not approved, the entity\u2019s ability to make capital distributions is restricted.\u00a0</p><p>The bill also establishes the Climate Risk Scenario Technical Development Group to provide recommendations to the board regarding climate change risk scenarios, and determine the financial and economic risks of these scenarios.</p><p>The board must develop a survey to assess (1) the ability of other large financial institutions to withstand each scenario, (2) which surveyed entities have activities in geographical areas or industries that are significantly exposed to the impacts of climate change, and (3) how these surveyed entities plan to adapt to risks presented in each scenario.\u00a0</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr2823"
    },
    "title": "Climate Change Financial Risk Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-10",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Climate Change Financial Risk Act of 2025</strong></p><p>This bill addresses climate change risk and its potential impact on the financial system.</p><p>The Federal Reserve Board must develop financial risk analyses relating to climate change for certain large nonbank financial companies and bank holding companies. Specifically, these entities must be evaluated every two years on whether they have the capital necessary to absorb financial losses that would arise under several different climate change risk scenarios.\u00a0In response to the results of the evaluation, entities must develop and submit for approval a climate risk resolution plan. The plan must include a capital policy with respect to climate risk planning and targets to remedy identified vulnerabilities. If the plan is not approved, the entity\u2019s ability to make capital distributions is restricted.\u00a0</p><p>The bill also establishes the Climate Risk Scenario Technical Development Group to provide recommendations to the board regarding climate change risk scenarios, and determine the financial and economic risks of these scenarios.</p><p>The board must develop a survey to assess (1) the ability of other large financial institutions to withstand each scenario, (2) which surveyed entities have activities in geographical areas or industries that are significantly exposed to the impacts of climate change, and (3) how these surveyed entities plan to adapt to risks presented in each scenario.\u00a0</p>",
      "updateDate": "2026-03-02",
      "versionCode": "id119hr2823"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2823ih.xml"
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
      "title": "Climate Change Financial Risk Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-26T03:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Climate Change Financial Risk Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-26T03:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Board of Governors of the Federal Reserve System, in consultation with the heads of other relevant Federal agencies, to develop and conduct financial risk analyses relating to climate change, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-26T03:18:20Z"
    }
  ]
}
```
