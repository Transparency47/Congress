# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5676?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5676
- Title: Stop Stealing Our Jobs Act
- Congress: 119
- Bill type: HR
- Bill number: 5676
- Origin chamber: House
- Introduced date: 2025-10-03
- Update date: 2025-11-01T08:05:55Z
- Update date including text: 2025-11-01T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-03: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-10-03: Introduced in House

## Actions

- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Introduced in House
- 2025-10-03 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-03",
    "latestAction": {
      "actionDate": "2025-10-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5676",
    "number": "5676",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "C001127",
        "district": "20",
        "firstName": "Sheila",
        "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
        "lastName": "Cherfilus-McCormick",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Stop Stealing Our Jobs Act",
    "type": "HR",
    "updateDate": "2025-11-01T08:05:55Z",
    "updateDateIncludingText": "2025-11-01T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-03",
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
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-03",
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
          "date": "2025-10-03T19:31:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "B001300",
      "district": "44",
      "firstName": "Nanette",
      "fullName": "Rep. Barrag\u00e1n, Nanette Diaz [D-CA-44]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrag\u00e1n",
      "middleName": "Diaz",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "J000309",
      "district": "1",
      "firstName": "Jonathan",
      "fullName": "Rep. Jackson, Jonathan L. [D-IL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Jackson",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "IL"
    },
    {
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "OH"
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
      "sponsorshipDate": "2025-10-03",
      "state": "DC"
    },
    {
      "bioguideId": "S000344",
      "district": "32",
      "firstName": "Brad",
      "fullName": "Rep. Sherman, Brad [D-CA-32]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherman",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "CA"
    },
    {
      "bioguideId": "T000488",
      "district": "13",
      "firstName": "Shri",
      "fullName": "Rep. Thanedar, Shri [D-MI-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Thanedar",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MI"
    },
    {
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "NV"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "MO"
    },
    {
      "bioguideId": "L000582",
      "district": "36",
      "firstName": "Ted",
      "fullName": "Rep. Lieu, Ted [D-CA-36]",
      "isOriginalCosponsor": "False",
      "lastName": "Lieu",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "S001200",
      "district": "9",
      "firstName": "Darren",
      "fullName": "Rep. Soto, Darren [D-FL-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Soto",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "FL"
    },
    {
      "bioguideId": "T000193",
      "district": "2",
      "firstName": "Bennie",
      "fullName": "Rep. Thompson, Bennie G. [D-MS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Thompson",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MS"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NJ"
    },
    {
      "bioguideId": "K000402",
      "district": "26",
      "firstName": "Timothy",
      "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Kennedy",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-10-10",
      "state": "NY"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-21",
      "state": "CA"
    },
    {
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "IL"
    },
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5676ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5676\nIN THE HOUSE OF REPRESENTATIVES\nOctober 3, 2025 Mrs. Cherfilus-McCormick (for herself, Ms. Barrag\u00e1n , Mr. Jackson of Illinois , Mr. Landsman , Ms. Norton , Mr. Sherman , Mr. Thanedar , Ms. Titus , and Mr. Bell ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit any Executive agency from terminating employees during any period in which there is a lapse in appropriations, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Stop Stealing Our Jobs Act .\n#### 2. Limit on termination of employees during Government shutdowns\n##### (a) In general\nDuring any period in which there is a lapse in discretionary appropriations, neither the President nor the head of an Executive agency may remove from the civil service, including as part of a reduction in force, any employee of an Executive agency, other than a political appointee.\n##### (b) Definitions\nIn this section:\n**(1) Civil service; Executive agency**\nThe terms civil service and Executive agency have the meanings given such terms in sections 2101 and 105, respectively, of title 5, United States Code.\n**(2) Political appointee**\nThe term political appointee means an individual serving in an appointment to a political position.\n**(3) Political position**\nThe term political position means\u2014\n**(A)**\na position described under sections 5312 through 5316 of title 5, United States Code (relating to the Executive Schedule);\n**(B)**\na noncareer appointment in the Senior Executive Service (as defined in section 3132(a) of title 5, United States Code); or\n**(C)**\na position in the executive branch of the Government of a confidential or policy-determining character under schedule C of subpart C of part 213 of title 5, Code of Federal Regulations.",
      "versionDate": "2025-10-03",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-10-17T13:04:20Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-03",
    "originChamber": "House",
    "payload": {
      "dublinCore": {
        "contributor": "Congressional Research Service, Library of Congress",
        "description": "This file contains bill summaries for federal legislation. A bill summary describes the most significant provisions of a piece of legislation and details the effects the legislative text may have on current law and federal programs. Bill summaries are authored by the Congressional Research Service (CRS) of the Library of Congress. As stated in Public Law 91-510 (2 USC 166 (d)(6)), one of the duties of CRS is \"to prepare summaries and digests of bills and resolutions of a public general nature introduced in the Senate or House of Representatives\". For more information, refer to the User Guide that accompanies this file.",
        "format": "text/xml",
        "language": "EN",
        "rights": "Pursuant to Title 17 Section 105 of the United States Code, this file is not subject to copyright protection and is in the public domain."
      },
      "item": {
        "@attributes": {
          "congress": "119",
          "measure-id": "id119hr5676",
          "measure-number": "5676",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-03",
          "originChamber": "HOUSE",
          "update-date": "2025-10-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5676v00",
            "update-date": "2025-10-17"
          },
          "action-date": "2025-10-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Stop Stealing Our Jobs Act</strong></p><p>This bill prohibits the President or the head of an executive agency from removing a federal employee from the civil service (e.g., as part of a reduction in force) during a lapse in discretionary appropriations (i.e., government shutdown) unless the employee is a political appointee.\u00a0</p>"
        },
        "title": "Stop Stealing Our Jobs Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5676.xml",
    "summary": {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Stealing Our Jobs Act</strong></p><p>This bill prohibits the President or the head of an executive agency from removing a federal employee from the civil service (e.g., as part of a reduction in force) during a lapse in discretionary appropriations (i.e., government shutdown) unless the employee is a political appointee.\u00a0</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5676"
    },
    "title": "Stop Stealing Our Jobs Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Stop Stealing Our Jobs Act</strong></p><p>This bill prohibits the President or the head of an executive agency from removing a federal employee from the civil service (e.g., as part of a reduction in force) during a lapse in discretionary appropriations (i.e., government shutdown) unless the employee is a political appointee.\u00a0</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5676"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5676ih.xml"
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
      "title": "Stop Stealing Our Jobs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T05:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Stop Stealing Our Jobs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T05:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit any Executive agency from terminating employees during any period in which there is a lapse in appropriations, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T05:48:30Z"
    }
  ]
}
```
