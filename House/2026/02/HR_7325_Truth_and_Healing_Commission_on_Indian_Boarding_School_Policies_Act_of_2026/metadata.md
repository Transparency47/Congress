# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7325?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7325
- Title: Truth and Healing Commission on Indian Boarding School Policies Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7325
- Origin chamber: House
- Introduced date: 2026-02-03
- Update date: 2026-05-05T08:06:29Z
- Update date including text: 2026-05-05T08:06:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2026-02-03: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2026-02-03: Introduced in House

## Actions

- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Introduced in House
- 2026-02-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-02-03 - IntroReferral: Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-03",
    "latestAction": {
      "actionDate": "2026-02-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7325",
    "number": "7325",
    "originChamber": "House",
    "policyArea": {
      "name": "Native Americans"
    },
    "sponsors": [
      {
        "bioguideId": "C001053",
        "district": "4",
        "firstName": "Tom",
        "fullName": "Rep. Cole, Tom [R-OK-4]",
        "lastName": "Cole",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-05T08:06:29Z",
    "updateDateIncludingText": "2026-05-05T08:06:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
      "committees": {
        "item": {
          "name": "Natural Resources Committee",
          "systemCode": "hsii00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-03",
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
      "text": "Referred to the Committee on Education and Workforce, and in addition to the Committee on Natural Resources, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-03",
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
          "date": "2026-02-03T15:00:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Natural Resources Committee",
      "systemCode": "hsii00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2026-02-03T15:00:05Z",
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
      "bioguideId": "D000629",
      "district": "3",
      "firstName": "Sharice",
      "fullName": "Rep. Davids, Sharice [D-KS-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Davids",
      "party": "D",
      "sponsorshipDate": "2026-02-03",
      "state": "KS"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "AZ"
    },
    {
      "bioguideId": "F000459",
      "district": "3",
      "firstName": "Charles",
      "fullName": "Rep. Fleischmann, Charles J. \"Chuck\" [R-TN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Fleischmann",
      "middleName": "J. \"Chuck\"",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "TN"
    },
    {
      "bioguideId": "N000189",
      "district": "4",
      "firstName": "Dan",
      "fullName": "Rep. Newhouse, Dan [R-WA-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Newhouse",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "WA"
    },
    {
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "MI"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NY"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2026-02-04",
      "state": "NE"
    },
    {
      "bioguideId": "Y000067",
      "district": "2",
      "firstName": "Rudy",
      "fullName": "Rep. Yakym, Rudy [R-IN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Yakym",
      "party": "R",
      "sponsorshipDate": "2026-02-09",
      "state": "IN"
    },
    {
      "bioguideId": "F000484",
      "district": "6",
      "firstName": "Randy",
      "fullName": "Rep. Fine, Randy [R-FL-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Fine",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "FL"
    },
    {
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "IN"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "CA"
    },
    {
      "bioguideId": "E000071",
      "district": "6",
      "firstName": "Jake",
      "fullName": "Rep. Ellzey, Jake [R-TX-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Ellzey",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "TX"
    },
    {
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "FL"
    },
    {
      "bioguideId": "M001194",
      "district": "2",
      "firstName": "John",
      "fullName": "Rep. Moolenaar, John R. [R-MI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Moolenaar",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2026-03-18",
      "state": "MI"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "M001219",
      "district": "0",
      "firstName": "James",
      "fullName": "Del. Moylan, James C. [R-GU-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Moylan",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2026-04-14",
      "state": "GU"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2026-05-04",
      "state": "KS"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7325ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7325\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 3, 2026 Mr. Cole (for himself and Ms. Davids of Kansas ) introduced the following bill; which was referred to the Committee on Education and Workforce , and in addition to the Committee on Natural Resources , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo establish the Truth and Healing Commission on Indian Boarding School Policies in the United States, and for other purposes.\n#### 1. Short title; table of contents\n##### (a) Short title\nThis Act may be cited as the Truth and Healing Commission on Indian Boarding School Policies Act of 2026 .\n##### (b) Table of contents\nThe table of contents for this Act is as follows:\nSec. 1. Short title; table of contents.\nSec. 2. Purposes.\nSec. 3. Definitions.\nTITLE I\u2014Commission and Subcommittee\nSubtitle A\u2014Truth and Healing Commission on Indian Boarding School Policies in the United States\nSec. 101. Truth and Healing Commission on Indian Boarding School Policies in the United States.\nSubtitle B\u2014Duties of the Commission\nSec. 111. Duties of the Commission.\nSubtitle C\u2014Survivors Truth and Healing Subcommittee\nSec. 121. Survivors Truth and Healing Subcommittee.\nTITLE II\u2014Advisory Committees\nSubtitle A\u2014Native American Truth and Healing Advisory Committee\nSec. 201. Native American Truth and Healing Advisory Committee.\nSubtitle B\u2014Federal and Religious Truth and Healing Advisory Committee\nSec. 211. Federal and Religious Truth and Healing Advisory Committee.\nTITLE III\u2014General Provisions\nSec. 301. Clarification.\nSec. 302. Burial management.\nSec. 303. Co-stewardship agreements.\nSec. 304. No right of action.\n#### 2. Purposes\nThe purposes of this Act are\u2014\n**(1)**\nto establish a Truth and Healing Commission on Indian Boarding School Policies in the United States, including other necessary advisory committees and subcommittees;\n**(2)**\nto formally investigate, document, and report on the histories of Indian Boarding Schools, Indian Boarding School Polices, and the systematic and long-term effects of those schools and policies on Native American peoples;\n**(3)**\nto develop recommendations for Federal efforts based on the findings of the Commission; and\n**(4)**\nto promote healing for survivors of Indian Boarding Schools, the descendants of those survivors, and the communities of those survivors.\n#### 3. Definitions\nIn this Act:\n**(1) Commission**\nThe term Commission means the Truth and Healing Commission on Indian Boarding School Policies in the United States established by section 101(a).\n**(2) Federal and religious truth and healing advisory committee**\nThe term Federal and Religious Truth and Healing Advisory Committee means the Federal and Religious Truth and Healing Advisory Committee established by section 211(a).\n**(3) Indian**\nThe term Indian has the meaning given the term in section 6151 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7491 ).\n**(4) Indian boarding school**\nThe term Indian Boarding School means\u2014\n**(A)**\na site of an institution that\u2014\n**(i)**\nprovided on-site housing or overnight lodging;\n**(ii)**\nwas described in Federal records as providing formal academic or vocational training and instruction to Native Americans;\n**(iii)**\nreceived Federal funds or other Federal support; and\n**(iv)**\nwas operational before 1969;\n**(B)**\na site of an institution identified by the Department of the Interior in appendices A and B of the report entitled Federal Indian Boarding School Initiative Investigative Report and dated May 2022 (or a successor report); or\n**(C)**\nany other institution that implemented Indian Boarding School Policies, including an Indian day school.\n**(5) Indian boarding school policies**\nThe term Indian Boarding School Policies means Federal laws, policies, and practices purported to assimilate and civilize Native Americans that included psychological, physical, sexual, and mental abuse, forced removal from home or community, and identity-altering practices intended to terminate Native languages, cultures, religions, social organizations, or connections to traditional land.\n**(6) Indian tribe**\nThe term Indian Tribe has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\n**(7) Native american**\nThe term Native American means an individual who is\u2014\n**(A)**\nan Indian; or\n**(B)**\na Native Hawaiian.\n**(8) Native american truth and healing advisory committee**\nThe term Native American Truth and Healing Advisory Committee means the Native American Truth and Healing Advisory Committee established by the Commission under section 201(a).\n**(9) Native hawaiian**\nThe term Native Hawaiian has the meaning given the term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ).\n**(10) Native hawaiian organization**\nThe term Native Hawaiian organization means a private nonprofit organization that\u2014\n**(A)**\nserves and represents the interests of Native Hawaiians;\n**(B)**\nhas as its primary and stated purpose the provision of services to Native Hawaiians;\n**(C)**\nhas Native Hawaiians serving in substantive and policymaking positions; and\n**(D)**\nhas expertise in Native Hawaiian affairs.\n**(11) Office of hawaiian affairs**\nThe term Office of Hawaiian Affairs has the meaning given the term in section 6207 of the Elementary and Secondary Education Act of 1965 ( 20 U.S.C. 7517 ).\n**(12) Survivors truth and healing subcommittee**\nThe term Survivors Truth and Healing Subcommittee means the Survivors Truth and Healing Subcommittee established by section 121(a).\n**(13) Trauma-informed care**\nThe term trauma-informed care means holistic psychological and health care practices that include promoting culturally responsive practices, patient psychological, physical, and emotional safety, and environments of healing, trust, peer support, and recovery.\n**(14) Tribal organization**\nThe term Tribal organization has the meaning given the term in section 4 of the Indian Self-Determination and Education Assistance Act ( 25 U.S.C. 5304 ).\nI\nCommission and Subcommittee\nA\nTruth and Healing Commission on Indian Boarding School Policies in the United States\n#### 101. Truth and Healing Commission on Indian Boarding School Policies in the United States\n##### (a) Establishment\nThere is established in the legislative branch a commission, to be known as the Truth and Healing Commission on Indian Boarding School Policies in the United States .\n##### (b) Membership\n**(1) Appointment**\nNominees submitted under paragraph (2)(A) shall be appointed as members to the Commission as follows:\n**(A)**\n1 member shall be appointed by the majority leader of the Senate, in consultation with the Chairperson of the Committee on Indian Affairs of the Senate.\n**(B)**\n1 member shall be appointed by the minority leader of the Senate, in consultation with the Vice Chairperson of the Committee on Indian Affairs of the Senate.\n**(C)**\n1 member shall be appointed by the Speaker of the House of Representatives, in consultation with the Chair of the Committee on Natural Resources of the House of Representatives.\n**(D)**\n1 member shall be appointed by the minority leader of the House of Representatives, in consultation with the Ranking Member of the Committee on Natural Resources of the House of Representatives.\n**(E)**\n1 member shall be jointly appointed by the Chairperson and Vice Chairperson of the Committee on Indian Affairs of the Senate.\n**(2) Nominations**\n**(A) In general**\nNot later than 90 days after the date of the enactment of this Act, Indian Tribes, Tribal organizations, Native Americans, the Office of Hawaiian Affairs, and Native Hawaiian organizations may submit to the Secretary of the Interior nominations for individuals to be appointed as members of the Commission.\n**(B) Submission to congress**\nNot later than 7 days after the submission deadline for nominations described in subparagraph (A), the Secretary of the Interior shall submit to Congress a list of the individuals nominated under that subparagraph.\n**(C) Qualifications**\n**(i) In general**\nNominees to serve on the Commission shall have significant experience in matters relating to\u2014\n**(I)**\noverseeing or leading complex research initiatives with and for Indian Tribes and Native Americans;\n**(II)**\nindigenous human rights law and policy;\n**(III)**\nTribal court judicial and restorative justice systems and Federal agencies, such as participation as a Tribal judge, researcher, or former presidentially appointed commissioner;\n**(IV)**\nproviding and coordinating trauma-informed care and other health-related services to Indian Tribes and Native Americans; or\n**(V)**\ntraditional and cultural resources and practices in Native communities.\n**(ii) Additional qualifications**\nIn addition to the qualifications described in clause (i), each member of the Commission shall be an individual of recognized integrity and empathy, with a demonstrated commitment to the values of truth, reconciliation, healing, and expertise in truth and healing endeavors that are traditionally and culturally appropriate so as to provide balanced points of view and expertise with respect to the duties of the Commission.\n**(3) Date**\nMembers of the Commission under paragraph (1) shall be appointed not later than 180 days after the date of the enactment of this Act.\n**(4) Period of appointment; vacancies; removal**\n**(A) Period of appointment**\nA member of the Commission shall be appointed for a term that is the shorter of\u2014\n**(i)**\n6 years; and\n**(ii)**\nthe life of the Commission.\n**(B) Vacancies**\nAfter all initial members of the Commission are appointed and the initial business meeting of the Commission has been convened under subsection (c)(1), a single vacancy in the Commission\u2014\n**(i)**\nshall not affect the powers of the Commission; and\n**(ii)**\nshall be filled within 90 days in the same manner as was the original appointment.\n**(C) Removal**\nA quorum of members of the Commission may remove a member of the Commission only for neglect of duty or malfeasance.\n**(5) Termination**\nThe Commission shall terminate 6 years after the date of the enactment of this Act.\n**(6) Limitation**\nNo member of the Commission may otherwise be an officer or employee of the Federal Government.\n##### (c) Business meetings\n**(1) Initial business meeting**\n90 days after the date on which all of the members of the Commission are appointed under subsection (b)(1)(A), the Commission shall hold the initial business meeting of the Commission\u2014\n**(A)**\nto appoint a Chairperson, a Vice Chairperson, and such other positions as determined necessary by the Commission;\n**(B)**\nto establish rules for meetings of the Commission; and\n**(C)**\nto appoint members of\u2014\n**(i)**\nthe Survivors Truth and Healing Subcommittee under section 121(b)(1); and\n**(ii)**\nthe Native American Truth and Healing Advisory Committee under section 201(b)(1).\n**(2) Subsequent business meetings**\nAfter the initial business meeting of the Commission is held under paragraph (1), the Commission shall meet at the call of the Chairperson.\n**(3) Advisory and subcommittee committees designees**\nEach Commission business meeting shall include participation by 2 non-voting designees from each of the Survivors Truth and Healing Subcommittee, the Native American Truth and Healing Advisory Committee, and the Federal and Religious Truth and Healing Advisory Committee, as appointed in accordance with section 121(c)(1)(D), section 201(e)(1)(C), and section 211(c)(1)(B), as applicable.\n**(4) Format of meetings**\nA business meeting of the Commission may be conducted in-person or virtually.\n**(5) Quorum required**\nA business meeting of the Commission may be held only after a quorum, established in accordance with subsection (d), is present.\n##### (d) Quorum\nA simple majority of the members of the Commission shall constitute a quorum for a business meeting.\n##### (e) Rules\nThe Commission may establish, by a majority vote, any rules for the conduct of Commission business, in accordance with this section and other applicable law.\n##### (f) Commission personnel matters\n**(1) Compensation of commissioners**\nA member of the Commission shall be compensated at a daily equivalent of the annual rate of basic pay prescribed for grade 5 of the General Schedule under section 5332 of title 5, United States Code, for each day, not to exceed 10 days per month, for which a member is engaged in the performance of their duties under this Act, limited to convening meetings, including public or private meetings to receive testimony in furtherance of the duties of the Commission and the purposes of this Act.\n**(2) Travel expenses**\nA member of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Commission.\n**(3) Detail of government employees**\nAny Federal Government employee, with the approval of the head of the appropriate Federal agency and at the request of the Commission, may be detailed to the Commission without\u2014\n**(A)**\nreimbursement to the agency of that employee; and\n**(B)**\ninterruption or loss of civil service status, benefits, or privileges.\n##### (g) Powers of commission\n**(1) Convenings and information**\nThe Commission may, for the purpose of carrying out this Act\u2014\n**(A)**\nhold such convenings and sit and act at such times and places, take such testimony, and receive such information, virtually or in-person, as the Commission may determine necessary to accomplish the purposes of this Act;\n**(B)**\nconduct or request such interdisciplinary research, investigation, or analysis of such information and documents, records, or other data as the Commission may determine necessary to accomplish the purposes of this Act, including\u2014\n**(i)**\nsecuring, directly from a Federal agency, such information as the Commission considers necessary to accomplish the purposes of this Act; and\n**(ii)**\nrequesting the head of any relevant Tribal or State agency to provide to the Commission such information as the Commission considers necessary to accomplish the purposes of this Act;\n**(C)**\nrequest such records, papers, correspondence, memoranda, documents, books, videos, oral histories, recordings, or any other paper or electronic material, as the Commission may determine necessary to accomplish the purposes of this Act;\n**(D)**\noversee, direct, and collaborate with the Federal and Religious Truth and Healing Advisory Committee, the Native American Truth and Healing Advisory Committee, and the Survivors Truth and Healing Subcommittee to accomplish the purposes of this Act; and\n**(E)**\ncoordinate with Federal and non-Federal entities to preserve and archive, as appropriate, any gifts, documents, or other property received while carrying out the purposes of this Act.\n**(2) Contracting; volunteer services**\n**(A) Contracting**\nThe Commission may, to such extent and in such amounts as are provided in appropriations Acts, and in accordance with applicable law, enter into contracts and other agreements with public agencies, private organizations, and individuals to enable the Commission to carry out the duties of the Commission under this Act.\n**(B) Volunteer and uncompensated services**\nNotwithstanding section 1342 of title 31, United States Code, the Commission may accept and use such voluntary and uncompensated services as the Commission determines to be necessary.\n**(C) General services administration**\nThe Administrator of General Services shall provide, on request of the Commission, on a reimbursable basis, administrative support and other services for the performance of the functions of the Commission under this Act.\n**(3) Postal services**\nThe Commission may use the United States mails in the same manner and under the same conditions as other agencies of the Federal Government.\n**(4) Gifts, fundraising, and disbursement**\n**(A) Gifts and donations**\n**(i) In general**\nThe Commission may accept, use, and dispose of any gift, donation, service, property, or other record or recording to accomplish the purposes of this Act.\n**(ii) Return of gifts and donations**\nOn termination of the Commission under subsection (b)(5), any gifts, unspent donations, property, or other record or recording accepted by the Commission under clause (i) shall be\u2014\n**(I)**\nreturned to the donor that made the donation under that clause; or\n**(II)**\narchived under subparagraph (E).\n**(B) Fundraising**\nThe Commission may, on the affirmative vote of 3\u20445 of the members of the Commission, solicit funds to accomplish the purposes of this Act.\n**(C) Disbursement**\nThe Commission may, on the affirmative vote of 3\u20445 of the members of the Commission, approve a spending plan of funds to accomplish the purposes of this Act.\n**(D) Tax documents**\nThe Commission (or a designee) shall, on request of a donor under subparagraph (A) or (B), provide tax documentation to that donor for any tax-deductible gift made by that donor under those subparagraphs.\n**(E) Archiving**\nThe Commission shall coordinate with the Library of Congress and the Smithsonian Institution to archive and preserve relevant gifts or donations received under subparagraph (A) or (B).\n##### (h) Convening\n**(1) Convening protocol**\n**(A) In general**\nNot later than 45 days after the initial business meeting of the Native American Truth and Healing Advisory Committee, the Commission, 3 designees from the Native American Truth and Healing Advisory Committee, and 3 designees from the Survivors Truth and Healing Subcommittee shall hold a meeting to recommend rules, protocols, and formats for convenings carried out under this subsection.\n**(B) Rules and protocols**\nNot later than 45 days after the initial meeting described in subparagraph (A), the Commission shall finalize rules, protocols, and formats for convenings carried out under this subsection by a 3\u20445 majority in attendance at a meeting of the Commission.\n**(C) Additional meetings**\nThe Commission and designees described in subparagraph (A) may hold additional meetings, as necessary, to amend, by a 3\u20445 majority in attendance at a meeting of the Commission, the rules, protocols, and formats for convenings established under that subparagraph.\n**(2) Announcement of convenings**\nNot later than 30 days before the date of a convening under this subsection, the Commission shall announce the location and details of the convening.\n**(3) Minimum number of convenings**\nThe Commission shall hold\u2014\n**(A)**\nnot fewer than 1 convening in each of the 12 regions of the Bureau of Indian Affairs and in Hawai\u2018i during the life of the Commission; and\n**(B)**\nbeginning 1 year after the date of the enactment of this Act, not fewer than 1 convening in each quarter to receive testimony each calendar year until the date on which the Commission submits the final report of the Commission under section 111(e)(3).\n**(4) Opportunity to provide testimony**\nNo person or entity shall be denied the opportunity to provide relevant testimony or information at a convening held under this subsection, except at the discretion of the Chairperson of the Commission (or a designee).\n##### (i) Federal advisory committee act applicability\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), shall not apply to the Commission.\n##### (j) Congressional Accountability Act applicability\nFor purposes of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. )\u2014\n**(1)**\nany individual who is an employee of the Commission shall be considered a covered employee under the Act;\n**(2)**\nthe Commission shall be considered an employing office under the Act; and\n**(3)**\na member of the Commission shall be considered a covered employee under the Act.\n##### (k) Consultation or engagement with Native Americans, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations\nIn carrying out the duties of the Commission under section 111, the Commission shall meaningfully consult or engage, as appropriate, in a timely manner with Native Americans, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations.\n##### (l) Funding\nOf the amounts authorized to be appropriated pursuant to section 105 of the Indian Land Consolidation Act Amendments of 2000 ( 25 U.S.C. 2201 note; Public Law 106\u2013462 ) and section 403 of the Indian Financing Act of 1974 ( 25 U.S.C. 1523 ), $90,000,000 shall be used to carry out this Act.\nB\nDuties of the Commission\n#### 111. Duties of the Commission\n##### (a) Investigation\n**(1) In general**\nThe Commission shall conduct a comprehensive interdisciplinary investigation of Indian Boarding School Policies, including the social, cultural, economic, emotional, and physical effects of Indian Boarding School Policies in the United States on Native American communities, Indian Tribes, survivors of Indian Boarding Schools, families of those survivors, and their descendants.\n**(2) Matters to be investigated**\nThe matters to be investigated by the Commission under paragraph (1) shall include, at a minimum\u2014\n**(A)**\nconducting a comprehensive review of existing research and historical records of Indian Boarding School Policies and any documentation, scholarship, or other resources relevant to the purposes of this Act from\u2014\n**(i)**\nany archive or any other document storage location, notwithstanding the location of that archive or document storage location; and\n**(ii)**\nany research conducted by private individuals, private entities, and non-Federal Government entities, whether domestic or foreign, including religious institutions;\n**(B)**\ncollaborating with the Federal and Religious Truth and Healing Advisory Committee to obtain all relevant information from\u2014\n**(i)**\nthe Department of the Interior, the Department of Health and Human Services, other relevant Federal agencies, and institutions or organizations, including religious institutions or organizations, that operated an Indian Boarding School, carried out Indian Boarding School Policies, or have information that the Commission determines to be relevant to the investigation of the Commission; and\n**(ii)**\nIndian Tribes, Tribal organizations, Native Americans, the Office of Hawaiian Affairs, and Native Hawaiian organizations; and\n**(C)**\nconducting a comprehensive assessment of the impacts of Indian Boarding School Policies on Native American students and alumni, including the impact on cultures, traditions, and languages.\n**(3) Research related to objects, artifacts, and real property**\nIf the Commission conducts a comprehensive review of research described in paragraph (2)(A)(ii) that focuses on objects, artifacts, or real or personal property that are in the possession or control of private individuals, private entities, or non-Federal Government entities within the United States, the Commission may enter into a contract or agreement to acquire, hold, curate, or maintain those objects, artifacts, or real or personal property until the objects, artifacts, or real or personal property can be properly repatriated or returned, consistent with applicable Federal law, subject to the condition that no Federal funds may be used to purchase those objects, artifacts, or real or personal property.\n##### (b) Meetings and convenings\n**(1) In general**\nThe Commission shall hold, with the advice of the Native American Truth and Healing Advisory Committee and the Survivors Truth and Healing Subcommittee, and in coordination with, as relevant, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations, as part of its investigation under subsection (a), safe, trauma-informed, and culturally appropriate public or private meetings or convenings to receive testimony relating to that investigation.\n**(2) Requirements**\nThe Commission shall ensure that meetings and convenings held under paragraph (1) provide access to adequate trauma-informed care services for participants, attendees, and communities during and following the meetings and convenings where the Commission receives testimony, including ensuring that private space is available for survivors and descendants of survivors, family members, and other community members to receive trauma-informed care services.\n##### (c) Recommendations\n**(1) In general**\nThe Commission shall make recommendations to Congress relating to the investigation carried out under subsection (a), which shall be included in the final report required under subsection (e)(3).\n**(2) Inclusions**\nRecommendations made under paragraph (1) shall include, at a minimum, recommendations relating to\u2014\n**(A)**\nin light of Tribal and Native Hawaiian law, Tribal customary law, tradition, custom, and practice, how the Federal Government can meaningfully acknowledge the role of the Federal Government in supporting Indian Boarding School Policies in all issue areas that the Commission determines relevant, including appropriate forms of memorialization, preservation of records, objects, artifacts, and burials;\n**(B)**\nhow modification of existing statutes, procedures, regulations, policies, budgets, and practices will, in the determination of the Commission, address the findings of the Commission and ongoing effects of Indian Boarding School Policies;\n**(C)**\nhow the Federal Government can promote public awareness of, and education about, Indian Boarding School Policies and the impacts of those policies, including through coordinating with the Native American Truth and Healing Advisory Committee, the Survivors Truth and Healing Subcommittee, the Smithsonian Institution, and other relevant institutions and organizations; and\n**(D)**\nthe views of religious institutions.\n##### (d) Duties related to burials\nThe Commission shall, with respect to burial sites associated with Indian Boarding Schools\u2014\n**(1)**\ncoordinate, as appropriate, with the Native American Truth and Healing Advisory Committee, the Federal and Religious Truth and Healing Advisory Committee, the Survivors Truth and Healing Subcommittee, lineal descendants, Indian Tribes, the Office of Hawaiian Affairs, Federal agencies, institutions, and organizations to locate and identify, in a culturally appropriate manner, marked and unmarked burial sites, including cemeteries, unmarked graves, and mass burial sites, where students of Indian Boarding Schools were originally or later interred;\n**(2)**\nlocate, document, analyze, and coordinate the preservation or continued preservation of records and information relating to the interment of students, including any records held by Federal, State, international, or local entities or religious institutions or organizations; and\n**(3)**\nshare, to the extent practicable, with affected lineal descendants, Indian Tribes, and the Office of Hawaiian Affairs burial locations and the identities of children who attended Indian Boarding Schools.\n##### (e) Reports\n**(1) Annual reports to congress**\nNot less frequently than annually until the year before the year in which the Commission terminates, the Commission shall submit to the Committee on Indian Affairs of the Senate and the Committee on Natural Resources of the House of Representatives a report that describes the activities of the Commission during the previous year, including an accounting of funds and gifts received and expenditures made, the progress made, and any barriers encountered in carrying out this Act.\n**(2) Commission initial report**\nNot later than 4 years after the date on which a majority of the members of the Commission are appointed under section 101(b)(1), the Commission shall submit to the individuals described in paragraph (4), and make publicly available, an initial report containing\u2014\n**(A)**\na detailed review of existing research, including documentation, scholarship, or other resources shared with the Commission that further the purposes of this Act;\n**(B)**\na detailed statement of the initial findings and conclusions of the Commission; and\n**(C)**\na detailed statement of the initial recommendations of the Commission.\n**(3) Commission final report**\nBefore the termination of the Commission, the Commission shall submit to the individuals described in paragraph (4), and make publicly available, a final report containing the findings, conclusions, and recommendations of the Commission that have been agreed on by the vote of a majority of the members of the Commission and 3\u20445 of the members of each of the Native American Truth and Healing Advisory Committee and the Survivors Truth and Healing Subcommittee.\n**(4) Report recipients**\nThe individuals referred to in paragraphs (2) and (3) are\u2014\n**(A)**\nthe President;\n**(B)**\nthe Secretary of the Interior;\n**(C)**\nthe Attorney General;\n**(D)**\nthe Comptroller General of the United States;\n**(E)**\nthe Secretary of Education;\n**(F)**\nthe Secretary of Health and Human Services;\n**(G)**\nthe Secretary of Defense;\n**(H)**\nthe Chairperson and Vice Chairperson of the Committee on Indian Affairs of the Senate;\n**(I)**\nthe Chairperson and ranking minority member of the Committee on Natural Resources of the House of Representatives;\n**(J)**\nthe Co-Chairs of the Congressional Native American Caucus;\n**(K)**\nthe Executive Director of the White House Council on Native American Affairs;\n**(L)**\nthe Director of the Office of Management and Budget;\n**(M)**\nthe Archivist of the United States;\n**(N)**\nthe Librarian of Congress; and\n**(O)**\nthe Director of the National Museum of the American Indian.\n**(5) Additional commission responsibilities relating to the publication of the initial and final reports**\n**(A) Events relating to initial report**\n**(i) In general**\nThe Commission shall hold not fewer than 2 events in each region of the Bureau of Indian Affairs and in Hawai\u2018i following publication of the initial report under paragraph (2) to receive comments on the initial report.\n**(ii) Timing**\nThe schedule of events referred to in clause (i) shall be announced not later than 90 days after the date on which the initial report under paragraph (2) is published.\n**(B) Publication of final report**\nNot later than 180 days after the date on which the Commission submits the final report under paragraph (3), the Commission, the Secretary of the Interior, the Secretary of Education, the Secretary of Defense, and the Secretary of Health and Human Services shall each make the final report publicly available on the website of the applicable agency.\n**(6) Secretarial response to final report**\nNot later than 120 days after the date on which the Secretary of the Interior, the Secretary of Education, the Secretary of Defense, and the Secretary of Health and Human Services receive the final report under paragraph (3), the Secretaries shall each make publicly available a written response to recommendations for future action by those agencies, if any, contained in the final report, and submit the written response to\u2014\n**(A)**\nthe President;\n**(B)**\nthe Committee on Indian Affairs of the Senate;\n**(C)**\nthe Committee on Natural Resources of the House of Representatives; and\n**(D)**\nthe Comptroller General of the United States.\nC\nSurvivors Truth and Healing Subcommittee\n#### 121. Survivors Truth and Healing Subcommittee\n##### (a) Establishment\nThere is established a subcommittee of the Commission, to be known as the Survivors Truth and Healing Subcommittee .\n##### (b) Membership, nomination, and appointment to the survivors truth and healing subcommittee\n**(1) Membership**\nThe Survivors Truth and Healing Subcommittee shall include 15 members, to be appointed by the Commission, in consultation with the National Native American Boarding School Healing Coalition, from among the nominees submitted under paragraph (2)(A), of whom\u2014\n**(A)**\n12 shall be representatives from each of the 12 regions of the Bureau of Indian Affairs and 1 shall be a representative from Hawai\u2018i;\n**(B)**\n9 shall be individuals who attended an Indian Boarding School of whom\u2014\n**(i)**\nnot fewer than 2 shall be individuals who graduated during the 5-year period preceding the date of the enactment of this Act from\u2014\n**(I)**\nan Indian Boarding School in operation as of that date of the enactment; or\n**(II)**\na Bureau of Indian Education-funded school; and\n**(ii)**\nall shall represent diverse regions of the United States;\n**(C)**\n5 shall be descendants of individuals who attended Indian Boarding Schools, who shall represent diverse regions of the United States; and\n**(D)**\n1 shall be an educator who, as of the date of the appointment\u2014\n**(i)**\nis employed at an Indian Boarding School; or\n**(ii)**\nwas employed at an Indian Boarding School during the 5-year period preceding the date of the enactment of this Act.\n**(2) Nominations**\n**(A) In general**\nNot later than 90 days after the date of the enactment of this Act, Indian Tribes, Tribal organizations, Native Americans, the Office of Hawaiian Affairs, and Native Hawaiian organizations may submit to the Secretary of the Interior nominations for individuals to be appointed as members of the Survivors Truth and Healing Subcommittee.\n**(B) Submission**\nThe Secretary of the Interior shall provide the Commission with nominations submitted under subparagraph (A) at the initial business meeting of the Commission under section 101(c)(1) and the Commission shall select the members of the Survivors Truth and Healing Subcommittee from among those nominees.\n**(3) Date**\n**(A) In general**\nThe Commission shall appoint all members of the Survivors Truth and Healing Subcommittee during the initial business meeting of the Commission under section 101(c)(1).\n**(B) Failure to appoint**\nIf the Commission fails to appoint all members of the Survivors Truth and Healing Subcommittee in accordance with subparagraph (A), the Chair of the Committee on Indian Affairs of the Senate, with the concurrence of the Vice Chair of the Committee on Indian Affairs of the Senate, shall appoint individuals, in accordance with the requirements of paragraph (1), to all vacant positions of the Survivors Truth and Healing Subcommittee not later than 30 days after the date of the initial business meeting of the Commission under section 101(c)(1).\n**(4) Period of appointment; vacancies; removal**\n**(A) Period of appointment**\nA member of the Survivors Truth and Healing Subcommittee shall be appointed for an automatically renewable term of 2 years.\n**(B) Vacancies**\n**(i) In general**\nA member of the Survivors Truth and Healing Subcommittee may vacate the position at any time and for any reason.\n**(ii) Effect; filling of vacancy**\nA vacancy in the Survivors Truth and Healing Subcommittee\u2014\n**(I)**\nshall not affect the powers of the Survivors Truth and Healing Subcommittee if a simple majority of the positions of the Survivors Truth and Healing Subcommittee are filled; and\n**(II)**\nshall be filled within 90 days in the same manner as was the original appointment.\n**(C) Removal**\nA quorum of members of the Commission may remove a member of the Survivors Truth and Healing Subcommittee only for neglect of duty or malfeasance.\n**(5) Termination**\nThe Survivors Truth and Healing Subcommittee shall terminate 90 days after the date on which the Commission submits the final report required under section 111(e)(3).\n**(6) Limitation**\nNo member of the Survivors Truth and Healing Subcommittee may otherwise be an officer or employee of the Federal Government.\n##### (c) Business meetings\n**(1) Initial meeting**\nNot later than 30 days after the date on which all members of the Survivors Truth and Healing Subcommittee are appointed under subsection (b)(1), the Survivors Truth and Healing Subcommittee shall hold an initial business meeting\u2014\n**(A)**\nto appoint\u2014\n**(i)**\na Chairperson, who shall also serve as the Vice Chairperson of the Federal and Religious Truth and Healing Advisory Committee;\n**(ii)**\na Vice Chairperson, who shall also serve as the Vice Chairperson of the Native American Truth and Healing Advisory Committee; and\n**(iii)**\nother positions, as determined necessary by the Survivors Truth and Healing Subcommittee;\n**(B)**\nto establish, with the advice of the Commission, rules for the Survivors Truth and Healing Subcommittee;\n**(C)**\nto appoint 3 designees to fulfill the responsibilities described in section 101(h)(1)(A); and\n**(D)**\nto appoint, with the advice of the Commission, 2 members of the Survivors Truth and Healing Subcommittee to serve as non-voting designees on the Commission in accordance with section 101(c)(3).\n**(2) Subsequent business meetings**\nAfter the initial business meeting of the Survivors Truth and Healing Subcommittee is held under paragraph (1), the Survivors Truth and Healing Subcommittee shall meet at the call of the Chairperson.\n**(3) Format of business meetings**\nA business meeting of the Survivors Truth and Healing Subcommittee may be conducted in-person or virtually.\n**(4) Quorum required**\nA business meeting of the Survivors Truth and Healing Subcommittee may be held only after a quorum, established in accordance with subsection (d), is present.\n##### (d) Quorum\nA simple majority of the members of the Survivors Truth and Healing Subcommittee shall constitute a quorum for a business meeting.\n##### (e) Rules\nThe Survivors Truth and Healing Subcommittee, with the advice of the Commission, may establish, by a majority vote, any rules for the conduct of business, in accordance with this section and other applicable law.\n##### (f) Duties\nThe Survivors Truth and Healing Subcommittee shall\u2014\n**(1)**\nassist the Commission, the Native American Truth and Healing Advisory Committee, and the Federal and Religious Truth and Healing Advisory Committee in coordinating public and private convenings, including providing advice to the Commission on developing criteria and protocols for convenings;\n**(2)**\nprovide advice and evaluate Committee recommendations relating to the commemoration and public education relating to Indian Boarding Schools and Indian Boarding School Policies;\n**(3)**\nassist the Commission\u2014\n**(A)**\nin the production of the initial and final reports required under paragraphs (2) and (3), respectively, of section 111(e); and\n**(B)**\nby providing such other advice, or fulfilling such other requests, as may be required by the Commission; and\n**(4)**\ncoordinate with the Commission, the Native American Truth and Healing Advisory Committee, and the Federal and Religious Truth and Healing Advisory Committee.\n##### (g) Consultation or engagement with native americans, indian tribes, tribal organizations, the office of hawaiian affairs, and native hawaiian organizations\nIn carrying out the duties of the Survivors Truth and Healing Subcommittee under subsection (f), the Survivors Truth and Healing Subcommittee shall meaningfully consult or engage, as appropriate, in a timely manner with Native Americans, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations.\n##### (h) Federal advisory committee act applicability\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), shall not apply to the Survivors Truth and Healing Subcommittee.\n##### (i) Congressional Accountability Act applicability\nFor purposes of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ), any individual who is a member of the Survivors Truth and Healing Subcommittee shall be considered a covered employee under the Act.\n##### (j) Personnel matters\n**(1) Compensation of members**\nA member of the Survivors Truth and Healing Subcommittee shall be compensated at a daily equivalent of the annual rate of basic pay prescribed for grade 7, step 1, of the General Schedule under section 5332 of title 5, United States Code, for each day, not to exceed 10 days per month, for which a member of the Survivors Truth and Healing Subcommittee is engaged in the performance of their duties under this Act limited to convening meetings, including public and private meetings to receive testimony in furtherance of the duties of the Survivors Truth and Healing Subcommittee and the purposes of this Act.\n**(2) Travel expenses**\nA member of the Survivors Truth and Healing Subcommittee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Survivors Truth and Healing Subcommittee.\nII\nAdvisory Committees\nA\nNative American Truth and Healing Advisory Committee\n#### 201. Native American Truth and Healing Advisory Committee\n##### (a) Establishment\nThe Commission shall establish an advisory committee, to be known as the Native American Truth and Healing Advisory Committee .\n##### (b) Membership, nomination, and appointment to the native american truth and healing advisory committee\n**(1) Membership**\n**(A) In general**\nThe Native American Truth and Healing Advisory Committee shall include 19 members, to be appointed by the Commission from among the nominees submitted under paragraph (2)(A), of whom\u2014\n**(i)**\n1 shall be the Vice Chairperson of the Commission, who shall serve as the Chairperson of the Native American Truth and Healing Advisory Committee;\n**(ii)**\n1 shall be the Vice Chairperson of the Survivors Truth and Healing Subcommittee, who shall serve as the Vice Chairperson of the Native American Truth and Healing Advisory Committee;\n**(iii)**\n1 shall be the Secretary of the Interior, or a designee, who shall serve as the Secretary of the Native American Truth and Healing Advisory Committee;\n**(iv)**\n12 shall be representatives from each of the 12 regions of the Bureau of Indian Affairs and 1 shall be a representative from Hawai\u2018i;\n**(v)**\n1 shall represent the National Native American Boarding School Healing Coalition;\n**(vi)**\n1 shall represent the National Association of Tribal Historic Preservation Officers; and\n**(vii)**\n1 shall represent the National Indian Education Association.\n**(B) Additional requirements**\nNot fewer than 2 members of the Native American Truth and Healing Advisory Committee shall have experience with health care or mental health, traditional healing or cultural practices, counseling, or working with survivors, or descendants of survivors, of Indian Boarding Schools to ensure that the Commission considers culturally responsive support for survivors, families, and communities.\n**(2) Nominations**\n**(A) In general**\nNot later than 90 days after the date of the enactment of this Act, Indian Tribes, Tribal organizations, Native Americans, the Office of Hawaiian Affairs, and Native Hawaiian organizations may submit to the Secretary of the Interior nominations for individuals to be appointed as members of the Native American Truth and Healing Advisory Committee.\n**(B) Submission**\nThe Secretary of the Interior shall provide the Commission with nominations submitted under subparagraph (A) at the initial business meeting of the Commission under section 101(c)(1) and the Commission shall select the members of the Native American Truth and Healing Advisory Committee from among those nominees.\n**(3) Date**\n**(A) In general**\nThe Commission shall appoint all members of the Native American Truth and Healing Advisory Committee during the initial business meeting of the Commission under section 101(c)(1).\n**(B) Failure to appoint**\nIf the Commission fails to appoint all members of the Native American Truth and Healing Advisory Committee in accordance with subparagraph (A), the Chair of the Committee on Indian Affairs of the Senate, with the concurrence of the Vice Chair of the Committee on Indian Affairs of the Senate, shall appoint, in accordance with the requirements of paragraph (1), individuals to all vacant positions of the Native American Truth and Healing Advisory Committee not later than 30 days after the date of the initial business meeting of the Commission under section 101(c)(1).\n**(4) Period of appointment; vacancies**\n**(A) Period of appointment**\nA member of the Native American Truth and Healing Advisory Committee shall be appointed for an automatically renewable term of 2 years.\n**(B) Vacancies**\nA vacancy in the Native American Truth and Healing Advisory Committee\u2014\n**(i)**\nshall not affect the powers of the Native American Truth and Healing Advisory Committee if a simple majority of the positions of the Native American Truth and Healing Advisory Committee are filled; and\n**(ii)**\nshall be filled within 90 days in the same manner as was the original appointment.\n**(5) Termination**\nThe Native American Truth and Healing Advisory Committee shall terminate 90 days after the date on which the Commission submits the final report required under section 111(e)(3).\n**(6) Limitation**\nNo member of the Native American Truth and Healing Advisory Committee (other than the member described in paragraph (1)(A)(iii)) may otherwise be an officer or employee of the Federal Government.\n##### (c) Quorum\nA simple majority of the members of the Native American Truth and Healing Advisory Committee shall constitute a quorum.\n##### (d) Removal\nA quorum of members of the Native American Truth and Healing Advisory Committee may remove another member only for neglect of duty or malfeasance.\n##### (e) Business meetings\n**(1) Initial business meeting**\nNot later than 30 days after the date on which all members of the Native American Truth and Healing Advisory Committee are appointed under subsection (b)(1)(A), the Native American Truth and Healing Advisory Committee shall hold an initial business meeting\u2014\n**(A)**\nto establish rules for the Native American Truth and Healing Advisory Committee;\n**(B)**\nto appoint 3 designees to fulfill the responsibilities described in section 101(h)(1)(A); and\n**(C)**\nto appoint 2 members of the Native American Truth and Healing Advisory Committee to serve as non-voting designees on the Commission in accordance with section 101(c)(3).\n**(2) Subsequent business meetings**\nAfter the initial business meeting of the Native American Truth and Healing Advisory Committee is held under paragraph (1), the Native American Truth and Healing Advisory Committee shall meet at the call of the Chairperson.\n**(3) Format of business meetings**\nA meeting of the Native American Truth and Healing Advisory Committee may be conducted in-person or virtually.\n**(4) Quorum required**\nA business meeting of the Native American Truth and Healing Advisory Committee may be held only after a quorum, established in accordance with subsection (c), is present.\n##### (f) Rules\nThe Native American Truth and Healing Advisory Committee may establish, with the advice of the Commission, by a majority vote, any rules for the conduct of business, in accordance with this section and other applicable law.\n##### (g) Duties\nThe Native American Truth and Healing Advisory Committee shall\u2014\n**(1)**\nserve as an advisory body to the Commission;\n**(2)**\nassist the Commission in organizing and carrying out culturally appropriate public and private convenings relating to the duties of the Commission;\n**(3)**\nassist the Commission in determining what documentation from Federal and religious organizations and institutions may be necessary to fulfill the duties of the Commission;\n**(4)**\nassist the Commission in the production of the initial report and final report required under paragraphs (2) and (3), respectively, of section 111(e);\n**(5)**\ncoordinate with the Commission, the Federal and Religious Truth and Healing Advisory Committee, and the Survivors Truth and Healing Subcommittee; and\n**(6)**\nprovide advice to, or fulfill such other requests by, the Commission as the Commission may require to carry out the purposes described in section 2.\n##### (h) Consultation or engagement with native americans, indian tribes, tribal organizations, the office of hawaiian affairs, and native hawaiian organizations\nIn carrying out the duties of the Native American Truth and Healing Advisory Committee under subsection (g), the Native American Truth and Healing Advisory Committee shall meaningfully consult or engage, as appropriate, in a timely manner with Native Americans, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations.\n##### (i) Federal advisory committee act applicability\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), shall not apply to the Native American Truth and Healing Advisory Committee.\n##### (j) Congressional Accountability Act applicability\nFor purposes of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. ), any individual who is a member of the Native American Truth and Healing Advisory Committee shall be considered a covered employee under the Act.\n##### (k) Personnel matters\n**(1) Compensation of members**\nA member of the Native American Truth and Healing Advisory Committee shall be compensated at a daily equivalent of the annual rate of basic pay prescribed for grade 7, step 1, of the General Schedule under section 5332 of title 5, United States Code, for each day, not to exceed 14 days per month, for which a member is engaged in the performance of their duties under this Act, limited to convening meetings, including public and private meetings to receive testimony in furtherance of the duties of the Native American Truth and Healing Advisory Committee and the purposes of this Act.\n**(2) Travel expenses**\nA member of the Native American Truth and Healing Advisory Committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Native American Truth and Healing Advisory Committee.\nB\nFederal and Religious Truth and Healing Advisory Committee\n#### 211. Federal and Religious Truth and Healing Advisory Committee\n##### (a) Establishment\nThere is established within the Department of the Interior an advisory committee, to be known as the Federal and Religious Truth and Healing Advisory Committee .\n##### (b) Membership and appointment to the Federal and Religious Truth and Healing Advisory Committee\n**(1) Membership**\nThe Federal and Religious Truth and Healing Advisory Committee shall include 20 members, of whom\u2014\n**(A)**\n1 shall be the Chairperson of the Commission, who shall serve as the Chairperson of the Federal and Religious Truth and Healing Advisory Committee;\n**(B)**\n1 shall be the Chairperson of the Survivors Truth and Healing Subcommittee, who shall serve as the Vice Chairperson of the Federal and Religious Truth and Healing Advisory Committee;\n**(C)**\n1 shall be the White House Domestic Policy Advisor, who shall serve as the Secretary of the Federal and Religious Truth and Healing Advisory Committee;\n**(D)**\n1 shall be the Director of the Bureau of Trust Funds Administration (or a designee);\n**(E)**\n1 shall be the Archivist of the United States (or a designee);\n**(F)**\n1 shall be the Librarian of Congress (or a designee);\n**(G)**\n1 shall be the Director of the Department of the Interior Library (or a designee);\n**(H)**\n1 shall be the Director of the Indian Health Service (or a designee);\n**(I)**\n1 shall be the Assistant Secretary for Mental Health and Substance Abuse of the Department of Health and Human Services (or a designee);\n**(J)**\n1 shall be the Commissioner of the Administration for Native Americans of the Department of Health and Human Services (or a designee);\n**(K)**\n1 shall be the Director of the National Institutes of Health (or a designee);\n**(L)**\n1 shall be the Senior Program Director of the Office of Native Hawaiian Relations of the Department of the Interior (or a designee);\n**(M)**\n1 shall be the Director of the Office of Indian Education of the Department of Education (or a designee);\n**(N)**\n1 shall be the Director of the Rural, Insular, and Native American Achievement Programs of the Department of Education (or a designee);\n**(O)**\n1 shall be the Chair of the Advisory Council on Historic Preservation (or a designee);\n**(P)**\n1 shall be the Assistant Secretary of Indian Affairs (or a designee);\n**(Q)**\n1 shall be the Director of the Bureau of Indian Education (or a designee); and\n**(R)**\n3 shall be representatives employed by, or representatives of, religious institutions, to be appointed by the White House Office of Faith-Based and Neighborhood Partnerships in consultation with relevant religious institutions.\n**(2) Period of service; vacancies; removal**\n**(A) Period of service**\nA member of the Federal and Religious Truth and Healing Advisory Committee shall serve for an automatically renewable term of 2 years.\n**(B) Vacancies**\nA vacancy in the Federal and Religious Truth and Healing Advisory Committee\u2014\n**(i)**\nshall not affect the powers of the Federal and Religious Truth and Healing Advisory Committee if a simple majority of the positions of the Federal and Religious Truth and Healing Advisory Committee are filled; and\n**(ii)**\nshall be filled within 90 days in the same manner as was the original appointment.\n**(C) Removal**\nA quorum of members of the Federal and Religious Truth and Healing Advisory Committee may remove a member of the Federal and Religious Truth and Healing Advisory Committee only for neglect of duty or malfeasance.\n**(3) Termination**\nThe Federal and Religious Truth and Healing Advisory Committee shall terminate 90 days after the date on which the Commission submits the final report required under section 111(e)(3).\n##### (c) Business meetings\n**(1) Initial business meeting**\nNot later than 30 days after the date of the initial business meeting of the Commission under section 101(c)(1), the Federal and Religious Truth and Healing Advisory Committee shall hold an initial business meeting\u2014\n**(A)**\nto establish rules for the Federal and Religious Truth and Healing Advisory Committee; and\n**(B)**\nto appoint 2 members of the Federal and Religious Truth and Healing Advisory Committee to serve as non-voting designees on the Commission in accordance with section 101(c)(3).\n**(2) Subsequent business meetings**\nAfter the initial business meeting of the Federal and Religious Truth and Healing Advisory Committee is held under paragraph (1), the Federal and Religious Truth and Healing Advisory Committee shall meet at the call of the Chairperson.\n**(3) Format of business meetings**\nA business meeting of the Federal and Religious Truth and Healing Advisory Committee may be conducted in-person or virtually.\n**(4) Quorum required**\nA business meeting of the Federal and Religious Truth and Healing Advisory Committee may be held only after a quorum, established in accordance with subsection (d), is present.\n##### (d) Quorum\nA simple majority of the members of the Federal and Religious Truth and Healing Advisory Committee shall constitute a quorum for a business meeting.\n##### (e) Rules\nThe Federal and Religious Truth and Healing Advisory Committee may establish, with the advice of the Commission, by a majority vote, any rules for the conduct of business, in accordance with this section and other applicable law.\n##### (f) Duties\nThe Federal and Religious Truth and Healing Advisory Committee shall\u2014\n**(1)**\nensure the effective and timely coordination among Federal agencies and religious institutions in furtherance of the purposes of this Act;\n**(2)**\nassist the Commission and the Native American Truth and Healing Advisory Committee in coordinating\u2014\n**(A)**\nmeetings and other related public and private convenings; and\n**(B)**\nthe collection, organization, and preservation of information obtained from witnesses and by other Federal agencies and religious institutions;\n**(3)**\nensure the timely submission to the Commission of materials, documents, testimony, and such other information as the Commission determines to be necessary to carry out the duties of the Commission; and\n**(4)**\ncoordinate with the Commission, the Native American Truth and Healing Advisory Committee, and the Survivors Truth and Healing Subcommittee to carry out the purposes of this Act.\n##### (g) Consultation or engagement with native americans, indian tribes, tribal organizations, the office of hawaiian affairs, and native hawaiian organizations\nIn carrying out the duties of the Federal and Religious Truth and Healing Advisory Committee under subsection (f), the Federal and Religious Truth and Healing Advisory Committee shall meaningfully consult or engage, as appropriate, in a timely manner with Native Americans, Indian Tribes, Tribal organizations, the Office of Hawaiian Affairs, and Native Hawaiian organizations.\n##### (h) Nondisclosure\n**(1) Privacy Act of 1974 applicability**\nSubsection (b) of section 552a of title 5, United States Code (commonly known as the Privacy Act of 1974 ), shall not apply to the Federal and Religious Truth and Healing Advisory Committee.\n**(2) Freedom of Information Act applicability**\nRecords and other communications in the possession of the Federal and Religious Truth and Healing Advisory Committee shall be exempt from disclosure under subsection (b)(3)(B) of section 552 of title 5, United States Code (commonly known as the Freedom of Information Act ).\n**(3) Federal advisory committee act applicability**\nChapter 10 of title 5, United States Code (commonly known as the Federal Advisory Committee Act ), shall not apply to the Federal and Religious Truth and Healing Advisory Committee.\nIII\nGeneral Provisions\n#### 301. Clarification\nThe Native American Graves Protection and Repatriation Act ( 25 U.S.C. 3001 et seq. ) shall apply to cultural items (as defined in section 2 of that Act ( 25 U.S.C. 3001 )) relating to an Indian Boarding School or Indian Boarding School Policies regardless of interpretation of applicability by a Federal agency.\n#### 302. Burial management\nFederal agencies shall permit reburial of cultural items relating to an Indian Boarding School or Indian Boarding School Policies that have been repatriated pursuant to the Native American Graves Protection and Repatriation Act ( 25 U.S.C. 3001 et seq. ), or returned to a lineal descendant, Indian Tribe, or Native Hawaiian organization by any other disinterment process, on any Federal land as agreed to by the relevant parties.\n#### 303. Co-stewardship agreements\nA Federal agency that carries out activities pursuant to this Act or that created or controls a cemetery with remains of an individual who attended an Indian Boarding School or an Indian Boarding School may enter into a co-stewardship agreement for the management of the cemetery or Indian Boarding School.\n#### 304. No right of action\nNothing in this Act creates a private right of action to seek administrative or judicial relief.",
      "versionDate": "2026-02-03",
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
        "actionDate": "2025-07-31",
        "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 139."
      },
      "number": "761",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2025",
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
        "name": "Native Americans",
        "updateDate": "2026-02-13T18:26:23Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-03",
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
          "measure-id": "id119hr7325",
          "measure-number": "7325",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-03",
          "originChamber": "HOUSE",
          "update-date": "2026-04-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7325v00",
            "update-date": "2026-04-10"
          },
          "action-date": "2026-02-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Truth and Healing Commission on Indian Boarding School Policies Act of 2026</strong></p><p>This bill establishes the Truth and Healing Commission on Indian Boarding School Policies in the United States within the legislative branch and sets forth its powers, duties, and membership.</p><p>Among other duties, the commission must investigate the impacts and ongoing effects of the Indian Boarding School Policies (federal policies under which American Indian, Alaska Native, and Native Hawaiian children were forcibly removed from their family homes and placed in boarding schools).</p><p>Further, the commission must develop recommendations on ways to (1) protect unmarked graves and accompanying land protections; (2) support repatriation and identify the tribal nations from which children were taken; and (3) discontinue the removal of American Indian, Alaska Native, and Native Hawaiian children from their families and tribal communities by state social service departments, foster care agencies, and adoption agencies.</p>"
        },
        "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2026"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7325.xml",
    "summary": {
      "actionDate": "2026-02-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truth and Healing Commission on Indian Boarding School Policies Act of 2026</strong></p><p>This bill establishes the Truth and Healing Commission on Indian Boarding School Policies in the United States within the legislative branch and sets forth its powers, duties, and membership.</p><p>Among other duties, the commission must investigate the impacts and ongoing effects of the Indian Boarding School Policies (federal policies under which American Indian, Alaska Native, and Native Hawaiian children were forcibly removed from their family homes and placed in boarding schools).</p><p>Further, the commission must develop recommendations on ways to (1) protect unmarked graves and accompanying land protections; (2) support repatriation and identify the tribal nations from which children were taken; and (3) discontinue the removal of American Indian, Alaska Native, and Native Hawaiian children from their families and tribal communities by state social service departments, foster care agencies, and adoption agencies.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr7325"
    },
    "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2026"
  },
  "summaries": [
    {
      "actionDate": "2026-02-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Truth and Healing Commission on Indian Boarding School Policies Act of 2026</strong></p><p>This bill establishes the Truth and Healing Commission on Indian Boarding School Policies in the United States within the legislative branch and sets forth its powers, duties, and membership.</p><p>Among other duties, the commission must investigate the impacts and ongoing effects of the Indian Boarding School Policies (federal policies under which American Indian, Alaska Native, and Native Hawaiian children were forcibly removed from their family homes and placed in boarding schools).</p><p>Further, the commission must develop recommendations on ways to (1) protect unmarked graves and accompanying land protections; (2) support repatriation and identify the tribal nations from which children were taken; and (3) discontinue the removal of American Indian, Alaska Native, and Native Hawaiian children from their families and tribal communities by state social service departments, foster care agencies, and adoption agencies.</p>",
      "updateDate": "2026-04-10",
      "versionCode": "id119hr7325"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7325ih.xml"
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
      "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T04:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Truth and Healing Commission on Indian Boarding School Policies Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To establish the Truth and Healing Commission on Indian Boarding School Policies in the United States, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T04:48:20Z"
    }
  ]
}
```
