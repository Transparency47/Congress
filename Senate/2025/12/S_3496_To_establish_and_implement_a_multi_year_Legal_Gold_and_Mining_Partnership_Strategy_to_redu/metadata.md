# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3496?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3496
- Title: United States Legal Gold and Mining Partnership Act
- Congress: 119
- Bill type: S
- Bill number: 3496
- Origin chamber: Senate
- Introduced date: 2025-12-16
- Update date: 2026-04-22T23:37:07Z
- Update date including text: 2026-04-22T23:37:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in Senate
- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 329.
- Latest action: 2025-12-16: Introduced in Senate

## Actions

- 2025-12-16 - IntroReferral: Introduced in Senate
- 2025-12-16 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 329.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3496",
    "number": "3496",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "United States Legal Gold and Mining Partnership Act",
    "type": "S",
    "updateDate": "2026-04-22T23:37:07Z",
    "updateDateIncludingText": "2026-04-22T23:37:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 329.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-02-10",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-01-29",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-16",
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
            "date": "2026-02-10T16:35:45Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:14Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:21:08Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
    },
    {
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "TX"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "NV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3496is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3496\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Cornyn (for himself, Mr. Kaine , Mr. Cruz , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo establish and implement a multi-year Legal Gold and Mining Partnership Strategy to reduce the negative environmental and social impacts of illicit gold mining in the Western Hemisphere, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the United States Legal Gold and Mining Partnership Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nSec. 4. Legal Gold and Mining Partnership Strategy.\nSec. 5. Classified briefing on illicit gold mining in Venezuela.\nSec. 6. Investigation of the illicit gold trade in Venezuela.\nSec. 7. Leveraging international support.\nSec. 8. Public-private partnership to build responsible gold value chains.\nSec. 9. Rule of construction regarding not authorizing the use of military force.\nSec. 10. Consideration of certain transactions involving precious metals for purposes of identifying primary money laundering concerns.\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe illicit mining, trafficking, and commercialization of gold in the Western Hemisphere\u2014\n**(A)**\nnegatively affects the region\u2019s economic and social dynamics;\n**(B)**\nstrengthens transnational criminal organizations and other international illicit actors; and\n**(C)**\nhas a deleterious impact on the environment, indigenous peoples, and food security.\n**(2)**\nA lack of economic opportunities and the weak rule of law promote illicit activities, such as illicit gold mining, which increases the vulnerability of individuals in mining areas, including indigenous communities, which have been subjected to trafficking in persons, other human rights abuses, and population displacement in relation to mining activity, particularly in the artisanal and small-scale mining sector.\n**(3)**\nIllicit gold mining in Latin America often involves and benefits transnational criminal organizations, drug trafficking organizations, terrorist groups, and other illegal armed groups that extort miners and enter into illicit partnerships with them in order to gain revenue from the illicit activity.\n**(4)**\nIllicit gold supply chains are international in nature and frequently involve\u2014\n**(A)**\nthe smuggling of gold and supplies, such as mercury;\n**(B)**\ntrade-based money laundering; and\n**(C)**\nother cross-border flows of illicit assets.\n**(5)**\nIn Latin America, mineral traders and exporters, local processors, and shell companies linked to transnational criminal networks and illegally armed groups all play a key role in the trafficking, laundering, and commercialization of illicit gold from the region.\n**(6)**\nAccording to a report on illegally mined gold in Latin America by the Global Initiative Against Transnational Organized Crime\u2014\n**(A)**\nmore than 70 percent of the gold mined in several Latin American countries, such as Colombia, Ecuador, and Peru, is mined through illicit means; and\n**(B)**\nabout 80 percent of the gold mined in Venezuela is mined through illicit means and a large percentage of such gold is sold\u2014\n**(i)**\nto Mibiturven, a joint venture operated by the Maduro regime composed of Minerven, a gold processor that has been designated by the Office of Foreign Assets Control of the Department of the Treasury, pursuant to Executive Order 13850 (relating to blocking property of additional persons contributing to the situation in Venezuela), and Marilyns Proje Yatirim, S.A., which is a Turkish company; or\n**(ii)**\nthrough other trafficking and commercialization networks from which the Maduro regime benefits financially.\n**(7)**\nIllegal armed groups and foreign terrorist organizations, such as the Ej\u00e9rcito de Liberaci\u00f3n Nacional (National Liberation Army\u2014ELN), work with transnational criminal organizations in Venezuela that participate in the illicit mining, trafficking, and commercialization of gold.\n**(8)**\nTransnational criminal organizations based in Venezuela, such as El Tren de Aragua, have expanded their role in the illicit mining, trafficking, and commercialization of gold to increase their criminal profits.\n**(9)**\nNicaragua\u2019s gold exports during 2023 were valued at an estimated $1,240,000,000, of which\u2014\n**(A)**\ngold valued at an estimated 637,000,000 was shipped to the United States;\n**(B)**\ngold valued at an estimated $353,000,000 was shipped to Canada;\n**(C)**\ngold valued at an estimated $244,000,000 was shipped to Switzerland; and\n**(D)**\ngold valued at an estimated $6,560,000 was shipped to Italy.\n**(10)**\nU.S. Customs and Border Protection has recognized that illegal logging is the world\u2019s most profitable natural resource crime and that profits from illegal logging finance illegal mining.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Financial Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Artisanal and small-scale mining; ASM**\nThe terms artisanal and small-scale mining and ASM refer to a form of mining common in the developing world that\u2014\n**(A)**\ntypically employs rudimentary, simple, and low-cost extractive technologies and manual labor-intensive techniques;\n**(B)**\nis frequently subject to limited regulation; and\n**(C)**\noften features harsh and dangerous working conditions.\n**(3) Key stakeholders**\nThe term key stakeholders means private sector organizations, industry representatives, and civil society groups that represent communities in areas affected by illicit mining and trafficking of gold, including indigenous groups, that are committed to the implementation of the Legal Gold and Mining Partnership Strategy.\n**(4) Legal gold and mining partnership strategy; strategy**\nThe terms Legal Gold and Mining Partnership Strategy and Strategy mean the strategy developed pursuant to section 4.\n**(5) Relevant Federal departments and agencies**\nThe term relevant Federal departments and agencies means the Department of State and all other Federal departments and agencies designated by the President as having significant domestic or foreign affairs equities in countering illicit mining.\n**(6) Secretary**\nThe term Secretary means the Secretary of State.\n#### 4. Legal Gold and Mining Partnership Strategy\n##### (a) Strategy required\nThe Secretary, in coordination with the heads of relevant Federal departments and agencies, shall develop a comprehensive, multi-year strategy, which shall be known as the Legal Gold and Mining Partnership Strategy, to combat illicit gold mining in the Western Hemisphere.\n##### (b) Elements\nThe Strategy shall include policies, programs, and initiatives\u2014\n**(1)**\nto interrupt the linkages between gold mining, including ASM, and illicit actors that profit from illicit mining in the Western Hemisphere;\n**(2)**\nto deter ASM in environmentally protected areas, such as national parks and conservation zones, to prevent mining-related contamination of critical natural resources, such as water resources, soil, tropical forests, and other flora and fauna, and aerosol contamination linked to detrimental health impacts;\n**(3)**\nto counter the financing and enrichment of actors involved in the illicit mining, trafficking, and commercialization of gold, and the abetting of their activities by\u2014\n**(A)**\npromoting the exercise of due diligence and the use of responsible sourcing methods in the purchase and trade of ASM;\n**(B)**\npreventing and prohibiting foreign persons who control commodity trading chains linked to illicit actors from enjoying the benefits of access to the territory, markets or financial system of the United States, and halting any such ongoing activity by such foreign persons;\n**(C)**\ncombating related impunity afforded to illicit actors by addressing corruption in government institutions and interrupting linkages between corrupt officials and illicit actors that exploit ASM miners;\n**(D)**\nsupporting the capacity of financial intelligence units, customs agencies, and other government institutions focused on anti-money laundering initiatives and combating the financing of criminal activities and terrorism to exercise oversight consistent with the threats posed by illicit gold mining; and\n**(E)**\nworking with the governments and appropriate institutions of countries that host gold refineries or processing centers to deter the importation of illicit gold and implement greater due diligence practices;\n**(4)**\nto build the capacity of foreign civilian law enforcement institutions in the Western Hemisphere to effectively counter\u2014\n**(A)**\nlinkages between illicit gold mining, illicit actors, money laundering, and other financial crimes, including trade-based money laundering;\n**(B)**\nlinkages between illicit gold mining, illicit actors, trafficking in persons, and forced or coerced labor, including sex work and child labor;\n**(C)**\nlinkages between illicit gold mining, illicit actors, and the illegal timber trade;\n**(D)**\nthe cross-border trafficking of illicit gold, and the mercury, cyanide, explosives, and other hazardous materials used in illicit gold mining, particularly those originating in China or trafficked by transnational criminal organizations; and\n**(E)**\nsurveillance and investigation of illicit and related activities that are related to or are indicators of illicit gold mining activities;\n**(5)**\nto ensure the successful implementation of the existing Memoranda of Understanding signed with the Governments of Peru and of Colombia in 2017 and 2018, respectively, to expand bilateral cooperation to combat illicit gold mining;\n**(6)**\nto work with governments in the Western Hemisphere, bolster the effectiveness of anti-money laundering efforts to combat the financing of illicit actors in Latin America and the Caribbean and counter the laundering of proceeds related to illicit gold mining by\u2014\n**(A)**\nfostering international and regional cooperation and facilitating intelligence sharing, as appropriate, to identify and disrupt financial flows related to the illicit gold mining, trafficking, and commercialization of gold and other minerals and illicit metals; and\n**(B)**\nsupporting the formulation of strategies to ensure the compliance of reporting institutions involved in the mining sector and to promote transparency in mining-sector transactions;\n**(7)**\nto support foreign government efforts\u2014\n**(A)**\nto facilitate licensing and formalization processes for ASM miners;\n**(B)**\nto develop mechanisms to support regulated cultural artisanal mining and artisanal mining as a job growth area; and\n**(C)**\nto implement existing environmental standards;\n**(8)**\nto engage the mining industry and relevant trade or industry associations to encourage the building of technical expertise in best practices and access to new technologies;\n**(9)**\nto support the establishment of gold commodity supply chain due diligence, responsible sourcing, tracing and tracking capacities, and standards-compliant commodity certification systems in countries in Latin America and the Caribbean, including efforts recommended in the OECD Due Diligence Guidance for Responsible Supply Chains of Minerals from Conflict-Affected and High Risk Areas, Third Edition (2016);\n**(10)**\nto engage with civil society to reduce the negative environmental impacts of ASM, particularly\u2014\n**(A)**\nthe use of mercury in preliminary refining;\n**(B)**\nthe destruction of tropical forests;\n**(C)**\nthe construction of illegal and unregulated dams and the resulting valley floods;\n**(D)**\nthe pollution of water resources and soil; and\n**(E)**\nthe release of dust, which can contain toxic chemicals and heavy metals that can cause severe health problems;\n**(11)**\nto aid and encourage ASM miners\u2014\n**(A)**\nto formalize their business activities, including through skills training, technical and business assistance, and access to financing, loans, and credit;\n**(B)**\nto utilize mercury-free gold refining technologies and mining methods that minimize deforestation, air pollution, and water and soil contamination;\n**(C)**\nto reduce the costs associated with formalization and compliance with mining regulations; and\n**(D)**\nto fully break away from the influence of illicit actors who leverage the control of territory and use violence to extort miners and push them into illicit arrangements;\n**(12)**\nto interrupt the illicit gold trade in Nicaragua, including through the use of targeted United States measures against the government led by President Daniel Ortega and Vice-President Rosario Murillo and their collaborators pursuant to Executive Order 14088 (relating to taking additional steps to address the national emergency with respect to the situation in Nicaragua), which was issued on October 24, 2022;\n**(13)**\nto assist local journalists with investigations of illicit mining, trafficking, and commercialization of gold and its supplies in the Western Hemisphere;\n**(14)**\nto promote responsible sourcing and due diligence at all levels of gold supply chains, including through the use of existing widely adopted, industry-standard responsible sourcing and due diligence standards; and\n**(15)**\nto prevent the intentional misinvoicing of the origins of gold shipments at transshipment points.\n##### (c) Assessment of challenges\nThe Strategy shall include an assessment of the challenges posed by, and policy recommendations to address\u2014\n**(1)**\nlinkages between ASM sector production and trade, particularly relating to gold, to the activities of illicit actors, including linkages that help to finance or enrich such illicit actors or abet their activities;\n**(2)**\nlinkages between illicit or grey market trade, and markets in gold and other metals or minerals and legal trade and commerce in such commodities, notably with respect to activities that abet the entry of such commodities into legal commerce, including\u2014\n**(A)**\nillicit cross-border trafficking, including with respect to goods, persons and illegal narcotics;\n**(B)**\nmoney-laundering;\n**(C)**\nthe financing of illicit actors or their activities; and\n**(D)**\nthe extralegal entry into the United States of\u2014\n**(i)**\nmetals or minerals, whether of legal foreign origin or not; and\n**(ii)**\nthe proceeds of such metals or minerals;\n**(3)**\nlinkages between the illicit mining, trafficking, and commercialization of gold, diamonds, and precious metals and stones, and the financial and political activities of the regime of Nicol\u00e1s Maduro of Venezuela;\n**(4)**\nfactors that\u2014\n**(A)**\nproduce linkages between ASM miners and illicit actors, prompting some ASM miners to utilize mining practices that are environmentally damaging and unsustainable, notably mining or related ore processing practices that\u2014\n**(i)**\ninvolve the use of elemental mercury; or\n**(ii)**\nresult in labor, health, environmental, and safety code infractions and workplace hazards; and\n**(B)**\nlead some ASM miners to operate in the extralegal or poorly regulated informal sector, and often prevent such miners from improving the socioeconomic status of themselves and their families and communities, or hinder their ability to formalize their operations, enhance their technical and business capacities, and access finance of fair market prices for their output;\n**(5)**\nmining-related trafficking in persons and forced or coerced labor, including sex work and child labor; and\n**(6)**\nthe use of elemental mercury and cyanide in ASM operations, including the technical aims and scope of such usage and its impact on human health and the environment, including flora, fauna, water resources, soil, and air quality.\n##### (d) Foreign assistance\nThe Strategy shall describe\u2014\n**(1)**\nexisting foreign assistance programs that address elements of the Strategy; and\n**(2)**\nadditional foreign assistance resources needed to fully implement the Strategy.\n##### (e) Best practices\nThe Strategy shall, to the extent practicable, avoid duplication of effort in the development of due diligence and responsible sourcing standards, including through the use of existing widely adopted industry standards.\n##### (f) Submission\nNot later than 180 days after the date of the enactment of this Act, the President shall submit the Strategy to the appropriate congressional committees.\n##### (g) Semiannual briefings\nNot later than 180 days after submission of the Strategy, and semiannually thereafter for the following 3 years, the Secretary, or the Secretary\u2019s designee, shall provide a briefing to the appropriate congressional committees regarding\u2014\n**(1)**\nthe implementation of the strategy, including efforts to leverage international support and develop a public-private partnership to build responsible gold value chains with other governments;\n**(2)**\nrevisions to the Strategy that are needed to better align the Strategy to new or emerging challenges in combating illicit gold mining; and\n**(3)**\nrecommendations from the Strategy that can be applied to combat illicit gold mining on a global scale.\n#### 5. Classified briefing on illicit gold mining in Venezuela\nNot later than 90 days after the date of the enactment of this Act, the Secretary, or the Secretary\u2019s designee, in coordination with the Director of National Intelligence, or the Director's designee, shall provide a classified briefing to the appropriate congressional committees, the Select Committee on Intelligence of the Senate , and the Permanent Select Committee on Intelligence of the House of Representatives that describes\u2014\n**(1)**\nthe activities related to illicit gold mining, including the illicit mining, trafficking, and commercialization of gold, inside Venezuelan territory carried out by illicit actors, including defectors from the Revolutionary Armed Forces of Colombia (FARC) and members of the National Liberation Army (ELN); and\n**(2)**\nVenezuela\u2019s illicit gold trade with foreign governments, including the Government of the Republic of Turkey and the Government of the Islamic Republic of Iran.\n#### 6. Investigation of the illicit gold trade in Venezuela\nThe Secretary, in coordination with the Secretary of the Treasury, the Attorney General, and allied and partner governments in the Western Hemisphere, shall\u2014\n**(1)**\nlead a coordinated international effort to carry out financial investigations to identify and track assets taken from the people and institutions in Venezuela that are linked to money laundering and illicit activities, including mining-related activities, by sharing financial investigations intelligence, as appropriate and as permitted by law; and\n**(2)**\nprovide technical assistance to help eligible governments in Latin America establish legislative and regulatory frameworks capable of imposing and effectively implementing targeted sanctions on\u2014\n**(A)**\nofficials of the Maduro regime who are directly engaged in the illicit mining, trafficking, and commercialization of gold; and\n**(B)**\nforeign persons engaged in the laundering of illicit gold assets linked to designated terrorist and drug trafficking organizations.\n#### 7. Leveraging international support\nIn implementing the Strategy pursuant to section 4, the President should direct United States representatives accredited to relevant multilateral institutions and development banks and United States ambassadors in the Western Hemisphere to use the influence of the United States to foster international cooperation to achieve the objectives of this Act, including\u2014\n**(1)**\nmarshaling resources and political support; and\n**(2)**\nencouraging the development of policies and consultation with key stakeholders to accomplish such objectives and provisions.\n#### 8. Public-private partnership to build responsible gold value chains\n##### (a) In general\nThe Secretary shall coordinate with the Governments of Colombia, of Ecuador, of Peru, and of other democratically elected governments in the region determined by the Secretary to establish a public-private partnership to support programming in participating countries that will\u2014\n**(1)**\nsupport the ASM gold mining sector's formalization and compliance with the existing environmental and labor standards in participating countries;\n**(2)**\nincrease awareness of access to financing for ASM gold miners who are taking significant steps to formalize their operations and comply with the existing labor and environmental standards in participating countries;\n**(3)**\nenhance the traceability and support the establishment of a certification process for ASM gold;\n**(4)**\nsupport a public relations campaign to promote responsibly sourced gold;\n**(5)**\ninclude representatives of local civil society to work towards soliciting the free and informed consent of those living on lands with mining potential;\n**(6)**\nfacilitate contact between vendors of responsibly sourced gold and United States companies; and\n**(7)**\npromote policies and practices in participating countries that are conducive to the formalization of ASM gold mining and promoting adherence of ASM to internationally recognized best practices and standards.\n#### 9. Rule of construction regarding not authorizing the use of military force\nNothing in this Act may be construed as authorizing the use of military force or the introduction of United States forces into hostilities.\n#### 10. Consideration of certain transactions involving precious metals for purposes of identifying primary money laundering concerns\nSection 5318A(c)(2) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby redesignating clauses (iii) through (vii) as clauses (iv) through (viii), respectively; and\n**(B)**\nby inserting after clause (ii) the following:\n(iii) the extent to which the jurisdiction or financial institutions operating in that jurisdiction facilitate transactions involving the mining, sale, or trade of precious metals subject to any sanctions imposed by the United States; ; and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby redesignating clauses (ii) and (iii) as clauses (iii) and (iv), respectively; and\n**(B)**\nby inserting after clause (i) the following:\n(ii) the extent to which such financial institutions are used to facilitate transactions involving the mining, sale, or trade of precious metals and are subject to any sanctions imposed by the United States; .",
      "versionDate": "2025-12-16",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3496rs.xml",
      "text": "II\nCalendar No. 329\n119th CONGRESS\n2d Session\nS. 3496\nIN THE SENATE OF THE UNITED STATES\nDecember 16, 2025 Mr. Cornyn (for himself, Mr. Kaine , Mr. Cruz , and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo establish and implement a multi-year Legal Gold and Mining Partnership Strategy to reduce the negative environmental and social impacts of illicit gold mining in the Western Hemisphere, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the United States Legal Gold and Mining Partnership Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Findings.\nSec. 3. Definitions.\nSec. 4. Legal Gold and Mining Partnership Strategy.\nSec. 5. Classified briefing on illicit gold mining in Venezuela.\nSec. 6. Investigation of the illicit gold trade in Venezuela.\nSec. 7. Leveraging international support.\nSec. 8. Public-private partnership to build responsible gold value chains.\nSec. 9. Rule of construction regarding not authorizing the use of military force.\nSec. 10. Consideration of certain transactions involving precious metals for purposes of identifying primary money laundering concerns.\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe illicit mining, trafficking, and commercialization of gold in the Western Hemisphere\u2014\n**(A)**\nnegatively affects the region\u2019s economic and social dynamics;\n**(B)**\nstrengthens transnational criminal organizations and other international illicit actors; and\n**(C)**\nhas a deleterious impact on the environment, indigenous peoples, and food security.\n**(2)**\nA lack of economic opportunities and the weak rule of law promote illicit activities, such as illicit gold mining, which increases the vulnerability of individuals in mining areas, including indigenous communities, which have been subjected to trafficking in persons, other human rights abuses, and population displacement in relation to mining activity, particularly in the artisanal and small-scale mining sector.\n**(3)**\nIllicit gold mining in Latin America often involves and benefits transnational criminal organizations, drug trafficking organizations, terrorist groups, and other illegal armed groups that extort miners and enter into illicit partnerships with them in order to gain revenue from the illicit activity.\n**(4)**\nIllicit gold supply chains are international in nature and frequently involve\u2014\n**(A)**\nthe smuggling of gold and supplies, such as mercury;\n**(B)**\ntrade-based money laundering; and\n**(C)**\nother cross-border flows of illicit assets.\n**(5)**\nIn Latin America, mineral traders and exporters, local processors, and shell companies linked to transnational criminal networks and illegally armed groups all play a key role in the trafficking, laundering, and commercialization of illicit gold from the region.\n**(6)**\nAccording to a report on illegally mined gold in Latin America by the Global Initiative Against Transnational Organized Crime\u2014\n**(A)**\nmore than 70 percent of the gold mined in several Latin American countries, such as Colombia, Ecuador, and Peru, is mined through illicit means; and\n**(B)**\nabout 80 percent of the gold mined in Venezuela is mined through illicit means and a large percentage of such gold is sold\u2014\n**(i)**\nto Mibiturven, a joint venture operated by the Maduro regime composed of Minerven, a gold processor that has been designated by the Office of Foreign Assets Control of the Department of the Treasury, pursuant to Executive Order 13850 (relating to blocking property of additional persons contributing to the situation in Venezuela), and Marilyns Proje Yatirim, S.A., which is a Turkish company; or\n**(ii)**\nthrough other trafficking and commercialization networks from which the Maduro regime benefits financially.\n**(7)**\nIllegal armed groups and foreign terrorist organizations, such as the Ej\u00e9rcito de Liberaci\u00f3n Nacional (National Liberation Army\u2014ELN), work with transnational criminal organizations in Venezuela that participate in the illicit mining, trafficking, and commercialization of gold.\n**(8)**\nTransnational criminal organizations based in Venezuela, such as El Tren de Aragua, have expanded their role in the illicit mining, trafficking, and commercialization of gold to increase their criminal profits.\n**(9)**\nNicaragua\u2019s gold exports during 2023 were valued at an estimated $1,240,000,000, of which\u2014\n**(A)**\ngold valued at an estimated 637,000,000 was shipped to the United States;\n**(B)**\ngold valued at an estimated $353,000,000 was shipped to Canada;\n**(C)**\ngold valued at an estimated $244,000,000 was shipped to Switzerland; and\n**(D)**\ngold valued at an estimated $6,560,000 was shipped to Italy.\n**(10)**\nU.S. Customs and Border Protection has recognized that illegal logging is the world\u2019s most profitable natural resource crime and that profits from illegal logging finance illegal mining.\n#### 3. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Financial Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Artisanal and small-scale mining; ASM**\nThe terms artisanal and small-scale mining and ASM refer to a form of mining common in the developing world that\u2014\n**(A)**\ntypically employs rudimentary, simple, and low-cost extractive technologies and manual labor-intensive techniques;\n**(B)**\nis frequently subject to limited regulation; and\n**(C)**\noften features harsh and dangerous working conditions.\n**(3) Key stakeholders**\nThe term key stakeholders means private sector organizations, industry representatives, and civil society groups that represent communities in areas affected by illicit mining and trafficking of gold, including indigenous groups, that are committed to the implementation of the Legal Gold and Mining Partnership Strategy.\n**(4) Legal gold and mining partnership strategy; strategy**\nThe terms Legal Gold and Mining Partnership Strategy and Strategy mean the strategy developed pursuant to section 4.\n**(5) Relevant Federal departments and agencies**\nThe term relevant Federal departments and agencies means the Department of State and all other Federal departments and agencies designated by the President as having significant domestic or foreign affairs equities in countering illicit mining.\n**(6) Secretary**\nThe term Secretary means the Secretary of State.\n#### 4. Legal Gold and Mining Partnership Strategy\n##### (a) Strategy required\nThe Secretary, in coordination with the heads of relevant Federal departments and agencies, shall develop a comprehensive, multi-year strategy, which shall be known as the Legal Gold and Mining Partnership Strategy, to combat illicit gold mining in the Western Hemisphere.\n##### (b) Elements\nThe Strategy shall include policies, programs, and initiatives\u2014\n**(1)**\nto interrupt the linkages between gold mining, including ASM, and illicit actors that profit from illicit mining in the Western Hemisphere;\n**(2)**\nto deter ASM in environmentally protected areas, such as national parks and conservation zones, to prevent mining-related contamination of critical natural resources, such as water resources, soil, tropical forests, and other flora and fauna, and aerosol contamination linked to detrimental health impacts;\n**(3)**\nto counter the financing and enrichment of actors involved in the illicit mining, trafficking, and commercialization of gold, and the abetting of their activities by\u2014\n**(A)**\npromoting the exercise of due diligence and the use of responsible sourcing methods in the purchase and trade of ASM;\n**(B)**\npreventing and prohibiting foreign persons who control commodity trading chains linked to illicit actors from enjoying the benefits of access to the territory, markets or financial system of the United States, and halting any such ongoing activity by such foreign persons;\n**(C)**\ncombating related impunity afforded to illicit actors by addressing corruption in government institutions and interrupting linkages between corrupt officials and illicit actors that exploit ASM miners;\n**(D)**\nsupporting the capacity of financial intelligence units, customs agencies, and other government institutions focused on anti-money laundering initiatives and combating the financing of criminal activities and terrorism to exercise oversight consistent with the threats posed by illicit gold mining; and\n**(E)**\nworking with the governments and appropriate institutions of countries that host gold refineries or processing centers to deter the importation of illicit gold and implement greater due diligence practices;\n**(4)**\nto build the capacity of foreign civilian law enforcement institutions in the Western Hemisphere to effectively counter\u2014\n**(A)**\nlinkages between illicit gold mining, illicit actors, money laundering, and other financial crimes, including trade-based money laundering;\n**(B)**\nlinkages between illicit gold mining, illicit actors, trafficking in persons, and forced or coerced labor, including sex work and child labor;\n**(C)**\nlinkages between illicit gold mining, illicit actors, and the illegal timber trade;\n**(D)**\nthe cross-border trafficking of illicit gold, and the mercury, cyanide, explosives, and other hazardous materials used in illicit gold mining, particularly those originating in China or trafficked by transnational criminal organizations; and\n**(E)**\nsurveillance and investigation of illicit and related activities that are related to or are indicators of illicit gold mining activities;\n**(5)**\nto ensure the successful implementation of the existing Memoranda of Understanding signed with the Governments of Peru and of Colombia in 2017 and 2018, respectively, to expand bilateral cooperation to combat illicit gold mining;\n**(6)**\nto work with governments in the Western Hemisphere, bolster the effectiveness of anti-money laundering efforts to combat the financing of illicit actors in Latin America and the Caribbean and counter the laundering of proceeds related to illicit gold mining by\u2014\n**(A)**\nfostering international and regional cooperation and facilitating intelligence sharing, as appropriate, to identify and disrupt financial flows related to the illicit gold mining, trafficking, and commercialization of gold and other minerals and illicit metals; and\n**(B)**\nsupporting the formulation of strategies to ensure the compliance of reporting institutions involved in the mining sector and to promote transparency in mining-sector transactions;\n**(7)**\nto support foreign government efforts\u2014\n**(A)**\nto facilitate licensing and formalization processes for ASM miners;\n**(B)**\nto develop mechanisms to support regulated cultural artisanal mining and artisanal mining as a job growth area; and\n**(C)**\nto implement existing environmental standards;\n**(8)**\nto engage the mining industry and relevant trade or industry associations to encourage the building of technical expertise in best practices and access to new technologies;\n**(9)**\nto support the establishment of gold commodity supply chain due diligence, responsible sourcing, tracing and tracking capacities, and standards-compliant commodity certification systems in countries in Latin America and the Caribbean, including efforts recommended in the OECD Due Diligence Guidance for Responsible Supply Chains of Minerals from Conflict-Affected and High Risk Areas, Third Edition (2016);\n**(10)**\nto engage with civil society to reduce the negative environmental impacts of ASM, particularly\u2014\n**(A)**\nthe use of mercury in preliminary refining;\n**(B)**\nthe destruction of tropical forests;\n**(C)**\nthe construction of illegal and unregulated dams and the resulting valley floods;\n**(D)**\nthe pollution of water resources and soil; and\n**(E)**\nthe release of dust, which can contain toxic chemicals and heavy metals that can cause severe health problems;\n**(11)**\nto aid and encourage ASM miners\u2014\n**(A)**\nto formalize their business activities, including through skills training, technical and business assistance, and access to financing, loans, and credit;\n**(B)**\nto utilize mercury-free gold refining technologies and mining methods that minimize deforestation, air pollution, and water and soil contamination;\n**(C)**\nto reduce the costs associated with formalization and compliance with mining regulations; and\n**(D)**\nto fully break away from the influence of illicit actors who leverage the control of territory and use violence to extort miners and push them into illicit arrangements;\n**(12)**\nto interrupt the illicit gold trade in Nicaragua, including through the use of targeted United States measures against the government led by President Daniel Ortega and Vice-President Rosario Murillo and their collaborators pursuant to Executive Order 14088 (relating to taking additional steps to address the national emergency with respect to the situation in Nicaragua), which was issued on October 24, 2022;\n**(13)**\nto assist local journalists with investigations of illicit mining, trafficking, and commercialization of gold and its supplies in the Western Hemisphere;\n**(14)**\nto promote responsible sourcing and due diligence at all levels of gold supply chains, including through the use of existing widely adopted, industry-standard responsible sourcing and due diligence standards; and\n**(15)**\nto prevent the intentional misinvoicing of the origins of gold shipments at transshipment points.\n##### (c) Assessment of challenges\nThe Strategy shall include an assessment of the challenges posed by, and policy recommendations to address\u2014\n**(1)**\nlinkages between ASM sector production and trade, particularly relating to gold, to the activities of illicit actors, including linkages that help to finance or enrich such illicit actors or abet their activities;\n**(2)**\nlinkages between illicit or grey market trade, and markets in gold and other metals or minerals and legal trade and commerce in such commodities, notably with respect to activities that abet the entry of such commodities into legal commerce, including\u2014\n**(A)**\nillicit cross-border trafficking, including with respect to goods, persons and illegal narcotics;\n**(B)**\nmoney-laundering;\n**(C)**\nthe financing of illicit actors or their activities; and\n**(D)**\nthe extralegal entry into the United States of\u2014\n**(i)**\nmetals or minerals, whether of legal foreign origin or not; and\n**(ii)**\nthe proceeds of such metals or minerals;\n**(3)**\nlinkages between the illicit mining, trafficking, and commercialization of gold, diamonds, and precious metals and stones, and the financial and political activities of the regime of Nicol\u00e1s Maduro of Venezuela;\n**(4)**\nfactors that\u2014\n**(A)**\nproduce linkages between ASM miners and illicit actors, prompting some ASM miners to utilize mining practices that are environmentally damaging and unsustainable, notably mining or related ore processing practices that\u2014\n**(i)**\ninvolve the use of elemental mercury; or\n**(ii)**\nresult in labor, health, environmental, and safety code infractions and workplace hazards; and\n**(B)**\nlead some ASM miners to operate in the extralegal or poorly regulated informal sector, and often prevent such miners from improving the socioeconomic status of themselves and their families and communities, or hinder their ability to formalize their operations, enhance their technical and business capacities, and access finance of fair market prices for their output;\n**(5)**\nmining-related trafficking in persons and forced or coerced labor, including sex work and child labor; and\n**(6)**\nthe use of elemental mercury and cyanide in ASM operations, including the technical aims and scope of such usage and its impact on human health and the environment, including flora, fauna, water resources, soil, and air quality.\n##### (d) Foreign assistance\nThe Strategy shall describe\u2014\n**(1)**\nexisting foreign assistance programs that address elements of the Strategy; and\n**(2)**\nadditional foreign assistance resources needed to fully implement the Strategy.\n##### (e) Best practices\nThe Strategy shall, to the extent practicable, avoid duplication of effort in the development of due diligence and responsible sourcing standards, including through the use of existing widely adopted industry standards.\n##### (f) Submission\nNot later than 180 days after the date of the enactment of this Act, the President shall submit the Strategy to the appropriate congressional committees.\n##### (g) Semiannual briefings\nNot later than 180 days after submission of the Strategy, and semiannually thereafter for the following 3 years, the Secretary, or the Secretary\u2019s designee, shall provide a briefing to the appropriate congressional committees regarding\u2014\n**(1)**\nthe implementation of the strategy, including efforts to leverage international support and develop a public-private partnership to build responsible gold value chains with other governments;\n**(2)**\nrevisions to the Strategy that are needed to better align the Strategy to new or emerging challenges in combating illicit gold mining; and\n**(3)**\nrecommendations from the Strategy that can be applied to combat illicit gold mining on a global scale.\n#### 5. Classified briefing on illicit gold mining in Venezuela\nNot later than 90 days after the date of the enactment of this Act, the Secretary, or the Secretary\u2019s designee, in coordination with the Director of National Intelligence, or the Director's designee, shall provide a classified briefing to the appropriate congressional committees, the Select Committee on Intelligence of the Senate , and the Permanent Select Committee on Intelligence of the House of Representatives that describes\u2014\n**(1)**\nthe activities related to illicit gold mining, including the illicit mining, trafficking, and commercialization of gold, inside Venezuelan territory carried out by illicit actors, including defectors from the Revolutionary Armed Forces of Colombia (FARC) and members of the National Liberation Army (ELN); and\n**(2)**\nVenezuela\u2019s illicit gold trade with foreign governments, including the Government of the Republic of Turkey and the Government of the Islamic Republic of Iran.\n#### 6. Investigation of the illicit gold trade in Venezuela\nThe Secretary, in coordination with the Secretary of the Treasury, the Attorney General, and allied and partner governments in the Western Hemisphere, shall\u2014\n**(1)**\nlead a coordinated international effort to carry out financial investigations to identify and track assets taken from the people and institutions in Venezuela that are linked to money laundering and illicit activities, including mining-related activities, by sharing financial investigations intelligence, as appropriate and as permitted by law; and\n**(2)**\nprovide technical assistance to help eligible governments in Latin America establish legislative and regulatory frameworks capable of imposing and effectively implementing targeted sanctions on\u2014\n**(A)**\nofficials of the Maduro regime who are directly engaged in the illicit mining, trafficking, and commercialization of gold; and\n**(B)**\nforeign persons engaged in the laundering of illicit gold assets linked to designated terrorist and drug trafficking organizations.\n#### 7. Leveraging international support\nIn implementing the Strategy pursuant to section 4, the President should direct United States representatives accredited to relevant multilateral institutions and development banks and United States ambassadors in the Western Hemisphere to use the influence of the United States to foster international cooperation to achieve the objectives of this Act, including\u2014\n**(1)**\nmarshaling resources and political support; and\n**(2)**\nencouraging the development of policies and consultation with key stakeholders to accomplish such objectives and provisions.\n#### 8. Public-private partnership to build responsible gold value chains\n##### (a) In general\nThe Secretary shall coordinate with the Governments of Colombia, of Ecuador, of Peru, and of other democratically elected governments in the region determined by the Secretary to establish a public-private partnership to support programming in participating countries that will\u2014\n**(1)**\nsupport the ASM gold mining sector's formalization and compliance with the existing environmental and labor standards in participating countries;\n**(2)**\nincrease awareness of access to financing for ASM gold miners who are taking significant steps to formalize their operations and comply with the existing labor and environmental standards in participating countries;\n**(3)**\nenhance the traceability and support the establishment of a certification process for ASM gold;\n**(4)**\nsupport a public relations campaign to promote responsibly sourced gold;\n**(5)**\ninclude representatives of local civil society to work towards soliciting the free and informed consent of those living on lands with mining potential;\n**(6)**\nfacilitate contact between vendors of responsibly sourced gold and United States companies; and\n**(7)**\npromote policies and practices in participating countries that are conducive to the formalization of ASM gold mining and promoting adherence of ASM to internationally recognized best practices and standards.\n#### 9. Rule of construction regarding not authorizing the use of military force\nNothing in this Act may be construed as authorizing the use of military force or the introduction of United States forces into hostilities.\n#### 10. Consideration of certain transactions involving precious metals for purposes of identifying primary money laundering concerns\nSection 5318A(c)(2) of title 31, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A)\u2014\n**(A)**\nby redesignating clauses (iii) through (vii) as clauses (iv) through (viii), respectively; and\n**(B)**\nby inserting after clause (ii) the following:\n(iii) the extent to which the jurisdiction or financial institutions operating in that jurisdiction facilitate transactions involving the mining, sale, or trade of precious metals subject to any sanctions imposed by the United States; ; and\n**(2)**\nin subparagraph (B)\u2014\n**(A)**\nby redesignating clauses (ii) and (iii) as clauses (iii) and (iv), respectively; and\n**(B)**\nby inserting after clause (i) the following:\n(ii) the extent to which such financial institutions are used to facilitate transactions involving the mining, sale, or trade of precious metals and are subject to any sanctions imposed by the United States; .",
      "versionDate": "2026-02-10",
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
        "actionDate": "2025-02-27",
        "text": "Read twice and referred to the Committee on Foreign Relations."
      },
      "number": "799",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "United States Legal Gold and Mining Partnership Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Colombia",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Crime prevention",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Drug trafficking and controlled substances",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Ecuador",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Environmental health",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Hazardous wastes and toxic substances",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2026-04-15T16:55:34Z"
          },
          {
            "name": "Metals",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Mining",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Nicaragua",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Peru",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Public-private cooperation",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Terrorism",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Venezuela",
            "updateDate": "2026-04-15T16:55:33Z"
          },
          {
            "name": "Wildlife conservation and habitat protection",
            "updateDate": "2026-04-15T16:55:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-01-12T22:34:07Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3496is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3496rs.xml"
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
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "United States Legal Gold and Mining Partnership Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "title": "United States Legal Gold and Mining Partnership Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "United States Legal Gold and Mining Partnership Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-10T09:09:05Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish and implement a multi-year Legal Gold and Mining Partnership Strategy to reduce the negative environmental and social impacts of illicit gold mining in the Western Hemisphere, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-10T09:03:24Z"
    }
  ]
}
```
