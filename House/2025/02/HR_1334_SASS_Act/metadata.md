# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1334?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/hr/1334
- Title: SASS Act
- Congress: 119
- Bill type: HR
- Bill number: 1334
- Origin chamber: House
- Introduced date: 2025-02-13
- Update date: 2025-07-08T12:36:43Z
- Update date including text: 2025-07-08T12:36:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-02-13: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.
- Latest action: 2025-02-13: Introduced in House

## Actions

- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Introduced in House
- 2025-02-13 - IntroReferral: Referred to the House Committee on the Judiciary.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-13",
    "latestAction": {
      "actionDate": "2025-02-13",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/hr/1334",
    "number": "1334",
    "originChamber": "House",
    "policyArea": {
      "name": "Crime and Law Enforcement"
    },
    "sponsors": [
      {
        "bioguideId": "M001217",
        "district": "23",
        "firstName": "Jared",
        "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
        "lastName": "Moskowitz",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "SASS Act",
    "type": "HR",
    "updateDate": "2025-07-08T12:36:43Z",
    "updateDateIncludingText": "2025-07-08T12:36:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-13",
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
      "actionDate": "2025-02-13",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-13",
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
          "date": "2025-02-13T14:03:30Z",
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
      "bioguideId": "D000600",
      "district": "26",
      "firstName": "Mario",
      "fullName": "Rep. Diaz-Balart, Mario [R-FL-26]",
      "isOriginalCosponsor": "True",
      "lastName": "Diaz-Balart",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "C001127",
      "district": "20",
      "firstName": "Sheila",
      "fullName": "Rep. Cherfilus-McCormick, Sheila [D-FL-20]",
      "isOriginalCosponsor": "True",
      "lastName": "Cherfilus-McCormick",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "FL"
    },
    {
      "bioguideId": "G000594",
      "district": "23",
      "firstName": "Tony",
      "fullName": "Rep. Gonzales, Tony [R-TX-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Gonzales",
      "party": "R",
      "sponsorshipDate": "2025-02-13",
      "state": "TX"
    },
    {
      "bioguideId": "N000193",
      "district": "3",
      "firstName": "Zachary",
      "fullName": "Rep. Nunn, Zachary [R-IA-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Nunn",
      "party": "R",
      "sponsorshipDate": "2025-04-08",
      "state": "IA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1334ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1334\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 13, 2025 Mr. Moskowitz (for himself, Mr. Diaz-Balart , Mrs. Cherfilus-McCormick , and Mr. Tony Gonzales of Texas ) introduced the following bill; which was referred to the Committee on the Judiciary\nA BILL\nTo permit a single application to be submitted to the COPS Director or BJA Director for the matching grant program for school security.\n#### 1. Short title\nThis Act may be cited as the Single Application for School Safety Act or the SASS Act .\n#### 2. Matching grant program for school security application requirement\nSection 2702 of the Omnibus Crime Control and Safe Streets Act of 1968 ( 34 U.S.C. 10552 ) is amended by adding at the end the following:\n(c) Multipurpose applications The Attorney General shall establish a process under which a single grant application may be submitted for a grant that is authorized to be made by the COPS Director under paragraph (1) of section 2701(a) and the BJA Director under paragraph (2) of such section. (d) Technical assistance The COPS Director or the BJA Director, as the case may be, shall provide technical assistance to applicants to complete an application for a grant under this part. .",
      "versionDate": "2025-02-13",
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
            "name": "Education programs funding",
            "updateDate": "2025-07-08T12:36:27Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2025-07-08T12:36:43Z"
          },
          {
            "name": "Law enforcement administration and funding",
            "updateDate": "2025-07-08T12:36:38Z"
          },
          {
            "name": "School administration",
            "updateDate": "2025-07-08T12:36:08Z"
          }
        ]
      },
      "policyArea": {
        "name": "Crime and Law Enforcement",
        "updateDate": "2025-03-14T12:43:53Z"
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
      "date": "2025-02-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1334ih.xml"
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
      "title": "SASS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-13T04:23:36Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "SASS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Single Application for School Safety Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-13T04:23:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To permit a single application to be submitted to the COPS Director or BJA Director for the matching grant program for school security.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-13T04:20:35Z"
    }
  ]
}
```
