# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6290?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6290
- Title: Safe Social Media Act
- Congress: 119
- Bill type: HR
- Bill number: 6290
- Origin chamber: House
- Introduced date: 2025-11-25
- Update date: 2026-01-08T09:06:45Z
- Update date including text: 2026-01-08T09:06:45Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-25: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-25: Introduced in House

## Actions

- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Introduced in House
- 2025-11-25 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-11-25 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2025-12-11 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-12-11 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-25",
    "latestAction": {
      "actionDate": "2025-11-25",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6290",
    "number": "6290",
    "originChamber": "House",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B000668",
        "district": "2",
        "firstName": "Cliff",
        "fullName": "Rep. Bentz, Cliff [R-OR-2]",
        "lastName": "Bentz",
        "party": "R",
        "state": "OR"
      }
    ],
    "title": "Safe Social Media Act",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:45Z",
    "updateDateIncludingText": "2026-01-08T09:06:45Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-25",
      "committees": {
        "item": {
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Commerce, Manufacturing, and Trade.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-25",
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
      "actionDate": "2025-11-25",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-25",
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
          "date": "2025-11-25T16:00:40Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-12-11T21:26:47Z",
                "name": "Reported by"
              },
              {
                "date": "2025-12-11T21:25:32Z",
                "name": "Markup by"
              },
              {
                "date": "2025-11-25T21:24:50Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Commerce, Manufacturing, and Trade Subcommittee",
          "systemCode": "hsif17"
        }
      },
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
      "bioguideId": "S001216",
      "district": "8",
      "firstName": "Kim",
      "fullName": "Rep. Schrier, Kim [D-WA-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Schrier",
      "party": "D",
      "sponsorshipDate": "2025-11-25",
      "state": "WA"
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
      "sponsorshipDate": "2026-01-07",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6290ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6290\nIN THE HOUSE OF REPRESENTATIVES\nNovember 25, 2025 Mr. Bentz (for himself and Ms. Schrier ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo require the Federal Trade Commission to conduct a study regarding social media use by teenagers.\n#### 1. Short title\nThis Act may be cited as the Safe Social Media Act .\n#### 2. Report by FTC on social media use by teenagers\n##### (a) In general\nThe Federal Trade Commission, in coordination with the Secretary of Health and Human Services (acting through the Assistant Secretary for Mental Health and Substance Use), shall\u2014\n**(1)**\nconduct a study on social media platform use among individuals younger than age 17, including\u2014\n**(A)**\nwhat personal information is collected by social media platforms regarding such individuals;\n**(B)**\nhow such personal information is used by the algorithms of the social media platforms;\n**(C)**\nhow such personal information is used with respect to targeted advertising;\n**(D)**\nhow often such individuals use social media platforms daily;\n**(E)**\ndifferences in use of social media platforms related to the age ranges of such individuals;\n**(F)**\nmental health effects on such individuals linked to the use of social media platforms; and\n**(G)**\npotential harmful effects and benefits for such individuals from extended social media platform use; and\n**(2)**\nnot later than 3 years after the date of enactment of this Act, submit to Congress a report on the findings of the study under paragraph (1), including any recommended policy changes based on such findings.\n##### (b) Exemption\nSubchapter I of chapter 35 of title 44, United States Code (commonly known as the Paperwork Reduction Act ) shall not apply to this section.\n#### 3. Definition of social media platform\n##### (a) In general\nIn this Act, the term social media platform means a public-facing website, internet application, or mobile internet application, including a social network or video sharing service that\u2014\n**(1)**\nserves the public; and\n**(2)**\nprimarily provides a forum for user-generated content, including messages, videos, images, games, and audio files.\n##### (b) Exclusions\nIn this Act, the term social media platform does not include the following:\n**(1)**\nA provider of broadband internet access service (as described in section 8.1(b) of title 47, Code of Federal Regulations (or any successor regulation)).\n**(2)**\nElectronic mail.",
      "versionDate": "2025-11-25",
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
            "name": "Child safety and welfare",
            "updateDate": "2026-01-05T17:54:53Z"
          },
          {
            "name": "Congressional oversight",
            "updateDate": "2026-01-05T17:54:53Z"
          },
          {
            "name": "Internet, web applications, social media",
            "updateDate": "2026-01-05T17:54:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Commerce",
        "updateDate": "2025-12-09T22:20:33Z"
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
      "date": "2025-11-25",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6290ih.xml"
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
      "title": "Safe Social Media Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-26T09:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Safe Social Media Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-26T09:23:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Federal Trade Commission to conduct a study regarding social media use by teenagers.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-26T09:18:19Z"
    }
  ]
}
```
