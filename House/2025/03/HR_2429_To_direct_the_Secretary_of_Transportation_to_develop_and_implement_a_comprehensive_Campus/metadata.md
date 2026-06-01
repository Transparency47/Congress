# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2429?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2429
- Title: To direct the Secretary of Transportation to develop and implement a comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 2429
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2026-02-03T09:05:38Z
- Update date including text: 2026-02-03T09:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Armed Services.
- Latest action: 2025-03-27: Introduced in House

## Actions

- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Armed Services.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-27",
    "latestAction": {
      "actionDate": "2025-03-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2429",
    "number": "2429",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "To direct the Secretary of Transportation to develop and implement a comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-02-03T09:05:38Z",
    "updateDateIncludingText": "2026-02-03T09:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
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
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-27",
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
          "date": "2025-03-27T13:04:05Z",
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
      "bioguideId": "G000602",
      "district": "4",
      "firstName": "Laura",
      "fullName": "Rep. Gillen, Laura [D-NY-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Gillen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-03-31",
      "state": "NY"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "MN"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "NJ"
    },
    {
      "bioguideId": "O000176",
      "district": "2",
      "firstName": "Johnny",
      "fullName": "Rep. Olszewski, Johnny [D-MD-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Olszewski",
      "party": "D",
      "sponsorshipDate": "2025-04-07",
      "state": "MD"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-04-09",
      "state": "FL"
    },
    {
      "bioguideId": "M001232",
      "district": "6",
      "firstName": "April",
      "fullName": "Rep. McClain Delaney, April [D-MD-6]",
      "isOriginalCosponsor": "False",
      "lastName": "McClain Delaney",
      "party": "D",
      "sponsorshipDate": "2025-04-24",
      "state": "MD"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-04-24",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-05-19",
      "state": "NJ"
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
      "sponsorshipDate": "2025-06-04",
      "state": "PA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-07-10",
      "state": "NY"
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
      "sponsorshipDate": "2025-10-03",
      "state": "VA"
    },
    {
      "bioguideId": "S001145",
      "district": "9",
      "firstName": "Janice",
      "fullName": "Rep. Schakowsky, Janice D. [D-IL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Schakowsky",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-12-18",
      "state": "IL"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2429ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2429\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Mr. Garbarino (for himself, Ms. Gillen , Mrs. Kiggans of Virginia , Mr. Suozzi , and Mr. LaLota ) introduced the following bill; which was referred to the Committee on Armed Services\nA BILL\nTo direct the Secretary of Transportation to develop and implement a comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, and for other purposes.\n#### 1. Authorization of appropriations for United States Merchant Marine Academy infrastructure and facilities modernization\n##### (a) Findings\nCongress finds the following:\n**(1)**\nThe United States Merchant Marine Academy plays a critical role in training service-obligated licensed merchant mariners to operate commercial vessels, in peacetime and during times of conflict.\n**(2)**\nThe United States Merchant Marine Academy is 1 of the 5 Federal service academies and plays a critical role in maintaining a domestic, commercial maritime industry, with each graduate having a commitment to serve not less than 8 years in the foreign and domestic commerce and the national defense of the United States, which may include service on a merchant vessel documented under chapter 121 of title 46, and graduates make up more than 80 percent of the United States Navy\u2019s Strategic Sealift Officer Program.\n**(3)**\nThe United States defense readiness relies on a strong investment in educating and training militarily obligated United States Merchant Marine officers at the United States Merchant Marine Academy.\n**(4)**\nMost of the facilities at the United States Merchant Marine Academy date back to the Academy\u2019s founding, have not been modernized since, and are not conducive to the immersive training and demanding coursework today\u2019s Midshipmen are required to complete.\n**(5)**\nRehabilitating and modernizing the campus infrastructure at the United States Merchant Marine Academy is necessary to ensuring current and future generations of Midshipmen receive a first-class education.\n##### (b) Sense of the House of Representatives\nIt is the sense of the House of Representatives\u2014\n**(1)**\nto ensure that the United States continues to have a sufficient number of service-obligated licensed merchant mariners to meet current and future national security needs, the Maritime Administration and the Department of Transportation have a responsibility to provide suitable academic, training, and dormitory facilities at the United States Merchant Marine Academy by rapidly implementing a comprehensive plan for campus-wide modernization in accordance with section 51329 of title 46, United States Code, (referred to in this section as the Campus Modernization Plan ) and providing sufficient accountability and oversight to ensure that milestones in such plan are met;\n**(2)**\nin developing the comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, the Maritime Administration, and the Department of Transportation should utilize, to the maximum extent practicable, the Merchant Marine Academy Full Speed Ahead Plan developed by the Maritime Security Infrastructure Council as summarized in the Congressional Record, dated February 28, 2024;\n**(3)**\ngiven the conditions of the United States Merchant Marine Academy as of the date of enactment of this section, a comprehensive, campus-wide modernization is needed to significantly upgrade or replace facilities throughout the campus; and\n**(4)**\nthe Maritime Administration and the Department of Transportation should identify opportunities to utilize design-build contracts to increase delivery times and reduce costs.\n##### (c) Campus modernization plan\nChapter 513 of title 46, United States Code, is amended by adding at the end the following:\n51329. 10-year campus modernization plan (a) In general Not later than 180 days after the date of enactment of this section, the Secretary shall develop and begin to implement a comprehensive Campus Modernization Plan (referred to in this section as the Campus Modernization Plan ), informed by the United States Merchant Marine Academy Full Speed Ahead Plan developed by the Maritime Security Infrastructure Council as summarized in the Congressional Record, dated February 28, 2024, to carry out a campus-wide modernization at the United States Merchant Marine Academy. (b) Objectives In carrying out the Campus Modernization Plan, the Administrator shall prioritize the following objectives: (1) Promoting modern education best practices by constructing learning facilities that leverage state-of-the art technologies and learning best practices. (2) Providing Midshipmen with access to facilities needed to pass the United States Coast Guard License Exam for Third Mate or Third Assistant Engineer Unlimited. (3) Ensuring Midshipmen have access to facilities sufficient to enable Midshipmen to maintain physical readiness standards required of United States Navy officers. (4) Developing campus infrastructure to ensure the Academy attracts a diverse pool of applicants. (5) Providing facilities that enable industry engagement and continuing education opportunities. (6) Maintaining a safe and secure campus environment for all Midshipmen, which shall include any facilities or infrastructure needed to meet the requirements of sections 51326, 51327, or 51328. (7) Implementing, to the extent practicable, the facilities and infrastructure recommendations in chapter 4 of the report titled Organizational Assessment of the United States Merchant Marine Academy: A Path Forward issued by the National Academy of Public Administration in November 2021. (c) Inclusions In meeting the objectives described in subsection (b), the Campus Modernization Plan shall include\u2014 (1) construction of new facilities or significant renovation of existing facilities to provide\u2014 (A) Standards of Training, Certification, and Watchkeeping applications laboratories; (B) a Safety Of Life At Sea training pool; (C) engineering powerplant laboratories; (D) athletic facilities that meet the needs of both male and female students; (E) enhanced waterfront facilities, to include a new pier; (F) a visitor welcome center and main campus security office building; (G) housing facilities for senior staff and faculty; and (H) sufficient parking facilities for faculty, staff, and campus visitors; (2) upgrades to all classrooms and laboratories with modern information technology infrastructure; (3) a campus-wide upgrade and retrofit of\u2014 (A) the electric distribution power grid; (B) the sanitary sewer system piping; (C) the storm drainage system; and (D) the drinking water system, including development of a separate and redundant fire suppression system; and (4) renovations of existing campus facilities to ensure all campus facilities\u2014 (A) are structurally sound; (B) have reliable heating and air conditioning systems; (C) have functioning plumbing and electrical systems; (D) are protected from the elements, including through roof replacements and window repairs or replacements, as needed; (E) are accessible in accordance with the Americans with Disabilities Act of 1990; and (F) have working fire alarm and fire suppression systems. (d) Requirements For the duration of the Campus Modernization Plan, the Administrator shall ensure that the Academy remains fully operational. (e) Use of a Federal construction agent Consistent with the requirements of section 3515(d)(3) of the James M. Inhofe National Defense Authorization Act for Fiscal Year 2023 ( Public Law 117\u2013263 ), the Administrator shall seek to enter into an agreement with a Federal construction agent to carry out the Campus Modernization Plan authorized under subsection (a). (f) Authorization of appropriations There are authorized to be appropriated to the Secretary of Transportation, out of the Maritime Security Trust Fund established under section 9512 of the Internal Revenue Code of 1986, for fiscal years 2026 through 2035, for the phased rehabilitation, modernization, and construction of facilities and infrastructure at the United States Merchant Marine Academy, in accordance with this section, including the Campus Modernization Plan authorized in subsection (a), $1,020,000,000 of which\u2014 (1) $54,000,000 is authorized to be appropriated for fiscal year 2026 for design and planning purposes, which shall be used for the development of a design-build plan for the phased rehabilitation, modernization, and construction of facilities and infrastructure at the United States Merchant Marine Academy in accordance with the Campus Modernization Plan; and (2) for fiscal years 2026 through 2035, $107,333,333 is authorized to be appropriated for each fiscal year for construction and contingency purchases necessary to execute the Campus Modernization Plan. .\n##### (d) Clerical amendment\nThe analysis for chapter 513 of title 46, United States Code, is amended by adding at the end the following:\n51329. 10-Year Campus Modernization Plan. .",
      "versionDate": "2025-03-27",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-04-30",
        "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation."
      },
      "number": "1541",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHIPS for America Act of 2025",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-05-01",
        "text": "Referred to the Subcommittee on Coast Guard and Maritime Transportation."
      },
      "number": "3151",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "SHIPS for America Act of 2025",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-05-21T13:57:39Z"
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
      "date": "2025-03-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2429ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Transportation to develop and implement a comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-06T04:33:53Z"
    },
    {
      "title": "To direct the Secretary of Transportation to develop and implement a comprehensive Campus Modernization Plan for the United States Merchant Marine Academy, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:58Z"
    }
  ]
}
```
