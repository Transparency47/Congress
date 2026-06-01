# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7873?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7873
- Title: Taiwan Energy Security and Anti-Embargo Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7873
- Origin chamber: House
- Introduced date: 2026-03-09
- Update date: 2026-05-12T08:06:05Z
- Update date including text: 2026-05-12T08:06:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-03-09: Introduced in House

## Actions

- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Introduced in House
- 2026-03-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-09 - IntroReferral: Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-09",
    "latestAction": {
      "actionDate": "2026-03-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7873",
    "number": "7873",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "H001101",
        "district": "10",
        "firstName": "Pat",
        "fullName": "Rep. Harrigan, Pat [R-NC-10]",
        "lastName": "Harrigan",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-12T08:06:05Z",
    "updateDateIncludingText": "2026-05-12T08:06:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-09",
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
      "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-09",
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
          "date": "2026-03-09T17:01:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-03-09T17:01:25Z",
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
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-03-09",
      "state": "MD"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-09",
      "state": "NY"
    },
    {
      "bioguideId": "F000246",
      "district": "4",
      "firstName": "Pat",
      "fullName": "Rep. Fallon, Pat [R-TX-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Fallon",
      "party": "R",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
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
    },
    {
      "bioguideId": "E000300",
      "district": "8",
      "firstName": "Gabe",
      "fullName": "Rep. Evans, Gabe [R-CO-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "R",
      "sponsorshipDate": "2026-05-11",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7873ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7873\nIN THE HOUSE OF REPRESENTATIVES\nMarch 9, 2026 Mr. Harrigan (for himself, Mr. Olszewski , and Mr. Lawler ) introduced the following bill; which was referred to the Committee on Foreign Affairs , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo promote the energy security of Taiwan, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Energy Security and Anti-Embargo Act of 2026 .\n#### 2. Findings\nCongress makes the following findings:\n**(1)**\nTaiwan is a vital democratic partner the energy security of which is critical to the strategic interests of the United States in the Indo-Pacific region.\n**(2)**\nEnhancing Taiwan\u2019s energy resilience through diversified and reliable sources reduces vulnerability to coercion, disruption, or attack by authoritarian regimes.\n**(3)**\nThe United States possesses abundant supplies of energy resources, technologies, and expertise that support economic growth, job creation, and the national security interests of the United States.\n**(4)**\nPromoting United States energy exports to and partnerships with Taiwan aligns with United States energy diplomacy objectives, strengthens bilateral economic and security ties, and contributes to regional stability.\n**(5)**\nTaiwan\u2019s energy infrastructure, including electric grid systems and liquefied natural gas import facilities, is vulnerable to asymmetric and kinetic threats from the People\u2019s Republic of China.\n**(6)**\nSupporting Taiwan\u2019s efforts to improve the resilience and security of its energy infrastructure advances deterrence and promotes continuity of government operations in the event of a crisis.\n**(7)**\nIn 2024, the United States exported 212,837,000,000 cubic feet of liquefied natural gas to the People\u2019s Republic of China and 118,162,000,000 cubic feet of liquefied natural gas to Taiwan. That export imbalance indicates that the United States could help meet Taiwan\u2019s needs for liquefied natural gas by redirecting a portion of exports of liquefied natural gas currently destined for the People\u2019s Republic of China to Taiwan, assuming sufficient import and storage capacity in Taiwan.\n#### 3. Promotion of United States energy exports and energy infrastructure resilience for Taiwan\nThe Taiwan Enhanced Resilience Act ( 22 U.S.C. 3351 et seq. ) is amended by adding at the end the following:\n8 Promotion of United States energy exports and energy infrastructure resilience for Taiwan 5540A. Definitions In this part: (1) Appropriate congressional committees The term appropriate congressional committees means\u2014 (A) the Committee on Foreign Relations, the Committee on Commerce, Science, and Transportation, and the Committee on Energy and Natural Resources of the Senate; and (B) the Committee on Foreign Affairs, the Committee on Energy and Commerce, and the Committee on Natural Resources of the House of Representatives. (2) Asymmetric threat The term asymmetric threat means a threat posed by unconventional means, including a cyberattack, sabotage, or economic coercion, designed to undermine or disrupt the operation of critical infrastructure. 5540B. Promotion of United States energy exports to Taiwan (a) In general The Secretary of State, in coordination with the Secretary of Commerce and the Secretary of Energy, may prioritize efforts to support and facilitate\u2014 (1) United States energy exports to Taiwan; and (2) the development of energy projects that diversify Taiwan\u2019s energy sources. (b) Activities In carrying out subsection (a), the Secretaries may\u2014 (1) engage with United States liquefied natural gas producers, exporters, and infrastructure entities to identify and address barriers to liquefied natural gas exports and storage projects intended for the market of Taiwan; (2) facilitate coordination between United States private sector entities, relevant governing authorities, and private sector stakeholders in Taiwan, including to promote investment in energy projects in Taiwan and the export of United States technologies to Taiwan; (3) provide diplomatic and technical support for liquefied natural gas exports, exports of other United States energy resources and technologies, and storage and related infrastructure for any relevant energy projects linked to Taiwan; (4) consult with Taiwan to assess and strengthen liquefied natural gas import and storage capabilities; and (5) coordinate interagency efforts to ensure cohesive and sustained United States support for Taiwan\u2019s energy security. (c) Assessment required Not later than one year after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2026 , the National Academy of Sciences shall submit to the appropriate congressional committees an assessment of\u2014 (1) potential opportunities for boosting exports of liquefied natural gas produced in the United States to Taiwan, including by redirecting exports of such gas that flow to the People\u2019s Republic of China as of such date of enactment; (2) potential ways the United States could shift the flow of such exports toward Taiwan; and (3) potential ways the United States could support efforts to redirect such exports to Taiwan. 5540C. Energy infrastructure resilience capacity building (a) Requirement Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2026 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, may seek to engage with appropriate officials of Taiwan for the purpose of cooperating with the Ministry of Foreign Affairs, the Ministry of the Interior, the Ministry of Defense, and the head of any other applicable ministry of Taiwan for capacity building to enhance energy infrastructure resilience, including defensive military cybersecurity activities. (b) Identification of activities In carrying out subsection (a), the Secretary of State may identify cooperative activities\u2014 (1) to enhance cybersecurity programs to protect grid operating systems, liquefied natural gas and other energy storage terminals, and supervisory control and data acquisition systems; (2) to support physical security improvements, operational redundancy, and continuity-of-operations planning; (3) to engage in joint training exercises and scenario-based planning with relevant agencies in Taiwan; and (4) to support workforce development, emergency response planning, and institutional modernization of energy sector operators. (c) United States-Taiwan energy security center The Secretary of State, in coordination with the Secretary of Energy, may establish a joint United States-Taiwan Energy Security Center in the United States, leveraging the expertise of institutions of higher education and private sector entities to foster dialogue and collaboration for academic cooperation in energy security and resilience. (d) Authorization of assistance The Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, may provide technical assistance to support the activities described in subsection (b) or the center described in subsection (c). (e) Implementation (1) In general Assistance under this section shall be provided through the American Institute in Taiwan and in consultation with relevant authorities in Taiwan, consistent with the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ). (2) Notification Any assistance provided by the Department of State pursuant this section shall be subject to the regular notification requirements of section 634A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2394\u20131 ). (f) Briefings Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2026 , the Secretary of State, in coordination with the Secretary of Defense and the Secretary of Energy, shall provide to the appropriate congressional committees a briefing on the implementation of this section. 5540D. Annual report (a) In general Not later than 180 days after the date of the enactment of the Taiwan Energy Security and Anti-Embargo Act of 2026 , and annually thereafter for 3 years, the Secretary of State, in coordination with the Secretary of Commerce, the Secretary of Energy, and the Secretary of Defense, shall submit to the appropriate congressional committees a report that\u2014 (1) describes actions taken under this part; (2) identifies barriers to\u2014 (A) increased United States energy exports to Taiwan; (B) increased investment in Taiwan\u2019s energy sector that would strengthen Taiwan\u2019s energy resilience; (C) energy infrastructure security cooperation; and (D) enhancing the resilience of Taiwan\u2019s energy supply against economic coercion and supply chain disruptions, with due consideration for national security implications; (3) evaluates the effectiveness of capacity building and technical assistance activities carried out under section 5540C; and (4) provides recommendations to expand and diversify Taiwan\u2019s energy sources and improve future bilateral energy cooperation between the United States and Taiwan. (b) Form Each report required by subsection (a) shall be submitted in unclassified form but may include a classified annex. .\n#### 4. Training to improve Taiwan's critical energy infrastructure protection\nSection 5504(a)(3) of the Taiwan Enhanced Resilience Act ( 22 U.S.C. 3353(a)(3) ) is amended by inserting after capabilities the following: and critical energy infrastructure protection .\n#### 5. Findings and sense of Congress regarding Taiwan\u2019s use of nuclear energy\n##### (a) Findings\nCongress makes the following findings:\n**(1)**\nAccording to the International Atomic Energy Agency, nuclear energy\u2014\n**(A)**\nis the second safest source of energy;\n**(B)**\nis one of only 2 clean energies that offer non-stop baseload power required for sustainable economic growth and improved human welfare; and\n**(C)**\nwhen compared with other sources of electricity from cradle to grave, has the lowest carbon footprint, uses fewer materials, and takes up less land.\n**(2)**\nA nuclear fuel assembly lasts up to 6 years, making supply more resistant to maritime disruption.\n**(3)**\nTaiwan has built a robust civilian nuclear capability over previous decades that has shown the potential to provide clean, reliable power to Taiwan.\n**(4)**\nOn May 17, 2025, the Maanshan-2, Taiwan\u2019s last operating nuclear power plant, was shut down after its 40-year operating license expired.\n**(5)**\nThere are compelling economic and security reasons to evaluate placing existing infrastructure back in service to ensure Taiwan has clean, reliable power that is more resilient in a contingency.\n**(6)**\nAs a result of Taiwan\u2019s substantial use of energy in industrial manufacturing and production, and emerging energy requirements for electrification, artificial intelligence, and data center support, there is considerable benefit for Taiwan to evaluate new small modular reactors technology to augment its energy capacity and resilience.\n**(7)**\nAs Taiwan modernizes its military, the power demand from command-and-control systems, intelligence platforms, drone operations, and joint battlespace integration will continue to increase.\n##### (b) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nit is in the interests of both the United States and Taiwan for Taiwan\u2014\n**(A)**\nto maintain nuclear power as an energy source; and\n**(B)**\nto utilize new nuclear technologies, including Gen III+ nuclear reactors and small modular reactor technology; and\n**(2)**\nthe United States should prioritize assistance and cooperation with Taiwan on nuclear energy to improve technology exports and job creation in the United States and energy security and resilience in Taiwan.\n#### 6. Insurance for vessels transporting vital goods to strategic partners\nSection 53902 of title 46, United States Code, is amended by adding at the end the following:\n(d) Vessels transporting vital goods to strategic partners (1) In general The Secretary of Transportation may provide insurance and reinsurance under this chapter for any vessel engaged in commerce transporting critical energy, humanitarian, or other goods to Taiwan or another strategic partner of the United States that is facing coercive maritime threats if the Secretary determines, in consultation with the Secretary of Defense, the Secretary of State, and the Director of National Intelligence, that providing such insurance or reinsurance is necessary to support vital strategic commerce or to deter coercive maritime behavior that undermines regional security. (2) Nonapplicability of certain condition The condition under section 53902(c) shall not apply with respect to a vessel described in paragraph (1). .\n#### 7. Rule of construction regarding continued United States policy toward Taiwan and the Government of the People's Republic of China\nNothing in this Act may be construed as a change to the One China Policy of the United States, which is guided by the Taiwan Relations Act ( 22 U.S.C. 3301 et seq. ), the three United States-People\u2019s Republic of China Joint Communiqu\u00e9s, and the Six Assurances.",
      "versionDate": "2026-03-09",
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
        "actionDate": "2026-02-10",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 325."
      },
      "number": "2722",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
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
        "name": "International Affairs",
        "updateDate": "2026-04-02T22:40:38Z"
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
      "date": "2026-03-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7873ih.xml"
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
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Taiwan Energy Security and Anti-Embargo Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote the energy security of Taiwan, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:29Z"
    }
  ]
}
```
