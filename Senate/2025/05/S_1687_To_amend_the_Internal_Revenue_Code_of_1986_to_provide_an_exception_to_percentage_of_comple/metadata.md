# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1687?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1687
- Title: Fair Accounting for Condominium Construction Act
- Congress: 119
- Bill type: S
- Bill number: 1687
- Origin chamber: Senate
- Introduced date: 2025-05-08
- Update date: 2025-07-03T12:03:30Z
- Update date including text: 2025-07-03T12:03:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-05-08: Introduced in Senate
- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-05-08: Introduced in Senate

## Actions

- 2025-05-08 - IntroReferral: Introduced in Senate
- 2025-05-08 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-05-08",
    "latestAction": {
      "actionDate": "2025-05-08",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1687",
    "number": "1687",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "Y000064",
        "district": "",
        "firstName": "Todd",
        "fullName": "Sen. Young, Todd [R-IN]",
        "lastName": "Young",
        "party": "R",
        "state": "IN"
      }
    ],
    "title": "Fair Accounting for Condominium Construction Act",
    "type": "S",
    "updateDate": "2025-07-03T12:03:30Z",
    "updateDateIncludingText": "2025-07-03T12:03:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-05-08",
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
      "actionDate": "2025-05-08",
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
          "date": "2025-05-08T17:47:08Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1687is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1687\nIN THE SENATE OF THE UNITED STATES\nMay 8, 2025 Mr. Young introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to provide an exception to percentage of completion method of accounting for certain residential construction contracts.\n#### 1. Short title\nThis Act may be cited as the Fair Accounting for Condominium Construction Act .\n#### 2. Exception to percentage of completion method of accounting for certain residential construction contracts\n##### (a) In general\nSection 460(e) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin paragraph (1)\u2014\n**(A)**\nby striking home construction contract both places it appears and inserting residential construction contract , and\n**(B)**\nby inserting (determined by substituting 3-year for 2-year in subparagraph (B)(i) for any residential construction contract which is not a home construction contract) after the requirements of clauses (i) and (ii) of subparagraph (B) ,\n**(2)**\nby striking paragraph (4) and redesignating paragraph (5) as paragraph (4), and\n**(3)**\nin subparagraph (A) of paragraph (4), as so redesignated, by striking paragraph (4) and inserting paragraph (3) .\n##### (b) Application of exception for purposes of alternative minimum tax\nSection 56(a)(3) of such Code is amended by striking any home construction contract (as defined in section 460(e)(6)) and inserting any residential construction contract (as defined in section 460(e)(4)) .\n##### (c) Effective date\nThe amendments made by this section shall apply to contracts entered into after the date of the enactment of this Act.",
      "versionDate": "2025-05-08",
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
        "actionDate": "2025-07-03",
        "actionTime": "14:31:40",
        "text": "Motion to reconsider laid on the table Agreed to without objection."
      },
      "number": "1",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "One Big Beautiful Bill Act",
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
        "updateDate": "2025-06-06T18:26:53Z"
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
      "date": "2025-05-08",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1687is.xml"
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
      "title": "Fair Accounting for Condominium Construction Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Fair Accounting for Condominium Construction Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-05-20T04:23:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to provide an exception to percentage of completion method of accounting for certain residential construction contracts.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-05-20T04:18:20Z"
    }
  ]
}
```
