# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/6436?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/6436
- Title: To amend the Agricultural Act of 2014 to allow for the advance payment of assistance under Tree Assistance Program, and for other purposes.
- Congress: 119
- Bill type: HR
- Bill number: 6436
- Origin chamber: House
- Introduced date: 2025-12-04
- Update date: 2026-05-16T08:08:05Z
- Update date including text: 2026-05-16T08:08:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-04: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Forestry and Horticulture.
- Latest action: 2025-12-04: Introduced in House

## Actions

- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Introduced in House
- 2025-12-04 - IntroReferral: Referred to the House Committee on Agriculture.
- 2026-01-13 - Committee: Referred to the Subcommittee on Forestry and Horticulture.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-04",
    "latestAction": {
      "actionDate": "2025-12-04",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/6436",
    "number": "6436",
    "originChamber": "House",
    "policyArea": {
      "name": "Agriculture and Food"
    },
    "sponsors": [
      {
        "bioguideId": "E000246",
        "district": "11",
        "firstName": "Chuck",
        "fullName": "Rep. Edwards, Chuck [R-NC-11]",
        "lastName": "Edwards",
        "party": "R",
        "state": "NC"
      }
    ],
    "title": "To amend the Agricultural Act of 2014 to allow for the advance payment of assistance under Tree Assistance Program, and for other purposes.",
    "type": "HR",
    "updateDate": "2026-05-16T08:08:05Z",
    "updateDateIncludingText": "2026-05-16T08:08:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Forestry and Horticulture.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-12-04",
      "committees": {
        "item": {
          "name": "Agriculture Committee",
          "systemCode": "hsag00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Agriculture.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-12-04",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-12-04",
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
          "date": "2025-12-04T14:03:45Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Agriculture Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-01-13T20:03:46Z",
              "name": "Referred to"
            }
          },
          "name": "Forestry and Horticulture Subcommittee",
          "systemCode": "hsag15"
        }
      },
      "systemCode": "hsag00",
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
      "bioguideId": "T000487",
      "district": "2",
      "firstName": "Jill",
      "fullName": "Rep. Tokuda, Jill N. [D-HI-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Tokuda",
      "middleName": "N.",
      "party": "D",
      "sponsorshipDate": "2025-12-04",
      "state": "HI"
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
      "sponsorshipDate": "2025-12-16",
      "state": "VA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6436ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 6436\nIN THE HOUSE OF REPRESENTATIVES\nDecember 4, 2025 Mr. Edwards (for himself and Ms. Tokuda ) introduced the following bill; which was referred to the Committee on Agriculture\nA BILL\nTo amend the Agricultural Act of 2014 to allow for the advance payment of assistance under Tree Assistance Program, and for other purposes.\n#### 1. Advance payment of assistance under Tree Assistance Program\nSection 1501(e) of the Agricultural Act of 2014 ( 7 U.S.C. 9081(e) ) is amended by adding at the end the following:\n(6) Advance payment Of the amount of assistance to be provided by the Secretary under paragraph (3) to eligible orchardists and nursery tree growers for losses described in paragraph (2), the Secretary may disburse not more than 25 percent of such amount to such eligible orchardists and nursery tree growers before the eligible orchardists or nursery tree growers begin replanting the trees for which such assistance is provided. .",
      "versionDate": "2025-12-04",
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
        "name": "Agriculture and Food",
        "updateDate": "2025-12-08T21:14:39Z"
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
      "date": "2025-12-04",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr6436ih.xml"
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
      "title": "To amend the Agricultural Act of 2014 to allow for the advance payment of assistance under Tree Assistance Program, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-05T09:18:19Z"
    },
    {
      "title": "To amend the Agricultural Act of 2014 to allow for the advance payment of assistance under Tree Assistance Program, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-05T09:06:42Z"
    }
  ]
}
```
