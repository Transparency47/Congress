# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/173?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/173
- Title: High Rise Fire Sprinkler Incentive Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 173
- Origin chamber: House
- Introduced date: 2025-01-03
- Update date: 2026-03-21T08:05:55Z
- Update date including text: 2026-03-21T08:05:55Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-01-03: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-01-03: Introduced in House

## Actions

- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Introduced in House
- 2025-01-03 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-01-03",
    "latestAction": {
      "actionDate": "2025-01-03",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/173",
    "number": "173",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M000317",
        "district": "11",
        "firstName": "Nicole",
        "fullName": "Rep. Malliotakis, Nicole [R-NY-11]",
        "lastName": "Malliotakis",
        "party": "R",
        "state": "NY"
      }
    ],
    "title": "High Rise Fire Sprinkler Incentive Act of 2025",
    "type": "HR",
    "updateDate": "2026-03-21T08:05:55Z",
    "updateDateIncludingText": "2026-03-21T08:05:55Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-01-03",
      "committees": {
        "item": {
          "name": "Ways and Means Committee",
          "systemCode": "hswm00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Ways and Means.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-01-03",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-01-03",
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
          "date": "2025-01-03T16:28:00Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Ways and Means Committee",
      "systemCode": "hswm00",
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
      "bioguideId": "L000601",
      "district": "1",
      "firstName": "Greg",
      "fullName": "Rep. Landsman, Greg [D-OH-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Landsman",
      "party": "D",
      "sponsorshipDate": "2025-03-04",
      "state": "OH"
    },
    {
      "bioguideId": "L000557",
      "district": "1",
      "firstName": "John",
      "fullName": "Rep. Larson, John B. [D-CT-1]",
      "isOriginalCosponsor": "False",
      "lastName": "Larson",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-03-10",
      "state": "CT"
    },
    {
      "bioguideId": "S001201",
      "district": "3",
      "firstName": "Thomas",
      "fullName": "Rep. Suozzi, Thomas R. [D-NY-3]",
      "isOriginalCosponsor": "False",
      "lastName": "Suozzi",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-03-21",
      "state": "NY"
    },
    {
      "bioguideId": "N000191",
      "district": "2",
      "firstName": "Joe",
      "fullName": "Rep. Neguse, Joe [D-CO-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Neguse",
      "party": "D",
      "sponsorshipDate": "2025-04-01",
      "state": "CO"
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
      "sponsorshipDate": "2025-04-17",
      "state": "PA"
    },
    {
      "bioguideId": "V000138",
      "district": "7",
      "firstName": "Eugene",
      "fullName": "Rep. Vindman, Eugene Simon [D-VA-7]",
      "isOriginalCosponsor": "False",
      "lastName": "Vindman",
      "middleName": "Simon",
      "party": "D",
      "sponsorshipDate": "2025-09-09",
      "state": "VA"
    },
    {
      "bioguideId": "L000599",
      "district": "17",
      "firstName": "Michael",
      "fullName": "Rep. Lawler, Michael [R-NY-17]",
      "isOriginalCosponsor": "False",
      "lastName": "Lawler",
      "party": "R",
      "sponsorshipDate": "2026-03-05",
      "state": "NY"
    },
    {
      "bioguideId": "M001160",
      "district": "4",
      "firstName": "Gwen",
      "fullName": "Rep. Moore, Gwen [D-WI-4]",
      "isOriginalCosponsor": "False",
      "lastName": "Moore",
      "party": "D",
      "sponsorshipDate": "2026-03-20",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr173ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 173\nIN THE HOUSE OF REPRESENTATIVES\nJanuary 3, 2025 Ms. Malliotakis introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to classify certain automatic fire sprinkler system retrofits as 15-year property for purposes of depreciation.\n#### 1. Short title\nThis Act may be cited as the High Rise Fire Sprinkler Incentive Act of 2025 .\n#### 2. Classification of certain automatic fire sprinkler system retrofits\n##### (a) Treatment as 15-Year property\nSection 168(e)(3)(E) of the Internal Revenue Code of 1986 is amended by striking and at the end of clause (vi), by striking the period at the end of clause (vii) and inserting , and , and by adding at the end the following:\n(viii) any automatic fire sprinkler system retrofit property. .\n##### (b) Applicable depreciation method\nSection 168(b)(3) of such Code is amended by adding at the end the following new subparagraph:\n(H) Any automatic fire sprinkler system retrofit property. .\n##### (c) Alternative system\nThe table contained in section 168(g)(3)(B) of such Code is amended by inserting after the item relating to subparagraph (E)(vii) the following:\n(E)(viii) 39 .\n##### (d) Definition of automatic fire sprinkler system retrofit property\nSection 168(i) of such Code is amended by adding at the end the following new paragraph:\n(20) Automatic fire sprinkler system retrofit property The term automatic fire sprinkler system retrofit property means any sprinkler system which\u2014 (A) meets the standards of National Fire Protection Association 13 (or any successor benchmark), (B) is installed for use in residential property, and (C) is installed in a building which\u2014 (i) was placed in service before the date of such installation, and (ii) has an occupiable floor more than 75 feet above the lowest level of fire department vehicle access. .\n##### (e) Effective date\nThe amendments made by this section shall apply after the date of enactment of this Act.",
      "versionDate": "2025-01-03",
      "versionType": "Introduced in House"
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
        "actionDate": "2025-02-10",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "504",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "High Rise Fire Sprinkler Incentive Act of 2025",
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
            "name": "Business investment and capital",
            "updateDate": "2025-08-28T18:16:06Z"
          },
          {
            "name": "Fires",
            "updateDate": "2025-08-28T18:16:06Z"
          },
          {
            "name": "Income tax deductions",
            "updateDate": "2025-08-28T18:16:06Z"
          },
          {
            "name": "Residential rehabilitation and home repair",
            "updateDate": "2025-08-28T18:16:06Z"
          }
        ]
      },
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-02-05T14:48:01Z"
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
      "date": "2025-01-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr173ih.xml"
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
      "title": "High Rise Fire Sprinkler Incentive Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-04-03T13:58:05Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "High Rise Fire Sprinkler Incentive Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-02-04T05:38:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to classify certain automatic fire sprinkler system retrofits as 15-year property for purposes of depreciation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-02-04T05:33:24Z"
    }
  ]
}
```
