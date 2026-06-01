# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5947?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5947
- Title: To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the "Commodore Dixie Kiefer Memorial Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 5947
- Origin chamber: House
- Introduced date: 2025-11-07
- Update date: 2025-12-08T15:56:14Z
- Update date including text: 2025-12-08T15:56:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-11-07: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-11-07: Introduced in House

## Actions

- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Introduced in House
- 2025-11-07 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-07",
    "latestAction": {
      "actionDate": "2025-11-07",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5947",
    "number": "5947",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "F000474",
        "district": "1",
        "firstName": "Mike",
        "fullName": "Rep. Flood, Mike [R-NE-1]",
        "lastName": "Flood",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\".",
    "type": "HR",
    "updateDate": "2025-12-08T15:56:14Z",
    "updateDateIncludingText": "2025-12-08T15:56:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-07",
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
      "actionDate": "2025-11-07",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-07",
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
          "date": "2025-11-07T19:07:00Z",
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
      "bioguideId": "S001172",
      "district": "3",
      "firstName": "Adrian",
      "fullName": "Rep. Smith, Adrian [R-NE-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Smith",
      "party": "R",
      "sponsorshipDate": "2025-11-12",
      "state": "NE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5947ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5947\nIN THE HOUSE OF REPRESENTATIVES\nNovember 7, 2025 Mr. Flood introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the Commodore Dixie Kiefer Memorial Post Office Building .\n#### 1. Commodore Dixie Kiefer Memorial Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, shall be known and designated as the Commodore Dixie Kiefer Memorial Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Commodore Dixie Kiefer Memorial Post Office Building .",
      "versionDate": "2025-11-07",
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
        "updateDate": "2025-12-08T15:56:06Z"
      }
    }
  ]
}
```

## API Data: summaries

```json
{
  "govinfoBulk": {
    "introducedDate": "2025-11-07",
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
          "measure-id": "id119hr5947",
          "measure-number": "5947",
          "measure-type": "hr",
          "orig-publish-date": "2025-11-07",
          "originChamber": "HOUSE",
          "update-date": "2025-11-11"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5947v00",
            "update-date": "2025-11-11"
          },
          "action-date": "2025-11-07",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5947.xml",
    "summary": {
      "actionDate": "2025-11-07",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\".",
      "updateDate": "2025-11-11",
      "versionCode": "id119hr5947"
    },
    "title": "To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-11-07",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\".",
      "updateDate": "2025-11-11",
      "versionCode": "id119hr5947"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-11-07",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5947ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-11T07:04:29Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 1201 Calvert Street in Lincoln, Nebraska, as the \"Commodore Dixie Kiefer Memorial Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-08T09:05:49Z"
    }
  ]
}
```
