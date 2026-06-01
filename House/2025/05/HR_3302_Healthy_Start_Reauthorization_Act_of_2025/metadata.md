# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3302?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3302
- Title: Healthy Start Reauthorization Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 3302
- Origin chamber: House
- Introduced date: 2025-05-08
- Update date: 2026-02-04T05:06:18Z
- Update date including text: 2026-02-04T05:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Hearings Held
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-17 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 0.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 284.
- 2025-10-03 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-331.
- 2025-10-03 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-331.
- Latest action: 2025-05-08: Introduced in House

## Actions

- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Introduced in House
- 2025-05-08 - IntroReferral: Referred to the House Committee on Energy and Commerce.
- 2025-09-10 - Committee: Forwarded by Subcommittee to Full Committee by Voice Vote.
- 2025-09-10 - Committee: Referred to the Subcommittee on Health.
- 2025-09-10 - Committee: Subcommittee Hearings Held
- 2025-09-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-09-17 - Committee: Ordered to be Reported by the Yeas and Nays: 49 - 0.
- 2025-10-03 - Calendars: Placed on the Union Calendar, Calendar No. 284.
- 2025-10-03 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-331.
- 2025-10-03 - Committee: Reported by the Committee on Energy and Commerce. H. Rept. 119-331.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3302",
    "number": "3302",
    "originChamber": "House",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "O000172",
        "district": "14",
        "firstName": "Alexandria",
        "fullName": "Rep. Ocasio-Cortez, Alexandria [D-NY-14]",
        "lastName": "Ocasio-Cortez",
        "party": "D",
        "state": "NY"
      }
    ],
    "title": "Healthy Start Reauthorization Act of 2025",
    "type": "HR",
    "updateDate": "2026-02-04T05:06:18Z",
    "updateDateIncludingText": "2026-02-04T05:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2025-10-03",
      "calendarNumber": {
        "calendar": "U00284"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 284.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2025-10-03",
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
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-331.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2025-10-03",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported by the Committee on Energy and Commerce. H. Rept. 119-331.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported by the Yeas and Nays: 49 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-17",
      "committees": {
        "item": {
          "name": "Energy and Commerce Committee",
          "systemCode": "hsif00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Committee Consideration and Mark-up Session Held",
      "type": "Committee"
    },
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
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
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
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
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
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
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-08",
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
            "date": "2025-10-03T20:27:56Z",
            "name": "Reported By"
          },
          {
            "date": "2025-09-17T16:03:36Z",
            "name": "Markup By"
          },
          {
            "date": "2025-05-08T13:03:00Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Energy and Commerce Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": [
              {
                "date": "2025-09-10T17:51:45Z",
                "name": "Reported by"
              },
              {
                "date": "2025-09-10T17:45:37Z",
                "name": "Hearings By (subcommittee)"
              },
              {
                "date": "2025-09-10T17:45:30Z",
                "name": "Referred to"
              }
            ]
          },
          "name": "Health Subcommittee",
          "systemCode": "hsif14"
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
      "bioguideId": "M000317",
      "district": "11",
      "firstName": "Nicole",
      "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
      "isOriginalCosponsor": "True",
      "lastName": "Malliotakis",
      "party": "R",
      "sponsorshipDate": "2025-05-08",
      "state": "NY"
    },
    {
      "bioguideId": "F000466",
      "district": "1",
      "firstName": "Brian",
      "fullName": "Rep. Fitzpatrick, Brian K. [R-PA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Fitzpatrick",
      "middleName": "K.",
      "party": "R",
      "sponsorshipDate": "2025-06-03",
      "state": "PA"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2025-06-03",
      "state": "WI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3302ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3302\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Ocasio-Cortez (for herself and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nA BILL\nTo amend the Public Health Service Act to reauthorize the Healthy Start Initiative.\n#### 1. Short title\nThis Act may be cited as the Healthy Start Reauthorization Act of 2025 .\n#### 2. Reauthorization of Healthy Start Initiative\nSection 330H(e)(1) of the Public Health Service Act ( 42 U.S.C. 254c\u20138(e)(1) ) is amended\u2014\n**(1)**\nby striking appropriated and inserting the following:\nappropriated\u2014 (A) ;\n**(2)**\nin subparagraph (A), as so inserted, by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(B) $145,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-05-08",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3302rh.xml",
      "text": "IB\nUnion Calendar No. 284\n119th CONGRESS\n1st Session\nH. R. 3302\n[Report No. 119\u2013331]\nIN THE HOUSE OF REPRESENTATIVES\nMay 8, 2025 Ms. Ocasio-Cortez (for herself and Ms. Malliotakis ) introduced the following bill; which was referred to the Committee on Energy and Commerce\nOctober 3, 2025 Additional sponsors: Mr. Fitzpatrick and Ms. Moore of Wisconsin\nOctober 3, 2025 Committed to the Committee of the Whole House on the State of the Union and ordered to be printed\nA BILL\nTo amend the Public Health Service Act to reauthorize the Healthy Start Initiative.\n#### 1. Short title\nThis Act may be cited as the Healthy Start Reauthorization Act of 2025 .\n#### 2. Reauthorization of Healthy Start Initiative\nSection 330H(e)(1) of the Public Health Service Act ( 42 U.S.C. 254c\u20138(e)(1) ) is amended\u2014\n**(1)**\nby striking appropriated and inserting the following:\nappropriated\u2014 (A) ;\n**(2)**\nin subparagraph (A), as so inserted, by striking the period at the end and inserting ; and ; and\n**(3)**\nby adding at the end the following:\n(B) $145,000,000 for each of fiscal years 2026 through 2030. .",
      "versionDate": "2025-10-03",
      "versionType": "Reported in House"
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
            "name": "Child health",
            "updateDate": "2025-09-16T14:09:43Z"
          },
          {
            "name": "Community life and organization",
            "updateDate": "2025-09-16T14:10:00Z"
          },
          {
            "name": "Health programs administration and funding",
            "updateDate": "2025-09-16T14:09:39Z"
          },
          {
            "name": "Health promotion and preventive care",
            "updateDate": "2025-09-16T14:09:56Z"
          },
          {
            "name": "Sex and reproductive health",
            "updateDate": "2025-09-16T14:09:47Z"
          },
          {
            "name": "Women's health",
            "updateDate": "2025-09-16T14:09:51Z"
          }
        ]
      },
      "policyArea": {
        "name": "Health",
        "updateDate": "2025-05-22T17:08:02Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3302ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2025-10-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3302rh.xml"
        }
      ],
      "type": "Reported in House"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "billTextVersionCode": "RH",
      "billTextVersionName": "Reported in House",
      "chamberCode": "H",
      "chamberName": "House",
      "title": "Healthy Start Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2025-10-04T05:23:15Z"
    },
    {
      "title": "Healthy Start Reauthorization Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-18T04:38:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Healthy Start Reauthorization Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-18T04:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Public Health Service Act to reauthorize the Healthy Start Initiative.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-18T04:33:27Z"
    }
  ]
}
```
