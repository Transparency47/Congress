# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1904?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1904
- Title: Improving Coordination of Agriculture Research and Data Act
- Congress: 119
- Bill type: HR
- Bill number: 1904
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-04-01T17:38:44Z
- Update date including text: 2025-04-01T17:38:44Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Conservation, Research, and Biotechnology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1904",
    "number": "1904",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001285",
        "district": "26",
        "firstName": "Julia",
        "fullName": "Rep. Brownley, Julia [D-CA-26]",
        "lastName": "Brownley",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Improving Coordination of Agriculture Research and Data Act",
    "type": "HR",
    "updateDate": "2025-04-01T17:38:44Z",
    "updateDateIncludingText": "2025-04-01T17:38:44Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Conservation, Research, and Biotechnology.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:50:18Z",
              "name": "Referred to"
            }
          },
          "name": "Conservation, Research, and Biotechnology Subcommittee",
          "systemCode": "hsag14"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1904ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1904\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Ms. Brownley (for herself and Ms. Stansbury ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to establish the Climate Scientific Research Advisory Committee and the Rural Climate Alliance Network, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Coordination of Agriculture Research and Data Act .\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto strategically align agriculture climate research and data systems;\n**(2)**\nto strengthen technical assistance and technology transfer; and\n**(3)**\nto establish a national agriculture climate research agenda to mitigate and adapt to climate change.\n#### 3. Agriculture climate research coordination and data\n##### (a) Agriculture Climate Scientific Research Advisory Committee\nSubtitle B of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 ( 7 U.S.C. 3121 et seq. ) is amended by adding at the end the following:\n1413C. Agriculture Climate Scientific Research Advisory Committee (a) Establishment The Secretary shall establish within the Office of the Chief Scientist an advisory committee, to be known as the Agriculture Climate Scientific Research Advisory Committee (referred to in this section as the Committee ). (b) Duties The Committee shall\u2014 (1) review, and make recommendations and provide consultation to the Secretary regarding, the long-term and short-term national policies and priorities of the Department of Agriculture for\u2014 (A) data collection for climate-specific agricultural research, extension, education, and economics; and (B) agricultural climate research priority areas and scientific agendas for measuring, monitoring, reporting, and verification of climate and environmental outcomes that include\u2014 (i) carbon removal, carbon sequestration, and greenhouse gas emission related to agriculture; (ii) soil health; (iii) livestock methane production; (iv) wetland management; and (v) climate smart agriculture practices; (2) identify gaps in current agriculture climate research and develop a biennial national research agenda and annual scientific recommendations to address areas of critical need for publicly funded agriculture climate research; (3) (A) every 5 years, evaluate the results and effectiveness of climate-specific agricultural research, extension, education, and economics with respect to the policies and priorities described in paragraph (1); and (B) make recommendations to the Secretary based on such evaluation; (4) review and make programmatic and priority research recommendations to the Under Secretary for Research, Education, and Economics on the climate-specific agricultural research, extension, education, and economics described in paragraph (3)(A); (5) review and make recommendations on the mechanisms of the Department of Agriculture for technology assessment, which shall be conducted by qualified professionals, for the purposes of\u2014 (A) performance measurement and evaluation of the implementation by the Secretary of the strategic plan of the Department of Agriculture required under section 306 of title 5, United States Code; (B) implementation of climate-specific national research policies and priorities that are consistent with the purposes described in section 1402; and (C) the development of mechanisms for the assessment of emerging public and private climate-specific agricultural research and technology transfer initiatives; (6) every 5 years, establish and update standardized data collection, management, and dissemination protocols for\u2014 (A) agriculture climate research programs of the Department of Agriculture; and (B) initiatives of the Rural Climate Alliance Network established under section 1419(c); (7) (A) consult with industry groups, producer networks, advocacy organizations, scientific societies, and higher education associations on climate-specific agricultural research, extension, education, and economics; and (B) make recommendations to the Secretary based on such consultation; (8) consult with, and receive communications from, other Federal departments and agencies on climate plans and priorities relating to agriculture and forestry for the purpose of advising the Secretary of opportunities for collaboration, coordination, and avoiding duplication; (9) (A) review climate research technology transfer and new scientific practices for climate mitigation and adaptation; and (B) make recommendations to the Rural Climate Alliance Network established under section 1419(c) based on such review; and (10) review and suggest annual budget recommendations to support a climate research agenda for the Secretary to propose in each annual budget of the Department of Agriculture. (c) Membership (1) Number and appointment (A) In general The Committee shall be composed of 18 members as follows: (i) The Secretary. (ii) The Chief Scientist. (iii) The Director of the Global Climate Change Program established under section 2402 of the Food, Agriculture, Conservation, and Trade Act of 1990 ( 7 U.S.C. 6701 ). (iv) The Under Secretary for Natural Resources and Environment. (v) The Under Secretary for Farm Production and Conservation. (vi) The Under Secretary for Marketing and Regulatory Programs. (vii) The Executive Director of the Foundation for Food and Agriculture Research. (viii) The Administrator of the Agricultural Research Service. (ix) The Director of the National Institute of Food and Agriculture. (x) The Administrator of the Economic Research Service. (xi) The Administrator of the National Agricultural Statistics Service. (xii) The Director of the Office of Energy and Environmental Policy. (xiii) The Deputy Chief for Research and Development of the Forest Service. (xiv) 1 member of the National Academy of Sciences, to be appointed by the Secretary. (xv) 4 members to be appointed by the Secretary from nominations submitted by the nominating entities described in subparagraph (B). (B) Nominating entities described The nominating entities described in this subparagraph are organizations, associations, societies, cooperative extensions, State agricultural experiment stations, technical assistance provider organizations, councils, federations, producer groups, agriculture manufacturing entities, restaurants, the food service industry, the agriculture technology industry, environmental organizations, forestry organizations, nonprofit organizations, and companies or other entities as determined appropriate by the Secretary. (2) Terms (A) In general Except as provided in subparagraph (B), members of the Committee appointed under clause (xiv) or (xv) of paragraph (1)(A) shall be appointed for a term of not more than 6 years. (B) Terms of initial appointees The initial members of the Committee appointed under clause (xiv) or (xv) of paragraph (1)(A) shall be appointed for the following terms: (i) 2 shall be appointed for a term of 2 years, which may be extended by the Secretary for an additional 6 years. (ii) 2 shall be appointed for a term of 4 years, which may be extended by the Secretary for an additional 6 years. (iii) 1 shall be appointed for a term of 6 years. (C) Limitation Except as provided in subparagraph (B), members of the Committee appointed under clause (xiv) or (xv) of paragraph (1)(A) may not serve consecutive terms on the Committee. (D) Vacancies Any vacancy on the Committee\u2014 (i) shall not affect the duties of the Committee under this section; and (ii) shall be filled in the same manner as the original appointment. (3) Chairperson, vice chairperson, and executive subcommittee (A) Election At the first meeting of the Committee each calendar year, the Committee shall elect from among the members of the Committee\u2014 (i) a chairperson; (ii) a vice chairperson; and (iii) 7 members to serve on the executive subcommittee established under subparagraph (B). (B) Executive subcommittee The Committee shall establish an executive subcommittee charged with the responsibility of working with the Secretary and officers and employees of the Department of Agriculture to summarize and disseminate the recommendations of the Committee. (d) Consultation and recommendations (1) Duties of Committee In fulfilling the duties of the Committee under this section, the Committee shall consult with appropriate agencies of the Department of Agriculture. (2) Duties of Secretary After receiving recommendations from the Committee pursuant to any provision in this section, the Secretary shall provide a written response to the Committee regarding the manner and extent to which the Secretary will implement such recommendations. (e) Compensation and personnel (1) Appointment of executive director and staff To assist the Committee in the performance of the duties of the Committee, the Secretary may appoint, without regard to the civil service laws, and after consultation with the chairperson of the Committee\u2014 (A) a full-time executive director, who shall\u2014 (i) perform such duties as the chairperson of the Committee may direct; and (ii) receive compensation at a rate not to exceed the rate payable for GS\u201315 of the General Schedule established by section 5332 of title 5, United States Code; and (B) a professional staff of not more than 3 full-time employees qualified in climate-specific agricultural research, extension, education, and economics, of which 1 shall serve as the executive secretary of the Committee. (2) Additional assistance and personnel The Secretary shall detail, on a reimbursable basis, personnel of the Department of Agriculture to the Committee as necessary to assist the Commission in carrying out its duties under this section. (3) Compensation of members (A) In general Except as provided in subparagraph (B), members of the Committee shall serve without pay for each day during which such members are engaged in the actual performance of duties vested in the Committee. (B) Prohibition of compensation of Federal employees Members of the Committee who are full-time officers or employees of the United States may not receive additional pay, allowances, or benefits by reason of their service on the Committee. (C) Travel expenses A member of the Committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from the home or regular place of business of the member in the performance of services for the Committee. (f) Federal Advisory Committee Act charter The Committee shall be deemed to have filed a charter for the purpose of section 1008(c) of title 5, United States Code (commonly known as the Federal Advisory Committee Act ). (g) Termination Section 1013(a)(2) of title 5, United States Code, (relating to the termination of advisory committees) shall not apply to the Committee. (h) Committee expenses not counted toward general limitations The expenses of the Committee shall not be counted toward any general limitation on the expenses of advisory committees, panels, commissions, and task forces of the Department of Agriculture contained in any Act making appropriations for the Department of Agriculture, whether enacted before, on, or after the date of enactment of this section, unless the appropriation Act specifically refers to this subsection and specifically includes the Committee within the general limitation. .\n##### (b) Rural climate alliance network\nSubtitle C of title XIV of the National Agricultural Research, Extension, and Teaching Policy Act of 1977 is amended by inserting after section 1418 ( 7 U.S.C. 3153 ) the following:\n1419. Rural Climate Alliance Network (a) Definition of agricultural producer In this section, the term agricultural producer means an individual who is engaged in farming, ranching, forestry, aquaculture, or another occupation relating to agriculture. (b) Purposes The purposes of this section are\u2014 (1) to provide science-based climate adaptation and mitigation assistance and training programs to rural communities and agricultural producers; (2) to coordinate the transfer of new technology and research relating to climate change that will impact behavioral and management changes to agricultural systems, including to\u2014 (A) individuals who work in the field of climate science, including agricultural producers; and (B) individuals, organizations, and other entities with an established history of working with agricultural producers; (3) to improve agriculture research collaboration, data collection, and partnerships and the sharing of information about new scientific advancements in climate research, as well as inform future research efforts; and (4) to facilitate the exchange of regional agriculture climate data and research through a network of partners. (c) Rural Climate Alliance Network (1) In general The Secretary shall establish and administer through the Climate Hubs a network, to be known as the Rural Climate Alliance Network (referred to in this subsection as the Network )\u2014 (A) that serves as a coordination hub for the provision of agriculture climate research, climate data, extension, and technical assistance for agricultural producers, the food and agricultural industry, nonprofit organizations relating to food and agriculture, and researchers relating to food and agriculture to address the effects of climate change; and (B) to improve\u2014 (i) responses to climate disasters through data collection and information sharing; (ii) communication of climate risks; (iii) accessible education and technical transfer of climate-related, regionally relevant agricultural data and research to agricultural producers in all regionally appropriate languages; (iv) tools and networks that deliver information to prevent damage from extreme weather events, pest and disease outbreaks, and other related climate change impacts; (v) communication between agricultural producers and the agricultural research community to ensure that agricultural research considers the perspectives of agricultural producers, such as changes in yield and fluctuating costs of inputs; (vi) coordination between other Federal agencies, as the Secretary determines appropriate; and (vii) coordination between entities in the private sector, such as participants in the agricultural and food supply chains that work with agricultural producers, relating to climate data, adaptation, mitigation, and response. (2) Composition The Network shall include\u2014 (A) entities, and employees of entities, that conduct research, exchange data, provide monitoring and verification services, or provide technical assistance relating to food and agriculture, including\u2014 (i) colleges and universities; (ii) State cooperative institutions; (iii) State extension services; (iv) State departments of agriculture; (v) State agricultural experiment stations; (vi) Indian Tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); (vii) qualified nonprofit organizations, as determined by the Secretary; (viii) qualified private businesses, as determined by the Secretary; (ix) agricultural producers, producer groups, or producer organizations, including agricultural trade associations and research and promotion boards (commonly known as checkoffs ); (x) agencies and offices within the Department of Agriculture; and (xi) any other technical assistance provider, research entity, or data analytics entity that the Secretary determines to be qualified to participate in the Network; (B) climate resilience-related research networks within the Department of Agriculture, including\u2014 (i) the Long-Term Agroecosystem Research Network; (ii) the Extension Disaster Education Network; (iii) the Eastern Forest Environmental Threat Assessment Center; (iv) the Western Wildland Environmental Threat Assessment Center; (v) the Sustainable Agriculture Research and Education program; (vi) the National Soil Dynamics Laboratory; (vii) the National Cooperative Soil Survey; (viii) the Economic Research Service; (ix) regional and rural development centers; and (x) other existing climate-related research networks within the Department of Agriculture that the Secretary determines to be appropriate to participate in the Network; and (C) other government-affiliated entities and climate resilience-related research networks outside of the Department of Agriculture, including\u2014 (i) the Foundation for Food and Agriculture Research; (ii) the U.S. Global Change Research Program; (iii) State and public weather station networks; (iv) the National Weather Service and other weather data systems within the National Oceanic and Atmospheric Administration; (v) the harvest program of the National Aeronautics and Space Administration; and (vi) other existing local, State, or Federal climate-related research networks, as determined by the Secretary. (d) Activities of the network (1) In general An individual or entity within the Network may\u2014 (A) through the means described in paragraph (2)\u2014 (i) initiate, expand, or sustain agricultural research programs that build capacity to mitigate, respond to, and recover from climate change disasters, including\u2014 (I) programs of the Agricultural Research Service; (II) the Agriculture and Food Research Initiative; (III) the Sustainable Agriculture Research and Education program; (IV) the Agriculture Advanced Research and Development Authority; and (V) programs of the Foundation for Food and Agriculture Research; (ii) inform and advise about agricultural climate variability, change, vulnerability, risk, adaptation, and mitigation; (iii) respond to climate impacts on ecosystems, economics, and diversity; (iv) collect and store agricultural climate data to share with other individuals and entities within the Network and Federal research partners; (v) assist agricultural producers in implementing new management approaches to adapt to, reduce the risk of, and provide societal solutions to mitigate climate change; (vi) transfer technology, research outcomes, and information; and (vii) improve climate change awareness, education, and planning assistance, as necessary; and (B) enter into cooperative agreements or contracts, on a multiyear basis, with community-based, direct-service organizations to initiate, expand, or sustain\u2014 (i) activities carried out under subparagraph (A) and paragraph (2); or (ii) programs described in subsection (b)(1). (2) Means described An eligible entity may carry out the activities described in paragraph (1)(A) through\u2014 (A) the development of phone technology, online applications, websites, handbooks, manuals, publications, warning systems, and other communication networks in all regionally appropriate languages; (B) training, including training programs and workshops, for disseminating information to\u2014 (i) crop insurance agents; (ii) loan and credit officers; (iii) agricultural suppliers; (iv) agricultural producers; (v) State cooperative agents; (vi) third-party providers (as defined in section 1242(a) of the Food Security Act of 1985 ( 16 U.S.C. 3842(a) )); (vii) Certified Crop Advisers and Certified Professional Soil Scientists certified by the American Society of Agronomy; (viii) Federal officers and employees, including officers and employees of the Natural Resources Conservation Service, the Farm Service Agency, the Agricultural Research Service, and the Forest Service; (ix) non-Federal technical assistance providers; (x) climate change experts who work with agricultural producers; and (xi) other individuals and entities that may\u2014 (I) assist agricultural producers who are vulnerable to climate impacts; or (II) provide societal solutions to mitigate the climate impacts of agriculture; (C) curriculum development for managing climate risks, mitigating climate change, and understanding climate risks and economic implications; and (D) such other means as the Secretary determines to be appropriate. (e) Report to Congress (1) In general Not later than 1 year after the date of enactment of the Improving Coordination of Agriculture Research and Data Act , the Secretary shall submit to Congress and any relevant Federal department or agency, and make publicly available, a report describing\u2014 (A) the current needs of climate mitigation and resilience research and data systems in the food and agriculture sector; (B) progress made toward developing and adopting climate solutions across the food and agriculture system; (C) technical assistance needs of rural communities and agricultural producers; (D) actions and recommendations of the Agriculture Climate Scientific Research Committee (established under section 1413C); and (E) recommended Federal budget activities and funding levels for research, data systems, and technical assistance priorities relating to climate mitigation. (2) Contents The report under paragraph (1) shall include\u2014 (A) an inventory and assessment of efforts to support the climate change adaptation, mitigation, risk management, and resilience tools for agricultural producers by\u2014 (i) the Federal Government; (ii) States and territories of the United States; (iii) Indian Tribes (as defined in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 )); (iv) units of local government; (v) communities comprising agricultural producers; (vi) qualified nonprofit organizations, as determined by the Secretary; (vii) agriculture and food businesses; (viii) State extension services; (ix) land-grant colleges and universities; and (x) other appropriate entities, as determined by the Secretary; (B) a baseline report on soil carbon sequestration on measurable soil carbon stocks and sequestration; (C) a description of the challenges faced by agricultural producers that may impact the climate change resilience of those agricultural producers; (D) a long-term strategy for responding to the challenges described under subparagraph (C) and recommendations based on best practices for further action to be carried out by appropriate Federal departments or agencies\u2014 (i) to improve the response by the Federal Government to those challenges; and (ii) to seek to improve climate change resilience among rural communities and agricultural producers; and (E) an evaluation of the impact that climate change challenges faced by rural communities, Indian Tribes, and agricultural producers have on\u2014 (i) the agricultural workforce; (ii) agricultural production; (iii) rural families and communities, including relating to food security; and (iv) succession planning. .",
      "versionDate": "2025-03-06",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Agriculture and Food",
        "updateDate": "2025-04-01T13:51:25Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr1904",
          "measure-number": "1904",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-04-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1904v00",
            "update-date": "2025-04-01"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Coordination of Agriculture Research and Data Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish an Agriculture Climate Scientific Research Advisory Committee and a Rural Climate Alliance Network.\u00a0</p><p>The advisory committee,\u00a0within USDA's Office of the Chief Scientist, must review and make recommendations on the agency's long-term and short-term national policies and priorities for (1) data collection for climate-specific agricultural research, extension, education, and economics; and (2) agricultural climate research.</p><p>The Rural Climate Alliance Network must coordinate the provision of agriculture climate research, climate data, extension, and technical assistance for agricultural producers, the food and agricultural industry, nonprofit organizations, and researchers. The bill defines an\u00a0<em>agricultural producer </em>as an individual who is engaged in farming, ranching, forestry, aquaculture, or another occupation relating to agriculture.</p><p>USDA must also submit a report to Congress that includes a long-term strategy for responding to the challenges faced by agricultural producers that may impact agricultural producers' climate change resilience. The report must also include recommendations for further action by federal departments and agencies that are based on best practices.</p>"
        },
        "title": "Improving Coordination of Agriculture Research and Data Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1904.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Coordination of Agriculture Research and Data Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish an Agriculture Climate Scientific Research Advisory Committee and a Rural Climate Alliance Network.\u00a0</p><p>The advisory committee,\u00a0within USDA's Office of the Chief Scientist, must review and make recommendations on the agency's long-term and short-term national policies and priorities for (1) data collection for climate-specific agricultural research, extension, education, and economics; and (2) agricultural climate research.</p><p>The Rural Climate Alliance Network must coordinate the provision of agriculture climate research, climate data, extension, and technical assistance for agricultural producers, the food and agricultural industry, nonprofit organizations, and researchers. The bill defines an\u00a0<em>agricultural producer </em>as an individual who is engaged in farming, ranching, forestry, aquaculture, or another occupation relating to agriculture.</p><p>USDA must also submit a report to Congress that includes a long-term strategy for responding to the challenges faced by agricultural producers that may impact agricultural producers' climate change resilience. The report must also include recommendations for further action by federal departments and agencies that are based on best practices.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119hr1904"
    },
    "title": "Improving Coordination of Agriculture Research and Data Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Coordination of Agriculture Research and Data Act</strong></p><p>This bill directs the Department of Agriculture (USDA) to establish an Agriculture Climate Scientific Research Advisory Committee and a Rural Climate Alliance Network.\u00a0</p><p>The advisory committee,\u00a0within USDA's Office of the Chief Scientist, must review and make recommendations on the agency's long-term and short-term national policies and priorities for (1) data collection for climate-specific agricultural research, extension, education, and economics; and (2) agricultural climate research.</p><p>The Rural Climate Alliance Network must coordinate the provision of agriculture climate research, climate data, extension, and technical assistance for agricultural producers, the food and agricultural industry, nonprofit organizations, and researchers. The bill defines an\u00a0<em>agricultural producer </em>as an individual who is engaged in farming, ranching, forestry, aquaculture, or another occupation relating to agriculture.</p><p>USDA must also submit a report to Congress that includes a long-term strategy for responding to the challenges faced by agricultural producers that may impact agricultural producers' climate change resilience. The report must also include recommendations for further action by federal departments and agencies that are based on best practices.</p>",
      "updateDate": "2025-04-01",
      "versionCode": "id119hr1904"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1904ih.xml"
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
      "title": "Improving Coordination of Agriculture Research and Data Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-25T05:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Coordination of Agriculture Research and Data Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-25T05:38:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Agricultural Research, Extension, and Teaching Policy Act of 1977 to establish the Climate Scientific Research Advisory Committee and the Rural Climate Alliance Network, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-25T05:33:20Z"
    }
  ]
}
```
