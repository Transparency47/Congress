# Metadata

- API URL: https://api.congress.gov/v3/bill/119/s/4601?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-bill/4601
- Title: Chinese CBDC Prohibition Act of 2026
- Congress: 119
- Bill type: S
- Bill number: 4601
- Origin chamber: Senate
- Introduced date: 2026-05-20
- Update date: 2026-05-30T04:53:26Z
- Update date including text: 2026-05-30T04:53:26Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, fullTexts, text, titles

## Timeline

- 2026-05-20: Introduced in Senate
- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.
- Latest action: 2026-05-20: Introduced in Senate

## Actions

- 2026-05-20 - IntroReferral: Introduced in Senate
- 2026-05-20 - IntroReferral: Read twice and referred to the Committee on Banking, Housing, and Urban Affairs.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-05-20",
    "latestAction": {
      "actionDate": "2026-05-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-bill/4601",
    "number": "4601",
    "originChamber": "Senate",
    "policyArea": {},
    "sponsors": [
      {
        "bioguideId": "S001217",
        "district": "",
        "firstName": "Rick",
        "fullName": "Sen. Scott, Rick [R-FL]",
        "lastName": "Scott",
        "party": "R",
        "state": "FL"
      }
    ],
    "title": "Chinese CBDC Prohibition Act of 2026",
    "type": "S",
    "updateDate": "2026-05-30T04:53:26Z",
    "updateDateIncludingText": "2026-05-30T04:53:26Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-05-20",
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
      "actionDate": "2026-05-20",
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
          "date": "2026-05-20T19:54:57Z",
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4601is.xml",
      "text": "II\n119th CONGRESS\n2d Session\nS. 4601\nIN THE SENATE OF THE UNITED STATES\nMay 20, 2026 Mr. Scott of Florida introduced the following bill; which was read twice and referred to the Committee on Banking, Housing, and Urban Affairs\nA BILL\nTo prohibit money services businesses from engaging in any transaction that involves a central bank digital currency issued by the People\u2019s Republic of China, and for other purposes.\n#### 1. Short title\nThis Act may be cited as the Chinese CBDC Prohibition Act of 2026 .\n#### 2. Money services businesses\n##### (a) In general\nSubchapter II of chapter 53 of title 31, United States Code, is amended by adding at the end the following:\n5337. Money services businesses (a) Definition In this section, the term money services business has the meaning given the term in section 1010.100 of title 31, Code of Federal Regulations. (b) Transactions involving digital currency of the People's Republic of China No money services business may engage in any transaction, directly or indirectly, that involves a central bank digital currency issued by the People\u2019s Republic of China. .\n##### (b) Technical and conforming amendment\nThe table of sections for subchapter II of chapter 53 of title 31, United States Code, is amended by adding at the end the following:\n5337. Money services businesses. .",
      "versionDate": "2026-05-20",
      "versionType": "Introduced in Senate"
    }
  ]
}
```

## API Data: text

```json
{
  "textVersions": [
    {
      "date": "2026-05-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/s/BILLS-119s4601is.xml"
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
      "title": "Chinese CBDC Prohibition Act of 2026",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-05-30T04:53:26Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "Chinese CBDC Prohibition Act of 2026",
      "titleType": "Short Title(s) as Introduced",
      "titleTypeCode": "101",
      "updateDate": "2026-05-30T04:53:25Z"
    },
    {
      "billTextVersionCode": "IS",
      "billTextVersionName": "Introduced in Senate",
      "title": "A bill to prohibit money services businesses from engaging in any transaction that involves a central bank digital currency issued by the People's Republic of China, and for other purposes.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-05-30T04:48:26Z"
    }
  ]
}
```
