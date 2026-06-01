# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2984?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2984
- Title: ASTRO Act
- Congress: 119
- Bill type: HR
- Bill number: 2984
- Origin chamber: House
- Introduced date: 2025-04-24
- Update date: 2025-08-28T08:05:38Z
- Update date including text: 2025-08-28T08:05:38Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-24: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.
- Latest action: 2025-04-24: Introduced in House

## Actions

- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Introduced in House
- 2025-04-24 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-24 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2025-04-29 - Committee: Committee Consideration and Mark-up Session Held
- 2025-04-29 - Committee: Ordered to be Reported by Voice Vote.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-24",
    "latestAction": {
      "actionDate": "2025-04-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2984",
    "number": "2984",
    "originChamber": "House",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001291",
        "district": "36",
        "firstName": "Brian",
        "fullName": "Rep. Babin, Brian [R-TX-36]",
        "lastName": "Babin",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "ASTRO Act",
    "type": "HR",
    "updateDate": "2025-08-28T08:05:38Z",
    "updateDateIncludingText": "2025-08-28T08:05:38Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-04-29",
      "committees": {
        "item": {
          "name": "Science, Space, and Technology Committee",
          "systemCode": "hssy00"
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
      "actionDate": "2025-04-24",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-24",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Science, Space, and Technology, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-04-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-24",
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
            "date": "2025-04-29T21:12:16Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-29T15:02:03Z",
            "name": "Markup By"
          },
          {
            "date": "2025-04-24T15:04:20Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Science, Space, and Technology Committee",
      "systemCode": "hssy00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-04-24T15:04:15Z",
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
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "NY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2984ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2984\nIN THE HOUSE OF REPRESENTATIVES\nApril 24, 2025 Mr. Babin introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Science, Space, and Technology , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo amend title 31, United States Code, to authorize transportation of officers and employees of Federal agencies returning from space, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Astronaut Safe Temporary Ride Options Act or the ASTRO Act .\n#### 2. Transportation of astronauts returning from space\n##### (a) In general\nSubsection (b) of section 1344 of title 31, United States Code, is amended\u2014\n**(1)**\nin paragraph (8), by striking and after the semicolon;\n**(2)**\nin paragraph (9), by striking the period and inserting ; and ; and\n**(3)**\nby adding at the end the following new paragraph:\n(10) an officer or employee returning from space when transportation is necessary for the performance of medical research, monitoring, diagnosis, or treatment, or other official duties as approved by the Administrator of the National Aeronautics and Space Administration, prior to such officer or employee receiving post-flight medical clearance to operate a motor vehicle. .\n##### (b) Report\n**(1) In general**\nNot later than one year after the date of the enactment of this Act and annually thereafter, the Administrator of the National Aeronautics and Space Administration shall submit to the Committee on Science, Space, and Technology and the Committee on Oversight and Accountability of the House of Representatives and the Committee on Commerce, Science, and Transportation and the Committee on Homeland Security and Governmental Affairs of the Senate a report on transportation under paragraph (10) of section 1344(b) of title 31, United States Code (as amended by subsection (a)).\n**(2) Contents**\nEach report under paragraph (1) shall include, for the immediately preceding 12 month period, the following:\n**(A)**\nFor each officer or employee of a Federal agency transported, the following:\n**(i)**\nA description of such transportation.\n**(ii)**\nThe name of any such officer or employee who received such transportation.\n**(iii)**\nCosts associated with such transportation.\n**(B)**\nThe total number of instances such transportation was provided.\n**(C)**\nThe total cost of such transportation.\n##### (c) Prohibition on certain funding\nNo additional amounts are authorized to be appropriated to carry out this Act or the amendments made by this Act.",
      "versionDate": "2025-04-24",
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
            "name": "Congressional oversight",
            "updateDate": "2025-06-05T14:04:26Z"
          },
          {
            "name": "Government employee pay, benefits, personnel management",
            "updateDate": "2025-06-05T14:04:19Z"
          },
          {
            "name": "Space flight and exploration",
            "updateDate": "2025-06-05T14:05:01Z"
          },
          {
            "name": "Transportation costs",
            "updateDate": "2025-06-05T14:04:09Z"
          }
        ]
      },
      "policyArea": {
        "name": "Government Operations and Politics",
        "updateDate": "2025-05-29T15:39:50Z"
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
      "date": "2025-04-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2984ih.xml"
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
      "title": "ASTRO Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-25T08:23:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "ASTRO Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Astronaut Safe Temporary Ride Options Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-25T08:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 31, United States Code, to authorize transportation of officers and employees of Federal agencies returning from space, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-25T08:18:24Z"
    }
  ]
}
```
