# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/582?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/582
- Title: A resolution expressing the sense of the Senate in support of Operation Absolute Resolve.
- Congress: 119
- Bill type: SRES
- Bill number: 582
- Origin chamber: Senate
- Introduced date: 2026-01-13
- Update date: 2026-01-16T18:53:57Z
- Update date including text: 2026-01-16T18:53:57Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2026-01-13: Introduced in Senate
- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S163-164)
- Latest action: 2026-01-13: Introduced in Senate

## Actions

- 2026-01-13 - IntroReferral: Introduced in Senate
- 2026-01-13 - IntroReferral: Referred to the Committee on Foreign Relations. (text: CR S163-164)

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2026-01-13",
    "latestAction": {
      "actionDate": "2026-01-13",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/582",
    "number": "582",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "C001056",
        "district": "",
        "firstName": "John",
        "fullName": "Sen. Cornyn, John [R-TX]",
        "lastName": "Cornyn",
        "party": "R",
        "state": "TX"
      }
    ],
    "title": "A resolution expressing the sense of the Senate in support of Operation Absolute Resolve.",
    "type": "SRES",
    "updateDate": "2026-01-16T18:53:57Z",
    "updateDateIncludingText": "2026-01-16T18:53:57Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2026-01-13",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations. (text: CR S163-164)",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2026-01-13",
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
          "date": "2026-01-13T21:36:13Z",
          "name": "Referred To"
        }
      },
      "chamber": "Senate",
      "name": "Foreign Relations Committee",
      "systemCode": "ssfr00",
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
      "bioguideId": "C001098",
      "firstName": "Ted",
      "fullName": "Sen. Cruz, Ted [R-TX]",
      "isOriginalCosponsor": "True",
      "lastName": "Cruz",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "TX"
    },
    {
      "bioguideId": "C001096",
      "firstName": "Kevin",
      "fullName": "Sen. Cramer, Kevin [R-ND]",
      "isOriginalCosponsor": "True",
      "lastName": "Cramer",
      "party": "R",
      "sponsorshipDate": "2026-01-13",
      "state": "ND"
    },
    {
      "bioguideId": "S001217",
      "firstName": "Rick",
      "fullName": "Sen. Scott, Rick [R-FL]",
      "isOriginalCosponsor": "False",
      "lastName": "Scott",
      "party": "R",
      "sponsorshipDate": "2026-01-14",
      "state": "FL"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres582is.xml",
      "text": "III\n119th CONGRESS\n2d Session\nS. RES. 582\nIN THE SENATE OF THE UNITED STATES\nJanuary 13, 2026 Mr. Cornyn (for himself, Mr. Cruz , and Mr. Cramer ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nExpressing the sense of the Senate in support of Operation Absolute Resolve.\nThat the Senate\u2014\n**(1)**\nsupports President Trump\u2019s decisive military and law enforcement effort under Operation Absolute Resolve to arrest Nicol\u00e1s Maduro and bring him to justice;\n**(2)**\ncommends the Trump Administration for taking resolute action and praises the bravery and gallantry of United States servicemembers and law enforcement officers who participated in Operation Absolute Resolve; and\n**(3)**\nsupports President Trump's efforts to assist the Venezuelan people in their fight for freedom.",
      "versionDate": "2026-01-13",
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
        "name": "International Affairs",
        "updateDate": "2026-01-16T18:53:57Z"
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
      "date": "2026-01-13",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/2/sres/BILLS-119sres582is.xml"
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
      "title": "A resolution expressing the sense of the Senate in support of Operation Absolute Resolve.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2026-01-16T05:48:23Z"
    },
    {
      "title": "A resolution expressing the sense of the Senate in support of Operation Absolute Resolve.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2026-01-14T11:56:17Z"
    }
  ]
}
```
