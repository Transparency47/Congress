# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3663?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3663
- Title: Bridge Protection Act
- Congress: 119
- Bill type: HR
- Bill number: 3663
- Origin chamber: House
- Introduced date: 2025-05-29
- Update date: 2025-10-29T08:05:48Z
- Update date including text: 2025-10-29T08:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-29: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.
- Latest action: 2025-05-29: Introduced in House

## Actions

- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Introduced in House
- 2025-05-29 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-05-30 - Committee: Referred to the Subcommittee on Highways and Transit.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-29",
    "latestAction": {
      "actionDate": "2025-05-29",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3663",
    "number": "3663",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "V000133",
        "district": "2",
        "firstName": "Jefferson",
        "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
        "lastName": "Van Drew",
        "party": "R",
        "state": "NJ"
      }
    ],
    "title": "Bridge Protection Act",
    "type": "HR",
    "updateDate": "2025-10-29T08:05:48Z",
    "updateDateIncludingText": "2025-10-29T08:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-30",
      "committees": {
        "item": {
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Highways and Transit.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-29",
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
      "actionDate": "2025-05-29",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-29",
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
          "date": "2025-05-29T15:06:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-30T19:47:44Z",
              "name": "Referred to"
            }
          },
          "name": "Highways and Transit Subcommittee",
          "systemCode": "hspw12"
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
      "bioguideId": "T000468",
      "district": "1",
      "firstName": "Dina",
      "fullName": "Rep. Titus, Dina [D-NV-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Titus",
      "party": "D",
      "sponsorshipDate": "2025-05-29",
      "state": "NV"
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
      "sponsorshipDate": "2025-10-28",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3663ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3663\nIN THE HOUSE OF REPRESENTATIVES\nMay 29, 2025 Mr. Van Drew (for himself and Ms. Titus ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend title 23, United States Code, to establish requirements for owners of certain bridges, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Bridge Protection Act .\n#### 2. Additional requirements for bridge projects\n##### (a) In general\nChapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Requirements for certain bridges (a) In general As a condition for receiving funds under this title, the Secretary of Transportation shall require any owner of a covered bridge to conduct vessel collision vulnerability assessments using the American Association of State Highway and Transportation Officials Method II and submit the results of such assessment to the Secretary. (b) Results (1) In general If a covered bridge assessed under subsection (a) exceeds the American Association of State Highway and Transportation Officials risk threshold for such bridge, the owner shall develop and implement a risk reduction plan not later than 1 year after the completion of the assessment under subsection (a). (2) Ineligibility for future grants Beginning on October 1, 2026, if an owner of a bridge required to develop a risk reduction plan under paragraph (1) fails to develop and implement such plan, the owner shall be ineligible for any Federal grant relating to such bridge, unless such owner receives an extension to implement such plan from the Secretary of Transportation. (c) Integration of data (1) In general Not later than 1 year after the completion of an assessment under subsection (a), the Secretary of Transportation shall integrate the results of such assessment into the National Bridge Inventory of the Department of Transportation. (2) Protection of sensitive data In integrating results under paragraph (1), the Secretary may withhold any sensitive secure data that the Secretary determines appropriate to preserve the security of the bridges involved in such assessments. (d) Covered bridge defined In this section, the term covered bridge means a bridge over navigable water that was built before 1996. 181. Interdisciplinary Bridge Safety team (a) In general The Secretary of Transportation shall establish an interdisciplinary bridge safety team within the Department of Transportation to provide guidance, oversee compliance, and maintain a national vulnerability database for bridges. (b) Membership The team established under subsection (a) shall be comprised of detailees from the Federal Highway Administration, the Coast Guard, and the Corps of Engineers. 182. Bridge vulnerability grant program (a) In general The Secretary of Transportation shall establish a program to provide grants on a competitive basis for assessments and physical improvements for covered bridges. (b) Applications To be eligible to receive a grant under this section, an owner of a covered bridge shall submit to the Secretary an application in such form, in such manner, and containing such information as the Secretary may require. (c) Use of funds A recipient of a grant under this section may use the grant provided to carry out assessments or make physical improvements to a covered bridge. (d) Authorization of appropriations There are authorized to be appropriated to carry out the program under this section, $500,000,000 for fiscal years 2026 through 2030. (e) Covered bridge defined In this section, the term covered bridge means a bridge over navigable water that was built before 1996. .\n##### (b) Clerical amendment\nThe analysis for chapter 1 of title 23, United States Code, is amended by adding at the end the following:\n180. Requirements for certain bridges. 181. Interagency Bridge Safety Office. 182. Bridge vulnerability grant program. .",
      "versionDate": "2025-05-29",
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
        "name": "Transportation and Public Works",
        "updateDate": "2025-06-16T13:06:04Z"
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
      "date": "2025-05-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3663ih.xml"
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
      "title": "Bridge Protection Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-04T03:23:28Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Bridge Protection Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-04T03:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 23, United States Code, to establish requirements for owners of certain bridges, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-04T03:18:39Z"
    }
  ]
}
```
