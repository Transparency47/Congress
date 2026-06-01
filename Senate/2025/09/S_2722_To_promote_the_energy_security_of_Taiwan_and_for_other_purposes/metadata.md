# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2722
- Title: Taiwan Energy Security and Anti-Embargo Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 2722
- Origin chamber: Senate
- Introduced date: 2025-09-04
- Update date: 2026-04-02T22:40:29Z
- Update date including text: 2026-04-02T22:40:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-04: Introduced in Senate
- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 325.
- Latest action: 2025-09-04: Introduced in Senate

## Actions

- 2025-09-04 - IntroReferral: Introduced in Senate
- 2025-09-04 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 325.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-04",
    "latestAction": {
      "actionDate": "2025-09-04",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2722",
    "number": "2722",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
    "type": "S",
    "updateDate": "2026-04-02T22:40:29Z",
    "updateDateIncludingText": "2026-04-02T22:40:29Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 325.",
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
      "actionDate": "2025-09-04",
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
      "actionDate": "2025-09-04",
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
            "date": "2026-02-10T16:30:30Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:06Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-04T18:04:03Z",
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
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-09-04",
      "state": "DE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-09-16",
      "state": "NC"
    },
    {
      "bioguideId": "H000273",
      "firstName": "John",
      "fullName": "Sen. Hickenlooper, John W. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Hickenlooper",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "CO"
    },
    {
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "ND"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2722is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2722\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Ricketts (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo promote the energy security of Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Energy Security and Anti-Embargo Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a vital democratic partner the energy security of which is critical to the strategic interests of the United States in the Indo-Pacific region.\n**(2)**\nEnhancing Taiwan\u2019s energy resilience through diversified and reliable sources reduces vulnerability to coercion, disruption, or attack by authoritarian regimes.\n**(3)**\nThe United States possesses abundant supplies of liquefied natural gas and other energy resources that support economic growth, job creation, and the national security interests of the United States.\n**(4)**\nPromoting United States energy exports to and partnerships with Taiwan aligns with United States energy diplomacy objectives, strengthens bilateral economic and security ties, and contributes to regional stability.\n**(5)**\nThe Alaska Liquefied Natural Gas Project, which has received pledged support from Taiwan\u2019s state energy firm CPC Corp, would enhance the ability of the United States to supply Taiwan and other allies and partners of the United States in the Indo-Pacific with a cost-effective, reliable supply of energy.\n**(6)**\nTaiwan\u2019s energy infrastructure, including electric grid systems and liquefied natural gas import facilities, is vulnerable to asymmetric and kinetic threats from the People\u2019s Republic of China.\n**(7)**\nSupporting Taiwan\u2019s efforts to improve the resilience and security of its energy infrastructure advances deterrence and promotes continuity of government operations in the event of a crisis.\n#### 3. Promotion of liquefied natural gas exports and energy infrastructure resilience for Taiwan\nThe Taiwan Enhanced Resilience Act ( 22 U.S.C. 3351 et seq. ) is amended by adding at the end the following:\n8 Promotion of liquefied natural gas exports and energy infrastructure resilience for Taiwan 5540A. Definitions In this part: (1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Foreign Relations, the Committee on Commerce, Science, and Transportation, and the Committee on Energy and Natural Resources of the Senate; and (B) the Committee on Foreign Affairs, the Committee on Energy and Commerce, and the Committee on Natural Resources of the House of Representatives. (2) Asymmetric threat The term asymmetric threat means a threat posed by unconventional means, including a cyberattack, sabotage, or economic coercion, designed to undermine or disrupt the operation of critical infrastructure. 5540B. Promotion of liquefied natural gas exports to Taiwan (a) In general The Secretary of State, in coordination with the Secretary of Commerce and the Secretary of Energy, shall prioritize efforts to support and facilitate increased exportation to Taiwan of liquefied natural gas produced in the United States. (b) Required activities In carrying out subsection (a), the Secretaries shall\u2014 (1) engage with United States liquefied natural gas producers, exporters, and infrastructure entities to identify and address barriers to liquefied natural gas exports and storage projects intended for the market of Taiwan; (2) facilitate coordination between United States private sector entities and relevant government and private sector stakeholders in Taiwan; (3) provide diplomatic and technical support to streamline regulatory processes and expedite permitting for liquefied natural gas export and storage infrastructure projects linked to Taiwan; (4) consult with the Government of Taiwan to assess and strengthen liquefied natural gas import and storage capabilities; and (5) coordinate interagency efforts to ensure cohesive and sustained United States support for liquefied natural gas exports to Taiwan. 5540C. Energy infrastructure resilience capacity building (a) Requirement Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, shall seek to engage with appropriate officials of Taiwan for the purpose of cooperating with the Ministry of Foreign Affairs, the Ministry of the Interior, the Ministry of Defense, and the head of any other applicable ministry of Taiwan for capacity building to enhance energy infrastructure resilience, including defensive military cybersecurity activities. (b) Identification of activities In carrying out subsection (a), the Secretary of State may identify cooperative activities\u2014 (1) to enhance cybersecurity programs to protect grid operating systems, liquefied natural gas terminals, and supervisory control and data acquisition systems; (2) to support physical security improvements, operational redundancy, and continuity-of-operations planning; (3) to engage in joint training exercises and scenario-based planning with relevant agencies in Taiwan; and (4) to support workforce development, emergency response planning, and institutional modernization of energy sector operators. (c) United States-Taiwan energy security center The Secretary of State may establish a joint United States-Taiwan Energy Security Center in the United States, leveraging the expertise of institutions of higher education and private sector entities to foster dialogue and collaboration for academic cooperation in energy security and resilience. (d) Authorization of assistance The Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, may provide technical assistance to support the activities described in subsection (b) or the center described in subsection (c). (e) Implementation (1) In general Assistance under this section shall be provided through the American Institute in Taiwan and in consultation with relevant authorities in Taiwan, consistent with the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ). (2) Notification Any assistance provided by the Department of State pursuant this section shall be subject to the regular notification requirements of section 634A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2394\u20131 ). (f) Briefings Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, shall provide to the appropriate congressional committees a briefing on the implementation of this section. 5540D. Annual report (a) In general Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , and annually thereafter for 3 years, the Secretary of State, in coordination with the Secretary of Commerce, the Secretary of Energy, and the Secretary of Defense, shall submit to the appropriate congressional committees a report that\u2014 (1) describes actions taken under this part; (2) identifies barriers to\u2014 (A) increased exportation of liquefied natural gas to Taiwan; and (B) energy infrastructure security cooperation; (3) evaluates the effectiveness of capacity building and technical assistance activities carried out under section 5540C; and (4) provides recommendations to expand and improve future bilateral energy cooperation between the United States and Taiwan. (b) Form Each report required by subsection (a) shall be submitted in unclassified form but may include a classified annex. .\n#### 4. Training to improve Taiwan's critical energy infrastructure protection\nSection 5504(a)(3) of the Taiwan Enhanced Resilience Act ( 22 U.S.C. 3353(a)(3) ) is amended by inserting after capabilities the following: and critical energy infrastructure protection .\n#### 5. Findings and sense of Congress regarding Taiwan\u2019s use of nuclear energy\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to the International Atomic Energy Agency, nuclear energy\u2014\n**(A)**\nis the second safest source of energy;\n**(B)**\nis one of only 2 clean energies that offer non-stop baseload power required for sustainable economic growth and improved human welfare; and\n**(C)**\nwhen compared with other sources of electricity from cradle to grave, has the lowest carbon footprint, uses fewer materials, and takes up less land.\n**(2)**\nA nuclear fuel assembly lasts up to 6 years, making supply more resistant to maritime disruption.\n**(3)**\nTaiwan has built a robust civilian nuclear capability over previous decades that has shown the potential to provide clean, reliable power to Taiwan.\n**(4)**\nOn May 17, 2025, the Maanshan-2, Taiwan\u2019s last operating nuclear power plant, was shut down after its 40-year operating license expired.\n**(5)**\nThere are compelling economic and security reasons to evaluate placing existing infrastructure back in service to ensure Taiwan has clean, reliable power that is more resilient in a contingency.\n**(6)**\nAs a result of Taiwan\u2019s substantial use of energy in industrial manufacturing and production, and emerging energy requirements for electrification, artificial intelligence, and data center support, there is considerable benefit for Taiwan to evaluate new small modular reactors technology to augment its energy capacity and resilience.\n**(7)**\nAs Taiwan modernizes its military, the power demand from command-and-control systems, intelligence platforms, drone operations, and joint battlespace integration will continue to increase.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is in the interests of both the United States and Taiwan for the Government of Taiwan to consider\u2014\n**(A)**\nmaintaining nuclear power as an energy source; and\n**(B)**\nutilizing new nuclear technologies, including Gen III+ nuclear reactors and small modular reactor technology; and\n**(2)**\nthe United States should prioritize assistance and cooperation with Taiwan on nuclear energy to improve technology exports and job creation in the United States and energy security and resilience in Taiwan.\n#### 6. Insurance for vessels transporting vital goods to strategic partners\nSection 53902 of title 46, United States Code, is amended by adding at the end the following:\n(d) Vessels transporting vital goods to strategic partners (1) In general The Secretary of Transportation may provide insurance and reinsurance under this chapter for any vessel engaged in commerce transporting critical energy, humanitarian, or other goods to Taiwan or another strategic partner of the United States that is facing coercive maritime threats if the Secretary determines, in consultation with the Secretary of Defense, the Secretary of State, and the Director of National Intelligence, that providing such insurance or reinsurance is necessary to support vital strategic commerce or to deter coercive maritime behavior that undermines regional security. (2) Nonapplicability of certain condition The condition under section 53902(c) shall not apply with respect to a vessel described in paragraph (1). .",
      "versionDate": "2025-09-04",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2722rs.xml",
      "text": "II\nCalendar No. 325\n119th CONGRESS\n2d Session\nS. 2722\nIN THE SENATE OF THE UNITED STATES\nSeptember 4, 2025 Mr. Ricketts (for himself, Mr. Coons , Mr. Budd , Mr. Hickenlooper , and Mr. Hoeven ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo promote the energy security of Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Energy Security and Anti-Embargo Act of 2025 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a vital democratic partner the energy security of which is critical to the strategic interests of the United States in the Indo-Pacific region.\n**(2)**\nEnhancing Taiwan\u2019s energy resilience through diversified and reliable sources reduces vulnerability to coercion, disruption, or attack by authoritarian regimes.\n**(3)**\nThe United States possesses abundant supplies of liquefied natural gas and other energy resources that support economic growth, job creation, and the national security interests of the United States.\n**(4)**\nPromoting United States energy exports to and partnerships with Taiwan aligns with United States energy diplomacy objectives, strengthens bilateral economic and security ties, and contributes to regional stability.\n**(5)**\nThe Alaska Liquefied Natural Gas Project, which has received pledged support from Taiwan\u2019s state energy firm CPC Corp, would enhance the ability of the United States to supply Taiwan and other allies and partners of the United States in the Indo-Pacific with a cost-effective, reliable supply of energy.\n**(6)**\nTaiwan\u2019s energy infrastructure, including electric grid systems and liquefied natural gas import facilities, is vulnerable to asymmetric and kinetic threats from the People\u2019s Republic of China.\n**(7)**\nSupporting Taiwan\u2019s efforts to improve the resilience and security of its energy infrastructure advances deterrence and promotes continuity of government operations in the event of a crisis.\n#### 3. Promotion of liquefied natural gas exports and energy infrastructure resilience for Taiwan\nThe Taiwan Enhanced Resilience Act ( 22 U.S.C. 3351 et seq. ) is amended by adding at the end the following:\n8 Promotion of liquefied natural gas exports and energy infrastructure resilience for Taiwan 5540A. Definitions In this part: (1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Foreign Relations, the Committee on Commerce, Science, and Transportation, and the Committee on Energy and Natural Resources of the Senate; and (B) the Committee on Foreign Affairs, the Committee on Energy and Commerce, and the Committee on Natural Resources of the House of Representatives. (2) Asymmetric threat The term asymmetric threat means a threat posed by unconventional means, including a cyberattack, sabotage, or economic coercion, designed to undermine or disrupt the operation of critical infrastructure. 5540B. Promotion of liquefied natural gas exports to Taiwan (a) In general The Secretary of State, in coordination with the Secretary of Commerce and the Secretary of Energy, shall prioritize efforts to support and facilitate increased exportation to Taiwan of liquefied natural gas produced in the United States. (b) Required activities In carrying out subsection (a), the Secretaries shall\u2014 (1) engage with United States liquefied natural gas producers, exporters, and infrastructure entities to identify and address barriers to liquefied natural gas exports and storage projects intended for the market of Taiwan; (2) facilitate coordination between United States private sector entities and relevant government and private sector stakeholders in Taiwan; (3) provide diplomatic and technical support to streamline regulatory processes and expedite permitting for liquefied natural gas export and storage infrastructure projects linked to Taiwan; (4) consult with the Government of Taiwan to assess and strengthen liquefied natural gas import and storage capabilities; and (5) coordinate interagency efforts to ensure cohesive and sustained United States support for liquefied natural gas exports to Taiwan. 5540C. Energy infrastructure resilience capacity building (a) Requirement Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, shall seek to engage with appropriate officials of Taiwan for the purpose of cooperating with the Ministry of Foreign Affairs, the Ministry of the Interior, the Ministry of Defense, and the head of any other applicable ministry of Taiwan for capacity building to enhance energy infrastructure resilience, including defensive military cybersecurity activities. (b) Identification of activities In carrying out subsection (a), the Secretary of State may identify cooperative activities\u2014 (1) to enhance cybersecurity programs to protect grid operating systems, liquefied natural gas terminals, and supervisory control and data acquisition systems; (2) to support physical security improvements, operational redundancy, and continuity-of-operations planning; (3) to engage in joint training exercises and scenario-based planning with relevant agencies in Taiwan; and (4) to support workforce development, emergency response planning, and institutional modernization of energy sector operators. (c) United States-Taiwan energy security center The Secretary of State may establish a joint United States-Taiwan Energy Security Center in the United States, leveraging the expertise of institutions of higher education and private sector entities to foster dialogue and collaboration for academic cooperation in energy security and resilience. (d) Authorization of assistance The Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, may provide technical assistance to support the activities described in subsection (b) or the center described in subsection (c). (e) Implementation (1) In general Assistance under this section shall be provided through the American Institute in Taiwan and in consultation with relevant authorities in Taiwan, consistent with the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ). (2) Notification Any assistance provided by the Department of State pursuant this section shall be subject to the regular notification requirements of section 634A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2394\u20131 ). (f) Briefings Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, shall provide to the appropriate congressional committees a briefing on the implementation of this section. 5540D. Annual report (a) In general Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2025 , and annually thereafter for 3 years, the Secretary of State, in coordination with the Secretary of Commerce, the Secretary of Energy, and the Secretary of Defense, shall submit to the appropriate congressional committees a report that\u2014 (1) describes actions taken under this part; (2) identifies barriers to\u2014 (A) increased exportation of liquefied natural gas to Taiwan; and (B) energy infrastructure security cooperation; (3) evaluates the effectiveness of capacity building and technical assistance activities carried out under section 5540C; and (4) provides recommendations to expand and improve future bilateral energy cooperation between the United States and Taiwan. (b) Form Each report required by subsection (a) shall be submitted in unclassified form but may include a classified annex. .\n#### 4. Training to improve Taiwan's critical energy infrastructure protection\nSection 5504(a)(3) of the Taiwan Enhanced Resilience Act ( 22 U.S.C. 3353(a)(3) ) is amended by inserting after capabilities the following: and critical energy infrastructure protection .\n#### 5. Findings and sense of Congress regarding Taiwan\u2019s use of nuclear energy\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to the International Atomic Energy Agency, nuclear energy\u2014\n**(A)**\nis the second safest source of energy;\n**(B)**\nis one of only 2 clean energies that offer non-stop baseload power required for sustainable economic growth and improved human welfare; and\n**(C)**\nwhen compared with other sources of electricity from cradle to grave, has the lowest carbon footprint, uses fewer materials, and takes up less land.\n**(2)**\nA nuclear fuel assembly lasts up to 6 years, making supply more resistant to maritime disruption.\n**(3)**\nTaiwan has built a robust civilian nuclear capability over previous decades that has shown the potential to provide clean, reliable power to Taiwan.\n**(4)**\nOn May 17, 2025, the Maanshan-2, Taiwan\u2019s last operating nuclear power plant, was shut down after its 40-year operating license expired.\n**(5)**\nThere are compelling economic and security reasons to evaluate placing existing infrastructure back in service to ensure Taiwan has clean, reliable power that is more resilient in a contingency.\n**(6)**\nAs a result of Taiwan\u2019s substantial use of energy in industrial manufacturing and production, and emerging energy requirements for electrification, artificial intelligence, and data center support, there is considerable benefit for Taiwan to evaluate new small modular reactors technology to augment its energy capacity and resilience.\n**(7)**\nAs Taiwan modernizes its military, the power demand from command-and-control systems, intelligence platforms, drone operations, and joint battlespace integration will continue to increase.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is in the interests of both the United States and Taiwan for the Government of Taiwan to consider\u2014\n**(A)**\nmaintaining nuclear power as an energy source; and\n**(B)**\nutilizing new nuclear technologies, including Gen III+ nuclear reactors and small modular reactor technology; and\n**(2)**\nthe United States should prioritize assistance and cooperation with Taiwan on nuclear energy to improve technology exports and job creation in the United States and energy security and resilience in Taiwan.\n#### 6. Insurance for vessels transporting vital goods to strategic partners\nSection 53902 of title 46, United States Code, is amended by adding at the end the following:\n(d) Vessels transporting vital goods to strategic partners (1) In general The Secretary of Transportation may provide insurance and reinsurance under this chapter for any vessel engaged in commerce transporting critical energy, humanitarian, or other goods to Taiwan or another strategic partner of the United States that is facing coercive maritime threats if the Secretary determines, in consultation with the Secretary of Defense, the Secretary of State, and the Director of National Intelligence, that providing such insurance or reinsurance is necessary to support vital strategic commerce or to deter coercive maritime behavior that undermines regional security. (2) Nonapplicability of certain condition The condition under section 53902(c) shall not apply with respect to a vessel described in paragraph (1). .",
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
        "actionDate": "2026-03-09",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "7873",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
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
            "name": "Asia",
            "updateDate": "2026-04-01T20:13:40Z"
          },
          {
            "name": "China",
            "updateDate": "2026-04-01T20:14:53Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2026-04-01T20:14:39Z"
          },
          {
            "name": "Computer security and identity theft",
            "updateDate": "2026-04-01T20:14:10Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T20:14:31Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-04-01T20:13:54Z"
          },
          {
            "name": "Infrastructure development",
            "updateDate": "2026-04-01T20:14:03Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2026-04-01T20:14:25Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2026-04-01T20:14:18Z"
          },
          {
            "name": "Nuclear power",
            "updateDate": "2026-04-01T20:14:47Z"
          },
          {
            "name": "Oil and gas",
            "updateDate": "2026-04-01T20:13:47Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2026-04-01T20:13:35Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-09-23T15:07:58Z"
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
      "date": "2025-09-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2722is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2722rs.xml"
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
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T04:38:21Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-10T04:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to promote the energy security of Taiwan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-10T04:18:23Z"
    }
  ]
}
```
