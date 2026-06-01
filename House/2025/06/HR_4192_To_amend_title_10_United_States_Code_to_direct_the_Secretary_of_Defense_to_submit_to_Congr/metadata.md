# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4192
- Title: the Military PFAS Transparency Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 4192
- Origin chamber: House
- Introduced date: 2025-06-26
- Update date: 2026-04-28T08:06:46Z
- Update date including text: 2026-04-28T08:06:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-06-26: Introduced in House

## Actions

- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Introduced in House
- 2025-06-26 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4192",
    "number": "4192",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001237",
        "district": "8",
        "firstName": "Kristen",
        "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
        "lastName": "McDonald Rivet",
        "party": "D",
        "state": "MI"
      }
    ],
    "title": "the Military PFAS Transparency Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:46Z",
    "updateDateIncludingText": "2026-04-28T08:06:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-26",
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
      "text": "Referred to the House Committee on Armed Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T14:04:25Z",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "MI"
    },
    {
      "bioguideId": "D000624",
      "district": "6",
      "firstName": "Debbie",
      "fullName": "Rep. Dingell, Debbie [D-MI-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Dingell",
      "party": "D",
      "sponsorshipDate": "2025-06-26",
      "state": "MI"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "PA"
    },
    {
      "bioguideId": "K000399",
      "district": "2",
      "firstName": "Jennifer",
      "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Kiggans",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-06-26",
      "state": "VA"
    },
    {
      "bioguideId": "P000614",
      "district": "1",
      "firstName": "Chris",
      "fullName": "Rep. Pappas, Chris [D-NH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Pappas",
      "party": "D",
      "sponsorshipDate": "2025-09-26",
      "state": "NH"
    },
    {
      "bioguideId": "L000606",
      "district": "16",
      "firstName": "George",
      "fullName": "Rep. Latimer, George [D-NY-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Latimer",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-03-26",
      "state": "CO"
    },
    {
      "bioguideId": "M001234",
      "district": "3",
      "firstName": "Kelly",
      "fullName": "Rep. Morrison, Kelly [D-MN-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Morrison",
      "party": "D",
      "sponsorshipDate": "2026-04-20",
      "state": "MN"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-04-27",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4192ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4192\nIN THE HOUSE OF REPRESENTATIVES\nJune 26, 2025 Ms. McDonald Rivet (for herself, Mr. Bergman , Mrs. Dingell , Mr. Fitzpatrick , and Mrs. Kiggans of Virginia ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo amend title 10, United States Code, to direct the Secretary of Defense to submit to Congress an annual report on the funding and status of interim remedial actions of the Department of Defense relating to perfluoroalkyl and polyfluoroalkyl substances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Military PFAS Transparency Act of 2025 .\n#### 2. Annual report on funding and status of interim remedial actions of Department of Defense relating to PFAS\n##### (a) In general\nChapter 160 of title 10, United States Code, is amended by adding at the end the following new section:\n2717. Annual report on perfluoroalkyl and polyfluoroalkyl substances (a) In general Not later than one year after the date of the enactment of this section, and annually thereafter, the Secretary of Defense shall submit to the Committees on Armed Services of the Senate and the House of Representatives a report on the funding and status of interim remedial actions of the Department of Defense relating to perfluoroalkyl and polyfluoroalkyl substances (in this section referred to as PFAS ). (b) Elements Each report required by subsection (a) shall include information regarding the following: (1) The total funding budgeted and obligated, for the current fiscal year and for any prior fiscal year, per site at each installation, for interim remedial actions of the Department of Defense relating to PFAS. (2) In the case of each report after the initial report, the total funding budgeted, obligated and expensed, per site at each installation, on such actions since the previous report. (3) The general and operating status of interim remedial actions related to PFAS per site at each installation, including\u2014 (A) a list of all announced or selected interim remedial actions, and for each such action, the function and role of the action with respect to addressing PFAS at the installation; (B) for each action listed, a phase-specific status update including whether\u2014 (i) the design is pending, in progress, or completed; (ii) contracting is pending, in solicitation, awarded, or delayed; (iii) construction or execution has begun, is in progress, completed, or delayed; (iv) the action is currently operating, its duration, and any performance metrics available; (C) identification of actions that are one-time in nature (such as soil removal and disposal), and the status of each action; (D) timelines for completion of each phase, including original projected timelines and any updates; (E) for any phase delayed by more than 12 months beyond the original projection, a site-specific explanation for the delay; and (F) identification of any administrative, regulatory, funding, or other barriers contributing to delays or budgetary effects, along with the plan of the Secretary to address each such barrier. .\n##### (b) Required remediation acceleration strategy\nNot later than 180 days after the date of the enactment of this Act, the Secretary of Defense shall submit to the congressional defense committees a perfluoroalkyl and polyfluoroalkyl substances remediation acceleration strategy, which shall include\u2014\n**(1)**\ncriteria for prioritizing military installations based on risk to human health, environmental impact, and proximity to affected communities;\n**(2)**\ntimelines for completing each phase of the Comprehensive Environmental Response, Compensation, and Liability Act ( 42 U.S.C. 9601 et seq. ) cleanup process;\n**(3)**\na plan for deploying additional resources, technologies, or personnel to reduce delays, including an identification of\u2014\n**(A)**\nthe number of laboratories that are accredited by the Department of Defense Environmental Laboratory Accreditation Program to test for PFAS; and\n**(B)**\nthe number of laboratories that are in the process of being so accredited; and\n**(4)**\nbenchmarks for evaluating performance of each military department or defense agency on perfluoroalkyl and polyfluoroalkyl substances response efforts.\n##### (c) Public transparency\nNot later than one year after the date of the enactment of this Act, the Secretary of Defense shall make publicly available an accessible online dashboard that includes the actions of the Department of Defense relating to perfluoroalkyl and polyfluoroalkyl substances. The dashboard shall be updated semiannually and shall include a summary of\u2014\n**(1)**\nsite-by-site funding levels and expenditures at each installation;\n**(2)**\nthe status of remediation and investigation efforts;\n**(3)**\nprojected and actual completion timelines; and\n**(4)**\npoints of contact for community engagement.",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-17T18:35:40Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4192ih.xml"
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
      "title": "the Military PFAS Transparency Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "the Military PFAS Transparency Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-10T03:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 10, United States Code, to direct the Secretary of Defense to submit to Congress an annual report on the funding and status of interim remedial actions of the Department of Defense relating to perfluoroalkyl and polyfluoroalkyl substances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-10T03:03:24Z"
    }
  ]
}
```
