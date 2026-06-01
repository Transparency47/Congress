# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/772?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/772
- Title: Employer Participation in Repayment Act
- Congress: 119
- Bill type: S
- Bill number: 772
- Origin chamber: Senate
- Introduced date: 2025-02-27
- Update date: 2025-12-05T21:54:50Z
- Update date including text: 2025-12-05T21:54:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-27: Introduced in Senate
- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-27: Introduced in Senate

## Actions

- 2025-02-27 - IntroReferral: Introduced in Senate
- 2025-02-27 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-27",
    "latestAction": {
      "actionDate": "2025-02-27",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/772",
    "number": "772",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "W000805",
        "district": "",
        "firstName": "Mark",
        "fullName": "Sen. Warner, Mark R. [D-VA]",
        "lastName": "Warner",
        "party": "D",
        "state": "VA"
      }
    ],
    "title": "Employer Participation in Repayment Act",
    "type": "S",
    "updateDate": "2025-12-05T21:54:50Z",
    "updateDateIncludingText": "2025-12-05T21:54:50Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-27",
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
      "actionDate": "2025-02-27",
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
          "date": "2025-02-27T16:38:50Z",
          "name": "Referred To"
        }
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
      "bioguideId": "T000250",
      "firstName": "John",
      "fullName": "Sen. Thune, John [R-SD]",
      "isOriginalCosponsor": "True",
      "lastName": "Thune",
      "party": "R",
      "sponsorshipDate": "2025-02-27",
      "state": "SD"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s772is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 772\nIN THE SENATE OF THE UNITED STATES\nFebruary 27, 2025 Mr. Warner (for himself and Mr. Thune ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to make the exclusion for certain employer payments of student loans under educational assistance programs permanent.\n#### 1. Short title\nThis Act may be cited as the Employer Participation in Repayment Act .\n#### 2. Exclusion for certain employer payments of student loans under educational assistance programs made permanent\n##### (a) In general\nSection 127(c)(1)(B) of the Internal Revenue Code of 1986 is amended by striking in the case of payments made before January 1, 2026, .\n##### (b) Effective date\nThe amendment made by this section shall apply to payments made after the date of the enactment of this Act.",
      "versionDate": "2025-02-27",
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
        "actionDate": "2025-03-03",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1801",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Employer Participation in Repayment Act",
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
        "updateDate": "2025-05-07T19:49:25Z"
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
      "date": "2025-02-27",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s772is.xml"
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
      "title": "Employer Participation in Repayment Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-21T04:08:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Employer Participation in Repayment Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-21T04:08:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to make the exclusion for certain employer payments of student loans under educational assistance programs permanent.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-21T04:03:30Z"
    }
  ]
}
```
