# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2992?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2992
- Title: Gas Can Freedom Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 2992
- Origin chamber: Senate
- Introduced date: 2025-10-08
- Update date: 2025-12-09T22:16:08Z
- Update date including text: 2025-12-09T22:16:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-10-08: Introduced in Senate
- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.
- Latest action: 2025-10-08: Introduced in Senate

## Actions

- 2025-10-08 - IntroReferral: Introduced in Senate
- 2025-10-08 - IntroReferral: Read twice and referred to the Committee on Commerce, Science, and Transportation.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-08",
    "latestAction": {
      "actionDate": "2025-10-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2992",
    "number": "2992",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Commerce"
    },
    "sponsors": [
      {
        "bioguideId": "B001299",
        "district": "",
        "firstName": "Jim",
        "fullName": "Sen. Banks, Jim [R-IN]",
        "lastName": "Banks",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Gas Can Freedom Act of 2025",
    "type": "S",
    "updateDate": "2025-12-09T22:16:08Z",
    "updateDateIncludingText": "2025-12-09T22:16:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-08",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Commerce, Science, and Transportation.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-08",
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
          "date": "2025-10-08T23:15:52Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
      "type": "Standing"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2992is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2992\nIN THE SENATE OF THE UNITED STATES\nOctober 8, 2025 Mr. Banks introduced the following bill; which was read twice and referred to the Committee on Commerce, Science, and Transportation\nA BILL\nTo repeal the Portable Fuel Container Safety Act of 2020 and the Children\u2019s Gasoline Burn Prevention Act, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Gas Can Freedom Act of 2025 .\n#### 2. Repeals\n##### (a) Portable Fuel Container Safety Act of 2020\nThe Portable Fuel Container Safety Act of 2020 ( 15 U.S.C. 2056d ) is repealed.\n##### (b) Children\u2019s Gasoline Burn Prevention Act\nThe Children\u2019s Gasoline Burn Prevention Act ( 15 U.S.C. 2056 note) is repealed.\n##### (c) Regulations\n**(1) Effect of repeal**\nA regulation promulgated by the Consumer Product Safety Commission pursuant to an Act repealed by subsection (a) or (b) shall have no force or effect.\n**(2) Prohibition**\nNotwithstanding any other provision of law, the Consumer Product Safety Commission may not promulgate any regulation that requires\u2014\n**(A)**\na flame mitigation device in a portable fuel container; or\n**(B)**\na portable gasoline container to conform to child-resistant requirements.",
      "versionDate": "2025-10-08",
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
        "actionDate": "2025-02-13",
        "text": "Referred to the House Committee on Energy and Commerce."
      },
      "number": "1345",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Gas Can Freedom Act of 2025",
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
        "name": "Commerce",
        "updateDate": "2025-12-09T22:16:08Z"
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
      "date": "2025-10-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2992is.xml"
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
      "title": "Gas Can Freedom Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-23T02:53:15Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Gas Can Freedom Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-23T02:53:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to repeal the Portable Fuel Container Safety Act of 2020 and the Children's Gasoline Burn Prevention Act, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-23T02:48:16Z"
    }
  ]
}
```
