# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/1923?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/s/1923
- Title: CFPB Pay Fairness Act of 2025
- Congress: 119
- Bill type: S
- Bill number: 1923
- Origin chamber: Senate
- Introduced date: 2025-06-02
- Update date: 2025-06-18T13:36:05Z
- Update date including text: 2025-06-18T13:36:05Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2025-06-02: Introduced in Senate
- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2025-06-02: Introduced in Senate

## Actions

- 2025-06-02 - IntroReferral: Introduced in Senate
- 2025-06-02 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-06-02",
    "latestAction": {
      "actionDate": "2025-06-02",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/s/1923",
    "number": "1923",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Government Operations and Politics"
    },
    "sponsors": [
      {
        "bioguideId": "K000393",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Kennedy, John [R-LA]",
        "lastName": "Kennedy",
        "party": "R",
        "state": "LA"
      }
    ],
    "title": "CFPB Pay Fairness Act of 2025",
    "type": "S",
    "updateDate": "2025-06-18T13:36:05Z",
    "updateDateIncludingText": "2025-06-18T13:36:05Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-06-02",
      "committees": {
        "item": {
          "name": "Banking, Housing, and Urban Affairs Committee",
          "systemCode": "ssbk00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-06-02",
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
          "date": "2025-06-02T20:22:15Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Banking, Housing, and Urban Affairs Committee",
      "systemCode": "ssbk00",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1923is.xml",
      "text": "II\n119th CONGRESS\n1st Session\nS. 1923\nIN THE SENATE OF THE UNITED STATES\nJune 2, 2025 Mr. Kennedy introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo amend the Consumer Financial Protection Act of 2010 to set the rate of pay for employees of the Bureau of Consumer Financial Protection in accordance with the General Schedule.\n#### 1. Short title\nThis Act may be cited as the CFPB Pay Fairness Act of 2025 .\n#### 2. Rate of pay for employees of the Bureau of Consumer Financial Protection\n##### (a) In general\nSection 1013(a)(2) of the Consumer Financial Protection Act of 2010 ( 12 U.S.C. 5493(a)(2) ) is amended to read as follows:\n(2) Compensation The rates of basic pay for all employees of the Bureau shall be set and adjusted by the Director in accordance with the General Schedule set forth in section 5332 of title 5, United States Code. .\n##### (b) Effective date\nThe amendment made by subsection (a) shall take effect on the date that is 90 days after the date of enactment of this Act.",
      "versionDate": "2025-06-02",
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
        "name": "Government Operations and Politics",
        "updateDate": "2025-06-18T13:36:05Z"
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
      "date": "2025-06-02",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/s/BILLS-119s1923is.xml"
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
      "title": "CFPB Pay Fairness Act of 2025",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-06-05T07:53:18Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "CFPB Pay Fairness Act of 2025",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2025-06-05T07:53:17Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Consumer Financial Protection Act of 2010 to set the rate of pay for employees of the Bureau of Consumer Financial Protection in accordance with the General Schedule.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-06-05T07:48:33Z"
    }
  ]
}
```
