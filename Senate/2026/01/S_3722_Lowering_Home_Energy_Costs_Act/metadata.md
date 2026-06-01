# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3722?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3722
- Title: Lowering Home Energy Costs Act
- Congress: 119
- Bill type: S
- Bill number: 3722
- Origin chamber: Senate
- Introduced date: 2026-01-29
- Update date: 2026-02-23T13:52:28Z
- Update date including text: 2026-02-23T13:52:28Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-01-29: Introduced in Senate
- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-01-29: Introduced in Senate

## Actions

- 2026-01-29 - IntroReferral: Introduced in Senate
- 2026-01-29 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-29",
    "latestAction": {
      "actionDate": "2026-01-29",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3722",
    "number": "3722",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001113",
        "district": "",
        "firstName": "Catherine",
        "fullName": "Sen. Cortez Masto, Catherine [D-NV]",
        "lastName": "Cortez Masto",
        "party": "D",
        "state": "NV"
      }
    ],
    "title": "Lowering Home Energy Costs Act",
    "type": "S",
    "updateDate": "2026-02-23T13:52:28Z",
    "updateDateIncludingText": "2026-02-23T13:52:28Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-29",
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
      "actionDate": "2026-01-29",
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
          "date": "2026-01-29T16:27:00Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3722is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 3722\nIN THE SENATE OF THE UNITED STATES\nJanuary 29, 2026 Ms. Cortez Masto introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to restore and extend certain tax credits to incentivize energy efficiency.\n#### 1. Short title\nThis Act may be cited as the Lowering Home Energy Costs Act .\n#### 2. Extension of new energy efficient home credit\nSection 45L(h) of the Internal Revenue Code of 1986 is amended by striking June 30, 2026 and inserting December 31, 2032 .\n#### 3. Extension of residential clean energy credit\nSection 25D(h) of the Internal Revenue Code of 1986 is amended by striking December 31, 2025 and inserting December 31, 2032 .\n#### 4. Restoration of energy efficient home improvement credit\n##### (a) Repeal\nSection 70505 of Public Law 119\u201321 is repealed, and section 25C of the Internal Revenue Code of 1986 is restored as if such section 70505 had not been enacted.\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect as if included in the enactment of Public Law 119\u201321 .",
      "versionDate": "2026-01-29",
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
        "name": "Taxation",
        "updateDate": "2026-02-23T13:52:28Z"
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
      "date": "2026-01-29",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s3722is.xml"
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
      "title": "Lowering Home Energy Costs Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-02-19T04:08:24Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Lowering Home Energy Costs Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-02-19T04:08:23Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to restore and extend certain tax credits to incentivize energy efficiency.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-02-19T04:03:39Z"
    }
  ]
}
```
