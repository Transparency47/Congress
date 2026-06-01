# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/1980?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/1980
- Title: State Strategic Stockpile Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 1980
- Origin chamber: House
- Introduced date: 2025-03-10
- Update date: 2025-09-02T19:57:43Z
- Update date including text: 2025-09-02T19:57:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-10: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- Latest action: 2025-03-10: Introduced in House

## Actions

- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Introduced in House
- 2025-03-10 - IntroReferral: Referred to the House Committee on Energy and Commerce.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-10",
    "latestAction": {
      "actionDate": "2025-03-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/1980",
    "number": "1980",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "C001103",
        "district": "1",
        "firstName": "Earl",
        "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
        "lastName": "Carter",
        "party": "R",
        "state": "GA"
      }
    ],
    "title": "State Strategic Stockpile Act of 2025",
    "type": "HR",
    "updateDate": "2025-09-02T19:57:43Z",
    "updateDateIncludingText": "2025-09-02T19:57:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-03-10",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Energy and Commerce.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-03-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-03-10",
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
          "date": "2025-03-10T16:07:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "systemCode": "hsif00",
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
      "bioguideId": "V000131",
      "district": "33",
      "firstName": "Marc",
      "fullName": "Rep. Veasey, Marc A. [D-TX-33]",
      "isOriginalCosponsor": "True",
      "lastName": "Veasey",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "TX"
    },
    {
      "bioguideId": "M001215",
      "district": "1",
      "firstName": "Mariannette",
      "fullName": "Rep. Miller-Meeks, Mariannette [R-IA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Miller-Meeks",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
      "state": "IA"
    },
    {
      "bioguideId": "H001085",
      "district": "6",
      "firstName": "Chrissy",
      "fullName": "Rep. Houlahan, Chrissy [D-PA-6]",
      "isOriginalCosponsor": "True",
      "lastName": "Houlahan",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "PA"
    },
    {
      "bioguideId": "M001230",
      "district": "7",
      "firstName": "Ryan",
      "fullName": "Rep. Mackenzie, Ryan [R-PA-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Mackenzie",
      "party": "R",
      "sponsorshipDate": "2025-03-10",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1980ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 1980\nIN THE HOUSE OF REPRESENTATIVES\nMarch 10, 2025 Mr. Carter of Georgia (for himself, Mr. Veasey , Mrs. Miller-Meeks , Ms. Houlahan , and Mr. Mackenzie ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo reauthorize and make improvements to the State medical stockpile pilot program administered by the Office of the Assistant Secretary for Preparedness and Response through fiscal year 2030.\n#### 1. Short title\nThis Act may be cited as the State Strategic Stockpile Act of 2025 .\n#### 2. Reauthorization of pilot program to support State medical stockpiles\n##### (a) In general\nSection 319F\u20132(i) of the Public Health Service Act (42 U.S.C. 247d\u20136b(i)) is amended\u2014\n**(1)**\nin paragraph (2)(B)(i)\u2014\n**(A)**\nin subclause (I), by striking and 2024 and inserting through 2025 ; and\n**(B)**\nin subclause (II), by striking 2025 and inserting 2026 ;\n**(2)**\nin paragraph (4)\u2014\n**(A)**\nin subparagraph (G), by striking ; and at the end and inserting a semicolon;\n**(B)**\nby redesignating subparagraph (H) as subparagraph (I);\n**(C)**\nby inserting after subparagraph (G) the following:\n(H) facilitate the sharing of best practices among States within a consortia of States in receipt of funding related to establishing and maintaining a stockpile of medical products; and ; and\n**(D)**\nin subparagraph (I), as so redesignated, by striking State efforts and inserting State or regional efforts ;\n**(3)**\nby redesignating paragraphs (5) through (9) as paragraphs (6) through (10), respectively;\n**(4)**\nby inserting after paragraph (4) the following:\n(5) Coordination An entity in receipt of an award under paragraph (1), in carrying out the activities under this subsection, shall coordinate with appropriate health care entities, health officials, and emergency management officials within the jurisdiction of such State or States. ; and\n**(5)**\nin paragraph (10), as so redesignated, by striking fiscal years 2023 and 2024 and inserting fiscal years 2026 through 2030 .\n##### (b) GAO report\nSection 2409(b) of the PREVENT Pandemics Act ( Public Law 117\u2013328 ) is amended\u2014\n**(1)**\nin paragraph (2), by striking ; and and inserting a semicolon;\n**(2)**\nin paragraph (3), by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(4) the impact of any regional stockpiling approaches carried out under subsection (i)(1) of section 319F\u20132 of the Public Health Service Act ( 42 U.S.C. 247d\u20136b ). .",
      "versionDate": "2025-03-10",
      "versionType": "Introduced in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-06",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "891",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Bipartisan Health Care Act",
      "type": "S"
    },
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-03-03",
        "text": "Referred to the Committee on Energy and Commerce, and in addition to the Committees on Ways and Means, the Budget, the Judiciary, and Education and Workforce, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "1768",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Lower Costs for Everyday Americans Act",
      "type": "HR"
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
        "name": "Health",
        "updateDate": "2025-03-25T14:26:44Z"
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
      "date": "2025-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr1980ih.xml"
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
      "title": "State Strategic Stockpile Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-24T13:23:22Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "State Strategic Stockpile Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-24T13:23:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To reauthorize and make improvements to the State medical stockpile pilot program administered by the Office of the Assistant Secretary for Preparedness and Response through fiscal year 2030.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-24T13:18:22Z"
    }
  ]
}
```
