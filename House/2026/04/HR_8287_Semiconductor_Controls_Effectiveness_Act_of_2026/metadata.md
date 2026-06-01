# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8287?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8287
- Title: Semiconductor Controls Effectiveness Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8287
- Origin chamber: House
- Introduced date: 2026-04-15
- Update date: 2026-05-13T17:35:26Z
- Update date including text: 2026-05-13T17:35:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-04-15: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.
- Latest action: 2026-04-15: Introduced in House

## Actions

- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Introduced in House
- 2026-04-15 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8287",
    "number": "8287",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "S001211",
        "district": "4",
        "firstName": "Greg",
        "fullName": "Rep. Stanton, Greg [D-AZ-4]",
        "lastName": "Stanton",
        "party": "D",
        "state": "AZ"
      }
    ],
    "title": "Semiconductor Controls Effectiveness Act of 2026",
    "type": "HR",
    "updateDate": "2026-05-13T17:35:26Z",
    "updateDateIncludingText": "2026-05-13T17:35:26Z"
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 43 - 0.",
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
            "date": "2026-04-22T20:36:00Z",
            "name": "Markup By"
          },
          {
            "date": "2026-04-15T14:02:05Z",
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
      "bioguideId": "I000056",
      "district": "48",
      "firstName": "Darrell",
      "fullName": "Rep. Issa, Darrell [R-CA-48]",
      "isOriginalCosponsor": "True",
      "lastName": "Issa",
      "party": "R",
      "sponsorshipDate": "2026-04-15",
      "state": "CA"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "NY"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-21",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "B001287",
      "district": "6",
      "firstName": "Ami",
      "fullName": "Rep. Bera, Ami [D-CA-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Bera",
      "party": "D",
      "sponsorshipDate": "2026-04-21",
      "state": "CA"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8287ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8287\nIN THE HOUSE OF REPRESENTATIVES\nApril 15, 2026 Mr. Stanton (for himself and Mr. Issa ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require the Assistant Secretary of State for Intelligence and Research to submit a comprehensive report on the impact and effectiveness of United States semiconductor export controls on the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Semiconductor Controls Effectiveness Act of 2026 .\n#### 2. Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nUnited States export controls on semiconductor manufacturing equipment and advanced integrated circuits are critical for United States national security and the Artificial Intelligence race with the People\u2019s Republic of China (PRC);\n**(2)**\nthe efficacy of export controls requires rigorous, data-driven evaluation and assessment;\n**(3)**\nexport controls on semiconductor manufacturing equipment and advanced integrated circuits to the PRC have impacted the PRC\u2019s military modernization efforts, indigenous semiconductor industry, and advanced artificial intelligence development; and\n**(4)**\ngiven the stakes of the strategic and technology competition with the PRC, the American public benefits from public disclosure of the real-world data and impact analysis to understand the national security, foreign policy, and economic impact of specific export control policies.\n#### 3. Report on impact and effectiveness of semiconductor and advanced computing export controls\n##### (a) In general\nNot later than 360 days after the date of the enactment of this Act, the Assistant Secretary of State for Intelligence and Research (in this section referred to as the Assistant Secretary ), in coordination with the Under Secretary of Commerce for Industry and Security and the Director of National Intelligence, shall submit to the appropriate congressional committees a report on the impact and effectiveness of United States semiconductor export controls on the People\u2019s Republic of China (PRC).\n##### (b) Elements\nThe report required by subsection (a) shall include a comprehensive inventory of all United States export controls concerning semiconductors and semiconductor manufacturing equipment (SME) destined for the PRC. For each such control, the report should detail the following:\n**(1)**\nA short description of the control and when it was imposed.\n**(2)**\nWhether the control constitutes a technology control, an end-use control, or an end-user control.\n**(3)**\nWhether such control is unilateral in nature or has been implemented by any international partners and allies.\n**(4)**\nAn analysis, including quantitative data and evidence to the maximum extent practicable, on\u2014\n**(A)**\nthe intended goal or stated purpose of the control when it was originally imposed;\n**(B)**\nthe impact of the control on the PRC\u2019s military, intelligence, and surveillance capabilities;\n**(C)**\nthe impact of the control on the PRC\u2019s ability to develop, manufacture, and acquire advanced integrated circuits;\n**(D)**\nthe impact of the control on the broader PRC indigenous semiconductor industry, its revenue, and global market share;\n**(E)**\nthe impact of the control on PRC artificial intelligence capabilities, including, but not limited to, computing capacity, model usage, and data-processing capacity;\n**(F)**\nthe impact of the control on the revenue and global market share of United States companies, and, if negatively impacted, whether that revenue went to companies headquartered in allied countries or to PRC companies;\n**(G)**\nthe impact of the control on United States long-term technology leadership and global competitiveness; and\n**(H)**\na determination as to whether the control has been and remains effective in achieving its stated national security objective.\n**(5)**\nAn analysis of whether the availability of comparable items, software, or technology from sources outside the United States has undermined the effectiveness of the control. In detailing such foreign availability, the Assistant Secretary shall include whether the foreign availability originates from within the PRC or from allies and partners of the United States.\n##### (c) Additional elements\nThe report required by subsection (a) shall also identify\u2014\n**(1)**\ncontrols that have been the most successful in constraining the PRC\u2019s strategic capabilities;\n**(2)**\na list of controls, if any, that have failed to constrain the PRC and disproportionately harm United States industry without a corresponding advancement in United States national security and foreign policy, and the reason for why the control has failed to constrain the PRC;\n**(3)**\nrecommendations on how to bolster cooperation with United States industry to enhance compliance with the controls and the overall effectiveness of controls; and\n**(4)**\na set of recommendations to improve the efficacy of the export control regime, including\u2014\n**(A)**\nspecific refinements to existing controls;\n**(B)**\nmethods for bolstering enforcement efforts; and\n**(C)**\nrecommendations for closing diversion loopholes.\n##### (d) Stakeholder engagement\nIn carrying out the requirements under subsection (a), the Assistant Secretary shall engage relevant stakeholders to inform the assessment of United States export controls, including\u2014\n**(1)**\nrelevant Federal departments and agencies;\n**(2)**\nprivate sector entities from the United States semiconductor, semiconductor manufacturing equipment, and advanced computing sectors; and\n**(3)**\nindividuals from academic institutions, think tanks, and other research organizations with relevant expertise;\n##### (e) Form\nThe report required by subsection (a) shall be submitted in unclassified form and posted on the Department\u2019s website. The Assistant Secretary of State for Intelligence and Research may include a classified annex as appropriate.\n#### 4. Appropriate congressional committees defined\nIn this Act, the term appropriate congressional committees means\u2014\n**(1)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(2)**\nthe Committee on Foreign Relations and the Committee on Banking, Housing, and Urban Affairs of the Senate.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2026-04-21T21:31:16Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8287ih.xml"
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
      "title": "Semiconductor Controls Effectiveness Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Semiconductor Controls Effectiveness Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-16T12:38:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Assistant Secretary of State for Intelligence and Research to submit a comprehensive report on the impact and effectiveness of United States semiconductor export controls on the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-16T12:33:44Z"
    }
  ]
}
```
