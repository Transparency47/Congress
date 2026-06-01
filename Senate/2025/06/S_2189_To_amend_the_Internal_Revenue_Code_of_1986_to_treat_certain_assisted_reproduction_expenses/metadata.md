# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/2189?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/2189
- Title: Equal Access to Reproductive Care Act
- Congress: 119
- Bill type: S
- Bill number: 2189
- Origin chamber: Senate
- Introduced date: 2025-06-26
- Update date: 2025-07-17T19:09:41Z
- Update date including text: 2025-07-17T19:09:41Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-26: Introduced in Senate
- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Finance.
- Latest action: 2025-06-26: Introduced in Senate

## Actions

- 2025-06-26 - IntroReferral: Introduced in Senate
- 2025-06-26 - IntroReferral: Read twice and referred to the Committee on Finance.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-26",
    "latestAction": {
      "actionDate": "2025-06-26",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/2189",
    "number": "2189",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Taxation"
    },
    "sponsors": [
      {
        "bioguideId": "S001150",
        "district": "",
        "firstName": "Adam",
        "fullName": "Sen. Schiff, Adam B. [D-CA]",
        "lastName": "Schiff",
        "party": "D",
        "state": "CA"
      }
    ],
    "title": "Equal Access to Reproductive Care Act",
    "type": "S",
    "updateDate": "2025-07-17T19:09:41Z",
    "updateDateIncludingText": "2025-07-17T19:09:41Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-26",
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
      "actionDate": "2025-06-26",
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
          "date": "2025-06-26T20:24:27Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2189is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 2189\nIN THE SENATE OF THE UNITED STATES\nJune 26 (legislative day, June 24), 2025 Mr. Schiff introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Internal Revenue Code of 1986 to treat certain assisted reproduction expenses as medical expenses of the taxpayer.\n#### 1. Short title\nThis Act may be cited as the Equal Access to Reproductive Care Act .\n#### 2. Treatment of certain assisted reproduction expenses as medical expenses of the taxpayer\n##### (a) In general\nSection 213(d) of the Internal Revenue Code of 1986 is amended by adding at the end the following new paragraph:\n(12) Assisted reproduction expenses (A) In general The term medical care includes assisted reproduction. (B) Assisted reproduction defined The term assisted reproduction means any methods, treatments, procedures, and services for the purpose of effectuating a pregnancy and carrying it to term, including gamete and embryo donation, intrauterine insemination, in vitro fertilization, intracervical insemination, traditional reproductive surrogacy, and gestational reproductive surrogacy. (C) Coverage of surrogacy, etc Assisted reproduction shall be treated as medical care of the taxpayer or the taxpayer\u2019s spouse or dependent to the extent that the taxpayer or the taxpayer\u2019s spouse or dependent, respectively, intends to take legal custody or responsibility for any children born as a result of such assisted reproduction. (D) Coordination with certain other rules related to transportation, insurance, etc Assisted reproduction shall be treated as medical care referred to in paragraph (1)(A). .\n##### (b) Effective date\nThe amendment made by this section shall apply to taxable years beginning after the date of the enactment of this Act.",
      "versionDate": "2025-06-26",
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
        "updateDate": "2025-07-17T19:09:41Z"
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
      "date": "2025-06-26",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s2189is.xml"
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
      "title": "Equal Access to Reproductive Care Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Equal Access to Reproductive Care Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-07-16T03:38:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Internal Revenue Code of 1986 to treat certain assisted reproduction expenses as medical expenses of the taxpayer.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-07-16T03:33:23Z"
    }
  ]
}
```
