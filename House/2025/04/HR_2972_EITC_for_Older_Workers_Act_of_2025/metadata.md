# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/2972?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/2972
- Title: EITC for Older Workers Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 2972
- Origin chamber: House
- Introduced date: 2025-04-21
- Update date: 2026-01-08T09:06:43Z
- Update date including text: 2026-01-08T09:06:43Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-04-21: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-04-21: Introduced in House

## Actions

- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Introduced in House
- 2025-04-21 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-04-21",
    "latestAction": {
      "actionDate": "2025-04-21",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/2972",
    "number": "2972",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001126",
        "district": "15",
        "firstName": "Mike",
        "fullName": "Rep. Carey, Mike [R-OH-15]",
        "lastName": "Carey",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "EITC for Older Workers Act of 2025",
    "type": "HR",
    "updateDate": "2026-01-08T09:06:43Z",
    "updateDateIncludingText": "2026-01-08T09:06:43Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-04-21",
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
      "actionDate": "2025-04-21",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-04-21",
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
          "date": "2025-04-21T16:00:25Z",
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
      "bioguideId": "D000096",
      "district": "7",
      "firstName": "Danny",
      "fullName": "Rep. Davis, Danny K. [D-IL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Davis",
      "middleName": "K.",
      "party": "D",
      "sponsorshipDate": "2025-04-21",
      "state": "IL"
    },
    {
      "bioguideId": "M001237",
      "district": "8",
      "firstName": "Kristen",
      "fullName": "Rep. McDonald Rivet, Kristen [D-MI-8]",
      "isOriginalCosponsor": "False",
      "lastName": "McDonald Rivet",
      "party": "D",
      "sponsorshipDate": "2026-01-06",
      "state": "MI"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2972ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 2972\nIN THE HOUSE OF REPRESENTATIVES\nApril 21, 2025 Mr. Carey (for himself and Mr. Davis of Illinois ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the upper age limit on eligibility for the earned income tax credit.\n#### 1. Short title\nThis Act may be cited as the EITC for Older Workers Act of 2025 .\n#### 2. Repeal of upper age limit on eligibility for earned income tax credit\n##### (a) In general\nSubclause (II) of section 32(c)(1)(A)(ii) of the Internal Revenue Code of 1986 is amended by striking but not attained age 65 .\n##### (b) Effective date\nThe amendment made by subsection (a) shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-04-21",
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
        "name": "Taxation",
        "updateDate": "2025-05-28T15:46:47Z"
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
      "date": "2025-04-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr2972ih.xml"
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
      "title": "EITC for Older Workers Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-07T03:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "EITC for Older Workers Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-07T03:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Internal Revenue Code of 1986 to repeal the upper age limit on eligibility for the earned income tax credit.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-07T03:03:24Z"
    }
  ]
}
```
