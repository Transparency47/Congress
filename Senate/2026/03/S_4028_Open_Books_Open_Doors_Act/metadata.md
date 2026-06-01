# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4028?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4028
- Title: Open Books, Open Doors Act
- Congress: 119
- Bill type: S
- Bill number: 4028
- Origin chamber: Senate
- Introduced date: 2026-03-09
- Update date: 2026-03-26T18:16:57Z
- Update date including text: 2026-03-26T18:16:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-09: Introduced in Senate
- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2026-03-09: Introduced in Senate

## Actions

- 2026-03-09 - IntroReferral: Introduced in Senate
- 2026-03-09 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

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
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4028",
    "number": "4028",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "K000394",
        "district": "",
        "firstName": "Andy",
        "fullName": "Sen. Kim, Andy [D-NJ]",
        "lastName": "Kim",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "Open Books, Open Doors Act",
    "type": "S",
    "updateDate": "2026-03-26T18:16:57Z",
    "updateDateIncludingText": "2026-03-26T18:16:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-09",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-09",
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
        "item": {
          "date": "2026-03-09T20:27:17Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4028is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4028\nIN THE SENATE OF THE UNITED STATES\nMarch 9, 2026 Mr. Kim introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo expand equitable access to developmentally-appropriate literacy materials, programs, and family engagement in reading, especially in underserved communities, and strengthen the connection between literacy and long-term academic and economic success.\n#### 1. Short title\nThis Act may be cited as the Open Books, Open Doors Act .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nThe 2024 National Assessment of Educational Progress reading assessment results show a continued decline in reading scores for both fourth and eighth grade students, with average scores lower than both 2022 and 2019 levels.\n**(2)**\nAccording to the Annie E. Casey Foundation, 1 in 6 children who are not reading proficiently in third grade do not graduate from high school on time, a rate 4 times greater than that for proficient readers.\n**(3)**\nFamilies with incomes of $100,000 or more have nearly twice the number of books than families with less than $35,000 in annual income, at 125 and 73 respectively.\n**(4)**\nAccording to the American Consortium for Equity in Education, 45 percent of children in the United States live in neighborhoods that lack public libraries and stores that sell books or in homes where books are not present.\n**(5)**\n85 percent of all juveniles who interact with the juvenile court system are functionally low literate.\n**(6)**\nOnly 2 percent of the 20,600,000 17- to 21-year-olds in the United States are eligible, propensed to serve, and of high academic quality for military service, and only 29 percent of youth are eligible for military service without requiring some form of a standards waiver.\n**(7)**\nA 2025 study from the University of Florida and the University College London found that daily reading for pleasure among individuals in the United States has declined by more than 40 percent over the past 2 decades, a trend with serious implications for children\u2019s literacy development and long-term education outcomes.\n**(8)**\nChildren born to parents with low literacy skills are likely to have low skills themselves, perpetuating poverty and other socioeconomic issues related to low literacy.\n**(9)**\nAccording to the Department of Education, 43,000,000 adults in the United States, nearly 1 in 5 adults in the United States, can\u2019t read well enough to hold a basic job.\n**(10)**\nAccording to the Nobel Prize-winning economist James Heckman, every $1 invested in early childhood, including literacy programs, yields between $4 to $16 in long-term economic benefits.\n**(11)**\nAccording to the World Literacy Foundation, low literacy costs the United States economy more than $300,000,000,000 in lost earnings, lower workplace productivity, higher crime, and more government assistance.\n#### 3. Definitions\nIn this Act:\n**(1) ESEA definitions**\nThe terms local educational agency and State educational agency have the meanings given the terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(2) Book desert**\nThe term book desert means a geographic area (as defined by census tract, ZIP Code, or local educational agency) where children and families have limited or non-consistent access to developmentally-appropriate, high-interest, and culturally relevant books and print materials in the home, schools, or community settings, as evidenced by meeting 1 or more of the following criteria, as determined by the Secretary:\n**(A)**\nFewer than 1 book available per 300 children younger than 18 years of age.\n**(B)**\nNo public library or bookstore within a 1-mile radius in an urban area or a 10-mile radius in a rural area.\n**(C)**\nA high concentration of poverty, housing instability, or limited English proficiency that contributes to barriers in accessing books.\n**(D)**\n40 percent of households with children lacking reading materials at home.\n**(E)**\nLimited or no book distribution programs, literacy events, or reading-focused community infrastructure.\n**(3) Evidence-based literacy program**\nThe term evidence-based literacy program means any instructional or community-based program, intervention, or practice that\u2014\n**(A)**\nis grounded in the science of reading and incorporates methods shown, through high-quality research, to be effective in improving literacy skills for infants, toddlers, children, teens, young adults, parents, or other caregivers;\n**(B)**\ndemonstrates measurable outcomes in improving reading comprehension, phonemic awareness, vocabulary acquisition, early language development, fluency, or engagement with reading;\n**(C)**\nhas been evaluated through a rigorous study, such as randomized control trials, quasi-experiential designs, or longitudinal research, and shows statistically significant positive effects on literacy outcomes for the target population; and\n**(D)**\nincludes components for adult-child interaction, culturally responsive instruction, or family and caregiver engagement, where appropriate.\n**(4) Family literacy**\nThe term family literacy means services that are of sufficient intensity in terms of hours, and of sufficient duration, to make sustainable changes in a family, and that integrate all of the following activities:\n**(A)**\nInteractive literacy activities between parents and their children.\n**(B)**\nTraining for parents regarding how to be the primary teacher for their children and full partners in the education of their children.\n**(C)**\nParent literacy training that leads to economic self-sufficiency and financial literacy.\n**(D)**\nA developmentally-appropriate education to prepare children for success in school and life experiences.\n**(5) Qualified applicant**\nThe term qualified applicant means a State government, Tribal government, local government, State educational agency, State humanities council, State service commission, public library, local educational agency, public school, juvenile justice facility, community-based organization, nonprofit organization, or a consortium of such entities, that works with children and has a demonstrated record of promoting literacy for infants, toddlers, children, and young adults for not less than 1 year.\n**(6) Qualified literacy materials**\nThe term qualified literacy materials \u2014\n**(A)**\nmeans any developmentally-appropriate, culturally relevant, and accessible print or digital content\u2014\n**(i)**\ndesigned to support literacy development in infants, toddlers, children, or young adults; and\n**(ii)**\nwhich may be provided in English or any other language; and\n**(B)**\nmay include\u2014\n**(i)**\nstorybooks, chapter books, graphic novels, and picture books;\n**(ii)**\nmulti-lingual and dual-language materials;\n**(iii)**\nbooks in accessible formats, such as braille and large print;\n**(iv)**\ncomics, newspapers, magazines, poetry, play scripts, and encyclopedias;\n**(v)**\neducational brochures and printed media intended to support language acquisition, vocabulary building, and reading comprehension;\n**(vi)**\ndigital materials and e-books that can be accessible offline; and\n**(vii)**\nreading-level-appropriate content reflecting diverse cultures, experiences, and voices.\n**(7) Secretary**\nThe term Secretary means the Secretary of Education.\n#### 4. Open Books, Open Doors Grant Program\n##### (a) Establishment\n**(1) In general**\nThe Secretary shall award grants, on a competitive basis, to qualified applicants to help promote child literacy.\n**(2) Funding allocations**\nThe Secretary shall allocate funds appropriated to carry out this Act for a fiscal year as follows:\n**(A)**\nNot less than 70 percent of the funds shall be awarded as grants to qualified applicants located within, or that coordinate or provide services to, communities within book deserts and that collaborate with\u2014\n**(i)**\nbarbershops or salons;\n**(ii)**\nhouses of worship;\n**(iii)**\ncommunity centers;\n**(iv)**\nchildcare centers;\n**(v)**\nHead Start or Early Head Start centers;\n**(vi)**\nlaundromats;\n**(vii)**\nprimary care providers, community health centers, health clinics, and urgent care centers;\n**(viii)**\na local entity providing services under the special supplemental nutrition program for women, infants, and children established under section 17 of the Child Nutrition Act of 1966 ( 42 U.S.C. 1786 );\n**(ix)**\nindependent bookstores;\n**(x)**\nyouth-serving organizations;\n**(xi)**\ndirect mail programs;\n**(xii)**\nfamily literacy programs; or\n**(xiii)**\nother highly trafficked places, as designated by the Secretary.\n**(B)**\n15 percent of the funds shall be awarded as grants to qualified applicants for early screening, early intervention, and educator training related to children with learning disabilities\u2014\n**(i)**\nwhich shall\u2014\n**(I)**\ncomplement funding awarded under the Individuals with Disabilities Education Act ( 20 U.S.C. 1401 et seq. );\n**(II)**\nsupport programs that are developmentally-appropriate, non-punitive, and followed by family communication and support, not identification alone; and\n**(III)**\nsupport programs that do not stigmatize or over-pathologize early readers; and\n**(ii)**\npriority for which shall be to qualified applicants serving areas where the rate of reading disabilities or the rate of dyslexia screening or identification, is higher than the national average.\n**(C)**\n**(i)**\nNot less than 8 percent of the funds shall be awarded as grants to qualified applicants proposing to develop, pilot, or scale promising strategies that expand access to books, promote reading engagement, or enhance literacy instruction and family literacy, of which\u2014\n**(I)**\nnot less than 25 percent shall be awarded to qualified applicants that are small entities or community-based organizations or pilot programs serving not more than 5,000 children; and\n**(II)**\nnot less than 25 percent shall be awarded to qualified applicants that conduct family literacy programs;\n**(ii)**\nRecipients of grants under clause (i) shall participate in an evaluation process as determined by the Secretary to assess effectiveness, scalability, and alignment with the purpose of this Act.\n**(iii)**\nThe Secretary shall publish and disseminate findings, toolkits, or case studies from strategies developed, piloted, or scaled under this paragraph to qualified applicants, State agencies, educators, and the general public to encourage replication or continuous improvement.\n**(D)**\nNot more than 5 percent of the funds may be used for technical assistance and capacity building, including for regional hubs or intermediary nonprofit organizations to provide coaching, help convene grantees, or share best practices.\n**(E)**\nNot more than 3 percent of the funds may be used to support public engagement or awareness campaigns, including supporting national or regional campaigns to promote reading habits, funding public service announcements, digital ads, or toolkits for local partners, and conducting special campaigns for reading in non-English languages or within immigrant or refugee communities.\n**(F)**\nNot more than 3 percent of the funds may be used to support disaster-impacted areas, as defined by the Federal Emergency Management Agency.\n##### (b) Applications\nA qualified applicant that desires to receive a grant under this Act shall submit an application to the Secretary at such a time, in such manner, and containing such information as the Secretary may require, including the following:\n**(1)**\nA description of the educational and financial need of the community to be served by the qualified applicant.\n**(2)**\nA description of how the qualified applicant would partner with local publishers, businesses, libraries, or other stakeholders to raise additional funds to carry out grant activities and increase book donations.\n**(3)**\nA description of how the qualified applicant would conduct outreach to marginalized and underserved communities to understand their literacy needs.\n**(4)**\nA sustainability plan for how the qualified applicant will continue to promote child literacy after the grant period ends.\n**(5)**\nA description on how the qualified applicant will, where appropriate, partner with or procure qualified literacy materials through local businesses as a way to support local economies.\n**(6)**\nA description of how the qualified applicant will deliver, or collaborate with partners already engaged in, evidence-based literacy programs.\n##### (c) Grant activities\n**(1) In general**\nA qualified applicant that receives a grant under this Act shall use the grant funds for at least one of the following:\n**(A)**\nPurchasing or renting property to construct and maintain distribution facilities for qualified literacy materials.\n**(B)**\nEstablishing new literacy centers, book-exchange boxes, neighborhood libraries, mobile libraries, and book banks.\n**(C)**\nPurchasing and transporting qualified literacy materials or hosting book drives.\n**(D)**\nConducting in person programs and utilizing digital and online tools that promote literacy, adult engagement, and reading comprehension.\n**(E)**\nEliminating or waiving late fees at public and school-based libraries.\n**(F)**\nFacilitating community or cultural events that promote literacy and family literacy.\n**(G)**\nImplementing universal early screening and diagnostic or identification tools for learning disabilities, such as dyslexia, including training for staff on identifying and supporting students with reading disabilities.\n**(H)**\nPurchasing screening tools and providing follow-up assessments and referrals in collaboration with local educational agencies or community health providers.\n**(I)**\nHiring, paying, and training (including coaching) educators, volunteers, health care professionals, caretakers, and parents in evidence-based literacy programs.\n**(J)**\nProviding meals or transportation services for individuals receiving services in any of the activities described in this subsection.\n**(2) Administrative cap**\n**(A) Nonpublic entity**\nA qualified applicant that is a non public entity and receives a grant under this Act may use not more than 25 percent of the grant funds on operating expenses, including salaries, utilities, equipment, and supplies, unless the Secretary approves a waiver of such cap.\n**(B) Public entity**\nA qualified applicant that is a public entity and receives a grant under this Act may use not more than 25 percent of the grant funds on operating expenses, including salaries, utilities, equipment, and supplies, unless the Secretary approves a waiver of such cap.\n##### (d) Maintenance of effort\nA qualified applicant may receive grant funds for a fiscal year only if the Secretary finds that the expenditures of the qualified applicant on literacy efforts for the preceding fiscal year were not less than the expenditures of the qualified applicant on literacy efforts for the second preceding fiscal year.\n##### (e) Matching requirements\n**(1) In general**\nEach qualified applicant that receives a grant under this Act shall provide, from non-Federal sources, an amount equal to 25 percent of the amount of the grant to carry out activities supported by the grant.\n**(2) Waiver**\nThe Secretary may waive the requirement under paragraph (1) when determined appropriate by the Secretary.\n#### 5. Reporting requirements\nNot later than 2 years after the date of enactment of this Act, and annually thereafter, the Secretary shall submit to the Committee on Health, Education, Labor, and Pensions and the Committee on Appropriations of the Senate and the Committee on Education and Workforce and the Committee on Appropriations of the House of Representatives, a report containing the following information for each grantee:\n**(1)**\nA breakdown of the number of students served through grant activities and relevant demographics (including socioeconomic status, race, age, and disability status) in each grade that is participating in the program carried out with grant funds.\n**(2)**\nState assessment data or other validated literacy engagement scales, on a biannual basis, for local educational agencies that receive support under the grant.\n**(3)**\nSurvey responses from teachers and parents measuring the impact increased access to books is having on children's reading enthusiasm and confidence.\n**(4)**\nThe number of books per child before and after the program carried out with grant funds and the number of caregivers participating in the program.\n#### 6. Interagency collaboration\n##### (a) In general\nTo ensure implementation and maximize the impact of the grant program established under this Act, the Secretary shall coordinate with relevant Federal agencies, including\u2014\n**(1)**\nthe Corporation for National and Community Services;\n**(2)**\nthe Food and Nutrition Service of the Department of Agriculture;\n**(3)**\nthe Department of Health and Human Services, including the Health Resources and Services Administration, the Maternal and Child Health Bureau, and the Office of Head Start;\n**(4)**\nthe Department of Housing and Urban Affairs;\n**(5)**\nthe Department of Labor;\n**(6)**\nthe Office of Juvenile Justice and Delinquency Prevention of the Department of Justice;\n**(7)**\nthe Federal Communications Commission;\n**(8)**\nthe Institute of Museum and Library Services; and\n**(9)**\nthe National Endowment for the Humanities.\n##### (b) Activities\nThe coordination required under subsection (a) shall include\u2014\n**(1)**\naligning literacy efforts with existing Federal early childhood, education, health, and community development programs;\n**(2)**\nsharing data and best practices to identify geographic areas of greatest need;\n**(3)**\nensuring consistent messaging and outreach to families across federally supported platforms;\n**(4)**\nencouraging joint applications and cross-sector partnerships among grantees supported by multiple agencies; and\n**(5)**\nidentifying opportunities for co-location or integration of literacy services in federally supported housing, health, education, and nutrition programs.\n##### (c) Interagency working group\n**(1) In general**\nNot later than 180 days after the date of enactment of this Act, the Secretary shall establish an interagency working group to support implementation of this Act.\n**(2) Meeting frequency**\nThe working group shall meet not less often than twice annually.\n**(3) Report and national strategy**\nThe working group shall\u2014\n**(A)**\nsubmit an interagency coordination report to Congress every 2 years outlining shared initiatives, challenges, and recommendations to strengthen Federal literacy programming; and\n**(B)**\ncreate and develop a national strategy to promote literacy among young children from birth to age 5, school-aged children from kindergarten to 12th grade, and young adults.\n#### 7. Rule of construction\nNothing in this Act shall be construed to authorize the Secretary to ban or censor materials or otherwise influence local curricular or content decisions based on political or viewpoint grounds.\n#### 8. Federal Clearinghouse on Book Access\n##### (a) Establishment\nThe Secretary, in coordination with each of the Federal agencies listed in section 6(a), shall establish a Federal Clearinghouse on Book Access that shall\u2014\n**(1)**\nidentify, collect, and evaluate evidence-based strategies, programs, and interventions that have been shown to have a significant effect on children accessing qualified literacy materials and improving literacy outcomes for children and families living in book deserts; and\n**(2)**\nprovide guidance, toolkits, and technical resources to States, local educational agencies, health professionals, libraries, and nonprofit organizations seeking to expand book access in book deserts.\n##### (b) Information To include\nThe Federal Clearinghouse on Book Access shall ensure the guidance, toolkits, and technical resources provided under subsection (a) include, to the extent practicable, the following information:\n**(1)**\nThe strength of the evidence that the guidance, toolkit, or technical resource expands book access and increases literacy outcomes.\n**(2)**\nThe populations that were served in the programs that are the bases for the guidance, toolkit, or technical resource, along with where the populations are located, such as urban, suburban, or rural areas.\n**(3)**\nImplementation models for the programs described in paragraph (2), such as whether the programs were school-based, library-based, health care-based, or community-based approaches.\n**(4)**\nCost considerations of implementation.\n**(5)**\nDemonstrated literacy outcomes in the programs described in paragraph (2).\n**(6)**\nFindings and data from previous Federal or State commissions recommending improvements to book access and increasing literacy outcomes.\n**(7)**\nOther supportive evidence or findings relied upon by the Clearinghouse, in consultation with Federal agencies listed in section 6(a), in identifying evidence-based strategies, programs, and interventions, as described in subsection (a)(1).\n##### (c) Consistency with civil rights\nThe guidance, toolkits, and technical resources provided by the Clearinghouse shall be consistent with Federal civil rights laws, including title II of the Americans with Disabilities Act of 1990 ( 42 U.S.C. 12131 et seq. ), the Rehabilitation Act of 1973 ( 29 U.S.C. 701 et seq. ), and title VI of the Civil Rights Act of 1964 ( 42 U.S.C. 2000d et seq. ).\n##### (d) Consultation\nIn identifying the evidence-based strategies, programs, and interventions for the Federal Clearinghouse on Book Access, the Secretary shall consult with\u2014\n**(1)**\nliteracy researchers and experts; and\n**(2)**\nState educational agencies, local educational agencies, early childhood education providers, community-based and nonprofit literacy groups focused on book access and literacy development, libraries, health providers, educators, and school administrators.\n##### (e) Administration\n**(1) In general**\nThe Federal Clearinghouse on Book Access shall be assigned such personnel and resources as the Secretary considers appropriate to carry out this section.\n**(2) Detail**\nThe heads of each of the Federal agencies listed in section 6(a) may detail personnel to the Federal Clearinghouse on Book Access.\n##### (f) Production and publication of materials\nThe Secretary may produce and publish materials identified, collected, and evaluated by the Federal Clearinghouse on Book Access to assist and train early childhood, educational, health care, law enforcement, and workforce agencies on the implementation of the evidence-based strategies, programs, and interventions for literacy development and enhancing access to books.\n##### (g) Collection of data, feedback, and evaluations\nFor the purpose of continuous improvement of the Federal Clearinghouse on Book Access, the Secretary shall collect\u2014\n**(1)**\nClearinghouse data analytics;\n**(2)**\nuser feedback on the implementation of evidence-based strategies, programs, and interventions identified by the Clearinghouse; and\n**(3)**\nany evaluations conducted on implementation of the evidence-based strategies, programs, and interventions.\n##### (h) Rule of construction\nNothing in this section shall be construed to require State educational agencies or local educational agencies to adopt the evidence-based strategies, programs, and interventions identified pursuant to subsection (a).\n#### 9. Authorization of appropriations\n##### (a) In general\nThere is authorized to be appropriated to carry out this Act $100,000,000 for each of fiscal years 2026 through 2031.\n##### (b) Supplemental appropriations\nThe Secretary may request supplemental appropriations based on demand for literacy services.",
      "versionDate": "2026-03-09",
      "versionType": "Introduced in Senate"
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
        "updateDate": "2026-03-26T18:16:57Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4028is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Open Books, Open Doors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T03:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Open Books, Open Doors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-21T03:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to expand equitable access to developmentally-appropriate literacy materials, programs, and family engagement in reading, especially in underserved communities, and strengthen the connection between literacy and long-term academic and economic success.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-21T03:48:28Z"
    }
  ]
}
```
