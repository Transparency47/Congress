# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2364?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2364
- Title: A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.
- Congress: 119
- Bill type: S
- Bill number: 2364
- Origin chamber: Senate
- Introduced date: 2025-07-21
- Update date: 2025-09-24T17:32:31Z
- Update date including text: 2025-09-24T17:32:31Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-07-21: Introduced in Senate
- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S4507)
- Latest action: 2025-07-21: Introduced in Senate

## Actions

- 2025-07-21 - IntroReferral: Introduced in Senate
- 2025-07-21 - IntroReferral: Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S4507)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-07-21",
    "latestAction": {
      "actionDate": "2025-07-21",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2364",
    "number": "2364",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "B001261",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Barrasso, John [R-WY]",
        "lastName": "Barrasso",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
    "type": "S",
    "updateDate": "2025-09-24T17:32:31Z",
    "updateDateIncludingText": "2025-09-24T17:32:31Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-07-21",
      "committees": {
        "item": {
          "name": "Homeland Security and Governmental Affairs Committee",
          "systemCode": "ssga00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Homeland Security and Governmental Affairs. (text: CR S4507)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-07-21",
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
          "date": "2025-07-21T22:03:48Z",
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
      "bioguideId": "L000571",
      "firstName": "Cynthia",
      "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Lummis",
      "middleName": "M.",
      "party": "R",
      "sponsorshipDate": "2025-07-21",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2364is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2364\nIN THE SENATE OF THE UNITED STATES\nJuly 21, 2025 Mr. Barrasso (for himself and Ms. Lummis ) introduced the following bill; which was read twice and referred to the Committee on Homeland Security and Governmental Affairs\nA BILL\nTo direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.\n#### 1. Single, unique zip codes for certain communities\nNot later than 270 days after the date of enactment of this Act, the United States Postal Service shall designate a single, unique ZIP Code for each of the following communities:\n**(1)**\nMills, Wyoming.\n**(2)**\nStar Valley Ranch, Wyoming.",
      "versionDate": "2025-07-21",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-09-17T20:52:21Z"
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
      "date": "2025-07-21",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2364is.xml"
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
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-08-05T05:03:34Z"
    },
    {
      "title": "A bill to direct the United States Postal Service to designate single, unique ZIP Codes for certain communities, and for other purposes.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-22T10:56:20Z"
    }
  ]
}
```
