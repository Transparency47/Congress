# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6621?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6621
- Title: Workforce of the Future Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 6621
- Origin chamber: House
- Introduced date: 2025-12-11
- Update date: 2026-03-18T08:06:48Z
- Update date including text: 2026-03-18T08:06:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-12-11: Introduced in House

## Actions

- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Introduced in House
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-12-11 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6621",
    "number": "6621",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "C001061",
        "district": "5",
        "firstName": "Emanuel",
        "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
        "lastName": "Cleaver",
        "party": "D",
        "state": "MO"
      }
    ],
    "title": "Workforce of the Future Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-18T08:06:48Z",
    "updateDateIncludingText": "2026-03-18T08:06:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T16:04:25Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-12-11T16:04:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "M001229",
      "district": "10",
      "firstName": "LaMonica",
      "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
      "isOriginalCosponsor": "True",
      "lastName": "McIver",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NJ"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "CT"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "DC"
    },
    {
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2026-01-08",
      "state": "HI"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "TX"
    },
    {
      "bioguideId": "W000831",
      "district": "11",
      "firstName": "James",
      "fullName": "Rep. Walkinshaw, James R. [D-VA-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Walkinshaw",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "VA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-03-17",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6621ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6621\nIN THE HOUSE OF REPRESENTATIVES\nDecember 11, 2025 Mr. Cleaver (for himself, Mrs. McIver , Mr. Larson of Connecticut , Mr. Goldman of New York , and Ms. Norton ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo promote a 21st-century workforce, to authorize grants to support emerging and advanced technology education, and to support training and quality employment for workers in industries most impacted by artificial intelligence.\n#### 1. Short title\nThis Act may be cited as the Workforce of the Future Act of 2025 .\n#### 2. Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title.\nSec. 2. Table of contents.\nTITLE I\u2014Impact of Artificial Intelligence on Jobs\nSec. 101. Sense of Congress.\nSec. 102. Definitions.\nSec. 103. Report on artificial intelligence.\nTITLE II\u2014Emerging and Advanced Technology Education and Workforce Development\nSec. 201. Findings.\nSec. 202. Definitions.\nSec. 203. Department of Education grants.\nSec. 204. Department of Labor grants.\nSec. 205. Reporting requirements.\nSec. 206. Amendments to the Education Sciences Reform Act.\nI\nImpact of Artificial Intelligence on Jobs\n#### 101. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nwhile the field of artificial intelligence is evolving quickly and has potential to disrupt jobs, there are opportunities to prepare the American workforce to develop and work alongside this new technology and mitigate the potential negative consequences of job displacement; and\n**(2)**\nto ensure these opportunities, it is imperative to identify the following:\n**(A)**\nData and data access necessary to properly analyze the impact of artificial intelligence on the United States workforce.\n**(B)**\nIndustries projected to be most impacted by artificial intelligence.\n**(C)**\nOpportunities for workers and other stakeholders to influence the impact of artificial intelligence across industries.\n**(D)**\nCharacteristics of workers and communities whose career opportunities are most likely to be affected by the growth of artificial intelligence.\n**(E)**\nThe skills, expertise, and education needed to develop, operate, or work alongside artificial intelligence.\n**(F)**\nMethods to ensure necessary skills, expertise, and education are accessible to all segments of the current and future workforce.\n#### 102. Definitions\nIn this title:\n**(1) Artificial intelligence**\nThe term artificial intelligence has the meaning given the term in section 5002 of the National Artificial Intelligence Initiative Act of 2020 ( 15 U.S.C. 9401 ).\n**(2) Community college**\nThe term community college has the meaning given the term junior or community college in section 312(f) of the Higher Education Act of 1965 ( 20 U.S.C. 1058(f) ).\n**(3) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(4) Labor organization**\nThe term labor organization includes a labor organization as defined in section 2(5) of the National Labor Relations Act ( 29 U.S.C. 152(5) ) and an organization representing public sector employees.\n**(5) Local educational agency**\nThe term local educational agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(6) Minority-serving institution**\nThe term minority-serving institution means an eligible institution as described in section 371 of the Higher Education Act of 1965 ( 20 U.S.C. 1067q ).\n**(7) State educational agency**\nThe term State educational agency has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(8) Technical college**\nThe term technical college means a postsecondary vocational institution, as that term is defined in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) ).\n**(9) Tribal College or University**\nThe term Tribal College or University has the meaning given the term in section 316 of the Higher Education Act of 1965 ( 20 U.S.C. 1059c ).\n#### 103. Report on artificial intelligence\n##### (a) In general\n**(1) Interim and final reports**\nThe Secretary of Labor, the Secretary of Commerce, and the Secretary of Education shall, jointly and in collaboration with the individuals and entities described in subsection (c), prepare and submit to the Committee on Education and Workforce, the Committee on Energy and Commerce, and the Committee on Science, Space, and Technology of the House of Representatives, and the Committee on Health, Education, Labor, and Pensions and the Committee on Commerce, Science, and Transportation of the Senate\u2014\n**(A)**\nnot later than 6 months after the date of enactment of this Act, an interim report on artificial intelligence and its impact on the workforce of the United States, which shall include the information and recommendations listed in subsection (b);\n**(B)**\nnot later than 1 year after the date of enactment of this Act, a final report on artificial intelligence and its impact on the workforce of the United States, which shall include the information and recommendations listed in subsection (b); and\n**(C)**\nnot later than 3 years after the final report described in subparagraph (B) is submitted, an updated report reassessing the information and recommendations listed in subsection (b).\n**(2) Memorandum of understanding**\nThe Secretary of Labor may enter into a memorandum of understanding with the Secretary of Commerce and the Secretary of Education to establish procedures for the preparation and submission of the interim and final reports described in paragraph (1).\n##### (b) Required information\nEach report submitted under subsection (a) shall include the following:\n**(1)**\nAn identification of the specific data relating to the workforce, and the availability of such data, necessary to properly analyze the impact and growth of artificial intelligence on the workforce of the United States and outline how much of this data is privately owned, and the effectiveness of Federal, State, or industry efforts (including public-private partnerships) to make privately owned data on the workforce of the United States available for Federal research purposes.\n**(2)**\nIdentification of industries and occupations projected to have the most growth in artificial intelligence use, the extent to which the technology is likely to result in the enhancement of workers\u2019 capabilities or their displacement, and level of education currently consistent with industries and occupations identified.\n**(3)**\nAnalysis of how growth in artificial intelligence use will impact job quality in the industries and occupations identified in paragraph (2).\n**(4)**\nIdentification of opportunities for workers, educators, institutions of higher education, Congress, labor organizations, or other relevant stakeholders to influence the impact of artificial intelligence on workers across various industries.\n**(5)**\nAnalysis of how educational entities, workforce development organizations, and labor organizations can collaborate to advance new opportunities for education and workforce development to support an artificial intelligence-enabled economy and workforce.\n**(6)**\nAnalysis of which demographics (including ethnic, race, gender, economic, age, disability status, and regional) currently stand to experience expanded career opportunities, and which demographics currently appear most vulnerable to career displacement, due to artificial intelligence.\n**(7)**\nAnalysis of the skills, expertise, and education in emerging and advanced technology needed to develop, operate, or work alongside artificial intelligence over the next decades, as compared to the levels of such comparable expertise and education among the workforce as of the date of enactment of this Act, with a differentiation between core competencies required across the entire workforce and competencies required within the industries and occupations identified in paragraph (2).\n**(8)**\nIdentification of methods by which necessary skills, expertise, and education can be effectively delivered to various segments of the United States workforce, including promising efforts underway as of the time of the report that can be expanded.\n**(9)**\nIdentification of industry leaders, institutions of higher education, and labor organizations at the forefront of research and application of artificial intelligence in the industries and occupations identified in paragraph (2).\n**(10)**\nIdentification of the resources and opportunities required for labor organizations and institutions of higher education, including community colleges, technical colleges, minority-serving institutions (including Tribal Colleges and Universities), and institutions of higher education serving rural areas, to deliver skills, expertise, and education identified in paragraph (7).\n**(11)**\nIdentification of the demographic characteristics and educational background (including level of education) of the individuals who deliver skills, expertise, and education to students at the institutions described in paragraph (10).\n**(12)**\nRecommendations to support enhanced workforce development and prepare future workforce members for the artificial intelligence economy, and any other relevant observations or recommendations within the field of emerging and advanced technology, which shall include recommendations on\u2014\n**(A)**\nmethods to expand public access to privately owned workforce data and government-owned workforce data, for the purpose of researching the effect of emerging technologies on the United States workforce;\n**(B)**\npolicy, regulatory, or programmatic options for stakeholders (workers, educators, institutions of higher education, Congress, labor organizations, or other relevant stakeholders) to effectively enhance educational and workforce development opportunities, including mitigating perceived negative impacts of artificial intelligence on segments of the United States workforce;\n**(C)**\nrecommendations to employers on best practices to engage workers and representatives of workers, including labor organizations, in decision-making on the integration of artificial intelligence into the workplace;\n**(D)**\nmethods to upskill or mitigate earnings or income losses to demographic groups identified in paragraph (6) as most vulnerable to career displacement, due to artificial intelligence;\n**(E)**\nmethods to encourage low cost, open source sharing of industry valued credentials certifying the types of skills, expertise, and education identified in paragraph (7);\n**(F)**\nmethods to ensure core skills and competencies identified in paragraph (7) can be evaluated, updated, and made public by relevant stakeholders as needed, given rapid developments in the field of artificial intelligence;\n**(G)**\nmethods to ensure community colleges, technical colleges, minority-serving institutions (including Tribal Colleges and Universities), and institutions of higher education serving rural areas receive resources and opportunities identified in paragraph (10);\n**(H)**\nmethods to promote knowledge sharing and capacity building between industry leaders, labor organizations, and institutions identified in paragraph (9) and community colleges, technical colleges, minority-serving institutions (including Tribal Colleges and Universities), and rural institutions of higher education; and\n**(I)**\nother methods to ensure that the skills, expertise, and education needed to develop, operate, or work alongside artificial intelligence are delivered to vulnerable demographic groups identified in paragraph (6), rural workers, and other historically underserved segments of the United States workforce (including workers with disabilities).\n##### (c) Collaboration\nIn preparing the report under subsection (a), the Secretary of Labor, the Secretary of Commerce, and the Secretary of Education shall collaborate, through a series of public meetings, roundtables or other methods, with\u2014\n**(1)**\nlocal educational agencies, State educational agencies, State agencies with responsibility for the administration of a core program (as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )), institutions of higher education (including community colleges, technical colleges, minority-serving institutions (including Tribal Colleges and Universities), and institutions of higher education serving rural areas), labor organizations, workforce-training organizations, National Laboratories, and teacher and educator preparation programs;\n**(2)**\na broad range of industrial stakeholders in the technology, manufacturing, employment, human resources, and service sectors, including companies (large and small), think tanks, organized labor, and industry organizations;\n**(3)**\nthe National Academies of Sciences, Engineering, and Medicine, including by sharing relevant information obtained as a result of the study conducted under section 5105 of the National Artificial Intelligence Initiative Act of 2020 ( Public Law 116\u2013283 ; 134 Stat. 4530); and\n**(4)**\nthe Director of the National Science Foundation, the Director of the White House Office of Science and Technology Policy, the Director of the National Artificial Intelligence Initiative Office, the National Cyber Director, and the heads of any other Federal agency the Secretary of Labor, the Secretary of Commerce, and the Secretary of Education determine appropriate.\nII\nEmerging and Advanced Technology Education and Workforce Development\n#### 201. Findings\nCongress finds the following:\n**(1)**\nEmerging and advanced technologies are transforming industry, creating new fields of commerce, driving innovation, and bolstering productivity. Emerging and advanced technology and information occupations are projected to grow by 377,500 jobs per year on average between 2022 and 2032, much faster than the average for all other occupations.\n**(2)**\nAs of 2024, more than 400,000 computing and technology jobs remain unfilled in the United States. These unfilled jobs present a significant opportunity for individuals to advance in the 21st-century economy. It is projected that there will be 660,000 new jobs in the technology and computing sector by 2032. However, the availability of emerging and advanced technology education at the time of enactment of this Act does not equitably provide all students in the United States with the tools to fill these technology sector jobs.\n**(3)**\nGiven the rapidly increasing interest and deployment of artificial intelligence and other new technologies in the workplace, knowledge of, and the skills to use, emerging and advanced technology is increasingly essential for all individuals, not just those working or planning to work in the technology sector.\n**(4)**\nProviding students with emerging and advanced technology education in elementary school and secondary school is critical for student success, and strengthening the workforce of a 21st-century economy.\n**(5)**\nWhile an estimated 90 percent of parents want technology, such as computer science, taught in their children\u2019s schools, just 44 percent of all middle schools and 57.5 percent of secondary schools offer high-quality technology instruction that includes programming and coding.\n**(6)**\nLack of universal emerging and advanced technology education is evident in the lack of a widespread tech industry, which is overwhelmingly concentrated in a few cities nationwide. Emerging and advanced technology education is limited to affluent schools and students, placing low-income, minority, and rural communities at risk of being left behind.\n#### 202. Definitions\nIn this title:\n**(1) Computational thinking**\nThe term computational thinking means the wide range of creative processes that go into formulating problems and their solutions in such a way that the solutions can be carried out by a computer, and may involve some understanding of software and hardware design, logic and the use of abstraction and representation, algorithm design, algorithm expression, problem decomposition, modularity, programming paradigms and languages, issues of information security and privacy, the application of computation across a wide range of disciplines, and the societal impact of computing.\n**(2) Eligible entity**\nThe term eligible entity means\u2014\n**(A)**\na State educational agency, as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 );\n**(B)**\na local educational agency, as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 );\n**(C)**\nan eligible Tribal school;\n**(D)**\na community college, which shall have the meaning given the term junior or community college in section 312(f) of the Higher Education Act of 1965 ( 20 U.S.C. 1058(f) );\n**(E)**\na technical college or postsecondary vocational institution, as that term is defined in section 102(c) of the Higher Education Act of 1965 ( 20 U.S.C. 1002(c) );\n**(F)**\na labor organization (as defined in section 102);\n**(G)**\na State agency with responsibility for a workforce development program, as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 ); or\n**(H)**\nan institution of higher education.\n**(3) Eligible tribal school**\nThe term eligible Tribal school means\u2014\n**(A)**\na school operated by the Bureau of Indian Education;\n**(B)**\na school operated pursuant to the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5301 et seq. ); or\n**(C)**\na tribally controlled school (as defined in section 5212 of the Tribally Controlled Schools Act of 1988 ( 25 U.S.C. 2511 )).\n**(4) Emerging and advanced technology education**\nThe term emerging and advanced technology education includes education in any of the following: computational thinking; software design; hardware architecture and organization; theoretical foundations; use of abstraction and representation in problem solving; logic; algorithm design and implementation; the limits of computation; programming paradigms and languages; parallel and distributed computing; information security and privacy; computing systems and networks; graphics and visualization; databases and information retrieval; the relationship between computing and mathematics; artificial intelligence; quantum computing; applications of computing across a broad range of disciplines and problems; cloud computing; and the social impacts and professional practices of computing.\n**(5) Institution of higher education**\nThe term institution of higher education has the meaning given the term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(6) Minority-serving institution**\nThe term minority-serving institution means an eligible institution as described in section 371 of the Higher Education Act of 1965 ( 20 U.S.C. 1067q ).\n**(7) Poverty line**\nThe term poverty line has the meaning given the term in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(8) Programming**\nThe term programming means a hands-on, inquiry-based way in which computational thinking may be learned.\n**(9) Secretary**\nThe term Secretary means the Secretary of Education.\n**(10) STEAM**\nThe term STEAM means the subjects of science, technology, engineering, arts, and mathematics, including emerging and advanced technology.\n#### 203. Department of Education grants\n##### (a) Authorization of grants\n**(1) In general**\nThe Secretary shall award grants to eligible entities to support the expansion of emerging and advanced technology education. From the amounts appropriated under subsection (g), after reserving amounts under subsection (e), the Secretary shall\u2014\n**(A)**\nreserve 50 percent of the remaining funds to award grants to eligible entities that propose to use grant funds in accordance with subsection (c); and\n**(B)**\nreserve 50 percent of the remaining funds to award grants to eligible entities that propose to use grant funds in accordance with subsection (d).\n**(2) Consortia**\nAn eligible entity may apply for a grant under this section as part of a consortium of one or more eligible entities.\n**(3) Duration**\nGrants awarded under this section shall be for a period of not less than 3 years and not more than 5 years.\n**(4) Considerations**\nIn awarding grants under this section, the Secretary shall consider\u2014\n**(A)**\nthe information and recommendations included in the reports prepared under section 103; and\n**(B)**\nstructural and other barriers facing specific demographic groups, as informed by the reports prepared under section 103.\n**(5) Multiple awards**\n**(A) In general**\nExcept as provided in subparagraph (B), an eligible entity may receive only 1 grant award under this section.\n**(B) Part of consortia**\n**(i) In general**\nAn eligible entity may receive more than 1 grant award under this section if the eligible entity is part of consortia that receive the grant awards.\n**(ii) Lead fiscal agent**\nAn eligible entity that receives more than 1 grant award under this section as part of consortia, may be the lead fiscal agent only on 1 grant award under this section.\n##### (b) Application requirements\n**(1) In general**\nAn eligible entity that desires a grant under this section shall submit an application to the Secretary at such time, in such manner, and containing such information as the Secretary may require.\n**(2) Plan**\nAn eligible entity that proposes to use grant funds in accordance with subsection (c) shall include in the application under paragraph (1), at a minimum, plans for the following:\n**(A)**\nEvery high school student served by the eligible entity to have access to emerging and advanced technology education not later than 5 years after receipt of grant funds.\n**(B)**\nAll students served by the eligible entity to have access to a progression of emerging and advanced technology education from prekindergarten through the middle grades (as defined in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )) that prepares students for high school emerging and advanced technology education.\n**(C)**\nExpansion of overall access to rigorous (as defined by the Secretary) STEAM classes, utilizing emerging and advanced technology as a catalyst for increased interest in STEAM more broadly, and reducing the enrollment and academic achievement gap for underrepresented groups, such as minorities, girls, and youth from families living at, or below, the poverty line.\n**(D)**\nContinuous monitoring and evaluation of project activities.\n**(E)**\nEffectively sustaining project activities after the grant period ends, and the length of time which the applicant plans to sustain the project activities.\n**(F)**\nDisclosure of how the eligible entity will engage with industry to inform the project activities, and with which entities from industry they will engage.\n**(G)**\nLeveraging of permissible activities described in subsection (c)(2), if relevant to support and enhance program activities.\n##### (c) Grant funds for emerging and advanced technology education\n**(1) Required activities**\nAn eligible entity that receives a grant under subsection (a)(1)(A) shall use the grant funds for each of the following activities:\n**(A)**\nTraining teachers to teach emerging and advanced technology, including providing professional development opportunities.\n**(B)**\nExpanding access to high-quality learning materials and online learning options, including equipment and other related technologies and access to broadband internet that are necessary to fully perform in the area of emerging and advanced technologies.\n**(C)**\nCreating plans for expanding overall access to rigorous STEAM classes, utilizing emerging and advanced technology as a catalyst for increased interest in STEAM more broadly, and reducing course equity gaps for all students, including underrepresented groups, such as minorities, girls, and youth from low-income families.\n**(D)**\nEnsuring additional support and resources, which may include mentoring for students traditionally underrepresented in STEAM fields.\n**(E)**\nOngoing industry engagement to receive feedback on curricula and the emerging skills needed of artificial intelligence-related jobs.\n**(2) Permissible activities**\nAn eligible entity that receives a grant under subsection (a)(1)(A) may use the grant funds for 1 or more of the following activities:\n**(A)**\nBuilding effective regional collaborations with industry, nonprofit organizations, State boards and local boards (as such terms are defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )), institutions of higher education (including community colleges, technical colleges, and minority-serving institutions), and out-of-school providers.\n**(B)**\nRecruiting and hiring instructional personnel as needed, including teachers and paraeducators (which shall have the meaning given the term paraprofessional in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 )), including through support for the workforce development system (as defined in section 3 of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3102 )) in the State.\n**(C)**\nPreparations for effectively sustaining project activities after the grant period ends.\n**(D)**\nDisseminating information about effective practices.\n**(3) Limitation**\nNot more than 15 percent of a grant awarded under subsection (a)(1)(A) may be used to purchase equipment.\n##### (d) Grant funds for emerging and advanced technology teacher development and recruitment\n**(1) In general**\nAn eligible entity that receives a grant under subsection (a)(1)(B) shall use the grant funds for emerging and advanced technology teacher development and recruitment, which may include professional development opportunities, loan repayment, or tuition reimbursement for service as an emerging and advanced technology teacher, or any other program designed to develop and recruit emerging and advanced technology teachers.\n**(2) Fulfilling obligation**\nIf an eligible entity that receives a grant under subsection (a)(1)(B) uses the grant funds to implement a loan repayment program or program for tuition reimbursement for service as an emerging and advanced technology teacher, the eligible entity shall fulfill any loan repayment or tuition reimbursement obligation made to a teacher in exchange for service.\n##### (e) National activities\nThe Secretary may reserve not more than 2.5 percent of funds available for grants under this section for national activities, including technical assistance, evaluation, and dissemination.\n##### (f) Evaluations\nIn carrying out this section, the Secretary shall authorize third-party evaluations of grants awarded under this section to help build an evidence base of effective programs that advance a 21st-century artificial intelligence workforce. Such evaluations shall assess the scalability of activities funded by such grants to support the 21st-century artificial intelligence workforce.\n##### (g) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $160,000,000 for fiscal year 2026.\n#### 204. Department of Labor grants\n##### (a) Grants authorized\n**(1) In General**\nThe Secretary of Labor shall award grants to eligible entities to support workforce training for workers most impacted by artificial intelligence. From the amounts appropriated under subsection (f), after reserving amounts under subsection (d), the Secretary of Labor shall award grants as described in subsection (b).\n**(2) Consortia**\nAn eligible entity may apply for a grant under this section as part of a consortium of eligible entities.\n**(3) Duration**\nGrants awarded under this section shall be for a period of not less than 3 years and not more than 5 years.\n**(4) Considerations**\nIn awarding grants under this section, the Secretary of Labor shall consider\u2014\n**(A)**\nthe information and recommendations included in the reports prepared under section 103; and\n**(B)**\nstructural and other barriers facing specific demographic groups, as informed by the reports prepared under section 103.\n**(5) Priority**\nIn awarding grants under this section, the Secretary of Labor shall give priority to eligible entities that are labor organizations representing workers in industries or occupations identified in the report under section 103(b)(2), or consortia of eligible entities that include such a labor organization.\n##### (b) Grant funds To serve individuals seriously affected by AI\n**(1) Target population**\nAn eligible entity that receives a grant under this section shall use the grant funds to serve individuals who have a high school diploma or its recognized equivalent and\u2014\n**(A)**\nare employed in an industry or occupation projected, pursuant to the report under section 103(b)(2), to have the most growth in artificial intelligence use, which is likely to significantly impact the job opportunities or wages of workers; or\n**(B)**\nnot earlier than 1 year prior to the date of enactment of this Act, involuntarily separated from an industry or occupation projected, pursuant to the report under section 103(b)(2), to have the most growth in artificial intelligence use, and are eligible for unemployment insurance.\n**(2) Activities**\nIn serving the target population described in paragraph (1), an eligible entity that receives a grant under this section shall use the grant funds for 1 or more of the following purposes:\n**(A)**\nProviding training to such individuals, including skill certifications, or by supporting other programs that directly enable such individuals to enter high-skill, high-wage jobs in in-demand sectors, including emerging and advanced technology sectors.\n**(B)**\nProviding training to such individuals, including continuing education certificates or programs aiming\u2014\n**(i)**\nto update workers\u2019 skills related to advanced and emerging technology; and\n**(ii)**\nto support maintaining or advancing in high-skill, high-wage jobs in in-demand sectors, including emerging and advanced technology sectors.\n##### (c) Application requirements\nAn eligible entity that desires a grant under this section shall submit an application to the Secretary of Labor at such time, in such manner, and containing such information and assurances as the Secretary of Labor may require, including, at a minimum each of the following:\n**(1)**\nA detailed description of project activities that will be carried out using grant funds, how such activities will serve the target population described in subsection (b)(1), and how such programs will support the growth of the 21st-century workforce.\n**(2)**\nA detailed description of how the eligible entity will engage workers and utilize input from workers in the design of project activities.\n**(3)**\nA detailed description of how job quality and wage considerations, alongside skill development, have informed project activities.\n**(4)**\nA plan for continuous monitoring and evaluation of project activities.\n**(5)**\nA plan for effectively sustaining project activities after the grant period ends, and the length of time which the applicant plans to sustain the project activities.\n**(6)**\nAn assurance to provide performance data, as described in subclause (I) through (VI) of section 116(b)(2)(A)(i) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3141(b)(2)(A)(i) ).\n##### (d) National activities\nThe Secretary of Labor may reserve not more than 2.5 percent of funds available for grants under this section for national activities, including technical assistance, evaluation, and dissemination.\n##### (e) Evaluations\n**(1) In general**\nIn carrying out this section, the Secretary of Labor shall authorize third-party evaluations of grants awarded under this section to help build an evidence base of programs that advance a 21st-century workforce.\n**(2) Scalability; worker engagement**\nThe evaluations described in paragraph (1) shall assess\u2014\n**(A)**\nthe scalability of activities funded by the grants; and\n**(B)**\nthe effectiveness of worker engagement in the design of project activities in improving training relevance, completion rates, and employment outcomes for the target population.\n##### (f) Authorization of appropriations\nThere is authorized to be appropriated to carry out this section $90,000,000 for fiscal year 2026.\n#### 205. Reporting requirements\n##### (a) Grantee reports\nEach eligible entity\u2014\n**(1)**\nthat receives a grant under section 203 shall submit to the Secretary a report, not less than twice a year during the grant period, on the use of grant funds that shall include data on the numbers of individuals served through activities funded under such section, disaggregated by race (for Asian and Native Hawaiian or Pacific Islander individuals using the same race response categories as the decennial census of the population), ethnicity, gender, and eligibility to participate in the school lunch program established under the Richard B. Russell National School Lunch Act ( 42 U.S.C. 1751 et seq. ); and\n**(2)**\nthat receives a grant under section 204 shall submit to the Secretary of Labor a report, not less than twice a year during the grant period, on the use of grant funds that shall include data on the numbers of individuals served through activities funded under such section, disaggregated by race (for Asian and Native Hawaiian or Pacific Islander individuals using the same race response categories as the decennial census of the population), ethnicity, and gender.\n##### (b) Report by the secretary\nNot later than 5 years after the first grant is awarded under this title, the Secretary and the Secretary of Labor shall submit to Congress a report based on the analysis of reports received under subsection (a) with a recommendation on how to expand the programs under this title.\n#### 206. Amendments to the Education Sciences Reform Act\nSection 153(a)(1) of the Education Sciences Reform Act of 2002 ( 20 U.S.C. 9543(a)(1) ) is amended\u2014\n**(1)**\nin subparagraph (N), by striking and after the semicolon;\n**(2)**\nin subparagraph (O), by inserting and after the semicolon; and\n**(3)**\nby adding at the end the following:\n(P) the existence of emerging and advanced technology education (as defined in section 202 of the Workforce of the Future Act of 2025 ) in elementary schools and secondary schools, and the degree of competency in emerging and advanced technology fields among such students; .",
      "versionDate": "2025-12-11",
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
        "actionDate": "2025-12-03",
        "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions."
      },
      "number": "3319",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Workforce of the Future Act of 2025",
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
        "name": "Education",
        "updateDate": "2026-01-09T13:14:10Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6621ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To promote a 21st-century workforce, to authorize grants to support emerging and advanced technology education, and to support training and quality employment for workers in industries most impacted by artificial intelligence.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-07T09:05:39Z"
    },
    {
      "title": "Workforce of the Future Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-07T06:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Workforce of the Future Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-07T06:23:31Z"
    }
  ]
}
```
