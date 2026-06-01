# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2050?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/2050
- Title: Homeland Heroes Pay Act
- Congress: 119
- Bill type: HR
- Bill number: 2050
- Origin chamber: House
- Introduced date: 2025-03-11
- Update date: 2025-06-30T17:55:09Z
- Update date including text: 2025-06-30T17:55:09Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-11: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Appropriations.
- Latest action: 2025-03-11: Introduced in House

## Actions

- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Introduced in House
- 2025-03-11 - IntroReferral: Referred to the House Committee on Appropriations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/2050",
    "number": "2050",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000590",
        "district": "7",
        "firstName": "Mark",
        "fullName": "Rep. Green, Mark E. [R-TN-7]",
        "lastName": "Green",
        "party": "R",
        "state": "TN"
      }
    ],
    "title": "Homeland Heroes Pay Act",
    "type": "HR",
    "updateDate": "2025-06-30T17:55:09Z",
    "updateDateIncludingText": "2025-06-30T17:55:09Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Appropriations Committee",
          "systemCode": "hsap00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Appropriations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T14:05:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Appropriations Committee",
      "systemCode": "hsap00",
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
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "True",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "FL"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "True",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "TX"
    },
    {
      "bioguideId": "C001133",
      "district": "6",
      "firstName": "Juan",
      "fullName": "Rep. Ciscomani, Juan [R-AZ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Ciscomani",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "AZ"
    },
    {
      "bioguideId": "L000597",
      "district": "15",
      "firstName": "Laurel",
      "fullName": "Rep. Lee, Laurel M. [R-FL-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2050ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2050\nIN THE HOUSE OF REPRESENTATIVES\nMarch 11, 2025 Mr. Green of Tennessee (for himself, Mr. Gimenez , Ms. De La Cruz , and Mr. Ciscomani ) introduced the following bill; which was referred to the Committee on Appropriations\nA BILL\nMaking continuing appropriations for the salary and expenses of certain excepted employees of U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Homeland Heroes Pay Act .\n#### 2. Continuing appropriations for certain employees of CBP and ICE\n##### (a) In general\nThere are appropriated, out of any money in the Treasury not otherwise appropriated, such sums as are necessary to pay, during the period of any lapse in discretionary appropriations occurring on or after the date of the enactment of this Act, the salaries and expenses of\u2014\n**(1)**\nU.S. Customs and Border Protection agents and officers who are performing mission critical functions at United States Southwest, Northern, and maritime border ports of entry, and between such ports of entry, including preventing terrorists, terrorists weapons, illegal aliens, illicit drugs, and other illegal contraband; and\n**(2)**\nU.S. Immigration and Customs Enforcement officers and agents who conduct\u2014\n**(A)**\nimmigration enforcement, including detaining and removing aliens (as defined in section 101 of the Immigration and Nationality Act); and\n**(B)**\ninvestigations of criminal operations and organizations, including\u2014\n**(i)**\nthe illegal trade of contraband such as goods, weapons, and drugs; and\n**(ii)**\nthe smuggling and trafficking of people.\n##### (b) Termination\nAppropriations and funds made available and authority granted pursuant to this section shall be available until whichever of the following first occurs:\n**(1)**\nThe enactment into law of an appropriation (including a continuing appropriation) for any purpose for which amounts are made available in subsection (a).\n**(2)**\nThe enactment into law of the applicable regular or continuing appropriations resolution or other Act without any appropriation for such purpose.",
      "versionDate": "2025-03-11",
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
        "name": "Immigration",
        "updateDate": "2025-05-15T14:52:09Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-11",
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
          "measure-id": "id119hr2050",
          "measure-number": "2050",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-11",
          "originChamber": "HOUSE",
          "update-date": "2025-06-30"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2050v00",
            "update-date": "2025-06-30"
          },
          "action-date": "2025-03-11",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Homeland Heroes Pay Act</strong></p><p>This bill provides continuing appropriations for the salaries and expenses of certain U.S. Customs and Border Protection (CBP) and U.S. Immigration and Customs Enforcement (ICE) officers and agents during any lapse in appropriations (i.e., government shutdown).</p><p>If a lapse in appropriations occurs, the bill provides continuing appropriations for the salaries and expenses of (1) CBP officers and agents who are performing mission critical functions at U.S. southwest, northern, and maritime border ports of entry, and between such ports of entry; and (2) ICE officers and agents who conduct immigration enforcement and investigations of criminal operations and organizations.</p>"
        },
        "title": "Homeland Heroes Pay Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2050.xml",
    "summary": {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Homeland Heroes Pay Act</strong></p><p>This bill provides continuing appropriations for the salaries and expenses of certain U.S. Customs and Border Protection (CBP) and U.S. Immigration and Customs Enforcement (ICE) officers and agents during any lapse in appropriations (i.e., government shutdown).</p><p>If a lapse in appropriations occurs, the bill provides continuing appropriations for the salaries and expenses of (1) CBP officers and agents who are performing mission critical functions at U.S. southwest, northern, and maritime border ports of entry, and between such ports of entry; and (2) ICE officers and agents who conduct immigration enforcement and investigations of criminal operations and organizations.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2050"
    },
    "title": "Homeland Heroes Pay Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-11",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Homeland Heroes Pay Act</strong></p><p>This bill provides continuing appropriations for the salaries and expenses of certain U.S. Customs and Border Protection (CBP) and U.S. Immigration and Customs Enforcement (ICE) officers and agents during any lapse in appropriations (i.e., government shutdown).</p><p>If a lapse in appropriations occurs, the bill provides continuing appropriations for the salaries and expenses of (1) CBP officers and agents who are performing mission critical functions at U.S. southwest, northern, and maritime border ports of entry, and between such ports of entry; and (2) ICE officers and agents who conduct immigration enforcement and investigations of criminal operations and organizations.</p>",
      "updateDate": "2025-06-30",
      "versionCode": "id119hr2050"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2050ih.xml"
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
      "title": "Homeland Heroes Pay Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T09:53:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Homeland Heroes Pay Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T09:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making continuing appropriations for the salary and expenses of certain excepted employees of U.S. Customs and Border Protection and U.S. Immigration and Customs Enforcement, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T09:48:27Z"
    }
  ]
}
```
