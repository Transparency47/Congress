# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5717?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5717
- Title: To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the "Mildred Joyce Coleman Crump Post Office Building".
- Congress: 119
- Bill type: HR
- Bill number: 5717
- Origin chamber: House
- Introduced date: 2025-10-08
- Update date: 2025-12-08T19:44:28Z
- Update date including text: 2025-12-08T19:44:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, summaries, text, titles

## Timeline

- 2025-10-08: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held
- Latest action: 2025-10-08: Introduced in House

## Actions

- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Introduced in House
- 2025-10-08 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2025-12-02 - Committee: Committee Consideration and Mark-up Session Held

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5717",
    "number": "5717",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M001229",
        "district": "10",
        "firstName": "LaMonica",
        "fullName": "Rep. McIver, LaMonica [D-NJ-10]",
        "lastName": "McIver",
        "party": "D",
        "state": "NJ"
      }
    ],
    "title": "To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\".",
    "type": "HR",
    "updateDate": "2025-12-08T19:44:28Z",
    "updateDateIncludingText": "2025-12-08T19:44:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-02",
      "committees": {
        "item": {
          "name": "Oversight and Government Reform Committee",
          "systemCode": "hsgo00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-08",
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
        "item": [
          {
            "date": "2025-12-02T17:48:51Z",
            "name": "Markup By"
          },
          {
            "date": "2025-10-08T19:01:15Z",
            "name": "Referred To"
          }
        ]
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
      "bioguideId": "C001136",
      "district": "3",
      "firstName": "Herbert",
      "fullName": "Rep. Conaway, Herbert C. [D-NJ-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Conaway",
      "middleName": "C.",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "W000822",
      "district": "12",
      "firstName": "Bonnie",
      "fullName": "Rep. Watson Coleman, Bonnie [D-NJ-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Watson Coleman",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "K000398",
      "district": "7",
      "firstName": "Thomas",
      "fullName": "Rep. Kean, Thomas H. [R-NJ-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Kean",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "M001226",
      "district": "8",
      "firstName": "Robert",
      "fullName": "Rep. Menendez, Robert [D-NJ-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Menendez",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "N000188",
      "district": "1",
      "firstName": "Donald",
      "fullName": "Rep. Norcross, Donald [D-NJ-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Norcross",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "P000034",
      "district": "6",
      "firstName": "Frank",
      "fullName": "Rep. Pallone, Frank [D-NJ-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Pallone",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "P000621",
      "district": "9",
      "firstName": "Nellie",
      "fullName": "Rep. Pou, Nellie [D-NJ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Pou",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "S001207",
      "district": "11",
      "firstName": "Mikie",
      "fullName": "Rep. Sherrill, Mikie [D-NJ-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Sherrill",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "S000522",
      "district": "4",
      "firstName": "Christopher",
      "fullName": "Rep. Smith, Christopher H. [R-NJ-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Smith",
      "middleName": "H.",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-10-08",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5717ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5717\nIN THE HOUSE OF REPRESENTATIVES\nOctober 8, 2025 Mrs. McIver (for herself, Mr. Conaway , Mrs. Watson Coleman , Mr. Gottheimer , Mr. Kean , Mr. Menendez , Mr. Norcross , Mr. Pallone , Ms. Pou , Ms. Sherrill , Mr. Smith of New Jersey , and Mr. Van Drew ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the Mildred Joyce Coleman Crump Post Office Building .\n#### 1. Mildred Joyce Coleman Crump Post Office Building\n##### (a) Designation\nThe facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, shall be known and designated as the Mildred Joyce Coleman Crump Post Office Building .\n##### (b) References\nAny reference in a law, map, regulation, document, paper, or other record of the United States to the facility referred to in subsection (a) shall be deemed to be a reference to the Mildred Joyce Coleman Crump Post Office Building .",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Congressional tributes",
            "updateDate": "2025-12-08T19:44:24Z"
          },
          {
            "name": "Government buildings, facilities, and property",
            "updateDate": "2025-12-08T19:44:24Z"
          },
          {
            "name": "New Jersey",
            "updateDate": "2025-12-08T19:44:28Z"
          },
          {
            "name": "Postal service",
            "updateDate": "2025-12-08T19:44:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-12-08T15:54:28Z"
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
          "measure-id": "id119hr5717",
          "measure-number": "5717",
          "measure-type": "hr",
          "orig-publish-date": "2025-10-08",
          "originChamber": "HOUSE",
          "update-date": "2025-10-16"
        },
        "summary": {
          "@attributes": {
            "currentChamber": "HOUSE",
            "summary-id": "id119hr5717v00",
            "update-date": "2025-10-16"
          },
          "action-date": "2025-10-08",
          "action-desc": "Introduced in House",
          "summary-text": "This bill designates the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\"."
        },
        "title": "To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\"."
      }
    },
    "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLSUM/119/hr/BILLSUM-119hr5717.xml",
    "summary": {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\".",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5717"
    },
    "title": "To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\"."
  },
  "summaries": [
    {
      "actionDate": "2025-10-08",
      "actionDesc": "Introduced in House",
      "text": "This bill designates the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\".",
      "updateDate": "2025-10-16",
      "versionCode": "id119hr5717"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5717ih.xml"
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
      "title": "To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-16T02:48:24Z"
    },
    {
      "title": "To designate the facility of the United States Postal Service located at 514 Frelinghuysen Avenue in Newark, New Jersey, as the \"Mildred Joyce Coleman Crump Post Office Building\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-09T08:05:42Z"
    }
  ]
}
```
