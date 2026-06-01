# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4920?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4920
- Title: BIS IT Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 4920
- Origin chamber: House
- Introduced date: 2025-08-08
- Update date: 2026-04-30T20:50:20Z
- Update date including text: 2026-04-30T20:50:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-08: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 5.
- Latest action: 2025-08-08: Introduced in House

## Actions

- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Introduced in House
- 2025-08-08 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-04-22 - Committee: Committee Consideration and Mark-up Session Held
- 2026-04-22 - Committee: Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 5.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-08",
    "latestAction": {
      "actionDate": "2025-08-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4920",
    "number": "4920",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "BIS IT Modernization Act",
    "type": "HR",
    "updateDate": "2026-04-30T20:50:20Z",
    "updateDateIncludingText": "2026-04-30T20:50:20Z"
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
      "text": "Ordered to be Reported in the Nature of a Substitute by the Yeas and Nays: 39 - 5.",
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
      "actionDate": "2025-08-08",
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
      "actionDate": "2025-08-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-08",
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
            "date": "2026-04-22T20:18:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-08-08T15:31:15Z",
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
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-08-08",
      "state": "NJ"
    },
    {
      "bioguideId": "M001137",
      "district": "5",
      "firstName": "Gregory",
      "fullName": "Rep. Meeks, Gregory W. [D-NY-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Meeks",
      "middleName": "W.",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-08-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "PA"
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
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2026-04-22",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4920ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4920\nIN THE HOUSE OF REPRESENTATIVES\nAugust 8, 2025 Mr. Crow (for himself, Mr. Kean , Mr. Meeks , and Ms. Kamlager-Dove ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo require modernization of information technology systems and applications of the Bureau of Industry and Security of the Department of Commerce.\n#### 1. Short title\nThis Act may be cited as the Bureau of Industry and Security Information Technology Modernization Act or the BIS IT Modernization Act .\n#### 2. Modernization of information technology systems and applications of the Bureau of Industry and Security\n##### (a) Sense of Congress\nIt is the sense of Congress that the effective use of Bureau authorities requires that\u2014\n**(1)**\nthe Bureau adopt and deploy cutting-edge data fusion, analytics, and decision-making capabilities, as well as supply chain illumination tools and additional commercial data sets, to streamline and standardize the export license adjudication process, better assess global industrial relationships, enhance the evaluation of information and communications technologies and services, identify dual use items of concern for control, and identify evasive trade patterns and shell companies being used by adversary militaries;\n**(2)**\nthe Bureau expand and scale up the adoption and use of modern data sharing interfaces and capabilities to share data safely and efficiently with industry, Federal agencies, and international partners;\n**(3)**\nBureau information technology systems should over time enable the incorporation of artificial intelligence, machine learning, and other advanced tools as technologies evolve;\n**(4)**\nthe Bureau expedite Entity List, Military End User List, and Unverified List deliberations tied to countries of concern and enforcement activities related to tracking military end users and end uses in countries of concern, including the People\u2019s Republic of China (PRC), Russia, and Iran;\n**(5)**\nthe Bureau work with relevant agencies to comprehensively map the PRC defense industrial base and its military civil fusion strategy; and\n**(6)**\nthe Bureau work with relevant agencies to comprehensively map the commercial linkages between the industrial bases of the PRC, Russia, North Korea, Iran, and other countries of concern.\n##### (b) In general\nSubject to the availability of appropriations, the Under Secretary of Commerce for Industry and Security shall, on an ongoing basis through fiscal year 2030, modernize the information technology systems of the Bureau.\n##### (c) Elements\nIn carrying out subsection (b), the Under Secretary should\u2014\n**(1)**\nreplace the Bureau\u2019s primary information technology systems with a unified environment that\u2014\n**(A)**\nallows for deployment of a seamless case and customer relationship management information technology solution; and\n**(B)**\nprovides analysis of data obtained from external data providers that is collected by trade transactions and other sources as appropriate;\n**(2)**\nadopt and deploy cutting-edge data fusion, analytics, and decision-making capabilities, as well as supply chain illumination tools, and additional commercial data sets to streamline and standardize the export license adjudication process, and better assess global industrial relationships;\n**(3)**\nenhance the processes that maintain a list of foreign persons determined to be a threat to the national security and foreign policy of the United States, which support Entity List deliberations and, enforcement activities, such as tracking military end users and end uses and identifying evasive trade patterns and shell companies; and\n**(4)**\nexpand and scale up the adoption and use of modern data sharing interfaces and capabilities to share the appropriate data elements safely and efficiently with industry, Federal agencies, including the intelligence community, and international partners.\n##### (d) Objectives\nBefore any informational technology solutions are adopted with respect to the elements in subsection (c), such solutions should be analyzed based on their ability to\u2014\n**(1)**\nenhance productivity and efficiency, including by reducing the need for manual review and processing of data;\n**(2)**\nreduce redundancies and manage costs;\n**(3)**\nenhance the overall data and cyber security of Bureau systems and underlying information technology infrastructure;\n**(4)**\nfacilitate seamless and safe sharing of appropriate data with relevant stakeholders and partners;\n**(5)**\nfacilitate seamless data sharing with relevant agencies and the intelligence community; and\n**(6)**\nenhance the ease of access and user experience for United States parties that are utilizing Bureau systems.\n##### (e) Personnel assessment\nThe Under Secretary should\u2014\n**(1)**\nreassess staffing and personnel needs across the Bureau throughout the modernization process described in this section; and\n**(2)**\nconsult with Congress on whether additional or less personnel may be most effective for utilizing modern applications and systems.\n##### (f) Authorization of appropriations\nThere are authorized to be appropriated $25,000,000 for each of the fiscal years 2026 through 2029 to carry out this Act.\n##### (g) Definitions\nIn this Act:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Foreign Affairs of the House of Representatives; and\n**(B)**\nthe Committee on Banking, Housing, and Urban Affairs of the Senate.\n**(2) Bureau**\nThe term Bureau means the Bureau of Industry and Security of the Department of Commerce.\n**(3) Entity list**\nThe term Entity List means the list maintained by the Bureau and set forth in Supplement No. 4 to part 744 of title 15, Code of Federal Regulations.\n**(4) Under Secretary**\nThe term Under Secretary means the Under Secretary of Commerce for Industry and Security.",
      "versionDate": "2025-08-08",
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
        "updateDate": "2025-09-18T20:57:15Z"
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
      "date": "2025-08-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4920ih.xml"
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
      "title": "BIS IT Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-12T03:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "BIS IT Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bureau of Industry and Security Information Technology Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-12T03:08:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require modernization of information technology systems and applications of the Bureau of Industry and Security of the Department of Commerce.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-12T03:03:30Z"
    }
  ]
}
```
