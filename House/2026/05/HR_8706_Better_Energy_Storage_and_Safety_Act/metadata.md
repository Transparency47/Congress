# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8706?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8706
- Title: Better Energy Storage and Safety Act
- Congress: 119
- Bill type: HR
- Bill number: 8706
- Origin chamber: House
- Introduced date: 2026-05-07
- Update date: 2026-05-21T17:53:30Z
- Update date including text: 2026-05-21T17:53:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-05-07: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2026-05-07: Introduced in House

## Actions

- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Introduced in House
- 2026-05-07 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-07",
    "latestAction": {
      "actionDate": "2026-05-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8706",
    "number": "8706",
    "originChamber": "House",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "P000613",
        "district": "19",
        "firstName": "Jimmy",
        "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
        "lastName": "Panetta",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Better Energy Storage and Safety Act",
    "type": "HR",
    "updateDate": "2026-05-21T17:53:30Z",
    "updateDateIncludingText": "2026-05-21T17:53:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-05-07",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-05-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-05-07",
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
          "date": "2026-05-07T13:04:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "H001101",
      "district": "10",
      "firstName": "Pat",
      "fullName": "Rep. Harrigan, Pat [R-NC-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Harrigan",
      "party": "R",
      "sponsorshipDate": "2026-05-07",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8706ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8706\nIN THE HOUSE OF REPRESENTATIVES\nMay 7, 2026 Mr. Panetta (for himself and Mr. Harrigan ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo amend the Energy Act of 2020 to modify certain programs and projects with respect to energy storage technology, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Better Energy Storage and Safety Act .\n#### 2. Modification of certain programs and projects with respect to energy storage technology\n##### (a) Clarification of definition of energy storage system\nSubsection (a)(1) of section 3201 of the Energy Act of 2020 ( 42 U.S.C. 17232 ) is amended by inserting (including any components or modules that comprise such a system) after any system .\n##### (b) Energy Storage System Research, Development, and Deployment Program\n**(1) Expanding objectives**\nParagraph (2) of section 3201(b) of the Energy Act of 2020 ( 42 U.S.C. 17232(b) ) is amended\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin the matter preceding clause (i), by inserting modules, after components, ; and\n**(ii)**\nin clause (i), by inserting of residential and utility energy storage systems after deployment ;\n**(B)**\nin subparagraph (I), by striking and after the semicolon; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(K) models, tools, and diagnostic data sets to improve the safe installation and long-term operation of energy storage systems by abating expected failure modes that could damage such a system, including\u2014 (i) component, module, or system failure; and (ii) thermal runaway and other fire and explosion risks; and (L) early detection methods and preventative maintenance techniques relating to failure modes of energy storage systems. .\n**(2) Modifying testing and validation**\nParagraph (3) of section 3201(b) of the Energy Act of 2020 ( 42 U.S.C. 17232(b) ) is amended to read as follows:\n(3) Benchmarking, testing, and validation (A) In general In coordination with one or more National Laboratories, the Director of the National Institute of Standards and Technology, and the Administrator of the United States Fire Administration, the Secretary shall support the development, standardized testing, and validation of energy storage systems specified in subparagraph (B), including test-bed trials and field tests, by developing testing and evaluation methodologies for the following: (i) Storage technologies, controls, and power electronics for such systems under a variety of operating and failure conditions, including such conditions that occur while such a system is being utilized. (ii) Standardized and grid performance testing for energy storage systems, materials, and technologies at each stage of development and at the operational system level. (iii) Reliability, safety, degradation, and durability testing under standard and evolving duty cycles. (iv) Component, module, and integrated system level safety and degradation stress testing to failure. (v) Accelerated life testing protocols to predict estimated lifetime metrics with accuracy. (vi) Equipment, including automated fire suppression systems, and techniques for mitigating risks of such energy storage systems. (B) Energy storage systems specified The energy storage systems specified in this subparagraph are energy storage systems that satisfy the following requirements: (i) Are under the program. (ii) Are operational and connected to the grid. (iii) Were installed before the most recent codes and standards for such systems. (iv) Represent a variety of the following characteristics: (I) Chemistries. (II) Compositions. (III) Installation and manufacturing techniques. (IV) Any other characteristic the Secretary determines appropriate. .\n**(3) Modifying periodic evaluations**\nParagraph (4) of section 3201(b) of the Energy Act of 2020 ( 42 U.S.C. 17232(b) ) is amended\u2014\n**(A)**\nby inserting the testing and evaluation of after advance ; and\n**(B)**\nby striking costs and increasing the duration and inserting costs, increasing the lifetime, and improving the safety .\n**(4) Modifying strategic plan**\nParagraph (5)(B) of section 3201(b) of the Energy Act of 2020 ( 42 U.S.C. 17232(b) ) is amended\u2014\n**(A)**\nin clause (iii)(II)(bb), by striking and the mission of the Department, as determined by the Secretary ;\n**(B)**\nin clause (iv)(II), by striking and after the semicolon;\n**(C)**\nin clause (v), by striking the period at the end and inserting ; and ; and\n**(D)**\nby adding at the end the following new clause:\n(vi) include a summary of the status of any innovative, emerging, or alternative technologies that could improve the performance, durability, or safety of grid-scale energy storage systems and any potential commercial barriers to such innovative, emerging, or alternative technologies. .\n**(5) Leveraging of resources**\nParagraph (6) of section 3201(b) of the Energy Act of 2020 ( 42 U.S.C. 17232(b) ) is amended\u2014\n**(A)**\nin subparagraph (C)\u2014\n**(i)**\nin clause (ii), by adding and at the end; and\n**(ii)**\nin clause (iii), by striking and after the semicolon;\n**(B)**\nin subparagraph (D), by striking the period at the end and inserting a semicolon; and\n**(C)**\nby adding at the end the following new subparagraphs:\n(E) the United States Fire Administration; and (F) the National Institute of Standards and Technology. .\n##### (c) Increasing number of energy storage demonstration projects\nParagraph (1) of section 3201(c) of the Energy Act of 2020 ( 42 U.S.C. 17232(c) ) is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A)\u2014\n**(A)**\nby striking September 30, 2023 and inserting September 30, 2030 ; and\n**(B)**\nby striking 3 and inserting 5 ;\n**(2)**\nin subparagraph (A), by striking and after the semicolon;\n**(3)**\nin subparagraph (B), by striking the period at the end and inserting a semicolon; and\n**(4)**\nby adding at the end the following new subparagraphs:\n(C) at least 1 energy storage system demonstration project designed to further the safety of technologies described in clause (iii) or (iv) of such subsection, including through stress testing to failure; and (D) at least 1 energy storage system demonstration project designed to further the safety of technologies described in clause (v) or (vi) of such subsection, including through stress testing to failure. .\n##### (d) Energy storage pilot grant program\n**(1) Expanding selection requirements**\nParagraph (2)(C)(ii) of section 3201(c) of the Energy Act of 2020 ( 42 U.S.C. 17232(c) ) is amended\u2014\n**(A)**\nin subclause (II), by striking and after the semicolon; and\n**(B)**\nby adding at the end the following new subclauses:\n(IV) improve the safety of operational energy storage systems through component, module, and integrated system level testing and evaluation; and (V) utilize data from such energy storage systems to improve, such as through the prediction of system failure, the safety of such energy storage systems; .\n**(2) Expanding objectives**\nParagraph (2)(D) of section 3201(c) of the Energy Act of 2020 ( 42 U.S.C. 17232(c) ) is amended by adding at the end the following new clauses:\n(xiii) To improve and advance the robustness of testing and evaluation methodologies for energy storage systems. (xiv) To improve and advance data collection mechanisms for operational energy storage systems. (xv) To improve the diagnostic, artificial intelligence, computing, and digital twin capabilities of energy storage systems. (xvi) To improve the safety of installed energy storage systems. (xvii) To test innovative chemistries for grid-connected energy storage systems that are safer than conventional chemistries for such energy storage systems. .\n##### (e) Expanding priorities of the electric vehicle battery second-Life project\nParagraph (3)(C) of section 3201(c) of the Energy Act of 2020 ( 42 U.S.C. 17232(c) ) is amended by inserting advanced safety testing and evaluation methodologies or after from .\n##### (f) Chemistries and stress testing in long-Duration demonstration initiative and joint program\nSubsection (d) of section 3201 of the Energy Act of 2020 ( 42 U.S.C. 17232 ) is amended\u2014\n**(1)**\nin paragraph (3)(A), by inserting and chemistries after types ; and\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (A)\u2014\n**(i)**\nin clause (i), by striking scales; and and inserting scales and with various chemistries; ;\n**(ii)**\nin clause (ii), by striking the period at the end and inserting ; and ; and\n**(iii)**\nby adding at the end the following new clause:\n(iii) to develop safety features that prevent or mitigate the failure of long-duration energy storage technologies. ; and\n**(B)**\nin subparagraph (C)(ii), by inserting for stress testing integrated energy storage systems to failure after appropriate .\n##### (g) Authorization of appropriations\nSubsection (h) of section 3201 of the Energy Act of 2020 ( 42 U.S.C. 17232 ) is amended\u2014\n**(1)**\nin paragraph (2), by striking and ;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(4) to carry out programs, initiatives, and associated activities relating to the safety of energy storage systems and energy storage technologies pursuant to subsections (b) through (d), as the case may be, $30,000,000 for each of fiscal years 2027 through 2031, to remain available until expended. .",
      "versionDate": "2026-05-07",
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
        "name": "Energy",
        "updateDate": "2026-05-21T17:53:30Z"
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
      "date": "2026-05-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8706ih.xml"
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
      "title": "Better Energy Storage and Safety Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-12T12:23:42Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Better Energy Storage and Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-12T12:23:40Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Energy Act of 2020 to modify certain programs and projects with respect to energy storage technology, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-12T12:18:29Z"
    }
  ]
}
```
