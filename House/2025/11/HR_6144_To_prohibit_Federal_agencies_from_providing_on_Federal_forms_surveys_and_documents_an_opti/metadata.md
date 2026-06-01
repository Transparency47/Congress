# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6144?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6144
- Title: Male or Female Only Act
- Congress: 119
- Bill type: HR
- Bill number: 6144
- Origin chamber: House
- Introduced date: 2025-11-19
- Update date: 2025-12-09T21:11:42Z
- Update date including text: 2025-12-09T21:11:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-19: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- Latest action: 2025-11-19: Introduced in House

## Actions

- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Introduced in House
- 2025-11-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-19",
    "latestAction": {
      "actionDate": "2025-11-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6144",
    "number": "6144",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "J000304",
        "district": "13",
        "firstName": "Ronny",
        "fullName": "Rep. Jackson, Ronny [R-TX-13]",
        "lastName": "Jackson",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "Male or Female Only Act",
    "type": "HR",
    "updateDate": "2025-12-09T21:11:42Z",
    "updateDateIncludingText": "2025-12-09T21:11:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-19",
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
      "actionDate": "2025-11-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-19",
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
          "date": "2025-11-19T15:00:35Z",
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
      "bioguideId": "B001325",
      "district": "3",
      "firstName": "Sheri",
      "fullName": "Rep. Biggs, Sheri [R-SC-3]",
      "isOriginalCosponsor": "True",
      "lastName": "Biggs",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "SC"
    },
    {
      "bioguideId": "M001212",
      "district": "1",
      "firstName": "Barry",
      "fullName": "Rep. Moore, Barry [R-AL-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AL"
    },
    {
      "bioguideId": "G000565",
      "district": "9",
      "firstName": "Paul",
      "fullName": "Rep. Gosar, Paul A. [R-AZ-9]",
      "isOriginalCosponsor": "True",
      "lastName": "Gosar",
      "middleName": "A.",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AZ"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6144ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6144\nIN THE HOUSE OF REPRESENTATIVES\nNovember 19, 2025 Mr. Jackson of Texas (for himself, Mrs. Biggs of South Carolina , Mr. Moore of Alabama , Mr. Gosar , and Mrs. Harshbarger ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo prohibit Federal agencies from providing on Federal forms, surveys, and documents, an option other than Male or Female to reference the sex of an individual, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Male or Female Only Act .\n#### 2. No option other than Male or Female to reference the sex of an individual\n##### (a) Prohibition\nWith respect to any collection of information conducted by the head of any agency through a form, survey, or other document, the head of such agency\u2014\n**(1)**\nmay not\u2014\n**(A)**\nsolicit or obtain any information regarding the gender or gender identity of an individual; and\n**(B)**\nwith respect to any such collection information regarding the sex of an individual, provide an option to select or mark on the form, survey, or document that sex of an individual is something other than male or female; and\n**(2)**\nshall reject\u2014\n**(A)**\nany response provided by the person from whom the information is being collected stating the gender or gender identity of an individual; and\n**(B)**\nany response provided by the person from whom the information is being collected stating that the sex of an individual is something other than male or female.\n##### (b) Update\nNot later than 60 days after the date of the enactment of this Act, the head of an agency of the Federal Government shall update the forms, surveys, and documents of the agency as necessary to ensure such forms, surveys, and documents comply with the prohibition under subsection (a).",
      "versionDate": "2025-11-19",
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
        "updateDate": "2025-12-09T21:11:42Z"
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
      "date": "2025-11-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6144ih.xml"
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
      "title": "Male or Female Only Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Male or Female Only Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T11:08:39Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit Federal agencies from providing on Federal forms, surveys, and documents, an option other than Male or Female to reference the sex of an individual, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T11:03:25Z"
    }
  ]
}
```
