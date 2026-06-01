# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8284?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8284
- Title: Bureau of Industry and Security License Administration Enhancement Act
- Congress: 119
- Bill type: HR
- Bill number: 8284
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-22T21:20:25Z
- Update date including text: 2026-05-22T21:20:25Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-04-15",
    "latestAction": {
      "actionDate": "2026-04-15",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8284",
    "number": "8284",
    "originChamber": "House",
    "policyArea": {
      "name": "Foreign Trade and International Finance"
    },
    "sponsors": [
      {
        "bioguideId": "M001157",
        "district": "10",
        "firstName": "Michael",
        "fullName": "Rep. McCaul, Michael T. [R-TX-10]",
        "lastName": "McCaul",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Bureau of Industry and Security License Administration Enhancement Act",
    "type": "HR",
    "updateDate": "2026-05-22T21:20:25Z",
    "updateDateIncludingText": "2026-05-22T21:20:25Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 1.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-22",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
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
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Foreign Affairs Committee",
          "systemCode": "hsfa00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Foreign Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-04-15",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-04-15",
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
            "date": "2026-04-22T20:34:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:00:10Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Foreign Affairs Committee",
      "systemCode": "hsfa00",
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
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
      "state": "MD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8284ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8284\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. McCaul introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo enhance the administration of export control licenses under the Export Control Reform Act of 2018, and other purposes.\n#### 1. Short title\nThis Act may be cited as the Bureau of Industry and Security License Administration Enhancement Act .\n#### 2. Enhancement of administration of export control licenses\nPart I of the Export Control Reform Act of 2018 (50 U.S.C. 4801 et. seq.) is amended by adding at the end the following:\n1769. Enhancement of administration of export control licenses (a) Enhancement of administration of certain communications (1) In general The Secretary shall administer any export control license or other authorization considered pursuant to an is-informed letter or similar targeted regulatory guidance or supplemental license requirement communication sent to a United States person or foreign person by the same interagency process as any license or other authorization administered pursuant to the Export Administration Regulations. (2) Publication Not later than 60 days after issuing a license or other authorization described in paragraph (1), the is-informed letter or similar targeted regulatory guidance or supplemental license requirement communication with respect to the license or authorization shall terminate unless the Secretary, in consultation with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, publishes in the Code of Federal Regulations a regulation that provides for the parameters of the letter or guidance or publishes in the Federal Register the communication. (b) Matters relating to the presumption of denial standard (1) Statement of policy It is the policy of the United States to prevent United States and allied technology from being used to facilitate the military modernization and human rights abuses of foreign adversaries. (2) Standards and factors for presumption of denial standard (A) Publication Not later than 90 days after the date of the enactment of this Act, the Secretary, in consultation with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, shall publish in the Federal Register the standards and factors that licensing officers should consider when considering a license under a presumption of denial standard. (B) Submission to Congress Not later than 7 days prior to the date the Secretary publishes or otherwise makes available to the public such standards and factors, the Secretary shall submit such standards and factors to\u2014 (i) the Committee on Foreign Affairs of the House of Representatives; and (ii) the Committee on Banking, Housing, and Urban Affairs of the Senate. .\n#### 3. Export control technical advisory committees\nSection 1754 of the Export Control Reform Act of 2018 ( 50 U.S.C. 4813 ) is amended by adding at the end the following new subsection:\n(g) Technical advisory committees (1) Duties The technical advisory committees shall advise the Secretary on\u2014 (A) the state of global technology supply chains and the development of advanced technologies by adversaries; (B) national security threats posed by access by adversaries to technologies sourced from the United States or an ally of the United States; (C) technical parameters for export controls; (D) the extent to which existing and proposed export controls achieve the policy of the United States described in section 1752; (E) the identification of emerging and foundational technologies pursuant to section 1758; (F) improvements to export licensing procedures, compliance mechanisms, and export enforcement strategies; and (G) any other matter requested by the Secretary. (2) Required committees The Secretary shall appoint a technical advisory committee for each of the following topics: (A) Computing technologies and information systems, including semiconductors, microelectronics, artificial intelligence, and quantum computing. (B) Biotechnologies. (C) Automation, including robotics, advanced manufacturing, and autonomous systems. (D) Aerospace and space technologies. (E) Advanced materials. (F) Weapons of mass destruction. (G) Emerging and foundational technologies. (H) Regulations and procedures. (3) Subcommittees The Secretary may appoint subcommittees for any technical advisory committee. (4) Committee review Beginning on the date that is 2 years after the date of the enactment of this subsection, the Secretary may, in coordination with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, review the technical advisory committees and create additional committees or adjust the topics of existing committees as necessary. (5) Choosing committees The Secretary, in coordination with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, shall adjust the topics of the technical advisory committees to reflect relevant executive branch strategies and critical technology lists, such as the National Security Strategy, the National Defense Strategy, the AI Action Plan (or a successor plan), the Critical and Emerging Technologies List (or a successor list), and the America First Investment Policy Memorandum (or a successor memorandum). (6) Membership (A) In general The membership of each technical advisory committee shall be equally divided between national security experts, technical specialists from a relevant industry, and academic experts in a relevant field. (B) Term The term of a member on a technical advisory committee shall be 3 years. (C) Non-disclosure agreement No individual may serve as a member of a technical advisory committee unless such individual has entered into a binding non-disclosure agreement with the Secretary that prohibits the individual from making an unauthorized disclosure of proprietary information, policy deliberations, and national security information communicated through or related to a technical advisory committee. (D) Staffing The Secretary shall process applications to join any technical advisory committee in a timely manner. (7) Meetings (A) Frequency Each technical advisory committee shall meet not less frequently than once every 120 days. (B) Submission of minutes The Secretary shall submit to the appropriate congressional committees the minutes of each meeting of a technical advisory committee within 30 days of each meeting. (8) Webpage The Bureau of Industry and Security shall maintain on the website of the Bureau a webpage describing each technical advisory committee, including the membership and meeting schedule of each such committee. (9) Technology and policy assessment Each technical advisory committee shall, not less frequently than annually, submit to the Secretary, the Secretary of State, the Secretary of Defense, the Secretary of Energy, and the appropriate congressional committees\u2014 (A) an assessment of developments within the purview of the technical advisory committee; and (B) recommendations related to the purview of the technical advisory committee for advancing the national security and foreign policy interests of the United States. (10) Definitions In this subsection: (A) Adversary The term adversary means\u2014 (i) the People\u2019s Republic of China, including the Hong Kong and Macau Special Administrative Regions; (ii) the Republic of Cuba; (iii) the Islamic Republic of Iran; (iv) the Democratic People\u2019s Republic of Korea; (v) the Russian Federation; and (vi) any other foreign country listed in Country Group D:5 under Supplement No. 1 to part 740 of the Export Administration Regulations, as published on January 1, 2026, that is designated by the Secretary of State as an adversary for purposes of this section and for which notice of such designation has been published in the Federal Register. (B) Appropriate congressional committees The term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Banking, Housing, and Urban Affairs of the Senate. (C) Technical advisory committee The term technical advisory committee means a technical advisory committee appointed pursuant to subsection (a)(13). .\n#### 4. Review and report regarding controlled integrated circuits\n##### (a) Review\nThe Secretary of Commerce, in coordination with the Secretary of State, Secretary of Defense, and Secretary of Energy, shall regularly review the implementation of the interim final rule of the Bureau of Industry and Security of the Department of Commerce entitled Implementation of Additional Due Diligence Measures for Advanced Computing Integrated Circuits; Amendments and Clarifications; and Extension of Comment Period , published in the Federal Register on January 16, 2025 (90 Fed. Reg. 5298; Docket No. 250108\u20130013), or any substantially similar successor rule, and consider any appropriate update or change to such rule to ensure that such rule is implemented effectively and fulfills the initial policy intent of such rule.\n##### (b) Report\nNot later than 120 days after the date of the enactment of this Act, Secretary of Commerce, in coordination with the Secretary of State, the Secretary of Defense, and the Secretary of Energy, shall submit to the appropriate congressional committees a report on\u2014\n**(1)**\nthe findings of the review required under subsection (a); and\n**(2)**\nany change to the rule described in such subsection that has been made or is under consideration pursuant to such subsection.\n#### 5. Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Secretary**\nThe term Secretary means the Secretary of Commerce acting through the Under Secretary for Industry and Security.",
      "versionDate": "2026-04-15",
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
            "name": "Administrative law and regulatory procedures",
            "updateDate": "2026-05-01T18:37:22Z"
          },
          {
            "name": "Advisory bodies",
            "updateDate": "2026-05-01T18:37:46Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-05-01T18:37:51Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-05-01T18:37:34Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-05-01T18:37:13Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2026-05-01T18:37:07Z"
          },
          {
            "name": "Trade restrictions",
            "updateDate": "2026-05-01T18:37:02Z"
          }
        ]
      },
      "policyArea": {
        "name": "Foreign Trade and International Finance",
        "updateDate": "2026-04-20T23:17:00Z"
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
      "date": "2026-04-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8284ih.xml"
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
      "title": "Bureau of Industry and Security License Administration Enhancement Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T08:23:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Industry and Security License Administration Enhancement Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T08:23:30Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To enhance the administration of export control licenses under the Export Control Reform Act of 2018, and other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T08:18:25Z"
    }
  ]
}
```
