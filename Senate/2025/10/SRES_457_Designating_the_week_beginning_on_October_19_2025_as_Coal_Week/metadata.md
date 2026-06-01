# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/457?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/457
- Title: A resolution designating the week beginning on October 19, 2025, as "Coal Week".
- Congress: 119
- Bill type: SRES
- Bill number: 457
- Origin chamber: Senate
- Introduced date: 2025-10-20
- Update date: 2026-04-09T13:00:30Z
- Update date including text: 2026-04-09T13:00:30Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-10-20: Introduced in Senate
- 2025-10-20 - IntroReferral: Introduced in Senate
- 2025-10-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7168)
- Latest action: 2025-10-20: Introduced in Senate

## Actions

- 2025-10-20 - IntroReferral: Introduced in Senate
- 2025-10-20 - IntroReferral: Referred to the Committee on the Judiciary. (text: CR S7168)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-10-20",
    "latestAction": {
      "actionDate": "2025-10-20",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/457",
    "number": "457",
    "originChamber": "Senate",
    "policyArea": {
      "name": "Environmental Protection"
    },
    "sponsors": [
      {
        "bioguideId": "L000571",
        "district": "",
        "firstName": "Cynthia",
        "fullName": "Sen. Lummis, Cynthia M. [R-WY]",
        "lastName": "Lummis",
        "party": "R",
        "state": "WY"
      }
    ],
    "title": "A resolution designating the week beginning on October 19, 2025, as \"Coal Week\".",
    "type": "SRES",
    "updateDate": "2026-04-09T13:00:30Z",
    "updateDateIncludingText": "2026-04-09T13:00:30Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-10-20",
      "committees": {
        "item": {
          "name": "Judiciary Committee",
          "systemCode": "ssju00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on the Judiciary. (text: CR S7168)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-10-20",
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
          "date": "2025-10-20T20:14:22Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Judiciary Committee",
      "systemCode": "ssju00",
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
      "bioguideId": "H001061",
      "firstName": "John",
      "fullName": "Sen. Hoeven, John [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Hoeven",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "ND"
    },
    {
      "bioguideId": "L000577",
      "firstName": "Mike",
      "fullName": "Sen. Lee, Mike [R-UT]",
      "isOriginalCosponsor": "True",
      "lastName": "Lee",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "UT"
    },
    {
      "bioguideId": "C001047",
      "firstName": "Shelley",
      "fullName": "Sen. Capito, Shelley Moore [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Capito",
      "middleName": "Moore",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WV"
    },
    {
      "bioguideId": "B001243",
      "firstName": "Marsha",
      "fullName": "Sen. Blackburn, Marsha [R-TN]",
      "isOriginalCosponsor": "True",
      "lastName": "Blackburn",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "TN"
    },
    {
      "bioguideId": "S001198",
      "firstName": "Dan",
      "fullName": "Sen. Sullivan, Dan [R-AK]",
      "isOriginalCosponsor": "True",
      "lastName": "Sullivan",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "AK"
    },
    {
      "bioguideId": "J000312",
      "firstName": "James",
      "fullName": "Sen. Justice, James C. [R-WV]",
      "isOriginalCosponsor": "True",
      "lastName": "Justice",
      "middleName": "C.",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WV"
    },
    {
      "bioguideId": "M000355",
      "firstName": "Mitch",
      "fullName": "Sen. McConnell, Mitch [R-KY]",
      "isOriginalCosponsor": "True",
      "lastName": "McConnell",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "KY"
    },
    {
      "bioguideId": "S001232",
      "firstName": "Tim",
      "fullName": "Sen. Sheehy, Tim [R-MT]",
      "isOriginalCosponsor": "True",
      "lastName": "Sheehy",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "MT"
    },
    {
      "bioguideId": "B001261",
      "firstName": "John",
      "fullName": "Sen. Barrasso, John [R-WY]",
      "isOriginalCosponsor": "True",
      "lastName": "Barrasso",
      "party": "R",
      "sponsorshipDate": "2025-10-20",
      "state": "WY"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres457is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 457\nIN THE SENATE OF THE UNITED STATES\nOctober 20, 2025 Ms. Lummis (for herself, Mr. Hoeven , Mr. Lee , Mrs. Capito , Mrs. Blackburn , Mr. Sullivan , Mr. Justice , Mr. McConnell , Mr. Sheehy , and Mr. Barrasso ) submitted the following resolution; which was referred to the Committee on the Judiciary\nRESOLUTION\nDesignating the week beginning on October 19, 2025, as Coal Week .\nThat the Senate\u2014\n**(1)**\ndesignates the week beginning on October 19, 2025, as Coal Week ; and\n**(2)**\ncongratulates the ongoing progress in reducing coal emissions every year, while recognizing the role of coal in ensuring essential energy for the military readiness and economic stability of the United States.",
      "versionDate": "2025-10-20",
      "versionType": "IS"
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
        "name": "Environmental Protection",
        "updateDate": "2026-04-09T13:00:30Z"
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
      "date": "2025-10-20",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres457is.xml"
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
      "title": "A resolution designating the week beginning on October 19, 2025, as \"Coal Week\".",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-10-22T03:48:16Z"
    },
    {
      "title": "A resolution designating the week beginning on October 19, 2025, as \"Coal Week\".",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-10-21T10:56:13Z"
    }
  ]
}
```
