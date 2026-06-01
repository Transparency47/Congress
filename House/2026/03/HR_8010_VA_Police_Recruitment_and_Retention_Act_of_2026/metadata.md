# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/8010?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/8010
- Title: VA Police Recruitment and Retention Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 8010
- Origin chamber: House
- Introduced date: 2026-03-19
- Update date: 2026-04-17T08:07:08Z
- Update date including text: 2026-04-17T08:07:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-19: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2026-03-19: Introduced in House

## Actions

- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Introduced in House
- 2026-03-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2026-03-24 - Committee: Referred to the Subcommittee on Oversight and Investigations.
- 2026-03-25 - Committee: Subcommittee Hearings Held
- 2026-04-15 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-15 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-19",
    "latestAction": {
      "actionDate": "2026-03-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/8010",
    "number": "8010",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "K000402",
        "district": "26",
        "firstName": "Timothy",
        "fullName": "Rep. Kennedy, Timothy M. [D-NY-26]",
        "lastName": "Kennedy",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "VA Police Recruitment and Retention Act of 2026",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:08Z",
    "updateDateIncludingText": "2026-04-17T08:07:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
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
      "text": "Forwarded by Subcommittee to Full Committee by Voice Vote.",
      "type": "Committee"
    },
    {
      "actionDate": "2026-04-15",
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
      "text": "Subcommittee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
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
      "actionDate": "2026-03-19",
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
      "actionDate": "2026-03-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2026-03-19",
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
          "date": "2026-03-19T13:02:05Z",
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
                "date": "2026-04-15T13:32:04Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-15T12:50:48Z",
                "name": "Markup by"
              },
              {
                "date": "2026-03-25T13:29:00Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2026-03-24T13:29:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8010ih.xml",
      "text": "I\n119th CONGRESS\n2d Session\nH. R. 8010\nIN THE HOUSE OF REPRESENTATIVES\nMarch 19, 2026 Mr. Kennedy of New York introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo prohibit the downgrading of law enforcement positions in the Department of Veterans Affairs, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the VA Police Recruitment and Retention Act of 2026 .\n#### 2. Prohibition on downgrading of law enforcement positions in the Department of Veterans Affairs\n##### (a) Prohibition\nNo official in the Department of Veterans Affairs, the Office of Personnel Management, or any other department or agency may propose, initiate, or carry out a position downgrade for any covered VA position, and no Federal funds may be used to propose, initiate, or carry out a position downgrade for any such position.\n##### (b) Retroactive application\nAny position downgrade for a covered VA position proposed, initiated, or carried out during the period beginning October 1, 2025, and ending on the date of the enactment of this Act shall have no force or effect. Any such position subjected to a position downgrade during this period shall be returned to the status it had prior to the position downgrade. Any employee occupying such a position shall receive all pay to which they otherwise would have been entitled.\n##### (c) Definitions\nFor purposes of this section:\n**(1)**\nThe term covered VA position means a position carrying out law enforcement functions within the Department of Veterans Affairs, whether permanent, temporary, full-time, part-time, or intermittent, and without regard to the source of funding for the position.\n**(2)**\nThe term position downgrade means a consistency review, incumbent-only review, or other classification action taken by the Office of Personnel Management or any other department or agency pursuant to chapter 51 of title 5, United States Code, or similar authority, that may result in a loss of grade or pay associated with a position or set of positions, without regard to whether an employee occupying such a position is entitled to or otherwise provided with retained grade or pay.",
      "versionDate": "2026-03-19",
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
        "updateDate": "2026-04-03T14:59:51Z"
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
      "date": "2026-03-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr8010ih.xml"
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
      "title": "VA Police Recruitment and Retention Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-02T05:38:26Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "VA Police Recruitment and Retention Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-02T05:38:25Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To prohibit the downgrading of law enforcement positions in the Department of Veterans Affairs, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-02T05:33:26Z"
    }
  ]
}
```
