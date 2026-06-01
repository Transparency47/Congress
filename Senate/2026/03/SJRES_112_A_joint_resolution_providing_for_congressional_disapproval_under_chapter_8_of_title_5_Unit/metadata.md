# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sjres/112?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-joint-resolution/112
- Title: A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to "One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities".
- Congress: 119
- Bill type: SJRES
- Bill number: 112
- Origin chamber: Senate
- Introduced date: 2026-03-05
- Update date: 2026-05-01T10:56:41Z
- Update date including text: 2026-05-06T04:18:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-03-05: Introduced in Senate
- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-04-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 403.
- 2026-04-30 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-04-30 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).
- Latest action: 2026-03-05: Introduced in Senate

## Actions

- 2026-03-05 - IntroReferral: Introduced in Senate
- 2026-03-05 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- 2026-04-30 - Calendars: Placed on Senate Legislative Calendar under General Orders. Calendar No. 403.
- 2026-04-30 - Discharge: Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).
- 2026-04-30 - Committee: Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-05",
    "latestAction": {
      "actionDate": "2026-03-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-joint-resolution/112",
    "number": "112",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "W000817",
        "district": "",
        "firstName": "Elizabeth",
        "fullName": "Sen. Warren, Elizabeth [D-MA]",
        "lastName": "Warren",
        "party": "D",
        "state": "MA"
      }
    ],
    "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to \"One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities\".",
    "type": "SJRES",
    "updateDate": "2026-05-01T10:56:41Z",
    "updateDateIncludingText": "2026-05-06T04:18:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-30",
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Placed on Senate Legislative Calendar under General Orders. Calendar No. 403.",
      "type": "Calendars"
    },
    {
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Discharge"
    },
    {
      "actionCode": "14500",
      "actionDate": "2026-04-30",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Senate Committee on Banking, Housing, and Urban Affairs discharged, by petition, pursuant to 5 U.S.C. 802(c).",
      "type": "Committee"
    },
    {
      "actionDate": "2026-03-05",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-05",
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
        "item": [
          {
            "date": "2026-04-30T19:38:37Z",
            "name": "Discharged From"
          },
          {
            "date": "2026-03-05T20:14:26Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "K000394",
      "firstName": "Andy",
      "fullName": "Sen. Kim, Andy [D-NJ]",
      "isOriginalCosponsor": "True",
      "lastName": "Kim",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NJ"
    },
    {
      "bioguideId": "W000779",
      "firstName": "Ron",
      "fullName": "Sen. Wyden, Ron [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Wyden",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "C001113",
      "firstName": "Catherine",
      "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
      "isOriginalCosponsor": "True",
      "lastName": "Cortez Masto",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "NV"
    },
    {
      "bioguideId": "K000384",
      "firstName": "Timothy",
      "fullName": "Sen. Kaine, Tim [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Kaine",
      "middleName": "M.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "VA"
    },
    {
      "bioguideId": "M001176",
      "firstName": "Jeff",
      "fullName": "Sen. Merkley, Jeff [D-OR]",
      "isOriginalCosponsor": "True",
      "lastName": "Merkley",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "OR"
    },
    {
      "bioguideId": "C001088",
      "firstName": "Christopher",
      "fullName": "Sen. Coons, Christopher A. [D-DE]",
      "isOriginalCosponsor": "True",
      "lastName": "Coons",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2026-03-05",
      "state": "DE"
    },
    {
      "bioguideId": "S000148",
      "firstName": "Charles",
      "fullName": "Sen. Schumer, Charles E. [D-NY]",
      "isOriginalCosponsor": "False",
      "lastName": "Schumer",
      "middleName": "E.",
      "party": "D",
      "sponsorshipDate": "2026-04-14",
      "state": "NY"
    },
    {
      "bioguideId": "K000377",
      "firstName": "Mark",
      "fullName": "Sen. Kelly, Mark [D-AZ]",
      "isOriginalCosponsor": "False",
      "lastName": "Kelly",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "AZ"
    },
    {
      "bioguideId": "A000382",
      "firstName": "Angela",
      "fullName": "Sen. Alsobrooks, Angela D. [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Alsobrooks",
      "party": "D",
      "sponsorshipDate": "2026-04-28",
      "state": "MD"
    },
    {
      "bioguideId": "B001267",
      "firstName": "Michael",
      "fullName": "Sen. Bennet, Michael F. [D-CO]",
      "isOriginalCosponsor": "False",
      "lastName": "Bennet",
      "party": "D",
      "sponsorshipDate": "2026-04-30",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres112is.xml",
      "text": "IIA\n119th CONGRESS\n2d Session\nS. J. RES. 112\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Ms. Warren (for herself, Mr. Kim , Mr. Wyden , Ms. Cortez Masto , Mr. Kaine , Mr. Merkley , and Mr. Coons ) introduced the following joint resolution; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities .\nThat Congress disapproves the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities (90 Fed. Reg. 50857 (November 12, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-03-05",
      "versionType": "IS"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres112pcs.xml",
      "text": "IIA\nCalendar No. 403\n119th CONGRESS\n2d Session\nS. J. RES. 112\nIN THE SENATE OF THE UNITED STATES\nMarch 5, 2026 Ms. Warren (for herself, Mr. Kim , Mr. Wyden , Ms. Cortez Masto , Mr. Kaine , Mr. Merkley , Mr. Coons , Mr. Schumer , Mr. Kelly , Ms. Alsobrooks , and Mr. Bennet ) introduced the following joint resolution; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nApril 30, 2026 Committee discharged, by petition, pursuant to 5 U.S.C. 802(c) , and placed on the calendar\nJOINT RESOLUTION\nProviding for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities .\nThat Congress disapproves the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities (90 Fed. Reg. 50857 (November 12, 2025)), and such rule shall have no force or effect.",
      "versionDate": "2026-04-30",
      "versionType": "PCS"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2026-03-09T18:24:35Z"
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
      "date": "2026-03-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres112is.xml"
        }
      ],
      "type": "IS"
    },
    {
      "date": "2026-04-30",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sjres/BILLS-119sjres112pcs.xml"
        }
      ],
      "type": "PCS"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to \"One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-07T04:18:26Z"
    },
    {
      "title": "A joint resolution providing for congressional disapproval under chapter 8 of title 5, United States Code, of the rule submitted by the Bureau of Industry and Security of the Department of Commerce relating to \"One Year Suspension of Expansion of End-User Controls for Affiliates of Certain Listed Entities\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-06T11:56:22Z"
    }
  ]
}
```
