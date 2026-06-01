# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/471?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/471
- Title: A bill to amend the Internal Revenue Code of 1986 to maintain the prohibition on allowing any deduction or credit associated with a trade or business involved in trafficking marijuana.
- Congress: 119
- Bill type: S
- Bill number: 471
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2026-02-11T11:56:36Z
- Update date including text: 2026-02-11T11:56:36Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/471",
    "number": "471",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "L000575",
        "district": "",
        "firstName": "James",
        "fullName": "Sen. Lankford, James [R-OK]",
        "lastName": "Lankford",
        "party": "R",
        "state": "OK"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to maintain the prohibition on allowing any deduction or credit associated with a trade or business involved in trafficking marijuana.",
    "type": "S",
    "updateDate": "2026-02-11T11:56:36Z",
    "updateDateIncludingText": "2026-02-11T11:56:36Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-06",
      "sourceSystem": {
        "code": "9",
        "name": "Library of Congress"
      },
      "text": "Introduced in Senate",
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
            "date": "2025-02-06T22:05:16Z",
            "name": "Referred To"
          },
          {
            "date": "2025-02-06T22:05:16Z",
            "name": "Referred To"
          }
        ]
      },
      "chamber": "Senate",
      "name": "Finance Committee",
      "systemCode": "ssfi00",
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
      "bioguideId": "R000618",
      "firstName": "Pete",
      "fullName": "Sen. Ricketts, Pete [R-NE]",
      "isOriginalCosponsor": "True",
      "lastName": "Ricketts",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "NE"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "False",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2026-02-10",
      "state": "NC"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s471is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 471\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Lankford (for himself and Mr. Ricketts ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to maintain the prohibition on allowing any deduction or credit associated with a trade or business involved in trafficking marijuana.\n#### 1. Short title\nThis Act may be cited as the No Deductions for Marijuana Businesses Act .\n#### 2. Expenditures in connection with the sale of marijuana\n##### (a) In general\nSection 280E of the Internal Revenue Code of 1986 is amended to read as follows:\n280E. Expenditures in connection with the illegal sale of drugs No deduction or credit shall be allowed for any amount paid or incurred during the taxable year in carrying on any trade or business if such trade or business (or the activities which comprise such trade or business) consists of trafficking in\u2014 (1) marijuana (as defined in section 102(16) of the Controlled Substances Act ( 21 U.S.C. 802(16) )), or (2) controlled substances (within the meaning of schedule I and II of the Controlled Substances Act), which is prohibited by Federal law or the law of any State in which such trade or business is conducted. .\n##### (b) Effective date\nThe amendment made by this section shall apply to amounts paid or incurred after the date of the enactment of this Act in taxable years ending after such date.",
      "versionDate": "2025-02-06",
      "versionType": "Introduced in Senate"
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
        "actionDate": "2025-02-21",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1447",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "No Deductions for Marijuana Businesses Act",
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
        "name": "Taxation",
        "updateDate": "2025-05-05T17:01:40Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s471is.xml"
        }
      ],
      "type": "Introduced in Senate"
    }
  ]
}
```

## API Data: titles

```json
{
  "titles": [
    {
      "title": "No Deductions for Marijuana Businesses Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-11T12:03:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to maintain the prohibition on allowing any deduction or credit associated with a trade or business involved in trafficking marijuana.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Deductions for Marijuana Businesses Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:25Z"
    }
  ]
}
```
