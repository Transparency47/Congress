# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1478?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1478
- Title: Countering Wrongful Detention Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1478
- Origin chamber: Senate
- Introduced date: 2025-04-10
- Update date: 2025-12-19T12:03:16Z
- Update date including text: 2025-12-19T12:03:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-10: Introduced in Senate
- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 94.
- Latest action: 2025-04-10: Introduced in Senate

## Actions

- 2025-04-10 - IntroReferral: Introduced in Senate
- 2025-04-10 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 94.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-10",
    "latestAction": {
      "actionDate": "2025-04-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1478",
    "number": "1478",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "R000584",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Risch, James E. [R-ID]",
        "lastName": "Risch",
        "party": "R",
        "state": "ID"
      }
    ],
    "title": "Countering Wrongful Detention Act of 2025",
    "type": "S",
    "updateDate": "2025-12-19T12:03:16Z",
    "updateDateIncludingText": "2025-12-19T12:03:16Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 94.",
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
      "actionDate": "2025-04-10",
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
      "actionDate": "2025-04-10",
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
            "date": "2025-06-18T18:14:46Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-10T20:16:10Z",
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
      "sponsorshipDate": "2025-04-10",
      "state": "DE"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1478is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1478\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Risch (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo provide the United States Government with additional tools to deter state and non-state actors from wrongfully detaining United States nationals for political leverage, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Countering Wrongful Detention Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Deterring and preventing unlawful or wrongful detention\nSec. 101. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention.\nSec. 102. Required certification regarding international travel advisories.\nTITLE II\u2014Strengthening processes and services for hostages and unlawful or wrongful detainees\nSec. 201. Advisory Council on Hostage Taking and Unlawful or Wrongful Detention.\nSec. 202. Congressional Report on Components Related to Hostage Affairs and Recovery.\nI\nDeterring and preventing unlawful or wrongful detention\n#### 101. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ) is amended by inserting after section 306 the following:\n306A. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention (a) In general Subject to the notice requirement of subsection (c)(1)(A), the Secretary of State, in consultation with the heads of other relevant Federal agencies, may designate a foreign country that has provided support for or directly engaged in the unlawful or wrongful detention of a United States national as a State Sponsor of Unlawful or Wrongful Detention based on any of the following criteria: (1) The unlawful or wrongful detention of a United States national occurs in the foreign country. (2) The government of the foreign country or an entity organized under the laws of a foreign country has failed to release an unlawfully or wrongfully detained United States national within 30 days of being officially notified by the Department of State of the unlawful or wrongful detention. (3) Actions taken by the government of the foreign country indicate that the government is responsible for, complicit in, or materially supports the unlawful or wrongful detention of a United States national, including by acting as described in paragraph (2) after having been notified by the Department of State. (4) The actions of a state or nonstate actor in the foreign country, including any previous action relating to unlawful or wrongful detention or hostage taking of a United States national, pose a risk to the safety and security of United States nationals abroad sufficient to warrant designation of the foreign country as a State Sponsor of Unlawful or Wrongful Detention, as determined by the Secretary. (b) Termination of designation The Secretary of State may terminate the designation of a foreign country under subsection (a) if the Secretary certifies to Congress that the government of the foreign country\u2014 (1) has released the United States nationals unlawfully or wrongfully detained within the territory of the foreign country; (2) has positively contributed to the release of United States nationals taken hostage within the territory of the foreign country or from the custody of a nonstate entity; (3) has demonstrated changes in leadership or policies with respect to unlawful or wrongful detention and hostage taking; or (4) has provided assurances that the government of the foreign country will not engage or be complicit in or support acts described in subsection (a). (c) Briefing and reports to Congress; publication (1) Reports to Congress (A) In general Not later than 7 days prior to making a designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State shall submit to the appropriate committees of Congress a report that notifies the committees of the proposed designation. (B) Elements In each report submitted under subparagraph (A) with respect to the designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention, the Secretary shall include\u2014 (i) the justification for the designation; and (ii) a description of any action taken by the United States Government, including the Secretary of State or the head of any other relevant Federal agency, in response to the designation to deter the unlawful or wrongful detention or hostage-taking of foreign nationals in the country. (2) Initial briefing required Not later than 60 days after the date of the enactment of this section, the Secretary shall brief Congress on the following: (A) Whether any of the following countries should be designated as a State Sponsor of Unlawful or Wrongful Detention under subsection (a): (i) Afghanistan. (ii) Eritrea. (iii) The Islamic Republic of Iran. (iv) The People's Republic of China. (v) The Russian Federation. (vi) The Syrian Arab Republic or any transitional government therein. (vii) Venezuela under the regime of Nicol\u00e1s Maduro. (viii) The Republic of Belarus. (B) The steps taken by the Secretary and the heads of other relevant Federal agencies to deter the unlawful and wrongful detention of United States nationals and to respond to such detentions, including\u2014 (i) any engagement with private sector companies to optimize the distribution of travel advisories; and (ii) any engagement with private companies responsible for promoting travel to foreign countries engaged in the unlawful or wrongful detention of United States nationals. (C) An assessment of a possible expansion of chapter 97 of title 28, United States Code (commonly known as the Foreign Sovereign Immunities Act of 1976 ) to include an exception from asset seizure immunity for State Sponsors of Unlawful or Wrongful Detention. (D) A detailed plan on the manner by which a geographic travel restriction could be instituted against State Sponsors of Unlawful or Wrongful Detention. (E) The progress made in multilateral fora, including the United Nations and other international organizations, to address the unlawful and wrongful detention of United States nationals, in addition to nationals of partners and allies of the United States in foreign countries. (3) Annual briefing Not later than one year after the date of the enactment of this section, and annually thereafter for 5 years, the Assistant Secretary of State for Consular Affairs and the Special Presidential Envoy for Hostage Affairs shall brief the appropriate committees of Congress with respect to unlawful or wrongful detentions taking place in the countries listed under paragraph (2)(A) and actions taken by the Secretary of State and the heads of other relevant Federal agencies to deter the wrongful detention of United States nationals, including any steps taken in accordance with paragraph (2)(B). (4) Publication The Secretary shall make available on a publicly accessible website of the Department of State, and regularly update, a list of foreign countries designated as State Sponsors of Unlawful or Wrongful Detention under subsection (a). (d) Review of available responses to state sponsors of unlawful or wrongful detention Upon designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State, in consultation with the heads of other relevant Federal agencies, shall conduct a comprehensive review of the use of existing authorities to respond to and deter the unlawful or wrongful detention of United States nationals in the foreign country, including\u2014 (1) sanctions available under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); (2) visa restrictions available under section 7031(c) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2024 (division F of Public Law 118\u201347 ; 8 U.S.C. 1182 note) or any other provision of Federal law; (3) sanctions available under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ); (4) imposition of a geographic travel restriction on citizens of the United States; (5) restrictions on assistance provided to the government of the country under the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) or any other provision of Federal law; (6) restrictions on the export of certain goods to the country under the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ), the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), or any other Federal law; and (7) designating the government of the country as a government that has repeatedly provided support for acts of international terrorism pursuant to\u2014 (A) section 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); (B) section 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); (C) section 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or (D) any other provision of law. (e) Appropriate committees of Congress defined In this paragraph, the term appropriate committees of Congress means\u2014 (1) the Committee on Foreign Relations and the Committee on Appropriations of the Senate; and (2) the Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives. (f) Rule of Construction Nothing in this section shall be construed to imply that the United States Government formally recognizes any particular country or the government of such country as legitimate. .\n#### 102. Required certification regarding international travel advisories\n##### (a) In general\nChapter 423 of title 49, United States Code, is amended by adding at the end the following new section:\n42309. Required certification regarding international travel advisories (a) In general An air carrier, foreign air carrier, or ticket agent who sells, in the United States, a ticket for foreign air transportation of a passenger to a country or other geographic area with a D or K indicator issued by the Department of State Travel Advisory System shall require the passenger listed on the ticket to certify that the passenger\u2014 (1) has reviewed the travel advisory of the Department of State applicable to such country or other geographic area; and (2) understands the risks involved with traveling to such country or other geographic area. (b) Definitions For purposes of this section: (1) D indicator The term D indicator means a travel advisory issued by the Department of State that indicates a risk of wrongful detention of a United States national. (2) K indicator The term K indicator means a travel advisory issued by the Department of State that indicates a criminal or terrorist individual or group has threatened to seize, detain, kill, or injure individuals (or has seized, detained, killed, or injured individuals) to compel a third party (including a governmental organization) to meet certain requirements as a condition of release. .\n##### (b) Clerical amendment\nThe analysis for chapter 423 of title 49, United States Code, is amended by inserting after the item relating to section 42308 the following:\n42309. Required certification regarding international travel advisories. .\nII\nStrengthening processes and services for hostages and unlawful or wrongful detainees\n#### 201. Advisory Council on Hostage-Taking and Unlawful or Wrongful Detention\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ), as amended by section 101, is further amended by inserting after section 305B the following:\n305C. Advisory Council on Hostage Taking and Unlawful or Wrongful Detention (a) Establishment The President shall establish an advisory council, to be known as the Advisory Council on Hostage Taking and Unlawful or Wrongful Detention (in this section referred to as the Advisory Council ), to advise the Special Presidential Envoy for Hostage Affairs, the Hostage Response Group, and the Hostage Recovery Fusion Cell with respect to Federal policies regarding hostage-taking and unlawful or wrongful detention. (b) Membership (1) In general The President shall invite individuals to the Advisory Council, which shall be comprised of\u2014 (A) United States nationals who have been unlawfully or wrongfully detained or taken hostage abroad; (B) family members of such United States nationals; and (C) not fewer than 2 experts on areas including hostage-taking, wrongful detention, international relations, rule of law, and counterterrorism who have been recommended by the Secretary of State. (2) Terms The term of a member of the Advisory Council shall be 3 years. (3) Compensation and travel expenses A member of the Advisory Council shall not be considered a Federal employee and shall not be compensated for service on the Advisory Council, but may be allowed travel expenses, including per diem in lieu of subsistence, in accordance with subchapter I of chapter 57 of title 5, United States Code. (c) Annual reports Not later than 1 year after the date of the enactment of this section, and annually thereafter, the Advisory Council shall submit to the President and the appropriate congressional committees a report setting forth the recommendations of the Advisory Council. (d) Termination The Advisory Council shall terminate on the date that is 10 years after the date of the enactment of this section. .\n#### 202. Congressional Report on Components Related to Hostage Affairs and Recovery\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the President shall submit to Congress a report on the following:\n**(1)**\nThe Hostage Response Group established pursuant to section 305(a) of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741c(a) ).\n**(2)**\nThe Hostage Recovery Fusion Cell established pursuant to section 304(a) of that Act ( 22 U.S.C. 1741b(a) ).\n**(3)**\nThe Office of the Special Presidential Envoy for Hostage Affairs established pursuant to section 303(a) of that Act ( 22 U.S.C. 1741a(a) ).\n##### (b) Elements\nThe report required by subsection (a) shall include\u2014\n**(1)**\na description of the existing structure of each component listed in subsection (a);\n**(2)**\nrecommendations on how the components can be improved, including through reorganization or consolidation of the components; and\n**(3)**\ncost efficiencies on the components listed in subsection (a), including resources available to eligible former wrongful detainees and hostages and their family members.",
      "versionDate": "2025-04-10",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1478rs.xml",
      "text": "II\nCalendar No. 94\n119th CONGRESS\n1st Session\nS. 1478\nIN THE SENATE OF THE UNITED STATES\nApril 10, 2025 Mr. Risch (for himself and Mr. Coons ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo provide the United States Government with additional tools to deter state and non-state actors from wrongfully detaining United States nationals for political leverage, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Countering Wrongful Detention Act of 2025 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nTITLE I\u2014Deterring and preventing unlawful or wrongful detention\nSec. 101. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention.\nSec. 102. Required certification regarding international travel advisories.\nTITLE II\u2014Strengthening processes and services for hostages and unlawful or wrongful detainees\nSec. 201. Advisory Council on Hostage Taking and Unlawful or Wrongful Detention.\nSec. 202. Congressional Report on Components Related to Hostage Affairs and Recovery.\nI\nDeterring and preventing unlawful or wrongful detention\n#### 101. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ) is amended by inserting after section 306 the following:\n306A. Designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention (a) In general Subject to the notice requirement of subsection (c)(1)(A), the Secretary of State, in consultation with the heads of other relevant Federal agencies, may designate a foreign country that has provided support for or directly engaged in the unlawful or wrongful detention of a United States national as a State Sponsor of Unlawful or Wrongful Detention based on any of the following criteria: (1) The unlawful or wrongful detention of a United States national occurs in the foreign country. (2) The government of the foreign country or an entity organized under the laws of a foreign country has failed to release an unlawfully or wrongfully detained United States national within 30 days of being officially notified by the Department of State of the unlawful or wrongful detention. (3) Actions taken by the government of the foreign country indicate that the government is responsible for, complicit in, or materially supports the unlawful or wrongful detention of a United States national, including by acting as described in paragraph (2) after having been notified by the Department of State. (4) The actions of a state or nonstate actor in the foreign country, including any previous action relating to unlawful or wrongful detention or hostage taking of a United States national, pose a risk to the safety and security of United States nationals abroad sufficient to warrant designation of the foreign country as a State Sponsor of Unlawful or Wrongful Detention, as determined by the Secretary. (b) Termination of designation The Secretary of State may terminate the designation of a foreign country under subsection (a) if the Secretary certifies to Congress that the government of the foreign country\u2014 (1) has released the United States nationals unlawfully or wrongfully detained within the territory of the foreign country; (2) has positively contributed to the release of United States nationals taken hostage within the territory of the foreign country or from the custody of a nonstate entity; (3) has demonstrated changes in leadership or policies with respect to unlawful or wrongful detention and hostage taking; or (4) has provided assurances that the government of the foreign country will not engage or be complicit in or support acts described in subsection (a). (c) Briefing and reports to Congress; publication (1) Reports to Congress (A) In general Not later than 7 days prior to making a designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State shall submit to the appropriate committees of Congress a report that notifies the committees of the proposed designation. (B) Elements In each report submitted under subparagraph (A) with respect to the designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention, the Secretary shall include\u2014 (i) the justification for the designation; and (ii) a description of any action taken by the United States Government, including the Secretary of State or the head of any other relevant Federal agency, in response to the designation to deter the unlawful or wrongful detention or hostage-taking of foreign nationals in the country. (2) Initial briefing required Not later than 60 days after the date of the enactment of this section, the Secretary shall brief Congress on the following: (A) Whether any of the following countries should be designated as a State Sponsor of Unlawful or Wrongful Detention under subsection (a): (i) Afghanistan. (ii) Eritrea. (iii) The Islamic Republic of Iran. (iv) The People's Republic of China. (v) The Russian Federation. (vi) The Syrian Arab Republic or any transitional government therein. (vii) Venezuela under the regime of Nicol\u00e1s Maduro. (viii) The Republic of Belarus. (B) The steps taken by the Secretary and the heads of other relevant Federal agencies to deter the unlawful and wrongful detention of United States nationals and to respond to such detentions, including\u2014 (i) any engagement with private sector companies to optimize the distribution of travel advisories; and (ii) any engagement with private companies responsible for promoting travel to foreign countries engaged in the unlawful or wrongful detention of United States nationals. (C) An assessment of a possible expansion of chapter 97 of title 28, United States Code (commonly known as the Foreign Sovereign Immunities Act of 1976 ) to include an exception from asset seizure immunity for State Sponsors of Unlawful or Wrongful Detention. (D) A detailed plan on the manner by which a geographic travel restriction could be instituted against State Sponsors of Unlawful or Wrongful Detention. (E) The progress made in multilateral fora, including the United Nations and other international organizations, to address the unlawful and wrongful detention of United States nationals, in addition to nationals of partners and allies of the United States in foreign countries. (3) Annual briefing Not later than one year after the date of the enactment of this section, and annually thereafter for 5 years, the Assistant Secretary of State for Consular Affairs and the Special Presidential Envoy for Hostage Affairs shall brief the appropriate committees of Congress with respect to unlawful or wrongful detentions taking place in the countries listed under paragraph (2)(A) and actions taken by the Secretary of State and the heads of other relevant Federal agencies to deter the wrongful detention of United States nationals, including any steps taken in accordance with paragraph (2)(B). (4) Publication The Secretary shall make available on a publicly accessible website of the Department of State, and regularly update, a list of foreign countries designated as State Sponsors of Unlawful or Wrongful Detention under subsection (a). (d) Review of available responses to state sponsors of unlawful or wrongful detention Upon designation of a foreign country as a State Sponsor of Unlawful or Wrongful Detention under subsection (a), the Secretary of State, in consultation with the heads of other relevant Federal agencies, shall conduct a comprehensive review of the use of existing authorities to respond to and deter the unlawful or wrongful detention of United States nationals in the foreign country, including\u2014 (1) sanctions available under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); (2) visa restrictions available under section 7031(c) of the Department of State, Foreign Operations, and Related Programs Appropriations Act, 2024 (division F of Public Law 118\u201347 ; 8 U.S.C. 1182 note) or any other provision of Federal law; (3) sanctions available under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ); (4) imposition of a geographic travel restriction on citizens of the United States; (5) restrictions on assistance provided to the government of the country under the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) or any other provision of Federal law; (6) restrictions on the export of certain goods to the country under the Arms Export Control Act ( 22 U.S.C. 2751 et seq. ), the Export Control Reform Act of 2018 ( 50 U.S.C. 4801 et seq. ), or any other Federal law; and (7) designating the government of the country as a government that has repeatedly provided support for acts of international terrorism pursuant to\u2014 (A) section 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); (B) section 620A of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371 ); (C) section 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) ); or (D) any other provision of law. (e) Appropriate committees of Congress defined In this paragraph, the term appropriate committees of Congress means\u2014 (1) the Committee on Foreign Relations and the Committee on Appropriations of the Senate; and (2) the Committee on Foreign Affairs and the Committee on Appropriations of the House of Representatives. (f) Rule of Construction Nothing in this section shall be construed to imply that the United States Government formally recognizes any particular country or the government of such country as legitimate. .\n#### 102. Required certification regarding international travel advisories\n##### (a) In general\nChapter 423 of title 49, United States Code, is amended by adding at the end the following new section:\n42309. Required certification regarding international travel advisories (a) In general An air carrier, foreign air carrier, or ticket agent who sells, in the United States, a ticket for foreign air transportation of a passenger to a country or other geographic area with a D or K indicator issued by the Department of State Travel Advisory System shall require the passenger listed on the ticket to certify that the passenger\u2014 (1) has reviewed the travel advisory of the Department of State applicable to such country or other geographic area; and (2) understands the risks involved with traveling to such country or other geographic area. (b) Definitions For purposes of this section: (1) D indicator The term D indicator means a travel advisory issued by the Department of State that indicates a risk of wrongful detention of a United States national. (2) K indicator The term K indicator means a travel advisory issued by the Department of State that indicates a criminal or terrorist individual or group has threatened to seize, detain, kill, or injure individuals (or has seized, detained, killed, or injured individuals) to compel a third party (including a governmental organization) to meet certain requirements as a condition of release. .\n##### (b) Clerical amendment\nThe analysis for chapter 423 of title 49, United States Code, is amended by inserting after the item relating to section 42308 the following:\n42309. Required certification regarding international travel advisories. .\nII\nStrengthening processes and services for hostages and unlawful or wrongful detainees\n#### 201. Advisory Council on Hostage-Taking and Unlawful or Wrongful Detention\nThe Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741 et seq. ), as amended by section 101, is further amended by inserting after section 305B the following:\n305C. Advisory Council on Hostage Taking and Unlawful or Wrongful Detention (a) Establishment The President shall establish an advisory council, to be known as the Advisory Council on Hostage Taking and Unlawful or Wrongful Detention (in this section referred to as the Advisory Council ), to advise the Special Presidential Envoy for Hostage Affairs, the Hostage Response Group, and the Hostage Recovery Fusion Cell with respect to Federal policies regarding hostage-taking and unlawful or wrongful detention. (b) Membership (1) In general The President shall invite individuals to the Advisory Council, which shall be comprised of\u2014 (A) United States nationals who have been unlawfully or wrongfully detained or taken hostage abroad; (B) family members of such United States nationals; and (C) not fewer than 2 experts on areas including hostage-taking, wrongful detention, international relations, rule of law, and counterterrorism who have been recommended by the Secretary of State. (2) Terms The term of a member of the Advisory Council shall be 3 years. (3) Compensation and travel expenses A member of the Advisory Council shall not be considered a Federal employee and shall not be compensated for service on the Advisory Council, but may be allowed travel expenses, including per diem in lieu of subsistence, in accordance with subchapter I of chapter 57 of title 5, United States Code. (c) Annual reports Not later than 1 year after the date of the enactment of this section, and annually thereafter, the Advisory Council shall submit to the President and the appropriate congressional committees a report setting forth the recommendations of the Advisory Council. (d) Termination The Advisory Council shall terminate on the date that is 10 years after the date of the enactment of this section. .\n#### 202. Congressional Report on Components Related to Hostage Affairs and Recovery\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, the President shall submit to Congress a report on the following:\n**(1)**\nThe Hostage Response Group established pursuant to section 305(a) of the Robert Levinson Hostage Recovery and Hostage-Taking Accountability Act ( 22 U.S.C. 1741c(a) ).\n**(2)**\nThe Hostage Recovery Fusion Cell established pursuant to section 304(a) of that Act ( 22 U.S.C. 1741b(a) ).\n**(3)**\nThe Office of the Special Presidential Envoy for Hostage Affairs established pursuant to section 303(a) of that Act ( 22 U.S.C. 1741a(a) ).\n##### (b) Elements\nThe report required by subsection (a) shall include\u2014\n**(1)**\na description of the existing structure of each component listed in subsection (a);\n**(2)**\nrecommendations on how the components can be improved, including through reorganization or consolidation of the components; and\n**(3)**\ncost efficiencies on the components listed in subsection (a), including resources available to eligible former wrongful detainees and hostages and their family members.",
      "versionDate": "2025-06-18",
      "versionType": "Reported in Senate"
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
            "updateDate": "2025-06-12T18:47:48Z"
          },
          {
            "name": "Afghanistan",
            "updateDate": "2025-06-12T18:45:21Z"
          },
          {
            "name": "Africa",
            "updateDate": "2025-06-12T18:46:42Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-12T18:46:48Z"
          },
          {
            "name": "Belarus",
            "updateDate": "2025-06-12T18:46:14Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-12T18:45:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-12T18:45:13Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-06-12T18:44:40Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-06-12T18:45:06Z"
          },
          {
            "name": "Due process and equal protection",
            "updateDate": "2025-06-12T18:44:48Z"
          },
          {
            "name": "Eritrea",
            "updateDate": "2025-06-12T18:45:28Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-06-12T18:46:22Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-06-12T18:47:42Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-12T18:47:05Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-06-12T18:44:54Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-12T18:48:02Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-06-12T18:45:34Z"
          },
          {
            "name": "Latin America",
            "updateDate": "2025-06-12T18:46:29Z"
          },
          {
            "name": "Middle East",
            "updateDate": "2025-06-12T18:46:37Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-12T18:47:35Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-06-12T18:45:00Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-06-12T18:45:49Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-06-12T18:47:17Z"
          },
          {
            "name": "Syria",
            "updateDate": "2025-06-12T18:45:56Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2025-06-12T18:47:23Z"
          },
          {
            "name": "Travel and tourism",
            "updateDate": "2025-06-12T18:46:56Z"
          },
          {
            "name": "Venezuela",
            "updateDate": "2025-06-12T18:46:05Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-22T21:06:31Z"
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
      "date": "2025-04-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1478is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1478rs.xml"
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
      "title": "Countering Wrongful Detention Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-19T12:03:16Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Countering Wrongful Detention Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Countering Wrongful Detention Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-06T03:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide the United States Government with additional tools to deter state and non-state actors from wrongfully detaining United States nationals for political leverage, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-06T03:48:21Z"
    }
  ]
}
```
