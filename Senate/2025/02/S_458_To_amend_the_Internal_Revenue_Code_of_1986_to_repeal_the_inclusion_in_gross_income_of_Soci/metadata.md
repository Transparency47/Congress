# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/458?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/458
- Title: Senior Citizens Tax Elimination Act
- Congress: 119
- Bill type: S
- Bill number: 458
- Origin chamber: Senate
- Introduced date: 2025-02-06
- Update date: 2025-12-05T21:34:58Z
- Update date including text: 2025-12-05T21:34:58Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-02-06: Introduced in Senate
- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-02-06: Introduced in Senate

## Actions

- 2025-02-06 - IntroReferral: Introduced in Senate
- 2025-02-06 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-02-06",
    "latestAction": {
      "actionDate": "2025-02-06",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/458",
    "number": "458",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "T000278",
        "district": "",
        "firstName": "Tommy",
        "fullName": "Sen. Tuberville, Tommy [R-AL]",
        "lastName": "Tuberville",
        "party": "R",
        "state": "AL"
      }
    ],
    "title": "Senior Citizens Tax Elimination Act",
    "type": "S",
    "updateDate": "2025-12-05T21:34:58Z",
    "updateDateIncludingText": "2025-12-05T21:34:58Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-02-06",
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
      "actionDate": "2025-02-06",
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
          "date": "2025-02-06T18:12:41Z",
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
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-02-06",
      "state": "MT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s458is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 458\nIN THE SENATE OF THE UNITED STATES\nFebruary 6 (legislative day, February 5), 2025 Mr. Tuberville (for himself and Mr. Sheehy ) introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to repeal the inclusion in gross income of Social Security benefits.\n#### 1. Short title\nThis Act may be cited as the Senior Citizens Tax Elimination Act .\n#### 2. Repeal of inclusion in gross income of Social Security benefits\n##### (a) In general\nSection 86 of the Internal Revenue Code of 1986 (relating to social security benefits) is amended by adding at the end the following new subsection:\n(g) Termination This section shall not apply to any taxable year beginning after the date of the enactment of this subsection. .\n##### (b) Social Security trust funds held harmless\n**(1) In general**\nThere are hereby appropriated (out of any money in the Treasury not otherwise appropriated) for each fiscal year to each fund under the Social Security Act or the Railroad Retirement Act of 1974 an amount equal to the reduction in the transfers to such fund for such fiscal year by reason of section 86(g) of the Internal Revenue Code of 1986.\n**(2) No tax increases**\nIt is the sense of the Congress that tax increases will not be used to provide the revenue necessary to carry out paragraph (1).",
      "versionDate": "2025-02-06",
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
        "actionDate": "2025-02-06",
        "text": "Referred to the House Committee on Ways and Means."
      },
      "number": "1040",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Identical bill"
        }
      },
      "title": "Senior Citizens Tax Elimination Act",
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
        "updateDate": "2025-05-05T17:03:40Z"
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
      "date": "2025-02-06",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s458is.xml"
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
      "title": "Senior Citizens Tax Elimination Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-03-12T02:23:34Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Senior Citizens Tax Elimination Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-03-12T02:23:28Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to repeal the inclusion in gross income of Social Security benefits.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-03-12T02:18:49Z"
    }
  ]
}
```
