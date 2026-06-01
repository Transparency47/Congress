# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3047?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3047
- Title: Restoring Rural Health Act
- Congress: 119
- Bill type: S
- Bill number: 3047
- Origin chamber: Senate
- Introduced date: 2025-10-23
- Update date: 2025-12-02T17:59:49Z
- Update date including text: 2025-12-02T17:59:49Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-23: Introduced in Senate
- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-10-23: Introduced in Senate

## Actions

- 2025-10-23 - IntroReferral: Introduced in Senate
- 2025-10-23 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-23",
    "latestAction": {
      "actionDate": "2025-10-23",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3047",
    "number": "3047",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Health"
    },
    "sponsors": [
      {
        "bioguideId": "H001079",
        "district": "",
        "firstName": "Cindy",
        "fullName": "Sen. Hyde-Smith, Cindy [R-MS]",
        "lastName": "Hyde-Smith",
        "party": "R",
        "state": "MS"
      }
    ],
    "title": "Restoring Rural Health Act",
    "type": "S",
    "updateDate": "2025-12-02T17:59:49Z",
    "updateDateIncludingText": "2025-12-02T17:59:49Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-23",
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
      "actionDate": "2025-10-23",
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
          "date": "2025-10-23T18:50:17Z",
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
      "bioguideId": "S001150",
      "firstName": "Adam",
      "fullName": "Sen. Schiff, Adam B. [D-CA]",
      "isOriginalCosponsor": "True",
      "lastName": "Schiff",
      "middleName": "B.",
      "party": "D",
      "sponsorshipDate": "2025-10-23",
      "state": "CA"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3047is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3047\nIN THE SENATE OF THE UNITED STATES\nOctober 23, 2025 Mrs. Hyde-Smith (for herself and Mr. Schiff ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo provide for the treatment of certain critical access hospitals.\n#### 1. Short title\nThis Act may be cited as the Restoring Rural Health Act .\n#### 2. Treatment of certain critical access hospitals\nSection 1820(c)(2)(B)(i) of the Social Security Act ( 42 U.S.C. 1395i\u20134(c)(2)(B)(i) ) is amended\u2014\n**(1)**\nin subclause (I), by striking or after the semicolon;\n**(2)**\nin subclause (II), by inserting or after the semicolon; and\n**(3)**\nby adding at the end the following new subclause:\n(III) is a facility that\u2014 (aa) as of January 1, 2024, was designated as a critical access hospital; and (bb) receives notice from the Centers for Medicare & Medicaid Services during the period beginning on December 1, 2024, and ending on January 1, 2027, that the facility was found to be noncompliant with the distance requirement under section 485.610(c) of title 42, Code of Federal Regulations (or a successor regulation); .",
      "versionDate": "2025-10-23",
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
        "name": "Health",
        "updateDate": "2025-12-02T17:59:49Z"
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
      "date": "2025-10-23",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3047is.xml"
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
      "title": "Restoring Rural Health Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-29T06:08:16Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Restoring Rural Health Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-10-29T06:08:14Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to provide for the treatment of certain critical access hospitals.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-29T06:03:17Z"
    }
  ]
}
```
