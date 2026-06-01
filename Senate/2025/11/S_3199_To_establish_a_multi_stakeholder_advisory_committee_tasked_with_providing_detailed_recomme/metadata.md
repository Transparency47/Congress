# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3199?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3199
- Title: 988 Lifeline Location Improvement Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 3199
- Origin chamber: Senate
- Introduced date: 2025-11-19
- Update date: 2026-05-18T20:50:59Z
- Update date including text: 2026-05-18T20:50:59Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in Senate
- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S8241-8242)
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.
- 2026-04-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 379.
- 2026-05-11 - Floor: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2204-2205; text: CR S2204-2205)
- 2026-05-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.
- 2026-05-12 - Floor: Message on Senate action sent to the House.
- 2026-05-12 15:06:01 - Floor: Received in the House.
- 2026-05-12 15:11:39 - Floor: Held at the desk.
- Latest action: 2025-11-19: Introduced in Senate

## Actions

- 2025-11-19 - IntroReferral: Introduced in Senate
- 2025-11-19 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S8241-8242)
- 2026-02-12 - Committee: Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.
- 2026-04-22 - Committee: Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.
- 2026-04-22 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 379.
- 2026-05-11 - Floor: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2204-2205; text: CR S2204-2205)
- 2026-05-11 - Floor: Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.
- 2026-05-12 - Floor: Message on Senate action sent to the House.
- 2026-05-12 15:06:01 - Floor: Received in the House.
- 2026-05-12 15:11:39 - Floor: Held at the desk.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3199",
    "number": "3199",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "988 Lifeline Location Improvement Act of 2026",
    "type": "S",
    "updateDate": "2026-05-18T20:50:59Z",
    "updateDateIncludingText": "2026-05-18T20:50:59Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H15000",
      "actionDate": "2026-05-12",
      "actionTime": "15:11:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Held at the desk.",
      "type": "Floor"
    },
    {
      "actionCode": "H14000",
      "actionDate": "2026-05-12",
      "actionTime": "15:06:01",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Received in the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-12",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Message on Senate action sent to the House.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Passed Senate with an amendment and an amendment to the Title by Unanimous Consent. (consideration: CR S2204-2205; text: CR S2204-2205)",
      "type": "Floor"
    },
    {
      "actionCode": "17000",
      "actionDate": "2026-05-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Passed/agreed to in Senate: Passed Senate with an amendment and an amendment to the Title by Unanimous Consent.",
      "type": "Floor"
    },
    {
      "actionDate": "2026-04-22",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 379.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.",
      "type": "Committee"
    },
    {
      "actionCode": "14000",
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Committee on Commerce, Science, and Transportation. Reported by Senator Cruz with an amendment in the nature of a substitute and an amendment to the title. With written report No. 119-119.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-12",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Commerce, Science, and Transportation. Ordered to be reported with an amendment in the nature of a substitute favorably.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-19",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation. (text: CR S8241-8242)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-19",
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
        "item": [
          {
            "date": "2026-04-22T17:18:01Z",
            "name": "Reported By"
          },
          {
            "date": "2026-02-12T15:00:04Z",
            "name": "Markup By"
          },
          {
            "date": "2025-11-19T15:47:37Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "L000570",
      "firstName": "Ben",
      "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Luj\u00e1n",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NM"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "WV"
    },
    {
      "bioguideId": "C000880",
      "firstName": "Mike",
      "fullName": "Sen. Crapo, Mike [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Crapo",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ID"
    },
    {
      "bioguideId": "D000618",
      "firstName": "Steve",
      "fullName": "Sen. Daines, Steve [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Daines",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "MT"
    },
    {
      "bioguideId": "F000463",
      "firstName": "Deb",
      "fullName": "Sen. Fischer, Deb [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Fischer",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "NE"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NY"
    },
    {
      "bioguideId": "H001076",
      "firstName": "Maggie",
      "fullName": "Sen. Hassan, Margaret Wood [D-NH]",
      "isOriginalCosponsor": "True",
      "lastName": "Hassan",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "NH"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MN"
    },
    {
      "bioguideId": "R000584",
      "firstName": "James",
      "fullName": "Sen. Risch, James E. [R-ID]",
      "isOriginalCosponsor": "True",
      "lastName": "Risch",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "ID"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "GA"
    },
    {
      "bioguideId": "O000174",
      "firstName": "Jon",
      "fullName": "Sen. Ossoff, Jon [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Ossoff",
      "party": "D",
      "sponsorshipDate": "2025-12-16",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3199is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3199\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Barrasso (for himself, Mr. Luj\u00e1n , Mrs. Blackburn , Mrs. Capito , Mr. Crapo , Mr. Daines , Mrs. Fischer , Mrs. Gillibrand , Ms. Hassan , Ms. Klobuchar , Mr. Risch , and Mr. Warnock ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo establish a multi-stakeholder advisory committee tasked with providing detailed recommendations to address challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 988 Lifeline Location Improvement Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) 911 system service provider**\nThe term 911 system service provider has the meaning given the term covered 911 service provider in section 9.19(a)(4) of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate ; and\n**(C)**\nthe Committee on Energy and Commerce of the House of Representatives .\n**(3) Committee**\nThe term committee means the advisory committee established under section 3.\n**(4) Community based mental health organization**\nThe term community based mental health organization means an organization that serves individuals with mental health conditions and the families of those individuals in a community setting.\n**(5) Dispatchable location**\nThe term dispatchable location has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(6) Handset manufacturer**\nThe term handset manufacturer means a manufacturer of cellular phones.\n**(7) Local crisis center**\nThe term local crisis center means a call center intended to receive calls from the 988 Suicide and Crisis Lifeline and the Veterans Crisis Line.\n**(8) Local government**\nThe term local government means the government of any political subdivision of a State.\n**(9) Low population State**\nThe term low population State means a State that has no urbanized areas with a population greater than 250,000, as reported in the decennial census.\n**(10) Mental health services organization**\nThe term mental health services organization means an organization or association that represents providers of mental health crisis services or crisis respite services.\n**(11) Public safety answering point**\nThe term public safety answering point has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(12) Small and rural communities**\nThe term small and rural communities means a noncore area, a micropolitan area, or a small metropolitan statistical area with a population of not more than 250,000, as reported in the decennial census.\n**(13) State**\nThe term State means any of the several States of the United States, the District of Columbia, and any territory or possession of the United States.\n**(14) Telecommunications service provider**\nThe term telecommunications service provider has the meaning given the term service provider in section 52.5(e) of title 47, Code of Federal Regulations, or any successor regulation.\n#### 3. Establishment of committee\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Federal Communications Commission, in coordination with the Secretary of Health and Human Services, shall establish an advisory committee to provide recommendations to address challenges to transmitting geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline.\n##### (b) Membership\n**(1) Composition**\n**(A) In general**\nThe committee shall be composed of 15 members, to be appointed in accordance with subparagraphs (B) and (C).\n**(B) Appointments by Federal Communications Commission**\nOf the 15 members of the committee appointed under this paragraph, the Federal Communications Commission shall appoint\u2014\n**(i)**\n1 member from a telecommunications service provider or an organization that represents telecommunications service providers;\n**(ii)**\n1 member from a handset manufacturer or an organization that represents handset manufacturers;\n**(iii)**\n1 member from a public safety answering point or an organization that represents public safety answering points;\n**(iv)**\n1 member from a 911 system service provider or an organization that represents 911 system service providers;\n**(v)**\n2 members from a State government, with at least 1 member representing a low population State; and\n**(vi)**\n2 members from a local government, with at least 1 member representing small and rural communities.\n**(C) Appointments by the Secretary of Health and Human Services**\nOf the 15 members of the committee appointed under this paragraph, the Secretary of Health and Human Services shall appoint\u2014\n**(i)**\n1 member from the 988 Suicide and Crisis Lifeline;\n**(ii)**\n1 member from a local crisis center or an organization that represents local crisis centers;\n**(iii)**\n1 member from the Veterans Crisis Line;\n**(iv)**\n1 member from the Substance Abuse and Mental Health Services Administration;\n**(v)**\n1 member from a mental health services organization;\n**(vi)**\n1 member from a community based mental health organization; and\n**(vii)**\n1 member with experience providing services for people who are deaf or hard of hearing or have hearing loss, such as access to the 988 Suicide and Crisis Lifeline through direct video calling and video relay service.\n**(2) Date**\nThe appointments of the members of the committee shall be made not later than 30 days after the date of enactment of this Act.\n##### (c) Period of appointment; vacancies\n**(1) In general**\nA member of the committee shall be appointed for the life of the committee.\n**(2) Vacancies**\nA vacancy in the committee\u2014\n**(A)**\nshall not affect the powers of the committee; and\n**(B)**\nshall be filled in the same manner as the original appointment.\n##### (d) Meetings\n**(1) Initial meeting**\nNot later than 30 days after the date on which all members of the committee have been appointed, the committee shall hold the first meeting of the committee.\n**(2) Frequency**\nThe committee shall meet at the call of the Chairperson.\n**(3) Quorum**\nA majority of the members of the committee shall constitute a quorum, but a lesser number of members may hold hearings.\n##### (e) Chairperson and Vice Chairperson\nThe committee shall select a Chairperson and Vice Chairperson from among the members of the committee.\n#### 4. Duties of Committee\n##### (a) Study\nThe committee shall conduct a study on\u2014\n**(1)**\npolicy considerations regarding consumer privacy and legal authority with respect to mandating transmission of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline;\n**(2)**\ntechnical implementation standards for telecommunications service providers, 911 system service providers, public safety answering points, and local crisis centers; and\n**(3)**\npotential recovery of costs or additional funding requirements for telecommunications service providers, the 988 Suicide and Crisis Lifeline, the Veterans Crisis Line, and local crisis centers.\n##### (b) Recommendations\nBased on the results of the study conducted under subsection (a), the committee shall develop recommendations on potential legislation that would address challenges relating to the inclusion of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the committee shall submit to appropriate committees of Congress and the Federal Communications Commission a report that contains a detailed statement of the findings and conclusions of the committee, together with the recommendations of the committee for such legislation and administrative actions as the committee considers appropriate.\n#### 5. Powers of committee\n##### (a) Hearings\nThe committee may hold such hearings, sit and act at such times and places, take such testimony, and receive such evidence as the committee considers advisable to carry out this Act.\n##### (b) Information from Federal agencies\n**(1) In general**\nThe committee may secure directly from a Federal department or agency such information as the committee considers necessary to carry out this Act.\n**(2) Furnishing information**\nOn request of the Chairperson of the committee, the head of the department or agency shall furnish the information to the committee.\n##### (c) Postal services\nThe committee may use the United States mails in the same manner and under the same conditions as other departments and agencies of the Federal Government.\n##### (d) Gifts\nThe committee may accept, use, and dispose of gifts or donations of services or property.\n#### 6. Committee personnel matters\n##### (a) Travel expenses\nA member of the committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the committee.\n##### (b) Staff\n**(1) In general**\nThe Chairperson of the committee may, without regard to the civil service laws (including regulations), appoint and terminate an executive director and such other additional personnel as may be necessary to enable the committee to perform its duties, except that the employment of an executive director shall be subject to confirmation by the committee.\n**(2) Compensation**\nThe Chairperson of the committee may fix the compensation of the executive director and other personnel without regard to chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for the executive director and other personnel may not exceed the rate payable for level V of the Executive Schedule under section 5316 of that title.\n##### (c) Detail of government employees\nA Federal Government employee may be detailed to the committee without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n##### (d) Procurement of temporary and intermittent services\nThe Chairperson of the committee may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals that do not exceed the daily equivalent of the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of that title.\n#### 7. Termination of committee\nThe committee shall terminate 30 days after the date on which the committee submits the report required under section 4(c).\n#### 8. Funding\nThis Act shall be carried out using amounts otherwise appropriated, and no additional amounts are authorized to be appropriated to carry out this Act.",
      "versionDate": "2025-11-19",
      "versionType": "Introduced in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3199rs.xml",
      "text": "II\nCalendar No. 379\n119th CONGRESS\n2d Session\nS. 3199\n[Report No. 119\u2013119]\nIN THE SENATE OF THE UNITED STATES\nNovember 19, 2025 Mr. Barrasso (for himself, Mr. Luj\u00e1n , Mrs. Blackburn , Mrs. Capito , Mr. Crapo , Mr. Daines , Mrs. Fischer , Mrs. Gillibrand , Ms. Hassan , Ms. Klobuchar , Mr. Risch , Mr. Warnock , and Mr. Ossoff ) introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nApril 22, 2026 Reported by Mr. Cruz , with an amendment and an amendment to the title Strike out all after the enacting clause and insert the part printed in italic\nA BILL\nTo establish a multi-stakeholder advisory committee tasked with providing detailed recommendations to address challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 988 Lifeline Location Improvement Act of 2025 .\n#### 2. Definitions\nIn this Act:\n**(1) 911 system service provider**\nThe term 911 system service provider has the meaning given the term covered 911 service provider in section 9.19(a)(4) of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate ; and\n**(C)**\nthe Committee on Energy and Commerce of the House of Representatives .\n**(3) Committee**\nThe term committee means the advisory committee established under section 3.\n**(4) Community based mental health organization**\nThe term community based mental health organization means an organization that serves individuals with mental health conditions and the families of those individuals in a community setting.\n**(5) Dispatchable location**\nThe term dispatchable location has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(6) Handset manufacturer**\nThe term handset manufacturer means a manufacturer of cellular phones.\n**(7) Local crisis center**\nThe term local crisis center means a call center intended to receive calls from the 988 Suicide and Crisis Lifeline and the Veterans Crisis Line.\n**(8) Local government**\nThe term local government means the government of any political subdivision of a State.\n**(9) Low population State**\nThe term low population State means a State that has no urbanized areas with a population greater than 250,000, as reported in the decennial census.\n**(10) Mental health services organization**\nThe term mental health services organization means an organization or association that represents providers of mental health crisis services or crisis respite services.\n**(11) Public safety answering point**\nThe term public safety answering point has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(12) Small and rural communities**\nThe term small and rural communities means a noncore area, a micropolitan area, or a small metropolitan statistical area with a population of not more than 250,000, as reported in the decennial census.\n**(13) State**\nThe term State means any of the several States of the United States, the District of Columbia, and any territory or possession of the United States.\n**(14) Telecommunications service provider**\nThe term telecommunications service provider has the meaning given the term service provider in section 52.5(e) of title 47, Code of Federal Regulations, or any successor regulation.\n#### 3. Establishment of committee\n##### (a) Establishment\nNot later than 180 days after the date of enactment of this Act, the Federal Communications Commission, in coordination with the Secretary of Health and Human Services, shall establish an advisory committee to provide recommendations to address challenges to transmitting geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline.\n##### (b) Membership\n**(1) Composition**\n**(A) In general**\nThe committee shall be composed of 15 members, to be appointed in accordance with subparagraphs (B) and (C).\n**(B) Appointments by Federal Communications Commission**\nOf the 15 members of the committee appointed under this paragraph, the Federal Communications Commission shall appoint\u2014\n**(i)**\n1 member from a telecommunications service provider or an organization that represents telecommunications service providers;\n**(ii)**\n1 member from a handset manufacturer or an organization that represents handset manufacturers;\n**(iii)**\n1 member from a public safety answering point or an organization that represents public safety answering points;\n**(iv)**\n1 member from a 911 system service provider or an organization that represents 911 system service providers;\n**(v)**\n2 members from a State government, with at least 1 member representing a low population State; and\n**(vi)**\n2 members from a local government, with at least 1 member representing small and rural communities.\n**(C) Appointments by the Secretary of Health and Human Services**\nOf the 15 members of the committee appointed under this paragraph, the Secretary of Health and Human Services shall appoint\u2014\n**(i)**\n1 member from the 988 Suicide and Crisis Lifeline;\n**(ii)**\n1 member from a local crisis center or an organization that represents local crisis centers;\n**(iii)**\n1 member from the Veterans Crisis Line;\n**(iv)**\n1 member from the Substance Abuse and Mental Health Services Administration;\n**(v)**\n1 member from a mental health services organization;\n**(vi)**\n1 member from a community based mental health organization; and\n**(vii)**\n1 member with experience providing services for people who are deaf or hard of hearing or have hearing loss, such as access to the 988 Suicide and Crisis Lifeline through direct video calling and video relay service.\n**(2) Date**\nThe appointments of the members of the committee shall be made not later than 30 days after the date of enactment of this Act.\n##### (c) Period of appointment; vacancies\n**(1) In general**\nA member of the committee shall be appointed for the life of the committee.\n**(2) Vacancies**\nA vacancy in the committee\u2014\n**(A)**\nshall not affect the powers of the committee; and\n**(B)**\nshall be filled in the same manner as the original appointment.\n##### (d) Meetings\n**(1) Initial meeting**\nNot later than 30 days after the date on which all members of the committee have been appointed, the committee shall hold the first meeting of the committee.\n**(2) Frequency**\nThe committee shall meet at the call of the Chairperson.\n**(3) Quorum**\nA majority of the members of the committee shall constitute a quorum, but a lesser number of members may hold hearings.\n##### (e) Chairperson and Vice Chairperson\nThe committee shall select a Chairperson and Vice Chairperson from among the members of the committee.\n#### 4. Duties of Committee\n##### (a) Study\nThe committee shall conduct a study on\u2014\n**(1)**\npolicy considerations regarding consumer privacy and legal authority with respect to mandating transmission of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline;\n**(2)**\ntechnical implementation standards for telecommunications service providers, 911 system service providers, public safety answering points, and local crisis centers; and\n**(3)**\npotential recovery of costs or additional funding requirements for telecommunications service providers, the 988 Suicide and Crisis Lifeline, the Veterans Crisis Line, and local crisis centers.\n##### (b) Recommendations\nBased on the results of the study conducted under subsection (a), the committee shall develop recommendations on potential legislation that would address challenges relating to the inclusion of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline.\n##### (c) Report\nNot later than 1 year after the date of enactment of this Act, the committee shall submit to appropriate committees of Congress and the Federal Communications Commission a report that contains a detailed statement of the findings and conclusions of the committee, together with the recommendations of the committee for such legislation and administrative actions as the committee considers appropriate.\n#### 5. Powers of committee\n##### (a) Hearings\nThe committee may hold such hearings, sit and act at such times and places, take such testimony, and receive such evidence as the committee considers advisable to carry out this Act.\n##### (b) Information from Federal agencies\n**(1) In general**\nThe committee may secure directly from a Federal department or agency such information as the committee considers necessary to carry out this Act.\n**(2) Furnishing information**\nOn request of the Chairperson of the committee, the head of the department or agency shall furnish the information to the committee.\n##### (c) Postal services\nThe committee may use the United States mails in the same manner and under the same conditions as other departments and agencies of the Federal Government.\n##### (d) Gifts\nThe committee may accept, use, and dispose of gifts or donations of services or property.\n#### 6. Committee personnel matters\n##### (a) Travel expenses\nA member of the committee shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the committee.\n##### (b) Staff\n**(1) In general**\nThe Chairperson of the committee may, without regard to the civil service laws (including regulations), appoint and terminate an executive director and such other additional personnel as may be necessary to enable the committee to perform its duties, except that the employment of an executive director shall be subject to confirmation by the committee.\n**(2) Compensation**\nThe Chairperson of the committee may fix the compensation of the executive director and other personnel without regard to chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for the executive director and other personnel may not exceed the rate payable for level V of the Executive Schedule under section 5316 of that title.\n##### (c) Detail of government employees\nA Federal Government employee may be detailed to the committee without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n##### (d) Procurement of temporary and intermittent services\nThe Chairperson of the committee may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals that do not exceed the daily equivalent of the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of that title.\n#### 7. Termination of committee\nThe committee shall terminate 30 days after the date on which the committee submits the report required under section 4(c).\n#### 8. Funding\nThis Act shall be carried out using amounts otherwise appropriated, and no additional amounts are authorized to be appropriated to carry out this Act.",
      "versionDate": "2026-04-22",
      "versionType": "Reported in Senate"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3199es.xml",
      "text": "119th CONGRESSui\n2d Session\nS. 3199\nIN THE SENATE OF THE UNITED STATES\nAN ACT\nTo instruct the Federal Communications Commission to initiate a notice of inquiry and instruct the Government Accountability Office to complete a study and report providing detailed recommendations to address challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the 988 Lifeline Location Improvement Act of 2026 .\n#### 2. Definitions\nIn this Act:\n**(1) 911 system service provider**\nThe term 911 system service provider has the meaning given the term covered 911 service provider in section 9.19(a)(4) of title 47, Code of Federal Regulations, or any successor regulation.\n**(2) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate;\n**(B)**\nthe Committee on Health, Education, Labor, and Pensions of the Senate ; and\n**(C)**\nthe Committee on Energy and Commerce of the House of Representatives .\n**(3) Dispatchable location**\nThe term dispatchable location has the meaning given that term in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(4) Emergency communications center**\nThe term emergency communications center means\u2014\n**(A)**\na facility that is designed to receive a 911 request for emergency assistance; or\n**(B)**\na public safety answering point, as defined in section 9.3 of title 47, Code of Federal Regulations, or any successor regulation.\n**(5) Telecommunications service provider**\nThe term telecommunications service provider has the meaning given the term service provider in section 52.5(e) of title 47, Code of Federal Regulations, or any successor regulation.\n#### 3. Notice of inquiry\n##### (a) In general\nNot later than 270 days after the date of enactment of this Act, the Federal Communications Commission shall initiate a notice of inquiry to address the challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline.\n##### (b) Evaluation considerations\nIn evaluating responses to the notice of inquiry under subsection (a), the Federal Communications Commission shall consider\u2014\n**(1)**\nlegal authorities with respect to mandating the transmission of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline;\n**(2)**\nthe protection of consumer privacy with respect to mandating the transmission of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline;\n**(3)**\nthe feasibility and technical implementation standards for telecommunications service providers, 911 system service providers, public safety answering points, and local crisis centers with respect to mandating the transmission of geolocation information;\n**(4)**\nan assessment of the potential costs, funding requirements, and options for recovery of costs for telecommunications service providers, the 988 Suicide and Crisis Lifeline, the Veterans Crisis Line, and local crisis centers with respect to mandating the transmission of geolocation information;\n**(5)**\ntechnical challenges associated with mandating the transmission of geolocation information for users who access the 988 American Sign Language line through direct video calling and video relay service; and\n**(6)**\nthe technologies currently available to provide dispatchable location information and methods for transferring location information from 988 centers to 911 centers.\n#### 4. GAO report\n##### (a) In general\nNot later than 180 days after the date of enactment of this Act, the Comptroller General of the United States shall conduct a study and submit to the appropriate committees of Congress a report on the opportunities and challenges related to implementing geolocation for the 988 Suicide and Crisis Lifeline, including\u2014\n**(1)**\npolicy considerations regarding consumer privacy and legal authority with respect to mandating transmission of geolocation information, including dispatchable location information, with calls to the 988 Suicide and Crisis Lifeline;\n**(2)**\ntechnical implementation standards for telecommunications service providers, 911 system service providers, emergency communications centers, and local crisis centers; and\n**(3)**\nthe potential recovery of costs or additional funding requirements for telecommunications service providers, the 988 Suicide and Crisis Lifeline, the Veterans Crisis Line, and local crisis centers.\n##### (b) Consultation\nIn conducting the study under subsection (a), the Comptroller General of the United States shall consult with\u2014\n**(1)**\nrepresentatives from\u2014\n**(A)**\ntelecommunications service providers or organizations that represent telecommunications service providers;\n**(B)**\nhandset manufacturers or organizations that represent handset manufacturers;\n**(C)**\nemergency communications centers or organizations that represent emergency communications centers;\n**(D)**\n911 system service providers or organizations that represent 911 system service providers;\n**(E)**\nState government, including those representing low population States;\n**(F)**\nlocal government, including those representing small and rural communities;\n**(G)**\nthe 988 Suicide and Crisis Lifeline;\n**(H)**\nlocal crisis centers or organizations that represent local crisis centers;\n**(I)**\nthe Veterans Crisis Line;\n**(J)**\nthe Substance Abuse and Mental Health Services Administration;\n**(K)**\nmental health services organizations; and\n**(L)**\ncommunity mental health centers; and\n**(2)**\nindividuals with experience providing services for people who are deaf or hard of hearing or have hearing loss, such as providing access to the 988 Suicide and Crisis Lifeline through direct video calling and video relay service.",
      "versionDate": "",
      "versionType": "Engrossed in Senate"
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
            "name": "Advisory bodies",
            "updateDate": "2026-03-26T18:50:09Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-03-26T18:50:09Z"
          },
          {
            "name": "Emergency communications systems",
            "updateDate": "2026-03-26T18:50:09Z"
          },
          {
            "name": "Government studies and investigations",
            "updateDate": "2026-03-26T18:50:09Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-03-26T18:50:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2026-05-18T20:50:58Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3199is.xml"
        }
      ],
      "type": "Introduced in Senate"
    },
    {
      "date": "2026-04-22",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3199rs.xml"
        }
      ],
      "type": "Reported in Senate"
    },
    {
      "date": "",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3199es.xml"
        }
      ],
      "type": "Engrossed in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "988 Lifeline Location Improvement Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-13T11:03:32Z"
    },
    {
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "A bill to instruct the Federal Communications Commission to initiate a notice of inquiry and instruct the Government Accountability Office to complete a study and report providing detailed recommendations to address challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline, and for other purposes.",
      "titleType": "Official Titles as Amended by Senate",
      "titleTypeCode": "8",
      "updateDate": "2026-05-12T10:56:35Z"
    },
    {
      "billTextVersionCode": "ES",
      "billTextVersionName": "Engrossed in Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "988 Lifeline Location Improvement Act of 2026",
      "titleType": "Short Title(s) as Passed Senate",
      "titleTypeCode": "105",
      "updateDate": "2026-05-12T05:53:24Z"
    },
    {
      "billTextVersionCode": "RS",
      "billTextVersionName": "Reported to Senate",
      "chamberCode": "S",
      "chamberName": "Senate",
      "title": "988 Lifeline Location Improvement Act of 2026",
      "titleType": "Short Title(s) as Reported to Senate",
      "titleTypeCode": "103",
      "updateDate": "2026-04-28T05:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "988 Lifeline Location Improvement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-17T04:23:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a multi-stakeholder advisory committee tasked with providing detailed recommendations to address challenges to transmitting geolocation information with calls to the 988 Suicide and Crisis Lifeline, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-17T04:18:25Z"
    }
  ]
}
```
