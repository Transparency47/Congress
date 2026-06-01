# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5661?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5661
- Title: Water Preservation and Affordability Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5661
- Origin chamber: House
- Introduced date: 2025-09-30
- Update date: 2026-04-28T08:06:36Z
- Update date including text: 2026-04-28T08:06:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-30: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-09-30: Introduced in House

## Actions

- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Introduced in House
- 2025-09-30 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-12-01 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-30",
    "latestAction": {
      "actionDate": "2025-09-30",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5661",
    "number": "5661",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "S001223",
        "district": "13",
        "firstName": "Emilia",
        "fullName": "Rep. Sykes, Emilia Strong [D-OH-13]",
        "lastName": "Sykes",
        "party": "D",
        "state": "OH"
      }
    ],
    "title": "Water Preservation and Affordability Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-28T08:06:36Z",
    "updateDateIncludingText": "2026-04-28T08:06:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-01",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-30",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-30",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-30",
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
          "date": "2025-09-30T16:01:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-12-01T19:42:06Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "PA"
    },
    {
      "bioguideId": "C001072",
      "district": "7",
      "firstName": "Andr\u00e9",
      "fullName": "Rep. Carson, Andr\u00e9 [D-IN-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Carson",
      "party": "D",
      "sponsorshipDate": "2025-10-17",
      "state": "IN"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "DC"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-31",
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
      "sponsorshipDate": "2026-04-16",
      "state": "PA"
    },
    {
      "bioguideId": "B001285",
      "district": "26",
      "firstName": "Julia",
      "fullName": "Rep. Brownley, Julia [D-CA-26]",
      "isOriginalCosponsor": "False",
      "lastName": "Brownley",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5661ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5661\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 30, 2025 Mrs. Sykes (for herself and Mr. Bresnahan ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act to consider the use of resource preservation techniques in certain programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Water Preservation and Affordability Act of 2025 .\n#### 2. Resource preservation techniques\n##### (a) Definition of resource preservation technique\nSection 502 of the Federal Water Pollution Control Act ( 33 U.S.C. 1362 ) is amended by adding at the end the following:\n(28) Resource preservation technique The term resource preservation technique means any process, material, technique, or technology that\u2014 (A) addresses water efficiency, including water reuse, recapture, and conservation; (B) addresses energy efficiency; (C) mitigates stormwater runoff; (D) encourages sustainable project planning, design, and construction; or (E) is environmentally innovative. .\n##### (b) Capitalization grant agreement\nSection 602(b)(13)(B) of the Federal Water Pollution Control Act ( 33 U.S.C. 1382(b)(13)(B) ) is amended by striking the potential for efficient water use, reuse, recapture, and conservation, and energy conservation and inserting the use of resource preservation techniques .\n##### (c) Water pollution control revolving loan funds\nSection 603 of the Federal Water Pollution Control Act ( 33 U.S.C. 1383 ) is amended\u2014\n**(1)**\nin subsection (d)(1), by striking subparagraph (E) and inserting the following:\n(E) for a treatment works proposed for repair, replacement, or expansion, and eligible for assistance under subsection (c)(1), the recipient of a loan shall evaluate, and will use, to the maximum extent practicable, resource preservation techniques for purposes of carrying out the repair, replacement, or expansion; ; and\n**(2)**\nin subsection (i)(1), by striking subparagraph (B) and inserting the following:\n(B) to use resource preservation techniques. .\n##### (d) Wastewater efficiency grant pilot program\nSection 222(e) of the Federal Water Pollution Control Act ( 33 U.S.C. 1302(e) ) is amended by striking paragraph (1) and inserting the following:\n(1) In general There is authorized to be appropriated to carry out this section $40,000,000 for each of fiscal years 2026 through 2031, to remain available until expended. .\n##### (e) Clean water infrastructure resiliency and sustainability program\nSection 223(g)(1) of the Federal Water Pollution Control Act ( 33 U.S.C. 1302a(g)(1) ) by striking $25,000,000 for each of fiscal years 2022 through 2026 and inserting $50,000,000 for each of fiscal years 2026 through 3031 .",
      "versionDate": "2025-09-30",
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-09T15:51:10Z"
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
      "date": "2025-09-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5661ih.xml"
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
      "title": "Water Preservation and Affordability Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-18T03:23:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Water Preservation and Affordability Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-18T03:23:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act to consider the use of resource preservation techniques in certain programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-18T03:18:20Z"
    }
  ]
}
```
