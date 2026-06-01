# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1643?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1643
- Title: SAFER Voter Act
- Congress: 119
- Bill type: HR
- Bill number: 1643
- Origin chamber: House
- Introduced date: 2025-02-27
- Update date: 2026-04-03T19:47:45Z
- Update date including text: 2026-04-03T19:47:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-02-27: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-27: Introduced in House

## Actions

- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Introduced in House
- 2025-02-27 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1643",
    "number": "1643",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001184",
        "district": "4",
        "firstName": "Thomas",
        "fullName": "Rep. Massie, Thomas [R-KY-4]",
        "lastName": "Massie",
        "party": "R",
        "state": "KY"
      }
    ],
    "title": "SAFER Voter Act",
    "type": "HR",
    "updateDate": "2026-04-03T19:47:45Z",
    "updateDateIncludingText": "2026-04-03T19:47:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T14:05:20Z",
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
      "bioguideId": "B000825",
      "district": "4",
      "firstName": "Lauren",
      "fullName": "Rep. Boebert, Lauren [R-CO-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Boebert",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CO"
    },
    {
      "bioguideId": "C001116",
      "district": "9",
      "firstName": "Andrew",
      "fullName": "Rep. Clyde, Andrew S. [R-GA-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Clyde",
      "middleName": "S.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "C001129",
      "district": "10",
      "firstName": "Mike",
      "fullName": "Rep. Collins, Mike [R-GA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Collins",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "G000596",
      "district": "14",
      "firstName": "Marjorie",
      "fullName": "Rep. Greene, Marjorie Taylor [R-GA-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Greene",
      "middleName": "Taylor",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "GA"
    },
    {
      "bioguideId": "H001096",
      "district": "0",
      "firstName": "Harriet",
      "fullName": "Rep. Hageman, Harriet M. [R-WY-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Hageman",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "WY"
    },
    {
      "bioguideId": "L000578",
      "district": "1",
      "firstName": "Doug",
      "fullName": "Rep. LaMalfa, Doug [R-CA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "LaMalfa",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "CA"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "PA"
    },
    {
      "bioguideId": "R000614",
      "district": "21",
      "firstName": "Chip",
      "fullName": "Rep. Roy, Chip [R-TX-21]",
      "isOriginalCosponsor": "True",
      "lastName": "Roy",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "S000929",
      "district": "5",
      "firstName": "Victoria",
      "fullName": "Rep. Spartz, Victoria [R-IN-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Spartz",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "IN"
    },
    {
      "bioguideId": "W000814",
      "district": "14",
      "firstName": "Randy",
      "fullName": "Rep. Weber, Randy K. Sr. [R-TX-14]",
      "isOriginalCosponsor": "True",
      "lastName": "Weber",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "G000603",
      "district": "26",
      "firstName": "Brandon",
      "fullName": "Rep. Gill, Brandon [R-TX-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Gill",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "TX"
    },
    {
      "bioguideId": "F000469",
      "district": "1",
      "firstName": "Russ",
      "fullName": "Rep. Fulcher, Russ [R-ID-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fulcher",
      "party": "R",
      "sponsorshipDate": "2025-03-14",
      "state": "ID"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-05-15",
      "state": "AZ"
    },
    {
      "bioguideId": "T000490",
      "district": "2",
      "firstName": "David",
      "fullName": "Rep. Taylor, David J. [R-OH-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Taylor",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-06-12",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1643ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1643\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 27, 2025 Mr. Massie (for himself, Ms. Boebert , Mr. Clyde , Mr. Collins , Ms. Greene of Georgia , Ms. Hageman , Mr. LaMalfa , Mr. Perry , Mr. Roy , Mrs. Spartz , Mr. Weber of Texas , and Mr. Gill of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo reduce, from 21 years of age to 18 years of age, the minimum age at which a person may obtain a handgun from a Federal firearms licensee.\n#### 1. Short title\nThis Act may be cited as the Second Amendment For Every Registrable Voter Act or the SAFER Voter Act .\n#### 2. Minimum age for obtaining a handgun from a Federal firearms licensee\n##### (a) In general\nSection 922(b)(1) of title 18, United States Code, is amended by striking , and, if the firearm, or ammunition is other than a shotgun or rifle, or ammunition for a shotgun or rifle, to any individual who the licensee knows or has reasonable cause to believe is less than twenty-one years of age .\n##### (b) Conforming amendment\nSection 922(c)(1) of such title is amended by striking , in the case of any firearm other than a shotgun or a rifle, I am twenty-one years or more of age, or that, in the case of a shotgun or a rifle, .",
      "versionDate": "2025-02-27",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Firearms and explosives",
            "updateDate": "2025-09-02T15:20:34Z"
          },
          {
            "name": "Licensing and registrations",
            "updateDate": "2025-09-02T15:20:34Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2025-09-02T15:20:34Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-21T14:55:14Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-02-27",
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
          "measure-id": "id119hr1643",
          "measure-number": "1643",
          "measure-type": "hr",
          "orig-publish-date": "2025-02-27",
          "originChamber": "HOUSE",
          "update-date": "2026-04-03"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr1643v00",
            "update-date": "2026-04-03"
          },
          "action-date": "2025-02-27",
          "action-desc": "Introduced in House",
          "summary-text": "<p><strong>Second Amendment For Every Registrable Voter Act or the SAFER Voter Act</strong></p> <p>This bill reduces the minimum age\u2014from 21 years to 18 years\u2014at which an individual may obtain a handgun from a federally licensed gun dealer, manufacturer, importer, or collector.</p>"
        },
        "title": "SAFER Voter Act"
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr1643.xml",
    "summary": {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Amendment For Every Registrable Voter Act or the SAFER Voter Act</strong></p> <p>This bill reduces the minimum age\u2014from 21 years to 18 years\u2014at which an individual may obtain a handgun from a federally licensed gun dealer, manufacturer, importer, or collector.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1643"
    },
    "title": "SAFER Voter Act"
  },
  "summaries": [
    {
      "actionDate": "2025-02-27",
      "actionDesc": "Introduced in House",
      "text": "<p><strong>Second Amendment For Every Registrable Voter Act or the SAFER Voter Act</strong></p> <p>This bill reduces the minimum age\u2014from 21 years to 18 years\u2014at which an individual may obtain a handgun from a federally licensed gun dealer, manufacturer, importer, or collector.</p>",
      "updateDate": "2026-04-03",
      "versionCode": "id119hr1643"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1643ih.xml"
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
      "title": "SAFER Voter Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-20T09:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SAFER Voter Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Second Amendment For Every Registrable Voter Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-20T09:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reduce, from 21 years of age to 18 years of age, the minimum age at which a person may obtain a handgun from a Federal firearms licensee.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-20T09:18:27Z"
    }
  ]
}
```
