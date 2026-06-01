# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/402?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/402
- Title: Words Matter for the District of Columbia Courts Act
- Congress: 119
- Bill type: S
- Bill number: 402
- Origin chamber: Senate
- Introduced date: 2025-02-05
- Update date: 2025-12-05T21:54:27Z
- Update date including text: 2025-12-05T21:54:27Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-05: Introduced in Senate
- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.
- Latest action: 2025-02-05: Introduced in Senate

## Actions

- 2025-02-05 - IntroReferral: Introduced in Senate
- 2025-02-05 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-05",
    "latestAction": {
      "actionDate": "2025-02-05",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/402",
    "number": "402",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Law"
    },
    "sponsors": [
      {
        "bioguideId": "M000934",
        "district": "",
        "firstName": "Jerry",
        "fullName": "Sen. Moran, Jerry [R-KS]",
        "lastName": "Moran",
        "party": "R",
        "state": "KS"
      }
    ],
    "title": "Words Matter for the District of Columbia Courts Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:27Z",
    "updateDateIncludingText": "2025-12-05T21:54:27Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-05",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-02-05",
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
        "item": {
          "date": "2025-02-05T16:02:23Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Homeland Security and Governmental Affairs Committee",
      "systemCode": "ssga00",
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
      "bioguideId": "P000595",
      "firstName": "Gary",
      "fullName": "Sen. Peters, Gary C. [D-MI]",
      "isOriginalCosponsor": "True",
      "lastName": "Peters",
      "party": "D",
      "sponsorshipDate": "2025-02-05",
      "state": "MI"
    },
    {
      "bioguideId": "W000790",
      "firstName": "Raphael",
      "fullName": "Sen. Warnock, Raphael G. [D-GA]",
      "isOriginalCosponsor": "False",
      "lastName": "Warnock",
      "party": "D",
      "sponsorshipDate": "2025-07-09",
      "state": "GA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s402is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 402\nIN THE SENATE OF THE UNITED STATES\nFebruary 5, 2025 Mr. Moran (for himself and Mr. Peters ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo amend title 11, District of Columbia Official Code, to revise references in such title to individuals with intellectual disabilities.\n#### 1. Short title\nThis Act may be cited as the Words Matter for the District of Columbia Courts Act .\n#### 2. References to individuals with intellectual disabilities\n##### (a) Jurisdiction of United States District Court\nSection 11\u2013501(2)(D), District of Columbia Official Code, is amended by striking substantially retarded persons and inserting persons with moderate intellectual disabilities .\n##### (b) Jurisdiction of Superior Court\nSection 11\u2013921(a)(4)(D), District of Columbia Official Code, is amended by striking substantially retarded persons and inserting persons with moderate intellectual disabilities .\n##### (c) Jurisdiction of Family Court\nSection 11\u20131101(a)(15), District of Columbia Official Code, is amended by striking the at least moderately mentally retarded and inserting persons with moderate intellectual disabilities .",
      "versionDate": "2025-02-05",
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
        "actionDate": "2025-02-05",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "1022",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Words Matter for the District of Columbia Courts Act",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Disability and health-based discrimination",
            "updateDate": "2025-06-18T14:13:20Z"
          },
          {
            "name": "District of Columbia",
            "updateDate": "2025-06-18T14:13:20Z"
          },
          {
            "name": "Federal district courts",
            "updateDate": "2025-06-18T14:13:20Z"
          },
          {
            "name": "Specialized courts",
            "updateDate": "2025-06-18T14:13:20Z"
          }
        ]
      },
      "policyArea": {
        "name": "Law",
        "updateDate": "2025-05-06T12:56:03Z"
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
      "date": "2025-02-05",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s402is.xml"
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
      "title": "Words Matter for the District of Columbia Courts Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-10T11:03:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Words Matter for the District of Columbia Courts Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:38:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend title 11, District of Columbia Official Code, to revise references in such title to individuals with intellectual disabilities.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:34:08Z"
    }
  ]
}
```
