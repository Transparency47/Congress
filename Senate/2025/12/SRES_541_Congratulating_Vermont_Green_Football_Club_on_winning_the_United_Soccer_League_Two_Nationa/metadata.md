# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/541?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/541
- Title: A resolution congratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.
- Congress: 119
- Bill type: SRES
- Bill number: 541
- Origin chamber: Senate
- Introduced date: 2025-12-11
- Update date: 2026-04-28T21:25:29Z
- Update date including text: 2026-04-28T21:25:29Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, relatedbills, subjects, text, titles

## Timeline

- 2025-12-11: Introduced in Senate
- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8676)
- Latest action: 2025-12-11: Introduced in Senate

## Actions

- 2025-12-11 - IntroReferral: Introduced in Senate
- 2025-12-11 - IntroReferral: Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8676)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-11",
    "latestAction": {
      "actionDate": "2025-12-11",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/541",
    "number": "541",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Sports and Recreation"
    },
    "sponsors": [
      {
        "bioguideId": "W000800",
        "district": "",
        "firstName": "Peter",
        "fullName": "Sen. Welch, Peter [D-VT]",
        "lastName": "Welch",
        "party": "D",
        "state": "VT"
      }
    ],
    "title": "A resolution congratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.",
    "type": "SRES",
    "updateDate": "2026-04-28T21:25:29Z",
    "updateDateIncludingText": "2026-04-28T21:25:29Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-11",
      "committees": {
        "item": {
          "name": "Commerce, Science, and Transportation Committee",
          "systemCode": "sscm00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Commerce, Science, and Transportation. (text: CR S8676)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-11",
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
          "date": "2025-12-11T18:01:10Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Commerce, Science, and Transportation Committee",
      "systemCode": "sscm00",
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
      "bioguideId": "S000033",
      "firstName": "Bernie",
      "fullName": "Sen. Sanders, Bernard [I-VT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sanders",
      "party": "I",
      "sponsorshipDate": "2025-12-11",
      "state": "VT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres541is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 541\nIN THE SENATE OF THE UNITED STATES\nDecember 11, 2025 Mr. Welch (for himself and Mr. Sanders ) submitted the following resolution; which was referred to the Committee on Commerce, Science, and Transportation\nRESOLUTION\nCongratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.\nThat the Senate\u2014\n**(1)**\ncongratulates the Vermont Green Football Club (referred to in this resolution as Vermont Green FC ) for an incredible season and for winning the United Soccer League Two National Championship;\n**(2)**\nrecognizes the achievements of all players, coaches, and staff who contributed to the team\u2019s success; and\n**(3)**\nrespectfully requests that the Secretary of the Senate transmit an enrolled copy of this resolution to\u2014\n**(A)**\nthe head coach, Chris Taylor;\n**(B)**\nthe sporting director of the Vermont Green FC; and\n**(C)**\nthe Vermont Green FC founders, Sam Glickman, Patrick Infurna, and Matthew Wolff.",
      "versionDate": "2025-12-11",
      "versionType": "IS"
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
        "actionDate": "2025-12-11",
        "text": "Referred to the House Committee on Oversight and Government Reform."
      },
      "number": "945",
      "relationshipDetails": {
        "item": {
          "identifiedBy": "CRS",
          "type": "Related bill"
        }
      },
      "title": "Congratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.",
      "type": "HRES"
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
        "name": "Sports and Recreation",
        "updateDate": "2025-12-15T18:39:03Z"
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
      "date": "2025-12-11",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres541is.xml"
        }
      ],
      "type": "IS"
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
      "title": "A resolution congratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-13T03:18:23Z"
    },
    {
      "title": "A resolution congratulating Vermont Green Football Club on winning the United Soccer League Two National Championship.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-12T11:56:22Z"
    }
  ]
}
```
