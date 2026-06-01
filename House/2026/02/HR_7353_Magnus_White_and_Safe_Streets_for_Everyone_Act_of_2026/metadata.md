# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7353?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7353
- Title: Magnus White and Safe Streets for Everyone Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 7353
- Origin chamber: House
- Introduced date: 2026-02-04
- Update date: 2026-03-18T15:42:49Z
- Update date including text: 2026-03-18T15:42:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-02-04: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-02-04: Introduced in House

## Actions

- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Introduced in House
- 2026-02-04 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2026-02-04 - Committee: Referred to the Subcommittee on Commerce, Manufacturing, and Trade.
- 2026-02-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-02-10 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-02-04",
    "latestAction": {
      "actionDate": "2026-02-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7353",
    "number": "7353",
    "originChamber": "House",
    "policyArea": {
      "name": "Transportation and Public Works"
    },
    "sponsors": [
      {
        "bioguideId": "C001067",
        "district": "9",
        "firstName": "Yvette",
        "fullName": "Rep. Clarke, Yvette D. [D-NY-9]",
        "lastName": "Clarke",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Magnus White and Safe Streets for Everyone Act of 2026",
    "type": "HR",
    "updateDate": "2026-03-18T15:42:49Z",
    "updateDateIncludingText": "2026-03-18T15:42:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-10",
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
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
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
      "actionDate": "2026-02-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-02-04",
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
          "date": "2026-02-04T15:03:35Z",
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
                "date": "2026-02-10T21:18:16Z",
                "name": "Reported by"
              },
              {
                "date": "2026-02-10T21:16:44Z",
                "name": "Markup by"
              },
              {
                "date": "2026-02-04T21:15:57Z",
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
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2026-02-04",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7353ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7353\nIN THE HOUSE OF REPRESENTATIVES\nFebruary 4, 2026 Ms. Clarke of New York (for herself and Mr. Neguse ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend title 49, United States Code, to require automatic emergency braking system and similar crash avoidance technology equipped light vehicles detect and respond in a wider range of circumstances, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Magnus White and Safe Streets for Everyone Act of 2026 .\n#### 2. Vehicle standard for automatic emergency braking\nSection 30129 of title 49, United States Code, is amended\u2014\n**(1)**\nin subsection (b), by inserting The compliance date of such final rule shall not be later than September 1, 2029. after the period at the end; and\n**(2)**\nby adding at the end the following:\n(c) Vulnerable Road User Safety (1) Amended rule Except as provided in paragraph (2) and not later than 180 days after the date of the enactment of this subsection, the Secretary shall initiate a rulemaking process to amend the rule promulgated pursuant to subsection (a), Federal Motor Vehicle Safety Standards; Automatic Emergency Braking Systems for Light Vehicles, (89 Fed. Reg. 39686; May 9, 2024) to ensure that an automatic emergency braking system installed in any passenger motor vehicle manufactured for sale in the United States\u2014 (A) functions in daylight and low light conditions; (B) functions at the entire range of speeds specified in such rule for pedestrian automatic emergency braking; and (C) detects and responds to a bicyclist, motorcyclist, other cyclist, or other vulnerable road user, including with respect to the entire range of colors and complexions presented by skin, clothing, and protective gear. (2) Restriction Any amendment made to the rule pursuant to paragraph (1)(A) may not alter any maximum speed at which an automatic emergency braking system may operate as specified in such rule as of May 9, 2024. (3) Deadline for final rule Not later than 2 years after the date on which the rulemaking process is initiated pursuant to paragraph (1)(A), the Secretary shall issue a final revised rule in accordance with this subsection. (4) Compliance date The compliance date of the revised rule issued pursuant to paragraph (3) shall be not later than 2 years after the date on which the revised rule is issued. (5) Vulnerable road user defined In this subsection, the term vulnerable road user \u2014 (A) means any individual who is not an occupant of a motor vehicle with more than 3 wheels; and (B) includes\u2014 (i) pedestrians; (ii) bicyclists; (iii) motorcyclists; (iv) individuals traveling in wheelchairs; and (v) riders or occupants of other transport vehicles that are not motor vehicles, including all-terrain vehicles and tractors. .",
      "versionDate": "2026-02-04",
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
            "name": "Accidents",
            "updateDate": "2026-03-18T15:41:49Z"
          },
          {
            "name": "Computers and information technology",
            "updateDate": "2026-03-18T15:42:08Z"
          },
          {
            "name": "Consumer affairs",
            "updateDate": "2026-03-18T15:42:16Z"
          },
          {
            "name": "Hybrid, electric, and advanced technology vehicles",
            "updateDate": "2026-03-18T15:42:00Z"
          },
          {
            "name": "Motor vehicles",
            "updateDate": "2026-03-18T15:41:55Z"
          },
          {
            "name": "Pedestrians and bicycling",
            "updateDate": "2026-03-18T15:42:36Z"
          },
          {
            "name": "Product safety and quality",
            "updateDate": "2026-03-18T15:42:49Z"
          },
          {
            "name": "Roads and highways",
            "updateDate": "2026-03-18T15:42:24Z"
          }
        ]
      },
      "policyArea": {
        "name": "Transportation and Public Works",
        "updateDate": "2026-02-13T17:34:15Z"
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
      "date": "2026-02-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7353ih.xml"
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
      "title": "Magnus White and Safe Streets for Everyone Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-07T05:08:21Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Magnus White and Safe Streets for Everyone Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-07T05:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 49, United States Code, to require automatic emergency braking system and similar crash avoidance technology equipped light vehicles detect and respond in a wider range of circumstances, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-07T05:03:19Z"
    }
  ]
}
```
