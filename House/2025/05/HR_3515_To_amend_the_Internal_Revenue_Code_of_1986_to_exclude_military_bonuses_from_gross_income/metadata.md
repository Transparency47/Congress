# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/3515?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/3515
- Title: To amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.
- Congress: 119
- Bill type: HR
- Bill number: 3515
- Origin chamber: House
- Introduced date: 2025-05-20
- Update date: 2025-12-05T22:54:34Z
- Update date including text: 2025-12-05T22:54:34Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-20: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the House Committee on Ways and Means.
- Latest action: 2025-05-20: Introduced in House

## Actions

- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Introduced in House
- 2025-05-20 - IntroReferral: Referred to the House Committee on Ways and Means.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-20",
    "latestAction": {
      "actionDate": "2025-05-20",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/3515",
    "number": "3515",
    "originChamber": "House",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "K000399",
        "district": "2",
        "firstName": "Jennifer",
        "fullName": "Rep. Kiggans, Jennifer A. [R-VA-2]",
        "lastName": "Kiggans",
        "party": "R",
        "state": "VA"
      }
    ],
    "title": "To amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.",
    "type": "HR",
    "updateDate": "2025-12-05T22:54:34Z",
    "updateDateIncludingText": "2025-12-05T22:54:34Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionCode": "H11100",
      "actionDate": "2025-05-20",
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
      "actionDate": "2025-05-20",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-05-20",
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
          "date": "2025-05-20T14:01:45Z",
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
      "bioguideId": "B000490",
      "district": "2",
      "firstName": "Sanford",
      "fullName": "Rep. Bishop, Sanford D. [D-GA-2]",
      "isOriginalCosponsor": "True",
      "lastName": "Bishop",
      "middleName": "D.",
      "party": "D",
      "sponsorshipDate": "2025-05-20",
      "state": "GA"
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
      "sponsorshipDate": "2025-06-26",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3515ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 3515\nIN THE HOUSE OF REPRESENTATIVES\nMay 20, 2025 Mrs. Kiggans of Virginia (for herself and Mr. Bishop ) introduced the following bill; which was referred to the Committee on Ways and Means\nA BILL\nTo amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.\n#### 1. Exclusion of military bonuses\n##### (a) In general\nSubsection (a) of section 134 of the Internal Revenue Code of 1986 is amended by striking any qualified military benefit and inserting any bonus paid to a member of the uniformed services under chapter 5 of title 37, United States Code, or any qualified military benefit .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after December 31, 2024.",
      "versionDate": "2025-05-20",
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
        "actionDate": "2025-05-22",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "1856",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.",
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
      "legislativeSubjects": "",
      "policyArea": {
        "name": "Taxation",
        "updateDate": "2025-06-06T20:31:35Z"
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
      "date": "2025-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr3515ih.xml"
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
      "title": "To amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-28T04:03:41Z"
    },
    {
      "title": "To amend the Internal Revenue Code of 1986 to exclude military bonuses from gross income.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-21T08:06:31Z"
    }
  ]
}
```
