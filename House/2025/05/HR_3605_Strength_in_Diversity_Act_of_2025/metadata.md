# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3605?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3605
- Title: Strength in Diversity Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3605
- Origin chamber: House
- Introduced date: 2025-05-23
- Update date: 2026-04-23T08:07:27Z
- Update date including text: 2026-04-23T08:07:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-23: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-23: Introduced in House

## Actions

- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Introduced in House
- 2025-05-23 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-23",
    "latestAction": {
      "actionDate": "2025-05-23",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3605",
    "number": "3605",
    "originChamber": "House",
    "policyArea": {
      "name": "Education"
    },
    "sponsors": [
      {
        "bioguideId": "S000185",
        "district": "3",
        "firstName": "Robert",
        "fullName": "Rep. Scott, Robert C. \"Bobby\" [D-VA-3]",
        "lastName": "Scott",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Strength in Diversity Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-23T08:07:27Z",
    "updateDateIncludingText": "2026-04-23T08:07:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-23",
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
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-23",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-23",
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
          "date": "2025-05-23T14:03:00Z",
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
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "WA"
    },
    {
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "OR"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "GA"
    },
    {
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001231",
      "district": "12",
      "firstName": "Lateefah",
      "fullName": "Rep. Simon, Lateefah [D-CA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "OH"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MS"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "Cleo",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Fields",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "LA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MI"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "True",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "IL"
    },
    {
      "bioguideId": "G000559",
      "district": "8",
      "firstName": "John",
      "fullName": "Rep. Garamendi, John [D-CA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Garamendi",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "TX"
    },
    {
      "bioguideId": "W000187",
      "district": "43",
      "firstName": "Maxine",
      "fullName": "Rep. Waters, Maxine [D-CA-43]",
      "isOriginalCosponsor": "True",
      "lastName": "Waters",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NY"
    },
    {
      "bioguideId": "R000617",
      "district": "3",
      "firstName": "Delia",
      "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Ramirez",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "IL"
    },
    {
      "bioguideId": "O000173",
      "district": "5",
      "firstName": "Ilhan",
      "fullName": "Rep. Omar, Ilhan [D-MN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Omar",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "MN"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "CA"
    },
    {
      "bioguideId": "C001067",
      "district": "9",
      "firstName": "Yvette",
      "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clarke",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NY"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-05-23",
      "state": "NY"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-06-06",
      "state": "GA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "C001066",
      "district": "14",
      "firstName": "Kathy",
      "fullName": "Rep. Castor, Kathy [D-FL-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Castor",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "FL"
    },
    {
      "bioguideId": "F000462",
      "district": "22",
      "firstName": "Lois",
      "fullName": "Rep. Frankel, Lois [D-FL-22]",
      "isOriginalCosponsor": "False",
      "lastName": "Frankel",
      "party": "D",
      "sponsorshipDate": "2025-07-14",
      "state": "FL"
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
      "sponsorshipDate": "2025-07-14",
      "state": "NY"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2025-08-29",
      "state": "PA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-09-08",
      "state": "IL"
    },
    {
      "bioguideId": "H001081",
      "district": "5",
      "firstName": "Jahana",
      "fullName": "Rep. Hayes, Jahana [D-CT-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hayes",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3605ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3605\nIN THE HOUSE OF REPRESENTATIVES\nMay 23, 2025 Mr. Scott of Virginia (for himself, Ms. Jayapal , Ms. Bonamici , Mrs. McBath , Ms. Vel\u00e1zquez , Ms. Simon , Mrs. Beatty , Mr. Thompson of Mississippi , Mr. Fields , Ms. Tlaib , Mr. Takano , Mr. Davis of Illinois , Mr. Garamendi , Ms. Garcia of Texas , Ms. Waters , Mr. Latimer , Mrs. Ramirez , Ms. Omar , Mr. DeSaulnier , Ms. Clarke of New York , and Mr. Meeks ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo establish the Strength in Diversity Program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Strength in Diversity Act of 2025 .\n#### 2. Purpose\nThe purpose of this Act is to support the development, implementation, and evaluation of comprehensive strategies to address the effects of racial isolation or concentrated poverty by increasing diversity, including racial diversity and socioeconomic diversity, in covered schools.\n#### 3. Reservation for national and State activities\n##### (a) National activities\nThe Secretary may reserve not more than 5 percent of the amounts made available under section 9 for a fiscal year to carry out activities of national significance relating to this Act, which may include\u2014\n**(1)**\nresearch, development, data collection, monitoring, technical assistance, evaluation, or dissemination activities; and\n**(2)**\nthe development and maintenance of best practices for recipients of grants under section 4 and other experts in the field of school diversity.\n##### (b) State activities\nThe Secretary may reserve not more than 10 percent of the amounts made available under section 9 for a fiscal year for planning grants and implementation grants made to State educational agencies under section 4.\n#### 4. Grant program authorized\n##### (a) Authorization\n**(1) In general**\nFrom the amounts made available under section 9 and not reserved under section 3 for a fiscal year, the Secretary shall award grants in accordance with subsection (b) to eligible entities to develop or implement plans to improve diversity and reduce or eliminate racial or socioeconomic isolation in covered schools.\n**(2) Types of grants**\nThe Secretary may, in any fiscal year, award\u2014\n**(A)**\nplanning grants to carry out the activities described in section 6(a);\n**(B)**\nimplementation grants to carry out the activities described in section 6(b); or\n**(C)**\nboth such planning grants and implementation grants.\n##### (b) Award basis\n**(1) Criteria for evaluating applications**\nThe Secretary shall award grants under this section on a competitive basis, based on\u2014\n**(A)**\nthe quality of the application submitted by an eligible entity under section 5;\n**(B)**\nthe likelihood, as determined by the Secretary, that the eligible entity will use the grant to improve student outcomes or outcomes on other performance measures described in section 7; and\n**(C)**\nthe likelihood that the grant will lead to a meaningful reduction in racial and economic isolation for children in covered schools.\n**(2) Priority**\nIn awarding grants under this section, the Secretary shall give priority to the following eligible entities:\n**(A)**\nFirst, to an eligible entity that proposes, in an application submitted under section 5, to use the grant to support a program that addresses racial isolation.\n**(B)**\nSecond, to an eligible entity that proposes, in an application submitted under section 5, to use the grant to support a program that extends beyond one local educational agency, such as an inter-district or regional program.\n**(C)**\nThird, to an eligible entity that demonstrates meaningful coordination with local housing agencies and transportation departments to increase access to schools that have a disproportionately low number of low-income students.\n##### (c) Duration of grants\n**(1) Planning grant**\nA planning grant awarded under this section shall be for a period of not more than 2 years.\n**(2) Implementation grant**\nAn implementation grant awarded under this section shall be for a period of not more than 3 years, except that the Secretary may extend an implementation grant for an additional 2-year period if the eligible entity receiving the grant demonstrates to the Secretary that the eligible entity is making significant progress, as determined by the Secretary, on the program performance measures described in section 7.\n#### 5. Applications\nIn order to receive a grant under section 4, an eligible entity shall submit an application to the Secretary at such time and in such manner as the Secretary may require. Such application shall include\u2014\n**(1)**\na description of the program for which the eligible entity is seeking a grant, including\u2014\n**(A)**\nhow the eligible entity proposes to use the grant to improve the academic and life outcomes of students in racial or socioeconomic isolation in covered schools by supporting interventions that increase diversity for students in such covered schools;\n**(B)**\nin the case of an implementation grant, the implementation grant plan described in section 6(b)(1); and\n**(C)**\nevidence, or if such evidence is not available, a rationale based on current research, regarding how the program will increase diversity;\n**(2)**\nin the case of an eligible entity proposing to use any of the grant to benefit covered schools that are racially isolated, a description of how the eligible entity will identify and define racial isolation;\n**(3)**\nin the case of an eligible entity proposing to use any portion of the grant to benefit high-poverty covered schools, a description of how the eligible entity will identify and define income level and socioeconomic status;\n**(4)**\na description of the plan of the eligible entity for continuing the program after the grant period ends;\n**(5)**\na description of how the eligible entity will assess, monitor, and evaluate the impact of the activities funded under the grant on student achievement and student enrollment diversity, and teacher diversity;\n**(6)**\nan assurance that the eligible entity has conducted, or will conduct, robust parent and community engagement, while planning for and implementing the program, such as through\u2014\n**(A)**\nconsultation with appropriate officials from Indian Tribes or Tribal organizations approved by the Tribes located in the area served by the eligible entity;\n**(B)**\nconsultation with other community entities, including local housing or transportation authorities;\n**(C)**\npublic hearings or other open forums to inform the development of any formal strategy to increase diversity; and\n**(D)**\noutreach to parents and students, in a language that parents and students can understand, and consultation with students and families in the targeted district or region that is designed to ensure participation in the planning and development of any formal strategy to increase diversity;\n**(7)**\nan estimate of the number of students that the eligible entity plans to serve under the program and the number of students to be served through additional expansion of the program after the grant period ends;\n**(8)**\nan assurance that the eligible entity will\u2014\n**(A)**\ncooperate with the Secretary in evaluating the program, including any evaluation that might require data and information from multiple recipients of grants under section 4; and\n**(B)**\nengage in the best practices developed under section 3(a)(2);\n**(9)**\nan assurance that, to the extent possible, the eligible entity has considered the potential implications of the grant activities on the demographics and student enrollment of nearby covered schools not included in the activities of the grant;\n**(10)**\nin the case of an eligible entity applying for an implementation grant, a description of how the eligible entity will\u2014\n**(A)**\nimplement, replicate, or expand a strategy based on a strong or moderate level of evidence (as described in subclause (I) or (II) of section 8101(21)(A)(i) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801(21)(A)(i) )); or\n**(B)**\ntest a promising strategy to increase diversity in covered schools;\n**(11)**\nin the case of an application by a consortium of local educational agencies, a specification of which agency is the lead applicant, and how the grant funds will be divided among the school districts served by such consortium; and\n**(12)**\nin the case of an application by a State educational agency, a demonstration that the agency has procedures in place\u2014\n**(A)**\nto assess and prevent the redrawing of school district lines in a manner that increases racial or socioeconomic isolation;\n**(B)**\nto assess the segregation impacts of new school construction proposals and to prioritize school construction funding that will foreseeably increase racial and economic integration; and\n**(C)**\nto include progress toward reduction of racial and economic isolation as a factor in the reports required under section 1111(h) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(h) ).\n#### 6. Uses of funds\n##### (a) Planning grants\nEach eligible entity that receives a planning grant under section 4 shall use the grant to support students in covered schools through the following activities:\n**(1)**\nCompleting a comprehensive assessment of, with respect to the geographic area served by such eligible entity\u2014\n**(A)**\nthe educational outcomes and racial and socioeconomic stratification of children attending covered schools;\n**(B)**\nan analysis of the location and capacity of program and school facilities and the adequacy of local or regional transportation infrastructure; and\n**(C)**\nteacher diversity in covered schools, and plans for expanding teacher diversity.\n**(2)**\nDeveloping and implementing a robust family, student, and community engagement plan, including, where feasible, public hearings or other open forums that would precede and inform the development of a formal strategy to improve diversity in covered schools.\n**(3)**\nDeveloping options, including timelines and cost estimates, for improving diversity in covered schools, such as weighted lotteries, revised feeder patterns, school boundary redesign, or regional coordination.\n**(4)**\nDeveloping an implementation plan based on community preferences among the options developed under paragraph (3).\n**(5)**\nBuilding the capacity to collect and analyze data that provide information for transparency, continuous improvement, and evaluation.\n**(6)**\nDeveloping an implementation plan to comply with a court-ordered school desegregation plan.\n**(7)**\nEngaging in best practices developed under section 3(a)(2).\n**(8)**\nIf applicable, developing an implementation plan to replace entrance exams or other competitive application procedures with methods of student assignment to promote racial and socioeconomic diversity.\n##### (b) Implementation grants\n**(1) Implementation grant plan**\nEach eligible entity that receives an implementation grant under section 4 shall implement a high-quality plan to support students in covered schools that includes\u2014\n**(A)**\na comprehensive set of strategies designed to improve academic outcomes for all students, particularly students of color and low-income students, by increasing diversity in covered schools;\n**(B)**\nevidence of strong family and community support for such strategies, including evidence that the eligible entity has engaged in meaningful family and community outreach activities;\n**(C)**\ngoals to increase diversity, including teacher diversity, in covered schools over the course of the grant period;\n**(D)**\ncollection and analysis of data to provide transparency and support continuous improvement throughout the grant period; and\n**(E)**\na rigorous method of evaluation of the effectiveness of the program.\n**(2) Implementation grant activities**\nEach eligible entity that receives an implementation grant under section 4 may use the grant to carry out one or more of the following activities:\n**(A)**\nRecruiting, hiring, or training additional teachers, administrators, school counselors, and other instructional and support staff in new, expanded, or restructured covered schools, or other professional development activities for staff and administrators.\n**(B)**\nInvesting in specialized academic programs or facilities designed to encourage inter-district school attendance patterns.\n**(C)**\nDeveloping or initiating a transportation plan for bringing students to and from covered schools, if such transportation is sustainable beyond the grant period and does not represent a significant portion of the grant received by an eligible entity under section 4.\n**(D)**\nDeveloping innovative and equitable school assignment plans.\n**(E)**\nCarrying out innovative activities designed to increase racial and socioeconomic school diversity and engagement between children from different racial, economic, and cultural backgrounds.\n**(F)**\nCreating or improving systems and partnerships to create a one-stop enrollment process for students with multiple public school options, including making school information and data more accessible and easy to understand, in order to ensure access to low poverty or high-performing schools for low-income children and to promote racial and socioeconomic diversity.\n**(G)**\nIncreasing teacher diversity in covered schools.\n#### 7. Performance measures\nThe Secretary shall establish performance measures for the programs and activities carried out through a grant under section 4. These measures, at a minimum, shall track the progress of each eligible entity in\u2014\n**(1)**\nimproving academic and other developmental or noncognitive outcomes for each subgroup described in section 1111(b)(2)(B)(xi) of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 6311(b)(2)(B)(xi) ) that is served by the eligible entity on measures, including, as applicable, by\u2014\n**(A)**\nincreasing school readiness;\n**(B)**\nincreasing student achievement and decreasing achievement gaps;\n**(C)**\nincreasing high school graduation rates;\n**(D)**\nincreasing readiness for postsecondary education and careers;\n**(E)**\nimproving access to mental health and social-emotional learning;\n**(F)**\nreducing school discipline rates; and\n**(G)**\nany other indicator the Secretary or eligible entity may identify; and\n**(2)**\nincreasing diversity and decreasing racial or socioeconomic isolation in covered schools.\n#### 8. Annual reports\nAn eligible entity that receives a grant under section 4 shall submit to the Secretary, at such time and in such manner as the Secretary may require, an annual report that includes\u2014\n**(1)**\na description of the efforts of the eligible entity to increase racial and socioeconomic diversity;\n**(2)**\ninformation on the progress of the eligible entity with respect to the performance measures described in section 7;\n**(3)**\nthe data supporting such progress;\n**(4)**\na description of how the eligible entity will continue to make improvements toward increasing diversity and decreasing racial or socioeconomic isolation in covered schools and sustaining inclusion; and\n**(5)**\ninformation on the progress of regional programs on reducing racial and socioeconomic isolation in covered schools, if applicable.\n#### 9. Authorization of appropriations\nThere are authorized to be appropriated to carry out this Act such sums as may be necessary for fiscal year 2025 and each of the 5 succeeding fiscal years.\n#### 10. Definitions\nIn this Act:\n**(1) Covered school**\nThe term covered school means\u2014\n**(A)**\na publicly-funded early childhood education program;\n**(B)**\na public elementary school; or\n**(C)**\na public secondary school.\n**(2) Eligible entity**\nThe term eligible entity means a State educational agency, a local educational agency, a consortium of such agencies, an educational service agency, or a regional educational agency that at the time of the application of such eligible entity has significant achievement gaps and socioeconomic or racial segregation within or between the school districts served by such entity.\n**(3) ESEA terms**\nThe terms educational service agency , elementary school , local educational agency , secondary school , Secretary , and State educational agency have the meanings given such terms in section 8101 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7801 ).\n**(4) Publicly-funded early childhood education program**\nThe term publicly-funded early childhood education program means an early childhood education program (as defined in section 103(8) of the Higher Education Act of 1965 ( 20 U.S.C. 1003(8) )) that receives State or Federal funds.\n#### 11. Prohibition against Federal control of education\nNo provision of this Act shall be construed to authorize any department, agency, officer, or employee of the United States to exercise any direction, supervision, or control over the curriculum, program of instruction, administration, or personnel of any educational institution, school, or school system.",
      "versionDate": "2025-05-23",
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
        "name": "Education",
        "updateDate": "2025-06-12T14:59:52Z"
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
      "date": "2025-05-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3605ih.xml"
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
      "title": "Strength in Diversity Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-03T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Strength in Diversity Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-03T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Strength in Diversity Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-03T04:33:41Z"
    }
  ]
}
```
