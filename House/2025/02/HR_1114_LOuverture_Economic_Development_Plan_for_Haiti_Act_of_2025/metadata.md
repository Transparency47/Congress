# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1114?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1114
- Title: L’Ouverture Economic Development Plan for Haiti Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1114
- Origin chamber: House
- Introduced date: 2025-02-07
- Update date: 2025-12-12T09:07:04Z
- Update date including text: 2025-12-12T09:07:04Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-07: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-02-07: Introduced in House

## Actions

- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Introduced in House
- 2025-02-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-07 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-07",
    "latestAction": {
      "actionDate": "2025-02-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1114",
    "number": "1114",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "L\u2019Ouverture Economic Development Plan for Haiti Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-12T09:07:04Z",
    "updateDateIncludingText": "2025-12-12T09:07:04Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-07",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-07",
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
          "date": "2025-02-07T14:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-07T14:01:05Z",
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
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-02-07",
      "state": "IL"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-06-02",
      "state": "FL"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-06-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "False",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-07-29",
      "state": "FL"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "NY"
    },
    {
      "bioguideId": "D000197",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. DeGette, Diana [D-CO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "DeGette",
      "party": "D",
      "sponsorshipDate": "2025-11-07",
      "state": "CO"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1114ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1114\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 7, 2025 Mrs. Cherfilus-McCormick (for herself, Ms. Schakowsky , and Mr. Jackson of Illinois ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Ways and Means , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo authorize the establishment of a Haitian American Enterprise Fund for Haiti, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the L\u2019Ouverture Economic Development Plan for Haiti Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe General Secretariat of the Organization of the American States stated in 2022, The international community, international financial institutions, the multilateral system, and the international financial community of donor countries must make a decision: whether they want to industrialize Haiti sufficiently to ensure work for nine million Haitians, or whether it is economically more profitable to continue absorbing Haitian migrants and let host countries accommodate them as and how they can and in such economic conditions as they can offer. .\n**(2)**\nRather than building upon the ongoing lucrative trade relations with a newly independent Republic of Haiti in 1804, the United States decided to impose a trade embargo on the nascent state in 1806 because Haiti\u2019s independence ended chattel slavery in its land and perceived it as a threat because it became the world\u2019s first Black republic.\n**(3)**\nAfter its independence, Haiti was made to pay an indemnity to France, its former colonial power, beginning in 1825, for breaking away from slavery, which amounts to at least $21,000,000,000 today, setting the stage for Haiti\u2019s dire impoverishment today.\n**(4)**\nHaiti\u2019s independence from France in 1804 directly resulted in France selling the bulk of its possessions in mainland North America in what became the Louisiana Purchase, fueling the westward expansion of the young United States to the Pacific Ocean in what is today States such as Arkansas, Colorado, Iowa, Louisiana, Kansas, Montana, Missouri, and Nebraska.\n**(5)**\nDespite a tortured relationship, Haiti has long been a reliable partner of the United States. For example, after the bombing of Pearl Harbor in 1941, Haiti was among the first nations to join the United States in World War II and contributed funds to the United States effort.\n**(6)**\nHaiti bears a strategic importance to the United States due to its location in the Western Hemisphere.\n**(7)**\nHaitian Americans continue to make important contributions to the United States economy and have played a significant role in education, health care, literature, politics, art, and culture.\n**(8)**\nThe Bureau of the Census estimates that the Haitian-American population is 1.2 million, which many believe may be severely undercounted, as persons of Haitian descent have been coming to the United States since prior to the founding of the United States.\n**(9)**\nThe Haitian American population plays a vital role in Haiti\u2019s development efforts, leveraging their resources, expertise, and networks to support education, technology, sustainable development, resilience, and prosperity in the country and could do much more in partnership with the United States Government.\n**(10)**\nAccording to the World Bank, the Haitian diaspora sent over $4,000,000,000 in remittances to Haiti in 2023, equaling more than one-fifth of the country\u2019s gross domestic product with these remittances having a crucial role in Haiti\u2019s economy, providing a steady source of income for families in Haiti, contributing to poverty reduction, amounting to more than the sum of yearly foreign assistance to the country.\n**(11)**\nHaiti has played a pivotal role in Afro-descendants\u2019 struggle for American values such as freedom in America, the Caribbean, and African countries, including the Haitian American leaders such as W.E.B. DuBois, cofounder of the National Association for the Advancement of Colored People, who have contributed to the Civil Rights movement in the United States and across the world.\n**(12)**\nAssisting Haiti with a well-processed development program leading to sustainable economic development that keeps Haitians at home is in the vital interest of the United States.\n**(13)**\nThe United States should assist Haiti in establishing sustainable inclusive development to meet the needs of all of its people, instead of being drawn to the lure of debt-trap driven development promoted by the People\u2019s Republic of China.\n**(14)**\nAccording to the United Nations Conference on Trade and Development, Haiti will need, at minimum, an estimate of $19,300,000,000 (in 2020/2021 dollars) to meet key development metrics including to\u2014\n**(A)**\nachieve 7 percent annual GDP growth;\n**(B)**\neliminate extreme poverty;\n**(C)**\ndouble manufacturing growth;\n**(D)**\nimprove health and well-being;\n**(E)**\nimprove quality primary and secondary formal education leading to relevant and effective learning outcomes; and\n**(F)**\nprotect environmental biodiversity.\n#### 3. Purposes\nThe purposes of this Act are to promote and facilitate\u2014\n**(1)**\ndevelopment of the Haitian private sector, particularly micro, small, and medium businesses, the agriculture, biodiversity, construction, energy, finance, manufacturing, and tourism industries, and U.S.-Haitian joint ventures, including the Haitian-American diaspora;\n**(2)**\npolicies and practices conducive to Haitian private sector development through equity investments, feasibility studies, grants, guarantees, insurance, loans, technical assistance, and training;\n**(3)**\nan economic environment conducive for an accountable, transparent, and sustained democratic system of governance in Haiti, inclusive for its people, in coordination with the Global Fragility Act of 2019 (section 501 of title V of division J of Public Law 116\u201394 ; Stat. 3060); and\n**(4)**\npolicies that engender conditions for an industrialized Haiti sufficient to ensure work at full employment levels meeting United Nations medium to high human development from human development index indicators for the people of Haiti, thereby reducing irregular migration flows from the country, a United States national security concern.\n#### 4. Statements of policy\nIt is the policy of the United States to support the sustainable rebuilding and development of Haiti in a manner that\u2014\n**(1)**\nrecognizes that the United States has longstanding historical, economic, and cultural ties to Haiti, with millions of Americans tracing their heritage to the country, and has a vested interest in Haiti\u2019s stability and development;\n**(2)**\nrecognizes Haitian independence, self-reliance, and sovereignty;\n**(3)**\nacknowledges that it is in the United States national and regional security interest to assist a stable, democratic and prosperous Haiti that will consequently reduce irregular migration, regional crime, narcotics proliferation, and insecurity;\n**(4)**\nsupports the restoration of democratic governance in Haiti through free, fair, and transparent elections as an essential condition for reestablishing lasting security, economic development, and the national interests of Haiti and the United States by\u2014\n**(A)**\nsupporting the self-determination of the Haitian people and recognizing that the sovereign and national right of the citizens of Haiti must be exercised free of interference;\n**(B)**\nacknowledging that any political transition must come from a Haitian-led solution; and\n**(C)**\nopposing any efforts to destabilize the state of Haiti;\n**(5)**\nsupports democratic transition, the strengthening of institutions, good governance, and the rule of law in Haiti by\u2014\n**(A)**\nassisting in strengthening Haiti\u2019s institutions, judiciary system, governance structures and mechanisms to better respond to the needs of Haitians;\n**(B)**\nsupporting anticorruption efforts;\n**(C)**\npromoting press freedom;\n**(D)**\nsupporting the empowerment of Haitian civil society;\n**(E)**\nimproving transparency and the independence of the media;\n**(F)**\npreventing favorable treatment or influence on behalf of any individual, entity, or party in the selection by the Haitian people of their future government; and\n**(G)**\nreducing violence against women and children and addressing human rights concerns, including through the enforcement of sanctions imposed in accordance with the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 2656 note) on individuals implicated in human rights violations and corruption;\n**(6)**\nimproves Haiti\u2019s security by\u2014\n**(A)**\nsupporting the goals of the U.S. Strategy to Prevent Conflict and Promote Stability 10-Year Plan for Haiti report, a derivative of the Global Fragility Act of 2019;\n**(B)**\nsupporting continued funding of the Haitian National Police;\n**(C)**\nsupporting Haiti\u2019s and international efforts to assist the Haitian National Police in combating internal insecurity, including gang violence;\n**(D)**\nstemming the flow of illicit firearms trafficking from the United States to the Caribbean, including Haiti;\n**(E)**\nencouraging the development of civilian oversight of the Haitian National Police;\n**(F)**\nencouraging the Haitian National Police to respect human rights and uphold anti-corruption measures in its practices; and\n**(G)**\nencouraging a Disarmaments, Demobilization, and Reinsertion program to reduce criminality and protect the youth;\n**(7)**\naddresses humanitarian needs by providing appropriate forms of assistance, such as humanitarian assistance, to the people of Haiti by addressing urgent food security, health, and education needs as well as protecting women and children;\n**(8)**\nspurs economic development by\u2014\n**(A)**\nleveraging public and private source funding to address Haiti\u2019s long term development goal and achieving United Nations Sustainable Development Goals;\n**(B)**\nhelping, creating, and enabling an environment that facilitates trade and investment in Haiti;\n**(C)**\nassisting in building the resilient and supportive physical infrastructure sector required for a stable and prosperous country, including country-wide access to reliable electricity, passable roads, ports, railroads, water, sanitation and health programs and digital infrastructure;\n**(D)**\nreducing poverty and building prosperity by providing capacity building support to promote entrepreneurship and support small and medium-sized enterprises, including participation of Haitian women and youth in governmental and nongovernmental institutions and in economic development and governance assistance programs funded by the United States;\n**(E)**\nsupporting trade preferences with Haiti, including the preferences created through the Haitian Hemispheric Opportunity Through Partnership Act of 2006 (title V of division D of Public Law 109\u2013432 ; 120 Stat. 3181) and the Haiti Economic Lift Program Act of 2010 ( 19 U.S.C. 2703 et seq. );\n**(F)**\nassisting in building the long-term capacity of the Government of Haiti, civil society, local resource mobilization in Haiti, and the private sector to foster economic opportunities in Haiti; and\n**(G)**\nfostering collaboration and activities between the Haitian diaspora in the United States, including dual citizens of Haiti and the United States, and the Government of Haiti, local resource mobilization in Haiti, and the business community in Haiti;\n**(9)**\nencourages other countries, along with bilateral and multilateral organizations, to provide similar assistance and to work cooperatively with such countries and organizations to coordinate such assistance; and\n**(10)**\nrespects and helps restore the natural resources of Haiti and strengthens community-level resilience to environmental and weather-related impacts.\n#### 5. Haitian American Enterprise Fund for Haiti\n##### (a) Designation\nThe President may designate a private, nonprofit organization (as described in section 501(c)(3) of the Internal Revenue Code of 1986 and exempt from tax under section 501(a) of such code) as the Haitian American Enterprise Fund for Haiti (in this Act referred to as the Enterprise Fund ), if the President\u2014\n**(1)**\ndetermines that such organization has the ability to carry out the activities described in section 7; and\n**(2)**\nhas consulted with the Speaker and the minority leader of the House of Representatives and the majority leader and the minority leader of the Senate regarding such designation.\n##### (b) Operation\nUpon the designation of the Enterprise Fund under subsection (a), the Chief Executive Officer of the United States International Development Finance Corporation shall operate such Fund.\n##### (c) Consultation\nThe Chief Executive Officer may consult and coordinate with the Administrator of the United States Agency for International Development regarding the Enterprise Fund.\n##### (d) Private character of Enterprise Fund\nNothing in this Act may be construed to make\u2014\n**(1)**\nthe Enterprise Fund an agency or establishment of the United States Government; or\n**(2)**\nthe officers and employees of the Enterprise Fund or members of the Oversight Panel officers or employees of the United States for purposes of title 5, United States Code.\n#### 6. Oversight Panel\n##### (a) In general\nThe Enterprise Fund shall be monitored by a Board of Directors Oversight Panel (hereafter referred to as the Oversight Panel ) composed of 9 members.\n##### (b) Composition\n**(1) Appointments by Chief Executive Officer**\nThe Chief Executive Officer shall appoint to the Oversight Panel\u2014\n**(A)**\n5 individuals who are not employed by the Federal Government and\u2014\n**(i)**\nare citizens of the United States; or\n**(ii)**\nare citizens of the Republic of Haiti who\u2014\n**(I)**\nprimarily reside in the United States; and\n**(II)**\nhave demonstrated respect for democracy and a free-market economy; and\n**(B)**\n2 individuals who are citizens of Haiti who\u2014\n**(i)**\nare not citizens of the United States;\n**(ii)**\nhave demonstrated respect for democracy and a free-market economy; and\n**(iii)**\nhave\u2014\n**(I)**\nhad a successful business career in private equity, banking, or finance in a developing economy; or\n**(II)**\nexperience comparable to service on the board of directors of a fund that is similar to the Enterprise Fund and which earned a positive return on the amounts under the control of such fund.\n**(2) Appointments by President**\nThe President shall appoint to the Oversight Panel 2 individuals who are citizens of the United States, who\u2014\n**(A)**\nprimarily reside in the United States; and\n**(B)**\nhave demonstrated concern for and commitment to the economic development of Haiti.\n##### (c) Consultations\nThe Chief Executive Officer and members of the Oversight Panel are encouraged to consult extensively with\u2014\n**(1)**\nrepresentatives of similar enterprise funds established by the United States Government, in order to learn best practices relating to the start-up phase and ongoing business of an enterprise fund;\n**(2)**\nrepresentatives of multilateral institutions, including the Inter-American Development Bank, the World Bank, and the International Monetary Fund, to coordinate support for infrastructure in Haiti; and\n**(3)**\nleaders from the private sector, civil society, labor organizations, human rights groups, academia, and environmental organizations in the United States and Haiti.\n#### 7. Investments for certain programs and projects\n##### (a) Requirements for investments\nThe Enterprise Fund may only provide investments in programs and projects that\u2014\n**(1)**\npromote development of the Haitian private sector, particularly with respect to\u2014\n**(A)**\nmicro, small, and medium businesses;\n**(B)**\nthe agriculture, biodiversity, construction, energy, finance, manufacturing, and tourism industries; and\n**(C)**\njoint ventures between the United States and Haiti or the Haitian-American diaspora, including joint ventures that empower women and youth;\n**(2)**\npromote policies and practices that facilitate the development of the Haitian private sector through\u2014\n**(A)**\nequity investments;\n**(B)**\nfeasibility studies;\n**(C)**\ngrants;\n**(D)**\nguarantees;\n**(E)**\ninsurance;\n**(F)**\nloans;\n**(G)**\ntechnical assistance; and\n**(H)**\ntraining;\n**(3)**\nfacilitate an economic environment conducive for an accountable, transparent, and sustained democratic system of governance in Haiti, aligned with the Global Fragility Strategy required in section 504(a) of the Global Fragility Act of 2019 ( 22 U.S.C. 9803(a) );\n**(4)**\nbuild the resilient physical infrastructure required for Haiti to be stable and prosperous, including\u2014\n**(A)**\ncountry-wide access to reliable electricity;\n**(B)**\nelectricity generation plants;\n**(C)**\npassable roads and bridges;\n**(D)**\nports;\n**(E)**\nrailroads;\n**(F)**\nhydrological dams;\n**(G)**\nagriculture canals;\n**(H)**\nstorm water management systems;\n**(I)**\nwater infrastructure; and\n**(J)**\nsanitation and health programs and infrastructure;\n**(5)**\ncreate a report that includes\u2014\n**(A)**\nthe cost to update the physical infrastructure described in paragraph (4) in Haiti to meet resilience standards; and\n**(B)**\nan analysis of completed physical infrastructure projects;\n**(6)**\nassist in leveraging public and private funding to address development needs in Haiti; or\n**(7)**\nengender conditions for development and industrialization, create sustainable jobs, or reduce the root cause of irregular migrations in Haiti.\n##### (b) Authorized activities\nThe Enterprise Fund may make investments in and encourage\u2014\n**(1)**\nincreased access to consumer credit in Haiti, including from consumer credit unions (also known as caisse populaires );\n**(2)**\nthe establishment of local agriculture cooperatives in Haiti;\n**(3)**\nthe establishment of major electricity generation facilities and complementary regional and national electricity grids in Haiti;\n**(4)**\nthe establishment of working global manufacturing facilities, including facilities manufacturing\u2014\n**(A)**\nfood;\n**(B)**\nbeverages;\n**(C)**\ntobacco;\n**(D)**\nchemicals;\n**(E)**\npharmaceuticals;\n**(F)**\nelectronics;\n**(G)**\noptical products;\n**(H)**\ntextiles;\n**(I)**\napparel; and\n**(J)**\nleather;\n**(5)**\nprojects providing modern information technology infrastructure required to deliver and monitor development services to economically vulnerable populations in Haiti; and\n**(6)**\nprojects providing management and technical capacity training and development to promote private sector development, including training on effective management and governance.\n##### (c) Financial instruments for investment in Haiti\n**(1) In general**\nThe Enterprise Fund shall, if practicable, establish financial instruments to enable individuals to invest in the Haitian private sector.\n**(2) Preferred investments**\nIf practicable, the financial instruments established under paragraph (1) shall\u2014\n**(A)**\nfacilitate investment in projects that support development and humanitarian relief in Haiti; and\n**(B)**\nsupport Haitian businesses and employees.\n##### (d) Investment priority\nIn making investments under this section, the Enterprise Fund shall give priority to industries identified by the Government of Haiti as priorities for the economic recovery and growth of Haiti.\n##### (e) Matters for consideration\nThe Enterprise Fund shall take into account\u2014\n**(1)**\ninternationally recognized human rights, including the rights of workers;\n**(2)**\nenvironmental factors;\n**(3)**\nthe effect of the activities of the Fund on the economy and labor market of the United States; and\n**(4)**\nthe likelihood that the activity receiving investments from the Enterprise Fund will be commercially viable.\n#### 8. Administration of funds\n##### (a) Use of investment returns and payments\nThe Enterprise Fund may use returns on the investments of the Enterprise Fund and payments to the Enterprise Fund to provide the investments described in section 7, without transferring such returns or payments to the Treasury and without further appropriation by Congress.\n##### (b) Ensuring ability To repay funds\nThe Chief Executive Officer shall provide investments in a manner that ensures that the Enterprise Fund will be able to repay the Treasury as required by section 11.\n##### (c) Use of United States private venture capital\n**(1) In general**\nThe Enterprise Fund may conduct public offerings or private placements for the purpose of soliciting and accepting United States venture capital, which may be used, separately or together with funds appropriated to the Enterprise Fund, for any lawful investment purpose that the Chief Executive Officer considers appropriate to carry out this Act.\n**(2) No private investor oversight**\nAcceptance of private venture capital does not authorize private investors to have a role in the oversight of the Enterprise Fund.\n**(3) Distributions**\nFinancial returns on Enterprise Fund investments that include private venture capital may be distributed, at such times and in such amounts as the Chief Executive Officer considers appropriate, to the investors of such capital.\n##### (d) Limitations\n**(1) Payments to Enterprise Fund personnel**\nNo funds of the Enterprise Fund shall inure to the benefit of any Oversight Panel member, officer, or employee of the Enterprise Fund, except as salary or reasonable compensation for services.\n**(2) Use of Federal funds for grants**\nNot more than 20 percent of Federal funds made available to the Enterprise Fund may be used for investments in the form of grants.\n**(3) Use of appropriated funds for costs and feasibility studies**\nNot more than 15 percent, in total, of funds appropriated to the Enterprise Fund may be used for operating costs and feasibility studies to assess commercial viability of activities and projects funded by the Enterprise Fund.\n#### 9. Audits and recordkeeping\n##### (a) Independent private audits\nThe Chief Executive Officer shall ensure that the Enterprise Fund is audited annually by an independent certified public accountant or independent licensed public accountant certified or licensed by a regulatory authority of a State or political subdivision of a State, in accordance with generally accepted auditing standards.\n##### (b) Government Accountability Office audits\nWith respect to any year during which the Enterprise Fund is in possession of funds received from the United States Government, the Comptroller General of the United States shall audit the financial transactions of the Enterprise Fund to identify waste, fraud, or abuse, in accordance with such principles and procedures and under such rules and regulations as the Comptroller General may prescribe.\n##### (c) Recordkeeping requirements\nThe Chief Executive Officer shall ensure that\u2014\n**(1)**\neach recipient of funds provided by the Enterprise Fund under section 7 keeps\u2014\n**(A)**\na separate account for such funds;\n**(B)**\nsuch records as may be reasonably necessary to fully disclose\u2014\n**(i)**\nthe amount of such funds;\n**(ii)**\nthe total amount of such funds received by such recipient;\n**(iii)**\nthe total cost of the project or activity for which the Enterprise Fund provided such funds; and\n**(iv)**\nthe amount of the cost of the project or activity supplied by sources other than the Enterprise Fund; and\n**(C)**\nany other records that will facilitate an effective audit; and\n**(2)**\nthe Chief Executive Officer has access, for the purpose of audit and examination, to any record described in paragraph (1)(B).\n#### 10. Reports\n##### (a) Public report on Enterprise Fund activities\nNot later than 180 days after the establishment of the Enterprise Fund and annually thereafter until the Enterprise Fund terminates, the Chief Executive Officer shall make publicly available on the websites of the Enterprise Fund, the United States International Development Finance Corporation, and the United States Agency for International Development a report describing the funds provided by the Enterprise Fund for activities and projects described in section 7, with a written explanation of the commercial viability of each such activity and project.\n##### (b) Report to Congress on Enterprise Fund activities\n**(1) In general**\nNot later than 120 days after the end of the fiscal year during which the Enterprise Fund is established and annually thereafter until the Enterprise Fund terminates, the Chief Executive Officer shall submit to the appropriate congressional committees a report that\u2014\n**(A)**\ndescribes the successes, failures, expenses, activities, funding, and forecasted projections of the Enterprise Fund; and\n**(B)**\nincludes the results of the audit required by section 9(a).\n**(2) Appropriate congressional committees defined**\nIn this section, the term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Appropriations, the Committee on Financial Services, and the Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Appropriations and the Committee on Foreign Relations of the Senate.\n##### (c) Report on Oversight Panel duties\nNot later than 180 days after the date of the enactment of this Act and annually thereafter until the Enterprise Fund terminates, the Oversight Panel shall submit to Congress and the President a report on the implementation of the duties of the Oversight Panel during the preceding year, including a description of successes regarding implementation of the Enterprise Fund and challenges preventing the Enterprise Fund from meeting its full potential.\n##### (d) Report after failure To repay\nNot later than 120 days after the last day of any year in which the repayment to the Treasury required by section 11 has not yet been completed, the Chief Executive Officer shall make publicly available a report that includes a comprehensive and detailed description of the operations, activities, financial condition, and accomplishments of the Enterprise Fund during such year.\n#### 11. Termination\nNot later than December 31, 2031\u2014\n**(1)**\nthe Chief Executive Officer shall repay from the Enterprise Fund to the Treasury the full amount of funds the Enterprise Fund received from the United States Government; and\n**(2)**\nthe Enterprise Fund shall terminate.\n#### 12. Nonapplicability of other laws\nNotwithstanding any other provision of law, executive branch agencies may conduct programs and activities and provide services in support of the activities of the Enterprise Fund.\n#### 13. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act $1,000,000,000 for each of fiscal years 2026 through 2031, which shall be authorized to remain available until expended or until the Enterprise Fund terminates, whichever occurs first.",
      "versionDate": "2025-02-07",
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
        "updateDate": "2025-05-07T13:19:27Z"
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
      "date": "2025-02-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1114ih.xml"
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
      "title": "L\u2019Ouverture Economic Development Plan for Haiti Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:02Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "L\u2019Ouverture Economic Development Plan for Haiti Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-11T04:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize the establishment of a Haitian American Enterprise Fund for Haiti, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-11T04:19:10Z"
    }
  ]
}
```
