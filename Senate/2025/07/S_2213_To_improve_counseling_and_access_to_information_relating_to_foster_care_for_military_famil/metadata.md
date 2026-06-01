# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2213?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2213
- Title: Nikolas Hughey SAFE Homes for Kids Act
- Congress: 119
- Bill type: S
- Bill number: 2213
- Origin chamber: Senate
- Introduced date: 2025-07-08
- Update date: 2025-09-04T19:17:50Z
- Update date including text: 2025-09-04T19:17:50Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-07-08: Introduced in Senate
- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.
- Latest action: 2025-07-08: Introduced in Senate

## Actions

- 2025-07-08 - IntroReferral: Introduced in Senate
- 2025-07-08 - IntroReferral: Read twice and referred to the Committee on Armed Services.

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
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2213",
    "number": "2213",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Armed Forces and National Security"
    },
    "sponsors": [
      {
        "bioguideId": "S001198",
        "district": "",
        "firstName": "Dan",
        "fullName": "Sen. Sullivan, Dan [R-AK]",
        "lastName": "Sullivan",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "Nikolas Hughey SAFE Homes for Kids Act",
    "type": "S",
    "updateDate": "2025-09-04T19:17:50Z",
    "updateDateIncludingText": "2025-09-04T19:17:50Z"
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
          "name": "Armed Services Committee",
          "systemCode": "ssas00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Armed Services.",
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
          "date": "2025-07-08T21:50:43Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Armed Services Committee",
      "systemCode": "ssas00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2213is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2213\nIN THE SENATE OF THE UNITED STATES\nJuly 8, 2025 Mr. Sullivan introduced the following bill; which was read twice and referred to the Committee on Armed Services\nA BILL\nTo improve counseling and access to information relating to foster care for military families.\n#### 1. Short title\nThis Act may be cited as the Nikolas Hughey Securing Adoption and Foster Eligibility and Homes for Kids Act or the Nikolas Hughey SAFE Homes for Kids Act .\n#### 2. Improved counseling and access to information relating to foster care for military families\n##### (a) Training for counselors\n**(1) In general**\nThe Secretary of Defense shall require all counselors assigned to a Family Advocacy Program or Military and Family Life program at a military installation in the United States to be trained in the requirements and resources relating to foster care of the State in which the installation is located.\n**(2) Foster care liaisons**\nA counselor who has received training under paragraph (1) shall be known as a foster care liaison .\n##### (b) Inclusion of foster care information on Military OneSource\nThe Secretary shall require Military OneSource to include a mechanism for military families to obtain information on foster care, including the requirements and resources relating to foster care of each State.\n##### (c) Collaboration with Administration for Children and Families\nThe Secretary shall work with the Administration for Children and Families of the Department of Health and Human Services to obtain resources relating to foster care for military families, including curricula for training under paragraph (1).",
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
        "name": "Armed Forces and National Security",
        "updateDate": "2025-09-04T19:17:50Z"
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
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2213is.xml"
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
      "title": "Nikolas Hughey SAFE Homes for Kids Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-24T01:53:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nikolas Hughey SAFE Homes for Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Nikolas Hughey Securing Adoption and Foster Eligibility and Homes for Kids Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-24T01:53:22Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to improve counseling and access to information relating to foster care for military families.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-24T01:48:30Z"
    }
  ]
}
```
