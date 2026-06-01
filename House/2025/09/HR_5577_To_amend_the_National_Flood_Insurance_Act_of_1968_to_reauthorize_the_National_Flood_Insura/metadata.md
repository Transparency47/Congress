# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5577?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5577
- Title: NFIP Extension Act of 2026
- Congress: 119
- Bill type: HR
- Bill number: 5577
- Origin chamber: House
- Introduced date: 2025-09-26
- Update date: 2026-01-29T22:41:13Z
- Update date including text: 2026-01-29T22:41:13Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-26: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-01-15 - Calendars: Placed on the Union Calendar, Calendar No. 391.
- 2026-01-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.
- 2026-01-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.
- Latest action: 2025-09-26: Introduced in House

## Actions

- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Introduced in House
- 2025-09-26 - IntroReferral: Referred to the House Committee on Financial Services.
- 2025-12-16 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Committee Consideration and Mark-up Session Held
- 2025-12-17 - Committee: Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.
- 2026-01-15 - Calendars: Placed on the Union Calendar, Calendar No. 391.
- 2026-01-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.
- 2026-01-15 - Committee: Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-26",
    "latestAction": {
      "actionDate": "2025-09-26",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5577",
    "number": "5577",
    "originChamber": "House",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "G000597",
        "district": "2",
        "firstName": "Andrew",
        "fullName": "Rep. Garbarino, Andrew R. [R-NY-2]",
        "lastName": "Garbarino",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "NFIP Extension Act of 2026",
    "type": "HR",
    "updateDate": "2026-01-29T22:41:13Z",
    "updateDateIncludingText": "2026-01-29T22:41:13Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H12410",
      "actionDate": "2026-01-15",
      "calendarNumber": {
        "calendar": "U00391"
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Placed on the Union Calendar, Calendar No. 391.",
      "type": "Calendars"
    },
    {
      "actionCode": "H12200",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.",
      "type": "Committee"
    },
    {
      "actionCode": "5000",
      "actionDate": "2026-01-15",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Reported (Amended) by the Committee on Financial Services. H. Rept. 119-456.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Ordered to be Reported (Amended) by the Yeas and Nays: 53 - 0.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionDate": "2025-12-16",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
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
      "actionCode": "H11100",
      "actionDate": "2025-09-26",
      "committees": {
        "item": {
          "name": "Financial Services Committee",
          "systemCode": "hsba00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Financial Services.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-26",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-26",
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
            "date": "2026-01-15T18:04:53Z",
            "name": "Reported By"
          },
          {
            "date": "2025-12-17T20:15:13Z",
            "name": "Markup By"
          },
          {
            "date": "2025-12-16T20:15:05Z",
            "name": "Markup By"
          },
          {
            "date": "2025-09-26T14:02:40Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "House",
      "name": "Financial Services Committee",
      "systemCode": "hsba00",
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
      "bioguideId": "C001103",
      "district": "1",
      "firstName": "Earl",
      "fullName": "Rep. Carter, Earl L. \"Buddy\" [R-GA-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Carter",
      "middleName": "L. \"Buddy\"",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "GA"
    },
    {
      "bioguideId": "V000133",
      "district": "2",
      "firstName": "Jefferson",
      "fullName": "Rep. Van Drew, Jefferson [R-NJ-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Drew",
      "party": "R",
      "sponsorshipDate": "2025-09-30",
      "state": "NJ"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2025-10-03",
      "state": "NY"
    },
    {
      "bioguideId": "M001217",
      "district": "23",
      "firstName": "Jared",
      "fullName": "Rep. Moskowitz, Jared [D-FL-23]",
      "isOriginalCosponsor": "False",
      "lastName": "Moskowitz",
      "party": "D",
      "sponsorshipDate": "2025-10-03",
      "state": "FL"
    },
    {
      "bioguideId": "L000598",
      "district": "1",
      "firstName": "Nick",
      "fullName": "Rep. LaLota, Nick [R-NY-1]",
      "isOriginalCosponsor": "False",
      "lastName": "LaLota",
      "party": "R",
      "sponsorshipDate": "2025-11-10",
      "state": "NY"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "False",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-12-15",
      "state": "NJ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5577ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5577\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on Financial Services\nA BILL\nTo amend the National Flood Insurance Act of 1968 to reauthorize the National Flood Insurance Program.\n#### 1. Short title\nThis Act may be cited as the NFIP Extension Act of 2026 .\n#### 2. Extension of the National Flood Insurance Program\n##### (a) Financing\nSection 1309(a) of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4016(a) ) is amended by striking September 30, 2023 and inserting September 30, 2026 .\n##### (b) Program expiration\nProgram expiration.\u2014Section 1319 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4026 ) is amended by striking September 30, 2023 and inserting September 30, 2026 .\n##### (c) Retroactive effective date\nIf this Act is enacted after September 30, 2025, the amendments made by subsections (a) and (b) shall take effect as if enacted on September 30, 2025.",
      "versionDate": "2025-09-26",
      "versionType": "Introduced in House"
    },
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5577rh.xml",
      "text": "IB\nUnion Calendar No. 391\n119th CONGRESS\n2d Session\nH. R. 5577\n[Report No. 119\u2013456]\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 26, 2025 Mr. Garbarino introduced the following bill; which was referred to the Committee on Financial Services\nJanuary 15, 2026 Additional sponsors: Mr. Carter of Georgia , Mr. Van Drew , Mr. Lawler , Mr. Moskowitz , Mr. LaLota , and Mr. Gottheimer\nJanuary 15, 2026 Reported with an amendment, committed to the Committee of the Whole House on the State of the Union, and ordered to be printed Strike out all after the enacting clause and insert the part printed in italic For text of introduced bill, see copy of bill as introduced on September 26, 2025\nA BILL\nTo amend the National Flood Insurance Act of 1968 to reauthorize the National Flood Insurance Program.\n#### 1. Short title\nThis Act may be cited as the NFIP Extension Act of 2026 .\n#### 2. Extension of the National Flood Insurance Program\n##### (a) Financing\nSection 1309(a) of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4016(a) ) is amended by striking September 30, 2023 and inserting September 30, 2026 .\n##### (b) Program expiration\nSection 1319 of the National Flood Insurance Act of 1968 ( 42 U.S.C. 4026 ) is amended by striking September 30, 2023 and inserting September 30, 2026 .\n##### (c) Retroactive effective date\nIf this Act is enacted after January 30, 2026, the amendments made by subsections (a) and (b) shall take effect as if enacted on January 30, 2026.",
      "versionDate": "2026-01-15",
      "versionType": "Reported in House"
    }
  ]
}
```

## API Data: relatedbills

```json
{
  "relatedBills": [
    {
      "congress": "119",
      "latestAction": {
        "actionDate": "2025-09-29",
        "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs."
      },
      "number": "2931",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "NFIP Extension Act",
      "type": "S"
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
            "name": "Disaster relief and insurance",
            "updateDate": "2026-01-05T17:34:46Z"
          },
          {
            "name": "Floods and storm protection",
            "updateDate": "2026-01-05T17:34:46Z"
          },
          {
            "name": "Natural disasters",
            "updateDate": "2026-01-05T17:34:46Z"
          }
        ]
      },
      "policyArea": {
        "name": "Finance and Financial Sector",
        "updateDate": "2025-11-18T17:52:02Z"
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
      "date": "2025-09-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5577ih.xml"
        }
      ],
      "type": "Introduced in House"
    },
    {
      "date": "2026-01-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/hr/BILLS-119hr5577rh.xml"
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
      "title": "NFIP Extension Act of 2026",
      "titleType": "Short Title(s) as Reported to House",
      "titleTypeCode": "102",
      "updateDate": "2026-01-16T05:38:16Z"
    },
    {
      "title": "NFIP Extension Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-03T04:23:19Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "NFIP Extension Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-03T04:23:16Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the National Flood Insurance Act of 1968 to reauthorize the National Flood Insurance Program.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-03T04:18:23Z"
    }
  ]
}
```
