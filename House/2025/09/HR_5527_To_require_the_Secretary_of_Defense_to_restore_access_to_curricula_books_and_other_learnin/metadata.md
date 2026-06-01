# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5527?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5527
- Title: Stop Censoring Military Families Act
- Congress: 119
- Bill type: HR
- Bill number: 5527
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2026-03-04T09:06:34Z
- Update date including text: 2026-03-04T09:06:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-19 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-09-19 - IntroReferral: Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5527",
    "number": "5527",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000606",
        "district": "8",
        "firstName": "Jamie",
        "fullName": "Rep. Raskin, Jamie [D-MD-8]",
        "lastName": "Raskin",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "Stop Censoring Military Families Act",
    "type": "HR",
    "updateDate": "2026-03-04T09:06:34Z",
    "updateDateIncludingText": "2026-03-04T09:06:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-19",
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
      "text": "Referred to the Committee on Armed Services, and in addition to the Committee on Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:01:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-09-19T13:01:15Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "PA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "TX"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "GA"
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
      "sponsorshipDate": "2025-09-19",
      "state": "DC"
    },
    {
      "bioguideId": "J000305",
      "district": "51",
      "firstName": "Sara",
      "fullName": "Rep. Jacobs, Sara [D-CA-51]",
      "isOriginalCosponsor": "True",
      "lastName": "Jacobs",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "MA"
    },
    {
      "bioguideId": "J000298",
      "district": "7",
      "firstName": "Pramila",
      "fullName": "Rep. Jayapal, Pramila [D-WA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Jayapal",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "WA"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "GA"
    },
    {
      "bioguideId": "F000476",
      "district": "10",
      "firstName": "Maxwell",
      "fullName": "Rep. Frost, Maxwell [D-FL-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Frost",
      "party": "D",
      "sponsorshipDate": "2025-09-30",
      "state": "FL"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary Gay",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
    },
    {
      "bioguideId": "T000472",
      "district": "39",
      "firstName": "Mark",
      "fullName": "Rep. Takano, Mark [D-CA-39]",
      "isOriginalCosponsor": "False",
      "lastName": "Takano",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "CA"
    },
    {
      "bioguideId": "C001123",
      "district": "31",
      "firstName": "Gilbert",
      "fullName": "Rep. Cisneros, Gilbert Ray [D-CA-31]",
      "isOriginalCosponsor": "False",
      "lastName": "Cisneros",
      "middleName": "Ray",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
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
      "sponsorshipDate": "2025-12-01",
      "state": "MN"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2026-01-13",
      "state": "MO"
    },
    {
      "bioguideId": "L000560",
      "district": "2",
      "firstName": "Rick",
      "fullName": "Rep. Larsen, Rick [D-WA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Larsen",
      "party": "D",
      "sponsorshipDate": "2026-02-02",
      "state": "WA"
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
      "sponsorshipDate": "2026-02-20",
      "state": "IL"
    },
    {
      "bioguideId": "W000808",
      "district": "24",
      "firstName": "Frederica",
      "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
      "isOriginalCosponsor": "False",
      "lastName": "Wilson",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "FL"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5527ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5527\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Raskin (for himself, Ms. Houlahan , Mr. Doggett , Mr. Johnson of Georgia , Ms. Norton , Ms. Jacobs , Mr. McGovern , and Ms. Jayapal ) introduced the following bill; which was referred to the Committee on Armed Services , and in addition to the Committee on Education and Workforce , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo require the Secretary of Defense to restore access to curricula, books, and other learning materials at schools operated by the Department of Defense Education Activity, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Censoring Military Families Act .\n#### 2. Restoration of access to curricula, books, and other learning materials\n##### (a) Restoration and temporary limitation on further restrictions\n**(1) Restoration**\nAs soon as practicable after the date of the enactment of this Act, but not later than 30 days after such date, the Secretary of Defense shall restore access to all curricula, books, and other learning materials that were available at covered educational institutions before January 20, 2025.\n**(2) Limitation**\nThe Secretary of Defense may not take any action that would limit the availability of the materials described in paragraph (1) until after the beginning of the 2026\u20132027 academic year.\n##### (b) Report required\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the appropriate congressional committees a report that includes\u2014\n**(1)**\nidentification of all curricula, books, or other learning materials identified for potential removal pursuant to instructions issued by the Secretary of Defense after January 20, 2025;\n**(2)**\na detailed account of the processes and instructions used to carry out such actions; and\n**(3)**\nin the case of any such actions affecting schools operated by the Department of Defense Education Activity, an explanation of whether such actions complied with the requirements of section 2164a of title 10, United States Code.\n##### (c) Definitions\nIn this section:\n**(1)**\nThe term covered educational institution means a school operated by the Department of Defense Education Activity.\n**(2)**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Education and Workforce of the House of Representatives; and\n**(B)**\nthe Committee on Armed Services and the Committee on Health, Education, Labor, and Pensions of the Senate.\n#### 3. Limitations on further restrictions to curricula, books, other learning materials, and cultural events\n##### (a) In general\nSection 2164 of title 10, United States Code, is amended by adding at the end the following new subsection:\n(n) Limitation on restrictions to curricula, learning materials, and cultural events (1) The Secretary of Defense may not issue any directive affecting the curriculum, program of instruction, administration, or personnel of two or more schools operated by the Department of Defense Education Activity until one year after the following requirements have been met: (A) The Secretary has submitted to the School Advisory Committee (or the equivalent advisory body) and Installation Advisory Committee of the schools involved and to the Committees on Armed Services of the Senate and the House of Representatives written notice of the Secretary\u2019s intent to issue such directive together with a description of and justification for the directive. (B) Each School Advisory Committee (or the equivalent advisory body) that received the notice under subparagraph (A)\u2014 (i) with respect to a directive pertaining to curricula or programs of instruction, has voted to initiate the CMRC process with regard to the directive; or (ii) with respect to a directive pertaining to administration or personnel\u2014 (I) has voted to initiate the CMRC process with regard to the directive; or (II) in lieu of initiating such process, has conducted a review to determine how the directive will affect the school involved, produced a written response setting forth the results of the review, and approved such response via an official vote. (C) The findings of such process or review (as the case may be) were submitted to the Committees on Armed Services of the Senate and the House of Representatives not later than 90 days after the process or review was initiated, and such Committees have had an opportunity to consider potential legislative responses to the proposed directive. (2) The Secretary of Defense may not issue any directive affecting the curriculum, program of instruction, administration, or personnel of two or more schools operated by the Department of Defense Education Activity unless\u2014 (A) the Secretary submits to the School Advisory Committee (or the equivalent advisory body) of the schools involved and the Committees on Armed Services of the Senate and the House of Representatives written notice of the Secretary\u2019s intent to issue such directive together with a description of and justification for the directive; and (B) a period of 90 days has elapsed following the date on which such notice was submitted. (3) The requirements of paragraphs (1) and (2) shall apply to directives affecting two or more schools operated by the Department of Defense Education Activity regardless of whether such directives are issued collectively or separately to individual schools. (4) The Secretary of Defense may not issue any directive affecting the selection or removal of library resources, textbooks, or other printed or published instructional materials at any individual school operated by the Department of Defense Education Activity unless\u2014 (A) the Secretary submits to the School Advisory Committee (or the equivalent advisory body) of the school involved written notice of the Secretary\u2019s intent to issue such directive together with a description of and justification for the directive; and (B) a period of 30 days has elapsed following the date on which such notice was submitted. (5) The Secretary of Defense may not\u2014 (A) limit the authority of an individual school to plan or hold commemorative events or cultural events that have been duly approved by the principal, faculty, staff, or School Advisory Committee (or the equivalent) of the school involved; or (B) withhold funding or take other action against a school solely because such school plans or holds an event described in subparagraph (A). (6) In this subsection, the term CMRC process means the procedures described in Department of Defense Education Activity Administrative Instruction 2992.01 relating to \u2018Information Center and Classroom Supplemental Materials Selection Policy and Challenge Procedures\u2019, dated February 12, 2010. .\n##### (b) Effective date and applicability\nThe amendments made by subsection (a) shall take effect on the date of the enactment of this Act and shall apply beginning with the 2026\u20132027 academic year for schools operated by the Department of Defense Education Activity.\n#### 4. Nullification of certain Executive Orders\n##### (a) In general\nThe Executive orders specified in subsection (b) shall have no force or effect with respect to the Department of Defense and no Federal funds may be used to implement or enforce such Executive orders, or any substantially similar directives, within the Department of Defense.\n##### (b) Executive orders specified\nThe Executive orders specified in this subsection are the following:\n**(1)**\nExecutive Order 14190 (90 Fed. Reg. 8853; relating to ending radical indoctrination in K\u201312 schooling).\n**(2)**\nExecutive Order 14280 (90 Fed. Reg. 17533; relating to reinstating commonsense school discipline policies).\n**(3)**\nExecutive Order 14281 (90 Fed. Reg 17537; relating to restoring equality of opportunity and meritocracy).\n**(4)**\nExecutive Order 14185 (90 Fed. Reg. 8763; relating to restoring America\u2019s fighting force).\n**(5)**\nExecutive Order 14183 (90 Fed. Reg. 8757; relating to prioritizing military excellence and readiness).\n**(6)**\nExecutive Order 14168 (90 Fed. Reg. 8615; relating to defending women from gender ideology extremism and restoring biological truth to the Federal Government).\n**(7)**\nExecutive Order 14201 (90 Fed. Reg 9279; relating to keeping men out of women\u2019s sports).\n#### 5. Study and report on potential establishment of independent body to implement curricula for DODEA schools\n##### (a) In general\nThe Comptroller General of the United States shall conduct a study to determine the feasability and advisability of establishing an independent body to design and implement educational curricula for schools operated by the Department of Defense Education Activity. The study shall address\u2014\n**(1)**\nhow such an independent body could be established and structured;\n**(2)**\nwho should be appointed to such a body;\n**(3)**\nhow such body could maintain independence to ensure it is insulated from political influence and changing priorities of the Executive Branch; and\n**(4)**\nsuch other factors as the Comptroller General determines appropriate.\n##### (b) Report\nNot later than 270 days after the date of the enactment of this Act, the Comptroller General shall submit to the appropriate congressional committees a report on the results of the study conducted under subsection (a).\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Armed Services and the Committee on Education and Workforce of the House of Representatives; and\n**(2)**\nthe Committee on Armed Services and the Committee on Health, Education, Labor, and Pensions of the Senate.",
      "versionDate": "2025-09-19",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-25T18:41:52Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5527ih.xml"
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
      "title": "Stop Censoring Military Families Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-04T04:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Censoring Military Families Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-04T04:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Defense to restore access to curricula, books, and other learning materials at schools operated by the Department of Defense Education Activity, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-04T04:48:17Z"
    }
  ]
}
```
