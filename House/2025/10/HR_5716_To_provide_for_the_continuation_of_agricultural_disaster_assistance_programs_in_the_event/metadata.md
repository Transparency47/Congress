# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5716?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5716
- Title: FARM SAFE Act
- Congress: 119
- Bill type: HR
- Bill number: 5716
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2025-11-13T09:05:37Z
- Update date including text: 2025-11-13T09:05:37Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Agriculture.
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Agriculture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5716",
    "number": "5716",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "M001232",
        "district": "6",
        "firstName": "April",
        "fullName": "Rep. McClain Delaney, April [D-MD-6]",
        "lastName": "McClain Delaney",
        "party": "D",
        "state": "MD"
      }
    ],
    "title": "FARM SAFE Act",
    "type": "HR",
    "updateDate": "2025-11-13T09:05:37Z",
    "updateDateIncludingText": "2025-11-13T09:05:37Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
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
      "actionDate": "2025-10-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T19:02:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
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
      "bioguideId": "M001227",
      "district": "4",
      "firstName": "Jennifer",
      "fullName": "Rep. McClellan, Jennifer L. [D-VA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "McClellan",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "VA"
    },
    {
      "bioguideId": "R000599",
      "district": "25",
      "firstName": "Raul",
      "fullName": "Rep. Ruiz, Raul [D-CA-25]",
      "isOriginalCosponsor": "True",
      "lastName": "Ruiz",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "CA"
    },
    {
      "bioguideId": "F000481",
      "district": "2",
      "firstName": "Shomari",
      "fullName": "Rep. Figures, Shomari [D-AL-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Figures",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "AL"
    },
    {
      "bioguideId": "E000301",
      "district": "3",
      "firstName": "Sarah",
      "fullName": "Rep. Elfreth, Sarah [D-MD-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Elfreth",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "MD"
    },
    {
      "bioguideId": "C001125",
      "district": "2",
      "firstName": "Troy",
      "fullName": "Rep. Carter, Troy A. [D-LA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Carter",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "LA"
    },
    {
      "bioguideId": "A000370",
      "district": "12",
      "firstName": "Alma",
      "fullName": "Rep. Adams, Alma S. [D-NC-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Adams",
      "middleName": "S.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NC"
    },
    {
      "bioguideId": "I000058",
      "district": "4",
      "firstName": "Glenn",
      "fullName": "Rep. Ivey, Glenn [D-MD-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Ivey",
      "party": "D",
      "sponsorshipDate": "2025-10-28",
      "state": "MD"
    },
    {
      "bioguideId": "W000829",
      "district": "8",
      "firstName": "Tony",
      "fullName": "Rep. Wied, Tony [R-WI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Wied",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5716ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5716\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mrs. McClain Delaney (for herself, Ms. McClellan , Mr. Ruiz , Mr. Figures , Ms. Elfreth , Mr. Carter of Louisiana , and Ms. Adams ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo provide for the continuation of agricultural disaster assistance programs in the event of a Government shutdown.\n#### 1. Short title\nThis Act may be cited as the Federal Agricultural Relief Maintained during Shutdowns And Federal Emergencies Act or the FARM SAFE Act .\n#### 2. Continuation of agricultural disaster assistance programs during lapses in appropriations\n##### (a) In general\nNotwithstanding any other provision of law, during a lapse in appropriations described in subsection (a), any employee of the Department of Agriculture necessary to carry out an agricultural disaster assistance program\u2014\n**(1)**\nshall be treated as an excepted employee under section 1341 of title 31, United States Code, who is required to perform work during such lapse in appropriations, notwithstanding section 1342 of such title; and\n**(2)**\nmay not be removed under a reduction in force.\n##### (b) Agricultural disaster assistance program defined\nIn this section, the term agricultural disaster assistance program means\u2014\n**(1)**\na program under title IV of the Agricultural Credit Act of 1978 ( 16 U.S.C. 2201 et seq. );\n**(2)**\na program under section 1501 of the Agricultural Act of 2014 ( 7 U.S.C. 9081 ); and\n**(3)**\na program authorized pursuant to an Act of Congress under which the Secretary of Agriculture provides disaster assistance, as determined by the Secretary.",
      "versionDate": "2025-10-08",
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
        "updateDate": "2025-10-17T15:12:39Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-10-08",
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
          "measure-id": "id119hr5716",
          "measure-number": "5716",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-08",
          "originChamber": "HOUSE",
          "update-date": "2025-10-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5716v00",
            "update-date": "2025-10-17"
          },
          "action-date": "2025-10-08",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Federal Agricultural Relief Maintained during Shutdowns And Federal Emergencies Act or the FARM SAFE Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to continue activities related to agricultural disaster assistance programs during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill provides\u00a0that any USDA employee necessary to carry out an agricultural disaster assistance program (1) must be treated as an excepted employee who is required to perform work during a lapse in appropriations, and (2) may not be removed under a reduction in force.</p>"
        },
        "title": "FARM SAFE Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5716.xml",
    "summary": {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Agricultural Relief Maintained during Shutdowns And Federal Emergencies Act or the FARM SAFE Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to continue activities related to agricultural disaster assistance programs during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill provides\u00a0that any USDA employee necessary to carry out an agricultural disaster assistance program (1) must be treated as an excepted employee who is required to perform work during a lapse in appropriations, and (2) may not be removed under a reduction in force.</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5716"
    },
    "title": "FARM SAFE Act"
  },
  "summaries": [
    {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Federal Agricultural Relief Maintained during Shutdowns And Federal Emergencies Act or the FARM SAFE Act</strong></p><p>This bill requires the Department of Agriculture (USDA) to continue activities related to agricultural disaster assistance programs during a lapse in appropriations (i.e., government shutdown).</p><p>Specifically, the bill provides\u00a0that any USDA employee necessary to carry out an agricultural disaster assistance program (1) must be treated as an excepted employee who is required to perform work during a lapse in appropriations, and (2) may not be removed under a reduction in force.</p>",
      "updateDate": "2025-10-17",
      "versionCode": "id119hr5716"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5716ih.xml"
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
      "title": "FARM SAFE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-16T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "FARM SAFE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Federal Agricultural Relief Maintained during Shutdowns And Federal Emergencies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-16T02:53:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To provide for the continuation of agricultural disaster assistance programs in the event of a Government shutdown.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:22Z"
    }
  ]
}
```
