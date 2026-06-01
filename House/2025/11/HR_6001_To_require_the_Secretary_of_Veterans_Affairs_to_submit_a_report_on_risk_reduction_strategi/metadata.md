# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6001?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6001
- Title: Veterans with ALS Reporting Act
- Congress: 119
- Bill type: HR
- Bill number: 6001
- Origin chamber: House
- Introduced date: 2025-11-10
- Update date: 2026-04-17T08:07:17Z
- Update date including text: 2026-04-17T08:07:17Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-11-10: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held
- Latest action: 2025-11-10: Introduced in House

## Actions

- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Introduced in House
- 2025-11-10 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-11-17 - Committee: Referred to the Subcommittee on Health.
- 2026-01-13 - Committee: Subcommittee Hearings Held
- 2026-04-16 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2026-04-16 - Committee: Subcommittee Consideration and Mark-up Session Held

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-10",
    "latestAction": {
      "actionDate": "2025-11-10",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6001",
    "number": "6001",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "C001121",
        "district": "6",
        "firstName": "Jason",
        "fullName": "Rep. Crow, Jason [D-CO-6]",
        "lastName": "Crow",
        "party": "D",
        "state": "CO"
      }
    ],
    "title": "Veterans with ALS Reporting Act",
    "type": "HR",
    "updateDate": "2026-04-17T08:07:17Z",
    "updateDateIncludingText": "2026-04-17T08:07:17Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "actionDate": "2026-04-16",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "actionDate": "2025-11-17",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Health.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-11-10",
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
      "actionDate": "2025-11-10",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-11-10",
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
          "date": "2025-11-10T17:00:20Z",
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
                "date": "2026-04-16T20:32:37Z",
                "name": "Reported by"
              },
              {
                "date": "2026-04-16T13:38:03Z",
                "name": "Markup by"
              },
              {
                "date": "2026-01-13T17:13:29Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-11-17T18:38:16Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsvr03"
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
      "bioguideId": "C000059",
      "district": "41",
      "firstName": "Ken",
      "fullName": "Rep. Calvert, Ken [R-CA-41]",
      "isOriginalCosponsor": "True",
      "lastName": "Calvert",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "CA"
    },
    {
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-11-10",
      "state": "AL"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "True",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "PA"
    },
    {
      "bioguideId": "Q000023",
      "district": "5",
      "firstName": "Mike",
      "fullName": "Rep. Quigley, Mike [D-IL-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Quigley",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "IL"
    },
    {
      "bioguideId": "B001324",
      "district": "1",
      "firstName": "Wesley",
      "fullName": "Rep. Bell, Wesley [D-MO-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Bell",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "MO"
    },
    {
      "bioguideId": "R000622",
      "district": "19",
      "firstName": "Josh",
      "fullName": "Rep. Riley, Josh [D-NY-19]",
      "isOriginalCosponsor": "False",
      "lastName": "Riley",
      "party": "D",
      "sponsorshipDate": "2025-12-11",
      "state": "NY"
    },
    {
      "bioguideId": "H001086",
      "district": "1",
      "firstName": "Diana",
      "fullName": "Rep. Harshbarger, Diana [R-TN-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Harshbarger",
      "party": "R",
      "sponsorshipDate": "2026-01-07",
      "state": "TN"
    },
    {
      "bioguideId": "M001238",
      "district": "0",
      "firstName": "Sarah",
      "fullName": "Rep. McBride, Sarah [D-DE-At Large]",
      "isOriginalCosponsor": "False",
      "lastName": "McBride",
      "party": "D",
      "sponsorshipDate": "2026-02-25",
      "state": "DE"
    },
    {
      "bioguideId": "J000310",
      "district": "32",
      "firstName": "Julie",
      "fullName": "Rep. Johnson, Julie [D-TX-32]",
      "isOriginalCosponsor": "False",
      "lastName": "Johnson",
      "party": "D",
      "sponsorshipDate": "2026-03-27",
      "state": "TX"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6001ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6001\nIN THE HOUSE OF REPRESENTATIVES\nNovember 10, 2025 Mr. Crow (for himself, Mr. Calvert , Ms. Sewell , and Mr. Fitzpatrick ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo require the Secretary of Veterans Affairs to submit a report on risk reduction strategies to lower the incidence and prevalence of amyotrophic lateral sclerosis in veterans.\n#### 1. Short title\nThis Act may be cited as the Veterans with ALS Reporting Act .\n#### 2. Report on Amyotrophic Lateral Sclerosis in Veterans\n##### (a) In general\nNot later than one year after the date of the enactment of this Act, the Secretary of Veterans Affairs, in consultation with the Director of the Centers for Disease Control and Prevention, shall submit to Congress a report on the incidence and prevalence of amyotrophic lateral sclerosis (commonly known as ALS ). Such report shall include\u2014\n**(1)**\nan assessment of the incidence and prevalence of amyotrophic lateral sclerosis in veterans (as defined in section 101 of title 38, United States Code);\n**(2)**\na description of the resources and support that the the Centers for Disease Control and the Department of Veterans Affairs provides to veterans with amyotrophic lateral sclerosis;\n**(3)**\na description of any deficiencies in the resources and support described in paragraph (2);\n**(4)**\na strategy to develop and test risk reduction strategies intended to lower the incidence and prevalence of amyotrophic lateral sclerosis among veterans;\n**(5)**\na strategy to develop a pathway for veterans receiving amyotrophic lateral sclerosis care within Department of Veterans Affairs clinics to participate in clinical trials and research sponsored by the Department of Veterans Affairs; and\n**(6)**\nany recommendations for the enactment of legislation to address the challenges or needs associated with lowering the incidence and prevalence of amyotrophic lateral sclerosis among veterans.\n##### (b) Tracking of amyotrophic lateral sclerosis in members and veterans\nThe Secretary of Veterans Affairs shall track the prevalence of amyotrophic lateral sclerosis in veterans using the amyotrophic lateral sclerosis registry and biorepository of the Centers for Disease Control and Prevention.\n##### (c) Subsequent reports\nNot later than three years after the date of the enactment of this Act, and every three years thereafter, the Secretary of Veterans Affairs shall submit to Congress an update to the report required under subsection (a) and information on the prevalence of amyotrophic lateral sclerosis tracked under subsection (b).",
      "versionDate": "2025-11-10",
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
            "name": "Congressional oversight",
            "updateDate": "2026-03-10T18:48:05Z"
          },
          {
            "name": "Government information and archives",
            "updateDate": "2026-03-10T18:48:20Z"
          },
          {
            "name": "Health information and medical records",
            "updateDate": "2026-03-10T18:48:24Z"
          },
          {
            "name": "Neurological disorders",
            "updateDate": "2026-03-10T18:48:15Z"
          },
          {
            "name": "Veterans' medical care",
            "updateDate": "2026-03-10T18:48:11Z"
          }
        ]
      },
      "policyArea": {
        "name": "Armed Forces and National Security",
        "updateDate": "2025-11-18T16:17:53Z"
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
      "date": "2025-11-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6001ih.xml"
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
      "title": "Veterans with ALS Reporting Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-14T06:38:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Veterans with ALS Reporting Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-11-14T06:38:15Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To require the Secretary of Veterans Affairs to submit a report on risk reduction strategies to lower the incidence and prevalence of amyotrophic lateral sclerosis in veterans.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-11-14T06:33:16Z"
    }
  ]
}
```
