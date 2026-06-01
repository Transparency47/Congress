# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5539?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5539
- Title: POW Priority Care Act of 2025
- Congress: 119
- Bill type: HR
- Bill number: 5539
- Origin chamber: House
- Introduced date: 2025-09-19
- Update date: 2025-11-17T16:27:49Z
- Update date including text: 2025-11-17T16:27:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-19: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-15 - Committee: Referred to the Subcommittee on Health.
- Latest action: 2025-09-19: Introduced in House

## Actions

- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Introduced in House
- 2025-09-19 - IntroReferral: Referred to the House Committee on Veterans' Affairs.
- 2025-10-15 - Committee: Referred to the Subcommittee on Health.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-19",
    "latestAction": {
      "actionDate": "2025-09-19",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5539",
    "number": "5539",
    "originChamber": "House",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "W000798",
        "district": "5",
        "firstName": "Tim",
        "fullName": "Rep. Walberg, Tim [R-MI-5]",
        "lastName": "Walberg",
        "party": "R",
        "state": "MI"
      }
    ],
    "title": "POW Priority Care Act of 2025",
    "type": "HR",
    "updateDate": "2025-11-17T16:27:49Z",
    "updateDateIncludingText": "2025-11-17T16:27:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-15",
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
      "actionDate": "2025-09-19",
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
      "actionDate": "2025-09-19",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-19",
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
          "date": "2025-09-19T13:00:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Veterans' Affairs Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-15T18:50:18Z",
              "name": "Referred to"
            }
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
      "bioguideId": "K000391",
      "district": "8",
      "firstName": "Raja",
      "fullName": "Rep. Krishnamoorthi, Raja [D-IL-8]",
      "isOriginalCosponsor": "True",
      "lastName": "Krishnamoorthi",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
      "state": "IL"
    },
    {
      "bioguideId": "G000583",
      "district": "5",
      "firstName": "Josh",
      "fullName": "Rep. Gottheimer, Josh [D-NJ-5]",
      "isOriginalCosponsor": "True",
      "lastName": "Gottheimer",
      "party": "D",
      "sponsorshipDate": "2025-09-19",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5539ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5539\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 19, 2025 Mr. Walberg (for himself, Mr. Krishnamoorthi , and Mr. Gottheimer ) introduced the following bill; which was referred to the Committee on Veterans' Affairs\nA BILL\nTo amend title 38, United States Code, to assign the highest priority status for hospital care and medical services provided through the Department of Veterans Affairs to veterans who are former prisoners of war.\n#### 1. Short title\nThis Act may be cited as the POW Priority Care Act of 2025 .\n#### 2. Highest priority status for enrollment of former prisoners of war in health care system of Department of Veterans Affairs\n##### (a) Enrollment\nSection 1705(a) of title 38, United States Code, is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking and veterans and inserting , veterans ; and\n**(B)**\nby striking the period at the end and inserting , and veterans who are former prisoners of war. ; and\n**(2)**\nin paragraph (3), by striking who are former prisoners of war or .\n##### (b) Extended care services\nSection 1710B(c)(2)(D) of such title is amended by inserting a veteran who is a former prisoner of war or before a veteran who .\n##### (c) Applicability\nThe amendments made by this section shall apply with respect to veterans who are former prisoners of war before, on, or after the date of the enactment of this Act.",
      "versionDate": "2025-09-19",
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
        "updateDate": "2025-11-17T16:27:49Z"
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
      "date": "2025-09-19",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5539ih.xml"
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
      "title": "POW Priority Care Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-08T09:08:13Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "POW Priority Care Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-08T09:08:12Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend title 38, United States Code, to assign the highest priority status for hospital care and medical services provided through the Department of Veterans Affairs to veterans who are former prisoners of war.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-08T09:03:13Z"
    }
  ]
}
```
