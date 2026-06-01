# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2950?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2950
- Title: Scam Compound Accountability and Mobilization Act
- Congress: 119
- Bill type: S
- Bill number: 2950
- Origin chamber: Senate
- Introduced date: 2025-09-30
- Update date: 2026-01-05T17:12:50Z
- Update date including text: 2026-01-05T17:12:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in Senate
- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 244.
- 2025-12-08 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8533-8535; text: CR S8533--8535)
- 2025-12-08 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-09 - Floor: Message on Senate action sent to the House.
- 2025-12-09 14:03:52 - Floor: Received in the House.
- 2025-12-09 14:21:23 - Floor: Held at the desk.
- Latest action: 2025-09-30: Introduced in Senate

## Actions

- 2025-09-30 - IntroReferral: Introduced in Senate
- 2025-09-30 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-10-22 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-10-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 244.
- 2025-12-08 - Floor: Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8533-8535; text: CR S8533--8535)
- 2025-12-08 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.
- 2025-12-09 - Floor: Message on Senate action sent to the House.
- 2025-12-09 14:03:52 - Floor: Received in the House.
- 2025-12-09 14:21:23 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2950",
    "number": "2950",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Scam Compound Accountability and Mobilization Act",
    "type": "S",
    "updateDate": "2026-01-05T17:12:50Z",
    "updateDateIncludingText": "2026-01-05T17:12:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2025-12-09",
      "actionTime": "14:21:23",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2025-12-09",
      "actionTime": "14:03:52",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-09",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-12-08",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment by Unanimous Consent. (consideration: CR S8533-8535; text: CR S8533--8535)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2025-12-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2025-10-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 244.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-30",
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
      "actionDate": "2025-10-22",
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
      "actionDate": "2025-09-30",
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
      "actionDate": "2025-09-30",
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
            "date": "2025-10-30T15:41:57Z",
            "name": "Reported By"
          },
          {
            "date": "2025-10-22T14:03:55Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-30T19:18:04Z",
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
      "bioguideId": "S001181",
      "firstName": "Jeanne",
      "fullName": "Sen. Shaheen, Jeanne [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Shaheen",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "NH"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "FL"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "False",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "IL"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-10-21",
      "state": "NE"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "False",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "NH"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-12-01",
      "state": "OK"
    },
    {
      "bioguideId": "R000608",
      "firstName": "Jacky",
      "fullName": "Sen. Rosen, Jacky [D-NV]",
      "isOriginalCosponsor": "False",
      "lastName": "Rosen",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
      "state": "NV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "False",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-12-01",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2950\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Cornyn (for himself and Mrs. Shaheen ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo require the Secretary of State and relevant executive branch agencies to address international scam compounds defrauding people in the United States, to hold significant transnational criminal organizations accountable, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scam Compound Accountability and Mobilization Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ntransnational cyber-enabled fraud, particularly perpetrated from scam compounds in Southeast Asia, is a growing threat to citizens of the United States, national security, and economic interests globally, with the Federal Bureau of Investigation reporting $13,700,000,000 in losses in the United States due to cyber-enabled fraud in 2024, including schemes commonly perpetrated by significant transnational criminal organizations operating scam compounds;\n**(2)**\nsignificant transnational criminal organizations responsible for a large proportion of these scam compounds are affiliated with the People\u2019s Republic of China (PRC), actively spread PRC propaganda, promote unification with Taiwan, and have brokered projects for the Belt and Road Initiative;\n**(3)**\nsignificant transnational criminal organizations have lured hundreds of thousands of human trafficking victims from over 40 countries to scam compounds, primarily in Burma, Cambodia, and Laos, for purposes of forced criminality;\n**(4)**\nsignificant transnational criminal organizations are expanding scam compounds internationally including in Africa, the Middle East, South Asia, and the Pacific Islands, and related money laundering, human trafficking and recruitment fraud have occurred in Europe, North America, and South America;\n**(5)**\nthe United States should redouble efforts to hold the perpetrators and enablers of scam compound operations accountable, including those involved in related money laundering, human trafficking, and recruitment fraud, by employing tools, such as targeted financial sanctions, visa restrictions, asset seizures, and forfeiture;\n**(6)**\nto effectively address cyber-enabled fraud originating from scam compounds internationally, the United States Government should work with partner governments, multilateral institutions, civil society experts, and private sector stakeholders to improve information sharing, strengthen preventative measures, raise public awareness, and increase coordination on law enforcement investigations and regulatory actions; and\n**(7)**\nsurvivors of human trafficking, including forced criminality, require victim-centered support to ensure they are not punished for offenses committed under duress.\n#### 3. Definitions\n##### (a) In general\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Financial Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Cyber-enabled fraud**\nThe term cyber-enabled fraud means the use of the internet or other technology to commit fraudulent activity, including illicitly obtaining money, property, data, identification documents, or authentication features, or creating counterfeit goods or services.\n**(3) Enabling country**\nThe term enabling country means a country where\u2014\n**(A)**\ngovernment authorities actively or implicitly permit, enable, or perpetuate scam compound operations; or\n**(B)**\nineffective law enforcement or a failure to enact legislation intended to prevent facilitating services from reaching scam compounds or significant transnational criminal organizations enables scam compound operators to obtain facilitating services.\n**(4) Forced criminality**\nThe term forced criminality means a form of forced labor for the purpose of causing the victim to engage in criminal activity, which may include cyber-enabled fraud.\n**(5) Forced labor**\nThe term forced labor has the meaning given the term severe form of trafficking in persons in section 103(11)(B) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11)(B) ).\n**(6) Relevant foreign assistance programs and diplomatic efforts**\nThe term relevant foreign assistance programs and diplomatic efforts \u2014\n**(A)**\nmeans unclassified voluntary support programs funded directly by the United States Government that provide assistance to one or more foreign countries for the purpose of combating scam compound operations and related significant transnational criminal organizations; and\n**(B)**\nexcludes intelligence activities, including activities authorized by the President and reported to Congress in accordance with section 503 of the National Security Act of 1947 ( 50 U.S.C. 3093 ).\n**(7) Human trafficking**\nThe term human trafficking has the meaning given the term severe form of trafficking in persons in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(8) Human trafficking victim**\nThe terms human trafficking victim and victim of human trafficking mean a person subject to an act or practice described in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(9) Impacted country**\nThe term impacted country means a country that is a significant\u2014\n**(A)**\ntransit location for victims of human trafficking to scam compounds;\n**(B)**\nsource location for victims of human trafficking for scam compounds; or\n**(C)**\ntarget of cyber-enabled fraud originating from scam compounds internationally.\n**(10) Scam compound**\nThe term scam compound means a physical installation where a significant transnational criminal organization carries out cyber-enabled fraud operations, frequently using victims of human trafficking and forced criminality.\n**(11) Significant transnational criminal organization**\nThe term significant transnational criminal organization means a group of persons that\u2014\n**(A)**\nincludes one or more foreign person;\n**(B)**\nengages in or facilitates an ongoing pattern of serious criminal activity involving the jurisdictions of at least two foreign states or one foreign state and the United States; and\n**(C)**\nthreatens the national security, foreign policy, or economy of the United States.\n**(12) Strategy**\nThe term Strategy means the strategy to counter scam compounds and hold significant transnational criminal organizations accountable required under section 4.\n##### (b) Rule of construction\nThe definitions under this section are exclusive to this Act and may not be construed to affect any other provision of United States law.\n#### 4. Strategy to counter scam compounds and hold significant transnational criminal organizations accountable\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall submit to the appropriate congressional committees a comprehensive strategy that\u2014\n**(1)**\nis designed to counter scam compounds and hold significant transnational criminal organizations accountable;\n**(2)**\nis global in scope; and\n**(3)**\nmay prioritize efforts focused on Southeast Asian countries where scam compound operations are most prevalent.\n##### (b) Contents\nThe Strategy shall\u2014\n**(1)**\narticulate a comprehensive problem statement identifying the structural vulnerabilities exploited by significant transnational criminal organizations operating scam compounds;\n**(2)**\ndevelop a comprehensive list of enabling countries and impacted countries;\n**(3)**\nidentify all active executive branch relevant foreign assistance programs and diplomatic efforts underway to address scam compounds, significant transnational criminal organizations connected to scam compounds, and related money laundering, human trafficking and forced criminality, including efforts with enabling countries and impacted countries;\n**(4)**\nidentify relevant foreign assistance resources needed to fully implement the Strategy and any obstacles to the response of the Federal Government to scam compounds, including coordination with partner governments, to address the human trafficking, including forced criminality, and money laundering that facilitates and sustains scam compound operations;\n**(5)**\ninclude objectives, activities, and performance indicators regarding the response of the Federal Government to scam compounds, including\u2014\n**(A)**\nthe prevention of recruitment fraud and human trafficking, including by\u2014\n**(i)**\nengaging private sector entities operating internet platforms or other services that can be abused or exploited to perpetrate recruitment fraud, human trafficking or cyber-enabled fraud;\n**(ii)**\nraising awareness among at-risk populations to identify common recruitment fraud strategies and improve due diligence and self-protection measures;\n**(iii)**\nurging governments to monitor and enforce laws against fraudulent and unlawful recruitment practices; and\n**(iv)**\nsharing information and building awareness among foreign counterparts, including law enforcement and border officials, to identify potential human trafficking victims;\n**(B)**\nthe support for survivors of human trafficking and forced criminality under the direction of the Ambassador at Large to Monitor and Combat Trafficking in Persons;\n**(C)**\nthe enhancement of coordination and strengthening the capabilities of partner governments and law enforcement agencies;\n**(D)**\nthe use of sanctions, visa restrictions, and other accountability measures against enabling countries, significant transnational criminal organizations, and related third-party facilitators of scam compound operations;\n**(E)**\nthe support of partner governments in countering corruption and money laundering related to scam compound operations; and\n**(F)**\nthe investigation of PRC connections to significant transnational criminal organizations operating scam compounds.\n##### (c) Limitation\nNothing in the Strategy may affect, apply to, or create obligations related to past, present, or future criminal or civil law enforcement or intelligence activities of the United States or the law enforcement activities of any State or subdivision of a State.\n#### 5. Establishing a task force to implement the strategy\n##### (a) In general\nNot later than 90 days after submitting the Strategy pursuant to section 4(a), the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall establish an interagency task force (referred to in this section as the Task Force )\u2014\n**(1)**\nto coordinate the implementation of the Strategy;\n**(2)**\nto conduct regular monitoring and analysis of scam compound operations internationally;\n**(3)**\nto track and evaluate progress toward the objectives, activities, and performance indicators of the Strategy described in section 4(b)(5); and\n**(4)**\nto update the Strategy, in consultation with the appropriate congressional committees, as needed.\n##### (b) Annual reviews and reports\nNot later than one year after the establishment of the Task Force, and not less frequently than annually thereafter, the Secretary of State and the Attorney General, in consultation with the Secretary of the Treasury and the heads of other Federal departments and agencies, shall\u2014\n**(1)**\nconduct a status review of the Strategy and the overall state of scam compounds operated by significant transnational criminal organizations;\n**(2)**\ninclude a list of enabling countries and impacted countries; and\n**(3)**\nsubmit the results of such review in a public report to the appropriate congressional committees, which may contain a classified annex.\n##### (c) Task force termination\nThe Task Force shall terminate on the date that is six years after the date on which it is established.\n#### 6. Strengthening tools to dismantle scam compounds and hold significant transnational criminal organizations accountable\n##### (a) Imposition of sanctions with respect to significant actors in scam compound operations\nBeginning on and after the date that is 180 days after the date of the enactment of this Act, the President may impose the sanctions described in subsection (b) with respect to any foreign person that the President determines\u2014\n**(1)**\nhas materially assisted in, or provided significant financial or technological support to, or provided significant goods or services in support of, the activities of international scam compounds or enabling services, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money laundering; or\n**(2)**\nowned, controlled, directed, or acted for, or on behalf of, a significant scam compound operation or enabling service, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money laundering.\n##### (b) Sanctions described\nThe President may exercise of all powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), including, to the extent appropriate, the vessel of which the person is the beneficial owner, if such property or interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person who violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n##### (d) Intelligence and law enforcement activities\nSanctions authorized under this section shall not apply with respect to\u2014\n**(1)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(2)**\nany authorized intelligence or law enforcement activities of the United States.\n##### (e) Semiannual report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit a report to the appropriate congressional committees that\u2014\n**(1)**\nidentifies all foreign persons the President has sanctioned pursuant to the authorities under this section; and\n**(2)**\nthe dates on which sanctions were imposed.\n##### (f) Exception relating to importation of goods\n**(1) In general**\nA requirement to block and prohibit all transactions in all property and interests in property pursuant to subsection (b) shall not include the authority or a requirement to impose sanctions on the importation of goods.\n**(2) Defined term**\nIn this subsection, the term good means any article, natural or manmade substance, material, supply, or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (g) Waiver\n**(1) In general**\nThe President may waive the application of sanctions under this section with respect to a foreign person or a foreign financial institution if the President determines that such waiver is in the national interest of the United States.\n**(2) Report**\nNot later than 15 days before granting a waiver pursuant to paragraph (1), the President shall submit a report to the appropriate congressional committees that includes\u2014\n**(A)**\nthe name of the individual or institution that is benefitting from such waiver; and\n**(B)**\nif the beneficiary is an individual, a detailed justification explaining how the waiver serves the national security interests of the United States.\n#### 7. Sunset\nThis Act shall cease to be effective beginning on the date that is 7 years after the date of the enactment of this Act.",
      "versionDate": "2025-09-30",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950rs.xml",
      "text": "II\nCalendar No. 244\n119th CONGRESS\n1st Session\nS. 2950\nIN THE SENATE OF THE UNITED STATES\nSeptember 30, 2025 Mr. Cornyn (for himself, Mrs. Shaheen , Mr. Scott of Florida , Ms. Duckworth , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nOctober 30, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo require the Secretary of State and relevant executive branch agencies to address international scam compounds defrauding people in the United States, to hold significant transnational criminal organizations accountable, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scam Compound Accountability and Mobilization Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ntransnational cyber-enabled fraud, particularly perpetrated from scam compounds in Southeast Asia, is a growing threat to citizens of the United States, national security, and economic interests globally, with the Federal Bureau of Investigation reporting $13,700,000,000 in losses in the United States due to cyber-enabled fraud in 2024, including schemes commonly perpetrated by significant transnational criminal organizations operating scam compounds;\n**(2)**\nsignificant transnational criminal organizations responsible for a large proportion of these scam compounds are affiliated with the People\u2019s Republic of China (PRC), actively spread PRC propaganda, promote unification with Taiwan, and have brokered projects for the Belt and Road Initiative;\n**(3)**\nsignificant transnational criminal organizations have lured hundreds of thousands of human trafficking victims from over 40 countries to scam compounds, primarily in Burma, Cambodia, and Laos, for purposes of forced criminality;\n**(4)**\nsignificant transnational criminal organizations are expanding scam compounds internationally including in Africa, the Middle East, South Asia, and the Pacific Islands, and related money laundering, human trafficking and recruitment fraud have occurred in Europe, North America, and South America;\n**(5)**\nthe United States should redouble efforts to hold the perpetrators and enablers of scam compound operations accountable, including those involved in related money laundering, human trafficking, and recruitment fraud, by employing tools, such as targeted financial sanctions, visa restrictions, asset seizures, and forfeiture;\n**(6)**\nto effectively address cyber-enabled fraud originating from scam compounds internationally, the United States Government should work with partner governments, multilateral institutions, civil society experts, and private sector stakeholders to improve information sharing, strengthen preventative measures, raise public awareness, and increase coordination on law enforcement investigations and regulatory actions; and\n**(7)**\nsurvivors of human trafficking, including forced criminality, require victim-centered support to ensure they are not punished for offenses committed under duress.\n#### 3. Definitions\n##### (a) In general\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Financial Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Cyber-enabled fraud**\nThe term cyber-enabled fraud means the use of the internet or other technology to commit fraudulent activity, including illicitly obtaining money, property, data, identification documents, or authentication features, or creating counterfeit goods or services.\n**(3) Enabling country**\nThe term enabling country means a country where\u2014\n**(A)**\ngovernment authorities actively or implicitly permit, enable, or perpetuate scam compound operations; or\n**(B)**\nineffective law enforcement or a failure to enact legislation intended to prevent facilitating services from reaching scam compounds or significant transnational criminal organizations enables scam compound operators to obtain facilitating services.\n**(4) Forced criminality**\nThe term forced criminality means a form of forced labor for the purpose of causing the victim to engage in criminal activity, which may include cyber-enabled fraud.\n**(5) Forced labor**\nThe term forced labor has the meaning given the term severe form of trafficking in persons in section 103(11)(B) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11)(B) ).\n**(6) Relevant foreign assistance programs and diplomatic efforts**\nThe term relevant foreign assistance programs and diplomatic efforts \u2014\n**(A)**\nmeans unclassified voluntary support programs funded directly by the United States Government that provide assistance to one or more foreign countries for the purpose of combating scam compound operations and related significant transnational criminal organizations; and\n**(B)**\nexcludes intelligence activities, including activities authorized by the President and reported to Congress in accordance with section 503 of the National Security Act of 1947 ( 50 U.S.C. 3093 ).\n**(7) Human trafficking**\nThe term human trafficking has the meaning given the term severe form of trafficking in persons in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(8) Human trafficking victim**\nThe terms human trafficking victim and victim of human trafficking mean a person subject to an act or practice described in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(9) Impacted country**\nThe term impacted country means a country that is a significant\u2014\n**(A)**\ntransit location for victims of human trafficking to scam compounds;\n**(B)**\nsource location for victims of human trafficking for scam compounds; or\n**(C)**\ntarget of cyber-enabled fraud originating from scam compounds internationally.\n**(10) Scam compound**\nThe term scam compound means a physical installation where a significant transnational criminal organization carries out cyber-enabled fraud operations, frequently using victims of human trafficking and forced criminality.\n**(11) Significant transnational criminal organization**\nThe term significant transnational criminal organization means a group of persons that\u2014\n**(A)**\nincludes one or more foreign person;\n**(B)**\nengages in or facilitates an ongoing pattern of serious criminal activity involving the jurisdictions of at least two foreign states or one foreign state and the United States; and\n**(C)**\nthreatens the national security, foreign policy, or economy of the United States.\n**(12) Strategy**\nThe term Strategy means the strategy to counter scam compounds and hold significant transnational criminal organizations accountable required under section 4.\n##### (b) Rule of construction\nThe definitions under this section are exclusive to this Act and may not be construed to affect any other provision of United States law.\n#### 4. Strategy to counter scam compounds and hold significant transnational criminal organizations accountable\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall submit to the appropriate congressional committees a comprehensive strategy that\u2014\n**(1)**\nis designed to counter scam compounds and hold significant transnational criminal organizations accountable;\n**(2)**\nis global in scope; and\n**(3)**\nmay prioritize efforts focused on Southeast Asian countries where scam compound operations are most prevalent.\n##### (b) Contents\nThe Strategy shall\u2014\n**(1)**\narticulate a comprehensive problem statement identifying the structural vulnerabilities exploited by significant transnational criminal organizations operating scam compounds;\n**(2)**\ndevelop a comprehensive list of enabling countries and impacted countries;\n**(3)**\nidentify all active executive branch relevant foreign assistance programs and diplomatic efforts underway to address scam compounds, significant transnational criminal organizations connected to scam compounds, and related money laundering, human trafficking and forced criminality, including efforts with enabling countries and impacted countries;\n**(4)**\nidentify relevant foreign assistance resources needed to fully implement the Strategy and any obstacles to the response of the Federal Government to scam compounds, including coordination with partner governments, to address the human trafficking, including forced criminality, and money laundering that facilitates and sustains scam compound operations;\n**(5)**\ninclude objectives, activities, and performance indicators regarding the response of the Federal Government to scam compounds, including\u2014\n**(A)**\nthe prevention of recruitment fraud and human trafficking, including by\u2014\n**(i)**\nengaging private sector entities operating internet platforms or other services that can be abused or exploited to perpetrate recruitment fraud, human trafficking or cyber-enabled fraud;\n**(ii)**\nraising awareness among at-risk populations to identify common recruitment fraud strategies and improve due diligence and self-protection measures;\n**(iii)**\nurging governments to monitor and enforce laws against fraudulent and unlawful recruitment practices; and\n**(iv)**\nsharing information and building awareness among foreign counterparts, including law enforcement and border officials, to identify potential human trafficking victims;\n**(B)**\nthe support for survivors of human trafficking and forced criminality under the direction of the Ambassador at Large to Monitor and Combat Trafficking in Persons;\n**(C)**\nthe enhancement of coordination and strengthening the capabilities of partner governments and law enforcement agencies;\n**(D)**\nthe use of sanctions, visa restrictions, and other accountability measures against enabling countries, significant transnational criminal organizations, and related third-party facilitators of scam compound operations;\n**(E)**\nthe support of partner governments in countering corruption and money laundering related to scam compound operations; and\n**(F)**\nthe investigation of PRC connections to significant transnational criminal organizations operating scam compounds.\n##### (c) Limitation\nNothing in the Strategy may affect, apply to, or create obligations related to past, present, or future criminal or civil law enforcement or intelligence activities of the United States or the law enforcement activities of any State or subdivision of a State.\n#### 5. Establishing a task force to implement the strategy\n##### (a) In general\nNot later than 90 days after submitting the Strategy pursuant to section 4(a), the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall establish an interagency task force (referred to in this section as the Task Force )\u2014\n**(1)**\nto coordinate the implementation of the Strategy;\n**(2)**\nto conduct regular monitoring and analysis of scam compound operations internationally;\n**(3)**\nto track and evaluate progress toward the objectives, activities, and performance indicators of the Strategy described in section 4(b)(5); and\n**(4)**\nto update the Strategy, in consultation with the appropriate congressional committees, as needed.\n##### (b) Annual reviews and reports\nNot later than one year after the establishment of the Task Force, and not less frequently than annually thereafter, the Secretary of State and the Attorney General, in consultation with the Secretary of the Treasury and the heads of other Federal departments and agencies, shall\u2014\n**(1)**\nconduct a status review of the Strategy and the overall state of scam compounds operated by significant transnational criminal organizations;\n**(2)**\ninclude a list of enabling countries and impacted countries; and\n**(3)**\nsubmit the results of such review in a public report to the appropriate congressional committees, which may contain a classified annex.\n##### (c) Task force termination\nThe Task Force shall terminate on the date that is six years after the date on which it is established.\n#### 6. Strengthening tools to dismantle scam compounds and hold significant transnational criminal organizations accountable\n##### (a) Imposition of sanctions with respect to significant actors in scam compound operations\nBeginning on and after the date that is 180 days after the date of the enactment of this Act, the President may impose the sanctions described in subsection (b) with respect to any foreign person that the President determines\u2014\n**(1)**\nhas materially assisted in, or provided significant financial or technological support to, or provided significant goods or services in support of, the activities of international scam compounds or enabling services, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money laundering; or\n**(2)**\nowned, controlled, directed, or acted for, or on behalf of, a significant scam compound operation or enabling service, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money laundering.\n##### (b) Sanctions described\nThe President may exercise of all powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), including, to the extent appropriate, the vessel of which the person is the beneficial owner, if such property or interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person who violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n##### (d) Intelligence and law enforcement activities\nSanctions authorized under this section shall not apply with respect to\u2014\n**(1)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(2)**\nany authorized intelligence or law enforcement activities of the United States.\n##### (e) Semiannual report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit a report to the appropriate congressional committees that\u2014\n**(1)**\nidentifies all foreign persons the President has sanctioned pursuant to the authorities under this section; and\n**(2)**\nthe dates on which sanctions were imposed.\n##### (f) Exception relating to importation of goods\n**(1) In general**\nA requirement to block and prohibit all transactions in all property and interests in property pursuant to subsection (b) shall not include the authority or a requirement to impose sanctions on the importation of goods.\n**(2) Defined term**\nIn this subsection, the term good means any article, natural or manmade substance, material, supply, or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (g) Waiver\n**(1) In general**\nThe President may waive the application of sanctions under this section with respect to a foreign person or a foreign financial institution if the President determines that such waiver is in the national interest of the United States.\n**(2) Report**\nNot later than 15 days before granting a waiver pursuant to paragraph (1), the President shall submit a report to the appropriate congressional committees that includes\u2014\n**(A)**\nthe name of the individual or institution that is benefitting from such waiver; and\n**(B)**\nif the beneficiary is an individual, a detailed justification explaining how the waiver serves the national security interests of the United States.\n#### 7. Sunset\nThis Act shall cease to be effective beginning on the date that is 7 years after the date of the enactment of this Act.",
      "versionDate": "2025-10-30",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950es.xml",
      "text": "119th CONGRESS\n1st Session\nS. 2950\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo require the Secretary of State and relevant executive branch agencies to address international scam compounds defrauding people in the United States, to hold significant transnational criminal organizations accountable, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Scam Compound Accountability and Mobilization Act .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\ntransnational cyber-enabled fraud, particularly perpetrated from scam compounds in Southeast Asia, is a growing threat to citizens of the United States, national security, and economic interests globally, with the Federal Bureau of Investigation reporting $13,700,000,000 in losses in the United States due to cyber-enabled fraud in 2024, including schemes commonly perpetrated by significant transnational criminal organizations operating scam compounds;\n**(2)**\nsignificant transnational criminal organizations responsible for a large proportion of these scam compounds are affiliated with the People\u2019s Republic of China (PRC), actively spread PRC propaganda, promote unification with Taiwan, and have brokered projects for the Belt and Road Initiative;\n**(3)**\nsignificant transnational criminal organizations have lured hundreds of thousands of human trafficking victims from over 40 countries to scam compounds, primarily in Burma, Cambodia, and Laos, for purposes of forced criminality;\n**(4)**\nsignificant transnational criminal organizations are expanding scam compounds internationally including in Africa, the Middle East, South Asia, and the Pacific Islands, and related money laundering, human trafficking and recruitment fraud have occurred in Europe, North America, and South America;\n**(5)**\nthe United States should redouble efforts to hold the perpetrators and enablers of scam compound operations accountable, including those involved in related money laundering, human trafficking, and recruitment fraud, by employing tools, such as targeted financial sanctions, visa restrictions, asset seizures, and forfeiture;\n**(6)**\nto effectively address cyber-enabled fraud originating from scam compounds internationally, the United States Government should work with partner governments, multilateral institutions, civil society experts, and private sector stakeholders to improve information sharing, strengthen preventative measures, raise public awareness, and increase coordination on law enforcement investigations and regulatory actions; and\n**(7)**\nsurvivors of human trafficking, including forced criminality, require victim-centered support to ensure they are not punished for offenses committed under duress.\n#### 3. Definitions\n##### (a) In general\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on the Judiciary of the Senate ;\n**(C)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(D)**\nthe Select Committee on Intelligence of the Senate ;\n**(E)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(F)**\nthe Committee on the Judiciary of the House of Representatives ;\n**(G)**\nthe Committee on Financial Services of the House of Representatives ; and\n**(H)**\nthe Permanent Select Committee on Intelligence of the House of Representatives .\n**(2) Cyber-enabled fraud**\nThe term cyber-enabled fraud means the use of the internet or other technology to commit fraudulent activity, including illicitly obtaining money, property, data, identification documents, or authentication features, or creating counterfeit goods or services.\n**(3) Enabling country**\nThe term enabling country means a country where\u2014\n**(A)**\ngovernment authorities actively or implicitly permit, enable, or perpetuate scam compound operations; or\n**(B)**\nineffective law enforcement or a failure to enact legislation intended to prevent facilitating services from reaching scam compounds or significant transnational criminal organizations enables scam compound operators to obtain facilitating services.\n**(4) Forced criminality**\nThe term forced criminality means a form of forced labor for the purpose of causing the victim to engage in criminal activity, which may include cyber-enabled fraud.\n**(5) Forced labor**\nThe term forced labor has the meaning given the term severe form of trafficking in persons in section 103(11)(B) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11)(B) ).\n**(6) Relevant foreign assistance programs and diplomatic efforts**\nThe term relevant foreign assistance programs and diplomatic efforts \u2014\n**(A)**\nmeans unclassified voluntary support programs funded directly by the United States Government that provide assistance to one or more foreign countries for the purpose of combating scam compound operations and related significant transnational criminal organizations; and\n**(B)**\nexcludes intelligence activities, including activities authorized by the President and reported to Congress in accordance with section 503 of the National Security Act of 1947 ( 50 U.S.C. 3093 ).\n**(7) Human trafficking**\nThe term human trafficking has the meaning given the term severe form of trafficking in persons in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(8) Human trafficking victim**\nThe terms human trafficking victim and victim of human trafficking mean a person subject to an act or practice described in section 103(11) of the Trafficking Victims Protection Act of 2000 ( 22 U.S.C. 7102(11) ).\n**(9) Impacted country**\nThe term impacted country means a country that is a significant\u2014\n**(A)**\ntransit location for victims of human trafficking to scam compounds;\n**(B)**\nsource location for victims of human trafficking for scam compounds; or\n**(C)**\ntarget of cyber-enabled fraud originating from scam compounds internationally.\n**(10) Scam compound**\nThe term scam compound means a physical installation where a significant transnational criminal organization carries out cyber-enabled fraud operations, frequently using victims of human trafficking and forced criminality.\n**(11) Significant transnational criminal organization**\nThe term significant transnational criminal organization means a group of persons that\u2014\n**(A)**\nincludes one or more foreign person;\n**(B)**\nengages in or facilitates an ongoing pattern of serious criminal activity involving the jurisdictions of at least two foreign states or one foreign state and the United States; and\n**(C)**\nthreatens the national security, foreign policy, or economy of the United States.\n**(12) Strategy**\nThe term Strategy means the strategy to counter scam compounds and hold significant transnational criminal organizations accountable required under section 4.\n##### (b) Rule of construction\nThe definitions under this section are exclusive to this Act and may not be construed to affect any other provision of United States law.\n#### 4. Strategy to counter scam compounds and hold significant transnational criminal organizations accountable\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall submit to the appropriate congressional committees a comprehensive strategy that\u2014\n**(1)**\nis designed to counter scam compounds and hold significant transnational criminal organizations accountable;\n**(2)**\nis global in scope; and\n**(3)**\nmay prioritize efforts focused on Southeast Asian countries where scam compound operations are most prevalent.\n##### (b) Contents\nThe Strategy shall\u2014\n**(1)**\narticulate a comprehensive problem statement identifying the structural vulnerabilities exploited by significant transnational criminal organizations operating scam compounds;\n**(2)**\ndevelop a comprehensive list of enabling countries and impacted countries;\n**(3)**\nidentify all active executive branch relevant foreign assistance programs and diplomatic efforts underway to address scam compounds, significant transnational criminal organizations connected to scam compounds, and related money laundering, human trafficking and forced criminality, including efforts with enabling countries and impacted countries;\n**(4)**\nidentify relevant foreign assistance resources needed to fully implement the Strategy and any obstacles to the response of the Federal Government to scam compounds, including coordination with partner governments, to address the human trafficking, including forced criminality, and money laundering that facilitates and sustains scam compound operations;\n**(5)**\ninclude objectives, activities, and performance indicators regarding the response of the Federal government to scam compounds, including\u2014\n**(A)**\nthe prevention of recruitment fraud and human trafficking, including by\u2014\n**(i)**\nengaging private sector entities operating internet platforms or other services that can be abused or exploited to perpetrate recruitment fraud, human trafficking or cyber-enabled fraud;\n**(ii)**\nraising awareness among at-risk populations to identify common recruitment fraud strategies and improve due diligence and self-protection measures;\n**(iii)**\nurging governments to monitor and enforce laws against fraudulent and unlawful recruitment practices; and\n**(iv)**\nsharing information and building awareness among foreign counterparts, including law enforcement and border officials, to identify potential human trafficking victims;\n**(B)**\nthe support for survivors of human trafficking and forced criminality under the direction of the Ambassador at Large to Monitor and Combat Trafficking in Persons;\n**(C)**\nthe enhancement of coordination and strengthening the capabilities of partner governments and law enforcement agencies;\n**(D)**\nthe use of sanctions, visa restrictions, and other accountability measures against enabling countries, significant transnational criminal organizations, and related third-party facilitators of scam compound operations;\n**(E)**\nthe support of partner governments in countering corruption and money laundering related to scam compound operations; and\n**(F)**\nthe investigation of PRC connections to significant transnational criminal organizations operating scam compounds.\n##### (c) Limitation\nNothing in the Strategy may affect, apply to, or create obligations related to past, present, or future criminal or civil law enforcement or intelligence activities of the United States or the law enforcement activities of any State or subdivision of a State.\n#### 5. Establishing a task force to implement the strategy\n##### (a) In general\nNot later than 90 days after submitting the Strategy pursuant to section 4(a), the Secretary of State, in consultation with the Attorney General, the Secretary of the Treasury, and the heads of other Federal departments and agencies, shall establish an interagency task force (referred to in this section as the Task Force )\u2014\n**(1)**\nto coordinate the implementation of the Strategy;\n**(2)**\nto conduct regular monitoring and analysis of scam compound operations internationally;\n**(3)**\nto track and evaluate progress toward the objectives, activities, and performance indicators of the Strategy described in section 4(b)(5); and\n**(4)**\nto update the Strategy, in consultation with the appropriate congressional committees, as needed.\n##### (b) Annual reviews and reports\nNot later than one year after the establishment of the Task Force, and not less frequently than annually thereafter, the Secretary of State and the Attorney General, in consultation with the Secretary of the Treasury and the heads of other Federal departments and agencies, shall\u2014\n**(1)**\nconduct a status review of the Strategy and the overall state of scam compounds operated by significant transnational criminal organizations;\n**(2)**\ninclude a list of enabling countries and impacted countries; and\n**(3)**\nsubmit the results of such review in a public report to the appropriate congressional committees, which may contain a classified annex.\n##### (c) Task force termination\nThe Task Force shall terminate on the date that is six years after the date on which it is established.\n#### 6. Strengthening tools to dismantle scam compounds and hold significant transnational criminal organizations accountable\n##### (a) Imposition of sanctions with respect to significant actors in scam compound operations\nBeginning on and after the date that is 180 days after the date of the enactment of this Act, the President may impose the sanctions described in subsection (b) with respect to any foreign person that the President determines\u2014\n**(1)**\nhas materially assisted in, or provided significant financial or technological support to, or provided significant goods or services in support of, the activities of international scam compounds or enabling services, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money-laundering; or\n**(2)**\nowned, controlled, directed, or acted for, or on behalf of, a significant scam compound operation or enabling service, including recruitment fraud, human trafficking (including forced criminality), cyber-enabled fraud, or money-laundering.\n##### (b) Sanctions described\nThe President may exercise of all powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), including, to the extent appropriate, the vessel of which the person is the beneficial owner, if such property or interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n##### (c) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nThe penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) shall apply to any person who violates, attempts to violate, conspires to violate, or causes a violation of any prohibition of this section, or an order or regulation prescribed under this section, to the same extent that such penalties apply to a person that commits an unlawful act described in section 206(a) of such Act ( 50 U.S.C. 1705(a) ).\n##### (d) Intelligence and law enforcement activities\nSanctions authorized under this section shall not apply with respect to\u2014\n**(1)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(2)**\nany authorized intelligence or law enforcement activities of the United States.\n##### (e) Semiannual report\nNot later than 180 days after the date of the enactment of this Act, and every 180 days thereafter, the President shall submit a report to the appropriate congressional committees that\u2014\n**(1)**\nidentifies all foreign persons the President has sanctioned pursuant to the authorities under this section; and\n**(2)**\nthe dates on which sanctions were imposed.\n##### (f) Exception relating to importation of goods\n**(1) In general**\nA requirement to block and prohibit all transactions in all property and interests in property pursuant to subsection (b) shall not include the authority or a requirement to impose sanctions on the importation of goods.\n**(2) Defined term**\nIn this subsection, the term good means any article, natural or manmade substance, material, supply, or manufactured product, including inspection and test equipment, and excluding technical data.\n##### (g) Waiver\n**(1) In general**\nThe President may waive the application of sanctions under this section with respect to a foreign person or a foreign financial institution if the President determines that such waiver is in the national interest of the United States.\n**(2) Report**\nNot later than 15 days before granting a waiver pursuant to paragraph (1), the President shall submit a report to the appropriate congressional committees that includes\u2014\n**(A)**\nthe name of the individual or institution that is benefitting from such waiver; and\n**(B)**\nif the beneficiary is an individual, a detailed justification explaining how the waiver serves the national security interests of the United States.\n#### 7. Redress to victims of international scam compound operations\nNot later than 90 days after the date of the enactment of this Act, the Attorney General, in consultation with the Secretary of State, the Secretary of the Treasury, and the heads of other appropriate Federal departments and agencies, shall submit to the appropriate congressional committees a report containing an assessment of existing forfeiture law that\u2014\n**(1)**\noutlines challenges or limitations to providing financial redress to victims of international scam compound operations;\n**(2)**\noffers recommendations to amend existing forfeiture law to enable the Department of Justice to use assets forfeited as a result of law enforcement activities targeting international scam compound operations to provide financial redress to United States citizen victims of scam operations; and\n**(3)**\noffers recommendations for the administration of such a redress mechanism.\n#### 8. Sunset\nThis Act shall cease to be effective beginning on the date that is 7 years after the date of the enactment of this Act.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-01-05T17:07:53Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-01-05T17:08:00Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T17:12:35Z"
          },
          {
            "name": "Crime victims",
            "updateDate": "2026-01-05T17:12:50Z"
          },
          {
            "name": "Criminal investigation, prosecution, interrogation",
            "updateDate": "2026-01-05T17:09:19Z"
          },
          {
            "name": "Fraud offenses and financial crimes",
            "updateDate": "2026-01-05T17:05:22Z"
          },
          {
            "name": "Human trafficking",
            "updateDate": "2026-01-05T17:06:51Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2026-01-05T17:10:33Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-01-05T17:10:45Z"
          },
          {
            "name": "Organized crime",
            "updateDate": "2026-01-05T17:05:35Z"
          },
          {
            "name": "Subversive activities",
            "updateDate": "2026-01-05T17:08:58Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-11-19T21:18:19Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-10-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2950es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Scam Compound Accountability and Mobilization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-10T12:03:19Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Scam Compound Accountability and Mobilization Act",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2025-12-09T10:08:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Scam Compound Accountability and Mobilization Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-11-01T03:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Scam Compound Accountability and Mobilization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-11T02:38:12Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Secretary of State and relevant executive branch agencies to address international scam compounds defrauding people in the United States, to hold significant transnational criminal organizations accountable, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-11T02:33:14Z"
    }
  ]
}
```
