# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3869?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3869
- Title: Every Veteran Housed Act
- Congress: 119
- Bill type: HR
- Bill number: 3869
- Origin chamber: House
- Introduced date: 2025-06-10
- Update date: 2026-05-21T08:07:53Z
- Update date including text: 2026-05-21T08:07:53Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-10: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Economic Opportunity Discharged
- 2026-05-20 - Committee: Committee Hearings Held
- Latest action: 2025-06-10: Introduced in House

## Actions

- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Introduced in House
- 2025-06-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-23 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2026-03-18 - Committee: Committee Hearings Held
- 2026-03-18 - Committee: Subcommittee on Economic Opportunity Discharged
- 2026-05-20 - Committee: Committee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-10",
    "latestAction": {
      "actionDate": "2025-06-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3869",
    "number": "3869",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "D000635",
        "district": "3",
        "firstName": "Maxine",
        "fullName": "Rep. Dexter, Maxine [D-OR-3]",
        "lastName": "Dexter",
        "party": "D",
        "state": "OR"
      }
    ],
    "title": "Every Veteran Housed Act",
    "type": "HR",
    "updateDate": "2026-05-21T08:07:53Z",
    "updateDateIncludingText": "2026-05-21T08:07:53Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Veterans' Affairs Committee",
          "systemCode": "hsvr00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-18",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Subcommittee on Economic Opportunity Discharged",
      "type": "Committee"
    },
    {
      "actionDate": "2025-06-23",
      "committees": {
        "item": {
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Economic Opportunity.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-06-10",
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
      "text": "Referred to the House Committee on Veterans' Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-06-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-06-10",
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
            "date": "2026-05-20T13:27:46Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2026-03-18T16:54:03Z",
            "name": "Hearings By (full committee)"
          },
          {
            "date": "2025-06-10T14:04:45Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2026-03-18T16:53:56Z",
                "name": "Discharged from"
              },
              {
                "date": "2025-06-23T18:15:09Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Economic Opportunity Subcommittee",
          "systemCode": "hsvr10"
        }
      },
      "systemCode": "hsvr00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3869ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3869\nIN THE HOUSE OF REPRESENTATIVES\nJune 10, 2025 Ms. Dexter introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to expand eligibility for homelessness benefits under laws administered by the Secretary of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Every Veteran Housed Act .\n#### 2. Expansion of eligibility for homelessness benefits under laws administered by the Secretary of Veterans Affairs\n##### (a) Expansion\nSection 2002 of title 38, United States Code, is amended\u2014\n**(1)**\nin subsection (a)\u2014\n**(A)**\nby striking (a) In General.\u2014 ; and\n**(B)**\nby adding at the end the following new paragraphs:\n(3) The term veteran includes a person who was discharged or released from a period of service as a member of the uniformed services\u2014 (A) under conditions other than\u2014 (i) dishonorable; or (ii) by reason of the sentence of a general court-martial; and (B) regardless of\u2014 (i) the length of such period of service; (ii) whether such member was a member of an active or reserve component of the uniformed services; (iii) whether such service was active duty; (iv) whether such person currently serves as a member of the uniformed services; and (v) whether such person was discharged or released from another period of service under conditions described in clause (i) or (ii) of subparagraph (A). (4) The term uniformed services has the meaning given such term in section 101 of title 10. ; and\n**(2)**\nby striking subsection (b).\n##### (b) Conforming amendments\n**(1) Certain service deemed to be active service**\nSection 106(b) of such title is amended, in the matter following paragraph (3), by inserting 20, after 19, .\n**(2) Minimum active-duty service requirement**\nSection 5303A(b)(3)(F) of such title is amended by striking section 2011, 2012, 2013, 2044, or 2061 and inserting chapter 20 .",
      "versionDate": "2025-06-10",
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
            "name": "Homelessness and emergency shelter",
            "updateDate": "2026-04-06T20:31:45Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2026-04-06T20:31:40Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-24T20:22:32Z"
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
      "date": "2025-06-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3869ih.xml"
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
      "title": "Every Veteran Housed Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-13T06:53:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Every Veteran Housed Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-13T06:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to expand eligibility for homelessness benefits under laws administered by the Secretary of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-13T06:48:30Z"
    }
  ]
}
```
