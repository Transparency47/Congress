# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2675?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2675
- Title: Preventing HEAT Illness and Deaths Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2675
- Origin chamber: Senate
- Introduced date: 2025-08-01
- Update date: 2025-12-05T21:44:48Z
- Update date including text: 2025-12-05T21:44:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-08-01: Introduced in Senate
- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-08-01: Introduced in Senate

## Actions

- 2025-08-01 - IntroReferral: Introduced in Senate
- 2025-08-01 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2675",
    "number": "2675",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "M000133",
        "district": "",
        "firstName": "Edward",
        "fullName": "Sen. Markey, Edward J. [D-MA]",
        "lastName": "Markey",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "Preventing HEAT Illness and Deaths Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:44:48Z",
    "updateDateIncludingText": "2025-12-05T21:44:48Z"
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
        "item": {
          "date": "2025-08-01T23:24:27Z",
          "name": "Referred To"
        }
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
      "bioguideId": "P000145",
      "firstName": "Alex",
      "fullName": "Sen. Padilla, Alex [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Padilla",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CA"
    },
    {
      "bioguideId": "G000574",
      "firstName": "Ruben",
      "fullName": "Sen. Gallego, Ruben [D-AZ]",
      "isOriginalCosponsor": "True",
      "lastName": "Gallego",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "AZ"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NM"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CT"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OR"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "OR"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "NJ"
    },
    {
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-08-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2675is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2675\nIN THE SENATE OF THE UNITED STATES\nAugust 1, 2025 Mr. Markey (for himself, Mr. Padilla , Mr. Gallego , Mr. Heinrich , Mr. Blumenthal , Mr. Merkley , Mr. Wyden , Ms. Duckworth , Mr. Booker , and Mr. Sanders ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo reduce the health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, requiring a study, and establishing financial assistance programs to address heat effects, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Preventing Health Emergencies And Temperature-related Illness and Deaths Act of 2025 or the Preventing HEAT Illness and Deaths Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Community with environmental justice concerns**\nThe term community with environmental justice concerns means a community with significant representation of communities of color, low-income communities, or Tribal and indigenous communities, that experiences, or is at risk of experiencing, higher or more adverse human health or environmental effects as compared to other communities.\n**(2) Extreme heat**\nThe term extreme heat means heat that substantially exceeds local climatological norms in terms of any combination of the following:\n**(A)**\nDuration.\n**(B)**\nIntensity.\n**(C)**\nSeason length.\n**(D)**\nFrequency.\n**(3) Heat**\nThe term heat means any combination of the atmospheric parameters associated with modulating human thermoregulation, such as air temperature, humidity, solar exposure, and wind speed.\n**(4) Heat event**\nThe term heat event means an occurrence of extreme heat of 2 days or more that may have heat-health implications.\n**(5) Heat-health**\nThe term heat-health means health effects to humans from heat, during or outside of heat events, including from vulnerability and exposure, or the risk of such effects.\n**(6) Indian tribe**\nThe term Indian Tribe has the meaning given that term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(7) Native hawaiian organization**\nThe term Native Hawaiian organization has the meaning given that term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ).\n**(8) Planning**\nThe term planning means activities performed across timescales (including days, weeks, months, years, and decades) with scenario-based, probabilistic or deterministic information to identify and take actions to proactively mitigate heat-health risks from increased frequency, duration, and intensity of heat waves and increased ambient temperature.\n**(9) Preparedness**\nThe term preparedness means activities performed across timescales (including days, weeks, months, years, and decades) with decision support tools to manage risk in advance of a heat event and increased ambient temperature.\n**(10) Response**\nThe term response means activities performed during and after a heat event to address heat-health and other impacts and assess improvements to planning and preparedness activities.\n**(11) Urban heat island**\nThe term urban heat island means the phenomenon observed in urbanized areas in which heat is more extreme than in the surrounding exurban areas and heat is heterogeneously distributed within urbanized areas, due to factors including\u2014\n**(A)**\nlow albedo and impervious surfaces;\n**(B)**\nlow vegetation coverage; and\n**(C)**\nwaste heat produced in urban areas.\n#### 3. Findings\nCongress makes the following findings:\n**(1)**\nExtreme heat events have been the leading cause of weather-related death in the United States over the last 30 years, according to the Centers for Disease Control and Prevention and the National Weather Service.\n**(2)**\nThe fourth National Climate Assessment, mandated by the Global Change Research Act of 1990 ( 15 U.S.C. 2921 et seq. ), finds that during the next few decades, annual average temperature over the contiguous United States is projected to increase by a further 2.2\u00b0F relative to current temperatures, regardless of future scenarios. The National Climate Assessment projects that the frequency and intensity of extreme heat events will increase in the future as global temperature increases.\n**(3)**\nExposure to extreme heat can cause acute heat-related illnesses, such as heat stroke, which already result in more than 65,000 emergency room visits each year and exacerbate respiratory and cardiovascular illnesses.\n**(4)**\nHeat poses the greatest health risks for adults older than 65 years of age, pregnant people, young children, low-income communities, urban communities, communities with low air conditioning prevalence, socially isolated individuals, people with mental or physical disabilities, people with underlying medical conditions, agricultural or other outdoor workers, workers without sufficient access to cooling, athletes, incarcerated individuals, people experiencing homelessness, and military personnel.\n**(5)**\nExtreme heat is significantly associated with serious adverse pregnancy outcomes across the United States. Those adverse pregnancy outcomes disproportionately impact Black mothers.\n**(6)**\nHeat exposure is an issue of environmental justice, as people living in low-income communities, communities of color, and Tribal nations face a number of interacting factors that render them more vulnerable to extreme heat.\n**(7)**\nThe impacts of heat on human health are more severe in urban areas where land surface properties create an urban heat island, particularly in neighborhoods with limited availability of or access to green spaces, shade, and tree cover, due to higher density of building structures and more vehicular traffic.\n**(8)**\nLimited availability of tree cover and higher temperatures are correlated with low-income neighborhoods in urban areas. In Richmond, Virginia, Baltimore, Maryland, and Washington, DC, researchers found that risk of exposure to extreme heat is disproportionately distributed to communities of color in patterns associated with segregation and redlining.\n**(9)**\nResearchers have found that few communities in the United States have sufficient climate and health information, guidance, and resources for heat planning, preparedness, and response.\n**(10)**\nThe risks associated with extreme heat have complex interactions and impacts, and the management of those risks requires a transdisciplinary approach.\n**(11)**\nRegions, communities, and populations that face the greatest health consequences of extreme heat often may experience the lowest heat risk perceptions, have limited incentives, or have access to the fewest resources for responding to extreme heat, and as such, may be less likely to take precautions.\n**(12)**\nResearch on the impacts of extreme heat on human health and the effectiveness of solutions under varying climate, social, and other contexts is stymied by a lack of access to reliable, timely health observations and surveillance due to proprietary data rights, expense, privacy and security concerns, inconsistent reporting of health outcomes and contributory factors, poor data integration and interoperability, few incentives and little systematic coordination to address those problems, and a lack of adequate climate observation, modeling, and assessment in rural, urban, indoor, and occupational settings.\n**(13)**\nIntegrated climate and health research and information, when developed in a collaborative, transdisciplinary manner, can inform long- and medium-range scenario-based planning and decision making to protect communities with environmental justice concerns and other populations from extreme heat, reduce exposure to extreme heat, and address factors that increase vulnerability.\n**(14)**\nThe Federal Government has developed, and should maintain, preserve, or reinstate, various science-informed heat-health tools for communities with environmental justice concerns, workers, employers, and the public to understand heat risk and resources, including the Centers for Disease Control and Prevention Heat and Health Tracker, the Office of Climate Change and Health Equity Climate and Health Outlook, the National Weather Service HeatRisk portal, the National Emergency Medical Services Information System Heat-related Emergency Management Service Activation Surveillance Dashboard, and the Low Income Home Energy Assistance Program and Extreme Heat website.\n**(15)**\nIncreased heat can have cascading and compounding impacts across and among sectors including energy, food supply and quality, transportation, housing, infrastructure, hospital and healthcare delivery, and education, all of which affect health and well-being.\n**(16)**\nHeat action plans and early warning systems can reduce heat-related morbidity and mortality by clearly identifying roles and responsibilities as well as evidence-based actions and thresholds to enhance preparedness, and by promoting behavior changes and actions taken by local governments, communities, and individuals through awareness and increased risk perception among those most vulnerable to the health impacts of heat.\n#### 4. National Integrated Heat Health Information System Interagency Committee\n##### (a) Establishment of committee\nThere is established within the National Oceanic and Atmospheric Administration an interagency committee, to be known as the National Integrated Heat Health Information System Interagency Committee (in this section referred to as the Committee ).\n##### (b) Purpose\nThe Committee shall coordinate, plan, and direct agencies represented on the Committee to execute, as appropriate, activities across such agencies to ensure a united Federal approach to reducing health risks from heat across timescales (including days, weeks, months, years, and decades).\n##### (c) Membership\n**(1) In general**\nIn order to carry out and achieve the purpose described in subsection (b), the Committee shall include the following:\n**(A)**\nThe Director of the National Integrated Heat Health Information System.\n**(B)**\nNot fewer than 1 representative from each of the following:\n**(i)**\nFrom the Department of Commerce, the following:\n**(I)**\nFrom the National Oceanic and Atmospheric Administration, the following:\n**(aa)**\nThe National Weather Service.\n**(bb)**\nThe Office of Oceanic and Atmospheric Research.\n**(cc)**\nThe National Environmental Satellite, Data, and Information Service.\n**(II)**\nThe National Institute of Standards and Technology.\n**(III)**\nThe Bureau of the Census.\n**(ii)**\nFrom the Department of Health and Human Services, the following:\n**(I)**\nThe Centers for Disease Control and Prevention, including the National Institute for Occupational Safety and Health.\n**(II)**\nThe Office of the Assistant Secretary of Health and Human Services for Preparedness and Response.\n**(III)**\nThe Substance Abuse and Mental Health Services Administration.\n**(IV)**\nThe National Institutes of Health.\n**(V)**\nThe Indian Health Service.\n**(VI)**\nThe Administration for Children and Families.\n**(VII)**\nThe Administration for Community Living.\n**(iii)**\nFrom the Department of the Interior, the following:\n**(I)**\nThe Bureau of Indian Affairs.\n**(II)**\nThe Bureau of Land Management.\n**(III)**\nThe National Park Service.\n**(IV)**\nThe Office of Hawaiian Relations.\n**(iv)**\nFrom the Environmental Protection Agency, the following:\n**(I)**\nThe Office of Environmental Justice and External Civil Rights.\n**(II)**\nThe Office of Air and Radiation, if the Administrator of the Environmental Protection Agency determines appropriate.\n**(III)**\nThe Office of Research and Development, if the Administrator determines appropriate.\n**(IV)**\nThe Office of International and Tribal Affairs.\n**(v)**\nThe Department of Homeland Security, including the Federal Emergency Management Agency.\n**(vi)**\nThe Department of Defense.\n**(vii)**\nThe Department of Agriculture, including the United States Forest Service.\n**(viii)**\nThe Department of Housing and Urban Development.\n**(ix)**\nThe Department of Transportation.\n**(x)**\nThe Department of Energy.\n**(xi)**\nThe Department of Labor, including the Occupational Safety and Health Administration.\n**(xii)**\nThe Department of Veterans Affairs.\n**(xiii)**\nThe Department of Education.\n**(xiv)**\nThe Department of State.\n**(xv)**\nThe Small Business Administration.\n**(xvi)**\nSuch other Federal agencies as the Under Secretary of Commerce for Oceans and Atmosphere considers appropriate.\n**(2) Selection of representatives**\nThe head of an agency specified in paragraph (1)(B) shall, in appointing representatives of the agency to the Committee, select representatives who have expertise in areas relevant to the responsibilities of the Committee, such as weather and climate prediction, health impacts, environmental justice, urban planning, behavioral science, public health hazard preparedness and response, or mental health services.\n**(3) Co-chairs**\n**(A) In general**\nThe members of the Committee shall select 3 individuals from among such members to serve as co-chairs of the Committee, subject to the approval of the Under Secretary of Commerce for Oceans and Atmosphere.\n**(B) Selection**\n**(i) Initial selection**\nOf the co-chairs first selected, one co-chair shall be from each of the National Oceanic and Atmospheric Administration, the Department of Health and Human Services, and the Federal Emergency Management Agency.\n**(ii) Subsequent selection**\nSubsequent co-chairs shall be selected from among the members of the Committee, except the National Oceanic and Atmospheric Administration shall have the opportunity to maintain a co-chair position.\n**(C) Terms**\nEach co-chair shall serve for a term of not more than 5 years, except the National Oceanic and Atmospheric Administration shall have the opportunity to maintain a co-chair position.\n**(D) Representation of National Oceanic and Atmospheric Administration**\nIf determined appropriate by the Under Secretary of Commerce for Oceans and Atmosphere, 1 co-chair of the Committee shall be a representative from the National Oceanic and Atmospheric Administration.\n**(E) Responsibilities of co-chairs**\nThe co-chairs of the Committee shall work with the Director of the National Integrated Heat Health Information System\u2014\n**(i)**\nto determine the agenda of the Committee, in consultation with other members of the Committee;\n**(ii)**\nto direct the work of the Committee; and\n**(iii)**\nto convene meetings of the Committee not less frequently than once each fiscal quarter.\n##### (d) Responsibilities of Committee\nThe Committee shall promote an integrated, Federal Government-wide approach to reducing health risks and impacts of heat, including by\u2014\n**(1)**\ndeveloping the strategic plan and implementation plans required by subsection (e);\n**(2)**\ncoordinating across Federal agencies on heat-health communication, engagement, research, service delivery, financial assistance, contracting, and workforce development; and\n**(3)**\nbuilding capacity and partnerships with Federal and non-Federal entities.\n##### (e) Strategic plan\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Committee shall submit to Congress and make available on a public website a 5-year strategic plan that outlines the goals and projects of the Committee, including how the Committee will improve coordination and integration of interagency Federal capacity and capabilities to address health risks of heat, including\u2014\n**(A)**\na strategy for improving and coordinating existing Federal data collection and data management to include sharing of data and statistics on heat-related illnesses and mortalities and other impacts, such as agricultural losses, energy and transportation system disruptions, and labor productivity, to inform heat-related activities;\n**(B)**\na strategy for improving and coordinating Federal activities to understand user gaps and needs, conduct research, foster innovative solutions, and provide actionable information and services for extreme heat prevention and response; and\n**(C)**\nmechanisms for financing heat planning, and preparedness, and response within such agencies as the Committee considers appropriate.\n**(2) Implementation**\nThe head of an agency represented on the Committee may implement the portions of the strategic plan required by paragraph (1) that are relevant to that agency.\n**(3) Updates**\nNot later than 5 years after the submission of the strategic plan required by paragraph (1), and every 5 years thereafter, the Committee shall brief Congress on an update of the plan, which shall include progress made toward goals outlined in the plan and new priorities that emerge.\n##### (f) Administrative support\nThe Under Secretary of Commerce for Oceans and Atmosphere shall provide technical and administrative support to the Committee, using amounts authorized to be appropriated to the National Oceanic and Atmospheric Administration.\n##### (g) Consultation\nIn carrying out the responsibilities of the Committee, the Committee shall consult with relevant\u2014\n**(1)**\nregional, State, and local governments, and Indian Tribes;\n**(2)**\ninternational organizations and partners;\n**(3)**\nresearch institutions;\n**(4)**\nnongovernmental organizations and associations;\n**(5)**\nmedical experts with expertise in emergency response; and\n**(6)**\nenvironmental health, economic or business development, or community engagement organizations.\n#### 5. National Integrated Heat Health Information System\n##### (a) Establishment\nThe Under Secretary of Commerce for Oceans and Atmosphere shall establish within the National Oceanic and Atmospheric Administration a system, to be known as the National Integrated Heat Health Information System (NIHHIS) (in this section referred to as the System ).\n##### (b) Purpose\nThe purpose of the System is to reduce heat-related impacts by\u2014\n**(1)**\nimproving the delivery of data, information, forecasts, warnings, predictions, and projections related to temperature, extreme heat, and related impacts, especially for disproportionately affected communities;\n**(2)**\nthrough the Office of Oceanic and Atmospheric Research, developing, maintaining, and preserving science-based solutions and tools to build capacity and improve impact-based decision support services for heat resilience, particularly human life; and\n**(3)**\nentering into grant agreements with centers of excellence that provide technical and other assistance to support heat resilience.\n##### (c) Director\nThe System shall be headed by a Director.\n##### (d) Responsibilities\nIn carrying out the purpose described in subsection (b), the Director of the System shall\u2014\n**(1)**\ndevelop and sustain robust relationships with Federal and non-Federal partners and decisionmakers, representing different geographic (including urban and rural) regions and including\u2014\n**(A)**\nmembers of the emergency management field and emergency response providers, including fire service, law enforcement, hazardous materials response, emergency medical services, and emergency management personnel, or organizations representing such individuals;\n**(B)**\nhealth scientists, emergency and inpatient medical providers, public health professionals, and healthcare providers at Federally Qualified Health Centers;\n**(C)**\nexperts from Federal, State, and local governments and Indian Tribes, and the private sector, representing standards-setting and accrediting organizations, including representatives from the voluntary consensus codes and standards development community, particularly those with expertise in the emergency preparedness and response field;\n**(D)**\nstate and local government and Indian Tribes officials with expertise in preparedness, protection, response, recovery, and mitigation, including Adjutants General;\n**(E)**\nelected State and local government and Indian Tribe executives;\n**(F)**\nrepresentatives of individuals from communities who have a high proportion of extreme heat survivors and communities with environmental justice concerns;\n**(G)**\nrepresentatives of individuals with disabilities and other populations with special needs;\n**(H)**\nrepresentatives of individuals from the private, nonprofit, and public energy sector that help to protect consumers from energy shutoffs and assist with energy rebate funding; and\n**(I)**\nsuch other individuals as the Under Secretary of Commerce considers appropriate\u2014\n**(i)**\nto identify and respond to the demand for actionable weather- and climate-related information that reduces health risks on multiple timescales;\n**(ii)**\nto conduct research and scientific innovation; and\n**(iii)**\nto develop and deliver timely and accessible decision support services, solutions, tools, and information to inform planning, preparedness, and risk-reducing actions across timescales;\n**(2)**\ncoordinate and collaborate with the international community and global partners to conduct research and learn from, leverage, and contribute to global knowledge as it pertains to predicting and preventing the impacts of increased heat;\n**(3)**\nenhance observations, surveillance, monitoring, and analysis necessary for the activities described in paragraphs (1) and (2); and\n**(4)**\ncommunicate, educate, and build awareness regarding the risks and impacts of increased heat and extreme heat events to communities, educational and economic sectors, Indian Tribes, and other relevant stakeholders.\n##### (e) Data management\n**(1) Availability of data**\nThe Director of the System shall coordinate with interagency partners to ensure that data and metadata associated with the System is fully and openly available, within the legal right to redistribute, in accordance with chapter 31 of title 44, United States Code (commonly known as the Federal Records Act of 1950 ), and the Foundations for Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ; 132 Stat. 5529) and the amendments made by that Act, to maximize use of such data to support the goals of the System.\n**(2) Data management strategies**\nIn coordination with the activities described in paragraph (1), the Director of the System and interagency partners shall\u2014\n**(A)**\ndevelop data management strategies to ensure that data and metadata are adequately stewarded, maintained, and archived in accordance with\u2014\n**(i)**\nfindable, accessible, interoperable, and reusable (FAIR) principles;\n**(ii)**\nthe Foundations for Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ; 132 Stat. 5529) and the amendments made by that Act; and\n**(iii)**\ncollective benefit, authority to control, responsibility, and ethics (CARE) principles; and\n**(B)**\npreserve and curate such data and metadata, in accordance with chapter 31 of title 44, United States Code.\n**(3) National Centers for Environmental Information**\n**(A) In general**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall manage, maintain, and steward archival data and metadata associated with the System within the National Centers for Environmental Information.\n**(B) Warning coordination meteorologist**\nThe Under Secretary of Commerce for Oceans and Atmosphere shall designate at least one warning coordination meteorologist with expertise in heat warnings, as described in section 405 of the Weather Research and Forecasting Innovation Act of 2017 ( 15 U.S.C. 8545 ), at the National Centers for Environmental Information.\n##### (f) Research program\nThe Director of the System shall develop and implement a climate and health research grant program, in coordination with the financial assistance program under section 7 and other Federal programs\u2014\n**(1)**\nto improve understanding of\u2014\n**(A)**\nthe climate epidemiology and social, behavioral, and economic drivers of heat-health vulnerability and risk;\n**(B)**\nthe drivers of climate variability, predictability, and changes in extreme heat; and\n**(C)**\nthe impacts of extreme heat, compound hazards, and cascading impacts across timescales;\n**(2)**\nto investigate and evaluate the effectiveness of risk management actions, interventions, policies, standards, codes, and guidelines; and\n**(3)**\nto address other topics as appropriate, including topics outlined in the strategic plan required by section 4(e)(1) and the financial assistance program under section 7.\n##### (g) Additional activities\nThe Director of the System shall carry out such other activities as the National Integrated Heat Health Information System Interagency Committee established under section 5 considers appropriate.\n#### 6. Study on extreme heat information and response\n##### (a) Study\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the Under Secretary of Commerce for Oceans and Atmosphere, in consultation with the National Integrated Heat Health Information System Interagency Committee established under section 4 (in this section referred to as the Committee ) and the individuals and entities described in section 4(g), shall seek to enter into an agreement with the National Academies of Sciences, Engineering, and Medicine to conduct a study on extreme heat information and response, to be completed not later than 3 years after such date of enactment.\n**(2) Elements**\nThe study described in paragraph (1) shall\u2014\n**(A)**\nidentify policy and research gaps, which may include\u2014\n**(i)**\nregions of the United States with the largest gaps between awareness, preparedness, and capacity to address extreme heat; and\n**(ii)**\nheat-related gaps in data, such as\u2014\n**(I)**\nthe number of schools, prisons, and other public facilities that lack air conditioning;\n**(II)**\nthe demographic breakdown of people affected by heat events, including by race, age, gender, occupation, and income;\n**(III)**\ncapacity building, research, and heat resilience resource shortages in rural and urban communities;\n**(IV)**\nmedical coding in health care facilities (such as hospitals, emergency rooms, and health centers) that indicate heat-related illnesses (such as kidney failure, dehydration, and fainting spells);\n**(V)**\nwith respect to public policy at the State and community level that enhances vulnerabilities to extreme heat (such as outdoor working conditions and thresholds to protect workers, animals, and others susceptible to heat-related illness); and\n**(VI)**\nthe extent to which Federal heat-health tools that have been discontinued, dismantled, or otherwise limited in public accessibility and availability, including the Centers for Disease Control and Prevention Heat and Health Tracker, the Office of Climate Change and Health Equity Climate and Health Outlook, the National Weather Service HeatRisk portal, the National Emergency Medical Services Information System Heat-related Emergency Management Service Activation Surveillance Dashboard, and the Low Income Home Energy Assistance Program and Extreme Heat website, have contributed to changes in extreme heat risk, education, and data collection;\n**(B)**\nprovide recommendations for addressing gaps with respect to policy, research, operations, communications, and data, including the gaps identified under subparagraph (A), affecting heat-health planning, preparedness, response, resilience, adaptation, and environmental justice and equity;\n**(C)**\nprovide such other recommendations as the Director of the National Integrated Heat Health Information System established under section 5 considers appropriate, which may include strategies for\u2014\n**(i)**\ncommunicating warnings to and providing impact-based decision support to promote preparedness actions and resilience of populations with limited opportunities to avoid extreme heat, including to individuals who may have barriers to such information;\n**(ii)**\nunderstanding compound and cascading risks, and implementing alternative heat-health risk reduction interventions to manage those risks collectively, such as reducing risk of the transmission of infectious diseases during heat waves by creating outdoor cooling locations or increasing ventilation and filtration in indoor cooling centers;\n**(iii)**\npromoting community resilience to heat events and incorporating principles of environmental justice in community response to heat waves;\n**(iv)**\naddressing the impacts of extreme heat on energy cost, affordability, and reliability for residential and commercial infrastructure (such as weatherization, energy costs, electric power systems, and water supply and treatment systems); and\n**(v)**\ndeveloping protections for workers for the effects of indoor and outdoor heat; and\n**(D)**\nconsider such other subjects as the Committee considers appropriate, which may include\u2014\n**(i)**\nthe feasibility of enhancing and standardizing existing nationwide data collection on heat-related illnesses and mortalities to improve and ensure consistent collection of national-level heat illness data across all 50 States, territories, and local jurisdictions of the United States;\n**(ii)**\nmechanisms for financing heat preparedness; and\n**(iii)**\nthe effectiveness of county- or local-level heat awareness and communication approaches, heat action, and tools, preparedness plans, or mitigation.\n**(3) Development of definitions**\nFollowing the study described in paragraph (1), the Committee shall work with heat experts across disciplines to comprehensively identify impacts of increased heat to inform consistent and agreed upon definitions for heat events, heat waves, and other relevant terms.\n##### (b) Report\nNot later than 90 days after completing the study described in subsection (a)(1), the Committee shall\u2014\n**(1)**\nmake available to the public on a Federal internet website of the National Oceanic and Atmospheric Administration a report on the findings and conclusions of the study; and\n**(2)**\nsubmit the report to\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate;\n**(C)**\nthe Committee on Science, Space, and Technology of the House of Representatives;\n**(D)**\nthe Committee on Energy and Commerce of the House of Representatives; and\n**(E)**\nthe Committee on Education and Workforce of the House of Representatives.\n#### 7. Financial assistance for resilience in addressing extreme heat and health risks\n##### (a) Community heat resilience program\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Director of the National Integrated Heat Health Information System established under section 5 (in this section referred to as the Director ) may, in coordination with the National Integrated Heat Health Information System Interagency Committee established under section 4 (in this section referred to as the Committee ), establish and administer a community heat resilience program to provide financial assistance to eligible entities to carry out projects described in subsection (e) to ameliorate human health impacts of extreme heat events.\n**(2) Revision**\nUpon completion of the strategic plan required by section 4(e)(1), the Committee may revise the community heat resilience program to ensure the program aligns with the strategic plan and is administered in accordance with the plan.\n##### (b) Purpose\nThe purpose of the financial assistance provided under this section is to improve community resilience to heat and heat-health impacts and further scientific research to address adaptation gaps and priorities.\n##### (c) Forms of assistance\nFinancial assistance provided under this section may be in the form of prizes, contracts, grants, or cooperative agreements.\n##### (d) Eligible entities\nEntities eligible to receive financial assistance under this section to carry out projects described in subsection (e) include\u2014\n**(1)**\nnonprofit entities;\n**(2)**\nStates;\n**(3)**\nIndian Tribes;\n**(4)**\nlocal governments;\n**(5)**\nlocal workforce development boards;\n**(6)**\nacademic institutions; and\n**(7)**\ncenters of excellence designated by the National Integrated Heat Health Information System.\n##### (e) Eligible projects\nProjects described in this subsection include the following:\n**(1)**\nProjects to reduce heat-health risks, including sustainable heat reduction and mitigation solutions such as for cool roofs, cool pavements, urban forestry or tree plantings and maintenance, the provision of shade, cooling and resilience centers, retrofitting buildings for cooling, improving the resilience of the power grid to ensure reliable air conditioning, energy efficiency, acquisitions or upgrades of filtration systems or high-efficiency air conditioning systems, and strategies to improve community level response before and during a heat event.\n**(2)**\nTraining programs to support the development and integration of education and training programs for identifying and addressing risks associated with climate change for vulnerable individuals.\n**(3)**\nProjects designed to improve heat risk mitigation capacity, research, and resource access and deployment in rural and urban communities.\n**(4)**\nProjects focusing on being responsive to heat-related needs from communities heard from engagements at different geographic scales (national to regional to local) including\u2014\n**(A)**\nto expand public awareness of heat risks;\n**(B)**\nto conduct community-based climate and health observational campaigns;\n**(C)**\nto conduct scientific research to assess and address gaps and priorities regarding the risks of extreme heat in communities;\n**(D)**\nto communicate risks and warnings to isolated communities;\n**(E)**\nto support the establishment of workplace policies and practices to reduce the risk of extreme heat illness among workers;\n**(F)**\nto educate such communities about how to respond to extreme heat events; and\n**(G)**\nto establish local, city, and county heat planning and heat-related emergency action plans.\n**(5)**\nOther projects that the Director determines will achieve a significant reduction in heat risk or increased resilience to increased heat or extreme heat events.\n##### (f) Priorities\nIn selecting eligible entities to receive financial assistance under this section, the Director shall prioritize entities that will carry out projects that provide benefits for historically disadvantaged communities and communities with significant heat disparities associated with race, ethnicity, or income.\n##### (g) Distribution of assistance\n**(1) Communities with environmental justice concerns and low income communities**\nNot less than 40 percent of the amount of financial assistance provided under this section in any fiscal year shall be provided to eligible entities to implement projects described in subsection (e) in communities with environmental justice concerns or low-income communities.\n**(2) Equitable distribution**\nThe Director shall seek to equitably distribute financial assistance provided under this section based on geographic location or such other factors as the Director determines appropriate.\n#### 8. Authorization of appropriations\n##### (a) National Integrated Heat Health Information System Interagency Committee; National Integrated Heat Health Information System\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to carry out sections 4 and 5, including for any administrative costs for the National Integrated Heat Health Information System Interagency Committee and the National Integrated Heat Health Information System, the following:\n**(1)**\nFor fiscal year 2026, $20,000,000.\n**(2)**\nFor fiscal year 2027, $20,000,000.\n**(3)**\nFor fiscal year 2028, $20,000,000.\n**(4)**\nFor fiscal year 2029, $20,000,000.\n**(5)**\nFor fiscal year 2030, $20,000,000.\n##### (b) Study on extreme heat information and response\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to contract with the National Academies of Sciences, Engineering, and Medicine to carry out section 6 $500,000 for each of fiscal years 2026 through 2028.\n##### (c) Financial assistance for resilience in addressing extreme heat and health risks\nThere is authorized to be appropriated to the National Oceanic and Atmospheric Administration to carry out section 7 the following:\n**(1)**\nFor fiscal year 2026, $10,000,000.\n**(2)**\nFor fiscal year 2027, $10,000,000.\n**(3)**\nFor fiscal year 2028, $20,000,000.\n**(4)**\nFor fiscal year 2029, $30,000,000.\n**(5)**\nFor fiscal year 2030, $30,000,000.",
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
        "actionDate": "2025-09-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5104",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Preventing HEAT Illness and Deaths Act of 2025",
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
        "name": "Health",
        "updateDate": "2025-09-19T14:57:00Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2675is.xml"
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
      "title": "Preventing HEAT Illness and Deaths Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-15T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing HEAT Illness and Deaths Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-15T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Preventing Health Emergencies And Temperature-related Illness and Deaths Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-15T02:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to reduce the health risks of heat by establishing the National Integrated Heat Health Information System within the National Oceanic and Atmospheric Administration and the National Integrated Heat Health Information System Interagency Committee to improve extreme heat preparedness, planning, and response, requiring a study, and establishing financial assistance programs to address heat effects, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-15T02:18:19Z"
    }
  ]
}
```
