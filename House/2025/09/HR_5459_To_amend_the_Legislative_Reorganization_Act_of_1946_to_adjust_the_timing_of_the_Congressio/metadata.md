# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5459?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5459
- Title: To amend the Legislative Reorganization Act of 1946 to adjust the timing of the Congressional summer adjournment, and other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 5459
- Origin chamber: House
- Introduced date: 2025-09-18
- Update date: 2025-12-19T09:07:35Z
- Update date including text: 2025-12-19T09:07:35Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-18: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Rules.
- Latest action: 2025-09-18: Introduced in House

## Actions

- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Introduced in House
- 2025-09-18 - IntroReferral: Referred to the House Committee on Rules.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-18",
    "latestAction": {
      "actionDate": "2025-09-18",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5459",
    "number": "5459",
    "originChamber": "House",
    "policyArea": {
      "name": "Congress"
    },
    "sponsors": [
      {
        "bioguideId": "C001115",
        "district": "27",
        "firstName": "Michael",
        "fullName": "Rep. Cloud, Michael [R-TX-27]",
        "lastName": "Cloud",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "To amend the Legislative Reorganization Act of 1946 to adjust the timing of the Congressional summer adjournment, and other purposes.",
    "type": "HR",
    "updateDate": "2025-12-19T09:07:35Z",
    "updateDateIncludingText": "2025-12-19T09:07:35Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-09-18",
      "committees": {
        "item": {
          "name": "Rules Committee",
          "systemCode": "hsru00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Rules.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-09-18",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-09-18",
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
          "date": "2025-09-18T14:04:30Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Rules Committee",
      "systemCode": "hsru00",
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
      "bioguideId": "B001309",
      "district": "2",
      "firstName": "Tim",
      "fullName": "Rep. Burchett, Tim [R-TN-2]",
      "isOriginalCosponsor": "False",
      "lastName": "Burchett",
      "party": "R",
      "sponsorshipDate": "2025-09-19",
      "state": "TN"
    },
    {
      "bioguideId": "R000612",
      "district": "6",
      "firstName": "John",
      "fullName": "Rep. Rose, John W. [R-TN-6]",
      "isOriginalCosponsor": "False",
      "lastName": "Rose",
      "middleName": "W.",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TN"
    },
    {
      "bioguideId": "H001098",
      "district": "8",
      "firstName": "Abraham",
      "fullName": "Rep. Hamadeh, Abraham J. [R-AZ-8]",
      "isOriginalCosponsor": "False",
      "lastName": "Hamadeh",
      "middleName": "J.",
      "party": "R",
      "sponsorshipDate": "2025-12-18",
      "state": "AZ"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5459ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5459\nIN THE HOUSE OF REPRESENTATIVES\nSeptember 18, 2025 Mr. Cloud introduced the following bill; which was referred to the Committee on Rules\nA BILL\nTo amend the Legislative Reorganization Act of 1946 to adjust the timing of the Congressional summer adjournment, and other purposes.\n#### 1. Timing of Congressional summer adjournment\n##### (a) Timing\nSection 132 of the Legislative Reorganization Act of 1946 ( 2 U.S.C. 198 ) is amended\u2014\n**(1)**\nby striking July 31 each place it appears and inserting June 30 ; and\n**(2)**\nin subsection (a)(2)\u2014\n**(A)**\nby striking August and inserting July ; and\n**(B)**\nby striking the first Monday in September (Labor Day) of such year to the second day after Labor Day and inserting the first Monday in August of such year to that first Monday in August .\n##### (b) Effective date\nThe amendments made by subsection (a) shall take effect on the date on which the second session of the One Hundred Nineteenth Congress convenes.",
      "versionDate": "2025-09-18",
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
        "name": "Congress",
        "updateDate": "2025-11-18T16:37:33Z"
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
      "date": "2025-09-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5459ih.xml"
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
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Legislative Reorganization Act of 1946 to adjust the timing of the Congressional summer adjournment, and other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-01T04:48:25Z"
    },
    {
      "title": "To amend the Legislative Reorganization Act of 1946 to adjust the timing of the Congressional summer adjournment, and other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-19T08:06:54Z"
    }
  ]
}
```
