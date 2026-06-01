# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hconres/32?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/32
- Title: Congressional Evidence-Based Policymaking Resolution
- Congress: 119
- Bill type: HCONRES
- Bill number: 32
- Origin chamber: House
- Introduced date: 2025-05-13
- Update date: 2025-11-13T09:05:45Z
- Update date including text: 2025-11-13T09:05:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-13: Introduced in House
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Submitted in House
- 2025-05-13 - IntroReferral: Submitted in House
- Latest action: 2025-05-13: Submitted in House

## Actions

- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-05-13 - IntroReferral: Submitted in House
- 2025-05-13 - IntroReferral: Submitted in House

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-13",
    "latestAction": {
      "actionDate": "2025-05-13",
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-concurrent-resolution/32",
    "number": "32",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "T000480",
        "district": "4",
        "firstName": "William",
        "fullName": "Rep. Timmons, William R. [R-SC-4]",
        "lastName": "Timmons",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Congressional Evidence-Based Policymaking Resolution",
    "type": "HCONRES",
    "updateDate": "2025-11-13T09:05:45Z",
    "updateDateIncludingText": "2025-11-13T09:05:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "committees": {
        "item": {
          "name": "Committee on House Administration",
          "systemCode": "hsha00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on House Administration, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-05-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
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
          "date": "2025-05-13T16:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-05-13T16:03:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Committee on House Administration",
      "systemCode": "hsha00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "OH"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-05-13",
      "state": "CO"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sponsorshipDate": "2025-05-23",
      "state": "IN"
    },
    {
      "bioguideId": "M001213",
      "district": "1",
      "firstName": "Blake",
      "fullName": "Rep. Moore, Blake D. [R-UT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "middleName": "D.",
      "party": "R",
      "sponsorshipDate": "2025-05-23",
      "state": "UT"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2025-11-12",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres32ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. CON. RES. 32\nIN THE HOUSE OF REPRESENTATIVES\nMay 13, 2025 Mr. Timmons (for himself, Mr. Landsman , Ms. Pettersen , and Mr. Bacon ) submitted the following concurrent resolution; which was referred to the Committee on House Administration , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nCONCURRENT RESOLUTION\nEstablishing the Commission on Evidence-Based Policymaking to review, analyze, and make recommendations to Congress to promote the use of Federal data for evidence-building and evidence-based policymaking, and for other purposes.\n#### 1. Short title\nThis concurrent resolution may be cited as the Congressional Evidence-Based Policymaking Resolution .\n#### 2. Commission on Evidence-Based Policymaking\n##### (a) Establishment\nThere is established in the legislative branch the Commission on Evidence-Based Policymaking (in this section referred to as the Commission ) to review, analyze, and make recommendations with respect to promoting the use of Federal data for evidence-building and evidence-based policymaking.\n##### (b) Membership\nThe Commission shall be composed of 12 members, appointed not later than 45 days after the date of the adoption of this resolution, as follows:\n**(1)**\nThree shall be appointed by the Speaker of the House of Representatives, of whom\u2014\n**(A)**\none shall be an academic researcher specializing in Congress, social science, or data science;\n**(B)**\none shall be a former Member or senior staffer of the House; and\n**(C)**\none shall be an employee of an office that participates in the Congressional Data Task Force or other legislative branch support agency as appropriate for the purposes of studying and developing the recommendations under subsection (g).\n**(2)**\nThree shall be appointed by the minority leader of the House of Representatives, of whom\u2014\n**(A)**\none shall be an academic researcher specializing in Congress, social science, or data science;\n**(B)**\none shall be a former Member or senior staffer of the House; and\n**(C)**\none shall be an employee of an office that participates in the Congressional Data Task Force or other legislative branch support agency as appropriate for the purposes of studying and developing the recommendations under subsection (g).\n**(3)**\nThree shall be appointed by the majority leader of the Senate, of whom\u2014\n**(A)**\none shall be an academic researcher specializing in Congress, social science, or data science;\n**(B)**\none shall be a former Member or senior staffer of the Senate; and\n**(C)**\none shall be an employee of an office that participates in the Congressional Data Task Force or other legislative branch support agency as appropriate for the purposes of studying and developing the recommendations under subsection (g).\n**(4)**\nThree shall be appointed by the minority leader of the Senate, of whom\u2014\n**(A)**\none shall be an academic researcher specializing in Congress, social science, or data science;\n**(B)**\none shall be a former Member or senior staffer of the Senate; and\n**(C)**\none shall be an employee of an office that participates in the Congressional Data Task Force or other legislative branch support agency as appropriate for the purposes of studying and developing the recommendations under subsection (g).\n##### (c) Prohibition against service by current Members of Congress\nAn individual is not eligible to serve on the Commission if the individual is a current Member of Congress (including a Delegate or Resident Commissioner to the Congress).\n##### (d) Co-Chairs\nThe Speaker of the House of Representatives and the majority leader of the Senate shall each select one member of the Commission to serve as co-chairs.\n##### (e) Terms; vacancies\nEach member shall be appointed for the duration of the Commission. Any vacancy in the Commission shall not affect its powers, and shall be filled in the manner in which the original appointment was made.\n##### (f) Staff\n**(1) Director**\nThe Commission shall have a Director who shall be appointed jointly by the co-chairs. The Director shall be paid at a rate of pay established by the co-chairs, not to exceed the annual rate of basic pay payable for level V of the Executive Schedule under section 5316 of title 5, United States Code.\n**(2) Other staff**\nThe Director may appoint and fix the pay of not more than 8 full-time equivalent employees and 4 part-time employees.\n**(3) Coverage under Congressional Accountability Act of 1995**\nFor purposes of the Congressional Accountability Act of 1995 ( 2 U.S.C. 1301 et seq. )\u2014\n**(A)**\nthe Commission shall be treated as an employing office under the Act; and\n**(B)**\nan employee of the Commission shall be treated as a covered employee under the Act.\n**(4) Detail of employees**\nAt the request of the Commission, an employee of an office of the House of Representatives or Senate may be detailed to the Commission to assist the Commission with carrying out its duties.\n##### (g) Recommendations\n**(1) In general**\nThe Commission shall study and consider approval of applicable recommendations with respect to evidence-based policymaking within the Federal Government, including\u2014\n**(A)**\nhow Congress may encourage Federal agencies to produce and prioritize evidence on effectiveness for major new programs and reauthorizations, consistent with the Foundations for Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ) and the amendments made by such Act;\n**(B)**\nhow Congress may encourage Federal agencies to support States in making data more open and accessible, in a manner similar to that provided under the Foundations for Evidence-Based Policymaking Act of 2018 ( Public Law 115\u2013435 ) and the amendments made by such Act;\n**(C)**\nhow Congress can revise existing laws or enact new laws to improve access to administrative and survey data for evidence building;\n**(D)**\nhow to incorporate evidence such as outcomes measurement, rigorous impact analysis, and implementation-aligned language into the lawmaking process;\n**(E)**\nhow Congress can access and incorporate real-time, structured, integrated, and machine-readable data into the lawmaking process;\n**(F)**\nthe potential need for and duties of a congressional Chief Data Officer, including whether the officer should be located in a stand-alone office or housed within another existing agency and how such an office would function with existing data and transformation units in Congress; and\n**(G)**\nways to increase data and data privacy expertise in Congress through the incorporation of technologists, data scientists, data analysts, privacy experts, social scientists, and engineers to assist in policy evaluation and legislative drafting.\n**(2) Adoption of recommendations**\nAny recommendation considered by the Commission shall only be considered adopted by the Commission upon receiving the votes of at least two-thirds of the members of the Commission.\n##### (h) Reports\n**(1) Interim reports**\nThe Commission may submit to the Speaker of the House and the majority leader of the Senate interim reports containing such findings, conclusions, and recommendations as have been agreed to by at least two-thirds of the members of the Commission.\n**(2) Final report**\nNot later than the final day of the One Hundred Nineteenth Congress, the Commission shall submit a report to the Speaker of the House and the majority leader of the Senate on the activities and findings of the Commission.\n##### (i) Authorization of appropriations\nThere are authorized to be appropriated such sums as may be necessary to carry out this section, of which\u2014\n**(1)**\n50 percent shall be derived from the applicable accounts of the House of Representatives; and\n**(2)**\n50 percent shall be derived from the contingent fund of the Senate.",
      "versionDate": "2025-05-13",
      "versionType": "IH"
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
        "name": "Congress",
        "updateDate": "2025-05-20T14:58:38Z"
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
      "date": "2025-05-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hconres/BILLS-119hconres32ih.xml"
        }
      ],
      "type": "IH"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "Congressional Evidence-Based Policymaking Resolution",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-14T08:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Congressional Evidence-Based Policymaking Resolution",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-14T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Establishing the Commission on Evidence-Based Policymaking to review, analyze, and make recommendations to Congress to promote the use of Federal data for evidence-building and evidence-based policymaking, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-14T08:18:21Z"
    }
  ]
}
```
