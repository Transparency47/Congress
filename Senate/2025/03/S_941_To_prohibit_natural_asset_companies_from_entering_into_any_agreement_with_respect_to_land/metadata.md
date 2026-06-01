# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/941?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/941
- Title: A bill to prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.
- Congress: 119
- Bill type: S
- Bill number: 941
- Origin chamber: Senate
- Introduced date: 2025-03-11
- Update date: 2026-03-24T12:48:03Z
- Update date including text: 2026-03-24T12:48:03Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-03-11: Introduced in Senate
- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.
- Latest action: 2025-03-11: Introduced in Senate

## Actions

- 2025-03-11 - IntroReferral: Introduced in Senate
- 2025-03-11 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-03-11",
    "latestAction": {
      "actionDate": "2025-03-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/941",
    "number": "941",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "C001114",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Curtis, John R. [R-UT]",
        "lastName": "Curtis",
        "party": "R",
        "state": "UT"
      }
    ],
    "title": "A bill to prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.",
    "type": "S",
    "updateDate": "2026-03-24T12:48:03Z",
    "updateDateIncludingText": "2026-03-24T12:48:03Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-03-11",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-03-11",
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
          "date": "2025-03-11T19:42:34Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "systemCode": "sseg00",
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
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-03-11",
      "state": "UT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s941is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 941\nIN THE SENATE OF THE UNITED STATES\nMarch 11 (legislative day, March 10), 2025 Mr. Curtis (for himself and Mr. Lee ) introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.\n#### 1. Prohibition of natural asset companies from entering into certain agreements\n##### (a) Definition of natural asset company\nIn this section, the term natural asset company means\u2014\n**(1)**\na corporation that\u2014\n**(A)**\nholds the rights to the ecological performance of a defined area; and\n**(B)**\nhas the authority to manage the defined area for conservation, restoration, or sustainable management; or\n**(2)**\na company or organization that is substantially similar to a corporation described in paragraph (1).\n##### (b) Prohibition\nA natural asset company may not enter into any agreement with respect to\u2014\n**(1)**\nland in the State of Utah; or\n**(2)**\nnatural assets on or in land in the State of Utah.",
      "versionDate": "2025-03-11",
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
        "actionDate": "2025-03-11",
        "text": "Referred to the House Committee on Natural Resources."
      },
      "number": "2063",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "To prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.",
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
        "updateDate": "2025-05-22T13:56:16Z"
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
      "date": "2025-03-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s941is.xml"
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
      "title": "A bill to prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-29T02:19:02Z"
    },
    {
      "title": "A bill to prohibit natural asset companies from entering into any agreement with respect to land in the State of Utah or natural assets on or in land in the State of Utah.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T10:56:24Z"
    }
  ]
}
```
