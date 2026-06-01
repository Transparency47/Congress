# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/7948?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/7948
- Title: To deem certain individuals as parents of Department of Veterans Affairs employees for purposes of determining entitlement to certain family and medical leave for such employees.
- Congress: 119
- Bill type: HR
- Bill number: 7948
- Origin chamber: House
- Introduced date: 2026-03-16
- Update date: 2026-04-21T01:26:14Z
- Update date including text: 2026-04-21T01:26:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-16: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- Latest action: 2026-03-16: Introduced in House

## Actions

- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Introduced in House
- 2026-03-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-16 - IntroReferral: Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-16",
    "latestAction": {
      "actionDate": "2026-03-16",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/7948",
    "number": "7948",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "R000617",
        "district": "3",
        "firstName": "Delia",
        "fullName": "Rep. Ramirez, Delia C. [D-IL-3]",
        "lastName": "Ramirez",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "To deem certain individuals as parents of Department of Veterans Affairs employees for purposes of determining entitlement to certain family and medical leave for such employees.",
    "type": "HR",
    "updateDate": "2026-04-21T01:26:14Z",
    "updateDateIncludingText": "2026-04-21T01:26:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-25",
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-24",
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
      "actionDate": "2026-03-16",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2026-03-16",
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
      "text": "Referred to the Committee on Oversight and Government Reform, and in addition to the Committee on Veterans' Affairs, for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2026-03-16",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-16",
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
          "date": "2026-03-16T16:02:05Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-25T13:29:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-24T11:29:00Z",
                "name": "Referred to"
              }
            ]
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
          "date": "2026-03-16T16:02:00Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7948ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 7948\nIN THE HOUSE OF REPRESENTATIVES\nMarch 16, 2026 Mrs. Ramirez introduced the following bill; which was referred to the Committee on Oversight and Government Reform , and in addition to the Committee on Veterans' Affairs , for a period to be subsequently determined by the Speaker, in each case for consideration of such provisions as fall within the jurisdiction of the committee concerned\nA BILL\nTo deem certain individuals as parents of Department of Veterans Affairs employees for purposes of determining entitlement to certain family and medical leave for such employees.\n#### 1. Treatment of certain family members of Department of Veterans Affairs employees for purposes of family and medical leave\n##### (a) In general\nNotwithstanding section 7421 of title 38, United States Code, or any other provision of law, a parent of the spouse of a covered employee shall, for the purposes of determining eligibility for the entitlement of the covered employee to leave under section 6382(a)(1)(C) of title 5, United States Code, be deemed as a parent of the covered employee.\n##### (b) Definitions\nIn this section:\n**(1)**\nThe term covered employee means an employee of the Department of Veterans Affairs (including an employee who is appointed in the Veterans Health Administration under any provision of chapter 74 of such title on a full-time basis in a position listed in section 7421(b) of such title).\n**(2)**\nThe terms employee and parent have the meanings given such terms in section 6381 of title 5, United States Code.",
      "versionDate": "2026-03-16",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2026-04-21T01:26:14Z"
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
      "date": "2026-03-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr7948ih.xml"
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
      "title": "To deem certain individuals as parents of Department of Veterans Affairs employees for purposes of determining entitlement to certain family and medical leave for such employees.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-14T06:18:50Z"
    },
    {
      "title": "To deem certain individuals as parents of Department of Veterans Affairs employees for purposes of determining entitlement to certain family and medical leave for such employees.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-17T08:05:51Z"
    }
  ]
}
```
