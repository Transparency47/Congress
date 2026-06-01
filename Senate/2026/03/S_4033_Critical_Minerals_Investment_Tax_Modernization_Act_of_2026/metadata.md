# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4033?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4033
- Title: Critical Minerals Investment Tax Modernization Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4033
- Origin chamber: Senate
- Introduced date: 2026-03-10
- Update date: 2026-03-24T01:07:16Z
- Update date including text: 2026-03-24T01:07:16Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-10: Introduced in Senate
- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-10: Introduced in Senate

## Actions

- 2026-03-10 - IntroReferral: Introduced in Senate
- 2026-03-10 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-10",
    "latestAction": {
      "actionDate": "2026-03-10",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4033",
    "number": "4033",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "H001104",
        "district": "",
        "firstName": "Jon",
        "fullName": "Sen. Husted, Jon [R-OH]",
        "lastName": "Husted",
        "party": "R",
        "state": "OH"
      }
    ],
    "title": "Critical Minerals Investment Tax Modernization Act of 2026",
    "type": "S",
    "updateDate": "2026-03-24T01:07:16Z",
    "updateDateIncludingText": "2026-03-24T01:07:16Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-10",
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
      "actionDate": "2026-03-10",
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
          "date": "2026-03-10T18:15:39Z",
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

## API Data: fullTexts

```json
{
  "fullTexts": [
    {
      "fetchError": null,
      "sourceFormat": "Formatted XML",
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4033is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4033\nIN THE SENATE OF THE UNITED STATES\nMarch 10, 2026 Mr. Husted introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to adjust the percentage depletion rate for certain rare earths, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Critical Minerals Investment Tax Modernization Act of 2026 .\n#### 2. Adjustment of percentage depletion rate for certain rare earths\n##### (a) 22 percent depletion rate\nSection 613(b)(1)(B) of the Internal Revenue Code of 1986 is amended by inserting rare earths (in this subparagraph defined as the 15 lanthanide elements), scandium, before tantalum .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2026-03-10",
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
        "actionDate": "2025-07-25",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "4772",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Critical Minerals Investment Tax Modernization Act of 2025",
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
        "updateDate": "2026-03-24T01:07:16Z"
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
      "date": "2026-03-10",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4033is.xml"
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
      "title": "Critical Minerals Investment Tax Modernization Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Critical Minerals Investment Tax Modernization Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-20T02:23:29Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to adjust the percentage depletion rate for certain rare earths, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-20T02:18:29Z"
    }
  ]
}
```
