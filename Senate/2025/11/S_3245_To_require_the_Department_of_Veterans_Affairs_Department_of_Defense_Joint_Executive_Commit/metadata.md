# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3245?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3245
- Title: MIND Our Veterans Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 3245
- Origin chamber: Senate
- Introduced date: 2025-11-20
- Update date: 2026-04-16T19:21:19Z
- Update date including text: 2026-04-16T19:21:19Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-20: Introduced in Senate
- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.
- Latest action: 2025-11-20: Introduced in Senate

## Actions

- 2025-11-20 - IntroReferral: Introduced in Senate
- 2025-11-20 - IntroReferral: Read twice and referred to the Committee on Veterans' Affairs.
- 2026-03-19 - Committee: Committee on Health, Education, Labor, and Pensions. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-20",
    "latestAction": {
      "actionDate": "2025-11-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3245",
    "number": "3245",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000618",
        "district": "",
        "firstName": "Pete",
        "fullName": "Sen. Ricketts, Pete [R-NE]",
        "lastName": "Ricketts",
        "party": "R",
        "state": "NE"
      }
    ],
    "title": "MIND Our Veterans Act of 2025",
    "type": "S",
    "updateDate": "2026-04-16T19:21:19Z",
    "updateDateIncludingText": "2026-04-16T19:21:19Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-19",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Health, Education, Labor, and Pensions. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "ssva00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
          "date": "2026-03-19T14:01:04Z",
          "name": "Hearings By (full committee)"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
      "type": "Standing"
    },
    {
      "activities": {
        "item": {
          "date": "2025-11-20T17:21:54Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Veterans' Affairs Committee",
      "systemCode": "ssva00",
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
      "bioguideId": "S001208",
      "firstName": "Elissa",
      "fullName": "Sen. Slotkin, Elissa [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Slotkin",
      "party": "D",
      "sponsorshipDate": "2025-11-20",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3245is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3245\nIN THE SENATE OF THE UNITED STATES\nNovember 20, 2025 Mr. Ricketts (for himself and Ms. Slotkin ) introduced the following bill; which was read twice and referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Department of Veterans Affairs-Department of Defense Joint Executive Committee to improve mental health screening conducted under separation health assessments for members of the Armed Forces, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Medical Integrity in Necessary Diagnostics for Our Veterans Act of 2025 or the MIND Our Veterans Act of 2025 .\n#### 2. Improvement of mental health screening conducted under separation health assessments for members of the Armed Forces\n##### (a) Sense of Congress\nIt is the sense of Congress that\u2014\n**(1)**\nin order to address the mental health challenges following separation of members of the Armed Forces from military service, transitioning members must receive effective mental health screening prior to separation;\n**(2)**\nall screens conducted for mental health for members of the Armed Forces under the separation health assessment must be validated screens;\n**(3)**\nit is essential that the Department of Defense fully implement the separation health assessment with validated screening; and\n**(4)**\nscreening for substance use should be considered a necessary mental health screen and included in the separation health assessment.\n##### (b) Validated mental health screens\nThe Joint Executive Committee shall ensure the post-traumatic stress disorder (PTSD) mental health screen, the alcohol use mental health screen, and the violence risk mental health screen under the separation health assessment are each modified to be a validated tool, which may include taking steps to validate an existing screen or replacing an existing screen with an already validated screen.\n##### (c) Inclusion of substance use in mental health screens\n**(1) In general**\nThe Joint Executive Committee shall incorporate screening for substance use as a mental health screen and shall assess whether to include such screening in the separation health assessment, including by taking such action as the Joint Executive Committee considers appropriate, which may include taking steps to incorporate a validated screen.\n**(2) Report**\nNot later than 120 days after the date of the enactment of this Act, the Joint Executive Committee shall submit to the appropriate congressional committees a report on the justification of the Joint Executive Committee to include or not include a substance use screen under paragraph (1).\n##### (d) Implementation of separation health assessment\nNot later than 120 days after the date of the enactment of this Act, the Secretary of Defense, under the guidance of the Under Secretary of Defense for Personnel and Readiness, shall fully implement the separation health assessment.\n##### (e) Definitions\nIn this section:\n**(1) Appropriate congressional committees**\nThe term appropriate congressional committees means\u2014\n**(A)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the Senate; and\n**(B)**\nthe Committee on Armed Services and the Committee on Veterans\u2019 Affairs of the House of Representatives.\n**(2) Joint Executive Committee**\nThe term Joint Executive Committee means the Department of Veterans Affairs-Department of Defense Joint Executive Committee established under section 320 of title 38, United States Code.\n**(3) Separation health assessment**\nThe term separation health assessment means the health assessment for members of the Armed Forces separating from military service established by the Joint Executive Committee.",
      "versionDate": "2025-11-20",
      "versionType": "Introduced in Senate"
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
            "updateDate": "2026-04-16T19:21:18Z"
          },
          {
            "name": "Drug, alcohol, tobacco use",
            "updateDate": "2026-04-16T19:21:14Z"
          },
          {
            "name": "Medical tests and diagnostic methods",
            "updateDate": "2026-04-16T19:21:10Z"
          },
          {
            "name": "Mental health",
            "updateDate": "2026-04-16T19:20:43Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-04-16T19:21:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-12-19T17:31:31Z"
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
      "date": "2025-11-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3245is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "MIND Our Veterans Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T11:03:19Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "MIND Our Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Medical Integrity in Necessary Diagnostics for Our Veterans Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-18T05:23:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require the Department of Veterans Affairs-Department of Defense Joint Executive Committee to improve mental health screening conducted under separation health assessments for members of the Armed Forces, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-18T05:18:29Z"
    }
  ]
}
```
