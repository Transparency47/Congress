# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1927?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1927
- Title: HERITAGE Act
- Congress: 119
- Bill type: S
- Bill number: 1927
- Origin chamber: Senate
- Introduced date: 2025-06-03
- Update date: 2025-07-01T11:06:18Z
- Update date including text: 2025-07-01T11:06:18Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-03: Introduced in Senate
- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-03: Introduced in Senate

## Actions

- 2025-06-03 - IntroReferral: Introduced in Senate
- 2025-06-03 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-03",
    "latestAction": {
      "actionDate": "2025-06-03",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1927",
    "number": "1927",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
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
    "title": "HERITAGE Act",
    "type": "S",
    "updateDate": "2025-07-01T11:06:18Z",
    "updateDateIncludingText": "2025-07-01T11:06:18Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-03",
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
      "actionDate": "2025-06-03",
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
          "date": "2025-06-03T14:31:05Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1927is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1927\nIN THE SENATE OF THE UNITED STATES\nJune 3, 2025 Mrs. Hyde-Smith introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to increase the limitation with respect to the aggregate reduction in fair market value of farmland for purposes of application of the estate tax.\n#### 1. Short title\nThis Act may be cited as the Helping Ensure Rural Inheritance Transfers Are Generationally Enduring Act or the HERITAGE Act .\n#### 2. Increase in limitation on aggregate reduction in fair market value of farmland\n##### (a) In general\nSection 2032A(a)(2) of the Internal Revenue Code of 1986 is amended by striking shall not exceed $750,000 and inserting:\nshall not exceed\u2014 (A) in the case of qualified real property which was being used for a qualified use described in subparagraph (A) of subsection (b)(2), $15,000,000, and (B) in the case of qualified real property which was being used for a qualified use described in subparagraph (B) of such subsection, $750,000. .\n##### (b) Conforming amendment\nSection 2032A(a)(3) of the Internal Revenue Code of 1986 is amended\u2014\n**(1)**\nin the matter preceding subparagraph (A), by striking the $750,000 amount and inserting each dollar amount , and\n**(2)**\nin subparagraph (A), by striking $750,000 and inserting such dollar amount .\n##### (c) Effective date\nThe amendments made by this section shall apply to the estates of decedents dying after the date of the enactment of this Act.",
      "versionDate": "2025-06-03",
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
        "updateDate": "2025-06-25T20:18:43Z"
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
      "date": "2025-06-03",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1927is.xml"
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
      "title": "HERITAGE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "HERITAGE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Helping Ensure Rural Inheritance Transfers Are Generationally Enduring Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to increase the limitation with respect to the aggregate reduction in fair market value of farmland for purposes of application of the estate tax.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:32Z"
    }
  ]
}
```
