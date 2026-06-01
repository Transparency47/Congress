# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4221?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4221
- Title: Ensuring Better Interest Treatment and Deductibility Act (EBITDA)
- Congress: 119
- Bill type: S
- Bill number: 4221
- Origin chamber: Senate
- Introduced date: 2026-03-26
- Update date: 2026-04-09T16:43:01Z
- Update date including text: 2026-04-09T16:43:01Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2026-03-26: Introduced in Senate
- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-26: Introduced in Senate

## Actions

- 2026-03-26 - IntroReferral: Introduced in Senate
- 2026-03-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-26",
    "latestAction": {
      "actionDate": "2026-03-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4221",
    "number": "4221",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001047",
        "district": "",
        "firstName": "Shelley",
        "fullName": "Sen. Capito, Shelley Moore [R-WV]",
        "lastName": "Capito",
        "party": "R",
        "state": "WV"
      }
    ],
    "title": "Ensuring Better Interest Treatment and Deductibility Act (EBITDA)",
    "type": "S",
    "updateDate": "2026-04-09T16:43:01Z",
    "updateDateIncludingText": "2026-04-09T16:43:01Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-26",
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
      "actionDate": "2026-03-26",
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
          "date": "2026-03-26T16:47:56Z",
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
      "bioguideId": "C001056",
      "firstName": "John",
      "fullName": "Sen. Cornyn, John [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cornyn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TX"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "TN"
    },
    {
      "bioguideId": "H001104",
      "firstName": "Jon",
      "fullName": "Sen. Husted, Jon [R-OH]",
      "isOriginalCosponsor": "True",
      "lastName": "Husted",
      "party": "R",
      "sponsorshipDate": "2026-03-26",
      "state": "OH"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4221is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4221\nIN THE SENATE OF THE UNITED STATES\nMarch 26, 2026 Mrs. Capito (for herself, Mr. Cornyn , Mrs. Blackburn , and Mr. Husted ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the modification of the definition of adjusted taxable income for purposes of the limitation on business interest.\n#### 1. Short title\nThis Act may be cited as the Ensuring Better Interest Treatment and Deductibility Act (EBITDA) .\n#### 2. Repeal of modification to definition of adjusted taxable income for purposes of the limitation on business interest\n##### (a) In general\nSection 163(j)(8)(A) of the Internal Revenue Code of 1986, as amended by Public Law 119\u201321 , is amended by inserting and at the end of clause (iv) and by striking clause (vi).\n##### (b) Effective date\nThe amendments made by this section shall apply to taxable years beginning after December 31, 2025.",
      "versionDate": "2026-03-26",
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
        "actionDate": "2026-03-26",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "8101",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Ensuring Better Interest Treatment and Deductibility Act (EBITDA)",
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
        "updateDate": "2026-04-09T16:43:01Z"
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
      "date": "2026-03-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4221is.xml"
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
      "title": "Ensuring Better Interest Treatment and Deductibility Act (EBITDA)",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-03T05:38:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Ensuring Better Interest Treatment and Deductibility Act (EBITDA)",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-04-03T05:38:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to repeal the modification of the definition of adjusted taxable income for purposes of the limitation on business interest.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-04-03T05:33:39Z"
    }
  ]
}
```
