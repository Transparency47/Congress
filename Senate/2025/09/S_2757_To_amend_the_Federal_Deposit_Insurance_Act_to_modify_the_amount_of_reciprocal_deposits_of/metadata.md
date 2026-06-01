# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2757?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2757
- Title: Keeping Deposits Local Act
- Congress: 119
- Bill type: S
- Bill number: 2757
- Origin chamber: Senate
- Introduced date: 2025-09-10
- Update date: 2026-02-04T05:06:16Z
- Update date including text: 2026-02-04T05:06:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-09-10: Introduced in Senate
- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-09-10: Introduced in Senate

## Actions

- 2025-09-10 - IntroReferral: Introduced in Senate
- 2025-09-10 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-10",
    "latestAction": {
      "actionDate": "2025-09-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2757",
    "number": "2757",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Finance and Financial Sector"
    },
    "sponsors": [
      {
        "bioguideId": "R000605",
        "district": "",
        "firstName": "Mike",
        "fullName": "Sen. Rounds, Mike [R-SD]",
        "lastName": "Rounds",
        "party": "R",
        "state": "SD"
      }
    ],
    "title": "Keeping Deposits Local Act",
    "type": "S",
    "updateDate": "2026-02-04T05:06:16Z",
    "updateDateIncludingText": "2026-02-04T05:06:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-10",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-09-10",
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
          "date": "2025-09-10T17:41:32Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "bioguideId": "W000805",
      "firstName": "Mark",
      "fullName": "Sen. Warner, Mark R. [D-VA]",
      "isOriginalCosponsor": "True",
      "lastName": "Warner",
      "middleName": "R.",
      "party": "D",
      "sponsorshipDate": "2025-09-10",
      "state": "VA"
    },
    {
      "bioguideId": "B001319",
      "firstName": "Katie",
      "fullName": "Sen. Britt, Katie Boyd [R-AL]",
      "isOriginalCosponsor": "False",
      "lastName": "Britt",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "AL"
    },
    {
      "bioguideId": "V000128",
      "firstName": "Chris",
      "fullName": "Sen. Van Hollen, Chris [D-MD]",
      "isOriginalCosponsor": "False",
      "lastName": "Van Hollen",
      "party": "D",
      "sponsorshipDate": "2025-11-19",
      "state": "MD"
    },
    {
      "bioguideId": "M001242",
      "firstName": "Bernie",
      "fullName": "Sen. Moreno, Bernie [R-OH]",
      "isOriginalCosponsor": "False",
      "lastName": "Moreno",
      "party": "R",
      "sponsorshipDate": "2025-11-19",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2757is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2757\nIN THE SENATE OF THE UNITED STATES\nSeptember 10, 2025 Mr. Rounds (for himself and Mr. Warner ) introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Federal Deposit Insurance Act to modify the amount of reciprocal deposits of an insured depository institution that are not considered to be funds obtained by or through a deposit broker, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Keeping Deposits Local Act .\n#### 2. Amount of reciprocal deposits that are not considered to be funds obtained by or through a deposit broker\nSection 29(i) of the Federal Deposit Insurance Act ( 12 U.S.C. 1831f(i) ) is amended by striking paragraph (1) and inserting the following:\n(1) In general The sum of the following amounts of reciprocal deposits of an agent institution shall not be considered to be funds obtained, directly or indirectly, by or through a deposit broker: (A) An amount equal to 50 percent of the portion of the total liabilities of the agent institution that is not more than $1,000,000,000. (B) An amount equal to 40 percent of the portion, if any, of the total liabilities of the agent institution that is more than $1,000,000,000, but not more than $10,000,000,000. (C) An amount equal to 30 percent of the portion, if any, of the total liabilities of the agent institution that is more than $10,000,000,000, but not more than $250,000,000,000. (D) An amount equal to 20 percent of the portion, if any, of the total liabilities of the agent institution that is more than $250,000,000,000, but not more than $1,000,000,000,000. (E) An amount equal to 2 percent of the portion, if any, of the total liabilities of the agent institution that is more than $1,000,000,000,000. .\n#### 3. Definition of Agent Institution\nSection 29(i)(2)(A)(i)(I) of the Federal Deposit Insurance Act ( 12 U.S.C. 1831f(i)(2)(A)(i)(I) ) is amended by striking found to have a composite condition of outstanding or good and inserting assigned a CAMELS rating of 1, 2, or 3 .",
      "versionDate": "2025-09-10",
      "versionType": "Introduced in Senate"
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
        "name": "Finance and Financial Sector",
        "updateDate": "2025-09-23T16:11:13Z"
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
      "date": "2025-09-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2757is.xml"
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
      "title": "Keeping Deposits Local Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-11-20T12:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Keeping Deposits Local Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-09-19T02:53:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Federal Deposit Insurance Act to modify the amount of reciprocal deposits of an insured depository institution that are not considered to be funds obtained by or through a deposit broker, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-19T02:48:18Z"
    }
  ]
}
```
