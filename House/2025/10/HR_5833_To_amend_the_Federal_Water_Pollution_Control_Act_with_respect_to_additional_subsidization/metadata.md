# Metadata

- API URL: https://api.congress.gov/v3/bill/119/hr/5833?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/house-bill/5833
- Title: Clean Water Affordability Act
- Congress: 119
- Bill type: HR
- Bill number: 5833
- Origin chamber: House
- Introduced date: 2025-10-24
- Update date: 2026-04-08T22:43:05Z
- Update date including text: 2026-04-08T22:43:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-24: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-25 - Committee: Referred to the Subcommittee on Water Resources and Environment.
- Latest action: 2025-10-24: Introduced in House

## Actions

- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Introduced in House
- 2025-10-24 - IntroReferral: Referred to the House Committee on Transportation and Infrastructure.
- 2025-10-25 - Committee: Referred to the Subcommittee on Water Resources and Environment.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-24",
    "latestAction": {
      "actionDate": "2025-10-24",
      "text": "Introduced in House"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/house-bill/5833",
    "number": "5833",
    "originChamber": "House",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "W000808",
        "district": "24",
        "firstName": "Frederica",
        "fullName": "Rep. Wilson, Frederica S. [D-FL-24]",
        "lastName": "Wilson",
        "party": "D",
        "state": "FL"
      }
    ],
    "title": "Clean Water Affordability Act",
    "type": "HR",
    "updateDate": "2026-04-08T22:43:05Z",
    "updateDateIncludingText": "2026-04-08T22:43:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-25",
      "committees": {
        "item": {
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "sourceSystem": {
        "code": "1",
        "name": "House committee actions"
      },
      "text": "Referred to the Subcommittee on Water Resources and Environment.",
      "type": "Committee"
    },
    {
      "actionCode": "H11100",
      "actionDate": "2025-10-24",
      "committees": {
        "item": {
          "name": "Transportation and Infrastructure Committee",
          "systemCode": "hspw00"
        }
      },
      "sourceSystem": {
        "code": "2",
        "name": "House floor actions"
      },
      "text": "Referred to the House Committee on Transportation and Infrastructure.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "Intro-H",
      "actionDate": "2025-10-24",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in House",
      "type": "IntroReferral"
    },
    {
      "actionCode": "1000",
      "actionDate": "2025-10-24",
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
          "date": "2025-10-24T18:00:50Z",
          "name": "Referred To"
        }
      },
      "chamber": "House",
      "name": "Transportation and Infrastructure Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2025-10-25T17:01:19Z",
              "name": "Referred to"
            }
          },
          "name": "Water Resources and Environment Subcommittee",
          "systemCode": "hspw02"
        }
      },
      "systemCode": "hspw00",
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
      "bioguideId": "S001185",
      "district": "7",
      "firstName": "Terri",
      "fullName": "Rep. Sewell, Terri A. [D-AL-7]",
      "isOriginalCosponsor": "True",
      "lastName": "Sewell",
      "middleName": "A.",
      "party": "D",
      "sponsorshipDate": "2025-10-24",
      "state": "AL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5833ih.xml",
      "text": "I\n119th CONGRESS\n1st Session\nH. R. 5833\nIN THE HOUSE OF REPRESENTATIVES\nOctober 24, 2025 Ms. Wilson of Florida (for herself and Ms. Sewell ) introduced the following bill; which was referred to the Committee on Transportation and Infrastructure\nA BILL\nTo amend the Federal Water Pollution Control Act with respect to additional subsidization, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Clean Water Affordability Act .\n#### 2. Water pollution control revolving loan funds\nSection 603(i) of the Federal Water Pollution Control Act ( 33 U.S.C. 1383(i) ) is amended\u2014\n**(1)**\nin paragraph (1)(A)\u2014\n**(A)**\nin the matter preceding clause (i), by striking in assistance ; and\n**(B)**\nin clause (ii)(III), by striking to such ratepayers and inserting to help such ratepayers maintain access to wastewater (including stormwater) treatment services ; and\n**(2)**\nby striking paragraph (3) and inserting the following:\n(3) Subsidization amounts (A) In general A State may use for providing additional subsidization in a fiscal year under this subsection an amount that does not exceed the greater of\u2014 (i) 50 percent of the total amount received by the State in capitalization grants under this title for the fiscal year; or (ii) the annual average over the previous 10 fiscal years of the amounts deposited by the State in the State water pollution control revolving fund from State moneys that exceed the amounts required to be so deposited under section 602(b)(2). (B) Minimum To the extent there are sufficient applications for additional subsidization under this subsection that meet the criteria under paragraph (1)(A), a State shall use for providing additional subsidization in a fiscal year under this subsection an amount that is not less than 20 percent of the total amount received by the State in capitalization grants under this title for the fiscal year. (4) Exclusion A loan from the water pollution control revolving fund of a State with an interest rate equal to or greater than 0 percent shall not be considered additional subsidization for the purposes of this subsection. .",
      "versionDate": "2025-10-24",
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
        "actionDate": "2026-02-02",
        "text": "Referred to the Subcommittee on Water Resources and Environment."
      },
      "number": "6464",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Affordable Clean Water Infrastructure Act",
      "type": "HR"
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
        "name": "Environmental Protection",
        "updateDate": "2025-12-03T13:59:00Z"
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
      "date": "2025-10-24",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/hr/BILLS-119hr5833ih.xml"
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
      "title": "Clean Water Affordability Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-28T10:08:18Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "Clean Water Affordability Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-28T10:08:17Z"
    },
    {
      "billTextVersionCode": "IH",
      "billTextVersionName": "Introduced in House",
      "title": "To amend the Federal Water Pollution Control Act with respect to additional subsidization, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-28T10:03:15Z"
    }
  ]
}
```
