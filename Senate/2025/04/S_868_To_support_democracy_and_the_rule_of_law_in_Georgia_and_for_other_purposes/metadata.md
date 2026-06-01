# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/868?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/868
- Title: MEGOBARI Act
- Congress: 119
- Bill type: S
- Bill number: 868
- Origin chamber: Senate
- Introduced date: 2025-03-05
- Update date: 2026-05-20T14:05:45Z
- Update date including text: 2026-05-20T14:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-05: Introduced in Senate
- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 55.
- Latest action: 2025-03-05: Introduced in Senate

## Actions

- 2025-03-05 - IntroReferral: Introduced in Senate
- 2025-03-05 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-03-27 - Committee: Committee on Foreign Relations. Ordered to be reported without amendment favorably.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Committee: Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.
- 2025-04-28 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 55.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-05",
    "latestAction": {
      "actionDate": "2025-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/868",
    "number": "868",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001181",
        "district": "",
        "firstName": "Jeanne",
        "fullName": "Sen. Shaheen, Jeanne [D-NH]",
        "lastName": "Shaheen",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "MEGOBARI Act",
    "type": "S",
    "updateDate": "2026-05-20T14:05:45Z",
    "updateDateIncludingText": "2026-05-20T14:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-28",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 55.",
      "type": "Calendars"
    },
    {
      "actionDate": "2025-04-28",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2025-04-28",
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
      "text": "Committee on Foreign Relations. Reported by Senator Risch without amendment. Without written report.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Foreign Relations. Ordered to be reported without amendment favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-03-05",
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
      "actionDate": "2025-03-05",
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
            "date": "2025-04-28T20:35:49Z",
            "name": "Reported By"
          },
          {
            "date": "2025-03-27T17:55:19Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-05T20:53:46Z",
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
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-05",
      "state": "ID"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "False",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-24",
      "state": "DE"
    },
    {
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "False",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s868is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 868\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mrs. Shaheen (for herself and Mr. Risch ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo support democracy and the rule of law in Georgia, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Mobilizing and Enhancing Georgia\u2019s Options for Building Accountability, Resilience, and Independence Act or the MEGOBARI Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Appropriations of the Senate ;\n**(C)**\nthe Committee on Foreign Affairs of the House of Representatives ; and\n**(D)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) NATO**\nThe term NATO means the North Atlantic Treaty Organization.\n**(3) Secretary**\nThe term Secretary means the Secretary of State.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe progress made by the people of Georgia in forging an innovative and productive society since the country\u2019s independence from the Soviet Union should be applauded;\n**(2)**\nthe consolidation of democracy in Georgia is critical for regional stability and United States national interests;\n**(3)**\nGeorgia has seen significant democratic backsliding in recent years, as evidenced by numerous independent assessments and measures;\n**(4)**\nthe current Georgian government is increasingly hostile towards independent domestic civil society and its chief Euro-Atlantic partners while increasingly embracing enhanced ties with the Russian Federation, the People\u2019s Republic of China, and other anti-Western authoritarian regimes;\n**(5)**\nthe United States has an interest in protecting and securing democracy in Georgia; and\n**(6)**\nthe Secretary should suspend the United States-Georgia Strategic Partnership Commission, established through the United States-Georgia Charter on Strategic Partnership on January 9, 2009, until after the Government of Georgia takes measures\u2014\n**(A)**\nto represent the democratic wishes of the citizens of Georgia; and\n**(B)**\nto uphold its constitutional obligation to advance the country towards membership in the European Union and NATO.\n#### 4. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto support the constitutionally stated aspirations of Georgia to become a member of the European Union and NATO, which is made clear under Article 78 of the Constitution of Georgia and is supported by the overwhelming majority of the citizens of Georgia;\n**(2)**\nto continue supporting the capacity of the Government of Georgia to protect its sovereignty and territorial integrity from further Russian aggression or encroachment within its internationally recognized borders;\n**(3)**\nto call on all political parties and elected Members of the Parliament of Georgia to continue working on addressing the reform plan outlined by the European Commission to resume Georgia\u2019s recently granted candidate status through an inclusive and transparent consultation process that involves opposition parties and civil society organizations, which the people of Georgia have freely elected to pursue;\n**(4)**\nto reevaluate its relationship with the Government of Georgia and review all forms of foreign and security assistance made available to the Government if it takes the required steps\u2014\n**(A)**\nto reorient itself toward its European Union accession agenda; and\n**(B)**\nto advance policy or legislation reflecting the express wishes of the Georgian people;\n**(5)**\nto emphasize the importance of contributing to international efforts\u2014\n**(A)**\nto combat Russian aggression, including through sanctions on trade with Russia and the implementation and enforcement of worldwide sanctions on Russia; and\n**(B)**\nto reduce, rather than increase, trade ties between Georgia and Russia;\n**(6)**\nto continue supporting the ongoing development of democratic values in Georgia, including free and fair elections, freedom of association, an independent and accountable judiciary, an independent media, public-sector transparency and accountability, the rule of law, countering malign influence, and anti-corruption efforts and to impose swift consequences on individuals who are directly responsible for leading or have directly and knowingly engaged in leading actions of policies that significantly undermine those standards;\n**(7)**\nto continue to support the Georgian people and civil society organizations that reflect the aspirations of the Georgian people for democracy and a future with the people of Europe;\n**(8)**\nto continue supporting the right of the Georgian people to freely engage in peaceful protest, determine their future, and make independent and sovereign choices on foreign and security policy, including regarding Georgia\u2019s relationship with other countries and international organizations, without interference, intimidation, or coercion by other countries or those acting on their behalf;\n**(9)**\nto call on all political parties, elected Members of the Parliament of Georgia, and officers of the Ministry of Internal Affairs of Georgia to respect the freedoms of peaceful assembly, association, and expression, including for the press, and the rule of law, and encourage a vibrant and inclusive civil society;\n**(10)**\nto call on the Government of Georgia to release all persons detained or imprisoned on politically motivated grounds and drop any pending charges against them;\n**(11)**\nto call on the Government of Georgia to thoroughly investigate all allegations emerging from the recent national elections, which took place on October 2024, make a determination whether the elections should be judged as illegitimate and hold those responsible for interference in the elections; and\n**(12)**\nto continue impressing upon the Government of Georgia that the United States is committed to sustaining and deepening bilateral relations and supporting Georgia\u2019s Euro-Atlantic aspirations.\n#### 5. Reports and briefings\n##### (a) Report on Russian intelligence assets in Georgia\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Director of National Intelligence and the Secretary of Defense, shall submit to the appropriate committees of Congress a classified report, prepared consistent with the protection of sources and methods, examining the penetration of Russian intelligence elements and their assets in Georgia, that includes an annex examining Chinese influence and the potential intersection of Russian-Chinese cooperation in Georgia.\n**(2) Appropriate committees of Congress**\nIn this section, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Select Committee on Intelligence of the Senate ;\n**(C)**\nthe Committee on Armed Services of the Senate ;\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(E)**\nthe Permanent Select Committee on Intelligence of the House of Representatives ; and\n**(F)**\nthe Committee on Armed Services of the House of Representatives .\n##### (b) 5-Year United States strategy for bilateral relations with Georgia\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary and the Administrator of the United States Agency for International Development, in coordination with the heads of other relevant Federal departments and agencies, shall submit to the appropriate committees of Congress a detailed strategy that\u2014\n**(A)**\noutlines specific objectives for enhancing bilateral ties which reflect the current domestic political environment in Georgia;\n**(B)**\nincludes a determination of the tools, resources, and funding that should be available to achieve the objectives outlined pursuant to subparagraph (A) and an assessment whether Georgia should remain the second-highest recipient of United States funding in the Europe and Eurasia region;\n**(C)**\nincludes a determination of the extent to which the United States should continue to invest in its partnership with Georgia;\n**(D)**\nincludes a plan for how the United States can continue to support civil society and independent media organizations in Georgia; and\n**(E)**\nincludes a determination whether the Government of Georgia remains committed to expanding trade ties with the United States and Europe and whether the United States Government should continue to invest in Georgian projects.\n**(2) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, with a classified annex.\n#### 6. Sanctions\n##### (a) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given such terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(C)**\nthe Committee on the Judiciary of the Senate ;\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(E)**\nthe Committee on the Judiciary of the House of Representatives ; and\n**(F)**\nthe Committee on Financial Services of the House of Representatives .\n**(3) Foreign person**\nThe term foreign person means any individual or entity that is not a United States person.\n**(4) Immediate family members**\nThe term immediate family members has the meaning given the term immediate relatives in section 201(b)(2)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(b)(2)(A)(i) ).\n**(5) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(6) Unites States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person within the United States.\n##### (b) Inadmissibility of officials of Government of Georgia and certain other individuals involved in blocking Euro-Atlantic integration\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the President shall determine whether each of the following foreign persons has knowingly engaged in significant acts of corruption, or acts of violence or intimidation in relation to the blocking of Euro-Atlantic integration in Georgia:\n**(A)**\nAny individual who, on or after January 1, 2014, has served as a member of the Parliament of the Government of Georgia or as a current or former senior official of a Georgian political party.\n**(B)**\nAny individual who is serving as an official in a leadership position working on behalf of the Government of Georgia, including law enforcement, intelligence, judicial, or local or municipal government.\n**(C)**\nAn immediate family member of an official described in subparagraph (A) or a person described in subparagraph (B) who benefitted from the conduct of such official or person.\n**(2) Sanctions**\nThe President shall impose the sanctions described in subsection (d)(2) with respect to each foreign person with respect to which the President has made an affirmative decision under paragraph (1).\n**(3) Briefing**\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall brief the appropriate committees of Congress with respect to\u2014\n**(A)**\nany foreign person with respect to which the President has made an affirmative determination under paragraph (1); and\n**(B)**\nthe specific facts that justify each such affirmative determination.\n**(4) Waiver**\nThe President may waive imposition of sanctions under this subsection on a case-by-case basis if the President determines and reports to the appropriate committees of Congress that\u2014\n**(A)**\nsuch waiver would serve national security interests; or\n**(B)**\nthe circumstances which caused the individual to be ineligible have sufficiently changed.\n##### (c) Imposition of sanctions with respect to undermining peace, security, stability, sovereignty or territorial integrity of Georgia\n**(1) In general**\nThe President may impose the sanctions described in subsection (d)(1) and shall impose the sanctions described in subsection (d)(2) with respect to each foreign person the President determines, on or after the date of the enactment of this Act\u2014\n**(A)**\nis responsible for, complicit in, or has directly or indirectly engaged in or attempted to engage in, actions or policies, including ordering, controlling, or otherwise directing acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia;\n**(B)**\nis or has been a leader or official of an entity that has, or whose members have, engaged in any activity described in subparagraph (A); or\n**(C)**\nis an immediate family member of a person subject to sanctions for conduct described in subparagraph (A) or (B) and benefitted from the conduct of such person.\n**(2) Brief and written notification**\nNot later than 10 days after imposing sanctions on a foreign person or persons pursuant to this subsection, the President shall brief and provide written notification to the appropriate committees of Congress regarding the imposition of such sanctions, which shall describe\u2014\n**(A)**\nthe foreign person or persons subject to the imposition of such sanctions;\n**(B)**\nthe activity justifying the imposition of such sanctions; and\n**(C)**\nthe specific sanctions imposed on such foreign person or persons.\n**(3) Waiver**\nThe President may waive the application of sanctions under this subsection with respect to a foreign person for renewable periods not to exceed 180 days if, not later than 15 days before the date on which such waiver is to take effect, the President submits to the appropriate committees of Congress a written determination and justification that the waiver is in the national security interests of the United States.\n##### (d) Sanctions described\nThe sanctions described in this subsection are the following with respect to a foreign person described in subsection (b) or (c), as applicable:\n**(1) Blocking of property**\nNotwithstanding the requirements under section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President shall exercise all authorities granted under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nA foreign person that is an alien shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\nThe foreign person shall be subject to the following:\n**(i)**\nRevocation of any visa or other entry documentation regardless of when the visa or other entry documentation is or was issued.\n**(ii)**\nA revocation under clause (i) shall take effect immediately and automatically cancel any other valid visa or entry documentation that is in the foreign person\u2019s possession.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (d)(2)(A) or any regulation, license, or order issued under that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n**(3) Rule of construction**\nNothing in this Act, or any amendment made by this Act, may be construed to limit the authority of the President to designate or sanction persons pursuant to an applicable Executive order or otherwise pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n##### (f) Rulemaking\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the President shall prescribe such regulations as are necessary for the implementation of this section.\n**(2) Notification to congress**\nNot later than 10 days before prescribing regulations pursuant to paragraph (1), the President shall notify the appropriate committees of Congress of the proposed regulations and the provisions of this section that the regulations are implementing.\n##### (g) Sanctions with respect to broader corruption in Georgia\n**(1) Determination**\nThe President shall determine whether there are foreign persons who, on or after the date of the enactment of this Act, have engaged in significant corruption in Georgia or acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia for the purposes of potential imposition of sanctions pursuant to powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n**(2) Report**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall submit a report to the appropriate committees of Congress that\u2014\n**(i)**\nidentifies all foreign persons the President has determined, pursuant to this subsection, have engaged in significant corruption in Georgia or committed acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia;\n**(ii)**\nthe dates on which sanctions were imposed; and\n**(iii)**\nthe reasons for imposing such sanctions.\n**(B) Form**\nThe report required under subparagraph (A) shall be provided in unclassified form, but may include a classified annex.\n##### (h) Termination of sanctions\nAny sanctions imposed on a foreign person pursuant to this section shall terminate on the earlier of\u2014\n**(1)**\nthe date on which the President certifies to the appropriate committees of Congress that the foreign person is no longer engaging in the activities that led to the imposition of such sanction; or\n**(2)**\nthe sunset date described in section 8.\n##### (i) Exceptions\n**(1) Definitions**\nIn this subsection:\n**(A) Agricultural commodity**\nThe term agricultural commodity has the meaning given such term in section 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ).\n**(B) Good**\nThe term good means any article, natural or man-made substance, material, supply, or manufactured product, including inspection and test equipment and excluding technical data.\n**(C) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(D) Medicine**\nThe term medicine has the meaning given the term drug in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(2) Exceptions**\n**(A) Exception relating to intelligence activities**\nSanctions under this section shall not apply to\u2014\n**(i)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(ii)**\nany authorized intelligence activities of the United States.\n**(B) Exception to comply with international obligations**\nSanctions under this section shall not apply with respect to a foreign person if admitting or paroling the person into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(C) Humanitarian assistance**\nSanctions under this section shall not apply to\u2014\n**(i)**\nthe conduct or facilitation of a transaction for the provision of agricultural commodities, food, medicine, medical devices, or humanitarian assistance, or for humanitarian purposes; or\n**(ii)**\ntransactions that are necessary for, or related to, the activities described in paragraph (1).\n##### (j) Exception relating to importation of goods\nThe requirement to block and prohibit all transactions in all property and interests in property under this section shall not include the authority or a requirement to impose sanctions on the importation of goods.\n#### 7. Additional assistance with respect to Georgia\n##### (a) In general\nUpon submission to Congress of the certification described in subsection (c)\u2014\n**(1)**\nthe Secretary of State, in consultation with other heads of other relevant Federal departments and agencies, should seek to further enhance people-to-people contacts and academic exchanges between the United States and Georgia; and\n**(2)**\nthe President, in consultation with the Secretary of Defense, should maintain, and as appropriate, expand military cooperation with Georgia, including by providing further security and defense equipment ideally suited for territorial defense against Russian aggression and related training, maintenance, and operations support elements.\n##### (b) Sense of Congress\nIt is the sense of Congress that, after the submission of the certification described in subsection (c), if the Government of Georgia takes steps to realign itself with its Euro-Atlantic agenda, including significant changes to the foreign influence law, the President should take steps to improve the bilateral relationship between the United States and Georgia, including actions to bolster Georgia\u2019s ability to deter threats from Russia and other malign actors.\n##### (c) Certification described\nThe certification described in this subsection is a certification submitted to Congress by the President that Georgia has shown significant and sustained progress towards reinvigorating its democracy and advancing its Euro-Atlantic integration.\n#### 8. Sunset\nThis Act shall cease to have any force or effect beginning on the date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-03-05",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s868rs.xml",
      "text": "II\nCalendar No. 55\n119th CONGRESS\n1st Session\nS. 868\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2025 Mrs. Shaheen (for herself, Mr. Risch , Mr. Coons , and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nApril 28, 2025 Reported by Mr. Risch , without amendment\nA BILL\nTo support democracy and the rule of law in Georgia, and for other purposes.\n#### 1. Short titles\nThis Act may be cited as the Mobilizing and Enhancing Georgia\u2019s Options for Building Accountability, Resilience, and Independence Act or the MEGOBARI Act .\n#### 2. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Appropriations of the Senate ;\n**(C)**\nthe Committee on Foreign Affairs of the House of Representatives ; and\n**(D)**\nthe Committee on Appropriations of the House of Representatives .\n**(2) NATO**\nThe term NATO means the North Atlantic Treaty Organization.\n**(3) Secretary**\nThe term Secretary means the Secretary of State.\n#### 3. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nthe progress made by the people of Georgia in forging an innovative and productive society since the country\u2019s independence from the Soviet Union should be applauded;\n**(2)**\nthe consolidation of democracy in Georgia is critical for regional stability and United States national interests;\n**(3)**\nGeorgia has seen significant democratic backsliding in recent years, as evidenced by numerous independent assessments and measures;\n**(4)**\nthe current Georgian government is increasingly hostile towards independent domestic civil society and its chief Euro-Atlantic partners while increasingly embracing enhanced ties with the Russian Federation, the People\u2019s Republic of China, and other anti-Western authoritarian regimes;\n**(5)**\nthe United States has an interest in protecting and securing democracy in Georgia; and\n**(6)**\nthe Secretary should suspend the United States-Georgia Strategic Partnership Commission, established through the United States-Georgia Charter on Strategic Partnership on January 9, 2009, until after the Government of Georgia takes measures\u2014\n**(A)**\nto represent the democratic wishes of the citizens of Georgia; and\n**(B)**\nto uphold its constitutional obligation to advance the country towards membership in the European Union and NATO.\n#### 4. Statement of policy\nIt is the policy of the United States\u2014\n**(1)**\nto support the constitutionally stated aspirations of Georgia to become a member of the European Union and NATO, which is made clear under Article 78 of the Constitution of Georgia and is supported by the overwhelming majority of the citizens of Georgia;\n**(2)**\nto continue supporting the capacity of the Government of Georgia to protect its sovereignty and territorial integrity from further Russian aggression or encroachment within its internationally recognized borders;\n**(3)**\nto call on all political parties and elected Members of the Parliament of Georgia to continue working on addressing the reform plan outlined by the European Commission to resume Georgia\u2019s recently granted candidate status through an inclusive and transparent consultation process that involves opposition parties and civil society organizations, which the people of Georgia have freely elected to pursue;\n**(4)**\nto reevaluate its relationship with the Government of Georgia and review all forms of foreign and security assistance made available to the Government if it takes the required steps\u2014\n**(A)**\nto reorient itself toward its European Union accession agenda; and\n**(B)**\nto advance policy or legislation reflecting the express wishes of the Georgian people;\n**(5)**\nto emphasize the importance of contributing to international efforts\u2014\n**(A)**\nto combat Russian aggression, including through sanctions on trade with Russia and the implementation and enforcement of worldwide sanctions on Russia; and\n**(B)**\nto reduce, rather than increase, trade ties between Georgia and Russia;\n**(6)**\nto continue supporting the ongoing development of democratic values in Georgia, including free and fair elections, freedom of association, an independent and accountable judiciary, an independent media, public-sector transparency and accountability, the rule of law, countering malign influence, and anti-corruption efforts and to impose swift consequences on individuals who are directly responsible for leading or have directly and knowingly engaged in leading actions of policies that significantly undermine those standards;\n**(7)**\nto continue to support the Georgian people and civil society organizations that reflect the aspirations of the Georgian people for democracy and a future with the people of Europe;\n**(8)**\nto continue supporting the right of the Georgian people to freely engage in peaceful protest, determine their future, and make independent and sovereign choices on foreign and security policy, including regarding Georgia\u2019s relationship with other countries and international organizations, without interference, intimidation, or coercion by other countries or those acting on their behalf;\n**(9)**\nto call on all political parties, elected Members of the Parliament of Georgia, and officers of the Ministry of Internal Affairs of Georgia to respect the freedoms of peaceful assembly, association, and expression, including for the press, and the rule of law, and encourage a vibrant and inclusive civil society;\n**(10)**\nto call on the Government of Georgia to release all persons detained or imprisoned on politically motivated grounds and drop any pending charges against them;\n**(11)**\nto call on the Government of Georgia to thoroughly investigate all allegations emerging from the recent national elections, which took place on October 2024, make a determination whether the elections should be judged as illegitimate and hold those responsible for interference in the elections; and\n**(12)**\nto continue impressing upon the Government of Georgia that the United States is committed to sustaining and deepening bilateral relations and supporting Georgia\u2019s Euro-Atlantic aspirations.\n#### 5. Reports and briefings\n##### (a) Report on Russian intelligence assets in Georgia\n**(1) In general**\nNot later than 180 days after the date of the enactment of this Act, the Secretary of State, in coordination with the Director of National Intelligence and the Secretary of Defense, shall submit to the appropriate committees of Congress a classified report, prepared consistent with the protection of sources and methods, examining the penetration of Russian intelligence elements and their assets in Georgia, that includes an annex examining Chinese influence and the potential intersection of Russian-Chinese cooperation in Georgia.\n**(2) Appropriate committees of Congress**\nIn this section, the term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Select Committee on Intelligence of the Senate ;\n**(C)**\nthe Committee on Armed Services of the Senate ;\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(E)**\nthe Permanent Select Committee on Intelligence of the House of Representatives ; and\n**(F)**\nthe Committee on Armed Services of the House of Representatives .\n##### (b) 5-year United States strategy for bilateral relations with Georgia\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the Secretary and the Administrator of the United States Agency for International Development, in coordination with the heads of other relevant Federal departments and agencies, shall submit to the appropriate committees of Congress a detailed strategy that\u2014\n**(A)**\noutlines specific objectives for enhancing bilateral ties which reflect the current domestic political environment in Georgia;\n**(B)**\nincludes a determination of the tools, resources, and funding that should be available to achieve the objectives outlined pursuant to subparagraph (A) and an assessment whether Georgia should remain the second-highest recipient of United States funding in the Europe and Eurasia region;\n**(C)**\nincludes a determination of the extent to which the United States should continue to invest in its partnership with Georgia;\n**(D)**\nincludes a plan for how the United States can continue to support civil society and independent media organizations in Georgia; and\n**(E)**\nincludes a determination whether the Government of Georgia remains committed to expanding trade ties with the United States and Europe and whether the United States Government should continue to invest in Georgian projects.\n**(2) Form**\nThe report required by paragraph (1) shall be submitted in unclassified form, with a classified annex.\n#### 6. Sanctions\n##### (a) Definitions\nIn this section:\n**(1) Admission; admitted; alien**\nThe terms admission , admitted , and alien have the meanings given such terms in section 101 of the Immigration and Nationality Act ( 8 U.S.C. 1101 ).\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Foreign Relations of the Senate ;\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate ;\n**(C)**\nthe Committee on the Judiciary of the Senate ;\n**(D)**\nthe Committee on Foreign Affairs of the House of Representatives ;\n**(E)**\nthe Committee on the Judiciary of the House of Representatives ; and\n**(F)**\nthe Committee on Financial Services of the House of Representatives .\n**(3) Foreign person**\nThe term foreign person means any individual or entity that is not a United States person.\n**(4) Immediate family members**\nThe term immediate family members has the meaning given the term immediate relatives in section 201(b)(2)(A)(i) of the Immigration and Nationality Act ( 8 U.S.C. 1201(b)(2)(A)(i) ).\n**(5) Knowingly**\nThe term knowingly , with respect to conduct, a circumstance, or a result, means that a person has actual knowledge, or should have known, of the conduct, the circumstance, or the result.\n**(6) Unites States person**\nThe term United States person means\u2014\n**(A)**\na United States citizen or an alien lawfully admitted for permanent residence to the United States;\n**(B)**\nan entity organized under the laws of the United States or any jurisdiction within the United States, including a foreign branch of such an entity; or\n**(C)**\nany person within the United States.\n##### (b) Inadmissibility of officials of Government of Georgia and certain other individuals involved in blocking Euro-Atlantic integration\n**(1) In general**\nNot later than 90 days after the date of the enactment of this Act, the President shall determine whether each of the following foreign persons has knowingly engaged in significant acts of corruption, or acts of violence or intimidation in relation to the blocking of Euro-Atlantic integration in Georgia:\n**(A)**\nAny individual who, on or after January 1, 2014, has served as a member of the Parliament of the Government of Georgia or as a current or former senior official of a Georgian political party.\n**(B)**\nAny individual who is serving as an official in a leadership position working on behalf of the Government of Georgia, including law enforcement, intelligence, judicial, or local or municipal government.\n**(C)**\nAn immediate family member of an official described in subparagraph (A) or a person described in subparagraph (B) who benefitted from the conduct of such official or person.\n**(2) Sanctions**\nThe President shall impose the sanctions described in subsection (d)(2) with respect to each foreign person with respect to which the President has made an affirmative decision under paragraph (1).\n**(3) Briefing**\nNot later than 90 days after the date of the enactment of this Act, the Secretary shall brief the appropriate committees of Congress with respect to\u2014\n**(A)**\nany foreign person with respect to which the President has made an affirmative determination under paragraph (1); and\n**(B)**\nthe specific facts that justify each such affirmative determination.\n**(4) Waiver**\nThe President may waive imposition of sanctions under this subsection on a case-by-case basis if the President determines and reports to the appropriate committees of Congress that\u2014\n**(A)**\nsuch waiver would serve national security interests; or\n**(B)**\nthe circumstances which caused the individual to be ineligible have sufficiently changed.\n##### (c) Imposition of sanctions with respect to undermining peace, security, stability, sovereignty or territorial integrity of Georgia\n**(1) In general**\nThe President may impose the sanctions described in subsection (d)(1) and shall impose the sanctions described in subsection (d)(2) with respect to each foreign person the President determines, on or after the date of the enactment of this Act\u2014\n**(A)**\nis responsible for, complicit in, or has directly or indirectly engaged in or attempted to engage in, actions or policies, including ordering, controlling, or otherwise directing acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia;\n**(B)**\nis or has been a leader or official of an entity that has, or whose members have, engaged in any activity described in subparagraph (A); or\n**(C)**\nis an immediate family member of a person subject to sanctions for conduct described in subparagraph (A) or (B) and benefitted from the conduct of such person.\n**(2) Brief and written notification**\nNot later than 10 days after imposing sanctions on a foreign person or persons pursuant to this subsection, the President shall brief and provide written notification to the appropriate committees of Congress regarding the imposition of such sanctions, which shall describe\u2014\n**(A)**\nthe foreign person or persons subject to the imposition of such sanctions;\n**(B)**\nthe activity justifying the imposition of such sanctions; and\n**(C)**\nthe specific sanctions imposed on such foreign person or persons.\n**(3) Waiver**\nThe President may waive the application of sanctions under this subsection with respect to a foreign person for renewable periods not to exceed 180 days if, not later than 15 days before the date on which such waiver is to take effect, the President submits to the appropriate committees of Congress a written determination and justification that the waiver is in the national security interests of the United States.\n##### (d) Sanctions described\nThe sanctions described in this subsection are the following with respect to a foreign person described in subsection (b) or (c), as applicable:\n**(1) Blocking of property**\nNotwithstanding the requirements under section 202 of the International Emergency Economic Powers Act ( 50 U.S.C. 1701 ), the President shall exercise all authorities granted under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ) to the extent necessary to block and prohibit all transactions in property and interests in property of the foreign person if such property and interests in property are in the United States, come within the United States, or are or come within the possession or control of a United States person.\n**(2) Ineligibility for visas, admission, or parole**\n**(A) Visas, admission, or parole**\nA foreign person that is an alien shall be\u2014\n**(i)**\ninadmissible to the United States;\n**(ii)**\nineligible to receive a visa or other documentation to enter the United States; and\n**(iii)**\notherwise ineligible to be admitted or paroled into the United States or to receive any other benefit under the Immigration and Nationality Act ( 8 U.S.C. 1101 et seq. ).\n**(B) Current visas revoked**\nThe foreign person shall be subject to the following:\n**(i)**\nRevocation of any visa or other entry documentation regardless of when the visa or other entry documentation is or was issued.\n**(ii)**\nA revocation under clause (i) shall take effect immediately and automatically cancel any other valid visa or entry documentation that is in the foreign person\u2019s possession.\n##### (e) Implementation; penalties\n**(1) Implementation**\nThe President may exercise all authorities provided under sections 203 and 205 of the International Emergency Economic Powers Act (50 U.S.C. 1702 and 1704) to carry out this section.\n**(2) Penalties**\nA person that violates, attempts to violate, conspires to violate, or causes a violation of subsection (d)(2)(A) or any regulation, license, or order issued under that subsection shall be subject to the penalties set forth in subsections (b) and (c) of section 206 of the International Economic Powers Act ( 50 U.S.C. 1705 ) to the same extent as a person that commits an unlawful act described in subsection (a) of that section.\n**(3) Rule of construction**\nNothing in this Act, or any amendment made by this Act, may be construed to limit the authority of the President to designate or sanction persons pursuant to an applicable Executive order or otherwise pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n##### (f) Rulemaking\n**(1) In general**\nNot later than 120 days after the date of the enactment of this Act, the President shall prescribe such regulations as are necessary for the implementation of this section.\n**(2) Notification to congress**\nNot later than 10 days before prescribing regulations pursuant to paragraph (1), the President shall notify the appropriate committees of Congress of the proposed regulations and the provisions of this section that the regulations are implementing.\n##### (g) Sanctions with respect to broader corruption in Georgia\n**(1) Determination**\nThe President shall determine whether there are foreign persons who, on or after the date of the enactment of this Act, have engaged in significant corruption in Georgia or acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia for the purposes of potential imposition of sanctions pursuant to powers granted to the President under the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ).\n**(2) Report**\n**(A) In general**\nNot later than 180 days after the date of the enactment of this Act, the President shall submit a report to the appropriate committees of Congress that\u2014\n**(i)**\nidentifies all foreign persons the President has determined, pursuant to this subsection, have engaged in significant corruption in Georgia or committed acts that are intended to undermine the peace, security, stability, sovereignty, or territorial integrity of Georgia;\n**(ii)**\nthe dates on which sanctions were imposed; and\n**(iii)**\nthe reasons for imposing such sanctions.\n**(B) Form**\nThe report required under subparagraph (A) shall be provided in unclassified form, but may include a classified annex.\n##### (h) Termination of sanctions\nAny sanctions imposed on a foreign person pursuant to this section shall terminate on the earlier of\u2014\n**(1)**\nthe date on which the President certifies to the appropriate committees of Congress that the foreign person is no longer engaging in the activities that led to the imposition of such sanction; or\n**(2)**\nthe sunset date described in section 8.\n##### (i) Exceptions\n**(1) Definitions**\nIn this subsection:\n**(A) Agricultural commodity**\nThe term agricultural commodity has the meaning given such term in section 102 of the Agricultural Trade Act of 1978 ( 7 U.S.C. 5602 ).\n**(B) Good**\nThe term good means any article, natural or man-made substance, material, supply, or manufactured product, including inspection and test equipment and excluding technical data.\n**(C) Medical device**\nThe term medical device has the meaning given the term device in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(D) Medicine**\nThe term medicine has the meaning given the term drug in section 201 of the Federal Food, Drug, and Cosmetic Act ( 21 U.S.C. 321 ).\n**(2) Exceptions**\n**(A) Exception relating to intelligence activities**\nSanctions under this section shall not apply to\u2014\n**(i)**\nany activity subject to the reporting requirements under title V of the National Security Act of 1947 ( 50 U.S.C. 3091 et seq. ); or\n**(ii)**\nany authorized intelligence activities of the United States.\n**(B) Exception to comply with international obligations**\nSanctions under this section shall not apply with respect to a foreign person if admitting or paroling the person into the United States is necessary to permit the United States to comply with the Agreement regarding the Headquarters of the United Nations, signed at Lake Success June 26, 1947, and entered into force November 21, 1947, between the United Nations and the United States, or other applicable international obligations.\n**(C) Humanitarian assistance**\nSanctions under this section shall not apply to\u2014\n**(i)**\nthe conduct or facilitation of a transaction for the provision of agricultural commodities, food, medicine, medical devices, or humanitarian assistance, or for humanitarian purposes; or\n**(ii)**\ntransactions that are necessary for, or related to, the activities described in paragraph (1).\n##### (j) Exception relating to importation of goods\nThe requirement to block and prohibit all transactions in all property and interests in property under this section shall not include the authority or a requirement to impose sanctions on the importation of goods.\n#### 7. Additional assistance with respect to Georgia\n##### (a) In general\nUpon submission to Congress of the certification described in subsection (c)\u2014\n**(1)**\nthe Secretary of State, in consultation with other heads of other relevant Federal departments and agencies, should seek to further enhance people-to-people contacts and academic exchanges between the United States and Georgia; and\n**(2)**\nthe President, in consultation with the Secretary of Defense, should maintain, and as appropriate, expand military co-operation with Georgia, including by providing further security and defense equipment ideally suited for territorial defense against Russian aggression and related training, maintenance, and operations support elements.\n##### (b) Sense of Congress\nIt is the sense of Congress that, after the submission of the certification described in subsection (c), if the Government of Georgia takes steps to realign itself with its Euro-Atlantic agenda, including significant changes to the foreign influence law, the President should take steps to improve the bilateral relationship between the United States and Georgia, including actions to bolster Georgia\u2019s ability to deter threats from Russia and other malign actors.\n##### (c) Certification described\nThe certification described in this subsection is a certification submitted to Congress by the President that Georgia has shown significant and sustained progress towards reinvigorating its democracy and advancing its Euro-Atlantic integration.\n#### 8. Sunset\nThis Act shall cease to have any force or effect beginning on the date that is 5 years after the date of the enactment of this Act.",
      "versionDate": "2025-04-28",
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
            "name": "Alliances",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Books and print media",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Collective security",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Detention of persons",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Digital media",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Elections, voting, political campaign regulation",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "European Union",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Federal officials",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Foreign property",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Georgia (Republic)",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Government ethics and transparency, public corruption",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Human rights",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2026-05-20T14:05:44Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Iran",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Political parties and affiliation",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Presidents and presidential powers, Vice Presidents",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Protest and dissent",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Rule of law and government transparency",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Russia",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Sanctions",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Sovereignty, recognition, national governance and status",
            "updateDate": "2025-06-10T18:26:17Z"
          },
          {
            "name": "Visas and passports",
            "updateDate": "2025-06-10T18:26:17Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-15T00:30:54Z"
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
      "date": "2025-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s868is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-04-28",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s868rs.xml"
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
      "title": "MEGOBARI Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:38:15Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "Mobilizing and Enhancing Georgia\u2019s Options for Building Accountability, Resilience, and Independence Act",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-05-01T02:38:15Z"
    },
    {
      "title": "MEGOBARI Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-29T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MEGOBARI Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Mobilizing and Enhancing Georgia\u2019s Options for Building Accountability, Resilience, and Independence Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-27T03:23:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to support democracy and the rule of law in Georgia, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-27T03:18:54Z"
    }
  ]
}
```
