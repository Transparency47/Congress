# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5248?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5248
- Title: To ensure the alignment of economic and foreign policies, to position the Department of State to reflect that economic security is national security, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5248
- Origin chamber: House
- Introduced date: 2025-09-10
- Update date: 2025-12-15T21:50:52Z
- Update date including text: 2025-12-15T21:50:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 22.
- Latest action: 2025-09-10: Introduced in House

## Actions

- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Introduced in House
- 2025-09-10 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-18 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 22.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5248",
    "number": "5248",
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
    "title": "To ensure the alignment of economic and foreign policies, to position the Department of State to reflect that economic security is national security, and for other purposes.",
    "type": "HR",
    "updateDate": "2025-12-15T21:50:52Z",
    "updateDateIncludingText": "2025-12-15T21:50:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 28 - 22.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-10",
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
        "item": [
          {
            "date": "2025-09-18T18:17:29Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-17T18:17:19Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-10T14:07:00Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "M001157",
      "district": "10",
      "firstName": "Michael",
      "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
      "isOriginalCosponsor": "False",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "TX"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "GU"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5248ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5248\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 10, 2025 Mrs. Kim introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo ensure the alignment of economic and foreign policies, to position the Department of State to reflect that economic security is national security, and for other purposes.\nV\nEconomic Affairs\n#### 501. Under Secretary for Economic Affairs\n##### (a) Establishment\nThere shall be in the Department an Under Secretary for Economic Affairs who shall be responsible to the Secretary for matters pertaining to economic growth, commercial expansion, energy, technology policy and innovation, scientific research, commercial outer space affairs, critical minerals, water and the environment, protection of natural resources, sanctions policies, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Under Secretary for Economic Affairs shall maintain continuous observation and coordination of all matters pertaining to economic and business affairs in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nPreparing an annual strategic plan for expanding opportunities for United States private sector companies in international markets, coordinating the use of sanctions to achieve national security objectives, promoting international trade and investment, developing international policies around new and emerging technologies, ensuring United States leadership in science and technology, protecting natural resources, and promoting United States energy interests.\n**(2)**\nDeveloping policies for consideration by the Secretary to promote economic growth, facilitate market access, create business enabling environments abroad, expand trade and investment opportunities for United States companies, promote United States energy exports and energy security, conserve and manage economically important ecosystems and resources, expand access to critical minerals abroad, support United States civil and commercial space governance, promote international standards, policies, and best practices for emerging technology that facilitate United States economic growth, and safeguard the preeminence of the United States dollar in international markets.\n**(3)**\nPromoting United States international economic interests to be addressed in the Biannual National Economic Security Strategy Report, coordinated by the Office of the Chief Economist.\n**(4)**\nAttending and participating in meetings of the National Security Council, and National Space Council, when applicable, at the direction of the Secretary, for matters related to economic growth, energy, and commercial expansion, commercial outer space affairs, oceans, science and technology developments, natural resource protection, and fulfill the role of Foreign Affairs Sous Sherpa relating to the activities of the Group of Seven Industrial Nations (G\u20137).\n**(5)**\nProviding guidance to Department personnel in the United States and overseas who conduct or implement policies, programs, and activities related to economic growth, energy, and commercial expansion, science and technology affairs, natural resource conservation, and civil and commercial activities in outer space.\n**(6)**\nCoordinating activities related to promoting economic growth, facilitating market access, creating business enabling environments abroad, expanding trade and investment opportunities, promoting of energy exports, conserving and managing economically important ecosystems and resources, expanding access to critical minerals, maintaining United States leadership in science, technology, and outer space, and safeguarding the preeminence of the United States dollar in international markets.\n**(7)**\nAs directed by the Secretary, representing the Department at interdepartmental meetings including the National Economic Council, Homeland Security Council, Council on Environmental Quality, and in providing policy advice to the Secretary on matters under consideration by these groups.\n##### (c) First appointment\nOn the date of the enactment of this Act, the individual serving before such date of enactment as the Under Secretary for Economic Growth, Energy and the Environment shall be the Under Secretary for Economic Affairs. Any subsequent appointment of an individual to the position of Under Secretary for Economic Affairs shall be subject to the advice and consent of the Senate.\n#### 502. Administration of the International Technology Security and Innovation Fund\nSection 102(c) of the CHIPS Act of 2022 ( Public Law 117\u2013167 ; 136 Stat. 1375) is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby inserting , acting through the Under Secretary of State for Economic Affairs after Secretary of State ; and\n**(B)**\nby adding at the end the following: Within the Department of State, the Fund shall be overseen and administered by the Under Secretary for Economic Affairs. .\n**(2)**\nin paragraph (2)(B), by inserting , acting through the Under Secretary of State for Economic Affairs after Secretary of State .\n#### 503. Authorization of Appropriations for Economic Affairs\n##### (a) Administration of accounts\nThe Under Secretary for Economic Affairs shall direct, oversee, and otherwise exercise responsibility of funds made available for the International Technology Security and Innovation Fund.\n##### (b) Authorization of appropriations\nOf the funds authorized to be appropriated to the Secretary of State under section 141, the Under Secretary for Economic Affairs shall receive the funds necessary to fulfill the Under Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 504. Chief Economist\n##### (a) Establishment\nThere is authorized to be in the Department a Chief Economist who shall be responsible to the Under Secretary for Economic Affairs for matters pertaining to analyzing and forecasting the impact of economic trends on diplomatic functions and national security priorities, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Chief Economist shall provide research and analysis to inform the Department\u2019s strategy for deploying international economic policy to strengthen alliances, deter malign foreign actors, and reduce dependencies on strategic rivals in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nProviding research and analysis to inform the development of the Department\u2019s strategy for deploying foreign policy to ensure supply chain resilience, secure access to raw materials and critical minerals, and maximize international market access.\n**(2)**\nProviding analysis of complex, emerging geoeconomic issues and offer advice to Department leadership on economic diplomacy challenges.\n**(3)**\nConducting research and rigorous, data-driven analysis of high priority issues at the intersection of economics and foreign policy to inform decision-making and diplomatic engagements by senior Department officials.\n**(4)**\nMaintaining analytical products for the Department on international economic issues, including on sanctions evasion and the vulnerabilities of the United States and its partners to economic coercion, as well as the economic opportunities for United States businesses.\n**(5)**\nContributing to the expansion of the economic expertise of the Department through collaboration with the Foreign Service Institute, the academic community, international organizations, and other Federal departments and agencies the Chief Economist determines necessary.\n**(6)**\nServing as a liaison to technical experts in economics and related fields in partner governments, international institutions, and elsewhere in the United States government and academic community.\n**(7)**\nPerforming such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) Report\nNot later than one year after the date of the enactment of this section, and every two years for the subsequent four years, the Chief Economist shall transmit to Congress a report on the international economic strategy of the United States and its analytical basis. In preparing the report, the Chief Economist shall coordinate input and analysis from other bureaus within the Under Secretary for Economic Affairs.\n#### 505. Office of the Chief Economist\n##### (a) Establishment\nThe Secretary shall establish an Office of the Chief Economist, which shall perform such functions related to the provision of expert economic advice and analysis, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Chief economist\nThe Chief Economist shall be the head of the Office of the Chief Economist.\n#### 506. Authorization of Appropriations for the Chief Economist\nOf the funds authorized to be appropriated to the Under Secretary for Economic Affairs under section 503, the Chief Economist shall receive the funds necessary to fulfill Office functions and the Chief Economist\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 507. Assistant Secretary for Commercial Diplomacy\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Commercial Diplomacy who shall be responsible to the Under Secretary for Economic Affairs for matters pertaining to the trade and investment promotion and policy, international finance and development, transportation affairs, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Commercial Diplomacy shall be responsible for leading Department policies and programs, and coordinating with other United States agencies as appropriate, for all matters pertaining to the following:\n**(1)**\nTrade and investment promotion, such as\u2014\n**(A)**\nassisting and advocating for United States businesses and commercial interests overseas;\n**(B)**\nidentifying foreign market opportunities for United States businesses and helping United States firms overcome challenges in foreign business climates;\n**(C)**\nhelping United States companies compete for and win contracts in foreign markets;\n**(D)**\nattracting foreign investment into the United States by identifying high potential businesses in foreign countries;\n**(E)**\nensuring United States private sector concerns are integrated into United States foreign policy and economic policy; and\n**(F)**\npromoting international commercial projects that advance the national security interests of the United States, regardless of domestic content thresholds.\n**(2)**\nInternational trade policy, including negotiating and implementing trade agreements, resolving trade disputes, bolstering supply chain resilience, and protecting intellectual property rights.\n**(3)**\nInternational investment policy, including monitoring international investment climates, negotiating and implementing investment agreements, representing the Department in the Committee on Foreign Investment in the United States, and assisting United States companies involved in investment disputes with foreign governments.\n**(4)**\nDevelopment finance, including the mobilization of private, bilateral, and multilateral development finance for developing countries, particularly investments focused on infrastructure projects.\n**(5)**\nThe negotiation and extension of debt relief and sovereign loan guarantees for United States allies and partners.\n**(6)**\nThe promotion of sound, transparent, and stable economic policies overseas.\n**(7)**\nPerform such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) First appointment\nOn the date of the enactment of this Act, the individual serving before such date of enactment as the Assistant Secretary for Economic and Business Affairs shall be the Assistant Secretary for Commercial Diplomacy. Any subsequent appointment of an individual to the position of Assistant Secretary for Commercial Diplomacy shall be subject to the advice and consent of the Senate.\n#### 508. Bureau of Commercial Diplomacy\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Commercial Diplomacy which shall perform such functions related to trade and investment promotion and policy, international finance and development, and transportation affairs, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Commercial Diplomacy shall be the head of the Bureau of Commercial Diplomacy.\n#### 510. Enhancing Subnational Diplomacy\n##### (a) Establishment\nThere shall be established in the Department an Office of Subnational Diplomacy. The Office shall enable the Department\u2019s work with subnational governments (state, county, city, and municipal) within the United States to improve the ability of subnational governments to attract foreign investment, counter foreign malign influence within the United States, and contribute to the foreign policy priorities of the United States.\n##### (b) Coordinator\nThe head of the Office shall be the Coordinator for Subnational Diplomacy. The head of the office shall report through the Assistant Secretary for Commercial Diplomacy to the Under Secretary for Economic Affairs.\n##### (c) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Coordinator for Subnational Diplomacy shall maintain continuous observation and coordination of all matters pertaining to subnational diplomacy and Department engagements with subnational governments in the conduct of foreign policy, including the following:\n**(1)**\nAdvising the Under Secretary for Economic Affairs on subnational engagements within the United States and serve as the principal official on such matters within the Department.\n**(2)**\nCoordinating the Department\u2019s support for local and municipal governments\u2019 engagements with foreign governments.\n**(3)**\nAdvising subnational government officials on the potential risks of engagements with countries of concern and share best practices to build resilience against foreign political interference and malign influence.\n**(4)**\nAssisting subnational governments in the following areas:\n**(A)**\nAttracting or bidding to host major international events.\n**(B)**\nTracking foreign direct investment at the county and municipal levels to highlight trends and opportunities.\n**(C)**\nAttracting foreign direct investment and other forms of economic cooperation.\n**(D)**\nBuilding the capacity and knowledge of subnational government staff who have responsibility for engaging with foreign countries.\n**(E)**\nAdvancing sports diplomacy with foreign countries and entities.\n**(F)**\nImplementing programs to cooperate with foreign governments and entities on policy priorities or managing shared resources.\n**(G)**\nUnderstanding the local implications of foreign policy developments or policy changes.\n**(5)**\nSupporting the economic interests of the United States through subnational engagements, in consultation and coordination with other relevant agencies.\n**(6)**\nAdvising and informing local officials as they negotiate agreements and memoranda of understanding with foreign governments related to subnational engagements and priorities.\n**(7)**\nCoordinating subnational engagements with associations of subnational elected leaders, including the United States Conference of Mayors, National Governors Association, National League of Cities and similar associations.\n**(8)**\nPerforming other such duties as the Assistant Secretary for Commercial Diplomacy and the Under Secretary for Economic Affairs may from time to time designate.\n#### 511. Authorization of Appropriations for Commercial Diplomacy\nOf the funds authorized to be appropriated to the Under Secretary for Economic Affairs under section 503, the Assistant Secretary for Commercial Diplomacy shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 512. Assistant Secretary for Water, Environment, and Space Affairs\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Water, Environment, and Space Affairs who shall be responsible to the Under Secretary for Economic Affairs for matters pertaining to space, oceans, polar affairs, environmental quality, freshwater, fisheries, wildlife and wildlife trafficking, conservation, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Water, Environment, and Space Affairs shall maintain continuous observation and coordination of all matters pertaining to oceans, fisheries, natural resource conservation, and outer space in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nDeveloping United States policy on global environmental security issues with respect to oceans, fisheries, Antarctic region, waste and global pollution, and natural resource management and conservation, including water.\n**(2)**\nRepresenting the Department in bilateral and multilateral negotiations involving the law of the sea, including freedom of navigation and overflight and other lawful uses of the ocean; maritime security; United States maritime zones, including the United States extended continental shelf; marine science; sustainable management and protection of marine habitats and resources; marine pollution; and maritime claims and boundaries.\n**(3)**\nLeading United States engagement on Antarctica and in international oceans agreements and conventions with foreign governments and international organizations to promote solutions that advance United States national security, economic, and environmental interests.\n**(4)**\nCoordinating the development of policies and programs to conserve and manage economically important ecosystems, including, forests, wetlands, drylands, and coral reefs.\n**(5)**\nDeveloping policies and programs to address international threats to natural resources including but not limited to illicit trade; illegal, unreported and unregulated fishing; wildlife trafficking; and illegal logging and associated trade.\n**(6)**\nDeveloping and implementing United States foreign policy related to air, water and soil pollution and risks to human health and the environment caused by the transboundary movement of hazardous chemicals and waste and other forms of pollution to promote environmental security with trade partners and in multilateral institutions.\n**(7)**\nRepresenting the Department in bilateral and multilateral engagements including organizations, institutions, and negotiation of international agreements on related issues.\n**(8)**\nDeveloping policies and programs, in coordination with the National Aeronautics and Space Administration, the Department of Commerce, and other relevant Federal departments and agencies, as appropriate, to support partnerships between the United States and international and private industry partners in the development of infrastructure and policies that expand economic growth in outer space, including\u2014\n**(A)**\ncountering malign efforts by foreign adversaries and other actors that threaten United States interests in civil and commercial space;\n**(B)**\nexpanding access to foreign markets for United States commercial industry, including by encouraging reforms that reduce barriers to trade and cooperation with United States civil and commercial space actors; and\n**(C)**\nproviding assistance to foreign governments and organizations, including national, regional, and international institutions, on such terms and conditions as the Secretary may determine.\n**(9)**\nLeading bilateral and multilateral engagements related to civil and commercial space activities, resilient space services, burden sharing, and other matters related to international space law and diplomacy and other United States international obligations and commitments.\n**(10)**\nIn accordance with the National Space Policy, leading United States Government engagement with international Global Navigation Satellite Systems providers to ensure compatibility and encourage interoperability of civil global navigation satellite services based on United States-based global positioning systems, including through the International Committee on Global Navigation Satellite Systems.\n**(11)**\nLeading Department efforts to implement international arrangements and promote cooperation on Earth observation satellite systems.\n**(12)**\nLeading Department engagement in multilateral and bilateral forums on international space policy, space law, and commercial and civil treaties or agreements.\n**(13)**\nLeading Department efforts on transparency in space by maintaining the official United States space object registry and promoting best practices for safe operations in space, preservation of the space environment, space traffic coordination, and space situational awareness.\n**(14)**\nLeading Department efforts to align foreign space law, regulatory, and policy frameworks with United States-endorsed models, approaches, and best practices.\n**(15)**\nPerforming such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) First appointment\nOn the date of the enactment of this Act, the individual serving as the Assistant Secretary for Oceans and International Environmental and Scientific Affairs on the day before such date of enactment shall be the Assistant Secretary for Water, Environment, and Space Affairs. Any subsequent appointment of an individual to the position of Assistant Secretary for Water, Environment, and Space Affairs shall be subject to the advice and consent of the Senate.\n#### 513. Bureau of Water, Environment, and Space Affairs\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Water, Environment, and Space Affairs, which shall perform such functions related to space, oceans, environmental quality, fisheries, wildlife, and wildlife trafficking, and conservation affairs, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Water, Environment, and Space Affairs shall be the head of the Bureau of Water, Environment, and Space Affairs.\n#### 514. Authorization of Appropriations for Water, Environment, and Space Affairs\nOf the funds authorized to be appropriated to the Under Secretary for Economic Affairs under section 503, the Assistant Secretary for Water, Environment, and Space Affairs shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 515. Assistant Secretary for Energy Security and Diplomacy\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Energy Security and Diplomacy who shall be responsible to the Under Secretary for Economic Affairs for all matters pertaining to the formulation and implementation of international energy, energy technology, critical minerals, and relevant supply chain policies in the conduct of foreign policy by the Department, including, as appropriate, to protect United States energy security interests, lead the coordination of energy programs carried out by United States Government agencies abroad, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Energy Security and Diplomacy shall maintain continuous observation and coordination of all matters pertaining to the development of policies to secure access to international energy markets and diversify critical mineral supply chains in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nRepresenting the Secretary in interagency efforts to develop the international energy policy of the United States.\n**(2)**\nLeading the analysis, formulation, and implementation of international policies aimed at protecting and advancing United States energy interests.\n**(3)**\nEffectively managing United States bilateral and multilateral relations and, as directed by the Secretary, representing the Secretary in relevant international fora and organizations, including the International Energy Agency, to bolster global energy security and advance the interests of the United States.\n**(4)**\nEnsuring that analyses of the national security and economic security implications of global energy developments are reflected in the decision-making processes within the Department.\n**(5)**\nIncorporating energy and critical mineral security priorities into the activities of the Department.\n**(6)**\nCoordinating energy activities of the Department with relevant Federal departments and agencies, including the Departments of Energy, Commerce, Defense, and Interior, and the Development Finance Corporation to promote United States energy security and energy development to support United States national security readiness.\n**(7)**\nCoordinating with the Bureau of Sanctions Policy on economic sanctions pertaining to the international energy sector.\n**(8)**\nCoordinating energy security and other relevant functions within the Department currently undertaken by\u2014\n**(A)**\nthe Bureau of Commercial Diplomacy;\n**(B)**\nthe Bureau of Water, Environment, and Space Affairs;\n**(C)**\nthe Bureau of Arms Control and Nonproliferation; and\n**(D)**\nother bureaus and offices within the Department.\n**(9)**\nWorking internationally to\u2014\n**(A)**\nsupport the development of energy technologies, natural resources, critical minerals, and supply chains for the benefit of the United States and United States allies and trading partners for their energy security and economic development needs;\n**(B)**\npromote secure and diversified energy and critical minerals supply chains, and a well-functioning global market for energy resources, energy technologies, critical minerals;\n**(C)**\nresolve international disputes regarding the exploration, development, production, or distribution of energy and critical minerals resources where the United States strategic interests are present;\n**(D)**\nsupport the economic and commercial interests of United States persons operating in the energy markets of foreign countries; and\n**(E)**\nsupport and coordinate international efforts to alleviate energy poverty, enhance energy access and energy efficiency to promote United States strategic interests and offer alternatives to adversary initiatives for United States allies and partners.\n**(10)**\nConducting public diplomacy with regard to United States international energy policy to strengthen transparency and governance.\n**(11)**\nPerforming such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) Annual report\nNot later than one year after the date of the enactment of this section, and annually thereafter for three years, the Assistant Secretary for Energy Security and Diplomacy shall submit to Congress a report on the United States international energy strategy.\n#### 516. Bureau of Energy Security and Diplomacy\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Energy Security and Diplomacy, which shall perform such functions related to the formulation and implementation of international energy, energy technology, critical minerals, and relevant supply chain policies, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Energy Security and Diplomacy shall be the head of the Bureau of Energy Security and Diplomacy.\n#### 517. Authorization of Appropriations for Energy Security and Diplomacy\nOf the funds authorized to be appropriated to the Under Secretary for Economic Affairs under section 503, the Assistant Secretary for Energy Security and Diplomacy shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 518. Assistant Secretary for Sanctions Policy\n##### (a) Establishment\nThere is authorized to be in the Department an Assistant Secretary for Sanctions Policy, who shall be responsible to the Under Secretary for Economic Affairs for matters pertaining to the development of policies governing the imposition of sanctions, in consultation with the Under Secretary for International Security Affairs and the Assistant Secretary for Arms Control and Nonproliferation as appropriate, and such other related duties as the Secretary may from time to time designate.\n##### (b) Responsibilities\nIn addition to the responsibilities described under subsection (a), the Assistant Secretary for Sanctions Policy shall maintain continuous observation and coordination of all matters pertaining to the development and implementation of sanctions policies as part of United States diplomatic strategies in the conduct of foreign policy, including, as appropriate, the following:\n**(1)**\nDeveloping the foreign policy strategy of United States sanctions programs, including consideration of the use of sanctions in combination with other United States foreign policy tools and the political and economic implications of sanction policies.\n**(2)**\nCoordinating the effective implementation and enforcement of sanctions, including all activities, policies, and programs pertaining to sanctions within the Department.\n**(3)**\nCoordinating sanctions policy with foreign partners and allies to ensure the maximum effectiveness of sanctions imposed by the United States and such allies and partners.\n**(4)**\nConsulting regularly with a broad range of stakeholders on the implications of United States sanctions policy for United States economic interests.\n**(5)**\nContributing to the reports to Congress produced by the Chief Economist.\n**(6)**\nLeading the Department\u2019s efforts to identify and designate individuals for visa sanctions related to human rights violations.\n**(7)**\nDeveloping policies and programs, in coordination with the Department of the Treasury and other Federal departments and agencies as necessary and with foreign partners, to combat money laundering, terrorist financing, cybercrimes, and other illicit financial activities.\n**(8)**\nRepresenting the Department in all interagency groups or organizations within the executive branch that plan, assess, analyze, or review United States sanctions policies, such as interagency groups organized under the auspices of the Department of the Treasury, the Department of Commerce, and the Department of Homeland Security.\n**(9)**\nPerforming such other duties as the Under Secretary for Economic Affairs may from time to time designate.\n##### (c) Redelegation of authority\nThe Secretary may delegate, or authorize successive redelegation of, authority to the Assistant Secretary for Sanctions Policy to act and to render decisions, with respect to all sanctions policies administered by the Department. Within the limitations of such delegations, redelegations, or assignments, all official acts and decisions by the Assistant Secretary for Sanctions Policy shall have the same force and effect as though performed or rendered by the Secretary.\n##### (d) First appointment\nOn the date of the enactment of this Act, the individual serving before such date of enactment as the Coordinator for Sanctions shall be the Assistant Secretary for Sanctions Policy. Any subsequent appointment of an individual to the position of Assistant Secretary for Sanctions Policy shall be subject to the advice and consent of the Senate.\n#### 519. Bureau of Sanctions Policy\n##### (a) Establishment\nThe Secretary shall establish a Bureau of Sanctions Policy, which shall perform such functions related to the development of policies governing the imposition of sanctions and sanctions strategies, as the Under Secretary for Economic Affairs may prescribe.\n##### (b) Assistant secretary\nThe Assistant Secretary for Sanctions Policy shall be the head of the Bureau of Sanctions Policy.\n#### 520. Authorization of Appropriations for Sanctions Policy\nOf the funds authorized to be appropriated to the Under Secretary for Economic Affairs under section 503, the Assistant Secretary for Sanctions Policy shall receive the funds necessary to fulfill Bureau functions and the Assistant Secretary\u2019s responsibilities for fiscal years 2026 and 2027.\n#### 521. References\nAny reference in any statute, reorganization plan, Executive order, regulation, agreement, determination, or other official document or proceeding to\u2014\n**(1)**\nthe Under Secretary for Economic Growth, Energy and the Environment shall be deemed to refer to the Under Secretary for Economic Affairs;\n**(2)**\nthe Assistant Secretary for Economic and Business Affairs shall be deemed to refer to the Assistant Secretary for Commercial Diplomacy;\n**(3)**\nthe Bureau for Economic and Business Affairs shall be deemed to refer to the Bureau for Commercial Diplomacy;\n**(4)**\nthe Assistant Secretary for Oceans and International Environmental and Scientific Affairs shall be deemed to refer to the Assistant Secretary for Water, Environment, and Space Affairs;\n**(5)**\nthe Bureau for Oceans and International Environmental and Scientific Affairs shall be deemed to refer to the Bureau for Water, Environment, and Space Affairs;\n**(6)**\nthe Sanctions Coordinator shall be deemed to refer to the Assistant Secretary for Sanctions Policy; and\n**(7)**\nthe Office of the Sanctions Coordinator shall be deemed to refer to the Bureau of Sanctions Policy.\n#### 522. Classification in united states code\n##### (a)\nThe Office of Law Revision Counsel is directed to\u2014\n**(1)**\nutilize sections 129\u2013159 of title 22, United States Code, to classify the sections of this title; and\n**(2)**\nmaintain the legislative history, under editorial notes, of repealed law which previously occupied the corresponding sections of United States Code.",
      "versionDate": "2025-09-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-12-15T21:50:22Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-12-15T21:50:03Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-12-15T21:50:29Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-12-15T21:49:24Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-12-15T21:49:48Z"
          },
          {
            "name": "Economic development",
            "updateDate": "2025-12-15T21:49:57Z"
          },
          {
            "name": "Energy efficiency and conservation",
            "updateDate": "2025-12-15T21:50:39Z"
          },
          {
            "name": "Energy research",
            "updateDate": "2025-12-15T21:50:46Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-12-15T21:49:31Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-12-15T21:49:42Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-12-15T21:50:52Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-12-15T21:50:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-11T21:39:14Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5248ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To ensure the alignment of economic and foreign policies, to position the Department of State to reflect that economic security is national security, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-11T10:18:22Z"
    },
    {
      "title": "To ensure the alignment of economic and foreign policies, to position the Department of State to reflect that economic security is national security, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-11T08:06:26Z"
    }
  ]
}
```
