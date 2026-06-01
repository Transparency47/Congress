# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2824?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/2824
- Title: A bill to amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits.
- Congress: 119
- Bill type: S
- Bill number: 2824
- Origin chamber: Senate
- Introduced date: 2025-09-16
- Update date: 2025-12-16T22:34:07Z
- Update date including text: 2025-12-16T22:34:07Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-09-16: Introduced in Senate
- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-09-16: Introduced in Senate

## Actions

- 2025-09-16 - IntroReferral: Introduced in Senate
- 2025-09-16 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-09-16",
    "latestAction": {
      "actionDate": "2025-09-16",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/2824",
    "number": "2824",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "M001153",
        "district": "",
        "firstName": "Lisa",
        "fullName": "Sen. Murkowski, Lisa [R-AK]",
        "lastName": "Murkowski",
        "party": "R",
        "state": "AK"
      }
    ],
    "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits.",
    "type": "S",
    "updateDate": "2025-12-16T22:34:07Z",
    "updateDateIncludingText": "2025-12-16T22:34:07Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-09-16",
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
      "actionDate": "2025-09-16",
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
          "date": "2025-09-16T21:25:34Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2824is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2824\nIN THE SENATE OF THE UNITED STATES\nSeptember 16, 2025 Ms. Murkowski introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits.\n#### 1. Extension of temporary enhanced premium credits\n##### (a) In general\nClause (iii) of section 36B(b)(3)(A) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking January 1, 2026 and inserting January 1, 2028 , and\n**(2)**\nby striking 2025 in the heading and inserting 2027 .\n##### (b) Taxpayers whose household income exceeds 400 percent of the poverty line\nSection 36B(c)(1)(E) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nby striking January 1, 2026 and inserting January 1, 2028 , and\n**(2)**\nby striking 2025 in the heading and inserting 2027 .\n##### (c) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2025-09-16",
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
        "actionDate": "2025-11-04",
        "text": "Read twice and referred to the Committee on Finance."
      },
      "number": "3102",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits, and for other purposes.",
      "type": "S"
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
        "updateDate": "2025-09-30T23:27:59Z"
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
      "date": "2025-09-16",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2824is.xml"
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
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-09-30T04:33:18Z"
    },
    {
      "title": "A bill to amend the Internal Revenue Code of 1986 to extend the temporary enhanced premium credits.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-09-17T10:56:26Z"
    }
  ]
}
```
