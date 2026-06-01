# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/4024?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/4024
- Title: Filling Public Safety Vacancies Act
- Congress: 119
- Bill type: HR
- Bill number: 4024
- Origin chamber: House
- Introduced date: 2025-06-17
- Update date: 2026-04-10T08:05:24Z
- Update date including text: 2026-04-10T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-06-17: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- Latest action: 2025-06-17: Introduced in House

## Actions

- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Introduced in House
- 2025-06-17 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-06-17 - IntroReferral: Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-17",
    "latestAction": {
      "actionDate": "2025-06-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/4024",
    "number": "4024",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "C001112",
        "district": "24",
        "firstName": "Salud",
        "fullName": "Rep. Carbajal, Salud O. [D-CA-24]",
        "lastName": "Carbajal",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Filling Public Safety Vacancies Act",
    "type": "HR",
    "updateDate": "2026-04-10T08:05:24Z",
    "updateDateIncludingText": "2026-04-10T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
      "committees": {
        "item": {
          "name": "Budget Committee",
          "systemCode": "hsbu00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-17",
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
      "text": "Referred to the Committee on Appropriations, and in addition to the Committee on the Budget, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-17",
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
          "date": "2025-06-17T15:03:20Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Budget Committee",
      "systemCode": "hsbu00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-06-17T15:03:15Z",
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
      "bioguideId": "B001298",
      "district": "2",
      "firstName": "Don",
      "fullName": "Rep. Bacon, Don [R-NE-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bacon",
      "party": "R",
      "sponsorshipDate": "2025-06-17",
      "state": "NE"
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
      "sponsorshipDate": "2025-07-02",
      "state": "PA"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "IA"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2026-04-09",
      "state": "OR"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4024ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 4024\nIN THE HOUSE OF REPRESENTATIVES\nJune 17, 2025 Mr. Carbajal (for himself and Mr. Bacon ) introduced the following bill; which was referred to the Committee on Appropriations , and in addition to the Committee on the Budget , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nMaking emergency supplemental appropriations for the hiring and rehiring of additional career law enforcement officers for the fiscal year ending September 30, 2025, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Filling Public Safety Vacancies Act .\n#### 2. Appropriation\n##### (a) In general\nThere is appropriated, out of amounts in the Treasury not otherwise appropriated, for the fiscal year ending September 30, 2025, to remain available until expended, $162,000,000 for additional amounts for grants for the hiring and rehiring of additional career law enforcement officers under section 1701 of title I of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10381 ).\n##### (b) Background checks and psychological evaluations\nA law enforcement agency using amounts appropriated under subsection (a) to hire or rehire a law enforcement officer\u2014\n**(1)**\nshall\u2014\n**(A)**\nperform a background check on the law enforcement officer; and\n**(B)**\nensure that the law enforcement officer undergoes a psychological evaluation; and\n**(2)**\nshall use amounts appropriated under subsection (a) or other funds of the law enforcement agency to cover the cost of carrying out the requirements under paragraph (1).\n#### 3. Emergency designation\nThe amounts provided by this Act are designated as an emergency requirement pursuant to section 251(b)(2)(A)(i) of the Balanced Budget and Emergency Deficit Control Act of 1985.",
      "versionDate": "2025-06-17",
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
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-07-23T10:29:26Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-06-17",
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
          "measure-id": "id119hr4024",
          "measure-number": "4024",
          "measure-type": "hr",
          "orig-publish-date": "2025-06-17",
          "originChamber": "HOUSE",
          "update-date": "2025-07-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr4024v00",
            "update-date": "2025-07-23"
          },
          "action-date": "2025-06-17",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Filling Public Safety Vacancies Act</strong></p><p>The bill provides additional funding for grants for the hiring and rehiring of additional career law enforcement officers under the Department of Justice's Community Oriented Policing Services (COPS) program.</p><p>The bill also requires law enforcement agencies that use the funds to hire or rehire a law enforcement officer to (1) perform a background check on the law enforcement officer, and (2) ensure that the law enforcement officer undergoes a psychological evaluation.</p>"
        },
        "title": "Filling Public Safety Vacancies Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr4024.xml",
    "summary": {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Filling Public Safety Vacancies Act</strong></p><p>The bill provides additional funding for grants for the hiring and rehiring of additional career law enforcement officers under the Department of Justice's Community Oriented Policing Services (COPS) program.</p><p>The bill also requires law enforcement agencies that use the funds to hire or rehire a law enforcement officer to (1) perform a background check on the law enforcement officer, and (2) ensure that the law enforcement officer undergoes a psychological evaluation.</p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr4024"
    },
    "title": "Filling Public Safety Vacancies Act"
  },
  "summaries": [
    {
      "actionDate": "2025-06-17",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Filling Public Safety Vacancies Act</strong></p><p>The bill provides additional funding for grants for the hiring and rehiring of additional career law enforcement officers under the Department of Justice's Community Oriented Policing Services (COPS) program.</p><p>The bill also requires law enforcement agencies that use the funds to hire or rehire a law enforcement officer to (1) perform a background check on the law enforcement officer, and (2) ensure that the law enforcement officer undergoes a psychological evaluation.</p>",
      "updateDate": "2025-07-23",
      "versionCode": "id119hr4024"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-06-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr4024ih.xml"
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
      "title": "Filling Public Safety Vacancies Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-18T08:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Filling Public Safety Vacancies Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-18T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Making emergency supplemental appropriations for the hiring and rehiring of additional career law enforcement officers for the fiscal year ending September 30, 2025, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-18T08:18:18Z"
    }
  ]
}
```
