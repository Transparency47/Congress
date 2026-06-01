# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1601
- Title: Defending Ukraine’s Territorial Integrity Act
- Congress: 119
- Bill type: HR
- Bill number: 1601
- Origin chamber: House
- Introduced date: 2025-02-26
- Update date: 2026-01-12T16:26:13Z
- Update date including text: 2026-01-12T16:26:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-26: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-08 17:15:39 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1601, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.
- Latest action: 2025-02-26: Introduced in House

## Actions

- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Introduced in House
- 2025-02-26 - IntroReferral: Referred to the House Committee on Foreign Affairs.
- 2026-01-08 17:15:39 - Floor: ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1601, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-26",
    "latestAction": {
      "actionDate": "2025-02-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1601",
    "number": "1601",
    "originChamber": "House",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001078",
        "district": "11",
        "firstName": "Gerald",
        "fullName": "Rep. Connolly, Gerald E. [D-VA-11]",
        "lastName": "Connolly",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Defending Ukraine\u2019s Territorial Integrity Act",
    "type": "HR",
    "updateDate": "2026-01-12T16:26:13Z",
    "updateDateIncludingText": "2026-01-12T16:26:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H8D000",
      "actionDate": "2026-01-08",
      "actionTime": "17:15:39",
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "ASSUMING FIRST SPONSORSHIP - Mr. Walkinshaw asked unanimous consent that he may hereafter be considered as the first sponsor of H.R. 1601, a bill originally introduced by Representative Connolly, for the purpose of adding cosponsors and requesting reprintings pursuant to clause 7 of rule XII. Agreed to without objection.",
      "type": "Floor"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-26",
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
      "actionDate": "2025-02-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-26",
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
          "date": "2025-02-26T15:02:50Z",
          "name": "Referred To"
        }
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
      "bioguideId": "W000795",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Wilson, Joe [R-SC-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Wilson",
      "party": "R",
      "sponsorshipDate": "2025-02-26",
      "state": "SC"
    },
    {
      "bioguideId": "D000631",
      "district": "4",
      "firstName": "Madeleine",
      "fullName": "Rep. Dean, Madeleine [D-PA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Dean",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "PA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "DC"
    },
    {
      "bioguideId": "G000599",
      "district": "10",
      "firstName": "Daniel",
      "fullName": "Rep. Goldman, Daniel S. [D-NY-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Goldman",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "NY"
    },
    {
      "bioguideId": "K000009",
      "district": "9",
      "firstName": "Marcy",
      "fullName": "Rep. Kaptur, Marcy [D-OH-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaptur",
      "party": "D",
      "sponsorshipDate": "2025-02-26",
      "state": "OH"
    },
    {
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-03-03",
      "state": "NE"
    },
    {
      "bioguideId": "H000874",
      "district": "5",
      "firstName": "Steny",
      "fullName": "Rep. Hoyer, Steny H. [D-MD-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyer",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-03-03",
      "state": "MD"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "P000608",
      "district": "50",
      "firstName": "Scott",
      "fullName": "Rep. Peters, Scott H. [D-CA-50]",
      "isOriginalCosponsor": "False",
      "lastName": "Peters",
      "middleName": "H.",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
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
      "sponsorshipDate": "2025-04-09",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1601ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1601\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 26, 2025 Mr. Connolly (for himself, Mr. Wilson of South Carolina , Ms. Dean of Pennsylvania , Ms. Norton , Mr. Goldman of New York , and Ms. Kaptur ) introduced the following bill; which was referred to the Committee on Foreign Affairs\nA BILL\nTo counter Russian influence and aggression in Ukraine.\n#### 1. Short title\nThis Act may be cited as the Defending Ukraine\u2019s Territorial Integrity Act .\n#### 2. Countering Russian influence and aggression in Ukraine\n##### (a) Statement of policy\nIt is the policy of the United States not to recognize the Russian Federation\u2019s claim of sovereignty over, or independence, of any part of Ukraine occupied by Russian forces, including Crimea and Donetsk, Kherson, Luhansk, and Zaporizhzhia oblasts.\n##### (b) Prohibition\n**(1) In general**\nNone of the funds authorized to be appropriated or otherwise made available to any Federal department or agency may be used to provide assistance for the central government of a country that the Secretary of State determines and reports to the appropriate congressional committees\u2014\n**(A)**\nhas recognized the independence of, or has established diplomatic relations with, any region located in the territory of Ukraine that is occupied by the Russian Federation or under the control of Russian-backed separatists, including Crimea and Donetsk, Kherson, Luhansk, and Zaporizhzhia oblasts; or\n**(B)**\nhas taken affirmative steps intended to support or be supportive of the Russian Federation annexation of Crimea or other territory in Ukraine.\n**(2) Publication of list of central governments**\nThe Secretary of State shall publish on the Department of State website a list of such central governments in a timely manner.\n**(3) Waiver**\nThe Secretary of State may waive the prohibition on assistance required by paragraph (1) with respect to any such central government if the Secretary determines and reports to the appropriate congressional committees that to do so is in the national interest of the United States, and includes a justification for such interest.\n##### (c) Appropriate congressional committees defined\nIn this section, the term appropriate congressional committees means the Committee on Foreign Affairs of the House of Representatives and the Committee on Foreign Relations of the Senate.",
      "versionDate": "2025-02-26",
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
            "name": "Central Europe",
            "updateDate": "2026-01-12T16:25:09Z"
          },
          {
            "name": "Conflicts and wars",
            "updateDate": "2026-01-12T16:26:13Z"
          },
          {
            "name": "Russia",
            "updateDate": "2026-01-12T16:24:58Z"
          },
          {
            "name": "Ukraine",
            "updateDate": "2026-01-12T16:24:53Z"
          },
          {
            "name": "War crimes, genocide, crimes against humanity",
            "updateDate": "2026-01-12T16:25:28Z"
          }
        ]
      },
      "policyArea": {
        "name": "International Affairs",
        "updateDate": "2025-05-08T16:06:46Z"
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
      "date": "2025-02-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1601ih.xml"
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
      "title": "Defending Ukraine\u2019s Territorial Integrity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:31Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Defending Ukraine\u2019s Territorial Integrity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-17T12:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To counter Russian influence and aggression in Ukraine.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-17T12:48:31Z"
    }
  ]
}
```
