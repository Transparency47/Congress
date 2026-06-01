# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hres/259?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hres/259
- Title: Of inquiry requesting the President to provide certain documents in the President's possession to the House of Representatives relating to the access provided to the staff and advisers of, including any individual working for or in conjunction with, the Department of Government Efficiency to the systems, applications, and accounts, and any information contained therein, of the Bureau of Consumer Financial Protection.
- Congress: 119
- Bill type: HRES
- Bill number: 259
- Origin chamber: House
- Introduced date: 2025-03-27
- Update date: 2025-06-03T14:38:51Z
- Update date including text: 2025-06-03T14:38:51Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-03-27: Introduced in House
- 2025-03-27 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-04-02 - Committee: Committee Consideration and Mark-up Session Held
- Latest action: 2025-03-27: Submitted in House

## Actions

- 2025-03-27 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-03-27 - IntroReferral: Submitted in House
- 2025-04-02 - Committee: Committee Consideration and Mark-up Session Held

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
      "text": "Submitted in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hres/259",
    "number": "259",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "W000187",
        "district": "43",
        "firstName": "Maxine",
        "fullName": "Rep. Waters, Maxine [D-CA-43]",
        "lastName": "Waters",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Of inquiry requesting the President to provide certain documents in the President's possession to the House of Representatives relating to the access provided to the staff and advisers of, including any individual working for or in conjunction with, the Department of Government Efficiency to the systems, applications, and accounts, and any information contained therein, of the Bureau of Consumer Financial Protection.",
    "type": "HRES",
    "updateDate": "2025-06-03T14:38:51Z",
    "updateDateIncludingText": "2025-06-03T14:38:51Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-02",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2025-03-27",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Submitted in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1025",
      "actionDate": "2025-03-27",
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
        "item": [
          {
            "date": "2025-04-02T15:12:00Z",
            "name": "Markup By"
          },
          {
            "date": "2025-03-27T13:10:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "V000081",
      "district": "7",
      "firstName": "Nydia",
      "fullName": "Rep. Vel\u00e1zquez, Nydia M. [D-NY-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Vel\u00e1zquez",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
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
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "S001157",
      "district": "13",
      "firstName": "David",
      "fullName": "Rep. Scott, David [D-GA-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "GA"
    },
    {
      "bioguideId": "L000562",
      "district": "8",
      "firstName": "Stephen",
      "fullName": "Rep. Lynch, Stephen F. [D-MA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Lynch",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "G000553",
      "district": "9",
      "firstName": "Al",
      "fullName": "Rep. Green, Al [D-TX-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Green",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001061",
      "district": "5",
      "firstName": "Emanuel",
      "fullName": "Rep. Cleaver, Emanuel [D-MO-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Cleaver",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MO"
    },
    {
      "bioguideId": "F000454",
      "district": "11",
      "firstName": "Bill",
      "fullName": "Rep. Foster, Bill [D-IL-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Foster",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "B001281",
      "district": "3",
      "firstName": "Joyce",
      "fullName": "Rep. Beatty, Joyce [D-OH-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Beatty",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OH"
    },
    {
      "bioguideId": "V000130",
      "district": "52",
      "firstName": "Juan",
      "fullName": "Rep. Vargas, Juan [D-CA-52]",
      "isOriginalCosponsor": "True",
      "lastName": "Vargas",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CA"
    },
    {
      "bioguideId": "G000581",
      "district": "34",
      "firstName": "Vicente",
      "fullName": "Rep. Gonzalez, Vicente [D-TX-34]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzalez",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "C001117",
      "district": "6",
      "firstName": "Sean",
      "fullName": "Rep. Casten, Sean [D-IL-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Casten",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "IL"
    },
    {
      "bioguideId": "P000617",
      "district": "7",
      "firstName": "Ayanna",
      "fullName": "Rep. Pressley, Ayanna [D-MA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pressley",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MA"
    },
    {
      "bioguideId": "T000481",
      "district": "12",
      "firstName": "Rashida",
      "fullName": "Rep. Tlaib, Rashida [D-MI-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Tlaib",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "MI"
    },
    {
      "bioguideId": "T000486",
      "district": "15",
      "firstName": "Ritchie",
      "fullName": "Rep. Torres, Ritchie [D-NY-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Torres",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "NY"
    },
    {
      "bioguideId": "G000587",
      "district": "29",
      "firstName": "Sylvia",
      "fullName": "Rep. Garcia, Sylvia R. [D-TX-29]",
      "isOriginalCosponsor": "True",
      "lastName": "Garcia",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "TX"
    },
    {
      "bioguideId": "W000788",
      "district": "5",
      "firstName": "Nikema",
      "fullName": "Rep. Williams, Nikema [D-GA-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Williams",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "GA"
    },
    {
      "bioguideId": "P000620",
      "district": "7",
      "firstName": "Brittany",
      "fullName": "Rep. Pettersen, Brittany [D-CO-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Pettersen",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "CO"
    },
    {
      "bioguideId": "F000110",
      "district": "6",
      "firstName": "CLEO",
      "fullName": "Rep. Fields, Cleo [D-LA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "FIELDS",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "LA"
    },
    {
      "bioguideId": "B001326",
      "district": "5",
      "firstName": "Janelle",
      "fullName": "Rep. Bynum, Janelle [D-OR-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Bynum",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "L000607",
      "district": "16",
      "firstName": "Sam",
      "fullName": "Rep. Liccardo, Sam [D-CA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Liccardo",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-03-27",
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
      "sponsorshipDate": "2025-04-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres259ih.xml",
      "text": "IV\n119th CONGRESS\n1st Session\nH. RES. 259\nIN THE HOUSE OF REPRESENTATIVES\nMarch 27, 2025 Ms. Waters (for herself, Ms. Vel\u00e1zquez , Mr. Sherman , Mr. Meeks , Mr. David Scott of Georgia , Mr. Lynch , Mr. Green of Texas , Mr. Cleaver , Mr. Foster , Mrs. Beatty , Mr. Vargas , Mr. Vicente Gonzalez of Texas , Mr. Casten , Ms. Pressley , Ms. Tlaib , Mr. Torres of New York , Ms. Garcia of Texas , Ms. Williams of Georgia , Ms. Pettersen , Mr. Fields , Ms. Bynum , and Mr. Liccardo ) submitted the following resolution; which was referred to the Committee on Financial Services\nRESOLUTION\nOf inquiry requesting the President to provide certain documents in the President\u2019s possession to the House of Representatives relating to the access provided to the staff and advisers of, including any individual working for or in conjunction with, the Department of Government Efficiency to the systems, applications, and accounts, and any information contained therein, of the Bureau of Consumer Financial Protection.\nThat the President is requested to furnish to the House of Representatives, not later than 14 days after the adoption of this resolution, copies of any document, record, memo, correspondence, or other communication in the possession of the President relating to the following:\n**(1)**\nExcluding any individual employed by the U.S. Government prior to January 20, 2025, the name, age, and all professional and background experience of every individual that is working for, or in conjunction with, the Department on Government Efficiency ( DOGE ), including Elon Musk, Jeremy Lewin, Jordan Wick, Gavin Kliger, Nikhil Rajpal, Luke Farritor, Chris Young, and Edward Coristine, that have been provided access to any system, application, or account of the Bureau of Consumer Financial Protection, including public facing and internal websites and social media accounts, physical access control systems, and permissioning systems, or any information contained therein.\n**(2)**\nWith respect to each individual described in paragraph (1)\u2014\n**(A)**\nwhich of the systems, applications, accounts, physical access control systems, permissioning systems, or information therein described in paragraph (1) contained any confidential supervisory information, personally identifiable information, or sensitive compartmented information and, if so, what information was contained;\n**(B)**\nthe level of clearance, access, authorization, or any type of permission required to gain access to each of the systems, applications, accounts, physical access control systems, permissioning systems, or information contained therein;\n**(C)**\nthe level of clearance, access, authorization, or any type of permission held by the individual; and\n**(D)**\nwhether any of the access that the individual obtained or plans to obtain required or will require a level of clearance, access, authorization, or any type of permission that the individual did not have or will not have at the time that individual gained or will gain access.\n**(3)**\nAny information contained in systems, applications, accounts, physical access control systems, permissioning systems, or information therein described in paragraph (1) (including confidential supervisory information, personally identifiable information, or sensitive compartmented information) to which an individual described in paragraph (1) has been provided access that is not available to the public under section 552 of title 5, United States Code, that has\u2014\n**(A)**\nbeen put into external systems, tools, or locations, or otherwise shared with any other person by any individual described in paragraph (1);\n**(B)**\nbeen copied or placed in the possession of any individual described in paragraph (1); or\n**(C)**\nbeen modified by any individual described in paragraph (1).\n**(4)**\nWith respect to the accesses described in paragraph (1)\u2014\n**(A)**\na list of all required steps to provide individuals described in paragraph (1) with this type of access (statutorily mandated or otherwise); and\n**(B)**\na list of all steps actually taken to provide individuals described in paragraph (1) with such accesses, the timeline of when such steps were completed, the identity of each individual who reviewed and approved the completion of the required steps by each individual, and the level of clearance, access, authorization or any type of permission that was granted for each individual.\n**(5)**\nWith respect to each individuals described in paragraph (1) provided with an access described in paragraph (1)\u2014\n**(A)**\nthe signed Rules of Behavior for Privileged Users Form;\n**(B)**\nthe Privileged User Access Request Form, along with the required business justification, supervisor approval, system owner approval, and Information System Security Manager approval; and\n**(C)**\na list of trainings completed, including all Privileged User Trainings.\n**(6)**\nA list of identified and potential conflicts of interest implicated by individuals described in paragraph (1), steps taken to mitigate such conflicts of interest, and the name of the individual who reviewed and approved the status of each individual with respect to such conflicts of interest.\n**(7)**\nThe total number of full-time equivalent employees of the Bureau of Consumer Financial Protection as of December 31, 2024, with a breakdown of the number of such full-time equivalent employees by division and office.\n**(8)**\nThe total number of full-time equivalent employees of the Bureau of Consumer Financial Protection as of March 24, 2025, with a breakdown of the number of such full-time equivalent employees by division and office.\n**(9)**\nThe total number of full-time equivalent employees of the Bureau of Consumer Financial Protection that were not actively working as of March 24, 2025, due to a stop-work order or being placed on administrative leave, with a breakdown of the number of such full-time equivalent employees by division and office.",
      "versionDate": "2025-03-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Computers and information technology",
            "updateDate": "2025-06-03T14:38:40Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T14:38:12Z"
          },
          {
            "name": "Congressional-executive branch relations",
            "updateDate": "2025-06-03T14:38:02Z"
          },
          {
            "name": "Consumer Financial Protection Bureau",
            "updateDate": "2025-06-03T14:38:33Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-03T14:38:22Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-03T14:38:07Z"
          },
          {
            "name": "House of Representatives",
            "updateDate": "2025-06-03T14:38:51Z"
          },
          {
            "name": "Intelligence activities, surveillance, classified information",
            "updateDate": "2025-06-03T14:38:45Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-06-03T14:38:27Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-20T18:12:51Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hres/BILLS-119hres259ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Of inquiry requesting the President to provide certain documents in the President's possession to the House of Representatives relating to the access provided to the staff and advisers of, including any individual working for or in conjunction with, the Department of Government Efficiency to the systems, applications, and accounts, and any information contained therein, of the Bureau of Consumer Financial Protection.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-28T08:18:24Z"
    },
    {
      "title": "Of inquiry requesting the President to provide certain documents in the President's possession to the House of Representatives relating to the access provided to the staff and advisers of, including any individual working for or in conjunction with, the Department of Government Efficiency to the systems, applications, and accounts, and any information contained therein, of the Bureau of Consumer Financial Protection.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-28T08:07:12Z"
    }
  ]
}
```
