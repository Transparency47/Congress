# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3384?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3384
- Title: Refinancing Relief for Veterans Act
- Congress: 119
- Bill type: HR
- Bill number: 3384
- Origin chamber: House
- Introduced date: 2025-05-14
- Update date: 2026-02-04T05:06:20Z
- Update date including text: 2026-02-04T05:06:20Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-05-14: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-11 - Committee: Hearings Held by the Subcommittee on Economic Opportunity Prior to Referral.
- 2025-06-23 - Committee: Referred to the Subcommittee on Economic Opportunity.
- Latest action: 2025-05-14: Introduced in House

## Actions

- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Introduced in House
- 2025-05-14 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-06-11 - Committee: Hearings Held by the Subcommittee on Economic Opportunity Prior to Referral.
- 2025-06-23 - Committee: Referred to the Subcommittee on Economic Opportunity.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-14",
    "latestAction": {
      "actionDate": "2025-05-14",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3384",
    "number": "3384",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "V000135",
        "district": "3",
        "firstName": "Derrick",
        "fullName": "Rep. Van Orden, Derrick [R-WI-3]",
        "lastName": "Van Orden",
        "party": "R",
        "state": "WI"
      }
    ],
    "title": "Refinancing Relief for Veterans Act",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:20Z",
    "updateDateIncludingText": "2026-02-04T05:06:20Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
      "actionDate": "2025-06-11",
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
      "text": "Hearings Held by the Subcommittee on Economic Opportunity Prior to Referral.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-14",
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
      "actionDate": "2025-05-14",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-14",
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
          "date": "2025-05-14T14:04:50Z",
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
                "date": "2025-06-23T18:20:26Z",
                "name": "Referred to"
              },
              {
                "date": "2025-06-11T18:19:38Z",
                "name": "Hearings By (subcommittee)"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3384ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3384\nIN THE HOUSE OF REPRESENTATIVES\nMay 14, 2025 Mr. Van Orden introduced the following bill; which was referred to the Committee on Veterans\u2019 Affairs\nA BILL\nTo amend title 38, United States Code, to adjust fees for interest rate reduction refinancing housing loans guaranteed, insured, or made by the Secretary of Veterans Affairs.\n#### 1. Short title\nThis Act may be cited as the Refinancing Relief for Veterans Act .\n#### 2. Adjustment of fees for interest rate reduction refinancing housing loans guaranteed insured, or made by the Secretary of Veterans Affairs\nThe loan fee table in section 3729(b)(2) of title 38, United States Code, is amended by striking the row in subparagraph (E) (relating to interest rate reduction refinancing loans) and inserting the following:\n(E)(i) Interest rate reduction refinancing loan (closed on or after August 1, 2025, and before December 31, 2025) 0.50 0.50 0.50 (E)(ii) Interest rate reduction refinancing loan (closed on or after December 31, 2025, and before December 31, 2027) 0.25 0.25 0.25 (E)(iii) Interest rate reduction refinancing loan (closed on or after December 31, 2027, and before December 31, 2032) 0.50 0.50 0.50 (E)(iv) Interest rate reduction refinancing loan (closed on or after December 31, 2032, and before December 31, 2035) 0.75 0.75 0.75 (E)(v) Interest rate reduction refinancing loan (closed on or after December 31, 2035) 0.50 0.50 0.50 .",
      "versionDate": "2025-05-14",
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
            "name": "Government lending and loan guarantees",
            "updateDate": "2025-06-26T16:46:53Z"
          },
          {
            "name": "Interest, dividends, interest rates",
            "updateDate": "2025-06-26T16:46:57Z"
          },
          {
            "name": "User charges and fees",
            "updateDate": "2025-06-26T16:47:02Z"
          },
          {
            "name": "Veterans' loans, housing, homeless programs",
            "updateDate": "2025-06-26T16:46:48Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-06-03T19:58:48Z"
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
      "date": "2025-05-14",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3384ih.xml"
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
      "title": "Refinancing Relief for Veterans Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T04:53:20Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Refinancing Relief for Veterans Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-21T04:53:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to adjust fees for interest rate reduction refinancing housing loans guaranteed, insured, or made by the Secretary of Veterans Affairs.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-21T04:48:36Z"
    }
  ]
}
```
