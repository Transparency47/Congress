# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3131?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3131
- Title: Community Services Block Grant Improvement Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3131
- Origin chamber: House
- Introduced date: 2025-05-01
- Update date: 2026-03-03T21:50:48Z
- Update date including text: 2026-03-03T21:50:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-01: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-05-01: Introduced in House

## Actions

- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Introduced in House
- 2025-05-01 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-01",
    "latestAction": {
      "actionDate": "2025-05-01",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3131",
    "number": "3131",
    "originChamber": "House",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Community Services Block Grant Improvement Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-03T21:50:48Z",
    "updateDateIncludingText": "2026-03-03T21:50:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-01",
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
      "actionDate": "2025-05-01",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-01",
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
          "date": "2025-05-01T13:05:15Z",
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
      "bioguideId": "B001278",
      "district": "1",
      "firstName": "Suzanne",
      "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bonamici",
      "party": "D",
      "sponsorshipDate": "2025-05-01",
      "state": "OR"
    },
    {
      "bioguideId": "R000395",
      "district": "5",
      "firstName": "Harold",
      "fullName": "Rep. Rogers, Harold [R-KY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rogers",
      "party": "R",
      "sponsorshipDate": "2025-05-06",
      "state": "KY"
    },
    {
      "bioguideId": "D000623",
      "district": "10",
      "firstName": "Mark",
      "fullName": "Rep. DeSaulnier, Mark [D-CA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "DeSaulnier",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "CA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "M001233",
      "district": "8",
      "firstName": "Mark",
      "fullName": "Rep. Messmer, Mark B. [R-IN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Messmer",
      "middleName": "B.",
      "party": "R",
      "sponsorshipDate": "2025-05-14",
      "state": "IN"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "False",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "TX"
    },
    {
      "bioguideId": "T000491",
      "district": "45",
      "firstName": "Derek",
      "fullName": "Rep. Tran, Derek [D-CA-45]",
      "isOriginalCosponsor": "False",
      "lastName": "Tran",
      "party": "D",
      "sponsorshipDate": "2025-06-13",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "IL"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-06-20",
      "state": "CA"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "TX"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-06-25",
      "state": "CA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "DE"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-07-02",
      "state": "NJ"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "NE"
    },
    {
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-07-21",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2025-07-23",
      "state": "IN"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "IL"
    },
    {
      "bioguideId": "S001211",
      "district": "4",
      "firstName": "Greg",
      "fullName": "Rep. Stanton, Greg [D-AZ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Stanton",
      "party": "D",
      "sponsorshipDate": "2025-08-05",
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
      "sponsorshipDate": "2025-08-15",
      "state": "IL"
    },
    {
      "bioguideId": "M001241",
      "district": "47",
      "firstName": "Dave",
      "fullName": "Rep. Min, Dave [D-CA-47]",
      "isOriginalCosponsor": "False",
      "lastName": "Min",
      "party": "D",
      "sponsorshipDate": "2025-08-26",
      "state": "CA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "MI"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-09-15",
      "state": "TX"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-16",
      "state": "VA"
    },
    {
      "bioguideId": "R000579",
      "district": "18",
      "firstName": "Patrick",
      "fullName": "Rep. Ryan, Patrick [D-NY-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Ryan",
      "party": "D",
      "sponsorshipDate": "2025-09-17",
      "state": "NY"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-09-26",
      "state": "PA"
    },
    {
      "bioguideId": "T000460",
      "district": "4",
      "firstName": "Mike",
      "fullName": "Rep. Thompson, Mike [D-CA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-11-04",
      "state": "MN"
    },
    {
      "bioguideId": "C001059",
      "district": "21",
      "firstName": "Jim",
      "fullName": "Rep. Costa, Jim [D-CA-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Costa",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-11-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001205",
      "district": "1",
      "firstName": "Carol",
      "fullName": "Rep. Miller, Carol D. [R-WV-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Miller",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2026-01-12",
      "state": "WV"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3131ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3131\nIN THE HOUSE OF REPRESENTATIVES\nMay 1, 2025 Mr. Thompson of Pennsylvania (for himself and Ms. Bonamici ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend and reauthorize the Community Services Block Grant Act.\n#### 1. Short title\nThis Act may be cited as the Community Services Block Grant Improvement Act of 2025 .\n#### 2. Purposes and goals\nSection 672(1) of the Community Services Block Grant Act ( 42 U.S.C. 9901(1) ) is amended to read as follows:\n(1) to reduce poverty in the United States by supporting the activities of community action agencies and other community services network organizations that improve the economic security of low-income and working individuals and families, empower them to become fully sufficient, and create new economic opportunities in the communities where they live; and .\n#### 3. Definitions\nSection 673 of the Community Services Block Grant Act ( 42 U.S.C. 9902 ) is amended by striking paragraphs (1) through (5), and inserting the following:\n(1) Agency-wide strategic plan The term agency-wide strategic plan means a plan that has been adopted by an eligible entity in the previous 5 years and establishes goals that include meeting needs identified by the entity in consultation with residents of the community through a process of comprehensive community needs assessment. (2) Poverty line (A) In general The term poverty line means the official poverty guideline calculated by the Secretary from the most recent data available from the Bureau of the Census. The Secretary shall revise the poverty line annually (or at any shorter interval the Secretary determines to be feasible and desirable). The required revision shall be accomplished by multiplying the official poverty thresholds from the Bureau of the Census by the percentage change in the Consumer Price Index for All Urban Consumers during the annual or other interval immediately preceding the time at which the revision is made. .\n**(B) Eligibility criterion**\n200 percent of the poverty line shall be used as a criterion of eligibility for services, assistance, or resources provided directly to individuals or families through the grant program established under this subtitle.\n(3) Community action agency The term community action agency means an eligible entity (which meets the requirements of paragraph (1) or (2), as appropriate, of section 676B) that delivers multiple programs, projects, and services to a variety of low-income individuals and families. (4) Community action plan The term community action plan means a detailed plan, including a budget, that is adopted by an eligible entity, for expenditures of funds appropriated for a fiscal year under this subtitle for the activities supported directly or indirectly by such funds. (5) Community services network organization The term community services network organization means any of the following organizations funded under this subtitle: (A) A State. (B) An eligible entity. (C) An association with a membership composed primarily of States, eligible entities, or associations of States or eligible entities. (6) Eligible entity The Term eligible entity means an entity that\u2014 (A) is an eligible entity described in section 673(1) (as in effect immediately before the date of the enactment of the Community Services Block Grant Improvement Act of 2025), or has been designated by the process described in section 676A (including an organization serving migrant or seasonal farm workers that is so described or designated); and (B) has a tripartite board described in paragraph (1) or (2), as appropriate, of section 686B. (7) Private, nonprofit organization The term private, nonprofit organization includes a religious organization, to which section 679 applies. (8) Secretary The term Secretary means the Secretary of Health and Human Services. (9) State The term State means each of the several States, the District of Columbia, the Commonwealth of Puerto Rico, Guam, the United States Virgin Islands, American Samoa, and the Commonwealth of the Northern Mariana Islands. .\n#### 4. Authorization of appropriations\nSection 674 of the Community Services Block Grant Act ( 42 U.S.C. 9903 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking such sums as may be necessary for each of fiscal years 1999 through 2003 and inserting $1,000,000,000 for each of fiscal years 2026 through 2032 , and\n**(B)**\nby striking sections 681 and 682 and inserting section 680 ,\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (2)\u2014\n**(i)**\nby striking 1\u00bd percent and inserting 1 percent ,\n**(ii)**\nin subparagraph (A)\u2014\n**(I)**\nby striking entities, and inserting entities and other community services network organizations , and\n**(II)**\nby striking organizations or associations , and\n**(iii)**\nin subparagraph (B) by striking and at the end and inserting a period, and\n**(B)**\nby striking paragraph (3), and\n**(3)**\nby adding at the end the following:\n(c) Discretionary programs There are authorized to be appropriated $40,000,000 to carry out section 680(a)(2) and 680(a)(3) for each of the fiscal years 2026 through 2032. .\n#### 5. Establishment of block grant program\nSection 675 of Community Services Block Grant Act ( 42 U.S.C. 9904 ) is amended by striking through and all that follows through the period at the end, and inserting for the purposes described in section 672. .\n#### 6. Allotments and payments to States\nSection 675B of the Community Services Block Grant Act ( 42 U.S.C. 9906 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking except\u2014 and inserting except as provided in subsection (b). , and\n**(B)**\nby striking paragraphs (1) and (2),\n**(2)**\nby amending subsection (b) to read as follows:\n(b) Minimum allotments (1) In general No State shall receive less than \u00bd of 1 percent of the amount appropriated under section 674(a) for a fiscal year that remains after the Secretary makes the reservations required by section 674(b). (2) Years with greater available funds Notwithstanding paragraph (1), if the amount appropriated under section 674(a) for a fiscal year that remains after the Secretary makes the reservations required in section 674(b) exceeds $900,000,000, no State shall receive under this section less than \u00be of 1 percent of the remaining amount. , and\n**(3)**\nby amending subsection (c) to read as follows::\n(c) Grants and payments Subject to section 677, the Secretary shall make grants to eligible States for the allotments described in subsections (a) and (b). The Secretary shall make payments for the grants in accordance with section 6503(a) of title 31, United States Code. The Secretary shall allocate the amounts allotted under subsections (a) and (b) on a quarterly basis at a minimum, notify the States of their respective allocations, and make each State\u2019s first allocation amount in a fiscal year available for expenditure by the State no later than 30 days after receipt of an approved apportionment from the Office of Management and Budget and, for subsequent allocation amounts in the fiscal year, not later than 30 days after the start of the period for which the Secretary is allocating the funds. .\n#### 7. Uses of funds\nSection 675C of the Community Services Block Grant Act (42 U.S.C.. 9907) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1) by striking for the purposes described in section 672 to eligible entities and inserting to eligible entities that enable the entities to implement programs, projects, and services for the purposes described in section 672 ,\n**(B)**\nby amending paragraph (2) to read as follows:\n(2) Obligational requirements (A) Date of obligation The State shall obligate the funds for grants described in paragraph (1) and make such grants available for expenditure by eligible entities not later than the later of\u2014 (i) the 30th day after the date on which the State receives from the Secretary a notice of funding availability for the State\u2019s application under section 676(b) for a first or subsequent allocation for a fiscal year; or (ii) the first day of the State program year for which funds are to be expended under the State application. (B) Exception If funds are appropriated to carry out this subtitle for less than a full fiscal year, a State may request an exception from the Secretary from the requirement to make grants available for expenditure by eligible entities in accordance with subparagraph (A), except that a State may not accumulate more than one fiscal quarter\u2019s worth of funding without making such funds available for expenditure by eligible entities. (C) Availability Funds distributed to eligible entities through grants made in accordance with paragraph (1) for a fiscal year shall be available for obligation by the eligible entity during that fiscal year and the following fiscal year. , and\n**(C)**\nby striking paragraph (3),\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking (subject to paragraph (2)) for activities that may include\u2014 and inserting for activities described in the State\u2019s application and plan under section 676(b), as described in paragraph (2), and for administrative expenses subject to the limitations in paragraph (3). , and\n**(ii)**\nby striking subparagraphs (A) through (H), and\n**(B)**\nin paragraph (2)\u2014\n**(i)**\nby striking the greater of $55,000, or 5 percent, and inserting 5 percent ,\n**(ii)**\nin the 2d sentence by inserting under section 675B after allotment ,\n**(iii)**\nin the 3d sentence by striking paragraph (1)(A) and inserting paragraph (2), other than monitoring, ,\n**(iv)**\nby striking the last sentence,\n**(v)**\nby redesignating paragraph (2) as paragraph (3), and\n**(vi)**\nby inserting after paragraph (1) the following:\n(2) Training and technical assistance After the application of subsection (a), the State may use the remaining grant funds for the purposes of\u2014 (A) providing training and technical assistance and resources to eligible entities, including to\u2014 (i) assist eligible entities to respond to statewide or regional conditions that create economic insecurity, including emergency conditions; and (ii) support innovative programs and activities conducted by eligible entities for a purpose described in section 672, including assistance to eligible entities in building and using evidence of effectiveness in achieving such purpose; (B) supporting information and communication resources for the comprehensive community needs assessments described in section 676(b)(3)(B); (C) supporting performance measurement systems consistent with the requirements of section 678E; (D) coordinating State-operated programs and services, and at the option of the State, locally-operated programs and services, targeted to low-income children and families with services provided by eligible entities and other organizations funded under this subtitle, to ensure increased access to services provided by such State or local agencies; (E) supporting statewide coordination and communication among eligible entities in the State, including supporting activities of a statewide association of community services network organizations; and (F) analyzing the distribution of funds made available under this subtitle within the State to determine if such funds have been targeted to the areas of greatest need. , and\n**(3)**\nby striking subsection (c).\n#### 8. Application and plan\nSection 676 of the Community Services Block Grant Act ( 42 U.S.C. 9908 ) is amended\u2014\n**(1)**\nin subsection (a) by amending paragraph (2) to read as follows:\n(2) Duties The lead agency\u2014 (A) shall be authorized by the chief executive officer to convene State agencies and coordinate information and activities funded under this subtitle; (B) shall develop the State plan to be submitted to the Secretary under subsection (b), which shall be based primarily on the community action plans of eligible entities submitted to the State as a condition of receiving funding under this subtitle; (C) may revise an existing State plan for submission to the Secretary, subject to the notice and distribution requirements in subparagraph (D)(iii); (D) in conjunction with the development of the State plan as required under subsection (b)\u2014 (i) shall hold at least one hearing in the State on the proposed plan, to provide to the public an opportunity to comment on the public record on the proposed use and distribution of funds under the plan; (ii) not less than 15 days before the hearing, shall distribute notice of the hearing and a copy of the proposed plan statewide to the public and directly to the chief executive officer and board chairperson of each eligible entity and other community services network organization in the State; and (iii) in the case of any proposed plan revision, shall notify and distribute a copy of the proposed revision directly to the chief executive officer and board chairperson of each eligible entity and other community services network organization in the State, before submission of such proposed revision to the Secretary; and (E) shall conduct reviews of eligible entities under section 678B. ,\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin the matter preceding paragraph (1)\u2014\n**(i)**\nby striking 2000 and inserting 2026 , and\n**(ii)**\nby striking 30 and inserting 60 ,\n**(B)**\nin paragraph (1)\u2014\n**(i)**\nby striking made available through the grant or allotment will be used and inserting provided to an eligible entity under section 675C(a) shall be used by such entity for ,\n**(ii)**\nby striking to support activities that are designed and all that follows through will enable the families and individuals , and inserting programs, projects, and services that will enable low-income and working individuals and families ,\n**(iii)**\nin subparagraph (B) by striking and at the end,\n**(iv)**\nin subparagraph (C) by adding and at the end, and\n**(v)**\nby adding at the end the following:\n(D) to address the educational and economic needs of low-income individuals, families, and communities by providing assistance through trained navigators to help facilitate access to affordable high-speed broadband service, internet-enabled devices, digital literacy training, technical support, and other services to meet the broadband and digital needs of such individuals, families, and communities. ,\n**(C)**\nin paragraph (2) by striking related to and inserting and the building and use of evidence of effectiveness in achieving ,\n**(D)**\nin paragraph (3)\u2014\n**(i)**\nby inserting a description summarizing the community action plans and after (3) , and\n**(ii)**\nin subparagraph (D) by striking fatherhood initiatives and inserting whole family approaches ,\n**(E)**\nby amending paragraph (11) to read as follows:\n(11) an assurance that the State will secure from each eligible entity in the State, as a condition of receipt of funding by the entity under section 675C(a), a community action plan that\u2014 (A) contains information on the intended implementation of the entity\u2019s activities; (B) demonstrates how such activities will meet needs identified in the most recent comprehensive community needs assessment conducted by the entity in the previous three years, which may be coordinated with community needs assessments conducted for other programs; and (C) demonstrates how such activities will achieve the purposes of this subtitle; .\n**(F)**\nin paragraph (12)\u2014\n**(i)**\nby striking the comma and , not later than fiscal year 2001, ,\n**(ii)**\nby striking promoting and inserting achieving the goals of the State plan and community action plans of eligible entities, respectively, and the purposes of this subtitle, including , and\n**(iii)**\nby striking and at the end,\n**(G)**\nby amending paragraph (13) to read as follows:\n(13) an assurance that each eligible entity in the State shall make available to the public on the entity\u2019s publicly available website the entity\u2019s most recent agency-wide strategic plan, comprehensive community needs assessment, and community action plan; , and\n**(H)**\nby adding the following at the end:\n(14) an assurance that State personnel who conduct monitoring activities under section 678B will have expertise in the programs, projects, and services carried out under this subtitle and in the unique structure and role of eligible entities in their local communities; (15) an assurance that the State will make payments to eligible entities in accordance with section 675B(a); (16) an assurance that the State will develop a policy on board vacancies in accordance with section 676B(d) and provide guidance to assist eligible entities in filling board vacancies; and (17) information describing how the State will carry out the assurances described in this subsection. ,\n**(3)**\nby amending subsection (e) to read as follows:\n(e) Public inspection Each State plan prepared under this section shall be made available on the lead agency\u2019s website and distributed for public inspection and comment. A hearing on such plan shall be held as required under subparagraphs (C) and (D) of subsection (a) (2). , and\n**(4)**\nin subsection (f)\u2014\n**(A)**\nby striking 2000 and inserting 2026 , and\n**(B)**\nby striking Coats Human Services Reauthorization Act of 1998 and inserting Community Services Block Grant Improvement Act of 2025 .\n#### 9. Designation and redesignation of eligible entities in unserved areas\nSection 676A(a) of the Community Services Block Grant Act ( 42 U.S.C. 9909(a) ) is amended to read as follows:\n(a) Qualified organization in or near area (1) In general If any geographic area of a State is not, or ceases to be, served by an eligible entity under this subtitle, the State lead agency may, in consultation with local officials and organizations representing the area, solicit one or more applications and designate a new community action agency to provide programs, projects, and services to the area, that is\u2014 (A) a community action agency that is a private, nonprofit organization and that is geographically located in an area in reasonable proximity of, or contiguous to, the unserved area and that is already providing similar programs, projects, and services, and that has demonstrated financial capacity to manage and account for Federal funds; or (B) if no community action agency described in subparagraph (A) is available, a private, nonprofit organization (which may include an eligible entity) that is geographically located in, or is in reasonable proximity to, the unserved area and that is capable of providing a broad range of programs, projects, and services designed to achieve the purposes of this subtitle as stated in section 672. (2) Requirement In order to serve as the eligible entity for the area, an entity described in paragraph (1) shall agree to ensure that the governing board of directors of the entity will meet the requirements of section 676B. (3) Community A service area referred to in this subsection or a portion thereof shall be treated as a community for purposes of this subtitle. (4) Interim designation If no entity that meets the requirements of subsection (a) is available for designation as a permanent eligible entity, the State may designate a private, nonprofit agency (or public agency if a private nonprofit is not available) on an interim basis for no more than one year while the State completes a selection process for a permanent eligible entity that meets the requirements of subsection (a). An agency designated on an interim basis shall be capable of providing programs, projects, and services designed to achieve the purposes described in section 672 and have demonstrated financial capacity to manage and account for Federal funds, and may be designated as a permanent eligible entity only if, by the time of permanent designation, it meets all the requirements of paragraphs (1) and (2). .\n#### 10. Tripartite boards\nSection 676B of the Community Services Block Grant Act ( 42 U.S.C. 9910 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby amending paragraph (1) to read as follows:\n(1) Board In order for a private, nonprofit organization to be considered to be an eligible entity for purposes of 673(6), the entity shall be governed by a tripartite board of directors described in subparagraph (C) that fully participated in the development, planning, implementation, oversight, and evaluation of the programs, projects, and services carried out or provided through the subgrant made under section 675C(a) and all activities of the entity. ,\n**(B)**\nin paragraph (2)(A) by striking except and all that follows through requirement , and inserting (but if an elected official chooses not to serve, such official may designate a representative to serve as the voting board member); and , and\n**(C)**\nby adding at the end the following:\n(3) Compliance with tax-exempt and other requirements The board of a private, nonprofit organization shall ensure that the board operates and conducts activities under the subgrant made under section 679(Ca) that complies with\u2014 (A) the requirements for maintaining tax-exempt status under section 501(a) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(a) ) regarding the governance of charities under section 501(c)(3) of the Internal Revenue Code of 1986 ( 26 U.S.C. 501(c)(3) ); and (B) applicable requirements of State nonprofit law. , and\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby redesignating subparagraphs (A), (B), and (C) as clauses (i), (ii), and (iii), respectively, and\n**(ii)**\nin paragraph (2) by adding References under this subtitle to the board of an eligible entity shall apply to such other mechanism. at the end,\n**(B)**\nby redesignating paragraphs (1) and (2) as subparagraphs (A) and (B); respectively,\n**(C)**\nby striking public organizations.\u2014 and inserting, board or other mechanism.\u2014 (1) , and\n**(D)**\nby adding at the end the following:\n(2) Compliance with State requirements and policy The board of a public entity shall ensure that the board operates in a manner that complies with State requirements for open meetings, financial transparency, and State open records policy. , and\n**(3)**\nby adding at the end the following:\n(c) Expertise Each eligible entity shall ensure that the members of the board are provided resources, which may include contracted services with individuals and organizations with expertise in financial management, accounting, and law, to support the work of the board. (d) Board vacancies To fulfill the requirements under this section, an eligible entity shall fill a board vacancy not later than 6 months after such vacancy arises. In the event that an eligible entity is unable to fill a board vacancy in the 6-month period, the entity shall certify to the State that it is making a good faith effort to fill the vacancy and shall receive one additional 6-month period to fill such vacancy. (e) Operations and duties of the board The duties of a board described in paragraph (1) or (2) of subsection (a) shall include\u2014 (1) in the case of a board for a private, nonprofit organization that is an eligible entity, having legal and financial responsibility for administering and overseeing the eligible entity, including making proper use of Federal funds; (2) establishing terms for officers and adopting a code of ethical conduct, including a conflict of interest policy for board members; (3) participating in a comprehensive community needs assessment conducted at least once every three years, developing and adopting for the corresponding eligible entity an agency-wide strategic plan, and preparing the community action plan for the use of funds under this subtitle; (4) approving the eligible entity\u2019s operating budget; (5) reviewing all major policies such that\u2014 (A) for private, nonprofit organizations that are eligible entities, a review includes conducting annual performance reviews of the eligible entity\u2019s chief executive officer (or individual holding an equivalent position); and (B) for local public entities that are eligible entities, a review includes participating in annual performance reviews of the eligible entity\u2019s chief executive officer (or individual holding an equivalent position); (6) performing oversight of the eligible entity to include\u2014 (A) conducting assessments of the eligible entity\u2019s progress in carrying out programmatic and financial provisions in the community action plan; and (B) in the case of any required corrective action, reviewing the eligible entity\u2019s plans and progress in remedying identified deficiencies; and (7) concerning personnel policies and procedures\u2014 (A) in the case of private, nonprofit organizations that are eligible entities, adopting personnel policies and procedures, including for hiring, annual evaluation, compensation, and termination, of the eligible entity\u2019s chief executive officer (or individual holding a similar position); and (B) in the case of local public entities that are eligible entities, reviewing personnel policies and procedures, including for hiring, annual evaluation, compensation, and termination, of the eligible entity\u2019s chief executive officer (or individual holding a similar position). (f) Conflict of interest In establishing the conflict of interest policy described in subsection (e)(2), a board shall ensure that such policy\u2014 (1) requires a board member to recuse themself from any discussion, deliberations, and votes relating to any contract or transaction from which the following would receive a direct financial benefit from the eligible entity: (A) such board member; (B) the immediate family member of such board member; or (C) an organization or a business from which such board member, or an immediate family of such board member, receives a direct financial benefit; (2) prohibits a board member from receiving compensation for serving on the board from the eligible entity other than for reasonable expenses, except that a board member\u2019s receipt of an economic benefit from the eligible entity because such member is eligible to receive benefits and services under this subtitle shall not be considered to be compensation for purposes of this subsection; and (3) ensures all activities funded under this subtitle are conducted free of personal or family favoritism. .\n#### 11. Office of community services\nSection 678(b) of the Community Services Block Grant Act ( 42 U.S.C. 9912(b) ) is amended by inserting , acting through the Director, after The Secretary .\n#### 12. Training, technical assistance, and other activities\nSection 678A(c) of the Community Services Block Grant Act ( 42 U.S.C. 9913(c) ) is amended to read as follows:\n(c) Distribution requirement (1) In general The amounts reserved under section 674(b)(2)(A) for activities to be carried out under this subsection shall be distributed directly to eligible entities and other community services network organizations for\u2014 (A) professional development for key community services network organization personnel; (B) activities to improve community services network organization program quality, financial management, compliance, and governance practices (including practices related to performance management information systems); (C) activities that train community services network organizations in building and using evidence of effectiveness in achieving the purposes of this subtitle; and (D) activities to ensure responsiveness to identified local needs. (2) Eligible entities or organizations Eligible entities and other community services network organizations described in this subsection shall include such entities and organizations (and their partners, including institutions of higher education), with demonstrated expertise in providing training to individuals and organizations on methods of effectively addressing the needs of low-income and working families and communities. .\n#### 13. Fiscal controls, audits, and withholding\nSection 678D of the Community Services Block Grant Act ( 42 U.S.C. 9916 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nin paragraph (A) by inserting and, notwithstanding the applicability of subparagraph (B), issue payment to subrecipients on an advance basis. before the semicolon at the end, and\n**(ii)**\nby amending subparagraph (B) to read as follows:\n(B) Single audit requirements (i) In general Audits shall be conducted under this paragraph in the manner and to the extent provided in chapter 75 of title 31, United States Code (commonly known as the Single Audit Act Amendments of 1984 ), except in the event a serious financial deficiency is identified. (ii) Serious financial deficiency In the event that such a deficiency is identified, the Secretary shall order an audit conducted as described in subparagraph (1), or an audit of each of the accounts involved, in accordance with subparagraph (2). , and\n**(B)**\nby amending paragraph (3) to read as follows:\n(3) Repayments If the Secretary, after review of the audit, finds that a State has not expended an amount of funds in accordance with this subtitle, the Secretary is authorized to withhold funds from the State under this subtitle until the State remedies the improperly expended funds for the original purpose for which the grant funds were intended. , and\n**(2)**\nin subsection (b)(3) by inserting or a complaint of a serious deficiency concerning any State after any fiscal year .\n#### 14. Accountability and reporting requirements\nSection 678E(b) of the Community Services Block Grant Act ( 42 U.S.C. 9917 ) is amended\u2014\n**(1)**\nin paragraph (3) by striking Labor and Human Resources and inserting Health, Education, Labor, and Pensions , and\n**(2)**\nby striking paragraph (4).\n#### 15. Limitations on use of funds\nSection 678F(a)(1) of the Community Services Block Grant Act ( 42 U.S.C. 9918(a)(1) ) is amended by striking amounts reserved under section 674(b)(3) and inserting amounts appropriated under section 674(c) .\n#### 16. Discretionary authority of the Secretary\nSection 680 of the Community Services Block Grant Act ( 42 U.S.C. 9921 ) is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (1)\u2014\n**(i)**\nby striking funds reserved under section 674(b)(3) and inserting amounts made available to carry out this section , and\n**(ii)**\nby striking through (4) and inserting and (3) , and\n**(B)**\nby striking subparagraph (4), and\n**(2)**\nin subsection (c) by striking Labor and Human Resources and inserting Health, Education, Labor, and Pensions .\n#### 17. Community food and nutrition programs\nThe Community Services Block Grant Act ( 42 U.S.C. 9922 ) is amended by striking section 681.\n#### 18. National or regional programs designed to provide instructional activities for low-income youth\nThe Community Services Block Grant Act ( 42 U.S.C. 9923 ) is amended\u2014\n**(1)**\nby striking section 682, and\n**(2)**\nby redesignating section 683 as section 681.",
      "versionDate": "2025-05-01",
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
        "name": "Social Welfare",
        "updateDate": "2025-05-22T16:27:51Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-01",
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
          "measure-id": "id119hr3131",
          "measure-number": "3131",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-01",
          "originChamber": "HOUSE",
          "update-date": "2026-03-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3131v00",
            "update-date": "2026-03-03"
          },
          "action-date": "2025-05-01",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Community Services Block Grant Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Services Block Grant (CSBG) program through FY2032 and makes certain changes to the program and associated eligibility requirements. The CSBG program supports various antipoverty activities, primarily through formula-based allotments to states, tribes, and territories, the majority of which must be made available in grants to eligible local entities.\u00a0</p><p>Specifically, the bill permanently sets the measure of eligibility for services, assistance, or resources provided directly to individuals or families under the program at 200% of the poverty line. (Under current law, the eligibility measure is temporarily set at 200% of the poverty line, an increase from the previous measure of 125% of the poverty line.)</p><p>The bill also makes certain changes to the permitted uses of funding, including by allowing CSBG funds to be used to facilitate low-income individuals\u2019 and communities\u2019 access to high-speed broadband, digital literacy training, technical support, and other services. States may also use certain funds allocated for training and technical assistance to assist eligible entities in responding to statewide and regional conditions that create economic insecurity, including emergency conditions. \u00a0</p><p>The bill also expands requirements for the plans that states must submit to the Department of Health and Human Services in order to receive CSBG funds (e.g., transparency assurances), and sets deadlines by which states must make funds available to eligible entities.</p><p>Finally, the bill repeals a provision that allowed states to use CSBG funds to offset revenue losses associated with state charity tax credits.\u00a0</p>"
        },
        "title": "Community Services Block Grant Improvement Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3131.xml",
    "summary": {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community Services Block Grant Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Services Block Grant (CSBG) program through FY2032 and makes certain changes to the program and associated eligibility requirements. The CSBG program supports various antipoverty activities, primarily through formula-based allotments to states, tribes, and territories, the majority of which must be made available in grants to eligible local entities.\u00a0</p><p>Specifically, the bill permanently sets the measure of eligibility for services, assistance, or resources provided directly to individuals or families under the program at 200% of the poverty line. (Under current law, the eligibility measure is temporarily set at 200% of the poverty line, an increase from the previous measure of 125% of the poverty line.)</p><p>The bill also makes certain changes to the permitted uses of funding, including by allowing CSBG funds to be used to facilitate low-income individuals\u2019 and communities\u2019 access to high-speed broadband, digital literacy training, technical support, and other services. States may also use certain funds allocated for training and technical assistance to assist eligible entities in responding to statewide and regional conditions that create economic insecurity, including emergency conditions. \u00a0</p><p>The bill also expands requirements for the plans that states must submit to the Department of Health and Human Services in order to receive CSBG funds (e.g., transparency assurances), and sets deadlines by which states must make funds available to eligible entities.</p><p>Finally, the bill repeals a provision that allowed states to use CSBG funds to offset revenue losses associated with state charity tax credits.\u00a0</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr3131"
    },
    "title": "Community Services Block Grant Improvement Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-05-01",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Community Services Block Grant Improvement Act of 2025</strong></p><p>This bill reauthorizes the Community Services Block Grant (CSBG) program through FY2032 and makes certain changes to the program and associated eligibility requirements. The CSBG program supports various antipoverty activities, primarily through formula-based allotments to states, tribes, and territories, the majority of which must be made available in grants to eligible local entities.\u00a0</p><p>Specifically, the bill permanently sets the measure of eligibility for services, assistance, or resources provided directly to individuals or families under the program at 200% of the poverty line. (Under current law, the eligibility measure is temporarily set at 200% of the poverty line, an increase from the previous measure of 125% of the poverty line.)</p><p>The bill also makes certain changes to the permitted uses of funding, including by allowing CSBG funds to be used to facilitate low-income individuals\u2019 and communities\u2019 access to high-speed broadband, digital literacy training, technical support, and other services. States may also use certain funds allocated for training and technical assistance to assist eligible entities in responding to statewide and regional conditions that create economic insecurity, including emergency conditions. \u00a0</p><p>The bill also expands requirements for the plans that states must submit to the Department of Health and Human Services in order to receive CSBG funds (e.g., transparency assurances), and sets deadlines by which states must make funds available to eligible entities.</p><p>Finally, the bill repeals a provision that allowed states to use CSBG funds to offset revenue losses associated with state charity tax credits.\u00a0</p>",
      "updateDate": "2026-03-03",
      "versionCode": "id119hr3131"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-01",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3131ih.xml"
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
      "title": "Community Services Block Grant Improvement Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-23T14:12:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Community Services Block Grant Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-13T05:23:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend and reauthorize the Community Services Block Grant Act.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-13T05:18:44Z"
    }
  ]
}
```
