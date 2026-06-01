# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2720?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2720
- Title: Gold Star Family Education Parity Act
- Congress: 119
- Bill type: HR
- Bill number: 2720
- Origin chamber: House
- Introduced date: 2025-04-08
- Update date: 2026-02-21T09:05:57Z
- Update date including text: 2026-02-21T09:05:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-08: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held
- Latest action: 2025-04-08: Introduced in House

## Actions

- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Introduced in House
- 2025-04-08 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-05-08 - Committee: Referred to the Subcommittee on Economic Opportunity.
- 2025-06-11 - Committee: Subcommittee Hearings Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-08",
    "latestAction": {
      "actionDate": "2025-04-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2720",
    "number": "2720",
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
    "title": "Gold Star Family Education Parity Act",
    "type": "HR",
    "updateDate": "2026-02-21T09:05:57Z",
    "updateDateIncludingText": "2026-02-21T09:05:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
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
      "text": "Subcommittee Hearings Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-04-08",
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
      "actionDate": "2025-04-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-08",
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
          "date": "2025-04-08T14:06:05Z",
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
                "date": "2025-06-11T16:48:49Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-05-08T16:48:37Z",
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

## API Data: cosponsors

```json
{
  "cosponsors": [
    {
      "bioguideId": "C001068",
      "district": "9",
      "firstName": "Steve",
      "fullName": "Rep. Cohen, Steve [D-TN-9]",
      "isOriginalCosponsor": "False",
      "lastName": "Cohen",
      "party": "D",
      "sponsorshipDate": "2025-10-08",
      "state": "TN"
    },
    {
      "bioguideId": "L000397",
      "district": "18",
      "firstName": "Zoe",
      "fullName": "Rep. Lofgren, Zoe [D-CA-18]",
      "isOriginalCosponsor": "False",
      "lastName": "Lofgren",
      "party": "D",
      "sponsorshipDate": "2025-11-17",
      "state": "CA"
    },
    {
      "bioguideId": "M001214",
      "district": "1",
      "firstName": "Frank",
      "fullName": "Rep. Mrvan, Frank J. [D-IN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Mrvan",
      "middleName": "J.",
      "party": "D",
      "sponsorshipDate": "2026-02-20",
      "state": "IN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2720ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2720\nIN THE HOUSE OF REPRESENTATIVES\nApril 8, 2025 Mr. Kennedy of New York introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to provide for the termination of a certain educational assistance program, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gold Star Family Education Parity Act .\n#### 2. Termination of authority for certain educational assistance program\n##### (a) Survivors\u2019 and dependents\u2019 educational assistance\nChapter 35 of title 38, United States Code, is amended by adding at the end the following new subchapter:\nVIII Termination 3571. Termination of authority (a) In general The authority to provide educational assistance under this chapter shall terminate on August 1, 2029. (b) Eligibility for post-9/11 educational assistance An individual who is no longer eligible for educational assistance under this chapter pursuant to subsection (a) shall be entitled to educational assistance under chapter 33 of this title in the same manner as if the individual had elected to receive educational assistance under section 3327 of this title, notwithstanding the restrictions on crediting service under section 3322(h)(1) of this title, but subject to the limitations under section 3327(d)(2) of this title. .\n##### (b) Clerical amendment\nThe table of sections at the beginning of such chapter is amended by adding at the end the following:\nSubchapter VIII\u2013Termination 3571. Termination of authority. .",
      "versionDate": "2025-04-08",
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
            "name": "Family relationships",
            "updateDate": "2025-06-27T16:08:04Z"
          },
          {
            "name": "Higher education",
            "updateDate": "2025-06-27T16:07:59Z"
          },
          {
            "name": "Military personnel and dependents",
            "updateDate": "2025-06-27T16:08:11Z"
          },
          {
            "name": "Veterans' education, employment, rehabilitation",
            "updateDate": "2025-06-27T16:07:53Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-05-12T18:32:48Z"
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
      "date": "2025-04-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2720ih.xml"
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
      "title": "Gold Star Family Education Parity Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-17T10:08:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Gold Star Family Education Parity Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-04-17T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to provide for the termination of a certain educational assistance program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-04-17T10:03:22Z"
    }
  ]
}
```
