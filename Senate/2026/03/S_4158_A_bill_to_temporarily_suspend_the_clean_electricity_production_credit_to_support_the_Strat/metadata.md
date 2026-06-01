# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4158?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4158
- Title: A bill to temporarily suspend the clean electricity production credit to support the Strategic Petroleum Reserve.
- Congress: 119
- Bill type: S
- Bill number: 4158
- Origin chamber: Senate
- Introduced date: 2026-03-20
- Update date: 2026-04-02T22:52:52Z
- Update date including text: 2026-04-02T22:52:52Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-20: Introduced in Senate
- 2026-03-20 - IntroReferral: Introduced in Senate
- 2026-03-20 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2026-03-20: Introduced in Senate

## Actions

- 2026-03-20 - IntroReferral: Introduced in Senate
- 2026-03-20 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-20",
    "latestAction": {
      "actionDate": "2026-03-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4158",
    "number": "4158",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "C001095",
        "district": "",
        "firstName": "Tom",
        "fullName": "Sen. Cotton, Tom [R-AR]",
        "lastName": "Cotton",
        "party": "R",
        "state": "AR"
      }
    ],
    "title": "A bill to temporarily suspend the clean electricity production credit to support the Strategic Petroleum Reserve.",
    "type": "S",
    "updateDate": "2026-04-02T22:52:52Z",
    "updateDateIncludingText": "2026-04-02T22:52:52Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-20",
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
      "actionDate": "2026-03-20",
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
          "date": "2026-03-20T17:04:36Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4158is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4158\nIN THE SENATE OF THE UNITED STATES\nMarch 20, 2026 Mr. Cotton introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo temporarily suspend the clean electricity production credit to support the Strategic Petroleum Reserve.\n#### 1. Temporary suspension of clean electricity production credit\n##### (a) In general\nSection 45Y of the Internal Revenue Code of 1986 is amended by adding at the end the following:\n(i) Suspension during fiscal years 2026 and 2027 This section shall not apply with respect to any electricity produced during the period beginning on October 1, 2025, and ending on September 30, 2027. .\n##### (b) Transfer to SPR petroleum account\nThe Secretary of the Treasury shall deposit into the SPR Petroleum Account established under section 167(a) of the Energy Policy and Conservation Act ( 42 U.S.C. 6247(a) ) amounts equal to the increase in revenues to the Treasury by reason of the amendment made by subsection (a).",
      "versionDate": "2026-03-20",
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
        "updateDate": "2026-04-02T22:52:51Z"
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
      "date": "2026-03-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4158is.xml"
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
      "title": "A bill to temporarily suspend the clean electricity production credit to support the Strategic Petroleum Reserve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-26T05:18:35Z"
    },
    {
      "title": "A bill to temporarily suspend the clean electricity production credit to support the Strategic Petroleum Reserve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-21T10:56:20Z"
    }
  ]
}
```
