# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3387?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3387
- Title: ETS Act
- Congress: 119
- Bill type: HR
- Bill number: 3387
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-05-15T20:51:22Z
- Update date including text: 2026-05-15T20:51:22Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-14 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-06 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3387",
    "number": "3387",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "ETS Act",
    "type": "HR",
    "updateDate": "2026-05-15T20:51:22Z",
    "updateDateIncludingText": "2026-05-15T20:51:22Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-11",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-06",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
      "committees": {
        "item": {
          "name": "Armed Services Committee",
          "systemCode": "hsas00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-06-11T13:53:39Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-06-06T13:53:24Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-14T14:05:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Armed Services Committee",
      "systemCode": "hsas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3387ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3387\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 10 and 38, United States Code, to make improvements to certain programs for a member nearing separation, or for a veteran who recently separated, from the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Enhancing the Transitioning Servicemember\u2019s Experience Act or the ETS Act .\n#### 2. Transition Assistance Program: amendments; pilot program; reports\n##### (a) Special operations forces\nSubsection (a) of section 1142 of title 10, United States Code, is amended, in paragraph (1), by inserting (including each member of the special operations forces) after armed forces .\n##### (b) Requirement of preseparation counseling: number of days\nSuch subsection is further amended, in paragraph (1)\u2014\n**(1)**\nby inserting (A) before Within ; and\n**(2)**\nby adding at the end the following new subparagraph:\n(B) The Secretary concerned shall ensure that a member described in subparagraph (A) receives preseparation counseling in the following amounts: (i) In the case of a member who has accepted an offer of full-time employment, or has enrolled in a program of education or vocational training, that shall commence after the member separates, retires, or is discharged, not fewer than three days. (ii) In the case of a member other than a member described in clause (i), not fewer than five days. .\n##### (c) Provision of preseparation counseling: third party counselors; in-Person to the extent practicable\nSuch subsection is further amended, in paragraph (2)\u2014\n**(1)**\nby inserting (A) before In carrying ; and\n**(2)**\nby adding at the end the following new subparagraphs:\n(B) Preseparation counseling may not be provided by an individual responsible for the retention of members in the armed force concerned. (C) Preseparation counseling shall be provided in person to the extent practicable. If the Secretary concerned determines that a member cannot attend such counseling in person, such member may receive such counseling remotely. .\n##### (d) Period of eligibility: expansion\nSuch subsection is further amended, in paragraph (3)\u2014\n**(1)**\nby striking 365 each place it appears and inserting 540 ; and\n**(2)**\nby striking 365-day and inserting 540-day .\n##### (e) Waiver for certain members of the reserve components\nSuch subsection is further amended, in paragraph (4), by adding at the end the following new subparagraph:\n(D) The Secretary concerned may waive the requirement for preseparation counseling under paragraph (1) in the case of a member of the reserve components if\u2014 (i) the member requests such a waiver; (ii) the member received preseparation counseling during the period of three years preceding the date of such request; and (iii) matters covered by such counseling, specified in subsection (b), have not changed since the member last received such counseling. .\n##### (f) Eligibility of a member who reenlists To receive preseparation counseling\nSuch subsection is further amended by adding at the end the following new paragraph:\n(5) The commanding officer of a member described in this subsection may, on a space available basis, authorize such member to receive preseparation counseling, regardless of whether such member reenlists or agrees to a new period of obligated service. .\n##### (g) Repeat attendance\nSuch subsection is further amended by adding at the end the following new paragraph:\n(6) A member who received preseparation counseling under this section may, before separation, retirement, or discharge, request to receive, on a space-available basis, such preseparation counseling a second time. .\n##### (h) Elective inclusion of the spouse of a member\nSuch section is further amended, in subsection (b), in paragraph (5), by striking regarding the matters covered by paragraphs (9), (10), and (16) .\n##### (i) Minimum amount of counseling regarding financial planning\nSuch subsection is further amended, in paragraph (9)\u2014\n**(1)**\nby striking Financial and inserting (A) General financial ;\n**(2)**\nby striking loans and inserting loans and other debt, investing ; and\n**(3)**\nby adding at the end the following new subparagraphs:\n(B) Individualized assistance regarding matters described in subparagraph (A). (C) Counseling under subparagraph (A) or (B) shall be provided by an individual who has significant experience in financial planning and may not be shorter than one hour. .\n##### (j) Pathways: standardization; establishment of pathway for members of the reserve components\nSuch section is further amended, in paragraph (1) of subsection (c), in the matter preceding subparagraph (A)\u2014\n**(1)**\nby striking Each Secretary concerned and inserting The Secretaries of Defense and Homeland Security ; and\n**(2)**\nby striking pathways for members of the military department concerned and inserting pathways, standardized across the armed forces and including one pathway for members of the reserve components, for members .\n##### (k) Pathways: record of pathway assignment\nSuch subsection is further amended by adding at the end the following new paragraph:\n(4) The Secretary concerned shall ensure that the pathway in which a member is placed, and the reasons for such placement, are noted in the service record of such member. .\n##### (l) Coordination between Departments of Defense, Veterans Affairs, and Labor\nSuch section is further amended, in subsection (d)\u2014\n**(1)**\nby striking the heading and inserting Transmission of certain information to other departments ;\n**(2)**\nby inserting (1) before In the case ; and\n**(3)**\nby adding at the end the following new paragraphs:\n(2) Before a member described in subsection (a) separates, retires, or is discharged, the Secretary concerned shall transmit to the Secretary of Veterans Affairs the following information: (A) The contact information of such member. (B) The Department of Defense Form DD\u20132648 regarding such member. (3) (A) In the case of a member described in subsection (a) whom the Secretary concerned determines is at risk for a difficult transition to civilian life, the Secretary concerned shall, before the member separates, retires, or is discharged, provide\u2014 (i) such member with the contact information of an employee of the Department of Veterans Affairs and an employee of the Department of Labor; and (ii) such employees with the contact information of such member. (B) Each employee described in subparagraph (A) shall contact the member described in such subparagraph not later than 60 days after such member separates, retires, or is discharged. (C) The Secretary of Veterans Affairs and the Secretary of Labor shall each submit to the Committees on Armed Services and on Veterans\u2019 Affairs of the Senate and House of Representatives an annual report that identifies the number of times, and reasons why, an employee of the department under the jurisdiction of such Secretary failed to carry out subparagraph (B) in the year preceding the date of the report. (D) The Secretary of Defense and Secretary of Homeland Security shall prescribe regulations to ensure that, for purposes of this paragraph, each Secretary concerned uses the same definition of the term at risk for a difficult transition to civilian life . .\n##### (m) Contracting: standardization\nSuch section is further amended by adding at the end the following new subsection:\n(f) Contracting A Secretary concerned may enter into an agreement with an entity under which such entity shall provide preseparation counseling under this section. If more than one Secretary seeks to enter into such an agreement, such Secretaries concerned shall, to the extent practicable, seek to enter into such agreements with the same entity. .\n##### (n) Yearly surprise audits\nSuch section is further amended by adding at the end the following new subsection:\n(g) Audits (1) Not less than once each year, an employee or contractor of the Department of Veterans Affairs, and an employee or contractor of the Department of Labor, shall make unannounced visits to preseparation counseling under this section in order to audit such counseling. (2) Not later than 90 days after such a visit, the employee or contractor shall submit to the Committees on Armed Services and on Veterans\u2019 Affairs of the Senate and House of Representatives a report regarding such audit. (3) Such employees or contractors shall have expertise regarding matters described in subsection (b). .\n##### (o) Information provided to State veterans agencies regarding members separating from the Armed Forces\n**(1) Expansion**\nSection 570F of the National Defense Authorization Act for Fiscal Year 2020 ( Public Law 116\u201392 ; 10 U.S.C. 1142 note) is amended, in subsection (a)\u2014\n**(A)**\nby redesignating paragraph (8) as paragraph (9); and\n**(B)**\nby inserting, after paragraph (7), the following new paragraph (8):\n(8) Benefits for low-income households, including the supplemental nutrition assistance program (as such term is defined in section 3 of the Food and Nutrition Act of 2008 ( Public Law 88\u2013525 ; 7 U.S.C. 2012 )). .\n**(2) Limitation of voluntary participation**\nSuch section is further amended, in subsection (d), by striking Information and inserting Except for information related to whether an individual is eligible for benefits described in paragraph (8) of subsection (a), information .\n##### (p) Pilot program for military spouses\n**(1) Establishment**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall establish a pilot program for spouses of members of the covered Armed Forces who are eligible to receive preseparation counseling under TAP.\n**(2) Voluntary basis**\nParticipation in the pilot program shall be on a voluntary basis.\n**(3) Curriculum**\nThe Secretary of Defense, in coordination with the Secretary of Veterans Affairs and the Secretary of Labor, shall establish a curriculum based on TAP for the pilot program.\n**(4) Counseling**\nCounseling under the pilot program shall\u2014\n**(A)**\nbe tailored to the military spouse and family;\n**(B)**\nbe offered at least once per calendar quarter at each location selected under paragraph (5);\n**(C)**\nbe offered at times including nights and weekends; and\n**(D)**\ninclude at least one hour regarding benefits and assistance available to military families and veterans from each department under the jurisdiction of the Secretaries specified in subparagraph (C).\n**(5) Locations**\nThe Secretary of Defense shall carry out the pilot program at not fewer than five military installations of each of the covered Armed Forces. One such location shall be located outside the continental United States.\n**(6) Report**\nNot later than one year before the pilot program terminates, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and House of Representatives a report to the regarding the pilot program. Such report shall include elements the Secretary determines appropriate, including whether the pilot program should be made permanent.\n**(7) Termination**\nThe pilot program shall terminate three years after the Secretary of Defense establishes the pilot program.\n**(8) Definitions**\nIn this subsection:\n**(A)**\nThe term covered Armed Force means the Army, Navy, Marine Corps, Air Force, or Space Force.\n**(B)**\nThe term TAP means the Transition Assistance Program under sections 1142 and 1144 of title 10, United States Code.\n##### (q) Reports; tracking system\n**(1) Annual report on TAP participation**\nNot later than one year after the date of the enactment of this Act, and annually thereafter for four years, the Secretary of Defense shall submit to the Committees on Armed Services and on Veterans\u2019 Affairs of the Senate and House of Representatives a report on the Transition Assistance Program at military installations where at least 250 members per year receive preseparation counseling under section 1142 of title 10, United States Code. Such report shall include the following elements with regards to the year preceding the date of such report, disaggregated by military installation:\n**(A)**\nThe number of members described in subsection (a)(1)(B)(ii) of such section 1142, as added by subsection (a), who received fewer than five days of preseparation counseling under such section.\n**(B)**\nThe average period of time between when a member begins to receive preseparation counseling and the day the member separates, retires, or is discharged.\n**(C)**\nThe number of members who began to receive preseparation counseling and then re-enlisted or agreed to a new period of obligated service.\n**(D)**\nThe number of members who began to receive preseparation counseling and then were deployed.\n**(E)**\nThe number of members assigned to each pathway under subsection (c) of such section.\n**(F)**\nThe number of members who, in the course of such preseparation counseling, were referred to another Federal agency or department.\n**(G)**\nThe Federal agencies or departments to which members were so referred.\n**(H)**\nThe number of members who should have been, but were not, so referred, and reasons why such referrals did not occur.\n**(I)**\nThe number of members who receive such preseparation counseling and apply for unemployment compensation under subchapter II of chapter 85 of title 5, United States Code.\n**(J)**\nThe total amount of such unemployment compensation paid to members separating from the Armed Forces.\n**(K)**\nThe frequency with which the commander of the military installation received a briefing regarding attendance of members in accordance with statutory requirements of the Transition Assistance Program.\n**(2) Annual report on TAP curricula**\nNot less than once each year after the date of the enactment of this Act, the Secretaries of Defense, Veterans Affairs, and Labor shall\u2014\n**(A)**\nreview and update curricula under the Transition Assistance Program; and\n**(B)**\nsubmit to Congress copies of such curricula.\n**(3) Tracking of timeliness**\n**(A) Implementation**\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall implement a system to track how many, and what percentage of, members of the Armed Forces begin to receive preseparation counseling within the time periods established in section 1142 of title 10, United States Code.\n**(B) Annual report**\nNot later than two years after the date of the enactment of this Act, and annually thereafter, the Secretary of Defense shall submit to the Committees on Armed Services, and the Committees on Veterans\u2019 Affairs, of the Senate and House of Representatives, a report on data recorded with such tracking system during the year preceding the date of such report. Such report shall include a list of the seven military installations located inside the continental United States, and three military installations located outside the continental United States, where members are least likely to receive TAP preseparation counseling in accordance with such time periods.\n#### 3. Transitional health care for members being separated or recently separated: extension of availability\nSection 1145(a) of title 10, United States Code, is amended\u2014\n**(1)**\nin paragraph (4)\u2014\n**(A)**\nby striking 180 days and inserting 270 days ; and\n**(B)**\nby striking 180-day period and inserting 270-day period ; and\n**(2)**\nin paragraph (7)\u2014\n**(A)**\nby striking 180-day transition period and inserting 270-day transition period ; and\n**(B)**\nby striking 180 days both places it appears and inserting 270 days .\n#### 4. Skillbridge: GAO study\n##### (a) Study required\nThe Comptroller General of the United States shall conduct a study of the Skillbridge programs under section 1143(e) of title 10, United States Code.\n##### (b) Report\nNot later than two years after the date of the enactment of this Act, the Comptroller General shall submit to the Committees on Armed Services, and the Committees on Veterans\u2019 Affairs, of the Senate and House of Representatives, a report regarding such study. Such report shall include observations and recommendations of the Comptroller regarding, with respect to members and employers who participate in Skillbridge\u2014\n**(1)**\ndifferences in criteria for participation between the Armed Forces;\n**(2)**\nother differences in Skillbridge programs between the Armed Forces;\n**(3)**\nbest practices in Skillbridge programs across the Armed Forces, including\u2014\n**(A)**\nthe selection of employers; and\n**(B)**\nthe development of contracts; and\n**(4)**\nthe feasibility of making Skillbridge programs uniform across the Armed Forces.\n#### 5. Website of the Department of Veterans Affairs regarding programs for new veterans\nSection 523 of title 38, United States Code, is amended by adding at the end the following new subsection:\n(c) The Secretary shall maintain a publicly available website of the Department through which a veteran or dependent of a veteran may search by ZIP code for programs for veterans who recently separated from active military, naval, air, or space service, or dependents of such veterans. .\n#### 6. Expansion of eligibility for a certain program of job counseling, training, and placement service for veterans\n##### (a) Definition\nSection 4101 of title 38, United States Code, is amended in paragraph (5)\u2014\n**(1)**\nin subparagraph (A), by striking the comma at the end and inserting a semicolon;\n**(2)**\nin subparagraph (B), by striking power, or and inserting power; ;\n**(3)**\nin subparagraph (C), by striking the period at the end and inserting ; or ; and\n**(4)**\nby adding at the end the following new subparagraph:\n(D) a member of the Armed Forces eligible for the Transition Assistance Program under sections 1142 and 1144 of title 10. .\n##### (b) Outreach\nSection 4103A(a)(1) of such title is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by inserting and certain eligible persons after eligible veterans ;\n**(2)**\nby redesignating subparagraph (C) as subparagraph (D); and\n**(3)**\nby inserting after subparagraph (B) the following new subparagraph (C):\n(C) Eligible persons described in paragraph (5)(D) of section 4101 of this title. .\n#### 7. Solid Start program: interaction with Transition Assistance Program\n##### (a) Clarification of reference to TAP\nSubsection (b) of section 6320 of title 38, United States Code, is amended, in of paragraph (1), by striking transition classes or separation and inserting TAP classes or preseparation counseling .\n##### (b) Provision of TAP materials\nSuch paragraph is further amended\u2014\n**(1)**\nby redesignating subparagraphs (D) through (H) as subparagraphs (E) through (I), respectively; and\n**(2)**\nby inserting after subparagraph (C) the following new subparagraph (D):\n(D) furnishing TAP materials to veterans; .\n##### (c) Assessment of TAP\nSuch paragraph is further amended, in subparagraph (I), as redesignated, by inserting and of TAP before the period.\n##### (d) Definitions\nSuch section is further amended\u2014\n**(1)**\nby striking paragraph (3) of subsection (b); and\n**(2)**\nby adding at the end the following new subsection:\n(c) Definitions In this section: (1) The term TAP means the Transition Assistance Program under sections 1142 and 1144 of title 10. (2) The term Vet Center has the meaning given such term in section 1712A(h) of this title. (3) The term veterans service organization means an organization recognized by the Secretary for the representation of veterans under section 5902 of this title. .",
      "versionDate": "2025-05-14",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Accounting and auditing",
            "updateDate": "2025-06-26T17:46:32Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-26T17:46:22Z"
          },
          {
            "name": "Employment and training programs",
            "updateDate": "2025-06-26T17:47:05Z"
          },
          {
            "name": "Family relationships",
            "updateDate": "2025-06-26T17:46:40Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2025-06-26T17:46:53Z"
          },
          {
            "name": "Intergovernmental relations",
            "updateDate": "2025-06-26T17:46:36Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-26T17:46:59Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-26T17:46:13Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2025-06-26T17:46:28Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-26T17:46:17Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2025-06-26T17:46:47Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-11T14:57:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-05-14",
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
          "measure-id": "id119hr3387",
          "measure-number": "3387",
          "measure-type": "hr",
          "orig-publish-date": "2025-05-14",
          "originChamber": "HOUSE",
          "update-date": "2026-05-15"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr3387v00",
            "update-date": "2026-05-15"
          },
          "action-date": "2025-05-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Enhancing the Transitioning Servicemember\u2019s Experience Act or the ETS Act</strong></p><p>This bill expands the provision of pre-separation counseling\u00a0under the Transition Assistance Program (TAP) and\u00a0other services for members of the Armed Forces who are transitioning to civilian life.</p><p>Regarding pre-separation counseling under TAP, the bill</p><ul><li>sets a minimum\u00a0duration of counseling depending on a member's post-service employment, education, or training status;</li><li>prohibits individuals who are responsible for the retention of members in any of the Armed Forces from providing counseling;</li><li>removes restrictions on the types of counseling for which a spouse of a member may be included;</li><li>expands financial planning counseling to include information about debt and investing;</li><li>requires that financial planning counseling be provided by an individual who has significant experience in financial planning; and</li><li>requires the Department of Veterans Affairs (VA) and Department of Labor to audit counseling annually.</li></ul><p>If a military department determines an individual is at risk for a difficult transition to civilian life, that department must provide the individual's information to the VA\u00a0and Labor. The VA and Labor must timely contact\u00a0the individual, as specified.</p><p>Additionally, the bill extends transitional health care for members separating from service to 270 days (currently 180).</p><p>The bill also</p><ul><li>expands eligibility for certain Labor job counseling, training, and placement services for veterans to members of the Armed Forces who are eligible for TAP; and</li><li>expands the Solid Start program by requiring the VA to provide TAP materials to veterans and analyze data assessing the effectiveness of TAP.</li></ul>"
        },
        "title": "ETS Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr3387.xml",
    "summary": {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Enhancing the Transitioning Servicemember\u2019s Experience Act or the ETS Act</strong></p><p>This bill expands the provision of pre-separation counseling\u00a0under the Transition Assistance Program (TAP) and\u00a0other services for members of the Armed Forces who are transitioning to civilian life.</p><p>Regarding pre-separation counseling under TAP, the bill</p><ul><li>sets a minimum\u00a0duration of counseling depending on a member's post-service employment, education, or training status;</li><li>prohibits individuals who are responsible for the retention of members in any of the Armed Forces from providing counseling;</li><li>removes restrictions on the types of counseling for which a spouse of a member may be included;</li><li>expands financial planning counseling to include information about debt and investing;</li><li>requires that financial planning counseling be provided by an individual who has significant experience in financial planning; and</li><li>requires the Department of Veterans Affairs (VA) and Department of Labor to audit counseling annually.</li></ul><p>If a military department determines an individual is at risk for a difficult transition to civilian life, that department must provide the individual's information to the VA\u00a0and Labor. The VA and Labor must timely contact\u00a0the individual, as specified.</p><p>Additionally, the bill extends transitional health care for members separating from service to 270 days (currently 180).</p><p>The bill also</p><ul><li>expands eligibility for certain Labor job counseling, training, and placement services for veterans to members of the Armed Forces who are eligible for TAP; and</li><li>expands the Solid Start program by requiring the VA to provide TAP materials to veterans and analyze data assessing the effectiveness of TAP.</li></ul>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr3387"
    },
    "title": "ETS Act"
  },
  "summaries": [
    {
      "actionDate": "2025-05-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Enhancing the Transitioning Servicemember\u2019s Experience Act or the ETS Act</strong></p><p>This bill expands the provision of pre-separation counseling\u00a0under the Transition Assistance Program (TAP) and\u00a0other services for members of the Armed Forces who are transitioning to civilian life.</p><p>Regarding pre-separation counseling under TAP, the bill</p><ul><li>sets a minimum\u00a0duration of counseling depending on a member's post-service employment, education, or training status;</li><li>prohibits individuals who are responsible for the retention of members in any of the Armed Forces from providing counseling;</li><li>removes restrictions on the types of counseling for which a spouse of a member may be included;</li><li>expands financial planning counseling to include information about debt and investing;</li><li>requires that financial planning counseling be provided by an individual who has significant experience in financial planning; and</li><li>requires the Department of Veterans Affairs (VA) and Department of Labor to audit counseling annually.</li></ul><p>If a military department determines an individual is at risk for a difficult transition to civilian life, that department must provide the individual's information to the VA\u00a0and Labor. The VA and Labor must timely contact\u00a0the individual, as specified.</p><p>Additionally, the bill extends transitional health care for members separating from service to 270 days (currently 180).</p><p>The bill also</p><ul><li>expands eligibility for certain Labor job counseling, training, and placement services for veterans to members of the Armed Forces who are eligible for TAP; and</li><li>expands the Solid Start program by requiring the VA to provide TAP materials to veterans and analyze data assessing the effectiveness of TAP.</li></ul>",
      "updateDate": "2026-05-15",
      "versionCode": "id119hr3387"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3387ih.xml"
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
      "title": "ETS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ETS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Enhancing the Transitioning Servicemember\u2019s Experience Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 10 and 38, United States Code, to make improvements to certain programs for a member nearing separation, or for a veteran who recently separated, from the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:03:40Z"
    }
  ]
}
```
