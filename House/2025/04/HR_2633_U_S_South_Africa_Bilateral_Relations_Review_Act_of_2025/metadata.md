# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2633?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2633
- Title: U.S.-South Africa Bilateral Relations Review Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2633
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2025-10-09T08:05:45Z
- Update date including text: 2025-10-09T08:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 13.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-03 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-07-22 - Committee: Committee Consideration and Mark-up Session Held
- 2025-07-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 13.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2633",
    "number": "2633",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "U.S.-South Africa Bilateral Relations Review Act of 2025",
    "type": "HR",
    "updateDate": "2025-10-09T08:05:45Z",
    "updateDateIncludingText": "2025-10-09T08:05:45Z"
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 34 - 13.",
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
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
            "date": "2025-07-22T15:42:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-03T15:01:50Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-03T15:02:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "J000307",
      "district": "10",
      "firstName": "John",
      "fullName": "Rep. James, John [R-MI-10]",
      "isOriginalCosponsor": "True",
      "lastName": "James",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "MI"
    },
    {
      "bioguideId": "N000026",
      "district": "22",
      "firstName": "Troy",
      "fullName": "Rep. Nehls, Troy E. [R-TX-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Nehls",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "TX"
    },
    {
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "IN"
    },
    {
      "bioguideId": "S001214",
      "district": "17",
      "firstName": "W.",
      "fullName": "Rep. Steube, W. Gregory [R-FL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Steube",
      "middleName": "Gregory",
      "party": "R",
      "sponsorshipDate": "2025-07-02",
      "state": "FL"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2633ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2633\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Jackson of Texas (for himself and Mr. James ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on the Judiciary , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require a full review of the bilateral relationship between the United States and South Africa and identify South African government officials and ANC leaders eligible for the imposition of sanctions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the U.S.-South Africa Bilateral Relations Review Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe actions of factions within the African National Congress (ANC), the political party that since 1994 has held a governing majority and controlled South Africa\u2019s executive branch, are inconsistent with the South African Government\u2019s publicly stated policy of nonalignment in international affairs.\n**(2)**\nThe South African Government has a history of siding with malign actors, including Hamas, a United States designated Foreign Terrorist Organization and a proxy of the Iranian regime, and continues to pursue closer ties with the People\u2019s Republic of China (PRC) and the Russian Federation.\n**(3)**\nThe South African Government\u2019s support of Hamas dates back to 1994, when the ANC first came into power, taking a hardline stance of consistently accusing Israel of practicing apartheid.\n**(4)**\nFollowing the unprovoked and unprecedented horrendous attack by Hamas on Israel on October 7, 2023, where Hamas terrorists killed and kidnapped hundreds of Israelis, members of the South African Government and leaders of the ANC have delivered a variety of antisemitic and anti-Israel-related statements and actions, including\u2014\n**(A)**\non October 7, 2023, South Africa\u2019s Foreign Ministry released a statement expressing concern of escalating violence , urging Israel\u2019s restraint in response, and implicitly blaming Israel for provoking the attack through continued illegal occupation of Palestine land, continued settlement expansion, desecration of the Al Aqsa Mosque and Christian holy sites, and ongoing oppression of the Palestinian people ;\n**(B)**\non October 8, 2023, the ANC\u2019s national spokesperson, Mahlengi Bhengu-Motsiri, said of the devastating Hamas attack, the decision by Palestinians to respond to the brutality of the settler Israeli apartheid regime is unsurprising ;\n**(C)**\non October 14, 2023, President Cyril Ramaphosa of South Africa, accused Israel of genocide in statements during a pro-Palestinian rally;\n**(D)**\non October 17, 2023, South African Foreign Minister Naledi Pandor accepted a call with Hamas leader Ismail Haniyeh;\n**(E)**\non October 22, 2023, South African Foreign Minister Naledi Pandor visited Tehran and met with President Raisi of the Islamic Republic of Iran, which is actively funding Hamas;\n**(F)**\non November 7, 2023, in a parliamentary address, Foreign Minister Pandor called for the International Criminal Court to issue an immediate arrest warrant charging Israeli Prime Minister Benjamin Netanyahu with violations of international criminal law;\n**(G)**\non November 17, 2023, South Africa, along with 4 other countries, submitted a joint request to the International Criminal Court for an investigation into alleged war crimes being committed in the Palestinian territories;\n**(H)**\non December 5, 2023, the ANC hosted 3 members of Hamas in Pretoria, including Khaled Qaddoumi, Hamas\u2019s representative to Iran, and Bassem Naim, a member of Hamas\u2019s political bureau in Gaza;\n**(I)**\non December 29, 2023, South Africa filed a politically motivated suit in the International Court of Justice wrongfully accusing Israel of committing genocide;\n**(J)**\nin March 2024, South African Foreign Minister Pandor was quoted saying South Africa will arrest Israeli-South Africans who are fighting in the Israeli Defense Forces upon their return home and could strip them of their South African citizenship. Minister Pandor also implicitly encouraged protests outside of the United States Embassy;\n**(K)**\non October 7, 2024, the ANC commemorated only the Palestinian lives lost to Israel, while accusing Israel of genocide;\n**(L)**\nin October 2024, South Africa filed its Memorial to the International Court of Justice, accusing Israel of genocidal actions to depopulate Gaza through mass death and displacement;\n**(M)**\nin November 2024, South Africa appointed Ebrahim Rasool as their Ambassador to the United States, who previously hosted senior Hamas officials to South Africa when he was the Premier of the Western Cape and, in 2020, was a speaker at an annual event hosted by the Iranian regime to celebrate Hezbollah\u2019s resistance against Israel; and\n**(N)**\nthe ANC\u2019s ongoing attempt to rename the street that the United States Consulate in Johannesburg is located on as Leila Khaled Drive , including a quote from ANC first Deputy Secretary General Nomvula Mokonyane saying we want the United States of America embassy to change their letterhead to Number 1 Leila Khaled Drive .\n**(5)**\nThe South African Government and the ANC have maintained close relations with the Russian Federation, which has been accused of perpetrating war crimes in Ukraine and indiscriminately undermines human rights. South Africa\u2019s robust relationship with Russia spans the military and political space, including\u2014\n**(A)**\nallowing a United States-sanctioned Russian cargo ship, the Lady R, to dock and transfer arms at a South African naval base in December 2022;\n**(B)**\nhosting offshore naval exercises, entitled Operation Mosi II , carried out jointly with the PRC and Russia, between February 17 and 27, 2023, corresponding with the 1-year anniversary of Russia\u2019s unjustified and unprovoked invasion of Ukraine;\n**(C)**\nauthorizing a United States-sanctioned Russian military cargo airplane to land at a South African Air Force Base;\n**(D)**\nreneging on its initial call for the Russian Federation to immediately withdraw its forces from Ukraine and actively seeking improved relations with Moscow since February 2022;\n**(E)**\ndispatching multiple high-level official delegations to Russia to further political, intelligence, and military cooperation;\n**(F)**\nUnited States sanctioned oligarch Viktor Vekselberg donating $826,000 to the ANC in 2022; and\n**(G)**\nthe ANC publishing an article in their newspaper, ANC Today, in October 2024 promoting Russian propaganda about the war in Ukraine.\n**(6)**\nSouth African Government interactions with the PRC Government and ANC interactions with the Chinese Communist Party (CCP), who are committing gross violations of human rights in the Xinjiang province and implement economically coercive tactics around the globe, undermine South Africa\u2019s democratic constitutional system of governance, as exemplified in\u2014\n**(A)**\nongoing ANC and CCP inter-party cooperation, especially with the fundamental incompatibility between the civil and democratic rights guaranteed in South Africa\u2019s Constitution and the CCP\u2019s routine suppression of free expression and individual rights;\n**(B)**\nallowing the private Test Flying Academy of South Africa, which the Department of Commerce added to the Entity List on June 12, 2023, to recruit former United States and NATO fighter pilots to train Chinese People\u2019s Liberation Army pilots;\n**(C)**\nSouth Africa\u2019s hosting of 6 PRC Government-backed and CCP-linked Confucius Institutes, a type of entity that a CCP official characterized as an important part of the CCP\u2019s external propaganda structure , the most of any country in Africa;\n**(D)**\nSouth African Government support for, and ANC participation in, a political training school opened in Tanzania funded by the Chinese Communist Party where it trains political members of the ruling liberation movements in 6 Southern African countries. The school instills CCP ideology into the next-generation of African leaders and attempts to export the CCP\u2019s system of party-run authoritarian governance to the African continent;\n**(E)**\ncooperation with the PRC under the PRC\u2019s global Belt and Road Initiative which, while trade and infrastructure-focused, is designed to expand PRC global economic, political, and security sector-related influence;\n**(F)**\nthe widespread presence in South Africa\u2019s media and technology sectors of PRC state linked firms that the United States has restricted due to threats to national security, including Huawei Technologies, ZTE and Hikvision, which place South African sovereignty at risk and facilitate the CCP\u2019s export of its model of digitally aided authoritarian governance underpinned by cyber controls, social monitoring, propaganda, and surveillance; and\n**(G)**\nthe South African government\u2019s clear appeasement to the CCP in demanding that Taiwan relocate its representative office out of Pretoria and downgrade its status to that of a trade office.\n**(7)**\nThe ANC-led South African Government has a history of substantially mismanaging a range of state resources and has often proven incapable of effectively delivering public services, threatening the South African people and the South African economy, as illustrated by\u2014\n**(A)**\nPresident Cyril Ramaphosa\u2019s February 9, 2023, declaration of a national state of disaster over the worsening, multi-year power crisis caused by the ANC\u2019s chronic mismanagement of the state-owned power company Eskom, resulting from endemic, high-level corruption;\n**(B)**\nthe persistence of South African state-owned railway company Transnet\u2019s insufficient capacity, which has disrupted rail operations and hindered mining companies\u2019 export of iron ore, coal, and other commodities, in part due to malfeasance and corruption by former Transnet officials;\n**(C)**\noutbreaks of cholera in 2023 and 2024, the worst in 15 years, which were due in part to the South African Government\u2019s disease prevention failures, as President Ramaphosa admitted on June 9, 2023, including a failure to provide clean water to households; and\n**(D)**\nrampant state capture, that emerged and grew during the administration of former President Jacob Zuma and has damaged South Africa\u2019s international standing and profoundly undermined the rule of law, continues to negatively impact the economic development prospects and living standards of the South African people while deeply damaging public trust in state governance.\n**(8)**\nIn November 2024, South Africa appointed Ebrahim Rasool as Ambassador to the United States. Rasool had previously made public comments describing President Trump as extreme and in March 2025, Rasool characterized President Trump as a white supremacist . Secretary of State Marco Rubio subsequently declared Rasool as persona non grata in the United States.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is in the national security interest of the United States to deter strategic political and security cooperation and information sharing with the PRC and the Russian Federation, particularly any form of cooperation that may aid or abet Russia\u2019s war of aggression on Ukraine or its international standing or influence; and\n**(2)**\nthe South African Government\u2019s foreign policy actions have long ceased to reflect its stated stance of nonalignment, and now directly favor the PRC, the Russian Federation, and Hamas, a known proxy of Iran, and thereby undermine United States national security and foreign policy interests.\n#### 4. Presidential certification of determination with respect to South Africa\n##### (a) In general\nNot later than 30 days after the date of enactment of this Act, the President, in consultation with the Secretary of State and the Secretary of Defense, shall certify to the appropriate congressional committees and release publicly an unclassified determination explicitly stating whether South Africa has engaged in activities that undermine United States national security or foreign policy interests.\n##### (b) Accompanying report\nThe certification required by subsection (a) shall be accompanied by an unclassified report submitted to the appropriate congressional committees, with a classified annex if necessary, providing the justification for the determination.\n#### 5. Full review of the bilateral relationship\n##### (a) Bilateral relationship review\nThe President, in consultation with the Secretary of State, the Secretary of Defense, the United States Trade Representative, and the heads of other Federal departments and agencies that play a substantial role in United States relations with South Africa, shall conduct a comprehensive review of the bilateral relationship between the United States and South Africa.\n##### (b) Report on findings\nNot later than 120 days after the date of enactment of this Act, the President shall submit to the appropriate congressional committees a report that includes the findings of the review required by subsection (a).\n#### 6. Report on sanctionable persons\nNot later than 120 days after the date of the enactment of this Act, the President, in consultation with the Secretary of State and the Secretary of Treasury, shall submit to the appropriate congressional committees a classified report that includes\u2014\n**(1)**\na list of senior South African government officials and ANC leaders the President determines have engaged in corruption or human rights abuses that would be sufficient, based on credible evidence, to meet the criteria for the imposition of sanctions pursuant to the authorities provided by the Global Magnitsky Human Rights Accountability Act ( 22 U.S.C. 10101 et seq. ); and\n**(2)**\nwith respect to each person identified pursuant to paragraph (1)\u2014\n**(A)**\na detailed explanation describing the conduct forming the basis of the person\u2019s inclusion on the list; and\n**(B)**\n**(i)**\nthe expected timeline for sanctions described in paragraph (1) to be imposed with respect to such person; or\n**(ii)**\nif the President does not intend to impose sanctions with respect to such person, a detailed justification describing the rationale and legal authorities underlying such negative determination.\n#### 7. Definitions\n##### (a) ANC\nThe term ANC means the African National Congress.\n##### (b) Appropriate congressional committees\nThe term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations of the Senate.\n##### (c) CCP\nThe term CCP means the Chinese Communist Party.\n##### (d) PRC\nThe term PRC means the People\u2019s Republic of China.",
      "versionDate": "2025-04-03",
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
            "name": "Africa",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Political parties and affiliation",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "South Africa",
            "updateDate": "2025-08-05T17:10:33Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-08-05T17:10:33Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-22T17:42:45Z"
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
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2633ih.xml"
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
      "title": "U.S.-South Africa Bilateral Relations Review Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-10T01:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "U.S.-South Africa Bilateral Relations Review Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-10T01:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require a full review of the bilateral relationship between the United States and South Africa and identify South African government officials and ANC leaders eligible for the imposition of sanctions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-10T01:33:23Z"
    }
  ]
}
```
