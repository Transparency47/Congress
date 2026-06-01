# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5295?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5295
- Title: ACCESS Act
- Congress: 119
- Bill type: HR
- Bill number: 5295
- Origin chamber: House
- Introduced date: 2025-09-11
- Update date: 2025-10-18T08:05:24Z
- Update date including text: 2025-10-18T08:05:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-11: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Education and Workforce.
- Latest action: 2025-09-11: Introduced in House

## Actions

- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Introduced in House
- 2025-09-11 - IntroReferral: Referred to the House Committee on Education and Workforce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-11",
    "latestAction": {
      "actionDate": "2025-09-11",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5295",
    "number": "5295",
    "originChamber": "House",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "B001278",
        "district": "1",
        "firstName": "Suzanne",
        "fullName": "Rep. Bonamici, Suzanne [D-OR-1]",
        "lastName": "Bonamici",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "ACCESS Act",
    "type": "HR",
    "updateDate": "2025-10-18T08:05:24Z",
    "updateDateIncludingText": "2025-10-18T08:05:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-11",
      "committees": {
        "item": {
          "name": "Education and Workforce Committee",
          "systemCode": "hsed00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Education and Workforce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-11",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-11",
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
          "date": "2025-09-11T13:03:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Education and Workforce Committee",
      "systemCode": "hsed00",
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
      "bioguideId": "T000467",
      "district": "15",
      "firstName": "Glenn",
      "fullName": "Rep. Thompson, Glenn [R-PA-15]",
      "isOriginalCosponsor": "True",
      "lastName": "Thompson",
      "party": "R",
      "sponsorshipDate": "2025-09-11",
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
      "sponsorshipDate": "2025-10-17",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5295ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5295\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 11, 2025 Ms. Bonamici (for herself and Mr. Thompson of Pennsylvania ) introduced the following bill; which was referred to the Committee on Education and Workforce\nA BILL\nTo amend the Workforce Innovation and Opportunity Act to raise public awareness for skilled trade programs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Access to Career Counseling for Every Secondary Student Act or the ACCESS Act .\n#### 2. Career counseling and public awareness for skilled trade programs\n##### (a) Statewide activities\nSection 129(b)(2) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3164(b)(2) ) is amended by redesignating subparagraphs (D) and (E) as subparagraphs (E) and (F), respectively, and inserting after subparagraph (C) the following:\n(D) carrying out public awareness campaigns and public service announcements, including social media campaigns and other forms of media, about career and technical education programs and programs provided by community-based organizations that prepare eligible youth for high-skill, high-wage, or in-demand industry sectors or occupations in current or emerging professions (including skilled trades); ;\n##### (b) Local elements and requirements\nSection 129(c)(2)(M) of the Workforce Innovation and Opportunity Act ( 29 U.S.C. 3164(c)(2)(M) ) is amended to read as follows:\n(M) services and opportunities that provide labor market and employment information about high-skill, high-wage, or in-demand industry sectors or occupations in current or emerging professions (including skilled trades) available in the local area, such as career awareness, career counseling, and career exploration services; and .",
      "versionDate": "2025-09-11",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-24T14:41:04Z"
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
      "date": "2025-09-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5295ih.xml"
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
      "title": "ACCESS Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T02:53:14Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ACCESS Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Access to Career Counseling for Every Secondary Student Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Workforce Innovation and Opportunity Act to raise public awareness for skilled trade programs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:18Z"
    }
  ]
}
```
