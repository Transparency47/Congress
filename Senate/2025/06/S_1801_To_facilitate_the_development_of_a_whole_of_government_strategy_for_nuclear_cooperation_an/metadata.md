# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1801?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/1801
- Title: International Nuclear Energy Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1801
- Origin chamber: Senate
- Introduced date: 2025-05-19
- Update date: 2025-09-03T21:12:00Z
- Update date including text: 2025-09-03T21:12:00Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-19: Introduced in Senate
- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 98.
- Latest action: 2025-05-19: Introduced in Senate

## Actions

- 2025-05-19 - IntroReferral: Introduced in Senate
- 2025-05-19 - IntroReferral: Read twice and referred to the Committee on Foreign Relations.
- 2025-06-05 - Committee: Committee on Foreign Relations. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Committee: Committee on Foreign Relations. Reported by Senator Risch with an amendment in the nature of a substitute. Without written report.
- 2025-06-18 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 98.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-19",
    "latestAction": {
      "actionDate": "2025-05-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/1801",
    "number": "1801",
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
    "title": "International Nuclear Energy Act of 2025",
    "type": "S",
    "updateDate": "2025-09-03T21:12:00Z",
    "updateDateIncludingText": "2025-09-03T21:12:00Z"
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
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 98.",
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
      "actionDate": "2025-05-19",
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
      "actionDate": "2025-05-19",
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
            "date": "2025-06-18T18:23:31Z",
            "name": "Reported By"
          },
          {
            "date": "2025-06-05T14:30:10Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-19T20:14:07Z",
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
      "sponsorshipDate": "2025-05-19",
      "state": "DE"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-05-19",
      "state": "UT"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1801is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1801\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Risch (for himself, Mr. Coons , Mr. Lee , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nA BILL\nTo facilitate the development of a whole-of-government strategy for nuclear cooperation and nuclear exports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the International Nuclear Energy Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced nuclear reactor**\nThe term advanced nuclear reactor means\u2014\n**(A)**\na nuclear fission reactor, including a prototype plant (as defined in sections 50.2 and 52.1 of title 10, Code of Federal Regulations (or successor regulations)), with significant improvements compared to reactors operating on October 19, 2016, including improvements such as\u2014\n**(i)**\nadditional inherent safety features;\n**(ii)**\nlower waste yields;\n**(iii)**\nimproved fuel and material performance;\n**(iv)**\nincreased tolerance to loss of fuel cooling;\n**(v)**\nenhanced reliability or improved resilience;\n**(vi)**\nincreased proliferation resistance;\n**(vii)**\nincreased thermal efficiency;\n**(viii)**\nreduced consumption of cooling water and other environmental impacts;\n**(ix)**\nthe ability to integrate into electric applications and nonelectric applications;\n**(x)**\nmodular sizes to allow for deployment that corresponds with the demand for electricity or process heat; and\n**(xi)**\noperational flexibility to respond to changes in demand for electricity or process heat and to complement integration with intermittent renewable energy or energy storage;\n**(B)**\na fusion reactor; and\n**(C)**\na radioisotope power system that utilizes heat from radioactive decay to generate energy.\n**(2) Ally or partner nation**\nThe term ally or partner nation means\u2014\n**(A)**\nthe Government of any country that is a member of the Organisation for Economic Co-operation and Development;\n**(B)**\nthe Government of the Republic of India; and\n**(C)**\nthe Government of any country designated as an ally or partner nation by the Secretary of State for purposes of this Act.\n**(3) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committees on Foreign Relations and Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committees on Foreign Affairs and Energy and Commerce of the House of Representatives.\n**(4) Assistant**\nThe term Assistant means the Assistant to the President and Director for International Nuclear Energy Export Policy described in section 3(a)(1)(D).\n**(5) Associated entity**\nThe term associated entity means an entity that\u2014\n**(A)**\nis owned, controlled, or operated by\u2014\n**(i)**\nan ally or partner nation; or\n**(ii)**\nan associated individual; or\n**(B)**\nis organized under the laws of, or otherwise subject to the jurisdiction of, a country described in paragraph (2), including a corporation that is incorporated in a country described in that paragraph.\n**(6) Associated individual**\nThe term associated individual means a foreign national who is a national of a country described in paragraph (2).\n**(7) Civil nuclear**\nThe term civil nuclear means activities relating to\u2014\n**(A)**\nnuclear plant construction;\n**(B)**\nnuclear fuel services;\n**(C)**\nnuclear energy financing;\n**(D)**\nnuclear plant operations;\n**(E)**\nnuclear plant regulation;\n**(F)**\nnuclear medicine;\n**(G)**\nnuclear safety;\n**(H)**\ncommunity engagement in areas in reasonable proximity to nuclear sites;\n**(I)**\ninfrastructure support for nuclear energy;\n**(J)**\nnuclear plant decommissioning;\n**(K)**\nnuclear liability;\n**(L)**\nsafe storage and safe disposal of spent nuclear fuel;\n**(M)**\nenvironmental safeguards;\n**(N)**\nnuclear nonproliferation and security; and\n**(O)**\ntechnology related to the matters described in subparagraphs (A) through (N).\n**(8) Embarking civil nuclear nation**\n**(A) In general**\nThe term embarking civil nuclear nation means a country that\u2014\n**(i)**\ndoes not have a civil nuclear energy program;\n**(ii)**\nis in the process of developing or expanding a civil nuclear energy program, including safeguards and a legal and regulatory framework, for\u2014\n**(I)**\nnuclear safety;\n**(II)**\nnuclear security;\n**(III)**\nradioactive waste management;\n**(IV)**\ncivil nuclear energy;\n**(V)**\nenvironmental safeguards;\n**(VI)**\ncommunity engagement in areas in reasonable proximity to nuclear sites;\n**(VII)**\nnuclear liability; or\n**(VIII)**\nadvanced nuclear reactor licensing;\n**(iii)**\nis in the process of selecting, developing, constructing, or utilizing advanced light water reactors, advanced nuclear reactors, or advanced civil nuclear technologies; or\n**(iv)**\nis eligible to receive development lending from the World Bank.\n**(B) Exclusions**\nThe term embarking civil nuclear nation does not include\u2014\n**(i)**\nthe People\u2019s Republic of China;\n**(ii)**\nthe Russian Federation;\n**(iii)**\nthe Republic of Belarus;\n**(iv)**\nthe Islamic Republic of Iran;\n**(v)**\nthe Democratic People\u2019s Republic of Korea;\n**(vi)**\nthe Republic of Cuba;\n**(vii)**\nthe Bolivarian Republic of Venezuela;\n**(viii)**\nthe Syrian Arab Republic;\n**(ix)**\nBurma; or\n**(x)**\nany other country\u2014\n**(I)**\nthe property or interests in property of the government of which are blocked pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); or\n**(II)**\nthe government of which the Secretary of State has determined has repeatedly provided support for acts of international terrorism for purposes of\u2014\n**(aa)**\nsection 620A(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371(a) );\n**(bb)**\nsection 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) );\n**(cc)**\nsection 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); or\n**(dd)**\nany other relevant provision of law.\n**(9) National Energy Dominance Council**\nThe term National Energy Dominance Council means the National Energy Dominance Council established within the Executive Office of the President under Executive Order 14213 (90 Fed. Reg. 9945; relating to establishing the National Energy Dominance Council).\n**(10) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(11) Spent nuclear fuel**\nThe term spent nuclear fuel has the meaning given the term in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 ).\n**(12) U.S. nuclear energy company**\nThe term U.S. nuclear energy company means a company that\u2014\n**(A)**\nis organized under the laws of, or otherwise subject to the jurisdiction of, the United States; and\n**(B)**\nis involved in the nuclear energy industry.\n#### 3. Civil nuclear coordination and strategy\n##### (a) White house focal point on civil nuclear coordination\n**(1) Sense of congress**\nGiven the critical importance of developing and implementing, with input from various agencies throughout the executive branch, a cohesive policy with respect to international efforts related to civil nuclear energy, it is the sense of Congress that\u2014\n**(A)**\nthere should be a focal point within the White House, which may, if determined to be appropriate, report to the National Security Council, for coordination on issues relating to those efforts;\n**(B)**\nto provide that focal point, the President should designate, within the National Energy Dominance Council, an office, to be known as the Office of the Assistant to the President and Director for International Nuclear Energy Export Policy (referred to in this subsection as the Office );\n**(C)**\nthe Office should act as a coordinating office for\u2014\n**(i)**\ninternational civil nuclear cooperation; and\n**(ii)**\ncivil nuclear export strategy;\n**(D)**\nthe Office should be headed by an individual appointed as an Assistant to the President with the title of Director for International Nuclear Energy Export Policy who is also a member of the National Energy Dominance Council; and\n**(E)**\nthe Office should\u2014\n**(i)**\ncoordinate civil nuclear export policies for the United States;\n**(ii)**\ndevelop, in coordination with the officials described in paragraph (2), a cohesive Federal strategy for engagement with foreign governments (including ally or partner nations and the governments of embarking civil nuclear nations), associated entities, and associated individuals with respect to civil nuclear exports;\n**(iii)**\ncoordinate with the officials described in paragraph (2) to ensure that necessary framework agreements and trade controls relating to civil nuclear materials and technologies are in place for key markets; and\n**(iv)**\ndevelop\u2014\n**(I)**\na whole-of-government coordinating strategy for civil nuclear cooperation;\n**(II)**\na whole-of-government strategy for civil nuclear exports; and\n**(III)**\na whole-of-government approach to support appropriate foreign investment in civil nuclear energy projects supported by the United States in embarking civil nuclear nations.\n**(2) Officials described**\nThe officials referred to in paragraph (1)(E) are\u2014\n**(A)**\nappropriate officials of any Federal agency that the President determines to be appropriate; and\n**(B)**\nappropriate officials representing foreign countries and governments, including\u2014\n**(i)**\nally or partner nations;\n**(ii)**\nembarking civil nuclear nations; and\n**(iii)**\nany other country or government that the Assistant (if appointed) and the officials described in subparagraph (A) jointly determine to be appropriate.\n##### (b) Nuclear exports working group\n**(1) Establishment**\nThere is established a working group, to be known as the Nuclear Exports Working Group (referred to in this subsection as the working group ).\n**(2) Composition**\nThe working group shall be composed of\u2014\n**(A)**\nsenior-level Federal officials, selected internally by the applicable Federal agency or organization, from any Federal agency or organization that the President determines to be appropriate; and\n**(B)**\nother senior-level Federal officials, selected internally by the applicable Federal agency or organization, from any other Federal agency or organization that the Secretary determines to be appropriate.\n**(3) Reporting**\nThe working group shall report to the appropriate White House official, which may be the Assistant (if appointed).\n**(4) Duties**\nThe working group shall coordinate, not less frequently than quarterly, with the Civil Nuclear Trade Advisory Committee of the Department of Commerce, the Nuclear Energy Advisory Committee of the Department of Energy, and other advisory or stakeholder groups, as necessary, to maintain an accurate and up-to-date knowledge of the standing of civil nuclear exports from the United States, including with respect to meeting the targets established as part of the 10-year civil nuclear trade strategy described in paragraph (5)(A).\n**(5) Strategy**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the working group shall establish a 10-year civil nuclear trade strategy, including biennial targets for the export of civil nuclear technologies, including light water and non-light water reactors and associated equipment and technologies, civil nuclear materials, and nuclear fuel that align with meeting international energy demand while seeking to avoid or reduce emissions.\n**(B) Collaboration required**\nIn establishing the strategy under subparagraph (A), the working group shall collaborate with\u2014\n**(i)**\nany Federal agency that the President determines to be appropriate; and\n**(ii)**\nrepresentatives of private industry.\n#### 4. Engagement with ally or partner nations\n##### (a) In general\nThe President shall launch, in accordance with applicable nuclear technology export laws (including regulations), an international initiative to modernize the civil nuclear outreach to embarking civil nuclear nations.\n##### (b) Financing\nIn carrying out the initiative described in subsection (a), the President, acting through an appropriate Federal official, who may be the Assistant (if appointed), if determined to be appropriate, and in coordination with the officials described in section 3(a)(2), may, if the President determines to be appropriate, seek to establish cooperative financing relationships for the export of civil nuclear technology, components, materials, and infrastructure to embarking civil nuclear nations.\n##### (c) Activities\nIn carrying out the initiative described in subsection (a), the President shall\u2014\n**(1)**\nassist nongovernmental organizations and appropriate offices, administrations, agencies, laboratories, and programs of the Department of Energy and other relevant Federal agencies and offices in providing education and training to foreign governments in nuclear safety, security, and safeguards\u2014\n**(A)**\nthrough engagement with the International Atomic Energy Agency; or\n**(B)**\nindependently, if the applicable entity determines that it would be more advantageous under the circumstances to provide the applicable education and training independently;\n**(2)**\nassist the efforts of the International Atomic Energy Agency to expand the support provided by the International Atomic Energy Agency to embarking civil nuclear nations for nuclear safety, security, and safeguards;\n**(3)**\ncoordinate with appropriate Federal departments and agencies on efforts to expand outreach to the private investment community and establish public-private financing relationships that enable the adoption of civil nuclear technologies by embarking civil nuclear nations, including through exports from the United States;\n**(4)**\nseek to better coordinate, to the maximum extent practicable, the work carried out by any Federal agency that the President determines to be appropriate; and\n**(5)**\ncoordinate with the Export-Import Bank of the United States to improve the efficient and effective exporting and importing of civil nuclear technologies and materials.\n#### 5. Cooperative financing relationships with ally or partner nations and embarking civil nuclear nations\n##### (a) In general\nThe President shall designate an appropriate White House official, who may be the Assistant (if appointed), to coordinate with the officials described in section 3(a)(2) to develop, as the President determines to be appropriate, financing relationships with ally or partner nations to assist in the adoption of civil nuclear technologies exported from the United States or ally or partner nations to embarking civil nuclear nations.\n##### (b) United States competitiveness clauses\n**(1) Definition of United States competitiveness clause**\nIn this subsection, the term United States competitiveness clause means any United States competitiveness provision in any agreement entered into by the Department of Energy, including\u2014\n**(A)**\na cooperative agreement;\n**(B)**\na cooperative research and development agreement; and\n**(C)**\na patent waiver.\n**(2) Consideration**\nIn carrying out subsection (a), the relevant officials described in that subsection shall consider the impact of United States competitiveness clauses on any financing relationships entered into or proposed to be entered into under that subsection.\n**(3) Waiver**\nThe Secretary shall facilitate waivers of United States competitiveness clauses as necessary to facilitate financing relationships with ally or partner nations under subsection (a).\n#### 6. Cooperation with ally or partner nations on advanced nuclear reactor demonstration and cooperative research facilities for civil nuclear energy\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of State, in coordination with the Secretary and the Secretary of Commerce, shall conduct bilateral and multilateral meetings with not fewer than 5 ally or partner nations, with the aim of enhancing nuclear energy cooperation among those ally or partner nations and the United States, for the purpose of developing collaborative relationships with respect to research, development, licensing, and deployment of advanced nuclear reactor technologies for civil nuclear energy.\n##### (b) Requirement\nThe meetings described in subsection (a) shall include\u2014\n**(1)**\na focus on cooperation to demonstrate and deploy advanced nuclear reactors, with an emphasis on U.S. nuclear energy companies, during the 10-year period beginning on the date of enactment of this Act to provide options for addressing energy security and climate change; and\n**(2)**\na focus on developing a memorandum of understanding or any other appropriate agreement between the United States and ally or partner nations with respect to\u2014\n**(A)**\nthe demonstration and deployment of advanced nuclear reactors; and\n**(B)**\nthe development of cooperative research facilities.\n##### (c) Financing arrangements\nIn conducting the meetings described in subsection (a), the Secretary of State, in coordination with the Secretary, the Secretary of Commerce, and the heads of other relevant Federal agencies and only after initial consultation with the appropriate committees of Congress, shall seek to develop financing arrangements to share the costs of the demonstration and deployment of advanced nuclear reactors and the development of cooperative research facilities with the ally or partner nations participating in those meetings.\n##### (d) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary, the Secretary of State, and the Secretary of Commerce shall jointly submit to the appropriate committees of Congress a report highlighting potential partners\u2014\n**(1)**\nfor the establishment of cost-share arrangements described in subsection (c) and the details of those arrangements; or\n**(2)**\nwith which the United States may enter into agreements with respect to\u2014\n**(A)**\nthe demonstration of advanced nuclear reactors; or\n**(B)**\ncooperative research facilities.\n#### 7. International civil nuclear energy cooperation\nSection 959B of the Energy Policy Act of 2005 ( 42 U.S.C. 16279b ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Secretary and inserting the following:\n(a) In general The Secretary ;\n**(2)**\nin subsection (a) (as so designated)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking financing, ; and\n**(ii)**\nby striking and after the semicolon at the end;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking preparations for ; and\n**(ii)**\nin subparagraph (C)(v), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(3) to support, with the concurrence of the Secretary of State, the safe, secure, and peaceful use of civil nuclear technology in countries developing nuclear energy programs, with a focus on countries that have increased civil nuclear cooperation with the Russian Federation or the People\u2019s Republic of China; and (4) to promote the fullest utilization of the reactors, fuel, equipment, services, and technology of U.S. nuclear energy companies (as defined in section 2 of the International Nuclear Energy Act of 2025 ) in civil nuclear energy programs outside the United States through\u2014 (A) bilateral and multilateral arrangements developed and executed with the concurrence of the Secretary of State that contain commitments for the utilization of the reactors, fuel, equipment, services, and technology of U.S. nuclear energy companies (as defined in that section); (B) the designation of 1 or more U.S. nuclear energy companies (as defined in that section) to implement an arrangement under subparagraph (A) if the Secretary determines that the designation is necessary and appropriate to achieve the objectives of this section; and (C) the waiver of any provision of law relating to competition with respect to any activity related to an arrangement under subparagraph (A) if the Secretary, in consultation with the Attorney General and the Secretary of Commerce, determines that a waiver is necessary and appropriate to achieve the objectives of this section. ; and\n**(3)**\nby adding at the end the following:\n(b) Requirements The program under subsection (a) shall be supported in consultation with the Secretary of State and implemented by the Secretary\u2014 (1) to facilitate, to the maximum extent practicable, workshops and expert-based exchanges to engage industry, stakeholders, and foreign governments with respect to international civil nuclear issues, such as\u2014 (A) training; (B) financing; (C) safety; (D) security; (E) safeguards; (F) liability; (G) advanced fuels; (H) operations; and (I) options for multinational cooperation with respect to the disposal of spent nuclear fuel (as defined in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 )); and (2) in coordination with any Federal agency that the President determines to be appropriate. (c) Authorization of appropriations Of funds appropriated or otherwise made available to the Secretary to carry out the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) in fiscal years 2026 through 2030, the Secretary may use $15,500,000 to carry out this section. .\n#### 8. International civil nuclear program support\n##### (a) In general\nNot later than 120 days after the date of enactment of this Act, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), shall launch an international initiative (referred to in this section as the initiative ) to provide financial assistance to, and facilitate the building of technical capacities by, in accordance with this section, embarking civil nuclear nations for activities relating to the development of civil nuclear energy programs.\n##### (b) Financial assistance\n**(1) In general**\nIn carrying out the initiative, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), is authorized to award grants of financial assistance in amounts not greater than $5,500,000 to embarking civil nuclear nations in accordance with this subsection\u2014\n**(A)**\nfor activities relating to the development of civil nuclear energy programs; and\n**(B)**\nto facilitate the building of technical capacities for those activities.\n**(2) Limitations**\nThe Secretary of State, in coordination with the Secretary and the Assistant (if appointed), may award\u2014\n**(A)**\nnot more than 1 grant of financial assistance under paragraph (1) to any 1 embarking civil nuclear nation each fiscal year; and\n**(B)**\nnot more than a total of 5 grants of financial assistance under paragraph (1) to any 1 embarking civil nuclear nation.\n##### (c) Senior advisors\n**(1) In general**\nIn carrying out the initiative, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), is authorized to provide financial assistance to an embarking civil nuclear nation for the purpose of contracting with a U.S. nuclear energy company to hire 1 or more senior advisors to assist the embarking civil nuclear nation in establishing a civil nuclear program.\n**(2) Requirement**\nA senior advisor described in paragraph (1) shall have relevant experience and qualifications to advise the embarking civil nuclear nation on, and facilitate on behalf of the embarking civil nuclear nation, 1 or more of the following activities:\n**(A)**\nThe development of financing relationships.\n**(B)**\nThe development of a standardized financing and project management framework for the construction of nuclear power plants.\n**(C)**\nThe development of a standardized licensing framework for\u2014\n**(i)**\nlight water civil nuclear technologies; and\n**(ii)**\nnon-light water civil nuclear technologies and advanced nuclear reactors.\n**(D)**\nThe identification of qualified organizations and service providers.\n**(E)**\nThe identification of funds to support payment for services required to develop a civil nuclear program.\n**(F)**\nMarket analysis.\n**(G)**\nThe identification of the safety, security, safeguards, and nuclear governance required for a civil nuclear program.\n**(H)**\nRisk allocation, risk management, and nuclear liability.\n**(I)**\nTechnical assessments of nuclear reactors and technologies.\n**(J)**\nThe identification of actions necessary to participate in a global nuclear liability regime based on the Convention on Supplementary Compensation for Nuclear Damage, with Annex, done at Vienna September 12, 1997 (TIAS 15\u2013415).\n**(K)**\nStakeholder engagement.\n**(L)**\nManagement of spent nuclear fuel and nuclear waste.\n**(M)**\nAny other major activities to support the establishment of a civil nuclear program, such as the establishment of export, financing, construction, training, operations, and education requirements.\n**(3) Clarification**\nFinancial assistance under this subsection is authorized to be provided to an embarking civil nuclear nation in addition to any financial assistance provided to that embarking civil nuclear nation under subsection (b).\n##### (d) Limitation on assistance to embarking civil nuclear nations\nNot later than 1 year after the date of enactment of this Act, the Offices of the Inspectors General for the Department of State and the Department of Energy shall coordinate\u2014\n**(1)**\nto establish and submit to the appropriate committees of Congress a joint strategic plan to conduct comprehensive oversight of activities authorized under this section to prevent fraud, waste, and abuse; and\n**(2)**\nto engage in independent and effective oversight of activities authorized under this section through joint or individual audits, inspections, investigations, or evaluations.\n##### (e) Authorization of appropriations\nOf funds appropriated or otherwise made available to the Secretary of State to carry out the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) in fiscal years 2026 through 2030, the Secretary of State may use $50,000,000 to carry out this section.\n#### 9. Biennial cabinet-level international conference on nuclear safety, security, safeguards, and sustainability\n##### (a) In general\nThe President, in coordination with international partners, as determined by the President, and industry, shall hold a biennial conference on civil nuclear safety, security, safeguards, and sustainability (referred to in this section as a conference ).\n##### (b) Conference functions\nIt is the sense of Congress that each conference should\u2014\n**(1)**\nbe a forum in which ally or partner nations may engage with each other for the purpose of reinforcing the commitment to\u2014\n**(A)**\nnuclear safety, security, safeguards, and sustainability;\n**(B)**\nenvironmental safeguards; and\n**(C)**\nlocal community engagement in areas in reasonable proximity to nuclear sites; and\n**(2)**\nfacilitate\u2014\n**(A)**\nthe development of\u2014\n**(i)**\njoint commitments and goals to improve\u2014\n**(I)**\nnuclear safety, security, safeguards, and sustainability;\n**(II)**\nenvironmental safeguards; and\n**(III)**\nlocal community engagement in areas in reasonable proximity to nuclear sites;\n**(ii)**\nstronger international institutions that support nuclear safety, security, safeguards, and sustainability;\n**(iii)**\ncooperative financing relationships to promote competitive alternatives to Chinese and Russian financing;\n**(iv)**\na standardized financing and project management framework for the construction of civil nuclear power plants;\n**(v)**\na standardized licensing framework for civil nuclear technologies;\n**(vi)**\na strategy to change internal policies of multinational development banks, such as the World Bank, to support the financing of civil nuclear projects;\n**(vii)**\na document containing any lessons learned from countries that have partnered with the Russian Federation or the People\u2019s Republic of China with respect to civil nuclear power, including any detrimental outcomes resulting from that partnership; and\n**(viii)**\na global civil nuclear liability regime;\n**(B)**\ncooperation for enhancing the overall aspects of civil nuclear power, such as\u2014\n**(i)**\nnuclear safety, security, safeguards, and sustainability;\n**(ii)**\nnuclear laws (including regulations);\n**(iii)**\nwaste management;\n**(iv)**\nquality management systems;\n**(v)**\ntechnology transfer;\n**(vi)**\nhuman resources development;\n**(vii)**\nlocalization;\n**(viii)**\nreactor operations;\n**(ix)**\nnuclear liability; and\n**(x)**\ndecommissioning; and\n**(C)**\nthe development and determination of the mechanisms described in paragraphs (7) and (8) of section 10(a), if the President intends to establish an Advanced Reactor Coordination and Resource Center as described in that section.\n##### (c) Input from industry and government\nIt is the sense of Congress that each conference should include a meeting that convenes nuclear industry leaders and leaders of government agencies with expertise relating to nuclear safety, security, safeguards, or sustainability to discuss best practices relating to\u2014\n**(1)**\nthe safe and secure use, storage, and transport of nuclear and radiological materials;\n**(2)**\nmanaging the evolving cyber threat to nuclear and radiological security; and\n**(3)**\nthe role that the nuclear industry should play in nuclear and radiological safety, security, and safeguards, including with respect to the safe and secure use, storage, and transport of nuclear and radiological materials, including spent nuclear fuel and nuclear waste.\n#### 10. Advanced reactor coordination and resource center\n##### (a) In general\nThe President shall consider the feasibility of leveraging existing activities or frameworks or, as necessary, establishing a center, to be known as the Advanced Reactor Coordination and Resource Center (referred to in this section as the Center ), for the purposes of\u2014\n**(1)**\nidentifying qualified organizations and service providers\u2014\n**(A)**\nfor embarking civil nuclear nations;\n**(B)**\nto develop and assemble documents, contracts, and related items required to establish a civil nuclear program; and\n**(C)**\nto develop a standardized model for the establishment of a civil nuclear program that can be used by the International Atomic Energy Agency;\n**(2)**\ncoordinating with countries participating in the Center and with the Nuclear Exports Working Group established under section 3(b)\u2014\n**(A)**\nto identify funds to support payment for services required to develop a civil nuclear program;\n**(B)**\nto provide market analysis; and\n**(C)**\nto create\u2014\n**(i)**\nproject structure models;\n**(ii)**\nmodels for electricity market analysis;\n**(iii)**\nmodels for nonelectric applications market analysis; and\n**(iv)**\nfinancial models;\n**(3)**\nidentifying and developing the safety, security, safeguards, and nuclear governance required for a civil nuclear program;\n**(4)**\nsupporting multinational regulatory standards to be developed by countries with civil nuclear programs and experience;\n**(5)**\ndeveloping and strengthening communications, engagement, and consensus-building;\n**(6)**\ncarrying out any other major activities to support export, financing, education, construction, training, and education requirements relating to the establishment of a civil nuclear program;\n**(7)**\ndeveloping mechanisms for how to fund and staff the Center; and\n**(8)**\ndetermining mechanisms for the selection of the location or locations of the Center.\n##### (b) Objective\nThe President shall carry out subsection (a) with the objective of establishing the Center if the President determines that it is feasible to do so.\n#### 11. Strategic infrastructure fund working group\n##### (a) Establishment\nThere is established a working group, to be known as the Strategic Infrastructure Fund Working Group (referred to in this section as the working group ) to provide input on the feasibility of establishing a program to support strategically important capital-intensive infrastructure projects.\n##### (b) Composition\nThe working group shall be\u2014\n**(1)**\nled by a White House official, who may be the Assistant (if appointed), who shall serve as the White House focal point with respect to matters relating to the working group; and\n**(2)**\ncomposed of\u2014\n**(A)**\nsenior-level Federal officials, selected by the head of the applicable Federal agency or organization, from any Federal agency or organization that the President determines to be appropriate;\n**(B)**\nother senior-level Federal officials, selected by the head of the applicable Federal agency or organization, from any other Federal agency or organization that the Secretary determines to be appropriate; and\n**(C)**\nany senior-level Federal official selected by the White House official described in paragraph (1) from any Federal agency or organization.\n##### (c) Reporting\nThe working group shall report to the National Security Council.\n##### (d) Duties\nThe working group shall\u2014\n**(1)**\nprovide direction and advice to the officials described in section 3(a)(2)(A) and appropriate Federal agencies, as determined by the working group, with respect to the establishment of a Strategic Infrastructure Fund (referred to in this subsection as the Fund ) to be used\u2014\n**(A)**\nto support those aspects of projects relating to\u2014\n**(i)**\ncivil nuclear technologies; and\n**(ii)**\nmicroprocessors; and\n**(B)**\nfor strategic investments identified by the working group; and\n**(2)**\naddress critical areas in determining the appropriate design for the Fund, including\u2014\n**(A)**\ntransfer of assets to the Fund;\n**(B)**\ntransfer of assets from the Fund;\n**(C)**\nhow assets in the Fund should be invested; and\n**(D)**\ngovernance and implementation of the Fund.\n##### (e) Briefing and report required\n**(1) Briefing**\nNot later than 180 days after the date of enactment of this Act, the working group shall brief the committees described in paragraph (3) on the status of the development of the processes necessary to implement this section.\n**(2) Report**\nNot later than 1 year after the date of the enactment of this Act, the working group shall submit to the committees described in paragraph (3) a report on the findings of the working group that includes suggested legislative text for how to establish and structure a Strategic Infrastructure Fund.\n**(3) Committees described**\nThe committees referred to in paragraphs (1) and (2) are\u2014\n**(A)**\nthe Committee on Foreign Relations, the Committee on Commerce, Science, and Transportation, the Committee on Armed Services, the Committee on Energy and Natural Resources, the Committee on Environment and Public Works, the Committee on Finance, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs, the Committee on Energy and Commerce, the Committee on Armed Services, the Committee on Science, Space, and Technology, the Committee on Ways and Means, and the Committee on Appropriations of the House of Representatives.\n**(4) Administration of the fund**\nThe report submitted under paragraph (2) shall include suggested legislative language requiring all expenditures from a Strategic Infrastructure Fund established in accordance with this section to be administered by the Secretary of State (or a designee of the Secretary of State).\n#### 12. Joint assessment between the United States and india on nuclear liability rules\n##### (a) In general\nThe Secretary of State, in consultation with the heads of other relevant Federal departments and agencies, shall establish and maintain within the U.S.-India Strategic Security Dialogue a joint consultative mechanism with the Government of the Republic of India that convenes on a recurring basis\u2014\n**(1)**\nto assess the implementation of the Agreement for Cooperation between the Government of the United States of America and the Government of India Concerning Peaceful Uses of Nuclear Energy, signed at Washington October 10, 2008 (TIAS 08\u20131206);\n**(2)**\nto discuss opportunities for the Republic of India to align domestic nuclear liability rules with international norms; and\n**(3)**\nto develop a strategy for the United States and the Republic of India to pursue bilateral and multilateral diplomatic engagements related to analyzing and implementing those opportunities.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in consultation with the heads of other relevant Federal departments and agencies, shall submit to the appropriate committees of Congress a report that describes the joint assessment developed pursuant to subsection (a)(1).\n#### 13. Rule of construction\nExcept as expressly stated in this Act, nothing in this Act may be construed to alter or otherwise affect the interpretation or implementation of section 123 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2153 ) or any other provision of law, including the requirement that agreements pursuant to that section be submitted to Congress for consideration.",
      "versionDate": "2025-05-19",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1801rs.xml",
      "text": "II\nCalendar No. 98\n119th CONGRESS\n1st Session\nS. 1801\nIN THE SENATE OF THE UNITED STATES\nMay 19, 2025 Mr. Risch (for himself, Mr. Coons , Mr. Lee , and Mr. Heinrich ) introduced the following bill; which was read twice and referred to the Committee on Foreign Relations\nJune 18, 2025 Reported by Mr. Risch , with an amendment Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo facilitate the development of a whole-of-government strategy for nuclear cooperation and nuclear exports, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the International Nuclear Energy Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Advanced nuclear reactor**\nThe term advanced nuclear reactor means\u2014\n**(A)**\na nuclear fission reactor, including a prototype plant (as defined in sections 50.2 and 52.1 of title 10, Code of Federal Regulations (or successor regulations)), with significant improvements compared to reactors operating on October 19, 2016, including improvements such as\u2014\n**(i)**\nadditional inherent safety features;\n**(ii)**\nlower waste yields;\n**(iii)**\nimproved fuel and material performance;\n**(iv)**\nincreased tolerance to loss of fuel cooling;\n**(v)**\nenhanced reliability or improved resilience;\n**(vi)**\nincreased proliferation resistance;\n**(vii)**\nincreased thermal efficiency;\n**(viii)**\nreduced consumption of cooling water and other environmental impacts;\n**(ix)**\nthe ability to integrate into electric applications and nonelectric applications;\n**(x)**\nmodular sizes to allow for deployment that corresponds with the demand for electricity or process heat; and\n**(xi)**\noperational flexibility to respond to changes in demand for electricity or process heat and to complement integration with intermittent renewable energy or energy storage;\n**(B)**\na fusion reactor; and\n**(C)**\na radioisotope power system that utilizes heat from radioactive decay to generate energy.\n**(2) Ally or partner nation**\nThe term ally or partner nation means\u2014\n**(A)**\nthe Government of any country that is a member of the Organisation for Economic Co-operation and Development;\n**(B)**\nthe Government of the Republic of India; and\n**(C)**\nthe Government of any country designated as an ally or partner nation by the Secretary of State for purposes of this Act.\n**(3) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committees on Foreign Relations and Energy and Natural Resources of the Senate; and\n**(B)**\nthe Committees on Foreign Affairs and Energy and Commerce of the House of Representatives.\n**(4) Assistant**\nThe term Assistant means the Assistant to the President and Director for International Nuclear Energy Export Policy described in section 3(a)(1)(D).\n**(5) Associated entity**\nThe term associated entity means an entity that\u2014\n**(A)**\nis owned, controlled, or operated by\u2014\n**(i)**\nan ally or partner nation; or\n**(ii)**\nan associated individual; or\n**(B)**\nis organized under the laws of, or otherwise subject to the jurisdiction of, a country described in paragraph (2), including a corporation that is incorporated in a country described in that paragraph.\n**(6) Associated individual**\nThe term associated individual means a foreign national who is a national of a country described in paragraph (2).\n**(7) Civil nuclear**\nThe term civil nuclear means activities relating to\u2014\n**(A)**\nnuclear plant construction;\n**(B)**\nnuclear fuel services;\n**(C)**\nnuclear energy financing;\n**(D)**\nnuclear plant operations;\n**(E)**\nnuclear plant regulation;\n**(F)**\nnuclear medicine;\n**(G)**\nnuclear safety;\n**(H)**\ncommunity engagement in areas in reasonable proximity to nuclear sites;\n**(I)**\ninfrastructure support for nuclear energy;\n**(J)**\nnuclear plant decommissioning;\n**(K)**\nnuclear liability;\n**(L)**\nsafe storage and safe disposal of spent nuclear fuel;\n**(M)**\nenvironmental safeguards;\n**(N)**\nnuclear nonproliferation and security; and\n**(O)**\ntechnology related to the matters described in subparagraphs (A) through (N).\n**(8) Embarking civil nuclear nation**\n**(A) In general**\nThe term embarking civil nuclear nation means a country that\u2014\n**(i)**\ndoes not have a civil nuclear energy program;\n**(ii)**\nis in the process of developing or expanding a civil nuclear energy program, including safeguards and a legal and regulatory framework, for\u2014\n**(I)**\nnuclear safety;\n**(II)**\nnuclear security;\n**(III)**\nradioactive waste management;\n**(IV)**\ncivil nuclear energy;\n**(V)**\nenvironmental safeguards;\n**(VI)**\ncommunity engagement in areas in reasonable proximity to nuclear sites;\n**(VII)**\nnuclear liability; or\n**(VIII)**\nadvanced nuclear reactor licensing;\n**(iii)**\nis in the process of selecting, developing, constructing, or utilizing advanced light water reactors, advanced nuclear reactors, or advanced civil nuclear technologies; or\n**(iv)**\nis eligible to receive development lending from the World Bank.\n**(B) Exclusions**\nThe term embarking civil nuclear nation does not include\u2014\n**(i)**\nthe People\u2019s Republic of China;\n**(ii)**\nthe Russian Federation;\n**(iii)**\nthe Republic of Belarus;\n**(iv)**\nthe Islamic Republic of Iran;\n**(v)**\nthe Democratic People\u2019s Republic of Korea;\n**(vi)**\nthe Republic of Cuba;\n**(vii)**\nthe Bolivarian Republic of Venezuela;\n**(viii)**\nthe Syrian Arab Republic;\n**(ix)**\nBurma; or\n**(x)**\nany other country\u2014\n**(I)**\nthe property or interests in property of the government of which are blocked pursuant to the International Emergency Economic Powers Act ( 50 U.S.C. 1701 et seq. ); or\n**(II)**\nthe government of which the Secretary of State has determined has repeatedly provided support for acts of international terrorism for purposes of\u2014\n**(aa)**\nsection 620A(a) of the Foreign Assistance Act of 1961 ( 22 U.S.C. 2371(a) );\n**(bb)**\nsection 40(d) of the Arms Export Control Act ( 22 U.S.C. 2780(d) );\n**(cc)**\nsection 1754(c)(1)(A)(i) of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813(c)(1)(A)(i) ); or\n**(dd)**\nany other relevant provision of law.\n**(9) National Energy Dominance Council**\nThe term National Energy Dominance Council means the National Energy Dominance Council established within the Executive Office of the President under Executive Order 14213 (90 Fed. Reg. 9945; relating to establishing the National Energy Dominance Council).\n**(10) Secretary**\nThe term Secretary means the Secretary of Energy.\n**(11) Spent nuclear fuel**\nThe term spent nuclear fuel has the meaning given the term in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 ).\n**(12) U.S. nuclear energy company**\nThe term U.S. nuclear energy company means a company that\u2014\n**(A)**\nis organized under the laws of, or otherwise subject to the jurisdiction of, the United States; and\n**(B)**\nis involved in the nuclear energy industry.\n#### 3. Civil nuclear coordination and strategy\n##### (a) White house focal point on civil nuclear coordination\n**(1) Sense of congress**\nGiven the critical importance of developing and implementing, with input from various agencies throughout the executive branch, a cohesive policy with respect to international efforts related to civil nuclear energy, it is the sense of Congress that\u2014\n**(A)**\nthere should be a focal point within the White House, which may, if determined to be appropriate, report to the National Security Council, for coordination on issues relating to those efforts;\n**(B)**\nto provide that focal point, the President should designate, within the National Energy Dominance Council, an office, to be known as the Office of the Assistant to the President and Director for International Nuclear Energy Export Policy (referred to in this subsection as the Office );\n**(C)**\nthe Office should act as a coordinating office for\u2014\n**(i)**\ninternational civil nuclear cooperation; and\n**(ii)**\ncivil nuclear export strategy;\n**(D)**\nthe Office should be headed by an individual appointed as an Assistant to the President with the title of Director for International Nuclear Energy Export Policy who is also a member of the National Energy Dominance Council; and\n**(E)**\nthe Office should\u2014\n**(i)**\ncoordinate civil nuclear export policies for the United States;\n**(ii)**\ndevelop, in coordination with the officials described in paragraph (2), a cohesive Federal strategy for engagement with foreign governments (including ally or partner nations and the governments of embarking civil nuclear nations), associated entities, and associated individuals with respect to civil nuclear exports;\n**(iii)**\ncoordinate with the officials described in paragraph (2) to ensure that necessary framework agreements and trade controls relating to civil nuclear materials and technologies are in place for key markets; and\n**(iv)**\ndevelop\u2014\n**(I)**\na whole-of-government coordinating strategy for civil nuclear cooperation;\n**(II)**\na whole-of-government strategy for civil nuclear exports; and\n**(III)**\na whole-of-government approach to support appropriate foreign investment in civil nuclear energy projects supported by the United States in embarking civil nuclear nations.\n**(2) Officials described**\nThe officials referred to in paragraph (1)(E) are\u2014\n**(A)**\nappropriate officials of any Federal agency that the President determines to be appropriate; and\n**(B)**\nappropriate officials representing foreign countries and governments, including\u2014\n**(i)**\nally or partner nations;\n**(ii)**\nembarking civil nuclear nations; and\n**(iii)**\nany other country or government that the Assistant (if appointed) and the officials described in subparagraph (A) jointly determine to be appropriate.\n##### (b) Nuclear exports working group\n**(1) Establishment**\nThere is established a working group, to be known as the Nuclear Exports Working Group (referred to in this subsection as the working group ).\n**(2) Composition**\nThe working group shall be composed of\u2014\n**(A)**\nsenior-level Federal officials, selected internally by the applicable Federal agency or organization, from any Federal agency or organization that the President determines to be appropriate; and\n**(B)**\nother senior-level Federal officials, selected internally by the applicable Federal agency or organization, from any other Federal agency or organization that the Secretary determines to be appropriate.\n**(3) Reporting**\nThe working group shall report to the appropriate White House official, which may be the Assistant (if appointed).\n**(4) Duties**\nThe working group shall coordinate, not less frequently than quarterly, with the Civil Nuclear Trade Advisory Committee of the Department of Commerce, the Nuclear Energy Advisory Committee of the Department of Energy, and other advisory or stakeholder groups, as necessary, to maintain an accurate and up-to-date knowledge of the standing of civil nuclear exports from the United States, including with respect to meeting the targets established as part of the 10-year civil nuclear trade strategy described in paragraph (5)(A).\n**(5) Strategy**\n**(A) In general**\nNot later than 1 year after the date of enactment of this Act, the working group shall establish a 10-year civil nuclear trade strategy, including biennial targets for the export of civil nuclear technologies, including light water and non-light water reactors and associated equipment and technologies, civil nuclear materials, and nuclear fuel that align with meeting international energy demand while seeking to avoid or reduce emissions.\n**(B) Collaboration required**\nIn establishing the strategy under subparagraph (A), the working group shall collaborate with\u2014\n**(i)**\nany Federal agency that the President determines to be appropriate; and\n**(ii)**\nrepresentatives of private industry.\n#### 4. Engagement with ally or partner nations\n##### (a) In general\nThe President shall launch, in accordance with applicable nuclear technology export laws (including regulations), an international initiative to modernize the civil nuclear outreach to embarking civil nuclear nations.\n##### (b) Financing\nIn carrying out the initiative described in subsection (a), the President, acting through an appropriate Federal official, who may be the Assistant (if appointed), if determined to be appropriate, and in coordination with the officials described in section 3(a)(2), may, if the President determines to be appropriate, seek to establish cooperative financing relationships for the export of civil nuclear technology, components, materials, and infrastructure to embarking civil nuclear nations.\n##### (c) Activities\nIn carrying out the initiative described in subsection (a), the President shall\u2014\n**(1)**\nassist nongovernmental organizations and appropriate offices, administrations, agencies, laboratories, and programs of the Department of Energy and other relevant Federal agencies and offices in providing education and training to foreign governments in nuclear safety, security, and safeguards\u2014\n**(A)**\nthrough engagement with the International Atomic Energy Agency; or\n**(B)**\nindependently, if the applicable entity determines that it would be more advantageous under the circumstances to provide the applicable education and training independently;\n**(2)**\nassist the efforts of the International Atomic Energy Agency to expand the support provided by the International Atomic Energy Agency to embarking civil nuclear nations for nuclear safety, security, and safeguards;\n**(3)**\ncoordinate with appropriate Federal departments and agencies on efforts to expand outreach to the private investment community and establish public-private financing relationships that enable the adoption of civil nuclear technologies by embarking civil nuclear nations, including through exports from the United States;\n**(4)**\nseek to better coordinate, to the maximum extent practicable, the work carried out by any Federal agency that the President determines to be appropriate; and\n**(5)**\ncoordinate with the Export-Import Bank of the United States to improve the efficient and effective exporting and importing of civil nuclear technologies and materials.\n#### 5. Cooperative financing relationships with ally or partner nations and embarking civil nuclear nations\n##### (a) In general\nThe President shall designate an appropriate White House official, who may be the Assistant (if appointed), to coordinate with the officials described in section 3(a)(2) to develop, as the President determines to be appropriate, financing relationships with ally or partner nations to assist in the adoption of civil nuclear technologies exported from the United States or ally or partner nations to embarking civil nuclear nations.\n##### (b) United States competitiveness clauses\n**(1) Definition of United States competitiveness clause**\nIn this subsection, the term United States competitiveness clause means any United States competitiveness provision in any agreement entered into by the Department of Energy, including\u2014\n**(A)**\na cooperative agreement;\n**(B)**\na cooperative research and development agreement; and\n**(C)**\na patent waiver.\n**(2) Consideration**\nIn carrying out subsection (a), the relevant officials described in that subsection shall consider the impact of United States competitiveness clauses on any financing relationships entered into or proposed to be entered into under that subsection.\n**(3) Waiver**\nThe Secretary shall facilitate waivers of United States competitiveness clauses as necessary to facilitate financing relationships with ally or partner nations under subsection (a).\n#### 6. Cooperation with ally or partner nations on advanced nuclear reactor demonstration and cooperative research facilities for civil nuclear energy\n##### (a) In general\nNot later than 2 years after the date of enactment of this Act, the Secretary of State, in coordination with the Secretary and the Secretary of Commerce, shall conduct bilateral and multilateral meetings with not fewer than 5 ally or partner nations, with the aim of enhancing nuclear energy cooperation among those ally or partner nations and the United States, for the purpose of developing collaborative relationships with respect to research, development, licensing, and deployment of advanced nuclear reactor technologies for civil nuclear energy.\n##### (b) Requirement\nThe meetings described in subsection (a) shall include\u2014\n**(1)**\na focus on cooperation to demonstrate and deploy advanced nuclear reactors, with an emphasis on U.S. nuclear energy companies, during the 10-year period beginning on the date of enactment of this Act to provide options for addressing energy security and climate change; and\n**(2)**\na focus on developing a memorandum of understanding or any other appropriate agreement between the United States and ally or partner nations with respect to\u2014\n**(A)**\nthe demonstration and deployment of advanced nuclear reactors; and\n**(B)**\nthe development of cooperative research facilities.\n##### (c) Financing arrangements\nIn conducting the meetings described in subsection (a), the Secretary of State, in coordination with the Secretary, the Secretary of Commerce, and the heads of other relevant Federal agencies and only after initial consultation with the appropriate committees of Congress, shall seek to develop financing arrangements to share the costs of the demonstration and deployment of advanced nuclear reactors and the development of cooperative research facilities with the ally or partner nations participating in those meetings.\n##### (d) Report\nNot later than 1 year after the date of enactment of this Act, the Secretary, the Secretary of State, and the Secretary of Commerce shall jointly submit to the appropriate committees of Congress a report highlighting potential partners\u2014\n**(1)**\nfor the establishment of cost-share arrangements described in subsection (c) and the details of those arrangements; or\n**(2)**\nwith which the United States may enter into agreements with respect to\u2014\n**(A)**\nthe demonstration of advanced nuclear reactors; or\n**(B)**\ncooperative research facilities.\n#### 7. International civil nuclear energy cooperation\nSection 959B of the Energy Policy Act of 2005 ( 42 U.S.C. 16279b ) is amended\u2014\n**(1)**\nin the matter preceding paragraph (1), by striking The Secretary and inserting the following:\n(a) In general The Secretary ;\n**(2)**\nin subsection (a) (as so designated)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking financing, ; and\n**(ii)**\nby striking and after the semicolon at the end;\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nin subparagraph (A), by striking preparations for ; and\n**(ii)**\nin subparagraph (C)(v), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following:\n(3) to support, with the concurrence of the Secretary of State, the safe, secure, and peaceful use of civil nuclear technology in countries developing nuclear energy programs, with a focus on countries that have increased civil nuclear cooperation with the Russian Federation or the People\u2019s Republic of China; and (4) to promote the fullest utilization of the reactors, fuel, equipment, services, and technology of U.S. nuclear energy companies (as defined in section 2 of the International Nuclear Energy Act of 2025 ) in civil nuclear energy programs outside the United States through\u2014 (A) bilateral and multilateral arrangements developed and executed with the concurrence of the Secretary of State that contain commitments for the utilization of the reactors, fuel, equipment, services, and technology of U.S. nuclear energy companies (as defined in that section); (B) the designation of 1 or more U.S. nuclear energy companies (as defined in that section) to implement an arrangement under subparagraph (A) if the Secretary determines that the designation is necessary and appropriate to achieve the objectives of this section; and (C) the waiver of any provision of law relating to competition with respect to any activity related to an arrangement under subparagraph (A) if the Secretary, in consultation with the Attorney General and the Secretary of Commerce, determines that a waiver is necessary and appropriate to achieve the objectives of this section. ; and\n**(3)**\nby adding at the end the following:\n(b) Requirements The program under subsection (a) shall be supported in consultation with the Secretary of State and implemented by the Secretary\u2014 (1) to facilitate, to the maximum extent practicable, workshops and expert-based exchanges to engage industry, stakeholders, and foreign governments with respect to international civil nuclear issues, such as\u2014 (A) training; (B) financing; (C) safety; (D) security; (E) safeguards; (F) liability; (G) advanced fuels; (H) operations; and (I) options for multinational cooperation with respect to the disposal of spent nuclear fuel (as defined in section 2 of the Nuclear Waste Policy Act of 1982 ( 42 U.S.C. 10101 )); and (2) in coordination with any Federal agency that the President determines to be appropriate. (c) Authorization of appropriations Of funds appropriated or otherwise made available to the Secretary to carry out the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) in fiscal years 2026 through 2030, the Secretary may use $15,500,000 to carry out this section. .\n#### 8. International civil nuclear program support\n##### (a) In general\nNot later than 120 days after the date of enactment of this Act, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), shall launch an international initiative (referred to in this section as the initiative ) to provide financial assistance to, and facilitate the building of technical capacities by, in accordance with this section, embarking civil nuclear nations for activities relating to the development of civil nuclear energy programs.\n##### (b) Financial assistance\n**(1) In general**\nIn carrying out the initiative, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), is authorized to award grants of financial assistance in amounts not greater than $5,500,000 to embarking civil nuclear nations in accordance with this subsection\u2014\n**(A)**\nfor activities relating to the development of civil nuclear energy programs; and\n**(B)**\nto facilitate the building of technical capacities for those activities.\n**(2) Limitations**\nThe Secretary of State, in coordination with the Secretary and the Assistant (if appointed), may award\u2014\n**(A)**\nnot more than 1 grant of financial assistance under paragraph (1) to any 1 embarking civil nuclear nation each fiscal year; and\n**(B)**\nnot more than a total of 5 grants of financial assistance under paragraph (1) to any 1 embarking civil nuclear nation.\n##### (c) Senior advisors\n**(1) In general**\nIn carrying out the initiative, the Secretary of State, in coordination with the Secretary and the Assistant (if appointed), is authorized to provide financial assistance to an embarking civil nuclear nation for the purpose of contracting with a U.S. nuclear energy company to hire 1 or more senior advisors to assist the embarking civil nuclear nation in establishing a civil nuclear program.\n**(2) Requirement**\nA senior advisor described in paragraph (1) shall have relevant experience and qualifications to advise the embarking civil nuclear nation on, and facilitate on behalf of the embarking civil nuclear nation, 1 or more of the following activities:\n**(A)**\nThe development of financing relationships.\n**(B)**\nThe development of a standardized financing and project management framework for the construction of nuclear power plants.\n**(C)**\nThe development of a standardized licensing framework for\u2014\n**(i)**\nlight water civil nuclear technologies; and\n**(ii)**\nnon-light water civil nuclear technologies and advanced nuclear reactors.\n**(D)**\nThe identification of qualified organizations and service providers.\n**(E)**\nThe identification of funds to support payment for services required to develop a civil nuclear program.\n**(F)**\nMarket analysis.\n**(G)**\nThe identification of the safety, security, safeguards, and nuclear governance required for a civil nuclear program.\n**(H)**\nRisk allocation, risk management, and nuclear liability.\n**(I)**\nTechnical assessments of nuclear reactors and technologies.\n**(J)**\nThe identification of actions necessary to participate in a global nuclear liability regime based on the Convention on Supplementary Compensation for Nuclear Damage, with Annex, done at Vienna September 12, 1997 (TIAS 15\u2013415).\n**(K)**\nStakeholder engagement.\n**(L)**\nManagement of spent nuclear fuel and nuclear waste.\n**(M)**\nAny other major activities to support the establishment of a civil nuclear program, such as the establishment of export, financing, construction, training, operations, and education requirements.\n**(3) Clarification**\nFinancial assistance under this subsection is authorized to be provided to an embarking civil nuclear nation in addition to any financial assistance provided to that embarking civil nuclear nation under subsection (b).\n##### (d) Limitation on assistance to embarking civil nuclear nations\nNot later than 1 year after the date of enactment of this Act, the Offices of the Inspectors General for the Department of State and the Department of Energy shall coordinate\u2014\n**(1)**\nto establish and submit to the appropriate committees of Congress a joint strategic plan to conduct comprehensive oversight of activities authorized under this section to prevent fraud, waste, and abuse; and\n**(2)**\nto engage in independent and effective oversight of activities authorized under this section through joint or individual audits, inspections, investigations, or evaluations.\n##### (e) Authorization of appropriations\nOf funds appropriated or otherwise made available to the Secretary of State to carry out the Foreign Assistance Act of 1961 ( 22 U.S.C. 2151 et seq. ) in fiscal years 2026 through 2030, the Secretary of State may use $50,000,000 to carry out this section.\n#### 9. Biennial cabinet-level international conference on nuclear safety, security, safeguards, and sustainability\n##### (a) In general\nThe President, in coordination with international partners, as determined by the President, and industry, shall hold a biennial conference on civil nuclear safety, security, safeguards, and sustainability (referred to in this section as a conference ).\n##### (b) Conference functions\nIt is the sense of Congress that each conference should\u2014\n**(1)**\nbe a forum in which ally or partner nations may engage with each other for the purpose of reinforcing the commitment to\u2014\n**(A)**\nnuclear safety, security, safeguards, and sustainability;\n**(B)**\nenvironmental safeguards; and\n**(C)**\nlocal community engagement in areas in reasonable proximity to nuclear sites; and\n**(2)**\nfacilitate\u2014\n**(A)**\nthe development of\u2014\n**(i)**\njoint commitments and goals to improve\u2014\n**(I)**\nnuclear safety, security, safeguards, and sustainability;\n**(II)**\nenvironmental safeguards; and\n**(III)**\nlocal community engagement in areas in reasonable proximity to nuclear sites;\n**(ii)**\nstronger international institutions that support nuclear safety, security, safeguards, and sustainability;\n**(iii)**\ncooperative financing relationships to promote competitive alternatives to Chinese and Russian financing;\n**(iv)**\na standardized financing and project management framework for the construction of civil nuclear power plants;\n**(v)**\na standardized licensing framework for civil nuclear technologies;\n**(vi)**\na strategy to change internal policies of multinational development banks, such as the World Bank, to support the financing of civil nuclear projects;\n**(vii)**\na document containing any lessons learned from countries that have partnered with the Russian Federation or the People\u2019s Republic of China with respect to civil nuclear power, including any detrimental outcomes resulting from that partnership; and\n**(viii)**\na global civil nuclear liability regime;\n**(B)**\ncooperation for enhancing the overall aspects of civil nuclear power, such as\u2014\n**(i)**\nnuclear safety, security, safeguards, and sustainability;\n**(ii)**\nnuclear laws (including regulations);\n**(iii)**\nwaste management;\n**(iv)**\nquality management systems;\n**(v)**\ntechnology transfer;\n**(vi)**\nhuman resources development;\n**(vii)**\nlocalization;\n**(viii)**\nreactor operations;\n**(ix)**\nnuclear liability; and\n**(x)**\ndecommissioning; and\n**(C)**\nthe development and determination of the mechanisms described in paragraphs (7) and (8) of section 10(a), if the President intends to establish an Advanced Reactor Coordination and Resource Center as described in that section.\n##### (c) Input from industry and government\nIt is the sense of Congress that each conference should include a meeting that convenes nuclear industry leaders and leaders of government agencies with expertise relating to nuclear safety, security, safeguards, or sustainability to discuss best practices relating to\u2014\n**(1)**\nthe safe and secure use, storage, and transport of nuclear and radiological materials;\n**(2)**\nmanaging the evolving cyber threat to nuclear and radiological security; and\n**(3)**\nthe role that the nuclear industry should play in nuclear and radiological safety, security, and safeguards, including with respect to the safe and secure use, storage, and transport of nuclear and radiological materials, including spent nuclear fuel and nuclear waste.\n#### 10. Advanced reactor coordination and resource center\n##### (a) In general\nThe President shall consider the feasibility of leveraging existing activities or frameworks or, as necessary, establishing a center, to be known as the Advanced Reactor Coordination and Resource Center (referred to in this section as the Center ), for the purposes of\u2014\n**(1)**\nidentifying qualified organizations and service providers\u2014\n**(A)**\nfor embarking civil nuclear nations;\n**(B)**\nto develop and assemble documents, contracts, and related items required to establish a civil nuclear program; and\n**(C)**\nto develop a standardized model for the establishment of a civil nuclear program that can be used by the International Atomic Energy Agency;\n**(2)**\ncoordinating with countries participating in the Center and with the Nuclear Exports Working Group established under section 3(b)\u2014\n**(A)**\nto identify funds to support payment for services required to develop a civil nuclear program;\n**(B)**\nto provide market analysis; and\n**(C)**\nto create\u2014\n**(i)**\nproject structure models;\n**(ii)**\nmodels for electricity market analysis;\n**(iii)**\nmodels for nonelectric applications market analysis; and\n**(iv)**\nfinancial models;\n**(3)**\nidentifying and developing the safety, security, safeguards, and nuclear governance required for a civil nuclear program;\n**(4)**\nsupporting multinational regulatory standards to be developed by countries with civil nuclear programs and experience;\n**(5)**\ndeveloping and strengthening communications, engagement, and consensus-building;\n**(6)**\ncarrying out any other major activities to support export, financing, education, construction, training, and education requirements relating to the establishment of a civil nuclear program;\n**(7)**\ndeveloping mechanisms for how to fund and staff the Center; and\n**(8)**\ndetermining mechanisms for the selection of the location or locations of the Center.\n##### (b) Objective\nThe President shall carry out subsection (a) with the objective of establishing the Center if the President determines that it is feasible to do so.\n#### 11. Strategic infrastructure fund working group\n##### (a) Establishment\nThere is established a working group, to be known as the Strategic Infrastructure Fund Working Group (referred to in this section as the working group ) to provide input on the feasibility of establishing a program to support strategically important capital-intensive infrastructure projects.\n##### (b) Composition\nThe working group shall be\u2014\n**(1)**\nled by a White House official, who may be the Assistant (if appointed), who shall serve as the White House focal point with respect to matters relating to the working group; and\n**(2)**\ncomposed of\u2014\n**(A)**\nsenior-level Federal officials, selected by the head of the applicable Federal agency or organization, from any Federal agency or organization that the President determines to be appropriate;\n**(B)**\nother senior-level Federal officials, selected by the head of the applicable Federal agency or organization, from any other Federal agency or organization that the Secretary determines to be appropriate; and\n**(C)**\nany senior-level Federal official selected by the White House official described in paragraph (1) from any Federal agency or organization.\n##### (c) Reporting\nThe working group shall report to the National Security Council.\n##### (d) Duties\nThe working group shall\u2014\n**(1)**\nprovide direction and advice to the officials described in section 3(a)(2)(A) and appropriate Federal agencies, as determined by the working group, with respect to the establishment of a Strategic Infrastructure Fund (referred to in this subsection as the Fund ) to be used\u2014\n**(A)**\nto support those aspects of projects relating to\u2014\n**(i)**\ncivil nuclear technologies; and\n**(ii)**\nmicroprocessors; and\n**(B)**\nfor strategic investments identified by the working group; and\n**(2)**\naddress critical areas in determining the appropriate design for the Fund, including\u2014\n**(A)**\ntransfer of assets to the Fund;\n**(B)**\ntransfer of assets from the Fund;\n**(C)**\nhow assets in the Fund should be invested; and\n**(D)**\ngovernance and implementation of the Fund.\n##### (e) Briefing and report required\n**(1) Briefing**\nNot later than 180 days after the date of enactment of this Act, the working group shall brief the committees described in paragraph (3) on the status of the development of the processes necessary to implement this section.\n**(2) Report**\nNot later than 1 year after the date of the enactment of this Act, the working group shall submit to the committees described in paragraph (3) a report on the findings of the working group that includes suggested legislative text for how to establish and structure a Strategic Infrastructure Fund.\n**(3) Committees described**\nThe committees referred to in paragraphs (1) and (2) are\u2014\n**(A)**\nthe Committee on Foreign Relations, the Committee on Commerce, Science, and Transportation, the Committee on Armed Services, the Committee on Energy and Natural Resources, the Committee on Environment and Public Works, the Committee on Finance, and the Committee on Appropriations of the Senate; and\n**(B)**\nthe Committee on Foreign Affairs, the Committee on Energy and Commerce, the Committee on Armed Services, the Committee on Science, Space, and Technology, the Committee on Ways and Means, and the Committee on Appropriations of the House of Representatives.\n**(4) Administration of the fund**\nThe report submitted under paragraph (2) shall include suggested legislative language requiring all expenditures from a Strategic Infrastructure Fund established in accordance with this section to be administered by the Secretary of State (or a designee of the Secretary of State).\n#### 12. Joint assessment between the United States and india on nuclear liability rules\n##### (a) In general\nThe Secretary of State, in consultation with the heads of other relevant Federal departments and agencies, shall establish and maintain within the U.S.-India Strategic Security Dialogue a joint consultative mechanism with the Government of the Republic of India that convenes on a recurring basis\u2014\n**(1)**\nto assess the implementation of the Agreement for Cooperation between the Government of the United States of America and the Government of India Concerning Peaceful Uses of Nuclear Energy, signed at Washington October 10, 2008 (TIAS 08\u20131206);\n**(2)**\nto discuss opportunities for the Republic of India to align domestic nuclear liability rules with international norms; and\n**(3)**\nto develop a strategy for the United States and the Republic of India to pursue bilateral and multilateral diplomatic engagements related to analyzing and implementing those opportunities.\n##### (b) Report\nNot later than 180 days after the date of the enactment of this Act, and annually thereafter for 5 years, the Secretary of State, in consultation with the heads of other relevant Federal departments and agencies, shall submit to the appropriate committees of Congress a report that describes the joint assessment developed pursuant to subsection (a)(1).\n#### 13. Rule of construction\nExcept as expressly stated in this Act, nothing in this Act may be construed to alter or otherwise affect the interpretation or implementation of section 123 of the Atomic Energy Act of 1954 ( 42 U.S.C. 2153 ) or any other provision of law, including the requirement that agreements pursuant to that section be submitted to Congress for consideration.",
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
        "actionDate": "2025-05-29",
        "text": "Referred to the Committee on Foreign Affairs, and in addition to the Committees on Energy and Commerce, Science, Space, and Technology, and Ways and Means, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "3626",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "International Nuclear Energy Act of 2025",
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
            "updateDate": "2025-06-24T17:45:26Z"
          },
          {
            "name": "Advanced technology and technological innovations",
            "updateDate": "2025-06-24T17:45:34Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2025-06-24T17:45:43Z"
          },
          {
            "name": "Alliances",
            "updateDate": "2025-06-24T17:45:50Z"
          },
          {
            "name": "Arms control and nonproliferation",
            "updateDate": "2025-06-24T17:46:15Z"
          },
          {
            "name": "Asia",
            "updateDate": "2025-06-24T17:46:06Z"
          },
          {
            "name": "China",
            "updateDate": "2025-06-24T17:46:20Z"
          },
          {
            "name": "Civil actions and liability",
            "updateDate": "2025-06-24T17:46:27Z"
          },
          {
            "name": "Competitiveness, trade promotion, trade deficits",
            "updateDate": "2025-06-24T17:46:35Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-24T17:46:50Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-24T17:47:00Z"
          },
          {
            "name": "Department of Energy",
            "updateDate": "2025-06-24T17:47:09Z"
          },
          {
            "name": "Diplomacy, foreign officials, Americans abroad",
            "updateDate": "2025-06-24T17:47:16Z"
          },
          {
            "name": "Emergency planning and evacuation",
            "updateDate": "2025-06-24T17:47:24Z"
          },
          {
            "name": "Energy research",
            "updateDate": "2025-06-24T17:47:32Z"
          },
          {
            "name": "Europe",
            "updateDate": "2025-06-24T17:47:39Z"
          },
          {
            "name": "Executive agency funding and structure",
            "updateDate": "2025-06-24T17:47:50Z"
          },
          {
            "name": "Export-Import Bank of the United States",
            "updateDate": "2025-06-24T17:47:57Z"
          },
          {
            "name": "Foreign aid and international relief",
            "updateDate": "2025-06-24T17:48:06Z"
          },
          {
            "name": "Foreign and international banking",
            "updateDate": "2025-06-24T17:48:17Z"
          },
          {
            "name": "Foreign and international corporations",
            "updateDate": "2025-06-24T17:48:29Z"
          },
          {
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-06-24T17:48:38Z"
          },
          {
            "name": "India",
            "updateDate": "2025-06-24T17:48:45Z"
          },
          {
            "name": "International organizations and cooperation",
            "updateDate": "2025-06-24T17:48:54Z"
          },
          {
            "name": "International scientific cooperation",
            "updateDate": "2025-06-24T17:49:07Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-06-24T17:49:19Z"
          },
          {
            "name": "Life, casualty, property insurance",
            "updateDate": "2025-06-24T17:49:30Z"
          },
          {
            "name": "South Asia",
            "updateDate": "2025-06-24T17:45:59Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-06-20T18:18:56Z"
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
      "date": "2025-05-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1801is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2025-06-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1801rs.xml"
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
      "title": "International Nuclear Energy Act of 2025",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2025-06-21T02:53:17Z"
    },
    {
      "title": "International Nuclear Energy Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-19T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "International Nuclear Energy Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-30T02:08:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to facilitate the development of a whole-of-government strategy for nuclear cooperation and nuclear exports, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-30T02:03:28Z"
    }
  ]
}
```
