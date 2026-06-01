# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1369?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1369
- Title: Protecting Global Fisheries Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 1369
- Origin chamber: Senate
- Introduced date: 2025-04-09
- Update date: 2026-05-15T11:03:25Z
- Update date including text: 2026-05-15T11:03:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in Senate
- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 322.
- Latest action: 2025-04-09: Introduced in Senate

## Actions

- 2025-04-09 - IntroReferral: Introduced in Senate
- 2025-04-09 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2026-01-29 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2026-02-10 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 322.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1369",
    "number": "1369",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Public Lands and Natural Resources"
    },
    "sponsors": [
      {
        "bioguideId": "K000384",
        "district": "",
        "firstName": "Timothy",
        "fullName": "Sen. Kaine, Tim [D-VA]",
        "lastName": "Kaine",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Protecting Global Fisheries Act of 2026",
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 322.",
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
      "actionDate": "2025-04-09",
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
      "actionDate": "2025-04-09",
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
            "date": "2026-02-10T16:29:40Z",
            "name": "Reported By"
          },
          {
            "date": "2026-01-29T14:30:02Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-09T16:27:51Z",
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
      "bioguideId": "C001075",
      "firstName": "Bill",
      "fullName": "Sen. Cassidy, Bill [R-LA]",
      "isOriginalCosponsor": "True",
      "lastName": "Cassidy",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "LA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "NM"
    },
    {
      "bioguideId": "C001114",
      "firstName": "John",
      "fullName": "Sen. Curtis, John R. [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Curtis",
      "party": "R",
      "sponsorshipDate": "2025-04-09",
      "state": "UT"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1369is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1369\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Kaine (for himself, Mr. Cassidy , Mr. Heinrich , and Mr. Curtis ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo support the execution of bilateral agreements concerning illicit transnational maritime activity and to authorize the President to impose sanctions with respect to illegal, unreported, or unregulated fishing and the sale, supply, purchase, or transfer of endangered species, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Global Fisheries Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Admission; admitted; alien; lawfully admitted for permanent residence**\nThe terms admission , admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Armed Services of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(4) Illegal, unreported, or unregulated fishing**\nThe term illegal, unreported, or unregulated fishing has the meaning given that term in the implementing regulations or any subsequent regulations issued pursuant to section 609(e) of the High Seas Driftnet Fishing Moratorium Protection Act ( 16 U.S.C. 1826j(e) ).\n**(5) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person located in the United States.\n#### 3. International collaboration related to countering illegal, unreported, or unregulated fishing\n##### (a) Statement of policy\nIt is the policy of the United States to prioritize collaboration with friendly countries, and through appropriate international institutions, to combat illegal, unreported, or unregulated fishing.\n##### (b) Actions by Secretary of State\nThe Secretary of State shall take such actions as may be necessary to use the voice, vote, and influence of the United States in all appropriate international fora and with appropriate countries that are allies or partners of the United States\u2014\n**(1)**\nto ensure that cutting edge technology is deployed in accordance to existing or future maritime law enforcement agreements the United States may enter or has entered into; and\n**(2)**\nto hold accountable those individuals or entities that are responsible or complicit in illegal, unreported, or unregulated fishing, with a particular focus on the harmful actions of the People\u2019s Republic of China.\n##### (c) Advocacy at United Nations\nThe President may direct the United States Permanent Representative to the United Nations to use the voice, vote, and influence of the United States to urge the United Nations to take greater action with respect to collaborative global efforts to counter illegal, unreported, or unregulated fishing.\n#### 4. Authorization of imposition of sanctions with respect to illegal, unreported, or unregulated fishing and trade in endangered species\n##### (a) In general\nThe President may impose the sanctions described in subsection (b) with respect to any foreign person or foreign vessel (regardless of ownership) that the President determines\u2014\n**(1)**\nis responsible for or complicit in\u2014\n**(A)**\nillegal, unreported, or unregulated fishing; or\n**(B)**\nexcept as part of a conservation effort, the sale, supply, purchase, or transfer (including transportation) of endangered species, as defined in section 3(6) of the Endangered Species Act of 1973 ( 16 U.S.C. 1532(6) );\n**(2)**\nis a leader or official of an entity, including a government entity, that has engaged in, or the members of which have engaged in, any of the activities described in paragraph (1) during the tenure of the leader or official;\n**(3)**\nhas ever owned, operated, chartered, or controlled a vessel during which time the personnel of the vessel engaged in any of the activities described in paragraph (1); or\n**(4)**\nhas materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services in support of\u2014\n**(A)**\nany of the activities described in paragraph (1); or\n**(B)**\nany foreign person engaged in any such activity.\n##### (b) Sanctions described\nThe sanctions that may be imposed under subsection (a) with respect to a foreign person or foreign vessel are the following:\n**(1) Blocking of property**\nNotwithstanding section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the exercise of all powers granted to the President by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Inadmissibility to the United States**\nIn the case of an alien described in subsection (a), or any alien that the President determines is a corporate officer or principal of, or a shareholder with a controlling interest in, a foreign person described in subsection (a) that is an entity\u2014\n**(A)**\nineligibility for a visa and inadmissibility to the United States; and\n**(B)**\nrevocation of any valid visa or travel documentation in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ).\n**(3) Prohibition on access to the united states**\nIn the case of a foreign vessel described in subsection (a), denial of access to United States ports.\n**(4) Loans from United States financial institutions**\nThe President may prohibit any United States financial institution from making loans or providing credits to a foreign person described in subsection (a).\n**(5) Foreign exchange**\nThe President may, pursuant to such regulations as the President may prescribe, prohibit any transactions in foreign exchange that are subject to the jurisdiction of the United States and in which a foreign person or foreign vessel described in subsection (a) has any interest.\n##### (c) Report required\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the President shall submit a report on the imposition of sanctions under this section to\u2014\n**(1)**\nthe Committee on Banking, Housing, and Urban Affairs and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Financial Services and the Committee on Foreign Affairs of the House of Representatives.\n##### (d) National interest waiver\nThe President may waive the imposition of sanctions under subsection (a) with respect to a foreign person or foreign vessel if the President determines that such a waiver is in the national interests of the United States.\n##### (e) Exceptions\n**(1) Exceptions for authorized intelligence and law enforcement activities**\nSanctions under this section shall not apply with respect to activities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence, law enforcement, or national security activities of the United States.\n**(2) Exception to comply with international agreements**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien to the United States if such admission is necessary to comply with the obligations of the United States under the Agreement regarding the Headquarters of the United Nations, signed at Lake Success on June 26, 1947, and entered into force on November 21, 1947, between the United Nations and the United States, or the Convention on Consular Relations, done at Vienna on April 24, 1963, and entered into force on March 19, 1967, or other international obligations.\n**(3) Exception for safety of vessels and crew**\nSanctions under this section shall not apply with respect to a person providing provisions to a vessel if such provisions are intended for the safety and care of the crew aboard the vessel or the maintenance of the vessel to avoid any environmental or other significant damage.\n**(4) Humanitarian exception**\n**(A) In general**\nExcept as provided in subparagraph (B), the President may not impose sanctions under this section with respect to any person for conducting or facilitating a transaction for the sale of agricultural commodities, food, medicine, or medical devices or for the provision of humanitarian assistance.\n**(B) Exclusion**\nThe exception under subparagraph (A) does not include transactions for the sale of food or agricultural commodities obtained through illegal, unreported, or unregulated fishing.\n##### (f) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (g) Rulemaking\n**(1) In general**\nThe head of any Federal agency responsible for the implementation of this section may promulgate such rules and regulations as may be necessary to carry out the provisions of this section (which may include regulatory exceptions), including under section 205 of the International Emergency Economic Powers Act ( 50 U.S.C. 1704 ).\n**(2) Rule of construction**\nNothing in this section may be construed to limit the authority of the President pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n#### 5. Briefing and report on global illegal, unreported, or unregulated fishing\n##### (a) Briefing\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Secretary of Defense, shall brief the appropriate congressional committees on\u2014\n**(1)**\nefforts to work with United States partners and allies to counter illegal, unreported, or unregulated fishing via bilateral engagements;\n**(2)**\nefforts to counter, and challenges faced in countering, illegal, unreported, or unregulated fishing through existing international agreements, institutions, and mechanisms; and\n**(3)**\nefforts by the Department of State and the Department of Defense to engage and collaborate with nongovernmental organizations and State and local agencies to spread awareness and coordinate responses to global illegal, unreported, or unregulated fishing concerns.\n##### (b) Report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for 4 years, the Secretary of State, in consultation with the Secretary of Defense, shall submit to the appropriate congressional committees a report that includes\u2014\n**(A)**\nrecommendations to bolster maritime law enforcement agreements with United States allies and partners;\n**(B)**\nan assessment of the global illegal, unreported, or unregulated fishing patterns, strategic goals, and regional priorities of the People's Republic of China, and government and non-government resourcing vectors of the People's Republic of China for illegal, unreported, or unregulated fishing fleets; and\n**(C)**\nan assessment of the efficacy of global forums to respond to illegal, unreported, or unregulated fishing, and a strategy for United States engagement in such forums.\n**(2) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2025-04-09",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1369rs.xml",
      "text": "II\nCalendar No. 322\n119th CONGRESS\n2d Session\nS. 1369\nIN THE SENATE OF THE UNITED STATES\nApril 9, 2025 Mr. Kaine (for himself, Mr. Cassidy , Mr. Heinrich , Mr. Curtis , and Mr. Scott of Florida ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nFebruary 10, 2026 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo support the execution of bilateral agreements concerning illicit transnational maritime activity and to authorize the President to impose sanctions with respect to illegal, unreported, or unregulated fishing and the sale, supply, purchase, or transfer of endangered species, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting Global Fisheries Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Admission; admitted; alien; lawfully admitted for permanent residence**\nThe terms admission , admitted , alien , and lawfully admitted for permanent residence have the meanings given those terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Foreign Relations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs and the Committee on Armed Services of the House of Representatives.\n**(3) Foreign person**\nThe term foreign person means an individual or entity that is not a United States person.\n**(4) Illegal, unreported, or unregulated fishing**\nThe term illegal, unreported, or unregulated fishing has the meaning given that term in the implementing regulations or any subsequent regulations issued pursuant to section 609(e) of the High Seas Driftnet Fishing Moratorium Protection Act ( 16 U.S.C. 1826j(e) ).\n**(5) United States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person located in the United States.\n#### 3. International collaboration related to countering illegal, unreported, or unregulated fishing\n##### (a) Statement of policy\nIt is the policy of the United States to prioritize collaboration with friendly countries, and through appropriate international institutions, to combat illegal, unreported, or unregulated fishing.\n##### (b) Actions by Secretary of State\nThe Secretary of State shall take such actions as may be necessary to use the voice, vote, and influence of the United States in all appropriate international fora and with appropriate countries that are allies or partners of the United States\u2014\n**(1)**\nto ensure that cutting edge technology is deployed in accordance to existing or future maritime law enforcement agreements the United States may enter or has entered into; and\n**(2)**\nto hold accountable those individuals or entities that are responsible or complicit in illegal, unreported, or unregulated fishing, with a particular focus on the harmful actions of the People\u2019s Republic of China.\n##### (c) Advocacy at United Nations\nThe President may direct the United States Permanent Representative to the United Nations to use the voice, vote, and influence of the United States to urge the United Nations to take greater action with respect to collaborative global efforts to counter illegal, unreported, or unregulated fishing.\n#### 4. Authorization of imposition of sanctions with respect to illegal, unreported, or unregulated fishing and trade in endangered species\n##### (a) In general\nThe President may impose the sanctions described in subsection (b) with respect to any foreign person or foreign vessel (regardless of ownership) that the President determines\u2014\n**(1)**\nis responsible for or complicit in\u2014\n**(A)**\nillegal, unreported, or unregulated fishing; or\n**(B)**\nexcept as part of a conservation effort, the sale, supply, purchase, or transfer (including transportation) of endangered species, as defined in section 3(6) of the Endangered Species Act of 1973 ( 16 U.S.C. 1532(6) );\n**(2)**\nis a leader or official of an entity, including a government entity, that has engaged in, or the members of which have engaged in, any of the activities described in paragraph (1) during the tenure of the leader or official;\n**(3)**\nhas ever owned, operated, chartered, or controlled a vessel during which time the personnel of the vessel engaged in any of the activities described in paragraph (1); or\n**(4)**\nhas materially assisted, sponsored, or provided financial, material, or technological support for, or goods or services in support of\u2014\n**(A)**\nany of the activities described in paragraph (1); or\n**(B)**\nany foreign person engaged in any such activity.\n##### (b) Sanctions described\nThe sanctions that may be imposed under subsection (a) with respect to a foreign person or foreign vessel are the following:\n**(1) Blocking of property**\nNotwithstanding section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the exercise of all powers granted to the President by the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in all property and interests in property of a foreign person described in subsection (a), if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Inadmissibility to the United States**\nIn the case of an alien described in subsection (a), or any alien that the President determines is a corporate officer or principal of, or a shareholder with a controlling interest in, a foreign person described in subsection (a) that is an entity\u2014\n**(A)**\nineligibility for a visa and inadmissibility to the United States; and\n**(B)**\nrevocation of any valid visa or travel documentation in accordance with section 221(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(i) ).\n**(3) Prohibition on access to the united states**\nIn the case of a foreign vessel described in subsection (a), denial of access to United States ports.\n**(4) Loans from United States financial institutions**\nThe President may prohibit any United States financial institution from making loans or providing credits to a foreign person described in subsection (a).\n**(5) Foreign exchange**\nThe President may, pursuant to such regulations as the President may prescribe, prohibit any transactions in foreign exchange that are subject to the jurisdiction of the United States and in which a foreign person or foreign vessel described in subsection (a) has any interest.\n##### (c) Report required\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter, the President shall submit a report on the imposition of sanctions under this section to\u2014\n**(1)**\nthe Committee on Banking, Housing, and Urban Affairs and the Committee on Foreign Relations of the Senate; and\n**(2)**\nthe Committee on Financial Services and the Committee on Foreign Affairs of the House of Representatives.\n##### (d) National interest waiver\nThe President may waive the imposition of sanctions under subsection (a) with respect to a foreign person or foreign vessel if the President determines that such a waiver is in the national interests of the United States.\n##### (e) Exceptions\n**(1) Exceptions for authorized intelligence and law enforcement activities**\nSanctions under this section shall not apply with respect to activities subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ) or any authorized intelligence, law enforcement, or national security activities of the United States.\n**(2) Exception to comply with international agreements**\nSanctions under subsection (b)(2) shall not apply with respect to the admission of an alien to the United States if such admission is necessary to comply with the obligations of the United States under the Agreement regarding the Headquarters of the United Nations, signed at Lake Success on June 26, 1947, and entered into force on November 21, 1947, between the United Nations and the United States, or the Convention on Consular Relations, done at Vienna on April 24, 1963, and entered into force on March 19, 1967, or other international obligations.\n**(3) Exception for safety of vessels and crew**\nSanctions under this section shall not apply with respect to a person providing provisions to a vessel if such provisions are intended for the safety and care of the crew aboard the vessel or the maintenance of the vessel to avoid any environmental or other significant damage.\n**(4) Humanitarian exception**\n**(A) In general**\nExcept as provided in subparagraph (B), the President may not impose sanctions under this section with respect to any person for conducting or facilitating a transaction for the sale of agricultural commodities, food, medicine, or medical devices or for the provision of humanitarian assistance.\n**(B) Exclusion**\nThe exception under subparagraph (A) does not include transactions for the sale of food or agricultural commodities obtained through illegal, unreported, or unregulated fishing.\n##### (f) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of this section or any regulation, license, or order issued to carry out this section shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Emergency Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n##### (g) Rulemaking\n**(1) In general**\nThe head of any Federal agency responsible for the implementation of this section may promulgate such rules and regulations as may be necessary to carry out the provisions of this section (which may include regulatory exceptions), including under section 205 of the International Emergency Economic Powers Act ( 50 U.S.C. 1704 ).\n**(2) Rule of construction**\nNothing in this section may be construed to limit the authority of the President pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n#### 5. Briefing and report on global illegal, unreported, or unregulated fishing\n##### (a) Briefing\nNot later than 90 days after the date of the enactment of this Act, the Secretary of State, in consultation with the Secretary of Defense, shall brief the appropriate congressional committees on\u2014\n**(1)**\nefforts to work with United States partners and allies to counter illegal, unreported, or unregulated fishing via bilateral engagements;\n**(2)**\nefforts to counter, and challenges faced in countering, illegal, unreported, or unregulated fishing through existing international agreements, institutions, and mechanisms; and\n**(3)**\nefforts by the Department of State and the Department of Defense to engage and collaborate with nongovernmental organizations and State and local agencies to spread awareness and coordinate responses to global illegal, unreported, or unregulated fishing concerns.\n##### (b) Report\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, and annually thereafter for 4 years, the Secretary of State, in consultation with the Secretary of Defense, shall submit to the appropriate congressional committees a report that includes\u2014\n**(A)**\nrecommendations to bolster maritime law enforcement agreements with United States allies and partners;\n**(B)**\nan assessment of the global illegal, unreported, or unregulated fishing patterns, strategic goals, and regional priorities of the People's Republic of China, and government and non-government resourcing vectors of the People's Republic of China for illegal, unreported, or unregulated fishing fleets; and\n**(C)**\nan assessment of the efficacy of global forums to respond to illegal, unreported, or unregulated fishing, and a strategy for United States engagement in such forums.\n**(2) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, but may include a classified annex.",
      "versionDate": "2026-02-10",
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
            "name": "China",
            "updateDate": "2026-02-11T14:54:09Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-02-11T14:54:56Z"
          },
          {
            "name": "Endangered and threatened species",
            "updateDate": "2026-02-11T14:54:04Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2026-02-11T14:54:42Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2026-02-11T14:54:18Z"
          },
          {
            "name": "Marine and coastal resources, fisheries",
            "updateDate": "2026-02-11T14:53:57Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2026-02-11T14:54:33Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2026-02-11T14:54:25Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2026-02-11T14:54:49Z"
          }
        ]
      },
      "policyArea": {
        "name": "Public Lands and Natural Resources",
        "updateDate": "2025-05-28T14:12:11Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1369is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-02-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s1369rs.xml"
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
      "title": "Protecting Global Fisheries Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-15T11:03:25Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Protecting Global Fisheries Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-02-12T04:38:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Protecting Global Fisheries Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-23T02:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support the execution of bilateral agreements concerning illicit transnational maritime activity and to authorize the President to impose sanctions with respect to illegal, unreported, or unregulated fishing and the sale, supply, purchase, or transfer of endangered species, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-23T02:48:20Z"
    }
  ]
}
```
