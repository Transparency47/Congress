# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2076?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2076
- Title: HCBS Relief Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2076
- Origin chamber: Senate
- Introduced date: 2025-06-12
- Update date: 2025-12-05T21:41:07Z
- Update date including text: 2025-12-05T21:41:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-06-12: Introduced in Senate
- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-12: Introduced in Senate

## Actions

- 2025-06-12 - IntroReferral: Introduced in Senate
- 2025-06-12 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-12",
    "latestAction": {
      "actionDate": "2025-06-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2076",
    "number": "2076",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "L000570",
        "district": "",
        "firstName": "Ben",
        "fullName": "Sen. Luj\u00e1n, Ben Ray [D-NM]",
        "lastName": "Luj\u00e1n",
        "party": "D",
        "state": "NM"
      }
    ],
    "title": "HCBS Relief Act of 2025",
    "type": "S",
    "updateDate": "2025-12-05T21:41:07Z",
    "updateDateIncludingText": "2025-12-05T21:41:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-12",
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
          "date": "2025-06-12T19:26:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VA"
    },
    {
      "bioguideId": "H001046",
      "firstName": "Martin",
      "fullName": "Sen. Heinrich, Martin [D-NM]",
      "isOriginalCosponsor": "True",
      "lastName": "Heinrich",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NM"
    },
    {
      "bioguideId": "F000479",
      "firstName": "John",
      "fullName": "Sen. Fetterman, John [D-PA]",
      "isOriginalCosponsor": "True",
      "lastName": "Fetterman",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "PA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "OR"
    },
    {
      "bioguideId": "W000817",
      "firstName": "Elizabeth",
      "fullName": "Sen. Warren, Elizabeth [D-MA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warren",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MA"
    },
    {
      "bioguideId": "S001203",
      "firstName": "Tina",
      "fullName": "Sen. Smith, Tina [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "K000367",
      "firstName": "Amy",
      "fullName": "Sen. Klobuchar, Amy [D-MN]",
      "isOriginalCosponsor": "True",
      "lastName": "Klobuchar",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MN"
    },
    {
      "bioguideId": "D000622",
      "firstName": "Tammy",
      "fullName": "Sen. Duckworth, Tammy [D-IL]",
      "isOriginalCosponsor": "True",
      "lastName": "Duckworth",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "IL"
    },
    {
      "bioguideId": "G000555",
      "firstName": "Kirsten",
      "fullName": "Sen. Gillibrand, Kirsten E. [D-NY]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillibrand",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NY"
    },
    {
      "bioguideId": "B001288",
      "firstName": "Cory",
      "fullName": "Sen. Booker, Cory A. [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Booker",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "NJ"
    },
    {
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "CT"
    },
    {
      "bioguideId": "R000122",
      "firstName": "John",
      "fullName": "Sen. Reed, Jack [D-RI]",
      "isOriginalCosponsor": "True",
      "lastName": "Reed",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "RI"
    },
    {
      "bioguideId": "W000800",
      "firstName": "Peter",
      "fullName": "Sen. Welch, Peter [D-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Welch",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "VT"
    },
    {
      "bioguideId": "B001230",
      "firstName": "Tammy",
      "fullName": "Sen. Baldwin, Tammy [D-WI]",
      "isOriginalCosponsor": "True",
      "lastName": "Baldwin",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "WI"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "MD"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2025-06-12",
      "state": "OR"
    },
    {
      "bioguideId": "W000802",
      "firstName": "Sheldon",
      "fullName": "Sen. Whitehouse, Sheldon [D-RI]",
      "isOriginalCosponsor": "False",
      "lastName": "Whitehouse",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "RI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2076is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2076\nIN THE SENATE OF THE UNITED STATES\nJune 12, 2025 Mr. Luj\u00e1n (for himself, Mr. Kaine , Mr. Heinrich , Mr. Fetterman , Mr. Merkley , Ms. Warren , Ms. Smith , Ms. Klobuchar , Ms. Duckworth , Mrs. Gillibrand , Mr. Booker , Mr. Blumenthal , Mr. Reed , Mr. Welch , Ms. Baldwin , Mr. Van Hollen , and Mr. Wyden ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for an emergency increase in Federal funding to State Medicaid programs for expenditures on home and community-based services.\n#### 1. Short title\nThis Act may be cited as the HCBS Relief Act of 2025 .\n#### 2. Additional support for Medicaid home and community-based services\n##### (a) Increased FMAP\n**(1) In general**\nNotwithstanding section 1905(b) of the Social Security Act ( 42 U.S.C. 1396d(b) ), in the case of an HCBS program State, the Federal medical assistance percentage determined for the State under section 1905(b) of such Act and, if applicable, increased under subsection (y), (z), or (aa) of section 1905 of such Act ( 42 U.S.C. 1396d ), or section 1915(k) of such Act ( 42 U.S.C. 1396n(k) ), shall be increased by 10 percentage points with respect to expenditures of the State under the State Medicaid program for home and community-based services that are provided during fiscal years 2026 and 2027. In no case may the application of the previous sentence result in the Federal medical assistance percentage determined for a State being more than 95 percent.\n**(2) Definitions**\nIn this section:\n**(A) HCBS program State**\nThe term HCBS program State means a State that meets the condition described in subsection (b) by submitting an application described in such subsection, which is approved by the Secretary pursuant to subsection (c).\n**(B) Home and community-based services**\nThe term home and community-based services means\u2014\n**(i)**\nhome health care services authorized under paragraph (7) of section 1905(a) of the Social Security Act ( 42 U.S.C. 1396d(a) );\n**(ii)**\nbehavioral health services authorized under paragraph (13) of such section;\n**(iii)**\npersonal care services authorized under paragraph (24) of such section;\n**(iv)**\nPACE services authorized under paragraph (26) of such section;\n**(v)**\nservices authorized under subsections (b), (c), (i), (j), and (k) of section 1915 of such Act ( 42 U.S.C. 1396n );\n**(vi)**\nsuch services authorized under a waiver under section 1115 of such Act ( 42 U.S.C. 1315 ); and\n**(vii)**\nsuch other services specified by the Secretary.\n##### (b) Condition\nThe condition described in this subsection, with respect to a State, is that the State submits an application to the Secretary, at such time and in such manner as specified by the Secretary, that includes, in addition to such other information as the Secretary shall require\u2014\n**(1)**\na description of which activities described in subsection (d) that a State plans to implement and a description of how it plans to implement such activities;\n**(2)**\nassurances that all Federal funds attributable to the increase under subsection (a) will be\u2014\n**(A)**\nexpended by the State in accordance with this section not later than September 30, 2029; and\n**(B)**\nused\u2014\n**(i)**\nto implement the activities described in subsection (d);\n**(ii)**\nto supplement, and not supplant, the level of State funds expended for home and community-based services for eligible individuals through programs in effect as of the date of the enactment of this section; and\n**(iii)**\nto increase reimbursement rates for home and community-based services to a level that will support recruitment and retention of a sufficient workforce to provide home and community-based services to eligible individuals; and\n**(3)**\nassurances that the State will conduct adequate oversight and ensure the validity of such data as may be required by the Secretary.\n##### (c) Approval of application\nNot later than 90 days after the date of submission of an application of a State under subsection (b), the Secretary shall certify if the application is complete. Upon certification that an application of a State is complete, the application shall be deemed to be approved for purposes of this section.\n##### (d) Activities To improve the delivery of HCBS\n**(1) In general**\nA State shall work with community partners, such as Area Agencies on Aging, Centers for Independent Living, non-profit home and community-based services providers, and other entities providing home and community-based services, to implement the purposes described in paragraph (2).\n**(2) Focused areas of HCBS improvement**\nThe purposes described in this paragraph, with respect to a State, are the following:\n**(A)**\nTo increase rates for home health agencies and agencies that employ direct support professionals (including independent providers in a self-directed or consumer-directed model) to provide home and community-based services under the State Medicaid program, provided that any agency or individual that receives payment under such an increased rate increases the compensation it pays its home health workers or direct support professionals.\n**(B)**\nTo provide paid sick leave, paid family leave, and paid medical leave for home health workers and direct support professionals.\n**(C)**\nTo provide hazard pay, overtime pay, and shift differential pay for home health workers and direct support professionals.\n**(D)**\nTo improve stability of home health worker and direct support professional jobs, including consistent hours, scheduling, pay, and benefit eligibility.\n**(E)**\nTo provide home and community-based services to eligible individuals who are on waiting lists for programs approved under sections 1115 or 1915 of the Social Security Act ( 42 U.S.C. 1315 , 1396n).\n**(F)**\nTo purchase emergency supplies and equipment, which may include items not typically covered under the Medicaid program, such as personal protective equipment, necessary to enhance access to services and to protect the health and well-being of home health workers and direct support professionals.\n**(G)**\nTo pay for the travel of home health workers and direct support professionals to conduct home and community-based services.\n**(H)**\nTo recruit new home health workers and direct support professionals.\n**(I)**\nTo support family care providers of eligible individuals with needed supplies, equipment, and services, which may include such items as family caregiver pay and respite services.\n**(J)**\nTo pay for training for home health workers and direct support professionals.\n**(K)**\nTo pay for assistive technologies, staffing, and training to facilitate eligible individuals' communication, and other costs incurred in order to facilitate community integration and ensure an individual\u2019s person-centered service plan continues to be fully implemented.\n**(L)**\nTo prepare information and public health and educational materials in accessible formats (including formats accessible to people with low literacy or intellectual disabilities) about prevention, treatment, recovery and other aspects of communicable diseases and threats to the health of eligible individuals, their families, and the general community served by agencies described in subparagraph (A).\n**(M)**\nTo protect the health and safety of home health workers and direct support professionals during public health emergencies and natural disasters.\n**(N)**\nTo pay for interpreters to assist in providing home and community-based services to eligible individuals and to inform the general public about communicable diseases and other public health threats.\n**(O)**\nTo allow day services providers to provide home and community-based services.\n**(P)**\nTo pay for other expenses deemed appropriate by the Secretary to enhance, expand, or strengthen Home and Community-Based Services, including retainer payments, and expenses which meet the criteria of the home and community-based settings rule published on January 16, 2014.\n**(Q)**\nTo assist eligible individuals who had to relocate to a nursing facility or institutional setting from their homes in\u2014\n**(i)**\nmoving back to their homes (including by paying for moving costs, first month\u2019s rent, and other one-time expenses and start-up costs);\n**(ii)**\nresuming home and community-based services;\n**(iii)**\nreceiving mental health services and necessary rehabilitative service to regain skills lost while relocated; and\n**(iv)**\nwhile funds attributable to the increased FMAP under this section remain available, continuing home and community-based services for eligible individuals who were served from a waiting list for such services during the emergency period described in section 1135(g)(1)(B) of the Social Security Act ( 42 U.S.C. 1320b\u20135(g)(1)(B) ).\n##### (e) Reporting requirements\n**(1) State reporting requirements**\nNot later than December 31, 2029, any State with respect to which an application is approved by the Secretary pursuant to subsection (c) shall submit a report to the Secretary that contains the following information:\n**(A)**\nActivities and programs that were funded using Federal funds attributable to such increase.\n**(B)**\nThe number of eligible individuals who were served by such activities and programs.\n**(C)**\nThe number of eligible individuals who were able to resume home and community-based services as a result of such activities and programs.\n**(2) HHS evaluation**\n**(A) In general**\nThe Secretary shall evaluate the implementation and outcomes of this section in the aggregate using an external evaluator with experience evaluating home and community-based services, disability programs, and older adult programs.\n**(B) Evaluation criteria**\nFor purposes of subparagraph (A), the external evaluator shall\u2014\n**(i)**\ndocument and evaluate changes in access, availability, and quality of home and community-based services in each HCBS program State;\n**(ii)**\ndocument and evaluate aggregate changes in access, availability, and quality of home and community-based services across all such States; and\n**(iii)**\nevaluate the implementation and outcomes of this section based on\u2014\n**(I)**\nthe impact of this section on increasing funding for home and community-based services;\n**(II)**\nthe impact of this section on achieving targeted access, availability, and quality of home and community-based services; and\n**(III)**\npromising practices identified by activities conducted pursuant to subsection (d) that increase access to, availability of, and quality of home and community-based services.\n**(C) Dissemination of evaluation findings**\nThe Secretary shall\u2014\n**(i)**\ndisseminate the findings from the evaluations conducted under this paragraph to\u2014\n**(I)**\nall State Medicaid directors; and\n**(II)**\nthe Committee on Energy and Commerce of the House of Representatives, the Committee on Finance of the Senate, and the Special Committee on Aging of the Senate; and\n**(ii)**\nmake all evaluation findings publicly available in an accessible electronic format and any other accessible format determined appropriate by the Secretary.\n**(D) Oversight**\nEach State with respect to which an application is approved by the Secretary pursuant to subsection (c) shall ensure adequate oversight of the expenditure of Federal funds pursuant to such increase in accordance with the Medicaid regulations, including section 1115 and 1915 waiver regulations and special terms and conditions for any relevant waiver or grant program.\n**(3) Non-Application Of The Paperwork Reduction Act**\nChapter 35 of title 44, United States Code (commonly referred to as the Paperwork Reduction Act of 1995 ), shall not apply to the provisions of this subsection.\n##### (f) Additional definitions\nIn this section:\n**(1) Eligible individual**\nThe term eligible individual means an individual who is eligible for or enrolled for medical assistance under a State Medicaid program.\n**(2) Medicaid program**\nThe term Medicaid program means, with respect to a State, the State program under title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ) (including any waiver or demonstration under such title or under section 1115 of such Act ( 42 U.S.C. 1315 ) relating to such title).\n**(3) Secretary**\nThe term Secretary means the Secretary of Health and Human Services.\n**(4) State**\nThe term State has the meaning given such term for purposes of title XIX of the Social Security Act ( 42 U.S.C. 1396 et seq. ).",
      "versionDate": "2025-06-12",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-06-17",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "4029",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To provide for an emergency increase in Federal funding to State Medicaid programs for expenditures on home and community-based services.",
      "type": "HR"
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
        "name": "Health",
        "updateDate": "2025-07-14T15:17:58Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-12",
    "originChamber": "Senate",
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
          "measure-id": "id119s2076",
          "measure-number": "2076",
          "measure-type": "s",
          "orig-publish-date": "2025-06-12",
          "originChamber": "SENATE",
          "update-date": "2025-07-25"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "SENATE",
            "summary-id": "id119s2076v00",
            "update-date": "2025-07-25"
          },
          "action-date": "2025-06-12",
          "action-desc": "Introduced in Senate",
          "summary-text": "<p><strong>HCBS Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily increases the applicable Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for certain approved home- and community-based services that are provided during FY2026-FY2027.</p><p>As a condition for receiving the increased rate, a state must agree to undertake activities to improve the delivery of such services, such as by providing additional benefits to home health workers and by helping individuals who were relocated to nursing facilities move back to their homes.</p>"
        },
        "title": "HCBS Relief Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/s/BILLSUM-119s2076.xml",
    "summary": {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>HCBS Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily increases the applicable Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for certain approved home- and community-based services that are provided during FY2026-FY2027.</p><p>As a condition for receiving the increased rate, a state must agree to undertake activities to improve the delivery of such services, such as by providing additional benefits to home health workers and by helping individuals who were relocated to nursing facilities move back to their homes.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2076"
    },
    "title": "HCBS Relief Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-06-12",
      "actionDesc": "Introduced in Senate",
      "text": "<p><strong>HCBS Relief Act of </strong><strong>2025</strong></p><p>This bill temporarily increases the applicable Federal Medical Assistance Percentage (i.e., federal matching rate) under Medicaid for certain approved home- and community-based services that are provided during FY2026-FY2027.</p><p>As a condition for receiving the increased rate, a state must agree to undertake activities to improve the delivery of such services, such as by providing additional benefits to home health workers and by helping individuals who were relocated to nursing facilities move back to their homes.</p>",
      "updateDate": "2025-07-25",
      "versionCode": "id119s2076"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2076is.xml"
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
      "title": "HCBS Relief Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HCBS Relief Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-03T04:23:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for an emergency increase in Federal funding to State Medicaid programs for expenditures on home and community-based services.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-03T04:18:24Z"
    }
  ]
}
```
