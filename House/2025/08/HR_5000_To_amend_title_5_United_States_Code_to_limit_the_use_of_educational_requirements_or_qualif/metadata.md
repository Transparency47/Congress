# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5000?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5000
- Title: Cybersecurity Hiring Modernization Act
- Congress: 119
- Bill type: HR
- Bill number: 5000
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2026-03-19T20:05:20Z
- Update date including text: 2026-03-19T20:05:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Oversight and Government Reform.
- 2026-02-04 - Committee: Committee Consideration and Mark-up Session Held
- 2026-02-04 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-08-19",
    "latestAction": {
      "actionDate": "2025-08-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5000",
    "number": "5000",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "M000194",
        "district": "1",
        "firstName": "Nancy",
        "fullName": "Rep. Mace, Nancy [R-SC-1]",
        "lastName": "Mace",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "Cybersecurity Hiring Modernization Act",
    "type": "HR",
    "updateDate": "2026-03-19T20:05:20Z",
    "updateDateIncludingText": "2026-03-19T20:05:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-04",
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
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 44 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-02-04",
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
      "actionDate": "2025-08-19",
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
      "actionDate": "2025-08-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-08-19",
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
            "date": "2026-02-04T14:56:47Z",
            "name": "Markup By"
          },
          {
            "date": "2025-08-19T14:02:00Z",
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
      "bioguideId": "B001313",
      "district": "11",
      "firstName": "Shontel",
      "fullName": "Rep. Brown, Shontel M. [D-OH-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Brown",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "OH"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5000ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5000\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Ms. Mace (for herself and Ms. Brown ) introduced the following bill; which was referred to the Committee on Oversight and Government Reform\nA BILL\nTo amend title 5, United States Code, to limit the use of educational requirements or qualifications in evaluating candidates for certain cybersecurity positions in the competitive service, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Cybersecurity Hiring Modernization Act .\n#### 2. Educational requirements for competitive service cybersecurity positions\nSection 3308 of title 5, United States Code, is amended\u2014\n**(1)**\nby striking The Office of Personnel Management and inserting (a) In general.\u2014 Consistent with subsection (b), the Office of Personnel Management ; and\n**(2)**\nby adding at the end the following:\n(b) Education requirements for cybersecurity positions (1) In general With respect to any covered position\u2014 (A) an agency may prescribe a minimum educational requirement for employment in such a position only if a minimum education qualification is required by law to perform the duties of the position in the State or locality where the duties of the position are to be performed; and (B) an agency may consider education in determining a candidate\u2019s satisfaction of any other minimum qualification only if the candidate\u2019s education directly reflects the competencies necessary to satisfy that qualification and perform the duties of the position. (2) Publication Not later than one year after the date of the enactment of the Cybersecurity Hiring Modernization Act and annually thereafter, the Office of Personnel Management shall publish on the Office\u2019s website\u2014 (A) any changes made to minimum qualifications standards concerning education for covered positions; and (B) aggregate data indicating the level of educational attainment, sorted by position classification, of all accessions to covered positions. (3) Covered position defined In this subsection, the term covered position means\u2014 (A) any position in the competitive service classified under the GS\u20132210 information technology management series, or any successor series; and (B) any other position in the competitive service designated as cybersecurity under the National Initiative for Cybersecurity Education (NICE) Cybersecurity Workforce Framework (NIST Special Publication 800\u2013181), or successor framework. .",
      "versionDate": "2025-08-19",
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
            "name": "Computer security and identity theft",
            "updateDate": "2026-03-16T16:50:21Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-16T16:50:21Z"
          },
          {
            "name": "Employee hiring",
            "updateDate": "2026-03-16T16:50:21Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2026-03-16T16:50:21Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-16T16:50:21Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-19T15:53:55Z"
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
      "date": "2025-08-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5000ih.xml"
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
      "title": "To amend title 5, United States Code, to limit the use of educational requirements or qualifications in evaluating candidates for certain cybersecurity positions in the competitive service, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-20T09:11:59Z"
    },
    {
      "title": "Cybersecurity Hiring Modernization Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-20T08:23:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Cybersecurity Hiring Modernization Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-20T08:23:16Z"
    }
  ]
}
```
