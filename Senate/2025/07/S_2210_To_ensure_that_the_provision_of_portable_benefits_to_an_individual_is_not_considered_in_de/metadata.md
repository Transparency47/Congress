# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2210?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2210
- Title: Unlocking Benefits for Independent Workers Act
- Congress: 119
- Bill type: S
- Bill number: 2210
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2025-09-04T15:21:08Z
- Update date including text: 2025-09-04T15:21:08Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Health, Education, Labor, and Pensions.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-08",
    "latestAction": {
      "actionDate": "2025-07-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2210",
    "number": "2210",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Labor and Employment"
    },
    "sponsors": [
      {
        "bioguideId": "C001075",
        "district": "",
        "firstName": "Bill",
        "fullName": "Sen. Cassidy, Bill [R-LA]",
        "lastName": "Cassidy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "Unlocking Benefits for Independent Workers Act",
    "type": "S",
    "updateDate": "2025-09-04T15:21:08Z",
    "updateDateIncludingText": "2025-09-04T15:21:08Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-08",
      "committees": {
        "item": {
          "name": "Health, Education, Labor, and Pensions Committee",
          "systemCode": "sshr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Health, Education, Labor, and Pensions.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-08",
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
          "date": "2025-07-08T21:28:57Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Health, Education, Labor, and Pensions Committee",
      "systemCode": "sshr00",
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
      "bioguideId": "T000278",
      "firstName": "Tommy",
      "fullName": "Sen. Tuberville, Tommy [R-AL]",
      "isOriginalCosponsor": "True",
      "lastName": "Tuberville",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "AL"
    },
    {
      "bioguideId": "S001184",
      "firstName": "Tim",
      "fullName": "Sen. Scott, Tim [R-SC]",
      "isOriginalCosponsor": "True",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "SC"
    },
    {
      "bioguideId": "B001305",
      "firstName": "Ted",
      "fullName": "Sen. Budd, Ted [R-NC]",
      "isOriginalCosponsor": "True",
      "lastName": "Budd",
      "party": "R",
      "sponsorshipDate": "2025-07-08",
      "state": "NC"
    },
    {
      "bioguideId": "B001299",
      "firstName": "Jim",
      "fullName": "Sen. Banks, Jim [R-IN]",
      "isOriginalCosponsor": "False",
      "lastName": "Banks",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "IN"
    },
    {
      "bioguideId": "L000575",
      "firstName": "James",
      "fullName": "Sen. Lankford, James [R-OK]",
      "isOriginalCosponsor": "False",
      "lastName": "Lankford",
      "party": "R",
      "sponsorshipDate": "2025-07-14",
      "state": "OK"
    },
    {
      "bioguideId": "M001244",
      "firstName": "Ashley",
      "fullName": "Sen. Moody, Ashley [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Moody",
      "party": "R",
      "sponsorshipDate": "2025-07-24",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2210is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2210\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Mr. Cassidy (for himself, Mr. Tuberville , Mr. Scott of South Carolina , and Mr. Budd ) introduced the following bill; which was read twice and referred to the Committee on Health, Education, Labor, and Pensions\nA BILL\nTo ensure that the provision of portable benefits to an individual is not considered in determining whether such individual is an employee of a person, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Unlocking Benefits for Independent Workers Act .\n#### 2. Consideration of portable benefits with respect to employment status\nA determination whether an individual is an employee of a person for the purposes of any Federal law shall be made without considering whether such person provides to the individual\u2014\n**(1)**\na benefit or protection that the individual may maintain without regard to whether the individual continues to perform work for such person;\n**(2)**\na benefit or protection of a type that is commonly provided to a full-time employee;\n**(3)**\na contribution, financial or otherwise, with respect to a benefit described in paragraph (1) or (2) that is\u2014\n**(A)**\nmade on behalf of the individual by the person in connection with work performed by the individual for the person; or\n**(B)**\nmade by the individual; or\n**(4)**\na benefit, protection, or contribution that is a combination of any benefit, protection, or contribution described in paragraph (1), (2), or (3).",
      "versionDate": "2025-07-08",
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
        "name": "Labor and Employment",
        "updateDate": "2025-09-04T15:21:08Z"
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
      "date": "2025-07-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2210is.xml"
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
      "title": "Unlocking Benefits for Independent Workers Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-25T11:03:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Unlocking Benefits for Independent Workers Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to ensure that the provision of portable benefits to an individual is not considered in determining whether such individual is an employee of a person, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:31Z"
    }
  ]
}
```
