# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4140?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4140
- Title: Burma GAP Act
- Congress: 119
- Bill type: HR
- Bill number: 4140
- Origin chamber: House
- Introduced date: 2025-06-25
- Update date: 2026-04-23T08:07:01Z
- Update date including text: 2026-04-23T08:07:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-25: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 5.
- Latest action: 2025-06-25: Introduced in House

## Actions

- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Introduced in House
- 2025-06-25 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 5.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-25",
    "latestAction": {
      "actionDate": "2025-06-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4140",
    "number": "4140",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "M001137",
        "district": "5",
        "firstName": "Gregory",
        "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
        "lastName": "Meeks",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Burma GAP Act",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:01Z",
    "updateDateIncludingText": "2026-04-23T08:07:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-22",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 5.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-07-22",
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
      "actionDate": "2025-06-25",
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
      "actionDate": "2025-06-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-25",
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
            "date": "2025-07-22T15:44:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-06-25T14:02:35Z",
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
      "isOriginalCosponsor": "True",
      "lastName": "McCaul",
      "middleName": "T.",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "H001058",
      "district": "4",
      "firstName": "Bill",
      "fullName": "Rep. Huizenga, Bill [R-MI-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Huizenga",
      "party": "R",
      "sponsorshipDate": "2025-06-25",
      "state": "MI"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "IN"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
      "state": "IL"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-07-10",
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
      "sponsorshipDate": "2025-07-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000389",
      "district": "17",
      "firstName": "Ro",
      "fullName": "Rep. Khanna, Ro [D-CA-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Khanna",
      "party": "D",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "K000397",
      "district": "40",
      "firstName": "Young",
      "fullName": "Rep. Kim, Young [R-CA-40]",
      "isOriginalCosponsor": "False",
      "lastName": "Kim",
      "party": "R",
      "sponsorshipDate": "2025-07-16",
      "state": "CA"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "NV"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-07-22",
      "state": "CA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "GA"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-07-29",
      "state": "CA"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "S001229",
      "district": "6",
      "firstName": "Jefferson",
      "fullName": "Rep. Shreve, Jefferson [R-IN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Shreve",
      "party": "R",
      "sponsorshipDate": "2025-11-18",
      "state": "IN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-11-18",
      "state": "DE"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4140ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4140\nIN THE HOUSE OF REPRESENTATIVES\nJune 25, 2025 Mr. Meeks (for himself, Mr. McCaul , Mr. Bera , and Mr. Huizenga ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo provide protection, support, and humanitarian assistance to Rohingya refugees and internally displaced people in Burma as well as promote accountability and a path out of genocide and crimes against humanity for Rohingya.\n#### 1. Short title\nThis Act may be cited as the Burma Genocide Accountability and Protection Act or the Burma GAP Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nIn its report dated September 17, 2018, the United Nations Independent International Fact-Finding Mission on Myanmar (FFM) found that impunity was a root cause of continued human rights violations in Myanmar that has significantly and demonstrably contributed to the validation of deeply oppressive and discriminatory conduct, enabled recurrence of human rights violations and atrocity crimes, and emboldened perpetrators and silenced victims , and concluded that ensuring accountability for crimes was the key to disrupting patterns of oppression and cycles of violence as well as a legal obligation for Burma.\n**(2)**\nOn December 13, 2018, the United States House of Representatives passed H. Res. 1091, by an overwhelming majority of 394 to 1, expressing the sense of the House of Representatives that atrocities committed against Rohingya by members of the Burma military and security forces since August 2017 constitute crimes against humanity and genocide.\n**(3)**\nOn September 16, 2019, the FFM reported that it has reasonable grounds to conclude that the evidence that infers genocidal intent on the part of the state, identified in its last report, has strengthened that there is a serious risk that genocidal actions may occur or recur .\n**(4)**\nOn February 1, 2021, the Burma military conducted a coup d\u2019\u00e9tat, derailing Burma\u2019s transition to democracy and disregarding the will of the people of Burma.\n**(5)**\nSince the February 2021 military coup, the Burma military and certain local armed groups have continued to commit crimes and abuses against Rohingya. In Rakhine state, over 600,000 Rohingya, including at least 130,000 confined in internally displaced persons (IDP) camps face heightened risks. The military continues to target Rohingya with laws and policies that criminalize the exercise of human rights, as well as with arbitrary arrest and detention, torture, sexual violence, and murder.\n**(6)**\nOn March 21, 2022, Secretary of State Antony Blinken announced the Secretary had determined that members of the Burmese military committed genocide and crimes against humanity against Rohingya .\n**(7)**\nThe United States has been the leading contributor of humanitarian assistance in response to the Rohingya crisis.\n**(8)**\nThe United Nations High Commissioner for Human Rights said in a June 2023 report that the Burma military\u2019s restrictions on aid access by local and international organizations seeking to respond to Cyclone Mocha in Rakhine state in May 2023 may amount to gross violations of international human rights law, and serious violations of international humanitarian law.\n**(9)**\nAccording to the World Food Program, over 15 percent of young children in the Rohingya refugee camps in Bangladesh are suffering from malnutrition. The World Food Program estimates that it needs another $83,000,000 in funding to maintain full rations and meet the basic minimum nutritional needs of refugees through May 2026.\n**(10)**\nFunding cuts and rising commodity prices have exacerbated protection concerns for Rohingya refugees in Bangladesh, especially with respect to gender-based violence and child protection, worsening health outcomes and fueling unsafe and irregular migration throughout the surrounding region.\n**(11)**\nCombined with rising food insecurity, Rohingya are increasingly unsafe in Bangladesh as a result of growing competition between armed and criminal groups in the refugee camps. These factors have driven thousands of Rohingya to flee to maritime Southeast Asia by boat only to face obstacles from regional navies and growing resentment from local populations.\n**(12)**\nThe long, systemic denial of the exercise of certain rights, including education, freedoms of expression, movement, and rights related to nationality have had enduring effects on many Rohingya persons\u2019 mental and physical well-being and perpetuate the risk of future genocidal violence until these root causes are addressed.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto uphold Article I of the Convention on the Prevention and Punishment of the Crime of Genocide, to which the United States is a party, to prevent the crime of genocide and punish its perpetrators;\n**(2)**\nto prevent and end atrocities committed against Rohingya by addressing the root causes of the genocide and crimes against humanity committed against them, holding the perpetrators of these crimes accountable, supporting solutions to respect the human rights and uphold the dignity of Rohingya, and to ensure Rohingya involvement and representation in decision making and implementation processes to address these needs;\n**(3)**\nto support the empowerment of Rohingya civilian leadership in diaspora communities, refugee camps in Bangladesh, and inside Burma through consultation and collaboration with Rohingya community representatives;\n**(4)**\nto provide holistic support to the Rohingya community to overcome decades of systematic persecution and discrimination and to best support the desires of all communities in Burma to achieve lasting peace and an inclusive, Federal democracy including through credible transitional justice processes;\n**(5)**\nto collaborate with other countries to pursue and implement coordinated, comprehensive, and sustained measures for upholding the dignity and protecting the human rights of Rohingya;\n**(6)**\nto engage in a coordinated manner with the United Nations High Commissioner for Refugees other relevant United Nations agencies, governments, and intergovernmental entities to establish protocols and respond to protection concerns and to prevent and protect Rohingya from further atrocities; and\n**(7)**\nto isolate the Burma military junta diplomatically and economically until such time that there is a return to civilian rule in Burma.\n#### 4. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe United States has a moral and legal responsibility to prevent and punish genocide, including against Rohingya;\n**(2)**\nthe Secretary of State\u2019s determination in March 2022 that genocide and crimes against humanity have been committed against Rohingya by members of the Burma military should lead to support for Rohingya to overcome decades of systemic persecution, marginalization, and violence;\n**(3)**\nthe Rohingya crisis and the broader Burma crisis must be addressed simultaneously to ensure that history does not repeat itself;\n**(4)**\nthe United States should work with other donor nations to ensure that Rohingya refugees in refugee camps in Bangladesh receive a ration sufficient to meet the humanitarian minimum standards for food and nutrition needs;\n**(5)**\nthe United States should encourage other countries to contribute additional assistance and follow United States leadership in protecting Rohingya through humanitarian assistance, political and economic empowerment, accountability for genocide, crimes against humanity, and any other international crimes committed by the Burma military and other armed groups in Burma, as well as supporting the voluntary resettlement or eventual safe repatriation of Rohingya refugees to Burma when conditions allow; and\n**(6)**\nthe United States should continue not to recognize the Burma military junta as the legitimate political representative of the Burmese people given the genocide, crimes against humanity, and coup that it has perpetrated.\n#### 5. United States Special Representative and Policy Coordinator for Burma\n##### (a) In general\nIn the absence of a United States Ambassador to Burma, the Secretary of State is authorized to appoint a career Foreign Service Officer of Senior Foreign Service rank as Special Representative and Policy Coordinator for Burma.\n##### (b) Duties\nThe Special Representative shall\u2014\n**(1)**\npromote a comprehensive international effort, including multilateral sanctions, direct dialogue with all parties, including democracy advocates, and support for nongovernmental organizations operating in Burma and neighboring countries, designed to restore civilian democratic governance to Burma and address the urgent humanitarian needs in the region;\n**(2)**\nconsult broadly, including with the Governments of Thailand, Bangladesh, India, the Republic of Korea, Japan, the member states of ASEAN, the European Union, and other nations to coordinate policies toward Burma;\n**(3)**\nassist efforts by the United Nations Special Envoy to secure the release of all political prisoners in Burma and to promote dialogue among all parties, including leaders of Burma\u2019s democracy movement;\n**(4)**\nconsult with Congress on policies relevant to Burma and the future and welfare of all the Burmese people, including refugees;\n**(5)**\ncoordinate multilateral sanctions efforts against Burma among United States allies and partners; and\n**(6)**\nsupport protection, humanitarian assistance, and accountability efforts for Rohingya and other Burmese ethnic minorities in Burma and the surrounding region.\n##### (c) Sunset\nThis section shall terminate on the date that is 5 years after the date of the enactment of this Act.\n#### 6. Support for protection efforts and durable solutions with respect to Rohingya\n##### (a) In general\nThe Secretary of State, in consultation with the Special Representative (if so designated under section 5(a)), should support efforts to protect Rohingya and prevent further atrocities against Rohingya and other Burmese ethnic minorities.\n##### (b) Protection efforts\nIn carrying out subsection (a), the Secretary should seek to engage in crisis response efforts and efforts to maximize the safety, security, and well-being of Rohingya in Burma and throughout South Asia and Southeast Asia, by\u2014\n**(1)**\nsupporting Rohingya refugees access to international protection as well as international asylum and refugee mechanisms, and preventing indefinite detention and nonrefoulement;\n**(2)**\nfacilitating greater access for Rohingya facing ongoing abuse, including human trafficking and gender-based violence, to appropriate legal support services;\n**(3)**\nsupporting a monitoring mechanism, rapid response team, legal assistance, and communication mechanisms to overcome military-imposed internet and telecommunication restrictions for Rohingya living in Burma;\n**(4)**\nworking with other governments in the region to strengthen regional mechanisms and overall coordination on lifesaving search and rescue, safe disembarkation, effective receiving and comprehensive assistance for Rohingya refugees;\n**(5)**\nsupporting host communities to facilitate a safer, more supportive, and welcoming environment for Rohingya refugees through the provision of technical assistance and cooperation with local organizations and governments; and\n**(6)**\nengaging the Government of Bangladesh and the international community to establish the necessary mechanisms for Rohingya refugees to file protection claims, and seek accountability by\u2014\n**(A)**\nimproving Rohingya refugees ability to access justice within Bangladesh through legal aid, simplifying the process for filing cases, facilitating the access of lawyers involved in international legal proceedings involving Rohingya, and enabling Rohingya to travel abroad to participate in legal proceedings in other courts;\n**(B)**\nsupporting enhanced coordination among Bangladesh security forces on investigations and accountability;\n**(C)**\nsupporting training for Bangladesh\u2019s Armed Police Battalion (APBn) and any other units providing security for Rohingya refugee camps on humanitarian protection principles and community safety; and\n**(D)**\nencouraging the Government of Bangladesh and other host governments to allow safe houses for Rohingya human rights activists, as well as defectors, insider witnesses to atrocities against Rohingya and other refugees facing imminent threats.\n##### (c) Promoting durable solutions\nIn carrying out subsection (a), the Secretary should seek to promote durable solutions with respect to Rohingya by\u2014\n**(1)**\nsupporting the inclusion of Rohingya across various sectors in Burma;\n**(2)**\nfacilitating training and capacity building on atrocity prevention for the National Unity Government (NUG), the National Unity Consultative Council (NUCC), the Committee Representing Pyidaungsu Hluttaw (CRPH), ethnic armed organizations, and other political stakeholders;\n**(3)**\nin consultation with Rohingya community representatives, including women and civil society leaders, collaborating with and supporting key non-military stakeholders to take preparatory steps for\u2014\n**(A)**\nensuring the safe and voluntary return of Rohingya, which should include those individuals displaced in the 1990s or born as internally displaced persons or refugees to their places of origin in Burma;\n**(B)**\nrestoring and protecting Rohingyas rights and providing them full and equal citizenship;\n**(C)**\nrecognizing Rohingya as an official ethnic group in Burma, and securing equal social and political power sharing under a Federal democratic Constitution;\n**(D)**\npromoting convenings and engagement among Rohingya, non state actors, civil society groups, and other key stakeholders in Rakhine state to promote trust building and reconciliation;\n**(E)**\nincluding Rohingya across administration and governance mechanisms of Burma, including Rakhine state; and\n**(F)**\ndeveloping a comprehensive transitional justice strategy;\n**(4)**\nworking with United States allies and partners to broaden resettlement programs and supporting the voluntary resettlement of the most vulnerable individuals within Rohingya populations, as well as defectors, deserters, and insider witnesses participating in justice processes; and\n**(5)**\nsupporting repatriation of Rohingya refugees only when conditions are conducive for a safe, voluntary, and sustainable return with full rights restored.\n#### 7. Humanitarian assistance and support for Rohingya refugees and internally displaced persons\n##### (a) In general\nThe Secretary of State, in consultation with the Special Representative (if so designated under section 5(a)) and other relevant United States Government agencies, should continue to provide assistance to Rohingya refugees, internally displaced persons, and host communities receiving such refugees and persons.\n##### (b) Activities supported\nAssistance provided under subsection (a) shall include the following:\n**(1)**\nProtection programming, including interventions focused on Rohingya civil society leaders, human rights activists, and others threatened by armed groups.\n**(2)**\nSupport for Rohingya civil society and community-based organizations, including diplomatic engagement to encourage the Government of Bangladesh to allow the operation of Rohingya-led civil society and community-based organizations in the refugee camps in Bangladesh.\n**(3)**\nPrograms to prevent and respond to gender-based violence, trafficking, forced marriage, as well as specialized training programs for vulnerable groups.\n**(4)**\nSupport for education, including higher education, for Rohingya refugees in Bangladesh.\n**(5)**\nSupport for displaced Rohingya to access livelihoods through vocational training and volunteer programs organized by international organizations and nongovernmental organizations.\n**(6)**\nSupport for meeting basic needs, including food, nutrition, health care, protection, shelter, water, sanitation, and hygiene support.\n**(7)**\nSupport to Rohingya in Burma, refugee camps in Bangladesh, and the diaspora to preserve Rohingya culture, history, and memory.\n#### 8. Promoting accountability for genocide and crimes against humanity committed against Rohingya in Burma\n##### (a) In general\nThe Secretary of State, in consultation with the Special Representative (if so designated under section 5(a)) and other relevant United States Government agencies, should take the actions described in subsection (b) to promote accountability for genocide and crimes against humanity committed against Rohingya in Burma.\n##### (b) Actions described\nThe actions described in this subsection are the following:\n**(1)**\nSupport comprehensive justice and accountability for genocide and crimes against humanity committed against Rohingya, including through consultation with and participation by the Rohingya community.\n**(2)**\nSupport for the efforts of entities, including the Independent Investigative Mechanism for Myanmar, in their work to safely collect and preserve evidence of genocide and crimes against humanity committed against Rohingya, including through open-source research and by cultivating insider, defector, deserter, and survivor witnesses, and to develop the chain of evidence, for potential use in prosecutions in domestic, hybrid, and international courts.\n**(3)**\nProvide assistance, particularly financial and technical assistance, to efforts led by Rohingya to monitor and document evidence to lead, assist, or inform other investigative mechanisms and justice processes.\n**(4)**\nEncourage the development of an intergovernmental fund to support reparative justice for Rohingya victims and survivors and identify sources of funding from foreign governments and within the United States Government that have already been appropriated.\n**(5)**\nEngage with Burma\u2019s civilian leadership and any subsequent democratic leadership in Burma to officially acknowledge genocide and crimes against humanity committed by members of the Burma military, restore Rohingya\u2019s citizenship and equal rights in Burma, and ensure compensation by the Government of Burma and restitution for their land and property, and by providing support, including technical and financial assistance, for efforts to memorialize genocide and crimes against humanity in Burma, particularly those efforts led by the affected communities.\n**(6)**\nProvide support for institutional reform and other guarantees of nonrecurrence by civilian leadership in Burma, including the security sector, legislature, and education system, and the inclusion and equal participation of Rohingya in all areas of administration and governance, under an eventual Federal democratic system.\n**(7)**\nUse convening authority to directly bring together various ethnic groups and other related stakeholders in Burma to promote truth, justice, nonrecurrence, and reconciliation, to support facilitation of related efforts by civilian leadership in Burma, and to provide both technical and financial support to entities, especially the civil society of Burma, to implement work aimed at strengthening rule of law and initiatives aimed at atrocity prevention.\n#### 9. Report\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in consultation with the Special Representative (if so designated under section 5(a)), shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\na description of and an assessment of the effectiveness of the efforts of the United States Government, during the year prior to the submission of such report, to\u2014\n**(A)**\nidentify and respond to atrocity risk factors that concern Rohingya;\n**(B)**\ndeter future atrocities against Rohingya and other Burmese ethnic minorities;\n**(C)**\nrespond to the need for humanitarian assistance for and protection of Rohingya and other Burmese ethnic minorities;\n**(D)**\ndocument the nature of and responsibility for atrocity crimes committed against Rohingya and other Burmese ethnic minorities; and\n**(E)**\npromote justice and accountability for atrocity crimes committed against Rohingya and other Burmese ethnic minorities;\n**(2)**\na detailed description of the actions taken pursuant to sections 6, 7, and 8;\n**(3)**\nan assessment of the effect of the actions described in paragraph (2) on the advancement of the policies described in section 3;\n**(4)**\na list of activities and programs initiated pursuant to this Act;\n**(5)**\nthe number of Rohingya refugees resettled in the United States in the year preceding the submission of such report, segmented by the country from which such refugees were resettled;\n**(6)**\nthe number of Rohingya refugees resettled in countries other than the United States in the year preceding the submission of such report;\n**(7)**\na description of any new challenges facing Rohingya in Burma or in refugee camps in the year preceding the submission of such report, including an assessment of early warning indicators and risk factors for atrocities; and\n**(8)**\na list of recommendations to facilitate the implementation of this Act and advance the policies described in section 3, which may include recommended\u2014\n**(A)**\nlegislative action;\n**(B)**\nadministrative action; and\n**(C)**\nprovision of additional resources.\n##### (b) Report form\n**(1) Classification**\nThe report required under subsection (a) shall be submitted in unclassified form and may contain a classified annex.\n**(2) Public availability of information**\nNot later than 45 days after the date on which the appropriate congressional committees received such report, the unclassified portion of such report shall be made publicly available on the website of the Department of State.\n#### 10. Authorization of appropriations\n##### (a) General authorizations\nFor each of fiscal years 2026 through 2030, there are authorized to be appropriated, from amounts made available to carry out the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ), such sums as may be necessary to carry out sections 6, 7, and 8 of this Act.\n##### (b) Specific authorizations of appropriations\nFor each of fiscal years 2026 through 2030, there are authorized to be appropriated\u2014\n**(1)**\n$5,000,000 for the Department of State to support atrocity crime investigations, documentation, and casework, transitional justice and accountability mechanisms, witness protection measures, and technical support related to Rohingya and other Burmese ethnic minorities; and\n**(2)**\n$4,000,000 to support programs that capture, analyze, and make widely available evidence of the ongoing atrocities against the people of Burma through the documentation, verification, and dissemination of open-source evidence.\n#### 11. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Foreign Relations of the Senate.\n**(2) Genocide**\nThe term genocide means any offense described in section 1091(a) of title 18, United States Code.\n**(3) Special representative**\nThe term Special Representative means the United States Special Representative and Policy Coordinator for Burma designated by the President pursuant to section 5(a).\n**(4) Burma military junta**\nThe term Burma military junta means the State Administrative Council of Burma or any successor to such entity.",
      "versionDate": "2025-06-25",
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
            "name": "Asia",
            "updateDate": "2025-08-19T13:49:25Z"
          },
          {
            "name": "Bangladesh",
            "updateDate": "2025-08-19T13:49:33Z"
          },
          {
            "name": "Burma",
            "updateDate": "2025-08-19T13:50:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-19T13:51:39Z"
          },
          {
            "name": "Department of State",
            "updateDate": "2025-08-19T13:51:47Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-08-19T13:51:53Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-08-19T13:52:01Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-08-19T13:52:10Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-08-19T13:52:18Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-08-19T13:52:25Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-08-19T13:52:31Z"
          },
          {
            "name": "Lawyers and legal services",
            "updateDate": "2025-08-19T13:52:37Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-08-19T13:53:22Z"
          },
          {
            "name": "Racial and ethnic relations",
            "updateDate": "2025-08-19T13:52:42Z"
          },
          {
            "name": "Refugees, asylum, displaced persons",
            "updateDate": "2025-08-19T13:52:52Z"
          },
          {
            "name": "South Asia",
            "updateDate": "2025-08-19T13:50:28Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2025-08-19T13:53:16Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:25:09Z"
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
      "date": "2025-06-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4140ih.xml"
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
      "title": "Burma GAP Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-30T12:52:02Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Burma GAP Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Burma Genocide Accountability and Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T02:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide protection, support, and humanitarian assistance to Rohingya refugees and internally displaced people in Burma as well as promote accountability and a path out of genocide and crimes against humanity for Rohingya.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T02:48:20Z"
    }
  ]
}
```
