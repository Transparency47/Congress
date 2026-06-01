# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7313?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7313
- Title: To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the "Poul Hornsleth Post Office".
- Congress: 119
- Bill type: HR
- Bill number: 7313
- Origin chamber: House
- Introduced date: 2026-02-02
- Update date: 2026-04-30T08:06:49Z
- Update date including text: 2026-04-30T08:06:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-02: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2026-02-02: Introduced in House

## Actions

- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Introduced in House
- 2026-02-02 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-02",
    "latestAction": {
      "actionDate": "2026-02-02",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7313",
    "number": "7313",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "L000596",
        "district": "13",
        "firstName": "Anna Paulina",
        "fullName": "Rep. Luna, Anna Paulina [R-FL-13]",
        "lastName": "Luna",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\".",
    "type": "HR",
    "updateDate": "2026-04-30T08:06:49Z",
    "updateDateIncludingText": "2026-04-30T08:06:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Oversight and Government Reform.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-02-02",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-02",
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
          "date": "2026-02-02T14:02:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Oversight and Government Reform Committee",
      "systemCode": "hsgo00",
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
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2026-04-16",
      "state": "FL"
    },
    {
      "bioguideId": "W000797",
      "district": "25",
      "firstName": "Debbie",
      "fullName": "Rep. Wasserman Schultz, Debbie [D-FL-25]",
      "isOriginalCosponsor": "False",
      "lastName": "Wasserman Schultz",
      "party": "D",
      "sponsorshipDate": "2026-04-27",
      "state": "FL"
    },
    {
      "bioguideId": "G000593",
      "district": "28",
      "firstName": "Carlos",
      "fullName": "Rep. Gimenez, Carlos A. [R-FL-28]",
      "isOriginalCosponsor": "False",
      "lastName": "Gimenez",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "H001099",
      "district": "8",
      "firstName": "Mike",
      "fullName": "Rep. Haridopolos, Mike [R-FL-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Haridopolos",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "B001260",
      "district": "16",
      "firstName": "Vern",
      "fullName": "Rep. Buchanan, Vern [R-FL-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Buchanan",
      "party": "R",
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
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
      "sponsorshipDate": "2026-04-28",
      "state": "FL"
    },
    {
      "bioguideId": "S001230",
      "district": "10",
      "firstName": "Suhas",
      "fullName": "Rep. Subramanyam, Suhas [D-VA-10]",
      "isOriginalCosponsor": "False",
      "lastName": "Subramanyam",
      "party": "D",
      "sponsorshipDate": "2026-04-29",
      "state": "VA"
    },
    {
      "bioguideId": "P000622",
      "district": "1",
      "firstName": "Jimmy",
      "fullName": "Rep. Patronis, Jimmy [R-FL-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Patronis",
      "party": "R",
      "sponsorshipDate": "2026-04-29",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7313ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7313\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 2, 2026 Mrs. Luna introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the Poul Hornsleth Post Office .\n#### 1. Poul Hornsleth Post Office\n##### (a) Designation\nThe facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, shall be known and designated as the Poul Hornsleth Post Office .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Poul Hornsleth Post Office .",
      "versionDate": "2026-02-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2026-02-19T18:50:21Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-02",
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
          "measure-id": "id119hr7313",
          "measure-number": "7313",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-02",
          "originChamber": "HOUSE",
          "update-date": "2026-02-19"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7313v00",
            "update-date": "2026-02-19"
          },
          "action-date": "2026-02-02",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7313.xml",
    "summary": {
      "actionDate": "2026-02-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\".",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr7313"
    },
    "title": "To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\"."
  },
  "summaries": [
    {
      "actionDate": "2026-02-02",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\".",
      "updateDate": "2026-02-19",
      "versionCode": "id119hr7313"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7313ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T07:48:28Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 3135 1st Avenue North in St. Petersburg, Florida, as the \"Poul Hornsleth Post Office\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-03T09:05:46Z"
    }
  ]
}
```
