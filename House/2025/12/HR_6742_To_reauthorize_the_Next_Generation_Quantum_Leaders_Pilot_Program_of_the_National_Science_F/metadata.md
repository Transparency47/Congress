# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6742?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6742
- Title: Q–LEAP
- Congress: 119
- Bill type: HR
- Bill number: 6742
- Origin chamber: House
- Introduced date: 2025-12-16
- Update date: 2026-01-31T09:05:48Z
- Update date including text: 2026-01-31T09:05:48Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-16: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.
- Latest action: 2025-12-16: Introduced in House

## Actions

- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Introduced in House
- 2025-12-16 - IntroReferral: Referred to the House Committee on Science, Space, and Technology.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-16",
    "latestAction": {
      "actionDate": "2025-12-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6742",
    "number": "6742",
    "originChamber": "House",
    "policyArea": {
      "name": "Science, Technology, Communications"
    },
    "sponsors": [
      {
        "bioguideId": "F000477",
        "district": "4",
        "firstName": "Valerie",
        "fullName": "Rep. Foushee, Valerie P. [D-NC-4]",
        "lastName": "Foushee",
        "party": "D",
        "state": "NC"
      }
    ],
    "title": "Q\u2013LEAP",
    "type": "HR",
    "updateDate": "2026-01-31T09:05:48Z",
    "updateDateIncludingText": "2026-01-31T09:05:48Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Science, Space, and Technology.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-16",
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
          "date": "2025-12-16T15:02:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
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
      "bioguideId": "O000019",
      "district": "23",
      "firstName": "Jay",
      "fullName": "Rep. Obernolte, Jay [R-CA-23]",
      "isOriginalCosponsor": "True",
      "lastName": "Obernolte",
      "party": "R",
      "sponsorshipDate": "2025-12-16",
      "state": "CA"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-01-30",
      "state": "DE"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6742ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6742\nIN THE HOUSE OF REPRESENTATIVES\nDecember 16, 2025 Mrs. Foushee (for herself and Mr. Obernolte ) introduced the following bill; which was referred to the Committee on Science, Space, and Technology\nA BILL\nTo reauthorize the Next Generation Quantum Leaders Pilot Program of the National Science Foundation for the education and training of the next generation of students and teachers in the fundamental principles of quantum mechanics, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Quantum Leaders Education and Advancement Program Act or the Q\u2013LEAP .\n#### 2. Reauthorization of Next Generation Quantum Leaders Pilot Program of the National Science Foundation\nParagraph (5) of section 10661(f) of the Research and Development, Competition, and Innovation Act ( Public Law 117\u2013167 ; relating to the Next Generation Quantum Leaders Pilot Program of the National Science Foundation for the education and training of the next generation of students and teachers in the fundamental principles of quantum mechanics) is amended by striking 2026 and inserting 2028 .",
      "versionDate": "2025-12-16",
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
        "name": "Science, Technology, Communications",
        "updateDate": "2026-01-12T16:55:12Z"
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
      "date": "2025-12-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6742ih.xml"
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
      "title": "Q\u2013LEAP",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T10:53:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Q\u2013LEAP",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Quantum Leaders Education and Advancement Program Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T10:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize the Next Generation Quantum Leaders Pilot Program of the National Science Foundation for the education and training of the next generation of students and teachers in the fundamental principles of quantum mechanics, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T10:48:26Z"
    }
  ]
}
```
