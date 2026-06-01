# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1906?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1906
- Title: Rural Wellness Act
- Congress: 119
- Bill type: HR
- Bill number: 1906
- Origin chamber: House
- Introduced date: 2025-03-06
- Update date: 2025-05-09T14:43:35Z
- Update date including text: 2025-05-09T14:43:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-06: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.
- Latest action: 2025-03-06: Introduced in House

## Actions

- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Introduced in House
- 2025-03-06 - IntroReferral: Referred to the House Committee on Agriculture.
- 2025-03-28 - Committee: Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-06",
    "latestAction": {
      "actionDate": "2025-03-06",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1906",
    "number": "1906",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "B001315",
        "district": "13",
        "firstName": "Nikki",
        "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
        "lastName": "Budzinski",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "Rural Wellness Act",
    "type": "HR",
    "updateDate": "2025-05-09T14:43:35Z",
    "updateDateIncludingText": "2025-05-09T14:43:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-28",
      "committees": {
        "item": {
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commodity Markets, Digital Assets, and Rural Development.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-06",
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
          "date": "2025-03-06T14:01:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-28T20:50:32Z",
              "name": "Referred to"
            }
          },
          "name": "Commodity Markets, Digital Assets, and Rural Development Subcommittee",
          "systemCode": "hsag22"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "F000475",
      "district": "1",
      "firstName": "Brad",
      "fullName": "Rep. Finstad, Brad [R-MN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Finstad",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "MN"
    },
    {
      "bioguideId": "D000230",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Davis, Donald G. [D-NC-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "G.",
      "party": "D",
      "sponsorshipDate": "2025-03-06",
      "state": "NC"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-03-06",
      "state": "OH"
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
      "sponsorshipDate": "2025-03-11",
      "state": "PA"
    },
    {
      "bioguideId": "S001218",
      "district": "1",
      "firstName": "Melanie",
      "fullName": "Rep. Stansbury, Melanie A. [D-NM-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Stansbury",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-05-08",
      "state": "NM"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1906ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1906\nIN THE HOUSE OF REPRESENTATIVES\nMarch 6, 2025 Ms. Budzinski (for herself, Mr. Finstad , Mr. Davis of North Carolina , and Mr. Taylor ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide for the prioritization of projects that provide behavioral and mental health treatment services in selecting grantees under certain rural development programs, and extend the substance abuse disorder set-aside and priority under the programs.\n#### 1. Short title\nThis Act may be cited as the Rural Wellness Act .\n#### 2. Prioritization of projects that provide behavioral and mental health treatment services in selecting grantees under certain rural development programs; extension of substance use disorder set-aside and priority under the programs\nSection 6101(a)(1) of the Agriculture Improvement Act of 2018 (132 Stat. 4726) is amended\u2014\n**(1)**\nby striking 2025 and inserting 2029 ;\n**(2)**\nin subparagraph (A), by striking 20 each place it appears and inserting 17 ;\n**(3)**\nin subparagraph (B)\u2014\n**(A)**\nin clause (ii)\u2014\n**(i)**\nby inserting or (ii) before that receives ; and\n**(ii)**\nby inserting or for behavioral and mental health treatment, respectively before the period; and\n**(B)**\nby redesignating clause (ii) as clause (iii) and inserting after clause (i) the following:\n(ii) Behavioral and mental health treatment selection priority In selecting recipients of direct loans or grants for the development of essential community facilities under section 306(a) of the Consolidated Farm and Rural Development Act ( 7 U.S.C. 1926(a) ), the Secretary shall give priority to entities eligible for those direct loans or grants\u2014 (I) to develop facilities to provide behavioral and mental health services such as\u2014 (aa) prevention services; (bb) treatment services; (cc) recovery services; or (dd) any combination of those services; and (II) that employ staff that have appropriate expertise and training in how to identify and treat individuals with behavioral and mental health concerns. ; and\n**(4)**\nby adding at the end the following:\n(D) Rural health and safety education programs; behavioral and mental health selection priority In making grants under section 502(i) of the Rural Development Act of 1972 ( 7 U.S.C. 2662(i) ), the Secretary shall give priority to an applicant that will use the grant for behavioral and mental health education and treatment. .",
      "versionDate": "2025-03-06",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-05-05T19:05:45Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-06",
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
          "measure-id": "id119hr1906",
          "measure-number": "1906",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-06",
          "originChamber": "HOUSE",
          "update-date": "2025-05-09"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1906v00",
            "update-date": "2025-05-09"
          },
          "action-date": "2025-03-06",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Rural Wellness Act</strong></p><p>This bill prioritizes behavioral and mental health treatment services under certain rural development grant and loan programs.\u00a0The bill also reauthorizes through FY2029 the set-asides and prioritizations for substance use disorder treatment services under\u00a0the Department of Agriculture's (1) Community Facilities Direct Loan and Grant\u00a0Program, (2) Rural Health and Safety Education Competitive Grants Program, and (3) Distance Learning and Telemedicine Grant Program.</p><p>Under the community facilities program, the bill prioritizes direct loans and grants for the development of behavioral and mental health services facilities, including facilities that provide treatment services. Further, loans and grants provided under the program may be used to develop facilities and systems\u00a0to provide telehealth services for behavioral and mental health treatment.</p><p>Under the\u00a0Rural Health and Safety Education Competitive Grants Program, the bill prioritizes grants for behavioral and mental health education and treatment.</p><p>Under the Distance Learning and Telemedicine Grants Program, the bill includes a 17% set-aside for telemedicine\u00a0projects that provide substance use disorder treatment services (currently a 20% set-aside).\u00a0</p><p>\u00a0</p>"
        },
        "title": "Rural Wellness Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1906.xml",
    "summary": {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Wellness Act</strong></p><p>This bill prioritizes behavioral and mental health treatment services under certain rural development grant and loan programs.\u00a0The bill also reauthorizes through FY2029 the set-asides and prioritizations for substance use disorder treatment services under\u00a0the Department of Agriculture's (1) Community Facilities Direct Loan and Grant\u00a0Program, (2) Rural Health and Safety Education Competitive Grants Program, and (3) Distance Learning and Telemedicine Grant Program.</p><p>Under the community facilities program, the bill prioritizes direct loans and grants for the development of behavioral and mental health services facilities, including facilities that provide treatment services. Further, loans and grants provided under the program may be used to develop facilities and systems\u00a0to provide telehealth services for behavioral and mental health treatment.</p><p>Under the\u00a0Rural Health and Safety Education Competitive Grants Program, the bill prioritizes grants for behavioral and mental health education and treatment.</p><p>Under the Distance Learning and Telemedicine Grants Program, the bill includes a 17% set-aside for telemedicine\u00a0projects that provide substance use disorder treatment services (currently a 20% set-aside).\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr1906"
    },
    "title": "Rural Wellness Act"
  },
  "summaries": [
    {
      "actionDate": "2025-03-06",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Rural Wellness Act</strong></p><p>This bill prioritizes behavioral and mental health treatment services under certain rural development grant and loan programs.\u00a0The bill also reauthorizes through FY2029 the set-asides and prioritizations for substance use disorder treatment services under\u00a0the Department of Agriculture's (1) Community Facilities Direct Loan and Grant\u00a0Program, (2) Rural Health and Safety Education Competitive Grants Program, and (3) Distance Learning and Telemedicine Grant Program.</p><p>Under the community facilities program, the bill prioritizes direct loans and grants for the development of behavioral and mental health services facilities, including facilities that provide treatment services. Further, loans and grants provided under the program may be used to develop facilities and systems\u00a0to provide telehealth services for behavioral and mental health treatment.</p><p>Under the\u00a0Rural Health and Safety Education Competitive Grants Program, the bill prioritizes grants for behavioral and mental health education and treatment.</p><p>Under the Distance Learning and Telemedicine Grants Program, the bill includes a 17% set-aside for telemedicine\u00a0projects that provide substance use disorder treatment services (currently a 20% set-aside).\u00a0</p><p>\u00a0</p>",
      "updateDate": "2025-05-09",
      "versionCode": "id119hr1906"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1906ih.xml"
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
      "title": "Rural Wellness Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T07:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Rural Wellness Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T07:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the prioritization of projects that provide behavioral and mental health treatment services in selecting grantees under certain rural development programs, and extend the substance abuse disorder set-aside and priority under the programs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T07:03:34Z"
    }
  ]
}
```
