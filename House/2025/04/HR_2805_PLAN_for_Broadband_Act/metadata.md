# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2805?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2805
- Title: PLAN for Broadband Act
- Congress: 119
- Bill type: HR
- Bill number: 2805
- Origin chamber: House
- Introduced date: 2025-04-09
- Update date: 2025-08-27T08:05:34Z
- Update date including text: 2025-08-27T08:05:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-09: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-04-09: Introduced in House

## Actions

- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Introduced in House
- 2025-04-09 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-09",
    "latestAction": {
      "actionDate": "2025-04-09",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2805",
    "number": "2805",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "PLAN for Broadband Act",
    "type": "HR",
    "updateDate": "2025-08-27T08:05:34Z",
    "updateDateIncludingText": "2025-08-27T08:05:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-09",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-09",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-09",
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
          "date": "2025-04-09T16:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "CA"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2025-07-15",
      "state": "MI"
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
      "sponsorshipDate": "2025-08-26",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2805ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2805\nIN THE HOUSE OF REPRESENTATIVES\nApril 9, 2025 Mr. Walberg (for himself and Mr. Peters ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo direct the Assistant Secretary of Commerce for Communications and Information to develop a National Strategy to Close the Digital Divide, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Proper Leadership to Align Networks for Broadband Act or the PLAN for Broadband Act .\n#### 2. National Strategy to Close the Digital Divide\n##### (a) In general\nNot later than 1 year after the date of the enactment of this Act, the Assistant Secretary, in consultation with the heads of the covered agencies, shall develop and submit to the appropriate committees of Congress a National Strategy to Close the Digital Divide to\u2014\n**(1)**\nsupport better management of Federal broadband programs to deliver on the goal of providing high-speed, affordable broadband internet access service to all individuals in the United States;\n**(2)**\nsynchronize interagency coordination among covered agencies for Federal broadband programs;\n**(3)**\nsynchronize interagency coordination regarding the process for approving the grant of an easement, right of way, or lease to, in, over, or on a building or any other property owned by the Federal Government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service; and\n**(4)**\nreduce barriers, lower costs, and ease administrative burdens for State, local, and Tribal governments to participate in Federal broadband programs.\n##### (b) Required contents\nThe Strategy shall\u2014\n**(1)**\nlist all\u2014\n**(A)**\nFederal broadband programs; and\n**(B)**\nprograms that exist at the State and local levels that are directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service;\n**(2)**\ndescribe current, as of the date on which the Strategy is submitted, Federal efforts to coordinate Federal broadband programs;\n**(3)**\nidentify gaps and limitations, including laws, that hinder, or may hinder, coordination across Federal broadband programs;\n**(4)**\nestablish clear roles and responsibilities for the heads of the covered agencies, as well as clear goals, objectives, and performance measures, for\u2014\n**(A)**\nthe management of all Federal broadband programs; and\n**(B)**\ninteragency coordination efforts with respect to Federal broadband programs;\n**(5)**\naddress the cost of the Strategy, the sources and types of resources and investments needed to carry out the Strategy, and where those resources and investments should be targeted based on balancing risk reductions with costs;\n**(6)**\naddress factors that increase the costs and administrative burdens for State, local, and Tribal governments with respect to participation in Federal broadband programs;\n**(7)**\nrecommend incentives, legislative solutions, and administrative actions to help State, local, and Tribal governments more efficiently\u2014\n**(A)**\ndistribute, and effectively administer, funding received from Federal broadband programs; and\n**(B)**\nresolve conflicts with respect to the funding described in subparagraph (A);\n**(8)**\nrecommend incentives, legislative solutions, and administrative actions to\u2014\n**(A)**\nimprove the coordination and management of Federal broadband programs; and\n**(B)**\neliminate duplication with respect to Federal broadband programs;\n**(9)**\ndescribe current, as of the date on which the Strategy is submitted, efforts by covered agencies to streamline the process for granting access to an easement, right of way, or lease to, in, over, or on a building or any other property owned by the Federal Government for the right to install, construct, modify, or maintain infrastructure with respect to broadband internet access service;\n**(10)**\nidentify gaps and limitations with respect to allowing regional, interstate, or cross-border economic development organizations to participate in Federal broadband programs; and\n**(11)**\naddress specific issues relating to closing the digital divide on Tribal lands.\n##### (c) Public consultation\nIn developing the Strategy, the Assistant Secretary shall consult with\u2014\n**(1)**\ngroups that represent consumers or the interests of the public, including economically or socially disadvantaged individuals;\n**(2)**\nsubject matter experts;\n**(3)**\nproviders of broadband internet access service;\n**(4)**\nTribal entities; and\n**(5)**\nState and local agencies and entities.\n#### 3. Implementation Plan\n##### (a) In general\nNot later than 120 days after the date on which the Assistant Secretary submits the Strategy to the appropriate committees of Congress under section 2(a), the Assistant Secretary shall develop and submit to the appropriate committees of Congress an implementation plan for the Strategy.\n##### (b) Required contents\nThe Implementation Plan shall, at a minimum\u2014\n**(1)**\nprovide a plan for implementing the roles, responsibilities, goals, objectives, and performance measures for the management of Federal broadband programs and interagency coordination efforts identified in the Strategy;\n**(2)**\nprovide a plan for holding the covered agencies accountable for the roles, responsibilities, goals, objectives, and performance measures identified in the Strategy;\n**(3)**\ndescribe the roles and responsibilities of the covered agencies, and the interagency mechanisms, to coordinate the implementation of the Strategy;\n**(4)**\nprovide a plan for regular meetings among the heads of the covered agencies to coordinate the implementation of the Strategy and improve coordination among Federal broadband programs and for permitting processes for infrastructure with respect to broadband internet access service;\n**(5)**\nprovide a plan for regular engagement with interested members of the public to evaluate Federal broadband programs, permitting processes for infrastructure with respect to broadband internet access service, and progress in implementing the Strategy;\n**(6)**\nwith respect to the awarding of Federal funds or subsidies to support the deployment of broadband internet access service, provide a plan for the adoption of\u2014\n**(A)**\ncommon data sets regarding those awards, including a requirement that covered agencies use the maps created under title VIII of the Communications Act of 1934 ( 47 U.S.C. 641 et seq. ); and\n**(B)**\napplications regarding those awards, as described in section 903(e) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(e) );\n**(7)**\nprovide a plan to monitor and reduce waste, fraud, and abuse in Federal broadband programs, including wasteful spending resulting from fragmented, overlapping, and unnecessarily duplicative programs;\n**(8)**\nrequire consistent obligation and expenditure reporting by covered agencies for Federal broadband programs, which shall be consistent with section 903(c)(2) of the ACCESS BROADBAND Act ( 47 U.S.C. 1307(c)(2) );\n**(9)**\nprovide a plan to increase awareness of, and participation and enrollment in, Federal broadband programs relating to the affordability and adoption of broadband internet access service; and\n**(10)**\ndescribe the administrative and legislative action that is necessary to carry out the Strategy.\n##### (c) Public comment\nNot later than 30 days after the date on which the Assistant Secretary submits the Strategy to the appropriate committees of Congress under section 2(a), the Assistant Secretary shall seek public comment regarding the development and implementation of the Implementation Plan.\n#### 4. Briefings and implementation\n##### (a) Briefing\nNot later than 21 days after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 3(a), the Assistant Secretary, and appropriate representatives from the covered agencies involved in the formulation of the Strategy, shall provide a briefing on the implementation of the Strategy to the appropriate committees of Congress.\n##### (b) Implementation\n**(1) In general**\nThe Assistant Secretary shall\u2014\n**(A)**\nimplement the Strategy in accordance with the terms of the Implementation Plan; and\n**(B)**\nnot later than 90 days after the date on which the Assistant Secretary begins to implement the Strategy, and not less frequently than once every 90 days thereafter until the date on which the Implementation Plan is fully implemented, brief the appropriate committees of Congress on the progress in implementing the Implementation Plan.\n**(2) Rule of construction**\nNothing in this subsection may be construed to affect the authority or jurisdiction of the Federal Communications Commission or confer upon the Assistant Secretary or any executive agency the power to direct the actions of the Federal Communications Commission, either directly or indirectly.\n#### 5. Government Accountability Office study and report\n##### (a) Study\nThe Comptroller General of the United States shall conduct a study that shall\u2014\n**(1)**\nexamine the efficacy of the Strategy and the Implementation Plan in closing the digital divide; and\n**(2)**\nmake recommendations regarding how to improve the Strategy and the Implementation Plan.\n##### (b) Report\nNot later than 1 year after the date on which the Assistant Secretary submits the Implementation Plan to the appropriate committees of Congress under section 3(a), the Comptroller General shall submit to the appropriate committees of Congress a report on the results of the study conducted under subsection (a).\n#### 6. Definitions\nIn this Act:\n**(1) Appropriate committees of Congress**\nThe term appropriate committees of Congress means\u2014\n**(A)**\nthe Committee on Commerce, Science, and Transportation of the Senate; and\n**(B)**\nthe Committee on Energy and Commerce of the House of Representatives.\n**(2) Assistant Secretary**\nThe term Assistant Secretary means the Assistant Secretary of Commerce for Communications and Information.\n**(3) Covered agencies**\nThe term covered agencies means\u2014\n**(A)**\nthe Federal Communications Commission;\n**(B)**\nthe Department of Agriculture;\n**(C)**\nthe National Telecommunications and Information Administration;\n**(D)**\nthe Department of Health and Human Services;\n**(E)**\nthe Appalachian Regional Commission;\n**(F)**\nthe Delta Regional Authority;\n**(G)**\nthe Economic Development Administration;\n**(H)**\nthe Department of Education;\n**(I)**\nthe Department of the Treasury;\n**(J)**\nthe Department of Transportation;\n**(K)**\nthe Institute of Museum and Library Services;\n**(L)**\nthe Northern Border Regional Commission;\n**(M)**\nthe Department of Housing and Urban Development; and\n**(N)**\nthe Department of the Interior.\n**(4) Federal broadband program**\nThe term Federal broadband program means any program administered by a covered agency that is directly or indirectly intended to increase the deployment of, access to, the affordability of, or the adoption of broadband internet access service.\n**(5) Implementation plan**\nThe term Implementation Plan means the implementation plan developed under section 3(a).\n**(6) State**\nThe term State means each State of the United States, the District of Columbia, and each commonwealth, territory, or possession of the United States.\n**(7) Strategy**\nThe term Strategy means the National Strategy to Close the Digital Divide developed under section 2(a).",
      "versionDate": "2025-04-09",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2025-05-19T16:14:39Z"
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
      "date": "2025-04-09",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2805ih.xml"
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
      "title": "PLAN for Broadband Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-17T11:31:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "PLAN for Broadband Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Proper Leadership to Align Networks for Broadband Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T06:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Assistant Secretary of Commerce for Communications and Information to develop a National Strategy to Close the Digital Divide, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T06:18:32Z"
    }
  ]
}
```
