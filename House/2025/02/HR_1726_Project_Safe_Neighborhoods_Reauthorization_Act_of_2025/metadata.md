# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1726?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1726
- Title: Project Safe Neighborhoods Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1726
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-05-13T08:06:10Z
- Update date including text: 2026-05-13T08:06:10Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1726",
    "number": "1726",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "N000191",
        "district": "2",
        "firstName": "Joe",
        "fullName": "Rep. Neguse, Joe [D-CO-2]",
        "lastName": "Neguse",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-13T08:06:10Z",
    "updateDateIncludingText": "2026-05-13T08:06:10Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "hsju00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on the Judiciary.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:12:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Judiciary Committee",
      "systemCode": "hsju00",
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
      "bioguideId": "R000609",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. Rutherford, John H. [R-FL-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Rutherford",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "C001110",
      "district": "46",
      "firstName": "J.",
      "fullName": "Rep. Correa, J. Luis [D-CA-46]",
      "isOriginalCosponsor": "True",
      "lastName": "Correa",
      "middleName": "Luis",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "NE"
    },
    {
      "bioguideId": "M001208",
      "district": "6",
      "firstName": "Lucy",
      "fullName": "Rep. McBath, Lucy [D-GA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "McBath",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "F000478",
      "district": "7",
      "firstName": "Russell",
      "fullName": "Rep. Fry, Russell [R-SC-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Fry",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SC"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "FL"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-02-27",
      "state": "MD"
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
      "sponsorshipDate": "2025-02-27",
      "state": "PA"
    },
    {
      "bioguideId": "K000401",
      "district": "3",
      "firstName": "Kevin",
      "fullName": "Rep. Kiley, Kevin [R-CA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Kiley",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "CA"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001223",
      "district": "2",
      "firstName": "Seth",
      "fullName": "Rep. Magaziner, Seth [D-RI-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Magaziner",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "RI"
    },
    {
      "bioguideId": "G000598",
      "district": "42",
      "firstName": "Robert",
      "fullName": "Rep. Garcia, Robert [D-CA-42]",
      "isOriginalCosponsor": "False",
      "lastName": "Garcia",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "CA"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "NJ"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-05-12",
      "state": "PA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1726ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1726\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Neguse (for himself, Mr. Rutherford , Mr. Correa , Mr. Bacon , Mrs. McBath , Mr. Fry , Ms. Williams of Georgia , Ms. Lee of Florida , Mr. Ivey , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo reauthorize the Project Safe Neighborhoods Grant Program Authorization Act of 2018, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Project Safe Neighborhoods Reauthorization Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nLaunched in 2001, the Project Safe Neighborhoods program is a nationwide initiative that brings together Federal, State, local, and Tribal law enforcement officials, prosecutors, community leaders, and other stakeholders to identify the most pressing crime problems in a community and work collaboratively to address those problems.\n**(2)**\nThe Project Safe Neighborhoods program\u2014\n**(A)**\noperates in all 94 Federal judicial districts throughout the 50 States and territories of the United States; and\n**(B)**\nimplements 4 key components to successfully reduce violent crime in communities, including community engagement, prevention and intervention, focused and strategic enforcement, and accountability.\n#### 3. Reauthorization\n##### (a) Definitions\nSection 2 of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60701 ) is amended\u2014\n**(1)**\nby redesignating paragraphs (1), (2), and (3) as paragraphs (2), (4), and (5), respectively;\n**(2)**\nby inserting before paragraph (2), as so redesignated, the following:\n(1) the term crime analyst means an individual employed by a law enforcement agency for the purpose of separating information into key components and contributing to plans of action to understand, mitigate, and neutralize criminal threats; ; and\n**(3)**\nby inserting after paragraph (2), as so redesignated, the following:\n(3) the term law enforcement assistant means an individual employed by a law enforcement agency or a prosecuting agency for the purpose of aiding law enforcement officers in investigative or administrative duties; .\n##### (b) Use of funds\nSection 4(b) of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60703(b) ) is amended\u2014\n**(1)**\nin paragraph (3), by striking or at the end;\n**(2)**\nin paragraph (4), by striking the period at the end and inserting a semicolon; and\n**(3)**\nby adding at the end the following:\n(5) hiring crime analysts to assist with violent crime reduction efforts; (6) the cost of overtime for law enforcement officers, prosecutors, and law enforcement assistants that assist with the Program; and (7) purchasing, implementing, and using technology to assist with violent crime reduction efforts. .\n##### (c) Authorization of appropriations\nSection 6 of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60705 ) is amended by striking fiscal years 2019 through 2021 and inserting fiscal years 2026 through 2030 .\n#### 4. Task force support\n##### (a) Short title\nThis section may be cited as the Officer Ella Grace French and Sergeant Jim Smith Task Force Support Act of 2025 .\n##### (b) Amendment\nSection 4(b) of the Project Safe Neighborhoods Grant Program Authorization Act of 2018 ( 34 U.S.C. 60703(b) ), as amended by section 3(b), is amended\u2014\n**(1)**\nin paragraph (6), by striking and at the end;\n**(2)**\nin paragraph (7), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(8) support for multi-jurisdictional task forces. .\n#### 5. Transparency\nNot less frequently than annually, the Attorney General shall submit to the Committee on the Judiciary of the Senate and the Committee on the Judiciary of the House of Representatives a report that details, for each area in which the Project Safe Neighborhoods Block Grant Program operates and with respect to the 1-year period preceding the date of the report\u2014\n**(1)**\nhow the area spent funds under the Project Safe Neighborhoods Block Grant Program;\n**(2)**\nthe community outreach efforts performed in the area; and\n**(3)**\nthe number and a description of the violent crime offenses committed in the area, including murder, non-negligent manslaughter, rape, robbery, and aggravated assault.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-04-03",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "1300",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "type": "S"
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
            "name": "Community life and organization",
            "updateDate": "2025-09-02T19:13:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-09-02T19:13:53Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2025-09-02T19:13:53Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-09-02T19:13:53Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-09-02T19:13:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T13:44:06Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1726ih.xml"
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
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-19T15:23:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Project Safe Neighborhoods Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Officer Ella Grace French and Sergeant Jim Smith Task Force Support Act of 2025",
      "titleType": "Short Title(s) as Introduced for portions of this bill",
      "titleTypeCode": "106",
      "updateDate": "2025-03-19T15:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Project Safe Neighborhoods Grant Program Authorization Act of 2018, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-19T15:18:25Z"
    }
  ]
}
```
