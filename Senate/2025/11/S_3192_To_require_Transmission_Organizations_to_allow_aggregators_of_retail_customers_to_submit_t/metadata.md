# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/3192?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/3192
- Title: REDUCE Act
- Congress: 119
- Bill type: S
- Bill number: 3192
- Origin chamber: Senate
- Introduced date: 2025-11-18
- Update date: 2026-04-27T14:06:14Z
- Update date including text: 2026-04-27T14:06:14Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-11-18: Introduced in Senate
- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S8207)
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.
- Latest action: 2025-11-18: Introduced in Senate

## Actions

- 2025-11-18 - IntroReferral: Introduced in Senate
- 2025-11-18 - IntroReferral: Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S8207)
- 2026-04-15 - Committee: Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-11-18",
    "latestAction": {
      "actionDate": "2025-11-18",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/3192",
    "number": "3192",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Energy"
    },
    "sponsors": [
      {
        "bioguideId": "D000563",
        "district": "",
        "firstName": "Richard",
        "fullName": "Sen. Durbin, Richard J. [D-IL]",
        "lastName": "Durbin",
        "party": "D",
        "state": "IL"
      }
    ],
    "title": "REDUCE Act",
    "type": "S",
    "updateDate": "2026-04-27T14:06:14Z",
    "updateDateIncludingText": "2026-04-27T14:06:14Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-04-15",
      "committees": {
        "item": {
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Committee on Energy and Natural Resources Subcommittee on Energy. Hearings held.",
      "type": "Committee"
    },
    {
      "actionDate": "2025-11-18",
      "committees": {
        "item": {
          "name": "Energy and Natural Resources Committee",
          "systemCode": "sseg00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Energy and Natural Resources. (text: CR S8207)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-11-18",
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
          "date": "2025-11-18T22:52:27Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Energy and Natural Resources Committee",
      "subcommittees": {
        "item": {
          "activities": {
            "item": {
              "date": "2026-04-15T19:37:26Z",
              "name": "Hearings By (subcommittee)"
            }
          },
          "name": "Energy Subcommittee",
          "systemCode": "sseg01"
        }
      },
      "systemCode": "sseg00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3192is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 3192\nIN THE SENATE OF THE UNITED STATES\nNovember 18, 2025 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Energy and Natural Resources\nA BILL\nTo require Transmission Organizations to allow aggregators of retail customers to submit to organized wholesale electric markets bids that aggregate demand flexibility of customers of certain utilities, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Responsive Energy Demand Unlocks Clean Energy Act or the REDUCE Act .\n#### 2. Aggregator bidding into organized power markets\n##### (a) In general\nNotwithstanding any prohibition established by State law or a State commission (as defined in section 3 of the Federal Power Act ( 16 U.S.C. 796 )) with respect to who may bid into an organized wholesale electric market, each Transmission Organization shall, consistent with any applicable market rules that do not establish such a prohibition, allow aggregators of retail customers to submit bids that aggregate demand flexibility of customers of utilities that distributed more than 4,000,000 megawatt-hours in the previous fiscal year.\n##### (b) Rulemaking\nNot later than 1 year after the date of enactment of this Act, the Federal Energy Regulatory Commission shall issue a rule to carry out the requirements of subsection (a).",
      "versionDate": "2025-11-18",
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
      "legislativeSubjects": {
        "item": [
          {
            "name": "Commodities markets",
            "updateDate": "2026-04-27T14:05:03Z"
          },
          {
            "name": "Energy storage, supplies, demand",
            "updateDate": "2026-04-27T14:02:47Z"
          },
          {
            "name": "Public contracts and procurement",
            "updateDate": "2026-04-27T14:04:41Z"
          },
          {
            "name": "Public utilities and utility rates",
            "updateDate": "2026-04-27T14:06:14Z"
          },
          {
            "name": "Retail and wholesale trades",
            "updateDate": "2026-04-27T14:05:22Z"
          }
        ]
      },
      "policyArea": {
        "name": "Energy",
        "updateDate": "2025-12-04T16:00:24Z"
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
      "date": "2025-11-18",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s3192is.xml"
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
      "title": "REDUCE Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-04-16T11:03:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "REDUCE Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T05:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Responsive Energy Demand Unlocks Clean Energy Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-12-02T05:23:27Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to require Transmission Organizations to allow aggregators of retail customers to submit to organized wholesale electric markets bids that aggregate demand flexibility of customers of certain utilities, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-02T05:18:21Z"
    }
  ]
}
```
