# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5009?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5009
- Title: Fine Arts Protection Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5009
- Origin chamber: House
- Introduced date: 2025-08-19
- Update date: 2026-04-07T08:05:40Z
- Update date including text: 2026-04-07T08:05:40Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-08-19: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-20 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.
- Latest action: 2025-08-19: Introduced in House

## Actions

- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Introduced in House
- 2025-08-19 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-08-20 - Committee: Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5009",
    "number": "5009",
    "originChamber": "House",
    "policyArea": {
      "name": "Arts, Culture, Religion"
    },
    "sponsors": [
      {
        "bioguideId": "T000468",
        "district": "1",
        "firstName": "Dina",
        "fullName": "Rep. Titus, Dina [D-NV-1]",
        "lastName": "Titus",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Fine Arts Protection Act of 2025",
    "type": "HR",
    "updateDate": "2026-04-07T08:05:40Z",
    "updateDateIncludingText": "2026-04-07T08:05:40Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-08-20",
      "committees": {
        "item": {
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Development, Public Buildings, and Emergency Management.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-08-19",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
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
        "item": {
          "date": "2025-08-19T14:01:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-08-20T21:36:34Z",
              "name": "Referred to"
            }
          },
          "name": "Economic Development, Public Buildings, and Emergency Management Subcommittee",
          "systemCode": "hspw13"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "P000597",
      "district": "1",
      "firstName": "Chellie",
      "fullName": "Rep. Pingree, Chellie [D-ME-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Pingree",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "ME"
    },
    {
      "bioguideId": "N000002",
      "district": "12",
      "firstName": "Jerrold",
      "fullName": "Rep. Nadler, Jerrold [D-NY-12]",
      "isOriginalCosponsor": "True",
      "lastName": "Nadler",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "NY"
    },
    {
      "bioguideId": "K000400",
      "district": "37",
      "firstName": "Sydney",
      "fullName": "Rep. Kamlager-Dove, Sydney [D-CA-37]",
      "isOriginalCosponsor": "True",
      "lastName": "Kamlager-Dove",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "CA"
    },
    {
      "bioguideId": "N000147",
      "district": "0",
      "firstName": "Eleanor",
      "fullName": "Del. Norton, Eleanor Holmes [D-DC-At Large]",
      "isOriginalCosponsor": "True",
      "lastName": "Norton",
      "middleName": "Holmes",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "DC"
    },
    {
      "bioguideId": "J000288",
      "district": "4",
      "firstName": "Henry",
      "fullName": "Rep. Johnson, Henry C. \"Hank\" [D-GA-4]",
      "isOriginalCosponsor": "True",
      "lastName": "Johnson",
      "middleName": "C. \"Hank\"",
      "party": "D",
      "sponsorshipDate": "2025-08-19",
      "state": "GA"
    },
    {
      "bioguideId": "D000399",
      "district": "37",
      "firstName": "Lloyd",
      "fullName": "Rep. Doggett, Lloyd [D-TX-37]",
      "isOriginalCosponsor": "False",
      "lastName": "Doggett",
      "party": "D",
      "sponsorshipDate": "2026-03-24",
      "state": "TX"
    },
    {
      "bioguideId": "T000469",
      "district": "20",
      "firstName": "Paul",
      "fullName": "Rep. Tonko, Paul [D-NY-20]",
      "isOriginalCosponsor": "False",
      "lastName": "Tonko",
      "party": "D",
      "sponsorshipDate": "2026-04-06",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5009ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5009\nIN THE HOUSE OF REPRESENTATIVES\nAugust 19, 2025 Ms. Titus (for herself, Ms. Pingree , Mr. Nadler , Ms. Kamlager-Dove , Ms. Norton , and Mr. Johnson of Georgia ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo require the Comptroller General of the United States to conduct a review of the Fine Arts Program of the General Services Administration, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Fine Arts Protection Act of 2025 .\n#### 2. Findings\nCongress finds the following:\n**(1)**\nArt plays an important role in helping people preserve and understand history.\n**(2)**\nThe Fine Arts Program of the General Services Administration contains the Fine Arts Collection, one of the oldest and largest public arts collections in the United States.\n**(3)**\nThe Fine Arts Program of the General Services Administration helps preserve historic works of cultural significance, including works commissioned under New Deal programs.\n#### 3. Review of Fine Arts Program\n##### (a) Review of Fine Arts Program\n**(1) In general**\nNot later than 1 year after the date of the enactment of this Act, the Comptroller General shall initiate a review of the Fine Arts Program of the General Services Administration.\n**(2) Requirements**\nIn conducting the review required under paragraph (1), the Comptroller General shall carry out the following:\n**(A)**\nSurvey each piece of art contained in the Fine Arts Collection of the General Services Administration.\n**(B)**\nProvide an estimate for the economic value of the Fine Arts Collection, including each work commissioned under a New Deal program.\n**(C)**\nReview the stewardship by the General Services Administration of the Fine Arts Program.\n**(D)**\nExplore whether the staffing and funding levels of the Fine Arts Program for the fiscal year in which the review is conducted are sufficient to manage and preserve the Fine Arts Collection.\n**(E)**\nExamine how the management by the General Services Administration of the Fine Arts Collection compares to other entities that preserve and manage art collections of similar size.\n**(F)**\nExamine whether the General Services Administration, given plans to continue reducing the staff and budget of the General Services Administration, has or should have plans to find a new home for the Fine Arts Collection.\n##### (b) Report to Congress\n**(1) In general**\nNot later than 2 years after the date of the enactment of this Act, the Comptroller General shall submit to the Committee on Transportation and Infrastructure of the House of Representatives and the Committee on Environment and Public Works of the Senate a report regarding the review conducted under subsection (a).\n**(2) Contents of report**\nThe report required under paragraph (1) shall include\u2014\n**(A)**\nthe findings of the review conducted under subsection (a); and\n**(B)**\nany recommendations for improvements in the management of the Fine Arts Collection, including whether the Fine Arts Program of the General Services Administration should continue managing the Fine Arts Collection.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Arts, Culture, Religion",
        "updateDate": "2025-09-19T15:48:10Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5009ih.xml"
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
      "title": "Fine Arts Protection Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-08-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Fine Arts Protection Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-08-21T04:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Comptroller General of the United States to conduct a review of the Fine Arts Program of the General Services Administration, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-21T04:03:19Z"
    }
  ]
}
```
