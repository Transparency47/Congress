# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1337?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1337
- Title: To add Ireland to the E3 nonimmigrant visa program.
- Congress: 119
- Bill type: HR
- Bill number: 1337
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2026-03-04T02:20:18Z
- Update date including text: 2026-03-04T02:20:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1337",
    "number": "1337",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "N000015",
        "district": "1",
        "firstName": "Richard",
        "fullName": "Rep. Neal, Richard E. [D-MA-1]",
        "lastName": "Neal",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "To add Ireland to the E3 nonimmigrant visa program.",
    "type": "HR",
    "updateDate": "2026-03-04T02:20:18Z",
    "updateDateIncludingText": "2026-03-04T02:20:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:06:00Z",
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
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "True",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "PA"
    },
    {
      "bioguideId": "M001225",
      "district": "15",
      "firstName": "Kevin",
      "fullName": "Rep. Mullin, Kevin [D-CA-15]",
      "isOriginalCosponsor": "False",
      "lastName": "Mullin",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "CA"
    },
    {
      "bioguideId": "M000312",
      "district": "2",
      "firstName": "James",
      "fullName": "Rep. McGovern, James P. [D-MA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "McGovern",
      "middleName": "P.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "MA"
    },
    {
      "bioguideId": "B001296",
      "district": "2",
      "firstName": "Brendan",
      "fullName": "Rep. Boyle, Brendan F. [D-PA-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Boyle",
      "middleName": "F.",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
    },
    {
      "bioguideId": "S001205",
      "district": "5",
      "firstName": "Mary",
      "fullName": "Rep. Scanlon, Mary Gay [D-PA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Scanlon",
      "middleName": "Gay",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "PA"
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
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
    },
    {
      "bioguideId": "M001210",
      "district": "3",
      "firstName": "Gregory",
      "fullName": "Rep. Murphy, Gregory F. [R-NC-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Murphy",
      "middleName": "F.",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NC"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2025-03-18",
      "state": "DE"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-03-18",
      "state": "NY"
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
      "sponsorshipDate": "2025-03-18",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1337ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1337\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Neal (for himself and Mr. Kelly of Pennsylvania ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo add Ireland to the E3 nonimmigrant visa program.\n#### 1. E\u20133 visas for Irish nationals\n##### (a) In general\nSection 101(a)(15)(E)(iii) of the Immigration and Nationality Act ( 8 U.S.C. 1101(a)(15)(E)(iii) ) is amended by inserting or, on a basis of reciprocity as determined by the Secretary of State, a national of Ireland, after Australia .\n##### (b) Employer requirements\nSection 212 of the Immigration and Nationality Act ( 8 U.S.C. 1182 ) is amended\u2014\n**(1)**\nby redesignating the second subsection (t) (as added by section 1(b)(2)(B) of Public Law 108\u2013449 (118 Stat. 3470)) as subsection (u); and\n**(2)**\nby adding at the end of subsection (t)(1) (as added by section 402(b)(2) of Public Law 108\u201377 (117 Stat. 941)) the following:\n(E) In the case of an attestation filed with respect to a national of Ireland described in section 101(a)(15)(E)(iii), the employer is, and will remain during the period of authorized employment of such Irish national, a participant in good standing in the E-Verify program described in section 403(a) of the Illegal Immigration Reform and Immigrant Responsibility Act of 1996 ( 8 U.S.C. 1324a note). .\n##### (c) Application allocation\nParagraph (11) of section 214(g) of the Immigration and Nationality Act ( 8 U.S.C. 1184(g)(11) ) is amended to read as follows:\n(11) (A) The Secretary of State may approve initial applications submitted for aliens described in section 101(a)(15)(E)(iii) only as follows: (i) For applicants who are nationals of the Commonwealth of Australia, not more than 10,500 for a fiscal year. (ii) For applicants who are nationals of Ireland, not more than a number equal to the difference between 10,500 and the number of applications approved in the prior fiscal year for aliens who are nationals of the Commonwealth of Australia. (B) The approval of an application described under subparagraph (A)(ii) shall be deemed for numerical control purposes to have occurred on September 30 of the prior fiscal year. (C) The numerical limitation under subparagraph (A) shall only apply to principal aliens and not to the spouses or children of such aliens. .",
      "versionDate": "2025-02-13",
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
        "updateDate": "2025-03-17T14:14:07Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-13",
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
          "measure-id": "id119hr1337",
          "measure-number": "1337",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-13",
          "originChamber": "HOUSE",
          "update-date": "2026-03-04"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1337v00",
            "update-date": "2026-03-04"
          },
          "action-date": "2025-02-13",
          "action-desc": "Introduced in House",
          "summary-text": "<p>This bill expands the E-3 visa program to cover Irish nationals. The E-3 visa is a nonimmigrant visa currently only available to Australian nationals coming to the United States for employment in a specialty occupation. For Irish E-3 initial applications, the Department of State may approve each fiscal year no more than 10,500 minus the number of Australian initial applications approved the previous fiscal year.</p>"
        },
        "title": "To add Ireland to the E3 nonimmigrant visa program."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1337.xml",
    "summary": {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill expands the E-3 visa program to cover Irish nationals. The E-3 visa is a nonimmigrant visa currently only available to Australian nationals coming to the United States for employment in a specialty occupation. For Irish E-3 initial applications, the Department of State may approve each fiscal year no more than 10,500 minus the number of Australian initial applications approved the previous fiscal year.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1337"
    },
    "title": "To add Ireland to the E3 nonimmigrant visa program."
  },
  "summaries": [
    {
      "actionDate": "2025-02-13",
      "actionDesc": "Introduced in House",
      "text": "<p>This bill expands the E-3 visa program to cover Irish nationals. The E-3 visa is a nonimmigrant visa currently only available to Australian nationals coming to the United States for employment in a specialty occupation. For Irish E-3 initial applications, the Department of State may approve each fiscal year no more than 10,500 minus the number of Australian initial applications approved the previous fiscal year.</p>",
      "updateDate": "2026-03-04",
      "versionCode": "id119hr1337"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1337ih.xml"
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
      "title": "To add Ireland to the E3 nonimmigrant visa program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:34:03Z"
    },
    {
      "title": "To add Ireland to the E3 nonimmigrant visa program.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-02-14T09:07:02Z"
    }
  ]
}
```
