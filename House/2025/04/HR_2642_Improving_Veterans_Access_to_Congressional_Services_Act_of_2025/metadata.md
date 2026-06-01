# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2642?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2642
- Title: Improving Veterans Access to Congressional Services Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2642
- Origin chamber: House
- Introduced date: 2025-04-03
- Update date: 2026-04-14T08:05:29Z
- Update date including text: 2026-04-14T08:05:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-04-03: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-09 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-04-03: Introduced in House

## Actions

- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Introduced in House
- 2025-04-03 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-09 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-03",
    "latestAction": {
      "actionDate": "2025-04-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2642",
    "number": "2642",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "M001199",
        "district": "21",
        "firstName": "Brian",
        "fullName": "Rep. Mast, Brian J. [R-FL-21]",
        "lastName": "Mast",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Improving Veterans Access to Congressional Services Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-14T08:05:29Z",
    "updateDateIncludingText": "2026-04-14T08:05:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-09",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-03",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-03",
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
          "date": "2025-04-03T15:03:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-05-09T15:35:28Z",
              "name": "Referred to"
            }
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "systemCode": "hsvr00",
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
      "bioguideId": "B001307",
      "district": "4",
      "firstName": "James",
      "fullName": "Rep. Baird, James R. [R-IN-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Baird",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IN"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "S000168",
      "district": "27",
      "firstName": "Maria",
      "fullName": "Rep. Salazar, Maria Elvira [R-FL-27]",
      "isOriginalCosponsor": "True",
      "lastName": "Salazar",
      "middleName": "Elvira",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "FL"
    },
    {
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "MN"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "IA"
    },
    {
      "bioguideId": "F000474",
      "district": "1",
      "firstName": "Mike",
      "fullName": "Rep. Flood, Mike [R-NE-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Flood",
      "party": "R",
      "sponsorshipDate": "2025-04-03",
      "state": "NE"
    },
    {
      "bioguideId": "P000613",
      "district": "19",
      "firstName": "Jimmy",
      "fullName": "Rep. Panetta, Jimmy [D-CA-19]",
      "isOriginalCosponsor": "True",
      "lastName": "Panetta",
      "party": "D",
      "sponsorshipDate": "2025-04-03",
      "state": "CA"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-04-21",
      "state": "AZ"
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
      "sponsorshipDate": "2025-09-15",
      "state": "VA"
    },
    {
      "bioguideId": "J000295",
      "district": "14",
      "firstName": "David",
      "fullName": "Rep. Joyce, David P. [R-OH-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2642ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2642\nIN THE HOUSE OF REPRESENTATIVES\nApril 3, 2025 Mr. Mast (for himself, Mr. Baird , Mrs. Cherfilus-McCormick , Ms. Salazar , Mr. Finstad , Mrs. Miller-Meeks , Mr. Flood , and Mr. Panetta ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo direct the Secretary of Veterans Affairs to permit Members of Congress to use facilities of the Department of Veterans Affairs for the purposes of meeting with constituents, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Improving Veterans Access to Congressional Services Act of 2025 .\n#### 2. Use of facilities of the Department of Veterans Affairs by Members of Congress\n##### (a) In general\nUpon request of a Member of Congress and subject to regulations prescribed under subsection (b), the Secretary of Veterans Affairs shall permit the Member to use a facility of the Department of Veterans Affairs for the purposes of meeting with constituents of the Member. The Secretary and the Administrator of General Services shall jointly identify available spaces in facilities of the Department for such purposes.\n##### (b) Regulations\nNot later than 90 days after the date of enactment of this Act, the Secretary of Veterans Affairs shall prescribe regulations regarding such use of a facility of the Department of Veterans Affairs by Members of Congress. Regulations prescribed under this subsection\u2014\n**(1)**\nshall require that a space within a facility of the Department provided to a Member under subsection (a) is\u2014\n**(A)**\navailable during normal business hours;\n**(B)**\nlocated in an area that is visible and accessible to constituents of the Member; and\n**(C)**\nsubject to a rate of rent (payable from the Member\u2019s Representational Allowance or the Senator\u2019s Official Personnel and Office Expense Account, as the case may be) that is similar to the rate charged by the Administrator of General Services for office space in the area of the facility;\n**(2)**\nmay not prohibit a Member from advertising the use by the Member of a space within a facility of the Department under subsection (a);\n**(3)**\nshall comply with sections 7321 through 7326 of title 5, United States Code (commonly referred to as the Hatch Act ) and section 1.218(a)(14) of title 38, Code of Federal Regulations (or successor regulation), by prohibiting activities including\u2014\n**(A)**\ncampaigning in support of or opposition to any political office;\n**(B)**\nstatements or actions that solicit, support, or oppose any change to Federal law or policy;\n**(C)**\nany activity that interferes with security or normal operation of the facility;\n**(D)**\nphotographing or recording a veteran patient at such facility;\n**(E)**\nphotographing or recording a patient, visitor to the facility, or employee of the Department without the consent of such individual; and\n**(F)**\nphotography or recording for the purpose of political campaign materials;\n**(4)**\nmay not permit a Member of Congress to use such a facility during the 60-day period preceding an election for Federal office in the jurisdiction in which such facility is located; and\n**(5)**\nmay not unreasonably restrict use of a facility of the Department by a Member under subsection (a) if\u2014\n**(A)**\nthere is space in such facility not in regular use by personnel of the Department; and\n**(B)**\nuse of such space shall not impede operations of the Department in such facility.",
      "versionDate": "2025-04-03",
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
        "actionDate": "2025-11-19",
        "text": "Read twice and referred to the Committee on Veterans' Affairs."
      },
      "number": "3205",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Improving Veterans Access to Congressional Services Act of 2025",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:15:52Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-04-03",
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
          "measure-id": "id119hr2642",
          "measure-number": "2642",
          "measure-type": "hr",
          "orig-publish-date": "2025-04-03",
          "originChamber": "HOUSE",
          "update-date": "2025-07-01"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2642v00",
            "update-date": "2025-07-01"
          },
          "action-date": "2025-04-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Improving Veterans Access to Congressional Services Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to permit a Member of Congress (upon request) to use a VA facility to meet with constituents. The VA and the General Services Administration must jointly identify available spaces in VA facilities for such purposes.</p><p>The VA must prescribe regulations regarding such use of a VA facility by a Member of Congress.</p>"
        },
        "title": "Improving Veterans Access to Congressional Services Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2642.xml",
    "summary": {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Veterans Access to Congressional Services Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to permit a Member of Congress (upon request) to use a VA facility to meet with constituents. The VA and the General Services Administration must jointly identify available spaces in VA facilities for such purposes.</p><p>The VA must prescribe regulations regarding such use of a VA facility by a Member of Congress.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr2642"
    },
    "title": "Improving Veterans Access to Congressional Services Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-04-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Improving Veterans Access to Congressional Services Act of 2025</strong></p><p>This bill requires the Department of Veterans Affairs (VA) to permit a Member of Congress (upon request) to use a VA facility to meet with constituents. The VA and the General Services Administration must jointly identify available spaces in VA facilities for such purposes.</p><p>The VA must prescribe regulations regarding such use of a VA facility by a Member of Congress.</p>",
      "updateDate": "2025-07-01",
      "versionCode": "id119hr2642"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-04-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2642ih.xml"
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
      "title": "Improving Veterans Access to Congressional Services Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-12T02:53:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Improving Veterans Access to Congressional Services Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-12T02:53:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To direct the Secretary of Veterans Affairs to permit Members of Congress to use facilities of the Department of Veterans Affairs for the purposes of meeting with constituents, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-12T02:48:19Z"
    }
  ]
}
```
