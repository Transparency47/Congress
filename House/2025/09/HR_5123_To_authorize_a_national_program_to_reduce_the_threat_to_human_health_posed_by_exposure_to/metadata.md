# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5123?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5123
- Title: Indoor Air Quality and Healthy Schools Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5123
- Origin chamber: House
- Introduced date: 2025-09-03
- Update date: 2026-05-20T08:08:23Z
- Update date including text: 2026-05-20T08:08:23Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-03: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-09-03: Introduced in House

## Actions

- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Introduced in House
- 2025-09-03 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-03",
    "latestAction": {
      "actionDate": "2025-09-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5123",
    "number": "5123",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "T000469",
        "district": "20",
        "firstName": "Paul",
        "fullName": "Rep. Tonko, Paul [D-NY-20]",
        "lastName": "Tonko",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Indoor Air Quality and Healthy Schools Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:23Z",
    "updateDateIncludingText": "2026-05-20T08:08:23Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-03",
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
          "date": "2025-09-03T14:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-09-03",
      "state": "PA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-09-11",
      "state": "IL"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-18",
      "state": "NJ"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2025-09-18",
      "state": "MN"
    },
    {
      "bioguideId": "H001090",
      "district": "9",
      "firstName": "Josh",
      "fullName": "Rep. Harder, Josh [D-CA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Harder",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "D000635",
      "district": "3",
      "firstName": "Maxine",
      "fullName": "Rep. Dexter, Maxine [D-OR-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Dexter",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "OR"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "False",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2026-02-09",
      "state": "DC"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-02-23",
      "state": "NY"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2026-03-30",
      "state": "CA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-02",
      "state": "NY"
    },
    {
      "bioguideId": "H001068",
      "district": "2",
      "firstName": "Jared",
      "fullName": "Rep. Huffman, Jared [D-CA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Huffman",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "CA"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "False",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "OR"
    },
    {
      "bioguideId": "L000593",
      "district": "49",
      "firstName": "Mike",
      "fullName": "Rep. Levin, Mike [D-CA-49]",
      "isOriginalCosponsor": "False",
      "lastName": "Levin",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "CO"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2026-05-04",
      "state": "CA"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2026-05-13",
      "state": "AZ"
    },
    {
      "bioguideId": "G000606",
      "district": "7",
      "firstName": "Adelita",
      "fullName": "Rep. Grijalva, Adelita S. [D-AZ-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Grijalva",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-05-14",
      "state": "AZ"
    },
    {
      "bioguideId": "S001225",
      "district": "17",
      "firstName": "Eric",
      "fullName": "Rep. Sorensen, Eric [D-IL-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Sorensen",
      "party": "D",
      "sponsorshipDate": "2026-05-19",
      "state": "IL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5123ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5123\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 3, 2025 Mr. Tonko (for himself and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo authorize a national program to reduce the threat to human health posed by exposure to indoor air contaminants, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Indoor Air Quality and Healthy Schools Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) Administrator**\nThe term Administrator means the Administrator of the Environmental Protection Agency.\n**(2) Covered childcare facility**\nThe term covered childcare facility means a facility used by an early childhood education program.\n**(3) Early childhood education program**\nThe term early childhood education program has the meaning given to that term in section 103 of the Higher Education Act of 1965 ( 20 U.S.C. 1003 ).\n**(4) Indoor**\nThe term indoor means the enclosed portions of buildings, including nonindustrial workplaces, public buildings, Federal buildings, schools, childcare facilities, commercial buildings, and residences.\n**(5) Indoor air contaminant**\nThe term indoor air contaminant means any solid, liquid, semisolid, dissolved solid, biogenic agent, aerosol, or gaseous material, including combinations or mixtures of substances, in indoor air which may reasonably be anticipated to have an adverse effect on human health.\n**(6) Indoor contaminant of concern**\nThe term indoor contaminant of concern means an indoor air contaminant that\u2014\n**(A)**\nis among the most commonly occurring and poses a risk to human health; or\n**(B)**\nis less commonly occurring and poses a significant risk to human health.\n**(7) Local educational agency**\nThe term local educational agency means\u2014\n**(A)**\na local educational agency (as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )); or\n**(B)**\na Tribal education agency (as the term tribal education agency is defined in section 3 of the National Environmental Education Act ( 20 U.S.C. 5502 )).\n**(8) State**\nThe term State includes each of the several States, the District of Columbia, Puerto Rico, the Virgin Islands, Guam, American Samoa, and the Commonwealth of the Northern Mariana Islands.\n#### 3. Indoor Air Quality Program\n##### (a) In general\nThe Administrator shall carry out a program to support the assessment, reduction, and avoidance of exposure to indoor air contaminants to reduce risks to human health.\n##### (b) Responsibilities\nIn carrying out the program under subsection (a), the Administrator shall support the assessment, reduction, and avoidance of exposure to indoor air contaminants to reduce risks to human health, including by\u2014\n**(1)**\ncarrying out research, development, and demonstration activities pursuant to the Radon Gas and Indoor Air Quality Research Act of 1986 ( 42 U.S.C. 7401 note);\n**(2)**\nlisting indoor contaminants of concern, and publishing guidelines for such indoor contaminants of concern, under section 4;\n**(3)**\nproviding training, education, outreach, and technical assistance to identify, eliminate, or reduce indoor air contaminants, including by effective monitoring, source control, ventilation, and filtration practices;\n**(4)**\nproviding training, education, outreach, and technical assistance to support the monitoring of humidity levels and the inspection, testing, prevention, and remediation of mold;\n**(5)**\ncarrying out or recognizing voluntary certifications to identify and promote buildings that are most effective at preventing or minimizing risks to health from indoor air contaminants under section 7;\n**(6)**\nsupporting efforts to improve indoor air quality in buildings used by local educational agencies and covered childcare facilities under section 9;\n**(7)**\nensuring effective consultation and coordination among Federal agencies in carrying out programs related to indoor air quality, including the Department of Labor, the Department of Energy, the Centers for Disease Control and Prevention, the Occupational Safety and Health Administration, the National Institute for Occupational Safety and Health, the Department of Housing and Urban Development, the Department of Health and Human Services, the Department of Education, the Department of Defense, the Federal Emergency Management Agency, the Consumer Product Safety Commission, and other appropriate agencies carrying out programs related to indoor air quality;\n**(8)**\nsupporting State, local, and Tribal governments, local educational agencies, housing authorities, and other entities to develop and implement indoor air quality management strategies, educational campaigns, assessments, guidelines, standards, and response programs;\n**(9)**\nproviding information, guidance, and assistance to the public, including building owners and occupants, on\u2014\n**(A)**\nhealth-related risks of exposure to indoor air contaminants; and\n**(B)**\neffective measures and programs for reducing or avoiding exposure to indoor air contaminants;\n**(10)**\nsupporting development and adoption of standardized methods, techniques, minimum product requirements, and protocols for assessing, measuring, and sampling indoor air to determine the presence and concentrations of indoor air contaminants;\n**(11)**\nsupporting development and adoption of control technologies, building design criteria, and management practices to prevent the entrance of contaminants into buildings and to reduce or mitigate emissions from indoor sources;\n**(12)**\nassessing the effectiveness of methods, techniques, protocols, response plans, products, and technologies to reduce or avoid exposure to indoor air contaminants;\n**(13)**\nsupporting the development and adoption of model provisions, to be incorporated into building codes for various types of buildings, designed to improve indoor air quality while taking into account comfort, safety, and energy conservation goals;\n**(14)**\nsupporting development and adoption of control technologies, building design criteria, and management practices to improve indoor air quality and building resilience against the impacts of more frequent extreme weather events and other consequences of climate change; and\n**(15)**\nensuring consideration of disadvantaged communities and individuals in carrying out such program, including by providing access to financial assistance, technical assistance, and other offerings developed pursuant to this Act for all people regardless of income, race, color, gender, national origin, Tribal affiliation, or disability.\n#### 4. Guidelines for indoor contaminants of concern\n##### (a) List\n**(1) In general**\nThe Administrator shall establish and maintain a list of indoor contaminants of concern.\n**(2) Contents**\nThe list under paragraph (1) may\u2014\n**(A)**\ninclude combinations or mixtures of contaminants; and\n**(B)**\nrefer to such combinations or mixtures by a common name.\n**(3) Initial list**\nNot later than 5 years after the date of enactment of this Act, the Administrator shall establish the initial list under paragraph (1).\n##### (b) Minimum contaminants on initial list\nAt a minimum, the initial list established under subsection (a) shall include\u2014\n**(1)**\nparticulate matter;\n**(2)**\ncarbon monoxide;\n**(3)**\nnitrogen dioxide;\n**(4)**\nozone;\n**(5)**\nformaldehyde; and\n**(6)**\nradon.\n##### (c) Indoor air quality guidelines\n**(1) In general**\nThe Administrator shall publish science-based, voluntary guidelines for each indoor contaminant of concern listed under subsection (a).\n**(2) Guideline components**\nA guideline published under this subsection shall\u2014\n**(A)**\ninclude information and a range of recommendations for operation and maintenance of existing buildings, the design and construction of new buildings, building renovation, and such other activities as are necessary to identify, and reduce or prevent exposure to, the indoor contaminant of concern listed under subsection (a);\n**(B)**\nbe designed to achieve significant risk reduction;\n**(C)**\nbe technologically achievable and readily implementable;\n**(D)**\ntake into consideration safety, energy, and other relevant factors;\n**(E)**\ninclude an assessment of effectiveness and cost; and\n**(F)**\nbe based on available research and expertise.\n**(3) Concentration limits**\n**(A) In general**\nEach guideline published under this subsection shall, upon the Administrator making a determination that sufficient scientific evidence exists, include a recommended health-based limit on concentration levels of indoor contaminants of concern.\n**(B) Best available science; lowest level of exposure**\nA limit under subparagraph (A)\u2014\n**(i)**\nshall be based on the best available science; and\n**(ii)**\nmay include a range that includes\u2014\n**(I)**\na concentration level at which a healthy adult should take action to reduce exposure; and\n**(II)**\na concentration level at which there is evidence of adverse human health effects in susceptible subpopulations, such as infants, children, pregnant women, workers, and the elderly.\n**(C) Insufficient evidence**\nIf the Administrator determines insufficient evidence exists to set a health-based concentration limit for an indoor contaminant of concern listed under subsection (a), the Administrator shall publish a report not later than 1 year after making such determination, which shall identify\u2014\n**(i)**\nstudies and other activities to be taken to develop the evidence necessary to set a health-based concentration limit; and\n**(ii)**\nresources necessary to carry out activities under clause (i).\n**(D) Interim guidelines**\nWhile the Administrator develops sufficient scientific evidence to set a recommended health-based concentration limit for an indoor contaminant of concern under subparagraph (A), the Administrator shall publish interim guidelines, which shall include best practices to reduce exposure to such indoor contaminant of concern.\n##### (d) Review and revision\nNot less than every five years, the Administrator shall review and, as necessary, revise\u2014\n**(1)**\nthe list of indoor contaminants of concern under subsection (a); and\n**(2)**\nthe guidelines published under subsection (c).\n##### (e) Consultation\nIn developing, reviewing, and revising the guidelines published under subsection (c), the Administrator shall consult with representatives from non-profit, professional, private sector, governmental, and labor organizations, and individuals, having demonstrated expertise in indoor air quality, public health, building systems, industrial hygiene, environmental engineering, toxicology, and environmental health and safety.\n##### (f) Consistency with indoor air regulations of other Federal agencies\n**(1) Labor**\n**(A) Consistency with certain regulations**\nThe Administrator shall, after consultation with the Secretary of Labor, ensure that the guidelines published under subsection (c) are consistent with any Federal workplace regulations addressing indoor air quality risks.\n**(B) Additional voluntary actions**\nNotwithstanding subparagraph (A), the guidelines published under subsection (c) may recommend additional voluntary actions to protect persons other than workers covered by such guidelines from indoor contaminants of concern listed under subsection (a).\n**(2) Energy**\nThe Administrator shall, after consultation with the Secretary of Energy, ensure that the guidelines published under subsection (c) are consistent with applicable energy conservation and efficiency statutes and regulations administered by the Secretary.\n#### 5. Indoor air quality index\n##### (a) In general\nThe Administrator shall seek to enter, not later than 1 year after the date of enactment of this Act, into an agreement with the National Academy of Sciences under which the Academy agrees to conduct a study to assess the feasibility of developing a science-based indoor air quality index aimed at informing action for the protection of public health.\n##### (b) Report\nNot later than 2 years after entering into an agreement with the Administrator under subsection (a), the Academy shall submit to the Congress and the Administrator a report, which shall\u2014\n**(1)**\nmake recommendations to support the development of an indoor air quality index while ensuring that such proposed index\u2014\n**(A)**\ncommunicates to the public in clear and simple terms the level of concern and description of indoor air quality;\n**(B)**\nconsiders health risks for certain sensitive groups of people;\n**(C)**\naddresses the feasibility of assessing indoor air quality through low-cost, real-time sensors and monitoring equipment; and\n**(D)**\nallows for updates to account for developments in science and harmonization with indoor air quality guidelines developed under section 4;\n**(2)**\nproposes methodologies, inputs, measurements, techniques, and equations to calculate a science-based assessment of indoor air quality; and\n**(3)**\nidentifies limitations and challenges to the development of an indoor air quality index.\n##### (c) Authorization of appropriations\nThere is authorized to be appropriated $1,000,000, to remain available until expended, to carry out this section.\n#### 6. Indoor air quality assistance\n##### (a) In general\nThe Administrator may provide technical assistance and financial assistance, which may include grants, to State, local, and Tribal governments, local educational agencies, housing authorities, nonprofit organizations, labor organizations, and other persons to develop and implement programs to assess and improve indoor air quality.\n##### (b) Use of funds\nFinancial assistance awarded under this section shall be used to support one or more of the following:\n**(1)**\nThe development and implementation of educational programs, training and technical assistance programs, assessment and monitoring programs, benchmarking programs, response programs, and other activities designed to reduce human exposure to indoor air contaminants.\n**(2)**\nMitigation of health risks from indoor air contaminants due to more frequent extreme weather events and other consequences of climate change.\n**(3)**\nAdoption or adaptation by State, local, and Tribal governments of indoor air quality guidelines published pursuant to section 4, or development and adoption of indoor air quality standards based on such guidelines, including development of assessment and compliance programs needed to implement such standards.\n##### (c) Matching requirement\nThe Federal share of the cost of the activities for which financial assistance is awarded under this section shall not exceed 75 percent of the total cost of such activities.\n#### 7. Healthy building certifications\n##### (a) In general\nThe Administrator shall provide for one or more types of voluntary certifications of buildings that are built, operated, and maintained to prevent or minimize risks to health from indoor air contaminants in an exemplary manner.\n##### (b) Requirements\nFor a building to be certified under this section, the owner or operator of the building\u2014\n**(1)**\nshall adhere to applicable guidelines published by the Administrator pursuant to section 4; and\n**(2)**\nshall develop and maintain an indoor air quality management plan in accordance with best practices developed or approved by the Administrator.\n##### (c) Consideration\nA certification process under subsection (a) may recognize actions taken by the owners and operators of existing buildings to improve indoor air quality using the most effective source control, air filtration, ventilation, and other best practices, techniques, and products.\n##### (d) Option for third-Party administration\nThe Administrator may\u2014\n**(1)**\ncarry out a certification process under subsection (a) directly; or\n**(2)**\nrecognize one or more certification processes under subsection (a) that are developed and administered through a third party.\n#### 8. Model provisions for building design, operation, and maintenance\n##### (a) Model provisions for authorities having jurisdiction\nNot later than 1 year after the date of enactment of this Act, the Administrator shall recommend one or more model provisions for building design, operation, and maintenance for use by States and local jurisdictions in establishing and implementing building codes.\n##### (b) Components of model provisions\nThe model provisions recommended under this section shall\u2014\n**(1)**\nestablish minimum requirements that address ventilation, filtration, air cleaning, and design, operation, and maintenance of relevant building systems (including equipment, filtration, and controls); and\n**(2)**\naddress acceptable indoor air quality and may include control of infectious aerosols and indoor contaminants of concern.\n##### (c) Consideration of model provisions\nIn accordance with section 12(d) of the National Technology Transfer and Advancement Act of 1995 ( 15 U.S.C. 272 note), the Administrator shall consider technical standards that are developed or adopted by voluntary consensus standards bodies in the development of recommendations under this section.\n##### (d) Consultation\nIn recommending model provisions under this section, the Administrator shall consult with organizations, including non-profit, professional, private sector, governmental, and labor organizations, having demonstrated expertise in building systems and indoor air quality, public health, indoor chemistry, building codes and standards, and above-code building programs.\n##### (e) No conflict with model energy code or standard\nThe Administrator shall consult with the Secretary of Energy to ensure that model provisions recommended under this section do not conflict with a model energy code or standard for which the Secretary has made an affirmative determination under section 304 of the Energy Conservation and Production Act, provided that such recommended model provisions may be additive and more stringent than related provisions of the model energy code or standard.\n##### (f) Review and revision\nThe Administrator shall, not less than once every three years, review and revise (as necessary), in accordance with this section, the recommendations for model provisions developed under this section.\n##### (g) Cost and benefit\nNot less than 12 months following a recommendation for model provisions under this section, the Administrator shall determine the incremental costs and the 30-year health benefits associated with compliance with the model provisions for new single-family homes, multifamily dwelling units, and a representative set of commercial building prototypes.\n#### 9. Healthy schools\n##### (a) Assessment of schools and covered childcare facilities\n**(1) In general**\nThe Administrator shall conduct a national assessment of indoor air quality in buildings used by local educational agencies and covered childcare facilities.\n**(2) Assessment contents**\nThe national assessment under this section, including updates thereto\u2014\n**(A)**\nshall include data and metrics, as determined appropriate by the Administrator, to track progress in, and challenges to, improving the indoor air quality in buildings used by local educational agencies and covered child care facilities;\n**(B)**\nshall assess whether buildings used by local educational agencies and covered childcare facilities achieve acceptable indoor air quality by meeting minimum ventilation rate requirements and other factors as set forth by widely recognized best practices and standards, as determined appropriate by the Administrator, such as ANSI/ASHRAE Standard 62.1\u20132022, Ventilation and Acceptable Indoor Air Quality; and\n**(C)**\nmay be conducted through a survey, an onsite representative sampling of buildings (accounting for geography and building size, type, and age), or other methods or combination of methods determined appropriate by the Administrator to accurately assess the condition of buildings used by local educational agencies and covered childcare facilities throughout the United States.\n**(3) Advisory group**\n**(A) Establishment**\nThe Administrator shall establish an advisory group to provide guidance and direction in the development of the initial national assessment under this subsection.\n**(B) Members**\nThe advisory group under subparagraph (A) shall include representatives of\u2014\n**(i)**\nschool administrators, teachers, maintenance staff, and other people working in buildings described in paragraph (1), labor organizations, childcare providers, and parents and caregivers; and\n**(ii)**\nother interested parties, including scientific and technical experts familiar with indoor air contaminant exposures, effects, and controls.\n**(4) Initial assessment; updates**\n**(A) Initial assessment**\nNot later than 3 years after the date of enactment of this Act, the Administrator shall conduct the initial national assessment under paragraph (1).\n**(B) Updates**\nNot less than five years following the completion of the initial national assessment under subparagraph (A), and each five years thereafter, the Administrator shall carry out an update of the previous national assessment under this subsection, accounting for\u2014\n**(i)**\nthe number of schools certified pursuant to subsection (c); and\n**(ii)**\nchanges in the guidelines, best practices, and other support published by the Administrator to improve indoor air quality.\n**(5) Reports to Congress**\nUpon completing each national assessment under this subsection, the Administrator shall\u2014\n**(A)**\nsubmit to the Congress a report on the results of such assessment; and\n**(B)**\ninclude in each such report such recommendations as the Administrator determines to be appropriate for activities or programs to reduce and avoid indoor air contaminants in buildings used by local educational agencies and covered childcare facilities.\n##### (b) Technical assistance and other support\n**(1) In general**\nThe Administrator shall develop and promote guidance, best practices, technical assistance, training, outreach, and other support to improve indoor air quality in buildings used by a local educational agency or a covered childcare facility.\n**(2) Considerations**\nThe Administrator shall tailor guidance, best practices, technical assistance, training, outreach, and other support under paragraph (1) to the needs of\u2014\n**(A)**\nstudents;\n**(B)**\nparents and caregivers;\n**(C)**\neducators;\n**(D)**\nchildcare providers;\n**(E)**\nmaintenance staff and other employees responsible for operating and maintaining buildings referred to in paragraph (1);\n**(F)**\nIndian Tribes; and\n**(G)**\nlow-income and disadvantaged communities.\n##### (c) Healthy school certification\nThe Administrator shall ensure that at least one type of certification carried out or recognized pursuant to section 7 is applicable to buildings used by local educational agencies and covered childcare facilities.\n##### (d) Interagency coordination\nThe Administrator shall coordinate with the Secretary of Education, the Secretary of Energy, the Secretary of Health and Human Services, the Secretary of Labor, and the heads of other relevant Federal agencies, to ensure that any Federal assistance made available to local educational agencies or covered childcare facilities for building construction, alteration, repair, and maintenance is consistent with any guidance and best practices developed by the Administrator under this Act.\n#### 10. Relation to other law\n##### (a) General authority\nNothing in this Act shall be construed, interpreted, or applied to preempt, displace, or supplant any other State or Federal law, whether statutory or common, or any local ordinance.\n##### (b) Occupational safety and health\nIn exercising any authority under this Act, the Administrator shall not, for purposes of section 4(b)(1) of the Occupational Safety and Health Act of 1970 ( 29 U.S.C. 653(b)(1) ), be considered to be exercising statutory authority to prescribe or enforce standards or regulations affecting occupational safety or health.\n#### 11. Authorization of appropriations\nThere is authorized to be appropriated $100,000,000 for each of fiscal years 2026 through 2030 to carry out this Act (other than section 5).",
      "versionDate": "2025-09-03",
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
        "name": "Environmental Protection",
        "updateDate": "2025-09-23T17:03:06Z"
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
      "date": "2025-09-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5123ih.xml"
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
      "title": "Indoor Air Quality and Healthy Schools Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-09T04:23:34Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Indoor Air Quality and Healthy Schools Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-09T04:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To authorize a national program to reduce the threat to human health posed by exposure to indoor air contaminants, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-09T04:18:25Z"
    }
  ]
}
```
