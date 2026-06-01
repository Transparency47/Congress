# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/932?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/932
- Title: Protecting VA Employees Act
- Congress: 119
- Bill type: HR
- Bill number: 932
- Origin chamber: House
- Introduced date: 2025-02-04
- Update date: 2026-01-12T19:43:54Z
- Update date including text: 2026-01-12T19:43:54Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-04: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- Latest action: 2025-02-04: Introduced in House

## Actions

- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Introduced in House
- 2025-02-04 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-02-04 - IntroReferral: Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-03-06 - Committee: Referred to the Subcommittee on Oversight and Investigations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-04",
    "latestAction": {
      "actionDate": "2025-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/932",
    "number": "932",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "F000466",
        "district": "1",
        "firstName": "Brian",
        "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
        "lastName": "Fitzpatrick",
        "party": "R",
        "state": "PA"
      }
    ],
    "title": "Protecting VA Employees Act",
    "type": "HR",
    "updateDate": "2026-01-12T19:43:54Z",
    "updateDateIncludingText": "2026-01-12T19:43:54Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-06",
      "committees": {
        "item": {
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Oversight and Investigations.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
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
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-02-04",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the Committee on Veterans' Affairs, and in addition to the Committee on Oversight and Government Reform, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-02-04",
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
          "date": "2025-02-04T17:06:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-03-06T22:42:57Z",
              "name": "Referred to"
            }
          },
          "name": "Oversight and Investigations Subcommittee",
          "systemCode": "hsvr08"
        }
      },
      "systemCode": "hsvr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-02-04T17:06:20Z",
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
      "bioguideId": "D000530",
      "district": "17",
      "firstName": "Christopher",
      "fullName": "Rep. Deluzio, Christopher R. [D-PA-17]",
      "isOriginalCosponsor": "True",
      "lastName": "Deluzio",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-02-04",
      "state": "PA"
    },
    {
      "bioguideId": "H001094",
      "district": "4",
      "firstName": "Val",
      "fullName": "Rep. Hoyle, Val T. [D-OR-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Hoyle",
      "middleName": "T.",
      "party": "D",
      "sponsorshipDate": "2025-02-11",
      "state": "OR"
    },
    {
      "bioguideId": "S001226",
      "district": "6",
      "firstName": "Andrea",
      "fullName": "Rep. Salinas, Andrea [D-OR-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Salinas",
      "party": "D",
      "sponsorshipDate": "2025-02-13",
      "state": "OR"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-08-01",
      "state": "CO"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr932ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 932\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2025 Mr. Fitzpatrick (for himself and Mr. Deluzio ) introduced the following bill; which was referred to the Committee on Veterans' Affairs , and in addition to the Committee on Oversight and Government Reform , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend titles 38 and 5, United States Code, to ensure that certain employees of the Department of Veterans Affairs are subject to the same removal, demotion, and suspension policies as other employees of the Federal Government, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Protecting VA Employees Act .\n#### 2. Repeal of separate removal, demotion, and suspension processes for certain employees of Department of Veterans Affairs\n##### (a) Repeal\n**(1) Title 38**\nSection 714 of title 38, United States Code, is amended\u2014\n**(A)**\nby striking subsections (a), (b), (c), (d), and (g);\n**(B)**\nby redesignating subsections (e), (f), and (h) as subsections (a), (b), and (c), respectively;\n**(C)**\nin subsection (a), as so redesignated, by striking under subsection (a) each place it appears; and\n**(D)**\nin subsection (c), as so redesignated\u2014\n**(i)**\nby striking paragraphs (3) and (4); and\n**(ii)**\nby redesignating paragraphs (5) and (6) as paragraphs (3) and (4), respectively.\n**(2) Title 5**\nSection 4303(f) of title 5, United States Code, is amended\u2014\n**(A)**\nin paragraph (2), by striking the comma at the end and inserting , or ;\n**(B)**\nin paragraph (3), by striking , or and inserting a period; and\n**(C)**\nby striking paragraph (4).\n##### (b) Conforming amendments\nChapter 7 of title 38, United States Code, is amended\u2014\n**(1)**\nin section 719, by striking under section 713, 714, or 7461 of this title each place it appears and inserting under section 713 or 7461 of this title ;\n**(2)**\nin section 714, as amended by subsection (a), by striking the section heading and inserting Protections for whistleblowers from removal, demotion, and suspension ;\n**(3)**\nby redesignating section 714 as section 734;\n**(4)**\nby transferring section 734, as so redesignated, so as to appear after section 733; and\n**(5)**\nin the table of sections\u2014\n**(A)**\nby striking the item relating to section 714; and\n**(B)**\nby inserting after the item relating to section 733 the following new item:\n734. Protections for whistleblowers from removal, demotion, and suspension. .\n#### 3. Restoration of certain disciplinary and grievance procedures for personnel of the Veterans Health Administration\nThe following provisions of title 38, United States Code, are each amended to read as such provisions read on the day before the date of the enactment of the Department of Veterans Affairs Accountability and Whistleblower Protection Act of 2017 ( Public Law 115\u201341 ):\n**(1)**\nSection 7461(b).\n**(2)**\nSection 7462(b).\n**(3)**\nSection 7463(c).",
      "versionDate": "2025-02-04",
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
        "actionDate": "2025-12-11",
        "text": "Referred to the Committee on Ways and Means, and in addition to the Committees on Energy and Commerce, Natural Resources, Education and Workforce, Transportation and Infrastructure, Science, Space, and Technology, Agriculture, Appropriations, Armed Services, the Budget, Rules, Ethics, Financial Services, Foreign Affairs, Homeland Security, House Administration, the Judiciary, Intelligence (Permanent Select), Oversight and Government Reform, Small Business, and Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned."
      },
      "number": "6637",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "To advance bipartisan priorities.",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Employee performance",
            "updateDate": "2025-04-11T14:59:42Z"
          },
          {
            "name": "Employment discrimination and employee rights",
            "updateDate": "2025-04-11T14:59:42Z"
          },
          {
            "name": "Personnel records",
            "updateDate": "2025-04-11T14:59:42Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-03-19T14:53:08Z"
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
      "date": "2025-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr932ih.xml"
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
      "title": "Protecting VA Employees Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-04T12:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Protecting VA Employees Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-04T12:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend titles 38 and 5, United States Code, to ensure that certain employees of the Department of Veterans Affairs are subject to the same removal, demotion, and suspension policies as other employees of the Federal Government, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-04T12:48:23Z"
    }
  ]
}
```
