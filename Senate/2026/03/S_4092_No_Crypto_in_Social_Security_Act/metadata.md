# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4092?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4092
- Title: No Crypto in Social Security Act
- Congress: 119
- Bill type: S
- Bill number: 4092
- Origin chamber: Senate
- Introduced date: 2026-03-12
- Update date: 2026-04-02T18:55:42Z
- Update date including text: 2026-04-02T18:55:42Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, subjects, text, titles

## Timeline

- 2026-03-12: Introduced in Senate
- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1049)
- Latest action: 2026-03-12: Introduced in Senate

## Actions

- 2026-03-12 - IntroReferral: Introduced in Senate
- 2026-03-12 - IntroReferral: Read twice and referred to the Committee on Finance. (text: CR S1049)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-03-12",
    "latestAction": {
      "actionDate": "2026-03-12",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4092",
    "number": "4092",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Social Welfare"
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
    "title": "No Crypto in Social Security Act",
    "type": "S",
    "updateDate": "2026-04-02T18:55:42Z",
    "updateDateIncludingText": "2026-04-02T18:55:42Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-03-12",
      "committees": {
        "item": {
          "name": "Finance Committee",
          "systemCode": "ssfi00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Read twice and referred to the Committee on Finance. (text: CR S1049)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-03-12",
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
          "date": "2026-03-12T18:39:57Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4092is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4092\nIN THE SENATE OF THE UNITED STATES\nMarch 12, 2026 Mr. Durbin introduced the following bill; which was read twice and referred to the Committee on Finance\nA BILL\nTo amend the Social Security Act to prohibit the Social Security Trust Funds from investing in cryptocurrency.\n#### 1. Short title\nThis Act may be cited as the No Crypto in Social Security Act .\n#### 2. Prohibit Social Security Trust Funds from investing in cryptocurrency\nSection 201 of the Social Security Act ( 42 U.S.C. 401 ) is amended\u2014\n**(1)**\nin subsection (d), by inserting after the second sentence the following: Such investment may not be made in any digital asset or any crypto-related investment. ; and\n**(2)**\nby adding at the end the following new subsection:\n(o) For purposes of subsection (d)\u2014 (1) the term digital asset has the same meaning given such term in section 2 of the GENIUS Act ( 12 U.S.C. 5901 ); and (2) the term crypto-related investment means\u2014 (A) any investment fund under the Investment Company Act of 1940 ( 15 U.S.C. 80a\u20131 et seq. ) related to futures on digital assets (as so defined) or on digital asset indices; (B) any stock or bond of a public company that\u2014 (i) substantially derives its value from holdings of digital assets; or (ii) primarily derives revenue from providing products or services (including issuance, trading, management, distribution, custody, settlement, or similar services) related to digital assets; or (C) any other asset or investment whose value is tied to, or derived from, digital assets. .",
      "versionDate": "2026-03-12",
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
        "name": "Social Welfare",
        "updateDate": "2026-04-02T18:55:42Z"
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
      "date": "2026-03-12",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4092is.xml"
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
      "title": "No Crypto in Social Security Act",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-03-25T03:53:21Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "No Crypto in Social Security Act",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-03-25T03:53:20Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to amend the Social Security Act to prohibit the Social Security Trust Funds from investing in cryptocurrency.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-03-25T03:48:30Z"
    }
  ]
}
```
