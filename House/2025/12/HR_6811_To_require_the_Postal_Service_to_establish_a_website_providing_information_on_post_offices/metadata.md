# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6811?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6811
- Title: Postal Suspension Transparency Act
- Congress: 119
- Bill type: HR
- Bill number: 6811
- Origin chamber: House
- Introduced date: 2025-12-17
- Update date: 2026-05-01T08:08:46Z
- Update date including text: 2026-05-01T08:08:46Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-12-17: Introduced in House

## Actions

- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Introduced in House
- 2025-12-17 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6811",
    "number": "6811",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "P000614",
        "district": "1",
        "firstName": "Chris",
        "fullName": "Rep. Pappas, Chris [D-NH-1]",
        "lastName": "Pappas",
        "party": "D",
        "state": "NH"
      }
    ],
    "title": "Postal Suspension Transparency Act",
    "type": "HR",
    "updateDate": "2026-05-01T08:08:46Z",
    "updateDateIncludingText": "2026-05-01T08:08:46Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-17",
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
      "actionDate": "2025-12-17",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T14:02:30Z",
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
      "bioguideId": "B001301",
      "district": "1",
      "firstName": "Jack",
      "fullName": "Rep. Bergman, Jack [R-MI-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Bergman",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "MI"
    },
    {
      "bioguideId": "B001315",
      "district": "13",
      "firstName": "Nikki",
      "fullName": "Rep. Budzinski, Nikki [D-IL-13]",
      "isOriginalCosponsor": "True",
      "lastName": "Budzinski",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "IL"
    },
    {
      "bioguideId": "G000597",
      "district": "2",
      "firstName": "Andrew",
      "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Garbarino",
      "middleName": "R.",
      "party": "R",
      "sponsorshipDate": "2025-12-17",
      "state": "NY"
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
      "sponsorshipDate": "2025-12-23",
      "state": "PA"
    },
    {
      "bioguideId": "C001119",
      "district": "2",
      "firstName": "Angie",
      "fullName": "Rep. Craig, Angie [D-MN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Craig",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
      "state": "MN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6811ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6811\nIN THE HOUSE OF REPRESENTATIVES\nDecember 17, 2025 Mr. Pappas (for himself, Mr. Bergman , Ms. Budzinski , and Mr. Garbarino ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo require the Postal Service to establish a website providing information on post offices experiencing emergency suspensions, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Postal Suspension Transparency Act .\n#### 2. Post office emergency suspension website\n##### (a) In general\nSubchapter VII of chapter 36 of title 39, United States Code, is amended by adding at the end the following new section:\n3693. Post office emergency suspension website (a) In general The Postal Service shall develop and maintain a publicly available website with an interactive web-tool that provides information about each covered post office, including the information described in subsection (b). (b) Emergency suspension information The information provided on the website shall include\u2014 (1) a list of each covered post office; and (2) for each covered post office\u2014 (A) a street address; (B) the date on which the relevant emergency suspension for such covered post office took effect; (C) the reason for such emergency suspension; (D) alternative services available, including how to request curbside delivery; (E) the location of, and hours of operation for, the nearest facility providing retail access to postal services; and (F) to the extent practicable, the estimated date on which operations at such covered post office will resume. (c) Address search functionality The website shall include functionality enabling a user to search for information about covered post offices by street address, ZIP Code, or post office box. (d) Format The information described in subsection (a) shall be provided on the website\u2014 (1) in a manner that\u2014 (A) presents such information on an interactive dashboard; (B) is searchable and may be sorted and filtered by the elements described in subsection (b)(2); and (C) to the extent practicable, enables any person or entity to download in bulk\u2014 (i) such information; and (ii) the results of a search by the elements described in subsection (b)(2); (2) in an open format that permits any individual or entity to reuse and analyze such information; and (3) in a structured data format, to the extent practicable. (e) Suspension notice Information provided on the website shall not be considered as providing notice to any person that the operations of a post office have been temporarily suspended pursuant to subchapter 61 of the Postal Service Handbook PO\u2013101, or any successor policy. (f) Definitions In this section: (1) Covered post office The term covered post office means a post office at which operations have been temporarily suspended pursuant to subchapter 61 of the Postal Service Handbook PO\u2013101, or any successor policy. (2) Emergency suspension The term emergency suspension means the temporary suspension of operations at a post office pursuant to subchapter 61 of the Postal Service Handbook PO\u2013101, or any successor policy. (3) Post office The term post office means a Post Office, as such term is defined in section 241.1 of title 39, Code of Federal Regulations, or any successor regulation, and includes a post office branch or post office station. (4) Website The term Website means the website described in subsection (a). .\n##### (b) Implementation deadline\nNot later than one year after the date of the enactment of this Act, the Postal Service shall establish the website required under section 3693(a) of title 39, United States Code, as added by this Act.\n##### (c) Clerical amendment\nThe table of sections for chapter 36 of title 39, United States Code, is amended by inserting after the item relating to section 3692 the following new item:\n3693. Post office emergency suspension website. .",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-21T16:34:34Z"
      }
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6811ih.xml"
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
      "title": "Postal Suspension Transparency Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-21T05:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Postal Suspension Transparency Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-21T05:23:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Postal Service to establish a website providing information on post offices experiencing emergency suspensions, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-21T05:18:26Z"
    }
  ]
}
```
