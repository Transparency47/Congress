# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7517?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7517
- Title: To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the "Robert Allen Bishop, Sr. Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 7517
- Origin chamber: House
- Introduced date: 2026-02-11
- Update date: 2026-05-22T08:07:55Z
- Update date including text: 2026-05-22T08:07:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2026-02-11: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H2204)
- Latest action: 2026-02-11: Introduced in House

## Actions

- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Introduced in House
- 2026-02-11 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-12 - IntroReferral: Sponsor introductory remarks on measure. (CR H2204)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-11",
    "latestAction": {
      "actionDate": "2026-02-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7517",
    "number": "7517",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "T000467",
        "district": "15",
        "firstName": "Glenn",
        "fullName": "Rep. Thompson, Glenn [R-PA-15]",
        "lastName": "Thompson",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\".",
    "type": "HR",
    "updateDate": "2026-05-22T08:07:55Z",
    "updateDateIncludingText": "2026-05-22T08:07:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "B00100",
      "actionDate": "2026-02-12",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Sponsor introductory remarks on measure. (CR H2204)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-02-11",
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
      "actionDate": "2026-02-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-11",
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
          "date": "2026-02-11T16:01:10Z",
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
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "E000296",
      "district": "3",
      "firstName": "Dwight",
      "fullName": "Rep. Evans, Dwight [D-PA-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Evans",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "P000605",
      "district": "10",
      "firstName": "Scott",
      "fullName": "Rep. Perry, Scott [R-PA-10]",
      "isOriginalCosponsor": "True",
      "lastName": "Perry",
      "party": "R",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2026-02-11",
      "state": "PA"
    },
    {
      "bioguideId": "B001327",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Bresnahan, Robert P. [R-PA-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Bresnahan",
      "middleName": "P.",
      "party": "R",
      "sponsorshipDate": "2026-02-17",
      "state": "PA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "L000602",
      "district": "12",
      "firstName": "Summer",
      "fullName": "Rep. Lee, Summer L. [D-PA-12]",
      "isOriginalCosponsor": "False",
      "lastName": "Lee",
      "middleName": "L.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "PA"
    },
    {
      "bioguideId": "J000302",
      "district": "13",
      "firstName": "John",
      "fullName": "Rep. Joyce, John [R-PA-13]",
      "isOriginalCosponsor": "False",
      "lastName": "Joyce",
      "party": "R",
      "sponsorshipDate": "2026-02-23",
      "state": "PA"
    },
    {
      "bioguideId": "M001204",
      "district": "9",
      "firstName": "Daniel",
      "fullName": "Rep. Meuser, Daniel [R-PA-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Meuser",
      "party": "R",
      "sponsorshipDate": "2026-03-03",
      "state": "PA"
    },
    {
      "bioguideId": "K000376",
      "district": "16",
      "firstName": "Mike",
      "fullName": "Rep. Kelly, Mike [R-PA-16]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "R",
      "sponsorshipDate": "2026-04-13",
      "state": "PA"
    },
    {
      "bioguideId": "R000610",
      "district": "14",
      "firstName": "Guy",
      "fullName": "Rep. Reschenthaler, Guy [R-PA-14]",
      "isOriginalCosponsor": "False",
      "lastName": "Reschenthaler",
      "party": "R",
      "sponsorshipDate": "2026-05-21",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7517ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7517\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 11, 2026 Mr. Thompson of Pennsylvania (for himself, Mr. Fitzpatrick , Mr. Evans of Pennsylvania , Mr. Perry , and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the Robert Allen Bishop, Sr. Post Office Building .\n#### 1. Robert Allen Bishop, Sr. Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, shall be known and designated as the Robert Allen Bishop, Sr. Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Robert Allen Bishop, Sr. Post Office Building .",
      "versionDate": "2026-02-11",
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
        "updateDate": "2026-02-23T16:36:15Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2026-02-11",
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
          "measure-id": "id119hr7517",
          "measure-number": "7517",
          "measure-type": "hr",
          "orig-publish-date": "2026-02-11",
          "originChamber": "HOUSE",
          "update-date": "2026-02-23"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr7517v00",
            "update-date": "2026-02-23"
          },
          "action-date": "2026-02-11",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr7517.xml",
    "summary": {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\".",
      "updateDate": "2026-02-23",
      "versionCode": "id119hr7517"
    },
    "title": "To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2026-02-11",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\".",
      "updateDate": "2026-02-23",
      "versionCode": "id119hr7517"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-02-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7517ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-23T13:18:29Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 10 East Main Street in Mahaffey, Pennsylvania, as the \"Robert Allen Bishop, Sr. Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-12T09:06:41Z"
    }
  ]
}
```
