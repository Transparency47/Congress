# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3479?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3479
- Title: No Tax Exemptions For Terror Act
- Congress: 119
- Bill type: S
- Bill number: 3479
- Origin chamber: Senate
- Introduced date: 2025-12-15
- Update date: 2026-01-12T19:58:24Z
- Update date including text: 2026-01-12T19:58:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-15: Introduced in Senate
- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-12-15: Introduced in Senate

## Actions

- 2025-12-15 - IntroReferral: Introduced in Senate
- 2025-12-15 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-15",
    "latestAction": {
      "actionDate": "2025-12-15",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3479",
    "number": "3479",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "No Tax Exemptions For Terror Act",
    "type": "S",
    "updateDate": "2026-01-12T19:58:24Z",
    "updateDateIncludingText": "2026-01-12T19:58:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-15",
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
      "actionDate": "2025-12-15",
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
          "date": "2025-12-15T22:40:28Z",
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
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-12-15",
      "state": "TN"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3479is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3479\nIN THE SENATE OF THE UNITED STATES\nDecember 15, 2025 Mr. Scott of Florida (for himself and Mrs. Blackburn ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo specify that the Council on American-Islamic Relations shall not be treated as described in section 501(c)(3) of the Internal Revenue Code of 1986.\n#### 1. Short title\nThis Act may be cited as the No Tax Exemptions For Terror Act .\n#### 2. Council on American-Islamic relations subject to taxation\n##### (a) In general\nNotwithstanding any other provision of law, the Council on American-Islamic Relations shall not be treated as described in section 501(c)(3) of the Internal Revenue Code of 1986.\n##### (b) Effective date\nThis section shall apply to taxable years ending after the date of the enactment of this Act.",
      "versionDate": "2025-12-15",
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
        "actionDate": "2025-10-31",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "5890",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "No Tax Exemptions For Terror Act",
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
        "updateDate": "2026-01-09T16:07:43Z"
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
      "date": "2025-12-15",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3479is.xml"
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
      "title": "No Tax Exemptions For Terror Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-09T03:23:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Tax Exemptions For Terror Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-01-09T03:23:13Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to specify that the Council on American-Islamic Relations shall not be treated as described in section 501(c)(3) of the Internal Revenue Code of 1986.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-09T03:18:15Z"
    }
  ]
}
```
