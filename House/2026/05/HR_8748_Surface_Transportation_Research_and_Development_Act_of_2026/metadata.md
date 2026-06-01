# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8748?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8748
- Title: Surface Transportation Research and Development Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8748
- Origin chamber: House
- Introduced date: 2026-05-12
- Update date: 2026-05-21T19:38:08Z
- Update date including text: 2026-05-21T19:38:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-12: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.
- Latest action: 2026-05-12: Introduced in House

## Actions

- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Introduced in House
- 2026-05-12 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-12 - IntroReferral: Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-05-20 - Committee: Committee Consideration and Mark-up Session Held
- 2026-05-20 - Committee: Ordered to be Reported (Amended) by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-12",
    "latestAction": {
      "actionDate": "2026-05-12",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8748",
    "number": "8748",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "F000480",
        "district": "20",
        "firstName": "Vince",
        "fullName": "Rep. Fong, Vince [R-CA-20]",
        "lastName": "Fong",
        "party": "R",
        "state": "CA"
      }
    ],
    "title": "Surface Transportation Research and Development Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-21T19:38:08Z",
    "updateDateIncludingText": "2026-05-21T19:38:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-12",
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
      "text": "Referred to the Committee on Science, Space, and Technology, and in addition to the Committee on Transportation and Infrastructure, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-12",
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
        "item": [
          {
            "date": "2026-05-20T18:21:50Z",
            "name": "Markup By"
          },
          {
            "date": "2026-05-12T16:04:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-05-12T16:04:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "systemCode": "hspw00",
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
      "bioguideId": "S001223",
      "district": "13",
      "firstName": "Emilia",
      "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Sykes",
      "middleName": "Strong",
      "party": "D",
      "sponsorshipDate": "2026-05-12",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8748ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8748\nIN THE HOUSE OF REPRESENTATIVES\nMay 12, 2026 Mr. Fong (for himself and Mrs. Sykes ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology , and in addition to the Committee on Transportation and Infrastructure , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo direct the Secretary of Transportation to carry out certain activities related to surface transportation research, development, and deployment, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Surface Transportation Research and Development Act of 2026 .\n#### 2. Technology and innovation programs related to highway and intermodal transportation systems\nSubsection (c) of section 503 of title 23, United States Code, is amended\u2014\n**(1)**\nin paragraph (3)(D), by striking fiscal years 2022 through 2026 and inserting fiscal years 2027 through 2031 ;\n**(2)**\nin paragraph (4)(I)(i), by striking fiscal years 2022 through 2026 and inserting fiscal years 2027 through 2031 ; and\n**(3)**\nin paragraph (5)(C), by striking fiscal years 2022 through 2026 and inserting fiscal years 2027 through 2031 .\n#### 3. Update to transportation statistics programs\nSection 6302 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (b)(3) by adding at the end the following new subparagraph:\n(C) Location The Director shall be located within the organizational structure of the Office of the Assistant Secretary for Research and Technology. ;\n**(2)**\nin subsection (d)(2), in the matter preceding subparagraph (A), by striking a significant role in and inserting exclusive authority over ; and\n**(3)**\nby adding at the end the following new subsection:\n(e) Coordination of statistical activities (1) In general The Secretary shall ensure the following: (A) Any activity of the Department related to the collection, analysis, and use of data for a statistical purpose is conducted in a manner that protects the trust of information providers and maintains the confidentiality, objectivity, and integrity of such data, in accordance with subchapter III of chapter 35 of title 44. (B) The Department and each operating administration thereof is following, as appropriate, best practices, technical standards, and requirements in accordance with subchapter II of chapter 3 of title 5, subchapter III of chapter 35 of title 44, and any other appropriate Federal policy in the collection, analysis, and use of any transportation-related data intended for a statistical purposes. (2) Statistical purpose defined In this subsection, the term statistical purpose has the meaning given such term in section 3561 of title 44. .\n#### 4. Transportation Statistics Coordination Council\n##### (a) In general\nTitle 49, United States Code, is amended by inserting after section 6302 the following new section:\n6302A. Transportation Statistics Coordination Council. (a) In general Not later than 90 days after the date of the enactment of this section, the Secretary shall establish the Transportation Statistics Coordination Council (in this subsection referred to as the Council ) to coordinate statistical activities and evaluations across the Department. (b) Membership The Council shall be composed of a representative from each operating administration of the Department that conducts a program related to any statistical activities and evaluations documented by the Department. The Secretary may designate additional members to the Council as the Secretary determines appropriate. (c) Chairperson The Director shall serve as the Chairperson of the Council. (d) Duties The Council shall carry out the following: (1) Assist the Director in carrying out the duties required under subsection (b)(3) of section 6302. (2) Review the comprehensive data inventory of the Department developed and maintained pursuant to section 3511 of title 44, to identify any data assets of the Department that are duplicative or fragmented across the Department; (3) Identify any opportunity to reduce burden, including with respect to a State, local, or Tribal government or a private sector entity, by consolidating into a centralized repository managed by the Director similar collection of information from different operating administrations. (4) Advise the Director with respect to the development and implementation of Department-wide data guidelines, standards, metadata schemas, and common taxonomies related to any statistical activities and evaluations conducted by the Department. (e) Report Not later than three years after the date of the enactment of this subsection, the Secretary shall submit to the Committee on Transportation and Infrastructure and the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate a report that includes information related to the following: (1) A comprehensive inventory of any statistical activities and evaluations conducted by the Department. (2) A plan for the elimination of any statistical activities and evaluations conducted outside the Bureau that duplicate the duties required under subsection (b)(3) of section 6302, including information relating to the following: (A) Any plan for an order or agreement under section 1535 of title 31. (B) An analysis related to whether all statistical activities and evaluations of the Department should be centralized within the Bureau. (3) A governance strategy and any recommendations to ensure the Department and any operating administration of the Department is following the Department-wide data guidelines, standards, metadata schemas, and common taxonomies referred to in subsection (d)(4). (4) An assessment of any administrative, technical, or legal barrier to the governance strategy and recommendations described in paragraph (3), including any findings or milestones for implementation by the Department the Council determines necessary to achieve a unified, secure, and efficient departmental statistical infrastructure in accordance with such subparagraph. (f) Definitions In this section: (1) Burden; collection of information The terms burden and collection of information have the meaning given such terms in section 3502 of title 44. (2) Evaluation The term evaluation has the meaning given such term in section 311 of title 5. (3) Statistical activities The term statistical activities has the meaning given such term in section 3561 of title 44. .\n##### (b) Clerical amendment\nThe table of sections in chapter 63 of title 49, United States Code, is amended by inserting after the item relating to section 6302 the following new item:\n6302A. Transportation Statistics Coordination Council. .\n#### 5. Amendments to the university transportation centers program\nSection 5505 of title 49, United States Code, is amended\u2014\n**(1)**\nin subparagraph (A) of subsection (c)(4), by striking not more than ; and\n**(2)**\nin paragraph (3) of subsection (d), by striking fiscal years 2022 through 2026 and inserting fiscal years 2027 through 2031 .\n#### 6. Open research initiative\nSection 5506 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (f), in the matter preceding paragraph (1), by striking Not less frequently than biennially, in accordance and inserting In accordance ;\n**(2)**\nin subsection (i), by striking 2022 through 2026 and inserting 2027 through 2031 ;\n**(3)**\nby redesignating subsection (i) as subsection (j); and\n**(4)**\nby inserting after subsection (h) the following new subsection:\n(i) Implementation plan (1) In general The Secretary shall develop an implementation plan to transition the advanced transportation research pilot program described in subsection (b) to a sustained open research initiative. (2) Report Not later than two years after the date of the enactment of this subsection, the Secretary shall submit to the Committee on Transportation and Infrastructure and the Committee on Science, Space, and Technology of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Environment and Public Works of the Senate a report that includes information relating to the following: (A) The implementation plan under paragraph (1). (B) How the Secretary is carrying out such implementation plan. .\n#### 7. Study on and recommendations relating to the safety effects of emerging headlamp technologies\n##### (a) In general\nNot later than 180 days after the date of the enactment of this Act, Secretary of Transportation (in this section referred to as the Secretary ), acting through the Assistant Secretary of Transportation for Research and Technology, and in consultation with the Administrator of the National Highway Traffic Safety Administration, shall seek to enter into an agreement with an appropriate entity with relevant expertise, as determined by the Secretary, to\u2014\n**(1)**\nconduct a study on the effects of high-intensity light-emitting diode (LED), matrix LED, and other emerging headlamp technologies with respect to driver visibility, glare exposure, and roadway safety; and\n**(2)**\nmake recommendations relating thereto.\n##### (b) Contents\n**(1) Study**\nThe study under subsection (a) may include any of the following:\n**(A)**\nAn assessment of any of the following:\n**(i)**\nLuminous intensity, total luminous flux, and beam-pattern characteristics of headlamp technologies utilized in road vehicles.\n**(ii)**\nThe role of vehicle mounting height and headlamp aim in real-world glare exposure, including the geometric interaction between headlamps and occupants of preceding or oncoming vehicles, across a range of vehicles and vehicle mounting heights.\n**(iii)**\nThe physiological and cognitive effects of high-intensity headlamp exposure on the following:\n**(I)**\nDrivers, with particular attention to older drivers, as defined by the appropriate entity referred to in such subsection, and drivers with cataracts or other visual impairments.\n**(II)**\nThe ability of drivers to visually identify and avoid vulnerable road users, including pedestrians, bicyclists, and motorcyclists.\n**(B)**\nAn analysis of the adequacy of existing headlamp photometric test procedures to address the luminance, spectral, and glare characteristics of high-intensity LED, matrix LED, and other emerging headlamp technologies.\n**(2) Recommendations**\nThe recommendations under subsection (a) may include a recommendation regarding how to mitigate a negative finding of the study under such subsection with respect to the effect of high-intensity LED, matrix LED, or another emerging headlamp technology on driver visibility, glare exposure, or roadway safety.\n##### (c) Report\nNot later than two years after entering into an agreement under subsection (a), the Secretary shall submit to the Committee on Science, Space, and Technology and the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Commerce, Science, and Transportation of the Senate, and make publicly available on a website of the Department of Transportation, a report that includes information relating to the findings of the study conducted pursuant to such subsection and the recommendations relating thereto.\n#### 8. Strategy on reclaimed asphalt pavement\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Transportation (in this section referred to as the Secretary ), acting through the Administrator of the Federal Highway Administration, shall submit to the Committee on Science, Space, and Technology and the Committee on Transportation and Infrastructure of the House of Representatives, and the Committee on Commerce, Science, and Transportation and the Committee on Environment and Public Works of the Senate a strategy to encourage the standardization and utilization of reclaimed asphalt pavement on roadways nationwide and ensure asphalt mixture quality does not decrease as a result of such utilization.\n##### (b) Contents\nThe strategy under subsection (a) shall include information relating to the following:\n**(1)**\nA review and inventory of the activities of the Secretary with respect to reclaimed asphalt pavement.\n**(2)**\nAn analysis of cost savings related to increasing the allowable use of reclaimed asphalt pavement on roadways nationwide.\n**(3)**\nA description of any such activities related to supporting the development of technical standards, best practices, methodologies, and frameworks for testing and use of reclaimed asphalt pavement.\n**(4)**\nRecommendations to promote through programs of the Department of Transportation the utilization of reclaimed asphalt pavement.\n##### (c) Consultation\nIn submitting the strategy under subsection (a), the Secretary, acting through the Administrator of the Federal Highway Administration, shall carry out the following:\n**(1)**\nSeek to consult with representatives from the following:\n**(A)**\nInstitutions of higher education.\n**(B)**\nState departments of transportation.\n**(C)**\nUnits of local government.\n**(D)**\nMetropolitan planning organizations.\n**(E)**\nRegional transportation planning organizations.\n**(F)**\nNonprofit research organizations.\n**(G)**\nPrivate sector entities that produce asphalt materials.\n**(2)**\nConsult with the following:\n**(A)**\nThe heads of other relevant Federal departments and agencies.\n**(B)**\nAny other relevant entity as the Secretary determines appropriate.\n##### (d) Definitions\nIn this section:\n**(1) Institution of higher education**\nThe term institution of higher education has the meaning given such term in section 101 of the Higher Education Act of 1965 ( 20 U.S.C. 1001 ).\n**(2) Metropolitan planning organization**\nThe term metropolitan planning organization has the meaning given such term in section 5303 of title 49, United States Code.\n**(3) Nonprofit research organization**\nThe term nonprofit research organization has the meaning given the term nonprofit institution in section 4 of the Stevenson-Wydler Technology Innovation Act of 1980 ( 15 U.S.C. 3703 ).\n**(4) Reclaimed asphalt pavement**\nThe term reclaimed asphalt pavement means material that is removed in the resurfacing, rehabilitation, or reconstruction of asphalt pavement and processed for utilization in the production of new asphalt pavement.\n**(5) Regional transportation planning organization**\nThe term regional transportation planning organization means an organization designated under subsection (l) of section 5304 of title 49, United States Code.\n#### 9. Rail research programs\nSection 24910 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nin paragraph (3), by striking and after the semicolon;\n**(B)**\nin paragraph (4), by striking the period at the end and inserting ; and ; and\n**(C)**\nby adding at the end the following new paragraph:\n(5) address safety challenges with modern and future infrastructure and technology related to commuter rail, passenger rail, freight rail, and other rail networks. ;\n**(2)**\nin subsection (b)\u2014\n**(A)**\nin paragraph (13), by striking and after the semicolon;\n**(B)**\nby redesignating paragraph (14) as paragraph (15); and\n**(C)**\nby inserting after paragraph (13) the following new paragraph:\n(14) to review safety standards related to the transportation of hazardous materials on freight rail; and ;\n**(3)**\nin paragraph (3) of subsection (c), by striking 2019 and inserting 2031 ; and\n**(4)**\nin subsection (e), by striking 2010 through 2013 and inserting 2027 through 2031 .",
      "versionDate": "2026-05-12",
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
        "name": "Transportation and Public Works",
        "updateDate": "2026-05-21T19:38:08Z"
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
      "date": "2026-05-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8748ih.xml"
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
      "title": "Surface Transportation Research and Development Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-14T03:23:29Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Surface Transportation Research and Development Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-14T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to carry out certain activities related to surface transportation research, development, and deployment, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-14T03:18:39Z"
    }
  ]
}
```
