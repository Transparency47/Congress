# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1883?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1883
- Title: DISRUPT Act
- Congress: 119
- Bill type: S
- Bill number: 1883
- Origin chamber: Senate
- Introduced date: 2025-05-22
- Update date: 2026-04-06T18:11:28Z
- Update date including text: 2026-04-06T18:11:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-22: Introduced in Senate
- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 99.
- Latest action: 2025-05-22: Introduced in Senate

## Actions

- 2025-05-22 - IntroReferral: Introduced in Senate
- 2025-05-22 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 99.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-22",
    "latestAction": {
      "actionDate": "2025-05-22",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1883",
    "number": "1883",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001088",
        "district": "",
        "firstName": "Christopher",
        "fullName": "Sen. Coons, Christopher A. [D-DE]",
        "lastName": "Coons",
        "party": "D",
        "state": "DE"
      }
    ],
    "title": "DISRUPT Act",
    "type": "S",
    "updateDate": "2026-04-06T18:11:28Z",
    "updateDateIncludingText": "2026-04-06T18:11:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-18",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 99.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-18",
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
      "actionDate": "2025-06-05",
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
      "actionDate": "2025-05-22",
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
      "actionDate": "2025-05-22",
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
            "date": "2025-06-18T18:27:09Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:12Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-22T17:37:24Z",
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
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-05-22",
      "state": "PA"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "False",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-09",
      "state": "MN"
    },
    {
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "False",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "TX"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "False",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-06-09",
      "state": "AK"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
      "state": "CO"
    },
    {
      "bioguideId": "M001190",
      "firstName": "Markwayne",
      "fullName": "Sen. Mullin, Markwayne [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "OK"
    },
    {
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "False",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-06-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1883is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1883\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Coons (for himself and Mr. McCormick ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the executive branch to develop a whole-of-government strategy to disrupt growing cooperation among the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, which are the foremost adversaries of the United States, and mitigate the risks posed to the United States.\n#### 1. Short title\nThis Act may be cited as the Defending International Security by Restricting Unacceptable Partnerships and Tactics Act or DISRUPT Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea are each considered\u2014\n**(A)**\na foreign adversary (as defined in section 825(d) of the National Defense Authorization Act for Fiscal Year 2024 ( Public Law 118\u201331 ; 137 Stat. 322; 46 U.S.C. 50309 note));\n**(B)**\na country of risk (as defined in section 6432(a) of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ; 138 Stat. 2488; 42 U.S.C. 7144b note)) for purposes of assessing counterintelligence risks posed by certain visitors to National Laboratories;\n**(C)**\na foreign country of concern (as defined in section 10612(a) of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 136 Stat. 1635; 42 U.S.C. 19221 note));\n**(D)**\na covered foreign country (as defined in section 164 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ; 138 Stat. 1818; 10 U.S.C. 4651 note prec.)) for purposes of a prohibition on operation, procurement, and contracting relating to foreign-made light detection and ranging technology; and\n**(E)**\na covered foreign country (as defined in section 1622 of the National Defense Authorization Act for Fiscal Year 2022 ( Public Law 117\u201381 ; 135 Stat. 2086; 10 U.S.C. 421 note prec.)) for purposes of a strategy and plan to implement certain defense intelligence reforms.\n**(2)**\nAccording to the 2025 Intelligence Community Annual Threat Assessment, the United States faces an increasingly contested and dangerous global landscape as the four adversaries named in paragraph (1) deepen cooperation in a manner that\u2014\n**(A)**\nreinforces threats posed by each such adversary individually; and\n**(B)**\nposes new challenges to the strength and power of the United States globally.\n**(3)**\nMuch of the cooperation referred to in paragraph (3) is occurring bilaterally, as the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea strengthen diplomatic, economic, and military ties in accordance with bilateral agreements, which include\u2014\n**(A)**\nthe Treaty on Friendship, Cooperation and Mutual Assistance between China and the Democratic People\u2019s Republic of Korea, signed at Beijing July 11, 1961;\n**(B)**\nthe Joint Statement on Comprehensive Strategic Partnership between the Islamic Republic of Iran and the People's Republic of China, issued on March 27, 2021;\n**(C)**\nthe Joint Statement of the Russian Federation and the People's Republic of China on International Relations Entering a New Era and Global Sustainable Development, issued on February 4, 2022;\n**(D)**\nthe Treaty on Comprehensive Strategic Partnership between the Russian Federation and the Democratic People\u2019s Republic of Korea, signed at Pyongyang June 18, 2024;\n**(E)**\nthe Iranian-Russian Treaty on Comprehensive Strategic Partnership, signed at Moscow January 17, 2025; and\n**(F)**\ntraditional relations of friendship and cooperation between the Islamic Republic of Iran and the Democratic People\u2019s Republic of Korea.\n**(4)**\nThe most concerning forms of such cooperation with respect to the interests of the United States occur bilaterally in the realm of defense cooperation. Examples include the following:\n**(A)**\nThe transfer and sharing of weapons and munitions. Since 2022, the Islamic Republic of Iran has supplied the Russian Federation with drones and ballistic missiles, and the Democratic People\u2019s Republic of Korea has provided artillery ammunition and ballistic missiles. Likewise, the Russian Federation has agreed to provide the Islamic Republic of Iran with Su\u201335 fighter jets and air defense assistance.\n**(B)**\nThe transfer and sharing of dual-use technologies and capabilities. Dual-use goods supplied by the People\u2019s Republic of China have enabled the Russian Federation to continue defense production in the face of wide-ranging sanctions and export controls intended to prevent the Russian Federation from accessing the necessary components to fuel its defense industry. In turn, reporting indicates that the Russian Federation has provided technical expertise on satellite technology to the Democratic People\u2019s Republic of Korea and is working closely with the People\u2019s Republic of China on air defense and submarine technology.\n**(C)**\nJoint military activities and exercises. The military forces of the Democratic People\u2019s Republic of Korea are actively participating in the Russian Federation's invasion of Ukraine, and joint military exercises between the People\u2019s Republic of China and the Russian Federation are expanding in scope, scale, and geographic reach, including in close proximity to territory of the United States.\n**(D)**\nCoordination on disinformation and cyber operations, including coordinated messaging aimed at denigrating and isolating the United States internationally.\n**(5)**\nAdversaries of the United States are also cooperating in a manner that may circumvent United States and multilateral economic tools. Examples include the following:\n**(A)**\nThe continued purchase by the People\u2019s Republic of China of oil from the Islamic Republic of Iran despite sanctions imposed by the Treasury of the United States on oil from the Islamic Republic of Iran.\n**(B)**\nThe veto by the Russian Federation of, and abstention by the People\u2019s Republic of China in a vote on, a United Nations Security Council resolution relating to monitoring United Nations Security Council-levied sanctions on the Democratic People\u2019s Republic of Korea.\n**(6)**\nAdversaries of the United States are cooperating multilaterally in international institutions such as the United Nations and through expanded multilateral groupings, such as the Brazil-Russia-India-China-South Africa group (commonly known as BRICS ), to isolate and erode the influence of the United States.\n**(7)**\nSuch increased cooperation and alignment among the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, to an unprecedented extent, poses a significant threat to United States interests and national security.\n**(8)**\nSuch increasing alignment\u2014\n**(A)**\nallows each such adversary to modernize its military more quickly than previously anticipated;\n**(B)**\nenables unforeseen breakthroughs in capabilities through the sharing among such adversaries of critical military technologies, which could erode the technological edge of the United States Armed Forces;\n**(C)**\npresents increasing challenges to strategies of isolation or containment against such individual adversaries, since the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea now provide critical lifelines to each other;\n**(D)**\nthreatens the effectiveness of United States economic tools, as such adversaries cooperate to evade United States sanctions and export controls and seek to establish alternative payment mechanisms that do not require transactions in United States dollars; and\n**(E)**\nincreases the chances of United States conflict or tensions with any one of such adversaries drawing in another, thereby posing a greater risk that the United States will have to contend with simultaneous threats from such adversaries in one or more theaters.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto disrupt or frustrate the most dangerous aspects of cooperation between and among the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, including by using the threat of sanctions and export controls, bringing such cooperation to light, and sharing information with United States allies and partners who may\u2014\n**(A)**\nshare the concerns and objectives of the United States; and\n**(B)**\nhave influence over such adversaries;\n**(2)**\nto constrain such grouping from expanding its footprint or capabilities across the world; and\n**(3)**\nto prepare for the increasing likelihood that the United States could face simultaneous challenges or conflict with multiple such adversaries in multiple theaters, including by bolstering deterrence across all priority theaters.\n#### 4. Task forces and reports\n##### (a) Task forces on adversary alignment\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of State, the Secretary of Defense, the Secretary of the Treasury, the Secretary of Commerce, the Director of National Intelligence, and the Director of the Central Intelligence Agency shall each\u2014\n**(A)**\nestablish a task force on adversary alignment; and\n**(B)**\ndesignate a point of contact on adversary alignment, who shall serve as the head of the task force for the applicable department, office, or agency.\n**(2) Requirements**\nEach task force established pursuant to paragraph (1) shall\u2014\n**(A)**\ncomprise\u2014\n**(i)**\nsubject matter experts covering each of\u2014\n**(I)**\nthe People's Republic of China;\n**(II)**\nthe Russian Federation;\n**(III)**\nthe Islamic Republic of Iran; and\n**(IV)**\nthe Democratic People\u2019s Republic of Korea;\n**(ii)**\nrepresentatives covering all core functions of the department, office, or agency of the Secretary or Director establishing the task force; and\n**(iii)**\na mix of analysts, operators, and senior management;\n**(B)**\nensure that the task force members have the requisite security clearances and access to critical compartmented information streams necessary to assess and understand the full scope of adversary cooperation, including how events in one theater might trigger actions in another; and\n**(C)**\nnot later than 180 days after the date of the enactment of this Act, submit to the Secretary or Director who established the task force, and to the appropriate committees of Congress, a report\u2014\n**(i)**\nevaluating the impact of adversary alignment on the relevant operations carried out by the individual department, office, or agency of the task force; and\n**(ii)**\nputting forth recommendations for such organizational changes as the task force considers necessary to ensure the department, office, or agency of the task force is well positioned to routinely evaluate and respond to the rapidly evolving nature of adversary cooperation and the attendant risks.\n**(3) Quarterly interagency meeting**\nNot less frequently than quarterly, the heads of the task forces established under this section shall meet to discuss findings, problems, and next steps with respect to adversary alignment.\n##### (b) Report on nature, trajectory, and risks of bilateral cooperation between, and multilateral cooperation among, adversaries of the United States\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Director of National Intelligence, in coordination with the head of any Federal agency the Director considers appropriate, shall submit to the President, any Federal officer of Cabinet-level rank the Director considers appropriate, and the appropriate committees of Congress, a report on bilateral and multilateral cooperation among adversaries of the United States and the resulting risks of such cooperation.\n**(2) Elements**\nThe report required by paragraph (1) shall include the following:\n**(A)**\nA description of the current nature and extent of bilateral or multilateral cooperation among the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea across the diplomatic, information, military, and economic spheres, and an assessment of the advantages that accrue to each such adversary from such cooperation.\n**(B)**\nAn assessment of the trajectory for cooperation among the adversaries described in subparagraph (A) during the 5-year period beginning on the date on which the report is submitted.\n**(C)**\nAn outline of the risks to the United States and allied diplomatic, military, intelligence, and economic operations, and broader security interests around the world, including the following:\n**(i)**\nThe risk of technology transfer dramatically increasing the military capabilities of adversaries of the United States and its impact on the relative balance of United States and allied capabilities as compared to that of the adversary.\n**(ii)**\nThe risk posed to the United States by efforts made by adversaries to establish alternate payment systems, in particular with respect to the dominance of the United States dollar and the effectiveness of United States sanctions and export control tools.\n**(iii)**\nThe risk that an adversary of the United States might assist or otherwise enable another adversary of the United States in the event that one or more adversaries become party to a conflict with the United States.\n**(iv)**\nThe risk that adversary cooperation poses a growing threat to United States intelligence collection efforts.\n**(D)**\nAn evaluation of the vulnerabilities and tension points within such adversary bilateral or multilateral relationships , and an assessment of the likely effect of efforts by the United States to separate adversaries.\n**(3) Form**\nThe report submitted pursuant to paragraph (1) shall be submitted in classified form.\n##### (c) Report on strategic approach\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Secretary of Defense, in consultation with the Secretary of the Treasury, the Secretary of Commerce, the Director of National Intelligence, and the Director of the Central Intelligence Agency, shall submit to the appropriate committees of Congress a report outlining the strategic approach of the United States to adversary alignment and the necessary steps to disrupt, frustrate, constrain, and prepare for adversary cooperation during the two-year period beginning on the date of the enactment of this Act.\n**(2) Elements**\nThe report required by paragraph (1) shall include the following:\n**(A)**\nA detailed description of the methods and tools available to the United States to disrupt the most dangerous elements of adversary cooperation, including the growing connectivity between the defense industrial bases of each adversary.\n**(B)**\nA timeline for using diplomatic engagement and intelligence diplomacy\u2014\n**(i)**\nto educate allies and partners about the increasing risk of adversary alignment; and\n**(ii)**\nto secure the support of allies and partners in combating adversary alignment.\n**(C)**\nA plan for ensuring the integrity of United States methods of economic statecraft, including an assessment of the efficiency of the United States sanctions and export control enforcement apparatus and any accompanying resourcing requirements.\n**(D)**\nA clear plan to bolster deterrence within the priority theaters of the Indo-Pacific region, Europe, and the Middle East by\u2014\n**(i)**\nincreasing United States and allied munitions stockpiles, particularly such stockpiles that are most critical for supporting frontline partners such as Israel, Taiwan, and Ukraine in the event of aggression by a United States adversary;\n**(ii)**\nfacilitating collaborative efforts with allies for the co-production, co-maintenance, and co-sustainment of critical munitions and platforms required by the United States and allies and partners of the United States in the event of a future conflict with the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, or the Democratic People\u2019s Republic of Korea; and\n**(iii)**\nmore effectively using funding through the United States Foreign Military Financing program to support allied and partner domestic defense production that can contribute to deterrence in each such priority theater.\n**(E)**\nA plan for digitizing and updating war-planning tools of the Department of Defense not later than 1 year after the date on which the report is submitted to ensure that United States war planners are better equipped to update and modify war plans in the face of rapidly evolving information on adversary cooperation.\n**(F)**\nAn assessment of the capability gaps and vulnerabilities the United States would face in deterring an adversary in the event that the United States is engaged in a conflict with another adversary, and a plan to work with allies and partners to address such gaps and vulnerabilities.\n**(3) Form**\nThe report required by paragraph (1) shall be submitted in classified form.\n##### (d) Appropriate committees of congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Armed Services, the Select Committee on Intelligence, the Committee on Foreign Relations, the Committee on Appropriations, the Committee on Banking, Housing, and Urban Affairs, and the Committee on Commerce, Science, and Transportation of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Permanent Select Committee on Intelligence, the Committee on Foreign Affairs, the Committee on Appropriations, the Committee on Financial Services, and the Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2025-05-22",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1883rs.xml",
      "text": "II\nCalendar No. 99\n119th CONGRESS\n1st Session\nS. 1883\nIN THE SENATE OF THE UNITED STATES\nMay 22, 2025 Mr. Coons (for himself, Mr. McCormick , Ms. Klobuchar , Mr. Cornyn , Mr. Sullivan , Mr. Bennet , Mr. Mullin , and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the executive branch to develop a whole-of-government strategy to disrupt growing cooperation among the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, which are the foremost adversaries of the United States, and mitigate the risks posed to the United States.\n#### 1. Short title\nThis Act may be cited as the Defending International Security by Restricting Unacceptable Partnerships and Tactics Act or DISRUPT Act .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nThe People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea are each considered\u2014\n**(A)**\na foreign adversary (as defined in section 825(d) of the National Defense Authorization Act for Fiscal Year 2024 ( Public Law 118\u201331 ; 137 Stat. 322; 46 U.S.C. 50309 note));\n**(B)**\na country of risk (as defined in section 6432(a) of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ; 138 Stat. 2488; 42 U.S.C. 7144b note)) for purposes of assessing counterintelligence risks posed by certain visitors to National Laboratories;\n**(C)**\na foreign country of concern (as defined in section 10612(a) of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; 136 Stat. 1635; 42 U.S.C. 19221 note));\n**(D)**\na covered foreign country (as defined in section 164 of the Servicemember Quality of Life Improvement and National Defense Authorization Act for Fiscal Year 2025 ( Public Law 118\u2013159 ; 138 Stat. 1818; 10 U.S.C. 4651 note prec.)) for purposes of a prohibition on operation, procurement, and contracting relating to foreign-made light detection and ranging technology; and\n**(E)**\na covered foreign country (as defined in section 1622 of the National Defense Authorization Act for Fiscal Year 2022 ( Public Law 117\u201381 ; 135 Stat. 2086; 10 U.S.C. 421 note prec.)) for purposes of a strategy and plan to implement certain defense intelligence reforms.\n**(2)**\nAccording to the 2025 Intelligence Community Annual Threat Assessment, the United States faces an increasingly contested and dangerous global landscape as the four adversaries named in paragraph (1) deepen cooperation in a manner that\u2014\n**(A)**\nreinforces threats posed by each such adversary individually; and\n**(B)**\nposes new challenges to the strength and power of the United States globally.\n**(3)**\nMuch of the cooperation referred to in paragraph (3) is occurring bilaterally, as the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea strengthen diplomatic, economic, and military ties in accordance with bilateral agreements, which include\u2014\n**(A)**\nthe Treaty on Friendship, Cooperation and Mutual Assistance between China and the Democratic People\u2019s Republic of Korea, signed at Beijing July 11, 1961;\n**(B)**\nthe Joint Statement on Comprehensive Strategic Partnership between the Islamic Republic of Iran and the People's Republic of China, issued on March 27, 2021;\n**(C)**\nthe Joint Statement of the Russian Federation and the People's Republic of China on International Relations Entering a New Era and Global Sustainable Development, issued on February 4, 2022;\n**(D)**\nthe Treaty on Comprehensive Strategic Partnership between the Russian Federation and the Democratic People\u2019s Republic of Korea, signed at Pyongyang June 18, 2024;\n**(E)**\nthe Iranian-Russian Treaty on Comprehensive Strategic Partnership, signed at Moscow January 17, 2025; and\n**(F)**\ntraditional relations of friendship and cooperation between the Islamic Republic of Iran and the Democratic People\u2019s Republic of Korea.\n**(4)**\nThe most concerning forms of such cooperation with respect to the interests of the United States occur bilaterally in the realm of defense cooperation. Examples include the following:\n**(A)**\nThe transfer and sharing of weapons and munitions. Since 2022, the Islamic Republic of Iran has supplied the Russian Federation with drones and ballistic missiles, and the Democratic People\u2019s Republic of Korea has provided artillery ammunition and ballistic missiles. Likewise, the Russian Federation has agreed to provide the Islamic Republic of Iran with Su\u201335 fighter jets and air defense assistance.\n**(B)**\nThe transfer and sharing of dual-use technologies and capabilities. Dual-use goods supplied by the People\u2019s Republic of China have enabled the Russian Federation to continue defense production in the face of wide-ranging sanctions and export controls intended to prevent the Russian Federation from accessing the necessary components to fuel its defense industry. In turn, reporting indicates that the Russian Federation has provided technical expertise on satellite technology to the Democratic People\u2019s Republic of Korea and is working closely with the People\u2019s Republic of China on air defense and submarine technology.\n**(C)**\nJoint military activities and exercises. The military forces of the Democratic People\u2019s Republic of Korea are actively participating in the Russian Federation's invasion of Ukraine, and joint military exercises between the People\u2019s Republic of China and the Russian Federation are expanding in scope, scale, and geographic reach, including in close proximity to territory of the United States.\n**(D)**\nCoordination on disinformation and cyber operations, including coordinated messaging aimed at denigrating and isolating the United States internationally.\n**(5)**\nAdversaries of the United States are also cooperating in a manner that may circumvent United States and multilateral economic tools. Examples include the following:\n**(A)**\nThe continued purchase by the People\u2019s Republic of China of oil from the Islamic Republic of Iran despite sanctions imposed by the Treasury of the United States on oil from the Islamic Republic of Iran.\n**(B)**\nThe veto by the Russian Federation of, and abstention by the People\u2019s Republic of China in a vote on, a United Nations Security Council resolution relating to monitoring United Nations Security Council-levied sanctions on the Democratic People\u2019s Republic of Korea.\n**(6)**\nAdversaries of the United States are cooperating multilaterally in international institutions such as the United Nations and through expanded multilateral groupings, such as the Brazil-Russia-India-China-South Africa group (commonly known as BRICS ), to isolate and erode the influence of the United States.\n**(7)**\nSuch increased cooperation and alignment among the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, to an unprecedented extent, poses a significant threat to United States interests and national security.\n**(8)**\nSuch increasing alignment\u2014\n**(A)**\nallows each such adversary to modernize its military more quickly than previously anticipated;\n**(B)**\nenables unforeseen breakthroughs in capabilities through the sharing among such adversaries of critical military technologies, which could erode the technological edge of the United States Armed Forces;\n**(C)**\npresents increasing challenges to strategies of isolation or containment against such individual adversaries, since the People\u2019s Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea now provide critical lifelines to each other;\n**(D)**\nthreatens the effectiveness of United States economic tools, as such adversaries cooperate to evade United States sanctions and export controls and seek to establish alternative payment mechanisms that do not require transactions in United States dollars; and\n**(E)**\nincreases the chances of United States conflict or tensions with any one of such adversaries drawing in another, thereby posing a greater risk that the United States will have to contend with simultaneous threats from such adversaries in one or more theaters.\n#### 3. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto disrupt or frustrate the most dangerous aspects of cooperation between and among the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea, including by using the threat of sanctions and export controls, bringing such cooperation to light, and sharing information with United States allies and partners who may\u2014\n**(A)**\nshare the concerns and objectives of the United States; and\n**(B)**\nhave influence over such adversaries;\n**(2)**\nto constrain such grouping from expanding its footprint or capabilities across the world; and\n**(3)**\nto prepare for the increasing likelihood that the United States could face simultaneous challenges or conflict with multiple such adversaries in multiple theaters, including by bolstering deterrence across all priority theaters.\n#### 4. Task forces and reports\n##### (a) Task forces on adversary alignment\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Secretary of State, the Secretary of Defense, the Secretary of the Treasury, the Secretary of Commerce, the Director of National Intelligence, and the Director of the Central Intelligence Agency shall each\u2014\n**(A)**\nestablish a task force on adversary alignment; and\n**(B)**\ndesignate a point of contact on adversary alignment, who shall serve as the head of the task force for the applicable department, office, or agency.\n**(2) Requirements**\nEach task force established pursuant to paragraph (1) shall\u2014\n**(A)**\ncomprise\u2014\n**(i)**\nsubject matter experts covering each of\u2014\n**(I)**\nthe People's Republic of China;\n**(II)**\nthe Russian Federation;\n**(III)**\nthe Islamic Republic of Iran; and\n**(IV)**\nthe Democratic People\u2019s Republic of Korea;\n**(ii)**\nrepresentatives covering all core functions of the department, office, or agency of the Secretary or Director establishing the task force; and\n**(iii)**\na mix of analysts, operators, and senior management;\n**(B)**\nensure that the task force members have the requisite security clearances and access to critical compartmented information streams necessary to assess and understand the full scope of adversary cooperation, including how events in one theater might trigger actions in another; and\n**(C)**\nnot later than 180 days after the date of the enactment of this Act, submit to the Secretary or Director who established the task force, and to the appropriate committees of Congress, a report\u2014\n**(i)**\nevaluating the impact of adversary alignment on the relevant operations carried out by the individual department, office, or agency of the task force; and\n**(ii)**\nputting forth recommendations for such organizational changes as the task force considers necessary to ensure the department, office, or agency of the task force is well positioned to routinely evaluate and respond to the rapidly evolving nature of adversary cooperation and the attendant risks.\n**(3) Quarterly interagency meeting**\nNot less frequently than quarterly, the heads of the task forces established under this section shall meet to discuss findings, problems, and next steps with respect to adversary alignment.\n##### (b) Report on nature, trajectory, and risks of bilateral cooperation between, and multilateral cooperation among, adversaries of the United States\n**(1) In general**\nNot later than 60 days after the date of the enactment of this Act, the Director of National Intelligence, in coordination with the head of any Federal agency the Director considers appropriate, shall submit to the President, any Federal officer of Cabinet-level rank the Director considers appropriate, and the appropriate committees of Congress, a report on bilateral and multilateral cooperation among adversaries of the United States and the resulting risks of such cooperation.\n**(2) Elements**\nThe report required by paragraph (1) shall include the following:\n**(A)**\nA description of the current nature and extent of bilateral or multilateral cooperation among the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People\u2019s Republic of Korea across the diplomatic, information, military, and economic spheres, and an assessment of the advantages that accrue to each such adversary from such cooperation.\n**(B)**\nAn assessment of the trajectory for cooperation among the adversaries described in subparagraph (A) during the 5-year period beginning on the date on which the report is submitted.\n**(C)**\nAn outline of the risks to the United States and allied diplomatic, military, intelligence, and economic operations, and broader security interests around the world, including the following:\n**(i)**\nThe risk of technology transfer dramatically increasing the military capabilities of adversaries of the United States and its impact on the relative balance of United States and allied capabilities as compared to that of the adversary.\n**(ii)**\nThe risk posed to the United States by efforts made by adversaries to establish alternate payment systems, in particular with respect to the dominance of the United States dollar and the effectiveness of United States sanctions and export control tools.\n**(iii)**\nThe risk that an adversary of the United States might assist or otherwise enable another adversary of the United States in the event that one or more adversaries become party to a conflict with the United States.\n**(iv)**\nThe risk that adversary cooperation poses a growing threat to United States intelligence collection efforts.\n**(D)**\nAn evaluation of the vulnerabilities and tension points within such adversary bilateral or multilateral relationships , and an assessment of the likely effect of efforts by the United States to separate adversaries.\n**(3) Form**\nThe report submitted pursuant to paragraph (1) shall be submitted in classified form.\n##### (c) Report on strategic approach\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State and the Secretary of Defense, in consultation with the Secretary of the Treasury, the Secretary of Commerce, the Director of National Intelligence, and the Director of the Central Intelligence Agency, shall submit to the appropriate committees of Congress a report outlining the strategic approach of the United States to adversary alignment and the necessary steps to disrupt, frustrate, constrain, and prepare for adversary cooperation during the two-year period beginning on the date of the enactment of this Act.\n**(2) Elements**\nThe report required by paragraph (1) shall include the following:\n**(A)**\nA detailed description of the methods and tools available to the United States to disrupt the most dangerous elements of adversary cooperation, including the growing connectivity between the defense industrial bases of each adversary.\n**(B)**\nA timeline for using diplomatic engagement and intelligence diplomacy\u2014\n**(i)**\nto educate allies and partners about the increasing risk of adversary alignment; and\n**(ii)**\nto secure the support of allies and partners in combating adversary alignment.\n**(C)**\nA plan for ensuring the integrity of United States methods of economic statecraft, including an assessment of the efficiency of the United States sanctions and export control enforcement apparatus and any accompanying resourcing requirements.\n**(D)**\nA clear plan to bolster deterrence within the priority theaters of the Indo-Pacific region, Europe, and the Middle East by\u2014\n**(i)**\nincreasing United States and allied munitions stockpiles, particularly such stockpiles that are most critical for supporting frontline partners such as Israel, Taiwan, and Ukraine in the event of aggression by a United States adversary;\n**(ii)**\nfacilitating collaborative efforts with allies for the co-production, co-maintenance, and co-sustainment of critical munitions and platforms required by the United States and allies and partners of the United States in the event of a future conflict with the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, or the Democratic People\u2019s Republic of Korea; and\n**(iii)**\nmore effectively using funding through the United States Foreign Military Financing program to support allied and partner domestic defense production that can contribute to deterrence in each such priority theater.\n**(E)**\nA plan for digitizing and updating war-planning tools of the Department of Defense not later than 1 year after the date on which the report is submitted to ensure that United States war planners are better equipped to update and modify war plans in the face of rapidly evolving information on adversary cooperation.\n**(F)**\nAn assessment of the capability gaps and vulnerabilities the United States would face in deterring an adversary in the event that the United States is engaged in a conflict with another adversary, and a plan to work with allies and partners to address such gaps and vulnerabilities.\n**(3) Form**\nThe report required by paragraph (1) shall be submitted in classified form.\n##### (d) Appropriate committees of congress defined\nIn this section, the term appropriate committees of Congress means\u2014\n**(1)**\nthe Committee on Armed Services, the Select Committee on Intelligence, the Committee on Foreign Relations, the Committee on Appropriations, the Committee on Banking, Housing, and Urban Affairs, and the Committee on Commerce, Science, and Transportation of the Senate; and\n**(2)**\nthe Committee on Armed Services, the Permanent Select Committee on Intelligence, the Committee on Foreign Affairs, the Committee on Appropriations, the Committee on Financial Services, and the Committee on Energy and Commerce of the House of Representatives.",
      "versionDate": "2025-06-18",
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
        "actionDate": "2025-11-04",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Armed Services, and Intelligence (Permanent Select), for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "5912",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "DISRUPT Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2025-06-24T17:44:00Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-24T17:42:45Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-24T17:43:04Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-24T17:44:17Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-06-24T17:44:25Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-06-24T17:42:38Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-24T17:44:10Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-06-24T17:42:53Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-06-24T17:43:36Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2025-06-24T17:44:35Z"
          },
          {
            "name": "North Korea",
            "updateDate": "2025-06-24T17:42:31Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-06-24T17:42:19Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-06-24T17:43:46Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-06-24T17:43:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-20T13:31:41Z"
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
      "date": "2025-05-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1883is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1883rs.xml"
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
      "title": "DISRUPT Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Defending International Security by Restricting Unacceptable Partnerships and Tactics Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "title": "DISRUPT Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "DISRUPT Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Defending International Security by Restricting Unacceptable Partnerships and Tactics Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:23:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the executive branch to develop a whole-of-government strategy to disrupt growing cooperation among the People's Republic of China, the Russian Federation, the Islamic Republic of Iran, and the Democratic People's Republic of Korea, which are the foremost adversaries of the United States, and mitigate the risks posed to the United States.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:18:16Z"
    }
  ]
}
```
