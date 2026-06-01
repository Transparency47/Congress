# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8615?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8615
- Title: FLEETS Now Act
- Congress: 119
- Bill type: HR
- Bill number: 8615
- Origin chamber: House
- Introduced date: 2026-04-30
- Update date: 2026-05-29T16:38:31Z
- Update date including text: 2026-05-29T16:38:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-30: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- Latest action: 2026-04-30: Introduced in House

## Actions

- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Introduced in House
- 2026-04-30 - IntroReferral: Referred to the House Committee on Foreign Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-30",
    "latestAction": {
      "actionDate": "2026-04-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8615",
    "number": "8615",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "K000397",
        "district": "40",
        "firstName": "Young",
        "fullName": "Rep. Kim, Young [R-CA-40]",
        "lastName": "Kim",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "FLEETS Now Act",
    "type": "HR",
    "updateDate": "2026-05-29T16:38:31Z",
    "updateDateIncludingText": "2026-05-29T16:38:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-30",
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
          "date": "2026-04-30T13:08:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "NY"
    },
    {
      "bioguideId": "R000600",
      "district": "0",
      "firstName": "Aumua Amata",
      "fullName": "Del. Radewagen, Aumua Amata Coleman [R-AS-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Radewagen",
      "middleName": "Coleman",
      "party": "R",
      "sponsorshipDate": "2026-04-30",
      "state": "AS"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8615ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8615\nIN THE HOUSE OF REPRESENTATIVES\nApril 30, 2026 Mrs. Kim (for herself, Mr. Lawler , and Mrs. Radewagen ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo combat China\u2019s unfair and non-market-oriented trade practices related to the shipbuilding industry, and for other purposes.\n#### 1. Short title and table of contents\n##### (a) Short title\nThis Act may be cited as the Facilitating Leadership and Expertise through Exchange and Training in Shipbuilding Now Act of 2026 or the FLEETS Now Act .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec.\u20021.\u2002Short title and table of contents.\nSec.\u20022.\u2002Findings.\nSec.\u20023.\u2002Definitions.\nTitle I\u2014Matters relating to shipbuilding and the People\u2019s Republic of China\nSec.\u2002101.\u2002Strategic ports; United States International Development Finance Corporation.\nSec.\u2002102.\u2002Briefing and report on China Ocean Shipping Company Shipping Heavy Industry and China State Shipbuilding Corporation.\nTitle II\u2014Matters relating to shipbuilding and the United States, its allies and partners, and the international community\nSec.\u2002201.\u2002Statement of policy to counter shipbuilding practices of the People\u2019s Republic of China.\nSec.\u2002202.\u2002International shipbuilding coordination responsibility.\nSec.\u2002203.\u2002Assistant Secretary for Water, Environment, and Space Affairs.\nSec.\u2002204.\u2002Exchange program for shipbuilding industry experts.\nSec.\u2002205.\u2002Maritime investigators.\nSec.\u2002206.\u2002Allied maritime framework.\nSec.\u2002207.\u2002Maritime group of nations.\nSec.\u2002208.\u2002International Maritime Organization.\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe People\u2019s Republic of China (hereafter in this section referred to as the PRC ) has deployed unfair and non-market-oriented practices in the maritime, logistics, and shipbuilding sectors to achieve a long-term dominant position in the shipbuilding ecosystem. In response, the United States Trade Representative launched an investigation under title III of the Trade Act of 1974 in April 2024, and reaffirmed its allegations in a notice of proposed actions in February 2025.\n**(2)**\nThe PRC\u2019s Military-Civil Fusion strategy uses the opacity of China\u2019s business ecosystem to channel commercial activities\u2014including foreign shipbuilding orders\u2014into upgrading its naval industrial base. By integrating commercial and military production at shared shipyards, the PRC enables the transfer of capital, technology, personnel, and supply chains to China\u2019s defense industrial base, strengthening military capabilities through civilian contracts.\n**(3)**\nThe PRC frames its shipbuilding and maritime sectors as strategic industries that must be targeted to build economic, technological and military power. This targeting necessarily means the displacement of foreign firms from existing markets, and taking new markets as they present, which diminishes competition. The United States has not taken sufficient action to counter the PRC and protect United States enterprises.\n**(4)**\nBy achieving dominant market positions, the PRC exercises increasing influence over global supply, pricing, and access to goods and services.\n**(5)**\nThe PRC\u2019s targeting of the maritime, logistics, and shipbuilding sectors creates dependencies on China, increasing risk and reducing supply chain resilience. The PRC seeks to displace foreign competitors throughout the maritime value chain in domestic and foreign markets, increasing the world\u2019s dependence on the PRC for products, services, and technology.\n**(6)**\nInternational dependencies on the PRC increases risks (potential disruptions, whether natural, accidental, or politically motivated) for individual firms and their workers, for economic sectors, and supply chain resilience. The PRC has demonstrated its willingness to weaponize dependencies for the purpose of economic coercion.\n**(7)**\nThe PRC\u2019s control over Chinese economic actors in the maritime, logistics, and shipbuilding sectors enables China to direct and influence commercial behavior in pursuit of market dominance in ways that run counter to fair competition and market-oriented principles.\n**(8)**\nThe PRC\u2019s industrial plans identify a matrix of mechanisms that are used to achieve market dominance, including government financial support, barriers for foreign firms, consolidation policies, measures associated with forced technology transfer and intellectual property theft, state-led investments, and government procurement.\n**(9)**\nAs a result of the PRC\u2019s market distortion, Chinese maritime, logistics, and shipbuilding sectors accrue a wide range of non-market advantages, such as artificially low costs or preferential supply from China\u2019s non-market excess capacity, including in steel, China\u2019s lack of effective labor rights, and China\u2019s control over digital logistics services.\n**(10)**\nThe PRC\u2019s direct intervention in the shipbuilding market makes ships built in the United States and elsewhere commercially less competitive. Less than one percent of new commercial ships are built in the United States and domestic shipbuilding is almost exclusively for military use.\n**(11)**\nIn 2024, the PRC accounted for 53.3 percent of the global shipbuilding industry and the China State Shipbuilding Corporation built more commercial ships by tonnage in 2024 than the entire United States shipbuilding industry has built since the end of World War II.\n**(12)**\nThe state-owned shipbuilding conglomerates like China Ocean Shipping Company Shipping Heavy Industry and China State Shipbuilding Corporation are China\u2019s largest commercial shipbuilding corporations and the primary entities responsible for the buildup of the People\u2019s Liberation Army Navy into the world\u2019s largest navy enabling the PRC to increase its capacity to undermine United States national security interests.\n**(13)**\nThe shipbuilding capacity of the United States has been weakened by decades of neglect, leading to a contraction of a once vibrant domestic maritime workforce while simultaneously empowering our adversaries, eroding United States national security, and reducing American jobs in the maritime sector.\n**(14)**\nIncreasing domestic shipbuilding capacity is essential to restoring America\u2019s maritime strength and self-sufficiency. This will require coordinated action across procurement policy, capital investment, supplier resilience, and workforce development.\n**(15)**\nAccording to America\u2019s Maritime Action Plan from February 2026, the United States does not have the capacity necessary to scale up the domestic shipbuilding industry to the rate required to meet national priorities.\n**(16)**\nFor decades, the United States strategic position and shipbuilding industrial capacity have been weakened, in part, by cumbersome Government procurement processes, a lack of strategic support for construction of commercial vessels in domestic shipyards, and the degradation of Federal financial investment in the Maritime Industrial Base.\n**(17)**\nStrengthening the United States maritime sector requires leveraging international and industry partnerships to align trade policies to enhance investment in the United States maritime sector. By creating clear pathways for foreign direct investments in United States shipyards, suppliers, and maritime infrastructure, the United States can expand domestic capacity while reinforcing relationships abroad.\n**(18)**\nCurrently, foreign firms are severely disadvantaged in competing with the resources of the Chinese state, resulting in lost sales, under-investment in capacity, diminished ability to attract financing, and lost jobs and lower wages.\n**(19)**\nForeign companies, including firms based in many United States-allied countries purchase 75 percent of the ships built at China\u2019s dual-use shipyards, funneling billions of dollars in revenue and transferring key technologies into the People\u2019s Liberation Army naval industrial base.\n**(20)**\nThe United States does not have a single agency or department charged with designing and implementing industrial shipbuilding policy. As a result, there is no single official charged with protecting and expanding the domestic shipbuilding industry in the United States. This creates inefficiency in reinvigorating the United States shipbuilding industry and confusion when engaging international partners about joint strategies for diversifying shipbuilding supply chains.\n**(21)**\nThe President\u2019s Maritime Action Plan outlines a strategy for reclaiming America\u2019s maritime strength, ensuring the Nation can defend its interests and ferry its trade. In implementing the Maritime Action Plan, the United States will modernize its procurement processes and streamline regulations to accelerate shipbuilding and reduce costs.\n#### 3. Definitions\nIn this Act:\n**(1) Allied country**\nThe term allied country has the meaning given such term in section 2350f(d) of title 10, United States Code.\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate.\n**(3) Deck-plate professional**\nThe term deck-plate professional means a skilled worker who operates directly on the production floor as a skilled tradesperson with specialized expertise related to a ship\u2019s systems and functionality.\n**(4) Foreign country of concern**\nThe term foreign country of concern has the meaning given the term covered nation in section 4872(f) of title 10, United States Code.\n**(5) Unreasonable refusal to deal**\nThe term unreasonable refusal to deal has the meaning given that term for purposes of section 7(d) of the Ocean Shipping Reform Act of 2022 ( 46 U.S.C. 41104 note).\nI\nMatters relating to shipbuilding and the People\u2019s Republic of China\n#### 101. Strategic ports; United States International Development Finance Corporation\nThe Better Utilization of Investments Leading to Development Act of 2018 is amended\u2014\n**(1)**\nin section 1402(3) ( 22 U.S.C. 9601(3) )\u2014\n**(A)**\nby striking subparagraph (A); and\n**(B)**\nby redesignating subparagraphs (B) through (G) as subparagraphs (A) through (F), respectively; and\n**(2)**\nin section 1412(f) ( 22 U.S.C. 9612(f) ), by adding at the end the following:\n(4) Harbors or ports (as such terms are defined in section 3 of the Communications Act of 1934 ( 47 U.S.C. 153 )) and related infrastructure. .\n#### 102. Briefing and report on China Ocean Shipping Company Shipping Heavy Industry and China State Shipbuilding Corporation\n##### (a) Briefing\nNot later than 1 year after the date of the enactment of this Act, the Secretary of State, in coordination with the heads of other Federal agencies and departments the Secretary determines relevant, shall brief the appropriate congressional committees on\u2014\n**(1)**\ncompanies or entities with formal or informal financial relationships with\u2014\n**(A)**\nthe China Ocean Shipping Company Shipping Heavy Industry; or\n**(B)**\nthe China State Shipbuilding Corporation; and\n**(2)**\nthe business practices of such companies and entities.\n##### (b) Report\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for 3 years, the President shall submit to the appropriate congressional committees a report that includes the following:\n**(1)**\nA description of each current and former subsidiary of the China Ocean Shipping Company Shipping Heavy Industry and the China State Shipbuilding Corporation.\n**(2)**\nAny trading practices of any such entities that are subject to review by the United States Trade Representative for being unreasonable, discriminatory, or violating trade agreements.\n**(3)**\nThe degree and extent of direct involvement by the Government of the People\u2019s Republic of China in the governance, strategic direction, planning, and commercial operations of\u2014\n**(A)**\nthe China Ocean Shipping Company Shipping Heavy Industry;\n**(B)**\nthe China State Shipbuilding Corporation; and\n**(C)**\nthe Chinese shipbuilding industry.\n**(4)**\nA description of each shipyard in China that is producing warships for the People\u2019s Liberation Army Navy or producing dual-use commercial ships, including ferries and barges, that may be used by the People\u2019s Liberation Army Navy.\n**(5)**\nAn indication of which such shipyards are conducting business with non-People\u2019s Republic of China foreign entities and potentially thereby facilitating the modernization of the People\u2019s Liberation Army Navy.\nII\nMatters relating to shipbuilding and the United States, its allies and partners, and the international community\n#### 201. Statement of policy to counter shipbuilding practices of the People\u2019s Republic of China\nIt is the policy of the United States to develop a domestic capacity to produce ships for both commercial and military application independent of supply chains that include materials sourced from the People\u2019s Republic of China. Such policy shall be given effect, among other things, through a comprehensive effort, in coordination with allies and partners of the United States where appropriate, that includes\u2014\n**(1)**\nrelevant knowledge transfer to and skillset development of a shipbuilding labor force in the United States;\n**(2)**\nsecuring direct investment in United States shipyards by allies and partners; and\n**(3)**\nthe development of a coherent long-term strategy to diversify shipbuilding supply chains and expand domestic shipbuilding capacity, incorporating all relevant Federal agencies and departments.\n#### 202. International shipbuilding coordination responsibility\nNot later than 90 days after the date of the enactment of this Act, the President shall designate an individual as the primary point of contact in the United States Government for purposes of\u2014\n**(1)**\nattracting international shipbuilding investment opportunities in the United States;\n**(2)**\nleading cooperation with the governments of foreign countries on international shipbuilding supply chain diversification; and\n**(3)**\nleading engagement on behalf of the United States Government for coordination of international shipbuilding industries in a manner that creates supply chain resilience and protects the national security interests of the United States.\n#### 203. Assistant Secretary for Water, Environment, and Space Affairs\nSection 9 of the Department of State Appropriations Authorization Act of 1973 ( 22 U.S.C. 2655a ) is amended to read as follows:\n9. Assistant Secretary for Water, Environment, and Space Affairs (a) Establishment There is authorized to be in the Department of State an Assistant Secretary for Water, Environment, and Space Affairs, who shall be responsible to the Under Secretary for Economic Affairs for matters pertaining to space, oceans and maritime diplomacy, polar affairs, environmental quality, freshwater, fisheries, wildlife and wildlife trafficking, conservation, and such other related duties as the Secretary may from time to time designate. (b) Responsibilities In addition to the responsibilities described under subsection (a), the Assistant Secretary for Water, Environment, and Space Affairs shall maintain continuous observation and coordination of all matters pertaining to oceans and maritime diplomacy, fisheries, natural resource conservation, and outer space in the conduct of foreign policy, including, as appropriate, the following: (1) Developing United States policy on global environmental security issues with respect to oceans, fisheries, the Antarctic region, waste and global pollution, and water and other natural resource management and conservation. (2) Representing the Department in bilateral and multilateral negotiations involving the law of the sea, including\u2014 (A) freedom of navigation, overflight, and other lawful uses of the ocean; (B) maritime security; (C) United States maritime zones, including the United States extended continental shelf; (D) marine science; (E) the sustainable management and protection of marine habitats and resources; (F) marine pollution; and (G) maritime claims and boundaries. (3) Leading United States engagement on Antarctica and in international oceans agreements and conventions with foreign governments and international organizations, to promote solutions that advance United States national security, economic, and environmental interests. (4) Coordinating the development of policies and programs to conserve and manage economically important ecosystems, including, forests, wetlands, drylands, and coral reefs. (5) Developing policies and programs to address international threats to natural resources, such as illicit trade, illegal, unreported and unregulated fishing, wildlife trafficking, and illegal logging and associated trade. (6) Developing and implementing United States foreign policy related to air, water and soil pollution and risks to human health and the environment caused by the transboundary movement of hazardous chemicals and waste and other forms of pollution to promote environmental security, with trade partners and in multilateral institutions. (7) Representing the Department in bilateral and multilateral engagements including organizations, institutions, and negotiation of international agreements on related issues. (8) Developing policies and programs, in coordination with the National Aeronautics and Space Administration, the Department of Commerce, and other relevant Federal departments and agencies, as appropriate, to support partnerships between the United States and international and private industry partners in the development of infrastructure and policies that expand economic growth in outer space, including\u2014 (A) countering malign efforts by foreign adversaries and other actors that threaten United States interests in civil and commercial space; and (B) expanding access to foreign markets for United States commercial industry, including by encouraging reforms that reduce barriers to trade and cooperation with United States civil and commercial space actors. (9) Leading bilateral and multilateral engagements related to civil and commercial space activities, resilient space services, burden sharing, and other matters related to international space law and diplomacy and other United States international obligations and commitments. (10) Leading United States Government engagement with international Global Navigation Satellite Systems providers to ensure compatibility and encourage interoperability of civil global navigation satellite services on United States-based global positioning systems, including through the International Committee on Global Navigation Satellite Systems. (11) Leading Department efforts to implement international arrangements and promote cooperation on Earth observation satellite systems. (12) Leading Department engagement in multilateral and bilateral forums on international space policy, space law, and commercial and civil treaties or agreements. (13) Leading Department efforts on transparency in space by maintaining the official United States space object registry and promoting best practices for safe operations in space, preservation of the space environment, space traffic coordination, and space situational awareness. (14) Leading Department efforts to align foreign space law, regulatory, and policy frameworks with United States-endorsed models, approaches, and best practices. (15) At the direction of the Under Secretary for Economic Affairs and the Secretary of State, represent the United States in international maritime diplomacy matters, including\u2014 (A) the creation and operation of the Allied Maritime Framework under section 206 of the FLEETS Now Act ; (B) the development of the report under section 103; and (C) leading United States engagement in the Maritime Group of Nations under section 207 of the FLEETS Now Act. (16) Authoring any reports produced by the Department which examine the maritime claims and boundaries of coastal countries and assessing their consistency with international law. (17) Performing such other duties as the Under Secretary for Economic Affairs may from time to time designate. (c) Appointment (1) Initial appointment On the date of the enactment of the FLEETS Now Act, the individual serving as the Assistant Secretary for Oceans and International Environmental and Scientific Affairs on the day before such date of enactment shall be the Assistant Secretary for Water, Environment, and Space Affairs. (2) Subsequent appointment Any subsequent appointment of an individual to the position of Assistant Secretary for Water, Environment, and Space Affairs shall be subject to the advice and consent of the Senate. (d) Establishment of Bureau of Water, Environment, and Space Affairs The Secretary shall establish a Bureau of Water, Environment, and Space Affairs, which shall perform such functions related to space, oceans, environmental quality, fisheries, wildlife, wildlife trafficking, and conservation affairs as the Under Secretary for Economic Affairs may prescribe. (e) Assistant Secretary The Assistant Secretary for Water, Environment, and Space Affairs shall be the head of the Bureau of Water, Environment, and Space Affairs. .\n#### 204. Exchange program for shipbuilding industry experts\n##### (a) Sense of Congress\nIt is the sense of the Congress that the Secretary of State should initiate an exchange visitor program of technical shipbuilding expertise to increase shipbuilding knowledge, training, experience, and expertise in the American shipbuilding workforce.\n##### (b) Authorization To provide for exchanges\nSection 102(b) of the Mutual Educational and Cultural Exchange Act of 1961 ( 22 U.S.C. 2452(b) ) is amended\u2014\n**(1)**\nin paragraph (11), by striking and at the end;\n**(2)**\nin paragraph (12), by striking the period and inserting ; and ; and\n**(3)**\nby inserting at the end the following:\n(13) interchanges and visits between the United States and other countries of marine engineers, naval architects, electrical engineers, deck-plate professionals, marine surveyors, shipyard infrastructure analysts, quality assurance and quality control personnel, shipyard project managers, and other experts related to the shipbuilding industry until the date that is 2 years after the date of the enactment of this paragraph. .\n#### 205. Maritime investigators\n##### (a) In general\nThe Secretary of State shall, in coordination with the Chair of the Federal Maritime Commission, detail to countries described in subsection (b) personnel from the Division for Trade Policy and Negotiations of the Bureau of Economic and Business Affairs for the purpose of investigating\u2014\n**(1)**\nunfair shipping practices, including price-fixing, market manipulation, or unreasonable refusal to deal;\n**(2)**\nspecific actions by foreign governments to deny port of entry to United States-flagged vessels;\n**(3)**\nflags of convenience to determine if lower safety, labor, and environmental standards in foreign countries create unfavorable shipping conditions for United States trade;\n**(4)**\nanticompetitive agreements between ocean carriers and marine terminal operators for potential antitrust issues; and\n**(5)**\nmapping the financial relationships of shipping companies of the People\u2019s Republic of China, including the Ocean Alliance.\n##### (b) Locations of investigators\nThe personnel described in subsection (a) shall be detailed to diplomatic and consular posts in countries that meet each of the following criteria:\n**(1)**\nThe country is among the top 5 countries globally by ship registry size and maintains an open registry , allowing foreign-owned vessels to register under the flag of such country without a residency requirement (also known as a flag of convenience policy).\n**(2)**\nThe country is among the top 15 countries globally with respect to not less than 2 of the following criteria:\n**(A)**\nShipbuilding, as measured by tonnage as a percentage of global total.\n**(B)**\nNumber of citizens or nationals who are merchant mariners.\n**(C)**\nNumber of commercially owned ships greater than 1,000 gross weight tonnage.\n##### (c) Inclusion of findings in investment climate statement\nSection 707(b) of the Further Consolidated Appropriations Act, 2020 ( 22 U.S.C. 9903 ) is amended by inserting after paragraph (11) the following new paragraph:\n(12) Information about unfair business practices in the maritime, logistics, and shipbuilding sectors in each applicable country or region, including\u2014 (A) price-fixing; (B) market manipulation; (C) unreasonable refusal to deal (as such term is defined for purposes of section 7(d) of the Ocean Shipping Reform Act of 2022 ( 46 U.S.C. 41104 note)); and (D) anticompetitive agreements between ocean carriers and marine terminal operators. .\n##### (d) Disclosure of certain investments by countries receiving aid\nSection 7031(b)(2) of division K of the Consolidated Appropriations Act, 2014 ( Public Law 113\u201376 ; 128 Stat. 510) is amended by inserting and investments in maritime, logistics, and shipbuilding sectors after allocation practices) .\n#### 206. Allied maritime framework\n##### (a) In general\nThe President, acting through the individual designated pursuant to section 202 and in coordination with other relevant agencies and departments, shall engage allied countries to develop a shared framework to enhance collective capacity to design, produce, and maintain military and civilian ships, through\u2014\n**(1)**\nenhancing information exchange between such countries regarding such design, production, and maintenance;\n**(2)**\nexpanding procompetitive industrial collaboration with respect to such ships; and\n**(3)**\nstrengthening the marine industries and the shipbuilding industries in allied countries.\n##### (b) Elements\nThe framework required in subsection (a) shall include\u2014\n**(1)**\nthe establishment of a mechanism to\u2014\n**(A)**\nensure countries participating in the framework can access reciprocal ports and shipping support during crises and conflicts;\n**(B)**\nco-develop best-in-class design principles for the construction of ships;\n**(C)**\ncollaborate, on a reciprocal basis, on the construction, repair, interoperability, and other capabilities of new ships to reduce costs;\n**(D)**\nestablish guiding principles for production line sequencing and supply chain management;\n**(E)**\ncoordinate Cabinet or Minister-level recommendations to drive down the production costs of ships and accelerate the delivery of ships, consistent with relevant laws in the relevant countries;\n**(F)**\nestablish a process for determining specific ship types or industry niches that are best suited for allied cooperation, including icebreakers, support ships, oilers, tankers, liquified natural gas carriers, undersea vessels, research vessels, and dual-fuel ships; and\n**(G)**\ndevelop a mechanism to incentivize financial investments from foreign sources and remove barriers to foreign direct investment in shipbuilding;\n**(2)**\nthe establishment of a joint workforce-development program between participating shipyards and partner networks engaged in the production of ships for the purpose of training, information sharing, and the exchange of technical advisors;\n**(3)**\nthe establishment of a mechanism to develop and share research and development and leverage innovation to promote sustainability and mutual benefit;\n**(4)**\nan agreement among countries participating in the framework to procure ships and ship components from shipyards identified by the participants as shipyards with specialized capabilities and experience in ship production; and\n**(5)**\nan agreement among countries participating in the framework to prevent leakage of dual-use technologies to companies connected to the military of the People\u2019s Republic of China.\n#### 207. Maritime group of nations\n##### (a) Establishment\nThe Secretary of State shall seek to establish a group, to be known as the Maritime Group of Nations , to coordinate regulatory and commerce policies to facilitate a new maritime multimodalism for commercial shipping.\n##### (b) Participation\n**(1) Inclusion**\nThe Secretary of State should invite to the Maritime Group of Nations appropriate counterparts from the governments of countries that meet each of the following criteria:\n**(A)**\nThe country is of significant importance for the purposes of establishing and advancing the objectives of the Maritime Group of Nations, as determined by the Secretary of State.\n**(B)**\nThe country additionally is among the top 15 countries globally with respect to at least two of the following criteria:\n**(i)**\nShipbuilding, as measured by tonnage as a percentage of global total.\n**(ii)**\nNumber of citizens or nationals who are merchant mariners.\n**(iii)**\nNumber of commercially owned ships greater than 1,000 gross weight tonnage.\n**(2) Exclusion**\nThe Maritime Group of Nations established under subsection (a) may not include a foreign country of concern.\n##### (c) Functions\nThe Maritime Group of Nations established under subsection (a) should consider the following:\n**(1)**\nSupporting the establishment of maritime prosperity zones across a diverse geography, including areas outside traditional coast shipbuilding and ship repair centers, to\u2014\n**(A)**\nincentivize and leverage national private capital and investment by allied countries in the maritime industries and waterfront communities; and\n**(B)**\nstrengthen industrial base capacity and readiness through shipbuilding, workforce development, and expanded manufacturing incentives.\n**(2)**\nSupporting the implementation of a coordinated, reciprocal fee on foreign-built vessels, to\u2014\n**(A)**\nprovide consistent funding to strengthen the merchant marine enterprise; and\n**(B)**\nsupport investments in commercial shipbuilding, fleet expansion, industrial base resilience, and maritime workforce development.\n**(3)**\nDeveloping standardized reciprocal trade agreements that\u2014\n**(A)**\nwould ensure fair competition; and\n**(B)**\nreduce dependency on adversarial supply chains.\n**(4)**\nCoordinating a collective position with respect to regulations and guidelines issued by the International Maritime Organization that protects domestic shipbuilding industries.\n**(5)**\nImplementing and contributing to the exchange visitor program authorized by the amendments made by section 204 .\n#### 208. International Maritime Organization\nThe Secretary of State shall direct the United States Ambassador to the United Nations to use the voice, vote, and influence of the United States mission to the United Nations to urge the International Maritime Organization of the United Nations, and the members of its Council, to\u2014\n**(1)**\nrevise the International Maritime Organization\u2019s Net-Zero Framework, specifically to\u2014\n**(A)**\nexclude any limits on conventional crude or diesel, liquified natural gas, or any other type of marine propulsion technology and instead champion an energy all approach that does not restrict or constrain current or breakthrough fuel types;\n**(B)**\nremove any financial penalties, carbon taxes, or multilateral funds which are used to help nations decarbonize;\n**(C)**\neliminate penalties on liquified natural gas, recognize biofuels as viable marine fuels, and support industry-led advances in alternative fuels and other technologies without creating undue advantage or disadvantage to certain fuels or technologies through regulation;\n**(D)**\nwithdraw or phase out of any regional shipping emissions reduction schemes, including the Emissions Trading System of the European Union;\n**(E)**\nsupport an opt-in model with respect to the rules of such organization; and\n**(F)**\nremove any net-zero 2050 targets the President determines unreasonable;\n**(2)**\nadvance the candidacy of United States citizens into senior-level positions within the\u2014\n**(A)**\nInternational Maritime Organization Assembly;\n**(B)**\nInternational Maritime Organization Council; and\n**(C)**\nmain committees of the International Maritime Organization, including\u2014\n**(i)**\nthe Maritime Safety Committee;\n**(ii)**\nthe Marine Environment Protection Committee;\n**(iii)**\nthe Legal Committee;\n**(iv)**\nthe Technical Cooperation Committee;\n**(v)**\nthe Facilitation Committee; and\n**(vi)**\nany Sub-Committee;\n**(3)**\nadvance the candidacy of a United States citizen to fill the position of Secretary-General of the International Maritime Organization;\n**(4)**\ncombat the anti-competitive practices of the People\u2019s Republic of China by investigating and regulating the deliberate use of policies and practices to give domestic shipbuilding industries a competitive advantage over foreign rivals (also known as industrial targeting );\n**(5)**\nadvocate for the consistent enforcement of existing safety and technical rules to ensure foreign-flagged vessels meet International Maritime Organization standards without requiring unilateral United States regulations; and\n**(6)**\nde-link United States domestic environmental requirements from international certificates to reduce compliance friction for United States shipyards.",
      "versionDate": "2026-04-30",
      "versionType": "Introduced in House"
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
        "name": "International Affairs",
        "updateDate": "2026-05-29T16:38:31Z"
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
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8615ih.xml"
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
      "title": "FLEETS Now Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-18T13:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FLEETS Now Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-18T13:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Facilitating Leadership and Expertise through Exchange and Training in Shipbuilding Now Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-18T13:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To combat China's unfair and non-market-oriented trade practices related to the shipbuilding industry, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-18T13:33:25Z"
    }
  ]
}
```
