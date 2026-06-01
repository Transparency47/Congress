# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2222?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2222
- Title: Critical Undersea Infrastructure Resilience Initiative Act
- Congress: 119
- Bill type: S
- Bill number: 2222
- Origin chamber: Senate
- Introduced date: 2025-07-09
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-07-09: Introduced in Senate
- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 323.
- Latest action: 2025-07-09: Introduced in Senate

## Actions

- 2025-07-09 - IntroReferral: Introduced in Senate
- 2025-07-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 323.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-09",
    "latestAction": {
      "actionDate": "2025-07-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2222",
    "number": "2222",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "Critical Undersea Infrastructure Resilience Initiative Act",
    "type": "S",
    "updateDate": "2026-05-15T11:03:25Z",
    "updateDateIncludingText": "2026-05-15T11:03:25Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 323.",
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
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.",
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
      "text": "Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute and an amendment to the title. Without written report.",
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
      "actionDate": "2025-07-09",
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
      "actionDate": "2025-07-09",
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
            "date": "2026-02-10T16:31:15Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-07-09T18:17:28Z",
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
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "NV"
    },
    {
      "bioguideId": "M001243",
      "firstName": "David",
      "fullName": "Sen. McCormick, David [R-PA]",
      "isOriginalCosponsor": "False",
      "lastName": "McCormick",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-05-14",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2222is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2222\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Curtis (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo enhance the security, resilience, and protection of undersea communication cables vital to Taiwan\u2019s national security, economic stability, and defense, particularly in countering gray zone tactics employed by the People's Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Undersea Cable Resilience Initiative Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUndersea communication cables (in this Act referred to as undersea cables ) are critical infrastructure essential for global communication, commerce, and national security, particularly for Taiwan, whose economic and security stability relies heavily on undersea cable connectivity.\n**(2)**\nThe Government of the People's Republic of China has increasingly used gray zone tactics to undermine the security and sovereignty of Taiwan, including suspected sabotage of undersea cables in and around Taiwan, such as the incidents involving the severing of cables around the Matsu Islands of Taiwan and other key regions in 2023 and 2025.\n**(3)**\nUndersea cables are a primary target in the strategy of the Government of the People's Republic of China to cripple the communication capabilities of Taiwan in the event of a military conflict, as part of broader hybrid warfare tactics. Disruption of undersea cables would significantly impact the ability of Taiwan to communicate both domestically and internationally, leading to a breakdown in military, economic, and social functions.\n**(4)**\nThe vulnerability of Taiwan to attacks on undersea cables has been compounded by an increasing number of foreign vessels suspected of involvement in sabotage, including Chinese-linked vessels, which are perceived as direct threats to Taiwan's critical infrastructure.\n**(5)**\nThe ability of the Government of the People's Republic of China to disrupt or sever undersea cables is a critical element of its military strategy aimed at softening Taiwan's defenses and isolating Taiwan from international support in the event of an invasion or military confrontation.\n**(6)**\nRecent activities by foreign adversaries, particularly the People's Republic of China, have increased the risk of sabotage and disruption to undersea cables serving Taiwan and other nations. Notably, in February 2023, the Matsu Islands of Taiwan experienced major internet disruptions due to two undersea cables being severed, with suspicions pointing toward deliberate external interference. Furthermore, in January 2025, Chunghwa Telecom reported damage to an international undersea cable and identified a suspicious vessel \u2014the Chinese-linked cargo ship Shunxin39\u2014near the affected area. The Coast Guard of Taiwan has indicated concerns that that vessel may have been involved in deliberately cutting the cable. In a subsequent incident, Taiwan seized the Togo-flagged Hong Tai 58, suspected of deliberately severing an undersea cable. The Coast Guard of Taiwan acknowledged the possibility of China's involvement as part of a grey area intrusion .\n**(7)**\nSince 2023, there have been at least 11 cases of damage to undersea cables around Taiwan and a similar number in the Baltic Sea, with authorities in Taiwan and Europe suspecting Chinese and Russian involvement in several incidents, although some damages have been attributed to natural causes. Those incidents highlight the vulnerability of those critical systems to gray zone tactics and the difficulty of proving sabotage or holding perpetrators accountable.\n**(8)**\nThe sabotage of undersea cables constitutes gray zone tactics designed to destabilize and undermine international security without direct military confrontation.\n**(9)**\nSeveral regional mechanisms have been established to bolster the security of undersea cables, including the Nordic Warden initiative for maritime domain awareness and the Quad Partnership for Cable Connectivity and Resilience, aimed at enhancing the security and resilience of undersea cables in the Indo-Pacific.\n**(10)**\nTo counter the threats described in this section and safeguard the resilience of Taiwan, it is imperative for the United States and its allies to take decisive action to bolster Taiwan's defenses for undersea cables and foster international cooperation to protect those critical assets.\n#### 3. Taiwan Undersea Cable Resilience Initiative\n##### (a) Establishment\nNot later than 360 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense, the Secretary of Homeland Security, the Commandant of the Coast Guard, and such other heads of agencies as the Secretary of State considers relevant, shall establish an initiative to be known as the Taiwan Undersea Cable Resilience Initiative (in this section referred to as the Initiative ).\n##### (b) Priority\nThe Initiative shall prioritize the protection and resilience of undersea cables near Taiwan, with a focus on countering threats from the People's Republic of China to the critical infrastructure of Taiwan.\n##### (c) Key focus areas\n**(1) Advanced monitoring and detection capabilities**\nIn carrying out the Initiative, the Secretary of State, in coordination with the Secretary of Homeland Security and the Secretary of Defense, shall develop and deploy advanced undersea cable monitoring systems for Taiwan capable of detecting disruptions or potential sabotage in real-time, including by informing Taiwan, as appropriate, of early warnings from global intelligence networks.\n**(2) Rapid response protocols**\nIn carrying out the Initiative, the Secretary of State shall\u2014\n**(A)**\nestablish rapid response protocols for repairing severed undersea cables or mitigating disruptions; and\n**(B)**\nwork with allies of the United States to help Taiwan develop the logistical capacity to respond quickly to attacks on undersea cables and minimize downtime.\n**(3) Enhancing maritime domain awareness**\nIn carrying out the Initiative\u2014\n**(A)**\nthe Secretary of the Navy and the Commandant of the Coast Guard, in collaboration with the Coast Guard of Taiwan and regional allies, shall enhance maritime domain awareness around Taiwan, focusing on the detection of suspicious vessels or activities near critical undersea cable routes; and\n**(B)**\nthe Commandant of the Coast Guard shall assist in joint patrols and surveillance, particularly in the Taiwan Strait and surrounding maritime zones, to monitor potential threats and prevent sabotage.\n**(4) International frameworks for protection**\n**(A) In general**\nIn carrying out the Initiative, the Secretary of State shall seek to establish cooperative frameworks with regional allies and global partners to protect the undersea cable networks near Taiwan.\n**(B) Elements**\nThe frameworks established under subparagraph (A) shall provide for participation by the United States in joint drills, intelligence-sharing platforms, and collaborative surveillance operations to enhance collective security against sabotage.\n**(5) Taiwan-specific cable hardening**\nIn carrying out the Initiative, the Secretary of State shall encourage and support the hardening of critical undersea cables near Taiwan, including reinforcing cables, improving burial depths, and using more resilient materials to reduce vulnerability to natural disasters and deliberate interference.\n#### 4. Countering China\u2019s gray zone tactics\n##### (a) Working with partners To counter Chinese sabotage\nThe President shall work with Taiwan and like-minded international partners to implement strategies that directly counter the use by the Government of the People's Republic of China of undersea cable sabotage as part of its gray zone warfare, including by increasing diplomatic pressure on that Government to adhere to international norms regarding the protection of undersea infrastructure.\n##### (b) Raising awareness\nThe President shall work with Taiwan to raise global awareness of the risks posed by interference by the Government of the People's Republic of China in undersea cables, including through public diplomacy efforts, information sharing, and international forums that address gray zone tactics and the protection of critical infrastructure.\n#### 5. Imposition of sanctions with respect to sabotage of undersea cables\n##### (a) In general\nThe President shall impose the sanctions described in subsection (b) with respect to any person of the People's Republic of China that the President determines is responsible for or complicit in damaging undersea cables critical to the national security of Taiwan.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (a) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (d) Exceptions\n**(1) Exception for intelligence activities**\nThis section shall not apply with respect to activities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(2) Exception to comply with international agreements**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien to the United States if such admission is necessary to comply with the obligations of the United States under the Agreement regarding the Headquarters of the United Nations, signed at Lake Success on June 26, 1947, and entered into force on November 21, 1947, between the United Nations and the United States, or the Convention on Consular Relations, done at Vienna on April 24, 1963, and entered into force on March 19, 1967, or other international obligations of the United States.\n**(3) Exception relating to importation of goods**\n**(A) In general**\nThe authorities and requirements to impose sanctions under this section shall not include the authority or requirement to impose sanctions on the importation of goods.\n**(B) Good defined**\nIn this paragraph, the term good means any article, natural or manmade substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (e) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Person of the People's Republic of China**\nThe term person of the People's Republic of China means\u2014\n**(A)**\nan individual who is a citizen or national of the People's Republic of China; and\n**(B)**\nan entity owned or controlled by the Government of the People's Republic of China, organized under the laws of the People's Republic of China, or otherwise subject to the jurisdiction of the Government of the People's Republic of China.\n**(3) United states person**\nThe term United States person means\u2014\n**(A)**\nany United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including any foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n#### 6. Semiannual report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit to Congress a report detailing\u2014\n**(1)**\nany incidents of interference in undersea cables near Taiwan; and\n**(2)**\nany actions taken in response to such incidents.",
      "versionDate": "2025-07-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2222rs.xml",
      "text": "II\nCalendar No. 323\n119th CONGRESS\n2d Session\nS. 2222\nIN THE SENATE OF THE UNITED STATES\nJuly 9, 2025 Mr. Curtis (for himself and Ms. Rosen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment and an amendment to the title Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo enhance the security, resilience, and protection of undersea communication cables vital to Taiwan\u2019s national security, economic stability, and defense, particularly in countering gray zone tactics employed by the People's Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Taiwan Undersea Cable Resilience Initiative Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nUndersea communication cables (in this Act referred to as undersea cables ) are critical infrastructure essential for global communication, commerce, and national security, particularly for Taiwan, whose economic and security stability relies heavily on undersea cable connectivity.\n**(2)**\nThe Government of the People's Republic of China has increasingly used gray zone tactics to undermine the security and sovereignty of Taiwan, including suspected sabotage of undersea cables in and around Taiwan, such as the incidents involving the severing of cables around the Matsu Islands of Taiwan and other key regions in 2023 and 2025.\n**(3)**\nUndersea cables are a primary target in the strategy of the Government of the People's Republic of China to cripple the communication capabilities of Taiwan in the event of a military conflict, as part of broader hybrid warfare tactics. Disruption of undersea cables would significantly impact the ability of Taiwan to communicate both domestically and internationally, leading to a breakdown in military, economic, and social functions.\n**(4)**\nThe vulnerability of Taiwan to attacks on undersea cables has been compounded by an increasing number of foreign vessels suspected of involvement in sabotage, including Chinese-linked vessels, which are perceived as direct threats to Taiwan's critical infrastructure.\n**(5)**\nThe ability of the Government of the People's Republic of China to disrupt or sever undersea cables is a critical element of its military strategy aimed at softening Taiwan's defenses and isolating Taiwan from international support in the event of an invasion or military confrontation.\n**(6)**\nRecent activities by foreign adversaries, particularly the People's Republic of China, have increased the risk of sabotage and disruption to undersea cables serving Taiwan and other nations. Notably, in February 2023, the Matsu Islands of Taiwan experienced major internet disruptions due to two undersea cables being severed, with suspicions pointing toward deliberate external interference. Furthermore, in January 2025, Chunghwa Telecom reported damage to an international undersea cable and identified a suspicious vessel \u2014the Chinese-linked cargo ship Shunxin39\u2014near the affected area. The Coast Guard of Taiwan has indicated concerns that that vessel may have been involved in deliberately cutting the cable. In a subsequent incident, Taiwan seized the Togo-flagged Hong Tai 58, suspected of deliberately severing an undersea cable. The Coast Guard of Taiwan acknowledged the possibility of China's involvement as part of a grey area intrusion .\n**(7)**\nSince 2023, there have been at least 11 cases of damage to undersea cables around Taiwan and a similar number in the Baltic Sea, with authorities in Taiwan and Europe suspecting Chinese and Russian involvement in several incidents, although some damages have been attributed to natural causes. Those incidents highlight the vulnerability of those critical systems to gray zone tactics and the difficulty of proving sabotage or holding perpetrators accountable.\n**(8)**\nThe sabotage of undersea cables constitutes gray zone tactics designed to destabilize and undermine international security without direct military confrontation.\n**(9)**\nSeveral regional mechanisms have been established to bolster the security of undersea cables, including the Nordic Warden initiative for maritime domain awareness and the Quad Partnership for Cable Connectivity and Resilience, aimed at enhancing the security and resilience of undersea cables in the Indo-Pacific.\n**(10)**\nTo counter the threats described in this section and safeguard the resilience of Taiwan, it is imperative for the United States and its allies to take decisive action to bolster Taiwan's defenses for undersea cables and foster international cooperation to protect those critical assets.\n#### 3. Taiwan Undersea Cable Resilience Initiative\n##### (a) Establishment\nNot later than 360 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Secretary of Defense, the Secretary of Homeland Security, the Commandant of the Coast Guard, and such other heads of agencies as the Secretary of State considers relevant, shall establish an initiative to be known as the Taiwan Undersea Cable Resilience Initiative (in this section referred to as the Initiative ).\n##### (b) Priority\nThe Initiative shall prioritize the protection and resilience of undersea cables near Taiwan, with a focus on countering threats from the People's Republic of China to the critical infrastructure of Taiwan.\n##### (c) Key focus areas\n**(1) Advanced monitoring and detection capabilities**\nIn carrying out the Initiative, the Secretary of State, in coordination with the Secretary of Homeland Security and the Secretary of Defense, shall develop and deploy advanced undersea cable monitoring systems for Taiwan capable of detecting disruptions or potential sabotage in real-time, including by informing Taiwan, as appropriate, of early warnings from global intelligence networks.\n**(2) Rapid response protocols**\nIn carrying out the Initiative, the Secretary of State shall\u2014\n**(A)**\nestablish rapid response protocols for repairing severed undersea cables or mitigating disruptions; and\n**(B)**\nwork with allies of the United States to help Taiwan develop the logistical capacity to respond quickly to attacks on undersea cables and minimize downtime.\n**(3) Enhancing maritime domain awareness**\nIn carrying out the Initiative\u2014\n**(A)**\nthe Secretary of the Navy and the Commandant of the Coast Guard, in collaboration with the Coast Guard of Taiwan and regional allies, shall enhance maritime domain awareness around Taiwan, focusing on the detection of suspicious vessels or activities near critical undersea cable routes; and\n**(B)**\nthe Commandant of the Coast Guard shall assist in joint patrols and surveillance, particularly in the Taiwan Strait and surrounding maritime zones, to monitor potential threats and prevent sabotage.\n**(4) International frameworks for protection**\n**(A) In general**\nIn carrying out the Initiative, the Secretary of State shall seek to establish cooperative frameworks with regional allies and global partners to protect the undersea cable networks near Taiwan.\n**(B) Elements**\nThe frameworks established under subparagraph (A) shall provide for participation by the United States in joint drills, intelligence-sharing platforms, and collaborative surveillance operations to enhance collective security against sabotage.\n**(5) Taiwan-specific cable hardening**\nIn carrying out the Initiative, the Secretary of State shall encourage and support the hardening of critical undersea cables near Taiwan, including reinforcing cables, improving burial depths, and using more resilient materials to reduce vulnerability to natural disasters and deliberate interference.\n#### 4. Countering China\u2019s gray zone tactics\n##### (a) Working with partners To counter Chinese sabotage\nThe President shall work with Taiwan and like-minded international partners to implement strategies that directly counter the use by the Government of the People's Republic of China of undersea cable sabotage as part of its gray zone warfare, including by increasing diplomatic pressure on that Government to adhere to international norms regarding the protection of undersea infrastructure.\n##### (b) Raising awareness\nThe President shall work with Taiwan to raise global awareness of the risks posed by interference by the Government of the People's Republic of China in undersea cables, including through public diplomacy efforts, information sharing, and international forums that address gray zone tactics and the protection of critical infrastructure.\n#### 5. Imposition of sanctions with respect to sabotage of undersea cables\n##### (a) In general\nThe President shall impose the sanctions described in subsection (b) with respect to any person of the People's Republic of China that the President determines is responsible for or complicit in damaging undersea cables critical to the national security of Taiwan.\n##### (b) Sanctions described\nThe sanctions described in this subsection are the following:\n**(1) Blocking of property**\nThe President shall exercise all of the powers granted by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nAn alien described in subsection (a) shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\n**(i) In general**\nThe visa or other entry documentation of an alien described in subsection (a) shall be revoked, regardless of when such visa or other entry documentation is or was issued.\n**(ii) Immediate effect**\nA revocation under clause (i) shall\u2014\n**(I)**\ntake effect immediately; and\n**(II)**\nautomatically cancel any other valid visa or entry documentation that is in the possession of the alien.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (d) Exceptions\n**(1) Exception for intelligence activities**\nThis section shall not apply with respect to activities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence activities of the United States.\n**(2) Exception to comply with international agreements**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien to the United States if such admission is necessary to comply with the obligations of the United States under the Agreement regarding the Headquarters of the United Nations, signed at Lake Success on June 26, 1947, and entered into force on November 21, 1947, between the United Nations and the United States, or the Convention on Consular Relations, done at Vienna on April 24, 1963, and entered into force on March 19, 1967, or other international obligations of the United States.\n**(3) Exception relating to importation of goods**\n**(A) In general**\nThe authorities and requirements to impose sanctions under this section shall not include the authority or requirement to impose sanctions on the importation of goods.\n**(B) Good defined**\nIn this paragraph, the term good means any article, natural or manmade substance, material, supply or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (e) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Person of the People's Republic of China**\nThe term person of the People's Republic of China means\u2014\n**(A)**\nan individual who is a citizen or national of the People's Republic of China; and\n**(B)**\nan entity owned or controlled by the Government of the People's Republic of China, organized under the laws of the People's Republic of China, or otherwise subject to the jurisdiction of the Government of the People's Republic of China.\n**(3) United states person**\nThe term United States person means\u2014\n**(A)**\nany United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or of any jurisdiction within the United States, including any foreign branch of such an entity; or\n**(C)**\nany person in the United States.\n#### 6. Semiannual report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit to Congress a report detailing\u2014\n**(1)**\nany incidents of interference in undersea cables near Taiwan; and\n**(2)**\nany actions taken in response to such incidents.",
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
        "actionDate": "2026-04-02",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committee on the Judiciary, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "8177",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Critical Undersea Infrastructure Resilience Initiative Act",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-04-01T20:10:48Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-01T20:11:04Z"
          },
          {
            "name": "Asia",
            "updateDate": "2026-04-01T20:09:18Z"
          },
          {
            "name": "Broadcasting, cable, digital technologies",
            "updateDate": "2026-04-01T20:09:31Z"
          },
          {
            "name": "China",
            "updateDate": "2026-04-01T20:09:12Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-01T20:10:57Z"
          },
          {
            "name": "Electric power generation and transmission",
            "updateDate": "2026-04-01T20:09:53Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2026-04-01T20:10:18Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2026-04-01T20:10:06Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-04-01T20:09:38Z"
          },
          {
            "name": "Marine and inland water transportation",
            "updateDate": "2026-04-01T20:10:41Z"
          },
          {
            "name": "Military assistance, sales, and agreements",
            "updateDate": "2026-04-01T20:09:59Z"
          },
          {
            "name": "Military operations and strategy",
            "updateDate": "2026-04-01T20:11:13Z"
          },
          {
            "name": "Pipelines",
            "updateDate": "2026-04-01T20:09:46Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2026-04-01T20:10:33Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-04-01T20:10:12Z"
          },
          {
            "name": "Taiwan",
            "updateDate": "2026-04-01T20:09:06Z"
          },
          {
            "name": "Telephone and wireless communication",
            "updateDate": "2026-04-01T20:09:25Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2026-04-01T20:10:26Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-07-17T21:40:34Z"
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
      "date": "2025-07-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2222is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s2222rs.xml"
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
      "title": "Critical Undersea Infrastructure Resilience Initiative Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Critical Undersea Infrastructure Resilience Initiative Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Taiwan Undersea Cable Resilience Initiative Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-17T02:23:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to enhance the security, resilience, and protection of undersea communication cables vital to Taiwan's national security, economic stability, and defense, particularly in countering gray zone tactics employed by the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-17T02:18:19Z"
    }
  ]
}
```
