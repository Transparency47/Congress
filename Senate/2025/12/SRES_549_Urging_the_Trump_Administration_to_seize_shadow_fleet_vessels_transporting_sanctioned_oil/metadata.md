# Metadata

- API URL: https://api.congress.gov/v3/bill/119/sres/549?format=json
- Congress.gov URL: https://www.congress.gov/bill/119th-congress/senate-resolution/549
- Title: A resolution urging the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.
- Congress: 119
- Bill type: SRES
- Bill number: 549
- Origin chamber: Senate
- Introduced date: 2025-12-17
- Update date: 2026-01-06T20:03:24Z
- Update date including text: 2026-01-06T20:03:24Z
- Date accessed: 2026-06-01T04:21:25.748028+00:00
- Embedded API data: bill, actions, committees, cosponsors, fullTexts, subjects, text, titles

## Timeline

- 2025-12-17: Introduced in Senate
- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.
- Latest action: 2025-12-17: Introduced in Senate

## Actions

- 2025-12-17 - IntroReferral: Introduced in Senate
- 2025-12-17 - IntroReferral: Referred to the Committee on Foreign Relations.

## Voters

- Voters: No recorded votes found in bill actions.

## API Data: bill

```json
{
  "bill": {
    "congress": 119,
    "introducedDate": "2025-12-17",
    "latestAction": {
      "actionDate": "2025-12-17",
      "text": "Introduced in Senate"
    },
    "legislationUrl": "https://www.congress.gov/bill/119th-congress/senate-resolution/549",
    "number": "549",
    "originChamber": "Senate",
    "policyArea": {
      "name": "International Affairs"
    },
    "sponsors": [
      {
        "bioguideId": "G000359",
        "district": "",
        "firstName": "Lindsey",
        "fullName": "Sen. Graham, Lindsey [R-SC]",
        "lastName": "Graham",
        "party": "R",
        "state": "SC"
      }
    ],
    "title": "A resolution urging the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.",
    "type": "SRES",
    "updateDate": "2026-01-06T20:03:24Z",
    "updateDateIncludingText": "2026-01-06T20:03:24Z"
  }
}
```

## API Data: actions

```json
{
  "actions": [
    {
      "actionDate": "2025-12-17",
      "committees": {
        "item": {
          "name": "Foreign Relations Committee",
          "systemCode": "ssfr00"
        }
      },
      "sourceSystem": {
        "name": "Senate"
      },
      "text": "Referred to the Committee on Foreign Relations.",
      "type": "IntroReferral"
    },
    {
      "actionCode": "10000",
      "actionDate": "2025-12-17",
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
          "date": "2025-12-17T22:08:32Z",
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
      "bioguideId": "B001277",
      "firstName": "Richard",
      "fullName": "Sen. Blumenthal, Richard [D-CT]",
      "isOriginalCosponsor": "True",
      "lastName": "Blumenthal",
      "party": "D",
      "sponsorshipDate": "2025-12-17",
      "state": "CT"
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
      "sourceUrl": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres549is.xml",
      "text": "III\n119th CONGRESS\n1st Session\nS. RES. 549\nIN THE SENATE OF THE UNITED STATES\nDecember 17, 2025 Mr. Graham (for himself and Mr. Blumenthal ) submitted the following resolution; which was referred to the Committee on Foreign Relations\nRESOLUTION\nUrging the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.\nThat the Senate\u2014\n**(1)**\ncondemns the use of shadow fleet vessels to transport sanctioned oil from the Russian Federation and views the transport of such oil as conduct that undermines United States national security interests and sanctions regimes;\n**(2)**\nurges the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation;\n**(3)**\nrecognizes that seizing shadow fleet vessels engaged in such transport is a lawful and appropriate measure to take against the Russian Federation\u2019s evasion of sanctions and illicit financing of its war in Ukraine; and\n**(4)**\ncalls on allies and partners to also seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.",
      "versionDate": "2025-12-17",
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
        "updateDate": "2026-01-06T20:03:24Z"
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
      "date": "2025-12-17",
      "formats": [
        {
          "type": "Formatted XML",
          "url": "https://www.govinfo.gov/bulkdata/BILLS/119/1/sres/BILLS-119sres549is.xml"
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
      "title": "A resolution urging the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.",
      "titleType": "Official Title as Introduced",
      "titleTypeCode": "6",
      "updateDate": "2025-12-20T06:18:27Z"
    },
    {
      "title": "A resolution urging the Trump Administration to seize shadow fleet vessels transporting sanctioned oil from the Russian Federation.",
      "titleType": "Display Title",
      "titleTypeCode": "45",
      "updateDate": "2025-12-18T11:56:16Z"
    }
  ]
}
```
