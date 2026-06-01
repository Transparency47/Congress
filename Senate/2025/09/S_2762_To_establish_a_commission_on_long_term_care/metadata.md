# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2762?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2762
- Title: Supporting Our Seniors Act
- Congress: 119
- Bill type: S
- Bill number: 2762
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-04-16T19:11:53Z
- Update date including text: 2026-04-16T19:11:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2762",
    "number": "2762",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
    },
    "sponsors": [
      {
        "bioguideId": "R000608",
        "district": "",
        "firstName": "Jacky",
        "fullName": "Sen. Rosen, Jacky [D-NV]",
        "lastName": "Rosen",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Supporting Our Seniors Act",
    "type": "S",
    "updateDate": "2026-04-16T19:11:53Z",
    "updateDateIncludingText": "2026-04-16T19:11:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
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
      "actionDate": "2025-09-10",
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
            "date": "2026-03-19T14:00:46Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-09-10T21:01:39Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "B001236",
      "firstName": "John",
      "fullName": "Sen. Boozman, John [R-AR]",
      "isOriginalCosponsor": "True",
      "lastName": "Boozman",
      "party": "R",
      "sponsorshipDate": "2025-09-10",
      "state": "AR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2762is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2762\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Ms. Rosen (for herself and Mr. Boozman ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo establish a commission on long-term care.\n#### 1. Short title\nThis Act may be cited as the Supporting Our Seniors Act .\n#### 2. Commission on Long-Term Care\n##### (a) In general\nThere is established a commission to be known as the Commission on Long-Term Care (referred to in this section as the Commission ).\n##### (b) Membership\n**(1) Composition**\n**(A) Members**\nThe Commission shall be composed of 12 members, of whom\u2014\n**(i)**\n6 shall be appointed by the President;\n**(ii)**\n2 shall be appointed by the Speaker of the House of Representatives;\n**(iii)**\n1 shall be appointed by the minority leader of the House of Representatives;\n**(iv)**\n2 shall be appointed by the majority leader of the Senate; and\n**(v)**\n1 shall be appointed by the minority leader of the Senate.\n**(B) Qualifications**\nEach member appointed under subparagraph (A) shall have experience in one or more of the following areas:\n**(i)**\nPalliative care.\n**(ii)**\nHospice care.\n**(iii)**\nHome and community-based services delivery.\n**(iv)**\nLabor and workforce development.\n**(v)**\nAging and geriatrics.\n**(vi)**\nAdvocating for the disability community.\n**(vii)**\nLong-term care insurance.\n**(viii)**\nAdvocating for patients and caregivers.\n**(ix)**\nSenior housing, including varied levels of assistance ranging from independent living to nursing facilities.\n**(C) Diversity of qualifications**\n**(i) In general**\nIn making appointments to the Commission under subparagraph (A), the President and the congressional leaders shall make every effort to select individuals whose qualifications are not already represented by other members of the Commission.\n**(ii) Representation of all qualification areas**\nIf no member of the Commission has experience in an area identified in subparagraph (B), the Secretary of Health and Human Services shall appoint an agency detailee or stakeholder representative who has experience in such area to be present for all meetings of the Commission.\n**(2) Date of appointments**\nThe appointments of the members of the Commission shall be made not later than 90 days after the date of enactment of this Act.\n**(3) Member terms; vacancies**\n**(A) Member terms**\nMembers shall be appointed to the Commission for terms of 6 years (in the case of members appointed by the President) and 4 years (in the case of all other members). There shall be no limitation on the number of terms a member may be appointed for.\n**(B) Vacancies**\nAny vacancy in the Commission shall not affect its powers, but shall be filled in the same manner as the original appointment.\n**(4) Chairperson**\nThe President shall select a Chairperson for the Commission from among its members.\n##### (c) Meetings\n**(1) Initial meeting**\nNot later than 60 days after the date on which a majority of the members of the Commission have been appointed, the Commission shall hold its first meeting.\n**(2) Meetings**\nThe Commission shall meet at the call of the Chairperson.\n**(3) Quorum**\nA majority of the members of the Commission shall constitute a quorum, but a lesser number of members may hold hearings.\n##### (d) Duties of the Commission\n**(1) In general**\nThe Commission shall not later than 1 year after the date of enactment of this Act, and on a yearly basis thereafter, submit policy recommendations to Congress, the President, appropriate Federal agencies, and the public with respect to the following:\n**(A)**\nLong-term care coverage for the non-Medicaid eligible population.\n**(B)**\nConsiderations for aging in place.\n**(C)**\nFinancing options for long-term care for low- and middle-income individuals.\n**(D)**\nCaregiver supports and workforce stability and preparedness.\n**(E)**\nAccess to comprehensive care, including geriatric care as appropriate, coordination of medical and personal care needs, and access to palliative care as needed, including both concurrently with curative treatment for serious illness or injury and as hospice end-of-life care.\n**(F)**\nAffordability of services.\n**(G)**\nConsiderations for children and non-senior adults with disabilities.\n**(H)**\nSupport for adult children caring for aging parents, including through health benefits, tax credits, and other tax incentives for caregivers who are not able to claim their parents as dependents for tax purposes.\n**(I)**\nIntegrating meals, access to basic services, and wraparound community services.\n**(J)**\nReducing hospitalization costs through increased access to home-based services, including with options through the Medicare and Medicaid programs.\n**(2) Interaction with outside groups**\nIn developing the recommendations under paragraph (1), the Commission shall regularly consult with\u2014\n**(A)**\na wide variety of stakeholder groups;\n**(B)**\nthe Medicare Payment Advisory Commission and the Medicaid and CHIP Payment and Access Commission; and\n**(C)**\nState and county aging agencies.\n**(3) Federal agency response**\nNot later than 6 months after the submission of a report required under paragraph (1), any Federal agency that is affected by a recommendation described in the report shall submit to Congress a report containing the response of the Federal agency to the recommendation and the plans of the Federal agency to address the recommendation.\n##### (e) Powers of the Commission\n**(1) In general**\nThe Commission may hold such hearings, sit and act at such times and places, take such testimony, and receive such evidence as the Commission considers advisable to carry out this Act. The Commission shall have the authority to exercise these powers via video conference or other remote technology as it determines to be appropriate.\n**(2) Information from federal agencies**\nThe Commission may secure directly from any Federal department or agency such information as the Commission considers necessary to carry out this Act. Upon request of the Chairperson of the Commission, the head of such department or agency shall furnish such information to the Commission.\n**(3) Postal services**\nThe Commission may use the United States mails in the same manner and under the same conditions as other departments and agencies of the Federal Government.\n**(4) Gifts**\nThe Commission may accept, use, and dispose of gifts or donations of services or property so long as such gifts or donations are publicly disclosed.\n##### (f) Commission personnel matters\n**(1) Travel expenses**\nThe members of the Commission shall be allowed travel expenses, including per diem in lieu of subsistence, at rates authorized for employees of agencies under subchapter I of chapter 57 of title 5, United States Code, while away from their homes or regular places of business in the performance of services for the Commission.\n**(2) Staff**\n**(A) In general**\nThe Chairperson of the Commission may, without regard to the civil service laws and regulations, appoint and terminate an executive director and such other additional personnel as may be necessary to enable the Commission to perform its duties. The employment of an executive director shall be subject to confirmation by the Commission.\n**(B) Compensation**\nThe Chairperson of the Commission may fix the compensation of the executive director and other personnel without regard to chapter 51 and subchapter III of chapter 53 of title 5, United States Code, relating to classification of positions and General Schedule pay rates, except that the rate of pay for the executive director and other personnel may not exceed the rate payable for level V of the Executive Schedule under section 5316 of such title.\n**(3) Detail of government employees**\nAt the discretion of the relevant agency, any Federal Government employee may be detailed to the Commission without reimbursement, and such detail shall be without interruption or loss of civil service status or privilege.\n**(4) Procurement of temporary and intermittent services**\nThe Chairperson of the Commission may procure temporary and intermittent services under section 3109(b) of title 5, United States Code, at rates for individuals that do not exceed the daily equivalent of the annual rate of basic pay prescribed for level V of the Executive Schedule under section 5316 of such title.\n##### (g) Termination of the Commission\nThe Commission shall terminate on the date that is 10 years after the date of enactment of this Act.\n#### 3. Authorization of appropriations\nThere are authorized to be appropriated such sums as are necessary to carry out this Act.",
      "versionDate": "2025-09-10",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Advisory bodies",
            "updateDate": "2026-04-16T19:11:35Z"
          },
          {
            "name": "Aging",
            "updateDate": "2026-04-16T19:11:26Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-04-16T19:11:39Z"
          },
          {
            "name": "Family services",
            "updateDate": "2026-04-16T19:11:52Z"
          },
          {
            "name": "Health care costs and insurance",
            "updateDate": "2026-04-16T19:11:43Z"
          },
          {
            "name": "Health care coverage and access",
            "updateDate": "2026-04-16T19:11:48Z"
          },
          {
            "name": "Long-term, rehabilitative, and terminal care",
            "updateDate": "2026-04-16T19:11:30Z"
          }
        ]
      },
      "policyArea": {
        "name": "Social Welfare",
        "updateDate": "2025-09-23T16:13:32Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2762is.xml"
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
      "title": "Supporting Our Seniors Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Supporting Our Seniors Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to establish a commission on long-term care.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:20Z"
    }
  ]
}
```
