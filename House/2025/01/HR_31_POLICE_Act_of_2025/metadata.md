# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/31?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/31
- Title: POLICE Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 31
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2025-12-06T06:46:54Z
- Update date including text: 2025-12-06T06:46:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, summaries, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/31",
    "number": "31",
    "originChamber": "House",
    "policyArea": {
      "name": "Immigration"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "POLICE Act of 2025",
    "type": "HR",
    "updateDate": "2025-12-06T06:46:54Z",
    "updateDateIncludingText": "2025-12-06T06:46:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
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
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:03:05Z",
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
      "bioguideId": "H001093",
      "district": "9",
      "firstName": "Erin",
      "fullName": "Rep. Houchin, Erin [R-IN-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Houchin",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IN"
    },
    {
      "bioguideId": "T000478",
      "district": "24",
      "firstName": "Claudia",
      "fullName": "Rep. Tenney, Claudia [R-NY-24]",
      "isOriginalCosponsor": "True",
      "lastName": "Tenney",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "NY"
    },
    {
      "bioguideId": "F000446",
      "district": "4",
      "firstName": "Randy",
      "fullName": "Rep. Feenstra, Randy [R-IA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Feenstra",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-01-03",
      "state": "IA"
    },
    {
      "bioguideId": "L000600",
      "district": "23",
      "firstName": "Nicholas",
      "fullName": "Rep. Langworthy, Nicholas A. [R-NY-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Langworthy",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-01-06",
      "state": "NY"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "OH"
    },
    {
      "bioguideId": "D000594",
      "district": "15",
      "firstName": "Monica",
      "fullName": "Rep. De La Cruz, Monica [R-TX-15]",
      "isOriginalCosponsor": "False",
      "lastName": "De La Cruz",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "TX"
    },
    {
      "bioguideId": "B001257",
      "district": "12",
      "firstName": "Gus",
      "fullName": "Rep. Bilirakis, Gus M. [R-FL-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Bilirakis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-01-07",
      "state": "FL"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-01-09",
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
      "sponsorshipDate": "2025-01-13",
      "state": "NC"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2025-01-15",
      "state": "PA"
    },
    {
      "bioguideId": "S001228",
      "district": "2",
      "firstName": "Derek",
      "fullName": "Rep. Schmidt, Derek [R-KS-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Schmidt",
      "party": "R",
      "sponsorshipDate": "2025-01-21",
      "state": "KS"
    },
    {
      "bioguideId": "S001212",
      "district": "8",
      "firstName": "Pete",
      "fullName": "Rep. Stauber, Pete [R-MN-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Stauber",
      "party": "R",
      "sponsorshipDate": "2025-01-22",
      "state": "MN"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-01-23",
      "state": "NY"
    },
    {
      "bioguideId": "S001196",
      "district": "21",
      "firstName": "Elise",
      "fullName": "Rep. Stefanik, Elise M. [R-NY-21]",
      "isOriginalCosponsor": "False",
      "lastName": "Stefanik",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-04-07",
      "state": "NY"
    },
    {
      "bioguideId": "E000246",
      "district": "11",
      "firstName": "Chuck",
      "fullName": "Rep. Edwards, Chuck [R-NC-11]",
      "isOriginalCosponsor": "False",
      "lastName": "Edwards",
      "party": "R",
      "sponsorshipDate": "2025-05-05",
      "state": "NC"
    },
    {
      "bioguideId": "M001239",
      "district": "5",
      "firstName": "John",
      "fullName": "Rep. McGuire, John J. [R-VA-5]",
      "isOriginalCosponsor": "False",
      "lastName": "McGuire",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-13",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr31ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 31\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Mr. Garbarino (for himself, Mrs. Houchin , Ms. Tenney , Ms. Malliotakis , Mr. Feenstra , and Mr. Nunn of Iowa ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo make the assault of a law enforcement officer a deportable offense, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025 .\n#### 2. Assault of law enforcement officer\nSection 237(a)(2) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2) ) is amended by adding at the end the following:\n(G) Assault of law enforcement officer (i) In general Any alien who has been convicted of, who admits having committed, or who admits committing acts which constitute the essential elements of, any offense involving assault of a law enforcement officer is deportable. (ii) Circumstances The circumstances referred to in clause (i) are that the law enforcement officer was assaulted\u2014 (I) while he or she was engaged in the performance of his or her official duties; (II) because of the performance of his or her official duties; or (III) because of his or her status as a law enforcement officer. (iii) Definitions In this subparagraph\u2014 (I) the term assault has the meaning given that term in the jurisdiction where the act occurred; and (II) the term law enforcement officer is a person authorized by law\u2014 (aa) to engage in or supervise the prevention, detention, investigation, or prosecution, or the incarceration of any person for any criminal violation of law; (bb) to apprehend, arrest, or prosecute an individual for any criminal violation of law; or (cc) to be a firefighter or other first responder. .\n#### 3. Report on aliens deported for assaulting a law enforcement officer\nOn an annual basis, the Secretary of Homeland Security shall submit to Congress and make publicly available on the website of the Department of Homeland Security a report on the number of aliens who were deported during the previous year under section 237(a)(2)(G) of the Immigration and Nationality Act ( 8 U.S.C. 1227(a)(2)(G) ).",
      "versionDate": "2025-01-03",
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
        "actionDate": "2025-01-23",
        "text": "Read twice and referred to the Committee on the Judiciary."
      },
      "number": "212",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "POLICE Act of 2025",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Border security and unlawful immigration",
            "updateDate": "2025-06-03T18:09:57Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2025-06-03T18:10:19Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-06-03T18:10:44Z"
          },
          {
            "name": "Immigration status and procedures",
            "updateDate": "2025-06-03T18:09:48Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2025-06-03T18:10:35Z"
          },
          {
            "name": "Law enforcement officers",
            "updateDate": "2025-06-03T18:09:33Z"
          },
          {
            "name": "Violent crime",
            "updateDate": "2025-06-03T18:10:04Z"
          }
        ]
      },
      "policyArea": {
        "name": "Immigration",
        "updateDate": "2025-02-03T15:08:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-01-03",
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
          "measure-id": "id119hr31",
          "measure-number": "31",
          "measure-type": "hr",
          "orig-publish-date": "2025-01-03",
          "originChamber": "HOUSE",
          "update-date": "2025-02-10"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr31v00",
            "update-date": "2025-02-10"
          },
          "action-date": "2025-01-03",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous year pursuant to this bill.</p>"
        },
        "title": "POLICE Act of 2025"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr31.xml",
    "summary": {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous year pursuant to this bill.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr31"
    },
    "title": "POLICE Act of 2025"
  },
  "summaries": [
    {
      "actionDate": "2025-01-03",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025 or the POLICE Act of 2025</strong></p><p>This bill makes assaulting a law enforcement officer, firefighter, or other first responder a deportable offense.</p><p>Specifically, the bill makes deportable any non-U.S. national (<em>alien</em> under federal law) who has been convicted of (or admits to have committed) any act that constitutes the essential elements of any offense involving assault of a law enforcement officer, firefighter, or other first responder.</p><p>The Department of Homeland Security must publish annually on its website a report on the number of individuals deported in the previous year pursuant to this bill.</p>",
      "updateDate": "2025-02-10",
      "versionCode": "id119hr31"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr31ih.xml"
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
      "title": "POLICE Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-01-30T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POLICE Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protect Our Law enforcement with Immigration Control and Enforcement Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-01-30T10:53:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To make the assault of a law enforcement officer a deportable offense, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-01-30T10:48:24Z"
    }
  ]
}
```
