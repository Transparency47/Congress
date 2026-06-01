# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2165?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2165
- Title: Choice in Automobile Retail Sales Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2165
- Origin chamber: House
- Introduced date: 2025-03-14
- Update date: 2026-05-20T08:08:33Z
- Update date including text: 2026-05-20T08:08:33Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-03-14: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H1317)
- Latest action: 2025-03-14: Introduced in House

## Actions

- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Introduced in House
- 2025-03-14 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-03-27 - IntroReferral: Sponsor introductory remarks on measure. (CR H1317)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-14",
    "latestAction": {
      "actionDate": "2025-03-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2165",
    "number": "2165",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "Choice in Automobile Retail Sales Act of 2025",
    "type": "HR",
    "updateDate": "2026-05-20T08:08:33Z",
    "updateDateIncludingText": "2026-05-20T08:08:33Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2025-03-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H1317)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-14",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-14",
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
          "date": "2025-03-14T13:07:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ID"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "FL"
    },
    {
      "bioguideId": "A000372",
      "district": "12",
      "firstName": "Rick",
      "fullName": "Rep. Allen, Rick W. [R-GA-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Allen",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "GA"
    },
    {
      "bioguideId": "B001306",
      "district": "12",
      "firstName": "Troy",
      "fullName": "Rep. Balderson, Troy [R-OH-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Balderson",
      "party": "R",
      "sponsorshipDate": "2025-03-24",
      "state": "OH"
    },
    {
      "bioguideId": "M000871",
      "district": "1",
      "firstName": "Tracey",
      "fullName": "Rep. Mann, Tracey [R-KS-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mann",
      "party": "R",
      "sponsorshipDate": "2025-03-25",
      "state": "KS"
    },
    {
      "bioguideId": "L000566",
      "district": "5",
      "firstName": "Robert",
      "fullName": "Rep. Latta, Robert E. [R-OH-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Latta",
      "middleName": "E.",
      "party": "R",
      "sponsorshipDate": "2025-03-26",
      "state": "OH"
    },
    {
      "bioguideId": "B000668",
      "district": "2",
      "firstName": "Cliff",
      "fullName": "Rep. Bentz, Cliff [R-OR-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Bentz",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "OR"
    },
    {
      "bioguideId": "G000568",
      "district": "9",
      "firstName": "H.",
      "fullName": "Rep. Griffith, H. Morgan [R-VA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Griffith",
      "middleName": "Morgan",
      "party": "R",
      "sponsorshipDate": "2025-03-27",
      "state": "VA"
    },
    {
      "bioguideId": "B001321",
      "district": "7",
      "firstName": "Tom",
      "fullName": "Rep. Barrett, Tom [R-MI-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Barrett",
      "party": "R",
      "sponsorshipDate": "2025-06-02",
      "state": "MI"
    },
    {
      "bioguideId": "L000585",
      "district": "16",
      "firstName": "Darin",
      "fullName": "Rep. LaHood, Darin [R-IL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "LaHood",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "IL"
    },
    {
      "bioguideId": "B001295",
      "district": "12",
      "firstName": "Mike",
      "fullName": "Rep. Bost, Mike [R-IL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bost",
      "party": "R",
      "sponsorshipDate": "2026-02-02",
      "state": "IL"
    },
    {
      "bioguideId": "G000576",
      "district": "6",
      "firstName": "Glenn",
      "fullName": "Rep. Grothman, Glenn [R-WI-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Grothman",
      "party": "R",
      "sponsorshipDate": "2026-05-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2165ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2165\nIN THE HOUSE OF REPRESENTATIVES\nMarch 14, 2025 Mr. Walberg (for himself, Mr. Fulcher , Mr. Bilirakis , and Mr. Allen ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Clean Air Act to ensure that tailpipe regulations do not limit the availability of new motor vehicles.\n#### 1. Short title\nThis Act may be cited as the Choice in Automobile Retail Sales Act of 2025 .\n#### 2. Ensuring tailpipe regulations do not limit the availability of new motor vehicles\n##### (a) In general\nSection 202(a)(2) of the Clean Air Act ( 42 U.S.C. 7521(a)(2) ) is amended\u2014\n**(1)**\nby striking (2) Any regulation and inserting (2)(A) Any regulation ; and\n**(2)**\nby adding at the end the following:\n(B) Any regulation proposed or prescribed, including any revision to a regulation, under paragraph (1) on or after January 1, 2021, shall not\u2014 (i) mandate the use of any specific technology; or (ii) result in limited availability of new motor vehicles based on the type of new motor vehicle engine in such new motor vehicles. .\n##### (b) Necessary revisions to regulations\nNot later than 24 months after the date of enactment of this Act, the Administrator of the Environmental Protection Agency shall promulgate such revisions to regulations as may be necessary to conform such regulations to section 202(a)(2)(B) of the Clean Air Act, as added by subsection (a).",
      "versionDate": "2025-03-14",
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
        "updateDate": "2025-04-01T17:44:17Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-03-14",
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
          "measure-id": "id119hr2165",
          "measure-number": "2165",
          "measure-type": "hr",
          "orig-publish-date": "2025-03-14",
          "originChamber": "HOUSE",
          "update-date": "2025-06-17"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr2165v00",
            "update-date": "2025-06-17"
          },
          "action-date": "2025-03-14",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Choice in Automobile Retail Sales Act of 2025</strong></p><p>This bill limits the authority of the Environmental Protection Agency (EPA) with regard to regulating emissions standards for new motor vehicles. Specifically, the EPA is prohibited from prescribing a regulation related to new motor vehicle emissions standards that (1) mandates the use of any specific technology, or (2) results in limited availability of new motor vehicles based on the type of new motor vehicle engine.</p>"
        },
        "title": "Choice in Automobile Retail Sales Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr2165.xml",
    "summary": {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Choice in Automobile Retail Sales Act of 2025</strong></p><p>This bill limits the authority of the Environmental Protection Agency (EPA) with regard to regulating emissions standards for new motor vehicles. Specifically, the EPA is prohibited from prescribing a regulation related to new motor vehicle emissions standards that (1) mandates the use of any specific technology, or (2) results in limited availability of new motor vehicles based on the type of new motor vehicle engine.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2165"
    },
    "title": "Choice in Automobile Retail Sales Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-03-14",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Choice in Automobile Retail Sales Act of 2025</strong></p><p>This bill limits the authority of the Environmental Protection Agency (EPA) with regard to regulating emissions standards for new motor vehicles. Specifically, the EPA is prohibited from prescribing a regulation related to new motor vehicle emissions standards that (1) mandates the use of any specific technology, or (2) results in limited availability of new motor vehicles based on the type of new motor vehicle engine.</p>",
      "updateDate": "2025-06-17",
      "versionCode": "id119hr2165"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-03-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2165ih.xml"
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
      "title": "Choice in Automobile Retail Sales Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-01T04:38:23Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Choice in Automobile Retail Sales Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-01T04:38:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Clean Air Act to ensure that tailpipe regulations do not limit the availability of new motor vehicles.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-01T04:33:37Z"
    }
  ]
}
```
